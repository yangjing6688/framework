"""
This class outlines all the constants for the vrf API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VrfConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VrfConstants(ApiConstants):
    def __init__(self):
        super(VrfConstants, self).__init__()
        self.CLEAR_INTERFACE_VLAN = {"constant": "clear_interface_vlan",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.clear_interface_vlan}
        self.CLEAR_ISIS_REDISTRIBUTE_DIRECT = {"constant": "clear_isis_redistribute_direct",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.clear_isis_redistribute_direct}
        self.CREATE_ROUTER = {"constant": "create_router",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.create_router}
        self.CREATE_ROUTER_WITH_VRFID = {"constant": "create_router_with_vrfid",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.create_router_with_vrfid}
        self.DELETE_ROUTER = {"constant": "delete_router",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.delete_router}
        self.DISABLE_IPV6_MAX_ROUTES_TRAP = {"constant": "disable_ipv6_max_routes_trap",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.disable_ipv6_max_routes_trap}
        self.DISABLE_IPVPN = {"constant": "disable_ipvpn",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.disable_ipvpn}
        self.DISABLE_ISIS_REDISTRIBUTE_DIRECT = {"constant": "disable_isis_redistribute_direct",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.disable_isis_redistribute_direct}
        self.DISABLE_MAX_ROUTES_TRAP = {"constant": "disable_max_routes_trap",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.disable_max_routes_trap}
        self.DISABLE_MVPN = {"constant": "disable_mvpn",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_mvpn}
        self.DISABLE_TRAP = {"constant": "disable_trap",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_trap}
        self.ENABLE_IPV6_MAX_ROUTES_TRAP = {"constant": "enable_ipv6_max_routes_trap",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.enable_ipv6_max_routes_trap}
        self.ENABLE_IPVPN = {"constant": "enable_ipvpn",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.enable_ipvpn}
        self.ENABLE_ISIS_REDISTRIBUTE_DIRECT = {"constant": "enable_isis_redistribute_direct",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.enable_isis_redistribute_direct}
        self.ENABLE_MAX_ROUTES_TRAP = {"constant": "enable_max_routes_trap",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.enable_max_routes_trap}
        self.ENABLE_MVPN = {"constant": "enable_mvpn",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_mvpn}
        self.ENABLE_TRAP = {"constant": "enable_trap",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_trap}
        self.SET_INTERFACE_VLAN = {"constant": "set_interface_vlan",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_interface_vlan}
        self.SET_IPV6_MAX_ROUTES = {"constant": "set_ipv6_max_routes",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_ipv6_max_routes}
        self.SET_IPVPN = {"constant": "set_ipvpn",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.set_ipvpn}
        self.SET_ISID = {"constant": "set_isid",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_isid}
        self.SET_ISIS_REDISTRIBUTE_DIRECT = {"constant": "set_isis_redistribute_direct",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_isis_redistribute_direct}
        self.SET_ISIS_REDISTRIBUTE_DIRECT_APPLY = {"constant": "set_isis_redistribute_direct_apply",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.set_isis_redistribute_direct_apply}
        self.SET_MAX_ROUTES = {"constant": "set_max_routes",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_max_routes}
        self.SET_MVPN_FWD_CACHE_TIMEOUT = {"constant": "set_mvpn_fwd_cache_timeout",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_mvpn_fwd_cache_timeout}
        self.SET_NAME = {"constant": "set_name",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_name}
        self.SET_VRFID = {"constant": "set_vrfid",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.set_vrfid}
        self.SHOW_ALL = {"constant": "show_all",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_all}
        self.SHOW_INTERFACE_VLAN = {"constant": "show_interface_vlan",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_interface_vlan}
        self.SHOW_IPV6_MAX_ROUTES = {"constant": "show_ipv6_max_routes",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_ipv6_max_routes}
        self.SHOW_IPV6_MAX_ROUTES_ALL = {"constant": "show_ipv6_max_routes_all",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_ipv6_max_routes_all}
        self.SHOW_IPV6_MAX_ROUTES_NAME = {"constant": "show_ipv6_max_routes_name",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_ipv6_max_routes_name}
        self.SHOW_IPVPN = {"constant": "show_ipvpn",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_ipvpn}
        self.SHOW_IP_ROUTE = {"constant": "show_ip_route",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_ip_route}
        self.SHOW_IP_ROUTING = {"constant": "show_ip_routing",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_ip_routing}
        self.SHOW_ISID_LIST = {"constant": "show_isid_list",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_isid_list}
        self.SHOW_ISIS_REDISTRIBUTE_DIRECT = {"constant": "show_isis_redistribute_direct",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_isis_redistribute_direct}
        self.SHOW_MAX_ROUTES = {"constant": "show_max_routes",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_max_routes}
        self.SHOW_MAX_ROUTES_ALL = {"constant": "show_max_routes_all",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_max_routes_all}
        self.SHOW_MAX_ROUTES_NAME = {"constant": "show_max_routes_name",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_max_routes_name}
        self.SHOW_MVPN = {"constant": "show_mvpn",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_mvpn}
        self.SHOW_NAME = {"constant": "show_name",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_name}
        self.SHOW_VRFIDS = {"constant": "show_vrfids",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_vrfids}
        self.SHOW_VRFID_IP_ROUTING = {"constant": "show_vrfid_ip_routing",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_vrfid_ip_routing}
