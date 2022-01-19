from extauto.common.WebElementHandler import *
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesBackupConfigurationWebElementsDefinitions import *


class NetworkDevicesDevicesBackupConfigurationWebElements(NetworkDevicesDevicesBackupConfigurationWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_yes_button(self):
        """
        :return: 'Yes' button in the Backup Configuration dialog
        """
        return self.weh.get_element(self.yes_button)

    def get_no_button(self):
        """
        :return: 'No' button in the Backup Configuration dialog
        """
        return self.weh.get_element(self.no_button)

    def get_ok_button(self):
        """
        :return: 'OK' button in the Backup Configuration dialog
        """
        return self.weh.get_element(self.ok_button)