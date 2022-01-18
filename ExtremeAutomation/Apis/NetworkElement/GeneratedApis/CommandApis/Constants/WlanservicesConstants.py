"""
This class outlines all the constants for the wlanservices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(WlanservicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class WlanservicesConstants(ApiConstants):
    def __init__(self):
        super(WlanservicesConstants, self).__init__()
        self.SHOW_ALL = {"constant": "show_all",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_all}
        self.SHOW_DETAIL = {"constant": "show_detail",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_detail}
