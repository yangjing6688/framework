"""
This class outlines all the constants for the nd API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NdConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NdConstants(ApiConstants):
    def __init__(self):
        super(NdConstants, self).__init__()
        self.CLEAR_V6_NEIGHBOR = {"constant": "clear_v6_neighbor",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_v6_neighbor}
        self.CLEAR_V6_NEIGHBOR_PORT = {"constant": "clear_v6_neighbor_port",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_v6_neighbor_port}
        self.SET_V6_NEIGHBOR = {"constant": "set_v6_neighbor",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_v6_neighbor}
        self.SHOW_TABLE = {"constant": "show_table",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_table}
