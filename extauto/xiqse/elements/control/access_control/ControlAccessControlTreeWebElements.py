from xiqse.defs.control.access_control.ControlAccessControlTreeWebElementsDefinitions import ControlAccessControlTreeWebElementsDefinitions
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.WebElementHandler import WebElementHandler

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
