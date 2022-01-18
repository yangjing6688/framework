"""
This class outlines all the constants for the xcaaccesspoints API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcaaccesspointsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcaaccesspointsConstants(ApiConstants):
    def __init__(self):
        super(XcaaccesspointsConstants, self).__init__()
        self.VERIFY_ACCESS_POINT_IS_ASSOCIATED_WITH_SITE = {"constant": "verify_access_point_is_associated_with_site",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.verify_access_point_is_associated_with_site}
