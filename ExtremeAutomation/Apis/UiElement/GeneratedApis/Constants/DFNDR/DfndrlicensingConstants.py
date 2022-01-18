"""
This class outlines all the constants for the dfndrlicensing API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DfndrlicensingConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DfndrlicensingConstants(ApiConstants):
    def __init__(self):
        super(DfndrlicensingConstants, self).__init__()
        self.DFNDR_LICENSING_FUNCTION = {"constant": "dfndr_licensing_function",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.dfndr_licensing_function}
