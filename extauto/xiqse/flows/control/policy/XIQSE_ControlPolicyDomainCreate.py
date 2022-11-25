from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements

from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu
from xiqse.elements.control.policy.ControlPolicyDomainCreateWebElements import ControlPolicyDomainCreateWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainDelete import XIQSE_ControlPolicyDomainDelete
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpen import XIQSE_ControlPolicyDomainOpen


class XIQSE_ControlPolicyDomainCreate(ControlPolicyDomainCreateWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.openmanage_menu = XIQSE_ControlPolicyDomainOpenManageMenu()
        self.delete_domain_els = XIQSE_ControlPolicyDomainDelete()
        self.open_domain_els = XIQSE_ControlPolicyDomainOpen()

    def xiqse_control_policy_create_domain(self, domain_name):
        """
        - This keyword selects the "Create Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -   and create a new policy domain
        -   NOTE:  If the domain exists, then it will get deleted and then re-created.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse control policy create domain      <domain_name>

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # delete the domain, if exists
        # NOTE: 1 = exists,  -1 = does not exist
        domain_exists = self.open_domain_els.xiqse_control_policy_domain_exists(domain_name)
        if domain_exists == 1:
            self.utils.print_info(f"{domain_name} exists, deleting it. ")
            self.delete_domain_els.xiqse_control_policy_delete_domain(domain_name)

        # actions in the Create Domain process
        launch_create_domain_win = self.openmanage_menu.xiqse_control_policy_select_create_domain_menu()
        input_domain_name = self._input_domain_name(domain_name)
        click_ok_button = self._click_create_domain_ok()
        create_domain_success = self._create_domain_result(domain_name)

        if ( launch_create_domain_win and
                input_domain_name and
                click_ok_button and
                create_domain_success):
            ret_val = 1

        return ret_val

    def _click_create_domain_ok(self):
        """
        - click OK button in the Create Domain window
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        create_ok_bttn = self.get_create_domain_ok_button()
        if create_ok_bttn:
            ok_disabled = create_ok_bttn.get_attribute("aria-disabled")
            if ok_disabled == 'true':
                self.utils.print_info("'OK' button is disabled in Create Domain window")
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.get_create_domain_cancel_button)
            else:
                self.utils.print_info("Clicking 'OK' button in Create Domain window")
                self.auto_actions.click(create_ok_bttn)
                ret_val = 1
        else:
            self.utils.print_info("Unable to locate 'OK' button in Create Domain window")
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.get_create_domain_cancel_button)

        return ret_val

    def _create_domain_result(self, domain_name):
        """
        - Check if the new policy domain is getting created successfully or not
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        sleep(2)

        if self.get_create_domain_success_msg():
            self.utils.print_info("Clicking OK button in the 'Create Domain successful' dialog")
            self.auto_actions.click_reference(self.get_create_domain_success_ok_button)
            ret_val = 1
        elif self.get_create_domain_error_msg():
            self.utils.print_info(f"Policy domain name {domain_name} already exists")
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.get_create_domain_error_ok_button)
        else:
            self.utils.print_info("Create Domain confirmation message is not seen.")
            self.screen.save_screen_shot()

        return ret_val

    def _input_domain_name(self, domain_name):
        """
        - input the domain name to the Domain Name input field
        :param self:
        :return:
        """
        ret_val = -1
        domain_name_field = self.get_create_domain_domain_name_field()
        if domain_name_field:
            self.utils.print_info(f"Inputting new policy domain name - '{domain_name}'. ")
            self.auto_actions.send_keys(domain_name_field, domain_name)
            sleep(1)
            ret_val = 1
        else:
            self.utils.print_info("Unable to local the Domain Name input field in Create Domain window.")
            self.screen.save_screen_shot()

        return ret_val