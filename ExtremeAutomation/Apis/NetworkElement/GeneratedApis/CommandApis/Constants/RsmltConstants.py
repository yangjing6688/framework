"""
This class outlines all the constants for the rsmlt API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(RsmltConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class RsmltConstants(ApiConstants):
    def __init__(self):
        super(RsmltConstants, self).__init__()
        self.DISABLE_EDGE_SUPPORT = {"constant": "disable_edge_support",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.disable_edge_support}
        self.DISABLE_VLAN_INTERFACE = {"constant": "disable_vlan_interface",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.disable_vlan_interface}
        self.ENABLE_EDGE_SUPPORT = {"constant": "enable_edge_support",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_edge_support}
        self.ENABLE_VLAN_INTERFACE = {"constant": "enable_vlan_interface",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.enable_vlan_interface}
        self.SET_INTERFACE_HOLDDOWN_TIMER = {"constant": "set_interface_holddown_timer",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_interface_holddown_timer}
        self.SET_INTERFACE_HOLDUP_TIMER = {"constant": "set_interface_holdup_timer",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_interface_holdup_timer}
        self.SHOW_EDGE_SUPPORT = {"constant": "show_edge_support",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_edge_support}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
        self.SHOW_LOCAL = {"constant": "show_local",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_local}
        self.SHOW_LOCAL_VRF = {"constant": "show_local_vrf",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_local_vrf}
        self.SHOW_LOCAL_VRFID = {"constant": "show_local_vrfid",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_local_vrfid}
        self.SHOW_PEER = {"constant": "show_peer",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_peer}
        self.SHOW_PEER_VRF = {"constant": "show_peer_vrf",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_peer_vrf}
        self.SHOW_PEER_VRFID = {"constant": "show_peer_vrfid",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_peer_vrfid}
        self.SHOW_VRF = {"constant": "show_vrf",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_vrf}
        self.SHOW_VRFID = {"constant": "show_vrfid",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_vrfid}
