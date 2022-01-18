from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.admin.profiles.cli_credentials.AdminProfilesCLICredentialsAddCredWebElements import AdminProfilesCLICredentialsAddCredWebElements
from xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsSaveFailed import XIQSE_AdminProfilesCLICredentialsSaveFailed


class XIQSE_AdminProfilesCLICredentialsAddCred(AdminProfilesCLICredentialsAddCredWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.save_failed_dlg = XIQSE_AdminProfilesCLICredentialsSaveFailed()

    def xiqse_add_cli_credential_dialog_set_description(self, the_value):
        """
         - This keyword enters the Description value in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Set Description    my_cli_cred``

        :param the_value: value to enter in the Description field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_field = self.get_add_cli_credential_dialog_description_field()
        if the_field:
            self.utils.print_info(f"Entering Description '{the_value}'")
            self.auto_actions.send_keys(the_field, the_value)
        else:
            self.utils.print_info("Could not find Description field in Add CLI Credential dialog")
            ret_val = -1
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_cli_credential_dialog_set_user_name(self, the_value):
        """
         - This keyword enters the User Name value in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Set User Name    admin``

        :param the_value: value to enter in the User Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_field = self.get_add_cli_credential_dialog_user_name_field()
        if the_field:
            self.utils.print_info(f"Entering User Name '{the_value}'")
            self.auto_actions.send_keys(the_field, the_value)
        else:
            self.utils.print_info("Could not find User Name field in Add CLI Credential dialog")
            ret_val = -1
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_cli_credential_dialog_select_telnet(self):
        """
         - This keyword selects Telnet from the Type dropdown in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Select Telnet``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_cli_credential_dialog_select_type("Telnet")

    def xiqse_add_cli_credential_dialog_select_ssh(self):
        """
         - This keyword selects SSH from the Type dropdown in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Select SSH``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_add_cli_credential_dialog_select_type("SSH")

    def xiqse_add_cli_credential_dialog_select_type(self, the_value):
        """
         - This keyword selects the CLI Version value in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Select Type    Telnet``
          - ``XIQSE Add CLI Credential Dialog Select Type    SSH``

        :param the_value: value to select in the Type field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_add_cli_credential_dialog_type_dropdown()
        if the_field:
            self.utils.print_info("Clicking the Type dropdown to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Type items count is {len(the_items)}")
                self.utils.print_info("Opening the Type dropdown")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Type dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Type dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Type dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find the Type dropdown in Add CLI Credential dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_cli_credential_dialog_set_login_password(self, the_value):
        """
         - This keyword enters the Login Password value in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Set Login Password    abc123``

        :param the_value: value to enter in the Login Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_field = self.get_add_cli_credential_dialog_login_pwd_field()
        if the_field:
            self.utils.print_info(f"Entering Login Password '{the_value}'")
            self.auto_actions.send_keys(the_field, the_value)
        else:
            self.utils.print_info("Could not find Login Password field in Add CLI Credential dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_cli_credential_dialog_set_enable_password(self, the_value):
        """
         - This keyword enters the Login Password value in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Set Enable Password    abc123``

        :param the_value: value to enter in the Enable Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_field = self.get_add_cli_credential_dialog_enable_pwd_field()
        if the_field:
            self.utils.print_info(f"Entering Login Password '{the_value}'")
            self.auto_actions.send_keys(the_field, the_value)
        else:
            self.utils.print_info("Could not find Enable Password field in Add CLI Credential dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_cli_credential_dialog_set_configuration_password(self, the_value):
        """
         - This keyword enters the Configuration Password value in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Set Configuration Password    abc123``

        :param the_value: value to enter in the Configuration Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_field = self.get_add_cli_credential_dialog_config_pwd_field()
        if the_field:
            self.utils.print_info(f"Entering Configuration Password '{the_value}'")
            self.auto_actions.send_keys(the_field, the_value)
        else:
            self.utils.print_info("Could not find Configuration Password field in Add CLI Credential dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_add_cli_credential_dialog_click_save(self):
        """
         - This keyword clicks Save in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Click Save``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        save_btn = self.get_add_cli_credential_dialog_save_button()
        if save_btn:
            save_disabled = save_btn.get_attribute("aria-disabled")
            if save_disabled and save_disabled == "true":
                self.utils.print_info("Save button is disabled - clicking Cancel to close dialog")
                self.xiqse_add_cli_credential_dialog_click_cancel()
                ret_val = -1
            else:
                self.utils.print_info("Clicking Save button")
                self.auto_actions.click(save_btn)
                sleep(2)

                ret_val = self.save_failed_dlg.xiqse_save_failed_dialog_handle_failure()
                if ret_val != 1:
                    # A failure of some type occurred so we need to close the Add CLI Credential dialog
                    self.xiqse_add_cli_credential_dialog_click_cancel()

                    # if the failure was due to the item already existing, set the return value to 1
                    if ret_val == 2:
                        ret_val = 1
        else:
            self.utils.print_info("Could not find Save button in Add CLI Credential dialog")
            self.screen.save_screen_shot()
            self.xiqse_add_cli_credential_dialog_click_cancel()
            ret_val = -1

        return ret_val

    def xiqse_add_cli_credential_dialog_click_cancel(self):
        """
         - This keyword clicks Cancel in the Add CLI Credential dialog.
         - It is assumed the Add CLI Credential dialog is open.
         - Keyword Usage
          - ``XIQSE Add CLI Credential Dialog Click Cancel``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        cancel_btn = self.get_add_cli_credential_dialog_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button")
            self.auto_actions.click(cancel_btn)
        else:
            self.utils.print_info("Could not find Cancel button in Add CLI Credential dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
