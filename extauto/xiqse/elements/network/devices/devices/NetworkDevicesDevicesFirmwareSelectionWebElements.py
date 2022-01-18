from common.WebElementHandler import *
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesFirmwareSelectionWebElementsDefinitions import *
import re


class NetworkDevicesDevicesFirmwareSelectionWebElements(NetworkDevicesDevicesFirmwareSelectionWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_firmware_images_table_rows(self):
        """
        :return: All the rows in the devices table
        """
        table_rows = self.weh.get_elements(self.firmware_images_table_rows)
        if table_rows:
            return table_rows
        else:
            return None

    def get_refresh_images_button(self):
        """
        :return: 'Refresh Images' button in the Assign Images dialog
        """
        return self.weh.get_element(self.refresh_images_button)

    def get_refresh_load_mask(self):
        """
        :return: load refresh mask if displayed, else None
        """
        elements = self.weh.get_elements(self.refresh_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_firmware_selection_ok_button(self):
        """
        :return: OK Button on Firmware Selection Dialog
        """
        return self.weh.get_element(self.firmware_selection_ok_button)

    def get_firmware_selection_cancel_button(self):
        """
        :return: Cancel Button on Firmware Selection Dialog
        """
        return self.weh.get_element(self.firmware_selection_cancel_button)