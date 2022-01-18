"""
This class outlines all the constants for the dfndrbrowser API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DfndrbrowserConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DfndrbrowserConstants(ApiConstants):
    def __init__(self):
        super(DfndrbrowserConstants, self).__init__()
        self.DFNDR_BROWSER_CLOSE_WEB_PAGE = {"constant": "dfndr_browser_close_web_page",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.dfndr_browser_close_web_page}
        self.DFNDR_BROWSER_LOGIN = {"constant": "dfndr_browser_login",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.dfndr_browser_login}
        self.DFNDR_BROWSER_LOGOUT = {"constant": "dfndr_browser_logout",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.dfndr_browser_logout}
        self.DFNDR_BROWSER_ONLY_URL = {"constant": "dfndr_browser_only_url",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.dfndr_browser_only_url}
        self.DFNDR_BROWSER_OPEN_WEB_PAGE = {"constant": "dfndr_browser_open_web_page",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.dfndr_browser_open_web_page}
