from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements

from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu import XIQSE_ControlPolicyDomainOpenManageMenu
from xiqse.elements.control.policy.ControlPolicyDomainDeleteWebElements import ControlPolicyDomainDeleteWebElements


class XIQSE_ControlPolicyDomainDelete(ControlPolicyDomainDeleteWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()
        self.openmanage_menu = XIQSE_ControlPolicyDomainOpenManageMenu()

    def xiqse_control_policy_delete_domain(self, domain_name):
        """
        - This keyword selects the "Delete Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -   and delete the specified policy domain
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse control policy delete domain      <domain_name>

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        launch_delete_domain_win = self.openmanage_menu.xiqse_control_policy_select_delete_domain_menu()
        select_domain = self._delete_domain_select_domain_from_menu(domain_name)

        if launch_delete_domain_win == 1:
            if select_domain == 1:
                ret_val = 1
                self._delete_domain_ok()
                self._delete_domain_are_you_sure()
                self._delete_domain_confirm_success()

        return ret_val

    def _delete_domain_select_domain_from_menu(self, domain_name):
        """
        - Select the policy domain name from the Domain list (or dropdown menu)
        :return:
        """
        ret_val = -1

        domain_list = self.get_delete_domain_name_list()
        if domain_list:
            self.utils.print_info("Expand the domain name list in the Delete Domain window.")
            self.auto_actions.click(domain_list)
            sleep(2)

            delete_domain_name = self.select_delete_domain_name(domain_name)
            if delete_domain_name:
                self.utils.print_info("Selecting the domain name from the domain name list (or dropdown menu).")
                self.auto_actions.click(delete_domain_name)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to locate the domain name '{domain_name}' on the dropdown menu in Delete Domain window.")
                self.screen.save_screen_shot()

                # dismiss/Close the "Delete Domain" window
                # click dropdowm menu again to dismiss it so that the buttons in the Delete Domain window can be accessed.
                self.auto_actions.click(domain_list)
                delete_domain_close = self.get_delete_domain_close_button()
                if delete_domain_close:
                    # Click Close button in the Delete Success dialog
                    self.utils.print_info("Clicking 'Close' button to close the Delete Domain dialog.")
                    self.auto_actions.click(delete_domain_close)
                else:
                    self.utils.print_info("Unable to locate 'Close' button in Delete Domain dialog.")
        else:
            self.utils.print_info("Cannot expand the domain name list in the dropdown menu.")
            self.screen.save_screen_shot()

        return ret_val

    def _delete_domain_ok(self):
        """
        - Click OK button in the Delete Domain window
        :return:  none
        """

        # found policy domain from the Domain field dropdown menu. Go ahead and delete it.
        delete_domain_ok_bttn = self.get_delete_domain_ok()
        if delete_domain_ok_bttn:
            self.utils.print_info("Clicking OK button in the Delete Domain window.")
            self.auto_actions.click(delete_domain_ok_bttn)
        else:
            self.utils.print_info("Unable to locate 'OK' button in Delete Domain window.")
            self.screen.save_screen_shot()

    def  _delete_domain_are_you_sure(self):
        """
        - Confirm to go ahead and delete the domain.
        :return:
        """
        ret_val = -1

        # Click Yes button in Are You Sure dialog
        delete_domain_yes = self.get_delete_domain_yes_button()
        if delete_domain_yes:
            self.utils.print_info("Clicking Yes button in the 'Are You Sure' dialog.")
            self.auto_actions.click(delete_domain_yes)
            ret_val = 1
        else:
            self.utils.print_info("Unable to locate 'Yes' button in 'Delete Domain - Are You Sure?' dialog.")
            self.screen.save_screen_shot()

        return ret_val

    def _delete_domain_confirm_success(self):
        """
        - Confirm that the domain is deleted successfully.
        :return:
        """
        ret_val = -1
        sleep(1)

        delete_domain_confirm_ok = self.get_delete_domain_confirm_ok()
        if delete_domain_confirm_ok:
            # Click OK button in the Delete Success dialog
            self.utils.print_info("Clicking OK button in the 'Domain deleted successfully' dialog.")
            self.auto_actions.click(delete_domain_confirm_ok)
            ret_val = 1
        else:
            self.utils.print_info("Unable to locate 'OK' button in Domain Deleted Successfully dialog.")
            self.screen.save_screen_shot()

        return ret_val