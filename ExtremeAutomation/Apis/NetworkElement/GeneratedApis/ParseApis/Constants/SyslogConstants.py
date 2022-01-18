"""
This class outlines all the constants for the syslog API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SyslogConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SyslogConstants(ApiConstants):
    def __init__(self):
        super(SyslogConstants, self).__init__()
        self.CHECK_SYSLOG_SERVER = {"constant": "check_syslog_server",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_syslog_server}
        self.VERIFY_LOGIN_EXISTS = {"constant": "verify_login_exists",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.verify_login_exists}
