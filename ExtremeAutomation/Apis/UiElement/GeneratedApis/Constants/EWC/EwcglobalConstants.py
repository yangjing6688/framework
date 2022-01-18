"""
This class outlines all the constants for the ewcglobal API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcglobalConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcglobalConstants(ApiConstants):
    def __init__(self):
        super(EwcglobalConstants, self).__init__()
        self.GLOBAL_AUTHENTICATION_CHECK_STRICT_MODE = {"constant": "global_authentication_check_strict_mode",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.global_authentication_check_strict_mode}
        self.GLOBAL_AUTHENTICATION_UNCHECK_STRICT_MODE = {"constant": "global_authentication_uncheck_strict_mode",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.global_authentication_uncheck_strict_mode}
        self.GLOBAL_CLICK_SAVE_BUTTON = {"constant": "global_click_save_button",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.global_click_save_button}
