"""
This class outlines all the constants for the clicredentials API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ClicredentialsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ClicredentialsConstants(ApiConstants):
    def __init__(self):
        super(ClicredentialsConstants, self).__init__()
        self.CLICREDENTIALS_CONFIRM_CREDENTIAL_EXISTS = {"constant": "clicredentials_confirm_credential_exists",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.clicredentials_confirm_credential_exists}
        self.CLICREDENTIALS_DIALOG_ADD_CLICK_CANCEL = {"constant": "clicredentials_dialog_add_click_cancel",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.clicredentials_dialog_add_click_cancel}
        self.CLICREDENTIALS_DIALOG_ADD_CLICK_CONFIGURATION_PASSWORD_EYE = {"constant": "clicredentials_dialog_add_click_configuration_password_eye",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.clicredentials_dialog_add_click_configuration_password_eye}
        self.CLICREDENTIALS_DIALOG_ADD_CLICK_ENABLE_PASSWORD_EYE = {"constant": "clicredentials_dialog_add_click_enable_password_eye",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.clicredentials_dialog_add_click_enable_password_eye}
        self.CLICREDENTIALS_DIALOG_ADD_CLICK_LOGIN_PASSWORD_EYE = {"constant": "clicredentials_dialog_add_click_login_password_eye",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.clicredentials_dialog_add_click_login_password_eye}
        self.CLICREDENTIALS_DIALOG_ADD_CLICK_SAVE = {"constant": "clicredentials_dialog_add_click_save",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.clicredentials_dialog_add_click_save}
        self.CLICREDENTIALS_DIALOG_ADD_SET_CONFIGURATION_PASSWORD = {"constant": "clicredentials_dialog_add_set_configuration_password",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.clicredentials_dialog_add_set_configuration_password}
        self.CLICREDENTIALS_DIALOG_ADD_SET_DESCRIPTION = {"constant": "clicredentials_dialog_add_set_description",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.clicredentials_dialog_add_set_description}
        self.CLICREDENTIALS_DIALOG_ADD_SET_ENABLE_PASSWORD = {"constant": "clicredentials_dialog_add_set_enable_password",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.clicredentials_dialog_add_set_enable_password}
        self.CLICREDENTIALS_DIALOG_ADD_SET_LOGIN_PASSWORD = {"constant": "clicredentials_dialog_add_set_login_password",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.clicredentials_dialog_add_set_login_password}
        self.CLICREDENTIALS_DIALOG_ADD_SET_TYPE = {"constant": "clicredentials_dialog_add_set_type",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.clicredentials_dialog_add_set_type}
        self.CLICREDENTIALS_DIALOG_ADD_SET_USER_NAME = {"constant": "clicredentials_dialog_add_set_user_name",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.clicredentials_dialog_add_set_user_name}
        self.CLICREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "clicredentials_dialog_confirm_delete_click_no",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.clicredentials_dialog_confirm_delete_click_no}
        self.CLICREDENTIALS_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "clicredentials_dialog_confirm_delete_click_yes",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.clicredentials_dialog_confirm_delete_click_yes}
        self.CLICREDENTIALS_DIALOG_EDIT_CLICK_CANCEL = {"constant": "clicredentials_dialog_edit_click_cancel",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.clicredentials_dialog_edit_click_cancel}
        self.CLICREDENTIALS_DIALOG_EDIT_CLICK_CONFIGURATION_PASSWORD_EYE = {"constant": "clicredentials_dialog_edit_click_configuration_password_eye",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.clicredentials_dialog_edit_click_configuration_password_eye}
        self.CLICREDENTIALS_DIALOG_EDIT_CLICK_ENABLE_PASSWORD_EYE = {"constant": "clicredentials_dialog_edit_click_enable_password_eye",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.clicredentials_dialog_edit_click_enable_password_eye}
        self.CLICREDENTIALS_DIALOG_EDIT_CLICK_LOGIN_PASSWORD_EYE = {"constant": "clicredentials_dialog_edit_click_login_password_eye",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.clicredentials_dialog_edit_click_login_password_eye}
        self.CLICREDENTIALS_DIALOG_EDIT_CLICK_SAVE = {"constant": "clicredentials_dialog_edit_click_save",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.clicredentials_dialog_edit_click_save}
        self.CLICREDENTIALS_DIALOG_EDIT_SET_CONFIGURATION_PASSWORD = {"constant": "clicredentials_dialog_edit_set_configuration_password",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.clicredentials_dialog_edit_set_configuration_password}
        self.CLICREDENTIALS_DIALOG_EDIT_SET_DESCRIPTION = {"constant": "clicredentials_dialog_edit_set_description",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.clicredentials_dialog_edit_set_description}
        self.CLICREDENTIALS_DIALOG_EDIT_SET_ENABLE_PASSWORD = {"constant": "clicredentials_dialog_edit_set_enable_password",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.clicredentials_dialog_edit_set_enable_password}
        self.CLICREDENTIALS_DIALOG_EDIT_SET_LOGIN_PASSWORD = {"constant": "clicredentials_dialog_edit_set_login_password",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.clicredentials_dialog_edit_set_login_password}
        self.CLICREDENTIALS_DIALOG_EDIT_SET_TYPE = {"constant": "clicredentials_dialog_edit_set_type",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.clicredentials_dialog_edit_set_type}
        self.CLICREDENTIALS_DIALOG_EDIT_SET_USER_NAME = {"constant": "clicredentials_dialog_edit_set_user_name",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.clicredentials_dialog_edit_set_user_name}
        self.CLICREDENTIALS_REFRESH = {"constant": "clicredentials_refresh",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.clicredentials_refresh}
        self.CLICREDENTIALS_SELECT_CREDENTIAL = {"constant": "clicredentials_select_credential",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.clicredentials_select_credential}
        self.CLICREDENTIALS_TOOLBAR_CLICK_ADD = {"constant": "clicredentials_toolbar_click_add",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.clicredentials_toolbar_click_add}
        self.CLICREDENTIALS_TOOLBAR_CLICK_DELETE = {"constant": "clicredentials_toolbar_click_delete",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.clicredentials_toolbar_click_delete}
        self.CLICREDENTIALS_TOOLBAR_CLICK_EDIT = {"constant": "clicredentials_toolbar_click_edit",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.clicredentials_toolbar_click_edit}
