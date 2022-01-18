"""
This class outlines all the constants for the home API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HomeConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HomeConstants(ApiConstants):
    def __init__(self):
        super(HomeConstants, self).__init__()
        self.CLOSE_OPERATION_PANEL = {"constant": "close_operation_panel",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.close_operation_panel}
        self.OPEN_OPERATION_PANEL = {"constant": "open_operation_panel",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.open_operation_panel}
        self.VERIFY_OPERATION_STATUS = {"constant": "verify_operation_status",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.verify_operation_status}
        self.WAIT_FOR_OPERATION = {"constant": "wait_for_operation",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.wait_for_operation}
