from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.cli_credentials.AdminProfilesCLICredentialsWebElements import AdminProfilesCLICredentialsWebElements
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.flows.admin.profiles.XIQSE_AdminProfiles import XIQSE_AdminProfiles
from xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsAddCred import XIQSE_AdminProfilesCLICredentialsAddCred
from xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsDeleteCred import XIQSE_AdminProfilesCLICredentialsDeleteCred


class XIQSE_AdminProfilesCLICredentials(AdminProfilesCLICredentialsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_nav = XIQSE_CommonNavigator()
        self.xiqse_table = XIQSE_CommonTable()
        self.xiqse_profiles = XIQSE_AdminProfiles()
        self.add_cred_dlg = XIQSE_AdminProfilesCLICredentialsAddCred()
        self.delete_cred_dlg = XIQSE_AdminProfilesCLICredentialsDeleteCred()

    def xiqse_refresh_cli_credentials_table(self):
        """
        - Refreshes the CLI Credentials table.
        - Assumes the Administration> Profiles> CLI Credentials tab is already selected.

        :return: return 1 if the action is successful, else -1
        """

        ret_val = -1

        the_btn = self.get_cli_credentials_refresh_table_button()
        if the_btn:
            self.utils.print_info("Refreshing the CLI Credentials table")
            self.auto_actions.click(the_btn)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Refresh button for the CLI Credentials table")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_and_create_cli_credential(self, desc, user_name, type="Telnet",
                                                 login_pwd=None, enable_pwd=None, config_pwd=None):
        """
         - This keyword navigates to the Administration> Profiles> CLI Credentials tab and
         - creates a new CLI credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1``
          - ``XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  type="SSH"``
          - ``XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  login_pwd=abc123``

        :param desc: value to enter in the Description field
        :param user_name: value to enter in the User Name field
        :param type: value to select for the Type field (Telnt, SSH)
        :param login_pwd: value to enter in the Login Password field
        :param enable_pwd: value to enter in the Enable Password field
        :param config_pwd: value to enter in the Configuration Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_cli_credentials_tab():
                ret_val = self.xiqse_create_cli_credential(desc, user_name, type, login_pwd, enable_pwd, config_pwd)

        return ret_val

    def xiqse_navigate_and_select_cli_credential(self, desc):
        """
         - This keyword navigates to the Administration> Profiles> CLI Credentials tab and
         - selects an existing CLI credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Select CLI Credential  cli_cred_1``

        :param desc: name (Description column) of the CLI credential to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_cli_credentials_tab():
                ret_val = self.xiqse_select_cli_credential(desc)

        return ret_val

    def xiqse_navigate_and_delete_cli_credential(self, desc):
        """
         - This keyword navigates to the Administration> Profiles> CLI Credentials tab and
         - deletes an existing CLI credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Delete CLI Credential  cli_cred_1``

        :param desc: name (Description column) of the CLI credential to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_cli_credentials_tab():
                ret_val = self.xiqse_delete_cli_credential(desc)

        return ret_val

    def xiqse_create_cli_credential(self, desc, user_name, type="Telnet",
                                    login_pwd=None, enable_pwd=None, config_pwd=None):
        """
         - This keyword creates a new CLI credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> CLI Credentials.
         - Keyword Usage
          - ``XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1``
          - ``XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  type="SSH"``
          - ``XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  login_pwd=abc123``

        :param desc: value to enter in the Description field
        :param user_name: value to enter in the User Name field
        :param type: value to select for the Type field (Telnt, SSH)
        :param login_pwd: value to enter in the Login Password field
        :param enable_pwd: value to enter in the Enable Password field
        :param config_pwd: value to enter in the Configuration Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_add_cli_credential_button()
        if add_btn:
            self.utils.print_info("Clicking 'Add...' toolbar button to display the Add CLI Credential dialog")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Enter Description (CLI credential name)
            ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_set_description(desc)

            # Enter User Name
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_set_user_name(user_name)

            # Select Type (Telnet or SSH)
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_select_type(type)

            # Enter Login Password
            if ret_val != -1 and login_pwd:
                ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_set_login_password(login_pwd)

            # Enter Enable Password
            if ret_val != -1 and enable_pwd:
                ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_set_enable_password(enable_pwd)

            # Enter Configuration Password
            if ret_val != -1 and config_pwd:
                ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_set_configuration_password(config_pwd)

            # Click Save
            if ret_val != -1:
                sleep(2)
                ret_val = self.add_cred_dlg.xiqse_add_cli_credential_dialog_click_save()
            else:
                self.utils.print_info("Unable to complete Add CLI Credential action; closing dialog")
                self.screen.save_screen_shot()
                self.add_cred_dlg.xiqse_add_cli_credential_dialog_click_cancel()
        else:
            self.utils.print_info("Unable to find Add CLI Credential toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_delete_cli_credential(self, name):
        """
         - This keyword deletes an existing CLI credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> CLI Credentials.
         - Keyword Usage
          - ``XIQSE Delete CLI Credential  test_cred_1``

        :param name: name of the CLI credential to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_cli_credential(name):
            delete_btn = self.get_delete_cli_credential_button()
            if delete_btn:
                btn_disabled = delete_btn.get_attribute("aria-disabled")
                if btn_disabled == "true":
                    self.utils.print_info("'Delete' button is disabled")
                else:
                    self.utils.print_info("Clicking 'Delete' toolbar button")
                    self.auto_actions.click(delete_btn)
                    sleep(2)

                    # Confirm the deletion
                    ret_val = self.delete_cred_dlg.xiqse_delete_cli_credential_confirm_delete()
            else:
                self.utils.print_info("Could not find 'Delete' button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_cli_credential(self, name):
        """
        - Searches for CLI Credential matching the specified name.
        - Assumes the Administration> Profiles> CLI Credentials tab is already selected.

        :param name: Name of the CLI credential to search for
        :return: return 1 if the CLI credential is found, else -1
        """

        ret_val = -1

        sleep(2)
        self.xiqse_refresh_cli_credentials_table()
        sleep(2)

        rows = self.get_cli_credentials_table_rows()
        if rows:
            for row in rows:
                self.utils.print_debug(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                if name in row.text:
                    self.utils.print_info(f"Found row for CLI credential with name {name}")
                    ret_val = 1
                    break
            if ret_val == -1:
                self.utils.print_info(f"Did not find row for CLI credential with name {name}")
        else:
            self.utils.print_info("Could not obtain rows from CLI Credentials table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_cli_credential(self, name):
        """
         - This keyword selects an existing CLI credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> CLI Credentials.
         - Keyword Usage
          - ``XIQSE Select CLI Credential  test_cred_1``

        :param name: name of the CLI credential to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        sleep(2)
        rows = self.get_cli_credentials_table_rows()
        for row in rows:
            if name in row.text:
                self.utils.print_debug(f"Found CLI Credential {name} in row {self.xiqse_table.format_table_row(row.text)}")
                row_selected = row.get_attribute("aria-selected")
                if row_selected and row_selected == "true":
                    self.utils.print_info(f"Row for CLI Credential {name} is already selected")
                else:
                    self.utils.print_info(f"Selecting CLI Credential {name}")
                    self.auto_actions.click(row)
                ret_val = 1
                break

        if ret_val == -1:
            self.utils.print_info(f"Unable to select CLI Credential {name}")
            self.screen.save_screen_shot()

        return ret_val
