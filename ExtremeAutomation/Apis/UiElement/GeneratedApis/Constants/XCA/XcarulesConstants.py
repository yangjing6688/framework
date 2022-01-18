"""
This class outlines all the constants for the xcarules API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcarulesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcarulesConstants(ApiConstants):
    def __init__(self):
        super(XcarulesConstants, self).__init__()
        self.CLICK_ADD_TO_CREATE_NEW_RULE = {"constant": "click_add_to_create_new_rule",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.click_add_to_create_new_rule}
        self.CLICK_RULE_NAME_TO_MOVE_DOWN = {"constant": "click_rule_name_to_move_down",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.click_rule_name_to_move_down}
        self.CLICK_RULE_NAME_TO_MOVE_UP = {"constant": "click_rule_name_to_move_up",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.click_rule_name_to_move_up}
        self.CLICK_RULE_NAME_TO_OPEN_RULE_SETTINGS = {"constant": "click_rule_name_to_open_rule_settings",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.click_rule_name_to_open_rule_settings}
        self.CONFIG_RULE_ACTIONS = {"constant": "config_rule_actions",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.config_rule_actions}
        self.CONFIG_RULE_CONDITIONS = {"constant": "config_rule_conditions",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.config_rule_conditions}
        self.CONFIG_RULE_NAME_AND_ENABLED = {"constant": "config_rule_name_and_enabled",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.config_rule_name_and_enabled}
        self.DELETE_RULE_IN_CONFIG_PAGE = {"constant": "delete_rule_in_config_page",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.delete_rule_in_config_page}
        self.DELETE_RULE_IN_RULES_PAGE = {"constant": "delete_rule_in_rules_page",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.delete_rule_in_rules_page}
        self.SAVE_CONFIG_AND_BACK_TO_RULES_PAGE = {"constant": "save_config_and_back_to_rules_page",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.save_config_and_back_to_rules_page}
        self.VERIFY_CONTROL_RULE_DOES_NOT_EXIST = {"constant": "verify_control_rule_does_not_exist",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.verify_control_rule_does_not_exist}
        self.VERIFY_CONTROL_RULE_EXISTS = {"constant": "verify_control_rule_exists",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.verify_control_rule_exists}
