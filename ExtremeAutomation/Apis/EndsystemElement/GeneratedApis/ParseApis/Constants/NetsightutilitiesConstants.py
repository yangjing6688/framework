"""
This class outlines all the constants for the netsightutilities API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NetsightutilitiesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NetsightutilitiesConstants(ApiConstants):
    def __init__(self):
        super(NetsightutilitiesConstants, self).__init__()
        self.VERIFY_REST_READ = {"constant": "verify_rest_read",
                                 "tags": ["PARSE_REST"],
                                 "link": self.link.verify_rest_read}
        self.VERIFY_REST_READ_ALL = {"constant": "verify_rest_read_all",
                                     "tags": ["PARSE_REST"],
                                     "link": self.link.verify_rest_read_all}
