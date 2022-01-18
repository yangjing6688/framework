"""
This class outlines all the constants for the engines API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EnginesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EnginesConstants(ApiConstants):
    def __init__(self):
        super(EnginesConstants, self).__init__()
        self.ENGINES_ADD_ENGINE_PROPERTIES = {"constant": "engines_add_engine_properties",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.engines_add_engine_properties}
        self.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_CANCEL_SETTINGS = {"constant": "engines_advanced_switch_settings_dialog_cancel_settings",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.engines_advanced_switch_settings_dialog_cancel_settings}
        self.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_CHECK_ENABLE_PORT_LINK_CONTROL = {"constant": "engines_advanced_switch_settings_dialog_check_enable_port_link_control",
                                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                                       "link": self.link.engines_advanced_switch_settings_dialog_check_enable_port_link_control}
        self.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_ENTER_SHARED_SECURITY = {"constant": "engines_advanced_switch_settings_dialog_enter_shared_security",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.engines_advanced_switch_settings_dialog_enter_shared_security}
        self.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_SAVE_SETTINGS = {"constant": "engines_advanced_switch_settings_dialog_save_settings",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.engines_advanced_switch_settings_dialog_save_settings}
        self.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_SELECT_IP_SUBNET = {"constant": "engines_advanced_switch_settings_dialog_select_ip_subnet",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.engines_advanced_switch_settings_dialog_select_ip_subnet}
        self.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_SELECT_REAUTH_TYPE = {"constant": "engines_advanced_switch_settings_dialog_select_reauth_type",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.engines_advanced_switch_settings_dialog_select_reauth_type}
        self.ENGINES_DIALOG_ADD_ACCESS_CONTROL_ENGINE = {"constant": "engines_dialog_add_access_control_engine",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.engines_dialog_add_access_control_engine}
        self.ENGINES_DIALOG_ADD_SWITCH = {"constant": "engines_dialog_add_switch",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.engines_dialog_add_switch}
        self.ENGINES_DIALOG_DELETE_ACCESS_CONTROL_ENGINE = {"constant": "engines_dialog_delete_access_control_engine",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.engines_dialog_delete_access_control_engine}
        self.ENGINES_DIALOG_DELETE_SWITCH = {"constant": "engines_dialog_delete_switch",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.engines_dialog_delete_switch}
        self.ENGINES_DIALOG_EDIT_SWITCH_CLICK_SAVE = {"constant": "engines_dialog_edit_switch_click_save",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.engines_dialog_edit_switch_click_save}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_AUTH_ACCESS_TYPE = {"constant": "engines_dialog_edit_switch_set_auth_access_type",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.engines_dialog_edit_switch_set_auth_access_type}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_NETWORK_RADIUS_SERVER = {"constant": "engines_dialog_edit_switch_set_network_radius_server",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.engines_dialog_edit_switch_set_network_radius_server}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_POLICY_DOMAIN = {"constant": "engines_dialog_edit_switch_set_policy_domain",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.engines_dialog_edit_switch_set_policy_domain}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_PRIMARY_ENGINE = {"constant": "engines_dialog_edit_switch_set_primary_engine",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.engines_dialog_edit_switch_set_primary_engine}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_ACCOUNTING = {"constant": "engines_dialog_edit_switch_set_radius_accounting",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.engines_dialog_edit_switch_set_radius_accounting}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_ATTR_TO_SEND = {"constant": "engines_dialog_edit_switch_set_radius_attr_to_send",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.engines_dialog_edit_switch_set_radius_attr_to_send}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_MGMT_SERVER_1 = {"constant": "engines_dialog_edit_switch_set_radius_mgmt_server_1",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.engines_dialog_edit_switch_set_radius_mgmt_server_1}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_MGMT_SERVER_2 = {"constant": "engines_dialog_edit_switch_set_radius_mgmt_server_2",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.engines_dialog_edit_switch_set_radius_mgmt_server_2}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_SECONDARY_ENGINE = {"constant": "engines_dialog_edit_switch_set_secondary_engine",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.engines_dialog_edit_switch_set_secondary_engine}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_SWITCH_TYPE = {"constant": "engines_dialog_edit_switch_set_switch_type",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.engines_dialog_edit_switch_set_switch_type}
        self.ENGINES_DIALOG_EDIT_SWITCH_SET_VIRTUAL_ROUTER_NAME = {"constant": "engines_dialog_edit_switch_set_virtual_router_name",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.engines_dialog_edit_switch_set_virtual_router_name}
        self.ENGINES_GIM_ADD_DOMAIN = {"constant": "engines_gim_add_domain",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.engines_gim_add_domain}
        self.ENGINES_GIM_ADD_GIM_IP = {"constant": "engines_gim_add_gim_ip",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.engines_gim_add_gim_ip}
        self.ENGINES_GIM_CLICK_ON_EDIT_PNG = {"constant": "engines_gim_click_on_edit_png",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.engines_gim_click_on_edit_png}
        self.ENGINES_GIM_CREATE_DOMAIN = {"constant": "engines_gim_create_domain",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.engines_gim_create_domain}
        self.ENGINES_GIM_DEFAULT_BUTTONS_VALIDATION = {"constant": "engines_gim_default_buttons_validation",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.engines_gim_default_buttons_validation}
        self.ENGINES_GIM_DEFAULT_VALIDATION_DETAILS_TAB = {"constant": "engines_gim_default_validation_details_tab",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.engines_gim_default_validation_details_tab}
        self.ENGINES_GIM_DEFAULT_VALIDATION_GIM_TAB = {"constant": "engines_gim_default_validation_gim_tab",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.engines_gim_default_validation_gim_tab}
        self.ENGINES_GIM_DELETE_GIM_IP = {"constant": "engines_gim_delete_gim_ip",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.engines_gim_delete_gim_ip}
        self.ENGINES_GIM_DETAILS_DOMAIN = {"constant": "engines_gim_details_domain",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.engines_gim_details_domain}
        self.ENGINES_GIM_DUPLICATE_IP = {"constant": "engines_gim_duplicate_ip",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.engines_gim_duplicate_ip}
        self.ENGINES_GIM_EDIT_GIM_IP = {"constant": "engines_gim_edit_gim_ip",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.engines_gim_edit_gim_ip}
        self.ENGINES_GIM_ENFORCE = {"constant": "engines_gim_enforce",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.engines_gim_enforce}
        self.ENGINES_GIM_MAP_DOMAIN_LPR_NONE = {"constant": "engines_gim_map_domain_lpr_none",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.engines_gim_map_domain_lpr_none}
        self.ENGINES_GIM_SELECT_ROW_FROM_LPR_TABLE = {"constant": "engines_gim_select_row_from_lpr_table",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.engines_gim_select_row_from_lpr_table}
        self.ENGINES_GIM_SELECT_ROW_FROM_MANAGE_TABLE = {"constant": "engines_gim_select_row_from_manage_table",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.engines_gim_select_row_from_manage_table}
        self.ENGINES_NAVIGATE_TO_EDIT_SWITCH = {"constant": "engines_navigate_to_edit_switch",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.engines_navigate_to_edit_switch}
        self.ENGINES_OPEN_ADVANCED_SETTINGS_DIALOG = {"constant": "engines_open_advanced_settings_dialog",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.engines_open_advanced_settings_dialog}
        self.ENGINES_REMOVE_ENGINE_PROPERTIES = {"constant": "engines_remove_engine_properties",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.engines_remove_engine_properties}
