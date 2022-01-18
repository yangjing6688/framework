"""
This class outlines all the constants for the alarmconfig API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AlarmconfigConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AlarmconfigConstants(ApiConstants):
    def __init__(self):
        super(AlarmconfigConstants, self).__init__()
        self.ALARMCONFIG_CLEAR_TABLE_FILTER = {"constant": "alarmconfig_clear_table_filter",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.alarmconfig_clear_table_filter}
        self.ALARMCONFIG_CLICK_ADD = {"constant": "alarmconfig_click_add",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.alarmconfig_click_add}
        self.ALARMCONFIG_CLICK_COPY = {"constant": "alarmconfig_click_copy",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.alarmconfig_click_copy}
        self.ALARMCONFIG_CLICK_DELETE = {"constant": "alarmconfig_click_delete",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.alarmconfig_click_delete}
        self.ALARMCONFIG_CLICK_EDIT = {"constant": "alarmconfig_click_edit",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.alarmconfig_click_edit}
        self.ALARMCONFIG_CLICK_FIRST_PAGE = {"constant": "alarmconfig_click_first_page",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.alarmconfig_click_first_page}
        self.ALARMCONFIG_CLICK_LAST_PAGE = {"constant": "alarmconfig_click_last_page",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.alarmconfig_click_last_page}
        self.ALARMCONFIG_CLICK_NEXT_PAGE = {"constant": "alarmconfig_click_next_page",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.alarmconfig_click_next_page}
        self.ALARMCONFIG_CLICK_PREV_PAGE = {"constant": "alarmconfig_click_prev_page",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.alarmconfig_click_prev_page}
        self.ALARMCONFIG_CLICK_REFRESH = {"constant": "alarmconfig_click_refresh",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.alarmconfig_click_refresh}
        self.ALARMCONFIG_CLICK_RESET = {"constant": "alarmconfig_click_reset",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.alarmconfig_click_reset}
        self.ALARMCONFIG_CONFIRM_ALARM_DEFINITION_EXISTS = {"constant": "alarmconfig_confirm_alarm_definition_exists",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.alarmconfig_confirm_alarm_definition_exists}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CLICK_ADD = {"constant": "alarmconfig_dialog_add_actions_click_add",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.alarmconfig_dialog_add_actions_click_add}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CLICK_EDIT = {"constant": "alarmconfig_dialog_add_actions_click_edit",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.alarmconfig_dialog_add_actions_click_edit}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CLICK_REMOVE = {"constant": "alarmconfig_dialog_add_actions_click_remove",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.alarmconfig_dialog_add_actions_click_remove}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CLICK_TEST = {"constant": "alarmconfig_dialog_add_actions_click_test",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.alarmconfig_dialog_add_actions_click_test}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CUSTOM_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_actions_custom_click_cancel",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_add_actions_custom_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CUSTOM_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_actions_custom_click_save",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_actions_custom_click_save}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CUSTOM_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_add_actions_custom_select_override_content",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_add_actions_custom_select_override_content}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CUSTOM_SET_CUSTOM_ARGUMENTS = {"constant": "alarmconfig_dialog_add_actions_custom_set_custom_arguments",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_actions_custom_set_custom_arguments}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CUSTOM_SET_PROGRAM = {"constant": "alarmconfig_dialog_add_actions_custom_set_program",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_add_actions_custom_set_program}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_CUSTOM_SET_WORKING_DIRECTORY = {"constant": "alarmconfig_dialog_add_actions_custom_set_working_directory",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_add_actions_custom_set_working_directory}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_actions_email_click_cancel",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_add_actions_email_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_CLICK_EDIT_EMAIL_LISTS = {"constant": "alarmconfig_dialog_add_actions_email_click_edit_email_lists",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_add_actions_email_click_edit_email_lists}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_actions_email_click_save",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.alarmconfig_dialog_add_actions_email_click_save}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_CLICK_ADD = {"constant": "alarmconfig_dialog_add_actions_email_editlist_click_add",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_actions_email_editlist_click_add}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_actions_email_editlist_click_cancel",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_actions_email_editlist_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_CLICK_CLOSE = {"constant": "alarmconfig_dialog_add_actions_email_editlist_click_close",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_add_actions_email_editlist_click_close}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_CLICK_EDIT = {"constant": "alarmconfig_dialog_add_actions_email_editlist_click_edit",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_actions_email_editlist_click_edit}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_CLICK_REMOVE = {"constant": "alarmconfig_dialog_add_actions_email_editlist_click_remove",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_actions_email_editlist_click_remove}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_actions_email_editlist_click_save",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_actions_email_editlist_click_save}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_SELECT_ROW = {"constant": "alarmconfig_dialog_add_actions_email_editlist_select_row",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_actions_email_editlist_select_row}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_SET_ADDRESSES = {"constant": "alarmconfig_dialog_add_actions_email_editlist_set_addresses",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_add_actions_email_editlist_set_addresses}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_EDITLIST_SET_LIST_NAME = {"constant": "alarmconfig_dialog_add_actions_email_editlist_set_list_name",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_add_actions_email_editlist_set_list_name}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_add_actions_email_select_override_content",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_actions_email_select_override_content}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_SET_BODY = {"constant": "alarmconfig_dialog_add_actions_email_set_body",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.alarmconfig_dialog_add_actions_email_set_body}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_SET_DESTINATION = {"constant": "alarmconfig_dialog_add_actions_email_set_destination",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.alarmconfig_dialog_add_actions_email_set_destination}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_EMAIL_SET_SUBJECT = {"constant": "alarmconfig_dialog_add_actions_email_set_subject",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_actions_email_set_subject}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SELECT_ENABLE_ALARM_ACTION_LIMIT = {"constant": "alarmconfig_dialog_add_actions_select_enable_alarm_action_limit",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.alarmconfig_dialog_add_actions_select_enable_alarm_action_limit}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SET_MAX_COUNT = {"constant": "alarmconfig_dialog_add_actions_set_max_count",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.alarmconfig_dialog_add_actions_set_max_count}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SET_RESET_INTERVAL = {"constant": "alarmconfig_dialog_add_actions_set_reset_interval",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_add_actions_set_reset_interval}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_actions_syslog_click_cancel",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_add_actions_syslog_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_actions_syslog_click_save",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_actions_syslog_click_save}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_add_actions_syslog_select_override_content",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_add_actions_syslog_select_override_content}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SET_MESSAGE = {"constant": "alarmconfig_dialog_add_actions_syslog_set_message",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_add_actions_syslog_set_message}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SET_SYSLOG_SERVER = {"constant": "alarmconfig_dialog_add_actions_syslog_set_syslog_server",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_actions_syslog_set_syslog_server}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_SYSLOG_SET_TAG = {"constant": "alarmconfig_dialog_add_actions_syslog_set_tag",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.alarmconfig_dialog_add_actions_syslog_set_tag}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_actions_trap_click_cancel",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_actions_trap_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_actions_trap_click_save",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.alarmconfig_dialog_add_actions_trap_click_save}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_add_actions_trap_select_override_content",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_add_actions_trap_select_override_content}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_SNMP_CREDENTIAL = {"constant": "alarmconfig_dialog_add_actions_trap_set_snmp_credential",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_actions_trap_set_snmp_credential}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_MESSAGE = {"constant": "alarmconfig_dialog_add_actions_trap_set_trap_message",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.alarmconfig_dialog_add_actions_trap_set_trap_message}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_MESSAGE_OID = {"constant": "alarmconfig_dialog_add_actions_trap_set_trap_message_oid",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_actions_trap_set_trap_message_oid}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_OID = {"constant": "alarmconfig_dialog_add_actions_trap_set_trap_oid",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_actions_trap_set_trap_oid}
        self.ALARMCONFIG_DIALOG_ADD_ACTIONS_TRAP_SET_TRAP_SERVER = {"constant": "alarmconfig_dialog_add_actions_trap_set_trap_server",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_add_actions_trap_set_trap_server}
        self.ALARMCONFIG_DIALOG_ADD_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_click_cancel",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.alarmconfig_dialog_add_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_click_save",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.alarmconfig_dialog_add_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CATEGORY_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_category_click_cancel",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_criteria_custom_category_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CATEGORY_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_category_click_save",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_custom_category_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CATEGORY_SELECT_CATEGORIES = {"constant": "alarmconfig_dialog_add_criteria_custom_category_select_categories",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_category_select_categories}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CATEGORY_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_category_select_exclude_selected",
                                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                                        "link": self.link.alarmconfig_dialog_add_criteria_custom_category_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CATEGORY_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_category_select_match_selected",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_category_select_match_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CLICK_ADD = {"constant": "alarmconfig_dialog_add_criteria_custom_click_add",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_criteria_custom_click_add}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CLICK_EDIT = {"constant": "alarmconfig_dialog_add_criteria_custom_click_edit",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_click_edit}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_CLICK_REMOVE = {"constant": "alarmconfig_dialog_add_criteria_custom_click_remove",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_add_criteria_custom_click_remove}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_EVENT_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_event_click_cancel",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_add_criteria_custom_event_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_EVENT_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_event_click_save",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_criteria_custom_event_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_EVENT_SELECT_EVENTS = {"constant": "alarmconfig_dialog_add_criteria_custom_event_select_events",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_custom_event_select_events}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_EVENT_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_event_select_exclude_selected",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.alarmconfig_dialog_add_criteria_custom_event_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_EVENT_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_event_select_match_selected",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_add_criteria_custom_event_select_match_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_click_cancel",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_CLICK_EDIT_LIST = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_click_edit_list",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_click_edit_list}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_click_save",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_ADD = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_add",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_add}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_cancel",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_REMOVE = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_remove",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_remove}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_save",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SELECT_HOST_NAME = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_host_name",
                                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                                        "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_host_name}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SELECT_IP_MASK = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_ip_mask",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_ip_mask}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SELECT_ROW = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_row",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_select_row}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SET_HOST_NAME = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_host_name",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_host_name}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SET_IP_ADDRESS = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_ip_address",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_ip_address}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SET_MASK = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_mask",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_editlist_set_mask}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_select_exclude_selected",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_SELECT_HOSTIPS = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_select_hostips",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_select_hostips}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_HOSTIP_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_hostip_select_match_selected",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_add_criteria_custom_hostip_select_match_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_information_click_cancel",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.alarmconfig_dialog_add_criteria_custom_information_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_CLICK_EDIT_LIST = {"constant": "alarmconfig_dialog_add_criteria_custom_information_click_edit_list",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_add_criteria_custom_information_click_edit_list}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_information_click_save",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_add_criteria_custom_information_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_ADD = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_click_add",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_click_add}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_click_cancel",
                                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                                         "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_REMOVE = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_click_remove",
                                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                                         "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_click_remove}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_click_save",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SELECT_CONTAINS = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_select_contains",
                                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                                            "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_select_contains}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SELECT_DOES_NOT_CONTAIN = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_select_does_not_contain",
                                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                                    "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_select_does_not_contain}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SELECT_ROW = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_select_row",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_select_row}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SET_PHRASE = {"constant": "alarmconfig_dialog_add_criteria_custom_information_editlist_set_phrase",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_add_criteria_custom_information_editlist_set_phrase}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_SELECT_MATCH_ALL_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_information_select_match_all_selected",
                                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                                             "link": self.link.alarmconfig_dialog_add_criteria_custom_information_select_match_all_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_SELECT_MATCH_ANY_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_information_select_match_any_selected",
                                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                                             "link": self.link.alarmconfig_dialog_add_criteria_custom_information_select_match_any_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_INFORMATION_SELECT_PHRASES = {"constant": "alarmconfig_dialog_add_criteria_custom_information_select_phrases",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_information_select_phrases}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_LOG_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_log_click_cancel",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_criteria_custom_log_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_LOG_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_log_click_save",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_log_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_LOG_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_log_select_exclude_selected",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_add_criteria_custom_log_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_LOG_SELECT_LOGS = {"constant": "alarmconfig_dialog_add_criteria_custom_log_select_logs",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_add_criteria_custom_log_select_logs}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_LOG_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_log_select_match_selected",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.alarmconfig_dialog_add_criteria_custom_log_select_match_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_SELECT_ROW = {"constant": "alarmconfig_dialog_add_criteria_custom_select_row",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_select_row}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_SEVERITY_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_severity_click_cancel",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_criteria_custom_severity_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_SEVERITY_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_severity_click_save",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_custom_severity_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_SEVERITY_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_severity_select_exclude_selected",
                                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                                        "link": self.link.alarmconfig_dialog_add_criteria_custom_severity_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_SEVERITY_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_severity_select_match_selected",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_add_criteria_custom_severity_select_match_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_SEVERITY_SELECT_SEVERITIES = {"constant": "alarmconfig_dialog_add_criteria_custom_severity_select_severities",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_severity_select_severities}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_TYPE_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_custom_type_click_cancel",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_criteria_custom_type_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_TYPE_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_custom_type_click_save",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_add_criteria_custom_type_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_TYPE_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_type_select_exclude_selected",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_add_criteria_custom_type_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_TYPE_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_custom_type_select_match_selected",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_custom_type_select_match_selected}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_CUSTOM_TYPE_SELECT_TYPES = {"constant": "alarmconfig_dialog_add_criteria_custom_type_select_types",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_criteria_custom_type_select_types}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_ALARM_INTERVAL = {"constant": "alarmconfig_dialog_add_criteria_flow_set_alarm_interval",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_criteria_flow_set_alarm_interval}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_ALARM_SOURCE = {"constant": "alarmconfig_dialog_add_criteria_flow_set_alarm_source",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.alarmconfig_dialog_add_criteria_flow_set_alarm_source}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_FROM_NETWORK = {"constant": "alarmconfig_dialog_add_criteria_flow_set_from_network",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.alarmconfig_dialog_add_criteria_flow_set_from_network}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_FROM_PORT = {"constant": "alarmconfig_dialog_add_criteria_flow_set_from_port",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_add_criteria_flow_set_from_port}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_INVERT = {"constant": "alarmconfig_dialog_add_criteria_flow_set_invert",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.alarmconfig_dialog_add_criteria_flow_set_invert}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_MATCH = {"constant": "alarmconfig_dialog_add_criteria_flow_set_match",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.alarmconfig_dialog_add_criteria_flow_set_match}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_TO_NETWORK = {"constant": "alarmconfig_dialog_add_criteria_flow_set_to_network",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_add_criteria_flow_set_to_network}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_FLOW_SET_TTL = {"constant": "alarmconfig_dialog_add_criteria_flow_set_ttl",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.alarmconfig_dialog_add_criteria_flow_set_ttl}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_SELECT_GROUPS = {"constant": "alarmconfig_dialog_add_criteria_select_groups",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.alarmconfig_dialog_add_criteria_select_groups}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_SEVERITY_SELECT_EVENTS_ONLY = {"constant": "alarmconfig_dialog_add_criteria_severity_select_events_only",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_add_criteria_severity_select_events_only}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_SEVERITY_SELECT_TRAPS_AND_EVENTS = {"constant": "alarmconfig_dialog_add_criteria_severity_select_traps_and_events",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.alarmconfig_dialog_add_criteria_severity_select_traps_and_events}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_SEVERITY_SELECT_TRAPS_ONLY = {"constant": "alarmconfig_dialog_add_criteria_severity_select_traps_only",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_severity_select_traps_only}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_SEVERITY_SET_EVENT_ALARM_SEVERITY = {"constant": "alarmconfig_dialog_add_criteria_severity_set_event_alarm_severity",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_severity_set_event_alarm_severity}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_STATUS_SELECT_BOTH = {"constant": "alarmconfig_dialog_add_criteria_status_select_both",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_add_criteria_status_select_both}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_STATUS_SELECT_CONTACT_ESTABLISHED = {"constant": "alarmconfig_dialog_add_criteria_status_select_contact_established",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_add_criteria_status_select_contact_established}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_STATUS_SELECT_CONTACT_LOST = {"constant": "alarmconfig_dialog_add_criteria_status_select_contact_lost",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_status_select_contact_lost}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_APPLICATION = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_application",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_application}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_APPLICATION_ANY = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_application_any",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_application_any}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_COLLECTOR = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_collector",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_collector}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_CROSS_WHEN_VALUE = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_cross_when_value",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_cross_when_value}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_ENGINES = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_engines",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_engines}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_LOCATION = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_location",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_location}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_LOCATION_ANY = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_location_any",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_location_any}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_REARM_WHEN_VALUE = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_rearm_when_value",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_rearm_when_value}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_STATISTIC = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_statistic",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_statistic}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_STATISTIC_NAME = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_statistic_name",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_statistic_name}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_STATISTIC_TYPE = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_statistic_type",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_statistic_type}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_TARGET_TYPE = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_target_type",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_target_type}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_THRESHOLD_SET_THRESHOLD_TYPE = {"constant": "alarmconfig_dialog_add_criteria_threshold_set_threshold_type",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_criteria_threshold_set_threshold_type}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_CLICK_CANCEL = {"constant": "alarmconfig_dialog_add_criteria_traps_click_cancel",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_add_criteria_traps_click_cancel}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_CLICK_SAVE = {"constant": "alarmconfig_dialog_add_criteria_traps_click_save",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_add_criteria_traps_click_save}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_CLICK_SELECT_TRAPS = {"constant": "alarmconfig_dialog_add_criteria_traps_click_select_traps",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_add_criteria_traps_click_select_traps}
        self.ALARMCONFIG_DIALOG_ADD_CRITERIA_TRAPS_SET_SELECTED = {"constant": "alarmconfig_dialog_add_criteria_traps_set_selected",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_add_criteria_traps_set_selected}
        self.ALARMCONFIG_DIALOG_ADD_OTHER_OPTIONS_SELECT_CLEARED_BY_ALARMS = {"constant": "alarmconfig_dialog_add_other_options_select_cleared_by_alarms",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_add_other_options_select_cleared_by_alarms}
        self.ALARMCONFIG_DIALOG_ADD_OTHER_OPTIONS_SELECT_NO_CURRENT_ALARM = {"constant": "alarmconfig_dialog_add_other_options_select_no_current_alarm",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_add_other_options_select_no_current_alarm}
        self.ALARMCONFIG_DIALOG_ADD_OTHER_OPTIONS_SET_CLEARED_BY_ALARMS = {"constant": "alarmconfig_dialog_add_other_options_set_cleared_by_alarms",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_add_other_options_set_cleared_by_alarms}
        self.ALARMCONFIG_DIALOG_ADD_SELECT_TAB = {"constant": "alarmconfig_dialog_add_select_tab",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.alarmconfig_dialog_add_select_tab}
        self.ALARMCONFIG_DIALOG_ADD_SET_ENABLED = {"constant": "alarmconfig_dialog_add_set_enabled",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.alarmconfig_dialog_add_set_enabled}
        self.ALARMCONFIG_DIALOG_ADD_SET_NAME = {"constant": "alarmconfig_dialog_add_set_name",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.alarmconfig_dialog_add_set_name}
        self.ALARMCONFIG_DIALOG_ADD_SET_SEVERITY = {"constant": "alarmconfig_dialog_add_set_severity",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.alarmconfig_dialog_add_set_severity}
        self.ALARMCONFIG_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "alarmconfig_dialog_confirm_delete_click_no",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.alarmconfig_dialog_confirm_delete_click_no}
        self.ALARMCONFIG_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "alarmconfig_dialog_confirm_delete_click_yes",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.alarmconfig_dialog_confirm_delete_click_yes}
        self.ALARMCONFIG_DIALOG_COPY_CLICK_CANCEL = {"constant": "alarmconfig_dialog_copy_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.alarmconfig_dialog_copy_click_cancel}
        self.ALARMCONFIG_DIALOG_COPY_CLICK_SAVE = {"constant": "alarmconfig_dialog_copy_click_save",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.alarmconfig_dialog_copy_click_save}
        self.ALARMCONFIG_DIALOG_COPY_SET_NAME = {"constant": "alarmconfig_dialog_copy_set_name",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.alarmconfig_dialog_copy_set_name}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CLICK_ADD = {"constant": "alarmconfig_dialog_edit_actions_click_add",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.alarmconfig_dialog_edit_actions_click_add}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CLICK_EDIT = {"constant": "alarmconfig_dialog_edit_actions_click_edit",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.alarmconfig_dialog_edit_actions_click_edit}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CLICK_REMOVE = {"constant": "alarmconfig_dialog_edit_actions_click_remove",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.alarmconfig_dialog_edit_actions_click_remove}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CLICK_TEST = {"constant": "alarmconfig_dialog_edit_actions_click_test",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.alarmconfig_dialog_edit_actions_click_test}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CUSTOM_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_actions_custom_click_cancel",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_edit_actions_custom_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CUSTOM_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_actions_custom_click_save",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_actions_custom_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CUSTOM_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_edit_actions_custom_select_override_content",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_edit_actions_custom_select_override_content}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CUSTOM_SET_CUSTOM_ARGUMENTS = {"constant": "alarmconfig_dialog_edit_actions_custom_set_custom_arguments",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_actions_custom_set_custom_arguments}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CUSTOM_SET_PROGRAM = {"constant": "alarmconfig_dialog_edit_actions_custom_set_program",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_edit_actions_custom_set_program}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_CUSTOM_SET_WORKING_DIRECTORY = {"constant": "alarmconfig_dialog_edit_actions_custom_set_working_directory",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_edit_actions_custom_set_working_directory}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_actions_email_click_cancel",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_edit_actions_email_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_CLICK_EDIT_EMAIL_LISTS = {"constant": "alarmconfig_dialog_edit_actions_email_click_edit_email_lists",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_edit_actions_email_click_edit_email_lists}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_actions_email_click_save",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_edit_actions_email_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_CLICK_ADD = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_click_add",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_click_add}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_click_cancel",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_CLICK_CLOSE = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_click_close",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_click_close}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_CLICK_EDIT = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_click_edit",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_click_edit}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_CLICK_REMOVE = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_click_remove",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_click_remove}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_click_save",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_SELECT_ROW = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_select_row",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_select_row}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_SET_ADDRESSES = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_set_addresses",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_set_addresses}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_EDITLIST_SET_LIST_NAME = {"constant": "alarmconfig_dialog_edit_actions_email_editlist_set_list_name",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_edit_actions_email_editlist_set_list_name}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_edit_actions_email_select_override_content",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_actions_email_select_override_content}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_SET_BODY = {"constant": "alarmconfig_dialog_edit_actions_email_set_body",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.alarmconfig_dialog_edit_actions_email_set_body}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_SET_DESTINATION = {"constant": "alarmconfig_dialog_edit_actions_email_set_destination",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.alarmconfig_dialog_edit_actions_email_set_destination}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_EMAIL_SET_SUBJECT = {"constant": "alarmconfig_dialog_edit_actions_email_set_subject",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_actions_email_set_subject}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SELECT_ENABLE_ALARM_ACTION_LIMIT = {"constant": "alarmconfig_dialog_edit_actions_select_enable_alarm_action_limit",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.alarmconfig_dialog_edit_actions_select_enable_alarm_action_limit}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SET_MAX_COUNT = {"constant": "alarmconfig_dialog_edit_actions_set_max_count",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.alarmconfig_dialog_edit_actions_set_max_count}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SET_RESET_INTERVAL = {"constant": "alarmconfig_dialog_edit_actions_set_reset_interval",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_edit_actions_set_reset_interval}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SYSLOG_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_actions_syslog_click_cancel",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_edit_actions_syslog_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SYSLOG_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_actions_syslog_click_save",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_actions_syslog_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SYSLOG_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_edit_actions_syslog_select_override_content",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_edit_actions_syslog_select_override_content}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SYSLOG_SET_MESSAGE = {"constant": "alarmconfig_dialog_edit_actions_syslog_set_message",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_edit_actions_syslog_set_message}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SYSLOG_SET_SYSLOG_SERVER = {"constant": "alarmconfig_dialog_edit_actions_syslog_set_syslog_server",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_actions_syslog_set_syslog_server}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_SYSLOG_SET_TAG = {"constant": "alarmconfig_dialog_edit_actions_syslog_set_tag",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.alarmconfig_dialog_edit_actions_syslog_set_tag}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_actions_trap_click_cancel",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_actions_trap_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_actions_trap_click_save",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.alarmconfig_dialog_edit_actions_trap_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_SELECT_OVERRIDE_CONTENT = {"constant": "alarmconfig_dialog_edit_actions_trap_select_override_content",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_edit_actions_trap_select_override_content}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_SET_SNMP_CREDENTIAL = {"constant": "alarmconfig_dialog_edit_actions_trap_set_snmp_credential",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_actions_trap_set_snmp_credential}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_SET_TRAP_MESSAGE = {"constant": "alarmconfig_dialog_edit_actions_trap_set_trap_message",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.alarmconfig_dialog_edit_actions_trap_set_trap_message}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_SET_TRAP_MESSAGE_OID = {"constant": "alarmconfig_dialog_edit_actions_trap_set_trap_message_oid",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_actions_trap_set_trap_message_oid}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_SET_TRAP_OID = {"constant": "alarmconfig_dialog_edit_actions_trap_set_trap_oid",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_actions_trap_set_trap_oid}
        self.ALARMCONFIG_DIALOG_EDIT_ACTIONS_TRAP_SET_TRAP_SERVER = {"constant": "alarmconfig_dialog_edit_actions_trap_set_trap_server",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.alarmconfig_dialog_edit_actions_trap_set_trap_server}
        self.ALARMCONFIG_DIALOG_EDIT_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.alarmconfig_dialog_edit_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_click_save",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.alarmconfig_dialog_edit_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CATEGORY_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_category_click_cancel",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_custom_category_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CATEGORY_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_category_click_save",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_custom_category_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CATEGORY_SELECT_CATEGORIES = {"constant": "alarmconfig_dialog_edit_criteria_custom_category_select_categories",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_category_select_categories}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CATEGORY_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_category_select_exclude_selected",
                                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_custom_category_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CATEGORY_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_category_select_match_selected",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_category_select_match_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CLICK_ADD = {"constant": "alarmconfig_dialog_edit_criteria_custom_click_add",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_criteria_custom_click_add}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CLICK_EDIT = {"constant": "alarmconfig_dialog_edit_criteria_custom_click_edit",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_click_edit}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_CLICK_REMOVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_click_remove",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_custom_click_remove}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_EVENT_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_event_click_cancel",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_edit_criteria_custom_event_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_EVENT_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_event_click_save",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_custom_event_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_EVENT_SELECT_EVENTS = {"constant": "alarmconfig_dialog_edit_criteria_custom_event_select_events",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_custom_event_select_events}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_EVENT_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_event_select_exclude_selected",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_edit_criteria_custom_event_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_EVENT_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_event_select_match_selected",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_custom_event_select_match_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_click_cancel",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_CLICK_EDIT_LIST = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_click_edit_list",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_click_edit_list}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_click_save",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_ADD = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_add",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_add}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_cancel",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_REMOVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_remove",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_remove}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_save",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SELECT_HOST_NAME = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_host_name",
                                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_host_name}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SELECT_IP_MASK = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_ip_mask",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_ip_mask}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SELECT_ROW = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_row",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_select_row}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SET_HOST_NAME = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_host_name",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_host_name}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SET_IP_ADDRESS = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_ip_address",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_ip_address}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_EDITLIST_SET_MASK = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_mask",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_editlist_set_mask}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_select_exclude_selected",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_SELECT_HOSTIPS = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_select_hostips",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_select_hostips}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_HOSTIP_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_hostip_select_match_selected",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_custom_hostip_select_match_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_click_cancel",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_CLICK_EDIT_LIST = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_click_edit_list",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_click_edit_list}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_click_save",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_ADD = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_click_add",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_click_add}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_click_cancel",
                                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                                          "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_REMOVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_click_remove",
                                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                                          "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_click_remove}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_click_save",
                                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                                        "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SELECT_CONTAINS = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_select_contains",
                                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                                             "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_select_contains}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SELECT_DOES_NOT_CONTAIN = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_select_does_not_contain",
                                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_select_does_not_contain}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SELECT_ROW = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_select_row",
                                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                                        "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_select_row}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_EDITLIST_SET_PHRASE = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_editlist_set_phrase",
                                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                                        "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_editlist_set_phrase}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_SELECT_MATCH_ALL_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_select_match_all_selected",
                                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_select_match_all_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_SELECT_MATCH_ANY_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_select_match_any_selected",
                                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_select_match_any_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_INFORMATION_SELECT_PHRASES = {"constant": "alarmconfig_dialog_edit_criteria_custom_information_select_phrases",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_information_select_phrases}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_LOG_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_log_click_cancel",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_custom_log_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_LOG_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_log_click_save",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_log_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_LOG_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_log_select_exclude_selected",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_custom_log_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_LOG_SELECT_LOGS = {"constant": "alarmconfig_dialog_edit_criteria_custom_log_select_logs",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_edit_criteria_custom_log_select_logs}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_LOG_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_log_select_match_selected",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_edit_criteria_custom_log_select_match_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_SELECT_ROW = {"constant": "alarmconfig_dialog_edit_criteria_custom_select_row",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_select_row}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_SEVERITY_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_severity_click_cancel",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_custom_severity_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_SEVERITY_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_severity_click_save",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_custom_severity_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_SEVERITY_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_severity_select_exclude_selected",
                                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_custom_severity_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_SEVERITY_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_severity_select_match_selected",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_custom_severity_select_match_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_SEVERITY_SELECT_SEVERITIES = {"constant": "alarmconfig_dialog_edit_criteria_custom_severity_select_severities",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_severity_select_severities}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_TYPE_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_custom_type_click_cancel",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_criteria_custom_type_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_TYPE_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_custom_type_click_save",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_edit_criteria_custom_type_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_TYPE_SELECT_EXCLUDE_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_type_select_exclude_selected",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_custom_type_select_exclude_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_TYPE_SELECT_MATCH_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_custom_type_select_match_selected",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_custom_type_select_match_selected}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_CUSTOM_TYPE_SELECT_TYPES = {"constant": "alarmconfig_dialog_edit_criteria_custom_type_select_types",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_criteria_custom_type_select_types}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_ALARM_INTERVAL = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_alarm_interval",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_alarm_interval}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_ALARM_SOURCE = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_alarm_source",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_alarm_source}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_FROM_NETWORK = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_from_network",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_from_network}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_FROM_PORT = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_from_port",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_from_port}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_INVERT = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_invert",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_invert}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_MATCH = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_match",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_match}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_TO_NETWORK = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_to_network",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_to_network}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_FLOW_SET_TTL = {"constant": "alarmconfig_dialog_edit_criteria_flow_set_ttl",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.alarmconfig_dialog_edit_criteria_flow_set_ttl}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_SELECT_GROUPS = {"constant": "alarmconfig_dialog_edit_criteria_select_groups",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.alarmconfig_dialog_edit_criteria_select_groups}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_SEVERITY_SELECT_EVENTS_ONLY = {"constant": "alarmconfig_dialog_edit_criteria_severity_select_events_only",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.alarmconfig_dialog_edit_criteria_severity_select_events_only}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_SEVERITY_SELECT_TRAPS_AND_EVENTS = {"constant": "alarmconfig_dialog_edit_criteria_severity_select_traps_and_events",
                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                  "link": self.link.alarmconfig_dialog_edit_criteria_severity_select_traps_and_events}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_SEVERITY_SELECT_TRAPS_ONLY = {"constant": "alarmconfig_dialog_edit_criteria_severity_select_traps_only",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_severity_select_traps_only}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_SEVERITY_SET_EVENT_ALARM_SEVERITY = {"constant": "alarmconfig_dialog_edit_criteria_severity_set_event_alarm_severity",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_severity_set_event_alarm_severity}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_STATUS_SELECT_BOTH = {"constant": "alarmconfig_dialog_edit_criteria_status_select_both",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_status_select_both}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_STATUS_SELECT_CONTACT_ESTABLISHED = {"constant": "alarmconfig_dialog_edit_criteria_status_select_contact_established",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.alarmconfig_dialog_edit_criteria_status_select_contact_established}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_STATUS_SELECT_CONTACT_LOST = {"constant": "alarmconfig_dialog_edit_criteria_status_select_contact_lost",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_status_select_contact_lost}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_APPLICATION = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_application",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_application}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_APPLICATION_ANY = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_application_any",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_application_any}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_COLLECTOR = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_collector",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_collector}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_CROSS_WHEN_VALUE = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_cross_when_value",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_cross_when_value}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_ENGINES = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_engines",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_engines}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_LOCATION = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_location",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_location}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_LOCATION_ANY = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_location_any",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_location_any}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_REARM_WHEN_VALUE = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_rearm_when_value",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_rearm_when_value}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_STATISTIC = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_statistic",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_statistic}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_STATISTIC_NAME = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_statistic_name",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_statistic_name}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_STATISTIC_TYPE = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_statistic_type",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_statistic_type}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_TARGET_TYPE = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_target_type",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_target_type}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_THRESHOLD_SET_THRESHOLD_TYPE = {"constant": "alarmconfig_dialog_edit_criteria_threshold_set_threshold_type",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_criteria_threshold_set_threshold_type}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_TRAPS_CLICK_CANCEL = {"constant": "alarmconfig_dialog_edit_criteria_traps_click_cancel",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_traps_click_cancel}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_TRAPS_CLICK_SAVE = {"constant": "alarmconfig_dialog_edit_criteria_traps_click_save",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.alarmconfig_dialog_edit_criteria_traps_click_save}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_TRAPS_CLICK_SELECT_TRAPS = {"constant": "alarmconfig_dialog_edit_criteria_traps_click_select_traps",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.alarmconfig_dialog_edit_criteria_traps_click_select_traps}
        self.ALARMCONFIG_DIALOG_EDIT_CRITERIA_TRAPS_SET_SELECTED = {"constant": "alarmconfig_dialog_edit_criteria_traps_set_selected",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.alarmconfig_dialog_edit_criteria_traps_set_selected}
        self.ALARMCONFIG_DIALOG_EDIT_OTHER_OPTIONS_SELECT_CLEARED_BY_ALARMS = {"constant": "alarmconfig_dialog_edit_other_options_select_cleared_by_alarms",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.alarmconfig_dialog_edit_other_options_select_cleared_by_alarms}
        self.ALARMCONFIG_DIALOG_EDIT_OTHER_OPTIONS_SELECT_NO_CURRENT_ALARM = {"constant": "alarmconfig_dialog_edit_other_options_select_no_current_alarm",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.alarmconfig_dialog_edit_other_options_select_no_current_alarm}
        self.ALARMCONFIG_DIALOG_EDIT_OTHER_OPTIONS_SET_CLEARED_BY_ALARMS = {"constant": "alarmconfig_dialog_edit_other_options_set_cleared_by_alarms",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.alarmconfig_dialog_edit_other_options_set_cleared_by_alarms}
        self.ALARMCONFIG_DIALOG_EDIT_SELECT_TAB = {"constant": "alarmconfig_dialog_edit_select_tab",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.alarmconfig_dialog_edit_select_tab}
        self.ALARMCONFIG_DIALOG_EDIT_SET_ENABLED = {"constant": "alarmconfig_dialog_edit_set_enabled",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.alarmconfig_dialog_edit_set_enabled}
        self.ALARMCONFIG_DIALOG_EDIT_SET_SEVERITY = {"constant": "alarmconfig_dialog_edit_set_severity",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.alarmconfig_dialog_edit_set_severity}
        self.ALARMCONFIG_SELECT_ALARM_DEFINITION = {"constant": "alarmconfig_select_alarm_definition",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.alarmconfig_select_alarm_definition}
        self.ALARMCONFIG_SET_TABLE_FILTER = {"constant": "alarmconfig_set_table_filter",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.alarmconfig_set_table_filter}
