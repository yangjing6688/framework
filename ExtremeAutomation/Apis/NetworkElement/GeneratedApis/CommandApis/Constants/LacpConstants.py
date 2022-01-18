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
        self.CLEAR_ALL_COUNTERS = {"constant": "clear_all_counters",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_all_counters}
        self.CLEAR_COUNTERS = {"constant": "clear_counters",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_counters}
        self.CLEAR_LAG_PORT = {"constant": "clear_lag_port",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_lag_port}
        self.CREATE_LAG = {"constant": "create_lag",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.create_lag}
        self.DELETE_LAG = {"constant": "delete_lag",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.delete_lag}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_port}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_port}
        self.SET_LAG_PORT = {"constant": "set_lag_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_lag_port}
        self.SET_MLT_ACTOR_KEY = {"constant": "set_mlt_actor_key",
                                  "tags": ["COMMAND_SNMP"],
                                  "link": self.link.set_mlt_actor_key}
        self.SET_MLT_ACTOR_SYSTEM_PRIORITY = {"constant": "set_mlt_actor_system_priority",
                                              "tags": ["COMMAND_SNMP"],
                                              "link": self.link.set_mlt_actor_system_priority}
        self.SET_PORT_PRIORITY = {"constant": "set_port_priority",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_port_priority}
        self.SET_SYSTEM_PRIORITY = {"constant": "set_system_priority",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_system_priority}
        self.SHOW_COUNTER = {"constant": "show_counter",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_counter}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
        self.SHOW_LAG = {"constant": "show_lag",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_lag}
        self.SHOW_LAG_INFO = {"constant": "show_lag_info",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_lag_info}
        self.SHOW_MLT_ID_LOGICAL_INDEX = {"constant": "show_mlt_id_logical_index",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.show_mlt_id_logical_index}
        self.SHOW_MLT_PORT = {"constant": "show_mlt_port",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.show_mlt_port}
        self.SHOW_PORT_ALL = {"constant": "show_port_all",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_port_all}
        self.SHOW_SYSID = {"constant": "show_sysid",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_sysid}
