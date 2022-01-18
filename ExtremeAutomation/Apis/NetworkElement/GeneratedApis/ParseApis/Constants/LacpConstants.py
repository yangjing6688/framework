"""
This class outlines all the constants for the lacp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(LacpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class LacpConstants(ApiConstants):
    def __init__(self):
        super(LacpConstants, self).__init__()
        self.CHECK_MLT_LACP_ACTOR_ADMIN_KEY = {"constant": "check_mlt_lacp_actor_admin_key",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_mlt_lacp_actor_admin_key}
        self.CHECK_MLT_LACP_ACTOR_OPER_KEY = {"constant": "check_mlt_lacp_actor_oper_key",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_mlt_lacp_actor_oper_key}
        self.CHECK_MLT_LACP_ACTOR_SYSTEM_PRIORITY = {"constant": "check_mlt_lacp_actor_system_priority",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_mlt_lacp_actor_system_priority}
        self.CHECK_PORT_IS_IN_LAG = {"constant": "check_port_is_in_lag",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_port_is_in_lag}
        self.VERIFY_LACP_ENABLED = {"constant": "verify_lacp_enabled",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.verify_lacp_enabled}
