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
        self.CLEAR_ENCAPSULATION_DOT1Q = {"constant": "clear_encapsulation_dot1q",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_encapsulation_dot1q}
        self.CLEAR_PORT_MEMBER = {"constant": "clear_port_member",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.clear_port_member}
        self.CREATE_ID = {"constant": "create_id",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.create_id}
        self.DELETE_ID = {"constant": "delete_id",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.delete_id}
        self.DISABLE_FLEX_UNI = {"constant": "disable_flex_uni",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.disable_flex_uni}
        self.DISABLE_LACP = {"constant": "disable_lacp",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_lacp}
        self.ENABLE_FLEX_UNI = {"constant": "enable_flex_uni",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.enable_flex_uni}
        self.ENABLE_LACP = {"constant": "enable_lacp",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_lacp}
        self.SET_ENCAPSULATION_DOT1Q = {"constant": "set_encapsulation_dot1q",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_encapsulation_dot1q}
        self.SET_PORT_MEMBER = {"constant": "set_port_member",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.set_port_member}
        self.SET_TYPE_NORMAL_MLT = {"constant": "set_type_normal_mlt",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_type_normal_mlt}
        self.SET_TYPE_SPLIT_MLT = {"constant": "set_type_split_mlt",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_type_split_mlt}
        self.SHOW_ADMIN_TYPE = {"constant": "show_admin_type",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.show_admin_type}
        self.SHOW_ENCAPSULATION = {"constant": "show_encapsulation",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_encapsulation}
        self.SHOW_FLEX_UNI_STATUS = {"constant": "show_flex_uni_status",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_flex_uni_status}
        self.SHOW_ID = {"constant": "show_id",
                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                        "link": self.link.show_id}
        self.SHOW_LACP_ADMIN_STATUS = {"constant": "show_lacp_admin_status",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_lacp_admin_status}
        self.SHOW_LACP_OPER_STATUS = {"constant": "show_lacp_oper_status",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_lacp_oper_status}
        self.SHOW_LOGICAL_INDEX = {"constant": "show_logical_index",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.show_logical_index}
        self.SHOW_PORTS = {"constant": "show_ports",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_ports}
        self.SHOW_RUNNING_TYPE = {"constant": "show_running_type",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_running_type}
