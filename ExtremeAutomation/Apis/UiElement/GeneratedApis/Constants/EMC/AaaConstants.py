"""
This class outlines all the constants for the aaa API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AaaConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AaaConstants(ApiConstants):
    def __init__(self):
        super(AaaConstants, self).__init__()
        self.AAA_ADD_AAA_CONFIGURATION = {"constant": "aaa_add_aaa_configuration",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.aaa_add_aaa_configuration}
        self.AAA_ADVANCED_AUTHENTICATION_RULE_OPEN_EDIT_DIALOG = {"constant": "aaa_advanced_authentication_rule_open_edit_dialog",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.aaa_advanced_authentication_rule_open_edit_dialog}
        self.AAA_ADVANCED_CLICK_ADD_AUTHENTICATION_RULE = {"constant": "aaa_advanced_click_add_authentication_rule",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.aaa_advanced_click_add_authentication_rule}
        self.AAA_ADVANCED_CLICK_DELETE_AUTHENTICATION_RULE = {"constant": "aaa_advanced_click_delete_authentication_rule",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.aaa_advanced_click_delete_authentication_rule}
        self.AAA_ADVANCED_CLICK_EDIT_AUTHENTICATION_RULE = {"constant": "aaa_advanced_click_edit_authentication_rule",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.aaa_advanced_click_edit_authentication_rule}
        self.AAA_ADVANCED_DELETE_AUTHENTICATION_RULE = {"constant": "aaa_advanced_delete_authentication_rule",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.aaa_advanced_delete_authentication_rule}
        self.AAA_ADVANCED_RULE_DIALOG_CHECK_PASSWORD_FOR_ALL_AUTHENTICATIONS = {"constant": "aaa_advanced_rule_dialog_check_password_for_all_authentications",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.aaa_advanced_rule_dialog_check_password_for_all_authentications}
        self.AAA_ADVANCED_RULE_DIALOG_CLICK_USER_MAC_HOST_PATTERN_OR_GROUP_BUTTON = {"constant": "aaa_advanced_rule_dialog_click_user_mac_host_pattern_or_group_button",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.aaa_advanced_rule_dialog_click_user_mac_host_pattern_or_group_button}
        self.AAA_ADVANCED_RULE_DIALOG_SAVE_CONFIGURATION = {"constant": "aaa_advanced_rule_dialog_save_configuration",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.aaa_advanced_rule_dialog_save_configuration}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_AUTHENTICATION_METHOD = {"constant": "aaa_advanced_rule_dialog_select_authentication_method",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.aaa_advanced_rule_dialog_select_authentication_method}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_AUTHENTICATION_TYPE = {"constant": "aaa_advanced_rule_dialog_select_authentication_type",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.aaa_advanced_rule_dialog_select_authentication_type}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_BACKUP_RADIUS_SERVER = {"constant": "aaa_advanced_rule_dialog_select_backup_radius_server",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.aaa_advanced_rule_dialog_select_backup_radius_server}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_INJECT_ACCOUNTING_ATTRIBUTES = {"constant": "aaa_advanced_rule_dialog_select_inject_accounting_attributes",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.aaa_advanced_rule_dialog_select_inject_accounting_attributes}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_INJECT_AUTHENTICATION_ATTRIBUTES = {"constant": "aaa_advanced_rule_dialog_select_inject_authentication_attributes",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.aaa_advanced_rule_dialog_select_inject_authentication_attributes}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_LDAP_CONFIGURATION = {"constant": "aaa_advanced_rule_dialog_select_ldap_configuration",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.aaa_advanced_rule_dialog_select_ldap_configuration}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_LDAP_POLICY_MAPPING = {"constant": "aaa_advanced_rule_dialog_select_ldap_policy_mapping",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.aaa_advanced_rule_dialog_select_ldap_policy_mapping}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_LOCATION = {"constant": "aaa_advanced_rule_dialog_select_location",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.aaa_advanced_rule_dialog_select_location}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_PRIMARY_RADIUS_SERVER = {"constant": "aaa_advanced_rule_dialog_select_primary_radius_server",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.aaa_advanced_rule_dialog_select_primary_radius_server}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_QUATERNARY_RADIUS_SERVER = {"constant": "aaa_advanced_rule_dialog_select_quaternary_radius_server",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.aaa_advanced_rule_dialog_select_quaternary_radius_server}
        self.AAA_ADVANCED_RULE_DIALOG_SELECT_TERTIARY_RADIUS_SERVER = {"constant": "aaa_advanced_rule_dialog_select_tertiary_radius_server",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.aaa_advanced_rule_dialog_select_tertiary_radius_server}
        self.AAA_ADVANCED_RULE_DIALOG_SET_LDAP_AUTHENTICATION_TYPE = {"constant": "aaa_advanced_rule_dialog_set_ldap_authentication_type",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.aaa_advanced_rule_dialog_set_ldap_authentication_type}
        self.AAA_ADVANCED_RULE_DIALOG_SET_PASSWORD = {"constant": "aaa_advanced_rule_dialog_set_password",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.aaa_advanced_rule_dialog_set_password}
        self.AAA_ADVANCED_RULE_DIALOG_SET_PATTERN_OR_GROUP = {"constant": "aaa_advanced_rule_dialog_set_pattern_or_group",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.aaa_advanced_rule_dialog_set_pattern_or_group}
        self.AAA_ADVANCED_RULE_DIALOG_SET_SUPPORTED_RADIUS_TYPE = {"constant": "aaa_advanced_rule_dialog_set_supported_radius_type",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.aaa_advanced_rule_dialog_set_supported_radius_type}
        self.AAA_ADVANCED_SELECT_AUTHENTICATION_RULE = {"constant": "aaa_advanced_select_authentication_rule",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.aaa_advanced_select_authentication_rule}
        self.AAA_CLICK_ADD_AAA_CONFIGURATION_BUTTON = {"constant": "aaa_click_add_aaa_configuration_button",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.aaa_click_add_aaa_configuration_button}
        self.AAA_CLICK_DELETE_AAA_CONFIGURATION_BUTTON = {"constant": "aaa_click_delete_aaa_configuration_button",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.aaa_click_delete_aaa_configuration_button}
        self.AAA_CLICK_EDIT_AAA_CONFIGURATION_BUTTON = {"constant": "aaa_click_edit_aaa_configuration_button",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.aaa_click_edit_aaa_configuration_button}
        self.AAA_CONFIRM_LDAP_CONFIGURATION_EXISTS = {"constant": "aaa_confirm_ldap_configuration_exists",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.aaa_confirm_ldap_configuration_exists}
        self.AAA_CONFIRM_RADIUS_SERVER_EXISTS = {"constant": "aaa_confirm_radius_server_exists",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.aaa_confirm_radius_server_exists}
        self.AAA_DEFAULT_CANCEL_DEFAULT_AAA_SETTINGS = {"constant": "aaa_default_cancel_default_aaa_settings",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.aaa_default_cancel_default_aaa_settings}
        self.AAA_DEFAULT_CHECK_AUTH_REQUEST_FOR = {"constant": "aaa_default_check_auth_request_for",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.aaa_default_check_auth_request_for}
        self.AAA_DEFAULT_SAVE_DEFAULT_AAA_SETTINGS = {"constant": "aaa_default_save_default_aaa_settings",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.aaa_default_save_default_aaa_settings}
        self.AAA_DEFAULT_SELECT_AUTH_METHODS = {"constant": "aaa_default_select_auth_methods",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.aaa_default_select_auth_methods}
        self.AAA_DEFAULT_SELECT_BACKUP_RADIUS_SERVER = {"constant": "aaa_default_select_backup_radius_server",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.aaa_default_select_backup_radius_server}
        self.AAA_DEFAULT_SELECT_LDAP_CONFIGURATION = {"constant": "aaa_default_select_ldap_configuration",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.aaa_default_select_ldap_configuration}
        self.AAA_DEFAULT_SELECT_LOCAL_PASSWORD_REPOSITORY = {"constant": "aaa_default_select_local_password_repository",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.aaa_default_select_local_password_repository}
        self.AAA_DEFAULT_SELECT_PRIMARY_RADIUS_SERVER = {"constant": "aaa_default_select_primary_radius_server",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.aaa_default_select_primary_radius_server}
        self.AAA_DELETE_AAA_CONFIGURATION = {"constant": "aaa_delete_aaa_configuration",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.aaa_delete_aaa_configuration}
        self.AAA_DIALOG_ADD_LDAP_CONFIGURATION = {"constant": "aaa_dialog_add_ldap_configuration",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.aaa_dialog_add_ldap_configuration}
        self.AAA_DIALOG_DELETE_LDAP_CONFIGURATION = {"constant": "aaa_dialog_delete_ldap_configuration",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.aaa_dialog_delete_ldap_configuration}
        self.AAA_DIALOG_SELECT_LDAP_CONFIGURATION = {"constant": "aaa_dialog_select_ldap_configuration",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.aaa_dialog_select_ldap_configuration}
        self.AAA_DIALOG_TEST_LDAP_CONFIGURATION = {"constant": "aaa_dialog_test_ldap_configuration",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.aaa_dialog_test_ldap_configuration}
        self.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_CANCEL_ADVANCED_SETTING = {"constant": "aaa_radius_advanced_config_dialog_cancel_advanced_setting",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.aaa_radius_advanced_config_dialog_cancel_advanced_setting}
        self.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_HEALTH_CHECK_OTHER_SETTINGS = {"constant": "aaa_radius_advanced_config_dialog_health_check_other_settings",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.aaa_radius_advanced_config_dialog_health_check_other_settings}
        self.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_HEALTH_CHECK_USE_ACCESS_REQUEST = {"constant": "aaa_radius_advanced_config_dialog_health_check_use_access_request",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.aaa_radius_advanced_config_dialog_health_check_use_access_request}
        self.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_SAVE_ADVANCED_SETTING = {"constant": "aaa_radius_advanced_config_dialog_save_advanced_setting",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.aaa_radius_advanced_config_dialog_save_advanced_setting}
        self.AAA_RADIUS_ADVANCED_CONFIG_DIALOG_USERNAME_SETTING = {"constant": "aaa_radius_advanced_config_dialog_username_setting",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.aaa_radius_advanced_config_dialog_username_setting}
        self.AAA_RADIUS_SERVER_CLICK_ADD_RADIUS_SERVER_BUTTON = {"constant": "aaa_radius_server_click_add_radius_server_button",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.aaa_radius_server_click_add_radius_server_button}
        self.AAA_RADIUS_SERVER_CLICK_DELETE_RADIUS_SERVER_BUTTON = {"constant": "aaa_radius_server_click_delete_radius_server_button",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.aaa_radius_server_click_delete_radius_server_button}
        self.AAA_RADIUS_SERVER_CLICK_EDIT_RADIUS_SERVER_BUTTON = {"constant": "aaa_radius_server_click_edit_radius_server_button",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.aaa_radius_server_click_edit_radius_server_button}
        self.AAA_RADIUS_SERVER_DELETE_RADIUS_SERVER = {"constant": "aaa_radius_server_delete_radius_server",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.aaa_radius_server_delete_radius_server}
        self.AAA_RADIUS_SERVER_DIALOG_CANCEL_CONFIGURATION = {"constant": "aaa_radius_server_dialog_cancel_configuration",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.aaa_radius_server_dialog_cancel_configuration}
        self.AAA_RADIUS_SERVER_DIALOG_CHANGE_SERVER_SHARED_SECRET = {"constant": "aaa_radius_server_dialog_change_server_shared_secret",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.aaa_radius_server_dialog_change_server_shared_secret}
        self.AAA_RADIUS_SERVER_DIALOG_OPEN_ADVANCED_CONFIG = {"constant": "aaa_radius_server_dialog_open_advanced_config",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.aaa_radius_server_dialog_open_advanced_config}
        self.AAA_RADIUS_SERVER_DIALOG_SAVE_CONFIGURATION = {"constant": "aaa_radius_server_dialog_save_configuration",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.aaa_radius_server_dialog_save_configuration}
        self.AAA_RADIUS_SERVER_DIALOG_SET_AUTHENTICATION_VIA_EMC = {"constant": "aaa_radius_server_dialog_set_authentication_via_emc",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.aaa_radius_server_dialog_set_authentication_via_emc}
        self.AAA_RADIUS_SERVER_DIALOG_SET_CONFIGURATION = {"constant": "aaa_radius_server_dialog_set_configuration",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.aaa_radius_server_dialog_set_configuration}
        self.AAA_RADIUS_SERVER_DIALOG_SET_IP_AND_RESPONSE_WINDOW = {"constant": "aaa_radius_server_dialog_set_ip_and_response_window",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.aaa_radius_server_dialog_set_ip_and_response_window}
        self.AAA_SELECT_AAA_CONFIGURATION = {"constant": "aaa_select_aaa_configuration",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.aaa_select_aaa_configuration}
