from extauto.xiq.defs.NavigatorWebElementDefinitions import NavigatorWebElementDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class NavigatorWebElements(NavigatorWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_common_objects_sub_tab(self):
        return self.weh.get_element(self.configure_common_objects_menu_item)

    def get_configure_tab(self):
        return self.weh.get_element(self.configure_nav)

    def get_configure_tab_img_class(self):
        return self.weh.get_element(self.configure_nav_img).get_attribute('class')

    def get_policy_toggle(self):
        return self.weh.get_element(self.policy_toggle)

    def get_policy_toggle_right_arrow(self):
        return self.weh.get_element(self.policy_toggle_right_arrow)

    def get_auto_provisioning_option(self):
        return self.weh.get_element(self.auto_provisioning_option)

    def get_manage_tab(self):
        return self.weh.get_element(self.manage_nav)

    def get_manage_tab_img_class(self):
        return self.weh.get_element(self.manage_nav_img).get_attribute('class')

    def get_ml_insight_tab(self):
        return self.weh.get_element(self.ml_insight_tab)

    def get_ml_insight_tab_img_class(self):
        return self.weh.get_element(self.ml_insight_tab_img).get_attribute('class')

    def get_devices_nav(self):
        return self.weh.get_element(self.device_nav)

    def get_devices_page(self):
        return self.weh.get_element(self.devices_page)

    def get_ssid_option(self):
        return self.weh.get_element(self.common_objects_ssids)

    def get_manage_tools_menu_item(self):
        return self.weh.get_element(self.manage_tools_menu_item)

    def get_subtab_head_img_nav(self):
        return self.weh.get_element(self.subtab_head_img_nav)

    def get_network_policies_sub_tab(self):
        return self.weh.get_element(self.configure_network_policy_nav)

    def get_clients_sub_tab(self):
        return self.weh.get_element(self.manage_clients_nav)

    def get_user_account_nav(self):
        return self.weh.get_element(self.user_account_nav)

    def get_global_settings_nav(self):
        return self.weh.get_element(self.global_settings)

    def get_configure_users_nav(self):
        return self.weh.get_element(self.configure_users_nav)

    def get_configure_users_user_management_side_menu(self):
        toggle_attr = self.weh.get_element(self.user_management_dropdown_toggle).get_attribute("class")
        if "right" in toggle_attr:
            if self.weh.get_element(self.configure_users_user_management_side_menu):
                return self.weh.get_element(self.configure_users_user_management_side_menu)
            elif self.weh.get_element(self.deutcshe_configure_users_user_management_side_menu):
                return self.weh.get_element(self.deutcshe_configure_users_user_management_side_menu)

    def get_configure_user_group_side_nav_item(self):
        if self.weh.get_element(self.configure_user_group_side_nav_item):
            return self.weh.get_element(self.configure_user_group_side_nav_item)
        elif self.weh.get_element(self.deutcshe_configure_user_group_side_nav_item):
            return self.weh.get_element(self.deutcshe_configure_user_group_side_nav_item)

    def get_common_object_authentication_tab(self):
        return self.weh.get_element(self.common_object_authentication_tab)

    def get_common_object_authentication_captive_portal(self):
        return self.weh.get_element(self.common_object_authentication_captive_portal)

    def get_common_object_authentication_aaa_server_settings(self):
        return self.weh.get_element(self.common_object_authentication_aaa_server_settings)

    def get_common_object_authentication_ad_servers(self):
        return self.weh.get_element(self.common_object_authentication_ad_servers)

    def get_common_object_authentication_external_radius_server(self):
        return self.weh.get_element(self.common_object_authentication_external_radius_server)

    def get_common_object_authentication_extreme_networks_a3(self):
        return self.weh.get_element(self.common_object_authentication_extreme_networks_a3)

    def get_common_object_authentication_servers(self):
        return self.weh.get_element(self.common_object_authentication_servers)

    def get_common_object_authentication_ldap_servers(self):
        return self.weh.get_element(self.common_object_authentication_ldap_servers)

    def get_manage_security_nav(self):
        return self.weh.get_element(self.manage_security_nav)

    def get_common_object_security_tab(self):
        return self.weh.get_element(self.common_object_security_tab)

    def get_common_object_security_wips_policies(self):
        return self.weh.get_element(self.common_object_security_wips_policies)

    def get_common_object_policy_tab(self):
        return self.weh.get_element(self.common_object_policy_tab )

    def get_common_object_policy_ap_template(self):
        return self.weh.get_element(self.common_object_policy_ap_template)

    def get_manage_reports_nav(self):
        return self.weh.get_element(self.manage_reports_nav)

    def get_common_object_policy_port_types(self):
        return self.weh.get_element(self.common_object_policy_port_types)

    def get_common_object_network_tab(self):
        return self.weh.get_element(self.common_object_network_tab )

    def get_common_object_network_sub_network_space(self):
        return self.weh.get_element(self.common_object_network_sub_network_space)

    def get_common_object_basic_tab(self):
        return self.weh.get_element(self.common_object_basic_tab)

    def get_common_object_basic_client_mode_profiles(self):
        return self.weh.get_element(self.common_object_basic_client_mode_profiles)

    def get_common_object_basic_vlans(self):
        return self.weh.get_element(self.common_object_basic_vlans)

    def get_common_object_basic_supplemental_cli(self):
        return self.weh.get_element(self.common_object_basic_supplemental_cli)

    def get_manage_alarms_nav(self):
        return self.weh.get_element(self.manage_alarms_nav)

    def get_ml_insight_client360(self):
        return self.weh.get_element(self.ml_insight_client360)

    def get_ml_insight_network360plan(self):
        return self.weh.get_element(self.ml_insight_network360plan)

    def get_ml_insight_network360monitor(self):
        return self.weh.get_element(self.ml_insight_network360monitor)

    def get_ml_insight_network_scorecard(self):
        return self.weh.get_element(self.ml_insight_networkScorecard)

    def get_ml_insight_retail(self):
        return self.weh.get_element(self.ml_insight_retail)

    def get_network_policy_list_view(self):
        return self.weh.get_element(self.list_view)

    def get_network_policy_card_view(self):
        return self.weh.get_element(self.card_view)

    def get_network_policy_page_size(self, page_size='100'):
        if els := self.weh.get_elements(self.network_policy_page_size):
            if els:
                for el in els:
                    if str(page_size) in el.text:
                        return el

    def get_device_actions_button(self):
        return self.weh.get_element(self.device_actions_button)

    def get_device_utilities(self):
        return self.weh.get_element(self.device_utilities)

    def get_utilities_status_wifi_status_summary(self):
        return self.weh.get_element(self.utilities_status_wifi_status_summary)

    def get_switch_template_option(self):
        return self.weh.get_element(self.common_objects_switch_templates)

    def get_api_token_mgmt_tab(self):
        return self.weh.get_element(self.api_token_mgmt_tab)

    def get_a3_tab(self):
        return self.weh.get_element(self.a3_nav)

    def get_a3_tab_img_class(self):
        return self.weh.get_element(self.a3_nav_img).get_attribute('class')

    def get_a3_inventory_tab(self):
        return self.weh.get_element(self.a3_inventory_menu)

    def get_a3_reporting_tab(self):
        return self.weh.get_element(self.a3_reporting_menu)

    def get_air_defence_menu(self):
        return self.weh.get_element(self.air_defence_nav)

    def get_onboard_tab(self):
        return self.weh.get_element(self.onboard_nav)

    def get_communications_nav(self):
        return self.weh.get_element(self.global_header_communication_nav)

    def get_extreme_iot_essentials_menu(self):
        return self.weh.get_element(self.extreme_IOT_essentials)

    def get_extreme_iot_essentials_devices_submenu(self):
        return self.weh.get_element(self.extreme_IOT_devices)

    def get_extreme_iot_essentials_dashboard_submenu(self):
        return self.weh.get_element(self.extreme_IOT_dashboard)

    def get_extreme_iot_essentials_clients_submenu(self):
        return self.weh.get_element(self.extreme_IOT_clients)

    def get_extreme_iot_essentials_user_profiles_submenu(self):
        return self.weh.get_element(self.extreme_IOT_user_profiles)

    def get_extreme_iot_essentials_policy_groups_submenu(self):
        return self.weh.get_element(self.extreme_IOT_policy_groups)

    def get_extreme_iot_essentials_subscribe_button(self):
        return self.weh.get_element(self.extreme_IOT_subscribe_button)

    def get_extreme_guest_subscribe_button(self):
        return self.weh.get_element(self.extreme_guest_subscribe_button)

    def get_extreme_location_subscribe_button(self):
        return self.weh.get_element(self.extreme_location_subscribe_button)

    def get_extreme_guest_menu(self):
        return self.weh.get_element(self.extreme_guest)

    def get_extreme_guest_configure_tab(self):
        return self.weh.get_element(self.extreme_guest_configure_tab)

    def get_extreme_guest_analyze_tab(self):
        return self.weh.get_element(self.extreme_guest_analyze_tab)

    def get_extreme_guest_configure_settings_menu(self):
        return self.weh.get_element(self.extreme_guest_configure_settings_menu)

    def get_eguest_configure_authorization_policy_menu(self):
        return self.weh.get_element(self.eguest_configure_authorization_policy_menu)

    def get_eguest_configure_access_groups_menu(self):
        return self.weh.get_element(self.eguest_configure_access_groups_menu)

    def get_eguest_configure_deployment_menu(self):
        return self.weh.get_element(self.eguest_configure_deployment_menu)

    def get_eguest_configure_location_menu(self):
        return self.weh.get_element(self.eguest_configure_location_menu)

    def get_eguest_configure_network_menu(self):
        return self.weh.get_element(self.eguest_configure_network_menu)

    def get_eguest_configure_devices_menu(self):
        return self.weh.get_element(self.eguest_configure_devices_menu)

    def get_eguest_configure_notification_menu(self):
        return self.weh.get_element(self.eguest_configure_notification_menu)

    def get_eguest_configure_notification_policy_menu(self):
        return self.weh.get_element(self.eguest_configure_notification_policy_menu)

    def get_eguest_configure_onboarding_menu(self):
        return self.weh.get_element(self.eguest_configure_onboarding_menu)

    def get_eguest_configure_onboarding_policy_menu(self):
        return self.weh.get_element(self.eguest_configure_onboarding_policy_menu)

    def get_eguest_configure_onboarding_rules_menu(self):
        return self.weh.get_element(self.eguest_configure_onboarding_rules_menu)

    def get_eguest_configure_splash_templates_menu(self):
        return self.weh.get_element(self.eguest_configure_splash_templates_menu)

    def get_eguest_configure_users_menu(self):
        return self.weh.get_element(self.eguest_configure_users_menu)

    def get_eguest_configure_clients_menu(self):
        return self.weh.get_element(self.eguest_configure_clients_menu)

    def get_extreme_location_dashboard_menu(self):
        return self.weh.get_element(self.extreme_location_dashboard_menu)

    def get_extreme_location_sites_menu(self):
        return self.weh.get_element(self.extreme_location_sites_menu)

    def get_extreme_location_category_menu(self):
        return self.weh.get_element(self.extreme_location_category_menu)

    def get_extreme_location_access_points_menu(self):
        return self.weh.get_element(self.extreme_location_access_points_menu)

    def get_extreme_location_beacons_menu(self):
        return self.weh.get_element(self.extreme_location_beacons_menu)

    def get_extreme_location_asset_management_menu(self):
        return self.weh.get_element(self.extreme_location_asset_management_menu)

    def get_extreme_location_asset_management_assets_menu(self):
        return self.weh.get_element(self.extreme_location_asset_management_assets_menu)

    def get_extreme_location_asset_management_alarms_menu(self):
        return self.weh.get_element(self.extreme_location_asset_management_alarms_menu)

    def get_extreme_location_devices_menu(self):
        return self.weh.get_element(self.extreme_location_devices_menu)

    def get_extreme_location_devices_wireless_devices_menu(self):
        return self.weh.get_element(self.extreme_location_devices_wireless_devices_menu)

    def get_extreme_location_devices_bss_devices_menu(self):
        return self.weh.get_element(self.extreme_location_devices_bss_devices_menu)

    def get_extreme_location_settings_menu(self):
        return self.weh.get_element(self.extreme_location_settings_menu)

    def get_extreme_location_settings_device_classification_menu(self):
        return self.weh.get_element(self.extreme_location_settings_device_classification_menu)

    def get_extreme_location_settings_threshold_menu(self):
        return self.weh.get_element(self.extreme_location_settings_threshold_menu)

    def get_extreme_location_settings_third_party_config_menu(self):
        return self.weh.get_element(self.extreme_location_settings_third_party_config_menu)

    def get_extreme_location_settings_alarms_menu(self):
        return self.weh.get_element(self.extreme_location_settings_alarms_menu)

    def get_extreme_location_menu(self):
        return self.weh.get_element(self.extreme_location)

    def get_essentials_menu(self):
        return self.weh.get_element(self.essentials_menu)

    def get_essentials_menu_img_class(self):
        return self.weh.get_element(self.essentials_menu_img).get_attribute('class')

    def get_ccg_option(self):
        return self.weh.get_element(self.common_objects_ccgs)

    def get_classification_option(self):
        return self.weh.get_element(self.common_objects_classification)

    def get_configure_ppsk_classification_side_nav_item(self):
        return self.weh.get_element(self.configure_ppsk_classification_side_nav_item)

    def get_viq_management_menu(self):
        return self.weh.get_element(self.viq_management_menu)

    def get_manage_applications_menu_item(self):
        return self.weh.get_element(self.manage_applications_menu_item)

    def get_license_mgmt(self):
        return self.weh.get_element(self.license_mgmt)

    def get_global_settings_authentication_logs_slider(self):
        return self.weh.get_element(self.global_settings_authentication_logs_slider)

    def get_global_settings_accounting_logs_slider(self):
        return self.weh.get_element(self.global_settings_accounting_logs_slider)

    def get_radio_profile(self):
        return self.weh.get_element(self.common_objects_radio_profile)

    def get_subtab_common_object(self):
        return self.weh.get_element(self.subtab_common_object)

    def get_subtab_common_object_basic(self):
        return self.weh.get_element(self.subtab_common_object_basic)

    def get_device_actions_advanced_cli_ap_access(self):
        return self.weh.get_element(self.device_actions_advanced_cli_access)

    def get_device_actions_advanced_cli_router_access(self):
        return self.weh.get_element(self.device_actions_advanced_cli_router_access())

    def get_global_settings_audit_logs_slider(self):
        return self.weh.get_element(self.global_settings_audit_logs_slider)

    def get_copilot_tab(self):
        return self.weh.get_element(self.copilot_tab)

    def get_copilot_tab_img_class(self):
        return self.weh.get_element(self.copilot_tab_img).get_attribute('class')

    def get_copilot_anomaly_notification_icon(self):
        return self.weh.get_element(self.copilot_anomaly_notification_icon)

    def get_configure_users_subtab_users_side_nav_item(self):
        return self.weh.get_element(self.configure_users_subtab_users_side_nav_item)

    def get_common_object_policy_imago_tag_profile(self):
        return self.weh.get_element(self.common_object_policy_imago_tag_profile)

    def get_common_object_security_ip_firewall_policies(self):
        return self.weh.get_element(self.common_object_security_ip_firewall_policies)

    def get_common_object_policy_user_profiles(self):
        return self.weh.get_element(self.common_object_policy_user_profiles)

    def get_navigate_to_device_management_settings_menu(self):
        return self.weh.get_element(self.navigate_to_device_management_settings_menu)

    def get_common_object_network_management_options(self):
        return self.weh.get_element(self.common_object_network_management_options)

    def get_device_utilities_button(self):
        """
        :return: Utilities Button
        """
        return self.weh.get_element(self.utilities_button)

    def get_device_tools_menu_item(self):
        """
        :return: Tools Menu Item
        """
        return self.weh.get_element(self.tools_menu_item)

    def get_device_tools_client_information_menu_item(self):
        """
        :return: Tools > Client Information Menu Item
        """
        return self.weh.get_element(self.tools_client_information_menu_item)

    def get_device_tools_get_tech_menu_item(self):
        """
        :return: Tools > Get Tech Menu Item
        """
        return self.weh.get_element(self.tools_get_tech_menu_item)

    def get_device_tools_locate_device_menu_item(self):
        """
        :return: Tools > Locate Device Menu Item
        """
        return self.weh.get_element(self.tools_locate_device_menu_item)

    def get_device_tools_layer_neighbor_info_menu_item(self):
        """
        :return: Tools > Layer Neighbor Info Menu Item
        """
        return self.weh.get_element(self.tools_layer_neighbor_info_menu_item)

    def get_device_tools_packet_capture_menu_item(self):
        """
        :return: Tools > Packet Capture Menu Item
        """
        return self.weh.get_element(self.tools_packet_capture_menu_item)

    def get_device_tools_vlan_probe_menu_item(self):
        """
        :return: Tools > Packet Capture Menu Item
        """
        return self.weh.get_element(self.tools_vlan_probe_menu_item)

    def get_device_diagnostics_menu_item(self):
        """
        :return: Diagnostics Menu Item
        """
        return self.weh.get_element(self.diagnostics_menu_item)

    def get_device_diagnostics_show_ping_menu_item(self):
        """
        :return: Diagnostics > Show Ping Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_ping_menu_item)

    def get_device_diagnostics_show_log_menu_item(self):
        """
        :return: Diagnostics > Show Log Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_log_menu_item)

    def get_device_diagnostics_show_mac_table_menu_item(self):
        """
        :return: Diagnostics > Show MAC Table Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_mac_table_menu_item)

    def get_device_diagnostics_show_version_menu_item(self):
        """
        :return: Diagnostics > Show Version Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_version_menu_item)

    def get_device_diagnostics_show_running_config_menu_item(self):
        """
        :return: Diagnostics > Show Running Config Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_running_config_menu_item)

    def get_device_diagnostics_show_startup_config_menu_item(self):
        """
        :return: Diagnostics > Show Startup Config Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_startup_config_menu_item)

    def get_device_diagnostics_show_ip_routes_menu_item(self):
        """
        :return: Diagnostics > Show IP Routes Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_ip_routes_menu_item)

    def get_device_diagnostics_show_mac_routes_menu_item(self):
        """
        :return: Diagnostics > Show MAC Routes Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_mac_routes_menu_item)

    def get_device_diagnostics_show_arp_cache_menu_item(self):
        """
        :return: Diagnostics > Show ARP Cache Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_arp_cache_menu_item)

    def get_device_diagnostics_show_roaming_cache_menu_item(self):
        """
        :return: Diagnostics > Show Roaming Cache Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_roaming_cache_menu_item)

    def get_device_diagnostics_show_dnxp_neighbors_menu_item(self):
        """
        :return: Diagnostics > Show DNXP Neighbors Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_dnxp_neighbors_menu_item)

    def get_device_diagnostics_show_dnxp_cache_menu_item(self):
        """
        :return: Diagnostics > Show DNXP Cache Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_dnxp_cache_menu_item)

    def get_device_diagnostics_show_amrp_tunnel_menu_item(self):
        """
        :return: Diagnostics > Show AMRP Tunnel Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_amrp_tunnel_menu_item)

    def get_device_diagnostics_show_gre_tunnel_menu_item(self):
        """
        :return: Diagnostics > Show GRE Tunnel Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_gre_tunnel_menu_item)

    def get_device_diagnostics_show_ike_event_menu_item(self):
        """
        :return: Diagnostics > Show IKE Event Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_ike_event_menu_item)

    def get_device_diagnostics_show_ike_sa_menu_item(self):
        """
        :return: Diagnostics > Show IKE SA Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_ike_sa_menu_item)

    def get_device_diagnostics_show_ipsec_sa_menu_item(self):
        """
        :return: Diagnostics > Show IPSec SA Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_ipsec_sa_menu_item)

    def get_device_diagnostics_show_ipsec_tunnel_menu_item(self):
        """
        :return: Diagnostics > Show IPSec Tunnel Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_ipsec_tunnel_menu_item)

    def get_device_diagnostics_show_vpn_tunnel_menu_item(self):
        """
        :return: Diagnostics > Show VPN Tunnel Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_vpn_tunnel_menu_item)

    def get_device_diagnostics_show_cpu_menu_item(self):
        """
        :return: Diagnostics > Show CPU Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_cpu_menu_item)

    def get_device_diagnostics_show_memory_menu_item(self):
        """
        :return: Diagnostics > Show Memory Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_memory_menu_item)

    def get_device_diagnostics_show_pse_menu_item(self):
        """
        :return: Diagnostics > Show PSE Menu Item
        """
        return self.weh.get_element(self.diagnostics_show_pse_menu_item)

    def get_spectrum_intelligence_menu_item(self):
        return self.weh.get_element(self.spectrum_intelligence_menu_item)

    def get_reset_device_to_default_menu_item(self):
        return self.weh.get_element(self.reset_device_to_default_menu_item)

    def get_device_utilities_status_menu_item(self):
        return self.weh.get_element(self.device_utilities_status)

    def get_device_status_advanced_channel_selection_protocol_menu_item(self):
        return self.weh.get_element(self.utilities_status_adv_channel_sel)

    def get_device_status_interface_menu_item(self):
        return self.weh.get_element(self.utilities_status_interface)

    def get_locked_users_tab(self):
        return self.weh.get_element(self.locked_users_tab)

    def get_unbind_device_tab(self):
        return self.weh.get_element(self.unbind_device_tab)

    def get_client_monitor_diagnosis_tab(self):
        return self.weh.get_element(self.client_monitor_diagnosis_tab)

    def get_alert_sub_tab(self):
        return self.weh.get_element(self.configure_alert_nav)

    def get_applications_tab(self):
        return self.weh.get_element(self.applications_tab)

    def get_manage_summary_menu_item(self):
        return self.weh.get_element(self.manage_summary_menu_item)

    def get_manage_users_menu_item(self):
        return self.weh.get_element(self.manage_users_menu_item)

    def get_manage_events_menu_item(self):
        return self.weh.get_element(self.manage_events_menu_item)

    def get_manage_alerts_menu_item(self):
        return self.weh.get_element(self.manage_alerts_menu_item)

    def get_configure_guest_essentials_users_menu_item(self):
        return self.weh.get_element(self.configure_guest_essentials_users_menu_item)

    def get_main_side_nav_tab_order_number(self, tab_tag):
        els = self.weh.get_elements(self.main_side_nav_tabs)
        order_number = 0
        for el in els:
            if el.is_displayed():
                order_number += 1
            if str(tab_tag) in el.get_attribute("data-automation-tag"):
                return order_number
        return -1

    def get_side_nav_panel_1_menu_order_number(self, menu_item_tag):
        els = self.weh.get_elements(self.side_nav_panel_1_menu_items)
        order_number = 0
        for el in els:
            if el.is_displayed():
                order_number += 1
            if str(menu_item_tag) in el.get_attribute("data-automation-tag"):
                return order_number
        return -1

    def get_side_nav_panel_2_menu_order_number(self, menu_item_tag):
        els = self.weh.get_elements(self.side_nav_panel_2_menu_items)
        order_number = 0
        for el in els:
            if el.is_displayed():
                order_number += 1
            if str(menu_item_tag) in el.get_attribute("data-automation-tag"):
                return order_number
        return -1

    def get_vpn_management_tab(self):
        return self.weh.get_element(self.vpn_management_tab)

    def get_vpn_services_tab(self):
        return self.weh.get_element(self.vpn_services_tab)

    def get_clients_hyperlink(self):
        return self.weh.get_element(self.clients_hyperlink)

    def get_configure_button_d360(self):
        return self.weh.get_element(self.configure_button_d360)

    def get_port_configuration_d360(self):
        return self.weh.get_element(self.port_configuration_d360)

    def get_port_rows_d360(self):
        return self.weh.get_elements(self.port_rows_d360)

    def get_table_load_spinner(self):
        return self.weh.get_element(self.table_load_spinner)


    def get_page_size(self, page_size='100'):
        try:
            if els := self.weh.get_elements(self.page_size):
                for el in els:
                    if str(page_size) in el.text:
                        return el
            # Nothing was found
            return None
        except Exception:
            # An error occured
            return None

    def get_100_devices_per_page(self):
        return self.weh.get_element(self.no_100_devices_per_page)

    def get_unknown_tooltip_error(self):
        return self.weh.get_element(self.unknown_tooltip_error)

    def get_unknown_error_tooltip_close_icon(self):
        return self.weh.get_element(self.unknown_error_tooltip_close_icon)
    
    def get_grid_loading_wheel(self):
        return self.weh.get_elements(self.grid_loading_wheel)

    def get_grid_spinner(self):
        return self.weh.get_elements(self.grid_spinner)

    def get_tools_page(self):
        return self.weh.get_element(self.tools_page)

    def get_grid_loading_mark(self):
        return self.weh.get_elements(self.grid_loading_mark)
