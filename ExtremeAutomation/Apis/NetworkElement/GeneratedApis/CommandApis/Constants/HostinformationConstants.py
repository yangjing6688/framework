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
        self.CLEAR_PROMPT = {"constant": "clear_prompt",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.clear_prompt}
        self.SET_HOST_CONTACT = {"constant": "set_host_contact",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.set_host_contact}
        self.SET_HOST_LOCATION = {"constant": "set_host_location",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.set_host_location}
        self.SET_HOST_NAME = {"constant": "set_host_name",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_host_name}
        self.SET_PROMPT = {"constant": "set_prompt",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.set_prompt}
        self.SHOW_APP_IQAGENT = {"constant": "show_app_iqagent",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_app_iqagent}
        self.SHOW_HOST_CONTACT = {"constant": "show_host_contact",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_host_contact}
        self.SHOW_HOST_DESCRIPTION = {"constant": "show_host_description",
                                      "tags": ["COMMAND_SNMP"],
                                      "link": self.link.show_host_description}
        self.SHOW_HOST_LOCATION = {"constant": "show_host_location",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_host_location}
        self.SHOW_HOST_NAME = {"constant": "show_host_name",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.show_host_name}
        self.SHOW_HOST_OBJECT_ID = {"constant": "show_host_object_id",
                                    "tags": ["COMMAND_SNMP"],
                                    "link": self.link.show_host_object_id}
        self.SHOW_HOST_SERVICES = {"constant": "show_host_services",
                                   "tags": ["COMMAND_SNMP"],
                                   "link": self.link.show_host_services}
        self.SHOW_HOST_UPTIME = {"constant": "show_host_uptime",
                                 "tags": ["COMMAND_SNMP"],
                                 "link": self.link.show_host_uptime}
        self.SHOW_SYSTEM_NAME = {"constant": "show_system_name",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_system_name}
        self.SHOW_SYSTEM_SOFTWARE_VERSION = {"constant": "show_system_software_version",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_system_software_version}
