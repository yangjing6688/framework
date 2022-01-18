"""
This class outlines all the constants for the ntp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NtpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NtpConstants(ApiConstants):
    def __init__(self):
        super(NtpConstants, self).__init__()
        self.CLEAR_AUTH_KEY = {"constant": "clear_auth_key",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.clear_auth_key}
        self.CREATE_SERVER = {"constant": "create_server",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.create_server}
        self.CREATE_SERVER_KEY = {"constant": "create_server_key",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.create_server_key}
        self.CREATE_SERVER_PRECEDENCE = {"constant": "create_server_precedence",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.create_server_precedence}
        self.CREATE_SERVER_PRECEDENCE_KEY = {"constant": "create_server_precedence_key",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.create_server_precedence_key}
        self.DELETE_SERVER = {"constant": "delete_server",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.delete_server}
        self.DISABLE_CLIENT = {"constant": "disable_client",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_client}
        self.DISABLE_CLIENT_VLAN = {"constant": "disable_client_vlan",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_client_vlan}
        self.DISABLE_SERVER = {"constant": "disable_server",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.disable_server}
        self.DISABLE_SERVER_AUTH = {"constant": "disable_server_auth",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.disable_server_auth}
        self.ENABLE_CLIENT = {"constant": "enable_client",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_client}
        self.ENABLE_CLIENT_VLAN = {"constant": "enable_client_vlan",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_client_vlan}
        self.ENABLE_SERVER = {"constant": "enable_server",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.enable_server}
        self.ENABLE_SERVER_AUTH = {"constant": "enable_server_auth",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.enable_server_auth}
        self.SET_AUTH = {"constant": "set_auth",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.set_auth}
        self.SET_AUTH_KEY = {"constant": "set_auth_key",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.set_auth_key}
        self.SET_AUTH_MD5 = {"constant": "set_auth_md5",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.set_auth_md5}
        self.SET_AUTH_SHA1 = {"constant": "set_auth_sha1",
                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                              "link": self.link.set_auth_sha1}
        self.SET_GLOBAL_INTERVAL = {"constant": "set_global_interval",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.set_global_interval}
        self.SET_SERVER_SOURCE_IP = {"constant": "set_server_source_ip",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.set_server_source_ip}
        self.SET_SOURCE_IP_CHASSIS = {"constant": "set_source_ip_chassis",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_source_ip_chassis}
        self.SET_SOURCE_IP_MM = {"constant": "set_source_ip_mm",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_source_ip_mm}
        self.SHOW_ASSOCIATION = {"constant": "show_association",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_association}
        self.SHOW_ASSOCIATION_DETAIL = {"constant": "show_association_detail",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_association_detail}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_info}
        self.SHOW_KEY = {"constant": "show_key",
                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                         "link": self.link.show_key}
        self.SHOW_SERVERS = {"constant": "show_servers",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.show_servers}
        self.SHOW_STATISTICS = {"constant": "show_statistics",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.show_statistics}
