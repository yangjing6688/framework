"""
This class outlines all the constants for the network API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NetworkConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NetworkConstants(ApiConstants):
    def __init__(self):
        super(NetworkConstants, self).__init__()
        self.NETWORK_SELECT_SUB_TAB = {"constant": "network_select_sub_tab",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.network_select_sub_tab}
