"""
This class outlines all the constants for the cloudconnectfsm API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CloudconnectfsmConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CloudconnectfsmConstants(ApiConstants):
    def __init__(self):
        super(CloudconnectfsmConstants, self).__init__()
        self.ADD_CONFIG_ENTRY_FOR_SERIAL = {"constant": "add_config_entry_for_serial",
                                            "tags": ["COMMAND_REST"],
                                            "link": self.link.add_config_entry_for_serial}
        self.ADD_CONNECT_ENTRY_FOR_SERIAL = {"constant": "add_connect_entry_for_serial",
                                             "tags": ["COMMAND_REST"],
                                             "link": self.link.add_connect_entry_for_serial}
        self.ADD_STATS_REPLY_FOR_SERIAL = {"constant": "add_stats_reply_for_serial",
                                           "tags": ["COMMAND_REST"],
                                           "link": self.link.add_stats_reply_for_serial}
        self.ADD_UPGRADE_ENTRY_FOR_SERIAL = {"constant": "add_upgrade_entry_for_serial",
                                             "tags": ["COMMAND_REST"],
                                             "link": self.link.add_upgrade_entry_for_serial}
        self.ALLOW_CONFIG_STATE_TIMEOUT = {"constant": "allow_config_state_timeout",
                                           "tags": ["COMMAND_REST"],
                                           "link": self.link.allow_config_state_timeout}
        self.ALLOW_CONNECT_STATE_TIMEOUT = {"constant": "allow_connect_state_timeout",
                                            "tags": ["COMMAND_REST"],
                                            "link": self.link.allow_connect_state_timeout}
        self.ALLOW_UPGRADE_STATE_TIMEOUT = {"constant": "allow_upgrade_state_timeout",
                                            "tags": ["COMMAND_REST"],
                                            "link": self.link.allow_upgrade_state_timeout}
        self.CHECK_DEVICE_STATES = {"constant": "check_device_states",
                                    "tags": ["COMMAND_REST"],
                                    "link": self.link.check_device_states}
        self.CLEAR_FSM_STATES_BY_SERIAL = {"constant": "clear_fsm_states_by_serial",
                                           "tags": ["COMMAND_REST"],
                                           "link": self.link.clear_fsm_states_by_serial}
        self.REMOVE_CONFIG_ENTRY_FOR_SERIAL = {"constant": "remove_config_entry_for_serial",
                                               "tags": ["COMMAND_REST"],
                                               "link": self.link.remove_config_entry_for_serial}
        self.REMOVE_CONNECT_ENTRY_FOR_SERIAL = {"constant": "remove_connect_entry_for_serial",
                                                "tags": ["COMMAND_REST"],
                                                "link": self.link.remove_connect_entry_for_serial}
        self.REMOVE_UPGRADE_ENTRY_FOR_SERIAL = {"constant": "remove_upgrade_entry_for_serial",
                                                "tags": ["COMMAND_REST"],
                                                "link": self.link.remove_upgrade_entry_for_serial}
        self.SHOW_DEVICE_VERSION = {"constant": "show_device_version",
                                    "tags": ["COMMAND_REST"],
                                    "link": self.link.show_device_version}
        self.SHOW_MGMT_IP = {"constant": "show_mgmt_ip",
                             "tags": ["COMMAND_REST"],
                             "link": self.link.show_mgmt_ip}
