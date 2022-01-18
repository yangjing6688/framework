"""
This class outlines all the constants for the guestusers API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GuestusersConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GuestusersConstants(ApiConstants):
    def __init__(self):
        super(GuestusersConstants, self).__init__()
        self.GU_ACCOUNT_ON_VAL_ADD_GU = {"constant": "gu_account_on_val_add_gu",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.gu_account_on_val_add_gu}
        self.GU_ADD = {"constant": "gu_add",
                       "tags": ["COMMAND_SELENIUM"],
                       "link": self.link.gu_add}
        self.GU_ADD_SUCCESS_MSG = {"constant": "gu_add_success_msg",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.gu_add_success_msg}
        self.GU_CLICK_NAV_BAR = {"constant": "gu_click_nav_bar",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.gu_click_nav_bar}
        self.GU_CREATE_GUEST_USER = {"constant": "gu_create_guest_user",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.gu_create_guest_user}
        self.GU_CREATE_GU_USERNAME_FIELD = {"constant": "gu_create_gu_username_field",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.gu_create_gu_username_field}
        self.GU_CREATE_GU_VALIDATE_ACC_VALIDITY = {"constant": "gu_create_gu_validate_acc_validity",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.gu_create_gu_validate_acc_validity}
        self.GU_CREATE_GU_VALIDATE_UN_PWD = {"constant": "gu_create_gu_validate_un_pwd",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.gu_create_gu_validate_un_pwd}
        self.GU_CREATE_GU_VALIDATE_UN_PWD_SPONSOR = {"constant": "gu_create_gu_validate_un_pwd_sponsor",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.gu_create_gu_validate_un_pwd_sponsor}
        self.GU_DELETE = {"constant": "gu_delete",
                          "tags": ["COMMAND_SELENIUM"],
                          "link": self.link.gu_delete}
        self.GU_DURATION_VAL_ADD_GU = {"constant": "gu_duration_val_add_gu",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.gu_duration_val_add_gu}
        self.GU_EDIT = {"constant": "gu_edit",
                        "tags": ["COMMAND_SELENIUM"],
                        "link": self.link.gu_edit}
        self.GU_EXPIRED_GU = {"constant": "gu_expired_gu",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.gu_expired_gu}
        self.GU_EXT_EXP = {"constant": "gu_ext_exp",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.gu_ext_exp}
        self.GU_GUEST_USER_SHOULD_EXIST = {"constant": "gu_guest_user_should_exist",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.gu_guest_user_should_exist}
        self.GU_LOAD = {"constant": "gu_load",
                        "tags": ["COMMAND_SELENIUM"],
                        "link": self.link.gu_load}
        self.GU_PRINT = {"constant": "gu_print",
                         "tags": ["COMMAND_SELENIUM"],
                         "link": self.link.gu_print}
        self.GU_RESEND_PWD = {"constant": "gu_resend_pwd",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.gu_resend_pwd}
        self.GU_SHOW_FILTERS = {"constant": "gu_show_filters",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.gu_show_filters}
        self.GU_TABLE_MEETING_ID = {"constant": "gu_table_meeting_id",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.gu_table_meeting_id}
        self.GU_TABLE_SMS = {"constant": "gu_table_sms",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.gu_table_sms}
        self.GU_TABLE_SPONSOR_EMAIL = {"constant": "gu_table_sponsor_email",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.gu_table_sponsor_email}
        self.GU_TABLE_SPONSOR_NAME = {"constant": "gu_table_sponsor_name",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.gu_table_sponsor_name}
        self.GU_TABLE_SPONSOR_RESPONSE = {"constant": "gu_table_sponsor_response",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.gu_table_sponsor_response}
        self.GU_TABLE_START_END_TIME = {"constant": "gu_table_start_end_time",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.gu_table_start_end_time}
        self.GU_USER_NAME_SHOULD_NOT_EXIST = {"constant": "gu_user_name_should_not_exist",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.gu_user_name_should_not_exist}
        self.GU_VALIDATION_USERNAME_FIELD = {"constant": "gu_validation_username_field",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.gu_validation_username_field}
