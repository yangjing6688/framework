"""
This class outlines all the constants for the pim API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PimConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PimConstants(ApiConstants):
    def __init__(self):
        super(PimConstants, self).__init__()
        self.CLEAR_CACHE = {"constant": "clear_cache",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.clear_cache}
        self.CLEAR_RP = {"constant": "clear_rp",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.clear_rp}
        self.DISABLE = {"constant": "disable",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.disable}
        self.DISABLE_INTERFACE = {"constant": "disable_interface",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_interface}
        self.DISABLE_INTERFACE_VLAN = {"constant": "disable_interface_vlan",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.disable_interface_vlan}
        self.DISABLE_SPARSE = {"constant": "disable_sparse",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_sparse}
        self.ENABLE = {"constant": "enable",
                       "tags": ["COMMAND_CLI"],
                       "link": self.link.enable}
        self.ENABLE_INTERFACE = {"constant": "enable_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_interface}
        self.ENABLE_INTERFACE_VLAN = {"constant": "enable_interface_vlan",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.enable_interface_vlan}
        self.ENABLE_SPARSE = {"constant": "enable_sparse",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_sparse}
        self.ENABLE_SSM = {"constant": "enable_ssm",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.enable_ssm}
        self.SET_BSR_PRIORITY = {"constant": "set_bsr_priority",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_bsr_priority}
        self.SET_BSR_PRIORITY_VLAN = {"constant": "set_bsr_priority_vlan",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_bsr_priority_vlan}
        self.SET_INTERFACE_ACTIVE = {"constant": "set_interface_active",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_interface_active}
        self.SET_INTERFACE_PASSIVE = {"constant": "set_interface_passive",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_interface_passive}
        self.SET_RP = {"constant": "set_rp",
                       "tags": ["COMMAND_CLI"],
                       "link": self.link.set_rp}
        self.SET_RP_STATIC = {"constant": "set_rp_static",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_rp_static}
        self.SET_VLAN_ACTIVE = {"constant": "set_vlan_active",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_vlan_active}
        self.SET_VLAN_PASSIVE = {"constant": "set_vlan_passive",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_vlan_passive}
        self.SHOW_BSR = {"constant": "show_bsr",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_bsr}
        self.SHOW_CACHE = {"constant": "show_cache",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_cache}
        self.SHOW_CACHE_GROUP = {"constant": "show_cache_group",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_cache_group}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
        self.SHOW_INTERFACE = {"constant": "show_interface",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_interface}
        self.SHOW_RP = {"constant": "show_rp",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.show_rp}
        self.SHOW_RP_SET = {"constant": "show_rp_set",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_rp_set}
        self.SHOW_RP_SET_GROUP = {"constant": "show_rp_set_group",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_rp_set_group}
        self.SHOW_VLAN = {"constant": "show_vlan",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_vlan}
