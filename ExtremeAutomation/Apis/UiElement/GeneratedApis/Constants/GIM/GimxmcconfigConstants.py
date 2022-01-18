"""
This class outlines all the constants for the gimxmcconfig API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimxmcconfigConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimxmcconfigConstants(ApiConstants):
    def __init__(self):
        super(GimxmcconfigConstants, self).__init__()
        self.XMC_GIM_ADD_DOMAIN = {"constant": "xmc_gim_add_domain",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.xmc_gim_add_domain}
        self.XMC_GIM_ADD_GIM_IP = {"constant": "xmc_gim_add_gim_ip",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.xmc_gim_add_gim_ip}
        self.XMC_GIM_DEFAULT_BUTTONS_VALIDATION = {"constant": "xmc_gim_default_buttons_validation",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.xmc_gim_default_buttons_validation}
        self.XMC_GIM_DEFAULT_VALIDATION_DETAILS_TAB = {"constant": "xmc_gim_default_validation_details_tab",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.xmc_gim_default_validation_details_tab}
        self.XMC_GIM_DEFAULT_VALIDATION_GIM_TAB = {"constant": "xmc_gim_default_validation_gim_tab",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.xmc_gim_default_validation_gim_tab}
        self.XMC_GIM_DELETE_GIM_IP = {"constant": "xmc_gim_delete_gim_ip",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.xmc_gim_delete_gim_ip}
        self.XMC_GIM_DUPLICATE_IP = {"constant": "xmc_gim_duplicate_ip",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.xmc_gim_duplicate_ip}
        self.XMC_GIM_EDIT_GIM_IP = {"constant": "xmc_gim_edit_gim_ip",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.xmc_gim_edit_gim_ip}
        self.XMC_MAP_DOMAIN_LPR_NONE = {"constant": "xmc_map_domain_lpr_none",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.xmc_map_domain_lpr_none}
        self.XMC_ROOT_LOGIN = {"constant": "xmc_root_login",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.xmc_root_login}
