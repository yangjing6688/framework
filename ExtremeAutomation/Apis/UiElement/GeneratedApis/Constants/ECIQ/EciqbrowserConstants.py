"""
This class outlines all the constants for the eciqbrowser API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqbrowserConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqbrowserConstants(ApiConstants):
    def __init__(self):
        super(EciqbrowserConstants, self).__init__()
        self.BYPASS_CERTIFICATE_POPUP = {"constant": "bypass_certificate_popup",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.bypass_certificate_popup}
        self.CLICK_CLOSE_BUTTON = {"constant": "click_close_button",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.click_close_button}
        self.CLICK_DO_NOT_SHOW_AGAIN_CHECKBOX = {"constant": "click_do_not_show_again_checkbox",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.click_do_not_show_again_checkbox}
        self.CLOSE_WEB_PAGE = {"constant": "close_web_page",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.close_web_page}
        self.LOGIN = {"constant": "login",
                      "tags": ["COMMAND_SELENIUM"],
                      "link": self.link.login}
        self.OPEN_WEB_PAGE = {"constant": "open_web_page",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.open_web_page}
