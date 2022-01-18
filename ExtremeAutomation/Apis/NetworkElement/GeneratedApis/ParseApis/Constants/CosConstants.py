"""
This class outlines all the constants for the cos API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CosConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CosConstants(ApiConstants):
    def __init__(self):
        super(CosConstants, self).__init__()
        self.CHECK_COS_PORT_RESOURCE = {"constant": "check_cos_port_resource",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_cos_port_resource}
        self.CHECK_COS_REFERENCE = {"constant": "check_cos_reference",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_cos_reference}
        self.CHECK_COS_SETTINGS = {"constant": "check_cos_settings",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_cos_settings}
        self.CHECK_COS_STATE = {"constant": "check_cos_state",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_cos_state}
        self.CHECK_PORT_GROUP_EXISTS = {"constant": "check_port_group_exists",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_port_group_exists}
        self.CHECK_PORT_GROUP_PORTS = {"constant": "check_port_group_ports",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_port_group_ports}
        self.CHECK_PORT_QOS_PROFILE = {"constant": "check_port_qos_profile",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_port_qos_profile}
        self.CHECK_QOS_PROFILE_EXISTS = {"constant": "check_qos_profile_exists",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_qos_profile_exists}
        self.CHECK_QOS_SCHEDULER_MODE = {"constant": "check_qos_scheduler_mode",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_qos_scheduler_mode}
        self.CHECK_TXQ_WEIGHTS = {"constant": "check_txq_weights",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_txq_weights}
        self.VERIFY_PORT_PRIORITY = {"constant": "verify_port_priority",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.verify_port_priority}
