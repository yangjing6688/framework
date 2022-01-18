"""
This class outlines all the constants for the unittest API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(UnittestConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class UnittestConstants(ApiConstants):
    def __init__(self):
        super(UnittestConstants, self).__init__()
        self.FUNCTION = {"constant": "function",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.function}
