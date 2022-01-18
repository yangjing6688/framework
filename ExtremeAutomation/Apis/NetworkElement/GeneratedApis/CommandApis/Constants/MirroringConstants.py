"""
This class outlines all the constants for the mirroring API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MirroringConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MirroringConstants(ApiConstants):
    def __init__(self):
        super(MirroringConstants, self).__init__()
        self.CLEAR_SOURCE_PORT = {"constant": "clear_source_port",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_source_port}
        self.CREATE_BOTH = {"constant": "create_both",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.create_both}
        self.CREATE_EGRESS = {"constant": "create_egress",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.create_egress}
        self.CREATE_INGRESS = {"constant": "create_ingress",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.create_ingress}
        self.CREATE_PORTLIST = {"constant": "create_portlist",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.create_portlist}
        self.CREATE_REMOTE_BOTH = {"constant": "create_remote_both",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.create_remote_both}
        self.DELETE_PORT_MIRROR = {"constant": "delete_port_mirror",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.delete_port_mirror}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_port}
        self.DISABLE_REMOTE_PING_CHECK = {"constant": "disable_remote_ping_check",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.disable_remote_ping_check}
        self.ENABLE_PORT = {"constant": "enable_port",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.enable_port}
        self.ENABLE_REMOTE_PING_CHECK = {"constant": "enable_remote_ping_check",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.enable_remote_ping_check}
        self.SET_DESCRIPTION = {"constant": "set_description",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_description}
        self.SET_SOURCE_PORT_BOTH = {"constant": "set_source_port_both",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_source_port_both}
        self.SET_SOURCE_PORT_EGRESS = {"constant": "set_source_port_egress",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_source_port_egress}
        self.SET_SOURCE_PORT_INGRESS = {"constant": "set_source_port_ingress",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_source_port_ingress}
        self.SET_SOURCE_PORT_VLAN = {"constant": "set_source_port_vlan",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_source_port_vlan}
        self.SHOW_PORT_MIRROR = {"constant": "show_port_mirror",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_port_mirror}
        self.SHOW_PORT_MIRROR_ALL = {"constant": "show_port_mirror_all",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_port_mirror_all}
