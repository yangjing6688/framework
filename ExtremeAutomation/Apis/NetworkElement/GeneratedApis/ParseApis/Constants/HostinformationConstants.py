"""
This class outlines all the constants for the hostinformation API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostinformationConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostinformationConstants(ApiConstants):
    def __init__(self):
        super(HostinformationConstants, self).__init__()
        self.CHECK_APP_IQAGENT = {"constant": "check_app_iqagent",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_app_iqagent}
        self.CHECK_HOST_CONTACT = {"constant": "check_host_contact",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_host_contact}
        self.CHECK_HOST_LOCATION = {"constant": "check_host_location",
                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                    "link": self.link.check_host_location}
        self.CHECK_HOST_NAME = {"constant": "check_host_name",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.check_host_name}
        self.CHECK_HOST_SYSTEM_ID = {"constant": "check_host_system_id",
                                     "tags": ["PARSE_SNMP"],
                                     "link": self.link.check_host_system_id}
        self.CHECK_PROMPT = {"constant": "check_prompt",
                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                             "link": self.link.check_prompt}
        self.CHECK_STATE_IQAGENT = {"constant": "check_state_iqagent",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_state_iqagent}
        self.CHECK_VERSION = {"constant": "check_version",
                              "tags": ["PARSE_CLI"],
                              "link": self.link.check_version}
