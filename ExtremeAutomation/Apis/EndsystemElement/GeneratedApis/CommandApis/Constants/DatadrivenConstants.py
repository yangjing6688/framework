"""
This class outlines all the constants for the devices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print DevicesConstants().<SOME_CONSTANT>
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DatadrivenConstants(ApiConstants):
    def __init__(self):
        super(DatadrivenConstants, self).__init__()
        self.VERIFY_NORTHBOUND_QUERY = {"constant": "verify_northbound_query",
                                        "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                        "link": self.link.verify_northbound_query}
        self.VERIFY_NORTHBOUND_QUERY_WITH_REGEX = {"constant": "verify_northbound_query_with_regex",
                                                   "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                                   "link": self.link.verify_northbound_query_with_regex}
