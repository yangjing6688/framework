"""
This class outlines all the constants for the xcaportal API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcaportalConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcaportalConstants(ApiConstants):
    def __init__(self):
        super(XcaportalConstants, self).__init__()
        self.CLICK_ADD_TO_CREATE_NEW_PORTAL = {"constant": "click_add_to_create_new_portal",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.click_add_to_create_new_portal}
        self.CLICK_ADMINISTRATION_TAB = {"constant": "click_administration_tab",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.click_administration_tab}
        self.CLICK_NETWORK_SETTINGS_TAB = {"constant": "click_network_settings_tab",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.click_network_settings_tab}
        self.CLICK_PORTAL_CONFIGURATIONS_TAB = {"constant": "click_portal_configurations_tab",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.click_portal_configurations_tab}
        self.CLICK_PORTAL_NAME_TO_OPEN_PORTAL_SETTINGS = {"constant": "click_portal_name_to_open_portal_settings",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.click_portal_name_to_open_portal_settings}
        self.CONFIG_PORTAL_NETWORK_SETTINGS = {"constant": "config_portal_network_settings",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.config_portal_network_settings}
        self.DELETE_EXISTING_PORTAL = {"constant": "delete_existing_portal",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.delete_existing_portal}
        self.SAVE_PORTAL_CONFIG_AND_BACK_TO_PORTAL_PAGE = {"constant": "save_portal_config_and_back_to_portal_page",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.save_portal_config_and_back_to_portal_page}
        self.SELECT_AUTHENTICATED_PORTAL = {"constant": "select_authenticated_portal",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.select_authenticated_portal}
        self.SELECT_GUEST_PORTAL = {"constant": "select_guest_portal",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.select_guest_portal}
        self.SET_PORTAL_NAME = {"constant": "set_portal_name",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.set_portal_name}
        self.VERIFY_PORTAL_DOES_NOT_EXIST = {"constant": "verify_portal_does_not_exist",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.verify_portal_does_not_exist}
        self.VERIFY_PORTAL_EXISTS = {"constant": "verify_portal_exists",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.verify_portal_exists}
