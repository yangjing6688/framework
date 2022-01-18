"""
This class outlines all the constants for the gvrp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GvrpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GvrpConstants(ApiConstants):
    def __init__(self):
        super(GvrpConstants, self).__init__()
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_port}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_port}
        self.SHOW_STATE = {"constant": "show_state",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_state}
        self.SHOW_STATE_PORT = {"constant": "show_state_port",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_state_port}
