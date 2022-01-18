from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsAddCredWebElements import AdminProfilesSNMPCredentialsAddCredWebElements
from xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsSaveFailed import XIQSE_AdminProfilesSNMPCredentialsSaveFailed


class XIQSE_AdminProfilesSNMPCredentialsAddCred(AdminProfilesSNMPCredentialsAddCredWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.save_failed_dlg = XIQSE_AdminProfilesSNMPCredentialsSaveFailed()

    def xiqse_add_snmp_credential_dialog_set_credential_name(self, the_value):
        """
         - This keyword enters the Credential Name value in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Set Credential Name    my_snmp_cred``

        :param the_value: value to enter in the Credential Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        name_field = self.get_add_snmp_credential_dialog_name_field()
        if name_field:
            self.utils.print_info(f"Entering Credential Name '{the_value}'")
            self.auto_actions.send_keys(name_field, the_value)
        else:
            self.utils.print_info("Could not find Credential Name field in Add SNMP Credential dialog")
            ret_val = -1
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_snmp_credential_dialog_select_snmpv1(self):
        """
         - This keyword selects SNMP Version SNMPv1 in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Select SNMPv1``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_snmp_credential_dialog_select_snmp_version("SNMPv1")

    def xiqse_add_snmp_credential_dialog_select_snmpv2(self):
        """
         - This keyword selects SNMP Version SNMPv2 in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Select SNMPv2``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_snmp_credential_dialog_select_snmp_version("SNMPv2")

    def xiqse_add_snmp_credential_dialog_select_snmpv3(self):
        """
         - This keyword selects SNMP Version SNMPv3 in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Select SNMPv3``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_snmp_credential_dialog_select_snmp_version("SNMPv3")

    def xiqse_add_snmp_credential_dialog_select_snmp_version(self, the_value):
        """
         - This keyword selects the SNMP Version value in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Select SNMP Version    SNMPv1``
          - ``XIQSE Add SNMP Credential Dialog Select SNMP Version    SNMPv2``
          - ``XIQSE Add SNMP Credential Dialog Select SNMP Version    SNMPv3``

        :param the_value: value to select in the SNMP Version field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_snmp_credential_dialog_version_dropdown()
        if the_field:
            self.utils.print_info("Clicking the SNMP Version dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"SNMP Version items count is {len(the_items)}")
                self.utils.print_info("Opening the SNMP Version dropdown")
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
            self.utils.print_info("Could not find the SNMP Version dropdown in the Add SNMP Credential dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_snmp_credential_dialog_set_community_name(self, the_value):
        """
         - This keyword enters the Community Name value in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Set Community Name    public``
          - ``XIQSE Add SNMP Credential Dialog Set Community Name    private``
          - ``XIQSE Add SNMP Credential Dialog Set Community Name    ${MY_COMMUNITY}``

        :param the_value: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        comm_field = self.get_add_snmp_credential_dialog_community_field()
        if comm_field:
            self.utils.print_info(f"Entering Community Name '{the_value}'")
            self.auto_actions.send_keys(comm_field, the_value)
        else:
            self.utils.print_info("Could not find Community Name field in Add SNMP Credential dialog")
            ret_val = -1
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_snmp_credential_dialog_set_user_name(self, the_value):
        """
         - This keyword enters the User Name value in the Add SNMP Credential dialog for SNMPv3.
         - It is assumed the Add SNMP Credential dialog is open and the version is set to SNMPv3.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Set User Name    admin``

        :param the_value: value to enter in the User Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_field = self.get_add_snmp_credential_dialog_user_name_field()
        if the_field:
            self.utils.print_info(f"Entering User Name '{the_value}'")
            self.auto_actions.send_keys(the_field, the_value)
        else:
            self.utils.print_info("Could not find User Name field in Add SNMP Credential dialog")
            ret_val = -1

        return ret_val

    def xiqse_add_snmp_credential_dialog_select_authentication_type(self, the_value):
        """
         - This keyword selects the Authentication Type value in the Add SNMP Credential dialog for SNMPv3.
         - It is assumed the Add SNMP Credential dialog is open and the version is set to SNMPv3.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Select Authentication Type    None``
          - ``XIQSE Add SNMP Credential Dialog Select Authentication Type    MD5``
          - ``XIQSE Add SNMP Credential Dialog Select Authentication Type    SHA``

        :param the_value: value to select in the Authentication Type field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_snmp_credential_dialog_auth_type_dropdown()
        if the_field:
            field_hidden = the_field.get_attribute("aria-hidden")
            if field_hidden == "true":
                self.utils.print_info("Authentication Type field is not visible; make sure version is SNMPv3")
            else:
                self.utils.print_info("Clicking the Authentication Type dropdown to expand the choices")
                self.auto_actions.click(the_field)

                # Obtain the dropdown items
                the_id = self.view_el.get_dropdown_id(the_field)
                self.utils.print_debug(f"Got dropdown ID {the_id}")
                the_items = self.view_el.get_list_dropdown_items(the_id)
                if the_items:
                    self.utils.print_debug(f"Authentication Type items count is {len(the_items)}")
                    self.utils.print_info("Opening the Authentication Type dropdown")
                    if self.auto_actions.select_drop_down_options(the_items, the_value):
                        self.utils.print_info(f"Selected {the_value} in the Authentication Type dropdown")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Did not find {the_value} in the Authentication Type dropdown")
                        self.screen.save_screen_shot()

                        # Click the dropdown again to close it
                        self.auto_actions.click(the_field)
                else:
                    self.utils.print_info("Unable to get the Authentication Type dropdown items")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Authentication Type dropdown in Add SNMP Credential dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_snmp_credential_dialog_set_authentication_password(self, the_value):
        """
         - This keyword enters the Authentication Password value in the Add SNMP Credential dialog for SNMPv3.
         - It is assumed the Add SNMP Credential dialog is open, the version is set to SNMPv3, and the
         - Authentication Type is something other than "None".
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Set Authentication Password    ${PASSWORD}``

        :param the_value: value to enter in the Authentication Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_snmp_credential_dialog_auth_pwd_field()
        if the_field:
            field_hidden = the_field.get_attribute("aria-hidden")
            field_disabled = the_field.get_attribute("aria-disabled")
            if field_hidden == "true":
                self.utils.print_info("Authentication Password field is not visible; make sure version is SNMPv3")
            elif field_disabled == "true":
                self.utils.print_info(
                    "Authentication Password field is not editable; make sure Authentication Type is not 'None'")
            else:
                self.utils.print_info(f"Entering Authentication Password '{the_value}'")
                self.auto_actions.send_keys(the_field, the_value)
                ret_val = 1
        else:
            self.utils.print_info("Could not find Authentication Password field in Add SNMP Credential dialog")

        return ret_val

    def xiqse_add_snmp_credential_dialog_select_privacy_type(self, the_value):
        """
         - This keyword selects the Privacy Type value in the Add SNMP Credential dialog for SNMPv3.
         - It is assumed the Add SNMP Credential dialog is open, the version is set to SNMPv3, and the
         - Authentication Type is something other than "None".
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Select Privacy Type    None``
          - ``XIQSE Add SNMP Credential Dialog Select Privacy Type    AES``
          - ``XIQSE Add SNMP Credential Dialog Select Privacy Type    DES``

        :param the_value: value to select in the Privacy Type field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_snmp_credential_dialog_privacy_type_dropdown()
        if the_field:
            field_hidden = the_field.get_attribute("aria-hidden")
            field_disabled = the_field.get_attribute("aria-disabled")
            if field_hidden == "true":
                self.utils.print_info("Privacy Type field is not visible; make sure version is SNMPv3")
            elif field_disabled == "true":
                self.utils.print_info(
                    "Privacy Type field is not editable; make sure Authentication Type is not 'None'")
            else:
                self.utils.print_info("Clicking the Privacy Type dropdown to expand the choices")
                self.auto_actions.click(the_field)

                # Obtain the dropdown items
                the_id = self.view_el.get_dropdown_id(the_field)
                self.utils.print_debug(f"Got dropdown ID {the_id}")
                the_items = self.view_el.get_list_dropdown_items(the_id)
                if the_items:
                    item_count = len(the_items)
                    self.utils.print_debug(f"Privacy Type items count is {item_count}")
                    self.utils.print_info("Opening the Privacy Type dropdown")
                    if self.auto_actions.select_drop_down_options(the_items, the_value):
                        self.utils.print_info(f"Selected {the_value} in the Privacy Type dropdown")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Did not find {the_value} in the Privacy Type dropdown")
                        self.screen.save_screen_shot()

                        # Click the dropdown again to close it
                        self.auto_actions.click(the_field)
                else:
                    self.utils.print_info("Unable to get the Privacy Type dropdown items")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Privacy Type dropdown in Add SNMP Credential dialog")
            self.screen.save_screen_shot()


        return ret_val

    def xiqse_add_snmp_credential_dialog_set_privacy_password(self, the_value):
        """
         - This keyword enters the Privacy Password value in the Add SNMP Credential dialog for SNMPv3.
         - It is assumed the Add SNMP Credential dialog is open, the version is set to SNMPv3, and the
         - Privacy Type is something other than "None".
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Set Authentication Password    ${PASSWORD}``

        :param the_value: value to enter in the Authentication Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_snmp_credential_dialog_privacy_pwd_field()
        if the_field:
            field_hidden = the_field.get_attribute("aria-hidden")
            field_disabled = the_field.get_attribute("aria-disabled")
            if field_hidden == "true":
                self.utils.print_info("Privacy Password field is not visible; make sure version is SNMPv3")
            elif field_disabled == "true":
                self.utils.print_info(
                    "Privacy Password field is not editable; make sure Privacy Type is not 'None'")
            else:
                self.utils.print_info(f"Entering Privacy Password '{the_value}'")
                self.auto_actions.send_keys(the_field, the_value)
                ret_val = 1
        else:
            self.utils.print_info("Could not find Privacy Password field in Add SNMP Credential dialog")

        return ret_val

    def xiqse_add_snmp_credential_dialog_click_save(self):
        """
         - This keyword clicks Save in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Click Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        save_btn = self.get_add_snmp_credential_dialog_save_button()
        if save_btn:
            save_disabled = save_btn.get_attribute("aria-disabled")
            if save_disabled and save_disabled == "true":
                self.utils.print_info("Save button is disabled - clicking Cancel to close dialog")
                self.xiqse_add_snmp_credential_dialog_click_cancel()
            else:
                self.utils.print_info("Clicking Save button")
                self.auto_actions.click(save_btn)
                sleep(2)

                ret_val = self.save_failed_dlg.xiqse_save_failed_dialog_handle_failure()
                if ret_val != 1:
                    # A failure of some type occurred so we need to close the Add SNMP Credential dialog
                    self.screen.save_screen_shot()
                    self.xiqse_add_snmp_credential_dialog_click_cancel()

                    # if the failure was due to the item already existing, set the return value to 1
                    if ret_val == 2:
                        ret_val = 1
        else:
            self.utils.print_info("Could not find Save button in Add SNMP Credential dialog")
            self.screen.save_screen_shot()
            self.xiqse_add_snmp_credential_dialog_click_cancel()

        return ret_val

    def xiqse_add_snmp_credential_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Add SNMP Credential dialog.
         - It is assumed the Add SNMP Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add SNMP Credential Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.get_add_snmp_credential_dialog_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in Add SNMP Credential dialog")
            ret_val = -1
            self.screen.save_screen_shot()

        return ret_val
