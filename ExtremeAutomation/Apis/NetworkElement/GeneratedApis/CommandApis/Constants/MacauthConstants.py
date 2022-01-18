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
        self.CLEAR_MAC_USER = {"constant": "clear_mac_user",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_mac_user}
        self.CLEAR_PASSWORD = {"constant": "clear_password",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_password}
        self.CLEAR_PORT_QUIETPERIOD = {"constant": "clear_port_quietperiod",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_port_quietperiod}
        self.CLEAR_PORT_REAUTHPERIOD = {"constant": "clear_port_reauthperiod",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_port_reauthperiod}
        self.DISABLE = {"constant": "disable",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.disable}
        self.DISABLE_PORT_REAUTHENTICATION = {"constant": "disable_port_reauthentication",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.disable_port_reauthentication}
        self.ENABLE = {"constant": "enable",
                       "tags": ["COMMAND_CLI"],
                       "link": self.link.enable}
        self.ENABLE_PORT_REAUTHENTICATION = {"constant": "enable_port_reauthentication",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.enable_port_reauthentication}
        self.SET_MAC_FORMAT_TYPE = {"constant": "set_mac_format_type",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_mac_format_type}
        self.SET_MAC_USER = {"constant": "set_mac_user",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_mac_user}
        self.SET_MAC_USER_NOPASS = {"constant": "set_mac_user_nopass",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_mac_user_nopass}
        self.SET_PASSWORD = {"constant": "set_password",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_password}
        self.SET_PORT_QUIETPERIOD = {"constant": "set_port_quietperiod",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_port_quietperiod}
        self.SET_PORT_REAUTHPERIOD = {"constant": "set_port_reauthperiod",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_port_reauthperiod}
        self.SET_PORT_STATE = {"constant": "set_port_state",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_port_state}
        self.SET_REAUTHPERIOD = {"constant": "set_reauthperiod",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_reauthperiod}
        self.SHOW = {"constant": "show",
                     "tags": ["COMMAND_CLI"],
                     "link": self.link.show}
        self.SHOW_MAC_LIST = {"constant": "show_mac_list",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_mac_list}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_port}
        self.SHOW_PORT_AUTHENTICATION = {"constant": "show_port_authentication",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_port_authentication}
