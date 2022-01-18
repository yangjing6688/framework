"""
This class outlines all the constants for the sponsors API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SponsorsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SponsorsConstants(ApiConstants):
    def __init__(self):
        super(SponsorsConstants, self).__init__()
        self.SPONSOR_ADD = {"constant": "sponsor_add",
                            "tags": ["COMMAND_SELENIUM"],
                            "link": self.link.sponsor_add}
        self.SPONSOR_CONFIGURATION_OPTIONS = {"constant": "sponsor_configuration_options",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.sponsor_configuration_options}
        self.SPONSOR_DETAILS_ADD = {"constant": "sponsor_details_add",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.sponsor_details_add}
        self.SPONSOR_DETAILS_VALIDATION = {"constant": "sponsor_details_validation",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.sponsor_details_validation}
        self.SPONSOR_PAGE_VALIDATION = {"constant": "sponsor_page_validation",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.sponsor_page_validation}
