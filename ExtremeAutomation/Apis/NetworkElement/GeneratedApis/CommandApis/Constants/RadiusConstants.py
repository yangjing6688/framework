"""
This class outlines all the constants for the radius API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(RadiusConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class RadiusConstants(ApiConstants):
    def __init__(self):
        super(RadiusConstants, self).__init__()
        self.CLEAR_ACCT_SERVER = {"constant": "clear_acct_server",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_acct_server}
        self.CLEAR_ACCT_SERVER_GLOBAL = {"constant": "clear_acct_server_global",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.clear_acct_server_global}
        self.CLEAR_ALGORITHM_GLOBAL = {"constant": "clear_algorithm_global",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_algorithm_global}
        self.CLEAR_RETRIES_GLOBAL = {"constant": "clear_retries_global",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_retries_global}
        self.CLEAR_SERVER = {"constant": "clear_server",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.clear_server}
        self.CLEAR_SERVER_FOR_CLI = {"constant": "clear_server_for_cli",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.clear_server_for_cli}
        self.CLEAR_STATE = {"constant": "clear_state",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.clear_state}
        self.CLEAR_STATS_GLOBAL = {"constant": "clear_stats_global",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.clear_stats_global}
        self.CLEAR_TIMEOUT_GLOBAL = {"constant": "clear_timeout_global",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_timeout_global}
        self.DISABLE_ACCT = {"constant": "disable_acct",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_acct}
        self.DISABLE_CLI_PROFILE = {"constant": "disable_cli_profile",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_cli_profile}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_global}
        self.DISABLE_INCLUDE_CLI_CMDS = {"constant": "disable_include_cli_cmds",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.disable_include_cli_cmds}
        self.DISABLE_MGMT = {"constant": "disable_mgmt",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_mgmt}
        self.DISABLE_NETLOGIN = {"constant": "disable_netlogin",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_netlogin}
        self.DISABLE_SRC_IP_FLAG = {"constant": "disable_src_ip_flag",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_src_ip_flag}
        self.ENABLE_ACCT = {"constant": "enable_acct",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_acct}
        self.ENABLE_CLI_PROFILE = {"constant": "enable_cli_profile",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_cli_profile}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_global}
        self.ENABLE_INCLUDE_CLI_CMDS = {"constant": "enable_include_cli_cmds",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.enable_include_cli_cmds}
        self.ENABLE_MGMT = {"constant": "enable_mgmt",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_mgmt}
        self.ENABLE_NETLOGIN = {"constant": "enable_netlogin",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_netlogin}
        self.ENABLE_SRC_IP_FLAG = {"constant": "enable_src_ip_flag",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_src_ip_flag}
        self.SET_ACCESS_PRIORITY = {"constant": "set_access_priority",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_access_priority}
        self.SET_ACCOUNTING_RETRIES_GLOBAL = {"constant": "set_accounting_retries_global",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.set_accounting_retries_global}
        self.SET_ACCOUNTING_TIMEOUT_GLOBAL = {"constant": "set_accounting_timeout_global",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.set_accounting_timeout_global}
        self.SET_ACCT_ATTR = {"constant": "set_acct_attr",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_acct_attr}
        self.SET_ACCT_SERVER = {"constant": "set_acct_server",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_acct_server}
        self.SET_ALGORITHM_GLOBAL_RR = {"constant": "set_algorithm_global_rr",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_algorithm_global_rr}
        self.SET_ALGORITHM_GLOBAL_SRR = {"constant": "set_algorithm_global_srr",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_algorithm_global_srr}
        self.SET_ALGORITHM_GLOBAL_STD = {"constant": "set_algorithm_global_std",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_algorithm_global_std}
        self.SET_AUTH_INFO_ATTR = {"constant": "set_auth_info_attr",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_auth_info_attr}
        self.SET_CLI_CMD_ATTR = {"constant": "set_cli_cmd_attr",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.set_cli_cmd_attr}
        self.SET_CLI_CMD_COUNT = {"constant": "set_cli_cmd_count",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.set_cli_cmd_count}
        self.SET_CMD_ACCESS_ATTR = {"constant": "set_cmd_access_attr",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_cmd_access_attr}
        self.SET_MAX_SERVERS = {"constant": "set_max_servers",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.set_max_servers}
        self.SET_MCAST_ADDR_ATTR = {"constant": "set_mcast_addr_attr",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_mcast_addr_attr}
        self.SET_RETRIES_GLOBAL = {"constant": "set_retries_global",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_retries_global}
        self.SET_SERVER = {"constant": "set_server",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.set_server}
        self.SET_SERVER_FOR_CLI = {"constant": "set_server_for_cli",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_server_for_cli}
        self.SET_TIMEOUT_GLOBAL = {"constant": "set_timeout_global",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_timeout_global}
        self.SHOW_ACCT_GLOBAL = {"constant": "show_acct_global",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_acct_global}
        self.SHOW_ACCT_STATE = {"constant": "show_acct_state",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.show_acct_state}
        self.SHOW_ALGORITHM = {"constant": "show_algorithm",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_algorithm}
        self.SHOW_GLOBAL = {"constant": "show_global",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.show_global}
        self.SHOW_GLOBAL_AUTH_INVALID_SRV_ADDRS = {"constant": "show_global_auth_invalid_srv_addrs",
                                                   "tags": ["COMMAND_SNMP"],
                                                   "link": self.link.show_global_auth_invalid_srv_addrs}
        self.SHOW_GLOBAL_SCALARS = {"constant": "show_global_scalars",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_global_scalars}
        self.SHOW_GLOBAL_SNMP_SCALARS = {"constant": "show_global_snmp_scalars",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.show_global_snmp_scalars}
        self.SHOW_RETRIES_GLOBAL = {"constant": "show_retries_global",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_retries_global}
        self.SHOW_SERVERS = {"constant": "show_servers",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.show_servers}
        self.SHOW_STATE = {"constant": "show_state",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_state}
        self.SHOW_TIMEOUT_GLOBAL = {"constant": "show_timeout_global",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_timeout_global}
