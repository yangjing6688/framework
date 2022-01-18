"""
This class outlines all the constants for the upm API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(UpmConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class UpmConstants(ApiConstants):
    def __init__(self):
        super(UpmConstants, self).__init__()
        self.CLEAR_AUTH = {"constant": "clear_auth",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.clear_auth}
        self.CLEAR_AUTH_ALL_PORTS = {"constant": "clear_auth_all_ports",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_auth_all_ports}
        self.CLEAR_PROFILE = {"constant": "clear_profile",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_profile}
        self.CLEAR_UNAUTH = {"constant": "clear_unauth",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.clear_unauth}
        self.CLEAR_UNAUTH_ALL_PORTS = {"constant": "clear_unauth_all_ports",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_unauth_all_ports}
        self.SET_AUTH = {"constant": "set_auth",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_auth}
        self.SET_PROFILE = {"constant": "set_profile",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_profile}
        self.SET_UNAUTH = {"constant": "set_unauth",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.set_unauth}
        self.SHOW_EVENT_AUTHENTICATE = {"constant": "show_event_authenticate",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_event_authenticate}
        self.SHOW_EVENT_UNAUTHENTICATED = {"constant": "show_event_unauthenticated",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_event_unauthenticated}
