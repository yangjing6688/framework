from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.policy.ControlPolicyWebElements import ControlPolicyWebElements
from xiqse.elements.control.policy.ControlPolicyCreateRoleWebElements import ControlPolicyCreateRoleWebElements
from xiqse.elements.control.policy.ControlPolicyRoleTreeWebElements import ControlPolicyRoleTreeWebElements
from xiqse.elements.control.policy.ControlPolicyRoleDetailsWebElements import ControlPolicyRoleDetailsWebElements


class XIQSE_ControlPolicyRole(ControlPolicyRoleDetailsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.policy_elements = ControlPolicyWebElements()
        self.role_tree_elements = ControlPolicyRoleTreeWebElements()
        self.create_role_elements = ControlPolicyCreateRoleWebElements()

    def _right_click_roles_tree(self):
        ret_val = -1
        roles_node = self.role_tree_elements.get_roles_tree_node()
        if roles_node:
            self.utils.print_info(f"Right Clicking 'Roles' node in the Control->Policy->Roles tree")
            ret_val = self.auto_actions.right_click(roles_node)
        else:
            self.utils.print_info(f"Unable to find 'Roles' node in the Control->Policy->Roles tree")
            self.screen.save_screen_shot()
        return bool(ret_val > -1)

    def _click_create_role_action(self):
        ret_val = -1
        create_role_action = self.role_tree_elements.get_create_role_menu_action()
        if create_role_action:
            self.utils.print_info(f"Selecting 'Create Role...' action in the Control->Policy->Roles tree menu")
            ret_val = self.auto_actions.click(create_role_action)
            sleep(2)
        else:
            self.utils.print_info(f"Unable to find 'Create Role' action in the Control->Policy->Roles tree menu")
            self.screen.save_screen_shot()
        return bool(ret_val > -1)

    def _verify_create_role_window(self):
        self.utils.print_info(f"Verifying 'Create Role' window is displayed")
        create_role_window = self.create_role_elements.get_window()
        if create_role_window:
            self.utils.print_info(f"Found 'Create Role' window")
            return True
        else:
            self.utils.print_info(f"Unable to find 'Create Role' window")
            self.screen.save_screen_shot()
            return False

    def _enter_create_role_name(self, name):
        ret_val = -1
        name_input = self.create_role_elements.get_name_input()
        if (name_input):
            self.utils.print_info(f"Entering '"+name+"' in Create Role Window Name input field")
            ret_val = self.auto_actions.send_keys(name_input, name)
            sleep(2)
        else:
            self.utils.print_info(f"Unable to find 'Name' input field in Create Role Window")
            self.screen.save_screen_shot()

        return bool(ret_val > -1)

    def _click_create_role_ok(self):
        ret_val = -1
        ok_button = self.create_role_elements.get_ok_button()
        if (ok_button):
            self.utils.print_info(f"Clicking 'OK' button in Create Role Window")
            ret_val = self.auto_actions.click(ok_button)
        else:
            self.utils.print_info(f"Unable to find 'OK' button in Create Role Window")
            self.screen.save_screen_shot()
        return bool(ret_val > -1)

    def xiqse_control_policy_create_role(self, name):
        ret_val = -1
        if (self._right_click_roles_tree() and 
            self._click_create_role_action() and
            self._verify_create_role_window() and
            self._enter_create_role_name(name) and
            self._click_create_role_ok()):
            ret_val = 1
        return ret_val

    def _expand_roles_tree(self):
        ret_val = -1
        self.utils.print_info(f"Checking if Control->Policy->Roles/Services->Roles tree is expanded")
        if self.role_tree_elements.is_roles_tree_expanded():
            ret_val = 1
        else:
            expander = self.role_tree_elements.get_roles_tree_expander_arrow()
            if expander:
                self.utils.print_info(f"Expanding Control->Policy->Roles/Services->Roles tree")
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find Control->Policy->Roles/Services->Roles tree expander arrow")
                self.screen.save_screen_shot()
        return ret_val

    def _right_click_role_tree_node(self, name):
        ret_val = -1
        role_node = self.role_tree_elements.get_role_tree_node(name)
        if role_node:
            self.utils.print_info(f"Right Clicking '"+name+"' node in the Control->Policy->Roles tree")
            ret_val = self.auto_actions.right_click(role_node)
            sleep(2)
        return bool(ret_val > -1)

    def _click_delete_menu_action(self):
        ret_val = -1
        delete_role_action = self.policy_elements.get_delete_menu_action()
        if delete_role_action:
            self.utils.print_info(f"Selecting 'Delete' action in the Control->Policy tree node menu")
            ret_val = self.auto_actions.click(delete_role_action)
            sleep(2)
        else:
            self.utils.print_info(f"Unable to find 'Delete' action in Control->Policy tree node menu")
            self.screen.save_screen_shot()
        return bool(ret_val > -1)

    def _click_confirm_delete_yes(self):
        ret_val = -1
        confirm_yes_button = self.role_tree_elements.get_confirm_delete_yes_button()
        if confirm_yes_button:
            self.utils.print_info(f"Clicking 'Yes' button in the Control->Policy->Confirm Delete dialog")
            ret_val = self.auto_actions.click(confirm_yes_button)
            sleep(2)
        else:
            self.utils.print_info(f"Unable to find 'Yes' button in 'Confirm Delete' dialog")
            self.screen.save_screen_shot()
        return bool(ret_val > -1)

    def xiqse_control_policy_delete_role(self, name):
        """

        """
        ret_val = -1
        if (self._expand_roles_tree() and
            self._right_click_role_tree_node(name) and 
            self._click_delete_menu_action() and
            self._click_confirm_delete_yes()):
            ret_val = 1
        return ret_val
