"""
This class outlines all the constants for the mlt API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MltConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MltConstants(ApiConstants):
    def __init__(self):
        super(MltConstants, self).__init__()
        self.CHECK_MLT_ADMIN_TYPE_NORMAL = {"constant": "check_mlt_admin_type_normal",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_mlt_admin_type_normal}
        self.CHECK_MLT_ADMIN_TYPE_SPLIT = {"constant": "check_mlt_admin_type_split",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_mlt_admin_type_split}
        self.CHECK_MLT_EXISTS = {"constant": "check_mlt_exists",
                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                 "link": self.link.check_mlt_exists}
        self.CHECK_MLT_FLEX_UNI_STATUS = {"constant": "check_mlt_flex_uni_status",
                                          "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                          "link": self.link.check_mlt_flex_uni_status}
        self.CHECK_MLT_LACP_ACTOR_ADMIN_KEY = {"constant": "check_mlt_lacp_actor_admin_key",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_mlt_lacp_actor_admin_key}
        self.CHECK_MLT_LACP_ACTOR_OPER_KEY = {"constant": "check_mlt_lacp_actor_oper_key",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_mlt_lacp_actor_oper_key}
        self.CHECK_MLT_LACP_ACTOR_SYSTEM_PRIORITY = {"constant": "check_mlt_lacp_actor_system_priority",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_mlt_lacp_actor_system_priority}
        self.CHECK_MLT_LACP_ADMIN_STATUS = {"constant": "check_mlt_lacp_admin_status",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_mlt_lacp_admin_status}
        self.CHECK_MLT_LACP_OPER_STATUS = {"constant": "check_mlt_lacp_oper_status",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_mlt_lacp_oper_status}
        self.CHECK_MLT_PORT = {"constant": "check_mlt_port",
                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                               "link": self.link.check_mlt_port}
        self.CHECK_MLT_RUNNING_TYPE_NORMAL = {"constant": "check_mlt_running_type_normal",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_mlt_running_type_normal}
        self.CHECK_MLT_RUNNING_TYPE_SPLIT = {"constant": "check_mlt_running_type_split",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_mlt_running_type_split}
        self.CHECK_MLT_TRUNKING = {"constant": "check_mlt_trunking",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_mlt_trunking}
