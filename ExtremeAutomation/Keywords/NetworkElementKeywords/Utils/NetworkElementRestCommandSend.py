import time
import json
from ExtremeAutomation.Library.Utils.JsonUtils import JsonUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass


class NetworkElementRestCommandSend(NetworkElementKeywordBaseClass):
    # REST Constants
    _get_request = "get"
    _put_request = "put"
    _post_request = "post"
    _patch_request = "patch"
    _delete_request = "delete"

    _all_request_types = [_get_request,
                          _put_request,
                          _post_request,
                          _patch_request,
                          _delete_request
                          ]

    def __init__(self):
        super(NetworkElementRestCommandSend, self).__init__()
        self.rest_cmd_obj = RestCommandObject()

    def send_get_request(self, device_name, uri, data=None, expected_return_values=None, response_code=None,
                         rest_server_ip=None, rest_server_port=None, exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device name the keyword should be run against.
        [uri] - The location of the resource being requested.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.

        Sends a GET request with optional data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, self._get_request, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            kw_result = self._determine_result(dev, rest_cmd_obj, **kwargs)
        else:
            kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                               "REST command passed.", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_get_request_and_return_json_dictionary(self, device_name, uri, data=None, expected_return_values=None,
                                                    response_code=None, rest_server_ip=None, rest_server_port=None,
                                                    exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device name the keyword should be run against.
        [uri] - The location of the resource being requested.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.

        Sends a GET request with optional data and returns the JSON object in the form of a python dictionary.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, self._get_request, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            kw_result = self._determine_result(dev, rest_cmd_obj, **kwargs)
        else:
            kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                               "REST command passed.", fail_string, **kwargs)

        self._keyword_cleanup([kw_result])

        return rest_cmd_obj.return_text

    def send_put_request(self, device_name, uri, data=None, expected_return_values=None, response_code=None,
                         rest_server_ip=None, rest_server_port=None, exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device name the keyword should be run against.
        [uri] - The location of the resource being requested.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.

        Sends a PUT request with optional data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, self._put_request, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            kw_result = self._determine_result(dev, rest_cmd_obj, **kwargs)
        else:
            kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                               "REST command passed.", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_post_request(self, device_name, uri, data=None, expected_return_values=None, response_code=None,
                          rest_server_ip=None, rest_server_port=None, exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device name the keyword should be run against.
        [uri] - The location of the resource being requested.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.

        Sends a POST request with optional data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, self._post_request, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            kw_result = self._determine_result(dev, rest_cmd_obj, **kwargs)
        else:
            kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                               "REST command passed.", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_patch_request(self, device_name, uri, data=None, expected_return_values=None, response_code=None,
                           rest_server_ip=None, rest_server_port=None, exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device name the keyword should be run against.
        [uri] - The location of the resource being requested.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.

        Sends a PATCH request with optional data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, self._patch_request, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            kw_result = self._determine_result(dev, rest_cmd_obj, **kwargs)
        else:
            kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                               "REST command passed.", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_delete_request(self, device_name, uri, data=None, expected_return_values=None, response_code=None,
                            rest_server_ip=None, rest_server_port=None, exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device name the keyword should be run against.
        [uri] - The location of the resource being requested.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.

        Sends a DELETE request with optional data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, self._delete_request, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            kw_result = self._determine_result(dev, rest_cmd_obj, **kwargs)
        else:
            kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                               "REST command passed.", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_get_request_and_wait_for_expected_result(self, device_name, uri, expected_return_values, data=None,
                                                      response_code=None, rest_server_ip=None, rest_server_port=None,
                                                      max_wait="60", interval="5", exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device name the keyword should be run against.
        [uri] - The location if the resource being requested.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.
        [max_wait] - The longest the keyword will wait before determining the keyword failed.
        [interval] - How often the keyword should execute.

        Sends a GET request and waits until the expected return values are seen in the return data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__rest_wait_for(dev, uri, self._get_request, data,
                                                                 expected_return_values, response_code, rest_server_ip,
                                                                 rest_server_port, max_wait, interval, exact_match)

        kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                           "REST command passed", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_put_request_and_wait_for_expected_result(self, device_name, uri, expected_return_values, data=None,
                                                      response_code=None, rest_server_ip=None, rest_server_port=None,
                                                      max_wait="60", interval="5", exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device name the keyword should be run against.
        [uri] - The location if the resource being requested.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.
        [max_wait] - The longest the keyword will wait before determining the keyword failed.
        [interval] - How often the keyword should execute.

        Sends a GET request and waits until the expected return values are seen in the return data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__rest_wait_for(dev, uri, self._put_request, data,
                                                                 expected_return_values, response_code,
                                                                 rest_server_ip, rest_server_port, max_wait, interval,
                                                                 exact_match)

        kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                           "REST command passed", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_post_request_and_wait_for_expected_result(self, device_name, uri, expected_return_values, data=None,
                                                       response_code=None, rest_server_ip=None, rest_server_port=None,
                                                       max_wait="60", interval="5", exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device name the keyword should be run against.
        [uri] - The location if the resource being requested.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.
        [max_wait] - The longest the keyword will wait before determining the keyword failed.
        [interval] - How often the keyword should execute.

        Sends a GET request and waits until the expected return values are seen in the return data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__rest_wait_for(dev, uri, self._post_request, data,
                                                                 expected_return_values, response_code,
                                                                 rest_server_ip, rest_server_port, max_wait, interval,
                                                                 exact_match)

        kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                           "REST command passed", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_patch_request_and_wait_for_expected_result(self, device_name, uri, expected_return_values, data=None,
                                                        response_code=None, rest_server_ip=None, rest_server_port=None,
                                                        max_wait="60", interval="5", exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device name the keyword should be run against.
        [uri] - The location if the resource being requested.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.
        [max_wait] - The longest the keyword will wait before determining the keyword failed.
        [interval] - How often the keyword should execute.

        Sends a GET request and waits until the expected return values are seen in the return data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__rest_wait_for(dev, uri, self._patch_request, data,
                                                                 expected_return_values, response_code, rest_server_ip,
                                                                 rest_server_port, max_wait, interval, exact_match)

        kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                           "REST command passed", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def send_delete_request_and_wait_for_expected_result(self, device_name, uri, expected_return_values, data=None,
                                                         response_code=None, rest_server_ip=None, rest_server_port=None,
                                                         max_wait="60", interval="5", exact_match=False, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device name the keyword should be run against.
        [uri] - The location if the resource being requested.
        [expected_return_values] - This must be a python dictionary or string that can be converted
                                   to a python dictionary. Each key must have a single string or integer
                                   value.
        [data] - Extra that should be included in the request. Should be in dictionary format.
        [response_code] - The response code that is expected to be returned.
        [rest_server_ip] - This argument is only used for non-rest connections. When a non-rest connection
                           is used a curl command is sent instead. If the rest server IP is different than
                           the device IP this argument should be used.
        [rest_server_port] - Same as above, but the port that should be used.
        [max_wait] - The longest the keyword will wait before determining the keyword failed.
        [interval] - How often the keyword should execute.

        Sends a GET request and waits until the expected return values are seen in the return data.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result, fail_string, rest_cmd_obj = self.__rest_wait_for(dev, uri, self._delete_request, data,
                                                                 expected_return_values, response_code, rest_server_ip,
                                                                 rest_server_port, max_wait, interval, exact_match)

        kw_result = self._determine_result(dev, rest_cmd_obj, result, True,
                                           "REST command passed", fail_string, **kwargs)

        return self._keyword_cleanup([kw_result])

    def __rest_wait_for(self, dev, uri, request_type, data, expected_return_values, response_code, rest_server_ip,
                        rest_server_port, max_wait, interval, exact_match):
        result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, request_type, data,
                                                                     expected_return_values, response_code,
                                                                     rest_server_ip, rest_server_port, exact_match)

        if result is None:
            return False, fail_string, rest_cmd_obj

        if not result:
            start_time = time.time()
            time.sleep(int(interval))

            while (time.time() - start_time) < int(max_wait):
                result, fail_string, rest_cmd_obj = self.__send_rest_request(dev, uri, request_type, data,
                                                                             expected_return_values, response_code,
                                                                             rest_server_ip, rest_server_port,
                                                                             exact_match)

                if not result:
                    self.logger.log_info("Expected return value not found, resending command.")
                    self.logger.log_info("Elapsed time " + str(int(time.time() - start_time)) + " seconds.")
                    time.sleep(int(interval))
                else:
                    break

        return result, fail_string, rest_cmd_obj

    def send_rest_request(self, device_name, uri, request_type, data=None):
        """
        Executes the REST command request.
        """
        dev, _, _ = self._init_keyword(device_name)

        rest_cmd_obj = RestCommandObject()
        rest_cmd_obj.uri = uri
        rest_cmd_obj.request_type = request_type
        rest_cmd_obj.data = data

        return self.__send_via_http(dev, rest_cmd_obj)

    # ##################################################################################################################
    # ########################################## Non-keyword helper functions ##########################################
    # ##################################################################################################################
    def __send_rest_request(self, dev, uri, request_type, data, expected_return_values, response_code,
                            rest_server_ip, rest_server_port, exact_match):
        if request_type in self._all_request_types:
            fail_string = "REST command failed."
            json_value_inspection_result = None
            response_code_result = None
            if isinstance(data, str):
                json_data = json.loads(data)
                data = json.dumps(json_data)
            rest_cmd_obj = RestCommandObject()
            rest_cmd_obj.uri = uri
            rest_cmd_obj.request_type = request_type
            rest_cmd_obj.data = data

            if dev.connection_method == AgentConstants.TYPE_REST:
                rest_cmd_obj = self.__send_via_http(dev, rest_cmd_obj)

                if response_code is not None:
                    response_code_result = self.__validate_response_code(rest_cmd_obj, response_code)
            else:
                rest_cmd_obj, fail_string = self.__send_via_curl(dev, rest_server_ip, rest_server_port)

                if response_code is not None:
                    self.logger.log_info("Response code verification is not supported when sending REST requests " +
                                         "via curl, skipping.")

            if rest_cmd_obj.return_text is not None:
                self.logger.log_info("Returned JSON: " + json.dumps(rest_cmd_obj.return_text, indent=2))
                if expected_return_values is not None:
                    json_value_inspection_result = self.__validate_json_output(rest_cmd_obj.return_text,
                                                                               expected_return_values, exact_match)

            if json_value_inspection_result is not None and response_code_result is not None:
                request_result = json_value_inspection_result and response_code_result
            elif json_value_inspection_result is not None:
                request_result = json_value_inspection_result
            elif response_code_result is not None:
                request_result = response_code_result
            else:
                request_result = None

            request_result = False if rest_cmd_obj.return_text is None else request_result

            return request_result, fail_string, rest_cmd_obj
        else:
            raise Exception(request_type + " is not valid request type.")

    @staticmethod
    def __send_via_http(dev, rest_cmd_obj):
        return dev.current_agent.send_command_object(rest_cmd_obj)

    def __send_via_curl(self, dev, rest_server_ip, rest_server_port):
        fail_string = "REST command failed."

        command = self.__create_curl_command(dev, rest_server_ip, rest_server_port)

        cmd_obj = CliCommandObject()
        cmd_obj.command = command
        cmd_obj.prompt = "userPrompt"

        cmd_obj = dev.send_command_object(cmd_obj)

        curl_errors = ["curl: command not found",
                       "not installed"]

        if any(error in cmd_obj.return_text for error in curl_errors):
            fail_string = "Curl not installed on device, install it and re-run."
            cmd_obj.return_text = None
        elif "Connection refused" in cmd_obj.return_text:
            fail_string = "Unable to connect to REST server."
            cmd_obj.return_text = None
        else:
            try:
                cmd_obj.return_text = cmd_obj.return_text[cmd_obj.return_text.find("\r\n"):]
                cmd_obj.return_text = self.__get_curl_json(cmd_obj.return_text)
                self.logger.log_info(StringUtils.pretty_print_dict
                                     (StringUtils.format_json_output(cmd_obj.return_text)))
            except AttributeError as e:
                fail_string = "Unknown error when sending REST request via curl."
                self.logger.log_trace(e)
                cmd_obj.return_text = None
            except ValueError:
                fail_string = "Invalid JSON returned, is the URL, IP, and port correct?"
                cmd_obj.return_text = None

        return cmd_obj, fail_string

    @staticmethod
    def __get_curl_json(output):
        start_char = None
        json_start = None
        json_end = None

        for index, c in enumerate(output):
            if c in ["[", "{"]:
                start_char = c
                json_start = index
                break

        if json_start is None or start_char is None:
            raise ValueError("Invalid JSON.")

        for index in range(len(output) - 1, -1, -1):
            if start_char == "{":
                if output[index] == "}":
                    json_end = index
                    break
            elif start_char == "[":
                if output[index] == "]":
                    json_end = index
                    break
            else:
                raise ValueError("Invalid JSON.")

        return output[json_start:json_end + 1]

    def __validate_response_code(self, rest_cmd_obj, expected_response_code):
        if str(rest_cmd_obj.return_status_code) == str(expected_response_code):
            result = True
            self.logger.log_info("Received response code " + str(rest_cmd_obj.return_status_code) +
                                 " which was equal to " + str(expected_response_code) + ".")

        else:
            result = False
            self.logger.log_info("Received response code " + str(rest_cmd_obj.return_status_code) +
                                 " which was NOT equal to " + str(expected_response_code) + ".")

        return result

    def __validate_json_output(self, rest_cmd_obj, expected_values, exact_match):
        result = None

        if isinstance(expected_values, str):
            expected_values = StringUtils.format_json_output(expected_values)

        for key in expected_values.keys():
            if JsonUtils.search_json(rest_cmd_obj, key, expected_values[key], exact_match):
                self.logger.log_info("Found: {" + str(key) + ": " + str(expected_values[key]) + "}")

                if result is None:
                    result = True
            else:
                self.logger.log_info("Not found: {" + str(key) + ": " + str(expected_values[key]) + "}")
                result = False
        return result

    def __create_curl_command(self, dev, ip, port):
        if ip is None:
            ip = dev.hostname

        if port is None:
            port = dev.port

        if self.rest_cmd_obj.uri[0] != "/":
            uri = "/" + self.rest_cmd_obj.uri
        else:
            uri = self.rest_cmd_obj.uri

        url = "http://" + ip + ":" + port + uri

        command = "curl -X " + self.rest_cmd_obj.request_type.upper() + " --header \"Accept: application/json\" "

        if self.rest_cmd_obj.data is not None:
            if not isinstance(self.rest_cmd_obj.data, dict):
                data = str(StringUtils.format_json_output(self.rest_cmd_obj.data))
            else:
                data = str(self.rest_cmd_obj.data)
            data = data.replace("\\", "")
            data = data.replace("\'", "\"")
            command += "-d \'" + str(data).replace("\\", "") + "\' "

        command += url

        return command

    @staticmethod
    def __create_uri(request_type, uri):
        # if a leading "/" is present, remove it.
        if uri[0] == "/":
            uri = uri[1::]

        command_dict = {"command": request_type + " " + uri}

        return command_dict

    @staticmethod
    def __convert_data(data):
        if isinstance(data, dict):
            return json.dumps(data)
        else:
            return data
