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
        self.CLEAR_IPV4_ADDR_PREFIX = {"constant": "clear_ipv4_addr_prefix",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.clear_ipv4_addr_prefix}
        self.CLEAR_IPV4_ADDR_PREFIX_ON_PORT = {"constant": "clear_ipv4_addr_prefix_on_port",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.clear_ipv4_addr_prefix_on_port}
        self.CLEAR_IPV4_BROUTER_PORT = {"constant": "clear_ipv4_brouter_port",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.clear_ipv4_brouter_port}
        self.CLEAR_IPV4_LOOPBACK_ADDR_NETMASK = {"constant": "clear_ipv4_loopback_addr_netmask",
                                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                 "link": self.link.clear_ipv4_loopback_addr_netmask}
        self.CLEAR_IPV6_ADDRESS = {"constant": "clear_ipv6_address",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_ipv6_address}
        self.CLEAR_IPV6_ADDRESS_ON_PORT = {"constant": "clear_ipv6_address_on_port",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.clear_ipv6_address_on_port}
        self.CLEAR_IPV6_LOOPBACK_ADDRESS = {"constant": "clear_ipv6_loopback_address",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.clear_ipv6_loopback_address}
        self.CREATE_INTERFACE = {"constant": "create_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.create_interface}
        self.CREATE_LOOPBACK = {"constant": "create_loopback",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.create_loopback}
        self.DELETE_INTERFACE = {"constant": "delete_interface",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                 "link": self.link.delete_interface}
        self.DELETE_LOOPBACK = {"constant": "delete_loopback",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.delete_loopback}
        self.DISABLE_CHASSIS_FORCE_TOPOLOGY_IP_FLAG = {"constant": "disable_chassis_force_topology_ip_flag",
                                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                       "link": self.link.disable_chassis_force_topology_ip_flag}
        self.DISABLE_INTERFACE = {"constant": "disable_interface",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_interface}
        self.DISABLE_IPV6_FORWARDING = {"constant": "disable_ipv6_forwarding",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.disable_ipv6_forwarding}
        self.DISABLE_IPV6_FORWARDING_GLOBAL = {"constant": "disable_ipv6_forwarding_global",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.disable_ipv6_forwarding_global}
        self.DISABLE_IPV6_VLAN = {"constant": "disable_ipv6_vlan",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_ipv6_vlan}
        self.DISABLE_IP_FORWARDING = {"constant": "disable_ip_forwarding",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.disable_ip_forwarding}
        self.DISABLE_IP_FORWARDING_GLOBAL = {"constant": "disable_ip_forwarding_global",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.disable_ip_forwarding_global}
        self.DISABLE_LOOPBACK = {"constant": "disable_loopback",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_loopback}
        self.DISABLE_VLAN_SPB_MULTICAST = {"constant": "disable_vlan_spb_multicast",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.disable_vlan_spb_multicast}
        self.ENABLE_CHASSIS_FORCE_TOPOLOGY_IP_FLAG = {"constant": "enable_chassis_force_topology_ip_flag",
                                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                      "link": self.link.enable_chassis_force_topology_ip_flag}
        self.ENABLE_INTERFACE = {"constant": "enable_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_interface}
        self.ENABLE_IPV6_FORWARDING = {"constant": "enable_ipv6_forwarding",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.enable_ipv6_forwarding}
        self.ENABLE_IPV6_FORWARDING_GLOBAL = {"constant": "enable_ipv6_forwarding_global",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.enable_ipv6_forwarding_global}
        self.ENABLE_IPV6_VLAN = {"constant": "enable_ipv6_vlan",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_ipv6_vlan}
        self.ENABLE_IP_FORWARDING = {"constant": "enable_ip_forwarding",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.enable_ip_forwarding}
        self.ENABLE_IP_FORWARDING_GLOBAL = {"constant": "enable_ip_forwarding_global",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.enable_ip_forwarding_global}
        self.ENABLE_LOOPBACK = {"constant": "enable_loopback",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_loopback}
        self.ENABLE_VLAN_SPB_MULTICAST = {"constant": "enable_vlan_spb_multicast",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.enable_vlan_spb_multicast}
        self.SET_IPV4_BROUTER_PORT = {"constant": "set_ipv4_brouter_port",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.set_ipv4_brouter_port}
        self.SET_IPV4_LOOPBACK_ADDR_NETMASK = {"constant": "set_ipv4_loopback_addr_netmask",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.set_ipv4_loopback_addr_netmask}
        self.SET_IPV4_LOOPBACK_ADDR_PREFIX = {"constant": "set_ipv4_loopback_addr_prefix",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.set_ipv4_loopback_addr_prefix}
        self.SET_IPV4_PRIMARY_ADDR_NETMASK = {"constant": "set_ipv4_primary_addr_netmask",
                                              "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                              "link": self.link.set_ipv4_primary_addr_netmask}
        self.SET_IPV4_PRIMARY_ADDR_PREFIX = {"constant": "set_ipv4_primary_addr_prefix",
                                             "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                                             "link": self.link.set_ipv4_primary_addr_prefix}
        self.SET_IPV4_PRIMARY_ADDR_PREFIX_ON_PORT = {"constant": "set_ipv4_primary_addr_prefix_on_port",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.set_ipv4_primary_addr_prefix_on_port}
        self.SET_IPV4_SECONDARY_ADDR_NETMASK = {"constant": "set_ipv4_secondary_addr_netmask",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.set_ipv4_secondary_addr_netmask}
        self.SET_IPV4_SECONDARY_ADDR_PREFIX = {"constant": "set_ipv4_secondary_addr_prefix",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.set_ipv4_secondary_addr_prefix}
        self.SET_IPV4_SECONDARY_ADDR_PREFIX_ON_PORT = {"constant": "set_ipv4_secondary_addr_prefix_on_port",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.set_ipv4_secondary_addr_prefix_on_port}
        self.SET_IPV6_ADDRESS = {"constant": "set_ipv6_address",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_ipv6_address}
        self.SET_IPV6_ADDRESS_ON_PORT = {"constant": "set_ipv6_address_on_port",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_ipv6_address_on_port}
        self.SET_IPV6_EUI64_ADDRESS = {"constant": "set_ipv6_eui64_address",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_ipv6_eui64_address}
        self.SET_IPV6_EUI64_ADDRESS_ON_PORT = {"constant": "set_ipv6_eui64_address_on_port",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.set_ipv6_eui64_address_on_port}
        self.SET_IPV6_LINK_LOCAL_ADDR = {"constant": "set_ipv6_link_local_addr",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_ipv6_link_local_addr}
        self.SET_IPV6_LINK_LOCAL_ADDR_ON_PORT = {"constant": "set_ipv6_link_local_addr_on_port",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_ipv6_link_local_addr_on_port}
        self.SET_IPV6_LOOPBACK_ADDRESS = {"constant": "set_ipv6_loopback_address",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.set_ipv6_loopback_address}
        self.SET_MAC_ADDRESS = {"constant": "set_mac_address",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_mac_address}
        self.SHOW_ALL = {"constant": "show_all",
                         "tags": ["COMMAND_CLI", "COMMAND_REST"],
                         "link": self.link.show_all}
        self.SHOW_ALL_PORTS = {"constant": "show_all_ports",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_all_ports}
        self.SHOW_BROUTER_PORT_IPV4 = {"constant": "show_brouter_port_ipv4",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_brouter_port_ipv4}
        self.SHOW_BROUTER_PORT_VLAN = {"constant": "show_brouter_port_vlan",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_brouter_port_vlan}
        self.SHOW_CHASSIS_FORCE_TOPOLOGY_IP_FLAG = {"constant": "show_chassis_force_topology_ip_flag",
                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                    "link": self.link.show_chassis_force_topology_ip_flag}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_REST"],
                          "link": self.link.show_info}
        self.SHOW_INFO_BASIC = {"constant": "show_info_basic",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_info_basic}
        self.SHOW_INFO_PORT = {"constant": "show_info_port",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_info_port}
        self.SHOW_INFO_PORT_BASIC = {"constant": "show_info_port_basic",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_info_port_basic}
        self.SHOW_IPV6_INFO = {"constant": "show_ipv6_info",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_ipv6_info}
        self.SHOW_IPV6_PORT_INFO = {"constant": "show_ipv6_port_info",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_ipv6_port_info}
        self.SHOW_IPV6_VLAN = {"constant": "show_ipv6_vlan",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_ipv6_vlan}
        self.SHOW_LOOPBACK = {"constant": "show_loopback",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_loopback}
        self.SHOW_LOOPBACK_INFO = {"constant": "show_loopback_info",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_loopback_info}
        self.SHOW_VLAN_SPB = {"constant": "show_vlan_spb",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_vlan_spb}
        self.SHOW_VLAN_VRF = {"constant": "show_vlan_vrf",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_vlan_vrf}
        self.SHOW_VLAN_VRF_SPB = {"constant": "show_vlan_vrf_spb",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_vlan_vrf_spb}
