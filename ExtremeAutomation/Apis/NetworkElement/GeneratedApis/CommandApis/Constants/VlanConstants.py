"""
This class outlines all the constants for the vlan API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VlanConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VlanConstants(ApiConstants):
    def __init__(self):
        super(VlanConstants, self).__init__()
        self.CLEAR_DESCRIPTION = {"constant": "clear_description",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_description}
        self.CLEAR_EGRESS = {"constant": "clear_egress",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.clear_egress}
        self.CLEAR_EGRESS_TYPE = {"constant": "clear_egress_type",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_egress_type}
        self.CLEAR_ISID = {"constant": "clear_isid",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.clear_isid}
        self.CLEAR_MEMBER = {"constant": "clear_member",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.clear_member}
        self.CLEAR_NAME = {"constant": "clear_name",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.clear_name}
        self.CLEAR_NSI = {"constant": "clear_nsi",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.clear_nsi}
        self.CLEAR_PORT_ENCAPSULATION_DOT1Q = {"constant": "clear_port_encapsulation_dot1q",
                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                               "link": self.link.clear_port_encapsulation_dot1q}
        self.CLEAR_PVID = {"constant": "clear_pvid",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.clear_pvid}
        self.CLEAR_VMAN_EGRESS = {"constant": "clear_vman_egress",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_vman_egress}
        self.CREATE_SPBM = {"constant": "create_spbm",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.create_spbm}
        self.CREATE_VLAN = {"constant": "create_vlan",
                            "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                            "link": self.link.create_vlan}
        self.CREATE_VLAN_WITH_NAME = {"constant": "create_vlan_with_name",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.create_vlan_with_name}
        self.CREATE_VMAN = {"constant": "create_vman",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.create_vman}
        self.DELETE_VLAN = {"constant": "delete_vlan",
                            "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                            "link": self.link.delete_vlan}
        self.DELETE_VMAN = {"constant": "delete_vman",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.delete_vman}
        self.DISABLE_DYNAMIC_EGRESS = {"constant": "disable_dynamic_egress",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.disable_dynamic_egress}
        self.DISABLE_VLAN = {"constant": "disable_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_vlan}
        self.ENABLE_DYNAMIC_EGRESS = {"constant": "enable_dynamic_egress",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.enable_dynamic_egress}
        self.ENABLE_VLAN = {"constant": "enable_vlan",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_vlan}
        self.SET_DESCRIPTION = {"constant": "set_description",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_description}
        self.SET_EGRESS_FORBIDDEN = {"constant": "set_egress_forbidden",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_egress_forbidden}
        self.SET_EGRESS_TAGGED = {"constant": "set_egress_tagged",
                                  "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                  "link": self.link.set_egress_tagged}
        self.SET_EGRESS_UNTAGGED = {"constant": "set_egress_untagged",
                                    "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                    "link": self.link.set_egress_untagged}
        self.SET_ISID = {"constant": "set_isid",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.set_isid}
        self.SET_MEMBER = {"constant": "set_member",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.set_member}
        self.SET_NAME = {"constant": "set_name",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.set_name}
        self.SET_NSI = {"constant": "set_nsi",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.set_nsi}
        self.SET_PORT_ENCAPSULATION_DOT1Q = {"constant": "set_port_encapsulation_dot1q",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.set_port_encapsulation_dot1q}
        self.SET_PVID = {"constant": "set_pvid",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_pvid}
        self.SET_VMAN_EGRESS_TAGGED = {"constant": "set_vman_egress_tagged",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_vman_egress_tagged}
        self.SET_VMAN_EGRESS_UNTAGGED = {"constant": "set_vman_egress_untagged",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_vman_egress_untagged}
        self.SHOW_ALL_INFO = {"constant": "show_all_info",
                              "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                              "link": self.link.show_all_info}
        self.SHOW_ALL_VMAN_INFO = {"constant": "show_all_vman_info",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_all_vman_info}
        self.SHOW_DESCRIPTION = {"constant": "show_description",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_description}
        self.SHOW_FABRIC_ATTACH_ASSIGNMENTS = {"constant": "show_fabric_attach_assignments",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.show_fabric_attach_assignments}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_REST"],
                          "link": self.link.show_info}
        self.SHOW_ISID = {"constant": "show_isid",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_isid}
        self.SHOW_MEMBERS = {"constant": "show_members",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_members}
        self.SHOW_MEMBERS_PORT = {"constant": "show_members_port",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_members_port}
        self.SHOW_NAME = {"constant": "show_name",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_name}
        self.SHOW_NAMES = {"constant": "show_names",
                           "tags": ["COMMAND_SNMP"],
                           "link": self.link.show_names}
        self.SHOW_NSI = {"constant": "show_nsi",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_nsi}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_port}
        self.SHOW_PORT_EGRESS = {"constant": "show_port_egress",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_port_egress}
        self.SHOW_PVID = {"constant": "show_pvid",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_pvid}
        self.SHOW_STATIC = {"constant": "show_static",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_static}
        self.SHOW_STATUS = {"constant": "show_status",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_status}
        self.SHOW_VMAN_INFO = {"constant": "show_vman_info",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_vman_info}
