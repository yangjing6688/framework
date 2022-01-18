"""
This class outlines all the constants for the poe API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PoeConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PoeConstants(ApiConstants):
    def __init__(self):
        super(PoeConstants, self).__init__()
        self.CLEAR_INLINE_POWER_DISCONNECT = {"constant": "clear_inline_power_disconnect",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.clear_inline_power_disconnect}
        self.DISABLE_INLINE_POWER = {"constant": "disable_inline_power",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.disable_inline_power}
        self.DISABLE_INLINE_POWER_LEGACY = {"constant": "disable_inline_power_legacy",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_inline_power_legacy}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_port}
        self.ENABLE_INLINE_POWER = {"constant": "enable_inline_power",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_inline_power}
        self.ENABLE_INLINE_POWER_LEGACY = {"constant": "enable_inline_power_legacy",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_inline_power_legacy}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_port}
        self.SET_INLINE_POWER_DISCONNECT_DENY_PORT = {"constant": "set_inline_power_disconnect_deny_port",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.set_inline_power_disconnect_deny_port}
        self.SET_INLINE_POWER_DISCONNECT_LOWEST_PRIORITY = {"constant": "set_inline_power_disconnect_lowest_priority",
                                                            "tags": ["COMMAND_CLI"],
                                                            "link": self.link.set_inline_power_disconnect_lowest_priority}
        self.SET_INLINE_POWER_LABEL = {"constant": "set_inline_power_label",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_inline_power_label}
        self.SET_PORT_DETECT_TYPE = {"constant": "set_port_detect_type",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.set_port_detect_type}
        self.SET_PORT_POWER_LIMIT = {"constant": "set_port_power_limit",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.set_port_power_limit}
        self.SET_PORT_POWER_PRIORITY = {"constant": "set_port_power_priority",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_port_power_priority}
        self.SET_POWER_USAGE_THRESHOLD = {"constant": "set_power_usage_threshold",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.set_power_usage_threshold}
        self.SHOW_GLOBAL_STATUS = {"constant": "show_global_status",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_global_status}
        self.SHOW_INLINE_POWER = {"constant": "show_inline_power",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_inline_power}
        self.SHOW_INLINE_POWER_INFO_PORT = {"constant": "show_inline_power_info_port",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_inline_power_info_port}
        self.SHOW_INLINE_POWER_LABEL = {"constant": "show_inline_power_label",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_inline_power_label}
        self.SHOW_INLINE_POWER_LEGACY = {"constant": "show_inline_power_legacy",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_inline_power_legacy}
        self.SHOW_INLINE_POWER_OPERATOR_LIMIT = {"constant": "show_inline_power_operator_limit",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.show_inline_power_operator_limit}
        self.SHOW_PORT_DETECTION_STATUS = {"constant": "show_port_detection_status",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.show_port_detection_status}
        self.SHOW_PORT_DETECT_TYPE = {"constant": "show_port_detect_type",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_port_detect_type}
        self.SHOW_PORT_MEASUREMENTS = {"constant": "show_port_measurements",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_port_measurements}
        self.SHOW_PORT_POWER_CLASSIFICATION = {"constant": "show_port_power_classification",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.show_port_power_classification}
        self.SHOW_PORT_POWER_LIMIT = {"constant": "show_port_power_limit",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_port_power_limit}
        self.SHOW_PORT_POWER_PAIRS = {"constant": "show_port_power_pairs",
                                      "tags": ["COMMAND_SNMP"],
                                      "link": self.link.show_port_power_pairs}
        self.SHOW_PORT_POWER_PRIORITY = {"constant": "show_port_power_priority",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.show_port_power_priority}
        self.SHOW_PORT_STATUS = {"constant": "show_port_status",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_port_status}
        self.SHOW_POWER_USAGE_THRESHOLD = {"constant": "show_power_usage_threshold",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.show_power_usage_threshold}
