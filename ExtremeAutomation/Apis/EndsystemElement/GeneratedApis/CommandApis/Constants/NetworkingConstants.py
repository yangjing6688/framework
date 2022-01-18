"""
This class outlines all the constants for the networking API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NetworkingConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NetworkingConstants(ApiConstants):
    def __init__(self):
        super(NetworkingConstants, self).__init__()
        self.CONNECT_TO_WIRELESS_NETWORK = {"constant": "connect_to_wireless_network",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.connect_to_wireless_network}
        self.DISCONNECT_FROM_WIRELESS_NETWORK = {"constant": "disconnect_from_wireless_network",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.disconnect_from_wireless_network}
        self.SHOW_WIRELESS_NETWORK = {"constant": "show_wireless_network",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_wireless_network}
