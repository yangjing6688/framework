import time
import json
from extauto.xiq.xapi.XapiBase import XapiBase

class XapiDevices(XapiBase):

    def xapi_onboard_device(self, device_dict, **kwargs):
        """
            - Onboard a device

            :param device: The device object
            :return: api_response  This will be None if the command failed or will contain the JSON from the API call

            {
                "extreme": {
                    "sns": ["zzzz-zzz-zzz"]
                },
                "exos": {
                    "sns": ["zzzz-zzz-www"]
                },
                "voss": {
                    "sns": ["zzzz-zzz-www"]
                },
                "wing": {
                    "sn_to_mac": {
                        "serial_num": "mac_address"
                    }
                },
                "dell": {
                    "sn_to_st": {
                        "serial_num": "service_tag"
                    }
                }
            }
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
            dell_payload = self.extremecloudiq.XiqDellDevices(sn_to_st=[{device_serial : service_tag}])
            xiq_onboard_device_request = self.extremecloudiq.XiqOnboardDeviceRequest(dell=dell_payload)
        elif 'CONTROLLERS' in device_make.upper() or 'XCC' in device_make.upper():
            self.utils.print_info("Detected Wing, creating payload")
            dell_payload = self.extremecloudiq.XiqWingDevices(sn_to_st=[{device_serial : device_mac}])
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

        id = self._xapi_search_for_device_id(device_serial=device_serial, device_name=device_name, device_mac=device_mac, **kwargs)

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
                api_response = api_instance.get_device(id, _preload_content=False)  # total hack for now
                self.xapiHelper.common_validation.passed(**kwargs)
                return api_response.data
            except self.ApiException as e:
                print("Exception when calling DeviceApi->get_device: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_delete_device(self, id=None):
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
                api_response = api_instance.delete_device(id)
                self.xapiHelper.common_validation.passed(**kwargs)
                return api_response.data
            except self.ApiException as e:
                print("Exception when calling DeviceApi->delete_device: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_reboot_device(self, id=None):
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
                self.xapiHelper.common_validation.passed(**kwargs)
                return api_response.data
            except self.ApiException as e:
                print("Exception when calling DeviceApi->reboot_device: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1


    def xapi_list_devices(self, **kwargs):
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
        device_id = -1
        # Get all of the devices
        device_api_data = self.xapi_list_devices(**kwargs)
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