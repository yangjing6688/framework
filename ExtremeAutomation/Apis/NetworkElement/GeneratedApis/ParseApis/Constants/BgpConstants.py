"""
This class outlines all the constants for the bgp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(BgpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class BgpConstants(ApiConstants):
    def __init__(self):
        super(BgpConstants, self).__init__()
        self.CHECK_ADVERTISE_INACTIVE_ROUTES = {"constant": "check_advertise_inactive_routes",
                                                "tags": ["PARSE_REST"],
                                                "link": self.link.check_advertise_inactive_routes}
        self.CHECK_ALLOW_MULTIPLE_AS = {"constant": "check_allow_multiple_as",
                                        "tags": ["PARSE_REST"],
                                        "link": self.link.check_allow_multiple_as}
        self.CHECK_ALWAYS_COMPARE_MED = {"constant": "check_always_compare_med",
                                         "tags": ["PARSE_REST"],
                                         "link": self.link.check_always_compare_med}
        self.CHECK_BGP_AS = {"constant": "check_bgp_as",
                             "tags": ["PARSE_CLI", "PARSE_REST"],
                             "link": self.link.check_bgp_as}
        self.CHECK_BGP_AUTO_PEERING = {"constant": "check_bgp_auto_peering",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_bgp_auto_peering}
        self.CHECK_BGP_DELETED = {"constant": "check_bgp_deleted",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_bgp_deleted}
        self.CHECK_BGP_DISABLED = {"constant": "check_bgp_disabled",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_bgp_disabled}
        self.CHECK_BGP_ENABLED = {"constant": "check_bgp_enabled",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_bgp_enabled}
        self.CHECK_BGP_ROUTER_ID = {"constant": "check_bgp_router_id",
                                    "tags": ["PARSE_CLI", "PARSE_REST"],
                                    "link": self.link.check_bgp_router_id}
        self.CHECK_CONFEDERATION_ID = {"constant": "check_confederation_id",
                                       "tags": ["PARSE_REST"],
                                       "link": self.link.check_confederation_id}
        self.CHECK_CONFEDERATION_PEER_MEMBER_AS = {"constant": "check_confederation_peer_member_as",
                                                   "tags": ["PARSE_REST"],
                                                   "link": self.link.check_confederation_peer_member_as}
        self.CHECK_GRACEFUL_RESTART = {"constant": "check_graceful_restart",
                                       "tags": ["PARSE_REST"],
                                       "link": self.link.check_graceful_restart}
        self.CHECK_GRACEFUL_RESTART_TIME = {"constant": "check_graceful_restart_time",
                                            "tags": ["PARSE_REST"],
                                            "link": self.link.check_graceful_restart_time}
        self.CHECK_LINKLOCAL_NEIGHBOR_STATE = {"constant": "check_linklocal_neighbor_state",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_linklocal_neighbor_state}
        self.CHECK_MAXIMUM_PATHS = {"constant": "check_maximum_paths",
                                    "tags": ["PARSE_REST"],
                                    "link": self.link.check_maximum_paths}
        self.CHECK_NEIGHBOR_EXISTS = {"constant": "check_neighbor_exists",
                                      "tags": ["PARSE_CLI", "PARSE_REST"],
                                      "link": self.link.check_neighbor_exists}
        self.CHECK_NEIGHBOR_HOLD_TIME = {"constant": "check_neighbor_hold_time",
                                         "tags": ["PARSE_REST"],
                                         "link": self.link.check_neighbor_hold_time}
        self.CHECK_NEIGHBOR_KEEP_ALIVE_TIME = {"constant": "check_neighbor_keep_alive_time",
                                               "tags": ["PARSE_REST"],
                                               "link": self.link.check_neighbor_keep_alive_time}
        self.CHECK_NEIGHBOR_STATE = {"constant": "check_neighbor_state",
                                     "tags": ["PARSE_CLI", "PARSE_REST"],
                                     "link": self.link.check_neighbor_state}
        self.CHECK_NETWORK_EXISTS = {"constant": "check_network_exists",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_network_exists}
        self.CHECK_PEER_GROUP_EXISTS = {"constant": "check_peer_group_exists",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_peer_group_exists}
        self.CHECK_REDISTRIBUTED_ROUTE_EXISTS = {"constant": "check_redistributed_route_exists",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_redistributed_route_exists}
        self.CHECK_ROUTE_EXISTS = {"constant": "check_route_exists",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.check_route_exists}
        self.CHECK_STALE_ROUTE_TIME = {"constant": "check_stale_route_time",
                                       "tags": ["PARSE_REST"],
                                       "link": self.link.check_stale_route_time}
