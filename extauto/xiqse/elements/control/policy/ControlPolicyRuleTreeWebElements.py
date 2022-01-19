from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyWebElementsDefinitions import ControlPolicyWebElementsDefinitions
from xiqse.defs.control.policy.ControlPolicyRuleTreeWebElementsDefinitions import ControlPolicyRuleTreeWebElementsDefinitions


class ControlPolicyRuleTreeWebElements(ControlPolicyRuleTreeWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()
        self.policy = ControlPolicyWebElementsDefinitions()

    def get_rule_tree_node(self, node_name):
        """
        :return: the rule node in the tree panel
        """
        return self.weh.get_template_element(self.policy.root_tree_node_template, rootName=node_name)
