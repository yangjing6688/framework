"""
This class outlines all the constants for the arp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ArpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ArpConstants(ApiConstants):
    def __init__(self):
        super(ArpConstants, self).__init__()
        self.CLEAR_ALL_ENTRIES = {"constant": "clear_all_entries",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_all_entries}
        self.CREATE_ENTRY = {"constant": "create_entry",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.create_entry}
        self.CREATE_ENTRY_INTERFACE = {"constant": "create_entry_interface",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.create_entry_interface}
        self.CREATE_ENTRY_PORT = {"constant": "create_entry_port",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.create_entry_port}
        self.CREATE_ENTRY_PORT_VLAN = {"constant": "create_entry_port_vlan",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.create_entry_port_vlan}
        self.DELETE_ENTRY = {"constant": "delete_entry",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.delete_entry}
        self.SHOW_ALL_ENTRIES = {"constant": "show_all_entries",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_all_entries}
        self.SHOW_ENTRY = {"constant": "show_entry",
                           "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                           "link": self.link.show_entry}
        self.SHOW_VRF_ENTRY = {"constant": "show_vrf_entry",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.show_vrf_entry}
