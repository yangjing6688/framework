"""
This class outlines all the constants for the xcanetworks API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcanetworksConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcanetworksConstants(ApiConstants):
    def __init__(self):
        super(XcanetworksConstants, self).__init__()
        self.ADD_NEW_DHCP_CONFIG = {"constant": "add_new_dhcp_config",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.add_new_dhcp_config}
        self.ADD_NEW_RADIUS_SERVER = {"constant": "add_new_radius_server",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.add_new_radius_server}
        self.CLICK_ADD_TO_CREATE_NEW_NETWORK = {"constant": "click_add_to_create_new_network",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.click_add_to_create_new_network}
        self.CLICK_NETWORK_NAME_TO_OPEN_NETWORK_SETTINGS = {"constant": "click_network_name_to_open_network_settings",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.click_network_name_to_open_network_settings}
        self.CONFIG_AUTH_METHOD_LOCAL_AND_DHCP = {"constant": "config_auth_method_local_and_dhcp",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.config_auth_method_local_and_dhcp}
        self.CONFIG_AUTH_METHOD_RADIUS = {"constant": "config_auth_method_radius",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.config_auth_method_radius}
        self.CONFIG_DEFAULT_AAA = {"constant": "config_default_aaa",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.config_default_aaa}
        self.CONFIG_MAC_BASED_AUTHENTICATION = {"constant": "config_mac_based_authentication",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.config_mac_based_authentication}
        self.CONFIG_NETWORK_ADVANCED_SETTINGS = {"constant": "config_network_advanced_settings",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.config_network_advanced_settings}
        self.CONFIG_NEW_RADIUS_SERVER_ADVANCED_SETTINGS = {"constant": "config_new_radius_server_advanced_settings",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.config_new_radius_server_advanced_settings}
        self.DELETE_NETWORK = {"constant": "delete_network",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.delete_network}
        self.EDIT_DHCP_SCHEMA_DEFINITION = {"constant": "edit_dhcp_schema_definition",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.edit_dhcp_schema_definition}
        self.EDIT_ECP_URL = {"constant": "edit_ecp_url",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.edit_ecp_url}
        self.EDIT_IDENTITY_AND_SHARED_SECRET = {"constant": "edit_identity_and_shared_secret",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.edit_identity_and_shared_secret}
        self.EDIT_NETWORK_AUTH_TYPE_PRIVACY_SETTINGS = {"constant": "edit_network_auth_type_privacy_settings",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.edit_network_auth_type_privacy_settings}
        self.EDIT_NETWORK_NAME_SSID_AND_STATUS = {"constant": "edit_network_name_ssid_and_status",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.edit_network_name_ssid_and_status}
        self.SAVE_NEW_DHCP_CONFIG = {"constant": "save_new_dhcp_config",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.save_new_dhcp_config}
        self.SAVE_NEW_RADIUS_SERVER = {"constant": "save_new_radius_server",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.save_new_radius_server}
        self.SAVE_SETTINGS_AND_BACK_TO_NETWORKS_PAGE = {"constant": "save_settings_and_back_to_networks_page",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.save_settings_and_back_to_networks_page}
        self.SELECT_AUTH_METHOD = {"constant": "select_auth_method",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.select_auth_method}
        self.SELECT_CAPTIVE_PORTAL_TYPE = {"constant": "select_captive_portal_type",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.select_captive_portal_type}
        self.SELECT_MBA_TIMEOUT_ROLE = {"constant": "select_mba_timeout_role",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.select_mba_timeout_role}
        self.SELECT_NETWORK_AUTH_TYPE = {"constant": "select_network_auth_type",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.select_network_auth_type}
        self.SELECT_NETWORK_DEFAULT_AUTH_ROLE_AND_VLAN = {"constant": "select_network_default_auth_role_and_vlan",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.select_network_default_auth_role_and_vlan}
        self.SELECT_NETWORK_DEFAULT_UNAUTH_ROLE = {"constant": "select_network_default_unauth_role",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.select_network_default_unauth_role}
        self.SELECT_SEND_SUCCESSFUL_LOGIN = {"constant": "select_send_successful_login",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.select_send_successful_login}
        self.SELECT_WHETHER_ENABLE_CAPTIVE_PORTAL = {"constant": "select_whether_enable_captive_portal",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.select_whether_enable_captive_portal}
        self.SELECT_WHETHER_USE_FQDN_FOR_CONNECTION = {"constant": "select_whether_use_fqdn_for_connection",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.select_whether_use_fqdn_for_connection}
        self.SELECT_WHETHER_USE_HTTPS_CONNECTION = {"constant": "select_whether_use_https_connection",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.select_whether_use_https_connection}
        self.TEST_NEW_DHCP_CONFIG = {"constant": "test_new_dhcp_config",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.test_new_dhcp_config}
        self.VERIFY_NETWORK_DOES_NOT_EXIST = {"constant": "verify_network_does_not_exist",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.verify_network_does_not_exist}
        self.VERIFY_NETWORK_EXISTS = {"constant": "verify_network_exists",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.verify_network_exists}
