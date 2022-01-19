from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesInventorySettingsWebElements import NetworkDevicesDevicesInventorySettingsWebElements


class XIQSE_NetworkDevicesDevicesInventorySettings(NetworkDevicesDevicesInventorySettingsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()

    def xiqse_inventory_settings_dialog_select_file_transfer_mode(self, the_value):
        """
         - This keyword selects the File Transfer Mode in the Inventory Settings dialog.
         - It is assumed the Inventory Settings dialog is already open.
         - Keyword Usage
          - ``XIQSE Inventory Settings Dialog Select File Transfer Mode    TFTP``
          - ``XIQSE Inventory Settings Dialog Select File Transfer Mode    SCP``
          - ``XIQSE Inventory Settings Dialog Select File Transfer Mode    FTP``
          - ``XIQSE Inventory Settings Dialog Select File Transfer Mode    SFTP``

        :param the_value: value to select in the File Transfer Mode dropdown (TFTP,SCP,FTP,SFTP)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_file_transfer_mode_dropdown()
        if the_field:
            self.utils.print_info("Opening the File Transfer Mode dropdown")
            self.auto_actions.click(the_field)
            the_id = self.get_file_transfer_mode_dropdown_id()
            self.utils.print_debug(f"GOT ID FOR ELEMENT: '{the_id}'")
            the_items = self.get_file_transfer_mode_dropdown_items(the_id)
            if the_items:
                item_count = len(the_items)
                self.utils.print_debug(f"File Transfer Mode items count is {item_count}")
                if self.auto_actions.select_drop_down_options_partial_match(the_items, the_value):
                    self.utils.print_info(f"Selected {type} in the File Transfer Mode dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {type} in the File Transfer Mode dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the File Transfer Mode dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the File Transfer Mode dropdown in the Inventory Settings dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_inventory_settings_dialog_select_device_family_definition_filename(self, the_value):
        """
         - This keyword selects the File Definition Family Name in the Inventory Settings dialog.
         - It is assumed the Inventory Settings dialog is already open.
         - Keyword Usage
          - ``XIQSE Inventory Settings Dialog Select Device Family Definition Filename   Extreme Control Upgrade - SCP``

        :param the_value: value to select in the Device Family Definition Filename dropdown
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_device_family_definition_filename_dropdown()
        if the_field:
            self.utils.print_info("Opening the Device Family Definition Filename dropdown")
            self.auto_actions.click(the_field)
            the_id = self.get_device_family_definition_filename_dropdown_id()
            self.utils.print_debug(f"GOT ID FOR ELEMENT: '{the_id}'")
            the_items = self.get_device_family_definition_filename_dropdown_items(the_id)
            if the_items:
                item_count = len(the_items)
                self.utils.print_debug(f"Device Family Definition Filename items count is {item_count}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {type} in the Device Family Definition Filename dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {type} in the Device Family Definition Filename dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Device Family Definition Filename dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info(
                "Could not find the Device Family Definition Filename dropdown in the Inventory Settings dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_inventory_settings_dialog_select_firmware_download_mib(self, the_value):
        """
         - This keyword selects the Firmware Download MIB type in the Inventory Settings dialog.
         - It is assumed the Inventory Settings dialog is already open.
         - Keyword Usage
          - ``XIQSE Firmware Download MIB Type    Disabled``
          - ``XIQSE Firmware Download MIB Type    Script```

        :param the_value: value to select in the Firmware Download MIB dropdown (Disabled,Script)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_firmware_download_mib_dropdown()
        if the_field:
            self.utils.print_info("Opening the Firmware Download MIB dropdown")
            self.auto_actions.click(the_field)
            the_id = self.get_firmware_download_mib_dropdown_id()
            self.utils.print_debug(f"GOT ID FOR ELEMENT: '{the_id}'")
            the_items = self.get_firmware_download_mib_dropdown_items(the_id)
            if the_items:
                item_count = len(the_items)
                self.utils.print_debug(f"Firmware Download MIB items count is {item_count}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {type} in the Firmware Download MIB dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {type} in the Firmware Download MIB dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Firmware Download MIB dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Firmware Download MIB dropdown in the Inventory Settings dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_inventory_settings_dialog_select_configuration_download_mib(self, the_value):
        """
         - This keyword selects the Configuration Download MIB type in the Inventory Settings dialog.
         - It is assumed the Inventory Settings dialog is already open.
         - Keyword Usage
          - ``XIQSE Configuration Download MIB Type    Disabled``
          - ``XIQSE Configuration Download MIB Type    Script```

        :param the_value: value to select in the Configuration Download MIB dropdown (Disabled,Script)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_configuration_download_mib_dropdown()
        if the_field:
            self.utils.print_info("Opening the Configuration Download MIB dropdown")
            self.auto_actions.click(the_field)
            the_id = self.get_configuration_download_mib_dropdown_id()
            self.utils.print_debug(f"GOT ID FOR ELEMENT: '{the_id}'")
            the_items = self.get_configuration_download_mib_dropdown_items(the_id)
            if the_items:
                item_count = len(the_items)
                self.utils.print_debug(f"Configuration Download MIB items count is {item_count}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {type} in the Configuration Download MIB dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {type} in the Configuration Download MIB dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Configuration Download MIB dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Configuration Download MIB dropdown in the Inventory Settings dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_click_inventory_settings_ok_button(self):
        """
         - Clicks the OK button on the Inventory Settings Dialog to accept choices
         - It assumes the Inventory Settings dialog is already open
         - Keyword Usage
            - ``XIQSE Click Inventory Settings OK Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        ok_btn = self.get_inventory_settings_ok_button()
        if ok_btn:
            self.utils.print_info("Clicking OK button")
            self.auto_actions.click(ok_btn)
        else:
            self.utils.print_info("Could not find OK button in Inventory Settings")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_click_inventory_settings_cancel_button(self):
        """
         - Clicks the Cancel button for the Inventory Settings Dialog to close the dialog.
         - It assumes the Inventory Settings dialog is already open.
         - Keyword Usage
            - ``XIQSE Click Inventory Settings Cancel Button``

        :return: 1 if action was successful, else -1
        """

        ret_val = 1

        cancel_btn = self.get_inventory_settings_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in Inventory Settings dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
