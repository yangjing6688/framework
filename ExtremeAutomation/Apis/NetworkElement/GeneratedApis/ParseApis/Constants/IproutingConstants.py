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
        self.STORE_DEFAULT_GATEWAY = {"constant": "store_default_gateway",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.store_default_gateway}
        self.VALIDATE_IPV6_ROUTE_ENTRY = {"constant": "validate_ipv6_route_entry",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.validate_ipv6_route_entry}
        self.VALIDATE_IPV6_VRF_ROUTE_ENTRY = {"constant": "validate_ipv6_vrf_route_entry",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.validate_ipv6_vrf_route_entry}
        self.VALIDATE_ROUTE_ENTRY = {"constant": "validate_route_entry",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.validate_route_entry}
        self.VALIDATE_STATIC_ROUTE_INT_EXISTS = {"constant": "validate_static_route_int_exists",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.validate_static_route_int_exists}
        self.VALIDATE_VRF_ROUTE_ENTRY = {"constant": "validate_vrf_route_entry",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.validate_vrf_route_entry}
