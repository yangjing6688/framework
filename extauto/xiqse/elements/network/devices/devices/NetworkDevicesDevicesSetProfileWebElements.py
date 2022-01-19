from extauto.common.WebElementHandler import *
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesSetProfileWebElementsDefinitions import *


class NetworkDevicesDevicesSetProfileWebElements(NetworkDevicesDevicesSetProfileWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_profile_dropdown(self):
        """
        :return: 'Profile' dropdown in the Set Device Profile dialog
        """
        return self.weh.get_element(self.profile_dropdown)

    def get_cancel_button(self):
        """
        :return: 'Cancel' button in the Set Device Profile dialog
        """
        return self.weh.get_element(self.cancel_btn)

    def get_ok_button(self):
        """
        :return: 'OK' button in the Set Device Profile dialog
        """
        return self.weh.get_element(self.ok_btn)
