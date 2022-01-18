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
        self.CREATE_ADMIN_ACCOUNT = {"constant": "create_admin_account",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.create_admin_account}
        self.DELETE_ACCOUNT = {"constant": "delete_account",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.delete_account}
        self.DISABLE_CLI_L1_USER = {"constant": "disable_cli_l1_user",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_cli_l1_user}
        self.DISABLE_CLI_L2_USER = {"constant": "disable_cli_l2_user",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_cli_l2_user}
        self.DISABLE_CLI_L3_USER = {"constant": "disable_cli_l3_user",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_cli_l3_user}
        self.DISABLE_CLI_RO_USER = {"constant": "disable_cli_ro_user",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_cli_ro_user}
        self.DISABLE_CLI_RW_USER = {"constant": "disable_cli_rw_user",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_cli_rw_user}
        self.ENABLE_CLI_L1_USER = {"constant": "enable_cli_l1_user",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_cli_l1_user}
        self.ENABLE_CLI_L2_USER = {"constant": "enable_cli_l2_user",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_cli_l2_user}
        self.ENABLE_CLI_L3_USER = {"constant": "enable_cli_l3_user",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_cli_l3_user}
        self.ENABLE_CLI_RO_USER = {"constant": "enable_cli_ro_user",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_cli_ro_user}
        self.ENABLE_CLI_RW_USER = {"constant": "enable_cli_rw_user",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_cli_rw_user}
        self.SET_ACCOUNT_PASSWORD = {"constant": "set_account_password",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_account_password}
        self.SET_ACCOUNT_PASSWORD_POLICY_MAX_AGE = {"constant": "set_account_password_policy_max_age",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.set_account_password_policy_max_age}
        self.SET_ACCOUNT_PASSWORD_POLICY_MIN_AGE = {"constant": "set_account_password_policy_min_age",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.set_account_password_policy_min_age}
        self.SET_ACCOUNT_PASSWORD_POLICY_MIN_DIFFERENT_CHARS = {"constant": "set_account_password_policy_min_different_chars",
                                                                "tags": ["COMMAND_CLI"],
                                                                "link": self.link.set_account_password_policy_min_different_chars}
        self.SET_ACCOUNT_PASSWORD_POLICY_MIN_LENGTH = {"constant": "set_account_password_policy_min_length",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.set_account_password_policy_min_length}
        self.SET_CLI_TIMEOUT = {"constant": "set_cli_timeout",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.set_cli_timeout}
        self.SET_L1_USER = {"constant": "set_l1_user",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.set_l1_user}
        self.SET_L2_USER = {"constant": "set_l2_user",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.set_l2_user}
        self.SET_L3_USER = {"constant": "set_l3_user",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.set_l3_user}
        self.SET_MAX_RLOGIN_SESSIONS = {"constant": "set_max_rlogin_sessions",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_max_rlogin_sessions}
        self.SET_MAX_TELNET_SESSIONS = {"constant": "set_max_telnet_sessions",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_max_telnet_sessions}
        self.SET_READ_ONLY_USER = {"constant": "set_read_only_user",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_read_only_user}
        self.SET_READ_WRITE_ALL_USER = {"constant": "set_read_write_all_user",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_read_write_all_user}
        self.SET_READ_WRITE_USER = {"constant": "set_read_write_user",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_read_write_user}
        self.SHOW_ACCOUNTS = {"constant": "show_accounts",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_accounts}
        self.SHOW_ACCOUNTS_PASSWORD_POLICY = {"constant": "show_accounts_password_policy",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_accounts_password_policy}
        self.SHOW_CLI_INFO = {"constant": "show_cli_info",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.show_cli_info}
        self.SHOW_CLI_NUM_ACCESS_VIOLATIONS = {"constant": "show_cli_num_access_violations",
                                               "tags": ["COMMAND_SNMP"],
                                               "link": self.link.show_cli_num_access_violations}
        self.SHOW_CLI_USERS_STATE = {"constant": "show_cli_users_state",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_cli_users_state}
        self.SHOW_LOGGED_IN_USERS = {"constant": "show_logged_in_users",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_logged_in_users}
        self.SHOW_LOGGED_IN_USERS_DETAIL = {"constant": "show_logged_in_users_detail",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_logged_in_users_detail}
