"""
This class outlines all the constants for the xcaroles API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcarolesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcarolesConstants(ApiConstants):
    def __init__(self):
        super(XcarolesConstants, self).__init__()
        self.CLICK_ADD_TO_CREATE_NEW_POLICY_ROLE = {"constant": "click_add_to_create_new_policy_role",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.click_add_to_create_new_policy_role}
        self.CLICK_POLICY_ROLE_NAME_TO_OPEN_ROLE_SETTINGS = {"constant": "click_policy_role_name_to_open_role_settings",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.click_policy_role_name_to_open_role_settings}
        self.CREATE_APPLICATION_RULE_ON_POLICY_ROLE = {"constant": "create_application_rule_on_policy_role",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.create_application_rule_on_policy_role}
        self.CREATE_MAC_RULE_ON_POLICY_ROLE = {"constant": "create_mac_rule_on_policy_role",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.create_mac_rule_on_policy_role}
        self.CREATE_NETWORK_RULE_ON_POLICY_ROLE = {"constant": "create_network_rule_on_policy_role",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.create_network_rule_on_policy_role}
        self.DELETE_APPLICATION_RULE_ON_POLICY_ROLE = {"constant": "delete_application_rule_on_policy_role",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.delete_application_rule_on_policy_role}
        self.DELETE_MAC_RULE_ON_POLICY_ROLE = {"constant": "delete_mac_rule_on_policy_role",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.delete_mac_rule_on_policy_role}
        self.DELETE_NETWORK_RULE_ON_POLICY_ROLE = {"constant": "delete_network_rule_on_policy_role",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.delete_network_rule_on_policy_role}
        self.DELETE_POLICY_ROLE = {"constant": "delete_policy_role",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.delete_policy_role}
        self.EDIT_ROLE_NAME = {"constant": "edit_role_name",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.edit_role_name}
        self.SAVE_ROLES_SETTINGS = {"constant": "save_roles_settings",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.save_roles_settings}
        self.VERIFY_NETWORK_RULE_DOES_NOT_EXIST_ON_POLICY_ROLE = {"constant": "verify_network_rule_does_not_exist_on_policy_role",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.verify_network_rule_does_not_exist_on_policy_role}
        self.VERIFY_NETWORK_RULE_EXISTS_ON_POLICY_ROLE = {"constant": "verify_network_rule_exists_on_policy_role",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.verify_network_rule_exists_on_policy_role}
        self.VERIFY_POLICY_ROLE_DOES_NOT_EXIST = {"constant": "verify_policy_role_does_not_exist",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.verify_policy_role_does_not_exist}
        self.VERIFY_POLICY_ROLE_EXISTS = {"constant": "verify_policy_role_exists",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.verify_policy_role_exists}
