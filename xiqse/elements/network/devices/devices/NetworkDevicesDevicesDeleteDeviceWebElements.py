from common.WebElementHandler import *
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesDeleteDeviceWebElementsDefinitions import *


class NetworkDevicesDevicesDeleteDeviceWebElements(NetworkDevicesDevicesDeleteDeviceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_yes_button(self):
        """
        :return: 'Yes' button in the Delete Device dialog
        """
        return self.weh.get_element(self.yes_button)

    def get_no_button(self):
        """
        :return: 'No' button in the Delete Device dialog
        """
        return self.weh.get_element(self.no_button)
