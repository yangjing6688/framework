"""
This class outlines all the constants for the vrrp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VrrpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VrrpConstants(ApiConstants):
    def __init__(self):
        super(VrrpConstants, self).__init__()
        self.CHECK_VRRP_GLOBALLY_DISABLED = {"constant": "check_vrrp_globally_disabled",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_vrrp_globally_disabled}
        self.CHECK_VRRP_GLOBALLY_ENABLED = {"constant": "check_vrrp_globally_enabled",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_vrrp_globally_enabled}
        self.CHECK_VRRP_GROUP_EXISTS = {"constant": "check_vrrp_group_exists",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_vrrp_group_exists}
        self.CHECK_VRRP_STATE_IS_BACKUP = {"constant": "check_vrrp_state_is_backup",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_vrrp_state_is_backup}
        self.CHECK_VRRP_STATE_IS_MASTER = {"constant": "check_vrrp_state_is_master",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_vrrp_state_is_master}
        self.CHECK_VRRP_VLAN_EXISTS = {"constant": "check_vrrp_vlan_exists",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_vrrp_vlan_exists}
        self.CHECK_VRRP_VLAN_FABRIC_ROUTING_IS_SET = {"constant": "check_vrrp_vlan_fabric_routing_is_set",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_vrrp_vlan_fabric_routing_is_set}
        self.CHECK_VRRP_VLAN_IP_ADDRESS_IS_SET = {"constant": "check_vrrp_vlan_ip_address_is_set",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_vrrp_vlan_ip_address_is_set}
        self.CHECK_VRRP_VLAN_IS_ENABLED = {"constant": "check_vrrp_vlan_is_enabled",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_vrrp_vlan_is_enabled}
        self.CHECK_VRRP_VLAN_PRIORITY_IS_SET = {"constant": "check_vrrp_vlan_priority_is_set",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_vrrp_vlan_priority_is_set}
