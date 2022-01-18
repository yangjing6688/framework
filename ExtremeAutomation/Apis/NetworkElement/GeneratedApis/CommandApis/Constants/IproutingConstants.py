"""
This class outlines all the constants for the iprouting API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(IproutingConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class IproutingConstants(ApiConstants):
    def __init__(self):
        super(IproutingConstants, self).__init__()
        self.CREATE_STATIC_ROUTE = {"constant": "create_static_route",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.create_static_route}
        self.DELETE_STATIC_ROUTE = {"constant": "delete_static_route",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.delete_static_route}
        self.DISABLE_IPMCFORWARDING_GLOBAL = {"constant": "disable_ipmcforwarding_global",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.disable_ipmcforwarding_global}
        self.DISABLE_IPMCFORWARDING_IPV4_GLOBAL = {"constant": "disable_ipmcforwarding_ipv4_global",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.disable_ipmcforwarding_ipv4_global}
        self.DISABLE_IPMCFORWARDING_IPV4_VLAN = {"constant": "disable_ipmcforwarding_ipv4_vlan",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.disable_ipmcforwarding_ipv4_vlan}
        self.DISABLE_IPMCFORWARDING_IPV6_GLOBAL = {"constant": "disable_ipmcforwarding_ipv6_global",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.disable_ipmcforwarding_ipv6_global}
        self.DISABLE_IPMCFORWARDING_IPV6_VLAN = {"constant": "disable_ipmcforwarding_ipv6_vlan",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.disable_ipmcforwarding_ipv6_vlan}
        self.ENABLE_IPMCFORWARDING_GLOBAL = {"constant": "enable_ipmcforwarding_global",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.enable_ipmcforwarding_global}
        self.ENABLE_IPMCFORWARDING_IPV4_GLOBAL = {"constant": "enable_ipmcforwarding_ipv4_global",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.enable_ipmcforwarding_ipv4_global}
        self.ENABLE_IPMCFORWARDING_IPV4_VLAN = {"constant": "enable_ipmcforwarding_ipv4_vlan",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.enable_ipmcforwarding_ipv4_vlan}
        self.ENABLE_IPMCFORWARDING_IPV6_GLOBAL = {"constant": "enable_ipmcforwarding_ipv6_global",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.enable_ipmcforwarding_ipv6_global}
        self.ENABLE_IPMCFORWARDING_IPV6_VLAN = {"constant": "enable_ipmcforwarding_ipv6_vlan",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.enable_ipmcforwarding_ipv6_vlan}
        self.SHOW_ALL_IPV6_ROUTES = {"constant": "show_all_ipv6_routes",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_all_ipv6_routes}
        self.SHOW_ALL_ROUTES = {"constant": "show_all_routes",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_all_routes}
        self.SHOW_IPV6_ROUTE_VRF = {"constant": "show_ipv6_route_vrf",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_ipv6_route_vrf}
        self.SHOW_IP_ROUTE_VRF = {"constant": "show_ip_route_vrf",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_ip_route_vrf}
        self.SHOW_STATIC_ROUTE = {"constant": "show_static_route",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_static_route}
