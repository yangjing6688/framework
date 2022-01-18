"""
This class outlines all the constants for the dot1x API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(Dot1xConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class Dot1xConstants(ApiConstants):
    def __init__(self):
        super(Dot1xConstants, self).__init__()
        self.CLEAR_GLOBAL_IDLE_TIMEOUT = {"constant": "clear_global_idle_timeout",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_global_idle_timeout}
        self.CLEAR_GLOBAL_SESSION_TIMEOUT = {"constant": "clear_global_session_timeout",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.clear_global_session_timeout}
        self.CLEAR_PORT_REAUTHPERIOD = {"constant": "clear_port_reauthperiod",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_port_reauthperiod}
        self.CLEAR_PORT_STATE = {"constant": "clear_port_state",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_port_state}
        self.CLEAR_PORT_STATE_MAC = {"constant": "clear_port_state_mac",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_port_state_mac}
        self.CLEAR_STATE_MAC = {"constant": "clear_state_mac",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.clear_state_mac}
        self.DISABLE_ACCOUNTING = {"constant": "disable_accounting",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.disable_accounting}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_port}
        self.DISABLE_PORT_REAUTH = {"constant": "disable_port_reauth",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_port_reauth}
        self.ENABLE_ACCOUNTING = {"constant": "enable_accounting",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.enable_accounting}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_port}
        self.ENABLE_PORT_REAUTH = {"constant": "enable_port_reauth",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_port_reauth}
        self.SET_GLOBAL_IDLE_TIMEOUT = {"constant": "set_global_idle_timeout",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_global_idle_timeout}
        self.SET_GLOBAL_SESSION_TIMEOUT = {"constant": "set_global_session_timeout",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_global_session_timeout}
        self.SET_PORT_QUIETPERIOD = {"constant": "set_port_quietperiod",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_port_quietperiod}
        self.SET_PORT_REAUTHPERIOD = {"constant": "set_port_reauthperiod",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_port_reauthperiod}
        self.SET_PORT_SERVERTIMEOUT = {"constant": "set_port_servertimeout",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_port_servertimeout}
        self.SET_PORT_SUPP_RESPTIMEOUT = {"constant": "set_port_supp_resptimeout",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_port_supp_resptimeout}
        self.SHOW_AUTH_CFG = {"constant": "show_auth_cfg",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_auth_cfg}
        self.SHOW_AUTH_CFG_PORT = {"constant": "show_auth_cfg_port",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_auth_cfg_port}
        self.SHOW_GLOBAL_IDLE_TIMEOUT = {"constant": "show_global_idle_timeout",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_global_idle_timeout}
        self.SHOW_GLOBAL_SESSION_TIMEOUT = {"constant": "show_global_session_timeout",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_global_session_timeout}
        self.SHOW_SESSION = {"constant": "show_session",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_session}
        self.SHOW_SESSION_BY_PORT = {"constant": "show_session_by_port",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_session_by_port}
