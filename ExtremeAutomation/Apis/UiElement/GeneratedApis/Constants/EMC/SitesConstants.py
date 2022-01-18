"""
This class outlines all the constants for the sites API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SitesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SitesConstants(ApiConstants):
    def __init__(self):
        super(SitesConstants, self).__init__()
        self.SITES_CONFIGURE_ACTIONS_SET_ACCESS_CONTROL_ENGINE_GROUP = {"constant": "sites_configure_actions_set_access_control_engine_group",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.sites_configure_actions_set_access_control_engine_group}
        self.SITES_CONFIGURE_ACTIONS_SET_ADD_DEVICE_TO_ACCESS_CONTROL_ENGINE_GROUP = {"constant": "sites_configure_actions_set_add_device_to_access_control_engine_group",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.sites_configure_actions_set_add_device_to_access_control_engine_group}
        self.SITES_CONFIGURE_ACTIONS_SET_ADD_DEVICE_TO_POLICY_DOMAIN = {"constant": "sites_configure_actions_set_add_device_to_policy_domain",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.sites_configure_actions_set_add_device_to_policy_domain}
        self.SITES_CONFIGURE_ACTIONS_SET_ADD_SYSLOG_RECEIVER = {"constant": "sites_configure_actions_set_add_syslog_receiver",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.sites_configure_actions_set_add_syslog_receiver}
        self.SITES_CONFIGURE_ACTIONS_SET_ADD_TO_ARCHIVE = {"constant": "sites_configure_actions_set_add_to_archive",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.sites_configure_actions_set_add_to_archive}
        self.SITES_CONFIGURE_ACTIONS_SET_ADD_TO_MAP = {"constant": "sites_configure_actions_set_add_to_map",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_configure_actions_set_add_to_map}
        self.SITES_CONFIGURE_ACTIONS_SET_ADD_TRAP_RECEIVER = {"constant": "sites_configure_actions_set_add_trap_receiver",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.sites_configure_actions_set_add_trap_receiver}
        self.SITES_CONFIGURE_ACTIONS_SET_AUTOMATICALLY_ADD_DEVICES = {"constant": "sites_configure_actions_set_automatically_add_devices",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.sites_configure_actions_set_automatically_add_devices}
        self.SITES_CONFIGURE_ACTIONS_SET_ENABLE_AUTHENTICATION_USING_PORT_TEMPLATE = {"constant": "sites_configure_actions_set_enable_authentication_using_port_template",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.sites_configure_actions_set_enable_authentication_using_port_template}
        self.SITES_CONFIGURE_ACTIONS_SET_ENABLE_COLLECTION = {"constant": "sites_configure_actions_set_enable_collection",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.sites_configure_actions_set_enable_collection}
        self.SITES_CONFIGURE_ACTIONS_SET_MAP = {"constant": "sites_configure_actions_set_map",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.sites_configure_actions_set_map}
        self.SITES_CONFIGURE_ACTIONS_SET_POLICY_DOMAIN = {"constant": "sites_configure_actions_set_policy_domain",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.sites_configure_actions_set_policy_domain}
        self.SITES_CONFIGURE_ADDRESSES_CLICK_ADD = {"constant": "sites_configure_addresses_click_add",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_configure_addresses_click_add}
        self.SITES_CONFIGURE_ADDRESSES_CLICK_DELETE = {"constant": "sites_configure_addresses_click_delete",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_configure_addresses_click_delete}
        self.SITES_CONFIGURE_ADDRESSES_SELECT_ADDRESS = {"constant": "sites_configure_addresses_select_address",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.sites_configure_addresses_select_address}
        self.SITES_CONFIGURE_ADDRESSES_SET_ENABLED = {"constant": "sites_configure_addresses_set_enabled",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_addresses_set_enabled}
        self.SITES_CONFIGURE_CLICK_CANCEL = {"constant": "sites_configure_click_cancel",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.sites_configure_click_cancel}
        self.SITES_CONFIGURE_CLICK_CONFIGURE_DEVICES = {"constant": "sites_configure_click_configure_devices",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.sites_configure_click_configure_devices}
        self.SITES_CONFIGURE_CLICK_DISCOVER = {"constant": "sites_configure_click_discover",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.sites_configure_click_discover}
        self.SITES_CONFIGURE_CLICK_SAVE = {"constant": "sites_configure_click_save",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.sites_configure_click_save}
        self.SITES_CONFIGURE_CLICK_SCHEDULER = {"constant": "sites_configure_click_scheduler",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.sites_configure_click_scheduler}
        self.SITES_CONFIGURE_DEVICES_SELECT_DEVICE = {"constant": "sites_configure_devices_select_device",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_devices_select_device}
        self.SITES_CONFIGURE_PORTS_CLICK_EDIT = {"constant": "sites_configure_ports_click_edit",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.sites_configure_ports_click_edit}
        self.SITES_CONFIGURE_PORTS_ROW_CLICK_CANCEL = {"constant": "sites_configure_ports_row_click_cancel",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_configure_ports_row_click_cancel}
        self.SITES_CONFIGURE_PORTS_ROW_CLICK_UPDATE = {"constant": "sites_configure_ports_row_click_update",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_configure_ports_row_click_update}
        self.SITES_CONFIGURE_PORTS_ROW_SET_AUTHENTICATION = {"constant": "sites_configure_ports_row_set_authentication",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.sites_configure_ports_row_set_authentication}
        self.SITES_CONFIGURE_PORTS_ROW_SET_AUTO_NEGOTIATION = {"constant": "sites_configure_ports_row_set_auto_negotiation",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.sites_configure_ports_row_set_auto_negotiation}
        self.SITES_CONFIGURE_PORTS_ROW_SET_COLLECTION = {"constant": "sites_configure_ports_row_set_collection",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.sites_configure_ports_row_set_collection}
        self.SITES_CONFIGURE_PORTS_ROW_SET_LOOP_PROTECT = {"constant": "sites_configure_ports_row_set_loop_protect",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.sites_configure_ports_row_set_loop_protect}
        self.SITES_CONFIGURE_PORTS_ROW_SET_MVRP = {"constant": "sites_configure_ports_row_set_mvrp",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ports_row_set_mvrp}
        self.SITES_CONFIGURE_PORTS_ROW_SET_NODE_ALIAS = {"constant": "sites_configure_ports_row_set_node_alias",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.sites_configure_ports_row_set_node_alias}
        self.SITES_CONFIGURE_PORTS_ROW_SET_POLICY = {"constant": "sites_configure_ports_row_set_policy",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_configure_ports_row_set_policy}
        self.SITES_CONFIGURE_PORTS_ROW_SET_PVID = {"constant": "sites_configure_ports_row_set_pvid",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ports_row_set_pvid}
        self.SITES_CONFIGURE_PORTS_ROW_SET_SPAN_GUARD = {"constant": "sites_configure_ports_row_set_span_guard",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.sites_configure_ports_row_set_span_guard}
        self.SITES_CONFIGURE_PORTS_ROW_SET_TAGGED = {"constant": "sites_configure_ports_row_set_tagged",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_configure_ports_row_set_tagged}
        self.SITES_CONFIGURE_PORTS_ROW_SET_UNTAGGED = {"constant": "sites_configure_ports_row_set_untagged",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_configure_ports_row_set_untagged}
        self.SITES_CONFIGURE_PORTS_SELECT_PORT_CONFIGURATION = {"constant": "sites_configure_ports_select_port_configuration",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.sites_configure_ports_select_port_configuration}
        self.SITES_CONFIGURE_PORTS_SHOW_COLUMNS = {"constant": "sites_configure_ports_show_columns",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ports_show_columns}
        self.SITES_CONFIGURE_PROFILES_CLICK_ADD = {"constant": "sites_configure_profiles_click_add",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_profiles_click_add}
        self.SITES_CONFIGURE_PROFILES_CLICK_DELETE = {"constant": "sites_configure_profiles_click_delete",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_profiles_click_delete}
        self.SITES_CONFIGURE_PROFILES_CLICK_EDIT = {"constant": "sites_configure_profiles_click_edit",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_configure_profiles_click_edit}
        self.SITES_CONFIGURE_PROFILES_SELECT_PROFILE = {"constant": "sites_configure_profiles_select_profile",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.sites_configure_profiles_select_profile}
        self.SITES_CONFIGURE_PROFILES_SET_ACCEPT = {"constant": "sites_configure_profiles_set_accept",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_configure_profiles_set_accept}
        self.SITES_CONFIGURE_PROFILES_SET_REJECT = {"constant": "sites_configure_profiles_set_reject",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_configure_profiles_set_reject}
        self.SITES_CONFIGURE_VLAN_CLICK_ADD = {"constant": "sites_configure_vlan_click_add",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.sites_configure_vlan_click_add}
        self.SITES_CONFIGURE_VLAN_CLICK_DELETE = {"constant": "sites_configure_vlan_click_delete",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_vlan_click_delete}
        self.SITES_CONFIGURE_VLAN_CLICK_EDIT = {"constant": "sites_configure_vlan_click_edit",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.sites_configure_vlan_click_edit}
        self.SITES_CONFIGURE_VLAN_ROW_CLICK_CANCEL = {"constant": "sites_configure_vlan_row_click_cancel",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_vlan_row_click_cancel}
        self.SITES_CONFIGURE_VLAN_ROW_CLICK_UPDATE = {"constant": "sites_configure_vlan_row_click_update",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_vlan_row_click_update}
        self.SITES_CONFIGURE_VLAN_ROW_SET_ALWAYS_WRITE_TO_DEVICES = {"constant": "sites_configure_vlan_row_set_always_write_to_devices",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.sites_configure_vlan_row_set_always_write_to_devices}
        self.SITES_CONFIGURE_VLAN_ROW_SET_NAME = {"constant": "sites_configure_vlan_row_set_name",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_vlan_row_set_name}
        self.SITES_CONFIGURE_VLAN_ROW_SET_VID = {"constant": "sites_configure_vlan_row_set_vid",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.sites_configure_vlan_row_set_vid}
        self.SITES_CONFIGURE_VLAN_SELECT_VLAN = {"constant": "sites_configure_vlan_select_vlan",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.sites_configure_vlan_select_vlan}
        self.SITES_CONFIGURE_ZTP_SET_ADMIN_PROFILE = {"constant": "sites_configure_ztp_set_admin_profile",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_ztp_set_admin_profile}
        self.SITES_CONFIGURE_ZTP_SET_CONFIGURE_DEVICE = {"constant": "sites_configure_ztp_set_configure_device",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.sites_configure_ztp_set_configure_device}
        self.SITES_CONFIGURE_ZTP_SET_DNS_SERVER = {"constant": "sites_configure_ztp_set_dns_server",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ztp_set_dns_server}
        self.SITES_CONFIGURE_ZTP_SET_DOMAIN_NAME = {"constant": "sites_configure_ztp_set_domain_name",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_configure_ztp_set_domain_name}
        self.SITES_CONFIGURE_ZTP_SET_ENDING_IP_ADDRESS = {"constant": "sites_configure_ztp_set_ending_ip_address",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.sites_configure_ztp_set_ending_ip_address}
        self.SITES_CONFIGURE_ZTP_SET_GATEWAY_ADDRESS = {"constant": "sites_configure_ztp_set_gateway_address",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.sites_configure_ztp_set_gateway_address}
        self.SITES_CONFIGURE_ZTP_SET_LACP_ENABLED = {"constant": "sites_configure_ztp_set_lacp_enabled",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_configure_ztp_set_lacp_enabled}
        self.SITES_CONFIGURE_ZTP_SET_LACP_TYPE = {"constant": "sites_configure_ztp_set_lacp_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_ztp_set_lacp_type}
        self.SITES_CONFIGURE_ZTP_SET_LLDP_ENABLED = {"constant": "sites_configure_ztp_set_lldp_enabled",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_configure_ztp_set_lldp_enabled}
        self.SITES_CONFIGURE_ZTP_SET_LLDP_TYPE = {"constant": "sites_configure_ztp_set_lldp_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_ztp_set_lldp_type}
        self.SITES_CONFIGURE_ZTP_SET_MANAGEMENT_INTERFACE = {"constant": "sites_configure_ztp_set_management_interface",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.sites_configure_ztp_set_management_interface}
        self.SITES_CONFIGURE_ZTP_SET_MSTP_ENABLED = {"constant": "sites_configure_ztp_set_mstp_enabled",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_configure_ztp_set_mstp_enabled}
        self.SITES_CONFIGURE_ZTP_SET_MSTP_TYPE = {"constant": "sites_configure_ztp_set_mstp_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_ztp_set_mstp_type}
        self.SITES_CONFIGURE_ZTP_SET_MVRP_ENABLED = {"constant": "sites_configure_ztp_set_mvrp_enabled",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_configure_ztp_set_mvrp_enabled}
        self.SITES_CONFIGURE_ZTP_SET_MVRP_TYPE = {"constant": "sites_configure_ztp_set_mvrp_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_ztp_set_mvrp_type}
        self.SITES_CONFIGURE_ZTP_SET_NTP_SERVER = {"constant": "sites_configure_ztp_set_ntp_server",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ztp_set_ntp_server}
        self.SITES_CONFIGURE_ZTP_SET_POE_ENABLED = {"constant": "sites_configure_ztp_set_poe_enabled",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_configure_ztp_set_poe_enabled}
        self.SITES_CONFIGURE_ZTP_SET_POE_TYPE = {"constant": "sites_configure_ztp_set_poe_type",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.sites_configure_ztp_set_poe_type}
        self.SITES_CONFIGURE_ZTP_SET_POLL_GROUP = {"constant": "sites_configure_ztp_set_poll_group",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ztp_set_poll_group}
        self.SITES_CONFIGURE_ZTP_SET_POLL_TYPE = {"constant": "sites_configure_ztp_set_poll_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_configure_ztp_set_poll_type}
        self.SITES_CONFIGURE_ZTP_SET_STARTING_IP_ADDRESS = {"constant": "sites_configure_ztp_set_starting_ip_address",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.sites_configure_ztp_set_starting_ip_address}
        self.SITES_CONFIGURE_ZTP_SET_SUBNET_ADDRESS = {"constant": "sites_configure_ztp_set_subnet_address",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_configure_ztp_set_subnet_address}
        self.SITES_CONFIGURE_ZTP_SET_USE_DISCOVERED_IP = {"constant": "sites_configure_ztp_set_use_discovered_ip",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.sites_configure_ztp_set_use_discovered_ip}
        self.SITES_CONFIGURE_ZTP_SET_VXLAN_ENABLED = {"constant": "sites_configure_ztp_set_vxlan_enabled",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_configure_ztp_set_vxlan_enabled}
        self.SITES_CONFIGURE_ZTP_SET_VXLAN_TYPE = {"constant": "sites_configure_ztp_set_vxlan_type",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_configure_ztp_set_vxlan_type}
        self.SITES_CONFIRM_SITES_MENU_EXISTS = {"constant": "sites_confirm_sites_menu_exists",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.sites_confirm_sites_menu_exists}
        self.SITES_CONFIRM_SITE_EXISTS = {"constant": "sites_confirm_site_exists",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.sites_confirm_site_exists}
        self.SITES_CREATE_SITE = {"constant": "sites_create_site",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.sites_create_site}
        self.SITES_DELETE_SITE = {"constant": "sites_delete_site",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.sites_delete_site}
        self.SITES_DIALOG_ADDRESS_CLICK_CANCEL = {"constant": "sites_dialog_address_click_cancel",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.sites_dialog_address_click_cancel}
        self.SITES_DIALOG_ADDRESS_CLICK_OK = {"constant": "sites_dialog_address_click_ok",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.sites_dialog_address_click_ok}
        self.SITES_DIALOG_ADDRESS_SET_END_ADDRESS = {"constant": "sites_dialog_address_set_end_address",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_dialog_address_set_end_address}
        self.SITES_DIALOG_ADDRESS_SET_SEED_ADDRESS = {"constant": "sites_dialog_address_set_seed_address",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_dialog_address_set_seed_address}
        self.SITES_DIALOG_ADDRESS_SET_START_ADDRESS = {"constant": "sites_dialog_address_set_start_address",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.sites_dialog_address_set_start_address}
        self.SITES_DIALOG_ADDRESS_SET_SUBNET = {"constant": "sites_dialog_address_set_subnet",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.sites_dialog_address_set_subnet}
        self.SITES_DIALOG_ADDRESS_SET_TYPE = {"constant": "sites_dialog_address_set_type",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.sites_dialog_address_set_type}
        self.SITES_RENAME_SITE = {"constant": "sites_rename_site",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.sites_rename_site}
        self.SITES_SELECT_SUB_TAB = {"constant": "sites_select_sub_tab",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.sites_select_sub_tab}
        self.SITES_VALIDATE_ALL_SITE_SUMMARY_PARAMETERS = {"constant": "sites_validate_all_site_summary_parameters",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.sites_validate_all_site_summary_parameters}
        self.SITES_WAIT_FOR_SITE_ADD = {"constant": "sites_wait_for_site_add",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.sites_wait_for_site_add}
        self.SITES_WAIT_FOR_SITE_REMOVE = {"constant": "sites_wait_for_site_remove",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.sites_wait_for_site_remove}
