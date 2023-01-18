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


class AccountManagement(AccntMgmtWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.dialogue_web_elements = DialogWebElements()
        self.tools_elements = ToolsElements()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    def search_management_account(self, email_addr):
        """
        - Search the management account in accounts grid
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Search Management Account  ${ACCOUNT_EMAIL}``

        :param email_addr: Email Address Of the Account
        :return: row if Exists else None
        """
        for row in self.get_account_mgmt_grid_rows():
            if email_addr in row.text:
                self.utils.print_info(f"Account {email_addr} exists")
                return row

    def search_guest_accounts(self):
        """
        - Search the guest management accounts in accounts grid
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Search Management Account ``

        :return: row if Exists else None
        """
        row_guest = []
        for row in self.get_account_mgmt_grid_rows():
            if 'Guest Management' in row.text:
                row_guest.append(row)
        return row_guest

    def search_guest_account(self, email_addr):
        """
        - Search the management account in accounts grid
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Search Management Account  ${ACCOUNT_EMAIL}``

        :param email_addr: Email Address Of the Account
        :return: row if Exists else None
        """
        for row in self.get_account_mgmt_grid_rows():
            if email_addr in row.text:
                if 'Guest Management' in row.text:
                    self.utils.print_info(f"Account {email_addr} exists")
                    return row
                else:
                    self.utils.print_info(f"Account {email_addr} is not guest management account")

    def create_role_based_account(self, accnt_config, **kwargs):
        """
        - Creates an account based on the arguments from rbac_config.robot
        - &{OPERATOR_ROLE}, &{MONITOR_ROLE}, &{HELPDESK_ROLE}, &{Guest_Management_Role}, &{Observer_Role}
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Create Role Based Account  &{ACCOUNT_CONFIGS}``

        :param accnt_config: (dict) include email, name, timeout, role, organization, location
        :return: 1 if there is no error
        """

        self.utils.print_info(accnt_config)
        email = accnt_config.get('email')
        name = accnt_config.get('name')
        timeout = accnt_config.get('timeout')
        role = accnt_config.get('role')
        location = accnt_config.get('location')
        organization = accnt_config.get('organization')

        self.utils.print_info("Navigating to the account Management page..")
        self.navigator.navigate_to_account_mgmt()
        sleep(2)

        self.utils.print_info("Deleting the account if exists")
        if self.search_management_account(email):
            return 1

        self.utils.print_info("Clicking on account add button")
        self.auto_actions.click_reference(self.get_account_mgmt_add_button)
        sleep(2)

        self.utils.print_info(f"Entering email id:{email}")
        self.auto_actions.send_keys(self.get_account_mgmt_email_text(), email)

        self.utils.print_info(f"Entering name: {name}")
        self.auto_actions.send_keys(self.get_account_mgmt_name_text(), name)

        self.utils.print_info("Organisation drop down is visible only for MSP Account")
        if self.get_account_mgmt_organisation_sec().is_displayed():
            self.utils.print_info("Click on organisation drop down")
            self.auto_actions.click_reference(self.get_account_mgmt_org_drop_down)
            sleep(2)
            self.auto_actions.select_drop_down_options(self.get_account_mgmt_org_drop_down_opt(), organization)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info(f"Entering session timeout: {timeout}")
        self.auto_actions.send_keys(self.get_account_mgmt_timeout(), timeout)

        self.utils.print_info(f"Selecting the role:{role}")

        role_dict = {'Administrator': self.get_administrator_role_radio_button(),
                     'Operator': self.get_operator_role_radio_button(),
                     'Monitor': self.get_monitor_role_radio_button(),
                     'Helpdesk': self.get_help_desk_role_radio_button(),
                     'GuestManagement': self.get_guest_management_role_radio_button(),
                     'Observer': self.get_observer_role_radio_button()
                     }
        self.utils.print_info(f'click on account role:{role} radio button')
        self.auto_actions.click(role_dict[role])
        sleep(2)
        if role == "GuestManagement" or role == "Administrator":
            self.utils.print_info(f'Cannot select location for :{role} role')
        if role != "GuestManagement" and role != "Administrator":
            self.utils.print_info('selecting the location check box')
            self.auto_actions.click_reference(self.get_Rbac_Assign_Location_checkbox)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info('Clicking Account Management save button')
        self.auto_actions.click_reference(self.get_account_mgmt_save_button)
        sleep(5)
        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tooltip: ", tool_tip_text)
        for text in tool_tip_text:
            if "An admin account for" in text:
                kwargs['fail_msg'] = f"'create_role_based_account()' -> {text}"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['pass_msg'] = "'create_role_based_account()' -> Successfully create role based account"
        self.common_validation.passed(**kwargs)
        return 1

    def delete_management_account(self, email_addr, **kwargs):
        """
        - Search the management account in accounts grid
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

        if row := self.search_management_account(email_addr):
            self.utils.print_info(f"Deleting {email_addr} account")
            self.auto_actions.click(self.get_account_mgmt_grid_row_check_box(row))
            sleep(2)
            self.utils.print_info("click on delete button")
            self.auto_actions.click_reference(self.get_account_mgmt_delete_button)
            sleep(1)
            self.auto_actions.click_reference(self.get_account_mgmt_delete_conf_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "'delete_management_account()' -> Account found on grid and got deleted successfully"
            self.common_validation.passed(**kwargs)
            return 1

    def delete_guest_management_accounts(self, **kwargs):
        """
        - Search the guest accounts in accounts grid
        - if exist delete the account
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Delete Management Account ``

        :return: 1 if Account found on grid and got deleted successfully else None
        """
        self.utils.print_info("Navigating to the account Management page..")
        self.navigator.navigate_to_account_mgmt()
        sleep(2)

        if row := self.search_guest_accounts():
            self.utils.print_info("Deleting Guest account")
            for row_guest in row:
                self.auto_actions.click(self.get_account_mgmt_grid_row_check_box(row_guest))
            sleep(2)
            self.utils.print_info("click on delete button")
            self.auto_actions.click_reference(self.get_account_mgmt_delete_button)
            sleep(1)
            self.auto_actions.click_reference(self.get_account_mgmt_delete_conf_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "'delete_guest_management_accounts()' -> Account found on grid and got deleted " \
                                 "successfully"
            self.common_validation.passed(**kwargs)
            return 1

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
            kwargs['pass_msg'] = "'delete_guest_management_account()' -> Account found on grid and got deleted " \
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
            kwargs['pass_msg'] = "'open_account_mgmt_page()' -> No issues in opening Account Management page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'open_account_mgmt_page()' -> Found issues in opening Account Management page"
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
            kwargs['pass_msg'] = "'open_license_mgmt_page()' -> No issues in opening License Management page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'open_license_mgmt_page()' -> Found issues in opening License Management page"
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
                    kwargs['fail_msg'] = "'open_tools_page()' -> Found issues in opening Tools. Your account does " \
                                         "not have permission to perform that action"
                    self.common_validation.failed(**kwargs)
                    return -2
            kwargs['pass_msg'] = "'open_tools_page()' -> No issues in opening Tools"
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
            kwargs['pass_msg'] = "'open_dashboard_page()' -> No issues in opening Dashboard"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'open_dashboard_page()' -> Found issues in opening License Management page"
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
            kwargs['pass_msg'] = "'check_for_dashboard_page()' -> No issues in opening page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            utils_ele = self.tools_elements.get_utilities_button()
            if utils_ele.is_displayed():
                kwargs['fail_msg'] = "'check_for_dashboard_page()' -> Found issues in opening page"
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
            kwargs['pass_msg'] = "'open_guest_mgmt_page()' -> No issues in opening Guest Management page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'open_guest_mgmt_page()' -> Found issues in opening Guest Management page"
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
            kwargs['fail_msg'] = "'check_packet_capture_option()' -> Unsuccessfuly navigate to tools page"
            self.common_validation.fault(**kwargs)
            return -2
        else:
            pkt_cap = self.get_packet_capture_button()
            if pkt_cap == 1:
                kwargs['pass_msg'] = "'check_packet_capture_option()' -> No issues in opening Tools --> Packet " \
                                     "Capture page"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "'check_packet_capture_option()' -> Found issues in opening Tools --> Packet " \
                                     "Capture page"
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
            kwargs['pass_msg'] = "'check_config_error()' -> no error message after saving the config"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'check_config_error()' -> Found error message after saving the config"
            self.common_validation.failed(**kwargs)
            return -2

    def get_packet_capture_button(self, **kwargs):
        self.utils.print_info("Clicking on packet capture button...")
        cdg_ele = self.weh.get_element(self.packet_capture)
        sleep(2)
        if cdg_ele:
            self.auto_actions.click(cdg_ele)
            kwargs['pass_msg'] = "'get_packet_capture_button()' -> Successfully Get packet capture"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'get_packet_capture_button()' -> Unsuccessfully Get packet capture"
            self.common_validation.failed(**kwargs)
            return -2

    def _check_config_error_msg(self, **kwargs):
        self.utils.print_info("Checking error...")
        cdg_ele = self.weh.get_element(self.config_error)
        sleep(2)
        if cdg_ele.is_displayed():
            kwargs['fail_msg'] = "'_check_config_error_msg()' -> Got error..."
            self.common_validation.failed(**kwargs)
            return -2
        else:
            kwargs['pass_msg'] = "'_check_config_error_msg()' -> No Errors"
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
            kwargs['fail_msg'] = "'create_credential_distribution_groups()' -> User must be a member of a group."
            self.common_validation.failed(**kwargs)
            return -2

        if "Select at least one user group." in tool_tp_text:
            kwargs['fail_msg'] = "'create_credential_distribution_groups()' -> Select at least one user group."
            self.common_validation.failed(**kwargs)
            return -3

        if "That group already exists." in tool_tp_text:
            kwargs['fail_msg'] = "'create_credential_distribution_groups()' -> That group already exists."
            self.common_validation.failed(**kwargs)
            return -4

        if "The Member Group cannot be saved because the name " + member_of + " already exists.":
            kwargs['fail_msg'] = "'create_credential_distribution_groups()' -> The Member Group cannot be saved " \
                                 "because the name " + member_of + " already exists."
            self.common_validation.failed(**kwargs)
            return -5

        if "The Employee Group was saved successfully." in tool_tp_text:
            kwargs['pass_msg'] = "'create_credential_distribution_groups()' ->The Employee Group was saved successfully."
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "'create_credential_distribution_groups()' -> Failed to save the employee group."
        self.common_validation.failed(**kwargs)
        return -1
