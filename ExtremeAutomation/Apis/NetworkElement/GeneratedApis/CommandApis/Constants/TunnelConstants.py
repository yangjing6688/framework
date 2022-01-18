"""
This class outlines all the constants for the tunnel API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(TunnelConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class TunnelConstants(ApiConstants):
    def __init__(self):
        super(TunnelConstants, self).__init__()
        self.CLEAR_DEST_IP = {"constant": "clear_dest_ip",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.clear_dest_ip}
        self.CLEAR_MODE_GRE = {"constant": "clear_mode_gre",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_mode_gre}
        self.CLEAR_SOURCE_IP = {"constant": "clear_source_ip",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.clear_source_ip}
        self.CREATE_INTERFACE = {"constant": "create_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.create_interface}
        self.DELETE_INTERFACE = {"constant": "delete_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.delete_interface}
        self.DISABLE_INTERFACE = {"constant": "disable_interface",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.disable_interface}
        self.ENABLE_INTERFACE = {"constant": "enable_interface",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.enable_interface}
        self.SET_DEST_IP = {"constant": "set_dest_ip",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_dest_ip}
        self.SET_MODE_GRE = {"constant": "set_mode_gre",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_mode_gre}
        self.SET_MODE_GRE_L2_PORT = {"constant": "set_mode_gre_l2_port",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_mode_gre_l2_port}
        self.SET_MODE_VXLAN = {"constant": "set_mode_vxlan",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_mode_vxlan}
        self.SET_MODE_VXLAN_L2TB_PORT = {"constant": "set_mode_vxlan_l2tb_port",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_mode_vxlan_l2tb_port}
        self.SET_SOURCE_IP = {"constant": "set_source_ip",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.set_source_ip}
        self.SHOW_ALL = {"constant": "show_all",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_all}
        self.SHOW_TUNNEL = {"constant": "show_tunnel",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.show_tunnel}
