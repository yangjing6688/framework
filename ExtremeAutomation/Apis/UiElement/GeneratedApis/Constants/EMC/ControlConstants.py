"""
This class outlines all the constants for the control API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ControlConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ControlConstants(ApiConstants):
    def __init__(self):
        super(ControlConstants, self).__init__()
        self.CONTROL_SELECT_SUB_TAB = {"constant": "control_select_sub_tab",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.control_select_sub_tab}
