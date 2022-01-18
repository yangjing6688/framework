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
        self.CHECK_GVRP_STATE = {"constant": "check_gvrp_state",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.check_gvrp_state}
        self.CHECK_GVRP_STATE_PORT = {"constant": "check_gvrp_state_port",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_gvrp_state_port}
