from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesSetProfileWebElements import NetworkDevicesDevicesSetProfileWebElements


class XIQSE_NetworkDevicesDevicesSetProfile(NetworkDevicesDevicesSetProfileWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_set_profile_dialog_select_profile(self, the_value):
        """
         - This keyword sets the IP Address value in the Add Device dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Device Dialog Select Profile  public_v2_Profile``

        :param the_value:  profile value to select in the Set Device Profile dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_field = self.get_profile_dropdown()
        if the_field:
            self.utils.print_info("Opening the Profile dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_div_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected profile {the_value} in the Profile dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find profile {the_value} in the Profile dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Profile dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Profile dropdown in Set Device Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_profile_dialog_click_ok(self):
        """
         - This keyword clicks OK in the Set Device Profile dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Set Profile Dialog Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        ok_btn = self.get_ok_button()
        if ok_btn:
            self.utils.print_info("Clicking OK in Set Device Profile dialog")
            self.auto_actions.click(ok_btn)
        else:
            ret_val = -1
            self.utils.print_info("Could not find OK button in Set Device Profile dialog")
            self.screen.save_screen_shot()
            self.xiqse_set_profile_dialog_click_cancel()

        return ret_val

    def xiqse_set_profile_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Set Device Profile dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Set Profile Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        cancel_btn = self.get_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel in Set Device Profile dialog")
            self.auto_actions.click(cancel_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Cancel button in Set Device Profile dialog")
            self.screen.save_screen_shot()

        return ret_val
