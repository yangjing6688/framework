from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.profiles.AdminProfilesWebElements import AdminProfilesWebElements
from xiqse.flows.admin.profiles.XIQSE_AdminProfilesAddProfile import XIQSE_AdminProfilesAddProfile
from xiqse.flows.admin.profiles.XIQSE_AdminProfilesEditProfile import XIQSE_AdminProfilesEditProfile
from xiqse.flows.admin.profiles.XIQSE_AdminProfilesDeleteProfile import XIQSE_AdminProfilesDeleteProfile
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable


class XIQSE_AdminProfiles(AdminProfilesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_nav = XIQSE_CommonNavigator()
        self.xiqse_table = XIQSE_CommonTable()
        self.add_profile_dlg = XIQSE_AdminProfilesAddProfile()
        self.edit_profile_dlg = XIQSE_AdminProfilesEditProfile()
        self.delete_profile_dlg = XIQSE_AdminProfilesDeleteProfile()

    def xiqse_profiles_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Administration> Profiles page
        - Keyword Usage
        - ``XIQSE Profiles Select Tab    SNMP Credentials``
        - ``XIQSE Profiles Select Tab    CLI Credentials``
        - ``XIQSE Profiles Select Tab    Device Mapping``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "SNMP Credentials":
            the_tab = self.get_snmp_credentials_tab()
        elif tab_name == "CLI Credentials":
            the_tab = self.get_cli_credentials_tab()
        elif tab_name == "Device Mapping":
            the_tab = self.get_device_mapping_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Administration> Profiles page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Administration> Profiles page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_profiles_select_snmp_credentials_tab(self):
        """
        - This keyword selects the SNMP Credentials tab on the Administration> Profiles page.
        - It is assumed the Administration> Profiles page is currently being displayed.
        - Keyword Usage
        - ``XIQSE Profiles Select SNMP Credentials Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_profiles_select_tab("SNMP Credentials")

    def xiqse_profiles_select_cli_credentials_tab(self):
        """
        - This keyword selects the CLI Credentials tab on the Administration> Profiles page.
        - It is assumed the Administration> Profiles page is currently being displayed.
        - Keyword Usage
        - ``XIQSE Profiles Select CLI Credentials Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_profiles_select_tab("CLI Credentials")

    def xiqse_profiles_select_device_mapping_tab(self):
        """
        - This keyword selects the Device Mapping tab on the Administration> Profiles page.
        - It is assumed the Administration> Profiles page is currently being displayed.
        - Keyword Usage
        - ``XIQSE Profiles Select Device Mapping Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_profiles_select_tab("Device Mapping")

    def xiqse_refresh_profiles_table(self):
        """
        - Refreshes the Profiles table.
        - Assumes the Administration> Profiles tab is already selected.

        :return: return 1 if the action is successful, else -1
        """

        ret_val = -1

        the_btn = self.get_profiles_refresh_table_button()
        if the_btn:
            self.utils.print_info("Refreshing the Profiles table")
            self.auto_actions.click(the_btn)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Refresh button for the Profiles table")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_and_create_profile(self, name, version="SNMPv1", read=None, write=None, max=None, cli=None):
        """
        - This keyword navigates to the Administration> Profiles tab and creates a new profile in XIQ-SE.
        - Keyword Usage
        - ``XIQSE Navigate and Create Profile  test_profile_1``
        - ``XIQSE Navigate and Create Profile  test_profile_2  SNMPv2  public_v1  private_v1  private_v1  Default``

        :param name: value to enter in the Profile Name field
        :param version: value to select for the SNMP Version field (SNMPv1, SNMPv2, SNMPv3)
        :param read: value to select for the Read field
        :param write: value to select for the Write field
        :param max: value to select for the Max Access field
        :param cli: value to select for the CLI Credential field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            ret_val = self.xiqse_create_profile(name, version, read, write, max, cli)

        return ret_val

    def xiqse_navigate_and_select_profile(self, name):
        """
        - This keyword navigates to the Administration> Profiles tab and selects an existing profile in XIQ-SE.
        - Keyword Usage
        - ``XIQSE Navigate and Select Profile  test_profile_1``

        :param name: name of the profile to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            ret_val = self.xiqse_select_profile(name)

        return ret_val

    def xiqse_navigate_and_delete_profile(self, name):
        """
        - This keyword navigates to the Administration> Profiles tab and deletes an existing profile in XIQ-SE.
        - Keyword Usage
        - ``XIQSE Navigate and Delete Profile  test_profile_1``

        :param name: name of the profile to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_nav.xiqse_navigate_to_admin_profiles_tab():
            ret_val = self.xiqse_delete_profile(name)

        return ret_val

    def xiqse_create_profile(self, name, version="SNMPv1", read=None, write=None, max=None, cli=None,
                              read_sec=None, write_sec=None, max_sec=None):
        """
        - This keyword creates a new profile in XIQ-SE.
        - It is assumed the view is already navigated to Administration> Profiles.
        - Keyword Usage
        - ``XIQSE Create Profile  test_profile_1``
        - ``XIQSE Create Profile  test_profile_2  SNMPv2  public_v1  private_v1  private_v1  Default``

        :param name: value to enter in the Profile Name field
        :param version: value to select for the SNMP Version field (SNMPv1, SNMPv2, SNMPv3)
        :param read: value to select for the Read field
        :param write: value to select for the Write field
        :param max: value to select for the Max Access field
        :param read_sec: value to select for the Read Security field (for SNMPv3 version only)
        :param write_sec: value to select for the Write Security field (for SNMPv3 version only)
        :param max_sec: value to select for the Max Security field (for SNMPv3 version only)
        :param cli: value to select for the CLI Credential field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_add_profile_button()
        if add_btn:
            self.utils.print_info("Clicking 'Add...' toolbar button")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Enter Profile Name
            ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_set_profile_name(name)

            # Select SNMP Version
            if ret_val != -1:
                ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_snmp_version(version)

            # Select Read value
            if read and ret_val != -1:
                ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_read(read)

            # Select Write value
            if write and ret_val != -1:
                ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_write(write)

            # Select Max Access value
            if max and ret_val != -1:
                ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_max_access(max)

            # Handle SNMPv3 Profile's additional fields
            if version == "SNMPv3":
                self.utils.print_debug("Handling SNMPv3 fields")
                # Select Read value
                if read_sec and ret_val != -1:
                    ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_read_security(read_sec)

                # Select Write value
                if write_sec and ret_val != -1:
                    ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_write_security(write_sec)

                # Select Max Access value
                if max_sec and ret_val != -1:
                    ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_max_security(max_sec)

            # Select CLI Credential
            if cli and ret_val != -1:
                ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_select_cli(cli)

            # Click Save
            sleep(2)
            if ret_val != -1:
                ret_val = self.add_profile_dlg.xiqse_add_profile_dialog_click_save()
            else:
                self.utils.print_info("Problems entering information into Add Profile dialog")
                self.screen.save_screen_shot()
                self.add_profile_dlg.xiqse_add_profile_dialog_click_cancel()
        else:
            self.utils.print_info("Unable to find Add Profile toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_edit_profile(self, name, read=None, write=None, max=None, cli=None):
        """
        - This keyword edits the specified profile in XIQ-SE.
        - It is assumed the view is already navigated to Administration> Profiles.
        - Keyword Usage
        - ``XIQSE Edit Profile  test_profile_1  cli=MY_CLI``
        - ``XIQSE Edit Profile  test_profile_2  read=public_v1  write=private_v1  max=private_v1  cli=Default``

        :param name: name of the profile to edit
        :param read: value to select for the Read field
        :param write: value to select for the Write field
        :param max: value to select for the Max Access field
        :param cli: value to select for the CLI Credential field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_profile(name):
            edit_btn = self.get_edit_profile_button()
            if edit_btn:
                btn_disabled = edit_btn.get_attribute("aria-disabled")
                if btn_disabled == "true":
                    self.utils.print_info("'Edit' button is disabled")
                else:
                    self.utils.print_info("Clicking 'Edit' toolbar button")
                    self.auto_actions.click(edit_btn)
                    sleep(2)

                    # Assume success - this will be updated if a field fails to be updated or save fails
                    ret_val = 1

                    # Select Read value
                    if read and ret_val != -1:
                        ret_val = self.edit_profile_dlg.xiqse_edit_profile_dialog_select_read(read)

                    # Select Write value
                    if write and ret_val != -1:
                        ret_val = self.edit_profile_dlg.xiqse_edit_profile_dialog_select_write(write)

                    # Select Max Access value
                    if max and ret_val != -1:
                        ret_val = self.edit_profile_dlg.xiqse_edit_profile_dialog_select_max_access(max)

                    # Select CLI Credential
                    if cli and ret_val != -1:
                        ret_val = self.edit_profile_dlg.xiqse_edit_profile_dialog_select_cli(cli)

                    # Click Save
                    sleep(2)
                    if ret_val != -1:
                        ret_val = self.edit_profile_dlg.xiqse_edit_profile_dialog_click_save()
                    else:
                        self.utils.print_info("Problems entering information into Edit Profile dialog")
                        self.screen.save_screen_shot()
                        self.edit_profile_dlg.xiqse_edit_profile_dialog_click_cancel()
            else:
                self.utils.print_info("Could not find 'Edit' button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find Add Profile toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_delete_profile(self, name):
        """
        - This keyword deletes an existing profile in XIQ-SE.
        - It is assumed the view is already navigated to Administration> Profiles.
        - Keyword Usage
        - ``XIQSE Delete Profile  test_profile_1``

        :param name: name of the profile to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_profile(name):
            delete_btn = self.get_delete_profile_button()
            if delete_btn:
                btn_disabled = delete_btn.get_attribute("aria-disabled")
                if btn_disabled == "true":
                    self.utils.print_info("'Delete' button is disabled")
                else:
                    self.utils.print_info("Clicking 'Delete' toolbar button")
                    self.auto_actions.click(delete_btn)
                    sleep(2)

                    # Confirm the deletion
                    ret_val = self.delete_profile_dlg.xiqse_delete_profile_confirm_delete()
            else:
                self.utils.print_info("Could not find 'Delete' button")
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_profile(self, name):
        """
        - This keyword selects an existing profile in XIQ-SE.
        - It is assumed the view is already navigated to Administration> Profiles.
        - Keyword Usage
        - ``XIQSE Select Profile  test_profile_1``

        :param name: name of the profile to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        sleep(2)
        rows = self.get_profiles_table_rows()
        for row in rows:
            if name in row.text:
                self.utils.print_debug(f"Found profile {name} in row {self.xiqse_table.format_table_row(row.text)}")
                row_selected = row.get_attribute("aria-selected")
                if row_selected and row_selected == "true":
                    self.utils.print_info(f"Row for profile {name} is already selected")
                else:
                    self.utils.print_info(f"Selecting profile {name}")
                    self.auto_actions.click(row)
                ret_val = 1
                break
        if ret_val == -1:
            self.utils.print_info(f"Unable to select profile {name}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_profile(self, name):
        """
        - Searches for Profile matching the specified name.
        - Assumes the Administration> Profiles tab is already selected.

        :param name: Name of the Profile to search for
        :return: return 1 if the Profile is found, else -1
        """

        ret_val = -1

        sleep(2)
        self.xiqse_refresh_profiles_table()
        sleep(2)

        rows = self.get_profiles_table_rows()
        if rows:
            self.utils.print_debug(f"Profile row count: {len(rows)}")
            for row in rows:
                self.utils.print_debug(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                if name in row.text:
                    self.utils.print_info(f"Found row for profile with name {name}")
                    ret_val = 1
                    break
            if ret_val == -1:
                self.utils.print_info(f"Did not find row for profile with name {name}")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not obtain rows from Profiles table")
            self.screen.save_screen_shot()

        return ret_val
