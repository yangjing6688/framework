"""
This class outlines all the constants for the gimbrowser API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimbrowserConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimbrowserConstants(ApiConstants):
    def __init__(self):
        super(GimbrowserConstants, self).__init__()
        self.BROWSER_CLOSE_WEB_PAGE = {"constant": "browser_close_web_page",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.browser_close_web_page}
        self.BROWSER_LOGIN = {"constant": "browser_login",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.browser_login}
        self.BROWSER_LOGOUT = {"constant": "browser_logout",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.browser_logout}
        self.BROWSER_ONLY_URL = {"constant": "browser_only_url",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.browser_only_url}
        self.BROWSER_OPEN_WEB_PAGE = {"constant": "browser_open_web_page",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.browser_open_web_page}
