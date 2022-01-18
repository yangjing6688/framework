"""
This class outlines all the constants for the multiauth API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MultiauthConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MultiauthConstants(ApiConstants):
    def __init__(self):
        super(MultiauthConstants, self).__init__()
        self.CLEAR_IDLE_TYPE_TIMEOUT = {"constant": "clear_idle_type_timeout",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_idle_type_timeout}
        self.CLEAR_SESSION_REFRESH = {"constant": "clear_session_refresh",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.clear_session_refresh}
        self.CLEAR_SESSION_TYPE_TIMEOUT = {"constant": "clear_session_type_timeout",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.clear_session_type_timeout}
        self.CLEAR_STATION_AGENT = {"constant": "clear_station_agent",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_station_agent}
        self.CLEAR_STATION_MAC = {"constant": "clear_station_mac",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_station_mac}
        self.CLEAR_STATION_MAC_PORT = {"constant": "clear_station_mac_port",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_station_mac_port}
        self.CLEAR_STATION_PORT = {"constant": "clear_station_port",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_station_port}
        self.CLEAR_VLAN = {"constant": "clear_vlan",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.clear_vlan}
        self.DISABLE_SESSION_REFRESH = {"constant": "disable_session_refresh",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.disable_session_refresh}
        self.ENABLE_SESSION_REFRESH = {"constant": "enable_session_refresh",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.enable_session_refresh}
        self.SET_IDLE_TIMEOUT = {"constant": "set_idle_timeout",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_idle_timeout}
        self.SET_IDLE_TYPE_TIMEOUT = {"constant": "set_idle_type_timeout",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_idle_type_timeout}
        self.SET_MODE = {"constant": "set_mode",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_mode}
        self.SET_PORT_FORCE_AUTH = {"constant": "set_port_force_auth",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_port_force_auth}
        self.SET_PORT_MODE = {"constant": "set_port_mode",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_port_mode}
        self.SET_PORT_NUMUSERS = {"constant": "set_port_numusers",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_port_numusers}
        self.SET_SESSION_REFRESH = {"constant": "set_session_refresh",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_session_refresh}
        self.SET_SESSION_TIMEOUT = {"constant": "set_session_timeout",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_session_timeout}
        self.SET_SESSION_TYPE_TIMEOUT = {"constant": "set_session_type_timeout",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_session_type_timeout}
        self.SET_VLAN = {"constant": "set_vlan",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_vlan}
        self.SHOW_IDLE_TIMEOUT = {"constant": "show_idle_timeout",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_idle_timeout}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
        self.SHOW_SESSION = {"constant": "show_session",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_session}
        self.SHOW_SESSION_ALL = {"constant": "show_session_all",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_session_all}
        self.SHOW_SESSION_MAC = {"constant": "show_session_mac",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_session_mac}
        self.SHOW_SESSION_PORT = {"constant": "show_session_port",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_session_port}
        self.SHOW_SESSION_TIMEOUT = {"constant": "show_session_timeout",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_session_timeout}
