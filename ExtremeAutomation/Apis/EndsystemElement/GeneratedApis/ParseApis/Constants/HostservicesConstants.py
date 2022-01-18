"""
This class outlines all the constants for the hostservices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostservicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostservicesConstants(ApiConstants):
    def __init__(self):
        super(HostservicesConstants, self).__init__()
        self.CHECK_PING_RESULT_ON_ENDSYS = {"constant": "check_ping_result_on_endsys",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_ping_result_on_endsys}
