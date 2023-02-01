from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesRestoreConfigurationWebElementsDefinitions import NetworkDevicesDevicesRestoreConfigurationWebElementsDefinitions


class NetworkDevicesDevicesRestoreConfigurationWebElements(NetworkDevicesDevicesRestoreConfigurationWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_restore_dropdown_trigger(self):
        """
        :return: 'Configuration' dropdown trigger arrow in the Restore Configuration dialog
        """
        return self.weh.get_element(self.restore_dropdown_trigger)

    def get_restore_dropdown(self):
        """
        :return: 'Configuration' dropdown field in the Restore Configuration dialog
        """
        return self.weh.get_element(self.restore_dropdown)

    def get_start_button(self):
        """
        :return: 'Start' button in the Restore Configuration dialog
        """
        return self.weh.get_element(self.start_btn)

    def get_cancel_button(self):
        """
        :return: 'Cancel' button in the Restore Configuration dialog
        """
        return self.weh.get_element(self.cancel_btn)

    def get_yes_button(self):
        """
        :return: 'Yes' button in the Confirm Change dialog
        """
        return self.weh.get_element(self.yes_btn)

    def get_no_button(self):
        """
        :return: 'No' button in the Confirm Change dialog
        """
        return self.weh.get_element(self.no_btn)

    def get_ok_button(self):
        """
        :return: 'OK' button in the Confirm Change dialog
        """
        return self.weh.get_element(self.ok_btn)