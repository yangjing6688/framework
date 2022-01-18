"""
This class outlines all the constants for the spanningtree API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SpanningtreeConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SpanningtreeConstants(ApiConstants):
    def __init__(self):
        super(SpanningtreeConstants, self).__init__()
        self.CHECK_CIST_REGIONAL_ROOT = {"constant": "check_cist_regional_root",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_cist_regional_root}
        self.CHECK_INSTANCE_REGIONAL_ROOT = {"constant": "check_instance_regional_root",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_instance_regional_root}
        self.CHECK_INSTANCE_ROOT_PORT = {"constant": "check_instance_root_port",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_instance_root_port}
        self.CHECK_MSTP_BRIDGE_ADDRESS = {"constant": "check_mstp_bridge_address",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_mstp_bridge_address}
        self.CHECK_MSTP_CIST_FORWARD_DELAY = {"constant": "check_mstp_cist_forward_delay",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_mstp_cist_forward_delay}
        self.CHECK_MSTP_CIST_MAX_AGE = {"constant": "check_mstp_cist_max_age",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_mstp_cist_max_age}
        self.CHECK_MSTP_CIST_REGIONAL_ROOT = {"constant": "check_mstp_cist_regional_root",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_mstp_cist_regional_root}
        self.CHECK_MSTP_CIST_REGIONAL_ROOT_COST = {"constant": "check_mstp_cist_regional_root_cost",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_mstp_cist_regional_root_cost}
        self.CHECK_MSTP_CIST_ROOT = {"constant": "check_mstp_cist_root",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_mstp_cist_root}
        self.CHECK_MSTP_CIST_ROOT_COST = {"constant": "check_mstp_cist_root_cost",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_mstp_cist_root_cost}
        self.CHECK_MSTP_CIST_ROOT_PORT = {"constant": "check_mstp_cist_root_port",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_mstp_cist_root_port}
        self.CHECK_MSTP_ENABLED_ON_INTERFACE = {"constant": "check_mstp_enabled_on_interface",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_mstp_enabled_on_interface}
        self.CHECK_REGIONAL_NAME = {"constant": "check_regional_name",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_regional_name}
        self.CHECK_REVISION_LEVEL = {"constant": "check_revision_level",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_revision_level}
        self.CHECK_SPANNING_TREE_BRIDGE_PRIORITY = {"constant": "check_spanning_tree_bridge_priority",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_spanning_tree_bridge_priority}
        self.CHECK_SPANNING_TREE_CIST_ROOT = {"constant": "check_spanning_tree_cist_root",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_spanning_tree_cist_root}
        self.CHECK_SPANNING_TREE_ENABLED = {"constant": "check_spanning_tree_enabled",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_spanning_tree_enabled}
        self.CHECK_SPANNING_TREE_LOOP_PROTECT_ENABLED = {"constant": "check_spanning_tree_loop_protect_enabled",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.check_spanning_tree_loop_protect_enabled}
        self.CHECK_SPANNING_TREE_ROOT = {"constant": "check_spanning_tree_root",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_spanning_tree_root}
        self.CHECK_SPANNING_TREE_SPAN_GUARD_ENABLED = {"constant": "check_spanning_tree_span_guard_enabled",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_spanning_tree_span_guard_enabled}
        self.CHECK_SPANNING_TREE_TC_INCREMENTED = {"constant": "check_spanning_tree_tc_incremented",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_spanning_tree_tc_incremented}
        self.CHECK_SPANNING_TREE_TC_SAME = {"constant": "check_spanning_tree_tc_same",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_spanning_tree_tc_same}
        self.CHECK_SPANNING_TREE_VERSION = {"constant": "check_spanning_tree_version",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_spanning_tree_version}
        self.CHECK_STP_BOOT_FLAG_IS_MSTP = {"constant": "check_stp_boot_flag_is_mstp",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_stp_boot_flag_is_mstp}
        self.CHECK_STP_BOOT_FLAG_IS_RSTP = {"constant": "check_stp_boot_flag_is_rstp",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_stp_boot_flag_is_rstp}
        self.CHECK_STP_BPDUGUARD = {"constant": "check_stp_bpduguard",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_stp_bpduguard}
        self.CHECK_STP_BRIDGE_FWD_DELAY = {"constant": "check_stp_bridge_fwd_delay",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_stp_bridge_fwd_delay}
        self.CHECK_STP_BRIDGE_HELLO_TIME = {"constant": "check_stp_bridge_hello_time",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_stp_bridge_hello_time}
        self.CHECK_STP_BRIDGE_MAX_AGE = {"constant": "check_stp_bridge_max_age",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_stp_bridge_max_age}
        self.CHECK_STP_FWD_DELAY = {"constant": "check_stp_fwd_delay",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_stp_fwd_delay}
        self.CHECK_STP_HELLO_TIME = {"constant": "check_stp_hello_time",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_stp_hello_time}
        self.CHECK_STP_MAX_AGE = {"constant": "check_stp_max_age",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_stp_max_age}
        self.CHECK_STP_PORTADMIN = {"constant": "check_stp_portadmin",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_stp_portadmin}
        self.CHECK_STP_PORTADMIN_OPER = {"constant": "check_stp_portadmin_oper",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_stp_portadmin_oper}
        self.CHECK_STP_PORTS_LINK_TYPE_IS_EDGE = {"constant": "check_stp_ports_link_type_is_edge",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_stp_ports_link_type_is_edge}
        self.CHECK_STP_PORTS_LINK_TYPE_IS_POINT_TO_POINT = {"constant": "check_stp_ports_link_type_is_point_to_point",
                                                            "tags": ["PARSE_CLI"],
                                                            "link": self.link.check_stp_ports_link_type_is_point_to_point}
        self.CHECK_STP_PORT_AUTOEDGE = {"constant": "check_stp_port_autoedge",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_stp_port_autoedge}
        self.CHECK_STP_PORT_CONFIG_TYPE = {"constant": "check_stp_port_config_type",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_stp_port_config_type}
        self.CHECK_STP_PORT_RESTRICTED = {"constant": "check_stp_port_restricted",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_stp_port_restricted}
        self.CHECK_STP_PORT_ROLE = {"constant": "check_stp_port_role",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_stp_port_role}
        self.CHECK_STP_PORT_STATE = {"constant": "check_stp_port_state",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_stp_port_state}
        self.CHECK_STP_ROOT_FWD_DELAY = {"constant": "check_stp_root_fwd_delay",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_stp_root_fwd_delay}
        self.CHECK_STP_ROOT_HELLO_TIME = {"constant": "check_stp_root_hello_time",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_stp_root_hello_time}
        self.CHECK_STP_ROOT_MAX_AGE = {"constant": "check_stp_root_max_age",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_stp_root_max_age}
        self.RETURN_SPANNING_TREE_CONFIG_DIGEST = {"constant": "return_spanning_tree_config_digest",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.return_spanning_tree_config_digest}
        self.STORE_SPANNING_TREE_TC_COUNTER = {"constant": "store_spanning_tree_tc_counter",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.store_spanning_tree_tc_counter}
