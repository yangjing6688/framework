from extauto.xiq.defs.CommonObjectsWebElementsDefinitions import *
from extauto.common.WebElementHandler import *


class CommonObjectsWebElements(CommonObjectsWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_dislayed_element(self, elements):
        for el in elements:
            if el.is_displayed():
                return el

    def get_common_object_policy_tab(self):
        """
        :return: Get Common Objects --> Policy Tab
        """
        return self.weh.get_element(self.common_object_policy_slider_button)

    def get_common_object_policy_ssid_tab(self):
        """
        :return: Get Common Objects --> Policy---> SSIDs Tab
        """
        return self.weh.get_element(self.common_object_policy_manage_ssid)

    def get_common_object_authentication_tab(self):
        """
        :return: Get Common Objects --> Authentication Tab
        """
        return self.weh.get_element(self.common_object_authentication_slider_button)

    def get_common_object_authentication_captive_portal_tab(self):
        """
        :return: Get Common Objects --> Authentication---> Captive Web Portal Tab
        """
        return self.weh.get_element(self.common_object_authentication_captive_portal)

    def get_authentication_external_radius_server_tab(self):
        return self.weh.get_element(self.authentication_external_radius_server_tab)

    def get_basic_tab(self):
        return self.weh.get_element(self.basic_slider_button)

    def get_ip_object_host_name_button(self):
        return self.weh.get_element(self.ip_object_host_name_button)

    def get_common_object_grid_rows(self):
        return self.weh.get_elements(self.common_object_grid_rows)

    def get_common_object_grid_row_cells(self, row, field='field-name'):
        cells = self.weh.get_elements(self.common_object_grid_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_common_object_edit_button(self):
        """

        :return: common object edit button
        """
        elements = self.weh.get_elements(self.common_object_edit_button)
        return self.get_dislayed_element(elements)

    def get_common_objects_delete_button(self):
        elements = self.weh.get_elements(self.common_object_delete_button)
        return self.get_dislayed_element(elements)

    def get_common_object_confirm_delete_button(self):
        # return self.weh.get_element(self.common_object_confirm_delete_button)
        elements = self.weh.get_elements(self.common_object_confirm_delete_button)
        return self.get_dislayed_element(elements)

    def get_cwp_self_reg_employee_approval_button(self):
        return self.weh.get_element(self.cwp_self_reg_employee_approval_button)

    def get_cwp_save_button(self):
        elements = self.weh.get_elements(self.cwp_save_button)
        return self.get_dislayed_element(elements)

    def get_paze_size_element(self, page_size='50'):
        if els := self.weh.get_elements(self.page_size_element):
            for el in els:
                if str(page_size) in el.text:
                    return el

    def get_next_page_element(self, page_size='50'):
        return self.weh.get_elements(self.next_page_element)

    def get_common_object_authentication_aaa_server_settings(self):
        """
        :return: Get Common Objects --> Authentication---> AAA server Profile Settings
        """
        return self.weh.get_element(self.common_object_authentication_aaa_server_settings)

    def get_common_object_policy_port_types_tab(self):
        """
        :return: Get Common Objects --> Policy---> SSIDs Tab
        """
        return self.weh.get_element(self.common_object_policy_manage_port_types)

    def get_common_object_policy_port_types_view_all_pages(self):
        """
        :return: get_common_object_policy_port_types_view_all_pages
        """
        return self.weh.get_element(self.common_object_policy_port_types_view_all_pages)

    def get_common_object_network_subnetwork_space_tab(self):
        """
        :return: Get Common Objects --> network-->Subnetwork Space
        """
        return self.weh.get_element(self.common_object_network_subnetwork_space_tab)

    def get_common_object_network_tab(self):
        """
        :return: Get Common Objects --> network
        """
        return self.weh.get_element(self.common_object_network_tab)

    def get_common_object_basic_tab(self):
        """
        :return: Get Common Objects --> Basic tab
        """
        return self.weh.get_element(self.common_object_basic_tab)

    def get_common_object_basic_vlan_tab(self):
        """
        :return: Get Common Objects --> Basic --> Vlans
        """
        return self.weh.get_element(self.common_object_basic_vlan_tab)

    def get_common_object_security_tab(self):
        """
        :return: Get Common Objects --> Security tab
        """
        return self.weh.get_element(self.common_object_security_tab)

    def get_common_object_security_wips_policies_tab(self):
        """
        :return: Get Common Objects --> Security --> Policies
        """
        return self.weh.get_element(self.common_object_security_wips_policies_tab)

    def get_common_object_policy_ap_template_tab(self):
        """
        :return: Get Common Objects --> Policy---> AP Templates
        """
        return self.weh.get_element(self.common_object_policy_ap_template_tab)

    def get_common_object_template_grid_row_cells(self, row, field='dgrid-column-2 field-tmpl'):
        cells = self.weh.get_elements(self.common_object_grid_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_common_object_policy_ap_templates_view_all_pages(self):
        """
        :return: get_common_object_policy_ap_templates_view_all_pages
        """
        return self.weh.get_element(self.common_object_policy_ap_templates_view_all_pages)

    def get_common_objects_edit_button(self):
        elements = self.weh.get_elements(self.common_object_edit_button)
        return self.get_dislayed_element(elements)

    def get_common_object_policy_add_ssid_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.common_object_policy_add_ssid_button)

    def get_common_object_policy_clone_ssid_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.common_object_policy_clone_ssid_button)

    def get_common_object_policy_clone_ssid_saveas_textfield(self):
        """
        :return:
        """
        return self.weh.get_element(self.common_object_policy_clone_ssid_saveas_textfield)

    def get_common_object_policy_ssid_clone_save_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.common_object_policy_ssid_clone_save_button)

    def get_common_object_add_button_radio_profile(self):
        """
        :return:
        """
        return self.weh.get_element(self.common_object_radio_profile_add_button)

    def get_common_object_radio_profile_name(self):
        return self.weh.get_element(self.common_object_radio_profile_name)

    def get_common_object_radio_profile_mode(self):
        return self.weh.get_element(self.common_object_radio_profile_mode)

    def get_common_object_radio_profile_select_mode(self):
        return self.weh.get_elements(self.common_object_radio_profile_select_mode)

    def get_common_object_radio_profile_enable_dfs(self):
        return self.weh.get_element(self.common_object_radio_profile_enable_dfs)

    def get_common_object_radio_profile_exclude_channel(self):
        return self.weh.get_element(self.common_object_radio_profile_exclude_channels)

    def get_common_object_radio_profile_bg_scan(self):
        return self.weh.get_element(self.common_object_radio_bg_scan)

    def get_common_object_radio_profile_save(self):
        return self.weh.get_element(self.common_object_radio_profile_save)

    def get_common_object_radio_profile_exclude_ch_u_1(self):
        return self.weh.get_element(self.common_object_radio_exclude_ch_u_1)

    def get_common_object_radio_profile_exclude_ch_u_2(self):
        return self.weh.get_element(self.common_object_radio_exclude_ch_u_2)

    def get_common_object_radio_profile_exclude_ch_u_2e(self):
        return self.weh.get_element(self.common_object_radio_exclude_ch_u_2e)

    def get_common_object_radio_profile_exclude_ch_u_3(self):
        return self.weh.get_element(self.common_object_radio_exclude_ch_u_3)
      
    def get_common_object_add_ap_template_button(self):
        return self.weh.get_element(self.common_object_add_ap_template_button)

    def get_common_object_matched_ap_model_dropdown(self):
        return self.weh.get_elements(self.common_object_matched_ap_model_dropdown)

    def get_common_object_add_ap_template_name(self):
        return self.weh.get_element(self.common_object_add_ap_template_name)

    def get_common_object_ap_template_wifi0_tab(self):
        """
        :return: get_device_template_ap_template_wifi1_tab
        """
        wifi0_tabs = self.weh.get_elements(self.common_object_ap_template_wifi_tab)
        for wifi0_tab in wifi0_tabs:
            if wifi0_tab.text == "WiFi0":
                return wifi0_tab

    def get_common_object_ap_template_wifi1_tab(self):
        """
        :return: get_device_template_ap_template_wifi1_tab
        """
        wifi1_tabs = self.weh.get_elements(self.common_object_ap_template_wifi_tab)
        for wifi1_tab in wifi1_tabs:
            if wifi1_tab.text == "WiFi1":
                return wifi1_tab

    def get_common_object_ap_template_wifi2_tab(self):
        """
        :return: get_device_template_ap_template_wifi2_tab
        """
        wifi2_tabs = self.weh.get_elements(self.common_object_ap_template_wifi_tab)
        for wifi2_tab in wifi2_tabs:
            if wifi2_tab.text == "WiFi2":
                return wifi2_tab

    def get_common_object_wifi0_radio_status_button(self):
        return self.weh.get_element(self.common_object_wifi0_radio_status_button)

    def get_common_object_wifi1_radio_status_button(self):
        return self.weh.get_element(self.common_object_wifi1_radio_status_button)

    def get_common_object_wifi2_radio_status_button(self):
        return self.weh.get_element(self.common_object_wifi1_radio_status_button)

    def get_common_object_wifi0_radio_profile_button(self):
        return self.weh.get_element(self.common_object_wifi0_radio_profile_button)

    def get_common_object_wifi1_radio_profile_button(self):
        return self.weh.get_element(self.common_object_wifi1_radio_profile_button)

    def get_common_object_wifi0_radio_profile_dropdown(self):
        return self.weh.get_elements(self.common_object_wifi0_radio_profile_dropdown)

    def get_common_object_wifi1_radio_profile_dropdown(self):
        return self.weh.get_elements(self.common_object_wifi1_radio_profile_dropdown)

    def get_common_object_wifi0_client_access(self):
        return self.weh.get_element(self.common_object_wifi0_client_access)

    def get_common_object_wifi0_mesh_link(self):
        return self.weh.get_element(self.common_object_wifi0_mesh_link)

    def get_common_object_wifi0_sensor(self):
        return self.weh.get_element(self.common_object_wifi0_sensor)

    def get_common_object_wifi1_client_access(self):
        return self.weh.get_element(self.common_object_wifi1_client_access)

    def get_common_object_wifi1_mesh_link(self):
        return self.weh.get_element(self.common_object_wifi1_mesh_link)

    def get_common_object_wifi1_sensor(self):
        return self.weh.get_element(self.common_object_wifi1_sensor)

    def get_common_object_ap_template_enable_sdr(self):
        return self.weh.get_element(self.common_object_ap_template_enable_sdr)

    def get_common_object_ap_template_sdr_dropdown_button(self):
        return self.weh.get_element(self.common_object_ap_template_sdr_dropdown_button)

    def get_common_object_ap_template_sdr_dropdown(self):
        return self.weh.get_elements(self.common_object_ap_template_sdr_dropdown)

    def get_common_object_ap_template_disable_ssid(self):
        return self.weh.get_element(self.common_object_ap_template_disable_ssid)

    def get_common_object_ap_template_lldp_eth0(self):
        return self.weh.get_element(self.common_object_ap_template_lldp_eth0)

    def get_common_object_ap_template_lldp_eth1(self):
        return self.weh.get_element(self.common_object_ap_template_lldp_eth1)

    def get_common_object_ap_template_cdp_eth0(self):
        return self.weh.get_element(self.common_object_ap_template_cdp_eth0)

    def get_common_object_ap_template_cdp_eth1(self):
        return self.weh.get_element(self.common_object_ap_template_cdp_eth1)

    def get_common_object_ap_template_eth0_status(self):
        return self.weh.get_element(self.common_object_ap_template_eth0_status)

    def get_common_object_ap_template_eth1_status(self):
        return self.weh.get_element(self.common_object_ap_template_eth1_status)

    def get_common_object_wifi2_primary_server_ip(self):
        return self.weh.get_element(self.common_object_wifi2_primary_server_ip)

    def get_common_object_wifi2_primary_server_port(self):
        return self.weh.get_element(self.common_object_wifi2_primary_server_port)

    def get_common_object_ap_template_save_button(self):
        return self.weh.get_element(self.common_object_ap_template_save_button)

    def get_common_object_radio_profile_pagination_max(self):
        return self.weh.get_element(self.common_object_radio_profile_select_pagination_max)

    def get_common_object_imago_tag_profile_add_button(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_add_button)

    def get_common_object_imago_tag_profile_name_textfield(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_name_textfield)

    def get_common_object_imago_tag_profile_description_textfield(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_description_textfield)
    
    def get_common_object_imago_tag_profile_server_textfield(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_server_textfield)

    def get_common_object_imago_tag_profile_channel_drop_down_button(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_channel_drop_down_button)

    def get_common_object_imago_tag_profile_channel_drop_down_options(self):
        return self.weh.get_elements(self.common_object_imago_tag_profile_channel_drop_down_options)

    def get_common_object_imago_tag_profile_fcc_mode_checkbox(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_fcc_mode_checkbox)

    def get_common_object_imago_tag_profile_advanced_settings_tab(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_advanced_settings_tab)

    def get_common_object_imago_tag_profile_advanced_settings_server_port(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_advanced_settings_server_port)

    def get_common_object_imago_tag_profile_save_button(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_save_button)

    def get_common_object_imago_tag_profile_save_tooltip_text(self):
        return self.weh.get_element(self.common_object_imago_tag_profile_save_tooltip_text)

    def get_imago_tag_profile_grid_rows(self):
        grid_rows = self.weh.get_elements(self.imago_tag_profile_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_imago_tag_profile_select_checkbox(self, row):
        return self.weh.get_element(self.imago_tag_profile_select_checkbox, parent=row)

    def get_imago_tag_profile_edit_button(self):
        return self.weh.get_element(self.imago_tag_profile_edit_button)

    def get_common_object_ip_firewall_policy_add_button(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_add_button)

    def get_common_object_ip_firewall_policy_name_textfield(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_name_textfield)

    def get_common_object_ip_firewall_policy_description_textfield(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_description_textfield)

    def get_common_object_ip_firewall_policy_add_rule_button(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_add_rule_button)

    def get_common_object_ip_firewall_policy_add_rule_select_button(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_add_rule_select_button)

    def get_common_object_ip_firewall_policy_add_rule_application_tab(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_add_rule_application_tab)

    def get_common_object_ip_firewall_policy_add_rule_select_application_rows(self):
        grid_rows = self.weh.get_elements(self.common_object_ip_firewall_policy_add_rule_select_application_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_firewall_policy_add_rule_select_application_check_box(self, row):
        return self.weh.get_element(self.firewall_policy_add_rule_select_application_check_box, parent=row)

    def get_common_object_ip_firewall_policy_select_application_save_button(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_select_application_save_button)

    def get_common_object_ip_firewall_policy_rule_action_dropdown_button(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_rule_action_dropdown_button)

    def get_common_object_ip_firewall_policy_rule_action_dropdown_options(self):
        return self.weh.get_elements(self.common_object_ip_firewall_policy_rule_action_dropdown_options)

    def get_common_object_ip_firewall_policy_save_button(self):
        return self.weh.get_element(self.common_object_ip_firewall_policy_save_button)

    def get_common_object_policy_user_profile_name_textfield(self):
        return self.weh.get_element(self.common_object_policy_user_profile_name_textfield)

    def get_common_object_policy_user_profile_security_tab(self):
        return self.weh.get_element(self.common_object_policy_user_profiles_security_tab)

    def get_common_object_user_profile_add_button(self):
        return self.weh.get_element(self.common_object_user_profile_add_button)

    def get_common_object_user_profile_firewall_rules_radio_button(self):
        return self.weh.get_element(self.common_object_user_profile_firewall_rules_radio_button)

    def get_common_object_user_profile_select_ip_firewall_policy_button(self):
        return self.weh.get_element(self.common_object_user_profile_select_ip_firewall_policy_button)

    def get_firewall_policy_select_dialog_rows(self):
        parent = self.weh.get_element(self.firewall_policy_select_dialog)
        return self.weh.get_elements(self.firewall_policy_select_dialog_rows, parent)

    def get_firewall_policy_select_dialog_cancel_button(self):
        parent = self.weh.get_element(self.firewall_policy_select_dialog)
        return self.weh.get_element(self.firewall_policy_select_dialog_cancel_button, parent)

    def get_firewall_policy_select_dialog_row_checkbox(self, row):
        return self.weh.get_element(self.firewall_policy_select_dialog_row_checkbox, row)

    def get_firewall_policy_select_dialog_select_button(self):
        return self.weh.get_element(self.firewall_policy_select_dialog_select_button)

    def get_user_profile_save_button(self):
        return self.weh.get_element(self.user_profile_save_button)