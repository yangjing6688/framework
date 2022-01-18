"""
This class outlines all the constants for the ewcaps API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcapsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcapsConstants(ApiConstants):
    def __init__(self):
        super(EwcapsConstants, self).__init__()
        self.APS_AP_ENVIRONMENT_SHOULD_EXIST = {"constant": "aps_ap_environment_should_exist",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.aps_ap_environment_should_exist}
        self.APS_AP_NAME_SHOULD_EXIST = {"constant": "aps_ap_name_should_exist",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.aps_ap_name_should_exist}
        self.APS_AP_NAME_SHOULD_NOT_EXIST = {"constant": "aps_ap_name_should_not_exist",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.aps_ap_name_should_not_exist}
        self.APS_EDIT_AP_ENVIRONMENT = {"constant": "aps_edit_ap_environment",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.aps_edit_ap_environment}
        self.APS_RENAME_AP_NAME = {"constant": "aps_rename_ap_name",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.aps_rename_ap_name}
