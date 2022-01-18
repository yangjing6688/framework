"""
Keyword class for all radius cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.RadiusConstants import \
    RadiusConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.RadiusConstants import \
    RadiusConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils


class NetworkElementRadiusGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementRadiusGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "radius"

    def radius_enable_global(self, device_name, **kwargs):
        """
        Description: Enables RADIUS.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def radius_enable_acct(self, device_name, **kwargs):
        """
        Description: Enables RADIUS Accounting.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ACCT,
                                    **kwargs)

    def radius_disable_global(self, device_name, **kwargs):
        """
        Description: Disables RADIUS.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def radius_disable_acct(self, device_name, **kwargs):
        """
        Description: Disables RADIUS Accounting.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ACCT,
                                    **kwargs)

    def radius_set_server(self, device_name, addr='', secret='', index='', port='', client_ip='', vr='', **kwargs):
        """
        Description: Creates a RADIUS server.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "addr": addr,
            "client_ip": client_ip,
            "index": index,
            "port": port,
            "secret": secret,
            "vr": vr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SERVER,
                                    **kwargs)

    def radius_set_acct_server(self, device_name, addr='', index='', port='', secret='', client_ip='', vr='', **kwargs):
        """
        Description: Creates a RADIUS Accounting Server.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "addr": addr,
            "client_ip": client_ip,
            "index": index,
            "port": port,
            "secret": secret,
            "vr": vr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCT_SERVER,
                                    **kwargs)

    def radius_set_retries_global(self, device_name, num='', **kwargs):
        """
        Description: Sets the RADIUS Server retry attempts.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "num": num
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RETRIES_GLOBAL,
                                    **kwargs)

    def radius_set_timeout_global(self, device_name, sec='', **kwargs):
        """
        Description: Sets the RADIUS Server timeout value in seconds.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "sec": sec
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TIMEOUT_GLOBAL,
                                    **kwargs)

    def radius_set_algorithm_global_std(self, device_name, **kwargs):
        """
        Description: Sets the RADIUS Algorithm type to Standard.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ALGORITHM_GLOBAL_STD,
                                    **kwargs)

    def radius_set_algorithm_global_rr(self, device_name, **kwargs):
        """
        Description: Sets the RADIUS Algorithm type to Round Robin.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ALGORITHM_GLOBAL_RR,
                                    **kwargs)

    def radius_set_algorithm_global_srr(self, device_name, **kwargs):
        """
        Description: Sets the RADIUS Algorithm type to Sticky Round Robin.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ALGORITHM_GLOBAL_SRR,
                                    **kwargs)

    def radius_set_accounting_retries_global(self, device_name, num='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "num": num
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNTING_RETRIES_GLOBAL,
                                    **kwargs)

    def radius_set_accounting_timeout_global(self, device_name, sec='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "sec": sec
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCOUNTING_TIMEOUT_GLOBAL,
                                    **kwargs)

    def radius_clear_server(self, device_name, client_ip='', index='', **kwargs):
        """
        Description: Removes a RADIUS server.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            SNMP: EOS, EXOS
        """
        args = {
            "client_ip": client_ip,
            "index": index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SERVER,
                                    **kwargs)

    def radius_clear_acct_server(self, device_name, index='', **kwargs):
        """
        Description: Removes a RADIUS accounting server.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "index": index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACCT_SERVER,
                                    **kwargs)

    def radius_clear_acct_server_global(self, device_name, **kwargs):
        """
        Description: Removes ALL the RADIUS accounting servers configured on the Network Element.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACCT_SERVER_GLOBAL,
                                    **kwargs)

    def radius_clear_algorithm_global(self, device_name, **kwargs):
        """
        Description: Sets the RADIUS Algorithm type to the default setting.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALGORITHM_GLOBAL,
                                    **kwargs)

    def radius_clear_retries_global(self, device_name, **kwargs):
        """
        Description: Clears the RADIUS Server retry attempts setting them back to the default setting.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RETRIES_GLOBAL,
                                    **kwargs)

    def radius_clear_timeout_global(self, device_name, **kwargs):
        """
        Description: Clears the RADIUS Server timeout value setting it back to the default setting.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TIMEOUT_GLOBAL,
                                    **kwargs)

    def radius_clear_state(self, device_name, **kwargs):
        """
        Description: Clears the RADIUS client state and sets it back to the default value.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATE,
                                    **kwargs)

    def radius_enable_mgmt(self, device_name, **kwargs):
        """
        Description: Enables RADIUS Management Access.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MGMT,
                                    **kwargs)

    def radius_enable_netlogin(self, device_name, **kwargs):
        """
        Description: Enables RADIUS Netlogin.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_NETLOGIN,
                                    **kwargs)

    def radius_disable_mgmt(self, device_name, **kwargs):
        """
        Description: Disables RADIUS Management Access.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MGMT,
                                    **kwargs)

    def radius_disable_netlogin(self, device_name, **kwargs):
        """
        Description: Disables RADIUS Netlogin.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_NETLOGIN,
                                    **kwargs)

    def radius_enable_include_cli_cmds(self, device_name, **kwargs):
        """
        Description: Enables the inclusion of cli commands in RADIUS accounting updates.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INCLUDE_CLI_CMDS,
                                    **kwargs)

    def radius_enable_cli_profile(self, device_name, **kwargs):
        """
        Description: Enables RADIUS CLI Profiling.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CLI_PROFILE,
                                    **kwargs)

    def radius_enable_src_ip_flag(self, device_name, **kwargs):
        """
        Description: Enables the flag to include the configured IP address as source address in RADIUS packets.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SRC_IP_FLAG,
                                    **kwargs)

    def radius_disable_include_cli_cmds(self, device_name, **kwargs):
        """
        Description: Disables the inclusion of cli commands in RADIUS accounting updates.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INCLUDE_CLI_CMDS,
                                    **kwargs)

    def radius_disable_cli_profile(self, device_name, **kwargs):
        """
        Description: Disables RADIUS CLI Profiling.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CLI_PROFILE,
                                    **kwargs)

    def radius_disable_src_ip_flag(self, device_name, **kwargs):
        """
        Description: Disables the flag to include the configured IP address as source address in RADIUS packets.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SRC_IP_FLAG,
                                    **kwargs)

    def radius_set_max_servers(self, device_name, max_servers='', **kwargs):
        """
        Description: Configure the maximum number of RADIUS servers.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "max_servers": max_servers
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAX_SERVERS,
                                    **kwargs)

    def radius_set_access_priority(self, device_name, attr_value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS Access-Priority attribute.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "attr_value": attr_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_PRIORITY,
                                    **kwargs)

    def radius_set_acct_attr(self, device_name, attr_value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS User-Command attribute.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "attr_value": attr_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCT_ATTR,
                                    **kwargs)

    def radius_set_mcast_addr_attr(self, device_name, attr_value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS multicast address vendor specific attribute.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "attr_value": attr_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MCAST_ADDR_ATTR,
                                    **kwargs)

    def radius_set_auth_info_attr(self, device_name, attr_value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS Auth-Info vendor specific attribute.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "attr_value": attr_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH_INFO_ATTR,
                                    **kwargs)

    def radius_set_cmd_access_attr(self, device_name, attr_value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS Command-Access attribute..

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "attr_value": attr_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CMD_ACCESS_ATTR,
                                    **kwargs)

    def radius_set_cli_cmd_attr(self, device_name, attr_value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS Cli-Command attribute.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "attr_value": attr_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CLI_CMD_ATTR,
                                    **kwargs)

    def radius_set_cli_cmd_count(self, device_name, value='', **kwargs):
        """
        Description: Configure the integer value for the RADIUS Cli-Command-count.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "value": value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CLI_CMD_COUNT,
                                    **kwargs)

    def radius_set_server_for_cli(self, device_name, acct_port='', addr='', auth_port='', max_retries='', priority='',
                                  secret='', source_ip='', timeout='', **kwargs):
        """
        Description: Adds a RADIUS server.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acct_port": acct_port,
            "addr": addr,
            "auth_port": auth_port,
            "max_retries": max_retries,
            "priority": priority,
            "secret": secret,
            "source_ip": source_ip,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SERVER_FOR_CLI,
                                    **kwargs)

    def radius_clear_server_for_cli(self, device_name, addr='', **kwargs):
        """
        Description: Removes a RADIUS server for CLI.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "addr": addr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SERVER_FOR_CLI,
                                    **kwargs)

    def radius_clear_stats_global(self, device_name, **kwargs):
        """
        Description: Clears the RADIUS Statistics for all configured servers.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATS_GLOBAL,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def radius_verify_server_exists(self, device_name, index='', addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [index]       - The Index of the RADIUS server
        [addr]        - The IP address of the RADIUS server

        Verifies that a RADIUS server exists.
        """
        args = {"index": index,
                "addr": addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_SERVER_EXISTS, True,
                                           "Found RADIUS Server {addr}.",
                                           "WARNING: FAILED to find RADIUS Server {addr}!",
                                           **kwargs)

    def radius_verify_server_does_not_exist(self, device_name, index='', addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [index]       - The Index of the RADIUS server
        [addr]        - The IP address of the RADIUS server

        Verifies that a RADIUS server does not exist.
        """
        args = {"index": index,
                "addr": addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_SERVER_EXISTS, False,
                                           "Did not find RADIUS Server {addr}.",
                                           "ERROR: Found RADIUS Server {addr}!",
                                           **kwargs)

    def radius_verify_server_active(self, device_name, index='', addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [index]       - The Index of the RADIUS server
        [addr]        - The IP address of the RADIUS server

        Checks to see if the RADIUS Server Status is set to Active.
        """
        args = {"index": index,
                "addr": addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_SERVER_STATUS, True,
                                           "RADIUS server {addr} Status is correctly set to Active.",
                                           "WARNING: The RADIUS Server Status IS NOT Active!",
                                           **kwargs)

    def radius_verify_server_inactive(self, device_name, index='', addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [index]       - The Index of the RADIUS server
        [addr]        - The IP address of the RADIUS server

        Checks to see if the RADIUS Server Status is set to Inactive.
        """
        args = {"index": index,
                "addr": addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_SERVER_STATUS, False,
                                           "RADIUS server {addr} Status is correctly set to Inactive.",
                                           "WARNING: The RADIUS Server Status IS STILL Active!",
                                           **kwargs)

    def radius_verify_accounting_server_exists(self, device_name, index='', addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [index]       - The Index of the RADIUS server
        [addr]        - The IP address of the RADIUS server

        Verifies that a RADIUS Accounting server exists.
        """
        args = {"index": index,
                "addr": addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCT_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_ACCOUNTING_SERVER_EXISTS, True,
                                           "Found RADIUS Accounting Server {addr}.",
                                           "WARNING: FAILED to find RADIUS Accounting Server {addr}!",
                                           **kwargs)

    def radius_verify_accounting_server_does_not_exist(self, device_name, index='', addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will run against.
        [index]        - The Index of the RADIUS server
        [addr]         - The IP address of the RADIUS server

        Verifies that a RADIUS Accounting server does not exist.
        """
        args = {"index": index,
                "addr": addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCT_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_ACCOUNTING_SERVER_EXISTS, False,
                                           "Did not find RADIUS Accounting Server {addr}.",
                                           "WARNING: Found RADIUS Accounting Server {addr}!",
                                           **kwargs)

    def radius_verify_state_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the Global RADIUS state is set to Enabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_RADIUS_STATE, True,
                                           "RADIUS state is ENABLED on {device_name}.",
                                           "RADIUS state is DISABLED on {device_name}!",
                                           **kwargs)

    def radius_verify_accounting_state_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the Global RADIUS Accounting state is set to Enabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCT_STATE,
                                           self.parse_const.CHECK_RADIUS_ACCOUNTING_STATE, True,
                                           "RADIUS Accounting state is ENABLED on {device_name}.",
                                           "RADIUS Accounting state is DISABLED on {device_name}!",
                                           **kwargs)

    def radius_verify_state_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that Global RADIUS state is set to Disabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_RADIUS_STATE, False,
                                           "RADIUS state was DISABLED on {device_name}.",
                                           "RADIUS state was ENABLED on {device_name}!",
                                           **kwargs)

    def radius_verify_accounting_state_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that Global RADIUS Accounting state is set to Disabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCT_STATE,
                                           self.parse_const.CHECK_RADIUS_ACCOUNTING_STATE, False,
                                           "RADIUS Accounting state is DISABLED on {device_name}.",
                                           "RADIUS Accounting state is ENABLED on {device_name}!",
                                           **kwargs)

    def radius_verify_retries(self, device_name, num='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [num]         - The number of RADIUS server retries to perform

        Verifies the RADIUS Server retries value.
        """
        args = {"num": num}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RETRIES_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_SERVER_RETRIES, True,
                                           "The RADIUS Server Retries is correctly set to {num}.",
                                           "WARNING: The RADIUS Server Retries is NOT SET to {num}!",
                                           **kwargs)

    def radius_verify_retries_set_to_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the RADIUS Retries is set to the Default Setting value.
        EOS = 3 attempts
        EXOS = 3 attempts
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RETRIES_GLOBAL,
                                           self.parse_const.CHECK_IF_RADIUS_RETRIES_IS_SET_TO_DEFAULT_SETTING,
                                           True, "The RADIUS Retries is correctly set to default.",
                                           "WARNING: The RADIUS Retries IS NOT SET to the default!",
                                           **kwargs)

    def radius_verify_timeout(self, device_name, sec='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [sec]         - The RADIUS timeout value in seconds

        Verifies the RADIUS Server timeout value in seconds.
        """
        args = {"sec": sec}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TIMEOUT_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_SERVER_TIMEOUT, True,
                                           "The RADIUS Server Timeout is correctly set to {sec}.",
                                           "WARNING: The RADIUS Server Timeout is NOT SET to {sec}!",
                                           **kwargs)

    def radius_verify_timeout_set_to_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the RADIUS Timeout is set to the Default Setting value.
        EOS = 20 seconds
        EXOS = 3 seconds
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TIMEOUT_GLOBAL,
                                           self.parse_const.CHECK_IF_RADIUS_TIMEOUT_IS_SET_TO_DEFAULT_SETTING,
                                           True, "The RADIUS Timeout is correctly set to default.",
                                           "WARNING: The RADIUS Timeout IS NOT SET to the default!",
                                           **kwargs)

    def radius_verify_algorithm_type_standard(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the Global RADIUS Algorithm Type is set to Standard.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALGORITHM,
                                           self.parse_const.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_STANDARD, True,
                                           "The RADIUS Algorithm Type is properly set to Standard.",
                                           "WARNING: The RADIUS Algorithm Type IS NOT SET TO Standard!",
                                           **kwargs)

    def radius_verify_algorithm_type_round_robin(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the Global RADIUS Algorithm Type is set to Round Robin.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALGORITHM,
                                           self.parse_const.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_ROUND_ROBIN, True,
                                           "The RADIUS Algorithm Type is properly set to Round-Robin.",
                                           "WARNING: The RADIUS Algorithm Type IS NOT SET TO Round-Robin!",
                                           **kwargs)

    def radius_verify_algorithm_type_sticky_round_robin(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the Global RADIUS Algorithm Type is set to Sticky Round Robin.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALGORITHM,
                                           self.parse_const.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_STICKY_ROUND_ROBIN,
                                           True,
                                           "The RADIUS Algorithm Type is properly set to Sticky-Round-Robin.",
                                           "WARNING: The RADIUS Algorithm Type IS NOT SET TO Sticky-Round-Robin!",
                                           **kwargs)

    def radius_verify_algorithm_set_to_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that the RADIUS Algorithm type is set to the Default Setting.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALGORITHM,
                                           self.parse_const.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_STANDARD, True,
                                           "The RADIUS Algorithm Type is properly set to the default.",
                                           "WARNING: The RADIUS Algorithm Type IS NOT SET TO the default!",
                                           **kwargs)

    def radius_verify_enabled_for_management(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that RADIUS is enabled for management users.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_MGMT_AUTHENTICATION_STATE, True,
                                           "RADIUS Auth is enabled for management users.",
                                           "RADIUS Auth IS NOT enabled for management users!",
                                           **kwargs)

    def radius_verify_disabled_for_management(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that RADIUS is disabled for management users.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_MGMT_AUTHENTICATION_STATE, False,
                                           "RADIUS Auth is disabled for management users.",
                                           "RADIUS Auth IS NOT disabled for management users!",
                                           **kwargs)

    def radius_verify_enabled_for_multiauth(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that RADIUS is enabled for multiauth users.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_NETLOGIN_AUTHENTICATION_STATE, True,
                                           "RADIUS Auth is enabled for multiauth users.",
                                           "RADIUS Auth IS NOT enabled for multiauth users!",
                                           **kwargs)

    def radius_verify_disabled_for_multiauth(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies that RADIUS is disabled for multiauth users.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_RADIUS_NETLOGIN_AUTHENTICATION_STATE, False,
                                           "RADIUS Auth is disabled for multiauth users.",
                                           "RADIUS Auth IS NOT disabled for multiauth users!",
                                           **kwargs)

    def radius_verify_max_servers(self, device_name, max_servers='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [max_servers] - The maximum amount of RADIUS servers the system can support.

        Verifies maximum number of RADIUS servers.
        Applies to VOSS only.
        """
        args = {"max_servers": max_servers,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_MAX_SERVERS, True,
                                           "RADIUS max servers is {max_servers}.",
                                           "RADIUS max servers is NOT {max_servers}!",
                                           **kwargs)

    def radius_verify_access_priority(self, device_name, attr_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [attr_value]  - The RADIUS attribute value.

        Verifies the integer value for the Access-Priority attribute.
        Applies to VOSS only.
        """
        args = {"attr_value": attr_value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_ACCESS_PRIORITY, True,
                                           "RADIUS access priority is {attr_value}.",
                                           "RADIUS access priority is NOT {attr_value}!",
                                           **kwargs)

    def radius_verify_accounting_attribute(self, device_name, attr_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [attr_value]  - The RADIUS attribute value.

        Verifies the integer value for the User-Command accounting attribute in RADIUS.
        Applies to VOSS only.
        """
        args = {"attr_value": attr_value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_ACCT_ATTR, True,
                                           "RADIUS User Command accounting attribute is {attr_value}.",
                                           "RADIUS User Command accounting attribute is NOT {attr_value}.!",
                                           **kwargs)

    def radius_verify_include_cli_cmds_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies the inclusion of cli-commands in RADIUS accounting updates is enabled.
        Applies to VOSS only.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_INCLUDE_CLI_CMDS, True,
                                           "RADIUS setting to include CLI commands in acct updates is enabled.",
                                           "RADIUS setting to include CLI commands in acct updates is DISABLED!",
                                           **kwargs)

    def radius_verify_include_cli_cmds_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies the inclusion of cli-commands in RADIUS accounting updates is disabled.
        Applies to VOSS only.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_INCLUDE_CLI_CMDS, False,
                                           "RADIUS setting to include CLI commands in acct updates is disabled.",
                                           "RADIUS setting to include CLI commands in acct updates is ENABLED!",
                                           **kwargs)

    def radius_verify_multicast_address_attribute(self, device_name, attr_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [attr_value]  - The RADIUS attribute value.

        Verifies the Integer value for the multicast address vendor specific attribute.
        Applies to VOSS only.
        """
        args = {"attr_value": attr_value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_MCAST_ADDR_ATTR, True,
                                           "RADIUS multicast address attribute is {attr_value}.",
                                           "RADIUS multicast address attribute is NOT {attr_value}!",
                                           **kwargs)

    def radius_verify_authentication_information_attribute(self, device_name, attr_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [attr_value]  - The RADIUS attribute value.

        Verifies the integer value for Auth-Info vendor specific attribute.
        Applies to VOSS only.
        """
        args = {"attr_value": attr_value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_AUTH_INFO_ATTR, True,
                                           "RADIUS authentication information attribute is {attr_value}.",
                                           "RADIUS authentication information attribute is NOT {attr_value}!",
                                           **kwargs)

    def radius_verify_command_access_attribute(self, device_name, attr_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [attr_value]  - The RADIUS attribute value.

        Verifies the integer value for Command-Access attribute..
        """
        args = {"attr_value": attr_value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_CMD_ACCESS_ATTR, True,
                                           "RADIUS Command-Access attribute is {attr_value}.",
                                           "RADIUS Command-Access attribute is NOT {attr_value}!",
                                           **kwargs)

    def radius_verify_command_attribute(self, device_name, attr_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [attr_value]  - The RADIUS attribute value.

        Verifies the integer value for the Cli-Command attribute.
        Applies to VOSS only.
        """
        args = {"attr_value": attr_value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_CLI_CMD_ATTR, True,
                                           "RADIUS CLI-Command attribute is {attr_value}.",
                                           "RADIUS CLI-Command attribute is NOT {attr_value}!",
                                           **kwargs)

    def radius_verify_profiling_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies Radius CLI Profiling is enabled.
        Applies to VOSS only.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_CLI_PROFILE, True,
                                           "RADIUS CLI profiling is enabled.",
                                           "RADIUS CLI profiling is DISABLED!",
                                           **kwargs)

    def radius_verify_profiling_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies Radius CLI Profiling is disabled.
        Applies to VOSS only.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_CLI_PROFILE, False,
                                           "RADIUS CLI profiling is disabled.",
                                           "RADIUS CLI profiling is ENABLED!",
                                           **kwargs)

    def radius_verify_source_ip_flag_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies the Radius Flag to include the configured IP address as source address in RADIUS packets.
        Applies to VOSS only.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_SRC_IP_FLAG, True,
                                           "Source IP inclusion in RADIUS packets is enabled.",
                                           "Source IP inclusion in RADIUS packets is DISABLED!",
                                           **kwargs)

    def radius_verify_source_ip_flag_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.

        Verifies the Radius Flag to not include the configured IP address as source address in RADIUS packets.
        Applies to VOSS only.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_SRC_IP_FLAG, False,
                                           "Source IP inclusion in RADIUS packets is disabled.",
                                           "Source IP inclusion in RADIUS packets is ENABLED!",
                                           **kwargs)

    def radius_verify_command_count(self, device_name, value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [value]       - The value for the CLI Command count.

        Verifies the integer value Integer value for Cli-Command-Count.
        Applies to VOSS only.
        """
        args = {"value": value,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SCALARS,
                                           self.parse_const.CHECK_RADIUS_CLI_CMD_COUNT, True,
                                           "RADIUS Cli-Command-Count is {value}.",
                                           "RADIUS Cli-Command-Count is NOT {value}!",
                                           **kwargs)

    def radius_verify_server_host_priority(self, device_name, addr='', priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.
        [priority]    - The expected priority value. Range is 1..10.

        Verifies the CLI RADIUS Server priority, used to control which server to choose first to send authentication.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_PRIORITY, True,
                                           "CLI RADIUS server priority is {priority}.",
                                           "CLI RADIUS server priority is NOT {priority}!",
                                           **kwargs)

    def radius_verify_server_host_timeout(self, device_name, addr='', timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.
        [timeout]    - The expected timeout value. Range is 1..20 seconds.

        Verifies the CLI RADIUS time interval in seconds before the client retransmits the packet.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_TIMEOUT, True,
                                           "CLI RADIUS server priority is {timeout}.",
                                           "CLI RADIUS server priority is NOT {timeout}!",
                                           **kwargs)

    def radius_verify_server_host_enabled(self, device_name, addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.

        Verifies that the CLI RADIUS server status is enabled.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "status": "true",
                "status_snmp": "1"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_STATUS, True,
                                           "CLI RADIUS server status is enabled.",
                                           "CLI RADIUS server status is NOT enabled!",
                                           **kwargs)

    def radius_verify_server_host_disabled(self, device_name, addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.

        Verifies that the CLI RADIUS server status is disabled.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "status": "false",
                "status_snmp": "2"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_STATUS, True,
                                           "CLI RADIUS server status is disabled.",
                                           "CLI RADIUS server status is NOT disabled!",
                                           **kwargs)

    def radius_verify_server_host_retries(self, device_name, addr='', max_retries='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.
        [max_retries] - The expected maximum retry value. Range is 0..6.

        Verifies the  maximum number of retransmissions to the CLI RADIUS server.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "max_retries": max_retries}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_MAX_RETRIES, True,
                                           "CLI RADIUS server maximum retries is {max_retries}.",
                                           "CLI RADIUS server maximum retries is NOT {max_retries}!",
                                           **kwargs)

    def radius_verify_server_host_auth_port(self, device_name, addr='', auth_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.
        [auth_port]   - The expected UDP port used by RADIUS authentication.

        Verifies the UDP port the client is using to send authentication requests to the CLI RADIUS server.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "auth_port": auth_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_AUTH_PORT, True,
                                           "CLI RADIUS server authentication port is {auth_port}.",
                                           "CLI RADIUS server authentication port is NOT {auth_port}!",
                                           **kwargs)

    def radius_verify_server_host_accounting_enabled(self, device_name, addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.

        Verifies that the CLI RADIUS server accounting status is enabled.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "status": "true",
                "status_snmp": "1"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_ACCT_STATUS, True,
                                           "CLI RADIUS server accounting status is enabled.",
                                           "CLI RADIUS server accounting status NOT enabled!",
                                           **kwargs)

    def radius_verify_server_host_accounting_disabled(self, device_name, addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.

        Verifies that the CLI RADIUS server accounting status is disabled.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "status": "false",
                "status_snmp": "2"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_ACCT_STATUS, True,
                                           "CLI RADIUS server accounting status is disabled.",
                                           "CLI RADIUS server accounting status is NOT disabled!",
                                           **kwargs)

    def radius_verify_server_host_accounting_port(self, device_name, addr='', acct_port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.
        [acct_port]   - The expected UDP port used by RADIUS accounting.

        Verifies the UDP port the client is using to send accounting reports to the CLI RADIUS server.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "acct_port": acct_port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_ACCT_PORT, True,
                                           "CLI RADIUS server accounting port is {acct_port}.",
                                           "CLI RADIUS server accounting port is NOT {acct_port}!",
                                           **kwargs)

    def radius_verify_server_host_source_ip(self, device_name, addr='', source_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [addr]        - The IP address of the radius server host used by cli.
        [source_ip]   - The expected source IP address used by the device.

        Verifies the source IP address of RADIUS packets.
        Applies to VOSS only.
        """
        args = {"addr": addr,
                "oid_index": SnmpUtils().vos_radius_server_instance_for_cli(addr),
                "source_ip": source_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVERS,
                                           self.parse_const.CHECK_RADIUS_SERVER_HOST_SOURCE_IP, True,
                                           "CLI RADIUS server source IP is {source_ip}.",
                                           "CLI RADIUS server source IP is NOT {source_ip}!",
                                           **kwargs)
