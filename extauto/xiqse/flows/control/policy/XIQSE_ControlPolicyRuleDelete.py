from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.control.policy.XIQSE_ControlPolicyService import XIQSE_ControlPolicyService
from xiqse.elements.control.policy.ControlPolicyRuleDeleteWebElements import ControlPolicyRuleDeleteWebElements


class XIQSE_ControlPolicyRuleDelete(ControlPolicyRuleDeleteWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.serv_els = XIQSE_ControlPolicyService()

    def xiqse_control_policy_delete_rule(self, rule_name, service_name, service_type="local"):
        """
        - This keyword deletes a rule (local or global). Users need to specify which service the rule is in.
        - IMPORTANT NOTE:
        -   I think accessing tree nodes (e.g. select, right-click, expand, etc) in Roles/Services/Rules trees are the same.
        -   Since I already have the methods created in Service files, I use them to access the rule nodes for now.
        -   These methods can be rolled up to the ControlPolicy level, if time allows.
        :param rule_name:
        :param service_name:
        :param service_type: local or global
        :return: 1 if success, else -1
        """
        ret_val = -1
        go = 1

        # actions:
        # For Local service: expand "Service Repository", "Local Services", "Services" and then a service
        # For Global service: expand "Service Repository", "Services" and then a service
        # And then select "Delete" from the popup menu of the selected rule
        if self.serv_els.expand_service_tree_node("Service Repository"):
            if service_type == "global":
                self.serv_els.expand_service_tree_node("Global Services (All Domains)")
                self.serv_els.collapse_service_tree_node("Local Services")
            elif service_type == "local":
                self.serv_els.expand_service_tree_node("Local Services")
                self.serv_els.collapse_service_tree_node("Global Services (All Domains)")
            else:
                self.utils.print_info("Unknown service type.  A service should either be 'local' or 'global')")
                go = -1
        if (go == 1 and
                self.serv_els.expand_service_tree_node("Services") and
                self.serv_els.expand_service_tree_node(service_name) and
                self.serv_els.right_click_service_tree_node(rule_name) and
                self._delete_rule()):
            ret_val = 1
            self.utils.print_info(f"Successfully deleted '{service_type}' rule - {rule_name}")
            sleep(1)
        return ret_val

    def _delete_rule(self):
        ret_val = -1
        del_menu = self.get_delete_rule_menu()
        if del_menu:
            self.utils.print_info("Selecting 'Delete' menu option from the popup menu of a rule")
            self.auto_actions.click(del_menu)
            # check for the "Confirm Delete" window
            confirm_win = self.get_confirm_window()
            if confirm_win:
                self._click_yes_button()
                ret_val = 1
        else:
            self.utils.print_info("Unable to locate 'Delete' menu option from the popup menu on a rule")
            self.screen.save_screen_shot()
        return ret_val

    def _click_yes_button(self):
        ret_val = -1
        yes_bttn = self.get_yes_button()
        if yes_bttn:
            self.utils.print_info("Clicking the 'Yes' button in Confirm Delete dialog")
            self.auto_actions.click(yes_bttn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to locate the 'Yes' button in Confirm Delete dialog")
            self.screen.save_screen_shot()
        return ret_val
