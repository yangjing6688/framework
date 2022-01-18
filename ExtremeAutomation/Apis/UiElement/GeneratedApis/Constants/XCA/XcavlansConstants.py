"""
This class outlines all the constants for the xcavlans API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcavlansConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcavlansConstants(ApiConstants):
    def __init__(self):
        super(XcavlansConstants, self).__init__()
        self.CLICK_ADD_TO_CREATE_NEW_VLAN = {"constant": "click_add_to_create_new_vlan",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.click_add_to_create_new_vlan}
        self.CLICK_VLAN_NAME_TO_OPEN_VLAN_SETTINGS = {"constant": "click_vlan_name_to_open_vlan_settings",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.click_vlan_name_to_open_vlan_settings}
        self.CONFIG_DHCP_LOCAL_SERVER = {"constant": "config_dhcp_local_server",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.config_dhcp_local_server}
        self.CONFIG_DHCP_RELAY_SERVERS = {"constant": "config_dhcp_relay_servers",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.config_dhcp_relay_servers}
        self.DELETE_EXISTING_VLAN = {"constant": "delete_existing_vlan",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.delete_existing_vlan}
        self.EDIT_ADVANCED_SETTINGS_FOR_VLAN = {"constant": "edit_advanced_settings_for_vlan",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.edit_advanced_settings_for_vlan}
        self.EDIT_INFO_FOR_VLAN_IN_BRIDGED_AT_AC_MODE = {"constant": "edit_info_for_vlan_in_bridged_at_ac_mode",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.edit_info_for_vlan_in_bridged_at_ac_mode}
        self.EDIT_INFO_FOR_VLAN_IN_BRIDGED_AT_AP_MODE = {"constant": "edit_info_for_vlan_in_bridged_at_ap_mode",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.edit_info_for_vlan_in_bridged_at_ap_mode}
        self.EDIT_INFO_FOR_VLAN_IN_FABRIC_ATTACH_MODE = {"constant": "edit_info_for_vlan_in_fabric_attach_mode",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.edit_info_for_vlan_in_fabric_attach_mode}
        self.EDIT_LAYER3_SETTINGS_FOR_VLAN = {"constant": "edit_layer3_settings_for_vlan",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.edit_layer3_settings_for_vlan}
        self.SAVE_SETTINGS_AND_BACK_TO_VLANS_PAGE = {"constant": "save_settings_and_back_to_vlans_page",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.save_settings_and_back_to_vlans_page}
        self.VERIFY_VLAN_DOES_NOT_EXIST = {"constant": "verify_vlan_does_not_exist",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.verify_vlan_does_not_exist}
        self.VERIFY_VLAN_EXISTS = {"constant": "verify_vlan_exists",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.verify_vlan_exists}
