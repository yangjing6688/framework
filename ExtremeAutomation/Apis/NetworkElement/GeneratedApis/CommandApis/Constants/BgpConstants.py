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
        self.CLEAR_AUTO_PEERING = {"constant": "clear_auto_peering",
                                   "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                   "link": self.link.clear_auto_peering}
        self.CLEAR_CONFEDERATION_ID = {"constant": "clear_confederation_id",
                                       "tags": ["COMMAND_REST"],
                                       "link": self.link.clear_confederation_id}
        self.CLEAR_CONFEDERATION_PEER_MEMBER_AS = {"constant": "clear_confederation_peer_member_as",
                                                   "tags": ["COMMAND_REST"],
                                                   "link": self.link.clear_confederation_peer_member_as}
        self.CLEAR_GRACEFUL_RESTART_TIME = {"constant": "clear_graceful_restart_time",
                                            "tags": ["COMMAND_REST"],
                                            "link": self.link.clear_graceful_restart_time}
        self.CLEAR_GRACEFUL_STALE_ROUTE_TIME = {"constant": "clear_graceful_stale_route_time",
                                                "tags": ["COMMAND_REST"],
                                                "link": self.link.clear_graceful_stale_route_time}
        self.CLEAR_MAXIMUM_PATHS = {"constant": "clear_maximum_paths",
                                    "tags": ["COMMAND_REST"],
                                    "link": self.link.clear_maximum_paths}
        self.CLEAR_NEIGHBOR = {"constant": "clear_neighbor",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_neighbor}
        self.CLEAR_NEIGHBOR_ALL = {"constant": "clear_neighbor_all",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_neighbor_all}
        self.CLEAR_REDISTRIBUTE = {"constant": "clear_redistribute",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_redistribute}
        self.CLEAR_ROUTER_ID = {"constant": "clear_router_id",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.clear_router_id}
        self.CREATE_AS = {"constant": "create_as",
                          "tags": ["COMMAND_CLI", "COMMAND_REST"],
                          "link": self.link.create_as}
        self.CREATE_NEIGHBOR = {"constant": "create_neighbor",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.create_neighbor}
        self.CREATE_NEIGHBOR_LINK_LOCAL = {"constant": "create_neighbor_link_local",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.create_neighbor_link_local}
        self.DELETE_AS = {"constant": "delete_as",
                          "tags": ["COMMAND_CLI", "COMMAND_REST"],
                          "link": self.link.delete_as}
        self.DELETE_NEIGHBOR = {"constant": "delete_neighbor",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.delete_neighbor}
        self.DELETE_NEIGHBOR_LINK_LOCAL = {"constant": "delete_neighbor_link_local",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.delete_neighbor_link_local}
        self.DISABLE_ADVERTISE_INACTIVE_ROUTES_IPV4_UNICAST = {"constant": "disable_advertise_inactive_routes_ipv4_unicast",
                                                               "tags": ["COMMAND_REST"],
                                                               "link": self.link.disable_advertise_inactive_routes_ipv4_unicast}
        self.DISABLE_ADVERTISE_INACTIVE_ROUTES_IPV6_UNICAST = {"constant": "disable_advertise_inactive_routes_ipv6_unicast",
                                                               "tags": ["COMMAND_REST"],
                                                               "link": self.link.disable_advertise_inactive_routes_ipv6_unicast}
        self.DISABLE_ADVERTISE_INACTIVE_ROUTES_L3VPN_IPV4_UNICAST = {"constant": "disable_advertise_inactive_routes_l3vpn_ipv4_unicast",
                                                                     "tags": ["COMMAND_REST"],
                                                                     "link": self.link.disable_advertise_inactive_routes_l3vpn_ipv4_unicast}
        self.DISABLE_ALLOW_MULTIPLE_AS = {"constant": "disable_allow_multiple_as",
                                          "tags": ["COMMAND_REST"],
                                          "link": self.link.disable_allow_multiple_as}
        self.DISABLE_ALWAYS_COMPARE_MED = {"constant": "disable_always_compare_med",
                                           "tags": ["COMMAND_REST"],
                                           "link": self.link.disable_always_compare_med}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_GRACEFUL_RESTART = {"constant": "disable_graceful_restart",
                                         "tags": ["COMMAND_REST"],
                                         "link": self.link.disable_graceful_restart}
        self.DISABLE_NEIGHBOR = {"constant": "disable_neighbor",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                 "link": self.link.disable_neighbor}
        self.DISABLE_NEIGHBOR_CAPABILITY = {"constant": "disable_neighbor_capability",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_neighbor_capability}
        self.DISABLE_NEIGHBOR_LINK_LOCAL = {"constant": "disable_neighbor_link_local",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_neighbor_link_local}
        self.ENABLE_ADVERTISE_INACTIVE_ROUTES_IPV4_UNICAST = {"constant": "enable_advertise_inactive_routes_ipv4_unicast",
                                                              "tags": ["COMMAND_REST"],
                                                              "link": self.link.enable_advertise_inactive_routes_ipv4_unicast}
        self.ENABLE_ADVERTISE_INACTIVE_ROUTES_IPV6_UNICAST = {"constant": "enable_advertise_inactive_routes_ipv6_unicast",
                                                              "tags": ["COMMAND_REST"],
                                                              "link": self.link.enable_advertise_inactive_routes_ipv6_unicast}
        self.ENABLE_ADVERTISE_INACTIVE_ROUTES_L3VPN_IPV4_UNICAST = {"constant": "enable_advertise_inactive_routes_l3vpn_ipv4_unicast",
                                                                    "tags": ["COMMAND_REST"],
                                                                    "link": self.link.enable_advertise_inactive_routes_l3vpn_ipv4_unicast}
        self.ENABLE_ALLOW_MULTIPLE_AS = {"constant": "enable_allow_multiple_as",
                                         "tags": ["COMMAND_REST"],
                                         "link": self.link.enable_allow_multiple_as}
        self.ENABLE_ALWAYS_COMPARE_MED = {"constant": "enable_always_compare_med",
                                          "tags": ["COMMAND_REST"],
                                          "link": self.link.enable_always_compare_med}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_GRACEFUL_RESTART = {"constant": "enable_graceful_restart",
                                        "tags": ["COMMAND_REST"],
                                        "link": self.link.enable_graceful_restart}
        self.ENABLE_NEIGHBOR = {"constant": "enable_neighbor",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.enable_neighbor}
        self.ENABLE_NEIGHBOR_CAPABILITY = {"constant": "enable_neighbor_capability",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_neighbor_capability}
        self.ENABLE_NEIGHBOR_LINK_LOCAL = {"constant": "enable_neighbor_link_local",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_neighbor_link_local}
        self.SET_AUTO_PEERING = {"constant": "set_auto_peering",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                 "link": self.link.set_auto_peering}
        self.SET_CONFEDERATION_ID = {"constant": "set_confederation_id",
                                     "tags": ["COMMAND_REST"],
                                     "link": self.link.set_confederation_id}
        self.SET_CONFEDERATION_PEER_MEMBER_AS = {"constant": "set_confederation_peer_member_as",
                                                 "tags": ["COMMAND_REST"],
                                                 "link": self.link.set_confederation_peer_member_as}
        self.SET_GRACEFUL_RESTART_TIME = {"constant": "set_graceful_restart_time",
                                          "tags": ["COMMAND_REST"],
                                          "link": self.link.set_graceful_restart_time}
        self.SET_GRACEFUL_STALE_ROUTE_TIME = {"constant": "set_graceful_stale_route_time",
                                              "tags": ["COMMAND_REST"],
                                              "link": self.link.set_graceful_stale_route_time}
        self.SET_MAXIMUM_PATHS = {"constant": "set_maximum_paths",
                                  "tags": ["COMMAND_REST"],
                                  "link": self.link.set_maximum_paths}
        self.SET_NEIGHBOR_KEEP_ALIVE_INTERVAL_AND_HOLD_TIME = {"constant": "set_neighbor_keep_alive_interval_and_hold_time",
                                                               "tags": ["COMMAND_REST"],
                                                               "link": self.link.set_neighbor_keep_alive_interval_and_hold_time}
        self.SET_NEIGHBOR_PASSWORD = {"constant": "set_neighbor_password",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_neighbor_password}
        self.SET_NEIGHBOR_TRANSPORT_ADDRESS = {"constant": "set_neighbor_transport_address",
                                               "tags": ["COMMAND_REST"],
                                               "link": self.link.set_neighbor_transport_address}
        self.SET_REDISTRIBUTE = {"constant": "set_redistribute",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_redistribute}
        self.SET_ROUTER_ID = {"constant": "set_router_id",
                              "tags": ["COMMAND_CLI", "COMMAND_REST"],
                              "link": self.link.set_router_id}
        self.SHOW_ADVERTISE_INACTIVE_ROUTES_IPV4_UNICAST = {"constant": "show_advertise_inactive_routes_ipv4_unicast",
                                                            "tags": ["COMMAND_REST"],
                                                            "link": self.link.show_advertise_inactive_routes_ipv4_unicast}
        self.SHOW_ADVERTISE_INACTIVE_ROUTES_IPV6_UNICAST = {"constant": "show_advertise_inactive_routes_ipv6_unicast",
                                                            "tags": ["COMMAND_REST"],
                                                            "link": self.link.show_advertise_inactive_routes_ipv6_unicast}
        self.SHOW_ADVERTISE_INACTIVE_ROUTES_L3VPN_IPV4_UNICAST = {"constant": "show_advertise_inactive_routes_l3vpn_ipv4_unicast",
                                                                  "tags": ["COMMAND_REST"],
                                                                  "link": self.link.show_advertise_inactive_routes_l3vpn_ipv4_unicast}
        self.SHOW_ALL_ROUTES = {"constant": "show_all_routes",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_all_routes}
        self.SHOW_ALWAYS_COMPARE_MED = {"constant": "show_always_compare_med",
                                        "tags": ["COMMAND_REST"],
                                        "link": self.link.show_always_compare_med}
        self.SHOW_CONFEDERATION = {"constant": "show_confederation",
                                   "tags": ["COMMAND_REST"],
                                   "link": self.link.show_confederation}
        self.SHOW_GRACEFUL_RESTART = {"constant": "show_graceful_restart",
                                      "tags": ["COMMAND_REST"],
                                      "link": self.link.show_graceful_restart}
        self.SHOW_NEIGHBORS = {"constant": "show_neighbors",
                               "tags": ["COMMAND_CLI", "COMMAND_REST"],
                               "link": self.link.show_neighbors}
        self.SHOW_NEIGHBOR_TIMERS = {"constant": "show_neighbor_timers",
                                     "tags": ["COMMAND_REST"],
                                     "link": self.link.show_neighbor_timers}
        self.SHOW_NETWORKS = {"constant": "show_networks",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_networks}
        self.SHOW_PEER_GROUP = {"constant": "show_peer_group",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_peer_group}
        self.SHOW_REDISTRIBUTED_ROUTES = {"constant": "show_redistributed_routes",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_redistributed_routes}
        self.SHOW_ROUTE_IP = {"constant": "show_route_ip",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_route_ip}
        self.SHOW_STATS = {"constant": "show_stats",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_stats}
        self.SHOW_STATUS = {"constant": "show_status",
                            "tags": ["COMMAND_CLI", "COMMAND_REST"],
                            "link": self.link.show_status}
        self.SHOW_SUMMARY = {"constant": "show_summary",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_summary}
        self.SHOW_USE_MULTIPLE_PATHS = {"constant": "show_use_multiple_paths",
                                        "tags": ["COMMAND_REST"],
                                        "link": self.link.show_use_multiple_paths}
