"""
This class outlines all the constants for the cloudconnectfsm API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CloudconnectfsmConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CloudconnectfsmConstants(ApiConstants):
    def __init__(self):
        super(CloudconnectfsmConstants, self).__init__()
        self.CHECK_DEVICE_STATES = {"constant": "check_device_states",
                                    "tags": ["PARSE_REST"],
                                    "link": self.link.check_device_states}
        self.CHECK_DEVICE_VERSION = {"constant": "check_device_version",
                                     "tags": ["PARSE_REST"],
                                     "link": self.link.check_device_version}
        self.STORE_MGMT_IP = {"constant": "store_mgmt_ip",
                              "tags": ["PARSE_REST"],
                              "link": self.link.store_mgmt_ip}
