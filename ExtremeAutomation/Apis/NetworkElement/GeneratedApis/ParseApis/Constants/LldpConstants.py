"""
This class outlines all the constants for the lldp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(LldpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class LldpConstants(ApiConstants):
    def __init__(self):
        super(LldpConstants, self).__init__()
        self.CHECK_LLDP_NEIGHBOR_SYSNAME = {"constant": "check_lldp_neighbor_sysname",
                                            "tags": ["PARSE_CLI", "PARSE_REST"],
                                            "link": self.link.check_lldp_neighbor_sysname}
        self.CHECK_LLDP_REMOTE_PORT = {"constant": "check_lldp_remote_port",
                                       "tags": ["PARSE_CLI", "PARSE_REST"],
                                       "link": self.link.check_lldp_remote_port}
        self.CHECK_LLDP_SYS_NAME = {"constant": "check_lldp_sys_name",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_lldp_sys_name}
        self.CHECK_LLDP_TX_HOLD_MULTIPLIER = {"constant": "check_lldp_tx_hold_multiplier",
                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                              "link": self.link.check_lldp_tx_hold_multiplier}
        self.CHECK_LLDP_TX_INTERVAL = {"constant": "check_lldp_tx_interval",
                                       "tags": ["PARSE_CLI", "PARSE_REST", "PARSE_SNMP"],
                                       "link": self.link.check_lldp_tx_interval}
        self.CHECK_TLV_STATUS = {"constant": "check_tlv_status",
                                 "tags": ["PARSE_CLI", "PARSE_REST"],
                                 "link": self.link.check_tlv_status}
        self.DETERMINE_LLDP_PORT_RECEIVE_STATE = {"constant": "determine_lldp_port_receive_state",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.determine_lldp_port_receive_state}
        self.DETERMINE_LLDP_PORT_TRANSMIT_STATE = {"constant": "determine_lldp_port_transmit_state",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.determine_lldp_port_transmit_state}
