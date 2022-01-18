"""
This class outlines all the constants for the igmp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(IgmpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class IgmpConstants(ApiConstants):
    def __init__(self):
        super(IgmpConstants, self).__init__()
        self.CLEAR_SNOOPING_QUERIER = {"constant": "clear_snooping_querier",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_snooping_querier}
        self.CLEAR_SNOOPING_QUERIER_ADDRESS = {"constant": "clear_snooping_querier_address",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.clear_snooping_querier_address}
        self.DISABLE_SNOOPING = {"constant": "disable_snooping",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_snooping}
        self.DISABLE_SNOOPING_COMPATIBILITY_MODE_VLAN = {"constant": "disable_snooping_compatibility_mode_vlan",
                                                         "tags": ["COMMAND_CLI"],
                                                         "link": self.link.disable_snooping_compatibility_mode_vlan}
        self.DISABLE_SNOOPING_DYNAMIC_DOWNGRADE_VLAN = {"constant": "disable_snooping_dynamic_downgrade_vlan",
                                                        "tags": ["COMMAND_CLI"],
                                                        "link": self.link.disable_snooping_dynamic_downgrade_vlan}
        self.DISABLE_SNOOPING_EXPLICIT_HOST_TRACKING_VLAN = {"constant": "disable_snooping_explicit_host_tracking_vlan",
                                                             "tags": ["COMMAND_CLI"],
                                                             "link": self.link.disable_snooping_explicit_host_tracking_vlan}
        self.DISABLE_SNOOPING_FAST_LEAVE = {"constant": "disable_snooping_fast_leave",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_snooping_fast_leave}
        self.DISABLE_SNOOPING_PROXY = {"constant": "disable_snooping_proxy",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.disable_snooping_proxy}
        self.DISABLE_SNOOPING_VLAN = {"constant": "disable_snooping_vlan",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_snooping_vlan}
        self.DISABLE_VLAN = {"constant": "disable_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_vlan}
        self.ENABLE_SNOOPING = {"constant": "enable_snooping",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_snooping}
        self.ENABLE_SNOOPING_COMPATIBILITY_MODE_VLAN = {"constant": "enable_snooping_compatibility_mode_vlan",
                                                        "tags": ["COMMAND_CLI"],
                                                        "link": self.link.enable_snooping_compatibility_mode_vlan}
        self.ENABLE_SNOOPING_DYNAMIC_DOWNGRADE_VLAN = {"constant": "enable_snooping_dynamic_downgrade_vlan",
                                                       "tags": ["COMMAND_CLI"],
                                                       "link": self.link.enable_snooping_dynamic_downgrade_vlan}
        self.ENABLE_SNOOPING_EXPLICIT_HOST_TRACKING_VLAN = {"constant": "enable_snooping_explicit_host_tracking_vlan",
                                                            "tags": ["COMMAND_CLI"],
                                                            "link": self.link.enable_snooping_explicit_host_tracking_vlan}
        self.ENABLE_SNOOPING_FAST_LEAVE = {"constant": "enable_snooping_fast_leave",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_snooping_fast_leave}
        self.ENABLE_SNOOPING_PROXY = {"constant": "enable_snooping_proxy",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.enable_snooping_proxy}
        self.ENABLE_SNOOPING_VLAN = {"constant": "enable_snooping_vlan",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_snooping_vlan}
        self.ENABLE_VLAN = {"constant": "enable_vlan",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_vlan}
        self.SET_SNOOPING_LAST_MEMBER_QUERY_COUNT = {"constant": "set_snooping_last_member_query_count",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.set_snooping_last_member_query_count}
        self.SET_SNOOPING_LAST_MEMBER_QUERY_INTERVAL = {"constant": "set_snooping_last_member_query_interval",
                                                        "tags": ["COMMAND_CLI"],
                                                        "link": self.link.set_snooping_last_member_query_interval}
        self.SET_SNOOPING_QUERIER = {"constant": "set_snooping_querier",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_snooping_querier}
        self.SET_SNOOPING_QUERIER_ADDRESS = {"constant": "set_snooping_querier_address",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_snooping_querier_address}
        self.SET_SNOOPING_QUERY_INTERVAL = {"constant": "set_snooping_query_interval",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.set_snooping_query_interval}
        self.SET_SNOOPING_QUERY_MAX_RESPONSE_TIME = {"constant": "set_snooping_query_max_response_time",
                                                     "tags": ["COMMAND_CLI"],
                                                     "link": self.link.set_snooping_query_max_response_time}
        self.SET_VERSION = {"constant": "set_version",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_version}
        self.SET_VERSION_INTERFACE = {"constant": "set_version_interface",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_version_interface}
        self.SHOW_GROUP = {"constant": "show_group",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_group}
        self.SHOW_GROUPS_VLAN = {"constant": "show_groups_vlan",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_groups_vlan}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_port}
        self.SHOW_ROUTER_ALERT = {"constant": "show_router_alert",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_router_alert}
        self.SHOW_SENDER = {"constant": "show_sender",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_sender}
        self.SHOW_SNOOPING = {"constant": "show_snooping",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_snooping}
        self.SHOW_SNOOPING_QUERIER_ADDRESS = {"constant": "show_snooping_querier_address",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_snooping_querier_address}
        self.SHOW_SNOOP_TRACE = {"constant": "show_snoop_trace",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_snoop_trace}
        self.SHOW_STATE = {"constant": "show_state",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_state}
        self.SHOW_STATISTICS_PORT = {"constant": "show_statistics_port",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_statistics_port}
        self.SHOW_STATISTICS_VLAN = {"constant": "show_statistics_vlan",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_statistics_vlan}
        self.SHOW_VERSION = {"constant": "show_version",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_version}
        self.SHOW_VLAN = {"constant": "show_vlan",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_vlan}
