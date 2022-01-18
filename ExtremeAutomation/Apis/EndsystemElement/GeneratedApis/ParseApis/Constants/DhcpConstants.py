"""
This class outlines all the constants for the dhcp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DhcpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DhcpConstants(ApiConstants):
    def __init__(self):
        super(DhcpConstants, self).__init__()
        self.CHECK_DHCP_PROCESS = {"constant": "check_dhcp_process",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_dhcp_process}
