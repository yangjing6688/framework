"""
This class outlines all the constants for the vxlan API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VxlanConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VxlanConstants(ApiConstants):
    def __init__(self):
        super(VxlanConstants, self).__init__()
        self.CLEAR_REMOTE_VTEP = {"constant": "clear_remote_vtep",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_remote_vtep}
        self.CREATE_LOGICAL_SWITCH = {"constant": "create_logical_switch",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.create_logical_switch}
        self.CREATE_LOGICAL_SWITCH_TO_VLAN_MAP = {"constant": "create_logical_switch_to_vlan_map",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.create_logical_switch_to_vlan_map}
        self.CREATE_LOGICAL_SWITCH_TO_VNI_MAP = {"constant": "create_logical_switch_to_vni_map",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.create_logical_switch_to_vni_map}
        self.CREATE_LOGICAL_SWITCH_VNI_VLAN_MAP = {"constant": "create_logical_switch_vni_vlan_map",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.create_logical_switch_vni_vlan_map}
        self.DELETE_LOGICAL_SWITCH = {"constant": "delete_logical_switch",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.delete_logical_switch}
        self.SET_REMOTE_VTEP = {"constant": "set_remote_vtep",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_remote_vtep}
        self.SHOW_LOGICAL_SWITCH = {"constant": "show_logical_switch",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_logical_switch}
