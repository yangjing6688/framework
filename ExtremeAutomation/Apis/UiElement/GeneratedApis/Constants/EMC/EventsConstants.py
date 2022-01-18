"""
This class outlines all the constants for the events API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EventsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EventsConstants(ApiConstants):
    def __init__(self):
        super(EventsConstants, self).__init__()
        self.EVENTS_CLEAR_COLUMN_FILTER = {"constant": "events_clear_column_filter",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.events_clear_column_filter}
        self.EVENTS_CLEAR_TABLE_FILTER = {"constant": "events_clear_table_filter",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.events_clear_table_filter}
        self.EVENTS_CLICK_FIRST_PAGE = {"constant": "events_click_first_page",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.events_click_first_page}
        self.EVENTS_CLICK_LAST_PAGE = {"constant": "events_click_last_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.events_click_last_page}
        self.EVENTS_CLICK_NEXT_PAGE = {"constant": "events_click_next_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.events_click_next_page}
        self.EVENTS_CLICK_PREV_PAGE = {"constant": "events_click_prev_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.events_click_prev_page}
        self.EVENTS_CLICK_RESET = {"constant": "events_click_reset",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.events_click_reset}
        self.EVENTS_CONFIRM_EVENT_EVENT = {"constant": "events_confirm_event_event",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.events_confirm_event_event}
        self.EVENTS_CONFIRM_EVENT_EVENT_AND_INFORMATION = {"constant": "events_confirm_event_event_and_information",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.events_confirm_event_event_and_information}
        self.EVENTS_CONFIRM_EVENT_EVENT_INFORMATION_AND_SOURCE = {"constant": "events_confirm_event_event_information_and_source",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.events_confirm_event_event_information_and_source}
        self.EVENTS_CONFIRM_EVENT_EXISTS = {"constant": "events_confirm_event_exists",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.events_confirm_event_exists}
        self.EVENTS_CONFIRM_EVENT_MESSAGE_CONTAINS = {"constant": "events_confirm_event_message_contains",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.events_confirm_event_message_contains}
        self.EVENTS_DISABLE_COLUMN_FILTER = {"constant": "events_disable_column_filter",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.events_disable_column_filter}
        self.EVENTS_ENABLE_COLUMN_FILTER = {"constant": "events_enable_column_filter",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.events_enable_column_filter}
        self.EVENTS_SELECT_EVENT = {"constant": "events_select_event",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.events_select_event}
        self.EVENTS_SET_COLUMN_FILTER = {"constant": "events_set_column_filter",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.events_set_column_filter}
        self.EVENTS_SET_EVENT_TYPES = {"constant": "events_set_event_types",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.events_set_event_types}
        self.EVENTS_SET_TABLE_FILTER = {"constant": "events_set_table_filter",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.events_set_table_filter}
        self.EVENTS_SET_TIME_SPAN = {"constant": "events_set_time_span",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.events_set_time_span}
