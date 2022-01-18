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
        self.CHECK_REGEX_IN_OUTPUT = {"constant": "check_regex_in_output",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_regex_in_output}
        self.CHECK_STRING_IN_OUTPUT = {"constant": "check_string_in_output",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_string_in_output}
