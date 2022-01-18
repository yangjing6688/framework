"""
This class outlines all the constants for the gimsponsors API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimsponsorsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimsponsorsConstants(ApiConstants):
    def __init__(self):
        super(GimsponsorsConstants, self).__init__()
        self.GIM_SPONSOR_DETAILS_ADD = {"constant": "gim_sponsor_details_add",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.gim_sponsor_details_add}
