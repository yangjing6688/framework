"""
This class outlines all the constants for the users API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(UsersConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class UsersConstants(ApiConstants):
    def __init__(self):
        super(UsersConstants, self).__init__()
        self.USERS_CLICK_ADD_GROUP = {"constant": "users_click_add_group",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.users_click_add_group}
        self.USERS_CLICK_ADD_USER = {"constant": "users_click_add_user",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.users_click_add_user}
        self.USERS_CLICK_COPY_GROUP = {"constant": "users_click_copy_group",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.users_click_copy_group}
        self.USERS_CLICK_DELETE_GROUP = {"constant": "users_click_delete_group",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.users_click_delete_group}
        self.USERS_CLICK_DELETE_USER = {"constant": "users_click_delete_user",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.users_click_delete_user}
        self.USERS_CLICK_EDIT_GROUP = {"constant": "users_click_edit_group",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.users_click_edit_group}
        self.USERS_CLICK_EDIT_USER = {"constant": "users_click_edit_user",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.users_click_edit_user}
        self.USERS_CONFIRM_GROUP_EXISTS = {"constant": "users_confirm_group_exists",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.users_confirm_group_exists}
        self.USERS_CONFIRM_USER_EXISTS = {"constant": "users_confirm_user_exists",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.users_confirm_user_exists}
        self.USERS_CONFIRM_USER_LOGGED_IN = {"constant": "users_confirm_user_logged_in",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.users_confirm_user_logged_in}
        self.USERS_DIALOG_ADD_GROUP_CLICK_CANCEL = {"constant": "users_dialog_add_group_click_cancel",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.users_dialog_add_group_click_cancel}
        self.USERS_DIALOG_ADD_GROUP_CLICK_SAVE = {"constant": "users_dialog_add_group_click_save",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.users_dialog_add_group_click_save}
        self.USERS_DIALOG_ADD_GROUP_COLLAPSE_CAPABILITY = {"constant": "users_dialog_add_group_collapse_capability",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.users_dialog_add_group_collapse_capability}
        self.USERS_DIALOG_ADD_GROUP_DISABLE_CAPABILITY = {"constant": "users_dialog_add_group_disable_capability",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.users_dialog_add_group_disable_capability}
        self.USERS_DIALOG_ADD_GROUP_ENABLE_CAPABILITY = {"constant": "users_dialog_add_group_enable_capability",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.users_dialog_add_group_enable_capability}
        self.USERS_DIALOG_ADD_GROUP_EXPAND_CAPABILITY = {"constant": "users_dialog_add_group_expand_capability",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.users_dialog_add_group_expand_capability}
        self.USERS_DIALOG_ADD_GROUP_SET_MEMBERSHIP_CRITERIA = {"constant": "users_dialog_add_group_set_membership_criteria",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.users_dialog_add_group_set_membership_criteria}
        self.USERS_DIALOG_ADD_GROUP_SET_NAME = {"constant": "users_dialog_add_group_set_name",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.users_dialog_add_group_set_name}
        self.USERS_DIALOG_ADD_GROUP_SET_SNMP_REDIRECT = {"constant": "users_dialog_add_group_set_snmp_redirect",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.users_dialog_add_group_set_snmp_redirect}
        self.USERS_DIALOG_ADD_USER_CLICK_CANCEL = {"constant": "users_dialog_add_user_click_cancel",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.users_dialog_add_user_click_cancel}
        self.USERS_DIALOG_ADD_USER_CLICK_SAVE = {"constant": "users_dialog_add_user_click_save",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.users_dialog_add_user_click_save}
        self.USERS_DIALOG_ADD_USER_SET_DOMAIN = {"constant": "users_dialog_add_user_set_domain",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.users_dialog_add_user_set_domain}
        self.USERS_DIALOG_ADD_USER_SET_GROUP = {"constant": "users_dialog_add_user_set_group",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.users_dialog_add_user_set_group}
        self.USERS_DIALOG_ADD_USER_SET_NAME = {"constant": "users_dialog_add_user_set_name",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.users_dialog_add_user_set_name}
        self.USERS_DIALOG_CONFIRM_DELETE_GROUP_CLICK_NO = {"constant": "users_dialog_confirm_delete_group_click_no",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.users_dialog_confirm_delete_group_click_no}
        self.USERS_DIALOG_CONFIRM_DELETE_GROUP_CLICK_YES = {"constant": "users_dialog_confirm_delete_group_click_yes",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.users_dialog_confirm_delete_group_click_yes}
        self.USERS_DIALOG_CONFIRM_DELETE_USER_CLICK_NO = {"constant": "users_dialog_confirm_delete_user_click_no",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.users_dialog_confirm_delete_user_click_no}
        self.USERS_DIALOG_CONFIRM_DELETE_USER_CLICK_YES = {"constant": "users_dialog_confirm_delete_user_click_yes",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.users_dialog_confirm_delete_user_click_yes}
        self.USERS_DIALOG_COPY_GROUP_CLICK_CANCEL = {"constant": "users_dialog_copy_group_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.users_dialog_copy_group_click_cancel}
        self.USERS_DIALOG_COPY_GROUP_CLICK_SAVE = {"constant": "users_dialog_copy_group_click_save",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.users_dialog_copy_group_click_save}
        self.USERS_DIALOG_COPY_GROUP_SET_NAME = {"constant": "users_dialog_copy_group_set_name",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.users_dialog_copy_group_set_name}
        self.USERS_DIALOG_EDIT_GROUP_CLICK_CANCEL = {"constant": "users_dialog_edit_group_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.users_dialog_edit_group_click_cancel}
        self.USERS_DIALOG_EDIT_GROUP_CLICK_SAVE = {"constant": "users_dialog_edit_group_click_save",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.users_dialog_edit_group_click_save}
        self.USERS_DIALOG_EDIT_GROUP_COLLAPSE_CAPABILITY = {"constant": "users_dialog_edit_group_collapse_capability",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.users_dialog_edit_group_collapse_capability}
        self.USERS_DIALOG_EDIT_GROUP_DISABLE_CAPABILITY = {"constant": "users_dialog_edit_group_disable_capability",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.users_dialog_edit_group_disable_capability}
        self.USERS_DIALOG_EDIT_GROUP_ENABLE_CAPABILITY = {"constant": "users_dialog_edit_group_enable_capability",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.users_dialog_edit_group_enable_capability}
        self.USERS_DIALOG_EDIT_GROUP_EXPAND_CAPABILITY = {"constant": "users_dialog_edit_group_expand_capability",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.users_dialog_edit_group_expand_capability}
        self.USERS_DIALOG_EDIT_GROUP_SET_MEMBERSHIP_CRITERIA = {"constant": "users_dialog_edit_group_set_membership_criteria",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.users_dialog_edit_group_set_membership_criteria}
        self.USERS_DIALOG_EDIT_GROUP_SET_SNMP_REDIRECT = {"constant": "users_dialog_edit_group_set_snmp_redirect",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.users_dialog_edit_group_set_snmp_redirect}
        self.USERS_DIALOG_EDIT_USER_CLICK_CANCEL = {"constant": "users_dialog_edit_user_click_cancel",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.users_dialog_edit_user_click_cancel}
        self.USERS_DIALOG_EDIT_USER_CLICK_SAVE = {"constant": "users_dialog_edit_user_click_save",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.users_dialog_edit_user_click_save}
        self.USERS_DIALOG_EDIT_USER_SET_DOMAIN = {"constant": "users_dialog_edit_user_set_domain",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.users_dialog_edit_user_set_domain}
        self.USERS_DIALOG_EDIT_USER_SET_GROUP = {"constant": "users_dialog_edit_user_set_group",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.users_dialog_edit_user_set_group}
        self.USERS_HANDLE_LOCK = {"constant": "users_handle_lock",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.users_handle_lock}
        self.USERS_SELECT_GROUP = {"constant": "users_select_group",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.users_select_group}
        self.USERS_SELECT_USER = {"constant": "users_select_user",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.users_select_user}
        self.USERS_WAIT_FOR_GROUP_ADD = {"constant": "users_wait_for_group_add",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.users_wait_for_group_add}
        self.USERS_WAIT_FOR_GROUP_REMOVE = {"constant": "users_wait_for_group_remove",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.users_wait_for_group_remove}
        self.USERS_WAIT_FOR_USER_ADD = {"constant": "users_wait_for_user_add",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.users_wait_for_user_add}
        self.USERS_WAIT_FOR_USER_REMOVE = {"constant": "users_wait_for_user_remove",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.users_wait_for_user_remove}
