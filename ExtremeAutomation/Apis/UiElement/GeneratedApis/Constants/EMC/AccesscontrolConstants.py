"""
This class outlines all the constants for the accesscontrol API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AccesscontrolConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AccesscontrolConstants(ApiConstants):
    def __init__(self):
        super(AccesscontrolConstants, self).__init__()
        self.ACCESS_CONTROL_CLICK_REFRESH_BUTTON = {"constant": "access_control_click_refresh_button",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.access_control_click_refresh_button}
        self.ACCESS_CONTROL_CLICK_TREE_PANEL = {"constant": "access_control_click_tree_panel",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.access_control_click_tree_panel}
        self.ACCESS_CONTROL_COLLAPSE_NODE = {"constant": "access_control_collapse_node",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.access_control_collapse_node}
        self.ACCESS_CONTROL_ENFORCE_ALL = {"constant": "access_control_enforce_all",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.access_control_enforce_all}
        self.ACCESS_CONTROL_EXPAND_NODE = {"constant": "access_control_expand_node",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.access_control_expand_node}
        self.ACCESS_CONTROL_SELECT_NODE = {"constant": "access_control_select_node",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.access_control_select_node}
