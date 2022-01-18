"""
This class outlines all the constants for the demo API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DemoConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DemoConstants(ApiConstants):
    def __init__(self):
        super(DemoConstants, self).__init__()
        self.GET_GUEST_USER_DATA = {"constant": "get_guest_user_data",
                                    "tags": ["COMMAND_REST"],
                                    "link": self.link.get_guest_user_data}
