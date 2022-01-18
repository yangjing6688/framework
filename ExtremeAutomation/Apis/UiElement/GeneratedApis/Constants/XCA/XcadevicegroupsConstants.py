"""
This class outlines all the constants for the xcadevicegroups API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcadevicegroupsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcadevicegroupsConstants(ApiConstants):
    def __init__(self):
        super(XcadevicegroupsConstants, self).__init__()
        self.CLICK_ADD_TO_CREATE_NEW_GROUP = {"constant": "click_add_to_create_new_group",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.click_add_to_create_new_group}
        self.CLICK_DEVICE_GROUP_EDIT_PROFILE_BUTTON = {"constant": "click_device_group_edit_profile_button",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.click_device_group_edit_profile_button}
        self.CLONE_DEVICE_GROUP = {"constant": "clone_device_group",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.clone_device_group}
        self.CONFIG_DEVICE_GROUP_ADVANCED_SETTINGS = {"constant": "config_device_group_advanced_settings",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.config_device_group_advanced_settings}
        self.CONFIG_DEVICE_GROUP_DEVICES = {"constant": "config_device_group_devices",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.config_device_group_devices}
        self.CONFIG_DEVICE_GROUP_NAME_AND_COUNTRY = {"constant": "config_device_group_name_and_country",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.config_device_group_name_and_country}
        self.CONFIG_DEVICE_GROUP_NETWORKS = {"constant": "config_device_group_networks",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.config_device_group_networks}
        self.CONFIG_DEVICE_GROUP_ROLES = {"constant": "config_device_group_roles",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.config_device_group_roles}
        self.DELETE_EXISTING_DEVICE_GROUP = {"constant": "delete_existing_device_group",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.delete_existing_device_group}
        self.SAVE_CONFIG_AND_BACK_TO_GROUPS_PAGE = {"constant": "save_config_and_back_to_groups_page",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.save_config_and_back_to_groups_page}
        self.SELECT_DEVICE_GROUP = {"constant": "select_device_group",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.select_device_group}
        self.SELECT_DEVICE_GROUP_EDIT_CONFIG = {"constant": "select_device_group_edit_config",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.select_device_group_edit_config}
        self.VERIFY_DEVICE_GROUP_EXISTS = {"constant": "verify_device_group_exists",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.verify_device_group_exists}
