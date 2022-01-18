"""
This class outlines all the constants for the vrrp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VrrpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VrrpConstants(ApiConstants):
    def __init__(self):
        super(VrrpConstants, self).__init__()
        self.CLEAR_GROUP = {"constant": "clear_group",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.clear_group}
        self.CLEAR_VLAN = {"constant": "clear_vlan",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.clear_vlan}
        self.CREATE_GROUP = {"constant": "create_group",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.create_group}
        self.CREATE_VLAN = {"constant": "create_vlan",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.create_vlan}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.DISABLE_VLAN = {"constant": "disable_vlan",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_vlan}
        self.DISABLE_VLAN_FABRIC_ROUTING = {"constant": "disable_vlan_fabric_routing",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_vlan_fabric_routing}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.ENABLE_VLAN = {"constant": "enable_vlan",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_vlan}
        self.ENABLE_VLAN_FABRIC_ROUTING = {"constant": "enable_vlan_fabric_routing",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_vlan_fabric_routing}
        self.SET_VLAN_IPADDRESS = {"constant": "set_vlan_ipaddress",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_vlan_ipaddress}
        self.SET_VLAN_PRIORITY = {"constant": "set_vlan_priority",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_vlan_priority}
        self.SHOW_ALL = {"constant": "show_all",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_all}
        self.SHOW_DETAIL = {"constant": "show_detail",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_detail}
        self.SHOW_GROUP = {"constant": "show_group",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_group}
        self.SHOW_GROUP_ALL = {"constant": "show_group_all",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_group_all}
        self.SHOW_VIRTUAL_ROUTER = {"constant": "show_virtual_router",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_virtual_router}
        self.SHOW_VIRTUAL_ROUTER_ALL = {"constant": "show_virtual_router_all",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_virtual_router_all}
        self.SHOW_VLAN = {"constant": "show_vlan",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_vlan}
        self.SHOW_VR = {"constant": "show_vr",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.show_vr}
        self.SHOW_VR_ALL = {"constant": "show_vr_all",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_vr_all}
