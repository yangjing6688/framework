"""
This class outlines all the constants for the fdb API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(FdbConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class FdbConstants(ApiConstants):
    def __init__(self):
        super(FdbConstants, self).__init__()
        self.CLEAR_AGETIME = {"constant": "clear_agetime",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_agetime}
        self.CLEAR_AGETIME_CONVERSATIONAL = {"constant": "clear_agetime_conversational",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.clear_agetime_conversational}
        self.CLEAR_ALL = {"constant": "clear_all",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.clear_all}
        self.CLEAR_ALL_LINECARD = {"constant": "clear_all_linecard",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_all_linecard}
        self.CLEAR_ALL_LINECARD_RBID = {"constant": "clear_all_linecard_rbid",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_all_linecard_rbid}
        self.CLEAR_ALL_PORT = {"constant": "clear_all_port",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_all_port}
        self.CLEAR_ALL_VLAN = {"constant": "clear_all_vlan",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_all_vlan}
        self.CLEAR_DYNAMIC_ENTRY = {"constant": "clear_dynamic_entry",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_dynamic_entry}
        self.CLEAR_FDB_LEARN_MODE = {"constant": "clear_fdb_learn_mode",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_fdb_learn_mode}
        self.CLEAR_MAC_PORT = {"constant": "clear_mac_port",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_mac_port}
        self.CLEAR_MAC_PORT_VLAN = {"constant": "clear_mac_port_vlan",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_mac_port_vlan}
        self.CREATE_BLACKHOLE_ENTRY = {"constant": "create_blackhole_entry",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.create_blackhole_entry}
        self.CREATE_ENTRY = {"constant": "create_entry",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.create_entry}
        self.CREATE_MULTICAST_ENTRY = {"constant": "create_multicast_entry",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.create_multicast_entry}
        self.DELETE_ENTRY = {"constant": "delete_entry",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.delete_entry}
        self.DISABLE_LEARNING = {"constant": "disable_learning",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_learning}
        self.DISABLE_LEARNING_PORT = {"constant": "disable_learning_port",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_learning_port}
        self.DISABLE_LEARNING_VLAN = {"constant": "disable_learning_vlan",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_learning_vlan}
        self.DISABLE_UNICAST_AS_MULTICAST = {"constant": "disable_unicast_as_multicast",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.disable_unicast_as_multicast}
        self.ENABLE_LEARNING = {"constant": "enable_learning",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_learning}
        self.ENABLE_LEARNING_PORT = {"constant": "enable_learning_port",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_learning_port}
        self.ENABLE_LEARNING_VLAN = {"constant": "enable_learning_vlan",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_learning_vlan}
        self.ENABLE_UNICAST_AS_MULTICAST = {"constant": "enable_unicast_as_multicast",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.enable_unicast_as_multicast}
        self.SET_AGETIME = {"constant": "set_agetime",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_agetime}
        self.SET_AGETIME_CONVERSATIONAL = {"constant": "set_agetime_conversational",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_agetime_conversational}
        self.SET_AGETIME_MIN = {"constant": "set_agetime_min",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_agetime_min}
        self.SET_FDB_LEARN_MODE_CONVERSATIONAL = {"constant": "set_fdb_learn_mode_conversational",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.set_fdb_learn_mode_conversational}
        self.SHOW_AGETIME = {"constant": "show_agetime",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_agetime}
        self.SHOW_ALL_ENTRIES = {"constant": "show_all_entries",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_all_entries}
        self.SHOW_ENTRIES_PORT = {"constant": "show_entries_port",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_entries_port}
        self.SHOW_ENTRIES_VLAN = {"constant": "show_entries_vlan",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_entries_vlan}
        self.SHOW_ENTRY = {"constant": "show_entry",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_entry}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_port}
        self.SHOW_STATS = {"constant": "show_stats",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_stats}
        self.SHOW_STATS_PORT = {"constant": "show_stats_port",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_stats_port}
        self.SHOW_STATS_VLAN = {"constant": "show_stats_vlan",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_stats_vlan}
        self.SHOW_STATS_VLAN_NAME = {"constant": "show_stats_vlan_name",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_stats_vlan_name}
        self.SHOW_VLAN = {"constant": "show_vlan",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_vlan}
        self.SHOW_VLAN_NAME = {"constant": "show_vlan_name",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_vlan_name}
