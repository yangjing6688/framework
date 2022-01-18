"""
This class outlines all the constants for the eciqnetworkpolicies API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqnetworkpoliciesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqnetworkpoliciesConstants(ApiConstants):
    def __init__(self):
        super(EciqnetworkpoliciesConstants, self).__init__()
        self.NETWORK_POLICIES_CLICK_ADD_NETWORK_POLICY_BUTTON = {"constant": "network_policies_click_add_network_policy_button",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.network_policies_click_add_network_policy_button}
        self.NETWORK_POLICIES_CLICK_EXPRESS_POLICY_SETUP_BUTTON = {"constant": "network_policies_click_express_policy_setup_button",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.network_policies_click_express_policy_setup_button}
        self.NETWORK_POLICIES_DELETE_NETWORK_POLICY = {"constant": "network_policies_delete_network_policy",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.network_policies_delete_network_policy}
        self.NETWORK_POLICIES_DIALOG_ADD_NETWORK_POLICY_DESCRIPTION = {"constant": "network_policies_dialog_add_network_policy_description",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.network_policies_dialog_add_network_policy_description}
        self.NETWORK_POLICIES_DIALOG_ADD_NETWORK_POLICY_NAME = {"constant": "network_policies_dialog_add_network_policy_name",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.network_policies_dialog_add_network_policy_name}
        self.NETWORK_POLICIES_DIALOG_CHECK_ROUTING_POLICY_TYPE_CHECKBOX = {"constant": "network_policies_dialog_check_routing_policy_type_checkbox",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.network_policies_dialog_check_routing_policy_type_checkbox}
        self.NETWORK_POLICIES_DIALOG_CHECK_SWITCHES_POLICY_TYPE_CHECKBOX = {"constant": "network_policies_dialog_check_switches_policy_type_checkbox",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.network_policies_dialog_check_switches_policy_type_checkbox}
        self.NETWORK_POLICIES_DIALOG_CHECK_WIRELESS_POLICY_TYPE_CHECKBOX = {"constant": "network_policies_dialog_check_wireless_policy_type_checkbox",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.network_policies_dialog_check_wireless_policy_type_checkbox}
        self.NETWORK_POLICIES_DIALOG_CLICK_EXIT_BUTTON = {"constant": "network_policies_dialog_click_exit_button",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.network_policies_dialog_click_exit_button}
        self.NETWORK_POLICIES_DIALOG_CLICK_NEXT_BUTTON = {"constant": "network_policies_dialog_click_next_button",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.network_policies_dialog_click_next_button}
        self.NETWORK_POLICIES_DIALOG_CLICK_SAVE_BUTTON = {"constant": "network_policies_dialog_click_save_button",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.network_policies_dialog_click_save_button}
        self.NETWORK_POLICIES_DIALOG_CLICK_TAB_HEADER = {"constant": "network_policies_dialog_click_tab_header",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.network_policies_dialog_click_tab_header}
        self.NETWORK_POLICIES_SELECT_POLICY = {"constant": "network_policies_select_policy",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.network_policies_select_policy}
