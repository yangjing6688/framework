"""
This class outlines all the constants for the rsmlt API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(RsmltConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class RsmltConstants(ApiConstants):
    def __init__(self):
        super(RsmltConstants, self).__init__()
        self.VERIFY_RSMLT_DISABLED_ON_INTERFACE_VLAN = {"constant": "verify_rsmlt_disabled_on_interface_vlan",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.verify_rsmlt_disabled_on_interface_vlan}
        self.VERIFY_RSMLT_EDGE_SUPPORT_DISABLED = {"constant": "verify_rsmlt_edge_support_disabled",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_rsmlt_edge_support_disabled}
        self.VERIFY_RSMLT_EDGE_SUPPORT_ENABLED = {"constant": "verify_rsmlt_edge_support_enabled",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.verify_rsmlt_edge_support_enabled}
        self.VERIFY_RSMLT_ENABLED_ON_INTERFACE_VLAN = {"constant": "verify_rsmlt_enabled_on_interface_vlan",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.verify_rsmlt_enabled_on_interface_vlan}
        self.VERIFY_RSMLT_HOLDDOWN_TIMER_IS_SET = {"constant": "verify_rsmlt_holddown_timer_is_set",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_rsmlt_holddown_timer_is_set}
        self.VERIFY_RSMLT_HOLDUP_TIMER_IS_SET = {"constant": "verify_rsmlt_holdup_timer_is_set",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_rsmlt_holdup_timer_is_set}
