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
        self.CHECK_PIM_BSR = {"constant": "check_pim_bsr",
                              "tags": ["PARSE_CLI"],
                              "link": self.link.check_pim_bsr}
        self.CHECK_PIM_BSR_PRIORITY = {"constant": "check_pim_bsr_priority",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_pim_bsr_priority}
        self.CHECK_PIM_CACHE = {"constant": "check_pim_cache",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_pim_cache}
        self.CHECK_PIM_CANDIDATE_BSR_PRIORITY_ON_INTERFACE = {"constant": "check_pim_candidate_bsr_priority_on_interface",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.check_pim_candidate_bsr_priority_on_interface}
        self.CHECK_PIM_CANDIDATE_BSR_PRIORITY_ON_VLAN = {"constant": "check_pim_candidate_bsr_priority_on_vlan",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.check_pim_candidate_bsr_priority_on_vlan}
        self.CHECK_PIM_CANDIDATE_RP_IP = {"constant": "check_pim_candidate_rp_ip",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_pim_candidate_rp_ip}
        self.CHECK_PIM_CANDIDATE_RP_IP_GROUP_MASK = {"constant": "check_pim_candidate_rp_ip_group_mask",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_pim_candidate_rp_ip_group_mask}
        self.CHECK_PIM_INTERFACE_STATE = {"constant": "check_pim_interface_state",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_pim_interface_state}
        self.CHECK_PIM_MODE = {"constant": "check_pim_mode",
                               "tags": ["PARSE_CLI"],
                               "link": self.link.check_pim_mode}
        self.CHECK_PIM_OPERTYPE = {"constant": "check_pim_opertype",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_pim_opertype}
        self.CHECK_PIM_RP = {"constant": "check_pim_rp",
                             "tags": ["PARSE_CLI"],
                             "link": self.link.check_pim_rp}
        self.CHECK_PIM_STATE = {"constant": "check_pim_state",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_pim_state}
        self.CHECK_PIM_STATIC_RP = {"constant": "check_pim_static_rp",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_pim_static_rp}
        self.CHECK_PIM_TYPE_SPARSE = {"constant": "check_pim_type_sparse",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_pim_type_sparse}
        self.CHECK_PIM_TYPE_SSM = {"constant": "check_pim_type_ssm",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_pim_type_ssm}
        self.CHECK_PIM_VLAN_STATE = {"constant": "check_pim_vlan_state",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_pim_vlan_state}
        self.VERIFY_PIM_ANY_SOURCE_GROUP = {"constant": "verify_pim_any_source_group",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.verify_pim_any_source_group}
        self.VERIFY_PIM_EXPECTED_BSR = {"constant": "verify_pim_expected_bsr",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_pim_expected_bsr}
        self.VERIFY_PIM_RP_SET = {"constant": "verify_pim_rp_set",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.verify_pim_rp_set}
        self.VERIFY_PIM_RP_SET_GROUP = {"constant": "verify_pim_rp_set_group",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_pim_rp_set_group}
        self.VERIFY_PIM_SOURCE_GROUP = {"constant": "verify_pim_source_group",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_pim_source_group}
