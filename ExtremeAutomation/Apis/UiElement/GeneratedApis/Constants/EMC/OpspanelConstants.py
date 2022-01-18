"""
This class outlines all the constants for the opspanel API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(OpspanelConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class OpspanelConstants(ApiConstants):
    def __init__(self):
        super(OpspanelConstants, self).__init__()
        self.OPSPANEL_CLICK_CLEAR_ALL = {"constant": "opspanel_click_clear_all",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.opspanel_click_clear_all}
        self.OPSPANEL_CLICK_OPERATIONS = {"constant": "opspanel_click_operations",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.opspanel_click_operations}
        self.OPSPANEL_CONFIRM_ALL_PARAMETERS_EXIST = {"constant": "opspanel_confirm_all_parameters_exist",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.opspanel_confirm_all_parameters_exist}
        self.OPSPANEL_CONFIRM_MESSAGE_EXISTS = {"constant": "opspanel_confirm_message_exists",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.opspanel_confirm_message_exists}
        self.OPSPANEL_CONFIRM_RESULT_EXISTS = {"constant": "opspanel_confirm_result_exists",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.opspanel_confirm_result_exists}
        self.OPSPANEL_CONFIRM_TARGET_EXISTS = {"constant": "opspanel_confirm_target_exists",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.opspanel_confirm_target_exists}
        self.OPSPANEL_CONFIRM_TYPE_EXISTS = {"constant": "opspanel_confirm_type_exists",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.opspanel_confirm_type_exists}
