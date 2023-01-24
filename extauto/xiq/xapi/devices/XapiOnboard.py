import pprint
import time
from extauto.xiq.xapi.XapiHelper import XapiHelper

try:
    import extremecloudiq
    from extremecloudiq.rest import ApiException
except:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')


class XapiOnboard:

    def __init__(self):
        self.xapiHelper = XapiHelper()

    def onBoardDevice(self, device, **kwargs):
        """
            - Onboard a device

            :param device: The device object
            :return: api_response  This will be None if the command failed or will contain the JSON from the API call
        """

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()

        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise "Error: access_token is None in the configuration"

        # Enter a context with an instance of the API client
        with extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = extremecloudiq.DeviceApi(api_client)
            xiq_onboard_device_request = extremecloudiq.XiqOnboardDeviceRequest()  # XiqOnboardDeviceRequest |
            self.xapiHelper.common_validation.passed(**kwargs)
            return -1
            try:
                # Onboard Devices
                api_instance.onboard_devices(xiq_onboard_device_request)
            except ApiException as e:
                print("Exception when calling DeviceApi->onboard_devices: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

