"""
This class outlines all the constants for the endsystems API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EndsystemsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EndsystemsConstants(ApiConstants):
    def __init__(self):
        super(EndsystemsConstants, self).__init__()
        self.ENDSYSTEMS_CLICK_FORCE_REAUTHENTICATION_BUTTON = {"constant": "endsystems_click_force_reauthentication_button",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.endsystems_click_force_reauthentication_button}
        self.ENDSYSTEMS_CLICK_REFRESH_BUTTON = {"constant": "endsystems_click_refresh_button",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.endsystems_click_refresh_button}
        self.ENDSYSTEMS_CONFIRM_DEVICE_EXISTS_BY_IP_ADDRESS = {"constant": "endsystems_confirm_device_exists_by_ip_address",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.endsystems_confirm_device_exists_by_ip_address}
        self.ENDSYSTEMS_CONFIRM_DEVICE_EXISTS_BY_MAC_ADDRESS = {"constant": "endsystems_confirm_device_exists_by_mac_address",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.endsystems_confirm_device_exists_by_mac_address}
        self.ENDSYSTEMS_DELETE_DEVICE_BY_MAC_ADDRESS = {"constant": "endsystems_delete_device_by_mac_address",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.endsystems_delete_device_by_mac_address}
        self.ENDSYSTEMS_SELECT_DEVICE_BY_MAC_ADDRESS = {"constant": "endsystems_select_device_by_mac_address",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.endsystems_select_device_by_mac_address}
        self.ENDSYSTEMS_VERIFY_AUTHORIZATION_TYPE_DISPLAY_VALUE_IN_END_SYSTEMS_GRID = {"constant": "endsystems_verify_authorization_type_display_value_in_end_systems_grid",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.endsystems_verify_authorization_type_display_value_in_end_systems_grid}
        self.ENDSYSTEMS_VERIFY_CELL_DISPLAY_VALUE_IN_END_SYSTEMS_GRID = {"constant": "endsystems_verify_cell_display_value_in_end_systems_grid",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.endsystems_verify_cell_display_value_in_end_systems_grid}
        self.ENDSYSTEMS_VERIFY_EXTENDED_STATE_DISPLAY_VALUE_IN_END_SYSTEMS_GRID = {"constant": "endsystems_verify_extended_state_display_value_in_end_systems_grid",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.endsystems_verify_extended_state_display_value_in_end_systems_grid}
        self.ENDSYSTEMS_VERIFY_STATE_OR_RISK_IN_END_SYSTEMS_GRID = {"constant": "endsystems_verify_state_or_risk_in_end_systems_grid",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.endsystems_verify_state_or_risk_in_end_systems_grid}
