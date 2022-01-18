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
        self.CHECK_MAC_SOURCE_ADMIN_PROFILE = {"constant": "check_mac_source_admin_profile",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_mac_source_admin_profile}
        self.CHECK_POLICY_ACL_ACTION_ALL = {"constant": "check_policy_acl_action_all",
                                            "tags": ["PARSE_CLI", "PARSE_REST"],
                                            "link": self.link.check_policy_acl_action_all}
        self.CHECK_POLICY_ACL_ACTION_COS = {"constant": "check_policy_acl_action_cos",
                                            "tags": ["PARSE_CLI", "PARSE_REST"],
                                            "link": self.link.check_policy_acl_action_cos}
        self.CHECK_POLICY_ACL_ACTION_DROP = {"constant": "check_policy_acl_action_drop",
                                             "tags": ["PARSE_CLI", "PARSE_REST"],
                                             "link": self.link.check_policy_acl_action_drop}
        self.CHECK_POLICY_ACL_ACTION_FORWARD = {"constant": "check_policy_acl_action_forward",
                                                "tags": ["PARSE_CLI", "PARSE_REST"],
                                                "link": self.link.check_policy_acl_action_forward}
        self.CHECK_POLICY_ACL_ACTION_MIRROR = {"constant": "check_policy_acl_action_mirror",
                                               "tags": ["PARSE_CLI", "PARSE_REST"],
                                               "link": self.link.check_policy_acl_action_mirror}
        self.CHECK_POLICY_ACL_ACTION_SET_ALL = {"constant": "check_policy_acl_action_set_all",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_acl_action_set_all}
        self.CHECK_POLICY_ACL_ACTION_SET_COS = {"constant": "check_policy_acl_action_set_cos",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_acl_action_set_cos}
        self.CHECK_POLICY_ACL_ACTION_SET_DOES_NOT_EXIST = {"constant": "check_policy_acl_action_set_does_not_exist",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_policy_acl_action_set_does_not_exist}
        self.CHECK_POLICY_ACL_ACTION_SET_DROP = {"constant": "check_policy_acl_action_set_drop",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_policy_acl_action_set_drop}
        self.CHECK_POLICY_ACL_ACTION_SET_FORWARD = {"constant": "check_policy_acl_action_set_forward",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_policy_acl_action_set_forward}
        self.CHECK_POLICY_ACL_ACTION_SET_MIRROR = {"constant": "check_policy_acl_action_set_mirror",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_policy_acl_action_set_mirror}
        self.CHECK_POLICY_ACL_ACTION_SET_SYSLOG_ENABLED = {"constant": "check_policy_acl_action_set_syslog_enabled",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_policy_acl_action_set_syslog_enabled}
        self.CHECK_POLICY_ACL_ACTION_SET_TRAP_ENABLED = {"constant": "check_policy_acl_action_set_trap_enabled",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.check_policy_acl_action_set_trap_enabled}
        self.CHECK_POLICY_ACL_ACTION_SYSLOG_ENABLED = {"constant": "check_policy_acl_action_syslog_enabled",
                                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                                       "link": self.link.check_policy_acl_action_syslog_enabled}
        self.CHECK_POLICY_ACL_ACTION_TRAP_ENABLED = {"constant": "check_policy_acl_action_trap_enabled",
                                                     "tags": ["PARSE_CLI", "PARSE_REST"],
                                                     "link": self.link.check_policy_acl_action_trap_enabled}
        self.CHECK_POLICY_ACL_APP_SIG = {"constant": "check_policy_acl_app_sig",
                                         "tags": ["PARSE_REST"],
                                         "link": self.link.check_policy_acl_app_sig}
        self.CHECK_POLICY_ACL_DOES_NOT_EXIST = {"constant": "check_policy_acl_does_not_exist",
                                                "tags": ["PARSE_CLI", "PARSE_REST"],
                                                "link": self.link.check_policy_acl_does_not_exist}
        self.CHECK_POLICY_ACL_ETHER = {"constant": "check_policy_acl_ether",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_policy_acl_ether}
        self.CHECK_POLICY_ACL_ICMP6TYPE = {"constant": "check_policy_acl_icmp6type",
                                           "tags": ["PARSE_CLI", "PARSE_REST"],
                                           "link": self.link.check_policy_acl_icmp6type}
        self.CHECK_POLICY_ACL_ICMPTYPE = {"constant": "check_policy_acl_icmptype",
                                          "tags": ["PARSE_CLI", "PARSE_REST"],
                                          "link": self.link.check_policy_acl_icmptype}
        self.CHECK_POLICY_ACL_IPDESTSOCKET = {"constant": "check_policy_acl_ipdestsocket",
                                              "tags": ["PARSE_CLI", "PARSE_REST"],
                                              "link": self.link.check_policy_acl_ipdestsocket}
        self.CHECK_POLICY_ACL_IPFRAG = {"constant": "check_policy_acl_ipfrag",
                                        "tags": ["PARSE_CLI", "PARSE_REST"],
                                        "link": self.link.check_policy_acl_ipfrag}
        self.CHECK_POLICY_ACL_IPPROTO = {"constant": "check_policy_acl_ipproto",
                                         "tags": ["PARSE_CLI", "PARSE_REST"],
                                         "link": self.link.check_policy_acl_ipproto}
        self.CHECK_POLICY_ACL_IPSOURCESOCKET = {"constant": "check_policy_acl_ipsourcesocket",
                                                "tags": ["PARSE_CLI", "PARSE_REST"],
                                                "link": self.link.check_policy_acl_ipsourcesocket}
        self.CHECK_POLICY_ACL_IPTOS = {"constant": "check_policy_acl_iptos",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_policy_acl_iptos}
        self.CHECK_POLICY_ACL_IPTTL = {"constant": "check_policy_acl_ipttl",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_policy_acl_ipttl}
        self.CHECK_POLICY_ACL_PROFILE_INDEX = {"constant": "check_policy_acl_profile_index",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_policy_acl_profile_index}
        self.CHECK_POLICY_ACL_PROFILE_INDEX_NONE = {"constant": "check_policy_acl_profile_index_none",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_policy_acl_profile_index_none}
        self.CHECK_POLICY_ACL_RULE_DOES_NOT_EXIST = {"constant": "check_policy_acl_rule_does_not_exist",
                                                     "tags": ["PARSE_CLI", "PARSE_REST"],
                                                     "link": self.link.check_policy_acl_rule_does_not_exist}
        self.CHECK_POLICY_ACL_TCPDESTPORTIP = {"constant": "check_policy_acl_tcpdestportip",
                                               "tags": ["PARSE_CLI", "PARSE_REST"],
                                               "link": self.link.check_policy_acl_tcpdestportip}
        self.CHECK_POLICY_ACL_TCPSOURCEPORTIP = {"constant": "check_policy_acl_tcpsourceportip",
                                                 "tags": ["PARSE_CLI", "PARSE_REST"],
                                                 "link": self.link.check_policy_acl_tcpsourceportip}
        self.CHECK_POLICY_ACL_UDPDESTPORTIP = {"constant": "check_policy_acl_udpdestportip",
                                               "tags": ["PARSE_CLI", "PARSE_REST"],
                                               "link": self.link.check_policy_acl_udpdestportip}
        self.CHECK_POLICY_ACL_UDPSOURCEPORTIP = {"constant": "check_policy_acl_udpsourceportip",
                                                 "tags": ["PARSE_CLI", "PARSE_REST"],
                                                 "link": self.link.check_policy_acl_udpsourceportip}
        self.CHECK_POLICY_ALLOWED_TYPES = {"constant": "check_policy_allowed_types",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_policy_allowed_types}
        self.CHECK_POLICY_GLOBAL_VLAN_AUTHORIZATION_STATE = {"constant": "check_policy_global_vlan_authorization_state",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_policy_global_vlan_authorization_state}
        self.CHECK_POLICY_INVALID_ACTION = {"constant": "check_policy_invalid_action",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_invalid_action}
        self.CHECK_POLICY_INVALID_COUNT = {"constant": "check_policy_invalid_count",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_policy_invalid_count}
        self.CHECK_POLICY_MAP_RESPONSE = {"constant": "check_policy_map_response",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_map_response}
        self.CHECK_POLICY_PROFILE_COS = {"constant": "check_policy_profile_cos",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_policy_profile_cos}
        self.CHECK_POLICY_PROFILE_COS_STATUS = {"constant": "check_policy_profile_cos_status",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_profile_cos_status}
        self.CHECK_POLICY_PROFILE_DISABLE_PORT = {"constant": "check_policy_profile_disable_port",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_policy_profile_disable_port}
        self.CHECK_POLICY_PROFILE_EGRESS_VLAN = {"constant": "check_policy_profile_egress_vlan",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_policy_profile_egress_vlan}
        self.CHECK_POLICY_PROFILE_EXISTS = {"constant": "check_policy_profile_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_profile_exists}
        self.CHECK_POLICY_PROFILE_FORBIDDEN_VLAN = {"constant": "check_policy_profile_forbidden_vlan",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_policy_profile_forbidden_vlan}
        self.CHECK_POLICY_PROFILE_FST = {"constant": "check_policy_profile_fst",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_policy_profile_fst}
        self.CHECK_POLICY_PROFILE_MIRROR_DEST = {"constant": "check_policy_profile_mirror_dest",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_policy_profile_mirror_dest}
        self.CHECK_POLICY_PROFILE_NAME = {"constant": "check_policy_profile_name",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_profile_name}
        self.CHECK_POLICY_PROFILE_PRECEDENCE = {"constant": "check_policy_profile_precedence",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_profile_precedence}
        self.CHECK_POLICY_PROFILE_PVID = {"constant": "check_policy_profile_pvid",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_profile_pvid}
        self.CHECK_POLICY_PROFILE_PVID_STATUS = {"constant": "check_policy_profile_pvid_status",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_policy_profile_pvid_status}
        self.CHECK_POLICY_PROFILE_SYSLOG = {"constant": "check_policy_profile_syslog",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_profile_syslog}
        self.CHECK_POLICY_PROFILE_TCI_OVERWRITE = {"constant": "check_policy_profile_tci_overwrite",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_policy_profile_tci_overwrite}
        self.CHECK_POLICY_PROFILE_TRAP = {"constant": "check_policy_profile_trap",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_profile_trap}
        self.CHECK_POLICY_PROFILE_UNTAGGED_VLAN = {"constant": "check_policy_profile_untagged_vlan",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_policy_profile_untagged_vlan}
        self.CHECK_POLICY_PROFILE_WEB_REDIRECT = {"constant": "check_policy_profile_web_redirect",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_policy_profile_web_redirect}
        self.CHECK_POLICY_RULE_APPLICATION = {"constant": "check_policy_rule_application",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_policy_rule_application}
        self.CHECK_POLICY_RULE_ETHER = {"constant": "check_policy_rule_ether",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_policy_rule_ether}
        self.CHECK_POLICY_RULE_ICMP6TYPE = {"constant": "check_policy_rule_icmp6type",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_rule_icmp6type}
        self.CHECK_POLICY_RULE_ICMPTYPE = {"constant": "check_policy_rule_icmptype",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_policy_rule_icmptype}
        self.CHECK_POLICY_RULE_IP6DEST = {"constant": "check_policy_rule_ip6dest",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_rule_ip6dest}
        self.CHECK_POLICY_RULE_IP6FLOWLABEL = {"constant": "check_policy_rule_ip6flowlabel",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_policy_rule_ip6flowlabel}
        self.CHECK_POLICY_RULE_IP6SOURCE = {"constant": "check_policy_rule_ip6source",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_rule_ip6source}
        self.CHECK_POLICY_RULE_IPDESTSOCKET = {"constant": "check_policy_rule_ipdestsocket",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_policy_rule_ipdestsocket}
        self.CHECK_POLICY_RULE_IPFRAG = {"constant": "check_policy_rule_ipfrag",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_policy_rule_ipfrag}
        self.CHECK_POLICY_RULE_IPPROTO = {"constant": "check_policy_rule_ipproto",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_rule_ipproto}
        self.CHECK_POLICY_RULE_IPSOURCESOCKET = {"constant": "check_policy_rule_ipsourcesocket",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_policy_rule_ipsourcesocket}
        self.CHECK_POLICY_RULE_IPTOS = {"constant": "check_policy_rule_iptos",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_policy_rule_iptos}
        self.CHECK_POLICY_RULE_IPTTL = {"constant": "check_policy_rule_ipttl",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_policy_rule_ipttl}
        self.CHECK_POLICY_RULE_IPXCLASS = {"constant": "check_policy_rule_ipxclass",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_policy_rule_ipxclass}
        self.CHECK_POLICY_RULE_IPXDEST = {"constant": "check_policy_rule_ipxdest",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_rule_ipxdest}
        self.CHECK_POLICY_RULE_IPXDESTSOCKET = {"constant": "check_policy_rule_ipxdestsocket",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_rule_ipxdestsocket}
        self.CHECK_POLICY_RULE_IPXSOURCE = {"constant": "check_policy_rule_ipxsource",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_rule_ipxsource}
        self.CHECK_POLICY_RULE_IPXSOURCESOCKET = {"constant": "check_policy_rule_ipxsourcesocket",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_policy_rule_ipxsourcesocket}
        self.CHECK_POLICY_RULE_IPXTYPE = {"constant": "check_policy_rule_ipxtype",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_rule_ipxtype}
        self.CHECK_POLICY_RULE_LLCDSAPSSAP = {"constant": "check_policy_rule_llcdsapssap",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_policy_rule_llcdsapssap}
        self.CHECK_POLICY_RULE_MACDEST = {"constant": "check_policy_rule_macdest",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_rule_macdest}
        self.CHECK_POLICY_RULE_MACSOURCE = {"constant": "check_policy_rule_macsource",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_policy_rule_macsource}
        self.CHECK_POLICY_RULE_MODEL_ACCESS_LIST = {"constant": "check_policy_rule_model_access_list",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_policy_rule_model_access_list}
        self.CHECK_POLICY_RULE_MODEL_HIERARCHICAL = {"constant": "check_policy_rule_model_hierarchical",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_policy_rule_model_hierarchical}
        self.CHECK_POLICY_RULE_PORT = {"constant": "check_policy_rule_port",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_policy_rule_port}
        self.CHECK_POLICY_RULE_TCI = {"constant": "check_policy_rule_tci",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_policy_rule_tci}
        self.CHECK_POLICY_RULE_TCPDESTPORTIP = {"constant": "check_policy_rule_tcpdestportip",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_rule_tcpdestportip}
        self.CHECK_POLICY_RULE_TCPSOURCEPORTIP = {"constant": "check_policy_rule_tcpsourceportip",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_policy_rule_tcpsourceportip}
        self.CHECK_POLICY_RULE_UDPDESTPORTIP = {"constant": "check_policy_rule_udpdestportip",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_policy_rule_udpdestportip}
        self.CHECK_POLICY_RULE_UDPSOURCEPORTIP = {"constant": "check_policy_rule_udpsourceportip",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_policy_rule_udpsourceportip}
        self.CHECK_POLICY_RULE_VLANTAG = {"constant": "check_policy_rule_vlantag",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_policy_rule_vlantag}
        self.CHECK_POLICY_STATE = {"constant": "check_policy_state",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_policy_state}
        self.CHECK_PORT_ADMIN_PROFILE = {"constant": "check_port_admin_profile",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_port_admin_profile}
        self.STORE_POLICY_INVALID_COUNTER = {"constant": "store_policy_invalid_counter",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.store_policy_invalid_counter}
        self.VERIFY_POLICY_INVALID_COUNT_INCREMENTED = {"constant": "verify_policy_invalid_count_incremented",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.verify_policy_invalid_count_incremented}
