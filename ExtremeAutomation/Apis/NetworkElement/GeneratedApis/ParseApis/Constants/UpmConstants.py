"""
This class outlines all the constants for the upm API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(UpmConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class UpmConstants(ApiConstants):
    def __init__(self):
        super(UpmConstants, self).__init__()
        self.CHECK_UPM_AUTHENTICATE_PROFILE_PORTS = {"constant": "check_upm_authenticate_profile_ports",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_upm_authenticate_profile_ports}
        self.CHECK_UPM_UNAUTHENTICATED_PROFILE_PORTS = {"constant": "check_upm_unauthenticated_profile_ports",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.check_upm_unauthenticated_profile_ports}
