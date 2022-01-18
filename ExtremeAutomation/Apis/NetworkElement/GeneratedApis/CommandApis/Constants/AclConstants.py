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
        self.CLEAR_ACE_ETHERNET_ETHERTYPE = {"constant": "clear_ace_ethernet_ethertype",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.clear_ace_ethernet_ethertype}
        self.CLEAR_PORT = {"constant": "clear_port",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.clear_port}
        self.CLEAR_VLAN = {"constant": "clear_vlan",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.clear_vlan}
        self.CREATE_ACE_INDEX = {"constant": "create_ace_index",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.create_ace_index}
        self.CREATE_IPV4 = {"constant": "create_ipv4",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.create_ipv4}
        self.CREATE_IPV6 = {"constant": "create_ipv6",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.create_ipv6}
        self.DELETE_ACE_INDEX = {"constant": "delete_ace_index",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.delete_ace_index}
        self.DELETE_LIST = {"constant": "delete_list",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.delete_list}
        self.DISABLE_ACE = {"constant": "disable_ace",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.disable_ace}
        self.DISABLE_LIST = {"constant": "disable_list",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_list}
        self.ENABLE_ACE = {"constant": "enable_ace",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.enable_ace}
        self.ENABLE_LIST = {"constant": "enable_list",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_list}
        self.SET_ACE_ACTION = {"constant": "set_ace_action",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.set_ace_action}
        self.SET_ACE_ETHERNET_ETHERTYPE = {"constant": "set_ace_ethernet_ethertype",
                                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                           "link": self.link.set_ace_ethernet_ethertype}
        self.SET_ACE_NAME = {"constant": "set_ace_name",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.set_ace_name}
        self.SET_DEFAULT_ACTION = {"constant": "set_default_action",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.set_default_action}
        self.SET_NAME = {"constant": "set_name",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.set_name}
        self.SET_PORT = {"constant": "set_port",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.set_port}
        self.SET_STANDARD_RULE = {"constant": "set_standard_rule",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_standard_rule}
        self.SET_VLAN = {"constant": "set_vlan",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.set_vlan}
        self.SHOW_ACE_INDEX_ACTION = {"constant": "show_ace_index_action",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_ace_index_action}
        self.SHOW_ACE_INDEX_ETHERNET_ETHERTYPE = {"constant": "show_ace_index_ethernet_ethertype",
                                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                  "link": self.link.show_ace_index_ethernet_ethertype}
        self.SHOW_ACE_INDEX_NAME = {"constant": "show_ace_index_name",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_ace_index_name}
        self.SHOW_ACE_INDEX_OPER_STATE = {"constant": "show_ace_index_oper_state",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.show_ace_index_oper_state}
        self.SHOW_ALL_ACES = {"constant": "show_all_aces",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.show_all_aces}
        self.SHOW_ALL_IPV4 = {"constant": "show_all_ipv4",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.show_all_ipv4}
        self.SHOW_ALL_IPV6 = {"constant": "show_all_ipv6",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.show_all_ipv6}
        self.SHOW_ID = {"constant": "show_id",
                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                        "link": self.link.show_id}
        self.SHOW_PORTS = {"constant": "show_ports",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_ports}
        self.SHOW_VLANS = {"constant": "show_vlans",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_vlans}
