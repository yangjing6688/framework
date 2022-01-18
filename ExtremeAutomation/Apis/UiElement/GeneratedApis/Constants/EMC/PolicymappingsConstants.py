"""
This class outlines all the constants for the policymappings API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PolicymappingsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PolicymappingsConstants(ApiConstants):
    def __init__(self):
        super(PolicymappingsConstants, self).__init__()
        self.POLICY_MAPPINGS_CLICK_SWITCH_TO_ADVANCED = {"constant": "policy_mappings_click_switch_to_advanced",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.policy_mappings_click_switch_to_advanced}
        self.POLICY_MAPPINGS_CLICK_SWITCH_TO_BASIC = {"constant": "policy_mappings_click_switch_to_basic",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.policy_mappings_click_switch_to_basic}
        self.POLICY_MAPPINGS_DIALOG_ADD_POLICY_MAPPING = {"constant": "policy_mappings_dialog_add_policy_mapping",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.policy_mappings_dialog_add_policy_mapping}
        self.POLICY_MAPPINGS_DIALOG_DELETE_POLICY_MAPPING = {"constant": "policy_mappings_dialog_delete_policy_mapping",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.policy_mappings_dialog_delete_policy_mapping}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_CLICK_SAVE = {"constant": "policy_mappings_dialog_edit_mapping_click_save",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.policy_mappings_dialog_edit_mapping_click_save}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_CUSTOM_FIELDS = {"constant": "policy_mappings_dialog_edit_mapping_set_custom_fields",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.policy_mappings_dialog_edit_mapping_set_custom_fields}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_FILTER = {"constant": "policy_mappings_dialog_edit_mapping_set_filter",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.policy_mappings_dialog_edit_mapping_set_filter}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_LOCATION = {"constant": "policy_mappings_dialog_edit_mapping_set_location",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.policy_mappings_dialog_edit_mapping_set_location}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_LOGIN_LAT_GROUP_AND_PORT = {"constant": "policy_mappings_dialog_edit_mapping_set_login_lat_group_and_port",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.policy_mappings_dialog_edit_mapping_set_login_lat_group_and_port}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_MANAGEMENT_ACCESS = {"constant": "policy_mappings_dialog_edit_mapping_set_management_access",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.policy_mappings_dialog_edit_mapping_set_management_access}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_NAME = {"constant": "policy_mappings_dialog_edit_mapping_set_name",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.policy_mappings_dialog_edit_mapping_set_name}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_POLICY_ROLE = {"constant": "policy_mappings_dialog_edit_mapping_set_policy_role",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.policy_mappings_dialog_edit_mapping_set_policy_role}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_PORT_PROFILE = {"constant": "policy_mappings_dialog_edit_mapping_set_port_profile",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.policy_mappings_dialog_edit_mapping_set_port_profile}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_RADIUS_ATTRIBUTE_LISTS = {"constant": "policy_mappings_dialog_edit_mapping_set_radius_attribute_lists",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.policy_mappings_dialog_edit_mapping_set_radius_attribute_lists}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_VIRTUAL_ROUTER = {"constant": "policy_mappings_dialog_edit_mapping_set_virtual_router",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.policy_mappings_dialog_edit_mapping_set_virtual_router}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_VLAN_EGRESS = {"constant": "policy_mappings_dialog_edit_mapping_set_vlan_egress",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.policy_mappings_dialog_edit_mapping_set_vlan_egress}
        self.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_VLAN_NAME = {"constant": "policy_mappings_dialog_edit_mapping_set_vlan_name",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.policy_mappings_dialog_edit_mapping_set_vlan_name}
        self.POLICY_MAPPINGS_NAVIGATE_TO_EDIT_POLICY_MAPPING = {"constant": "policy_mappings_navigate_to_edit_policy_mapping",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.policy_mappings_navigate_to_edit_policy_mapping}
        self.POLICY_MAPPINGS_SELECT_MAPPING = {"constant": "policy_mappings_select_mapping",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_mappings_select_mapping}
