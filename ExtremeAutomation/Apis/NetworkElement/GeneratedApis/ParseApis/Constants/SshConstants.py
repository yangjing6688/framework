"""
This class outlines all the constants for the ssh API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SshConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SshConstants(ApiConstants):
    def __init__(self):
        super(SshConstants, self).__init__()
        self.VERIFY_CLIENT_SOURCE_INTERFACE = {"constant": "verify_client_source_interface",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.verify_client_source_interface}
        self.VERIFY_DISABLED = {"constant": "verify_disabled",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.verify_disabled}
        self.VERIFY_ENABLED = {"constant": "verify_enabled",
                               "tags": ["PARSE_CLI"],
                               "link": self.link.verify_enabled}
        self.VERIFY_TCP_PORT = {"constant": "verify_tcp_port",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.verify_tcp_port}
        self.VERIFY_VERSION = {"constant": "verify_version",
                               "tags": ["PARSE_CLI"],
                               "link": self.link.verify_version}
