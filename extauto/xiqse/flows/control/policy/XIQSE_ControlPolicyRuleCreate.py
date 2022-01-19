from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.control.policy.XIQSE_ControlPolicyService import XIQSE_ControlPolicyService
from xiqse.elements.control.policy.ControlPolicyRuleCreateWebElements import ControlPolicyRuleCreateWebElements


class XIQSE_ControlPolicyRuleCreate(ControlPolicyRuleCreateWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.serv_els = XIQSE_ControlPolicyService()

    def xiqse_control_policy_create_rule(self, rule_name, service_name, service_type="local"):
        """
        - This keyword creates a rule (local or global). Users need to specify which service the rule is in.
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
        # Launch Create Rule window:
        # For Local service: expand "Service Repository", and then "Global Services (All Domains)"
        # For Global service: expand "Service Repository", "Local Services" and then "Services"
        # And then select "Create Rule" from the popup menu of the selected user-defined service node
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
                self.serv_els.right_click_service_tree_node(service_name) and
                self._launch_create_rule_window() and
                self._create_rule(rule_name)):
            ret_val = 1
            self.utils.print_info(f"Successfully created '{service_type}' rule - {rule_name}")
            sleep(1)
        return ret_val

    def _launch_create_rule_window(self):
        ret_val = -1
        create_menu = self.get_create_rule_menu()
        if create_menu:
            self.utils.print_info("Launching the 'Create Rule' window")
            self.auto_actions.click(create_menu)
            ret_val = 1
        else:
            self.utils.print_info("Unable to launch the 'Create Rule' window")
        return ret_val

    def _create_rule(self, rule_name):
        ret_val = -1
        input_name = self.get_name_input()
        if input_name:
            self.utils.print_info(f"Entering '{rule_name}' in the Name input field in Create Rule window")
            self.auto_actions.send_keys(input_name, rule_name)
            self._click_ok_button()
            ret_val = 1
            # noticed that it takes a bit of time to dismiss the Create Rule window.
            # without this delay, the next action (e.g. "Save Domain") may not get initiated successfully.
            sleep(1)
        else:
            self.utils.print_info(f"Unable to find 'Name' input field in Create Rule window")
            self.screen.save_screen_shot()
        return ret_val

    def _click_ok_button(self):
        ret_val = -1
        ok_bttn = self.get_ok_button()
        if ok_bttn:
            self.utils.print_info(f"Clicking the 'OK' button in Create Rule window")
            self.auto_actions.click(ok_bttn)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to locate the 'OK' button in Create Rule window")
            self.screen.save_screen_shot()
        return ret_val
