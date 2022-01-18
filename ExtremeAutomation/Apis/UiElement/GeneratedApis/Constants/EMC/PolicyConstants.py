"""
This class outlines all the constants for the policy API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(PolicyConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class PolicyConstants(ApiConstants):
    def __init__(self):
        super(PolicyConstants, self).__init__()
        self.CLICK_EMC_CONTROL_MENU = {"constant": "click_emc_control_menu",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.click_emc_control_menu}
        self.CLICK_EMC_POLICY_TAB = {"constant": "click_emc_policy_tab",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.click_emc_policy_tab}
        self.POLICY_ADD_DEVICE_TO_DOMAIN = {"constant": "policy_add_device_to_domain",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.policy_add_device_to_domain}
        self.POLICY_ADD_DEVICE_TO_DOMAIN_MENU = {"constant": "policy_add_device_to_domain_menu",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.policy_add_device_to_domain_menu}
        self.POLICY_ADD_PORTS_TO_DOMAIN = {"constant": "policy_add_ports_to_domain",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.policy_add_ports_to_domain}
        self.POLICY_ADD_SERVICE_TO_ROLE = {"constant": "policy_add_service_to_role",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.policy_add_service_to_role}
        self.POLICY_CONFIRM_DEVICE_IN_CURRENT_DOMAIN = {"constant": "policy_confirm_device_in_current_domain",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.policy_confirm_device_in_current_domain}
        self.POLICY_CONFIRM_DEVICE_IN_DOMAIN = {"constant": "policy_confirm_device_in_domain",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.policy_confirm_device_in_domain}
        self.POLICY_CREATE_LOCAL_SERVICE = {"constant": "policy_create_local_service",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.policy_create_local_service}
        self.POLICY_CREATE_ROLE = {"constant": "policy_create_role",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.policy_create_role}
        self.POLICY_CREATE_RULE = {"constant": "policy_create_rule",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.policy_create_rule}
        self.POLICY_CREATE_VLAN = {"constant": "policy_create_vlan",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.policy_create_vlan}
        self.POLICY_DELETE_ROLE = {"constant": "policy_delete_role",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.policy_delete_role}
        self.POLICY_DELETE_SERVICE = {"constant": "policy_delete_service",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.policy_delete_service}
        self.POLICY_ENFORCE_DOMAIN = {"constant": "policy_enforce_domain",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.policy_enforce_domain}
        self.POLICY_EXPAND_TREE_PANEL_CLASS_OF_SERVICE = {"constant": "policy_expand_tree_panel_class_of_service",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.policy_expand_tree_panel_class_of_service}
        self.POLICY_EXPAND_TREE_PANEL_DEVICES_PORT_GROUPS = {"constant": "policy_expand_tree_panel_devices_port_groups",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.policy_expand_tree_panel_devices_port_groups}
        self.POLICY_EXPAND_TREE_PANEL_NETWORK_RESOURCES = {"constant": "policy_expand_tree_panel_network_resources",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_expand_tree_panel_network_resources}
        self.POLICY_EXPAND_TREE_PANEL_ROLES_SERVICES = {"constant": "policy_expand_tree_panel_roles_services",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.policy_expand_tree_panel_roles_services}
        self.POLICY_EXPAND_TREE_PANEL_VLANS = {"constant": "policy_expand_tree_panel_vlans",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_expand_tree_panel_vlans}
        self.POLICY_OPEN_DOMAIN = {"constant": "policy_open_domain",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.policy_open_domain}
        self.POLICY_ROLE_DEFAULT_ACTIONS_CLICK_SHOW_ALL = {"constant": "policy_role_default_actions_click_show_all",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_role_default_actions_click_show_all}
        self.POLICY_ROLE_EDIT_TCI_OVERWRITE = {"constant": "policy_role_edit_tci_overwrite",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_role_edit_tci_overwrite}
        self.POLICY_ROLE_NAVIGATE_TO_ROLE_NAME = {"constant": "policy_role_navigate_to_role_name",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.policy_role_navigate_to_role_name}
        self.POLICY_ROLE_SET_ACCESS_CONTROL = {"constant": "policy_role_set_access_control",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_role_set_access_control}
        self.POLICY_ROLE_SET_COS = {"constant": "policy_role_set_cos",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.policy_role_set_cos}
        self.POLICY_RULE_EDIT_TRAFFIC_DESCRIPTION_CLICK_OK = {"constant": "policy_rule_edit_traffic_description_click_ok",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.policy_rule_edit_traffic_description_click_ok}
        self.POLICY_RULE_IP_TOS_DIALOG_CLICK_EDIT = {"constant": "policy_rule_ip_tos_dialog_click_edit",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.policy_rule_ip_tos_dialog_click_edit}
        self.POLICY_RULE_IP_TOS_DIALOG_CLICK_OK = {"constant": "policy_rule_ip_tos_dialog_click_ok",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.policy_rule_ip_tos_dialog_click_ok}
        self.POLICY_RULE_NAVIGATE_TO_RULE_NAME = {"constant": "policy_rule_navigate_to_rule_name",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.policy_rule_navigate_to_rule_name}
        self.POLICY_RULE_SET_ACCESS_CONTROL = {"constant": "policy_rule_set_access_control",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_rule_set_access_control}
        self.POLICY_RULE_SET_ADVANCED_VALUE = {"constant": "policy_rule_set_advanced_value",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.policy_rule_set_advanced_value}
        self.POLICY_RULE_SET_APPLICATION = {"constant": "policy_rule_set_application",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.policy_rule_set_application}
        self.POLICY_RULE_SET_APPLICATION_GROUP = {"constant": "policy_rule_set_application_group",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.policy_rule_set_application_group}
        self.POLICY_RULE_SET_COS = {"constant": "policy_rule_set_cos",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.policy_rule_set_cos}
        self.POLICY_RULE_SET_DSCP = {"constant": "policy_rule_set_dscp",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.policy_rule_set_dscp}
        self.POLICY_RULE_SET_RANGE_VALUE = {"constant": "policy_rule_set_range_value",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.policy_rule_set_range_value}
        self.POLICY_RULE_SET_SINGLE_VALUE = {"constant": "policy_rule_set_single_value",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.policy_rule_set_single_value}
        self.POLICY_RULE_SET_TOS = {"constant": "policy_rule_set_tos",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.policy_rule_set_tos}
        self.POLICY_RULE_SET_TOS_HEX = {"constant": "policy_rule_set_tos_hex",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.policy_rule_set_tos_hex}
        self.POLICY_RULE_SET_TOS_MASK = {"constant": "policy_rule_set_tos_mask",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.policy_rule_set_tos_mask}
        self.POLICY_RULE_SET_TRAFFIC_LAYER_TYPE = {"constant": "policy_rule_set_traffic_layer_type",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.policy_rule_set_traffic_layer_type}
        self.POLICY_RULE_SET_TRAFFIC_TYPE = {"constant": "policy_rule_set_traffic_type",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.policy_rule_set_traffic_type}
        self.POLICY_RULE_SET_WELL_KNOWN_VALUE = {"constant": "policy_rule_set_well_known_value",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.policy_rule_set_well_known_value}
        self.POLICY_RULE_TRAFFIC_DESCRIPTION_CLICK_EDIT = {"constant": "policy_rule_traffic_description_click_edit",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.policy_rule_traffic_description_click_edit}
        self.POLICY_SAVE_DOMAIN = {"constant": "policy_save_domain",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.policy_save_domain}
