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
        self.CHECK_PORT_64_BIT_IN_BROADCAST_PACKETS = {"constant": "check_port_64_bit_in_broadcast_packets",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_port_64_bit_in_broadcast_packets}
        self.CHECK_PORT_64_BIT_IN_MULTICAST_PACKETS = {"constant": "check_port_64_bit_in_multicast_packets",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_port_64_bit_in_multicast_packets}
        self.CHECK_PORT_64_BIT_IN_OCTETS = {"constant": "check_port_64_bit_in_octets",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_port_64_bit_in_octets}
        self.CHECK_PORT_64_BIT_IN_UNICAST_PACKETS = {"constant": "check_port_64_bit_in_unicast_packets",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_port_64_bit_in_unicast_packets}
        self.CHECK_PORT_64_BIT_OUT_BROADCAST_PACKETS = {"constant": "check_port_64_bit_out_broadcast_packets",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_port_64_bit_out_broadcast_packets}
        self.CHECK_PORT_64_BIT_OUT_MULTICAST_PACKETS = {"constant": "check_port_64_bit_out_multicast_packets",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_port_64_bit_out_multicast_packets}
        self.CHECK_PORT_64_BIT_OUT_OCTETS = {"constant": "check_port_64_bit_out_octets",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_port_64_bit_out_octets}
        self.CHECK_PORT_64_BIT_OUT_UNICAST_PACKETS = {"constant": "check_port_64_bit_out_unicast_packets",
                                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                      "link": self.link.check_port_64_bit_out_unicast_packets}
        self.CHECK_PORT_FLEX_UNI_STATUS = {"constant": "check_port_flex_uni_status",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_port_flex_uni_status}
        self.CHECK_PORT_IN_BROADCAST_PACKETS = {"constant": "check_port_in_broadcast_packets",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_port_in_broadcast_packets}
        self.CHECK_PORT_IN_DISCARD_PACKETS = {"constant": "check_port_in_discard_packets",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_port_in_discard_packets}
        self.CHECK_PORT_IN_ERROR_PACKETS = {"constant": "check_port_in_error_packets",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_port_in_error_packets}
        self.CHECK_PORT_IN_MULTICAST_PACKETS = {"constant": "check_port_in_multicast_packets",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_port_in_multicast_packets}
        self.CHECK_PORT_IN_OCTETS = {"constant": "check_port_in_octets",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_port_in_octets}
        self.CHECK_PORT_IN_UNICAST_PACKETS = {"constant": "check_port_in_unicast_packets",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_port_in_unicast_packets}
        self.CHECK_PORT_IN_UNKNOWN_PROTOCOL_PACKETS = {"constant": "check_port_in_unknown_protocol_packets",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_port_in_unknown_protocol_packets}
        self.CHECK_PORT_OUT_BROADCAST_PACKETS = {"constant": "check_port_out_broadcast_packets",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_port_out_broadcast_packets}
        self.CHECK_PORT_OUT_DISCARD_PACKETS = {"constant": "check_port_out_discard_packets",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_port_out_discard_packets}
        self.CHECK_PORT_OUT_ERROR_PACKETS = {"constant": "check_port_out_error_packets",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_port_out_error_packets}
        self.CHECK_PORT_OUT_MULTICAST_PACKETS = {"constant": "check_port_out_multicast_packets",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_port_out_multicast_packets}
        self.CHECK_PORT_OUT_OCTETS = {"constant": "check_port_out_octets",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.check_port_out_octets}
        self.CHECK_PORT_OUT_UNICAST_PACKETS = {"constant": "check_port_out_unicast_packets",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_port_out_unicast_packets}
        self.CHECK_PORT_PVID = {"constant": "check_port_pvid",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_port_pvid}
        self.CREATE_DOT1D_DICTIONARIES = {"constant": "create_dot1d_dictionaries",
                                          "tags": ["PARSE_SNMP"],
                                          "link": self.link.create_dot1d_dictionaries}
        self.CREATE_INTERFACE_DICTIONARIES = {"constant": "create_interface_dictionaries",
                                              "tags": ["PARSE_SNMP"],
                                              "link": self.link.create_interface_dictionaries}
        self.VALIDATE_JUMBO_FRAME_RECEPTION = {"constant": "validate_jumbo_frame_reception",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.validate_jumbo_frame_reception}
        self.VERIFY_PORT_ADVERTISED_SPEED_DUPLEX = {"constant": "verify_port_advertised_speed_duplex",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.verify_port_advertised_speed_duplex}
        self.VERIFY_PORT_ALIAS = {"constant": "verify_port_alias",
                                  "tags": ["PARSE_CLI", "PARSE_REST", "PARSE_SNMP"],
                                  "link": self.link.verify_port_alias}
        self.VERIFY_PORT_DISABLED = {"constant": "verify_port_disabled",
                                     "tags": ["PARSE_REST"],
                                     "link": self.link.verify_port_disabled}
        self.VERIFY_PORT_ENABLED = {"constant": "verify_port_enabled",
                                    "tags": ["PARSE_CLI", "PARSE_REST", "PARSE_SNMP"],
                                    "link": self.link.verify_port_enabled}
        self.VERIFY_PORT_HIGH_SPEED = {"constant": "verify_port_high_speed",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.verify_port_high_speed}
        self.VERIFY_PORT_MAC_ADDRESS = {"constant": "verify_port_mac_address",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.verify_port_mac_address}
        self.VERIFY_PORT_MTU = {"constant": "verify_port_mtu",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.verify_port_mtu}
        self.VERIFY_PORT_OPERATIONAL = {"constant": "verify_port_operational",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.verify_port_operational}
        self.VERIFY_PORT_RATE_BROADCAST = {"constant": "verify_port_rate_broadcast",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_port_rate_broadcast}
        self.VERIFY_PORT_RATE_EGRESS = {"constant": "verify_port_rate_egress",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_port_rate_egress}
        self.VERIFY_PORT_RATE_MULTICAST = {"constant": "verify_port_rate_multicast",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_port_rate_multicast}
        self.VERIFY_PORT_RATE_UNKNOWN_DESTMAC = {"constant": "verify_port_rate_unknown_destmac",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_port_rate_unknown_destmac}
