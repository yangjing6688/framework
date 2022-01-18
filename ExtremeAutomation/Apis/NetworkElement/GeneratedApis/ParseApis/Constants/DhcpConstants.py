"""
This class outlines all the constants for the dhcp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DhcpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DhcpConstants(ApiConstants):
    def __init__(self):
        super(DhcpConstants, self).__init__()
        self.CHECK_BOOTPRELAY_INTERFACE_DISABLED = {"constant": "check_bootprelay_interface_disabled",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_bootprelay_interface_disabled}
        self.CHECK_BOOTPRELAY_INTERFACE_ENABLED = {"constant": "check_bootprelay_interface_enabled",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_bootprelay_interface_enabled}
        self.CHECK_BOOTPRELAY_SERVERS = {"constant": "check_bootprelay_servers",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_bootprelay_servers}
        self.CHECK_DHCP_VLAN_ADDRESS_RANGE = {"constant": "check_dhcp_vlan_address_range",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_dhcp_vlan_address_range}
        self.CHECK_DHCP_VLAN_ASSIGNED_IP_ADDRESS_ALLOCATION = {"constant": "check_dhcp_vlan_assigned_ip_address_allocation",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_dhcp_vlan_assigned_ip_address_allocation}
        self.CHECK_DHCP_VLAN_ASSIGNED_MAC_ADDRESS_ALLOCATION = {"constant": "check_dhcp_vlan_assigned_mac_address_allocation",
                                                                "tags": ["PARSE_CLI"],
                                                                "link": self.link.check_dhcp_vlan_assigned_mac_address_allocation}
        self.CHECK_DHCP_VLAN_DEFAULT_GATEWAY = {"constant": "check_dhcp_vlan_default_gateway",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_dhcp_vlan_default_gateway}
        self.CHECK_DHCP_VLAN_ENABLED_PORTS = {"constant": "check_dhcp_vlan_enabled_ports",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_dhcp_vlan_enabled_ports}
        self.CHECK_DHCP_VLAN_LEASE_TIMER = {"constant": "check_dhcp_vlan_lease_timer",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_dhcp_vlan_lease_timer}
        self.CHECK_DHCP_VLAN_NETLOGIN_LEASE_TIMER = {"constant": "check_dhcp_vlan_netlogin_lease_timer",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_dhcp_vlan_netlogin_lease_timer}
        self.CHECK_DHCP_VLAN_NETLOGIN_LEASE_TIMER_DEFAULT = {"constant": "check_dhcp_vlan_netlogin_lease_timer_default",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_dhcp_vlan_netlogin_lease_timer_default}
        self.CHECK_DHCP_VLAN_PRIMARY_DNS = {"constant": "check_dhcp_vlan_primary_dns",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_dhcp_vlan_primary_dns}
        self.CHECK_DHCP_VLAN_SECONDARY_DNS = {"constant": "check_dhcp_vlan_secondary_dns",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_dhcp_vlan_secondary_dns}
