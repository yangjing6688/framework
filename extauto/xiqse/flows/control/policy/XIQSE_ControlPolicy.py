from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.policy.ControlPolicyWebElements import ControlPolicyWebElements
from xiqse.elements.control.policy.ControlPolicyRoleTreeWebElements import ControlPolicyRoleTreeWebElements
from xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave import XIQSE_ControlPolicyDomainSave


class XIQSE_ControlPolicy(ControlPolicyWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.role_tree = ControlPolicyRoleTreeWebElements()
        self.domain_save = XIQSE_ControlPolicyDomainSave()

    def xiqse_control_policy_select_tab(self, tab_name):
        the_tab = None
        if tab_name == "Devices/Port Groups":
            the_tab = self.get_devices_port_groups_tab()
        else:
            the_tab = self.get_accordian_tab(tab_name)
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Control->Policy page")
            self.auto_actions.click(the_tab)
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Control->Policy page")
            self.screen.save_screen_shot()

    def xiqse_control_policy_select_tree_node(self, node_name):
        """
        - This keyword selects the specified tab in the main navigation panel
        - Keyword Usage
        - ``XIQSE Policy Tree Node Select    Roles``
        :param node_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        the_node = None
        if node_name == "Roles":
            the_node = self.role_tree.get_roles_tree_node()
        elif node_name == "Class of Service":
            the_node = self.role_tree.get_class_of_service_node()
        if the_node:
            self.utils.print_info(f"Selecting '{node_name}' node in Control->Policy tree panel")
            self.auto_actions.click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select node with name '{node_name}' in Control->Policy tree panel")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_control_policy_dismiss_cached_window(self):
        """
        - This keyword dismisses the "Cached Policy Domain - Unsaved Changes" window, if present
        - Keyword Usage
        - ``XIQSE Control Policy Dismiss Cached Window
        :param none
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        cache_win = self.get_cached_unsaved_changes_window()
        if cache_win:
            self.utils.print_info("Detected the 'Cached Policy Domain - Unsaved Changes' window.  Dismissing it")
            self._click_ok_button()
            self.utils.print_info("Perform 'Save Domain', to avoid the window from popping up again.")
            self.domain_save.xiqse_control_policy_save_domain()
            ret_val = 1
        else:
            self.utils.print_info("The 'Cached Policy Domain - Unsaved Changes' window is not detected.  Continue...")
        return ret_val

    def _click_ok_button(self):
        ret_val = -1
        ok_bttn = self.get_cached_unsaved_changes_ok_button()
        if ok_bttn:
            self.utils.print_info("Clicking the 'OK' button in Dismiss Cache window")
            self.auto_actions.click(ok_bttn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to locate the 'OK' button in Dismiss Cache window")
            self.screen.save_screen_shot()
        return ret_val
