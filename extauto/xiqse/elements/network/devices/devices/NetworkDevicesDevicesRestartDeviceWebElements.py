from extauto.common.WebElementHandler import WebElementHandler
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesRestartDeviceWebElementsDefinitions import NetworkDevicesDevicesRestartDeviceWebElementsDefinitions


class NetworkDevicesDevicesRestartDeviceWebElements(NetworkDevicesDevicesRestartDeviceWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()
        self.xiqse_table = XIQSE_CommonTable()

    def get_start_restart_button_item(self):
        """
        :return: Start button on Restart Device dialog
        """
        return self.weh.get_element(self.start_restart_button_item)

    def get_start_restart_yes_button(self):
        """
        :return: Yes button to begin switch restart
        """
        return self.weh.get_element(self.start_restart_yes_button)

    def get_restart_operation_complete(self):
        """
        :return: load restart operation completed if displayed, else None
        """
        return self.weh.get_element(self.restart_operation_complete)

    def get_restart_device_close_button(self):
        """
        :return: closes restart device dialog
        """
        return self.weh.get_element(self.restart_devices_close_button)
