"""
This class outlines all the constants for the help API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HelpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HelpConstants(ApiConstants):
    def __init__(self):
        super(HelpConstants, self).__init__()
        self.HELP_CLICK_LAUNCH_NEW_TAB = {"constant": "help_click_launch_new_tab",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.help_click_launch_new_tab}
        self.HELP_CLICK_PAUSE = {"constant": "help_click_pause",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.help_click_pause}
        self.HELP_CLICK_RESUME = {"constant": "help_click_resume",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.help_click_resume}
        self.HELP_CONFIRM_CONTEXT_HELP_IS_VISIBLE = {"constant": "help_confirm_context_help_is_visible",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.help_confirm_context_help_is_visible}
        self.HELP_CONFIRM_GETTING_STARTED_EXISTS = {"constant": "help_confirm_getting_started_exists",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.help_confirm_getting_started_exists}
        self.HELP_CONFIRM_GETTING_STARTED_IS_VISIBLE = {"constant": "help_confirm_getting_started_is_visible",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.help_confirm_getting_started_is_visible}
        self.HELP_HIDE_CONTEXT_HELP = {"constant": "help_hide_context_help",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.help_hide_context_help}
        self.HELP_HIDE_GETTING_STARTED = {"constant": "help_hide_getting_started",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.help_hide_getting_started}
        self.HELP_SHOW_CONTEXT_HELP = {"constant": "help_show_context_help",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.help_show_context_help}
        self.HELP_SHOW_GETTING_STARTED = {"constant": "help_show_getting_started",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.help_show_getting_started}
