"""
This class outlines all the constants for the ospf API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(OspfConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class OspfConstants(ApiConstants):
    def __init__(self):
        super(OspfConstants, self).__init__()
        self.VERIFY_OSPF_DISABLED_ON_INTERFACE = {"constant": "verify_ospf_disabled_on_interface",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.verify_ospf_disabled_on_interface}
        self.VERIFY_OSPF_DISABLED_ON_VLAN = {"constant": "verify_ospf_disabled_on_vlan",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.verify_ospf_disabled_on_vlan}
        self.VERIFY_OSPF_ENABLED_ON_INTERFACE = {"constant": "verify_ospf_enabled_on_interface",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.verify_ospf_enabled_on_interface}
        self.VERIFY_OSPF_ENABLED_ON_VLAN = {"constant": "verify_ospf_enabled_on_vlan",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.verify_ospf_enabled_on_vlan}
        self.VERIFY_OSPF_GLOBALLY_DISABLED = {"constant": "verify_ospf_globally_disabled",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.verify_ospf_globally_disabled}
        self.VERIFY_OSPF_GLOBALLY_ENABLED = {"constant": "verify_ospf_globally_enabled",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.verify_ospf_globally_enabled}
        self.VERIFY_OSPF_INTERFACE_AUTHENTICATION = {"constant": "verify_ospf_interface_authentication",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_ospf_interface_authentication}
        self.VERIFY_OSPF_INTERFACE_AUTHENTICATION_NONE = {"constant": "verify_ospf_interface_authentication_none",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.verify_ospf_interface_authentication_none}
        self.VERIFY_OSPF_METRIC_TABLE_100G = {"constant": "verify_ospf_metric_table_100g",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_ospf_metric_table_100g}
        self.VERIFY_OSPF_METRIC_TABLE_100M = {"constant": "verify_ospf_metric_table_100m",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_ospf_metric_table_100m}
        self.VERIFY_OSPF_METRIC_TABLE_10G = {"constant": "verify_ospf_metric_table_10g",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_ospf_metric_table_10g}
        self.VERIFY_OSPF_METRIC_TABLE_10M = {"constant": "verify_ospf_metric_table_10m",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_ospf_metric_table_10m}
        self.VERIFY_OSPF_METRIC_TABLE_1G = {"constant": "verify_ospf_metric_table_1g",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.verify_ospf_metric_table_1g}
        self.VERIFY_OSPF_METRIC_TABLE_25G = {"constant": "verify_ospf_metric_table_25g",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_ospf_metric_table_25g}
        self.VERIFY_OSPF_METRIC_TABLE_2_5G = {"constant": "verify_ospf_metric_table_2_5g",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_ospf_metric_table_2_5g}
        self.VERIFY_OSPF_METRIC_TABLE_40G = {"constant": "verify_ospf_metric_table_40g",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_ospf_metric_table_40g}
        self.VERIFY_OSPF_METRIC_TABLE_50G = {"constant": "verify_ospf_metric_table_50g",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_ospf_metric_table_50g}
        self.VERIFY_OSPF_METRIC_TABLE_5G = {"constant": "verify_ospf_metric_table_5g",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.verify_ospf_metric_table_5g}
        self.VERIFY_OSPF_NEIGHBOR_ADJACENCY_FULL = {"constant": "verify_ospf_neighbor_adjacency_full",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.verify_ospf_neighbor_adjacency_full}
        self.VERIFY_OSPF_NEIGHBOR_EXISTS = {"constant": "verify_ospf_neighbor_exists",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.verify_ospf_neighbor_exists}
        self.VERIFY_OSPF_ROUTER_ID = {"constant": "verify_ospf_router_id",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.verify_ospf_router_id}
        self.VERIFY_OSPF_ROUTER_ID_IS_REMOVED = {"constant": "verify_ospf_router_id_is_removed",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.verify_ospf_router_id_is_removed}
