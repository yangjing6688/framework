from common.WebElementHandler import *
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesUpgradeFirmwareWebElementsDefinitions import *


class NetworkDevicesDevicesUpgradeFirmwareWebElements(NetworkDevicesDevicesUpgradeFirmwareWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_assign_firmware_images_button(self):
        """
        :return: 'Assign Firmware...' button in the Upgrade Firmware dialog
        """
        return self.weh.get_element(self.assign_firmware_images_button)

    def get_inventory_settings_button(self):
        """
        :return: 'Inventory Settings' button in the Upgrade Firmware dialog
        """
        return self.weh.get_element(self.inventory_settings_button)

    def get_upgrade_firmware_start_button(self):
        """
        :return: 'Start' button in the Upgrade Firmware dialog
        """
        return self.weh.get_element(self.upgrade_firmware_start_button)

    def get_upgrade_firmware_close_button(self):
        """
        :return: 'Close' button in the Upgrade Firmware dialog
        """
        return self.weh.get_element(self.upgrade_firmware_close_button)

    def get_begin_downloading_firmware_yes_button(self):
        """
        :return: 'Yes' button in the Downloadin Firmware dialog
        """
        return self.weh.get_element(self.begin_downloading_firmware_yes_button)

    def get_begin_downloading_firmware_no_button(self):
        """
        :return: 'No' button in the Downloading Firmware dialog
        """
        return self.weh.get_element(self.begin_downloading_firmware_no_button)

    def get_processed_devices_with_no_failures_text(self):
        """
        :return: Processed 1 of 1 devices with 0 failures
        """
        return self.weh.get_element(self.processed_upgrade_no_failures_text)
