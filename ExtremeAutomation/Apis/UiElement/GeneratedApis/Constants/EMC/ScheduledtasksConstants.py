"""
This class outlines all the constants for the scheduledtasks API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ScheduledtasksConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ScheduledtasksConstants(ApiConstants):
    def __init__(self):
        super(ScheduledtasksConstants, self).__init__()
        self.SCHEDULEDTASKS_CLICK_ADD = {"constant": "scheduledtasks_click_add",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.scheduledtasks_click_add}
        self.SCHEDULEDTASKS_CLICK_COPY = {"constant": "scheduledtasks_click_copy",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.scheduledtasks_click_copy}
        self.SCHEDULEDTASKS_CLICK_DELETE = {"constant": "scheduledtasks_click_delete",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.scheduledtasks_click_delete}
        self.SCHEDULEDTASKS_CLICK_DISABLE = {"constant": "scheduledtasks_click_disable",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.scheduledtasks_click_disable}
        self.SCHEDULEDTASKS_CLICK_EDIT = {"constant": "scheduledtasks_click_edit",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.scheduledtasks_click_edit}
        self.SCHEDULEDTASKS_CLICK_REFRESH = {"constant": "scheduledtasks_click_refresh",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.scheduledtasks_click_refresh}
        self.SCHEDULEDTASKS_CLICK_RUN = {"constant": "scheduledtasks_click_run",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.scheduledtasks_click_run}
        self.SCHEDULEDTASKS_CLICK_SMTP = {"constant": "scheduledtasks_click_smtp",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.scheduledtasks_click_smtp}
        self.SCHEDULEDTASKS_CONFIRM_TASK_EXISTS = {"constant": "scheduledtasks_confirm_task_exists",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.scheduledtasks_confirm_task_exists}
        self.SCHEDULEDTASKS_DIALOG_ADD_CLICK_CANCEL = {"constant": "scheduledtasks_dialog_add_click_cancel",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scheduledtasks_dialog_add_click_cancel}
        self.SCHEDULEDTASKS_DIALOG_ADD_CLICK_SAVE = {"constant": "scheduledtasks_dialog_add_click_save",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.scheduledtasks_dialog_add_click_save}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_EMAIL_BODY = {"constant": "scheduledtasks_dialog_add_set_email_body",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scheduledtasks_dialog_add_set_email_body}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_EMAIL_SUBJECT = {"constant": "scheduledtasks_dialog_add_set_email_subject",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scheduledtasks_dialog_add_set_email_subject}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_EMAIL_TO = {"constant": "scheduledtasks_dialog_add_set_email_to",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scheduledtasks_dialog_add_set_email_to}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_END_DATE = {"constant": "scheduledtasks_dialog_add_set_end_date",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scheduledtasks_dialog_add_set_end_date}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_END_TIME = {"constant": "scheduledtasks_dialog_add_set_end_time",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scheduledtasks_dialog_add_set_end_time}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_RECURRENCE_DAILY = {"constant": "scheduledtasks_dialog_add_set_recurrence_daily",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.scheduledtasks_dialog_add_set_recurrence_daily}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_RECURRENCE_HOURLY = {"constant": "scheduledtasks_dialog_add_set_recurrence_hourly",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_add_set_recurrence_hourly}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_RECURRENCE_MONTHLY = {"constant": "scheduledtasks_dialog_add_set_recurrence_monthly",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.scheduledtasks_dialog_add_set_recurrence_monthly}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_RECURRENCE_WEEKLY = {"constant": "scheduledtasks_dialog_add_set_recurrence_weekly",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_add_set_recurrence_weekly}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_REPORT_NAME = {"constant": "scheduledtasks_dialog_add_set_report_name",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_add_set_report_name}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_START_DATE = {"constant": "scheduledtasks_dialog_add_set_start_date",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scheduledtasks_dialog_add_set_start_date}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_START_TIME = {"constant": "scheduledtasks_dialog_add_set_start_time",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scheduledtasks_dialog_add_set_start_time}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_TASK_DESCRIPTION = {"constant": "scheduledtasks_dialog_add_set_task_description",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.scheduledtasks_dialog_add_set_task_description}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_TASK_ENABLED = {"constant": "scheduledtasks_dialog_add_set_task_enabled",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.scheduledtasks_dialog_add_set_task_enabled}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_TASK_NAME = {"constant": "scheduledtasks_dialog_add_set_task_name",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_add_set_task_name}
        self.SCHEDULEDTASKS_DIALOG_ADD_SET_TYPE = {"constant": "scheduledtasks_dialog_add_set_type",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.scheduledtasks_dialog_add_set_type}
        self.SCHEDULEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "scheduledtasks_dialog_confirm_delete_click_no",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scheduledtasks_dialog_confirm_delete_click_no}
        self.SCHEDULEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "scheduledtasks_dialog_confirm_delete_click_yes",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.scheduledtasks_dialog_confirm_delete_click_yes}
        self.SCHEDULEDTASKS_DIALOG_CONFIRM_DISABLE_CLICK_NO = {"constant": "scheduledtasks_dialog_confirm_disable_click_no",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.scheduledtasks_dialog_confirm_disable_click_no}
        self.SCHEDULEDTASKS_DIALOG_CONFIRM_DISABLE_CLICK_YES = {"constant": "scheduledtasks_dialog_confirm_disable_click_yes",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_confirm_disable_click_yes}
        self.SCHEDULEDTASKS_DIALOG_COPY_CLICK_CANCEL = {"constant": "scheduledtasks_dialog_copy_click_cancel",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_copy_click_cancel}
        self.SCHEDULEDTASKS_DIALOG_COPY_CLICK_SAVE = {"constant": "scheduledtasks_dialog_copy_click_save",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scheduledtasks_dialog_copy_click_save}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_EMAIL_BODY = {"constant": "scheduledtasks_dialog_copy_set_email_body",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_copy_set_email_body}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_EMAIL_SUBJECT = {"constant": "scheduledtasks_dialog_copy_set_email_subject",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scheduledtasks_dialog_copy_set_email_subject}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_EMAIL_TO = {"constant": "scheduledtasks_dialog_copy_set_email_to",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_copy_set_email_to}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_END_DATE = {"constant": "scheduledtasks_dialog_copy_set_end_date",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_copy_set_end_date}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_END_TIME = {"constant": "scheduledtasks_dialog_copy_set_end_time",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_copy_set_end_time}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_RECURRENCE_DAILY = {"constant": "scheduledtasks_dialog_copy_set_recurrence_daily",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_copy_set_recurrence_daily}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_RECURRENCE_HOURLY = {"constant": "scheduledtasks_dialog_copy_set_recurrence_hourly",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.scheduledtasks_dialog_copy_set_recurrence_hourly}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_RECURRENCE_MONTHLY = {"constant": "scheduledtasks_dialog_copy_set_recurrence_monthly",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.scheduledtasks_dialog_copy_set_recurrence_monthly}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_RECURRENCE_WEEKLY = {"constant": "scheduledtasks_dialog_copy_set_recurrence_weekly",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.scheduledtasks_dialog_copy_set_recurrence_weekly}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_START_DATE = {"constant": "scheduledtasks_dialog_copy_set_start_date",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_copy_set_start_date}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_START_TIME = {"constant": "scheduledtasks_dialog_copy_set_start_time",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_copy_set_start_time}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_TASK_DESCRIPTION = {"constant": "scheduledtasks_dialog_copy_set_task_description",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_copy_set_task_description}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_TASK_ENABLED = {"constant": "scheduledtasks_dialog_copy_set_task_enabled",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scheduledtasks_dialog_copy_set_task_enabled}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_TASK_NAME = {"constant": "scheduledtasks_dialog_copy_set_task_name",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scheduledtasks_dialog_copy_set_task_name}
        self.SCHEDULEDTASKS_DIALOG_COPY_SET_TYPE = {"constant": "scheduledtasks_dialog_copy_set_type",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.scheduledtasks_dialog_copy_set_type}
        self.SCHEDULEDTASKS_DIALOG_EDIT_CLICK_CANCEL = {"constant": "scheduledtasks_dialog_edit_click_cancel",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_edit_click_cancel}
        self.SCHEDULEDTASKS_DIALOG_EDIT_CLICK_SAVE = {"constant": "scheduledtasks_dialog_edit_click_save",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scheduledtasks_dialog_edit_click_save}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_EMAIL_BODY = {"constant": "scheduledtasks_dialog_edit_set_email_body",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_edit_set_email_body}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_EMAIL_SUBJECT = {"constant": "scheduledtasks_dialog_edit_set_email_subject",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scheduledtasks_dialog_edit_set_email_subject}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_EMAIL_TO = {"constant": "scheduledtasks_dialog_edit_set_email_to",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_edit_set_email_to}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_END_DATE = {"constant": "scheduledtasks_dialog_edit_set_end_date",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_edit_set_end_date}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_END_TIME = {"constant": "scheduledtasks_dialog_edit_set_end_time",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_edit_set_end_time}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_RECURRENCE_DAILY = {"constant": "scheduledtasks_dialog_edit_set_recurrence_daily",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_edit_set_recurrence_daily}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_RECURRENCE_HOURLY = {"constant": "scheduledtasks_dialog_edit_set_recurrence_hourly",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.scheduledtasks_dialog_edit_set_recurrence_hourly}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_RECURRENCE_MONTHLY = {"constant": "scheduledtasks_dialog_edit_set_recurrence_monthly",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.scheduledtasks_dialog_edit_set_recurrence_monthly}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_RECURRENCE_WEEKLY = {"constant": "scheduledtasks_dialog_edit_set_recurrence_weekly",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.scheduledtasks_dialog_edit_set_recurrence_weekly}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_START_DATE = {"constant": "scheduledtasks_dialog_edit_set_start_date",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_edit_set_start_date}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_START_TIME = {"constant": "scheduledtasks_dialog_edit_set_start_time",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scheduledtasks_dialog_edit_set_start_time}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_TASK_DESCRIPTION = {"constant": "scheduledtasks_dialog_edit_set_task_description",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.scheduledtasks_dialog_edit_set_task_description}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_TASK_ENABLED = {"constant": "scheduledtasks_dialog_edit_set_task_enabled",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scheduledtasks_dialog_edit_set_task_enabled}
        self.SCHEDULEDTASKS_DIALOG_EDIT_SET_TASK_NAME = {"constant": "scheduledtasks_dialog_edit_set_task_name",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scheduledtasks_dialog_edit_set_task_name}
        self.SCHEDULEDTASKS_DIALOG_SMTP_CLICK_CANCEL = {"constant": "scheduledtasks_dialog_smtp_click_cancel",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_smtp_click_cancel}
        self.SCHEDULEDTASKS_DIALOG_SMTP_CLICK_OK = {"constant": "scheduledtasks_dialog_smtp_click_ok",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.scheduledtasks_dialog_smtp_click_ok}
        self.SCHEDULEDTASKS_DIALOG_SMTP_SET_ADDRESS = {"constant": "scheduledtasks_dialog_smtp_set_address",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scheduledtasks_dialog_smtp_set_address}
        self.SCHEDULEDTASKS_DIALOG_SMTP_SET_PASSWORD = {"constant": "scheduledtasks_dialog_smtp_set_password",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scheduledtasks_dialog_smtp_set_password}
        self.SCHEDULEDTASKS_DIALOG_SMTP_SET_SERVER = {"constant": "scheduledtasks_dialog_smtp_set_server",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scheduledtasks_dialog_smtp_set_server}
        self.SCHEDULEDTASKS_SELECT_TASK = {"constant": "scheduledtasks_select_task",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.scheduledtasks_select_task}
        self.SCHEDULEDTASKS_WAIT_FOR_TASK_ADD = {"constant": "scheduledtasks_wait_for_task_add",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.scheduledtasks_wait_for_task_add}
        self.SCHEDULEDTASKS_WAIT_FOR_TASK_REMOVE = {"constant": "scheduledtasks_wait_for_task_remove",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.scheduledtasks_wait_for_task_remove}
