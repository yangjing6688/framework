from extauto.xiq.defs.DeviceConfigDefs import DeviceConfigDefs
from extauto.common.WebElementHandler import WebElementHandler


class DeviceConfigElements(DeviceConfigDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_interface_settings_tab(self):
        return self.weh.get_element(self.interface_settings_tab)

    def get_interface_settings_tab_single_device(self):
        return self.weh.get_element(self.interface_settings_tab_single_device)

    def get_wireless_interface_toggle(self):
        attr = self.weh.get_element(self.wireless_interface_toggle).get_attribute('class')
        if "header-toggle-caret" not in attr:
            return self.weh.get_element(self.wireless_interface_toggle)

    def get_wifi0_interface_tab(self):
        return self.weh.get_element(self.wifi0_interface_tab)

    def get_wifi1_interface_tab(self):
        return self.weh.get_element(self.wifi1_interface_tab)

    def get_wifi2_interface_tab(self):
        return self.weh.get_element(self.wifi2_interface_tab)

    def get_override_client_mode_wifi0_checked(self):
        return self.weh.get_element(self.override_client_mode_wifi0_checked)

    def get_override_client_mode_wifi1_checked(self):
        return self.weh.get_element(self.override_client_mode_wifi1_checked)

    def get_override_client_access_wifi0_checked(self):
        return self.weh.get_element(self.override_client_access_wifi0_checked)

    def get_override_client_access_wifi1_checked(self):
        return self.weh.get_element(self.override_client_access_wifi1_checked)

    def get_override_add_client_mode_wifi0_profile(self):
        return self.weh.get_element(self.override_add_client_mode_wifi0_profile)

    def get_override_add_client_mode_wifi1_profile(self):
        return self.weh.get_element(self.override_add_client_mode_wifi1_profile)

    def get_override_wifi0_1_client_mode_profile_name(self):
        return self.weh.get_element(self.override_wifi0_1_client_mode_profile_name)

    def get_override_wifi0_1_cm_local_web_page_checkbox(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_page_checkbox)

    def get_override_wifi0_1_cm_local_web_page_add(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_page_add)

    def get_override_wifi0_1_cm_local_web_page_ssid_textbox(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_page_ssid_textbox)

    def get_override_wifi0_1_cm_local_web_page_password_textbox(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_page_password_textbox)

    def get_override_wifi0_1_cm_local_web_page_auth_dropdown(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_page_auth_dropdown)

    def get_override_wifi0_1_cm_local_web_page_auth_dropdown_option(self):
        return self.weh.get_elements(self.override_wifi0_1_cm_local_web_page_auth_dropdown_option)

    def get_override_wifi0_1_cm_local_web_key_type_dropdown(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_key_type_dropdown)

    def get_override_wifi0_1_cm_local_web_key_type_dropdown_option(self):
        return self.weh.get_elements(self.override_wifi0_1_cm_local_web_key_type_dropdown_option)

    def get_override_wifi0_1_cm_local_web_page_add_button(self):
        return self.weh.get_element(self.override_wifi0_1_cm_local_web_page_add_button)

    def get_override_wifi0_1_client_mode_profile_dhcp_server_scope(self):
        return self.weh.get_element(self.override_wifi0_1_client_mode_profile_dhcp_server_scope)

    def get_override_wifi0_1_client_mode_profile_save(self):
        return self.weh.get_element(self.override_wifi0_1_client_mode_profile_save)

    def get_override_wifi0_ssid_broadcast_ssid_field(self):
        return self.weh.get_element(self.override_wifi0_ssid_broadcast_ssid_field)

    def get_override_wifi0_psk_password(self):
        return self.weh.get_element(self.override_wifi0_psk_password)

    def get_interface_settings_save_button(self):
        return self.weh.get_element(self.interface_settings_save_button)

    def get_configuration_tab(self):
        return self.weh.get_element(self.configuration_tab)

    def get_device_configuration_tab(self):
        return self.weh.get_element(self.device_configuration_tab)

    def get_device_configuration_dhcp_checkbox(self):
        return self.weh.get_element(self.device_configuration_dhcp_checkbox)

    def get_close_device360_dialog_window(self):
        return self.weh.get_element(self.close_device360_dialog_window)

    def get_wireless_interface_wifi0_channel_drop_down(self):
        return self.weh.get_element(self.wireless_interface_wifi0_channel_drop_down)

    def get_wireless_interface_wifi0_channel_options(self):
        return self.weh.get_elements(self.wireless_interface_wifi0_channel_options)

    def get_wireless_interface_wifi1_channel_drop_down(self):
        return self.weh.get_element(self.wireless_interface_wifi1_channel_drop_down)

    def get_wireless_interface_wifi1_channel_options(self):
        return self.weh.get_elements(self.wireless_interface_wifi1_channel_options)

    def get_wireless_wifi0_radio_profile_drop_down(self):
        return self.weh.get_element(self.wireless_wifi0_radio_profile_drop_down)

    def get_wireless_wifi0_radio_profile_options(self):
        return self.weh.get_elements(self.wireless_wifi0_radio_profile_options)

    def get_wireless_wifi1_radio_profile_drop_down(self):
        return self.weh.get_element(self.wireless_wifi1_radio_profile_drop_down)

    def get_wireless_wifi1_radio_profile_options(self):
        return self.weh.get_elements(self.wireless_wifi2_radio_profile_options)

    def get_manage_devices_select_all_devices_checkbox(self):
        return self.weh.get_element(self.manage_devices_select_all_devices_checkbox)

    def get_manage_devices_edit_interface_settings_tab(self):
        return self.weh.get_element(self.manage_devices_edit_interface_settings_tab)

    def get_manage_devices_edit_wireless_interface_link(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_link)

    def get_manage_devices_edit_wireless_interface_wifi0_tab(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi0_tab)

    def get_manage_devices_edit_wireless_interface_wifi1_tab(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi1_tab)

    def get_manage_devices_edit_wireless_interface_wifi0_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi0_button)

    def get_manage_devices_edit_wireless_interface_wifi0_on_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi0_on_button)

    def get_manage_devices_edit_wireless_interface_wifi0_off_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi0_off_button)

    def get_manage_devices_edit_wireless_interface_wifi1_on_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi1_on_button)

    def get_manage_devices_edit_wireless_interface_wifi1_off_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_wifi1_off_button)

    def get_wireless_interface_wifi0_transmission_mode_auto(self):
        return self.weh.get_element(self.wireless_interface_wifi0_transmission_mode_auto)

    def get_wireless_interface_wifi0_transmission_mode_manual(self):
        return self.weh.get_element(self.wireless_interface_wifi0_transmission_mode_manual)

    def get_wireless_interface_wifi1_transmission_mode_auto(self):
        return self.weh.get_element(self.wireless_interface_wifi1_transmission_mode_auto)

    def get_wireless_interface_wifi1_transmission_mode_manual(self):
        return self.weh.get_element(self.wireless_interface_wifi1_transmission_mode_manual)

    def get_manage_devices_edit_wireless_interface_save_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_save_button)

    def get_wifi1_transmission_power_slider_button(self):
        return self.weh.get_element(self.wifi1_transmission_power_slider_button)

    def get_wifi1_transmission_power_value_text(self):
        return self.weh.get_element(self.wifi1_transmission_power_value_text)

    def get_wifi0_transmission_power_value_text(self):
        return self.weh.get_element(self.wifi0_transmission_power_value_text)

    def get_wifi0_transmission_power_slider_button(self):
        return self.weh.get_element(self.wifi0_transmission_power_slider_button)

    def get_manage_devices_edit_wireless_interface_cancel_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_cancel_button)

    def get_device_override_configure_button(self):
        return self.weh.get_element(self.device_override_configure_button)

    def get_device_override_monitor_button(self):
        return self.weh.get_element(self.device_override_monitor_button)

    def get_device_override_configure_device_configuration_button(self):
        return self.weh.get_element(self.device_override_configure_device_configuration_button)

    def get_device_override_configure_exos_device_configuration_button(self):
        return self.weh.get_element(self.device_override_configure_exos_device_configuration_button)

    def get_device_override_configure_host_name(self):
        return self.weh.get_element(self.device_override_configure_host_name)

    def get_device_override_save_device_configuration(self):
        return self.weh.get_element(self.device_override_save_device_configuration)

    def get_device_override_exos_save_device_configuration(self):
        return self.weh.get_element(self.device_override_exos_save_device_configuration)

    def get_device_override_configure_interface_settings_button(self):
        return self.weh.get_element(self.device_override_configure_interface_settings_button)

    def get_device_override_configure_interface_settings_wifi0_tab(self):
        return self.weh.get_element(self.device_override_configure_interface_settings_wifi0_tab)

    def get_device_override_configure_interface_settings_wifi1_tab(self):
        return self.weh.get_element(self.device_override_configure_interface_settings_wifi1_tab)

    def get_device_override_configure_interface_settings_wifi0_radio_status(self):
        return self.weh.get_element(self.device_override_configure_interface_settings_wifi0_radio_status)

    def get_device_override_configure_interface_settings_wifi1_radio_status(self):
        return self.weh.get_element(self.device_override_configure_interface_settings_wifi1_radio_status)

    def get_device_override_configure_wireless_interface_link(self):
        return self.weh.get_element(self.device_override_configure_wireless_interface_link)

    def get_edit_button(self):
        return self.weh.get_element(self.device_edit_button)

    def get_close_dialog(self):
        return self.weh.get_element(self.close_dialog)

    def get_device_edit_wifi0_operating_mode_area(self):
        return self.weh.get_element(self.device_edit_wifi0_operating_mode_area)

    def get_device_edit_wifi0_operating_mode_drop_down(self):
        return self.weh.get_element(self.device_edit_wifi0_operating_mode_drop_down)

    def get_device_edit_wifi0_operating_mode_drop_down_options(self):
        return self.weh.get_element(self.device_edit_wifi0_operating_mode_drop_down_options)

    def get_device_edit_template_drop_down_options(self):
        return self.weh.get_elements(self.device_edit_template_drop_down_options)

    def get_device_edit_template_drop_down(self):
        return self.weh.get_element(self.device_edit_template_drop_down)

    def get_device_edit_template_text(self):
        return self.weh.get_element(self.device_edit_template_text)

    def get_devices_edit_config_button(self):
        return self.weh.get_element(self.devices_edit_config_button)

    def get_manage_devices_edit_wireless_interface_close_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_close_button)

    def get_device_supplemental_cli_drop_down(self):
        return self.weh.get_element(self.device_supplemental_cli_drop_down)

    def get_device_select_supplemental_cli_drop_down_options(self):
        return self.weh.get_elements(self.device_select_supplemental_cli_drop_down_options)

    def get_device_config_supplemental_cli_add_button(self):
        return self.weh.get_element(self.device_config_supplemental_cli_add_button)

    def get_device_config_supplemental_cli_enter_name(self):
        return self.weh.get_element(self.device_supplemental_cli_config_enter_name)

    def get_device_config_supplemental_cli_enter_commands(self):
        return self.weh.get_element(self.device_supplemental_cli_enter_commands)

    def get_device_config_supplemental_cli_save_button(self):
        return self.weh.get_element(self.device_supplemental_cli_save_button)

    def get_device_config_audit_view(self):
        return self.weh.get_element(self.device_open_config_audit_view)

    def get_devices_config_audit_view_button(self, row):
        return self.weh.get_element(self.devices_config_audit_view_button, parent=row)

    def get_config_audit_delta_view_button(self, row):
        return self.weh.get_element(self.config_audit_delta_view_button, parent=row)

    def get_device_config_audit_audit_view(self):
        return self.weh.get_element(self.device_config_audit_audit_view)

    def get_device_config_audit_delta_view(self):
        return self.weh.get_element(self.device_config_audit_delta_view)

    def get_device_config_audit_audit_view_content(self):
        return self.weh.get_element(self.device_config_audit_audit_view_content)

    def get_device_config_audit_delta_view_content(self):
        return self.weh.get_element(self.device_config_audit_delta_view_content)

    def get_device_config_audit_complete_view(self):
        return self.weh.get_element(self.device_config_audit_complete_view)

    def get_device_config_audit_complete_view_content(self):
        return self.weh.get_element(self.device_config_audit_complete_view_content)

    def get_device_config_audit_view_close_button(self):
        return self.weh.get_element(self.device_config_audit_view_close_button)

    def get_common_obj_basic_supplemental_cli_tab(self):
        return self.weh.get_element(self.common_obj_basic_supplemental_cli_tab)

    def get_supplemental_cli_select_rows(self):
        return self.weh.get_elements(self.select_supplemental_cli_object_rows)

    def get_supplemental_cli_select_checkbox(self, row):
        return self.weh.get_element(self.select_supplemental_cli_checkbox, parent=row)

    def get_supplemental_cli_delete_button(self):
        return self.weh.get_element(self.supplemental_cli_delete_button)

    def get_supplemental_cli_delete_confirm_button(self):
        return self.weh.get_element(self.supplemental_cli_delete_confirm_button)

    def get_device_events_select_severity(self):
        return self.weh.get_element(self.device_events_select_severity)

    def get_severity_dropdown_options(self):
        return self.weh.get_elements(self.severity_dropdown_options)

    def get_device_config_wireless_interfaces_wifi2_tab(self):
        return self.weh.get_element(self.device_config_wireless_interfaces_wifi2_tab)

    def get_device_config_wireless_interfaces_wifi2_status_radio_button(self):
        return self.weh.get_element(self.device_config_wireless_interfaces_wifi2_status_radio_button)

    def get_device_config_wireless_interfaces_wifi2_primary_server_textfield(self):
        return self.weh.get_element(self.device_config_wireless_interfaces_wifi2_primary_server_textfield)

    def get_device_config_wireless_interfaces_wifi2_primary_server_port_textfield(self):
        return self.weh.get_element(self.device_config_wireless_interfaces_wifi2_primary_server_port_textfield)

    def get_device_config_wireless_interfaces_wifi2_secondary_server_textfield(self):
        return self.weh.get_element(self.device_config_wireless_interfaces_wifi2_secondary_server_textfield)

    def get_device_config_wireless_interfaces_wifi2_secondary_server_port_textfield(self):
        return self.weh.get_element(self.device_config_wireless_interfaces_wifi2_secondary_server_port_textfield)

    def get_manage_device_edit_wireless_interface_cancel_button(self):
        return self.weh.get_element(self.manage_device_edit_wireless_interface_cancel_button)

    def get_manage_device_edit_wireless_interface_save_button(self):
        return self.weh.get_element(self.manage_device_edit_wireless_interface_save_button)

    def get_manage_device_interface_settings_save_button_disabled(self):
        return self.weh.get_element(self.manage_device_interface_settings_save_button_disabled)

    def get_wireless_wifi2_channel_list(self, channel):
        item1 = {}
        item1['XPATH'] = self.wireless_wifi2_channel_list['XPATH'] + channel + '"]'
        item1['wait_for'] = 3
        return item1

    def get_wireless_wifi2_radio_status(self):
        return self.weh.get_element(self.wireless_wifi2_radio_status)

    def get_wireless_interface_wifi2_transmission_mode_auto(self):
        return self.weh.get_element(self.wireless_interface_wifi2_transmission_mode_auto)

    def get_wireless_interface_wifi2_transmission_mode_manual(self):
        return self.weh.get_element(self.wireless_interface_wifi2_transmission_mode_manual)

    def get_wifi2_transmission_power_slider_button(self):
        return self.weh.get_element(self.wifi2_transmission_power_slider_button)

    def get_wifi2_transmission_power_textfield_input(self):
        return self.weh.get_element(self.wifi2_transmission_power_textfield_input)

    def get_wifi2_transmission_power_textfield(self):
        return self.weh.get_element(self.wifi2_transmission_power_textfield)

    def get_interface_settings_update_button(self):
        return self.weh.get_element(self.interface_settings_update_button)

    def get_interface_settings_perform_update_button(self):
        return self.weh.get_element(self.interface_settings_perform_update_button)

    def get_total_unique_clients(self):
        return self.weh.get_element(self.total_unique_clients)

    def get_go_to_clients(self):
        return self.weh.get_element(self.go_to_clients)

    def get_total_client_count(self):
        return self.weh.get_element(self.total_client_count)

    def get_poor_client_count(self):
        return self.weh.get_element(self.poor_client_count)

    def get_unique_clients_search_field(self):
        return self.weh.get_element(self.unique_clients_search_field)

    def get_client_connection_type(self):
        return self.weh.get_element(self.client_connection_type)

    def get_client_os_type(self):
        return self.weh.get_element(self.client_os_type)

    def get_client_connection_status(self):
        return self.weh.get_element(self.client_connection_status)

    def get_client_health_status(self):
        return self.weh.get_element(self.client_health_status)

    def get_client_hostname(self):
        return self.weh.get_element(self.client_hostname)

    def get_client_mac(self):
        return self.weh.get_element(self.client_mac)

    def get_client_IPv4(self):
        return self.weh.get_element(self.client_IPv4)

    def get_client_IPv6(self):
        return self.weh.get_element(self.client_IPv6)

    def get_client_user_name(self):
        return self.weh.get_element(self.client_user_name)

    def get_client_vlan(self):
        return self.weh.get_element(self.client_vlan)

    def get_client_connected_via(self):
        return self.weh.get_element(self.client_connected_via)

    def get_client_rssi(self):
        return self.weh.get_element(self.client_rssi)

    def get_client_snr(self):
        return self.weh.get_element(self.client_snr)

    def get_wireless_wifi_device_model(self):
        return self.weh.get_element(self.wireless_wifi_device_model)

    def get_wireless_wifi_device_template(self):
        return self.weh.get_element(self.wireless_wifi_device_template)

    def get_device_override_configure_interface_settings_wifi2_radio_status(self):
        return self.weh.get_element(self.device_override_configure_interface_settings_wifi2_radio_status)

    def get_wireless_wifi2_radio_mode(self):
        return self.weh.get_element(self.wireless_wifi2_radio_mode);

    def get_wireless_wifi1_radio_mode(self):
        return self.weh.get_element(self.wireless_wifi1_radio_mode);

    def get_wireless_wifi0_radio_mode(self):
        return self.weh.get_element(self.wireless_wifi0_radio_mode);

    def get_default_wireless_wifi2_radio_profile_drop_down(self):
        return self.weh.get_element(self.wireless_wifi2_default_radio_profile_drop_down)

    def get_default_wireless_wifi1_radio_profile_drop_down(self):
        return self.weh.get_element(self.wireless_wifi1_default_radio_profile_drop_down)

    def get_default_wireless_wifi0_radio_profile_drop_down(self):
        return self.weh.get_element(self.wireless_wifi0_default_radio_profile_drop_down)

    def get_wireless_wifi2_radio_usage_client_access_checkbox(self):
        return self.weh.get_element(self.wireless_wifi2_radio_usage_client_access_checkbox)

    def get_wireless_wifi1_radio_usage_client_access_checkbox(self):
        return self.weh.get_element(self.wireless_wifi1_radio_usage_client_access_checkbox)

    def get_wireless_wifi0_radio_usage_client_access_checkbox(self):
        return self.weh.get_element(self.wireless_wifi0_radio_usage_client_access_checkbox)

    def get_wireless_wifi2_radio_usage_blackhaul_mesh_link_checkbox(self):
        return self.weh.get_element(self.wireless_wifi2_radio_usage_blackhaul_mesh_link_checkbox)

    def get_wireless_wifi1_radio_usage_blackhaul_mesh_link_checkbox(self):
        return self.weh.get_element(self.wireless_wifi1_radio_usage_blackhaul_mesh_link_checkbox)

    def get_wireless_wifi0_radio_usage_blackhaul_mesh_link_checkbox(self):
        return self.weh.get_element(self.wireless_wifi0_radio_usage_blackhaul_mesh_link_checkbox)

    def get_wireless_wifi2_radio_usage_sensor_checkbox(self):
        return self.weh.get_element(self.wireless_wifi2_radio_usage_sensor_checkbox)

    def get_wireless_wifi2_channel_dropdown(self):
        return self.weh.get_element(self.wireless_wifi2_channel_dropdown)

    def get_wireless_wifi1_channel_dropdown(self):
        return self.weh.get_element(self.wireless_wifi1_channel_dropdown)

    def get_wireless_wifi0_channel_dropdown(self):
        return self.weh.get_element(self.wireless_wifi0_channel_dropdown)


    def get_wireless_wifi2_override_channel_exclusion_setting_radio_profile_checkbox(self):
        return self.weh.get_element(self.wireless_wifi2_override_channel_exclusion_setting_radio_profile_checkbox)

    def get_wireless_wifi1_override_channel_exclusion_setting_radio_profile_checkbox(self):
        return self.weh.get_element(self.wireless_wifi1_override_channel_exclusion_setting_radio_profile_checkbox)

    def get_wireless_wifi0_override_channel_exclusion_setting_radio_profile_checkbox(self):
        return self.weh.get_element(self.wireless_wifi0_override_channel_exclusion_setting_radio_profile_checkbox)


    def get_wireless_wifi2_channel_width_text(self):
        return self.weh.get_element(self.wireless_wifi2_channel_width_text)

    def get_wireless_wifi1_channel_width_text(self):
        return self.weh.get_element(self.wireless_wifi1_channel_width_text)

    def get_wireless_wifi0_channel_width_text(self):
        return self.weh.get_element(self.wireless_wifi0_channel_width_text)


    def get_manage_devices_edit_wireless_interface_save2_button(self):
        return self.weh.get_element(self.manage_devices_edit_wireless_interface_save_button2)


    def get_wireless_wifi2_override_channel_exclusion_setting_radio_profile_label(self):
        return self.weh.get_element(self.wireless_wifi2_override_channel_exclusion_setting_radio_profile_label)

    def get_wireless_wifi1_override_channel_exclusion_setting_radio_profile_label(self):
        return self.weh.get_element(self.wireless_wifi1_override_channel_exclusion_setting_radio_profile_label)

    def get_wireless_wifi0_override_channel_exclusion_setting_radio_profile_label(self):
        return self.weh.get_element(self.wireless_wifi0_override_channel_exclusion_setting_radio_profile_label)


    def get_wireless_wifi2_icon (self):
        return self.weh.get_element(self.wireless_wifi2_icon)


    def get_select_wireless_wifi2_radio_profile(self, profile):
        item = {}
        item['XPATH'] = self.wireless_wifi2_radio_profile_list['XPATH'] + profile + '"]'
        item['wait_for'] = 3

        return item

    def get_select_wireless_wifi1_radio_profile(self, profile):
        item = {}
        item['XPATH'] = self.wireless_wifi1_radio_profile_list['XPATH'] + profile + '"]'
        item['wait_for'] = 3

        return item

    def get_select_wireless_wifi0_radio_profile(self, profile):
        item = {}
        item['XPATH'] = self.wireless_wifi0_radio_profile_list['XPATH'] + profile + '"]'
        item['wait_for'] = 3

        return item

    def get_dialog_box_selected_radio_profile_yes_button (self):
        return self.weh.get_element(self.dialog_box_selected_radio_profile_yes_button)

    def get_dialog_box_selected_radio_profile_no_button (self):
        return self.weh.get_element(self.dialog_box_selected_radio_profile_no_button)

    def get_interface_settings_wifi2_80MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi2_80MHz_channel)

    def get_interface_settings_wifi2_20MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi2_20MHz_channel)

    def get_interface_settings_wifi2_160MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi2_160MHz_channel)

    def get_interface_settings_wifi2_40MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi2_40MHz_channel)

    def get_interface_settings_wifi1_80MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi1_80MHz_channel)

    def get_interface_settings_wifi1_20MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi1_20MHz_channel)

    def get_interface_settings_wifi1_160MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi1_160MHz_channel)

    def get_interface_settings_wifi1_40MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi1_40MHz_channel)

    def get_interface_settings_wifi0_80MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi0_80MHz_channel)

    def get_interface_settings_wifi0_20MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi0_20MHz_channel)

    def get_interface_settings_wifi0_160MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi0_160MHz_channel)

    def get_interface_settings_wifi0_40MHz_channel (self):
        return self.weh.get_element(self.interface_settings_wifi0_40MHz_channel)

    def get_devices_override_channel_exclusion_setting_wifi2(self, channel):
        item = {}
        item['XPATH'] = self.devices_override_channel_exclusion_setting_wifi2['XPATH'] + channel + '"]'
        item['wait_for'] = 3
        return item

    def get_devices_override_channel_exclusion_setting_wifi1(self, channel):
        item = {}
        item['XPATH'] = self.devices_override_channel_exclusion_setting_wifi1['XPATH'] + channel + '"]'
        item['wait_for'] = 3
        return item

    def get_devices_override_channel_exclusion_setting_wifi0(self, channel):
        item = {}
        item['XPATH'] = self.devices_override_channel_exclusion_setting_wifi0['XPATH'] + channel + '"]'
        item['wait_for'] = 3
        return item

    def get_wired_interface_toggle(self):
        attr = self.weh.get_element(self.wired_interface_toggle).get_attribute('class')
        if "header-toggle-caret" not in attr:
            return self.weh.get_element(self.wired_interface_toggle)

    def get_imago_tag_radio_button(self):
        return self.weh.get_element(self.imago_tag_radio_button)

    def get_imago_tag_add_profile_add_button(self):
        return self.weh.get_element(self.imago_tag_add_profile_add_button)

    def get_wired_client_connection_type(self):
        return self.weh.get_element(self.wired_client_connection_type)

    def get_wired_client_os_type(self):
        return self.weh.get_element(self.wired_client_os_type)

    def get_wired_client_connection_status(self):
        return self.weh.get_element(self.wired_client_connection_status)

    def get_wired_client_hostname(self):
        return self.weh.get_element(self.wired_client_hostname)

    def get_wired_client_mac(self):
        return self.weh.get_element(self.wired_client_mac)

    def get_wired_client_IPv4(self):
        return self.weh.get_element(self.wired_client_IPv4)

    def get_wired_client_IPv6(self):
        return self.weh.get_element(self.wired_client_IPv6)

    def get_wired_client_user_name(self):
        return self.weh.get_element(self.wired_client_user_name)

    def get_wired_client_vlan(self):
        return self.weh.get_element(self.wired_client_vlan)

    def get_wired_client_connected_via(self):
        return self.weh.get_element(self.wired_client_connected_via)

    def get_wired_client_popup_mac(self):
        return self.weh.get_element(self.wired_client_popup_mac)

    def get_wired_client_popup_IPv4(self):
        return self.weh.get_element(self.wired_client_popup_ipv4)

    def get_wired_client_popup_portSpeed(self):
        return self.weh.get_element(self.wired_client_popup_portSpeed)

    def get_wired_client_popup_negotiatedspeed(self):
        return self.weh.get_element(self.wired_client_popup_negotiatedspeed)

    def get_wired_client_popup_portMode(self):
        return self.weh.get_element(self.wired_client_popup_portMode)

    def get_wired_client_popup_vlan(self):
        return self.weh.get_element(self.wired_client_popup_vlan)

    def get_wired_client_popup_portNumber(self):
        return self.weh.get_element(self.wired_client_popup_portNumber)

    def get_client360_page_confirmation(self):
        return self.weh.get_element(self.wired_client_popup_confirmation)

    def get_close_D360_popup(self):
        return self.weh.get_element(self.close_D360_popup)

    def get_grid_rows(self):
        """
        :return: all the rows in the devices grid
        """
        grid_rows = self.weh.get_elements(self.devices_page_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False
