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
        self.CLEAR_BPDUGUARD_TIMEOUT = {"constant": "clear_bpduguard_timeout",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_bpduguard_timeout}
        self.CLEAR_MSTI_VLAN_MAPPING = {"constant": "clear_msti_vlan_mapping",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_msti_vlan_mapping}
        self.CLEAR_STP_MODE = {"constant": "clear_stp_mode",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_stp_mode}
        self.CLEAR_TC_TRAP = {"constant": "clear_tc_trap",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_tc_trap}
        self.CREATE_MST_INSTANCE = {"constant": "create_mst_instance",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.create_mst_instance}
        self.CREATE_MST_VLAN_INSTANCE = {"constant": "create_mst_vlan_instance",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.create_mst_vlan_instance}
        self.DELETE_MST_INSTANCE = {"constant": "delete_mst_instance",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.delete_mst_instance}
        self.DELETE_MST_VLAN_INSTANCE = {"constant": "delete_mst_vlan_instance",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.delete_mst_vlan_instance}
        self.DISABLE_AUTO_EDGE = {"constant": "disable_auto_edge",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_auto_edge}
        self.DISABLE_BPDUGUARD = {"constant": "disable_bpduguard",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_bpduguard}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_MSTP_GLOBAL = {"constant": "disable_mstp_global",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_mstp_global}
        self.DISABLE_MSTP_ON_PORT = {"constant": "disable_mstp_on_port",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.disable_mstp_on_port}
        self.DISABLE_MST_INSTANCE = {"constant": "disable_mst_instance",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.disable_mst_instance}
        self.DISABLE_PORT_ADMIN = {"constant": "disable_port_admin",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.disable_port_admin}
        self.DISABLE_RSTP_GLOBAL = {"constant": "disable_rstp_global",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_rstp_global}
        self.DISABLE_VLAN_AUTOBIND = {"constant": "disable_vlan_autobind",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_vlan_autobind}
        self.ENABLE_AUTO_EDGE = {"constant": "enable_auto_edge",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_auto_edge}
        self.ENABLE_BPDUGUARD = {"constant": "enable_bpduguard",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_bpduguard}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_MSTP_GLOBAL = {"constant": "enable_mstp_global",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_mstp_global}
        self.ENABLE_MSTP_ON_PORT = {"constant": "enable_mstp_on_port",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.enable_mstp_on_port}
        self.ENABLE_MST_INSTANCE = {"constant": "enable_mst_instance",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_mst_instance}
        self.ENABLE_PORT_ADMIN = {"constant": "enable_port_admin",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.enable_port_admin}
        self.ENABLE_RSTP_GLOBAL = {"constant": "enable_rstp_global",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_rstp_global}
        self.ENABLE_VLAN_AUTOBIND = {"constant": "enable_vlan_autobind",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_vlan_autobind}
        self.SET_BOOT_FLAG_MSTP = {"constant": "set_boot_flag_mstp",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_boot_flag_mstp}
        self.SET_BOOT_FLAG_RSTP = {"constant": "set_boot_flag_rstp",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_boot_flag_rstp}
        self.SET_BPDUGUARD_TIMEOUT = {"constant": "set_bpduguard_timeout",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_bpduguard_timeout}
        self.SET_FWD_DELAY = {"constant": "set_fwd_delay",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_fwd_delay}
        self.SET_HELLO_TIME = {"constant": "set_hello_time",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_hello_time}
        self.SET_INSTANCE_CIST = {"constant": "set_instance_cist",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_instance_cist}
        self.SET_INSTANCE_MSTI = {"constant": "set_instance_msti",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_instance_msti}
        self.SET_MAX_AGE = {"constant": "set_max_age",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_max_age}
        self.SET_MSTI_VLAN_MAPPING = {"constant": "set_msti_vlan_mapping",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_msti_vlan_mapping}
        self.SET_MST_INSTANCE_TAG = {"constant": "set_mst_instance_tag",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_mst_instance_tag}
        self.SET_MST_REGION_NAME = {"constant": "set_mst_region_name",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_mst_region_name}
        self.SET_MST_REVISION_LEVEL = {"constant": "set_mst_revision_level",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_mst_revision_level}
        self.SET_PORT_LINK_TYPE_EDGE = {"constant": "set_port_link_type_edge",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_port_link_type_edge}
        self.SET_PORT_LINK_TYPE_POINT_TO_POINT = {"constant": "set_port_link_type_point_to_point",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.set_port_link_type_point_to_point}
        self.SET_PRIORITY = {"constant": "set_priority",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_priority}
        self.SET_PRIORITY_MODE = {"constant": "set_priority_mode",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_priority_mode}
        self.SET_RESTRICTED_ROLE = {"constant": "set_restricted_role",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_restricted_role}
        self.SET_RESTRICTED_TCN = {"constant": "set_restricted_tcn",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_restricted_tcn}
        self.SET_STP_MODE = {"constant": "set_stp_mode",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_stp_mode}
        self.SET_TC_TRAP = {"constant": "set_tc_trap",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_tc_trap}
        self.SHOW_AUTOEDGE = {"constant": "show_autoedge",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_autoedge}
        self.SHOW_BOOT_FLAG = {"constant": "show_boot_flag",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_boot_flag}
        self.SHOW_BPDUGUARD = {"constant": "show_bpduguard",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_bpduguard}
        self.SHOW_INFO_DETAIL = {"constant": "show_info_detail",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_info_detail}
        self.SHOW_INFO_SUMMARY = {"constant": "show_info_summary",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_info_summary}
        self.SHOW_INSTANCE_INFO = {"constant": "show_instance_info",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_instance_info}
        self.SHOW_INSTANCE_INFO_DETAIL = {"constant": "show_instance_info_detail",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_instance_info_detail}
        self.SHOW_MSTP_EDGE = {"constant": "show_mstp_edge",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_mstp_edge}
        self.SHOW_MSTP_INFO_DETAIL = {"constant": "show_mstp_info_detail",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_mstp_info_detail}
        self.SHOW_MSTP_INFO_SUMMARY = {"constant": "show_mstp_info_summary",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_mstp_info_summary}
        self.SHOW_MSTP_INSTANCE_INFO = {"constant": "show_mstp_instance_info",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_mstp_instance_info}
        self.SHOW_MSTP_PORT_ADMIN = {"constant": "show_mstp_port_admin",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_mstp_port_admin}
        self.SHOW_MSTP_PORT_INFO = {"constant": "show_mstp_port_info",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_mstp_port_info}
        self.SHOW_MSTP_PORT_INFO_DETAIL = {"constant": "show_mstp_port_info_detail",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_mstp_port_info_detail}
        self.SHOW_MSTP_PORT_ROLE = {"constant": "show_mstp_port_role",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_mstp_port_role}
        self.SHOW_MST_DIGEST = {"constant": "show_mst_digest",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_mst_digest}
        self.SHOW_PORT_ADMIN = {"constant": "show_port_admin",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_port_admin}
        self.SHOW_PORT_EDGE = {"constant": "show_port_edge",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_port_edge}
        self.SHOW_PORT_INFO = {"constant": "show_port_info",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_port_info}
        self.SHOW_PORT_INFO_DETAIL = {"constant": "show_port_info_detail",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_info_detail}
        self.SHOW_PORT_ROLE = {"constant": "show_port_role",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_port_role}
        self.SHOW_STP_PORT_ROLE = {"constant": "show_stp_port_role",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_stp_port_role}
        self.SHOW_VERSION = {"constant": "show_version",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_version}
