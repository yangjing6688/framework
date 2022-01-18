"""
This class outlines all the constants for the policyvlans API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PolicyvlansConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PolicyvlansConstants(ApiConstants):
    def __init__(self):
        super(PolicyvlansConstants, self).__init__()
        self.POLICY_VLANS_CLICK_ALWAYS_TO_WRITE_VLAN_TO_DEVICES_CHECKBOX = {"constant": "policy_vlans_click_always_to_write_vlan_to_devices_checkbox",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.policy_vlans_click_always_to_write_vlan_to_devices_checkbox}
        self.POLICY_VLANS_CLICK_CANCEL_TO_DISCARD_NEW_VLAN = {"constant": "policy_vlans_click_cancel_to_discard_new_vlan",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.policy_vlans_click_cancel_to_discard_new_vlan}
        self.POLICY_VLANS_CLICK_DYNAMIC_EGRESS_CHECKBOX = {"constant": "policy_vlans_click_dynamic_egress_checkbox",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_vlans_click_dynamic_egress_checkbox}
        self.POLICY_VLANS_CLICK_NEXT_AVAILABLE_VID_BUTTON = {"constant": "policy_vlans_click_next_available_vid_button",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.policy_vlans_click_next_available_vid_button}
        self.POLICY_VLANS_CLICK_OK_TO_SAVE_NEW_VLAN = {"constant": "policy_vlans_click_ok_to_save_new_vlan",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.policy_vlans_click_ok_to_save_new_vlan}
        self.POLICY_VLANS_CLICK_VLAN_TO_OPEN_VLAN_SETTING_PAGE = {"constant": "policy_vlans_click_vlan_to_open_vlan_setting_page",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.policy_vlans_click_vlan_to_open_vlan_setting_page}
        self.POLICY_VLANS_ENTER_VLAN_NAME_AND_VID = {"constant": "policy_vlans_enter_vlan_name_and_vid",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.policy_vlans_enter_vlan_name_and_vid}
        self.POLICY_VLANS_OPEN_CREATE_VLAN_WINDOW = {"constant": "policy_vlans_open_create_vlan_window",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.policy_vlans_open_create_vlan_window}
        self.POLICY_VLANS_RELOAD_VLANS = {"constant": "policy_vlans_reload_vlans",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.policy_vlans_reload_vlans}
        self.POLICY_VLANS_RIGHT_CLICK_ON_GLOBAL_VLANS = {"constant": "policy_vlans_right_click_on_global_vlans",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.policy_vlans_right_click_on_global_vlans}
