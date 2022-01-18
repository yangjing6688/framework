"""
This class outlines all the constants for the hostutils API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostutilsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostutilsConstants(ApiConstants):
    def __init__(self):
        super(HostutilsConstants, self).__init__()
        self.CHECK_DEBUG_LOGIN = {"constant": "check_debug_login",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_debug_login}
        self.CHECK_DEBUG_LOGIN_ENABLED = {"constant": "check_debug_login_enabled",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_debug_login_enabled}
        self.CHECK_FAILED_LOGIN_ATTEMPTS = {"constant": "check_failed_login_attempts",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_failed_login_attempts}
        self.CHECK_L2PING_IPADDR_RESULT = {"constant": "check_l2ping_ipaddr_result",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_l2ping_ipaddr_result}
        self.CHECK_LAST_LOGIN_DATE = {"constant": "check_last_login_date",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_last_login_date}
        self.CHECK_LOGOUT_MESSAGE_EXISTS = {"constant": "check_logout_message_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_logout_message_exists}
        self.CHECK_PING_RESULT = {"constant": "check_ping_result",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_ping_result}
        self.CHECK_SUCCESSFUL_LOGIN_ATTEMPTS = {"constant": "check_successful_login_attempts",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_successful_login_attempts}
