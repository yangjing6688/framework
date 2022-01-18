"""
Keyword class for all loginconfig cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.LoginconfigConstants import \
    LoginconfigConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.LoginconfigConstants import \
    LoginconfigConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementLoginconfigGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementLoginconfigGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "loginconfig"

    def loginconfig_create_admin_account(self, device_name, username='', passwd='', **kwargs):
        """
        Description: Creates an Administrator user account on the device.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "passwd": passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ADMIN_ACCOUNT,
                                    **kwargs)

    def loginconfig_delete_account(self, device_name, username='', **kwargs):
        """
        Description: Removes a user account from the device.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_ACCOUNT,
                                    **kwargs)

    def loginconfig_set_account_password_policy_min_length(self, device_name, username='', min_length='', **kwargs):
        """
        Description: Configures a user account's password minimum length.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "min_length": min_length,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNT_PASSWORD_POLICY_MIN_LENGTH,
                                    **kwargs)

    def loginconfig_set_account_password_policy_min_different_chars(self, device_name, username='', min_chars='',
                                                                    **kwargs):
        """
        Description: Configures a user account's password minimum different characters.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "min_chars": min_chars,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNT_PASSWORD_POLICY_MIN_DIFFERENT_CHARS,
                                    **kwargs)

    def loginconfig_set_account_password_policy_min_age(self, device_name, username='', age='', **kwargs):
        """
        Description: Configures a user account's password min-age.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "age": age,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNT_PASSWORD_POLICY_MIN_AGE,
                                    **kwargs)

    def loginconfig_set_account_password_policy_max_age(self, device_name, username='', age='', **kwargs):
        """
        Description: Configures a user account's password max-age.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "age": age,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNT_PASSWORD_POLICY_MAX_AGE,
                                    **kwargs)

    def loginconfig_set_account_password(self, device_name, username='', old_password='', new_password='', **kwargs):
        """
        Description: Configures a user account's password.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "new_password": new_password,
            "old_password": old_password,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNT_PASSWORD,
                                    **kwargs)

    def loginconfig_enable_cli_ro_user(self, device_name, **kwargs):
        """
        Description: Used to enable the read-only CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLI_RO_USER,
                                    **kwargs)

    def loginconfig_disable_cli_ro_user(self, device_name, **kwargs):
        """
        Description: Used to disable the read-only CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLI_RO_USER,
                                    **kwargs)

    def loginconfig_enable_cli_rw_user(self, device_name, **kwargs):
        """
        Description: Used to enable the read-write CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLI_RW_USER,
                                    **kwargs)

    def loginconfig_disable_cli_rw_user(self, device_name, **kwargs):
        """
        Description: Used to disable the read-write CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLI_RW_USER,
                                    **kwargs)

    def loginconfig_enable_cli_l1_user(self, device_name, **kwargs):
        """
        Description: Used to enable the read-write-layer 1 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLI_L1_USER,
                                    **kwargs)

    def loginconfig_disable_cli_l1_user(self, device_name, **kwargs):
        """
        Description: Used to disable the read-write-layer 1 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLI_L1_USER,
                                    **kwargs)

    def loginconfig_enable_cli_l2_user(self, device_name, **kwargs):
        """
        Description: Used to enable the read-write-layer 2 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLI_L2_USER,
                                    **kwargs)

    def loginconfig_disable_cli_l2_user(self, device_name, **kwargs):
        """
        Description: Used to disable the read-write-layer 2 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLI_L2_USER,
                                    **kwargs)

    def loginconfig_enable_cli_l3_user(self, device_name, **kwargs):
        """
        Description: Used to enable the read-write-layer 3 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLI_L3_USER,
                                    **kwargs)

    def loginconfig_disable_cli_l3_user(self, device_name, **kwargs):
        """
        Description: Used to disable the read-write-layer 3 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLI_L3_USER,
                                    **kwargs)

    def loginconfig_set_read_only_user(self, device_name, username='', new_passwd='', old_passwd='', **kwargs):
        """
        Description: Modifies the username and password for the read-only CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "new_passwd": new_passwd,
            "old_passwd": old_passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_READ_ONLY_USER,
                                    **kwargs)

    def loginconfig_set_read_write_user(self, device_name, username='', new_passwd='', old_passwd='', **kwargs):
        """
        Description: Modifies the username and password for the read-write CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "new_passwd": new_passwd,
            "old_passwd": old_passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_READ_WRITE_USER,
                                    **kwargs)

    def loginconfig_set_read_write_all_user(self, device_name, username='', new_passwd='', old_passwd='', **kwargs):
        """
        Description: Modifies the username and password for the read-write-all CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "new_passwd": new_passwd,
            "old_passwd": old_passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_READ_WRITE_ALL_USER,
                                    **kwargs)

    def loginconfig_set_max_telnet_sessions(self, device_name, max_sessions='', **kwargs):
        """
        Description: Used to indicate the maximum number of telnet sessions the system will support.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "max_sessions": max_sessions
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAX_TELNET_SESSIONS,
                                    **kwargs)

    def loginconfig_set_max_rlogin_sessions(self, device_name, max_sessions='', **kwargs):
        """
        Description: Used to indicate the maximum number of rlogin sessions the system will support.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "max_sessions": max_sessions
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAX_RLOGIN_SESSIONS,
                                    **kwargs)

    def loginconfig_set_l1_user(self, device_name, username='', new_passwd='', old_passwd='', **kwargs):
        """
        Description: Modifies the username and password for the read-write layer-1 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "new_passwd": new_passwd,
            "old_passwd": old_passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L1_USER,
                                    **kwargs)

    def loginconfig_set_l2_user(self, device_name, username='', new_passwd='', old_passwd='', **kwargs):
        """
        Description: Modifies the username and password for the read-write layer-2 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "new_passwd": new_passwd,
            "old_passwd": old_passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L2_USER,
                                    **kwargs)

    def loginconfig_set_l3_user(self, device_name, username='', new_passwd='', old_passwd='', **kwargs):
        """
        Description: Modifies the username and password for the read-write layer-3 CLI account.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "new_passwd": new_passwd,
            "old_passwd": old_passwd,
            "username": username
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_L3_USER,
                                    **kwargs)

    def loginconfig_set_cli_timeout(self, device_name, timeout='', **kwargs):
        """
        Description: Used to indicate the amount of idle time.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CLI_TIMEOUT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def loginconfig_verify_account_exists(self, device_name, login_accounts='', access_level='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [login_account] - The login account that should exist.

        Verifies that the login account exists.
        """
        args = {"username": login_accounts,
                "access_level": access_level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.VERIFY_LOGIN_EXISTS, True,
                                           "Login account {username} with access level {access_level} exists.",
                                           "Login account {username} with access level {access_level} does NOT exist!",
                                           **kwargs)

    def loginconfig_verify_account_does_not_exist(self, device_name, login_accounts='', access_level='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [login_account] - The login account that should NOT exist.

        Verifies that the login account does NOT exist.
        """
        args = {"username": login_accounts,
                "access_level": access_level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.VERIFY_LOGIN_EXISTS, False,
                                           "Login account {username} does not exist.",
                                           "Login account {username} exists and should not!",
                                           **kwargs)

    def loginconfig_verify_admin_account_exists(self, device_name, username='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login admin account name that is expected to exist.

        Verifies that the named admin account exists on the system.
        """
        args = {"username": username}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.VERIFY_ADMIN_LOGIN_EXISTS, True,
                                           "Login account {username} exists as an admin account.",
                                           "Login account {username} DOES NOT exist as an admin account!",
                                           **kwargs)

    def loginconfig_verify_admin_account_does_not_exist(self, device_name, username='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login admin account name that is expected to exist.

        Verifies that the named admin account exists on the system.
        """
        args = {"username": username}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.VERIFY_ADMIN_LOGIN_DOES_NOT_EXIST, False,
                                           "Login account {username} does not exist as an admin account.",
                                           "Login account {username} DOES exist as an admin account!",
                                           **kwargs)

    def loginconfig_verify_user_auth_method(self, device_name, username='', auth_method='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [user_name] - The login admin account name that is expected to exist.
        [auth_method] -  The authentication method that the user logged in with i.e. local or RADIUS.
        Verifies that the named user is logged in with the correct authentication method.
        """
        args = {"username": username,
                "auth_method": auth_method}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOGGED_IN_USERS_DETAIL,
                                           self.parse_const.VERIFY_LOGIN_USER_AUTHENTICATION_METHOD, True,
                                           "Login account {username} logged in using {auth_method}.",
                                           "Login account {username} not logged in using {auth_method}!",
                                           **kwargs)

    def loginconfig_verify_cli_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The timeout value in seconds.

        Verifies that the cli idle timeout value is correct.
        """
        args = {"timeout": timeout,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_INFO,
                                           self.parse_const.CHECK_CLI_TIMEOUT, True,
                                           "CLI timeout value is {timeout}.",
                                           "CLI timeout value is NOT {timeout}!",
                                           **kwargs)

    def loginconfig_verify_max_telnet_sessions(self, device_name, max_sessions='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [max_sessions]  - The maximum number of sessions.

        Verifies that the maximum number of telnet sessions value is correct.
        """
        args = {"max_sessions": max_sessions,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_INFO,
                                           self.parse_const.CHECK_MAX_TELNET_SESSIONS, True,
                                           "CLI maximum telnet sessions is {max_sessions}.",
                                           "CLI maximum telnet sessions is NOT {max_sessions}!",
                                           **kwargs)

    def loginconfig_verify_max_rlogin_sessions(self, device_name, max_sessions='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [max_sessions]  - The maximum number of sessions.

        Verifies that the maximum number of rlogin sessions value is correct.
        """
        args = {"max_sessions": max_sessions,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_INFO,
                                           self.parse_const.CHECK_MAX_RLOGIN_SESSIONS, True,
                                           "CLI maximum rlogin sessions is {max_sessions}.",
                                           "CLI maximum rlogin sessions is NOT {max_sessions}!",
                                           **kwargs)

    def loginconfig_verify_ro_account_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the read only account is enabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_READ_ONLY_ACCOUNT, True,
                                           "CLI read only account is enabled.",
                                           "CLI read only account is NOT enabled!",
                                           **kwargs)

    def loginconfig_verify_ro_account_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the read only account is disabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_READ_ONLY_ACCOUNT, False,
                                           "CLI read only account is not enabled.",
                                           "CLI read only account is ENABLED!",
                                           **kwargs)

    def loginconfig_verify_rw_account_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the read write account is enabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_READ_WRITE_ACCOUNT, True,
                                           "CLI read write account is enabled.",
                                           "CLI read write account is NOT enabled!",
                                           **kwargs)

    def loginconfig_verify_rw_account_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the read write account is disabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_READ_WRITE_ACCOUNT, False,
                                           "CLI read write account is not enabled.",
                                           "CLI read write account is ENABLED!",
                                           **kwargs)

    def loginconfig_verify_l1_rw_account_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the L1 account is enabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_L1_READ_WRITE_ACCOUNT, True,
                                           "CLI L1 account is enabled.",
                                           "CLI L1 account is NOT enabled!",
                                           **kwargs)

    def loginconfig_verify_l1_rw_account_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the L1 account is disabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_L1_READ_WRITE_ACCOUNT, False,
                                           "CLI L1 account is not enabled.",
                                           "CLI L1 account is ENABLED!",
                                           **kwargs)

    def loginconfig_verify_l2_rw_account_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the L2 account is enabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_L2_READ_WRITE_ACCOUNT, True,
                                           "CLI L2 account is enabled.",
                                           "CLI L2 account is NOT enabled!",
                                           **kwargs)

    def loginconfig_verify_l2_rw_account_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the L2 account is disabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_L2_READ_WRITE_ACCOUNT, False,
                                           "CLI L2 account is not enabled.",
                                           "CLI L2 account is ENABLED!",
                                           **kwargs)

    def loginconfig_verify_l3_rw_account_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the L3 account is enabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_L3_READ_WRITE_ACCOUNT, True,
                                           "CLI L3 account is enabled.",
                                           "CLI L3 account is NOT enabled!",
                                           **kwargs)

    def loginconfig_verify_l3_rw_account_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verifies that the L3 account is disabled.
        Applies to VOSS.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CLI_USERS_STATE,
                                           self.parse_const.CHECK_L3_READ_WRITE_ACCOUNT, False,
                                           "CLI L3 account is not enabled.",
                                           "CLI L3 account is ENABLED!",
                                           **kwargs)

    def loginconfig_verify_total_failed_login_attempts(self, device_name, username='', login_attempts='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [login_attempts] - The expected number of login attempts in the table.

        Verifies the total number of failed login attempts for the provided user.
        """
        args = {"username": username,
                "login_attempts": login_attempts}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.CHECK_TOTAL_FAILED_LOGIN_ATTEMPTS, True,
                                           "Login {username} has the correct number of failed login attempts.",
                                           "Login {username} DOES NOT have the correct number of failed "
                                           "login attempts!",
                                           **kwargs)

    def loginconfig_verify_failed_login_attempts_since_success(self, device_name, username='', login_attempts='',
                                                               **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [login_attempts] - The expected number of login attempts in the table.

        Verifies the total number of failed login attempts since the last successful login for the provided user.
        """
        args = {"username": username,
                "login_attempts": login_attempts}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.CHECK_FAILED_LOGIN_ATTEMPTS_SINCE_SUCCESS, True,
                                           "Login {username} has the correct number of failed login attempts.",
                                           "Login {username} DOES NOT have the correct number of failed "
                                           "login attempts!",
                                           **kwargs)

    def loginconfig_verify_successful_logins(self, device_name, username='', login_attempts='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [login_attempts] - The expected number of login attempts in the table.

        Verifies the total number of successful logins for the provided user.
        """
        args = {"username": username,
                "login_attempts": login_attempts}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS,
                                           self.parse_const.CHECK_SUCCESSFUL_LOGIN_ATTEMPTS, True,
                                           "Login {username} has the correct number of successful login attempts.",
                                           "Login {username} DOES NOT have the correct number of successful "
                                           "login attempts!",
                                           **kwargs)

    def loginconfig_verify_password_max_age(self, device_name, username='', age='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [age] - The expected max age in the table.

        Verifies the max age password value for the provided user.
        """
        args = {"username": username,
                "age": age}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS_PASSWORD_POLICY,
                                           self.parse_const.CHECK_PASSWORD_MAX_AGE, True,
                                           "Login {username} has the correct password max-age.",
                                           "Login {username} DOES NOT have the correct password max-age!",
                                           **kwargs)

    def loginconfig_verify_password_min_age(self, device_name, username='', age='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [age] - The expected min age in the table.

        Verifies the min age password value for the provided user.
        """
        args = {"username": username,
                "age": age}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS_PASSWORD_POLICY,
                                           self.parse_const.CHECK_PASSWORD_MIN_AGE, True,
                                           "Login {username} has the correct password min-age.",
                                           "Login {username} DOES NOT have the correct password min-age!",
                                           **kwargs)

    def loginconfig_verify_password_min_length(self, device_name, username='', length='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [length] - The expected length in the table.

        Verifies the min length password value for the provided user.
        """
        args = {"username": username,
                "length": length}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS_PASSWORD_POLICY,
                                           self.parse_const.CHECK_PASSWORD_MIN_LENGTH, True,
                                           "Login {username} has the correct password min-length.",
                                           "Login {username} DOES NOT have the correct password min-length!",
                                           **kwargs)

    def loginconfig_verify_password_min_diff_chars(self, device_name, username='', min_diff_chars='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [username] - The login account to check login attempts on.
        [min_diff_chars] - The expected min-diff-chars in the table.

        Verifies the min-diff-chars password value for the provided user.
        """
        args = {"username": username,
                "min_diff_chars": min_diff_chars}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCOUNTS_PASSWORD_POLICY,
                                           self.parse_const.CHECK_PASSWORD_MIN_DIFF_CHAR, True,
                                           "Login {username} has the correct password min-diff-char value.",
                                           "Login {username} DOES NOT have the correct password min-diff-char value!",
                                           **kwargs)
