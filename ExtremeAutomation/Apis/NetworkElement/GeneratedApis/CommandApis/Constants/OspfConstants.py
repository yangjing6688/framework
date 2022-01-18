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
        self.CLEAR_ROUTER_ID = {"constant": "clear_router_id",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.clear_router_id}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_global}
        self.DISABLE_INTERFACE = {"constant": "disable_interface",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.disable_interface}
        self.DISABLE_VLAN = {"constant": "disable_vlan",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_vlan}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_global}
        self.ENABLE_INTERFACE = {"constant": "enable_interface",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.enable_interface}
        self.ENABLE_VLAN = {"constant": "enable_vlan",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_vlan}
        self.SET_ADD_VLAN = {"constant": "set_add_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_add_vlan}
        self.SET_DEL_VLAN = {"constant": "set_del_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_del_vlan}
        self.SET_METRIC_TABLE_100G = {"constant": "set_metric_table_100g",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_metric_table_100g}
        self.SET_METRIC_TABLE_100M = {"constant": "set_metric_table_100m",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_metric_table_100m}
        self.SET_METRIC_TABLE_10G = {"constant": "set_metric_table_10g",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_metric_table_10g}
        self.SET_METRIC_TABLE_10M = {"constant": "set_metric_table_10m",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_metric_table_10m}
        self.SET_METRIC_TABLE_1G = {"constant": "set_metric_table_1g",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_metric_table_1g}
        self.SET_METRIC_TABLE_25G = {"constant": "set_metric_table_25g",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_metric_table_25g}
        self.SET_METRIC_TABLE_2DOT5G = {"constant": "set_metric_table_2dot5g",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_metric_table_2dot5g}
        self.SET_METRIC_TABLE_40G = {"constant": "set_metric_table_40g",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_metric_table_40g}
        self.SET_METRIC_TABLE_50G = {"constant": "set_metric_table_50g",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_metric_table_50g}
        self.SET_METRIC_TABLE_5G = {"constant": "set_metric_table_5g",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_metric_table_5g}
        self.SET_ROUTER_ID = {"constant": "set_router_id",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_router_id}
        self.SET_VLAN_AUTH_MD5 = {"constant": "set_vlan_auth_md5",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_vlan_auth_md5}
        self.SET_VLAN_AUTH_NONE = {"constant": "set_vlan_auth_none",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_vlan_auth_none}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_info}
        self.SHOW_INTERFACE = {"constant": "show_interface",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.show_interface}
        self.SHOW_NEIGHBOR = {"constant": "show_neighbor",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_neighbor}
        self.SHOW_VLAN_INTERFACE = {"constant": "show_vlan_interface",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.show_vlan_interface}
