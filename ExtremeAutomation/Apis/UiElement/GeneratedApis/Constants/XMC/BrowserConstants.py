"""
This class outlines all the constants for the browser API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(BrowserConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class BrowserConstants(ApiConstants):
    def __init__(self):
        super(BrowserConstants, self).__init__()
        self.CLOSE_WEB_PAGE = {"constant": "close_web_page",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.close_web_page}
        self.LOGIN = {"constant": "login",
                      "tags": ["COMMAND_SELENIUM"],
                      "link": self.link.login}
        self.OPEN_WEB_PAGE = {"constant": "open_web_page",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.open_web_page}
