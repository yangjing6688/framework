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
        self.BULKWALK_SYSTEM = {"constant": "bulkwalk_system",
                                "tags": ["COMMAND_SNMP"],
                                "link": self.link.bulkwalk_system}
        self.GETNEXT_SYSTEM_LOCATION_DOT_ZERO = {"constant": "getnext_system_location_dot_zero",
                                                 "tags": ["COMMAND_SNMP"],
                                                 "link": self.link.getnext_system_location_dot_zero}
        self.SHOW_CHASSIS_INFO = {"constant": "show_chassis_info",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_chassis_info}
        self.SHOW_LICENSE_INFO = {"constant": "show_license_info",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_license_info}
        self.SHOW_PORT_INFO = {"constant": "show_port_info",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_port_info}
        self.SHOW_STACKING_INFO = {"constant": "show_stacking_info",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_stacking_info}
        self.SHOW_STACK_INFO = {"constant": "show_stack_info",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_stack_info}
        self.SHOW_SYSTEM_INFO = {"constant": "show_system_info",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_system_info}
        self.SHOW_UNIT_INFO = {"constant": "show_unit_info",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_unit_info}
        self.WALK_SYSTEM = {"constant": "walk_system",
                            "tags": ["COMMAND_SNMP"],
                            "link": self.link.walk_system}
