"""
This class outlines all the constants for the vxlan API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VxlanConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VxlanConstants(ApiConstants):
    def __init__(self):
        super(VxlanConstants, self).__init__()
        self.CHECK_LOGICAL_SWITCH_EXISTS = {"constant": "check_logical_switch_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_logical_switch_exists}
