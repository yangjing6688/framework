"""
This class outlines all the constants for the policycos API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PolicycosConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PolicycosConstants(ApiConstants):
    def __init__(self):
        super(PolicycosConstants, self).__init__()
        self.POLICY_CLICK_TREE_PANEL = {"constant": "policy_click_tree_panel",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.policy_click_tree_panel}
        self.POLICY_COS_CREATE = {"constant": "policy_cos_create",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.policy_cos_create}
        self.POLICY_COS_CREATE_RATE_LIMIT = {"constant": "policy_cos_create_rate_limit",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.policy_cos_create_rate_limit}
        self.POLICY_COS_DELETE_COS = {"constant": "policy_cos_delete_cos",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.policy_cos_delete_cos}
        self.POLICY_COS_DELETE_RATE_LIMIT = {"constant": "policy_cos_delete_rate_limit",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.policy_cos_delete_rate_limit}
        self.POLICY_COS_EDIT_IRL_INDEX = {"constant": "policy_cos_edit_irl_index",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.policy_cos_edit_irl_index}
        self.POLICY_COS_EDIT_TOS = {"constant": "policy_cos_edit_tos",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.policy_cos_edit_tos}
        self.POLICY_COS_EDIT_TOS_HEX_VALUE = {"constant": "policy_cos_edit_tos_hex_value",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.policy_cos_edit_tos_hex_value}
        self.POLICY_COS_EDIT_TXQ_INDEX = {"constant": "policy_cos_edit_txq_index",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.policy_cos_edit_txq_index}
        self.POLICY_COS_ENABLE_TOS = {"constant": "policy_cos_enable_tos",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.policy_cos_enable_tos}
        self.POLICY_COS_SELECT_COS_NODE = {"constant": "policy_cos_select_cos_node",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.policy_cos_select_cos_node}
        self.POLICY_COS_SET_IRL_INDEX = {"constant": "policy_cos_set_irl_index",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.policy_cos_set_irl_index}
        self.POLICY_COS_SET_ORL_INDEX = {"constant": "policy_cos_set_orl_index",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.policy_cos_set_orl_index}
