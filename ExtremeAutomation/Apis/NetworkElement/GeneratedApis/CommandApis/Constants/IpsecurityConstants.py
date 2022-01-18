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
        self.DISABLE_DHCP_SNOOPING = {"constant": "disable_dhcp_snooping",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_dhcp_snooping}
        self.ENABLE_DHCP_SNOOPING = {"constant": "enable_dhcp_snooping",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_dhcp_snooping}
        self.SET_TRUSTED_PORT = {"constant": "set_trusted_port",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_trusted_port}
        self.SHOW_SNOOPING_VLAN = {"constant": "show_snooping_vlan",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_snooping_vlan}
        self.SHOW_SNOOPING_VLAN_ENTRIES = {"constant": "show_snooping_vlan_entries",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_snooping_vlan_entries}
        self.SHOW_SNOOPING_VLAN_VIOLATIONS = {"constant": "show_snooping_vlan_violations",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_snooping_vlan_violations}
        self.SHOW_TRUSTED_PORTS = {"constant": "show_trusted_ports",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_trusted_ports}
