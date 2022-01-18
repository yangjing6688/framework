"""
This class outlines all the constants for the unit API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(UnitConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class UnitConstants(ApiConstants):
    def __init__(self):
        super(UnitConstants, self).__init__()
        self.CHANGE_CURRENT_SLOT = {"constant": "change_current_slot",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.change_current_slot}
        self.EXIT_CURRENT_SLOT = {"constant": "exit_current_slot",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.exit_current_slot}
