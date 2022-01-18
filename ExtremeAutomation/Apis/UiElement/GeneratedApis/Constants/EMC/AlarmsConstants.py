"""
This class outlines all the constants for the alarms API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AlarmsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AlarmsConstants(ApiConstants):
    def __init__(self):
        super(AlarmsConstants, self).__init__()
        self.ALARMS_CLEAR_TABLE_FILTER = {"constant": "alarms_clear_table_filter",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.alarms_clear_table_filter}
        self.ALARMS_CLICK_FIRST_PAGE = {"constant": "alarms_click_first_page",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.alarms_click_first_page}
        self.ALARMS_CLICK_LAST_PAGE = {"constant": "alarms_click_last_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.alarms_click_last_page}
        self.ALARMS_CLICK_NEXT_PAGE = {"constant": "alarms_click_next_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.alarms_click_next_page}
        self.ALARMS_CLICK_PREV_PAGE = {"constant": "alarms_click_prev_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.alarms_click_prev_page}
        self.ALARMS_CLICK_REFRESH = {"constant": "alarms_click_refresh",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.alarms_click_refresh}
        self.ALARMS_CONFIRM_ALARM_HISTORY_REASON_EXISTS = {"constant": "alarms_confirm_alarm_history_reason_exists",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.alarms_confirm_alarm_history_reason_exists}
        self.ALARMS_CONFIRM_ALARM_INFO_CONTAINS = {"constant": "alarms_confirm_alarm_info_contains",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.alarms_confirm_alarm_info_contains}
        self.ALARMS_CONFIRM_ALARM_NAME_EXISTS = {"constant": "alarms_confirm_alarm_name_exists",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.alarms_confirm_alarm_name_exists}
        self.ALARMS_DIALOG_EDIT_ALARM_DEFINITION_CANCEL = {"constant": "alarms_dialog_edit_alarm_definition_cancel",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.alarms_dialog_edit_alarm_definition_cancel}
        self.ALARMS_DIALOG_HISTORY_CLOSE = {"constant": "alarms_dialog_history_close",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.alarms_dialog_history_close}
        self.ALARMS_MENU_CLEAR_ALL_ALARMS = {"constant": "alarms_menu_clear_all_alarms",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.alarms_menu_clear_all_alarms}
        self.ALARMS_MENU_CLEAR_SELECTED_ALARMS = {"constant": "alarms_menu_clear_selected_alarms",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.alarms_menu_clear_selected_alarms}
        self.ALARMS_MENU_CLEAR_SELECTED_ALARMS_WITH_REASON = {"constant": "alarms_menu_clear_selected_alarms_with_reason",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.alarms_menu_clear_selected_alarms_with_reason}
        self.ALARMS_MENU_EDIT_ALARM_DEFINITION = {"constant": "alarms_menu_edit_alarm_definition",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.alarms_menu_edit_alarm_definition}
        self.ALARMS_MENU_HISTORY_ALL = {"constant": "alarms_menu_history_all",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.alarms_menu_history_all}
        self.ALARMS_MENU_HISTORY_BY_ALARM_NAME = {"constant": "alarms_menu_history_by_alarm_name",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.alarms_menu_history_by_alarm_name}
        self.ALARMS_MENU_HISTORY_BY_SOURCE = {"constant": "alarms_menu_history_by_source",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.alarms_menu_history_by_source}
        self.ALARMS_SELECT_ALARM_BY_NAME = {"constant": "alarms_select_alarm_by_name",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.alarms_select_alarm_by_name}
        self.ALARMS_SELECT_ALARM_BY_SOURCE_IP = {"constant": "alarms_select_alarm_by_source_ip",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.alarms_select_alarm_by_source_ip}
        self.ALARMS_SET_TABLE_FILTER = {"constant": "alarms_set_table_filter",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.alarms_set_table_filter}
