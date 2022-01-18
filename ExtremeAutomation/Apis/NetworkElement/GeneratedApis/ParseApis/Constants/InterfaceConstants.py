"""
This class outlines all the constants for the interface API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(InterfaceConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class InterfaceConstants(ApiConstants):
    def __init__(self):
        super(InterfaceConstants, self).__init__()
        self.CHECK_BROUTER_PORT_IPV4 = {"constant": "check_brouter_port_ipv4",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_brouter_port_ipv4}
        self.CHECK_BROUTER_PORT_VLAN = {"constant": "check_brouter_port_vlan",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_brouter_port_vlan}
        self.CHECK_CHASSIS_FORCE_TOPOLOGY_IP_FLAG = {"constant": "check_chassis_force_topology_ip_flag",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_chassis_force_topology_ip_flag}
        self.CHECK_INTERFACE_ENABLED = {"constant": "check_interface_enabled",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_interface_enabled}
        self.CHECK_INTERFACE_EXISTS = {"constant": "check_interface_exists",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_interface_exists}
        self.CHECK_INTERFACE_VLAN_SPB_MULTICAST_ENABLED = {"constant": "check_interface_vlan_spb_multicast_enabled",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_interface_vlan_spb_multicast_enabled}
        self.CHECK_INTERFACE_VLAN_VRF_SPB_MULTICAST_ENABLED = {"constant": "check_interface_vlan_vrf_spb_multicast_enabled",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_interface_vlan_vrf_spb_multicast_enabled}
        self.CHECK_IPV6_ADDRESS_EXISTS = {"constant": "check_ipv6_address_exists",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_ipv6_address_exists}
        self.CHECK_IPV6_INTERFACE_VLAN_IS_ENABLED = {"constant": "check_ipv6_interface_vlan_is_enabled",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_ipv6_interface_vlan_is_enabled}
        self.CHECK_IPV6_LINKLOCAL_EXISTS = {"constant": "check_ipv6_linklocal_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_ipv6_linklocal_exists}
        self.CHECK_IP_ADDRESS_EXISTS = {"constant": "check_ip_address_exists",
                                        "tags": ["PARSE_CLI", "PARSE_REST"],
                                        "link": self.link.check_ip_address_exists}
        self.CHECK_LOOPBACK_EXISTS = {"constant": "check_loopback_exists",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_loopback_exists}
        self.CHECK_LOOPBACK_ID = {"constant": "check_loopback_id",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_loopback_id}
        self.CHECK_LOOPBACK_IPV4_ADDRESS = {"constant": "check_loopback_ipv4_address",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_loopback_ipv4_address}
        self.CHECK_LOOPBACK_IPV6_ADDRESS = {"constant": "check_loopback_ipv6_address",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_loopback_ipv6_address}
        self.CHECK_LOOPBACK_IPV6_ADDRESS_EXISTS = {"constant": "check_loopback_ipv6_address_exists",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_loopback_ipv6_address_exists}
        self.CHECK_MAC_ADDRESS = {"constant": "check_mac_address",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_mac_address}
        self.CHECK_PORT_INTERFACE_NAME = {"constant": "check_port_interface_name",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_port_interface_name}
