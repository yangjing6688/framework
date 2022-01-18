"""
This class outlines all the constants for the mlag API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MlagConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MlagConstants(ApiConstants):
    def __init__(self):
        super(MlagConstants, self).__init__()
        self.CREATE_PEER = {"constant": "create_peer",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.create_peer}
        self.CREATE_PEER_AUTH_MD5_KEY = {"constant": "create_peer_auth_md5_key",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.create_peer_auth_md5_key}
        self.CREATE_PEER_AUTH_MD5_KEY_ENCRYPTED = {"constant": "create_peer_auth_md5_key_encrypted",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.create_peer_auth_md5_key_encrypted}
        self.CREATE_PEER_AUTH_MD5_KEY_NAME = {"constant": "create_peer_auth_md5_key_name",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.create_peer_auth_md5_key_name}
        self.DELETE_PEER = {"constant": "delete_peer",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.delete_peer}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.disable_port}
        self.DISABLE_PORT_RELOAD_DELAY = {"constant": "disable_port_reload_delay",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.disable_port_reload_delay}
        self.ENABLE_PORT_PEER_ID = {"constant": "enable_port_peer_id",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_port_peer_id}
        self.ENABLE_PORT_RELOAD_DELAY = {"constant": "enable_port_reload_delay",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.enable_port_reload_delay}
        self.SET_PEER = {"constant": "set_peer",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.set_peer}
        self.SET_PEER_ALTERNATE_IP = {"constant": "set_peer_alternate_ip",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_peer_alternate_ip}
        self.SET_PEER_ALTERNATE_IP_NONE = {"constant": "set_peer_alternate_ip_none",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_peer_alternate_ip_none}
        self.SET_PEER_ALTERNATE_IP_VR = {"constant": "set_peer_alternate_ip_vr",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_peer_alternate_ip_vr}
        self.SET_PEER_AUTH_MD5_KEY = {"constant": "set_peer_auth_md5_key",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_peer_auth_md5_key}
        self.SET_PEER_AUTH_MD5_KEY_ENCRYPTED = {"constant": "set_peer_auth_md5_key_encrypted",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.set_peer_auth_md5_key_encrypted}
        self.SET_PEER_AUTH_MD5_KEY_NAME = {"constant": "set_peer_auth_md5_key_name",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_peer_auth_md5_key_name}
        self.SET_PEER_AUTH_NONE = {"constant": "set_peer_auth_none",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_peer_auth_none}
        self.SET_PEER_INTERVAL = {"constant": "set_peer_interval",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_peer_interval}
        self.SET_PEER_IPADDRESS = {"constant": "set_peer_ipaddress",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_peer_ipaddress}
        self.SET_PEER_IPADDRESS_VR = {"constant": "set_peer_ipaddress_vr",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_peer_ipaddress_vr}
        self.SET_PEER_LACP_MAC = {"constant": "set_peer_lacp_mac",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_peer_lacp_mac}
        self.SET_PEER_LACP_MAC_AUTO = {"constant": "set_peer_lacp_mac_auto",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_peer_lacp_mac_auto}
        self.SET_PEER_NEW_NAME = {"constant": "set_peer_new_name",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_peer_new_name}
        self.SHOW_PEER = {"constant": "show_peer",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_peer}
        self.SHOW_PEER_ALL = {"constant": "show_peer_all",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_peer_all}
        self.SHOW_PORTS = {"constant": "show_ports",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_ports}
        self.SHOW_PORTS_ALL = {"constant": "show_ports_all",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_ports_all}
