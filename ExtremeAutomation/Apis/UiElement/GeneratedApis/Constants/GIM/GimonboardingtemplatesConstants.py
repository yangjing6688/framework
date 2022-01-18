"""
This class outlines all the constants for the gimonboardingtemplates API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimonboardingtemplatesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimonboardingtemplatesConstants(ApiConstants):
    def __init__(self):
        super(GimonboardingtemplatesConstants, self).__init__()
        self.OT_ACCESSIBLE_TO_PROV_DE = {"constant": "ot_accessible_to_prov_de",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.ot_accessible_to_prov_de}
        self.OT_ACCESSIBLE_TO_PROV_GU = {"constant": "ot_accessible_to_prov_gu",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.ot_accessible_to_prov_gu}
        self.OT_ACCESS_GROUPS = {"constant": "ot_access_groups",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.ot_access_groups}
        self.OT_ADD = {"constant": "ot_add",
                       "tags": ["COMMAND_SELENIUM"],
                       "link": self.link.ot_add}
        self.OT_ADD_LDAP_GROUP = {"constant": "ot_add_ldap_group",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.ot_add_ldap_group}
        self.OT_ADD_SPONSOR = {"constant": "ot_add_sponsor",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.ot_add_sponsor}
        self.OT_CANCEL = {"constant": "ot_cancel",
                          "tags": ["COMMAND_SELENIUM"],
                          "link": self.link.ot_cancel}
        self.OT_CLICK_NAV_BAR = {"constant": "ot_click_nav_bar",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.ot_click_nav_bar}
        self.OT_COMMON_TAB = {"constant": "ot_common_tab",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.ot_common_tab}
        self.OT_DEFAULT_VALIDATION = {"constant": "ot_default_validation",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.ot_default_validation}
        self.OT_DELETE_ERROR_TEXT = {"constant": "ot_delete_error_text",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.ot_delete_error_text}
        self.OT_EDIT_COMMON = {"constant": "ot_edit_common",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.ot_edit_common}
        self.OT_EDIT_DEVICES = {"constant": "ot_edit_devices",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.ot_edit_devices}
        self.OT_EDIT_GUEST_USERS = {"constant": "ot_edit_guest_users",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.ot_edit_guest_users}
        self.OT_EXPECTED_EXIST_TABLE = {"constant": "ot_expected_exist_table",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.ot_expected_exist_table}
        self.OT_GUEST_USERS = {"constant": "ot_guest_users",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.ot_guest_users}
        self.OT_GU_ACC_PRV_GEN_ACC_ACT = {"constant": "ot_gu_acc_prv_gen_acc_act",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.ot_gu_acc_prv_gen_acc_act}
        self.OT_GU_ACC_PRV_GEN_ACC_EXP = {"constant": "ot_gu_acc_prv_gen_acc_exp",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.ot_gu_acc_prv_gen_acc_exp}
        self.OT_GU_EDIT_USERNAME_FIELD = {"constant": "ot_gu_edit_username_field",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.ot_gu_edit_username_field}
        self.OT_GU_FINITIAL_LASTNAME = {"constant": "ot_gu_finitial_lastname",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.ot_gu_finitial_lastname}
        self.OT_GU_FIRST_LASTNAME = {"constant": "ot_gu_first_lastname",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.ot_gu_first_lastname}
        self.OT_GU_NOTIFICATION = {"constant": "ot_gu_notification",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.ot_gu_notification}
        self.OT_GU_PASSWORD = {"constant": "ot_gu_password",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.ot_gu_password}
        self.OT_GU_PWD_COMPLEXITY_CONFIG = {"constant": "ot_gu_pwd_complexity_config",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.ot_gu_pwd_complexity_config}
        self.OT_GU_RANDOM_UN = {"constant": "ot_gu_random_un",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.ot_gu_random_un}
        self.OT_GU_USERNAME = {"constant": "ot_gu_username",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.ot_gu_username}
        self.OT_MULTIPLE_ROW_SELECTION = {"constant": "ot_multiple_row_selection",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.ot_multiple_row_selection}
        self.OT_NOTIFICATION = {"constant": "ot_notification",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.ot_notification}
        self.OT_RESEND_DETAILS = {"constant": "ot_resend_details",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.ot_resend_details}
        self.OT_SAVE = {"constant": "ot_save",
                        "tags": ["COMMAND_SELENIUM"],
                        "link": self.link.ot_save}
        self.OT_SELECT_OTNAME_ROW_TABLE = {"constant": "ot_select_otname_row_table",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.ot_select_otname_row_table}
        self.OT_SELECT_OT_COPY = {"constant": "ot_select_ot_copy",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.ot_select_ot_copy}
        self.OT_SELECT_OT_DELETE = {"constant": "ot_select_ot_delete",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.ot_select_ot_delete}
        self.OT_SELECT_OT_EDIT = {"constant": "ot_select_ot_edit",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.ot_select_ot_edit}
        self.OT_SHOULD_EXIST = {"constant": "ot_should_exist",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.ot_should_exist}
        self.OT_SHOULD_NOT_EXIST = {"constant": "ot_should_not_exist",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.ot_should_not_exist}
        self.OT_SIGNED_IN_USER_SHOULD_EXIST = {"constant": "ot_signed_in_user_should_exist",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.ot_signed_in_user_should_exist}
        self.OT_SIGNED_USER_FOOTER = {"constant": "ot_signed_user_footer",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.ot_signed_user_footer}
        self.OT_SPONSOR_AUTO_APPROVE_DENY = {"constant": "ot_sponsor_auto_approve_deny",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.ot_sponsor_auto_approve_deny}
        self.OT_SUMMARY_ADVANCED = {"constant": "ot_summary_advanced",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.ot_summary_advanced}
        self.OT_SUMMARY_COMMON = {"constant": "ot_summary_common",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.ot_summary_common}
        self.OT_SUMMARY_DEVICE_FAMILY = {"constant": "ot_summary_device_family",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.ot_summary_device_family}
        self.OT_SUMMARY_GUEST_USERS = {"constant": "ot_summary_guest_users",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.ot_summary_guest_users}
        self.OT_SUMMARY_IOT_USER_DEVICES = {"constant": "ot_summary_iot_user_devices",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.ot_summary_iot_user_devices}
        self.OT_SUMMARY_MOBILE_APP = {"constant": "ot_summary_mobile_app",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.ot_summary_mobile_app}
        self.OT_SUMMARY_NOTIFICATION = {"constant": "ot_summary_notification",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.ot_summary_notification}
        self.OT_SUMMARY_SPONSOR = {"constant": "ot_summary_sponsor",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.ot_summary_sponsor}
        self.OT_TABLE_SHOULD_EMPTY = {"constant": "ot_table_should_empty",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.ot_table_should_empty}
        self.OT_TEMP_ACC_VALIDITY = {"constant": "ot_temp_acc_validity",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.ot_temp_acc_validity}
        self.OT_VALIDATION_ADVANCED_TAB = {"constant": "ot_validation_advanced_tab",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.ot_validation_advanced_tab}
        self.OT_VERIFY_ADMIN_SIGNED = {"constant": "ot_verify_admin_signed",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.ot_verify_admin_signed}
