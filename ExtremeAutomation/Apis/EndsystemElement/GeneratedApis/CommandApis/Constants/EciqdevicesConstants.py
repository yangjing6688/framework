"""
This class outlines all the constants for the eciqdevices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqdevicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqdevicesConstants(ApiConstants):
    def __init__(self):
        super(EciqdevicesConstants, self).__init__()
        self.GET_CLIENT_LIST_ON_DEVICE = {"constant": "get_client_list_on_device",
                                          "tags": ["COMMAND_REST"],
                                          "link": self.link.get_client_list_on_device}
        self.GET_DEVICE = {"constant": "get_device",
                           "tags": ["COMMAND_REST"],
                           "link": self.link.get_device}
        self.GET_DEVICE_LIST = {"constant": "get_device_list",
                                "tags": ["COMMAND_REST"],
                                "link": self.link.get_device_list}
        self.GET_NETWORK_POLICY_LIST = {"constant": "get_network_policy_list",
                                        "tags": ["COMMAND_REST"],
                                        "link": self.link.get_network_policy_list}
        self.REMOVE_DEVICE = {"constant": "remove_device",
                              "tags": ["COMMAND_REST"],
                              "link": self.link.remove_device}
