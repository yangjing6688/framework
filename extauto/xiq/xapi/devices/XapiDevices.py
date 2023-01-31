import time
from time import sleep
import json
from extauto.xiq.xapi.XapiBase import XapiBase

class XapiDevices(XapiBase):

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
            api_instance = self.extremecloudiq.DeviceApi(api_client)

            try:
                # Onboard Devices
                returnCode = api_instance.onboard_devices(xiq_onboard_device_request)
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1
            except self.ApiException as e:
                print("Exception when calling DeviceApi->onboard_devices: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1


    def xapi_search_for_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
            This methods will search for a device with the serial, name or mac address that is passed in.

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
                kwargs['pass_msg'] = 'Device was found'
                self.xapiHelper.common_validation.passed(**kwargs)
                return api_response.data
            except self.ApiException as e:
                kwargs['fail_msg'] = f'Exception when calling DeviceApi->get_device: {e}\n'
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_reboot_device(self, device_serial=None, device_mac=None, **kwargs):
        """
           This methods will reboot the device and will not sleep

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
                kwargs['pass_msg'] = 'Device reboot command was sent'
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1
            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->reboot_device: {e}\n"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1


    def _xapi_list_devices(self, **kwargs):
        """
           This helper methods will get all of the devices

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
                # ERROR - ValueError: Invalid value for `create_time`, must not be `None`
                api_response = api_instance.list_devices(_preload_content=False)  # total hack for now
                self.xapiHelper.common_validation.passed(**kwargs)
                return json.loads(api_response.data)

            except self.ApiException as e:
                print("Exception when calling DeviceApi->list_devices: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def _xapi_search_for_device_id(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
           This helper methods will search for the device ID given the parameters that were passed in

           :param device_serial: The device serial number
           :param device_name: The device hostname
           :param device_mac: The device MAC address
           :return: The device ID for success and -1 for failure
        """
        device_id = -1
        # Get all of the devices
        device_api_data = self._xapi_list_devices(**kwargs)
        device_list = device_api_data['data']

        if len(device_list) != 0:
            for device in device_list:
                # Search for the device based on the parameters that were passed in
                if device_serial:
                    if device['serial_number'] == device_serial:
                        device_id = device['id']
                        break
                elif device_name:
                    if device['hostname'] == device_name:
                        device_id = device['id']
                        break
                elif device_mac:
                    if device['mac_address'] == device_mac:
                        device_id = device['id']
                        break
        return device_id

    def xapi_wait_until_device_online(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=20,
                                     **kwargs):
        """
           This methods will search for the device and wait until the device is online

           :param device_serial: The device serial number
           :param device_mac: The device MAC address
           :param retry_duration: The duration of the sleep in between the loops
           :param retry_count: The number of loops

           :return: The device ID for success and -1 for failure
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
                while retry_value < retry_count:
                    # get Device information
                    api_response = api_instance.get_device(id, _preload_content=False)
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
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->xapi_wait_until_device_online: {e}\n"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

            # In the case that nothing is found
            kwargs['fail_msg'] = 'Device was not found'
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1

    def xapi_wait_until_device_managed(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=20,
                                      **kwargs):
        """
              This methods will search for the device and wait until the device is managed

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
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->get_device: {e}\n"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

            # In the case that nothing is found
            kwargs['fail_msg'] = 'Device did not get to Managed state'
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1

    def xapi_delete_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
            This methods will delete the device

            :param device_serial: The device serial number
            :param device_mac: The device MAC address
            :param device_name: The device Name

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
                # get Device information
                api_response = api_instance.delete_device(id)
                kwargs['pass_msg'] = f"Device has been delete"
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1

            except self.ApiException as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->delete_device: {e}\n"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

            # In the case that nothing is found
            self.xapiHelper.common_validation.failed(**kwargs)
            return -1


# def assign_device_network_policy(self, id=None, network_policy_id=None):
#     api_instance = extremecloudiq.DeviceApi(self.api_client)
#
#     api_response = api_instance.assign_device_network_policy(id, network_policy_id)
#
#     return api_response
#
#
# def assign_devices_country_code(self, ids=None):
#     api_instance = extremecloudiq.DeviceApi(self.api_client)
#
#     devices = extremecloudiq.XiqDeviceFilter(ids=ids)
#
#     country_code = extremecloudiq.XiqCountryCode.SINGAPORE_702  # see xiq_country_code.py for countries
#
#     xiq_assign_devices_country_code_request = extremecloudiq.XiqAssignDevicesCountryCodeRequest(devices=devices,
#                                                                                                 country_code=country_code)
#
#     api_response = api_instance.assign_devices_country_code(xiq_assign_devices_country_code_request)
#
#     return api_response
#
#
# def assign_device_location(self, id=None, location_id=None):
#     api_instance = extremecloudiq.DeviceApi(self.api_client)
#
#     xiq_device_location_assignment = extremecloudiq.XiqDeviceLocationAssignment(
#         location_id=location_id,
#         x=None,
#         y=None,
#         latitude=None,
#         longitude=None,
#         local_vars_configuration=None
#     )
#
#     api_response = api_instance.assign_device_location(id, xiq_device_location_assignment)
#
#     return api_response