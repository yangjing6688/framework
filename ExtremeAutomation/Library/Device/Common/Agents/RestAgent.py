import time
import logging
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.Common.Agents.LoginManagementAgent import LoginManagementAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject

# Suppress InsecureRequestWarning. Stops the warning from being shown in the console
# useful when self-signed certificates are being used.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RestAgent(LoginManagementAgent):
    def __init__(self, device):
        super(RestAgent, self).__init__(device)
        self.device = device
        self.verify_cert = StringUtils.string_to_boolean(device.agent_kwargs.get("verify_cert", True))
        self.auth_mode = device.agent_kwargs.get("auth_mode", RestAgentConstants.AUTH_NONE)
        self.oauth_token = device.agent_kwargs.get("oauth", None)
        self.headers = device.agent_kwargs.get("headers", None)
        self.type = self.constants.TYPE_REST
        self.retries = 3      # Number of times if unable to connect.
        self.retry_delay = 1  # Time in seconds to wait between each retry.
        self.full_uri = None

        # Disable excess logging from requests and urllib3 modules.
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def send_command(self, command):
        """
        Command - A string that should contain the type of query to make and uri to send it to. It should be space
                  delimited.

                  For example:
                  get /debug/v1/generalinformation

                  The leading "/" is optional.
        """
        if isinstance(command, dict):
            command = command['command']
        query_type, command = command.split()
        cmd_obj = RestCommandObject()
        cmd_obj.request_type = query_type
        cmd_obj.uri = command
        return self.send_command_object(cmd_obj)

    def send_command_object(self, cmd_obj, **kwargs):
        """
        cmd_obj - Accepts a GenericRestApiCommandObject. The object must contain the request type and uri, optionally
                  it can contain the JSON data to send with the request.
        """
        parsed_kwargs = self.parse_kwargs(**kwargs)
        cmd_obj.full_uri = self.get_full_uri(cmd_obj)
        response = self.send_request(cmd_obj, parsed_kwargs["retries"])

        if response is not None:
            response_text = StringUtils.format_json_output(response.text)

            if parsed_kwargs["log"]:
                self.__log_response(response_text, cmd_obj)

            cmd_obj.return_text = response_text
            cmd_obj.return_status_code = str(response.status_code)
            cmd_obj.response = response

            try:
                cmd_obj.return_status_text = str(StringUtils.format_json_output(response.text)["Result"])
            except (KeyError, TypeError):
                cmd_obj.return_status_text = response.reason

            if self.device.error_checker is not None:
                errs = self.device.error_checker.check_for_errors_json(cmd_obj.return_text)
                if errs is not None:
                    if len(errs) > 0:
                        cmd_obj.set_error_state(errs)

        else:
            cmd_obj.set_error_state("Unable to connect to " + cmd_obj.full_uri)

        return cmd_obj

    def send_request(self, cmd_obj, retry_count):
        """
        Function Args:
            [cmd_obj] - A command object containing the information needed to create a rest request.
            [retry_count] - The number of times the request should be tried before stopping.

        This function creates a rest request based on the request_type value in the passed command
        object. If the passed request_type is not valid an exception will be raised. If the request
        is successful the response object is returned.
        """
        retry = 0
        response = None
        request_args = self.get_request_args(cmd_obj)

        while retry < retry_count and response is None:
            try:
                cmd_obj.start_time = time.time()
                response = requests.request(**request_args)
                cmd_obj.end_time = time.time()
            except requests.exceptions.ConnectionError:
                retry += 1
                time.sleep(self.retry_delay)
        return response

    def get_request_args(self, cmd_obj):
        """
        Function Args:
            [cmd_obj] - Typically this is a RestCommandObject instance. The arguments passed
                        to the request will be based on the information in the passed object.

        This function creates a dictionary of arguments to pass to the request.<type> function.
        The following attributes can be set depending on the command object's contents.

            verify  - A boolean indicating whether or not the server's cert should be verified.
            method  - Which type of request should be made. Supported values are get, post,
                      head, patch, put, delete, options.
            url     - The full URL that the request should be sent to.
            json    - The data to include in the request.
            headers - Additional headers that should be included in the request. This should
                      be passed as a dictionary.
            auth    - Which auth mode should be used by the request. Supported modes can
                      be found in RestAgentConstants.
        """
        request_args = {"verify": self.verify_cert,
                        "method": self.get_request_type(cmd_obj),
                        "url": cmd_obj.full_uri}

        if cmd_obj.data is not None:
            request_args["json"] = StringUtils.format_json_output(cmd_obj.data)
        if self.headers is not None:
            request_args["headers"] = StringUtils.format_json_output(self.headers)
            if cmd_obj.headers is not None:
                request_args["headers"].update(cmd_obj.headers)
        elif cmd_obj.headers is not None:
            request_args["headers"] = cmd_obj.headers

        if self.auth_mode in [RestAgentConstants.AUTH_BASIC,
                              RestAgentConstants.AUTH_BASIC_SSL]:
            request_args["auth"] = HTTPBasicAuth(self.device.username, self.device.password)
        elif self.auth_mode == RestAgentConstants.AUTH_OAUTH:
            if self.oauth_token is not None:
                if "headers" in request_args:
                    request_args["headers"]["Authorization"] = "Bearer " + self.oauth_token
                else:
                    request_args["headers"] = {"Authorization": "Bearer " + self.oauth_token}
            else:
                raise ValueError("No oauth token provided.")

        return request_args

    def parse_kwargs(self, **kwargs):
        """
        This function parses the kwargs passed into the rest agent.
        It returns a dictionary with the parsed values. If any other
        kwargs are needed by the rest agent they should be added here.
        """
        return {"log": kwargs.get("log", True),
                "retries": kwargs.get("max_attempts", self.retries)}

    def get_full_uri(self, cmd_obj):
        """
        URI - The string URI that should be used ot create the full URI string.

        For example uri="/debug/v1/generalinformation" would return...

        http://<hostname>:<port>/<uri>

        or

        https://<hostname>:<port>/<uri>

        if secured.
        """
        http_mode = "http://"
        if self.auth_mode in [RestAgentConstants.AUTH_SSL,
                              RestAgentConstants.AUTH_OAUTH,
                              RestAgentConstants.AUTH_BASIC_SSL]:
            http_mode = "https://"
        if cmd_obj.uri.startswith("/"):
            cmd_obj.uri = cmd_obj.uri[1::]
        return "{0}{1}:{2}/{3}".format(http_mode, self.device.hostname, str(self.device.port), cmd_obj.uri)

    def __log_response(self, response_text, cmd_obj):
        log_message = ["Request Type: " + cmd_obj.request_type.upper(),
                       "URI:          " + cmd_obj.uri,
                       "Data:         " + str(cmd_obj.data) if cmd_obj.data is not None else ""]

        self.logger.log_trace("\n".join(log_message) + "\n")
        self.logger.log_trace("Response: " + StringUtils.pretty_print_dict(response_text))

    @staticmethod
    def get_request_type(cmd_obj):
        """
        Function Args:
            [cmd_obj] - An RestCommandObject instance. This is needed to get the request type.

        Checks the request type in the passed command object. If it is a list of supported
        request types the string is returned lower cased. Otherwise an exception is raised
        informing the user the request type specified is not valid.
        """
        if cmd_obj.request_type.lower() in ["get", "post", "head", "patch", "put", "delete", "options"]:
            return cmd_obj.request_type.lower()
        raise AttributeError("Query type " + cmd_obj.request_type.lower() + " is not a valid query type.")

    @staticmethod
    def check_response_code(response):
        """
        This function checks the returned response code. If the response code results in a HTTPError return
        False, otherwise return True.
        """
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return False
        return True

    def login(self):
        """
        Login function, not needed for Rest, returns True.
        """
        return True

    def connect(self):
        """
        Connect function, not needed for Rest, sets connected and logged_in to True.
        """
        self.connected = True
        self.logged_in = True

    def disconnect(self):
        """
        Disconnect function, not needed for Rest, sets connected and logged_in to False.
        """
        self.connected = False
        self.logged_in = False

    def logout(self):
        """
        Logout function, not needed for Rest, does nothing.
        """
        pass


class RestAgentConstants(object):
    REST_PORT = 80
    AUTH_NONE = "none"
    AUTH_BASIC = "basic"
    AUTH_BASIC_SSL = "basic_ssl"
    AUTH_SSL = "ssl"
    AUTH_OAUTH = "oauth"
