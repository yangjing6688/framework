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

    def _search_management_account(self, email_addr):
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

    def _search_guest_accounts(self):
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

    def _search_guest_account(self, email_addr):
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

    @deprecated('Please use the {create_role_based_account} keyword in '
                'keywords/gui/account_management/KeywordsAccountManagement.py'
                'This method can be removed after 7/1/2023')
    def create_role_based_account(self, account_config, **kwargs):
        return self.gui_create_role_based_account(account_config, **kwargs)

    def gui_create_role_based_account(self, account_config, **kwargs):
        """
        - Creates an account based on the arguments from rbac_config.robot
        - &{OPERATOR_ROLE}, &{MONITOR_ROLE}, &{HELPDESK_ROLE}, &{Guest_Management_Role}, &{Observer_Role}
        - Flow : User account image-->Global Settings--> Account Management
        - Keyword Usage
        - ``Create Role Based Account  &{ACCOUNT_CONFIGS}``

        :param account_config: (dict) include email, name, timeout, role, organization, location
        :return: 1 if there is no error
        """

        self.utils.print_info(account_config)
        email = account_config.get('email')
        name = account_config.get('name')
        timeout = account_config.get('timeout')
        role = account_config.get('role')
        # Commented on 1/18/23 because it is unused
        #location = account_config.get('location')
        organization = account_config.get('organization')

        self.utils.print_info("Navigating to the account Management page..")
        self.navigator.navigate_to_account_mgmt()
        sleep(2)

        self.utils.print_info("Deleting the account if exists")
        if self._search_management_account(email):
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
            location_checkbox_selected = self.get_rbac_location_tree_checkbox_selected_status()
            if not location_checkbox_selected:
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
                kwargs['fail_msg'] = f"{text}"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['pass_msg'] = "Successfully created role based account"
        self.common_validation.passed(**kwargs)
        return 1

    @deprecated('Please use the {delete_management_account} keyword in '
                'keywords/gui/account_management/KeywordsAccountManagement.py'
                'This method can be removed after 7/1/2023')
    def delete_management_account(self, email_addr, **kwargs):
        return self.gui_delete_management_account(email_addr, **kwargs)

    def gui_delete_management_account(self, email_addr, **kwargs):
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

        if row := self._search_management_account(email_addr):
            self.utils.print_info(f"Deleting {email_addr} account")
            self.auto_actions.click(self.get_account_mgmt_grid_row_check_box(row))
            sleep(2)
            self.utils.print_info("click on delete button")
            self.auto_actions.click_reference(self.get_account_mgmt_delete_button)
            sleep(1)
            self.auto_actions.click_reference(self.get_account_mgmt_delete_conf_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "Account found on grid and got deleted successfully"
            self.common_validation.passed(**kwargs)
            return 1

    @deprecated('Please use the {delete_guest_management_accounts} keyword in '
                'keywords/gui/account_management/KeywordsAccountManagement.py'
                'This method can be removed after 7/1/2023')
    def delete_guest_management_accounts(self, **kwargs):
        return self.gui_delete_guest_management_accounts(**kwargs)

    def gui_delete_guest_management_accounts(self, **kwargs):
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

        if row := self._search_guest_accounts():
            self.utils.print_info("Deleting Guest account")
            for row_guest in row:
                self.auto_actions.click(self.get_account_mgmt_grid_row_check_box(row_guest))
            sleep(2)
            self.utils.print_info("click on delete button")
            self.auto_actions.click_reference(self.get_account_mgmt_delete_button)
            sleep(1)
            self.auto_actions.click_reference(self.get_account_mgmt_delete_conf_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "Account found on grid and got deleted successfully"
            self.common_validation.passed(**kwargs)
            return 1

    def _open_tools_page(self, **kwargs):
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

    def _get_packet_capture_button(self, **kwargs):
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
