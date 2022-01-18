"""
This class outlines all the constants for the ewcleftnavipanel API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcleftnavipanelConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcleftnavipanelConstants(ApiConstants):
    def __init__(self):
        super(EwcleftnavipanelConstants, self).__init__()
        self.LEFT_NAVI_PANEL_COLLAPSE_TREE_NODE_IN_SECTION = {"constant": "left_navi_panel_collapse_tree_node_in_section",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.left_navi_panel_collapse_tree_node_in_section}
        self.LEFT_NAVI_PANEL_EXPAND_TREE_NODE_IN_SECTION = {"constant": "left_navi_panel_expand_tree_node_in_section",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.left_navi_panel_expand_tree_node_in_section}
        self.LEFT_NAVI_PANEL_SELECT_LINK_IN_SECTION = {"constant": "left_navi_panel_select_link_in_section",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.left_navi_panel_select_link_in_section}
        self.LEFT_NAVI_PANEL_SELECT_SECTION_TAB = {"constant": "left_navi_panel_select_section_tab",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.left_navi_panel_select_section_tab}
