"""
This class outlines all the constants for the snmp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SnmpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SnmpConstants(ApiConstants):
    def __init__(self):
        super(SnmpConstants, self).__init__()
        self.CHECK_SNMP_ACCESS = {"constant": "check_snmp_access",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_snmp_access}
        self.CHECK_SNMP_COMMUNITY = {"constant": "check_snmp_community",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_snmp_community}
        self.CHECK_SNMP_ENABLE_AUTHENTICATION_TRAP = {"constant": "check_snmp_enable_authentication_trap",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_snmp_enable_authentication_trap}
        self.CHECK_SNMP_ENABLE_SAME_SNMP_AND_IP_SENDER_FLAG = {"constant": "check_snmp_enable_same_snmp_and_ip_sender_flag",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_snmp_enable_same_snmp_and_ip_sender_flag}
        self.CHECK_SNMP_ENABLE_SAME_SNMP_TRAP_SENDER_IP = {"constant": "check_snmp_enable_same_snmp_trap_sender_ip",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_snmp_enable_same_snmp_trap_sender_ip}
        self.CHECK_SNMP_GROUP = {"constant": "check_snmp_group",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.check_snmp_group}
        self.CHECK_SNMP_NOTIFY_FILTER = {"constant": "check_snmp_notify_filter",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_snmp_notify_filter}
        self.CHECK_SNMP_USER = {"constant": "check_snmp_user",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_snmp_user}
        self.CHECK_SNMP_USER_ENGINE_ID = {"constant": "check_snmp_user_engine_id",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_snmp_user_engine_id}
        self.CHECK_SNMP_V1_TRAP_SERVER = {"constant": "check_snmp_v1_trap_server",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_snmp_v1_trap_server}
        self.CHECK_SNMP_V2C_INFORM_SERVER = {"constant": "check_snmp_v2c_inform_server",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_snmp_v2c_inform_server}
        self.CHECK_SNMP_V2C_TRAP_SERVER = {"constant": "check_snmp_v2c_trap_server",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_snmp_v2c_trap_server}
        self.CHECK_SNMP_V3_INFORM_SERVER = {"constant": "check_snmp_v3_inform_server",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_snmp_v3_inform_server}
        self.CHECK_SNMP_V3_TRAP_SERVER = {"constant": "check_snmp_v3_trap_server",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_snmp_v3_trap_server}
        self.CHECK_SNMP_VIEW = {"constant": "check_snmp_view",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_snmp_view}
        self.VERIFY_SNMP_ENABLED = {"constant": "verify_snmp_enabled",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.verify_snmp_enabled}
