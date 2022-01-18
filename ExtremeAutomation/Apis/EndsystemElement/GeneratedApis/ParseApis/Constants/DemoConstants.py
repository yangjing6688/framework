"""
This class outlines all the constants for the demo API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DemoConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DemoConstants(ApiConstants):
    def __init__(self):
        super(DemoConstants, self).__init__()
        self.VERIFY_GUEST_ONBOARDING_TEMPLATE = {"constant": "verify_guest_onboarding_template",
                                                 "tags": ["PARSE_REST"],
                                                 "link": self.link.verify_guest_onboarding_template}
