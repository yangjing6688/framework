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
        self.CHECK_MLD_SNOOPING_FAST_LEAVE = {"constant": "check_mld_snooping_fast_leave",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_mld_snooping_fast_leave}
        self.CHECK_MLD_SNOOPING_LAST_MEMBER_QUERY_COUNT = {"constant": "check_mld_snooping_last_member_query_count",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_mld_snooping_last_member_query_count}
        self.CHECK_MLD_SNOOPING_LAST_MEMBER_QUERY_INTERVAL = {"constant": "check_mld_snooping_last_member_query_interval",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.check_mld_snooping_last_member_query_interval}
        self.CHECK_MLD_SNOOPING_MROUTER = {"constant": "check_mld_snooping_mrouter",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_mld_snooping_mrouter}
        self.CHECK_MLD_SNOOPING_QUERIER_STATE = {"constant": "check_mld_snooping_querier_state",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_mld_snooping_querier_state}
        self.CHECK_MLD_SNOOPING_ROBUSTNESS_VARIABLE = {"constant": "check_mld_snooping_robustness_variable",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_mld_snooping_robustness_variable}
        self.CHECK_MLD_SNOOPING_STARTUP_QUERY_COUNT = {"constant": "check_mld_snooping_startup_query_count",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_mld_snooping_startup_query_count}
        self.CHECK_MLD_SNOOPING_STARTUP_QUERY_INTERVAL = {"constant": "check_mld_snooping_startup_query_interval",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_mld_snooping_startup_query_interval}
        self.CHECK_MLD_SNOOPING_STATE = {"constant": "check_mld_snooping_state",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_mld_snooping_state}
        self.CHECK_MLD_STATE = {"constant": "check_mld_state",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_mld_state}
        self.CHECK_MLD_VERSION = {"constant": "check_mld_version",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_mld_version}
