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
        self.CHECK_IF_DOT1X_ACCOUNTING_IS_ENABLED = {"constant": "check_if_dot1x_accounting_is_enabled",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_if_dot1x_accounting_is_enabled}
        self.CHECK_IF_DOT1X_IS_ENABLED = {"constant": "check_if_dot1x_is_enabled",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_if_dot1x_is_enabled}
        self.CHECK_IF_DOT1X_USER_IP_IS_CORRECT = {"constant": "check_if_dot1x_user_ip_is_correct",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_if_dot1x_user_ip_is_correct}
        self.CHECK_IF_DOT1X_USER_IS_AUTHENTICATED = {"constant": "check_if_dot1x_user_is_authenticated",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_if_dot1x_user_is_authenticated}
        self.CHECK_IF_DOT1X_USER_IS_AUTHENTICATED_BY_RADIUS = {"constant": "check_if_dot1x_user_is_authenticated_by_radius",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_if_dot1x_user_is_authenticated_by_radius}
        self.CHECK_IF_DOT1X_USER_IS_UNAUTHENTICATED = {"constant": "check_if_dot1x_user_is_unauthenticated",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_if_dot1x_user_is_unauthenticated}
        self.CHECK_IF_DOT1X_USER_LOGIN_NAME_IS_CORRECT = {"constant": "check_if_dot1x_user_login_name_is_correct",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_if_dot1x_user_login_name_is_correct}
        self.VERIFY_DOT1X_ACCOUNTING_STATE = {"constant": "verify_dot1x_accounting_state",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_dot1x_accounting_state}
        self.VERIFY_DOT1X_IDLE_TIMEOUT = {"constant": "verify_dot1x_idle_timeout",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_dot1x_idle_timeout}
        self.VERIFY_DOT1X_IS_ENABLED_ON_PORT = {"constant": "verify_dot1x_is_enabled_on_port",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.verify_dot1x_is_enabled_on_port}
        self.VERIFY_DOT1X_PORT_REAUTH_PERIOD = {"constant": "verify_dot1x_port_reauth_period",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.verify_dot1x_port_reauth_period}
        self.VERIFY_DOT1X_PORT_REAUTH_STATE = {"constant": "verify_dot1x_port_reauth_state",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.verify_dot1x_port_reauth_state}
        self.VERIFY_DOT1X_QUIET_PERIOD = {"constant": "verify_dot1x_quiet_period",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_dot1x_quiet_period}
        self.VERIFY_DOT1X_REAUTH_PERIOD = {"constant": "verify_dot1x_reauth_period",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_dot1x_reauth_period}
        self.VERIFY_DOT1X_SERVER_TIMEOUT = {"constant": "verify_dot1x_server_timeout",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.verify_dot1x_server_timeout}
        self.VERIFY_DOT1X_SESSION_TIMEOUT = {"constant": "verify_dot1x_session_timeout",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_dot1x_session_timeout}
        self.VERIFY_DOT1X_STATE = {"constant": "verify_dot1x_state",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.verify_dot1x_state}
        self.VERIFY_DOT1X_SUPP_RESPONSE_TIMEOUT = {"constant": "verify_dot1x_supp_response_timeout",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_dot1x_supp_response_timeout}
        self.VERIFY_GLOBAL_DOT1X_IDLE_TIMEOUT = {"constant": "verify_global_dot1x_idle_timeout",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_global_dot1x_idle_timeout}
        self.VERIFY_GLOBAL_DOT1X_SESSION_TIMEOUT = {"constant": "verify_global_dot1x_session_timeout",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.verify_global_dot1x_session_timeout}
