"""
This class outlines all the constants for the port API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PortConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PortConstants(ApiConstants):
    def __init__(self):
        super(PortConstants, self).__init__()
        self.CLEAR_SPEED = {"constant": "clear_speed",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.clear_speed}
        self.DISABLE_FLEX_UNI = {"constant": "disable_flex_uni",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.disable_flex_uni}
        self.DISABLE_JUMBO = {"constant": "disable_jumbo",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.disable_jumbo}
        self.DISABLE_STATE = {"constant": "disable_state",
                              "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                              "link": self.link.disable_state}
        self.ENABLE_FLEX_UNI = {"constant": "enable_flex_uni",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.enable_flex_uni}
        self.ENABLE_JUMBO = {"constant": "enable_jumbo",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.enable_jumbo}
        self.ENABLE_STATE = {"constant": "enable_state",
                             "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                             "link": self.link.enable_state}
        self.SET_ALIAS = {"constant": "set_alias",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.set_alias}
        self.SET_RATE_EGRESS_GBPS = {"constant": "set_rate_egress_gbps",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rate_egress_gbps}
        self.SET_RATE_EGRESS_KBPS = {"constant": "set_rate_egress_kbps",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rate_egress_kbps}
        self.SET_RATE_EGRESS_MBPS = {"constant": "set_rate_egress_mbps",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rate_egress_mbps}
        self.SET_RATE_EGRESS_NO_LIMIT = {"constant": "set_rate_egress_no_limit",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_rate_egress_no_limit}
        self.SET_RATE_FLOOD_BCAST = {"constant": "set_rate_flood_bcast",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rate_flood_bcast}
        self.SET_RATE_FLOOD_MCAST = {"constant": "set_rate_flood_mcast",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_rate_flood_mcast}
        self.SET_RATE_FLOOD_UNKNOWN = {"constant": "set_rate_flood_unknown",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_rate_flood_unknown}
        self.SET_RESTART = {"constant": "set_restart",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_restart}
        self.SET_SPEED = {"constant": "set_speed",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.set_speed}
        self.SHOW_64_BIT_IN_BROADCAST_PACKETS = {"constant": "show_64_bit_in_broadcast_packets",
                                                 "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                                 "link": self.link.show_64_bit_in_broadcast_packets}
        self.SHOW_64_BIT_IN_MULTICAST_PACKETS = {"constant": "show_64_bit_in_multicast_packets",
                                                 "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                                 "link": self.link.show_64_bit_in_multicast_packets}
        self.SHOW_64_BIT_IN_OCTETS = {"constant": "show_64_bit_in_octets",
                                      "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                      "link": self.link.show_64_bit_in_octets}
        self.SHOW_64_BIT_IN_UNICAST_PACKETS = {"constant": "show_64_bit_in_unicast_packets",
                                               "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                               "link": self.link.show_64_bit_in_unicast_packets}
        self.SHOW_64_BIT_OUT_BROADCAST_PACKETS = {"constant": "show_64_bit_out_broadcast_packets",
                                                  "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                                  "link": self.link.show_64_bit_out_broadcast_packets}
        self.SHOW_64_BIT_OUT_MULTICAST_PACKETS = {"constant": "show_64_bit_out_multicast_packets",
                                                  "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                                  "link": self.link.show_64_bit_out_multicast_packets}
        self.SHOW_64_BIT_OUT_OCTETS = {"constant": "show_64_bit_out_octets",
                                       "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                       "link": self.link.show_64_bit_out_octets}
        self.SHOW_64_BIT_OUT_UNICAST_PACKETS = {"constant": "show_64_bit_out_unicast_packets",
                                                "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                                "link": self.link.show_64_bit_out_unicast_packets}
        self.SHOW_ADMIN_STATUS = {"constant": "show_admin_status",
                                  "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                  "link": self.link.show_admin_status}
        self.SHOW_ADVERTISED = {"constant": "show_advertised",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_advertised}
        self.SHOW_ALIAS = {"constant": "show_alias",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_alias}
        self.SHOW_ALL_JUMBO = {"constant": "show_all_jumbo",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_all_jumbo}
        self.SHOW_DOT1D_IFINDEX = {"constant": "show_dot1d_ifindex",
                                   "tags": ["COMMAND_SNMP"],
                                   "link": self.link.show_dot1d_ifindex}
        self.SHOW_FLEX_UNI_STATUS = {"constant": "show_flex_uni_status",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_flex_uni_status}
        self.SHOW_HIGH_SPEED = {"constant": "show_high_speed",
                                "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                "link": self.link.show_high_speed}
        self.SHOW_INFO_DETAIL = {"constant": "show_info_detail",
                                 "tags": ["COMMAND_REST", "COMMAND_SNMP"],
                                 "link": self.link.show_info_detail}
        self.SHOW_IN_BROADCAST_PACKETS = {"constant": "show_in_broadcast_packets",
                                          "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                          "link": self.link.show_in_broadcast_packets}
        self.SHOW_IN_DISCARD_PACKETS = {"constant": "show_in_discard_packets",
                                        "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                        "link": self.link.show_in_discard_packets}
        self.SHOW_IN_ERROR_PACKETS = {"constant": "show_in_error_packets",
                                      "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                      "link": self.link.show_in_error_packets}
        self.SHOW_IN_MULTICAST_PACKETS = {"constant": "show_in_multicast_packets",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.show_in_multicast_packets}
        self.SHOW_IN_OCTETS = {"constant": "show_in_octets",
                               "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                               "link": self.link.show_in_octets}
        self.SHOW_IN_UNICAST_PACKETS = {"constant": "show_in_unicast_packets",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.show_in_unicast_packets}
        self.SHOW_IN_UNKNOWN_PROTOCOL_PACKETS = {"constant": "show_in_unknown_protocol_packets",
                                                 "tags": ["COMMAND_REST", "COMMAND_SNMP"],
                                                 "link": self.link.show_in_unknown_protocol_packets}
        self.SHOW_MAC_ADDRESS = {"constant": "show_mac_address",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                 "link": self.link.show_mac_address}
        self.SHOW_MTU = {"constant": "show_mtu",
                         "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                         "link": self.link.show_mtu}
        self.SHOW_NAMES = {"constant": "show_names",
                           "tags": ["COMMAND_SNMP"],
                           "link": self.link.show_names}
        self.SHOW_OPER_STATUS = {"constant": "show_oper_status",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                 "link": self.link.show_oper_status}
        self.SHOW_OUT_BROADCAST_PACKETS = {"constant": "show_out_broadcast_packets",
                                           "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                           "link": self.link.show_out_broadcast_packets}
        self.SHOW_OUT_DISCARD_PACKETS = {"constant": "show_out_discard_packets",
                                         "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                         "link": self.link.show_out_discard_packets}
        self.SHOW_OUT_ERROR_PACKETS = {"constant": "show_out_error_packets",
                                       "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                       "link": self.link.show_out_error_packets}
        self.SHOW_OUT_MULTICAST_PACKETS = {"constant": "show_out_multicast_packets",
                                           "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                           "link": self.link.show_out_multicast_packets}
        self.SHOW_OUT_OCTETS = {"constant": "show_out_octets",
                                "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                "link": self.link.show_out_octets}
        self.SHOW_OUT_UNICAST_PACKETS = {"constant": "show_out_unicast_packets",
                                         "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                         "link": self.link.show_out_unicast_packets}
        self.SHOW_RATE_LIMIT = {"constant": "show_rate_limit",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_rate_limit}
