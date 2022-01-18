"""
This class outlines all the constants for the dvr API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DvrConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DvrConstants(ApiConstants):
    def __init__(self):
        super(DvrConstants, self).__init__()
        self.CLEAR_DOMAIN_CONTROLLER = {"constant": "clear_domain_controller",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_domain_controller}
        self.CLEAR_HOST_ENTRIES = {"constant": "clear_host_entries",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_host_entries}
        self.CLEAR_HOST_ENTRIES_IPV4 = {"constant": "clear_host_entries_ipv4",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.clear_host_entries_ipv4}
        self.CLEAR_HOST_ENTRIES_IPV4_L3ISID = {"constant": "clear_host_entries_ipv4_l3isid",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.clear_host_entries_ipv4_l3isid}
        self.CLEAR_HOST_ENTRIES_L2ISID = {"constant": "clear_host_entries_l2isid",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_host_entries_l2isid}
        self.CLEAR_HOST_ENTRIES_L3ISID = {"constant": "clear_host_entries_l3isid",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_host_entries_l3isid}
        self.CLEAR_INTERFACE_GATEWAY_IPV4 = {"constant": "clear_interface_gateway_ipv4",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.clear_interface_gateway_ipv4}
        self.CLEAR_LEAF_VIRTUAL_IST = {"constant": "clear_leaf_virtual_ist",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_leaf_virtual_ist}
        self.CLEAR_REDISTRIBUTE_DIRECT = {"constant": "clear_redistribute_direct",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_redistribute_direct}
        self.CLEAR_REDISTRIBUTE_STATIC = {"constant": "clear_redistribute_static",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_redistribute_static}
        self.DISABLE_DOMAIN_CONTROLLER_INJECT_DEFAULT_ROUTE = {"constant": "disable_domain_controller_inject_default_route",
                                                               "tags": ["COMMAND_CLI"],
                                                               "link": self.link.disable_domain_controller_inject_default_route}
        self.DISABLE_DOMAIN_CONTROLLER_INJECT_DEFAULT_ROUTE_ALL = {"constant": "disable_domain_controller_inject_default_route_all",
                                                                   "tags": ["COMMAND_CLI"],
                                                                   "link": self.link.disable_domain_controller_inject_default_route_all}
        self.DISABLE_INTERFACE = {"constant": "disable_interface",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_interface}
        self.DISABLE_REDISTRIBUTE_DIRECT = {"constant": "disable_redistribute_direct",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_redistribute_direct}
        self.DISABLE_REDISTRIBUTE_STATIC = {"constant": "disable_redistribute_static",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_redistribute_static}
        self.ENABLE_INTERFACE = {"constant": "enable_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_interface}
        self.ENABLE_REDISTRIBUTE_DIRECT = {"constant": "enable_redistribute_direct",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_redistribute_direct}
        self.ENABLE_REDISTRIBUTE_STATIC = {"constant": "enable_redistribute_static",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_redistribute_static}
        self.SET_DOMAIN_CONTROLLER = {"constant": "set_domain_controller",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_domain_controller}
        self.SET_INTERFACE_GATEWAY_IPV4 = {"constant": "set_interface_gateway_ipv4",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_interface_gateway_ipv4}
        self.SET_LEAF_ID = {"constant": "set_leaf_id",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_leaf_id}
        self.SET_LEAF_VIRTUAL_IST = {"constant": "set_leaf_virtual_ist",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_leaf_virtual_ist}
        self.SET_REDISTRIBUTE = {"constant": "set_redistribute",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_redistribute}
        self.SET_REDISTRIBUTE_DIRECT = {"constant": "set_redistribute_direct",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_redistribute_direct}
        self.SET_REDISTRIBUTE_DIRECT_METRIC = {"constant": "set_redistribute_direct_metric",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.set_redistribute_direct_metric}
        self.SET_REDISTRIBUTE_STATIC = {"constant": "set_redistribute_static",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_redistribute_static}
        self.SET_REDISTRIBUTE_STATIC_METRIC = {"constant": "set_redistribute_static_metric",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.set_redistribute_static_metric}
        self.SET_REDISTRIBUTE_VRF = {"constant": "set_redistribute_vrf",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_redistribute_vrf}
        self.SHOW_BACKBONE_ENTRIES = {"constant": "show_backbone_entries",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_backbone_entries}
        self.SHOW_BACKBONE_MEMBERS = {"constant": "show_backbone_members",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_backbone_members}
        self.SHOW_DATABASE = {"constant": "show_database",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_database}
        self.SHOW_HOST_ENTRIES = {"constant": "show_host_entries",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_host_entries}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
        self.SHOW_INTERFACES = {"constant": "show_interfaces",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_interfaces}
        self.SHOW_L3VSN = {"constant": "show_l3vsn",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_l3vsn}
        self.SHOW_MEMBERS = {"constant": "show_members",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_members}
        self.SHOW_REDISTRIBUTE = {"constant": "show_redistribute",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_redistribute}
        self.SHOW_ROUTES = {"constant": "show_routes",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_routes}
