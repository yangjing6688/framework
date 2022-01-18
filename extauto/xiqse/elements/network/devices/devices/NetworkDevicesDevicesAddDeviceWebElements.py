from common.WebElementHandler import *
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesAddDeviceWebElementsDefinitions import *


class NetworkDevicesDevicesAddDeviceWebElements(NetworkDevicesDevicesAddDeviceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_ip_field(self):
        """
        :return: 'IP Address' text field in the Add Device dialog
        """
        return self.weh.get_element(self.ip_field)

    def get_profile_dropdown(self):
        """
        :return: 'Profile' dropdown field in the Add Device dialog
        """
        return self.weh.get_element(self.profile_dropdown)

    def get_nickname_field(self):
        """
        :return: 'Nickname' text field in the Add Device dialog
        """
        return self.weh.get_element(self.nickname_field)

    def get_status_only_checkbox(self):
        """
        :return: 'Poll Status Only' checkbox in the Add Device dialog
        """
        return self.weh.get_element(self.status_only_checkbox)

    def get_ok_button(self):
        """
        :return: 'OK' button in the Add Device dialog
        """
        return self.weh.get_element(self.ok_button)

    def get_close_button(self):
        """
        :return: 'Close' button in the Add Device dialog
        """
        return self.weh.get_element(self.close_button)
