from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyWebElementsDefinitions import ControlPolicyWebElementsDefinitions
from string import Template
class ControlPolicyWebElements(ControlPolicyWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_accordian_tab(self, title):
        return self.weh.get_template_element(self.accordian_tab_template, title=title)

    def get_devices_port_groups_tab(self):
        return self.weh.get_template_element(self.devices_port_groups_tab)

    def get_delete_menu_action(self):
        return self.weh.get_template_element(self.menu_action_template, action="Delete")

    def is_tree_node_expanded(self, nodeName):
        """
        DESC:  is the node in the tree panel expanded?
        :return:  returns 'true' if expanded, else returns 'false'
        """
        return self.weh.get_template_element(self.root_tree_expanded_template, rootName=nodeName, isExpanded="true")

    def get_tree_node_expander_arrow(self, nodeName):
        """
        DESC:  get the expand arrow on a given tree node
        :return:  returns expander arrow
        """
        return self.weh.get_template_element(self.root_tree_expander_arrow_template, rootName=nodeName)

    def get_tree_node(self, nodeName):
        """
        :return: the node in the tree panel
        """
        return self.weh.get_template_element(self.root_tree_node_template, rootName=nodeName)

    def get_cached_unsaved_changes_window(self,):
        """
        :return: the "Cached Policy Domain - Unsaved Changes" window'
        """
        return self.weh.get_template_element(self.cached_unsaved_changes_window)

    def get_cached_unsaved_changes_no_button(self,):
        """
        :return: the No button in "Cached Policy Domain - Unsaved Changes" window'
        """
        return self.weh.get_template_element(self.cached_unsaved_changes_no_button)

    def get_cached_unsaved_changes_ok_button(self,):
        """
        :return: the OK button in "Cached Policy Domain - Unsaved Changes" window'
        """
        return self.weh.get_template_element(self.cached_unsaved_changes_ok_button)
