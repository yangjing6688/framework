"""
This class outlines all the constants for the groups API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GroupsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GroupsConstants(ApiConstants):
    def __init__(self):
        super(GroupsConstants, self).__init__()
        self.GROUPS_CLICK_ADD_GROUP_BUTTON = {"constant": "groups_click_add_group_button",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.groups_click_add_group_button}
        self.GROUPS_CLICK_DELETE_GROUP_BUTTON = {"constant": "groups_click_delete_group_button",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.groups_click_delete_group_button}
        self.GROUPS_CLICK_EDIT_GROUP_BUTTON = {"constant": "groups_click_edit_group_button",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.groups_click_edit_group_button}
        self.GROUPS_CLICK_REFRESH_BUTTON = {"constant": "groups_click_refresh_button",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.groups_click_refresh_button}
        self.GROUPS_DELETE_GROUP = {"constant": "groups_delete_group",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.groups_delete_group}
        self.GROUPS_DIALOG_ADD_LDAP_USER_GROUP_ENTRY = {"constant": "groups_dialog_add_ldap_user_group_entry",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.groups_dialog_add_ldap_user_group_entry}
        self.GROUPS_DIALOG_ADD_LOCATION_GROUP_ENTRY = {"constant": "groups_dialog_add_location_group_entry",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.groups_dialog_add_location_group_entry}
        self.GROUPS_DIALOG_CLICK_CREATE_NEW_GROUP = {"constant": "groups_dialog_click_create_new_group",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.groups_dialog_click_create_new_group}
        self.GROUPS_DIALOG_SAVE_AND_CLOSE_GROUP = {"constant": "groups_dialog_save_and_close_group",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.groups_dialog_save_and_close_group}
        self.GROUPS_DIALOG_SAVE_GROUP_ENTRY = {"constant": "groups_dialog_save_group_entry",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.groups_dialog_save_group_entry}
        self.GROUPS_DIALOG_SELECT_GROUP_TYPE = {"constant": "groups_dialog_select_group_type",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.groups_dialog_select_group_type}
        self.GROUPS_DIALOG_SET_GROUP_NAME = {"constant": "groups_dialog_set_group_name",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.groups_dialog_set_group_name}
        self.GROUPS_SELECT_GROUP = {"constant": "groups_select_group",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.groups_select_group}
