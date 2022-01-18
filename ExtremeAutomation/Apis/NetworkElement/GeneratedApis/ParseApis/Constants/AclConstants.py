"""
This class outlines all the constants for the acl API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AclConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AclConstants(ApiConstants):
    def __init__(self):
        super(AclConstants, self).__init__()
        self.CHECK_ACE_EXISTS = {"constant": "check_ace_exists",
                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                 "link": self.link.check_ace_exists}
        self.CHECK_ACE_INDEX_ACTION = {"constant": "check_ace_index_action",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.check_ace_index_action}
        self.CHECK_ACE_INDEX_ETHERNET_ETHERTYPE = {"constant": "check_ace_index_ethernet_ethertype",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_ace_index_ethernet_ethertype}
        self.CHECK_ACE_INDEX_NAME = {"constant": "check_ace_index_name",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_ace_index_name}
        self.CHECK_ACE_INDEX_OPER_STATE = {"constant": "check_ace_index_oper_state",
                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                           "link": self.link.check_ace_index_oper_state}
        self.CHECK_ACL_ACTION = {"constant": "check_acl_action",
                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                 "link": self.link.check_acl_action}
        self.CHECK_ACL_ENABLE = {"constant": "check_acl_enable",
                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                 "link": self.link.check_acl_enable}
        self.CHECK_ACL_EXISTS = {"constant": "check_acl_exists",
                                 "tags": ["PARSE_SNMP"],
                                 "link": self.link.check_acl_exists}
        self.CHECK_ACL_NAME = {"constant": "check_acl_name",
                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                               "link": self.link.check_acl_name}
        self.CHECK_ACL_PORT = {"constant": "check_acl_port",
                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                               "link": self.link.check_acl_port}
        self.CHECK_ACL_VLAN = {"constant": "check_acl_vlan",
                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                               "link": self.link.check_acl_vlan}
        self.CHECK_IPV4_ACL_EXISTS = {"constant": "check_ipv4_acl_exists",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_ipv4_acl_exists}
        self.CHECK_IPV6_ACL_EXISTS = {"constant": "check_ipv6_acl_exists",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_ipv6_acl_exists}
