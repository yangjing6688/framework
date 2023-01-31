from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.control.policy.ControlPolicyWebElementsDefinitions import ControlPolicyWebElementsDefinitions
from xiqse.defs.control.policy.ControlPolicyRoleTreeWebElementsDefinitions import ControlPolicyRoleTreeWebElementsDefinitions
class ControlPolicyRoleTreeWebElements(ControlPolicyRoleTreeWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()
        self.policy = ControlPolicyWebElementsDefinitions()

    def get_roles_tree_node(self):
        return self.weh.get_template_element(self.policy.root_tree_node_template, rootName="Roles")

    def is_roles_tree_expanded(self):
        return bool(self.weh.get_template_element(self.policy.root_tree_expanded_template, rootName="Roles", isExpanded="true"))

    def get_roles_tree_expander_arrow(self):
        return self.weh.get_template_element(self.policy.root_tree_expander_arrow_template, rootName="Roles")

    def get_create_role_menu_action(self):
        return self.weh.get_template_element(self.policy.menu_action_template, action="Create Role")

    def get_create_role_name_input(self):
        return self.weh.get_element(self.create_role_window_name_input)

    def get_role_tree_node(self, name):
        return self.weh.get_template_element(self.role_tree_node_template, roleName=name)

    def get_confirm_delete_yes_button(self):
        return self.weh.get_element(self.confirm_delete_yes_button)
