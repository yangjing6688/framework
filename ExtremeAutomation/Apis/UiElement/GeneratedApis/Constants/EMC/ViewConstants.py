"""
This class outlines all the constants for the view API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ViewConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ViewConstants(ApiConstants):
    def __init__(self):
        super(ViewConstants, self).__init__()
        self.VIEW_CONFIRM_LOGGED_IN = {"constant": "view_confirm_logged_in",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.view_confirm_logged_in}
        self.VIEW_MENU_ABOUT = {"constant": "view_menu_about",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.view_menu_about}
        self.VIEW_MENU_LOGOUT = {"constant": "view_menu_logout",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.view_menu_logout}
        self.VIEW_SELECT_TAB = {"constant": "view_select_tab",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.view_select_tab}
