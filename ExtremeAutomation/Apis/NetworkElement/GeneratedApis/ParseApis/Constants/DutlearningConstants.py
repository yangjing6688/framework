"""
This class outlines all the constants for the dutlearning API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DutlearningConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DutlearningConstants(ApiConstants):
    def __init__(self):
        super(DutlearningConstants, self).__init__()
        self.CHECK_BACKUP_SLOT = {"constant": "check_backup_slot",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_backup_slot}
        self.GATHER_CHASSIS_INFO = {"constant": "gather_chassis_info",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.gather_chassis_info}
        self.GATHER_LICENSE_INFO = {"constant": "gather_license_info",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.gather_license_info}
        self.GATHER_PORT_INFO = {"constant": "gather_port_info",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.gather_port_info}
        self.GATHER_SYSTEM_INFO = {"constant": "gather_system_info",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.gather_system_info}
        self.GATHER_UNIT_INFO = {"constant": "gather_unit_info",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.gather_unit_info}
        self.GET_CHASSIS_SLOT_NUMBERS = {"constant": "get_chassis_slot_numbers",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.get_chassis_slot_numbers}
        self.GET_STACK_SLOT_NUMBERS = {"constant": "get_stack_slot_numbers",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.get_stack_slot_numbers}
        self.IS_CHASSIS = {"constant": "is_chassis",
                           "tags": ["PARSE_CLI"],
                           "link": self.link.is_chassis}
        self.IS_STACKED = {"constant": "is_stacked",
                           "tags": ["PARSE_CLI"],
                           "link": self.link.is_stacked}
        self.IS_STACK_IN_SYNC = {"constant": "is_stack_in_sync",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.is_stack_in_sync}
