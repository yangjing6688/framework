"""
This class outlines all the constants for the xcaaaa API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcaaaaConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcaaaaConstants(ApiConstants):
    def __init__(self):
        super(XcaaaaConstants, self).__init__()
        self.ADD_LDAP_CONNECTION_URL = {"constant": "add_ldap_connection_url",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.add_ldap_connection_url}
        self.CHECK_AUTHENTICATE_LOCALLY_FOR_MAC = {"constant": "check_authenticate_locally_for_mac",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.check_authenticate_locally_for_mac}
        self.CLICK_ADD_TO_CREATE_A_NEW_LDAP_CONFIGURATION = {"constant": "click_add_to_create_a_new_ldap_configuration",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.click_add_to_create_a_new_ldap_configuration}
        self.CLICK_ADD_TO_CREATE_A_NEW_LOCAL_PASSWORD_REPOSITORY_USER = {"constant": "click_add_to_create_a_new_local_password_repository_user",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.click_add_to_create_a_new_local_password_repository_user}
        self.CLICK_ADD_TO_CREATE_A_NEW_RADIUS_SERVER = {"constant": "click_add_to_create_a_new_radius_server",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.click_add_to_create_a_new_radius_server}
        self.CLICK_CONFIGURE_DEFAULT_AAA_CONFIGURATION = {"constant": "click_configure_default_aaa_configuration",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.click_configure_default_aaa_configuration}
        self.CLICK_LDAP_CONFIGURATIONS_TAB = {"constant": "click_ldap_configurations_tab",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.click_ldap_configurations_tab}
        self.CLICK_LDAP_CONFIGURATION_TO_OPEN_SETTINGS = {"constant": "click_ldap_configuration_to_open_settings",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.click_ldap_configuration_to_open_settings}
        self.CLICK_LOCAL_PASSWORD_REPOSITORY_TAB = {"constant": "click_local_password_repository_tab",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.click_local_password_repository_tab}
        self.CLICK_LOCAL_PASSWORD_REPOSITORY_USER_TO_OPEN_SETTINGS = {"constant": "click_local_password_repository_user_to_open_settings",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.click_local_password_repository_user_to_open_settings}
        self.CLICK_MANAGE_CERTIFICATES = {"constant": "click_manage_certificates",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.click_manage_certificates}
        self.CLICK_RADIUS_SERVERS_TAB = {"constant": "click_radius_servers_tab",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.click_radius_servers_tab}
        self.CLICK_RADIUS_SERVER_TO_OPEN_SETTINGS = {"constant": "click_radius_server_to_open_settings",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.click_radius_server_to_open_settings}
        self.DELETE_LDAP_CONFIGURATION = {"constant": "delete_ldap_configuration",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.delete_ldap_configuration}
        self.DELETE_LOCAL_PASSWORD_REPOSITORY_USER = {"constant": "delete_local_password_repository_user",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.delete_local_password_repository_user}
        self.DELETE_RADIUS_SERVER = {"constant": "delete_radius_server",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.delete_radius_server}
        self.EDIT_LDAP_CONFIGURATION_SETTINGS = {"constant": "edit_ldap_configuration_settings",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.edit_ldap_configuration_settings}
        self.EDIT_LDAP_CONNECTION_URL = {"constant": "edit_ldap_connection_url",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.edit_ldap_connection_url}
        self.EDIT_LDAP_SCHEMA_DEFINITION_AND_CLOSE = {"constant": "edit_ldap_schema_definition_and_close",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.edit_ldap_schema_definition_and_close}
        self.EDIT_LOCAL_PASSWORD_REPOSITORY_USER_SETTINGS = {"constant": "edit_local_password_repository_user_settings",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.edit_local_password_repository_user_settings}
        self.EDIT_RADIUS_SERVER_ADVANCED_SETTINGS_AND_CLOSE = {"constant": "edit_radius_server_advanced_settings_and_close",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.edit_radius_server_advanced_settings_and_close}
        self.EDIT_RADIUS_SERVER_SETTINGS = {"constant": "edit_radius_server_settings",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.edit_radius_server_settings}
        self.SAVE_CONFIG_AND_BACK_TO_AAA_PAGE = {"constant": "save_config_and_back_to_aaa_page",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.save_config_and_back_to_aaa_page}
        self.SELECT_AAA_AUTHENTICATION_METHOD = {"constant": "select_aaa_authentication_method",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.select_aaa_authentication_method}
        self.SELECT_AAA_LDAP_CONFIGURATION = {"constant": "select_aaa_ldap_configuration",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.select_aaa_ldap_configuration}
        self.SELECT_AAA_PRIMARY_AND_BACKUP_RADIUS = {"constant": "select_aaa_primary_and_backup_radius",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.select_aaa_primary_and_backup_radius}
