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
        self.CHECK_AUTOPEERING_ANYCAST_MAC = {"constant": "check_autopeering_anycast_mac",
                                              "tags": ["PARSE_CLI", "PARSE_REST"],
                                              "link": self.link.check_autopeering_anycast_mac}
        self.CHECK_AUTOPEERING_HOSTS_STATIC_ROUTE_NETWORK_ADDRESS_DOES_NOT_EXIST = {"constant": "check_autopeering_hosts_static_route_network_address_does_not_exist",
                                                                                    "tags": ["PARSE_CLI", "PARSE_REST"],
                                                                                    "link": self.link.check_autopeering_hosts_static_route_network_address_does_not_exist}
        self.CHECK_AUTOPEERING_HOSTS_STATIC_ROUTE_NETWORK_ADDRESS_EXISTS = {"constant": "check_autopeering_hosts_static_route_network_address_exists",
                                                                            "tags": ["PARSE_CLI", "PARSE_REST"],
                                                                            "link": self.link.check_autopeering_hosts_static_route_network_address_exists}
        self.CHECK_AUTOPEERING_HOSTS_STATIC_ROUTE_NEXTHOP_ADDRESS_EXISTS = {"constant": "check_autopeering_hosts_static_route_nexthop_address_exists",
                                                                            "tags": ["PARSE_CLI", "PARSE_REST"],
                                                                            "link": self.link.check_autopeering_hosts_static_route_nexthop_address_exists}
        self.CHECK_AUTOPEERING_HOSTS_VRF = {"constant": "check_autopeering_hosts_vrf",
                                            "tags": ["PARSE_CLI", "PARSE_REST"],
                                            "link": self.link.check_autopeering_hosts_vrf}
        self.CHECK_AUTOPEERING_HOSTS_VRF_DOES_NOT_EXIST = {"constant": "check_autopeering_hosts_vrf_does_not_exist",
                                                           "tags": ["PARSE_CLI", "PARSE_REST"],
                                                           "link": self.link.check_autopeering_hosts_vrf_does_not_exist}
        self.CHECK_AUTOPEERING_HOST_DOES_NOT_EXIST = {"constant": "check_autopeering_host_does_not_exist",
                                                      "tags": ["PARSE_CLI", "PARSE_REST"],
                                                      "link": self.link.check_autopeering_host_does_not_exist}
        self.CHECK_AUTOPEERING_HOST_EXISTS = {"constant": "check_autopeering_host_exists",
                                              "tags": ["PARSE_CLI", "PARSE_REST"],
                                              "link": self.link.check_autopeering_host_exists}
        self.CHECK_AUTOPEERING_ID = {"constant": "check_autopeering_id",
                                     "tags": ["PARSE_CLI", "PARSE_REST"],
                                     "link": self.link.check_autopeering_id}
        self.CHECK_AUTOPEERING_ROUTE_TARGET = {"constant": "check_autopeering_route_target",
                                               "tags": ["PARSE_CLI", "PARSE_REST"],
                                               "link": self.link.check_autopeering_route_target}
        self.CHECK_AUTOPEERING_SERVICE_DOES_NOT_EXIST = {"constant": "check_autopeering_service_does_not_exist",
                                                         "tags": ["PARSE_CLI", "PARSE_REST"],
                                                         "link": self.link.check_autopeering_service_does_not_exist}
        self.CHECK_AUTOPEERING_SERVICE_EXISTS = {"constant": "check_autopeering_service_exists",
                                                 "tags": ["PARSE_CLI", "PARSE_REST"],
                                                 "link": self.link.check_autopeering_service_exists}
        self.CHECK_SERVICE_ADDRESS_IP = {"constant": "check_service_address_ip",
                                         "tags": ["PARSE_CLI", "PARSE_REST"],
                                         "link": self.link.check_service_address_ip}
        self.CHECK_SERVICE_ADDRESS_PREFIX_LENGTH = {"constant": "check_service_address_prefix_length",
                                                    "tags": ["PARSE_CLI", "PARSE_REST"],
                                                    "link": self.link.check_service_address_prefix_length}
        self.CHECK_SERVICE_NSI_TYPE = {"constant": "check_service_nsi_type",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_service_nsi_type}
        self.CHECK_SERVICE_NSI_VALUE = {"constant": "check_service_nsi_value",
                                        "tags": ["PARSE_CLI", "PARSE_REST"],
                                        "link": self.link.check_service_nsi_value}
        self.CHECK_SERVICE_NSI_VRF = {"constant": "check_service_nsi_vrf",
                                      "tags": ["PARSE_CLI", "PARSE_REST"],
                                      "link": self.link.check_service_nsi_vrf}
