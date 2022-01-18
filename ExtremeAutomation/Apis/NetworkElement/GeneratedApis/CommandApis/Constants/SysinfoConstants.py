"""
This class outlines all the constants for the sysinfo API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SysinfoConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SysinfoConstants(ApiConstants):
    def __init__(self):
        super(SysinfoConstants, self).__init__()
        self.SHOW_CORE_FILES = {"constant": "show_core_files",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_core_files}
        self.SHOW_HARDWARE_SUMMARY = {"constant": "show_hardware_summary",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_hardware_summary}
        self.SHOW_SLOT_FILES = {"constant": "show_slot_files",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_slot_files}
        self.SHOW_SYSTEM_CPU_USAGE = {"constant": "show_system_cpu_usage",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_system_cpu_usage}
        self.SHOW_SYSTEM_INFO = {"constant": "show_system_info",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_system_info}
        self.SHOW_SYSTEM_SLOT_INFO = {"constant": "show_system_slot_info",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_system_slot_info}
