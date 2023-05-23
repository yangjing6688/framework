from time import sleep
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
from tools.xapi.XapiHelper import XapiHelper
import inspect
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from extauto.xiq.flows.globalsettings.AccountManagement import AccountManagement
from extauto.xiq.elements.AccntMgmtWebElements import AccntMgmtWebElements


class KeywordsAccountManagement(AccntMgmtWebElements, metaclass=Singleton):
    def __init__(self):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        super().__init__()
        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        self.account_mgmt = AccountManagement()

    def create_role_based_account(self, accnt_config, **kwargs):
        """
        Creates a new account under account management

        This method creates a new account and will configure the role for the account
        For example:
            - &{OPERATOR_ROLE} or &{MONITOR_ROLE} or &{HELPDESK_ROLE} or &{Guest_Management_Role}or &{Observer_Role}
        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/account_management/KeywordsAccountManagement.py
        -      Create Role Based Account   ${GUEST_MANAGEMENT_ROLE}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.account_management.KeywordsAccountManagement import KeywordsAccountManagement
        -      Calling Keyword:
        -         account_mgmt = KeywordsAccountManagement()
        -         account_mgmt.create_role_based_account(accnt_config, **kwargs)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param accnt_config: Name of the new account
        :return: Returns 1 if success, -1 if not success.
        """

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("32e34132-f94c-11ed-be56-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume Failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.account_mgmt.gui_create_role_based_account(accnt_config, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def delete_management_account(self, email_addr, **kwargs):
        """
        Deletes a management account

        This method will delete a management account from Account Management tab

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/account_management/KeywordsAccountManagement.py
        -      Delete Management Account       ${TENANT_EMAIL_ID}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.account_management.KeywordsAccountManagement import KeywordsAccountManagement
        -      Calling Keyword:
        -         account_mgmt = KeywordsAccountManagement()
        -         account_mgmt.delete_management_account(email_addr, **kwargs)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param email_addr: Email id of the management account
        :return: Returns 1 if success, -1 if not success.
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("32e3457e-f94c-11ed-be56-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume Failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.account_mgmt.gui_delete_management_account(email_addr, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def delete_guest_management_accounts(self, **kwargs):
        """
        Deletes guest management accounts

        This method will delete all the guest management account from the list of Account Management tab

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/account_management/KeywordsAccountManagement.py
        -      Delete Guest Management Accounts
        -   Pytest:
        -      Imports:
        -         from keywords.gui.account_management.KeywordsAccountManagement import KeywordsAccountManagement
        -      Calling Keyword:
        -         account_mgmt = KeywordsAccountManagement()
        -         account_mgmt.delete_guest_management_accounts(**kwargs)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param: N/A
        :return: Returns 1 if success, -1 if not success.
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("32e346c8-f94c-11ed-be56-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume Failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.account_mgmt.gui_delete_guest_management_accounts(**kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def delete_guest_management_account(self, email_addr, **kwargs):
        """
        - Search the specified guest account in accounts grid
        - if exist delete the account
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Delete Management Account  ${ACCOUNT_EMAIL}``

        :param email_addr: email address to search the account
        :return: 1 if Account found on grid and got deleted successfully else None
        """
        self.utils.print_info("Navigating to the account Management page..")
        self.navigator.navigate_to_account_mgmt()
        sleep(2)

        if row := self.search_guest_account(email_addr):
            self.utils.print_info("Deleting  account")
            self.auto_actions.click(self.get_account_mgmt_grid_row_check_box(row))
            sleep(2)
            self.utils.print_info("click on delete button")
            self.auto_actions.click_reference(self.get_account_mgmt_delete_button)
            sleep(1)
            self.auto_actions.click_reference(self.get_account_mgmt_delete_conf_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "Account found on grid and got deleted " \
                                 "successfully"
            self.common_validation.passed(**kwargs)
            return 1

    def open_account_mgmt_page(self, **kwargs):
        """
        - Navigates to Account Management Page
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Open Account Mgmt Page``

        :return: 1 if no issues in opening Account Management page else returns -2
        """
        self.utils.print_info("Navigating to the account Management page..")
        if self.navigator.navigate_to_account_mgmt() == 1:
            kwargs['pass_msg'] = "No issues in opening Account Management page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Found issues in opening Account Management page"
            self.common_validation.failed(**kwargs)
            return -2

    def open_license_mgmt_page(self, **kwargs):
        """
        - Navigates to License Management Page
        - Flow : User account image-->Global Settings--> ADMINISTRATION-->License Management
        - Keyword Usage
        - ``Open License Mgmt Page``

        :return: 1 if no issues in opening License Management page else returns -2
        """

        self.utils.print_info("Navigating to the license Management page..")
        if self.navigator.navigate_to_license_mgmt() == 1:
            kwargs['pass_msg'] = "No issues in opening License Management page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Found issues in opening License Management page"
            self.common_validation.failed(**kwargs)
            return -2

    def open_tools_page(self, **kwargs):
        """
        - Navigates to Tools Page on Monitor Menu Option
        - Flow : Manage-->Tools
        - Keyword Usage
        - ``Open Tools Page``

        :return: 1 if no issues in opening Tools page else returns -2
        """

        self.utils.print_info("Navigating to the Tools page..")
        if self.navigator.navigate_to_tools_page() == 1:
            tooltip_text = self.dialogue_web_elements.get_tooltip_text()
            self.utils.print_info("tooltip_text: ", tooltip_text)
            if tooltip_text:
                if "Your account does not have permission to perform that action" in tooltip_text:
                    kwargs['fail_msg'] = "Found issues in opening Tools. Your account does not have permission to " \
                                         "perform that action"
                    self.common_validation.failed(**kwargs)
                    return -2
            kwargs['pass_msg'] = "No issues in opening Tools"
            self.common_validation.passed(**kwargs)
            return 1

    def open_dashboard_page(self, **kwargs):
        """
        - Navigates to Dashboard Page
        - Keyword Usage
        - ``Open Dashboard Page``

        :return: 1 if no issues in opening Dashboard page else returns -2
        """
        self.utils.print_info("Navigating to Dashboard page..")
        if self.navigator.navigate_to_dashboard_page() == 1:
            kwargs['pass_msg'] = "No issues in opening Dashboard"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Found issues in opening License Management page"
            self.common_validation.failed(**kwargs)
            return -2

    def check_for_dashboard_page(self, **kwargs):
        """
        - Check for Dashboard Page
        - Keyword Usage
        - ``Check For Dashboard Page``

        :return: 1 if no issues in opening page else returns -2
        """
        self.utils.print_info("Navigating to Dashboard page..")
        if self.navigator.navigate_to_dashboard_page() == 1:
            kwargs['pass_msg'] = "No issues in opening page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            utils_ele = self.tools_elements.get_utilities_button()
            if utils_ele.is_displayed():
                kwargs['fail_msg'] = "Found issues in opening page"
                self.common_validation.failed(**kwargs)
                return -2

    def open_guest_mgmt_page(self, **kwargs):
        """
        - Navigates to Guest Management Page
        - Flow : Global settings > Credential Distribution Groups
        - Keyword Usage
        - ``Open Guest Mgmt Page``

        :return: 1 if no issues in opening Guest Management page else returns -2
        """

        self.utils.print_info("Navigating to Guest Management page..")
        if self.navigator.navigate_to_credential_dist_groups() == 1:
            kwargs['pass_msg'] = "No issues in opening Guest Management page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Found issues in opening Guest Management page"
            self.common_validation.failed(**kwargs)
            return -2

    def check_packet_capture_option(self, **kwargs):
        """
        - Navigates to Packet Capture option Page
        - Flow : Manage > Tools-->Packet Capture
        - Keyword Usage
        - ``Check Packet Capture Option``

        :return: 1 if no issues in opening Tools --> Packet Capture page else returns -2
        """

        self.utils.print_info("Navigating to Tools page..")
        if self.open_tools_page() == -2:
            kwargs['fail_msg'] = "Unsuccessfully navigate to tools page"
            self.common_validation.fault(**kwargs)
            return -2
        else:
            pkt_cap = self.get_packet_capture_button()
            if pkt_cap == 1:
                kwargs['pass_msg'] = "No issues in opening Tools --> Packet Capture page"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Found issues in opening Tools --> Packet Capture page"
                self.common_validation.failed(**kwargs)
                return -2

    def check_config_error(self, **kwargs):
        """
        - Check for Errors while Saving Configurations on XIQ
        - Keyword Usage
        - ``Check Config Error``

        :return: 1 if no error message after saving the config else returns -2
        """

        self.utils.print_info("Checking for the error after config..")
        if self._check_config_error_msg() == 1:
            kwargs['pass_msg'] = "no error message after saving the config"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Found error message after saving the config"
            self.common_validation.failed(**kwargs)
            return -2

    def get_packet_capture_button(self, **kwargs):
        self.utils.print_info("Clicking on packet capture button...")
        cdg_ele = self.weh.get_element(self.packet_capture)
        sleep(2)
        if cdg_ele:
            self.auto_actions.click(cdg_ele)
            kwargs['pass_msg'] = "Successfully Get packet capture"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unsuccessfully Get packet capture"
            self.common_validation.failed(**kwargs)
            return -2

    def _check_config_error_msg(self, **kwargs):
        self.utils.print_info("Checking error...")
        cdg_ele = self.weh.get_element(self.config_error)
        sleep(2)
        if cdg_ele.is_displayed():
            kwargs['fail_msg'] = "Got error..."
            self.common_validation.failed(**kwargs)
            return -2
        else:
            kwargs['pass_msg'] = "No Errors"
            self.common_validation.passed(**kwargs)
            return 1

    def create_credential_distribution_groups(self, group_name, admin_account, member_of, restriction_count,
                                              registration_operation, user_group_name, **kwargs):
        """
        :param group_name: group name
        :param admin_account: admin account
        :param member_of: member of
        :param restriction_count: credential_restriction`count
        :param registration_operation: registration_operation
        :param user_group_name: user_group_name
        :return: 1 if success. -1 if fails
        :return: -2 if error: User must be a member of a group.
        :return: -3 if error: Select at least one user group.
        :return: -4 if error: That group already exists.
        :return: -5 if error: The Member Group cannot be saved because the name << >> already exists.
        """

        self.utils.print_info("Navigating to Credential Distribution Groups...")
        self.navigator.navigate_to_credential_dist_groups()

        sleep(5)

        self.utils.print_info("Clicking + button")
        self.auto_actions.click_reference(self.get_credential_distribution_groups_add_button)
        sleep(2)

        self.utils.print_info("Entering group name")
        self.auto_actions.send_keys(self.get_credential_distribution_groups_name_textfield(), group_name)
        sleep(2)

        self.utils.print_info("Selecting admin account")
        self.auto_actions.click_reference(self.get_credential_distribution_groups_admin_account_dropdown)
        sleep(2)

        if admin_account == "Guest Management Role User":
            self.utils.print_info("Selecting guest management role user")
            self.auto_actions.click_reference(self.get_credential_distribution_groups_guest_management_role_user_option)
            sleep(2)

        if admin_account == "Active Directory User":
            self.utils.print_info("Selecting active directory user")
            self.auto_actions.click_reference(self.get_credential_distribution_groups_active_directory_user_option)
            sleep(2)

        self.utils.print_info("selecting member of ")
        self.auto_actions.send_keys(self.get_credential_distribution_groups_member_of(), member_of)
        sleep(2)

        self.utils.print_info("Selecting credential restriction")
        self.auto_actions.click_reference(self.get_credential_distribution_groups_credential_restriction_checkbox)
        sleep(2)

        self.utils.print_info("Selecting credential restriction count")
        self.auto_actions.send_keys(self.get_credential_distribution_groups_credential_restriction_count(), restriction_count)
        sleep(2)

        self.utils.print_info("Selecting registration operation: ", registration_operation)
        if registration_operation != "None":
            self.utils.print_info("Selecting registration operation")
            self.auto_actions.click_reference(self.get_credential_distribution_groups_registration_operation_checkbox)
            sleep(2)

        self.utils.print_info("Selecting enable user groups: ", user_group_name)
        if "Select All" in user_group_name:
            self.auto_actions.click_reference(self.get_credential_distribution_groups_select_all_checkbox)
        else:
            user_group_checkboxes = self.get_credential_distribution_groups_user_group_checkboxes()
            for user_group_checkbox in user_group_checkboxes:
                self.utils.print_info("user_group_checkbox.text: ", user_group_checkbox.text)
                if user_group_name in user_group_checkbox.text:
                    self.auto_actions.click(user_group_checkbox)
        sleep(2)

        self.utils.print_info("Saving...")
        self.auto_actions.click_reference(self.get_credential_distribution_groups_save_button)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info("Tooltip: ", tool_tp_text)
        if "User must be a member of a group." in tool_tp_text:
            kwargs['fail_msg'] = "User must be a member of a group."
            self.common_validation.failed(**kwargs)
            return -2

        if "Select at least one user group." in tool_tp_text:
            kwargs['fail_msg'] = "Select at least one user group."
            self.common_validation.failed(**kwargs)
            return -3

        if "That group already exists." in tool_tp_text:
            kwargs['fail_msg'] = "That group already exists."
            self.common_validation.failed(**kwargs)
            return -4

        if "The Member Group cannot be saved because the name " + member_of + " already exists.":
            kwargs['fail_msg'] = "The Member Group cannot be saved " \
                                 "because the name " + member_of + " already exists."
            self.common_validation.failed(**kwargs)
            return -5

        if "The Employee Group was saved successfully." in tool_tp_text:
            kwargs['pass_msg'] = "The Employee Group was saved successfully."
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "Failed to save the employee group."
        self.common_validation.failed(**kwargs)
        return -1
