from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements

from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu
from xiqse.elements.control.policy.ControlPolicyDomainOpenWebElements import ControlPolicyDomainOpenWebElements


class XIQSE_ControlPolicyDomainOpen(ControlPolicyDomainOpenWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.openmanage_menu = XIQSE_ControlPolicyDomainOpenManageMenu()

    def xiqse_control_policy_domain_exists(self, domain_name):
        """
         - This keyword checks if a domain exists in the Policy Manager database
         - It is assumed that the current view is Control>Policy.
         - Keyword Usage
         -     xiqse control policy domain exists      <domain_name>

        :return: 1 if domain exists, else -1
        """
        ret_val = -1

        self.openmanage_menu.xiqse_control_policy_select_open_domain_menu()

        domain_exists = self.get_domain_name(domain_name)
        self.utils.print_info(f"get_domain_name({domain_name}) - {domain_exists}")
        if domain_exists:
            self.utils.print_info(f"Policy domain {domain_name} exists in the Policy Manager database.")
            ret_val = 1
        else:
            self.utils.print_info(f"Policy domain {domain_name} does not exist in the Policy Manager database.")
            self.screen.save_screen_shot()

        # collapse (or reset) the Open/Manage Domain(s) menu
        self.openmanage_menu.xiqse_control_policy_select_openmanage_domains()

        return ret_val

    def xiqse_control_policy_open_domain(self, domain_name):
        """
         - This keyword opens an existing domain, if exists
         - It is assumed that the current view is Control>Policy.
         - Keyword Usage
         -     xiqse control policy open domain      <domain_name>

        :return: 1 if domain is open successfully, else -1
        """
        ret_val = -1

        self.openmanage_menu.xiqse_control_policy_select_open_domain_menu()

        domain_exists = self.get_domain_name(domain_name)
        if domain_exists:
            self.utils.print_info(f"Policy domain {domain_name} exists.  Opening it...")
            self.auto_actions.click(domain_exists)
            ret_val = 1
        else:
            self.utils.print_info(f"Policy domain {domain_name} does not exist in the Policy Manager database.")
            self.screen.save_screen_shot()

        return ret_val
