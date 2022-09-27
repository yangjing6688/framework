from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from xiqse.elements.admin.options.AdminOptionsWebElements import AdminOptionsWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator


class XIQSE_AdminOptions(AdminOptionsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_nav = XIQSE_CommonNavigator()
        self.common_validation = CommonValidation()

    def xiqse_select_site_engine_general_option(self):
        """
         - This keyword selects the Site Engine - General option in the Options tree.
         - Keyword Usage
          - ``XIQSE Select Site Engine General Option``

        :return: 1 if selection was made, else -1
        """
        ret_val = -1
        sleep(2)
        tree_option = self.get_site_engine_general_option()
        if tree_option:
            self.utils.print_info("Selecting the Site Engine General option in the tree")
            self.auto_actions.click(tree_option)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Site Engine General option in the tree")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_xiq_connection_option(self):
        """
         - This keyword selects the XIQ Connection option in the Options tree.
         - Keyword Usage
          - ``XIQSE Select XIQ Connection Option``

        :return: 1 if selection was made, else -1
        """
        ret_val = -1
        sleep(2)
        tree_option = self.get_xiq_connection_option()
        if tree_option:
            self.utils.print_info("Selecting the XIQ Connection option in the tree")
            self.auto_actions.click(tree_option)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the XIQ Connection option in the tree")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_alarm_event_option(self):
        """
        - This keyword selects the Alam/Event Logs and Tables option in the options tree.
        - Keyword Usage
         - ``XIQSE Select Alarm Event Option``
        :return:  1 if selection was made, else -1
        """
        ret_val = -1
        sleep(2)
        tree_option = self.get_alarm_event_option()
        if tree_option:
            self.utils.print_info("Selecting the Alarm/Event option in the tree")
            self.auto_actions.click(tree_option)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Alarm/Event option in the tree")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_select_web_server_option(self):
        """
         - This keyword selects the Web Server option in the Options tree.
         - Keyword Usage
          - ``XIQSE Select Web Server Option``

        :return: 1 if selection was made, else -1
        """
        ret_val = -1
        sleep(2)
        tree_option = self.get_web_server_option()
        if tree_option:
            self.utils.print_info("Selecting the Web Server option in the tree")
            self.auto_actions.click(tree_option)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Web Server option in the tree")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_save_options(self):
        """
         - This keyword clicks the Save button to save any unsaved options.
           If the button is disabled, there are no unsaved options and this is a no-op.
           It is assumed the view is already navigated to the Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Save Options``

        :return: 1 if options were saved (or button is disabled/no changes to save), else -1
        """
        ret_val = -1
        save_button = self.get_save_options_button()
        if save_button:
            save_disabled = save_button.get_attribute("aria-disabled")
            self.utils.print_debug(f"Save Disabled Value: '{save_disabled}'")
            if save_disabled == 'false':
                self.utils.print_info("Clicking Save button")
                self.auto_actions.click(save_button)
                sleep(2)
                confirm_save = self.get_confirm_save_warning_dialog()
                if confirm_save:
                    yes_btn = self.get_confirm_save_yes_btn()
                    if yes_btn:
                        self.utils.print_info("Clicking Yes button in Save Warning dialog")
                        self.auto_actions.click(yes_btn)
                    else:
                        self.utils.print_info("Could not find Yes button in Save Warning dialog")
                        self.screen.save_screen_shot()
            else:
                self.utils.print_info("Save button disabled - nothing to save")
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find Save button on Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_options(self):
        """
         - This keyword clicks the Restore Defaults button on the Options page.
           If the button is disabled, the options are already at the defaults and this is a no-op.
           It is assumed the view is already navigated to the Administration> Options tab and to
           the specific option to be restored.
         - Keyword Usage
          - ``XIQSE Restore Default Options``

        :return: 1 if options were restored to defaults (or button is disabled), else -1
        """
        ret_val = -1
        defaults_button = self.get_restore_default_options_button()
        if defaults_button:
            btn_disabled = defaults_button.get_attribute("aria-disabled")
            self.utils.print_debug(f"Restore Defaults Disabled Value: '{btn_disabled}'")
            if btn_disabled == 'false':
                self.utils.print_info("Clicking Restore Defaults button")
                self.auto_actions.click(defaults_button)
            else:
                self.utils.print_info("Restore Defaults button disabled - already at defaults")
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find Restore Defaults button on Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_options_and_save(self):
        """
         - This keyword clicks the Restore Defaults button on the Options page and then clicks Save.
           If the button is disabled, the options are already at the defaults and this is a no-op.
           It is assumed the view is already navigated to the Administration> Options tab and to
           the specific option to be restored.
         - Keyword Usage
          - ``XIQSE Restore Default Options and Save``

        :return: 1 if options were restored to defaults (or button is disabled), else -1
        """
        # Click the Restore Defaults button
        defaults_result = self.xiqse_restore_default_options()

        # Save Changes
        save_result = self.xiqse_save_options()

        if defaults_result == -1 or save_result == -1:
            self.utils.print_info("Action was not successful")
            self.screen.save_screen_shot()
            ret_val = -1
        else:
            self.utils.print_info("Action was successful")
            ret_val = 1

        return ret_val

    def xiqse_reset_options(self):
        """
         - This keyword clicks the Reset button on the Options page.
           If the button is disabled, the options are already at the last-saved values and this is a no-op.
           It is assumed the view is already navigated to the Administration> Options tab and to
           the specific option to be reset.
         - Keyword Usage
          - ``XIQSE Reset Options``

        :return: 1 if options were restored to defaults (or button is disabled), else -1
        """
        ret_val = -1
        reset_button = self.get_reset_options_button()
        if reset_button:
            btn_disabled = reset_button.get_attribute("aria-disabled")
            self.utils.print_debug(f"Reset Disabled Value: '{btn_disabled}'")
            if btn_disabled == 'false':
                self.utils.print_info("Clicking Reset button")
                self.auto_actions.click(reset_button)
            else:
                self.utils.print_info("Reset button disabled - already at last-saved values")
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find Reset button on Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_xiq_connection_enable_sharing_option(self, expected_value="true"):
        """
         - This keyword confirms the expected value of the Enable Sharing field for the XIQ Connection option.
         - It is assumed the view is already navigated to the XIQ Connection option on the Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Confirm XIQ Connection Enable Sharing Option  true``
            ``XIQSE Confirm XIQ Connection Enable Sharing Option  false``

        :param expected_value: indicates whether the Enable Sharing option is expected to be selected (true) or not (false)
        :return: 1 if value is at expected value, else -1
        """
        ret_val = -1
        the_field = self.get_xiq_connection_enable_sharing_checkbox()
        if the_field:
            is_checked = the_field.get_attribute("checked")
            self.utils.print_debug(f"Current checkbox checked attribute is '{is_checked}'")
            current_val = "false"
            if is_checked and (is_checked == "true" or is_checked == "checked"):
                current_val = "true"
            self.utils.print_debug(f"Current checkbox checked value is '{current_val}'")
            if current_val == expected_value:
                self.utils.print_info(f"Enable Sharing checkbox is at expected value '{expected_value}'")
                ret_val = 1
            else:
                self.utils.print_info(f"Enable Sharing checkbox is not at expected value '{expected_value}'")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Enable Sharing checkbox")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_xiq_connection_enable_sharing_option(self, value="true"):
        """
         - This keyword sets the value of the Enable Sharing field for the XIQ Connection option.
         - It is assumed the view is already navigated to the XIQ Connection option on the Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Set XIQ Connection Enable Sharing Option  true``
            ``XIQSE Set XIQ Connection Enable Sharing Option  false``

        :param value: indicates whether to select (true) or deselect (false) the Enable Sharing option
        :return: 1 if value was set, else -1
        """
        ret_val = -1
        set_option = self.get_xiq_connection_enable_sharing_checkbox()
        if set_option:
            self.utils.print_info(f"Setting the checkbox to {value}")
            is_checked = set_option.get_attribute("checked")
            self.utils.print_info(f"Current checkbox checked attribute is '{is_checked}'")
            current_val = "false"
            if is_checked and (is_checked == "true" or is_checked == "checked"):
                current_val = "true"
            self.utils.print_info(f"Current checkbox checked value is '{current_val}'")
            if current_val != value:
                self.utils.print_info("Clicking the Enable Sharing checkbox to toggle the value")
                self.auto_actions.click(set_option)
            else:
                self.utils.print_info(f"Enable Sharing checkbox is already at correct value '{value}'")
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Enable Sharing checkbox")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_xiq_connection_option_and_save(self, enable="true"):
        """
         - This keyword sets the value of the XIQ Connection option and saves the changes
         - Keyword Usage
            ``XIQSE Set XIQ Connection Option and Save  true``
            ``XIQSE Set XIQ Connection Option and Save  false``

        :param enable: indicates whether to select (true) or deselect (false) the Enable Sharing option
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_xiq_connection_option():
                # Enable Sharing
                enable_set = self.xiqse_set_xiq_connection_enable_sharing_option(enable)
                sleep(2)

                # Save Changes
                save_result = self.xiqse_save_options()

                if enable_set == -1 or save_result == -1:
                    self.utils.print_info("Action was not successful")
                    self.screen.save_screen_shot()
                    ret_val = -1
                else:
                    self.utils.print_info("Action was successful")
                    ret_val = 1
            else:
                self.utils.print_info("Unable to find the XIQ Connection option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_disable_xiq_connection_sharing_and_save(self):
        """
         - This keyword deselects the XIQ Connection "Enable Sharing" option and saves the changes
         - Keyword Usage
          - ``XIQSE Disable XIQ Connection Sharing and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_xiq_connection_option():
                # Disable Sharing
                enable_set = self.xiqse_set_xiq_connection_enable_sharing_option("false")
                sleep(2)

                # Save Changes
                save_result = self.xiqse_save_options()

                if enable_set == -1 or save_result == -1:
                    self.utils.print_info("Action was not successful")
                    self.screen.save_screen_shot()
                    ret_val = -1
                else:
                    self.utils.print_info("Action was successful")
                    ret_val = 1
            else:
                self.utils.print_info("Unable to find the XIQ Connection option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_enable_xiq_connection_sharing_and_save(self):
        """
         - This keyword selects the XIQ Connection "Enable Sharing" option and saves the changes
         - Keyword Usage
          - ``XIQSE Enable XIQ Connection Sharing and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_xiq_connection_option():
                # Enable Sharing
                enable_set = self.xiqse_set_xiq_connection_enable_sharing_option("true")
                sleep(2)

                # Save Changes
                save_result = self.xiqse_save_options()

                if enable_set == -1 or save_result == -1:
                    self.utils.print_info("Action was not successful")
                    self.screen.save_screen_shot()
                    ret_val = -1
                else:
                    self.utils.print_info("Action was successful")
                    ret_val = 1
            else:
                self.utils.print_info("Unable to find the XIQ Connection option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_xiq_connection_options_and_save(self):
        """
         - This keyword restores the default values of the XIQ Connection options and saves the changes
         - Keyword Usage
          - ``XIQSE Restore Default XIQ Connection Options and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_xiq_connection_option():
                ret_val = self.xiqse_restore_default_options_and_save()
            else:
                self.utils.print_info("Unable to find the XIQ Connection option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def get_xiqse_serial_number_label_value(self):
        """
         - This keyword returns the XIQ-SE serial number, found on the XIQ Connection options page.
         - It is assumed the view is already navigated to the XIQ Connection option on the Administration> Options tab.
         - Keyword Usage
          - ``Get XIQSE Serial Number Label Value``

        :return: XIQ-SE serial number, if found;  else, empty string
        """
        ret_val = ""
        the_label = self.get_xiqse_serial_number_label()
        if the_label:
            label_text = the_label.text
            if label_text:
                self.utils.print_info(f"Label text is {label_text}")
                # Split the string to get the serial number component
                text_lines = label_text.splitlines()
                prefix, serial_number = text_lines[0].split(":")
                self.utils.print_debug(f"Prefix is '{prefix}'")
                self.utils.print_info(f"Serial Number is '{serial_number.strip()}'")
                ret_val = serial_number.strip()
            else:
                self.utils.print_info("Unable to obtain the XIQ-SE Serial Number label text")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the XIQ-SE Serial Number label")
            self.screen.save_screen_shot()

        return ret_val

    def get_xiqse_serial_number(self):
        """
         - This keyword navigates to the XIQ Connection option on the Administration> Options tab and
         - returns the XIQ-SE serial number.
         - Keyword Usage
          - ``Get XIQSE Serial Number``

        :return: XIQ-SE serial number, if found;  else, -1
        """
        ret_val = ""
        self.utils.print_info("Selecting Administration> Options Tab...")
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_xiq_connection_option():
                # Get the XIQ-SE Serial Number label value
                sleep(2)
                ret_val = self.get_xiqse_serial_number_label_value()
            else:
                self.utils.print_info("Unable to find the XIQ Connection option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_web_server_session_timeout_value(self, value="20"):
        """
         - This keyword sets the Timeout value for the Web Server HTTP Session Timeout option.
         - It is assumed the view is already navigated to the Web Server option on the Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Set Web Server Session Timeout Value  20``
          - ``XIQSE Set Web Server Session Timeout Value  7``

        :param value: Value to enter in the HTTP Session Timeout option field
        :return: 1 if value was set, else -1
        """
        ret_val = -1
        set_option = self.get_web_server_session_timeout_value()
        if set_option:
            self.utils.print_info(f"Setting the Timeout value to {value}")
            self.auto_actions.send_keys(set_option, value)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Session Timeout value field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_web_server_session_timeout_units(self, units="min(s)"):
        """
         - This keyword sets the Timeout units for the Web Server HTTP Session Timeout option.
         - It is assumed the view is already navigated to the Web Server option on the Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Set Web Server Session Timeout Units  min(s)``
          - ``XIQSE Set Web Server Session Timeout Units  hr(s)``
          - ``XIQSE Set Web Server Session Timeout Units  day(s)``

        :param units: time units to select for the HTTP Session Timeout option (min(s), hr(s), day(s))
        :return: 1 if value was set, else -1
        """
        ret_val = -1

        the_field = self.get_web_server_session_timeout_units_dropdown()
        if the_field:
            self.utils.print_info("Opening the Session Timeout Units dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Timeout Units items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, units):
                    self.utils.print_info(f"Selected {units} in the Timeout Units dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {units} in the Timeout Units dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Session Timeout Units dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Session Timeout units field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_event_search_scope_and_save(self, value, **kwargs):
        """
        - This keyword sets the Event Search Scope to include Client, Event and Source Host Name columns.
        - Keyword Usage
        - ``XIQSE SET EVENT SEARCH SCOPE AND SAVE   true``
        - ``XIQSE SET EVENT SEARCH SCOPE AND SAVE   false``
        :param value: true to enable the extended scoping and false to disable
        """
        ret_val = 1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_alarm_event_option():
                # enable the client event search scope
                the_button = self.get_alarm_event_search_scope_client_checkbox()
                if the_button:
                    if value.lower() == "true":
                        self.utils.print_info("Enabling 'Event Search Scope - Client' checkbox")
                        self.auto_actions.enable_check_box(the_button)
                    else:
                        self.utils.print_info("Disabling 'Event Search Scope - Client' checkbox")
                        self.auto_actions.disable_check_box(the_button)
                else:
                    msg = "Unable to find the 'Event Search Scope - Client' checkbox"
                    self.utils.print_info(msg)
                    self.screen.save_screen_shot()
                    kwargs['fail_msg'] = f"{msg}"
                    self.common_validation.failed(**kwargs)

                the_button = self.get_alarm_event_search_scope_event_checkbox()
                if the_button:
                    if value.lower() == "true":
                        self.utils.print_info("Enabling 'Event Search Scope - Event' checkbox")
                        self.auto_actions.enable_check_box(the_button)
                    else:
                        self.utils.print_info("Disabling 'Event Search Scope - Event' checkbox")
                        self.auto_actions.disable_check_box(the_button)
                else:
                    msg = "Unable to find the 'Event Search Scope - Event' checkbox"
                    self.utils.print_info(msg)
                    self.screen.save_screen_shot()
                    kwargs['fail_msg'] = f"{msg}"
                    self.common_validation.failed(**kwargs)

                the_button = self.get_alarm_event_search_scope_source_host_name_checkbox()
                if the_button:
                    if value.lower() == "true":
                        self.utils.print_info("Enabling 'Event Search Scope - Source Host Name' checkbox")
                        self.auto_actions.enable_check_box(the_button)
                    else:
                        self.utils.print_info("Disabling 'Event Search Scope - Source Host Name' checkbox")
                        self.auto_actions.disable_check_box(the_button)
                else:
                    msg = "Unable to find the 'Event Search Scope - Source Host Name' checkbox"
                    self.utils.print_info(msg)
                    self.screen.save_screen_shot()
                    kwargs['fail_msg'] = f"{msg}"
                    self.common_validation.failed(**kwargs)

                # Save Changes
                save_result = self.xiqse_save_options()
                if save_result == -1:
                    msg = "Save Event Search Scope Settings was not successful"
                    self.utils.print_info(msg)
                    self.screen.save_screen_shot()
                    kwargs['fail_msg'] = f"{msg}"
                    self.common_validation.failed(**kwargs)
                else:
                    self.utils.print_info("Save Event Search Scope Settings was successful")
            else:
                msg = "Unable to find the Alarm/Event option in the tree"
                self.utils.print_info(msg)
                self.screen.save_screen_shot()
                kwargs['fail_msg'] = f"{msg}"
                self.common_validation.failed(**kwargs)
        else:
            msg = "Unable to navigate to Administration> Options tab"
            self.utils.print_info(msg)
            self.screen.save_screen_shot()
            kwargs['fail_msg'] = f"{msg}"
            self.common_validation.failed(**kwargs)

    def xiqse_set_web_server_session_timeout_and_save(self, value="20", units="min(s)"):
        """
         - This keyword sets the value of the Web Server Session Timeout option (value and units) and saves the changes
         - Keyword Usage
          - ``XIQSE Set Web Server Session Timeout and Save  20  min(s)``
            ``XIQSE Set Web Server Session Timeout and Save   8  hr(s)``
            ``XIQSE Set Web Server Session Timeout and Save   7  day(s)``

        :param value: Value to enter in the HTTP Session Timeout option field
        :param units: time units to select for the HTTP Session Timeout option (min(s), hr(s), day(s))
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_web_server_option():
                # Set Session Timeout value
                value_set = self.xiqse_set_web_server_session_timeout_value(value)
                sleep(2)

                # Set Session Timeout units
                units_set = self.xiqse_set_web_server_session_timeout_units(units)

                # Save Changes
                save_result = self.xiqse_save_options()

                if value_set == -1 or units_set == -1 or save_result == -1:
                    self.utils.print_info("Action was not successful")
                    ret_val = -1
                else:
                    self.utils.print_info("Action was successful")
                    ret_val = 1
            else:
                self.utils.print_info("Unable to find the Web Server option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_web_server_options_and_save(self):
        """
         - This keyword restores the default values of the Web Server options and saves the changes
         - Keyword Usage
          - ``XIQSE Restore Default Web Server Options and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_web_server_option():
                ret_val = self.xiqse_restore_default_options_and_save()
            else:
                self.utils.print_info("Unable to find the Web Server option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_device_tree_name_format(self, value="IP Address"):
        """
         - This keyword sets the Device Tree Name Format value for the Site Engine - General option.
         - It is assumed the view is already navigated to the Site Engine - General option on the
         - Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Set Device Tree Name Format Value    IP Address``
          - ``XIQSE Set Device Tree Name Format Value    Nickname``
          - ``XIQSE Set Device Tree Name Format Value    System Name``

        :param value: value to select in the Device Tree Name Format dropdown field
        :return: 1 if value was set, else -1
        """
        ret_val = -1

        # This dropdown is not opened by clicking on the input area, so need to get the dropdown trigger arrow
        the_field_trigger = self.get_device_tree_name_format_dropdown_trigger()
        if the_field_trigger:
            self.utils.print_info("Opening the Device Tree Name Format dropdown")
            self.auto_actions.click(the_field_trigger)

            # Obtain the dropdown items
            the_field = self.get_device_tree_name_format_dropdown()
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Device Tree Name Format items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, value):
                    self.utils.print_info(f"Selected {value} in the Device Tree Name Format dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {value} in the Device Tree Name Format dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field_trigger)
            else:
                self.utils.print_info("Unable to get the Device Tree Name Format dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field_trigger)
        else:
            self.utils.print_info("Unable to find the Device Tree Name Format field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_device_tree_name_format_and_save(self, value="IP Address"):
        """
         - This keyword sets the value of the Site Engine - General's Device Tree Name Format option
         - and saves the changes
         - Keyword Usage
          - ``XIQSE Set Device Tree Name Format and Save  IP Address``
          - ``XIQSE Set Device Tree Name Format and Save  Nickname``
          - ``XIQSE Set Device Tree Name Format and Save  System Name``

        :param value: value to select in the Device Tree Name Format dropdown field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_site_engine_general_option():
                # Set Device Tree Name Format value
                value_set = self.xiqse_set_device_tree_name_format(value)
                sleep(2)

                # Save Changes
                save_result = self.xiqse_save_options()

                if value_set == -1 or save_result == -1:
                    self.utils.print_info("Action was not successful")
                    self.screen.save_screen_shot()
                    ret_val = -1
                else:
                    self.utils.print_info("Action was successful")
                    ret_val = 1
            else:
                self.utils.print_info("Unable to find the Site Engine - General option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_site_engine_general_options_and_save(self):
        """
         - This keyword restores the default values of the Site Engine - General options and saves the changes
         - Keyword Usage
          - ``XIQSE Restore Default Site Engine General Options and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_site_engine_general_option():
                ret_val = self.xiqse_restore_default_options_and_save()
            else:
                self.utils.print_info("Unable to find the Site Engine - General option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_inventory_manager_options_and_save(self):
        """
         - This keyword restores the default values of the Inventory Manager options and saves the changes
         - Keyword Usage
          - ``XIQSE Restore Default Inventory Manager Options and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_inventory_manager_option():
                ret_val = self.xiqse_restore_default_options_and_save()
            else:
                self.utils.print_info("Unable to find the Inventory Manager option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_inventory_manager_option(self):
        """
        - This keyword selects the Inventory Manager option in the Administration> Options tree.
        - Keyword Usage
        - ``XIQSE Select Inventory Manager Option``

        :return: 1 if selection was made, else -1
        """
        ret_val = -1
        sleep(2)
        tree_option = self.get_inventory_manager_option()
        if tree_option:
            self.utils.print_info("Selecting the Inventory Manager option in the tree")
            self.auto_actions.click(tree_option)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Inventory Manager option in the tree")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_scp_login_information_anonymous(self, value):
        """
        - This keyword sets the 'Anonymous' checkbox in the Inventory Manager> File Transfer> SCP Server Properties section
        - It is assumed the view is already navigated to the Inventory Manager panel.
        - Keyword Usage
        - ``XIQSE Set SCP Login Information Anonymous  true``
        - ``XIQSE Set SCP Login Information Anonymous  false``

        :param value:  Indicates whether to enable or disable the checkbox; default is "true"
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_inventory_manager_option():
            the_button = self.get_scp_login_information_anonymous_checkbox()
            if the_button:
                if value.lower() == "true":
                    self.utils.print_info("Enabling 'Anonymous' checkbox")
                    self.auto_actions.enable_check_box(the_button)
                else:
                    self.utils.print_info("Disabling 'Anonymous' checkbox")
                    self.auto_actions.disable_check_box(the_button)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find the 'Anonymous' checkbox")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_scp_login_information_username(self, the_val):
        """
        - This keyword enters the Username value in the Inventory Manager> File Transfer> SCP Server Properties section
        - It is assumed the view is already navigated to the Inventory Manager panel.
        - Keyword Usage
        - ``XIQSE Set SCP Login Information Username  ${username}``

        :param the_val: A valid XIQSE username
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        username_field = self.get_scp_login_information_username()
        if username_field:
            self.utils.print_info(f"Entering Username value '{the_val}'")
            self.auto_actions.send_keys(username_field, the_val)
            ret_val = 1
        else:
            self.utils.print_info("Could not find the Username field in the SCP Server Properties dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_scp_login_information_password(self, the_val):
        """
        - This keyword enters the Password value in the Inventory Manager> File Transfer> SCP Server Properties section
        - It is assumed the view is already navigated to the Inventory Manager panel.
        - Keyword Usage
        - ``XIQSE Set SCP Login Information Password  ${password}``

        :param the_val: The password for the specified user
        :return: 1 if action was successful, else -1
        """

        ret_val = -1

        password_field = self.get_scp_login_information_password()
        if password_field:
            self.utils.print_info(f"Entering Password value '{the_val}'")
            self.auto_actions.send_keys(password_field, the_val)
            ret_val = 1
        else:
            self.utils.print_info("Could not find the Password field in the SCP Server Properties dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_sftp_login_information_anonymous(self, value):
        """
        - This keyword sets the 'Anonymous' checkbox in the Inventory Manager> File Transfer> SFTP Server Properties section
        - It is assumed the view is already navigated to the Inventory Manager panel.
        - Keyword Usage
        - ``XIQSE Set SFTP Login Information Anonymous  true``
        - ``XIQSE Set SFTP Login Information Anonymous  false``

        :param value:  Indicates whether to enable or disable the checkbox; default is "true"
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_inventory_manager_option():
            the_button = self.get_sftp_login_information_anonymous_checkbox()
            if the_button:
                if value.lower() == "true":
                    self.utils.print_info("Enabling 'Anonymous' checkbox")
                    self.auto_actions.enable_check_box(the_button)
                else:
                    self.utils.print_info("Disabling 'Anonymous' checkbox")
                    self.auto_actions.disable_check_box(the_button)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find the 'Anonymous' checkbox")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_sftp_login_information_username(self, the_val):
        """
        - This keyword enters the Username value in the Inventory Manager> File Transfer> SFTP Server Properties section
        - It is assumed the view is already navigated to the Inventory Manager panel.
        - Keyword Usage
        - ``XIQSE Set SFTP Login Information Username  ${username}``

        :param the_val: A valid XIQSE username
        :return: 1 if action was successful, else -1
        """

        ret_val = -1

        username_field = self.get_sftp_login_information_username()
        if username_field:
            self.utils.print_info(f"Entering Username value '{the_val}'")
            self.auto_actions.send_keys(username_field, the_val)
            ret_val = 1
        else:
            self.utils.print_info("Could not find the Username field in the SFTP Server Properties dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_sftp_login_information_password(self, the_val):
        """
        - This keyword enters the Password value in the Inventory Manager> File Transfer> SFTP Server Properties section
        - It is assumed the view is already navigated to the Inventory Manager panel.
        - Keyword Usage
        - ``XIQSE Set SFTP Login Information Password  ${password}``

        :param the_val: The password for the specified user
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        password_field = self.get_sftp_login_information_password()
        if password_field:
            self.utils.print_info(f"Entering Password value '{the_val}'")
            self.auto_actions.send_keys(password_field, the_val)
            ret_val = 1
        else:
            self.utils.print_info("Could not find the Password field in the SFTP Server Properties dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_status_polling_option(self):
        """
        - This keyword selects the Status Polling option in the Administration> Options tree.
        - Keyword Usage
        - ``XIQSE Select Status Polling Option``

        :return: 1 if selection was made, else -1
        """
        ret_val = -1
        sleep(2)
        tree_option = self.get_status_polling_option()
        if tree_option:
            self.utils.print_info("Selecting the Status Polling option in the tree")
            self.auto_actions.click(tree_option)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Status Polling option in the tree")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_status_polling_group_2_interval_value(self, value="5"):
        """
         - This keyword sets the value of the Status Polling Group 2 Interval option.
         - It is assumed the view is already navigated to the Status Polling option on the Administration> Options tab.
         - Keyword Usage
          - ``XIQSE Set Status Polling Group 2 Interval Value  5``
          - ``XIQSE Set Status Polling Group 2 Interval Value  2``

        :param value: Value to enter in the Group 2 Interval option field
        :return: 1 if value was set, else -1
        """
        ret_val = -1
        set_option = self.get_status_polling_group_2_interval_value()
        if set_option:
            self.utils.print_info(f"Setting the Interval value to {value}")
            self.auto_actions.send_keys(set_option, value)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Group 2 Interval value field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_set_status_polling_group_2_interval_value_and_save(self, value="5"):
        """
         - This keyword sets the value of the Status Polling Group 2 Interval option and saves the changes
         - Keyword Usage
          - ``XIQSE Set Status Polling Group 2 Interval Value and Save  5``
          - ``XIQSE Set Status Polling Group 2 Interval Value and Save  2``

        :param value: Value to enter in the Group 2 Interval option field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_status_polling_option():
                # Set Session Timeout value
                value_set = self.xiqse_set_status_polling_group_2_interval_value(value)
                sleep(2)

                # Save Changes
                save_result = self.xiqse_save_options()

                if value_set == -1 or save_result == -1:
                    self.utils.print_info("Action was not successful")
                    ret_val = -1
                else:
                    self.utils.print_info("Action was successful")
                    ret_val = 1
            else:
                self.utils.print_info("Unable to find the Status Polling option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restore_default_status_polling_options_and_save(self):
        """
         - This keyword restores the default values of the Status Polling options and saves the changes
         - Keyword Usage
          - ``XIQSE Restore Default Status Polling Options and Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_nav.xiqse_navigate_to_admin_options_tab():
            if self.xiqse_select_status_polling_option():
                ret_val = self.xiqse_restore_default_options_and_save()
            else:
                self.utils.print_info("Unable to find the Status Polling option in the tree")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to Administration> Options tab")
            self.screen.save_screen_shot()

        return ret_val

