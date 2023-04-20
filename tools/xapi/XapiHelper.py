from extauto.common.CommonValidation import CommonValidation
from robot.libraries.BuiltIn import BuiltIn
import json
from time import sleep
import pprint
from extauto.common.Utils import Utils
from ExtremeAutomation.Library.Utils.DotDict import DotDict
import urllib3

try:
    import extremecloudiq
    from extremecloudiq.rest import ApiException
except Exception:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')

class XapiHelper():

    def __init__(self):
        self.common_validation = CommonValidation()
        self.builtin = BuiltIn()
        self.utils = Utils()
        self.extremecloudiq = extremecloudiq
        self.ApiException = ApiException

    def set_xapi_global_device(self, value, id):
        """
            This will set the data on the global level for the mapping of device (serial, name or mac) to xapi ID
        :param value: The value for the type (device serial, device name, device mac)
        :param id: The device XAPI ID
        :return: None
        """
        configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')
        if configuration == None:
            # Create a new object
            self.builtin.set_global_variable('${XAPI_GLOBAL_DEVICE}', {})
            # Get the new object and continue
            configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')

        # Next add / replace the value
        configuration.update({value:id})

    def delete_xapi_global_device(self, value):
        """
            This will delete the data on the global level for the mapping of device (serial, name or mac) to xapi ID
        :param value: The value for the type (device serial, device name, device mac)
        :return: None
        """
        configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')
        if configuration != None:
            del configuration[value]

    def get_xapi_global_device(self, value):
        """
           This will set the data on the global level for the mapping of device (serial, name or mac) to xapi ID
        :param value: The value for the type (device serial, device name, device mac)
        :return: The value if found or -1 if not found
        """
        id = -1
        configuration = self.builtin.get_variable_value('${XAPI_GLOBAL_DEVICE}')
        if configuration:
            id = configuration.get(value, -1)
        return id

    def print_http_response(self, http_response):
        """
            Prints the http repsonse for the object that is passed in
        :param http_response: http repsonse object
        :return: None
        """
        try:
            self.utils.print_info("http_response: " + json.dumps(json.loads(http_response.data), indent=4, separators=(',', ': ')))
        except Exception:
            pass

    def valid_http_response(self, api_response):
        """
            This method will valid the http response object make sure the return code is 200 or 201
            :param api_response: The HTTPResponse object
            :return: True when the status is 200 or 201, throws exception otherwise
        """
        self.print_http_response(api_response)
        # if the api_response is None
        if not api_response:
            raise Exception(
                'ERROR: valid_http_response -> HTTPResponse is None')
        # Make sure we have a status to check
        elif 'status' in api_response.__dict__.keys():
            # we do, so check to make sure we got a 200 or 201
            if api_response.status != 200 and api_response.status != 201:
                raise Exception(f'ERROR: valid_http_response -> HTTPResponse status returned failure: {api_response.status}')
        return True

    def getLongRunningOperationId(self, response):
        id = -1
        if 'Location' in response.headers:
            id = response.headers['Location'].split('/')[-1]
        return id

    def getAsyncLongRunningOperation(self, operation_id, **kwargs):
        """
            This method will poll the operation untit it has completed
        :param operation_id: When calling keywords with the async_req=True, this will be the operation id that is returned
        :return: The completed operation json, or None for an error
        """

        # Get the configuration from the Global varibles
        configuration = self.get_xapi_configuration()

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.OperationApi(api_client)

            try:
                # get operation status
                operation_object = api_instance.get_operation(operation_id)
                while operation_object.metadata.status != 'SUCCEEDED':
                    self.utils.print_info(f'Operation {operation_id} has not completed [SUCCEEDED], sleep for 10 seconds and try again')
                    sleep(10)
                    operation_object = api_instance.get_operation(operation_id)
                return operation_object.response
            except Exception as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->onboard_devices: {e}"
                self.common_validation.failed(**kwargs)
                return None

    def set_xapi_configuration(self, value):
        """
            This function sets the global configuration for the XAPI
        :param value: The configuration object
        :return: None
        """
        self.builtin.set_global_variable('${XAPI_CONFIGRATION}', value)

    def get_xapi_configuration(self):
        """
           This function sets the global configuration for the XAPI
       :param value: The configuration object
       :return: None
       """
        configuration = self.builtin.get_variable_value('${XAPI_CONFIGRATION}')
        if not configuration:
            raise Exception(
                'The XAPI configuration was not set, please use the "login_user" method in the Login class with the kwarg XAPI_ENABLE set to True. Also ensure that the xapi_url is set in the topo file.')
        return configuration

    def get_xapi_url(self):
        """
            Gets the xapi URL
        :return: the xpai URL or returns None if it is not set
        """
        try:
            # Set the default as an empty string and test for that below
            xapi_url = self.builtin.get_variable_value("${XAPI_URL}", default='')
            if xapi_url == '':
                self.utils.print_warning(
                    'XAPI url was not set, please make sure the xapi_url is set in the topo file in order to use XAPI.')
                return None
            else:
                return xapi_url
        except Exception as e:
            raise Exception(
                f'Exception: {e} \nXAPI url was not set, please make sure the xapi_url is set in the topo file')
            return None

    def set_xapi_url(self, value):
        """
            Sets the XAPI URL globally
        :param value: The xapi_url
        :return: None
        """
        self.builtin.set_global_variable("${XAPI_URL}", value)

    def is_xapi_enabled(self, **kwargs):
        """
            Checks to see if the XAPI_ENABLE is set globally or in the kwargs
        :param kwargs: dict for kwargs
        :return: True if the XAPI_ENABLE is set, False if it isn't set
        """
        # old way 'access_token'
        old_access_token_kwargs = kwargs.get('access_token', False)
        xapi_enabled_globally = self.builtin.get_variable_value("${XAPI_ENABLE}", False)
        xapi_enabled_kwargs = kwargs.get('XAPI_ENABLE', False)
        if xapi_enabled_globally or xapi_enabled_kwargs or old_access_token_kwargs:
            return True
        else:
            return False


    def set_xapi_enabled_value(self, value):
        """
            Sets the XAPI_ENABLE value globally
        :param value: The XAPI_ENABLE value
        :return: None
        """
        self.builtin.set_global_variable("${XAPI_ENABLE}", value)

    def convert_preload_content_data_to_object(self, object_string):
        """
            When using the _preload_content=False with any XAPI SDK keyword, you
            will get back a byte string data from the SDK. This method will convert
            that byte string to a JSON object
        :param object_string: The object string to convert (btye string) (repsonse.data from the XAPI SDK call) (can take the HTTPRepsonse)
        :return: The json object for the string
        """

        if isinstance(object_string, urllib3.HTTPResponse):
            object_string = object_string.data
        if isinstance(object_string, (bytes, bytearray)):
            # Decode UTF-8 bytes to Unicode, and convert single quotes
            # to double quotes to make it valid JSON
            json_friendly = object_string.decode('utf8').replace("'", '"')
        else:
            json_friendly = object_string
        data = json.loads(json_friendly)
        return DotDict(data)

    def check_dict_keys_in_original_dict(self, original_dict, check_dict, level=0):
        """
            Check the keys from the check dict to the keys in the check dict
        :param original_dict:  The base dict for all of the key values
        :param check_dict:  The dict to check againsted the original_dict
        :param level: Always set to 0, unless this is called internally from this function
        :return: True, if all of the keys exist, false if they don't
        """
        return_value = True
        if isinstance(original_dict, dict) and isinstance(check_dict, dict):
            check_top_level_keys = check_dict.keys()
            original_top_level_keys = original_dict.keys()

            for check_key in check_top_level_keys:
                level_tabs = '\t' * level
                if check_key not in original_top_level_keys:
                    print(f"{level_tabs}Mising key: {check_key}")
                    return_value = False
                else:
                    print(f"{level_tabs}key: {check_key}")
                check_value = check_dict[check_key]
                if check_key in original_dict:
                    orignal_value = original_dict[check_key]
                else:
                    orignal_value = original_dict
                if isinstance(check_value, dict):
                    return_value = checkDictKeysInArray(orignal_value, check_value, level + 1)
        return return_value


    def convert_enable_disable_to_bool(self, value):
        """
            Convert enable (set to lower case) to True and Disable to False.
        :param value:
        :return: enable returns True and Disable returns False
        """
        if not isinstance(value, bool):
            if str(value).lower() == 'disable':
                return False
            else:
                return True
        return value