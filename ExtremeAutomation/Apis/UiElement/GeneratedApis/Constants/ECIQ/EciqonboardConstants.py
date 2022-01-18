"""
This class outlines all the constants for the eciqonboard API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqonboardConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqonboardConstants(ApiConstants):
    def __init__(self):
        super(EciqonboardConstants, self).__init__()
        self.BYPASS_ONBOARDING_ROUTINE = {"constant": "bypass_onboarding_routine",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.bypass_onboarding_routine}
        self.ONBOARD_DIALOG_ADD_NEW_POLICY_NAME = {"constant": "onboard_dialog_add_new_policy_name",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.onboard_dialog_add_new_policy_name}
        self.ONBOARD_DIALOG_ADD_SERIAL_NUMBER = {"constant": "onboard_dialog_add_serial_number",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.onboard_dialog_add_serial_number}
        self.ONBOARD_DIALOG_ASSIGN_LOCATION_CHECK_DEVICE_CHECKBOX = {"constant": "onboard_dialog_assign_location_check_device_checkbox",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.onboard_dialog_assign_location_check_device_checkbox}
        self.ONBOARD_DIALOG_ASSIGN_LOCATION_POPUP_CLICK_ASSIGN_BUTTON = {"constant": "onboard_dialog_assign_location_popup_click_assign_button",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.onboard_dialog_assign_location_popup_click_assign_button}
        self.ONBOARD_DIALOG_ASSIGN_LOCATION_POPUP_CLICK_CANCEL_BUTTON = {"constant": "onboard_dialog_assign_location_popup_click_cancel_button",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.onboard_dialog_assign_location_popup_click_cancel_button}
        self.ONBOARD_DIALOG_CLICK_ASSIGN_LOCATION_BUTTON = {"constant": "onboard_dialog_click_assign_location_button",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.onboard_dialog_click_assign_location_button}
        self.ONBOARD_DIALOG_CLICK_DEVICE_TYPE_REAL_BUTTON = {"constant": "onboard_dialog_click_device_type_real_button",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.onboard_dialog_click_device_type_real_button}
        self.ONBOARD_DIALOG_CLICK_DEVICE_TYPE_SIMULATED_BUTTON = {"constant": "onboard_dialog_click_device_type_simulated_button",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.onboard_dialog_click_device_type_simulated_button}
        self.ONBOARD_DIALOG_CLICK_DONE_BUTTON = {"constant": "onboard_dialog_click_done_button",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.onboard_dialog_click_done_button}
        self.ONBOARD_DIALOG_CLICK_FINISH_BUTTON = {"constant": "onboard_dialog_click_finish_button",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.onboard_dialog_click_finish_button}
        self.ONBOARD_DIALOG_CLICK_GET_STARTED_BUTTON = {"constant": "onboard_dialog_click_get_started_button",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.onboard_dialog_click_get_started_button}
        self.ONBOARD_DIALOG_CLICK_NEXT_BUTTON = {"constant": "onboard_dialog_click_next_button",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.onboard_dialog_click_next_button}
        self.ONBOARD_DIALOG_CLICK_SKIP_BUTTON = {"constant": "onboard_dialog_click_skip_button",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.onboard_dialog_click_skip_button}
        self.ONBOARD_DIALOG_SELECT_CREATE_NEW_NETWORK_POLICY = {"constant": "onboard_dialog_select_create_new_network_policy",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.onboard_dialog_select_create_new_network_policy}
        self.ONBOARD_DIALOG_SELECT_DEVICE_TYPE = {"constant": "onboard_dialog_select_device_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.onboard_dialog_select_device_type}
        self.ONBOARD_DIALOG_SELECT_NETWORK_POLICY = {"constant": "onboard_dialog_select_network_policy",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.onboard_dialog_select_network_policy}
        self.ONBOARD_DIALOG_SELECT_USE_AN_EXISTING_NETWORK_POLICY = {"constant": "onboard_dialog_select_use_an_existing_network_policy",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.onboard_dialog_select_use_an_existing_network_policy}
        self.ONBOARD_DIALOG_UNCHECK_NETWORK_POLICY_TYPE = {"constant": "onboard_dialog_uncheck_network_policy_type",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.onboard_dialog_uncheck_network_policy_type}
