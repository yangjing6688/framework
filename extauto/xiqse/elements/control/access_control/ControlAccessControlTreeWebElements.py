from xiqse.defs.control.access_control.ControlAccessControlTreeWebElementsDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class ControlAccessControlTreeWebElements(ControlAccessControlTreeWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def get_engines_tree_node(self, treenode):
        """
        :return: Tree Node Selection in the Access Control Tree
        """
        return self.weh.get_template_element(self.engines_tree_node, element_name=treenode)

