"""
This class outlines all the constants for the configurations API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ConfigurationsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ConfigurationsConstants(ApiConstants):
    def __init__(self):
        super(ConfigurationsConstants, self).__init__()
        self.CONFIGS_AAA_DEFAULT_CANCEL_AAA_DEFAULT = {"constant": "configs_aaa_default_cancel_aaa_default",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.configs_aaa_default_cancel_aaa_default}
        self.CONFIGS_AAA_DEFAULT_CHECK_AUTHENTICATE_FOR = {"constant": "configs_aaa_default_check_authenticate_for",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.configs_aaa_default_check_authenticate_for}
        self.CONFIGS_AAA_DEFAULT_SAVE_AAA_DEFAULT = {"constant": "configs_aaa_default_save_aaa_default",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.configs_aaa_default_save_aaa_default}
        self.CONFIGS_AAA_DEFAULT_SELECT_AUTH_METHODS = {"constant": "configs_aaa_default_select_auth_methods",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.configs_aaa_default_select_auth_methods}
        self.CONFIGS_AAA_DEFAULT_SELECT_BACKUP_RADIUS_SERVER = {"constant": "configs_aaa_default_select_backup_radius_server",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.configs_aaa_default_select_backup_radius_server}
        self.CONFIGS_AAA_DEFAULT_SELECT_LDAP_CONFIGURATION = {"constant": "configs_aaa_default_select_ldap_configuration",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.configs_aaa_default_select_ldap_configuration}
        self.CONFIGS_AAA_DEFAULT_SELECT_LOCAL_PASSWORD_REPOSITORY = {"constant": "configs_aaa_default_select_local_password_repository",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.configs_aaa_default_select_local_password_repository}
        self.CONFIGS_AAA_DEFAULT_SELECT_PRIMARY_RADIUS_SERVER = {"constant": "configs_aaa_default_select_primary_radius_server",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.configs_aaa_default_select_primary_radius_server}
        self.CONFIGS_ADD_ACCESS_CONTROL_CONFIGURATION = {"constant": "configs_add_access_control_configuration",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.configs_add_access_control_configuration}
        self.CONFIGS_CLICK_ADD_ACCESS_CONTROL_CONFIGURATION_BUTTON = {"constant": "configs_click_add_access_control_configuration_button",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.configs_click_add_access_control_configuration_button}
        self.CONFIGS_CLICK_DELETE_ACCESS_CONTROL_CONFIGURATION_BUTTON = {"constant": "configs_click_delete_access_control_configuration_button",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.configs_click_delete_access_control_configuration_button}
        self.CONFIGS_CLICK_EDIT_ACCESS_CONTROL_CONFIGURATION_BUTTON = {"constant": "configs_click_edit_access_control_configuration_button",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.configs_click_edit_access_control_configuration_button}
        self.CONFIGS_CLICK_SELECT_AAA_CONFIGURATION_BUTTON = {"constant": "configs_click_select_aaa_configuration_button",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.configs_click_select_aaa_configuration_button}
        self.CONFIGS_DELETE_ACCESS_CONTROL_CONFIGURATION = {"constant": "configs_delete_access_control_configuration",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.configs_delete_access_control_configuration}
        self.CONFIGS_RULES_CLICK_ADD_RULE_BUTTON = {"constant": "configs_rules_click_add_rule_button",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.configs_rules_click_add_rule_button}
        self.CONFIGS_RULES_CLICK_DELETE_RULE_BUTTON = {"constant": "configs_rules_click_delete_rule_button",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.configs_rules_click_delete_rule_button}
        self.CONFIGS_RULES_CLICK_EDIT_RULE_BUTTON = {"constant": "configs_rules_click_edit_rule_button",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.configs_rules_click_edit_rule_button}
        self.CONFIGS_RULES_CLICK_REFRESH_BUTTON = {"constant": "configs_rules_click_refresh_button",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.configs_rules_click_refresh_button}
        self.CONFIGS_RULES_DIALOG_ADD_RULE = {"constant": "configs_rules_dialog_add_rule",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.configs_rules_dialog_add_rule}
        self.CONFIGS_RULES_DIALOG_DELETE_RULE = {"constant": "configs_rules_dialog_delete_rule",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.configs_rules_dialog_delete_rule}
        self.CONFIGS_RULES_DIALOG_ENABLE_RULE = {"constant": "configs_rules_dialog_enable_rule",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.configs_rules_dialog_enable_rule}
        self.CONFIGS_RULES_SELECT_RULE = {"constant": "configs_rules_select_rule",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.configs_rules_select_rule}
        self.CONFIGS_SELECT_AAA_CONFIGURATION_DIALOG_SELECT_AAA_CONFIGURATION = {"constant": "configs_select_aaa_configuration_dialog_select_aaa_configuration",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.configs_select_aaa_configuration_dialog_select_aaa_configuration}
        self.CONFIGS_SELECT_ACCESS_CONTROL_CONFIGURATION = {"constant": "configs_select_access_control_configuration",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.configs_select_access_control_configuration}
