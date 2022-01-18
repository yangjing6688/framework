"""
This class outlines all the constants for the dhcp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DhcpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DhcpConstants(ApiConstants):
    def __init__(self):
        super(DhcpConstants, self).__init__()
        self.CLEAR_ADDRESS_RANGE = {"constant": "clear_address_range",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.clear_address_range}
        self.CLEAR_GLOBAL = {"constant": "clear_global",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.clear_global}
        self.CLEAR_LEASE_TIME = {"constant": "clear_lease_time",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_lease_time}
        self.CLEAR_NETLOGIN_LEASE_TIME = {"constant": "clear_netlogin_lease_time",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_netlogin_lease_time}
        self.CLEAR_OPTIONS_DNS = {"constant": "clear_options_dns",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_options_dns}
        self.CLEAR_OPTIONS_DNS_PRI = {"constant": "clear_options_dns_pri",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.clear_options_dns_pri}
        self.CLEAR_OPTIONS_DNS_SEC = {"constant": "clear_options_dns_sec",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.clear_options_dns_sec}
        self.CLEAR_OPTIONS_GATEWAY = {"constant": "clear_options_gateway",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.clear_options_gateway}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_port}
        self.DISABLE_VLAN = {"constant": "disable_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_vlan}
        self.ENABLE_BOOTPRELAY_VLAN = {"constant": "enable_bootprelay_vlan",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.enable_bootprelay_vlan}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_port}
        self.ENABLE_VLAN = {"constant": "enable_vlan",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_vlan}
        self.SET_ADDRESS_RANGE = {"constant": "set_address_range",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_address_range}
        self.SET_BOOTPRELAY_IP = {"constant": "set_bootprelay_ip",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_bootprelay_ip}
        self.SET_LEASE_TIME = {"constant": "set_lease_time",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_lease_time}
        self.SET_NETLOGIN_LEASE_TIME = {"constant": "set_netlogin_lease_time",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_netlogin_lease_time}
        self.SET_OPTIONS_DNS = {"constant": "set_options_dns",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_options_dns}
        self.SET_OPTIONS_DNS_PRI = {"constant": "set_options_dns_pri",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_options_dns_pri}
        self.SET_OPTIONS_DNS_SEC = {"constant": "set_options_dns_sec",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_options_dns_sec}
        self.SET_OPTIONS_GATEWAY = {"constant": "set_options_gateway",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_options_gateway}
        self.SHOW_ADDRESS_ALLOCATION = {"constant": "show_address_allocation",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_address_allocation}
        self.SHOW_BOOTPRELAY_INFO = {"constant": "show_bootprelay_info",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_bootprelay_info}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
