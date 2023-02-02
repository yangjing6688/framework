import time
from time import sleep
import json
from extauto.xiq.xapi.XapiBase import XapiBase

class XapiDevices(XapiBase):

    def __init__(self):
        super().__init__()
        # Supported UI to XAPI column selector
        self.NOT_SUPPORTED = 'not_supported'
        self.device_column_ui_to_xapi = {}
        self.device_column_ui_to_xapi['STATUS'] = 'connected'
        self.device_column_ui_to_xapi['HOST NAME'] = 'hostname'
        self.device_column_ui_to_xapi['NETWORK POLICY'] = 'network_policy_name'
        self.device_column_ui_to_xapi['MANAGED BY'] = self.NOT_SUPPORTED
        self.device_column_ui_to_xapi['UPTIME'] = self.NOT_SUPPORTED
        self.device_column_ui_to_xapi['MGT IP ADDRESS'] = 'ip_address'
        self.device_column_ui_to_xapi['DEFAULT GATEWAY'] = 'default_gateway'
        self.device_column_ui_to_xapi['CLIENTS'] = self.NOT_SUPPORTED
        self.device_column_ui_to_xapi['MAC'] = 'mac_address'
        self.device_column_ui_to_xapi['LOCATION'] = 'locations'
        self.device_column_ui_to_xapi['SERIAL #'] = 'serial_number'
        self.device_column_ui_to_xapi['FEATURE LICENSE'] = self.NOT_SUPPORTED
        self.device_column_ui_to_xapi['MODEL'] = 'product_type'
        self.device_column_ui_to_xapi['OS VERSION'] = 'software_version'
        self.device_column_ui_to_xapi['UPDATED'] = 'update_time'
        self.device_column_ui_to_xapi['MGT VLAN'] = self.NOT_SUPPORTED
        self.device_column_ui_to_xapi['MAKE'] = self.NOT_SUPPORTED
        self.device_column_ui_to_xapi['MANAGED'] = 'device_admin_state'
        self.device_column_ui_to_xapi['COUNTRY'] = 'country_code'
        self.device_column_ui_to_xapi['OS'] = self.NOT_SUPPORTED



    #########################################################################
    # Keyword functions
    #########################################################################

    def xapi_onboard_device(self, device_dict, **kwargs):
        """
            Onboard a device

            :param device_dict: The device object
            :return: 1 for success and -1 for failure

        """

        # Create the JSON payload
        unknown_device_type = 'Unknown_device_type'
        device_serial = device_dict.get("serial")
        device_make = device_dict.get('make', unknown_device_type)
        service_tag = device_dict.get("service_tag", None)  # argument for Real device ---> Dell
        device_mac = device_dict.get("mac", None)           # argument for Real device ---> WING

        json_payload = {}
        extreme_payload = None
        exos_payload = None
        voss_payload = None
        wing_payload = None
        dell_payload = None
        if 'Extreme - Aerohive' in device_make:
            self.utils.print_info("Detected AP, creating payload")
            extreme_payload = self.extremecloudiq.XiqExtremeDevices(sns=[device_serial])
            xiq_onboard_device_request = self.extremecloudiq.XiqOnboardDeviceRequest(extreme=extreme_payload)
        elif "VOSS" in device_make.upper():
            self.utils.print_info("Detected VOSS, creating payload")
            voss_payload = self.extremecloudiq.XiqVossDevices(sns=[device_serial])
            xiq_onboard_device_request = self.extremecloudiq.XiqOnboardDeviceRequest(voss=voss_payload)
        elif "EXOS" in device_make.upper():
            self.utils.print_info("Detected EXOS, creating payload")
            exos_payload = self.extremecloudiq.XiqExosDevices(sns=[device_serial])
            xiq_onboard_device_request = self.extremecloudiq.XiqOnboardDeviceRequest(exos=exos_payload)
        elif 'DELL' in device_make.upper():
            self.utils.print_info("Detected Dell, creating payload")
            dell_payload = self.extremecloudiq.XiqDellDevices(sn_to_st={device_serial : service_tag})
            xiq_onboard_device_request = self.extremecloudiq.XiqOnboardDeviceRequest(dell=dell_payload)
        elif 'CONTROLLERS' in device_make.upper() or 'XCC' in device_make.upper():
            self.utils.print_info("Detected Wing, creating payload")
            dell_payload = self.extremecloudiq.XiqWingDevices(sn_to_st={device_serial : device_mac})
            xiq_onboard_device_request = self.extremecloudiq.XiqOnboardDeviceRequest(wing=wing_payload)

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_device = self.extremecloudiq.DeviceApi(api_client)
            try:
                # Onboard Devices
                # FIXME = This returns NONE, however the swagger returns a 202 and no payload.
                #  The aysnc doens't appear to be working for this API function and the
                # swagger doens't support the [LRO], so there is no way of knowning
                # if this keyword was successful without creating a loop to check.
                api_device.onboard_devices(xiq_onboard_device_request)

                count = 0
                retries = 10
                device_found = self._xapi_search_for_device_id(device_serial=device_serial)
                while device_found == -1:
                    self.utils.print_info('Device was not found, sleep for 30 seconds')
                    sleep(30)
                    self.utils.print_info('Checking for device onboard completed')
                    device_found = self._xapi_search_for_device_id(device_serial=device_serial)

                if device_found == -1:
                    kwargs['fail_msg'] = f"Device was not found with serial: {device_serial}"
                    self.xapiHelper.common_validation.failed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = f"Device was found with serial: {device_serial}"
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return 1
            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->onboard_devices: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1


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

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                # Get Devices
                api_response = api_instance.get_device(id, _preload_content=False)
                self.valid_http_response(api_response)
                kwargs['pass_msg'] = 'Device was found'
                self.xapiHelper.common_validation.passed(**kwargs)
                return api_response.data
            except self.ApiException as e:
                kwargs['fail_msg'] = f'Exception when calling DeviceApi->get_device: {e}'
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_reboot_device(self, device_serial=None, device_mac=None, **kwargs):
        """
           This function will reboot the device and will not sleep

           :param device_serial: The device serial number
           :param device_mac: The device MAC address
           :return: 1 for success and -1 for failure
        """
        id = self._xapi_search_for_device_id(device_serial=device_serial, device_mac=device_mac, **kwargs)
        if id == -1:
            kwargs['fail_msg'] = f"Failed to get the device ID for serial:{device_serial} or mac:{device_mac}"
            self.xapiHelper.common_validation.fault(**kwargs)
            return -1

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                api_response = api_instance.reboot_device(id)
                self.valid_http_response(api_response)
                kwargs['pass_msg'] = 'Device reboot command was sent'
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1
            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->reboot_device: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_search_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        This function will search for the device based on the serial, name or mac

        :param device_serial: The device serial number
        :param device_name: The device hostname
        :param device_mac: The device mac address
        :param kwargs:
        :return: 1 if the device was found and -1 if the device wasn't found
        """
        device_id = self._xapi_search_for_device_id(device_serial=device_serial, device_name=device_name, device_mac=device_mac)
        if device_id != -1:
            kwargs['pass_msg'] = f"Found the device with serial:{device_serial}, name: {device_name} or MAC: {device_mac}"
            self.xapiHelper.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"Failed to find the device with serial:{device_serial}, name: {device_name} or MAC: {device_mac}"
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1


    def xapi_wait_until_device_online(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=20,
                                     **kwargs):
        """
           This function will search for the device and wait until the device is online

           :param device_serial: The device serial number
           :param device_mac: The device MAC address
           :param retry_duration: The duration of the sleep in between the loops
           :param retry_count: The number of loops

           :return: The device ID for success and -1 for failure
        """
        retry_value = 0
        id = self._xapi_search_for_device_id(device_serial=device_serial, device_mac=device_mac, **kwargs)
        if id == -1:
            kwargs['fail_msg'] = f"Failed to get the device ID for serial:{device_serial} or mac:{device_mac}"
            self.xapiHelper.common_validation.fault(**kwargs)
            return -1

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                while retry_value < retry_count:
                    # get Device information
                    api_response = api_instance.get_device(id, _preload_content=False)
                    self.valid_http_response(api_response)
                    data = json.loads(api_response.data)
                    if data.get('connected', False):
                        kwargs['pass_msg'] = "Device Connected Status Value is: True (Connected)"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return 1
                    else:
                        self.utils.print_info(f"Device Connected Status Value is: False (Not Connected), sleeping {retry_duration} seconds")
                        sleep(retry_duration)
                        retry_value += 1

            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->xapi_wait_until_device_online: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

            # In the case that nothing is found
            kwargs['fail_msg'] = 'Device was not found'
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1

    def xapi_wait_until_device_managed(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=20,
                                      **kwargs):
        """
              This function will search for the device and wait until the device is managed

              :param device_serial: The device serial number
              :param device_mac: The device MAC address
              :param retry_duration: The duration of the sleep in between the loops
              :param retry_count: The number of loops

              :return: The device ID for success and -1 for failure
           """
        retry_value = 0
        id = self._xapi_search_for_device_id(device_serial=device_serial, device_mac=device_mac, **kwargs)
        if id == -1:
            kwargs['fail_msg'] = f"Failed to get the device ID for serial:{device_serial} or mac:{device_mac}"
            self.xapiHelper.common_validation.fault(**kwargs)
            return -1

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                while retry_value < retry_count:
                    # get Device information
                    api_response = api_instance.get_device(id, _preload_content=False)
                    self.valid_http_response(api_response)
                    data = json.loads(api_response.data)
                    device_admin_state = data.get('device_admin_state', '')
                    if device_admin_state == 'MANAGED':
                        kwargs['pass_msg'] = f"Device admin state Value is: {device_admin_state}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return 1
                    else:
                        self.utils.print_info(
                            f"Device Connected Status Value is: {device_admin_state}, sleeping {retry_duration} seconds")
                        sleep(retry_duration)
                        retry_value += 1

            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->get_device: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

            # In the case that nothing is found
            kwargs['fail_msg'] = 'Device did not get to Managed state'
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1

    def xapi_delete_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
            This function will delete the device

            :param device_serial: The device serial number
            :param device_mac: The device MAC address
            :param device_name: The device Name

            :return: The device ID for success and -1 for failure
       """
        retry_value = 0
        id = self._xapi_search_for_device_id(device_serial=device_serial, device_mac=device_mac, **kwargs)
        if id == -1:
            kwargs['fail_msg'] = f"Failed to get the device ID for serial:{device_serial} or mac:{device_mac}"
            self.xapiHelper.common_validation.fail(**kwargs)
            return -1

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                # delete Device information
                # FIXME = This returns NONE, however the swagger returns a 202 and no payload.
                #  The aysnc doens't appear to be working for this API function and the
                # swagger doens't support the [LRO], so there is no way of knowning
                # if this keyword was successful without creating a loop to check.
                operation = api_instance.delete_device(id)

                # delete this from the cache
                self.xapiHelper.delete_xapi_global_device(device_serial)

                count = 0
                retries = 10
                device_found = self._xapi_search_for_device_id(device_serial=device_serial)
                while device_found == 1:
                    self.utils.print_info('Device was found, sleep for 30 seconds')
                    sleep(30)
                    self.utils.print_info('Checking to make sure the device was deleted')
                    device_found = self._xapi_search_for_device_id(device_serial=device_serial)

                if device_found == -1:
                    kwargs['pass_msg'] = f"Device was delete with serial: {device_serial}"
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = f"Device was found with serial: {device_serial}"
                    self.xapiHelper.common_validation.failed(**kwargs)
                    return 1

                kwargs['pass_msg'] = f"Device has been delete"
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1

            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->delete_device: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

            # In the case that nothing is found
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1

    def xapi_get_device_column_information(self, device_serial, column_array, **kwargs):
        """
            :param device_serial: The device serial number
            :param column_array: The list UI of columns to query
            :param kwargs: The kwargs
            :return: A dict for the {column name: value}, if the value isn't found the value will be replace with 'value_not_found'
        """
        id = self._xapi_search_for_device_id(device_serial=device_serial, **kwargs)
        if id == -1:
            kwargs['fail_msg'] = f"Failed to get the device ID for serial:{device_serial}"
            self.xapiHelper.common_validation.fault(**kwargs)
            return -1

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        return_data = {}
        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                # get Device information
                api_response = api_instance.get_device(id, views=['full'], _preload_content=False)
                self.valid_http_response(api_response)
                json_data = json.loads(api_response.data)
                for column in column_array:
                    json_column_name = self.device_column_ui_to_xapi.get(column)
                    if json_column_name != self.NOT_SUPPORTED:
                        column_data = json_data.get(json_column_name, 'value_not_found')
                        return_data[column.replace(' ',"_")] = column_data
                kwargs['pass_msg'] = f"Device has been quereid"
                self.xapiHelper.common_validation.passed(**kwargs)
                return return_data

            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->xapi_get_device_column_information: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1


    #########################################################################
    # Helper functions
    #########################################################################

    def _xapi_list_devices(self, **kwargs):
        """
           This helper function will get all of the devices

           :return: An Array of devices (JSON)
        """
        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.DeviceApi(api_client)
            try:
                api_response = api_instance.list_devices(limit = 100, _preload_content=False)
                self.valid_http_response(api_response)
                self.xapiHelper.common_validation.passed(**kwargs)
                return json.loads(api_response.data)

            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->list_devices: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

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
        device_api_data = self._xapi_list_devices(**kwargs)
        device_list = device_api_data['data']

        if len(device_list) != 0:
            for device in device_list:
                # Search for the device based on the parameters that were passed in
                if device_serial:
                    if device['serial_number'] == device_serial:
                        device_id = device['id']
                        self.utils.print_info(f"Setting global value for device [serial]: {device_serial}:{device_id}")
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