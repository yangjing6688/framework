"""
This class outlines all the constants for the autopeering API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AutopeeringConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AutopeeringConstants(ApiConstants):
    def __init__(self):
        super(AutopeeringConstants, self).__init__()
        self.CLEAR_ALL_HOSTS = {"constant": "clear_all_hosts",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.clear_all_hosts}
        self.CLEAR_ALL_SERVICES = {"constant": "clear_all_services",
                                   "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                   "link": self.link.clear_all_services}
        self.CLEAR_ALL_STATIC_ROUTE_FROM_HOST = {"constant": "clear_all_static_route_from_host",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.clear_all_static_route_from_host}
        self.CLEAR_ANYCAST_MAC = {"constant": "clear_anycast_mac",
                                  "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                  "link": self.link.clear_anycast_mac}
        self.CLEAR_ANYCAST_MAC_AND_ID = {"constant": "clear_anycast_mac_and_id",
                                         "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                         "link": self.link.clear_anycast_mac_and_id}
        self.CLEAR_ANYCAST_MAC_AND_ROUTE_TARGET = {"constant": "clear_anycast_mac_and_route_target",
                                                   "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                                   "link": self.link.clear_anycast_mac_and_route_target}
        self.CLEAR_HOST = {"constant": "clear_host",
                           "tags": ["COMMAND_CLI", "COMMAND_REST"],
                           "link": self.link.clear_host}
        self.CLEAR_SERVICE = {"constant": "clear_service",
                              "tags": ["COMMAND_CLI", "COMMAND_REST"],
                              "link": self.link.clear_service}
        self.CLEAR_STATIC_ROUTE_FROM_HOST = {"constant": "clear_static_route_from_host",
                                             "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                             "link": self.link.clear_static_route_from_host}
        self.SET_ANYCAST_MAC = {"constant": "set_anycast_mac",
                                "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                "link": self.link.set_anycast_mac}
        self.SET_ANYCAST_MAC_AND_ID = {"constant": "set_anycast_mac_and_id",
                                       "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                       "link": self.link.set_anycast_mac_and_id}
        self.SET_ANYCAST_MAC_AND_ROUTE_TARGET = {"constant": "set_anycast_mac_and_route_target",
                                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                                 "link": self.link.set_anycast_mac_and_route_target}
        self.SET_HOST_ADDRESS_HOST_VRF_STATIC_ROUTE_NETWORK_STATIC_ROUTE_NEXT_HOP = {"constant": "set_host_address_host_vrf_static_route_network_static_route_next_hop",
                                                                                     "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                                                                     "link": self.link.set_host_address_host_vrf_static_route_network_static_route_next_hop}
        self.SET_HOST_STATIC_ROUTE = {"constant": "set_host_static_route",
                                      "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                      "link": self.link.set_host_static_route}
        self.SET_SERVICE_NSI_NSI_TYPE_VRF_ADDRESS_IP_ADDRESS_PREFIX_LENGTH = {"constant": "set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length",
                                                                              "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                                                              "link": self.link.set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length}
        self.SHOW_ALL_SERVICES = {"constant": "show_all_services",
                                  "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                  "link": self.link.show_all_services}
        self.SHOW_GLOBAL = {"constant": "show_global",
                            "tags": ["COMMAND_CLI", "COMMAND_REST"],
                            "link": self.link.show_global}
        self.SHOW_HOSTS = {"constant": "show_hosts",
                           "tags": ["COMMAND_CLI", "COMMAND_REST"],
                           "link": self.link.show_hosts}
        self.SHOW_HOST_STATIC_ROUTES = {"constant": "show_host_static_routes",
                                        "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                        "link": self.link.show_host_static_routes}
        self.SHOW_SERVICE = {"constant": "show_service",
                             "tags": ["COMMAND_CLI", "COMMAND_REST"],
                             "link": self.link.show_service}
