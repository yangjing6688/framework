import json
from time import sleep
import pprint
from tools.xapi.XapiHelper import XapiHelper
from extauto.common.Utils import Utils

try:
    import extremecloudiq
    from extremecloudiq.rest import ApiException
except Exception:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')


class XapiBase(object):

    def __init__(self):
        self.xapiHelper = XapiHelper()
        self.utils = Utils()
        self.extremecloudiq = extremecloudiq
        self.ApiException = ApiException

    def is_xapi_enabled(self, **kwargs):
        """
            Checks to see if the XAPI_ENABLE variable is set in kwargs or globally

            :param kwargs: Looks for XAPI_ENABLE in kwargs
            :return: True if the XAPI_ENABLE is in kwargs or set globally, false otherwise
        """
        # Check to see if the user enabled XAPI via the kwargs or globally
        if self.XapiHelper.common_validation.get_kwarg(kwargs, "XAPI_ENABLE", None) or self.xapiHelper.is_xapi_enabled():
            return True
        else:
            return False

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
        configuration = self.xapiHelper.get_xapi_configuration()

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
                self.xapiHelper.common_validation.failed(**kwargs)
                return None

    #########################################################################
    # Helper functions
    #########################################################################

    def _xapi_search_for_device_id(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
           This helper function will search for the device ID given the parameters that were passed in.
           This ID is used in all of the XAPI keywords as the device ID

           :param device_serial: The device serial number
           :param device_name: The device hostname
           :param device_mac: The device MAC address
           :param device_mac: The device MAC address
           :param skip_global_check: false by default, will skip the global device check
           :return: The device ID for success and -1 for failure
        """
        device_id = -1

        # figure out the value being used to look for the device
        search_type = None
        if device_serial:
            self.utils.print_info(f"XAPI - Searching for device based on serial {device_serial}")
            search_type = device_serial
        elif device_name:
            self.utils.print_info(f"XAPI - Searching for device based on name {device_name}")
            search_type = device_name
        elif device_mac:
            self.utils.print_info(f"XAPI - Searching for device based on mac {device_mac}")
            search_type = device_mac

        # get the global dict for the type
        device_id = self.xapiHelper.get_xapi_global_device(search_type)
        if device_id != -1:
            self.utils.print_info(f"Found device ID: {device_id}")
            return device_id

        # Get all of the devices
        device_api_data = self.xapi_get_device(device_serial=device_serial, \
                                               device_name=device_name, \
                                               device_mac=device_mac, \
                                               **kwargs)

        device_list = device_api_data['data']

        if len(device_list) != 0:
            for device in device_list:
                # Search for the device based on the parameters that were passed in
                if device_serial:
                    if device['serial_number'] == device_serial:
                        device_id = device['id']
                        self.utils.print_info(
                            f"Setting global value for device [serial]: {device_serial}:{device_id}")
                        self.xapiHelper.set_xapi_global_device(device_serial, device_id)
                        break
                elif device_name:
                    if device['hostname'] == device_name:
                        device_id = device['id']
                        self.utils.print_info(f"Setting global value for device [name]: {device_name}:{device_id}")
                        self.xapiHelper.set_xapi_global_device(device_serial, device_id)
                        break
                elif device_mac:
                    if device['mac_address'] == device_mac:
                        device_id = device['id']
                        self.utils.print_info(f"Setting global value for device [mac]: {device_mac}:{device_id}")
                        self.xapiHelper.set_xapi_global_device(device_serial, device_id)
                        break
        return device_id


    def xapi_search_for_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
            This function will search for a device with the serial, name or mac address that is passed in.

            :param device_serial: The device serial number
            :param device_name: The device hostname
            :param device_mac: The device MAC address
            :return: 1 for success and -1 for failure
        """
        id = self._xapi_search_for_device_id(device_serial=device_serial, device_name=device_name, device_mac=device_mac, **kwargs)
        if id == -1:
            kwargs['fail_msg'] = f"Failed to get the device ID for serial:{device_serial} or mac:{device_mac} or name: {device_name}"
            self.xapiHelper.common_validation.fault(**kwargs)
            return -1

        return self.xapiBaseDeviceApi.xapi_base_get_device(id=id, _preload_content=False)

    def xapi_get_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
           This helper function will get the device given the parmeters that are passed in for
           device_serial, device_name or device_mac

           :param: device_serial - The device serial
           :param: device_name - The device name
           :param: device_mac - The device mac
           :return: The device JSON or -1 if an error occured
        """
        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        try:
            api_response = None
            device_args = {}
            device_args['_async'] = True
            device_args['_preload_content'] = False
            if device_serial:
                device_args['sns']=[device_serial]
            elif device_name:
                device_args['hostnames']=[device_name]
            elif device_mac:
                device_args['mac_addresses']=[device_mac]
            else:
                kwargs['fail_msg'] = f"xapi_get_device -> device_serial: {device_serial}, device_name: {device_name}, device_mac: {device_mac} are not set!"
                self.xapiHelper.common_validation.fault(**kwargs)
                return -1
            api_response = self.xapiBaseDeviceApi.xapi_base_list_devices(**device_args)
            return api_response

        except Exception as e:
            kwargs['fail_msg'] = f"Exception when calling DeviceApi->list_devices: {e}"
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1