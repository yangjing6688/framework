"""
This class outlines all the constants for the logging API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(LoggingConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class LoggingConstants(ApiConstants):
    def __init__(self):
        super(LoggingConstants, self).__init__()
        self.CLEAR_LOG = {"constant": "clear_log",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.clear_log}
        self.CLEAR_LOG_AUDITLOG = {"constant": "clear_log_auditlog",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_log_auditlog}
        self.CLEAR_LOG_RASLOG = {"constant": "clear_log_raslog",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_log_raslog}
        self.SHOW_LOG = {"constant": "show_log",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_log}
        self.SHOW_LOG_AUDITLOG = {"constant": "show_log_auditlog",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_log_auditlog}
        self.SHOW_LOG_RASLOG = {"constant": "show_log_raslog",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_log_raslog}
