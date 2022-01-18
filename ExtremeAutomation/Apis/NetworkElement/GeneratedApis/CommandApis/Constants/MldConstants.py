"""
This class outlines all the constants for the mld API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MldConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MldConstants(ApiConstants):
    def __init__(self):
        super(MldConstants, self).__init__()
        self.CLEAR_SNOOPING_FAST_LEAVE = {"constant": "clear_snooping_fast_leave",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_snooping_fast_leave}
        self.CLEAR_SNOOPING_LAST_MEMBER_QUERY_COUNT = {"constant": "clear_snooping_last_member_query_count",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.clear_snooping_last_member_query_count}
        self.CLEAR_SNOOPING_LAST_MEMBER_QUERY_INTERVAL = {"constant": "clear_snooping_last_member_query_interval",
                                                          "tags": ["COMMAND_CLI"],
                                                          "link": self.link.clear_snooping_last_member_query_interval}
        self.CLEAR_SNOOPING_MROUTER = {"constant": "clear_snooping_mrouter",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_snooping_mrouter}
        self.CLEAR_SNOOPING_ROBUSTNESS_VARIABLE = {"constant": "clear_snooping_robustness_variable",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.clear_snooping_robustness_variable}
        self.CLEAR_SNOOPING_STARTUP_QUERY_COUNT = {"constant": "clear_snooping_startup_query_count",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.clear_snooping_startup_query_count}
        self.CLEAR_SNOOPING_STARTUP_QUERY_INTERVAL = {"constant": "clear_snooping_startup_query_interval",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.clear_snooping_startup_query_interval}
        self.DISABLE_SNOOPING = {"constant": "disable_snooping",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_snooping}
        self.DISABLE_SNOOPING_QUERIER = {"constant": "disable_snooping_querier",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.disable_snooping_querier}
        self.DISABLE_VLAN = {"constant": "disable_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_vlan}
        self.ENABLE_SNOOPING = {"constant": "enable_snooping",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_snooping}
        self.ENABLE_SNOOPING_QUERIER = {"constant": "enable_snooping_querier",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.enable_snooping_querier}
        self.ENABLE_VLAN = {"constant": "enable_vlan",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_vlan}
        self.SET_SNOOPING_FAST_LEAVE = {"constant": "set_snooping_fast_leave",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_snooping_fast_leave}
        self.SET_SNOOPING_LAST_MEMBER_QUERY_COUNT = {"constant": "set_snooping_last_member_query_count",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.set_snooping_last_member_query_count}
        self.SET_SNOOPING_LAST_MEMBER_QUERY_INTERVAL = {"constant": "set_snooping_last_member_query_interval",
                                                        "tags": ["COMMAND_CLI"],
                                                        "link": self.link.set_snooping_last_member_query_interval}
        self.SET_SNOOPING_MROUTER = {"constant": "set_snooping_mrouter",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_snooping_mrouter}
        self.SET_SNOOPING_ROBUSTNESS_VARIABLE = {"constant": "set_snooping_robustness_variable",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_snooping_robustness_variable}
        self.SET_SNOOPING_STARTUP_QUERY_COUNT = {"constant": "set_snooping_startup_query_count",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_snooping_startup_query_count}
        self.SET_SNOOPING_STARTUP_QUERY_INTERVAL = {"constant": "set_snooping_startup_query_interval",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.set_snooping_startup_query_interval}
        self.SET_VERSION = {"constant": "set_version",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_version}
        self.SHOW_STATISTICS = {"constant": "show_statistics",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_statistics}
        self.SHOW_VERSION = {"constant": "show_version",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_version}
        self.SHOW_VLAN = {"constant": "show_vlan",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_vlan}
