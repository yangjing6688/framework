from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesRestoreConfigurationWebElements import NetworkDevicesDevicesRestoreConfigurationWebElements


class XIQSE_NetworkDevicesDevicesRestoreConfiguration(NetworkDevicesDevicesRestoreConfigurationWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_set_restore_dialog_select_configuration(self, the_value):
        """
        - This keyword selects the configuration value in the Restore Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Set Restore Dialog Select Configuration  Site Engine Archive``

        :param the_value:  configuration value to select in the Restore Configuration dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # This dropdown is not opened by clicking on the input area, so need to get the dropdown trigger arrow
        the_field_trigger = self.get_restore_dropdown_trigger()
        if the_field_trigger:
            self.utils.print_info("Opening the Configuration dropdown")
            self.auto_actions.click(the_field_trigger)

            # Obtain the dropdown items
            the_field = self.get_restore_dropdown()
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_div_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Configuration items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options_partial_match(the_items, the_value):
                    self.utils.print_info(f"Selected configuration {the_value} in the Configuration dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find configuration {the_value} in the Configuration dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field_trigger)
            else:
                self.utils.print_info("Unable to get the Configuration dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field_trigger)
        else:
            self.utils.print_info("Could not find the Configuration dropdown in Restore Configuration dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_restore_dialog_click_start(self):
        """
        - This keyword clicks Start in the Restore Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Set Restore Configuration Dialog Click  Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        start_btn = self.get_start_button()
        if start_btn:
            self.utils.print_info("Clicking Start in Restore Configuration dialog")
            self.auto_actions.click(start_btn)
            ret_val = 1
        else:
            ret_val = -1
            self.utils.print_info("Could not find Start button in Restore Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_confirm_restore_dialog_click_cancel(self):
        """
        - This keyword clicks Cancel in the Restore Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Set Restore Configuration Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        cancel_btn = self.get_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel in Restore Configuration dialog")
            self.auto_actions.click(cancel_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Cancel button in Restore Configuration dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_restore_dialog_click_yes(self):
        """
        - This keyword clicks Yes in the Confirm Change dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Set Restore Configuration Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        yes_btn = self.get_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking Yes in Restore Configuration dialog")
            self.auto_actions.click(yes_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Yes button in Restore Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_confirm_restore_dialog_click_no(self):
        """
        - This keyword clicks No in the Restore Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Set Restore Configuration Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        no_btn = self.get_no_button()
        if no_btn:
            self.utils.print_info("Clicking No in Restore Configuration dialog")
            self.auto_actions.click(no_btn)
            ret_val = 1
        else:
            ret_val = -1
            self.utils.print_info("Could not find No button in Restore Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_confirm_restore_dialog_click_ok(self):
        """
        - This keyword clicks OK in the Restore Configuration dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Confirm Restore Configuration Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        ok_btn = self.get_ok_button()
        if ok_btn:
            self.utils.print_info("Clicking 'OK' in Restore Configuration dialog")
            self.auto_actions.click(ok_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'OK' button in Restore Configuration dialog")
            self.screen.save_screen_shot()
        return ret_val