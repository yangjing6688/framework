""" This file contains code for keywords that have been archived.
    If the keywords need to be available again copy the code to xiq/flows/common/Login.py
    and implement the keyword move process.
    Instructions for moving a keyword can be found here:
    https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords """


from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.AccntMgmtWebElements import AccntMgmtWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.ToolsElements import ToolsElements
from extauto.common.CommonValidation import CommonValidation
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Utilities.deprecated import deprecated


class AccountManagement(AccntMgmtWebElements, metaclass=Singleton):
    def __init__(self):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.dialogue_web_elements = DialogWebElements()
        self.tools_elements = ToolsElements()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

        if row := self._search_guest_account(email_addr):
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def check_packet_capture_option(self, **kwargs):
        """
        - Navigates to Packet Capture option Page
        - Flow : Manage > Tools-->Packet Capture
        - Keyword Usage
        - ``Check Packet Capture Option``

        :return: 1 if no issues in opening Tools --> Packet Capture page else returns -2
        """

        self.utils.print_info("Navigating to Tools page..")
        if self._open_tools_page() == -2:
            kwargs['fail_msg'] = "Unsuccessfully navigate to tools page"
            self.common_validation.fault(**kwargs)
            return -2
        else:
            pkt_cap = self._get_packet_capture_button()
            if pkt_cap == 1:
                kwargs['pass_msg'] = "No issues in opening Tools --> Packet Capture page"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Found issues in opening Tools --> Packet Capture page"
                self.common_validation.failed(**kwargs)
                return -2

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
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
