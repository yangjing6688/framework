from common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyWebElementsDefinitions import ControlPolicyWebElementsDefinitions
from xiqse.defs.control.policy.ControlPolicyServiceTreeWebElementsDefinitions import ControlPolicyServiceTreeWebElementsDefinitions


class ControlPolicyServiceTreeWebElements(ControlPolicyServiceTreeWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()
        self.policy = ControlPolicyWebElementsDefinitions()

    def get_service_tree_node(self, node_name):
        """
        :return: the service node in the Services tree panel
        """
        return self.weh.get_template_element(self.policy.root_tree_node_template, rootName=node_name)

    def is_service_tree_node_expanded(self, node_name):
        """
        DESC:  is the Service node in the Services tree panel expanded?
        :return:  returns 'true' if expanded, else returns 'false'
        """
        return self.weh.get_template_element(self.policy.root_tree_expanded_template, rootName=node_name, isExpanded="true")

    def get_service_tree_node_expander_arrow(self, node_name):
        """
        DESC:  get the expand arrow on a given Service tree node
        :return:  returns expander arrow
        """
        return self.weh.get_template_element(self.policy.root_tree_expander_arrow_template, rootName=node_name)
