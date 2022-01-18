"""
This class outlines all the constants for the hostutils API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostutilsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostutilsConstants(ApiConstants):
    def __init__(self):
        super(HostutilsConstants, self).__init__()
        self.ENABLE_DEBUG_MODE = {"constant": "enable_debug_mode",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.enable_debug_mode}
        self.ENABLE_FEATURE_LICENSE = {"constant": "enable_feature_license",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.enable_feature_license}
        self.L2_PING_IPADDR = {"constant": "l2_ping_ipaddr",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.l2_ping_ipaddr}
        self.L2_PING_IPADDR_BURST = {"constant": "l2_ping_ipaddr_burst",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.l2_ping_ipaddr_burst}
        self.L2_PING_IPADDR_DATA_TLV_SIZE = {"constant": "l2_ping_ipaddr_data_tlv_size",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.l2_ping_ipaddr_data_tlv_size}
        self.L2_PING_IPADDR_FRAME_SIZE = {"constant": "l2_ping_ipaddr_frame_size",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.l2_ping_ipaddr_frame_size}
        self.L2_PING_IPADDR_TIME_OUT = {"constant": "l2_ping_ipaddr_time_out",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.l2_ping_ipaddr_time_out}
        self.L2_PING_IPADDR_VRF = {"constant": "l2_ping_ipaddr_vrf",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.l2_ping_ipaddr_vrf}
        self.L2_PING_VLAN_MAC = {"constant": "l2_ping_vlan_mac",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.l2_ping_vlan_mac}
        self.L2_PING_VLAN_ROUTERNODENAME = {"constant": "l2_ping_vlan_routernodename",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.l2_ping_vlan_routernodename}
        self.L2_PING_VLAN_ROUTERNODENAME_BURST = {"constant": "l2_ping_vlan_routernodename_burst",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.l2_ping_vlan_routernodename_burst}
        self.L2_PING_VLAN_ROUTERNODENAME_DATA_TLV_SIZE = {"constant": "l2_ping_vlan_routernodename_data_tlv_size",
                                                          "tags": ["COMMAND_CLI"],
                                                          "link": self.link.l2_ping_vlan_routernodename_data_tlv_size}
        self.L2_PING_VLAN_ROUTERNODENAME_FRAME_SIZE = {"constant": "l2_ping_vlan_routernodename_frame_size",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.l2_ping_vlan_routernodename_frame_size}
        self.L2_PING_VLAN_ROUTERNODENAME_PRIORITY = {"constant": "l2_ping_vlan_routernodename_priority",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.l2_ping_vlan_routernodename_priority}
        self.L2_PING_VLAN_ROUTERNODENAME_SOURCE_MODE_NODAL = {"constant": "l2_ping_vlan_routernodename_source_mode_nodal",
                                                              "tags": ["COMMAND_CLI"],
                                                              "link": self.link.l2_ping_vlan_routernodename_source_mode_nodal}
        self.L2_PING_VLAN_ROUTERNODENAME_SOURCE_MODE_NOVLANMAC = {"constant": "l2_ping_vlan_routernodename_source_mode_novlanmac",
                                                                  "tags": ["COMMAND_CLI"],
                                                                  "link": self.link.l2_ping_vlan_routernodename_source_mode_novlanmac}
        self.L2_PING_VLAN_ROUTERNODENAME_TESTFILL_PATTERN_ALL_ZERO = {"constant": "l2_ping_vlan_routernodename_testfill_pattern_all_zero",
                                                                      "tags": ["COMMAND_CLI"],
                                                                      "link": self.link.l2_ping_vlan_routernodename_testfill_pattern_all_zero}
        self.L2_PING_VLAN_ROUTERNODENAME_TESTFILL_PATTERN_ALL_ZERO_CRC = {"constant": "l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc",
                                                                          "tags": ["COMMAND_CLI"],
                                                                          "link": self.link.l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc}
        self.L2_PING_VLAN_ROUTERNODENAME_TESTFILL_PATTERN_PSEUDO_RAND_BIT_SEQ = {"constant": "l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq",
                                                                                 "tags": ["COMMAND_CLI"],
                                                                                 "link": self.link.l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq}
        self.L2_PING_VLAN_ROUTERNODENAME_TESTFILL_PATTERN_PSEUDO_RAND_BIT_SEQ_CRC = {"constant": "l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc",
                                                                                     "tags": ["COMMAND_CLI"],
                                                                                     "link": self.link.l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc}
        self.L2_PING_VLAN_ROUTERNODENAME_TIMEOUT = {"constant": "l2_ping_vlan_routernodename_timeout",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.l2_ping_vlan_routernodename_timeout}
        self.L2_TRACEMROUTE = {"constant": "l2_tracemroute",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.l2_tracemroute}
        self.L2_TRACEMROUTE_PRIORITY = {"constant": "l2_tracemroute_priority",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.l2_tracemroute_priority}
        self.L2_TRACEMROUTE_TTL = {"constant": "l2_tracemroute_ttl",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.l2_tracemroute_ttl}
        self.L2_TRACEMROUTE_VLAN = {"constant": "l2_tracemroute_vlan",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.l2_tracemroute_vlan}
        self.L2_TRACEMROUTE_VRF = {"constant": "l2_tracemroute_vrf",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.l2_tracemroute_vrf}
        self.L2_TRACEROUTE_IPADDR = {"constant": "l2_traceroute_ipaddr",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.l2_traceroute_ipaddr}
        self.L2_TRACEROUTE_IPADDR_TTL = {"constant": "l2_traceroute_ipaddr_ttl",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.l2_traceroute_ipaddr_ttl}
        self.L2_TRACEROUTE_IPADDR_VRF = {"constant": "l2_traceroute_ipaddr_vrf",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.l2_traceroute_ipaddr_vrf}
        self.L2_TRACEROUTE_VLAN_MAC = {"constant": "l2_traceroute_vlan_mac",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.l2_traceroute_vlan_mac}
        self.L2_TRACEROUTE_VLAN_ROUTERNODENAME_PRIORITY = {"constant": "l2_traceroute_vlan_routernodename_priority",
                                                           "tags": ["COMMAND_CLI"],
                                                           "link": self.link.l2_traceroute_vlan_routernodename_priority}
        self.L2_TRACEROUTE_VLAN_ROUTERNODENAME_SOURCE_MODE_NODAL = {"constant": "l2_traceroute_vlan_routernodename_source_mode_nodal",
                                                                    "tags": ["COMMAND_CLI"],
                                                                    "link": self.link.l2_traceroute_vlan_routernodename_source_mode_nodal}
        self.L2_TRACEROUTE_VLAN_ROUTERNODENAME_SOURCE_MODE_NOVLANMAC = {"constant": "l2_traceroute_vlan_routernodename_source_mode_novlanmac",
                                                                        "tags": ["COMMAND_CLI"],
                                                                        "link": self.link.l2_traceroute_vlan_routernodename_source_mode_novlanmac}
        self.L2_TRACEROUTE_VLAN_ROUTERNODENAME_TTL = {"constant": "l2_traceroute_vlan_routernodename_ttl",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.l2_traceroute_vlan_routernodename_ttl}
        self.L2_TRACETREE_VLAN_ISID = {"constant": "l2_tracetree_vlan_isid",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.l2_tracetree_vlan_isid}
        self.L2_TRACETREE_VLAN_ISID_MAC = {"constant": "l2_tracetree_vlan_isid_mac",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.l2_tracetree_vlan_isid_mac}
        self.L2_TRACETREE_VLAN_ISID_PRIORITY = {"constant": "l2_tracetree_vlan_isid_priority",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.l2_tracetree_vlan_isid_priority}
        self.L2_TRACETREE_VLAN_ISID_ROUTERNODENAME = {"constant": "l2_tracetree_vlan_isid_routernodename",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.l2_tracetree_vlan_isid_routernodename}
        self.L2_TRACETREE_VLAN_ISID_ROUTERNODENAME_PRIORITY = {"constant": "l2_tracetree_vlan_isid_routernodename_priority",
                                                               "tags": ["COMMAND_CLI"],
                                                               "link": self.link.l2_tracetree_vlan_isid_routernodename_priority}
        self.L2_TRACETREE_VLAN_ISID_ROUTERNODENAME_SOURCE_MODE_NODAL = {"constant": "l2_tracetree_vlan_isid_routernodename_source_mode_nodal",
                                                                        "tags": ["COMMAND_CLI"],
                                                                        "link": self.link.l2_tracetree_vlan_isid_routernodename_source_mode_nodal}
        self.L2_TRACETREE_VLAN_ISID_ROUTERNODENAME_TTL = {"constant": "l2_tracetree_vlan_isid_routernodename_ttl",
                                                          "tags": ["COMMAND_CLI"],
                                                          "link": self.link.l2_tracetree_vlan_isid_routernodename_ttl}
        self.L2_TRACETREE_VLAN_ISID_SOURCE_MODE_NODAL = {"constant": "l2_tracetree_vlan_isid_source_mode_nodal",
                                                         "tags": ["COMMAND_CLI"],
                                                         "link": self.link.l2_tracetree_vlan_isid_source_mode_nodal}
        self.L2_TRACETREE_VLAN_ISID_TTL = {"constant": "l2_tracetree_vlan_isid_ttl",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.l2_tracetree_vlan_isid_ttl}
        self.PING_HOST = {"constant": "ping_host",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.ping_host}
        self.RETURN_DEBUG_CREDS = {"constant": "return_debug_creds",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.return_debug_creds}
        self.SSH_TO_IP = {"constant": "ssh_to_ip",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.ssh_to_ip}
        self.TELNET_TO_IP = {"constant": "telnet_to_ip",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.telnet_to_ip}
