from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.AdminProfilesAddProfileWebElements import AdminProfilesAddProfileWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.admin.profiles.XIQSE_AdminProfilesSaveFailed import XIQSE_AdminProfilesSaveFailed


class XIQSE_AdminProfilesAddProfile(AdminProfilesAddProfileWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.save_failed_dlg = XIQSE_AdminProfilesSaveFailed()

    def xiqse_add_profile_dialog_set_profile_name(self, the_value):
        """
         - This keyword enters the Profile Name value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Set Profile Name    my_profile``

        :param the_value: value to enter in the Profile Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        name_field = self.get_add_profile_dialog_name_field()
        if name_field:
            self.utils.print_info(f"Entering Profile Name '{the_value}'")
            self.auto_actions.send_keys(name_field, the_value)
        else:
            self.utils.print_info("Could not find Profile Name field in Add Profile dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_profile_dialog_select_snmpv1(self):
        """
         - This keyword selects SNMP Version SNMPv1 in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select SNMPv1``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_profile_dialog_select_snmp_version("SNMPv1")

    def xiqse_add_profile_dialog_select_snmpv2(self):
        """
         - This keyword selects SNMP Version SNMPv2 in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select SNMPv2``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_profile_dialog_select_snmp_version("SNMPv2")

    def xiqse_add_profile_dialog_select_snmpv3(self):
        """
         - This keyword selects SNMP Version SNMPv3 in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select SNMPv3``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_profile_dialog_select_snmp_version("SNMPv3")

    def xiqse_add_profile_dialog_select_snmp_version(self, the_value):
        """
         - This keyword selects the SNMP Version value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select SNMP Version    SNMPv1``
          - ``XIQSE Add Profile Dialog Select SNMP Version    SNMPv2``
          - ``XIQSE Add Profile Dialog Select SNMP Version    SNMPv3``

        :param the_value: value to select in the SNMP Version field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_version_dropdown()
        if the_field:
            self.utils.print_info("Clicking the SNMP Version dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Version items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the SNMP Version dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the SNMP Version dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the SNMP Version dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the SNMP Version dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_read(self, the_value):
        """
         - This keyword selects the Read value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Read    public_v1``

        :param the_value: value to select in the Read field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_read_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Read dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Read items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Read dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Read dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Read dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Read dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_write(self, the_value):
        """
         - This keyword selects the Write value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Write    public_v1``

        :param the_value: value to select in the Write field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_write_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Write dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Write items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Write dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Write dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Write dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Write dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_max_access(self, the_value):
        """
         - This keyword selects the Max Access value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Max Access    public_v1``

        :param the_value: value to select in the Max Access field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_max_access_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Max Access dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Max Access items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Max Access dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Max Access dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Max Access dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Max Access dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_read_security(self, the_value):
        """
         - This keyword selects the Read Security value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open and the version is SNMPv3.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Read Security   NoAuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Read Security   AuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Read Security   AuthPriv``

        :param the_value: value to select in the Read Securityfield
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_read_security_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Read Security dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_info(f"Read Security items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Read Security dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Read Security dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Read Security dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Read Security dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_write_security(self, the_value):
        """
         - This keyword selects the Write Security value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open and the version is SNMPv3.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Write Security   NoAuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Write Security   AuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Write Security   AuthPriv``

        :param the_value: value to select in the Write Security field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_write_security_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Write Security dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Write Security items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Write Security dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Write Security dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Write Security dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Write Security dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_max_security(self, the_value):
        """
         - This keyword selects the Max Security value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open and the version is SNMPv3.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select Max Security   NoAuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Max Security   AuthNoPriv``
          - ``XIQSE Add Profile Dialog Select Max Security   AuthPriv``

        :param the_value: value to select in the Max Security field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_max_security_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Max Security dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Max Security items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Max Security dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Max Security dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Max Security dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Max Security dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_select_cli(self, the_value):
        """
         - This keyword selects the CLI Credential value in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Select CLI    Default``

        :param the_value: value to select in the CLI Credential field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_profile_dialog_cli_dropdown()
        if the_field:
            self.utils.print_info("Clicking the CLI Credential dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"CLI Credentials items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the CLI Credentials dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the CLI Credentials dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the CLI Credentials dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the CLI Credentials dropdown in Add Profile dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_profile_dialog_click_save(self):
        """
         - This keyword clicks Save in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Click Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        save_btn = self.get_add_profile_dialog_save_button()
        if save_btn:
            save_disabled = save_btn.get_attribute("aria-disabled")
            if save_disabled and save_disabled == "true":
                self.utils.print_info("Save button is disabled - clicking Cancel to close dialog")
                self.xiqse_add_profile_dialog_click_cancel()
                ret_val = -1
            else:
                self.utils.print_info("Clicking Save button")
                self.auto_actions.click(save_btn)
                sleep(2)

                ret_val = self.save_failed_dlg.xiqse_save_failed_dialog_handle_failure()
                if ret_val != 1:
                    # A failure of some type occurred so we need to close the Add Profile dialog
                    self.screen.save_screen_shot()
                    self.xiqse_add_profile_dialog_click_cancel()

                    # if the failure was due to the item already existing, set the return value to 1
                    if ret_val == 2:
                        ret_val = 1
        else:
            self.utils.print_info("Could not find Save button in Add Profile dialog")
            self.screen.save_screen_shot()
            self.xiqse_add_profile_dialog_click_cancel()
            ret_val = -1

        return ret_val

    def xiqse_add_profile_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Add Profile dialog.
         - It is assumed the Add Profile dialog is open.
         - Keyword Usage
          - ``XIQSE Add Profile Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.get_add_profile_dialog_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in Add Profile dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
