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
        self.CHECK_WIRELESS_NETWORK_CONNECTED = {"constant": "check_wireless_network_connected",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_wireless_network_connected}
        self.CHECK_WIRELESS_NETWORK_DISCONNECTED = {"constant": "check_wireless_network_disconnected",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_wireless_network_disconnected}
