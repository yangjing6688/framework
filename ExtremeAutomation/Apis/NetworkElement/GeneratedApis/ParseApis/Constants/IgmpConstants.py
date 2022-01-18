"""
This class outlines all the constants for the igmp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(IgmpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class IgmpConstants(ApiConstants):
    def __init__(self):
        super(IgmpConstants, self).__init__()
        self.CHECK_IGMP_SNOOPING_COMPATIBILITY_MODE_STATE = {"constant": "check_igmp_snooping_compatibility_mode_state",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.check_igmp_snooping_compatibility_mode_state}
        self.CHECK_IGMP_SNOOPING_DYNAMIC_DOWNGRADE_STATE = {"constant": "check_igmp_snooping_dynamic_downgrade_state",
                                                            "tags": ["PARSE_CLI"],
                                                            "link": self.link.check_igmp_snooping_dynamic_downgrade_state}
        self.CHECK_IGMP_SNOOPING_EXPLICIT_HOST_TRACKING_STATE = {"constant": "check_igmp_snooping_explicit_host_tracking_state",
                                                                 "tags": ["PARSE_CLI"],
                                                                 "link": self.link.check_igmp_snooping_explicit_host_tracking_state}
        self.CHECK_IGMP_SNOOPING_PROXY_STATE = {"constant": "check_igmp_snooping_proxy_state",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_igmp_snooping_proxy_state}
        self.CHECK_IGMP_SNOOPING_QUERIER_ADDRESS = {"constant": "check_igmp_snooping_querier_address",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_igmp_snooping_querier_address}
        self.CHECK_IGMP_SNOOPING_QUERIER_ADDRESS_IS_REMOVED = {"constant": "check_igmp_snooping_querier_address_is_removed",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_igmp_snooping_querier_address_is_removed}
        self.CHECK_IGMP_SNOOPING_QUERIER_STATE = {"constant": "check_igmp_snooping_querier_state",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_igmp_snooping_querier_state}
        self.CHECK_IGMP_SNOOPING_STATE = {"constant": "check_igmp_snooping_state",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_igmp_snooping_state}
        self.CHECK_IGMP_SNOOPING_VLAN_STATE = {"constant": "check_igmp_snooping_vlan_state",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_igmp_snooping_vlan_state}
        self.CHECK_IGMP_STATE = {"constant": "check_igmp_state",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.check_igmp_state}
        self.CHECK_IGMP_VERSION = {"constant": "check_igmp_version",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_igmp_version}
        self.CHECK_IGMP_VLAN_STATE = {"constant": "check_igmp_vlan_state",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_igmp_vlan_state}
        self.VERIFY_IGMP_GROUP = {"constant": "verify_igmp_group",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.verify_igmp_group}
