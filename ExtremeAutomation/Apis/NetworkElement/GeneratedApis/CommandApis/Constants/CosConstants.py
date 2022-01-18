"""
This class outlines all the constants for the cos API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CosConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CosConstants(ApiConstants):
    def __init__(self):
        super(CosConstants, self).__init__()
        self.CLEAR_ALL_CONFIG = {"constant": "clear_all_config",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.clear_all_config}
        self.CLEAR_FLOOD_CTRL_SETTINGS = {"constant": "clear_flood_ctrl_settings",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.clear_flood_ctrl_settings}
        self.CLEAR_INDEX = {"constant": "clear_index",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.clear_index}
        self.CLEAR_IRL = {"constant": "clear_irl",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.clear_irl}
        self.CLEAR_IRL_SETTINGS = {"constant": "clear_irl_settings",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_irl_settings}
        self.CLEAR_ORL_SETTINGS = {"constant": "clear_orl_settings",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_orl_settings}
        self.CLEAR_TOS_SETTINGS = {"constant": "clear_tos_settings",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_tos_settings}
        self.CLEAR_TXQ_SETTINGS = {"constant": "clear_txq_settings",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_txq_settings}
        self.CLEAR_TXQ_SHAPING = {"constant": "clear_txq_shaping",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.clear_txq_shaping}
        self.CREATE_PORT_GROUP = {"constant": "create_port_group",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.create_port_group}
        self.CREATE_QOS_PROFILE = {"constant": "create_qos_profile",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.create_qos_profile}
        self.DELETE_PORT_GROUP = {"constant": "delete_port_group",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.delete_port_group}
        self.DELETE_QOS_PROFILE = {"constant": "delete_qos_profile",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.delete_qos_profile}
        self.DISABLE_STATE = {"constant": "disable_state",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.disable_state}
        self.ENABLE_STATE = {"constant": "enable_state",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.enable_state}
        self.SET_DIFF_SERVE_REPLACEMENT = {"constant": "set_diff_serve_replacement",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_diff_serve_replacement}
        self.SET_DOT1P_PORT_TYPE = {"constant": "set_dot1p_port_type",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_dot1p_port_type}
        self.SET_DOT1P_TYPE = {"constant": "set_dot1p_type",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.set_dot1p_type}
        self.SET_DOT1P_TYPE_ONLY = {"constant": "set_dot1p_type_only",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_dot1p_type_only}
        self.SET_IRL_REFERENCE = {"constant": "set_irl_reference",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_irl_reference}
        self.SET_IRL_SETTINGS = {"constant": "set_irl_settings",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_irl_settings}
        self.SET_IRL_SETTINGS_COS_UNDER_SEVEN = {"constant": "set_irl_settings_cos_under_seven",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_irl_settings_cos_under_seven}
        self.SET_ORL_REFERENCE = {"constant": "set_orl_reference",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_orl_reference}
        self.SET_ORL_SETTINGS = {"constant": "set_orl_settings",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_orl_settings}
        self.SET_ORL_SETTINGS_COS_UNDER_SEVEN = {"constant": "set_orl_settings_cos_under_seven",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_orl_settings_cos_under_seven}
        self.SET_PORT_GROUP_PORT = {"constant": "set_port_group_port",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.set_port_group_port}
        self.SET_PORT_PRIORITY = {"constant": "set_port_priority",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_port_priority}
        self.SET_PORT_QOS_PROFILE = {"constant": "set_port_qos_profile",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_port_qos_profile}
        self.SET_PORT_RESOURCE_IRL = {"constant": "set_port_resource_irl",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_port_resource_irl}
        self.SET_PORT_RESOURCE_ORL = {"constant": "set_port_resource_orl",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_port_resource_orl}
        self.SET_PRIORITY_SETTINGS = {"constant": "set_priority_settings",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_priority_settings}
        self.SET_PRIORITY_SETTINGS_COS_UNDER_SEVEN = {"constant": "set_priority_settings_cos_under_seven",
                                                      "tags": ["COMMAND_CLI"],
                                                      "link": self.link.set_priority_settings_cos_under_seven}
        self.SET_QOS_SCHEDULER = {"constant": "set_qos_scheduler",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_qos_scheduler}
        self.SET_TOS_SETTINGS = {"constant": "set_tos_settings",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_tos_settings}
        self.SET_TOS_SETTINGS_COS_UNDER_SEVEN = {"constant": "set_tos_settings_cos_under_seven",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_tos_settings_cos_under_seven}
        self.SET_TXQ_REFERENCE = {"constant": "set_txq_reference",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.set_txq_reference}
        self.SET_TXQ_SETTINGS = {"constant": "set_txq_settings",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.set_txq_settings}
        self.SET_TXQ_SETTINGS_COS_UNDER_SEVEN = {"constant": "set_txq_settings_cos_under_seven",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.set_txq_settings_cos_under_seven}
        self.SET_TXQ_SHAPING = {"constant": "set_txq_shaping",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_txq_shaping}
        self.SET_TXQ_WEIGHTS = {"constant": "set_txq_weights",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.set_txq_weights}
        self.SHOW_IRL_PORT_GROUP = {"constant": "show_irl_port_group",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_irl_port_group}
        self.SHOW_IRL_PORT_GROUP_SPECIFIC = {"constant": "show_irl_port_group_specific",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_irl_port_group_specific}
        self.SHOW_IRL_PORT_RESOURCE = {"constant": "show_irl_port_resource",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_irl_port_resource}
        self.SHOW_IRL_PORT_RESOURCE_SPECIFIC = {"constant": "show_irl_port_resource_specific",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_irl_port_resource_specific}
        self.SHOW_IRL_REFERENCE = {"constant": "show_irl_reference",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_irl_reference}
        self.SHOW_IRL_WFQ_WEIGHTS = {"constant": "show_irl_wfq_weights",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_irl_wfq_weights}
        self.SHOW_ORL_PORT_RESOURCE = {"constant": "show_orl_port_resource",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_orl_port_resource}
        self.SHOW_ORL_REFERENCE = {"constant": "show_orl_reference",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_orl_reference}
        self.SHOW_PORT_INFO_DETAIL = {"constant": "show_port_info_detail",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_info_detail}
        self.SHOW_PORT_PRIORITY = {"constant": "show_port_priority",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_port_priority}
        self.SHOW_PORT_QOS_PROFILE = {"constant": "show_port_qos_profile",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_qos_profile}
        self.SHOW_QOS_PROFILE = {"constant": "show_qos_profile",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_qos_profile}
        self.SHOW_QOS_SCHEDULER = {"constant": "show_qos_scheduler",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_qos_scheduler}
        self.SHOW_SETTINGS = {"constant": "show_settings",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_settings}
        self.SHOW_STATE = {"constant": "show_state",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_state}
        self.SHOW_TXQ_PORT_GROUP = {"constant": "show_txq_port_group",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_txq_port_group}
        self.SHOW_TXQ_PORT_GROUP_SPECIFIC = {"constant": "show_txq_port_group_specific",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_txq_port_group_specific}
        self.SHOW_TXQ_PORT_RESOURCE = {"constant": "show_txq_port_resource",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_txq_port_resource}
        self.SHOW_TXQ_PORT_RESOURCE_SPECIFIC = {"constant": "show_txq_port_resource_specific",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_txq_port_resource_specific}
        self.SHOW_TXQ_REFERENCE = {"constant": "show_txq_reference",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_txq_reference}
        self.SHOW_TXQ_WFQ_WEIGHTS = {"constant": "show_txq_wfq_weights",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_txq_wfq_weights}
