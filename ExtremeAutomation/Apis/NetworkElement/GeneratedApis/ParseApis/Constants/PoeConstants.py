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
        self.CHECK_POE_INLINE_POWER = {"constant": "check_poe_inline_power",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_poe_inline_power}
        self.CHECK_POE_INLINE_POWER_CONFIG_PORT = {"constant": "check_poe_inline_power_config_port",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_poe_inline_power_config_port}
        self.CHECK_POE_INLINE_POWER_DISABLED = {"constant": "check_poe_inline_power_disabled",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_poe_inline_power_disabled}
        self.CHECK_POE_INLINE_POWER_DISCONNECT_DENY_PORT = {"constant": "check_poe_inline_power_disconnect_deny_port",
                                                            "tags": ["PARSE_CLI"],
                                                            "link": self.link.check_poe_inline_power_disconnect_deny_port}
        self.CHECK_POE_INLINE_POWER_DISCONNECT_LOWEST_PRIORITY = {"constant": "check_poe_inline_power_disconnect_lowest_priority",
                                                                  "tags": ["PARSE_CLI"],
                                                                  "link": self.link.check_poe_inline_power_disconnect_lowest_priority}
        self.CHECK_POE_INLINE_POWER_DISCONNECT_UNCONFIGURE = {"constant": "check_poe_inline_power_disconnect_unconfigure",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.check_poe_inline_power_disconnect_unconfigure}
        self.CHECK_POE_INLINE_POWER_ENABLED = {"constant": "check_poe_inline_power_enabled",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_poe_inline_power_enabled}
        self.CHECK_POE_INLINE_POWER_LABEL = {"constant": "check_poe_inline_power_label",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_poe_inline_power_label}
        self.CHECK_POE_INLINE_POWER_OPERATOR_LIMIT = {"constant": "check_poe_inline_power_operator_limit",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_poe_inline_power_operator_limit}
        self.CHECK_POE_INLINE_POWER_PORT_INFO = {"constant": "check_poe_inline_power_port_info",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_poe_inline_power_port_info}
        self.CHECK_POE_MAIN_AVAILABLE_POWER = {"constant": "check_poe_main_available_power",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_poe_main_available_power}
        self.CHECK_POE_MAIN_CONSUMPTION_POWER = {"constant": "check_poe_main_consumption_power",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_poe_main_consumption_power}
        self.CHECK_POE_MAIN_OPERATIONAL_STATUS = {"constant": "check_poe_main_operational_status",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_poe_main_operational_status}
        self.CHECK_POE_PORT_DETECTION_STATUS = {"constant": "check_poe_port_detection_status",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_poe_port_detection_status}
        self.CHECK_POE_PORT_DETECT_TYPE = {"constant": "check_poe_port_detect_type",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_poe_port_detect_type}
        self.CHECK_POE_PORT_MEASURED_CURRENT = {"constant": "check_poe_port_measured_current",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_poe_port_measured_current}
        self.CHECK_POE_PORT_MEASURED_POWER = {"constant": "check_poe_port_measured_power",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_poe_port_measured_power}
        self.CHECK_POE_PORT_MEASURED_VOLTAGE = {"constant": "check_poe_port_measured_voltage",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_poe_port_measured_voltage}
        self.CHECK_POE_PORT_POWER_CLASSIFICATION = {"constant": "check_poe_port_power_classification",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_poe_port_power_classification}
        self.CHECK_POE_PORT_POWER_LIMIT = {"constant": "check_poe_port_power_limit",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_poe_port_power_limit}
        self.CHECK_POE_PORT_POWER_PAIRS_ON_SIGNAL = {"constant": "check_poe_port_power_pairs_on_signal",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_poe_port_power_pairs_on_signal}
        self.CHECK_POE_PORT_POWER_PAIRS_ON_SPARE = {"constant": "check_poe_port_power_pairs_on_spare",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_poe_port_power_pairs_on_spare}
        self.CHECK_POE_PORT_POWER_PRIORITY = {"constant": "check_poe_port_power_priority",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_poe_port_power_priority}
        self.CHECK_POE_PORT_STATE = {"constant": "check_poe_port_state",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_poe_port_state}
        self.CHECK_POE_POWER_USAGE_THRESHOLD = {"constant": "check_poe_power_usage_threshold",
                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                "link": self.link.check_poe_power_usage_threshold}
