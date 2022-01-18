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
        self.CHECK_FDB_AGETIME = {"constant": "check_fdb_agetime",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_fdb_agetime}
        self.CHECK_FDB_ENTRY_EXISTS = {"constant": "check_fdb_entry_exists",
                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                       "link": self.link.check_fdb_entry_exists}
        self.CHECK_FDB_ENTRY_EXISTS_TWICE = {"constant": "check_fdb_entry_exists_twice",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_fdb_entry_exists_twice}
        self.CHECK_FDB_ENTRY_ONLY_EXISTS_ONCE = {"constant": "check_fdb_entry_only_exists_once",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_fdb_entry_only_exists_once}
        self.CHECK_FDB_STATS_DROPPED_EQUAL = {"constant": "check_fdb_stats_dropped_equal",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_fdb_stats_dropped_equal}
        self.CHECK_FDB_STATS_DROPPED_PORT_EQUAL = {"constant": "check_fdb_stats_dropped_port_equal",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_fdb_stats_dropped_port_equal}
        self.CHECK_FDB_STATS_DROPPED_VLAN_EQUAL = {"constant": "check_fdb_stats_dropped_vlan_equal",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_fdb_stats_dropped_vlan_equal}
        self.CHECK_FDB_STATS_DYNAMIC_EQUAL = {"constant": "check_fdb_stats_dynamic_equal",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_fdb_stats_dynamic_equal}
        self.CHECK_FDB_STATS_DYNAMIC_PORT_EQUAL = {"constant": "check_fdb_stats_dynamic_port_equal",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_fdb_stats_dynamic_port_equal}
        self.CHECK_FDB_STATS_DYNAMIC_VLAN_EQUAL = {"constant": "check_fdb_stats_dynamic_vlan_equal",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_fdb_stats_dynamic_vlan_equal}
        self.CHECK_FDB_STATS_LOCKED_EQUAL = {"constant": "check_fdb_stats_locked_equal",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_fdb_stats_locked_equal}
        self.CHECK_FDB_STATS_LOCKED_WITH_TIMEOUT_EQUAL = {"constant": "check_fdb_stats_locked_with_timeout_equal",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_fdb_stats_locked_with_timeout_equal}
        self.CHECK_FDB_STATS_PERM_EQUAL = {"constant": "check_fdb_stats_perm_equal",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_fdb_stats_perm_equal}
        self.CHECK_FDB_STATS_STATIC_EQUAL = {"constant": "check_fdb_stats_static_equal",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_fdb_stats_static_equal}
        self.CHECK_FDB_STATS_STATIC_PORT_EQUAL = {"constant": "check_fdb_stats_static_port_equal",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_fdb_stats_static_port_equal}
        self.CHECK_FDB_STATS_STATIC_VLAN_EQUAL = {"constant": "check_fdb_stats_static_vlan_equal",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_fdb_stats_static_vlan_equal}
        self.CHECK_FDB_STATS_TOTAL_EQUAL = {"constant": "check_fdb_stats_total_equal",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_fdb_stats_total_equal}
        self.CHECK_FDB_STATS_TOTAL_PORT_EQUAL = {"constant": "check_fdb_stats_total_port_equal",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_fdb_stats_total_port_equal}
        self.CHECK_FDB_STATS_TOTAL_VLAN_EQUAL = {"constant": "check_fdb_stats_total_vlan_equal",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_fdb_stats_total_vlan_equal}
