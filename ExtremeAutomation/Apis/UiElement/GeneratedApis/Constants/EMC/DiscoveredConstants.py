"""
This class outlines all the constants for the discovered API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DiscoveredConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DiscoveredConstants(ApiConstants):
    def __init__(self):
        super(DiscoveredConstants, self).__init__()
        self.CLICK_CLEAR_SELECTED = {"constant": "click_clear_selected",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.click_clear_selected}
        self.DISCOVERED_ADD_DEVICE_CLICK_ADD = {"constant": "discovered_add_device_click_add",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.discovered_add_device_click_add}
        self.DISCOVERED_ADD_DEVICE_CLICK_CANCEL = {"constant": "discovered_add_device_click_cancel",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.discovered_add_device_click_cancel}
        self.DISCOVERED_ADD_DEVICE_SELECT_TAB = {"constant": "discovered_add_device_select_tab",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.discovered_add_device_select_tab}
        self.DISCOVERED_ADD_DEVICE_SET_ADMIN_PROFILE = {"constant": "discovered_add_device_set_admin_profile",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.discovered_add_device_set_admin_profile}
        self.DISCOVERED_ADD_DEVICE_SET_CONTACT = {"constant": "discovered_add_device_set_contact",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.discovered_add_device_set_contact}
        self.DISCOVERED_ADD_DEVICE_SET_DEFAULT_SITE = {"constant": "discovered_add_device_set_default_site",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.discovered_add_device_set_default_site}
        self.DISCOVERED_ADD_DEVICE_SET_LOCATION = {"constant": "discovered_add_device_set_location",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.discovered_add_device_set_location}
        self.DISCOVERED_ADD_DEVICE_SET_POLL_GROUP = {"constant": "discovered_add_device_set_poll_group",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_add_device_set_poll_group}
        self.DISCOVERED_ADD_DEVICE_SET_POLL_TYPE = {"constant": "discovered_add_device_set_poll_type",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_add_device_set_poll_type}
        self.DISCOVERED_ADD_DEVICE_SET_SNMP_RETRIES = {"constant": "discovered_add_device_set_snmp_retries",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.discovered_add_device_set_snmp_retries}
        self.DISCOVERED_ADD_DEVICE_SET_SNMP_TIMEOUT = {"constant": "discovered_add_device_set_snmp_timeout",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.discovered_add_device_set_snmp_timeout}
        self.DISCOVERED_ADD_DEVICE_SET_SYSTEM_NAME = {"constant": "discovered_add_device_set_system_name",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.discovered_add_device_set_system_name}
        self.DISCOVERED_ADD_DEVICE_SET_TOPOLOGY_LAYER = {"constant": "discovered_add_device_set_topology_layer",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.discovered_add_device_set_topology_layer}
        self.DISCOVERED_CLICK_ADD_DEVICES = {"constant": "discovered_click_add_devices",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.discovered_click_add_devices}
        self.DISCOVERED_CLICK_CLEAR_ALL_DEVICES = {"constant": "discovered_click_clear_all_devices",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.discovered_click_clear_all_devices}
        self.DISCOVERED_CLICK_CLEAR_SELECTED = {"constant": "discovered_click_clear_selected",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.discovered_click_clear_selected}
        self.DISCOVERED_CLICK_EDIT_DEVICES = {"constant": "discovered_click_edit_devices",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.discovered_click_edit_devices}
        self.DISCOVERED_CLICK_PRE_REGISTER_DEVICE = {"constant": "discovered_click_pre_register_device",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_click_pre_register_device}
        self.DISCOVERED_CONFIRM_DEVICE_IP_EXISTS = {"constant": "discovered_confirm_device_ip_exists",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_confirm_device_ip_exists}
        self.DISCOVERED_CONFIRM_DEVICE_IP_PROFILE = {"constant": "discovered_confirm_device_ip_profile",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_confirm_device_ip_profile}
        self.DISCOVERED_CONFIRM_DEVICE_IP_STATUS = {"constant": "discovered_confirm_device_ip_status",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_confirm_device_ip_status}
        self.DISCOVERED_EDIT_DEVICE_CLICK_CANCEL = {"constant": "discovered_edit_device_click_cancel",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_click_cancel}
        self.DISCOVERED_EDIT_DEVICE_CLICK_SAVE = {"constant": "discovered_edit_device_click_save",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.discovered_edit_device_click_save}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW = {"constant": "discovered_edit_device_ports_edit_row",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.discovered_edit_device_ports_edit_row}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_ALIAS = {"constant": "discovered_edit_device_ports_edit_row_alias",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.discovered_edit_device_ports_edit_row_alias}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_AUTHENTICATION = {"constant": "discovered_edit_device_ports_edit_row_authentication",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.discovered_edit_device_ports_edit_row_authentication}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_AUTO_NEGOTIATION = {"constant": "discovered_edit_device_ports_edit_row_auto_negotiation",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.discovered_edit_device_ports_edit_row_auto_negotiation}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_CONFIGURATION = {"constant": "discovered_edit_device_ports_edit_row_configuration",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.discovered_edit_device_ports_edit_row_configuration}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_DUPLEX = {"constant": "discovered_edit_device_ports_edit_row_duplex",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.discovered_edit_device_ports_edit_row_duplex}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_ENABLED = {"constant": "discovered_edit_device_ports_edit_row_enabled",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.discovered_edit_device_ports_edit_row_enabled}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_LAG = {"constant": "discovered_edit_device_ports_edit_row_lag",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.discovered_edit_device_ports_edit_row_lag}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_LOOP_PROTECT = {"constant": "discovered_edit_device_ports_edit_row_loop_protect",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.discovered_edit_device_ports_edit_row_loop_protect}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_MVRP = {"constant": "discovered_edit_device_ports_edit_row_mvrp",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.discovered_edit_device_ports_edit_row_mvrp}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_NICKNAME = {"constant": "discovered_edit_device_ports_edit_row_nickname",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_ports_edit_row_nickname}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_NODE_ALIAS = {"constant": "discovered_edit_device_ports_edit_row_node_alias",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.discovered_edit_device_ports_edit_row_node_alias}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_PVID = {"constant": "discovered_edit_device_ports_edit_row_pvid",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.discovered_edit_device_ports_edit_row_pvid}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_SPAN_GUARD = {"constant": "discovered_edit_device_ports_edit_row_span_guard",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.discovered_edit_device_ports_edit_row_span_guard}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_SPEED = {"constant": "discovered_edit_device_ports_edit_row_speed",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.discovered_edit_device_ports_edit_row_speed}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_TAGGED = {"constant": "discovered_edit_device_ports_edit_row_tagged",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.discovered_edit_device_ports_edit_row_tagged}
        self.DISCOVERED_EDIT_DEVICE_PORTS_EDIT_ROW_UNTAGGED = {"constant": "discovered_edit_device_ports_edit_row_untagged",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_ports_edit_row_untagged}
        self.DISCOVERED_EDIT_DEVICE_PORTS_ROW_EDITOR_CANCEL = {"constant": "discovered_edit_device_ports_row_editor_cancel",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_ports_row_editor_cancel}
        self.DISCOVERED_EDIT_DEVICE_PORTS_ROW_EDITOR_UPDATE = {"constant": "discovered_edit_device_ports_row_editor_update",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_ports_row_editor_update}
        self.DISCOVERED_EDIT_DEVICE_PORTS_SELECT_PORT = {"constant": "discovered_edit_device_ports_select_port",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.discovered_edit_device_ports_select_port}
        self.DISCOVERED_EDIT_DEVICE_PORTS_SHOW_COLUMNS = {"constant": "discovered_edit_device_ports_show_columns",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.discovered_edit_device_ports_show_columns}
        self.DISCOVERED_EDIT_DEVICE_SELECT_TAB = {"constant": "discovered_edit_device_select_tab",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.discovered_edit_device_select_tab}
        self.DISCOVERED_EDIT_DEVICE_SET_ADMIN_PROFILE = {"constant": "discovered_edit_device_set_admin_profile",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.discovered_edit_device_set_admin_profile}
        self.DISCOVERED_EDIT_DEVICE_SET_ASSET_TAG = {"constant": "discovered_edit_device_set_asset_tag",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_edit_device_set_asset_tag}
        self.DISCOVERED_EDIT_DEVICE_SET_CONTACT = {"constant": "discovered_edit_device_set_contact",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.discovered_edit_device_set_contact}
        self.DISCOVERED_EDIT_DEVICE_SET_DEFAULT_SITE = {"constant": "discovered_edit_device_set_default_site",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.discovered_edit_device_set_default_site}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_ENABLE_PORT_LINK = {"constant": "discovered_edit_device_set_edit_access_control_advanced_settings_enable_port_link",
                                                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                                                  "link": self.link.discovered_edit_device_set_edit_access_control_advanced_settings_enable_port_link}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_IP_SUBNET = {"constant": "discovered_edit_device_set_edit_access_control_advanced_settings_ip_subnet",
                                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                                           "link": self.link.discovered_edit_device_set_edit_access_control_advanced_settings_ip_subnet}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_OPEN = {"constant": "discovered_edit_device_set_edit_access_control_advanced_settings_open",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.discovered_edit_device_set_edit_access_control_advanced_settings_open}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_REAUTH_TYPE = {"constant": "discovered_edit_device_set_edit_access_control_advanced_settings_reauth_type",
                                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                                             "link": self.link.discovered_edit_device_set_edit_access_control_advanced_settings_reauth_type}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_SAVE = {"constant": "discovered_edit_device_set_edit_access_control_advanced_settings_save",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.discovered_edit_device_set_edit_access_control_advanced_settings_save}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ADVANCED_SETTINGS_SHARED_SECRET = {"constant": "discovered_edit_device_set_edit_access_control_advanced_settings_shared_secret",
                                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                                               "link": self.link.discovered_edit_device_set_edit_access_control_advanced_settings_shared_secret}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_AUTH_ACCESS_TYPE = {"constant": "discovered_edit_device_set_edit_access_control_auth_access_type",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.discovered_edit_device_set_edit_access_control_auth_access_type}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ENABLE_AUTH_USING_PORT_TEMPLATE = {"constant": "discovered_edit_device_set_edit_access_control_enable_auth_using_port_template",
                                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                                               "link": self.link.discovered_edit_device_set_edit_access_control_enable_auth_using_port_template}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_ENGINE_GROUP_ = {"constant": "discovered_edit_device_set_edit_access_control_engine_group_",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.discovered_edit_device_set_edit_access_control_engine_group_}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_MGMT_RADIUS_SERVER_1 = {"constant": "discovered_edit_device_set_edit_access_control_mgmt_radius_server_1",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.discovered_edit_device_set_edit_access_control_mgmt_radius_server_1}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_MGMT_RADIUS_SERVER_2 = {"constant": "discovered_edit_device_set_edit_access_control_mgmt_radius_server_2",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.discovered_edit_device_set_edit_access_control_mgmt_radius_server_2}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_NETWORK_RADIUS_SERVER = {"constant": "discovered_edit_device_set_edit_access_control_network_radius_server",
                                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                                     "link": self.link.discovered_edit_device_set_edit_access_control_network_radius_server}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_POLICY_ENFORCEMENT_POINT_1 = {"constant": "discovered_edit_device_set_edit_access_control_policy_enforcement_point_1",
                                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                                          "link": self.link.discovered_edit_device_set_edit_access_control_policy_enforcement_point_1}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_POLICY_ENFORCEMENT_POINT_2 = {"constant": "discovered_edit_device_set_edit_access_control_policy_enforcement_point_2",
                                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                                          "link": self.link.discovered_edit_device_set_edit_access_control_policy_enforcement_point_2}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_PRIMARY_ENGINE = {"constant": "discovered_edit_device_set_edit_access_control_primary_engine",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.discovered_edit_device_set_edit_access_control_primary_engine}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_RADIUS_ACCOUNTING = {"constant": "discovered_edit_device_set_edit_access_control_radius_accounting",
                                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                                 "link": self.link.discovered_edit_device_set_edit_access_control_radius_accounting}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_RADIUS_ATTRS_TO_SEND = {"constant": "discovered_edit_device_set_edit_access_control_radius_attrs_to_send",
                                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                                    "link": self.link.discovered_edit_device_set_edit_access_control_radius_attrs_to_send}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_SECONDARY_ENGINE = {"constant": "discovered_edit_device_set_edit_access_control_secondary_engine",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.discovered_edit_device_set_edit_access_control_secondary_engine}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_SWITCH_TYPE = {"constant": "discovered_edit_device_set_edit_access_control_switch_type",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.discovered_edit_device_set_edit_access_control_switch_type}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_ACCESS_CONTROL_VIRTUAL_ROUTER_NAME = {"constant": "discovered_edit_device_set_edit_access_control_virtual_router_name",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.discovered_edit_device_set_edit_access_control_virtual_router_name}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_SYSLOG_RECEIVER = {"constant": "discovered_edit_device_set_edit_syslog_receiver",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.discovered_edit_device_set_edit_syslog_receiver}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_ACCESS_CONTROL_GROUP = {"constant": "discovered_edit_device_set_edit_to_access_control_group",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.discovered_edit_device_set_edit_to_access_control_group}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_ARCHIVE = {"constant": "discovered_edit_device_set_edit_to_archive",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.discovered_edit_device_set_edit_to_archive}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_MAP = {"constant": "discovered_edit_device_set_edit_to_map",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.discovered_edit_device_set_edit_to_map}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_TO_POLICY_DOMAIN = {"constant": "discovered_edit_device_set_edit_to_policy_domain",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.discovered_edit_device_set_edit_to_policy_domain}
        self.DISCOVERED_EDIT_DEVICE_SET_EDIT_TRAP_RECEIVER = {"constant": "discovered_edit_device_set_edit_trap_receiver",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.discovered_edit_device_set_edit_trap_receiver}
        self.DISCOVERED_EDIT_DEVICE_SET_ENABLE_COLLECTION = {"constant": "discovered_edit_device_set_enable_collection",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.discovered_edit_device_set_enable_collection}
        self.DISCOVERED_EDIT_DEVICE_SET_LOCATION = {"constant": "discovered_edit_device_set_location",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_set_location}
        self.DISCOVERED_EDIT_DEVICE_SET_NICKNAME = {"constant": "discovered_edit_device_set_nickname",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_set_nickname}
        self.DISCOVERED_EDIT_DEVICE_SET_NOTE = {"constant": "discovered_edit_device_set_note",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.discovered_edit_device_set_note}
        self.DISCOVERED_EDIT_DEVICE_SET_POLL_GROUP = {"constant": "discovered_edit_device_set_poll_group",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.discovered_edit_device_set_poll_group}
        self.DISCOVERED_EDIT_DEVICE_SET_POLL_TYPE = {"constant": "discovered_edit_device_set_poll_type",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_edit_device_set_poll_type}
        self.DISCOVERED_EDIT_DEVICE_SET_REMOVE_FROM_SERVICE = {"constant": "discovered_edit_device_set_remove_from_service",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_set_remove_from_service}
        self.DISCOVERED_EDIT_DEVICE_SET_REPLACEMENT_SERIAL_NUMBER = {"constant": "discovered_edit_device_set_replacement_serial_number",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.discovered_edit_device_set_replacement_serial_number}
        self.DISCOVERED_EDIT_DEVICE_SET_SNMP_RETRIES = {"constant": "discovered_edit_device_set_snmp_retries",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.discovered_edit_device_set_snmp_retries}
        self.DISCOVERED_EDIT_DEVICE_SET_SNMP_TIMEOUT = {"constant": "discovered_edit_device_set_snmp_timeout",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.discovered_edit_device_set_snmp_timeout}
        self.DISCOVERED_EDIT_DEVICE_SET_SYSTEM_NAME = {"constant": "discovered_edit_device_set_system_name",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.discovered_edit_device_set_system_name}
        self.DISCOVERED_EDIT_DEVICE_SET_TOPOLOGY_LAYER = {"constant": "discovered_edit_device_set_topology_layer",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.discovered_edit_device_set_topology_layer}
        self.DISCOVERED_EDIT_DEVICE_SET_USER_DATA = {"constant": "discovered_edit_device_set_user_data",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_edit_device_set_user_data}
        self.DISCOVERED_EDIT_DEVICE_VENDOR_PROFILE_DEVICE_TYPE = {"constant": "discovered_edit_device_vendor_profile_device_type",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.discovered_edit_device_vendor_profile_device_type}
        self.DISCOVERED_EDIT_DEVICE_VENDOR_PROFILE_FAMILY = {"constant": "discovered_edit_device_vendor_profile_family",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.discovered_edit_device_vendor_profile_family}
        self.DISCOVERED_EDIT_DEVICE_VENDOR_PROFILE_SUB_FAMILY = {"constant": "discovered_edit_device_vendor_profile_sub_family",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.discovered_edit_device_vendor_profile_sub_family}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_ADD = {"constant": "discovered_edit_device_vlan_definition_add",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.discovered_edit_device_vlan_definition_add}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_DELETE = {"constant": "discovered_edit_device_vlan_definition_delete",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.discovered_edit_device_vlan_definition_delete}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_EDIT = {"constant": "discovered_edit_device_vlan_definition_edit",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.discovered_edit_device_vlan_definition_edit}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SELECT_ROW = {"constant": "discovered_edit_device_vlan_definition_select_row",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.discovered_edit_device_vlan_definition_select_row}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_ALWAYS_WRITE_TO_DEVICES = {"constant": "discovered_edit_device_vlan_definition_set_always_write_to_devices",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.discovered_edit_device_vlan_definition_set_always_write_to_devices}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_NAME = {"constant": "discovered_edit_device_vlan_definition_set_name",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.discovered_edit_device_vlan_definition_set_name}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_VID = {"constant": "discovered_edit_device_vlan_definition_set_vid",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_vlan_definition_set_vid}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_SET_VRF = {"constant": "discovered_edit_device_vlan_definition_set_vrf",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_vlan_definition_set_vrf}
        self.DISCOVERED_EDIT_DEVICE_VLAN_DEFINITION_UPDATE = {"constant": "discovered_edit_device_vlan_definition_update",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.discovered_edit_device_vlan_definition_update}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_CONFIGURE_DEVICE = {"constant": "discovered_edit_device_ztp_set_configure_device",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.discovered_edit_device_ztp_set_configure_device}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_DNS_SERVER = {"constant": "discovered_edit_device_ztp_set_dns_server",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.discovered_edit_device_ztp_set_dns_server}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_DOMAIN_NAME = {"constant": "discovered_edit_device_ztp_set_domain_name",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.discovered_edit_device_ztp_set_domain_name}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE = {"constant": "discovered_edit_device_ztp_set_firmware_upgrade",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.discovered_edit_device_ztp_set_firmware_upgrade}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE_DATE = {"constant": "discovered_edit_device_ztp_set_firmware_upgrade_date",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.discovered_edit_device_ztp_set_firmware_upgrade_date}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE_TIME = {"constant": "discovered_edit_device_ztp_set_firmware_upgrade_time",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.discovered_edit_device_ztp_set_firmware_upgrade_time}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_FIRMWARE_UPGRADE_UTC_OFFSET = {"constant": "discovered_edit_device_ztp_set_firmware_upgrade_utc_offset",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.discovered_edit_device_ztp_set_firmware_upgrade_utc_offset}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_GATEWAY_ADDRESS = {"constant": "discovered_edit_device_ztp_set_gateway_address",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.discovered_edit_device_ztp_set_gateway_address}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_IP_ADDRESS_SUBNET = {"constant": "discovered_edit_device_ztp_set_ip_address_subnet",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.discovered_edit_device_ztp_set_ip_address_subnet}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_LACP = {"constant": "discovered_edit_device_ztp_set_lacp",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_ztp_set_lacp}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_LLDP = {"constant": "discovered_edit_device_ztp_set_lldp",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_ztp_set_lldp}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_MANAGEMENT_INTERFACE = {"constant": "discovered_edit_device_ztp_set_management_interface",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.discovered_edit_device_ztp_set_management_interface}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_MSTP = {"constant": "discovered_edit_device_ztp_set_mstp",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_ztp_set_mstp}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_MVRP = {"constant": "discovered_edit_device_ztp_set_mvrp",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_edit_device_ztp_set_mvrp}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_NTP_SERVER = {"constant": "discovered_edit_device_ztp_set_ntp_server",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.discovered_edit_device_ztp_set_ntp_server}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_POE = {"constant": "discovered_edit_device_ztp_set_poe",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.discovered_edit_device_ztp_set_poe}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_SERIAL_NUMBER = {"constant": "discovered_edit_device_ztp_set_serial_number",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.discovered_edit_device_ztp_set_serial_number}
        self.DISCOVERED_EDIT_DEVICE_ZTP_SET_XVLAN = {"constant": "discovered_edit_device_ztp_set_xvlan",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_edit_device_ztp_set_xvlan}
        self.DISCOVERED_MODIFY_TABLE_REFRESH_TIME = {"constant": "discovered_modify_table_refresh_time",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.discovered_modify_table_refresh_time}
        self.DISCOVERED_PRE_REGISTER_DEVICE_CANCEL = {"constant": "discovered_pre_register_device_cancel",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.discovered_pre_register_device_cancel}
        self.DISCOVERED_PRE_REGISTER_DEVICE_CREATE = {"constant": "discovered_pre_register_device_create",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.discovered_pre_register_device_create}
        self.DISCOVERED_PRE_REGISTER_DEVICE_NEXT = {"constant": "discovered_pre_register_device_next",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.discovered_pre_register_device_next}
        self.DISCOVERED_PRE_REGISTER_DEVICE_PREVIOUS = {"constant": "discovered_pre_register_device_previous",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.discovered_pre_register_device_previous}
        self.DISCOVERED_PRE_REGISTER_DEVICE_SET_DEFAULT_SITE = {"constant": "discovered_pre_register_device_set_default_site",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.discovered_pre_register_device_set_default_site}
        self.DISCOVERED_PRE_REGISTER_DEVICE_SET_IP_ADDRESS = {"constant": "discovered_pre_register_device_set_ip_address",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.discovered_pre_register_device_set_ip_address}
        self.DISCOVERED_PRE_REGISTER_DEVICE_SET_SERIAL_NUMBERS = {"constant": "discovered_pre_register_device_set_serial_numbers",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.discovered_pre_register_device_set_serial_numbers}
        self.DISCOVERED_REFRESH_TABLE = {"constant": "discovered_refresh_table",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.discovered_refresh_table}
        self.DISCOVERED_RESET_TABLE = {"constant": "discovered_reset_table",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.discovered_reset_table}
        self.DISCOVERED_SELECT_DEVICE_IN_TABLE = {"constant": "discovered_select_device_in_table",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.discovered_select_device_in_table}
        self.DISCOVERED_SELECT_ROW_BY_COLUMN_VALUE = {"constant": "discovered_select_row_by_column_value",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.discovered_select_row_by_column_value}
        self.DISCOVERED_WAIT_FOR_DEVICE_ADD = {"constant": "discovered_wait_for_device_add",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.discovered_wait_for_device_add}
        self.DISCOVERED_WAIT_FOR_DEVICE_REMOVE = {"constant": "discovered_wait_for_device_remove",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.discovered_wait_for_device_remove}
        self.DISCOVERY_GET_DEVICE_PORT_AUTO_NEGOTIATION_VALUE = {"constant": "discovery_get_device_port_auto_negotiation_value",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.discovery_get_device_port_auto_negotiation_value}
