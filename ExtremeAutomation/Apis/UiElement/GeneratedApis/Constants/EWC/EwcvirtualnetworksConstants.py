"""
This class outlines all the constants for the ewcvirtualnetworks API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcvirtualnetworksConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcvirtualnetworksConstants(ApiConstants):
    def __init__(self):
        super(EwcvirtualnetworksConstants, self).__init__()
        self.VIRTUAL_NETWORKS_CLICK_SAVE_BUTTON = {"constant": "virtual_networks_click_save_button",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.virtual_networks_click_save_button}
        self.VIRTUAL_NETWORKS_CREATE_VNS = {"constant": "virtual_networks_create_vns",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.virtual_networks_create_vns}
        self.VIRTUAL_NETWORKS_DELETE_VNS = {"constant": "virtual_networks_delete_vns",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.virtual_networks_delete_vns}
        self.VIRTUAL_NETWORKS_EDIT_AUTHENTICATED_POLICY_ROLE_IN_VNS = {"constant": "virtual_networks_edit_authenticated_policy_role_in_vns",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.virtual_networks_edit_authenticated_policy_role_in_vns}
        self.VIRTUAL_NETWORKS_EDIT_NON_AUTHENTICATED_POLICY_ROLE_IN_VNS = {"constant": "virtual_networks_edit_non_authenticated_policy_role_in_vns",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.virtual_networks_edit_non_authenticated_policy_role_in_vns}
        self.VIRTUAL_NETWORKS_EDIT_WLAN_SERVICE_IN_VNS = {"constant": "virtual_networks_edit_wlan_service_in_vns",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.virtual_networks_edit_wlan_service_in_vns}
        self.VIRTUAL_NETWORKS_VNS_SHOULD_BE_ENABLED = {"constant": "virtual_networks_vns_should_be_enabled",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.virtual_networks_vns_should_be_enabled}
        self.VIRTUAL_NETWORKS_VNS_SHOULD_EXIST = {"constant": "virtual_networks_vns_should_exist",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.virtual_networks_vns_should_exist}
        self.VIRTUAL_NETWORKS_VNS_SHOULD_NOT_EXIST = {"constant": "virtual_networks_vns_should_not_exist",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.virtual_networks_vns_should_not_exist}
