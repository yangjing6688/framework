from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.snmp_credentials.AdminProfilesSNMPCredentialsWebElements import AdminProfilesSNMPCredentialsWebElements
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.flows.admin.profiles.XIQSE_AdminProfiles import XIQSE_AdminProfiles
from xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsAddCred import XIQSE_AdminProfilesSNMPCredentialsAddCred
from xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsDeleteCred import XIQSE_AdminProfilesSNMPCredentialsDeleteCred


class XIQSE_AdminProfilesSNMPCredentials(AdminProfilesSNMPCredentialsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_nav = XIQSE_CommonNavigator()
        self.xiqse_table = XIQSE_CommonTable()
        self.xiqse_profiles = XIQSE_AdminProfiles()
        self.add_cred_dlg = XIQSE_AdminProfilesSNMPCredentialsAddCred()
        self.delete_cred_dlg = XIQSE_AdminProfilesSNMPCredentialsDeleteCred()

    def xiqse_refresh_snmp_credentials_table(self):
        """
        - Refreshes the SNMP Credentials table.
        - Assumes the Administration> Profiles> SNMP Credentials tab is already selected.

        :return: return 1 if the action is successful, else -1
        """

        ret_val = -1

        the_btn = self.get_snmp_credentials_refresh_table_button()
        if the_btn:
            self.utils.print_info("Refreshing the SNMP Credentials table")
            self.auto_actions.click(the_btn)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Refresh button for the SNMP Credentials table")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_and_create_snmp_credential(self, name, version, comm_str):
        """
         - This keyword navigates to the Administration> Profiles> SNMP Credentials tab and
         - creates a new SNMPv1 or SNMPv2 credential in XIQ-SE.
         - Please use xiqse_navigate_and_create_snmpv3_credential to create an SNMPv3 credential.
         - Keyword Usage
          - ``XIQSE Navigate and Create SNMP Credential  test_cred_1  SNMPv1  public``
          - ``XIQSE Navigate and Create SNMP Credential  test_cred_2  SNMPv2  private``

        :param name: value to enter in the Credential Name field
        :param version: value to select for the SNMP Version field (SNMPv1, SNMPv2)
        :param comm_str: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_snmp_credentials_tab():
                ret_val = self.xiqse_create_snmp_credential(name, version, comm_str)

        return ret_val

    def xiqse_navigate_and_create_snmpv1_credential(self, name, comm_str):
        """
         - This keyword navigates to the Administration> Profiles> SNMP Credentials tab and
         - creates a new SNMPv1 credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Create SNMPv1 Credential  test_cred_1  public``

        :param name: value to enter in the Credential Name field
        :param comm_str: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_snmp_credentials_tab():
                ret_val = self.xiqse_create_snmpv1_credential(name, comm_str)

        return ret_val

    def xiqse_navigate_and_create_snmpv2_credential(self, name, comm_str):
        """
         - This keyword navigates to the Administration> Profiles> SNMP Credentials tab and
         - creates a new SNMPv2 credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Create SNMP Credential  test_cred_2   private``

        :param name: value to enter in the Credential Name field
        :param comm_str: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_snmp_credentials_tab():
                ret_val = self.xiqse_create_snmpv2_credential(name, comm_str)

        return ret_val

    def xiqse_navigate_and_create_snmpv3_credential(self, name, user_name, auth_type="None", auth_pwd=None,
                                                    priv_type=None, priv_pwd=None):
        """
         - This keyword navigates to the Administration> Profiles> SNMP Credentials tab and
         - creates a new SNMPv3 credential in XIQ-SE.
         - Please use xiqse_navigate_and_create_credential to create an SNMPv1 or SNMPv2 credential
         - Keyword Usage
          - ``XIQSE Navigate and Create SNMPv3 Credential  test_cred_1  admin``
          - ``XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=MD5  auth_pwd=auth_pwd``
          - ``XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=SHA  auth_pwd=auth_pwd  priv_type=AES  priv_pwd=priv_pwd``

        :param name: value to enter in the Credential Name field
        :param user_name: value to enter in the User Name field
        :param auth_type: value to select for the Authentication Type field (None, MD5, SHA)
        :param auth_pwd: value to enter in the Authentication Password field
        :param priv_type: value to select for the Privacy Type field (None, AES, DES)
        :param priv_pwd: value to enter in the Privacy Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_snmp_credentials_tab():
                ret_val = self.xiqse_create_snmpv3_credential(name, user_name, auth_type, auth_pwd, priv_type, priv_pwd)

        return ret_val

    def xiqse_navigate_and_select_snmp_credential(self, name):
        """
         - This keyword navigates to the Administration> Profiles> SNMP Credentials tab and
         - selects an existing SNMP credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Select SNMP Credential  test_cred_1``

        :param name: name of the SNMP credential to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_snmp_credentials_tab():
                ret_val = self.xiqse_select_snmp_credential(name)

        return ret_val

    def xiqse_navigate_and_delete_snmp_credential(self, name):
        """
         - This keyword navigates to the Administration> Profiles> SNMP Credentials tab and
         - deletes an existing SNMP credential in XIQ-SE.
         - Keyword Usage
          - ``XIQSE Navigate and Delete SNMP Credential  test_cred_1``

        :param name: name of the SNMP credential to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            if self.xiqse_profiles.xiqse_profiles_select_snmp_credentials_tab():
                ret_val = self.xiqse_delete_snmp_credential(name)

        return ret_val

    def xiqse_create_snmp_credential(self, name, version, comm_str):
        """
         - This keyword creates a new SNMPv1 or SNMPv2 credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.
         - Please use xiqse_create_snmpv3_credential to create an SNMPv3 credential
         - Keyword Usage
          - ``XIQSE Create SNMP Credential  test_cred_1  SNMPv1  public``
          - ``XIQSE Create SNMP Credential  test_cred_2  SNMPv2  private``

        :param name: value to enter in the Credential Name field
        :param version: value to select for the SNMP Version field (SNMPv1, SNMPv2, SNMPv3)
        :param comm_str: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_add_snmp_credential_button()
        if add_btn:
            self.utils.print_info("Clicking 'Add...' toolbar button to display the Add SNMP Credential dialog")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Enter Credential Name
            ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_set_credential_name(name)

            # Select SNMP Version
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_select_snmp_version(version)

            # Enter Community Name
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_set_community_name(comm_str)

            # Click Save
            if ret_val != -1:
                sleep(2)
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_click_save()
            else:
                self.utils.print_info("Unable to complete Add SNMP Credential action; closing dialog")
                self.screen.save_screen_shot()
                self.add_cred_dlg.xiqse_add_snmp_credential_dialog_click_cancel()
        else:
            self.utils.print_info("Unable to find Add SNMP Credential toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_create_snmpv1_credential(self, name, comm_str):
        """
         - This keyword creates a new SNMPv1 credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.
         - Keyword Usage
          - ``XIQSE Create SNMP Credential  test_cred_1  public``

        :param name: value to enter in the Credential Name field
        :param comm_str: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        return self.xiqse_create_snmp_credential(name, "SNMPv1", comm_str)

    def xiqse_create_snmpv2_credential(self, name, comm_str):
        """
         - This keyword creates a new SNMPv2 credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.
         - Keyword Usage
          - ``XIQSE Create SNMP Credential  test_cred_2  private``

        :param name: value to enter in the Credential Name field
        :param comm_str: value to enter in the Community Name field
        :return: 1 if action was successful, else -1
        """
        return self.xiqse_create_snmp_credential(name, "SNMPv2", comm_str)

    def xiqse_create_snmpv3_credential(self, name, user_name, auth_type="None", auth_pwd=None,
                                       priv_type=None, priv_pwd=None):
        """
         - This keyword creates a new SNMPv3 credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.
         - Please use xiqse_create_snmp_credential to create an SNMPv1 or SNMPv2 credential
         - Keyword Usage
          - ``XIQSE Navigate and Create SNMPv3 Credential  test_cred_1  admin``
          - ``XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=MD5  auth_pwd=auth_pwd``
          - ``XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=SHA  auth_pwd=auth_pwd  priv_type=AES  priv_pwd=priv_pwd``

        :param name: value to enter in the Credential Name field
        :param user_name: value to enter in the User Name field
        :param auth_type: value to select for the Authentication Type field (None, MD5, SHA)
        :param auth_pwd: value to enter in the Authentication Password field
        :param priv_type: value to select for the Privacy Type field (None, AES, DES)
        :param priv_pwd: value to enter in the Privacy Password field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_add_snmp_credential_button()
        if add_btn:
            self.utils.print_info("Clicking 'Add...' toolbar button to display the Add SNMP Credential dialog")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Enter Credential Name
            ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_set_credential_name(name)

            # Select SNMP Version
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_select_snmp_version("SNMPv3")

            # Enter User Name
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_set_user_name(user_name)

            # Select Authentication Type
            if ret_val != -1:
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_select_authentication_type(auth_type)

            # The remaining fields are only enabled if Authentication Type is not "None"
            if auth_type != "None":
                # Enter Authentication Password
                if ret_val != -1 and auth_pwd:
                    ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_set_authentication_password(auth_pwd)

                # Select Privacy Type
                if ret_val != -1 and priv_type:
                    ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_select_privacy_type(priv_type)

                # The remaining fields are only enabled if Privacy Type is not "None"
                if priv_type != "None":
                    # Enter Privacy Password
                    if ret_val != -1 and priv_pwd:
                        ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_set_privacy_password(priv_pwd)
                else:
                    self.utils.print_debug("Privacy Type is None")
            else:
                self.utils.print_debug("Authentication Type is None")

            # Click Save
            if ret_val != -1:
                sleep(2)
                ret_val = self.add_cred_dlg.xiqse_add_snmp_credential_dialog_click_save()
            else:
                self.utils.print_info("Unable to complete Add SNMP Credential action; closing dialog")
                self.add_cred_dlg.xiqse_add_snmp_credential_dialog_click_cancel()
        else:
            self.utils.print_info("Unable to find Add SNMP Credential toolbar button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_delete_snmp_credential(self, name):
        """
         - This keyword deletes an existing SNMP credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.
         - Keyword Usage
          - ``XIQSE Delete SNMP Credential  test_cred_1``

        :param name: name of the SNMP credential to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_snmp_credential(name):
            delete_btn = self.get_delete_snmp_credential_button()
            if delete_btn:
                btn_disabled = delete_btn.get_attribute("aria-disabled")
                if btn_disabled == "true":
                    self.utils.print_info("'Delete' button is disabled")
                else:
                    self.utils.print_info("Clicking 'Delete' toolbar button")
                    self.auto_actions.click(delete_btn)
                    sleep(2)

                    # Confirm the deletion
                    ret_val = self.delete_cred_dlg.xiqse_delete_snmp_credential_confirm_delete()
            else:
                self.utils.print_info("Could not find 'Delete' button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_snmp_credential(self, name):
        """
        - Searches for SNMP Credential matching the specified name.
        - Assumes the Administration> Profiles> SNMP Credentials tab is already selected.

        :param name: Name of the SNMP credential to search for
        :return: return 1 if the SNMP credential is found, else -1
        """

        ret_val = -1

        sleep(2)
        self.xiqse_refresh_snmp_credentials_table()
        sleep(2)

        rows = self.get_snmp_credentials_table_rows()
        if rows:
            for row in rows:
                self.utils.print_debug(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                if name in row.text:
                    self.utils.print_info(f"Found row for SNMP credential with name {name}")
                    ret_val = 1
                    break
            if ret_val == -1:
                self.utils.print_info(f"Did not find row for SNMP credential with name {name}")
        else:
            self.utils.print_info("Could not obtain rows from SNMP Credentials table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_snmp_credential(self, name):
        """
         - This keyword selects an existing SNMP credential in XIQ-SE.
         - It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.
         - Keyword Usage
          - ``XIQSE Select SNMP Credential  test_cred_1``

        :param name: name of the SNMP credential to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        sleep(2)
        rows = self.get_snmp_credentials_table_rows()
        for row in rows:
            if name in row.text:
                self.utils.print_debug(f"Found SNMP Credential {name} in row {self.xiqse_table.format_table_row(row.text)}")
                row_selected = row.get_attribute("aria-selected")
                if row_selected and row_selected == "true":
                    self.utils.print_info(f"Row for SNMP Credential {name} is already selected")
                else:
                    self.utils.print_info(f"Selecting SNMP Credential {name}")
                    self.auto_actions.click(row)
                ret_val = 1
                break

        if ret_val == -1:
            self.utils.print_info(f"Unable to select SNMP Credential {name}")
            self.screen.save_screen_shot()

        return ret_val
