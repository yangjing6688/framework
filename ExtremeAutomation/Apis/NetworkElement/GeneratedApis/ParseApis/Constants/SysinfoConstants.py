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
        self.CHECK_FIRMWARE_VERSION = {"constant": "check_firmware_version",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_firmware_version}
        self.CHECK_FOR_CORES_DIR = {"constant": "check_for_cores_dir",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_for_cores_dir}
        self.CHECK_INSTALLED_XMODS = {"constant": "check_installed_xmods",
                                      "tags": ["PARSE_CLI", "PARSE_REST"],
                                      "link": self.link.check_installed_xmods}
        self.GET_ALL_SLOT_NUMBERS = {"constant": "get_all_slot_numbers",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.get_all_slot_numbers}
        self.GET_COREFILE_LIST = {"constant": "get_corefile_list",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.get_corefile_list}
        self.GET_CPU_USAGE = {"constant": "get_cpu_usage",
                              "tags": ["PARSE_CLI"],
                              "link": self.link.get_cpu_usage}
        self.GET_FIRMWARE_VERSION = {"constant": "get_firmware_version",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.get_firmware_version}
        self.GET_SLOT_UPTIME = {"constant": "get_slot_uptime",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.get_slot_uptime}
        self.GET_SYSTEM_UPTIME = {"constant": "get_system_uptime",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.get_system_uptime}
        self.STORE_FIRMWARE_VERSION = {"constant": "store_firmware_version",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.store_firmware_version}
        self.STORE_MODEL = {"constant": "store_model",
                            "tags": ["PARSE_CLI"],
                            "link": self.link.store_model}
