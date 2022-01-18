"""
This class outlines all the constants for the snmpcredentials API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SnmpcredentialsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SnmpcredentialsConstants(ApiConstants):
    def __init__(self):
        super(SnmpcredentialsConstants, self).__init__()
        self.SNMPCREDENTIALS_CONFIRM_CREDENTIAL_EXISTS = {"constant": "snmpcredentials_confirm_credential_exists",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.snmpcredentials_confirm_credential_exists}
        self.SNMPCREDENTIALS_DIALOG_ADD_CLICK_AUTHENTICATION_PASSWORD_EYE = {"constant": "snmpcredentials_dialog_add_click_authentication_password_eye",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.snmpcredentials_dialog_add_click_authentication_password_eye}
        self.SNMPCREDENTIALS_DIALOG_ADD_CLICK_CANCEL = {"constant": "snmpcredentials_dialog_add_click_cancel",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.snmpcredentials_dialog_add_click_cancel}
        self.SNMPCREDENTIALS_DIALOG_ADD_CLICK_COMMUNITY_NAME_EYE = {"constant": "snmpcredentials_dialog_add_click_community_name_eye",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.snmpcredentials_dialog_add_click_community_name_eye}
        self.SNMPCREDENTIALS_DIALOG_ADD_CLICK_PRIVACY_PASSWORD_EYE = {"constant": "snmpcredentials_dialog_add_click_privacy_password_eye",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.snmpcredentials_dialog_add_click_privacy_password_eye}
        self.SNMPCREDENTIALS_DIALOG_ADD_CLICK_SAVE = {"constant": "snmpcredentials_dialog_add_click_save",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.snmpcredentials_dialog_add_click_save}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_AUTHENTICATION_PASSWORD = {"constant": "snmpcredentials_dialog_add_set_authentication_password",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.snmpcredentials_dialog_add_set_authentication_password}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_AUTHENTICATION_TYPE = {"constant": "snmpcredentials_dialog_add_set_authentication_type",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.snmpcredentials_dialog_add_set_authentication_type}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_COMMUNITY_NAME = {"constant": "snmpcredentials_dialog_add_set_community_name",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.snmpcredentials_dialog_add_set_community_name}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_CREDENTIAL_NAME = {"constant": "snmpcredentials_dialog_add_set_credential_name",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.snmpcredentials_dialog_add_set_credential_name}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_PRIVACY_PASSWORD = {"constant": "snmpcredentials_dialog_add_set_privacy_password",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.snmpcredentials_dialog_add_set_privacy_password}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_PRIVACY_TYPE = {"constant": "snmpcredentials_dialog_add_set_privacy_type",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.snmpcredentials_dialog_add_set_privacy_type}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_SNMP_VERSION = {"constant": "snmpcredentials_dialog_add_set_snmp_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.snmpcredentials_dialog_add_set_snmp_version}
        self.SNMPCREDENTIALS_DIALOG_ADD_SET_USER_NAME = {"constant": "snmpcredentials_dialog_add_set_user_name",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.snmpcredentials_dialog_add_set_user_name}
        self.SNMPCREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "snmpcredentials_dialog_confirm_delete_click_no",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.snmpcredentials_dialog_confirm_delete_click_no}
        self.SNMPCREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "snmpcredentials_dialog_confirm_delete_click_yes",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.snmpcredentials_dialog_confirm_delete_click_yes}
        self.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_AUTHENTICATION_PASSWORD_EYE = {"constant": "snmpcredentials_dialog_edit_click_authentication_password_eye",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.snmpcredentials_dialog_edit_click_authentication_password_eye}
        self.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_CANCEL = {"constant": "snmpcredentials_dialog_edit_click_cancel",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.snmpcredentials_dialog_edit_click_cancel}
        self.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_COMMUNITY_NAME_EYE = {"constant": "snmpcredentials_dialog_edit_click_community_name_eye",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.snmpcredentials_dialog_edit_click_community_name_eye}
        self.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_PRIVACY_PASSWORD_EYE = {"constant": "snmpcredentials_dialog_edit_click_privacy_password_eye",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.snmpcredentials_dialog_edit_click_privacy_password_eye}
        self.SNMPCREDENTIALS_DIALOG_EDIT_CLICK_SAVE = {"constant": "snmpcredentials_dialog_edit_click_save",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.snmpcredentials_dialog_edit_click_save}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_AUTHENTICATION_PASSWORD = {"constant": "snmpcredentials_dialog_edit_set_authentication_password",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.snmpcredentials_dialog_edit_set_authentication_password}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_AUTHENTICATION_TYPE = {"constant": "snmpcredentials_dialog_edit_set_authentication_type",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.snmpcredentials_dialog_edit_set_authentication_type}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_COMMUNITY_NAME = {"constant": "snmpcredentials_dialog_edit_set_community_name",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.snmpcredentials_dialog_edit_set_community_name}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_CREDENTIAL_NAME = {"constant": "snmpcredentials_dialog_edit_set_credential_name",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.snmpcredentials_dialog_edit_set_credential_name}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_PRIVACY_PASSWORD = {"constant": "snmpcredentials_dialog_edit_set_privacy_password",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.snmpcredentials_dialog_edit_set_privacy_password}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_PRIVACY_TYPE = {"constant": "snmpcredentials_dialog_edit_set_privacy_type",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.snmpcredentials_dialog_edit_set_privacy_type}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_SNMP_VERSION = {"constant": "snmpcredentials_dialog_edit_set_snmp_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.snmpcredentials_dialog_edit_set_snmp_version}
        self.SNMPCREDENTIALS_DIALOG_EDIT_SET_USER_NAME = {"constant": "snmpcredentials_dialog_edit_set_user_name",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.snmpcredentials_dialog_edit_set_user_name}
        self.SNMPCREDENTIALS_REFRESH = {"constant": "snmpcredentials_refresh",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.snmpcredentials_refresh}
        self.SNMPCREDENTIALS_SELECT_CREDENTIAL = {"constant": "snmpcredentials_select_credential",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.snmpcredentials_select_credential}
        self.SNMPCREDENTIALS_TOOLBAR_CLICK_ADD = {"constant": "snmpcredentials_toolbar_click_add",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.snmpcredentials_toolbar_click_add}
        self.SNMPCREDENTIALS_TOOLBAR_CLICK_DELETE = {"constant": "snmpcredentials_toolbar_click_delete",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.snmpcredentials_toolbar_click_delete}
        self.SNMPCREDENTIALS_TOOLBAR_CLICK_EDIT = {"constant": "snmpcredentials_toolbar_click_edit",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.snmpcredentials_toolbar_click_edit}
