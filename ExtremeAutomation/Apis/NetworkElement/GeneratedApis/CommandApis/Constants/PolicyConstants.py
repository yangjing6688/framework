"""
This class outlines all the constants for the policy API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PolicyConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PolicyConstants(ApiConstants):
    def __init__(self):
        super(PolicyConstants, self).__init__()
        self.CLEAR_ACCESS_LIST = {"constant": "clear_access_list",
                                  "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                  "link": self.link.clear_access_list}
        self.CLEAR_ACCESS_LIST_ACTION_SET = {"constant": "clear_access_list_action_set",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.clear_access_list_action_set}
        self.CLEAR_ACCESS_LIST_ALL = {"constant": "clear_access_list_all",
                                      "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                      "link": self.link.clear_access_list_all}
        self.CLEAR_ACCESS_LIST_RULE = {"constant": "clear_access_list_rule",
                                       "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                       "link": self.link.clear_access_list_rule}
        self.CLEAR_ALL_RULES = {"constant": "clear_all_rules",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.clear_all_rules}
        self.CLEAR_INVALID = {"constant": "clear_invalid",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_invalid}
        self.CLEAR_MAC_SOURCE_ADMIN_PROFILE = {"constant": "clear_mac_source_admin_profile",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.clear_mac_source_admin_profile}
        self.CLEAR_MAPTABLE_RESPONSE = {"constant": "clear_maptable_response",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_maptable_response}
        self.CLEAR_PORT_ADMIN_PROFILE = {"constant": "clear_port_admin_profile",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.clear_port_admin_profile}
        self.CLEAR_PROFILE = {"constant": "clear_profile",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_profile}
        self.CLEAR_PROFILE_RULES = {"constant": "clear_profile_rules",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_profile_rules}
        self.CLEAR_RULE_APPLICATION = {"constant": "clear_rule_application",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_rule_application}
        self.CLEAR_RULE_ETHER = {"constant": "clear_rule_ether",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_rule_ether}
        self.CLEAR_RULE_ICMP6TYPE = {"constant": "clear_rule_icmp6type",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_rule_icmp6type}
        self.CLEAR_RULE_ICMPTYPE = {"constant": "clear_rule_icmptype",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_rule_icmptype}
        self.CLEAR_RULE_IP6DEST = {"constant": "clear_rule_ip6dest",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_rule_ip6dest}
        self.CLEAR_RULE_IP6FLOWLABEL = {"constant": "clear_rule_ip6flowlabel",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_rule_ip6flowlabel}
        self.CLEAR_RULE_IP6SOURCE = {"constant": "clear_rule_ip6source",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_rule_ip6source}
        self.CLEAR_RULE_IPDESTSOCKET = {"constant": "clear_rule_ipdestsocket",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_rule_ipdestsocket}
        self.CLEAR_RULE_IPFRAG = {"constant": "clear_rule_ipfrag",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_rule_ipfrag}
        self.CLEAR_RULE_IPPROTO = {"constant": "clear_rule_ipproto",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_rule_ipproto}
        self.CLEAR_RULE_IPSOURCESOCKET = {"constant": "clear_rule_ipsourcesocket",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_rule_ipsourcesocket}
        self.CLEAR_RULE_IPTOS = {"constant": "clear_rule_iptos",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_rule_iptos}
        self.CLEAR_RULE_IPTTL = {"constant": "clear_rule_ipttl",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_rule_ipttl}
        self.CLEAR_RULE_IPXCLASS = {"constant": "clear_rule_ipxclass",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_rule_ipxclass}
        self.CLEAR_RULE_IPXDEST = {"constant": "clear_rule_ipxdest",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_rule_ipxdest}
        self.CLEAR_RULE_IPXDESTSOCKET = {"constant": "clear_rule_ipxdestsocket",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.clear_rule_ipxdestsocket}
        self.CLEAR_RULE_IPXSOURCE = {"constant": "clear_rule_ipxsource",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_rule_ipxsource}
        self.CLEAR_RULE_IPXSOURCESOCKET = {"constant": "clear_rule_ipxsourcesocket",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.clear_rule_ipxsourcesocket}
        self.CLEAR_RULE_IPXTYPE = {"constant": "clear_rule_ipxtype",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_rule_ipxtype}
        self.CLEAR_RULE_L7 = {"constant": "clear_rule_l7",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_rule_l7}
        self.CLEAR_RULE_LLCDSAPSSAP = {"constant": "clear_rule_llcdsapssap",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_rule_llcdsapssap}
        self.CLEAR_RULE_MACDEST = {"constant": "clear_rule_macdest",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_rule_macdest}
        self.CLEAR_RULE_MACSOURCE = {"constant": "clear_rule_macsource",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_rule_macsource}
        self.CLEAR_RULE_PORT = {"constant": "clear_rule_port",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.clear_rule_port}
        self.CLEAR_RULE_TCI = {"constant": "clear_rule_tci",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_rule_tci}
        self.CLEAR_RULE_TCPDESTPORTIP = {"constant": "clear_rule_tcpdestportip",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.clear_rule_tcpdestportip}
        self.CLEAR_RULE_TCPSOURCEPORTIP = {"constant": "clear_rule_tcpsourceportip",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.clear_rule_tcpsourceportip}
        self.CLEAR_RULE_UDPDESTPORTIP = {"constant": "clear_rule_udpdestportip",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.clear_rule_udpdestportip}
        self.CLEAR_RULE_UDPSOURCEPORTIP = {"constant": "clear_rule_udpsourceportip",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.clear_rule_udpsourceportip}
        self.CLEAR_RULE_VLANTAG = {"constant": "clear_rule_vlantag",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_rule_vlantag}
        self.DISABLE = {"constant": "disable",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.disable}
        self.ENABLE = {"constant": "enable",
                       "tags": ["COMMAND_CLI"],
                       "link": self.link.enable}
        self.SET_ACCESS_LIST = {"constant": "set_access_list",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.set_access_list}
        self.SET_ACCESS_LIST_ACTION_SET = {"constant": "set_access_list_action_set",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_access_list_action_set}
        self.SET_ACCESS_LIST_PROFILE_HIGHEST = {"constant": "set_access_list_profile_highest",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.set_access_list_profile_highest}
        self.SET_ACCESS_LIST_PROFILE_INDEX = {"constant": "set_access_list_profile_index",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.set_access_list_profile_index}
        self.SET_ACCESS_LIST_PROFILE_LOWEST = {"constant": "set_access_list_profile_lowest",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.set_access_list_profile_lowest}
        self.SET_ACCESS_LIST_PROFILE_NONE = {"constant": "set_access_list_profile_none",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_access_list_profile_none}
        self.SET_ACCESS_LIST_RULE_PRECEDENCE_AFTER = {"constant": "set_access_list_rule_precedence_after",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.set_access_list_rule_precedence_after}
        self.SET_ACCESS_LIST_RULE_PRECEDENCE_BEFORE = {"constant": "set_access_list_rule_precedence_before",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.set_access_list_rule_precedence_before}
        self.SET_ACCESS_LIST_RULE_PRECEDENCE_FIRST = {"constant": "set_access_list_rule_precedence_first",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.set_access_list_rule_precedence_first}
        self.SET_ACCESS_LIST_RULE_PRECEDENCE_LAST = {"constant": "set_access_list_rule_precedence_last",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.set_access_list_rule_precedence_last}
        self.SET_INVALID = {"constant": "set_invalid",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_invalid}
        self.SET_MAC_SOURCE_ADMIN_PROFILE = {"constant": "set_mac_source_admin_profile",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_mac_source_admin_profile}
        self.SET_MAPTABLE_RESPONSE = {"constant": "set_maptable_response",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_maptable_response}
        self.SET_PORT_ADMIN_PROFILE = {"constant": "set_port_admin_profile",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_port_admin_profile}
        self.SET_PROFILE = {"constant": "set_profile",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_profile}
        self.SET_PROFILE_ACCESS_CONTROL = {"constant": "set_profile_access_control",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_profile_access_control}
        self.SET_PROFILE_COS = {"constant": "set_profile_cos",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_profile_cos}
        self.SET_PROFILE_COS_STATUS = {"constant": "set_profile_cos_status",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_profile_cos_status}
        self.SET_PROFILE_DISABLE_PORT = {"constant": "set_profile_disable_port",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_profile_disable_port}
        self.SET_PROFILE_EGRESS_VLAN = {"constant": "set_profile_egress_vlan",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_profile_egress_vlan}
        self.SET_PROFILE_FORBIDDEN_VLAN = {"constant": "set_profile_forbidden_vlan",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_profile_forbidden_vlan}
        self.SET_PROFILE_FST = {"constant": "set_profile_fst",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_profile_fst}
        self.SET_PROFILE_MIRROR_DEST = {"constant": "set_profile_mirror_dest",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_profile_mirror_dest}
        self.SET_PROFILE_NAME = {"constant": "set_profile_name",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_profile_name}
        self.SET_PROFILE_PRECEDENCE = {"constant": "set_profile_precedence",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_profile_precedence}
        self.SET_PROFILE_PVID = {"constant": "set_profile_pvid",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_profile_pvid}
        self.SET_PROFILE_PVID_PVID_STATUS = {"constant": "set_profile_pvid_pvid_status",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_profile_pvid_pvid_status}
        self.SET_PROFILE_PVID_STATUS = {"constant": "set_profile_pvid_status",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_profile_pvid_status}
        self.SET_PROFILE_SYSLOG = {"constant": "set_profile_syslog",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_profile_syslog}
        self.SET_PROFILE_TCI_OVERWRITE = {"constant": "set_profile_tci_overwrite",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_profile_tci_overwrite}
        self.SET_PROFILE_TRAFFIC_MIRROR = {"constant": "set_profile_traffic_mirror",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_profile_traffic_mirror}
        self.SET_PROFILE_TRAP = {"constant": "set_profile_trap",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_profile_trap}
        self.SET_PROFILE_UNTAGGED_PVID = {"constant": "set_profile_untagged_pvid",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_profile_untagged_pvid}
        self.SET_PROFILE_UNTAGGED_VLAN = {"constant": "set_profile_untagged_vlan",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_profile_untagged_vlan}
        self.SET_PROFILE_WEB_REDIRECT = {"constant": "set_profile_web_redirect",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_profile_web_redirect}
        self.SET_PROFILE_WITH_NAME = {"constant": "set_profile_with_name",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_profile_with_name}
        self.SET_RULE = {"constant": "set_rule",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_rule}
        self.SET_RULE_APPLICATION = {"constant": "set_rule_application",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rule_application}
        self.SET_RULE_APPLY = {"constant": "set_rule_apply",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_rule_apply}
        self.SET_RULE_ETHER = {"constant": "set_rule_ether",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_rule_ether}
        self.SET_RULE_ICMP6TYPE = {"constant": "set_rule_icmp6type",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_rule_icmp6type}
        self.SET_RULE_ICMPTYPE = {"constant": "set_rule_icmptype",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_rule_icmptype}
        self.SET_RULE_IP6DEST = {"constant": "set_rule_ip6dest",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_rule_ip6dest}
        self.SET_RULE_IP6FLOWLABEL = {"constant": "set_rule_ip6flowlabel",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_rule_ip6flowlabel}
        self.SET_RULE_IP6SOURCE = {"constant": "set_rule_ip6source",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_rule_ip6source}
        self.SET_RULE_IPDESTSOCKET = {"constant": "set_rule_ipdestsocket",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_rule_ipdestsocket}
        self.SET_RULE_IPFRAG = {"constant": "set_rule_ipfrag",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_rule_ipfrag}
        self.SET_RULE_IPPROTO = {"constant": "set_rule_ipproto",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_rule_ipproto}
        self.SET_RULE_IPSOURCESOCKET = {"constant": "set_rule_ipsourcesocket",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_rule_ipsourcesocket}
        self.SET_RULE_IPTOS = {"constant": "set_rule_iptos",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_rule_iptos}
        self.SET_RULE_IPTTL = {"constant": "set_rule_ipttl",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_rule_ipttl}
        self.SET_RULE_IPXCLASS = {"constant": "set_rule_ipxclass",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_rule_ipxclass}
        self.SET_RULE_IPXDEST = {"constant": "set_rule_ipxdest",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_rule_ipxdest}
        self.SET_RULE_IPXDESTSOCKET = {"constant": "set_rule_ipxdestsocket",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_rule_ipxdestsocket}
        self.SET_RULE_IPXSOURCE = {"constant": "set_rule_ipxsource",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_rule_ipxsource}
        self.SET_RULE_IPXSOURCESOCKET = {"constant": "set_rule_ipxsourcesocket",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_rule_ipxsourcesocket}
        self.SET_RULE_IPXTYPE = {"constant": "set_rule_ipxtype",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_rule_ipxtype}
        self.SET_RULE_L7 = {"constant": "set_rule_l7",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_rule_l7}
        self.SET_RULE_L7_CONFIGURE = {"constant": "set_rule_l7_configure",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_rule_l7_configure}
        self.SET_RULE_LLCDSAPSSAP = {"constant": "set_rule_llcdsapssap",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rule_llcdsapssap}
        self.SET_RULE_MACDEST = {"constant": "set_rule_macdest",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_rule_macdest}
        self.SET_RULE_MACSOURCE = {"constant": "set_rule_macsource",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_rule_macsource}
        self.SET_RULE_MODEL_ACCESS_LIST = {"constant": "set_rule_model_access_list",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_rule_model_access_list}
        self.SET_RULE_MODEL_HIERARCHICAL = {"constant": "set_rule_model_hierarchical",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.set_rule_model_hierarchical}
        self.SET_RULE_PORT = {"constant": "set_rule_port",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_rule_port}
        self.SET_RULE_TCI = {"constant": "set_rule_tci",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_rule_tci}
        self.SET_RULE_TCPDESTPORTIP = {"constant": "set_rule_tcpdestportip",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_rule_tcpdestportip}
        self.SET_RULE_TCPSOURCEPORTIP = {"constant": "set_rule_tcpsourceportip",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_rule_tcpsourceportip}
        self.SET_RULE_UDPDESTPORTIP = {"constant": "set_rule_udpdestportip",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_rule_udpdestportip}
        self.SET_RULE_UDPSOURCEPORTIP = {"constant": "set_rule_udpsourceportip",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_rule_udpsourceportip}
        self.SET_RULE_VLANTAG = {"constant": "set_rule_vlantag",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_rule_vlantag}
        self.SET_VLANAUTHORIZATION_STATE = {"constant": "set_vlanauthorization_state",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.set_vlanauthorization_state}
        self.SHOW_ACCESS_LIST_ACTION_SET = {"constant": "show_access_list_action_set",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_access_list_action_set}
        self.SHOW_ACCESS_LIST_LIST_NAME = {"constant": "show_access_list_list_name",
                                           "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                           "link": self.link.show_access_list_list_name}
        self.SHOW_ACCESS_LIST_RULE_NAME = {"constant": "show_access_list_rule_name",
                                           "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                           "link": self.link.show_access_list_rule_name}
        self.SHOW_ADMIN_PROFILES = {"constant": "show_admin_profiles",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_admin_profiles}
        self.SHOW_ALLOW_TYPE = {"constant": "show_allow_type",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_allow_type}
        self.SHOW_ALL_PROFILES = {"constant": "show_all_profiles",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_all_profiles}
        self.SHOW_ALL_RULES = {"constant": "show_all_rules",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_all_rules}
        self.SHOW_INVALID_ACTION = {"constant": "show_invalid_action",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_invalid_action}
        self.SHOW_INVALID_COUNT = {"constant": "show_invalid_count",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_invalid_count}
        self.SHOW_MAP_RESPONSE = {"constant": "show_map_response",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_map_response}
        self.SHOW_PROFILE = {"constant": "show_profile",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_profile}
        self.SHOW_PROFILES = {"constant": "show_profiles",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_profiles}
        self.SHOW_PROFILE_DETAIL = {"constant": "show_profile_detail",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_profile_detail}
        self.SHOW_RULES = {"constant": "show_rules",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_rules}
        self.SHOW_RULES_PROFILE = {"constant": "show_rules_profile",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_rules_profile}
        self.SHOW_STATE = {"constant": "show_state",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_state}
        self.SHOW_VLANAUTHORIZATION = {"constant": "show_vlanauthorization",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_vlanauthorization}
