"""
This class outlines all the constants for the macauth API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MacauthConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MacauthConstants(ApiConstants):
    def __init__(self):
        super(MacauthConstants, self).__init__()
        self.VERIFY_MACAUTH_MAC_LIST_MEMBERS = {"constant": "verify_macauth_mac_list_members",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.verify_macauth_mac_list_members}
        self.VERIFY_MACAUTH_PORT_AUTHENTICATION = {"constant": "verify_macauth_port_authentication",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_macauth_port_authentication}
        self.VERIFY_MACAUTH_PORT_REAUTH_DELAY = {"constant": "verify_macauth_port_reauth_delay",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_macauth_port_reauth_delay}
        self.VERIFY_MACAUTH_PORT_REAUTH_PERIOD = {"constant": "verify_macauth_port_reauth_period",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.verify_macauth_port_reauth_period}
        self.VERIFY_MACAUTH_PORT_REAUTH_STATE = {"constant": "verify_macauth_port_reauth_state",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_macauth_port_reauth_state}
        self.VERIFY_MACAUTH_PORT_STATE = {"constant": "verify_macauth_port_state",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_macauth_port_state}
        self.VERIFY_MACAUTH_REAUTH_PERIOD = {"constant": "verify_macauth_reauth_period",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_macauth_reauth_period}
        self.VERIFY_MACAUTH_STATE = {"constant": "verify_macauth_state",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.verify_macauth_state}
