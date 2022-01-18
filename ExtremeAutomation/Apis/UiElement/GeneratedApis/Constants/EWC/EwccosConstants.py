"""
This class outlines all the constants for the ewccos API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwccosConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwccosConstants(ApiConstants):
    def __init__(self):
        super(EwccosConstants, self).__init__()
        self.COS_CLICK_SAVE_BUTTON = {"constant": "cos_click_save_button",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.cos_click_save_button}
        self.COS_CREATE_COS_IRL = {"constant": "cos_create_cos_irl",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.cos_create_cos_irl}
        self.COS_CREATE_COS_ORL = {"constant": "cos_create_cos_orl",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.cos_create_cos_orl}
        self.COS_CREATE_COS_PROFILE = {"constant": "cos_create_cos_profile",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.cos_create_cos_profile}
        self.COS_DELETE_COS_PROFILE = {"constant": "cos_delete_cos_profile",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.cos_delete_cos_profile}
        self.COS_EDIT_COS_IRL = {"constant": "cos_edit_cos_irl",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.cos_edit_cos_irl}
        self.COS_EDIT_COS_ORL = {"constant": "cos_edit_cos_orl",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.cos_edit_cos_orl}
        self.COS_EDIT_COS_PROFILE_IRL = {"constant": "cos_edit_cos_profile_irl",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.cos_edit_cos_profile_irl}
        self.COS_EDIT_COS_PROFILE_ORL = {"constant": "cos_edit_cos_profile_orl",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.cos_edit_cos_profile_orl}
        self.COS_EDIT_COS_PROFILE_PRIORITY = {"constant": "cos_edit_cos_profile_priority",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.cos_edit_cos_profile_priority}
        self.COS_EDIT_COS_PROFILE_PRIORITY_OVERRIDE_FROM_WLAN = {"constant": "cos_edit_cos_profile_priority_override_from_wlan",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.cos_edit_cos_profile_priority_override_from_wlan}
        self.COS_EDIT_COS_PROFILE_TOS = {"constant": "cos_edit_cos_profile_tos",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.cos_edit_cos_profile_tos}
        self.COS_EDIT_COS_PROFILE_TXQ = {"constant": "cos_edit_cos_profile_txq",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.cos_edit_cos_profile_txq}
        self.COS_PROFILE_PRIORITY_OVERRIDE_SHOULD_BE_ENABLED = {"constant": "cos_profile_priority_override_should_be_enabled",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.cos_profile_priority_override_should_be_enabled}
        self.COS_VERIFY_COS_PROFILE_IRL = {"constant": "cos_verify_cos_profile_irl",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.cos_verify_cos_profile_irl}
        self.COS_VERIFY_COS_PROFILE_ORL = {"constant": "cos_verify_cos_profile_orl",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.cos_verify_cos_profile_orl}
        self.COS_VERIFY_COS_PROFILE_PRIORITY = {"constant": "cos_verify_cos_profile_priority",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.cos_verify_cos_profile_priority}
        self.COS_VERIFY_COS_PROFILE_TOS = {"constant": "cos_verify_cos_profile_tos",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.cos_verify_cos_profile_tos}
        self.COS_VERIFY_COS_PROFILE_TXQ = {"constant": "cos_verify_cos_profile_txq",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.cos_verify_cos_profile_txq}
