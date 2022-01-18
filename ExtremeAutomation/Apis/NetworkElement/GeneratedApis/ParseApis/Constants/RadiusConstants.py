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
        self.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_ROUND_ROBIN = {"constant": "check_if_radius_algorithm_type_is_round_robin",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.check_if_radius_algorithm_type_is_round_robin}
        self.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_STANDARD = {"constant": "check_if_radius_algorithm_type_is_standard",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_if_radius_algorithm_type_is_standard}
        self.CHECK_IF_RADIUS_ALGORITHM_TYPE_IS_STICKY_ROUND_ROBIN = {"constant": "check_if_radius_algorithm_type_is_sticky_round_robin",
                                                                     "tags": ["PARSE_CLI"],
                                                                     "link": self.link.check_if_radius_algorithm_type_is_sticky_round_robin}
        self.CHECK_IF_RADIUS_RETRIES_IS_SET_TO_DEFAULT_SETTING = {"constant": "check_if_radius_retries_is_set_to_default_setting",
                                                                  "tags": ["PARSE_CLI"],
                                                                  "link": self.link.check_if_radius_retries_is_set_to_default_setting}
        self.CHECK_IF_RADIUS_TIMEOUT_IS_SET_TO_DEFAULT_SETTING = {"constant": "check_if_radius_timeout_is_set_to_default_setting",
                                                                  "tags": ["PARSE_CLI"],
                                                                  "link": self.link.check_if_radius_timeout_is_set_to_default_setting}
        self.CHECK_RADIUS_ACCESS_PRIORITY = {"constant": "check_radius_access_priority",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_radius_access_priority}
        self.CHECK_RADIUS_ACCOUNTING_SERVER_EXISTS = {"constant": "check_radius_accounting_server_exists",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_radius_accounting_server_exists}
        self.CHECK_RADIUS_ACCOUNTING_STATE = {"constant": "check_radius_accounting_state",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_radius_accounting_state}
        self.CHECK_RADIUS_ACCT_ATTR = {"constant": "check_radius_acct_attr",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.check_radius_acct_attr}
        self.CHECK_RADIUS_AUTH_INFO_ATTR = {"constant": "check_radius_auth_info_attr",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_radius_auth_info_attr}
        self.CHECK_RADIUS_CLI_CMD_ATTR = {"constant": "check_radius_cli_cmd_attr",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_radius_cli_cmd_attr}
        self.CHECK_RADIUS_CLI_CMD_COUNT = {"constant": "check_radius_cli_cmd_count",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_radius_cli_cmd_count}
        self.CHECK_RADIUS_CLI_PROFILE = {"constant": "check_radius_cli_profile",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_radius_cli_profile}
        self.CHECK_RADIUS_CMD_ACCESS_ATTR = {"constant": "check_radius_cmd_access_attr",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_radius_cmd_access_attr}
        self.CHECK_RADIUS_INCLUDE_CLI_CMDS = {"constant": "check_radius_include_cli_cmds",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_radius_include_cli_cmds}
        self.CHECK_RADIUS_MAX_SERVERS = {"constant": "check_radius_max_servers",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_radius_max_servers}
        self.CHECK_RADIUS_MCAST_ADDR_ATTR = {"constant": "check_radius_mcast_addr_attr",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_radius_mcast_addr_attr}
        self.CHECK_RADIUS_MGMT_AUTHENTICATION_STATE = {"constant": "check_radius_mgmt_authentication_state",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_radius_mgmt_authentication_state}
        self.CHECK_RADIUS_NETLOGIN_AUTHENTICATION_STATE = {"constant": "check_radius_netlogin_authentication_state",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_radius_netlogin_authentication_state}
        self.CHECK_RADIUS_SERVER_EXISTS = {"constant": "check_radius_server_exists",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_radius_server_exists}
        self.CHECK_RADIUS_SERVER_HOST_ACCT_PORT = {"constant": "check_radius_server_host_acct_port",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_radius_server_host_acct_port}
        self.CHECK_RADIUS_SERVER_HOST_ACCT_STATUS = {"constant": "check_radius_server_host_acct_status",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_radius_server_host_acct_status}
        self.CHECK_RADIUS_SERVER_HOST_AUTH_PORT = {"constant": "check_radius_server_host_auth_port",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_radius_server_host_auth_port}
        self.CHECK_RADIUS_SERVER_HOST_MAX_RETRIES = {"constant": "check_radius_server_host_max_retries",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_radius_server_host_max_retries}
        self.CHECK_RADIUS_SERVER_HOST_PRIORITY = {"constant": "check_radius_server_host_priority",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_radius_server_host_priority}
        self.CHECK_RADIUS_SERVER_HOST_SOURCE_IP = {"constant": "check_radius_server_host_source_ip",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_radius_server_host_source_ip}
        self.CHECK_RADIUS_SERVER_HOST_STATUS = {"constant": "check_radius_server_host_status",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_radius_server_host_status}
        self.CHECK_RADIUS_SERVER_HOST_TIMEOUT = {"constant": "check_radius_server_host_timeout",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_radius_server_host_timeout}
        self.CHECK_RADIUS_SERVER_RETRIES = {"constant": "check_radius_server_retries",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_radius_server_retries}
        self.CHECK_RADIUS_SERVER_STATUS = {"constant": "check_radius_server_status",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_radius_server_status}
        self.CHECK_RADIUS_SERVER_TIMEOUT = {"constant": "check_radius_server_timeout",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_radius_server_timeout}
        self.CHECK_RADIUS_SRC_IP_FLAG = {"constant": "check_radius_src_ip_flag",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_radius_src_ip_flag}
        self.CHECK_RADIUS_STATE = {"constant": "check_radius_state",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_radius_state}
        self.GET_RADIUS_SERVER_PORT = {"constant": "get_radius_server_port",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.get_radius_server_port}
