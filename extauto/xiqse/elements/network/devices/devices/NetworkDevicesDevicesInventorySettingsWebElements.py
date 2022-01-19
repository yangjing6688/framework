from extauto.common.WebElementHandler import *
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesInventorySettingsWebElementsDefinitions import *
import re


class NetworkDevicesDevicesInventorySettingsWebElements(NetworkDevicesDevicesInventorySettingsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.xiqse_table = XIQSE_CommonTable()

    def get_table_rows(self):
        """
        :return: All the rows in the devices table
        """
        table_rows = self.weh.get_elements(self.devices_table_rows)
        if table_rows:
            return table_rows
        else:
            return None

#select type of transfer method for copying upgrade file from server to appliance

    def get_file_transfer_mode_dropdown(self):
        """
        - This keyword Returns the File Transfer Mode dropdown element in the Inventory Settings dialog.
        :return: File Transfer Mode dropdown element
        """

        return self.weh.get_element(self.file_transfer_mode_dropdown)

    def get_file_transfer_mode_dropdown_id(self):
        """
        :return: ID of the File Transfer Mode dropdown, else -1
        """
        el_id = -1
        the_element = self.weh.get_element(self.file_transfer_mode_dropdown)
        if the_element:
            el_id = the_element.get_attribute("id")
            el_id = re.sub('-trigger-picker', '', el_id)

        return el_id

    def get_file_transfer_mode_dropdown_items(self, the_id):
        """
        :param the_id: ID of the dropdown to return the itens of
        :return: Dropdown items of the ‘File Transfer Mode’ dropdown in the Inventory Settings dialog
        """
        el_def = {'XPATH': '//div[contains(@id, "' + the_id + '") and contains(@id, "-picker-listWrap")]/ul/li',
                  'wait_for': 10}
        return self.weh.get_elements(el_def)

    # select type of firmware download mib for downloading upgrade file from server to appliance

    def get_firmware_download_mib_dropdown(self):
        """
        - This keyword Returns the Firmware Download MIB dropdown element in the Inventory Settings dialog.
        :return: Firmware Download MIB dropdown element
        """
        return self.weh.get_element(self.firmware_download_mib_dropdown)

    def get_firmware_download_mib_dropdown_id(self):
        """
        :return: ID of the Firmware Download Mib dropdown, else -1
        """
        el_id = -1
        the_element = self.weh.get_element(self.firmware_download_mib_dropdown)
        if the_element:
            el_id = the_element.get_attribute("id")
            el_id = re.sub('-trigger-picker', '', el_id)

        return el_id

    def get_firmware_download_mib_dropdown_items(self, the_id):
        """
        :param the_id: ID of the dropdown to return the items of
        :return: Dropdown items of the ‘Firmware Download MIB’ dropdown in the Inventory Settings dialog
        """
        el_def = {'XPATH': '//div[contains(@id, "' + the_id + '") and contains(@id, "-picker-listWrap")]/ul/li',
                'wait_for': 10}
        return self.weh.get_elements(el_def)

    #Select type of Configuration Download MIB

    def get_configuration_download_mib_dropdown(self):
        """
        - This keyword Returns the Configuration Download MIB dropdown element in the Inventory Settings dialog.
        :return: Configuration Download MIB dropdown element
        """

        return self.weh.get_element(self.configuration_download_mib_dropdown)

    def get_configuration_download_mib_dropdown_id(self):
        """
        :return: ID of the Firmware Download Mib dropdown, else -1
        """
        el_id = -1
        the_element = self.weh.get_element(self.configuration_download_mib_dropdown)
        if the_element:
            el_id = the_element.get_attribute("id")
            el_id = re.sub('-trigger-picker', '', el_id)

        return el_id

    def get_configuration_download_mib_dropdown_items(self, the_id):
        """
        :param the_id: ID of the dropdown to return the items of
        :return: Dropdown items of the ‘Configuration Download MIB’ dropdown in the Inventory Settings dialog
        """
        el_def = {'XPATH': '//div[contains(@id, "' + the_id + '") and contains(@id, "-picker-listWrap")]/ul/li',
                  'wait_for': 10}
        return self.weh.get_elements(el_def)


    #select type of upgrade script

    def get_device_family_definition_filename_dropdown(self):
        """
        - This keyword returns the Device Family Definition Filename dropdown element in the Inventory Settings dialog.
        :return: Device Family Definition Filename dropdown element
        """

        return self.weh.get_element(self.device_family_definition_filename_dropdown)

    def get_device_family_definition_filename_dropdown_id(self):
        """
        :return: ID of the Device Family Definition Filename dropdown, else -1
        """
        el_id = -1
        the_element = self.weh.get_element(self.device_family_definition_filename_dropdown)
        if the_element:
            el_id = the_element.get_attribute("id")
            el_id = re.sub('-trigger-picker', '', el_id)

        return el_id

    def get_device_family_definition_filename_dropdown_items(self, the_id):
        """
        :param the_id: ID of the dropdown to return the itens of
        :return: Dropdown items of the ‘Device Family Definition Filename’ dropdown in the Inventory Settings dialog
        """
        el_def = {'XPATH': '//div[contains(@id, "' + the_id + '") and contains(@id, "-picker-listWrap")]/ul/li',
                  'wait_for': 10}
        return self.weh.get_elements(el_def)


    def get_inventory_settings_ok_button(self):
        """
        :return: OK Button on Inventory Settings Dialog
        """
        return self.weh.get_element(self.inventory_settings_ok_button)

    def get_inventory_settings_cancel_button(self):
        """
        :return: Cancel Button on Inventory Settings Dialog
        """
        return self.weh.get_element(self.inventory_settings_cancel_button)

