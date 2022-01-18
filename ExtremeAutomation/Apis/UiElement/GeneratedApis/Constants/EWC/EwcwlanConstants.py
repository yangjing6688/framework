"""
This class outlines all the constants for the ewcwlan API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcwlanConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcwlanConstants(ApiConstants):
    def __init__(self):
        super(EwcwlanConstants, self).__init__()
        self.WLAN_CHECK_APPLICATION_VISIBILITY = {"constant": "wlan_check_application_visibility",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.wlan_check_application_visibility}
        self.WLAN_CHECK_AP_NAME_VSA = {"constant": "wlan_check_ap_name_vsa",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.wlan_check_ap_name_vsa}
        self.WLAN_CHECK_SSID_VSA = {"constant": "wlan_check_ssid_vsa",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.wlan_check_ssid_vsa}
        self.WLAN_CLICK_RADIUS_TLVS_BUTTON = {"constant": "wlan_click_radius_tlvs_button",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.wlan_click_radius_tlvs_button}
        self.WLAN_CREATE_WLAN = {"constant": "wlan_create_wlan",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.wlan_create_wlan}
        self.WLAN_DELETE_WLAN = {"constant": "wlan_delete_wlan",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.wlan_delete_wlan}
        self.WLAN_DISABLE_MAC_AUTHENTICATION = {"constant": "wlan_disable_mac_authentication",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.wlan_disable_mac_authentication}
        self.WLAN_DISABLE_RADIUS_ACCOUNTING = {"constant": "wlan_disable_radius_accounting",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.wlan_disable_radius_accounting}
        self.WLAN_DISABLE_WLAN = {"constant": "wlan_disable_wlan",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.wlan_disable_wlan}
        self.WLAN_EDIT_SSID = {"constant": "wlan_edit_ssid",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.wlan_edit_ssid}
        self.WLAN_EDIT_WEP_KEY_STRING = {"constant": "wlan_edit_wep_key_string",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.wlan_edit_wep_key_string}
        self.WLAN_EDIT_WLAN_NAME = {"constant": "wlan_edit_wlan_name",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.wlan_edit_wlan_name}
        self.WLAN_ENABLE_MAC_AUTHENTICATION = {"constant": "wlan_enable_mac_authentication",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.wlan_enable_mac_authentication}
        self.WLAN_ENABLE_RADIUS_ACCOUNTING = {"constant": "wlan_enable_radius_accounting",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.wlan_enable_radius_accounting}
        self.WLAN_ENABLE_WLAN = {"constant": "wlan_enable_wlan",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.wlan_enable_wlan}
        self.WLAN_RADIUS_MESSAGE_OPTIONS_POPUP_CLICK_OK = {"constant": "wlan_radius_message_options_popup_click_ok",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.wlan_radius_message_options_popup_click_ok}
        self.WLAN_SAVE_WLAN_SETTINGS = {"constant": "wlan_save_wlan_settings",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.wlan_save_wlan_settings}
        self.WLAN_SELECT_AUTHENTICATION_MODE = {"constant": "wlan_select_authentication_mode",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.wlan_select_authentication_mode}
        self.WLAN_SELECT_DEFAULT_COS = {"constant": "wlan_select_default_cos",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.wlan_select_default_cos}
        self.WLAN_SELECT_DEFAULT_TOPOLOGY = {"constant": "wlan_select_default_topology",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.wlan_select_default_topology}
        self.WLAN_SELECT_DEFAULT_TRAFFIC = {"constant": "wlan_select_default_traffic",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.wlan_select_default_traffic}
        self.WLAN_SELECT_PRIVACY_MODE = {"constant": "wlan_select_privacy_mode",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.wlan_select_privacy_mode}
        self.WLAN_SELECT_RADIUS_ACCOUNTING_SERVER = {"constant": "wlan_select_radius_accounting_server",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.wlan_select_radius_accounting_server}
        self.WLAN_SELECT_RADIUS_SERVER = {"constant": "wlan_select_radius_server",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.wlan_select_radius_server}
        self.WLAN_SELECT_SUB_TAB = {"constant": "wlan_select_sub_tab",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.wlan_select_sub_tab}
        self.WLAN_SELECT_WEP_KEY_INPUT_METHOD = {"constant": "wlan_select_wep_key_input_method",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.wlan_select_wep_key_input_method}
        self.WLAN_UNCHECK_APPLICATION_VISIBILITY = {"constant": "wlan_uncheck_application_visibility",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.wlan_uncheck_application_visibility}
        self.WLAN_UNCHECK_SSID_VSA = {"constant": "wlan_uncheck_ssid_vsa",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.wlan_uncheck_ssid_vsa}
