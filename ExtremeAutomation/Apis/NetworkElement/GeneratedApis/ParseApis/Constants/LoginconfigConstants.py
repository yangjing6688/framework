"""
This class outlines all the constants for the loginconfig API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(LoginconfigConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class LoginconfigConstants(ApiConstants):
    def __init__(self):
        super(LoginconfigConstants, self).__init__()
        self.CHECK_CLI_TIMEOUT = {"constant": "check_cli_timeout",
                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                  "link": self.link.check_cli_timeout}
        self.CHECK_FAILED_LOGIN_ATTEMPTS_SINCE_SUCCESS = {"constant": "check_failed_login_attempts_since_success",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_failed_login_attempts_since_success}
        self.CHECK_L1_READ_WRITE_ACCOUNT = {"constant": "check_l1_read_write_account",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_l1_read_write_account}
        self.CHECK_L2_READ_WRITE_ACCOUNT = {"constant": "check_l2_read_write_account",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_l2_read_write_account}
        self.CHECK_L3_READ_WRITE_ACCOUNT = {"constant": "check_l3_read_write_account",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_l3_read_write_account}
        self.CHECK_MAX_RLOGIN_SESSIONS = {"constant": "check_max_rlogin_sessions",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_max_rlogin_sessions}
        self.CHECK_MAX_TELNET_SESSIONS = {"constant": "check_max_telnet_sessions",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_max_telnet_sessions}
        self.CHECK_PASSWORD_MAX_AGE = {"constant": "check_password_max_age",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_password_max_age}
        self.CHECK_PASSWORD_MIN_AGE = {"constant": "check_password_min_age",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_password_min_age}
        self.CHECK_PASSWORD_MIN_DIFF_CHAR = {"constant": "check_password_min_diff_char",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_password_min_diff_char}
        self.CHECK_PASSWORD_MIN_LENGTH = {"constant": "check_password_min_length",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_password_min_length}
        self.CHECK_READ_ONLY_ACCOUNT = {"constant": "check_read_only_account",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_read_only_account}
        self.CHECK_READ_WRITE_ACCOUNT = {"constant": "check_read_write_account",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_read_write_account}
        self.CHECK_SUCCESSFUL_LOGIN_ATTEMPTS = {"constant": "check_successful_login_attempts",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_successful_login_attempts}
        self.CHECK_TOTAL_FAILED_LOGIN_ATTEMPTS = {"constant": "check_total_failed_login_attempts",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_total_failed_login_attempts}
        self.VERIFY_ADMIN_LOGIN_DOES_NOT_EXIST = {"constant": "verify_admin_login_does_not_exist",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.verify_admin_login_does_not_exist}
        self.VERIFY_ADMIN_LOGIN_EXISTS = {"constant": "verify_admin_login_exists",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_admin_login_exists}
        self.VERIFY_LOGIN_EXISTS = {"constant": "verify_login_exists",
                                    "tags": ["PARSE_CLI", "PARSE_REST"],
                                    "link": self.link.verify_login_exists}
        self.VERIFY_LOGIN_USER_AUTHENTICATION_METHOD = {"constant": "verify_login_user_authentication_method",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.verify_login_user_authentication_method}
