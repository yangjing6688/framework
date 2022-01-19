from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.analytics.configuration.AnalyticsConfigurationAddEngineWebElements import AnalyticsConfigurationAddEngineWebElements


class XIQSE_AnalyticsConfigurationAddEngine(AnalyticsConfigurationAddEngineWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_add_analytics_engine_dialog_set_ip(self, the_value):
        """
         - This keyword sets the IP Address value in the Add Application Analytics Engine dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Analytics Engine Dialog Set IP  ${IP}``

        :param the_value:  IP address value to enter in the Add Application Analytics Engine dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        ip_field = self.get_engine_ip_field()
        if ip_field:
            self.utils.print_info(f"Entering IP Address {the_value}")
            self.auto_actions.send_keys(ip_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Could not find IP Address field in Add Application Analytics Engine dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_analytics_engine_dialog_set_name(self, the_value):
        """
         - This keyword sets the Name value in the Add Application Analytics Engine dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Analytics Engine Dialog Set Name  ${IP}``

        :param the_value:  Name value to enter in the Add Application Analytics Engine dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        name_field = self.get_engine_name_field()
        if name_field:
            self.utils.print_info(f"Entering Name {the_value}")
            self.auto_actions.send_keys(name_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Name field in Add Application Analytics Engine dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_analytics_engine_dialog_set_profile(self, the_value):
        """
         - This keyword sets the Profile value in the Add Application Analytics Engine dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Analytics Engine Dialog Set Profile  ${DEVICE_PROFILE}``

        :param the_value:  Profile value to enter in the Add Application Analytics Engine dialog
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_engine_profile_dropdown()
        if the_field:
            self.utils.print_info("Clicking the SNMP Profile drop down to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Profiles count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the SNMP Profile drop down")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the SNMP Profile drop down")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the SNMP Profile drop down items")
                self.screen.save_screen_shot()

                # Click the drop down again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the SNMP Profile dropdown in the Add Engine dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_engine_dialog_click_ok(self):
        """
            - This keyword clicks OK in the Add Application Analytics Engine dialog.
            - It is assumed the dialog is already opened.
            - Keyword Usage
             - ``XIQSE Add Engine Dialog Click OK``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        ok_btn = self.get_add_engine_ok_button()
        if ok_btn:
            ok_disabled = ok_btn.get_attribute("aria-disabled")
            if ok_disabled and ok_disabled == "true":
                ip_in_use = False

                # If button is disabled, see if it's because the engine IP already exists
                self.utils.print_info("OK button is disabled")
                ip_field = self.get_engine_ip_field()
                if ip_field:
                    ip_qtip = ip_field.get_attribute("data-errorqtip")
                    if ip_qtip:
                        self.utils.print_info(f"IP Address Field Error Message: '{ip_qtip}'")
                        if "already in use" in ip_qtip:
                            ip_in_use = True
                            ret_val = 1  # Engine IP already exists so this is not an error
                            self.utils.print_info("Engine IP already exists")
                            self.xiqse_add_engine_dialog_click_cancel()
                if not ip_in_use:
                    # The disabled OK button was not due to the engine IP already being in use, so check the Name field
                    name_field = self.get_engine_name_field()
                    if name_field:
                        name_qtip = name_field.get_attribute("data-errorqtip")
                        if name_qtip:
                            self.utils.print_info(f"Name Field Error Message: '{name_qtip}'")
                            if "already in use" in name_qtip:
                                ret_val = -1  # Engine name already exists so this is an error (might have an unexpected IP)
                                self.utils.print_info("Engine name already exists")
                                self.xiqse_add_engine_dialog_click_cancel()
            else:
                self.utils.print_info("Clicking OK button")
                self.auto_actions.click(ok_btn)
                ret_val = 1
        else:
            self.utils.print_info("Could not find OK button in Add Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_engine_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Add Application Analytics Engine dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Add Engine Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        cancel_btn = self.get_add_engine_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Cancel button in Add Application Analytics Engine dialog")
            self.screen.save_screen_shot()

        return ret_val
