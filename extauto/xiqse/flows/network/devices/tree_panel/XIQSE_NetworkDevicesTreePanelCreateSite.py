from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.tree_panel.NetworkDevicesTreePanelCreateSiteWebElements import NetworkDevicesTreePanelCreateSiteWebElements

class XIQSE_NetworkDevicesTreePanelCreateSite(NetworkDevicesTreePanelCreateSiteWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_create_site_dialog_set_name(self, the_value):
        """
         - This keyword sets the Name value in the Create Site dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Create Site Set Name  MySite``

        :param the_value:  Name value to enter in the Create Site dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        name_field = self.get_name_field()
        if name_field:
            self.utils.print_info(f"Entering Name {the_value}")
            self.auto_actions.send_keys(name_field, the_value)
        else:
            self.utils.print_info("Could not find Name field in Create Site dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_create_site_dialog_click_ok(self):
        """
         - This keyword clicks the OK button in the Create Site dialog.
         - It is assumed the Create Site dialog is already open.
         - Keyword Usage
          - ``XIQSE Create Site Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        ok_btn = self.get_ok_button()
        if ok_btn:
            ok_disabled = ok_btn.get_attribute("aria-disabled")
            if ok_disabled == 'true':
                self.utils.print_info("'OK' button is disabled")
                name_field = self.get_name_field()
                name_field_error = name_field.get_attribute("data-errorqtip")
                if "already exists" in name_field_error:
                    self.utils.print_info(f"Site already exists: {name_field_error}")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Error creating site: {name_field_error}")
                    self.screen.save_screen_shot()
                self.xiqse_create_site_dialog_click_cancel()
            else:
                self.utils.print_info("Clicking 'OK' button")
                self.auto_actions.click(ok_btn)
                ret_val = 1
        else:
            self.utils.print_info("Unable to find 'OK' button")
            self.screen.save_screen_shot()
            self.xiqse_create_site_dialog_click_cancel()

        return ret_val

    def xiqse_create_site_dialog_click_cancel(self):
        """
         - This keyword clicks the Cancel button in the Create Site dialog.
         - It is assumed the Create Site dialog is already open.
         - Keyword Usage
          - ``XIQSE Create Site Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.get_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking 'Cancel' button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find 'Cancel' button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
