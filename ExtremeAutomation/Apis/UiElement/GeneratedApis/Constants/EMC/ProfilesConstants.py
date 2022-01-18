"""
This class outlines all the constants for the profiles API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ProfilesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ProfilesConstants(ApiConstants):
    def __init__(self):
        super(ProfilesConstants, self).__init__()
        self.PROFILES_CONFIRM_PROFILE_EXISTS = {"constant": "profiles_confirm_profile_exists",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.profiles_confirm_profile_exists}
        self.PROFILES_DIALOG_ADD_PROFILE_CLICK_CANCEL = {"constant": "profiles_dialog_add_profile_click_cancel",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.profiles_dialog_add_profile_click_cancel}
        self.PROFILES_DIALOG_ADD_PROFILE_CLICK_SAVE = {"constant": "profiles_dialog_add_profile_click_save",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.profiles_dialog_add_profile_click_save}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_CLI_CREDENTIAL = {"constant": "profiles_dialog_add_profile_set_cli_credential",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.profiles_dialog_add_profile_set_cli_credential}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_MAX_ACCESS = {"constant": "profiles_dialog_add_profile_set_max_access",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.profiles_dialog_add_profile_set_max_access}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_MAX_SECURITY = {"constant": "profiles_dialog_add_profile_set_max_security",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.profiles_dialog_add_profile_set_max_security}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_PROFILE_NAME = {"constant": "profiles_dialog_add_profile_set_profile_name",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.profiles_dialog_add_profile_set_profile_name}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_READ = {"constant": "profiles_dialog_add_profile_set_read",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.profiles_dialog_add_profile_set_read}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_READ_SECURITY = {"constant": "profiles_dialog_add_profile_set_read_security",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.profiles_dialog_add_profile_set_read_security}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_SNMP_VERSION = {"constant": "profiles_dialog_add_profile_set_snmp_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.profiles_dialog_add_profile_set_snmp_version}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_WRITE = {"constant": "profiles_dialog_add_profile_set_write",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.profiles_dialog_add_profile_set_write}
        self.PROFILES_DIALOG_ADD_PROFILE_SET_WRITE_SECURITY = {"constant": "profiles_dialog_add_profile_set_write_security",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.profiles_dialog_add_profile_set_write_security}
        self.PROFILES_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "profiles_dialog_confirm_delete_click_no",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.profiles_dialog_confirm_delete_click_no}
        self.PROFILES_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "profiles_dialog_confirm_delete_click_yes",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.profiles_dialog_confirm_delete_click_yes}
        self.PROFILES_DIALOG_EDIT_PROFILE_CLICK_CANCEL = {"constant": "profiles_dialog_edit_profile_click_cancel",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.profiles_dialog_edit_profile_click_cancel}
        self.PROFILES_DIALOG_EDIT_PROFILE_CLICK_SAVE = {"constant": "profiles_dialog_edit_profile_click_save",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.profiles_dialog_edit_profile_click_save}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_CLI_CREDENTIAL = {"constant": "profiles_dialog_edit_profile_set_cli_credential",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.profiles_dialog_edit_profile_set_cli_credential}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_MAX_ACCESS = {"constant": "profiles_dialog_edit_profile_set_max_access",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.profiles_dialog_edit_profile_set_max_access}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_MAX_SECURITY = {"constant": "profiles_dialog_edit_profile_set_max_security",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.profiles_dialog_edit_profile_set_max_security}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_READ = {"constant": "profiles_dialog_edit_profile_set_read",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.profiles_dialog_edit_profile_set_read}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_READ_SECURITY = {"constant": "profiles_dialog_edit_profile_set_read_security",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.profiles_dialog_edit_profile_set_read_security}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_WRITE = {"constant": "profiles_dialog_edit_profile_set_write",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.profiles_dialog_edit_profile_set_write}
        self.PROFILES_DIALOG_EDIT_PROFILE_SET_WRITE_SECURITY = {"constant": "profiles_dialog_edit_profile_set_write_security",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.profiles_dialog_edit_profile_set_write_security}
        self.PROFILES_REFRESH = {"constant": "profiles_refresh",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.profiles_refresh}
        self.PROFILES_SELECT_PROFILE = {"constant": "profiles_select_profile",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.profiles_select_profile}
        self.PROFILES_SELECT_SUB_TAB = {"constant": "profiles_select_sub_tab",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.profiles_select_sub_tab}
        self.PROFILES_SET_DEFAULT_ACCESS_CONTROL_ENGINE_PROFILE = {"constant": "profiles_set_default_access_control_engine_profile",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.profiles_set_default_access_control_engine_profile}
        self.PROFILES_SET_DEFAULT_PROFILE = {"constant": "profiles_set_default_profile",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.profiles_set_default_profile}
        self.PROFILES_TOOLBAR_CLICK_ADD = {"constant": "profiles_toolbar_click_add",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.profiles_toolbar_click_add}
        self.PROFILES_TOOLBAR_CLICK_DELETE = {"constant": "profiles_toolbar_click_delete",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.profiles_toolbar_click_delete}
        self.PROFILES_TOOLBAR_CLICK_EDIT = {"constant": "profiles_toolbar_click_edit",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.profiles_toolbar_click_edit}
