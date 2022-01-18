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
        self.VERIFY_ROUTER_VRF_IPVPN_IS_ENABLED = {"constant": "verify_router_vrf_ipvpn_is_enabled",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_router_vrf_ipvpn_is_enabled}
        self.VERIFY_ROUTER_VRF_IPVPN_IS_SET = {"constant": "verify_router_vrf_ipvpn_is_set",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.verify_router_vrf_ipvpn_is_set}
        self.VERIFY_ROUTER_VRF_ISID_IS_SET = {"constant": "verify_router_vrf_isid_is_set",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_router_vrf_isid_is_set}
        self.VERIFY_ROUTER_VRF_ISIS_REDISTRIBUTE_DIRECT = {"constant": "verify_router_vrf_isis_redistribute_direct",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.verify_router_vrf_isis_redistribute_direct}
        self.VERIFY_ROUTER_VRF_ISIS_REDISTRIBUTE_DIRECT_ENABLED = {"constant": "verify_router_vrf_isis_redistribute_direct_enabled",
                                                                   "tags": ["PARSE_CLI"],
                                                                   "link": self.link.verify_router_vrf_isis_redistribute_direct_enabled}
        self.VERIFY_VRF_IPROUTE = {"constant": "verify_vrf_iproute",
                                   "tags": ["PARSE_CLI"],
                                   "link": self.link.verify_vrf_iproute}
        self.VERIFY_VRF_IPV6_MAX_ROUTES = {"constant": "verify_vrf_ipv6_max_routes",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_vrf_ipv6_max_routes}
        self.VERIFY_VRF_IPV6_MAX_ROUTES_TRAP_ENABLED = {"constant": "verify_vrf_ipv6_max_routes_trap_enabled",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.verify_vrf_ipv6_max_routes_trap_enabled}
        self.VERIFY_VRF_IS_ASSIGNED_TO_INTERFACE_VLAN = {"constant": "verify_vrf_is_assigned_to_interface_vlan",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.verify_vrf_is_assigned_to_interface_vlan}
        self.VERIFY_VRF_MAX_ROUTES = {"constant": "verify_vrf_max_routes",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.verify_vrf_max_routes}
        self.VERIFY_VRF_MAX_ROUTES_TRAP_ENABLED = {"constant": "verify_vrf_max_routes_trap_enabled",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_vrf_max_routes_trap_enabled}
        self.VERIFY_VRF_MVPN_DISABLED = {"constant": "verify_vrf_mvpn_disabled",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.verify_vrf_mvpn_disabled}
        self.VERIFY_VRF_MVPN_ENABLED = {"constant": "verify_vrf_mvpn_enabled",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_vrf_mvpn_enabled}
        self.VERIFY_VRF_MVPN_FWD_CACHE_TIMEOUT = {"constant": "verify_vrf_mvpn_fwd_cache_timeout",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.verify_vrf_mvpn_fwd_cache_timeout}
        self.VERIFY_VRF_NAME = {"constant": "verify_vrf_name",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.verify_vrf_name}
        self.VERIFY_VRF_NAME_AND_VRFID = {"constant": "verify_vrf_name_and_vrfid",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_vrf_name_and_vrfid}
        self.VERIFY_VRF_TRAP_ENABLED = {"constant": "verify_vrf_trap_enabled",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_vrf_trap_enabled}
        self.VERIFY_VRF_VRFID = {"constant": "verify_vrf_vrfid",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.verify_vrf_vrfid}
