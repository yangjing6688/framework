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
        self.CHECK_MULTIAUTH_IDLE_TIME = {"constant": "check_multiauth_idle_time",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_multiauth_idle_time}
        self.CHECK_MULTIAUTH_IDLE_TIMEOUT = {"constant": "check_multiauth_idle_timeout",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_multiauth_idle_timeout}
        self.CHECK_MULTIAUTH_IDLE_TIMEOUT_DEFAULT = {"constant": "check_multiauth_idle_timeout_default",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_multiauth_idle_timeout_default}
        self.CHECK_MULTIAUTH_IDLE_TIMEOUT_DOT1X = {"constant": "check_multiauth_idle_timeout_dot1x",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_multiauth_idle_timeout_dot1x}
        self.CHECK_MULTIAUTH_IDLE_TIMEOUT_MAC = {"constant": "check_multiauth_idle_timeout_mac",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_multiauth_idle_timeout_mac}
        self.CHECK_MULTIAUTH_IDLE_TIMEOUT_WEB = {"constant": "check_multiauth_idle_timeout_web",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_multiauth_idle_timeout_web}
        self.CHECK_MULTIAUTH_IDLE_TIME_GREATER = {"constant": "check_multiauth_idle_time_greater",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_multiauth_idle_time_greater}
        self.CHECK_MULTIAUTH_IDLE_TIME_LESS = {"constant": "check_multiauth_idle_time_less",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_multiauth_idle_time_less}
        self.CHECK_MULTIAUTH_SESSION_DURATION_GREATER = {"constant": "check_multiauth_session_duration_greater",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.check_multiauth_session_duration_greater}
        self.CHECK_MULTIAUTH_SESSION_DURATION_LESS = {"constant": "check_multiauth_session_duration_less",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_multiauth_session_duration_less}
        self.CHECK_MULTIAUTH_SESSION_EXISTS = {"constant": "check_multiauth_session_exists",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_multiauth_session_exists}
        self.CHECK_MULTIAUTH_SESSION_EXPIRED = {"constant": "check_multiauth_session_expired",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_multiauth_session_expired}
        self.CHECK_MULTIAUTH_SESSION_REFRESH = {"constant": "check_multiauth_session_refresh",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_multiauth_session_refresh}
        self.CHECK_MULTIAUTH_SESSION_REFRESH_INTERVAL = {"constant": "check_multiauth_session_refresh_interval",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.check_multiauth_session_refresh_interval}
        self.CHECK_MULTIAUTH_SESSION_TIMEOUT = {"constant": "check_multiauth_session_timeout",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_multiauth_session_timeout}
        self.CHECK_MULTIAUTH_SESSION_TIMEOUT_DEFAULT = {"constant": "check_multiauth_session_timeout_default",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.check_multiauth_session_timeout_default}
        self.CHECK_MULTIAUTH_SESSION_TIMEOUT_DOT1X = {"constant": "check_multiauth_session_timeout_dot1x",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_multiauth_session_timeout_dot1x}
        self.CHECK_MULTIAUTH_SESSION_TIMEOUT_MAC = {"constant": "check_multiauth_session_timeout_mac",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_multiauth_session_timeout_mac}
        self.CHECK_MULTIAUTH_SESSION_TIMEOUT_WEB = {"constant": "check_multiauth_session_timeout_web",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_multiauth_session_timeout_web}
        self.CHECK_MULTIAUTH_STATE = {"constant": "check_multiauth_state",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_multiauth_state}
        self.CHECK_MULTIAUTH_VLAN_EXISTS = {"constant": "check_multiauth_vlan_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_multiauth_vlan_exists}
