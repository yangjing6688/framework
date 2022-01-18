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
        self.CHECK_FORBIDDEN_PORTS = {"constant": "check_forbidden_ports",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_forbidden_ports}
        self.CHECK_PORT_IS_MEMBER_OF_DEFAULT_VLAN = {"constant": "check_port_is_member_of_default_vlan",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_port_is_member_of_default_vlan}
        self.CHECK_PORT_IS_MEMBER_OF_VLAN = {"constant": "check_port_is_member_of_vlan",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_port_is_member_of_vlan}
        self.CHECK_PORT_PVID = {"constant": "check_port_pvid",
                                "tags": ["PARSE_CLI", "PARSE_REST"],
                                "link": self.link.check_port_pvid}
        self.CHECK_STATIC_TAGGED_PORTS = {"constant": "check_static_tagged_ports",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_static_tagged_ports}
        self.CHECK_STATIC_UNTAGGED_PORTS = {"constant": "check_static_untagged_ports",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_static_untagged_ports}
        self.CHECK_TAGGED_OPERATIONAL_PORTS = {"constant": "check_tagged_operational_ports",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_tagged_operational_ports}
        self.CHECK_TAGGED_PORTS = {"constant": "check_tagged_ports",
                                   "tags": ["PARSE_CLI", "PARSE_REST"],
                                   "link": self.link.check_tagged_ports}
        self.CHECK_UNTAGGED_OPERATIONAL_PORTS = {"constant": "check_untagged_operational_ports",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_untagged_operational_ports}
        self.CHECK_UNTAGGED_PORTS = {"constant": "check_untagged_ports",
                                     "tags": ["PARSE_CLI", "PARSE_REST"],
                                     "link": self.link.check_untagged_ports}
        self.CHECK_VLAN_DESCRIPTION = {"constant": "check_vlan_description",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_vlan_description}
        self.CHECK_VLAN_EXISTS = {"constant": "check_vlan_exists",
                                  "tags": ["PARSE_CLI", "PARSE_REST", "PARSE_SNMP"],
                                  "link": self.link.check_vlan_exists}
        self.CHECK_VLAN_FABRIC_ATTACH_ASSIGNMENTS_ISID = {"constant": "check_vlan_fabric_attach_assignments_isid",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_vlan_fabric_attach_assignments_isid}
        self.CHECK_VLAN_FABRIC_ATTACH_ASSIGNMENTS_PORT = {"constant": "check_vlan_fabric_attach_assignments_port",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_vlan_fabric_attach_assignments_port}
        self.CHECK_VLAN_FABRIC_ATTACH_ASSIGNMENTS_STATUS = {"constant": "check_vlan_fabric_attach_assignments_status",
                                                            "tags": ["PARSE_CLI"],
                                                            "link": self.link.check_vlan_fabric_attach_assignments_status}
        self.CHECK_VLAN_FABRIC_ATTACH_ASSIGNMENTS_TYPE = {"constant": "check_vlan_fabric_attach_assignments_type",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_vlan_fabric_attach_assignments_type}
        self.CHECK_VLAN_FABRIC_ATTACH_ASSIGNMENTS_VLAN = {"constant": "check_vlan_fabric_attach_assignments_vlan",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_vlan_fabric_attach_assignments_vlan}
        self.CHECK_VLAN_FABRIC_ATTACH_ASSIGNMENTS_VLAN_NAME = {"constant": "check_vlan_fabric_attach_assignments_vlan_name",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_vlan_fabric_attach_assignments_vlan_name}
        self.CHECK_VLAN_ISID = {"constant": "check_vlan_isid",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.check_vlan_isid}
        self.CHECK_VLAN_NAME = {"constant": "check_vlan_name",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.check_vlan_name}
        self.CHECK_VLAN_NAME_ID = {"constant": "check_vlan_name_id",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_vlan_name_id}
        self.CHECK_VLAN_NSI = {"constant": "check_vlan_nsi",
                               "tags": ["PARSE_CLI"],
                               "link": self.link.check_vlan_nsi}
        self.CHECK_VLAN_ON_PORT_TAGGED_EGRESS = {"constant": "check_vlan_on_port_tagged_egress",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_vlan_on_port_tagged_egress}
        self.CHECK_VLAN_ON_PORT_UNTAGGED_EGRESS = {"constant": "check_vlan_on_port_untagged_egress",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_vlan_on_port_untagged_egress}
        self.CHECK_VLAN_STATE = {"constant": "check_vlan_state",
                                 "tags": ["PARSE_CLI", "PARSE_REST"],
                                 "link": self.link.check_vlan_state}
        self.CHECK_VMAN_EXISTS = {"constant": "check_vman_exists",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_vman_exists}
        self.CHECK_VMAN_TAGGED_PORTS = {"constant": "check_vman_tagged_ports",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_vman_tagged_ports}
        self.CHECK_VMAN_UNTAGGED_PORTS = {"constant": "check_vman_untagged_ports",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_vman_untagged_ports}
        self.GET_VLAN_IPV4 = {"constant": "get_vlan_ipv4",
                              "tags": ["PARSE_CLI", "PARSE_REST"],
                              "link": self.link.get_vlan_ipv4}
        self.GET_VLAN_TAG = {"constant": "get_vlan_tag",
                             "tags": ["PARSE_CLI", "PARSE_REST"],
                             "link": self.link.get_vlan_tag}
        self.VERIFY_PORT_ENCAPSULATION_DOT1Q_IS_SET = {"constant": "verify_port_encapsulation_dot1q_is_set",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.verify_port_encapsulation_dot1q_is_set}
