"""
This class outlines all the constants for the vpex API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VpexConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VpexConstants(ApiConstants):
    def __init__(self):
        super(VpexConstants, self).__init__()
        self.CHECK_ALL_CASCADE_PORTS = {"constant": "check_all_cascade_ports",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.check_all_cascade_ports}
        self.CHECK_VPEX_RING_REBALANCING_SET_TO_AUTO = {"constant": "check_vpex_ring_rebalancing_set_to_auto",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.check_vpex_ring_rebalancing_set_to_auto}
        self.CHECK_VPEX_SET_ON_PORT = {"constant": "check_vpex_set_on_port",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_vpex_set_on_port}
        self.CHECK_VPEX_TOPOLOGY_ON_PORT = {"constant": "check_vpex_topology_on_port",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_vpex_topology_on_port}
        self.VERIFY_VPEX_AUTO_CONFIGURATION_ENABLED = {"constant": "verify_vpex_auto_configuration_enabled",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.verify_vpex_auto_configuration_enabled}
        self.VERIFY_VPEX_ENABLED = {"constant": "verify_vpex_enabled",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.verify_vpex_enabled}
