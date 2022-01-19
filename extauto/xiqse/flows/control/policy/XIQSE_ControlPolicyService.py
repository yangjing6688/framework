from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.policy.ControlPolicyWebElements import ControlPolicyWebElements
from xiqse.elements.control.policy.ControlPolicyServiceTreeWebElements import ControlPolicyServiceTreeWebElements
from xiqse.elements.control.policy.ControlPolicyServiceDetailsWebElements import ControlPolicyServiceDetailsWebElements


class XIQSE_ControlPolicyService(ControlPolicyServiceDetailsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.policy_elements = ControlPolicyWebElements()
        self.serv_tree_elements = ControlPolicyServiceTreeWebElements()

    def right_click_service_tree_node(self, node_name):
        ret_val = -1
        serv_node = self.serv_tree_elements.get_service_tree_node(node_name)
        if serv_node:
            self.utils.print_info(f"Right Clicking '{node_name}' service node in the Control->Policy->Services tree")
            # without this delay, the right-click action does not seem to work.  the right click brings up the popup
            # menu for the page (e.g. Open Link, Inspect), instead of the node action (e.g. create/delete/rename). Strange!!
            # try to get around this issue by clicking on the node first, the delay, and then do the right-click
            self.auto_actions.click(serv_node)
            sleep(1)
            self.auto_actions.right_click(serv_node)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find '{node_name}' service node in the Control->Policy->Services tree")
            self.screen.save_screen_shot()
        return ret_val

    def expand_service_tree_node(self, node_name):
        ret_val = -1
        if self.serv_tree_elements.is_service_tree_node_expanded(node_name):
            self.utils.print_info(f"Control->Policy->'{node_name}' tree node is already expanded.")
            ret_val = 1
        else:
            expander = self.serv_tree_elements.get_service_tree_node_expander_arrow(node_name)
            if expander:
                self.utils.print_info(f"Expanding Control->Policy->Service tree node '{node_name}'")
                self.auto_actions.click(expander)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find Control->Policy->Service tree node expander arrow for '{node_name}'")
                self.screen.save_screen_shot()
        return ret_val

    def collapse_service_tree_node(self, node_name):
        ret_val = -1
        if self.serv_tree_elements.is_service_tree_node_expanded(node_name):
            expander = self.serv_tree_elements.get_service_tree_node_expander_arrow(node_name)
            if expander:
                self.utils.print_info(f"Collapsing Control->Policy->Service tree node '{node_name}'")
                self.auto_actions.click(expander)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find Control->Policy->Service tree node expander arrow for '{node_name}'")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info(f"Control->Policy->'{node_name}' tree node is already collapsed.")
            ret_val = 1
        return ret_val
