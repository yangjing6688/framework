"""
This class outlines all the constants for the devices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DevicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DevicesConstants(ApiConstants):
    def __init__(self):
        super(DevicesConstants, self).__init__()
        self.DEVICES_ADD_DEVICE = {"constant": "devices_add_device",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.devices_add_device}
        self.DEVICES_ADD_DEVICE_TO_GROUP = {"constant": "devices_add_device_to_group",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_add_device_to_group}
        self.DEVICES_CLOSE_DEVICE_TERMINAL = {"constant": "devices_close_device_terminal",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.devices_close_device_terminal}
        self.DEVICES_COLLECT_DEVICE_STATISTICS = {"constant": "devices_collect_device_statistics",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_collect_device_statistics}
        self.DEVICES_COLLECT_INTERFACE_STATISTICS = {"constant": "devices_collect_interface_statistics",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_collect_interface_statistics}
        self.DEVICES_COLLECT_PORT_STATISTICS = {"constant": "devices_collect_port_statistics",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_collect_port_statistics}
        self.DEVICES_CONFIGURE_DEVICE = {"constant": "devices_configure_device",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_configure_device}
        self.DEVICES_CONFIRM_ADMIN_PROFILE = {"constant": "devices_confirm_admin_profile",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.devices_confirm_admin_profile}
        self.DEVICES_CONFIRM_ASSET_TAG = {"constant": "devices_confirm_asset_tag",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_confirm_asset_tag}
        self.DEVICES_CONFIRM_CONTACT = {"constant": "devices_confirm_contact",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.devices_confirm_contact}
        self.DEVICES_CONFIRM_CONTEXT_MENU_EXISTS = {"constant": "devices_confirm_context_menu_exists",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_confirm_context_menu_exists}
        self.DEVICES_CONFIRM_DEFAULT_SITE = {"constant": "devices_confirm_default_site",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.devices_confirm_default_site}
        self.DEVICES_CONFIRM_DEVICE_IP_ARCHIVED = {"constant": "devices_confirm_device_ip_archived",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_confirm_device_ip_archived}
        self.DEVICES_CONFIRM_DEVICE_IS_COLLECTING_STATISTICS = {"constant": "devices_confirm_device_is_collecting_statistics",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.devices_confirm_device_is_collecting_statistics}
        self.DEVICES_CONFIRM_DEVICE_PORT_ALIAS = {"constant": "devices_confirm_device_port_alias",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_confirm_device_port_alias}
        self.DEVICES_CONFIRM_DEVICE_PORT_AUTHENTICATION = {"constant": "devices_confirm_device_port_authentication",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.devices_confirm_device_port_authentication}
        self.DEVICES_CONFIRM_DEVICE_PORT_AUTO_NEGOTIATION = {"constant": "devices_confirm_device_port_auto_negotiation",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.devices_confirm_device_port_auto_negotiation}
        self.DEVICES_CONFIRM_DEVICE_PORT_CONFIGURATION = {"constant": "devices_confirm_device_port_configuration",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.devices_confirm_device_port_configuration}
        self.DEVICES_CONFIRM_DEVICE_PORT_DEVICE_NICKNAME = {"constant": "devices_confirm_device_port_device_nickname",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_confirm_device_port_device_nickname}
        self.DEVICES_CONFIRM_DEVICE_PORT_DUPLEX = {"constant": "devices_confirm_device_port_duplex",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_confirm_device_port_duplex}
        self.DEVICES_CONFIRM_DEVICE_PORT_ENABLED = {"constant": "devices_confirm_device_port_enabled",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_confirm_device_port_enabled}
        self.DEVICES_CONFIRM_DEVICE_PORT_LAG = {"constant": "devices_confirm_device_port_lag",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_confirm_device_port_lag}
        self.DEVICES_CONFIRM_DEVICE_PORT_LOOP_PROTECT = {"constant": "devices_confirm_device_port_loop_protect",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_confirm_device_port_loop_protect}
        self.DEVICES_CONFIRM_DEVICE_PORT_MVRP = {"constant": "devices_confirm_device_port_mvrp",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_confirm_device_port_mvrp}
        self.DEVICES_CONFIRM_DEVICE_PORT_NICKNAME = {"constant": "devices_confirm_device_port_nickname",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_confirm_device_port_nickname}
        self.DEVICES_CONFIRM_DEVICE_PORT_NODE_ALIAS = {"constant": "devices_confirm_device_port_node_alias",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_confirm_device_port_node_alias}
        self.DEVICES_CONFIRM_DEVICE_PORT_POLICY = {"constant": "devices_confirm_device_port_policy",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_confirm_device_port_policy}
        self.DEVICES_CONFIRM_DEVICE_PORT_PVID = {"constant": "devices_confirm_device_port_pvid",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_confirm_device_port_pvid}
        self.DEVICES_CONFIRM_DEVICE_PORT_SPAN_GUARD = {"constant": "devices_confirm_device_port_span_guard",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_confirm_device_port_span_guard}
        self.DEVICES_CONFIRM_DEVICE_PORT_SPEED = {"constant": "devices_confirm_device_port_speed",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_confirm_device_port_speed}
        self.DEVICES_CONFIRM_DEVICE_PORT_TAGGED = {"constant": "devices_confirm_device_port_tagged",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_confirm_device_port_tagged}
        self.DEVICES_CONFIRM_DEVICE_PORT_UNTAGGED = {"constant": "devices_confirm_device_port_untagged",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_confirm_device_port_untagged}
        self.DEVICES_CONFIRM_DEVICE_SAVE = {"constant": "devices_confirm_device_save",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_confirm_device_save}
        self.DEVICES_CONFIRM_DEVICE_TERMINAL_ENTERS_DEVICE_PROMPT = {"constant": "devices_confirm_device_terminal_enters_device_prompt",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.devices_confirm_device_terminal_enters_device_prompt}
        self.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_COMPANY = {"constant": "devices_confirm_device_vendor_profile_company",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.devices_confirm_device_vendor_profile_company}
        self.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_DEVICE_TYPE = {"constant": "devices_confirm_device_vendor_profile_device_type",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.devices_confirm_device_vendor_profile_device_type}
        self.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_FAMILY = {"constant": "devices_confirm_device_vendor_profile_family",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.devices_confirm_device_vendor_profile_family}
        self.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_SUB_FAMILY = {"constant": "devices_confirm_device_vendor_profile_sub_family",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.devices_confirm_device_vendor_profile_sub_family}
        self.DEVICES_CONFIRM_DEVICE_VENDOR_PROFILE_VENDOR = {"constant": "devices_confirm_device_vendor_profile_vendor",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.devices_confirm_device_vendor_profile_vendor}
        self.DEVICES_CONFIRM_DEVICE_ZTP_CONFIGURE_DEVICE = {"constant": "devices_confirm_device_ztp_configure_device",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_confirm_device_ztp_configure_device}
        self.DEVICES_CONFIRM_DEVICE_ZTP_DNS_SERVER = {"constant": "devices_confirm_device_ztp_dns_server",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.devices_confirm_device_ztp_dns_server}
        self.DEVICES_CONFIRM_DEVICE_ZTP_DOMAIN_NAME = {"constant": "devices_confirm_device_ztp_domain_name",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_confirm_device_ztp_domain_name}
        self.DEVICES_CONFIRM_DEVICE_ZTP_GATEWAY_ADDRESS = {"constant": "devices_confirm_device_ztp_gateway_address",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.devices_confirm_device_ztp_gateway_address}
        self.DEVICES_CONFIRM_DEVICE_ZTP_IP_ADDRESS_SUBNET = {"constant": "devices_confirm_device_ztp_ip_address_subnet",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.devices_confirm_device_ztp_ip_address_subnet}
        self.DEVICES_CONFIRM_DEVICE_ZTP_LACP = {"constant": "devices_confirm_device_ztp_lacp",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_confirm_device_ztp_lacp}
        self.DEVICES_CONFIRM_DEVICE_ZTP_LLDP = {"constant": "devices_confirm_device_ztp_lldp",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_confirm_device_ztp_lldp}
        self.DEVICES_CONFIRM_DEVICE_ZTP_MANAGEMENT_INTERFACE = {"constant": "devices_confirm_device_ztp_management_interface",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.devices_confirm_device_ztp_management_interface}
        self.DEVICES_CONFIRM_DEVICE_ZTP_MSTP = {"constant": "devices_confirm_device_ztp_mstp",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_confirm_device_ztp_mstp}
        self.DEVICES_CONFIRM_DEVICE_ZTP_MVRP = {"constant": "devices_confirm_device_ztp_mvrp",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_confirm_device_ztp_mvrp}
        self.DEVICES_CONFIRM_DEVICE_ZTP_NTP_SERVER = {"constant": "devices_confirm_device_ztp_ntp_server",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.devices_confirm_device_ztp_ntp_server}
        self.DEVICES_CONFIRM_DEVICE_ZTP_POE = {"constant": "devices_confirm_device_ztp_poe",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_confirm_device_ztp_poe}
        self.DEVICES_CONFIRM_DEVICE_ZTP_SERIAL_NUMBER = {"constant": "devices_confirm_device_ztp_serial_number",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_confirm_device_ztp_serial_number}
        self.DEVICES_CONFIRM_DEVICE_ZTP_XVLAN = {"constant": "devices_confirm_device_ztp_xvlan",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_confirm_device_ztp_xvlan}
        self.DEVICES_CONFIRM_FIRMWARE_VERSION = {"constant": "devices_confirm_firmware_version",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_confirm_firmware_version}
        self.DEVICES_CONFIRM_FIRMWARE_VERSION_AND_REDISCOVER = {"constant": "devices_confirm_firmware_version_and_rediscover",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.devices_confirm_firmware_version_and_rediscover}
        self.DEVICES_CONFIRM_IP_ADMIN_PROFILE = {"constant": "devices_confirm_ip_admin_profile",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_confirm_ip_admin_profile}
        self.DEVICES_CONFIRM_IP_COLLECTION_STATISTICS = {"constant": "devices_confirm_ip_collection_statistics",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_confirm_ip_collection_statistics}
        self.DEVICES_CONFIRM_IP_EXISTS = {"constant": "devices_confirm_ip_exists",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_confirm_ip_exists}
        self.DEVICES_CONFIRM_IP_STATS = {"constant": "devices_confirm_ip_stats",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_confirm_ip_stats}
        self.DEVICES_CONFIRM_IP_SYSLOG_STATUS = {"constant": "devices_confirm_ip_syslog_status",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_confirm_ip_syslog_status}
        self.DEVICES_CONFIRM_IP_TRAP_STATUS = {"constant": "devices_confirm_ip_trap_status",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_confirm_ip_trap_status}
        self.DEVICES_CONFIRM_LOCATION = {"constant": "devices_confirm_location",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_confirm_location}
        self.DEVICES_CONFIRM_NICKNAME = {"constant": "devices_confirm_nickname",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_confirm_nickname}
        self.DEVICES_CONFIRM_NOTE = {"constant": "devices_confirm_note",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.devices_confirm_note}
        self.DEVICES_CONFIRM_POLL_GROUP = {"constant": "devices_confirm_poll_group",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.devices_confirm_poll_group}
        self.DEVICES_CONFIRM_POLL_TYPE = {"constant": "devices_confirm_poll_type",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_confirm_poll_type}
        self.DEVICES_CONFIRM_REMOVE_FROM_SERVICE = {"constant": "devices_confirm_remove_from_service",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_confirm_remove_from_service}
        self.DEVICES_CONFIRM_SERIAL_NUMBER = {"constant": "devices_confirm_serial_number",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.devices_confirm_serial_number}
        self.DEVICES_CONFIRM_SNMP_RETRIES = {"constant": "devices_confirm_snmp_retries",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.devices_confirm_snmp_retries}
        self.DEVICES_CONFIRM_SNMP_TIMEOUT = {"constant": "devices_confirm_snmp_timeout",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.devices_confirm_snmp_timeout}
        self.DEVICES_CONFIRM_STATUS = {"constant": "devices_confirm_status",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.devices_confirm_status}
        self.DEVICES_CONFIRM_SYSTEM_NAME = {"constant": "devices_confirm_system_name",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_confirm_system_name}
        self.DEVICES_CONFIRM_TABLE_VALUE = {"constant": "devices_confirm_table_value",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_confirm_table_value}
        self.DEVICES_CONFIRM_TOPOLOGY_LAYER = {"constant": "devices_confirm_topology_layer",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_confirm_topology_layer}
        self.DEVICES_CONFIRM_USER_DATA = {"constant": "devices_confirm_user_data",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_confirm_user_data}
        self.DEVICES_CONFIRM_VLAN_NAME = {"constant": "devices_confirm_vlan_name",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_confirm_vlan_name}
        self.DEVICES_CONFIRM_VLAN_VID = {"constant": "devices_confirm_vlan_vid",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_confirm_vlan_vid}
        self.DEVICES_CONFIRM_VLAN_WRITE_TO_DEVICE = {"constant": "devices_confirm_vlan_write_to_device",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_confirm_vlan_write_to_device}
        self.DEVICES_DELETE_DEVICE = {"constant": "devices_delete_device",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.devices_delete_device}
        self.DEVICES_DELETE_SELECTED_DEVICES = {"constant": "devices_delete_selected_devices",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_delete_selected_devices}
        self.DEVICES_DEVICE_VIEW_DISABLE_PORT = {"constant": "devices_device_view_disable_port",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_device_view_disable_port}
        self.DEVICES_DEVICE_VIEW_ENABLE_PORT = {"constant": "devices_device_view_enable_port",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_device_view_enable_port}
        self.DEVICES_DEVICE_VIEW_PORTS_EXPAND_TREE = {"constant": "devices_device_view_ports_expand_tree",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.devices_device_view_ports_expand_tree}
        self.DEVICES_DEVICE_VIEW_PORTS_VERIFY_PVID = {"constant": "devices_device_view_ports_verify_pvid",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.devices_device_view_ports_verify_pvid}
        self.DEVICES_DEVICE_VIEW_PORTS_VERIFY_VLAN_ID_VLAN_NAME_UNTAG_TAG = {"constant": "devices_device_view_ports_verify_vlan_id_vlan_name_untag_tag",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.devices_device_view_ports_verify_vlan_id_vlan_name_untag_tag}
        self.DEVICES_DEVICE_VIEW_SELECT_TAB = {"constant": "devices_device_view_select_tab",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_device_view_select_tab}
        self.DEVICES_DEVICE_VIEW_VERIFY_VLAN_NAME_AND_TAG = {"constant": "devices_device_view_verify_vlan_name_and_tag",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.devices_device_view_verify_vlan_name_and_tag}
        self.DEVICES_DEVICE_VIEW_VERIFY_VLAN_NAME_AND_TAG_VOSS = {"constant": "devices_device_view_verify_vlan_name_and_tag_voss",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.devices_device_view_verify_vlan_name_and_tag_voss}
        self.DEVICES_DEVICE_VIEW_VLAN_VLAN_PORT_TABLE_VERIFY_PORT_AND_PVID_VOSS = {"constant": "devices_device_view_vlan_vlan_port_table_verify_port_and_pvid_voss",
                                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                                   "link": self.link.devices_device_view_vlan_vlan_port_table_verify_port_and_pvid_voss}
        self.DEVICES_DEVICE_VIEW_VLAN_VLAN_TABLE_VERIFY_TAG_AND_PORTS_VOSS = {"constant": "devices_device_view_vlan_vlan_table_verify_tag_and_ports_voss",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.devices_device_view_vlan_vlan_table_verify_tag_and_ports_voss}
        self.DEVICES_DISABLE_PORT = {"constant": "devices_disable_port",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.devices_disable_port}
        self.DEVICES_EDIT_DEVICE_CANCEL = {"constant": "devices_edit_device_cancel",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.devices_edit_device_cancel}
        self.DEVICES_EDIT_DEVICE_ENFORCE_PREVIEW = {"constant": "devices_edit_device_enforce_preview",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_edit_device_enforce_preview}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW = {"constant": "devices_edit_device_ports_edit_row",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_edit_device_ports_edit_row}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_ALIAS = {"constant": "devices_edit_device_ports_edit_row_alias",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_edit_device_ports_edit_row_alias}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_AUTHENTICATION = {"constant": "devices_edit_device_ports_edit_row_authentication",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.devices_edit_device_ports_edit_row_authentication}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_AUTO_NEGOTIATION = {"constant": "devices_edit_device_ports_edit_row_auto_negotiation",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.devices_edit_device_ports_edit_row_auto_negotiation}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_CLEAR_TAGGED = {"constant": "devices_edit_device_ports_edit_row_clear_tagged",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.devices_edit_device_ports_edit_row_clear_tagged}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_CLEAR_UNTAGGED = {"constant": "devices_edit_device_ports_edit_row_clear_untagged",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.devices_edit_device_ports_edit_row_clear_untagged}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_CONFIGURATION = {"constant": "devices_edit_device_ports_edit_row_configuration",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.devices_edit_device_ports_edit_row_configuration}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_DUPLEX = {"constant": "devices_edit_device_ports_edit_row_duplex",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.devices_edit_device_ports_edit_row_duplex}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_ENABLED = {"constant": "devices_edit_device_ports_edit_row_enabled",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.devices_edit_device_ports_edit_row_enabled}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_LAG = {"constant": "devices_edit_device_ports_edit_row_lag",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_edit_device_ports_edit_row_lag}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_LOOP_PROTECT = {"constant": "devices_edit_device_ports_edit_row_loop_protect",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.devices_edit_device_ports_edit_row_loop_protect}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_MVRP = {"constant": "devices_edit_device_ports_edit_row_mvrp",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.devices_edit_device_ports_edit_row_mvrp}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_NICKNAME = {"constant": "devices_edit_device_ports_edit_row_nickname",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_edit_device_ports_edit_row_nickname}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_NODE_ALIAS = {"constant": "devices_edit_device_ports_edit_row_node_alias",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.devices_edit_device_ports_edit_row_node_alias}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_PORT_TEMPLATE = {"constant": "devices_edit_device_ports_edit_row_port_template",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.devices_edit_device_ports_edit_row_port_template}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_PVID = {"constant": "devices_edit_device_ports_edit_row_pvid",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.devices_edit_device_ports_edit_row_pvid}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_SPAN_GUARD = {"constant": "devices_edit_device_ports_edit_row_span_guard",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.devices_edit_device_ports_edit_row_span_guard}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_SPEED = {"constant": "devices_edit_device_ports_edit_row_speed",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_edit_device_ports_edit_row_speed}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_TAGGED = {"constant": "devices_edit_device_ports_edit_row_tagged",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.devices_edit_device_ports_edit_row_tagged}
        self.DEVICES_EDIT_DEVICE_PORTS_EDIT_ROW_UNTAGGED = {"constant": "devices_edit_device_ports_edit_row_untagged",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_edit_device_ports_edit_row_untagged}
        self.DEVICES_EDIT_DEVICE_PORTS_ROW_EDITOR_CANCEL = {"constant": "devices_edit_device_ports_row_editor_cancel",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_edit_device_ports_row_editor_cancel}
        self.DEVICES_EDIT_DEVICE_PORTS_ROW_EDITOR_UPDATE = {"constant": "devices_edit_device_ports_row_editor_update",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_edit_device_ports_row_editor_update}
        self.DEVICES_EDIT_DEVICE_PORTS_SELECT_PORT = {"constant": "devices_edit_device_ports_select_port",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.devices_edit_device_ports_select_port}
        self.DEVICES_EDIT_DEVICE_PORTS_SELECT_ROW = {"constant": "devices_edit_device_ports_select_row",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_edit_device_ports_select_row}
        self.DEVICES_EDIT_DEVICE_PORTS_SHOW_COLUMNS = {"constant": "devices_edit_device_ports_show_columns",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_edit_device_ports_show_columns}
        self.DEVICES_EDIT_DEVICE_RELOAD_DEVICE = {"constant": "devices_edit_device_reload_device",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_edit_device_reload_device}
        self.DEVICES_EDIT_DEVICE_REMOVE_FROM_SERVICE = {"constant": "devices_edit_device_remove_from_service",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.devices_edit_device_remove_from_service}
        self.DEVICES_EDIT_DEVICE_SAVE = {"constant": "devices_edit_device_save",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_edit_device_save}
        self.DEVICES_EDIT_DEVICE_SELECT_TAB = {"constant": "devices_edit_device_select_tab",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_edit_device_select_tab}
        self.DEVICES_EDIT_DEVICE_SET_ADMIN_PROFILE = {"constant": "devices_edit_device_set_admin_profile",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.devices_edit_device_set_admin_profile}
        self.DEVICES_EDIT_DEVICE_SET_ASSET_TAG = {"constant": "devices_edit_device_set_asset_tag",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_edit_device_set_asset_tag}
        self.DEVICES_EDIT_DEVICE_SET_CONTACT = {"constant": "devices_edit_device_set_contact",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_edit_device_set_contact}
        self.DEVICES_EDIT_DEVICE_SET_DEFAULT_SITE = {"constant": "devices_edit_device_set_default_site",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_edit_device_set_default_site}
        self.DEVICES_EDIT_DEVICE_SET_LOCATION = {"constant": "devices_edit_device_set_location",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_edit_device_set_location}
        self.DEVICES_EDIT_DEVICE_SET_NICKNAME = {"constant": "devices_edit_device_set_nickname",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_edit_device_set_nickname}
        self.DEVICES_EDIT_DEVICE_SET_NOTE = {"constant": "devices_edit_device_set_note",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.devices_edit_device_set_note}
        self.DEVICES_EDIT_DEVICE_SET_POLL_GROUP = {"constant": "devices_edit_device_set_poll_group",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_edit_device_set_poll_group}
        self.DEVICES_EDIT_DEVICE_SET_POLL_TYPE = {"constant": "devices_edit_device_set_poll_type",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_edit_device_set_poll_type}
        self.DEVICES_EDIT_DEVICE_SET_SNMP_RETRIES = {"constant": "devices_edit_device_set_snmp_retries",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_edit_device_set_snmp_retries}
        self.DEVICES_EDIT_DEVICE_SET_SNMP_TIMEOUT = {"constant": "devices_edit_device_set_snmp_timeout",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_edit_device_set_snmp_timeout}
        self.DEVICES_EDIT_DEVICE_SET_SYSTEM_NAME = {"constant": "devices_edit_device_set_system_name",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_edit_device_set_system_name}
        self.DEVICES_EDIT_DEVICE_SET_TOPOLOGY_LAYER = {"constant": "devices_edit_device_set_topology_layer",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_edit_device_set_topology_layer}
        self.DEVICES_EDIT_DEVICE_SET_USER_DATA = {"constant": "devices_edit_device_set_user_data",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_edit_device_set_user_data}
        self.DEVICES_EDIT_DEVICE_VENDOR_PROFILE_DEVICE_TYPE = {"constant": "devices_edit_device_vendor_profile_device_type",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.devices_edit_device_vendor_profile_device_type}
        self.DEVICES_EDIT_DEVICE_VENDOR_PROFILE_FAMILY = {"constant": "devices_edit_device_vendor_profile_family",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.devices_edit_device_vendor_profile_family}
        self.DEVICES_EDIT_DEVICE_VENDOR_PROFILE_SUB_FAMILY = {"constant": "devices_edit_device_vendor_profile_sub_family",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.devices_edit_device_vendor_profile_sub_family}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_ADD = {"constant": "devices_edit_device_vlan_definition_add",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.devices_edit_device_vlan_definition_add}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_DELETE = {"constant": "devices_edit_device_vlan_definition_delete",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.devices_edit_device_vlan_definition_delete}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_EDIT = {"constant": "devices_edit_device_vlan_definition_edit",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_edit_device_vlan_definition_edit}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SELECT_ROW = {"constant": "devices_edit_device_vlan_definition_select_row",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.devices_edit_device_vlan_definition_select_row}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_ALWAYS_WRITE_TO_DEVICES = {"constant": "devices_edit_device_vlan_definition_set_always_write_to_devices",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.devices_edit_device_vlan_definition_set_always_write_to_devices}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_NAME = {"constant": "devices_edit_device_vlan_definition_set_name",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.devices_edit_device_vlan_definition_set_name}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_VID = {"constant": "devices_edit_device_vlan_definition_set_vid",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_edit_device_vlan_definition_set_vid}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_SET_VRF = {"constant": "devices_edit_device_vlan_definition_set_vrf",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_edit_device_vlan_definition_set_vrf}
        self.DEVICES_EDIT_DEVICE_VLAN_DEFINITION_UPDATE = {"constant": "devices_edit_device_vlan_definition_update",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.devices_edit_device_vlan_definition_update}
        self.DEVICES_ENABLE_PORT = {"constant": "devices_enable_port",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.devices_enable_port}
        self.DEVICES_EXPAND_DEVICE_TREE_NODE = {"constant": "devices_expand_device_tree_node",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_expand_device_tree_node}
        self.DEVICES_LAUNCH_WEBVIEW = {"constant": "devices_launch_webview",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.devices_launch_webview}
        self.DEVICES_MAPS_ADD_TO_MAP = {"constant": "devices_maps_add_to_map",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.devices_maps_add_to_map}
        self.DEVICES_OPEN_DEVICE_TERMINAL = {"constant": "devices_open_device_terminal",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.devices_open_device_terminal}
        self.DEVICES_OPEN_DEVICE_VIEW = {"constant": "devices_open_device_view",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_open_device_view}
        self.DEVICES_OPEN_DEVICE_VIEW_FLEXVIEW = {"constant": "devices_open_device_view_flexview",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_open_device_view_flexview}
        self.DEVICES_OPEN_DEVICE_VIEW_INTERFACE_STATISTICS = {"constant": "devices_open_device_view_interface_statistics",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.devices_open_device_view_interface_statistics}
        self.DEVICES_OPEN_DEVICE_VIEW_PHYSICAL_ENTITY_SUMMARY = {"constant": "devices_open_device_view_physical_entity_summary",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.devices_open_device_view_physical_entity_summary}
        self.DEVICES_REFRESH_DEVICES_TABLE = {"constant": "devices_refresh_devices_table",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.devices_refresh_devices_table}
        self.DEVICES_REFRESH_DEVICE_TREE_MY_NETWORK = {"constant": "devices_refresh_device_tree_my_network",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_refresh_device_tree_my_network}
        self.DEVICES_REFRESH_PORT_STATUS = {"constant": "devices_refresh_port_status",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_refresh_port_status}
        self.DEVICES_REFRESH_REDISCOVER_DEVICE = {"constant": "devices_refresh_rediscover_device",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.devices_refresh_rediscover_device}
        self.DEVICES_REGISTER_SYSLOG_RECEIVER = {"constant": "devices_register_syslog_receiver",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_register_syslog_receiver}
        self.DEVICES_REGISTER_TRAP_RECEIVER = {"constant": "devices_register_trap_receiver",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_register_trap_receiver}
        self.DEVICES_REMOVE_DEVICE_FROM_GROUP = {"constant": "devices_remove_device_from_group",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_remove_device_from_group}
        self.DEVICES_SELECT_ALL_DEVICES_IN_TABLE = {"constant": "devices_select_all_devices_in_table",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_select_all_devices_in_table}
        self.DEVICES_SELECT_CONTEXT_MENU = {"constant": "devices_select_context_menu",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_select_context_menu}
        self.DEVICES_SELECT_DEVICES_SUMMARY_SUB_TAB = {"constant": "devices_select_devices_summary_sub_tab",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_select_devices_summary_sub_tab}
        self.DEVICES_SELECT_DEVICE_IN_TABLE = {"constant": "devices_select_device_in_table",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_select_device_in_table}
        self.DEVICES_SELECT_DEVICE_TREE_CONTEXT = {"constant": "devices_select_device_tree_context",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_select_device_tree_context}
        self.DEVICES_SELECT_DEVICE_TREE_NODE = {"constant": "devices_select_device_tree_node",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_select_device_tree_node}
        self.DEVICES_SELECT_SUB_TAB = {"constant": "devices_select_sub_tab",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.devices_select_sub_tab}
        self.DEVICES_SET_DEVICE_PROFILE = {"constant": "devices_set_device_profile",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.devices_set_device_profile}
        self.DEVICES_UNREGISTER_SYSLOG_RECEIVER = {"constant": "devices_unregister_syslog_receiver",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_unregister_syslog_receiver}
        self.DEVICES_UNREGISTER_TRAP_RECEIVER = {"constant": "devices_unregister_trap_receiver",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devices_unregister_trap_receiver}
        self.DEVICES_WAIT_FOR_DEVICE_ADD = {"constant": "devices_wait_for_device_add",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_wait_for_device_add}
        self.DEVICES_WAIT_FOR_DEVICE_REMOVE = {"constant": "devices_wait_for_device_remove",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_wait_for_device_remove}
        self.DEVICES_WAIT_FOR_DEVICE_VALUE = {"constant": "devices_wait_for_device_value",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.devices_wait_for_device_value}
