"""
This class outlines all the constants for the captiveportals API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CaptiveportalsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CaptiveportalsConstants(ApiConstants):
    def __init__(self):
        super(CaptiveportalsConstants, self).__init__()
        self.CAPTIVE_PORTALS_ADMIN_ADD_NEW_USER_FOR_LOGIN_CONFIG = {"constant": "captive_portals_admin_add_new_user_for_login_config",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.captive_portals_admin_add_new_user_for_login_config}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_ADD_BUTTON_SAVE_LOGIN_CONFIG = {"constant": "captive_portals_admin_click_add_button_save_login_config",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.captive_portals_admin_click_add_button_save_login_config}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_ADD_LOGIN_CONFIG_BUTTON = {"constant": "captive_portals_admin_click_add_login_config_button",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.captive_portals_admin_click_add_login_config_button}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_DELETE_LOGIN_CONFIG_BUTTON = {"constant": "captive_portals_admin_click_delete_login_config_button",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.captive_portals_admin_click_delete_login_config_button}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_EDIT_LOGIN_CONFIG_BUTTON = {"constant": "captive_portals_admin_click_edit_login_config_button",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.captive_portals_admin_click_edit_login_config_button}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_OK_BUTTON_ON_EDIT_USER_WINDOW = {"constant": "captive_portals_admin_click_ok_button_on_edit_user_window",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.captive_portals_admin_click_ok_button_on_edit_user_window}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_SAVE_BUTTON_ON_ADMINISTRATION_PAGE = {"constant": "captive_portals_admin_click_save_button_on_administration_page",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.captive_portals_admin_click_save_button_on_administration_page}
        self.CAPTIVE_PORTALS_ADMIN_CLICK_SAVE_BUTTON_SAVE_LOGIN_CONFIG = {"constant": "captive_portals_admin_click_save_button_save_login_config",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.captive_portals_admin_click_save_button_save_login_config}
        self.CAPTIVE_PORTALS_ADMIN_DELETE_LOGIN_CONFIG = {"constant": "captive_portals_admin_delete_login_config",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.captive_portals_admin_delete_login_config}
        self.CAPTIVE_PORTALS_ADMIN_FILL_MANDATORY_USER_INFO_ON_EDIT_USER_WINDOW = {"constant": "captive_portals_admin_fill_mandatory_user_info_on_edit_user_window",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.captive_portals_admin_fill_mandatory_user_info_on_edit_user_window}
        self.CAPTIVE_PORTALS_ADMIN_FILL_OPTIONAL_USER_INFO_ON_EDIT_USER_WINDOW = {"constant": "captive_portals_admin_fill_optional_user_info_on_edit_user_window",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.captive_portals_admin_fill_optional_user_info_on_edit_user_window}
        self.CAPTIVE_PORTALS_ADMIN_SELECT_AUTHENTICATION_FOR_LOGIN_CONFIG = {"constant": "captive_portals_admin_select_authentication_for_login_config",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.captive_portals_admin_select_authentication_for_login_config}
        self.CAPTIVE_PORTALS_ADMIN_SELECT_LOGIN_CONFIG = {"constant": "captive_portals_admin_select_login_config",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.captive_portals_admin_select_login_config}
        self.CAPTIVE_PORTALS_ADMIN_SELECT_ROLE_FOR_LOGIN_CONFIG = {"constant": "captive_portals_admin_select_role_for_login_config",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.captive_portals_admin_select_role_for_login_config}
        self.CAPTIVE_PORTALS_ADMIN_SELECT_USER_FOR_LOGIN_CONFIG = {"constant": "captive_portals_admin_select_user_for_login_config",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.captive_portals_admin_select_user_for_login_config}
        self.CAPTIVE_PORTALS_ADMIN_VERIFY_EXISTENCE_OF_LOGIN_CONFIG = {"constant": "captive_portals_admin_verify_existence_of_login_config",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.captive_portals_admin_verify_existence_of_login_config}
