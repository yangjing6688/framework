from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.AccesscontrolConstants import AccesscontrolConstants


class UiAccessControlKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAccessControlKeywords, self).__init__()
        self.api_const = self.constants.API_ACCESS_CONTROL
        self.command_const = AccesscontrolConstants()

    def access_control_click_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of access_control_click_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args, self.command_const.ACCESS_CONTROL_CLICK_TREE_PANEL, **kwargs)

    def access_control_expand_node(self, element_name, tree_name, node_name, **kwargs):
        """Returns the result of access_control_expand_node."""
        args = {"tree_name": tree_name,
                "node_name": node_name}

        return self.execute_keyword(element_name, args, self.command_const.ACCESS_CONTROL_EXPAND_NODE, **kwargs)

    def access_control_select_node(self, element_name, tree_name, node_name, **kwargs):
        """Returns the result of access_control_select_node."""
        args = {"tree_name": tree_name,
                "node_name": node_name}

        return self.execute_keyword(element_name, args, self.command_const.ACCESS_CONTROL_SELECT_NODE, **kwargs)

    def access_control_collapse_node(self, element_name, tree_name, node_name, **kwargs):
        """Returns the result of access_control_collapse_node."""
        args = {"tree_name": tree_name,
                "node_name": node_name}

        return self.execute_keyword(element_name, args, self.command_const.ACCESS_CONTROL_COLLAPSE_NODE, **kwargs)

    def access_control_enforce_all(self, element_name, **kwargs):
        """Returns the result of access_control_enforce_all."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ACCESS_CONTROL_ENFORCE_ALL, **kwargs)

    def access_control_click_refresh_button(self, element_name, **kwargs):
        """Returns the result of access_control_click_refresh_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ACCESS_CONTROL_CLICK_REFRESH_BUTTON,
                                    **kwargs)
