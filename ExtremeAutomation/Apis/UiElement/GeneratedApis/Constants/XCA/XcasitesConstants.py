"""
This class outlines all the constants for the xcasites API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcasitesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcasitesConstants(ApiConstants):
    def __init__(self):
        super(XcasitesConstants, self).__init__()
        self.CLICK_NAME_TO_OPEN_DEVICE_GROUP_EDIT_WINDOW = {"constant": "click_name_to_open_device_group_edit_window",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.click_name_to_open_device_group_edit_window}
        self.CLICK_SITE_OPEN_DETAIL_PAGE = {"constant": "click_site_open_detail_page",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.click_site_open_detail_page}
        self.CLOSE_DEVICE_GROUP_EDIT_WINDOW = {"constant": "close_device_group_edit_window",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.close_device_group_edit_window}
        self.CONFIG_RADIOS_FOR_DEVICE_GROUP_PROFILE = {"constant": "config_radios_for_device_group_profile",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.config_radios_for_device_group_profile}
        self.DESELECT_ROLES_FOR_DEVICE_GROUP_PROFILE = {"constant": "deselect_roles_for_device_group_profile",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.deselect_roles_for_device_group_profile}
        self.OPEN_DEVICE_GROUP_PROFILE_EDIT_WINDOW = {"constant": "open_device_group_profile_edit_window",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.open_device_group_profile_edit_window}
        self.OPEN_SITE_DEVICE_GROUPS_PAGE = {"constant": "open_site_device_groups_page",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.open_site_device_groups_page}
        self.OPEN_SITE_FLOOR_PLANS_PAGE = {"constant": "open_site_floor_plans_page",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.open_site_floor_plans_page}
        self.OPEN_SITE_LOCATION_PAGE = {"constant": "open_site_location_page",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.open_site_location_page}
        self.OPEN_SITE_SNMP_PAGE = {"constant": "open_site_snmp_page",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.open_site_snmp_page}
        self.OPEN_SITE_SWITCHES_PAGE = {"constant": "open_site_switches_page",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.open_site_switches_page}
        self.SAVE_DEVICE_GROUP_PROFILE_CONFIG = {"constant": "save_device_group_profile_config",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.save_device_group_profile_config}
        self.SAVE_SITE_CONFIG_AND_BACK_TO_SITE_PAGE = {"constant": "save_site_config_and_back_to_site_page",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.save_site_config_and_back_to_site_page}
        self.SELECT_ROLES_FOR_DEVICE_GROUP_PROFILE = {"constant": "select_roles_for_device_group_profile",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.select_roles_for_device_group_profile}
        self.SELECT_SITE_AND_CONFIG = {"constant": "select_site_and_config",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.select_site_and_config}
