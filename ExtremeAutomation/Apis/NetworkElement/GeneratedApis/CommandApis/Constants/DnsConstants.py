"""
This class outlines all the constants for the dns API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DnsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DnsConstants(ApiConstants):
    def __init__(self):
        super(DnsConstants, self).__init__()
        self.CLEAR_PRIMARY_SERVER_IP = {"constant": "clear_primary_server_ip",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.clear_primary_server_ip}
        self.CLEAR_SECONDARY_SERVER_IP = {"constant": "clear_secondary_server_ip",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.clear_secondary_server_ip}
        self.CLEAR_TERTIARY_SERVER_IP = {"constant": "clear_tertiary_server_ip",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.clear_tertiary_server_ip}
        self.CREATE_DOMAIN_NAME = {"constant": "create_domain_name",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.create_domain_name}
        self.DELETE_DOMAIN_NAME = {"constant": "delete_domain_name",
                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                   "link": self.link.delete_domain_name}
        self.SET_PRIMARY_SERVER_IP = {"constant": "set_primary_server_ip",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.set_primary_server_ip}
        self.SET_SECONDARY_SERVER_IP = {"constant": "set_secondary_server_ip",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.set_secondary_server_ip}
        self.SET_TERTIARY_SERVER_IP = {"constant": "set_tertiary_server_ip",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.set_tertiary_server_ip}
        self.SHOW_DOMAIN_NAME = {"constant": "show_domain_name",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_domain_name}
        self.SHOW_HOST_BY_IP = {"constant": "show_host_by_ip",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.show_host_by_ip}
        self.SHOW_HOST_BY_NAME = {"constant": "show_host_by_name",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.show_host_by_name}
        self.SHOW_SERVERS = {"constant": "show_servers",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.show_servers}
