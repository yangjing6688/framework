"""
This class outlines all the constants for the administration API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AdministrationConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AdministrationConstants(ApiConstants):
    def __init__(self):
        super(AdministrationConstants, self).__init__()
        self.ADMINISTRATION_SELECT_SUB_TAB = {"constant": "administration_select_sub_tab",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.administration_select_sub_tab}
