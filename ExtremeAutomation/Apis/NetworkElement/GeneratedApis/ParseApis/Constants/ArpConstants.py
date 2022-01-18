"""
This class outlines all the constants for the arp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ArpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ArpConstants(ApiConstants):
    def __init__(self):
        super(ArpConstants, self).__init__()
        self.VERIFY_ARP_ENTRY_EXISTS = {"constant": "verify_arp_entry_exists",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.verify_arp_entry_exists}
        self.VERIFY_ARP_VRF_ENTRY_EXISTS = {"constant": "verify_arp_vrf_entry_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.verify_arp_vrf_entry_exists}
