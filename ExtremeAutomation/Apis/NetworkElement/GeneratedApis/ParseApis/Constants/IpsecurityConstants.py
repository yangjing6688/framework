"""
This class outlines all the constants for the ipsecurity API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(IpsecurityConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class IpsecurityConstants(ApiConstants):
    def __init__(self):
        super(IpsecurityConstants, self).__init__()
        self.CHECK_DHCP_SNOOPING_VLAN = {"constant": "check_dhcp_snooping_vlan",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_dhcp_snooping_vlan}
        self.CHECK_DHCP_SNOOPING_VLAN_ENTRIES = {"constant": "check_dhcp_snooping_vlan_entries",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_dhcp_snooping_vlan_entries}
        self.CHECK_DHCP_SNOOPING_VLAN_VIOLATIONS = {"constant": "check_dhcp_snooping_vlan_violations",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_dhcp_snooping_vlan_violations}
        self.CHECK_TRUSTED_PORT_GLOBAL = {"constant": "check_trusted_port_global",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_trusted_port_global}
