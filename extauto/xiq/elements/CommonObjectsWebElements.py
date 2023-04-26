from extauto.xiq.defs.CommonObjectsWebElementsDefinitions import CommonObjectsWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


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


    def get_ip_object_hostname_page(self):
        return self.weh.get_element(self.ip_object_hostname_page)

    def get_ip_object_hostname_object_page_size_100(self):
        return self.weh.get_elements(self.ip_object_hostname_object_page_size_100)

    def get_ip_object_hostname_existed_object_list_per_page(self):
        return self.weh.get_elements(self.ip_object_hostname_existed_object_list_per_page)

    def get_ip_object_hostname_existed_object_name(self, ip_object_row):
        return self.weh.get_element(self.ip_object_hostname_existed_object_name, ip_object_row)

    def get_ip_object_hostname_add_button(self):
        return self.weh.get_element(self.ip_object_hostname_add_button)

    def get_ip_object_hostname_edit_button(self):
        return self.weh.get_element(self.ip_object_hostname_edit_button)

    def get_ip_object_hostname_delete_button(self):
        return self.weh.get_element(self.ip_object_hostname_delete_button)

    def get_ip_object_hostname_object_checkbox_checked(self, ip_object_row):
        return self.weh.get_element(self.ip_object_hostname_object_checkbox_checked, ip_object_row)

    def get_ip_object_hostname_delete_confirm_win(self):
        return self.weh.get_element(self.ip_object_hostname_delete_confirm_win)

    def get_ip_object_hostname_delete_confirm_win_no(self):
        return self.weh.get_element(self.ip_object_hostname_delete_confirm_win_no)

    def get_ip_object_hostname_delete_confirm_win_yes(self):
        return self.weh.get_element(self.ip_object_hostname_delete_confirm_win_yes)

    def get_ip_object_hostname_profile_name_textfield(self):
        return self.weh.get_element(self.ip_object_hostname_profile_name_textfield)

    def get_ip_object_type_drop_down(self):
        return self.weh.get_element(self.ip_object_type_drop_down)

    def get_ip_object_type_options(self):
        return self.weh.get_elements(self.ip_object_type_options)

    def get_ip_object_type(self):
        return self.weh.get_element(self.ip_object_type)

    def get_ip_object_ip_address_textfield(self):
        return self.weh.get_element(self.ip_object_ip_address_textfield)

    def get_ip_object_ip_address_value(self):
        return self.weh.get_element(self.ip_object_ip_address_value)

    def get_ip_object_hostname_textfield(self):
        return self.weh.get_element(self.ip_object_hostname_textfield)

    def get_ip_object_wildcard_hostname_textfield(self):
        return self.weh.get_element(self.ip_object_wildcard_hostname_textfield)

    def get_ip_object_ip_network_subnet_textfield(self):
        return self.weh.get_element(self.ip_object_ip_network_subnet_textfield)

    def get_ip_object_ip_network_netmask_textfield(self):
        return self.weh.get_element(self.ip_object_ip_network_netmask_textfield)

    def get_ip_object_ip_range_start_textfield(self):
        return self.weh.get_element(self.ip_object_ip_range_start_textfield)

    def get_ip_object_ip_range_end_textfield(self):
        return self.weh.get_element(self.ip_object_ip_range_end_textfield)

    def get_ip_object_wildcard_ip_textfield(self):
        return self.weh.get_element(self.ip_object_wildcard_ip_textfield)

    def get_ip_object_wildcard_mask_textfield(self):
        return self.weh.get_element(self.ip_object_wildcard_mask_textfield)

    def get_ip_object_ip_network_subnet_textfield_row(self, row: object) -> object:
        return self.weh.get_element(self.ip_object_ip_network_subnet_textfield, row)

    def get_ip_object_ip_network_netmask_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_ip_network_netmask_textfield, row)

    def get_ip_object_ip_range_start_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_ip_range_start_textfield, row)

    def get_ip_object_ip_range_end_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_ip_range_end_textfield, row)

    def get_ip_object_wildcard_ip_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_wildcard_ip_textfield, row)

    def get_ip_object_wildcard_mask_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_wildcard_mask_textfield, row)

    def get_ip_object_wildcard_host_textfield(self, row):
        return self.weh.get_element(self.ip_object_wildcard_host_textfield, row)

    def get_ip_object_ip_address_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_ip_address_textfield, row)

    def get_ip_object_hostname_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_hostname_textfield, row)

    def get_ip_object_wildcard_hostname_textfield_row(self, row):
        return self.weh.get_element(self.ip_object_wildcard_hostname_textfield, row)

    def get_ip_object_save_button(self):
        return self.weh.get_element(self.ip_object_save_button)

    def get_ip_object_cancel_button(self):
        return self.weh.get_element(self.ip_object_cancel_button)

    def get_ip_object_add_new_object(self):
        return self.weh.get_element(self.ip_object_add_new_object)

    def get_ip_object_confirm_message_window(self):
        return self.weh.get_element(self.ip_object_confirm_message_window)

    def get_ip_object_object_rows(self):
        return self.weh.get_elements(self.ip_object_object_rows, self.weh.get_element(self.ip_object_create_object_page))

    def get_ip_object_object_item_type(self, row):
        return self.weh.get_element(self.ip_object_object_item_type, row)

    def get_ip_object_hostname_object_items_page_size_100(self):
        return self.weh.get_element(self.ip_object_hostname_object_items_page_size_100)

    def get_ip_object_confirm_message_window_yes_button(self):
        return self.weh.get_element(self.ip_object_confirm_message_window_yes_button)

    def get_ip_object_hostname_add_cls_rule_button(self):
        return self.weh.get_element(self.ip_object_hostname_object_add_classification_rule)

    def get_ip_object_hostname_select_cls_rule_button(self, row):
        return self.weh.get_element(self.ip_object_hostname_select_cls_rule_button, row)

    def get_ip_object_hostname_classification_rule_page(self):
        return self.weh.get_element(self.ip_object_hostname_classification_rule_page)

    def get_ip_object_hostname_classification_rule_page_size_100(self):
        return self.weh.get_element(self.ip_object_hostname_classification_rule_page_size_100)

    def get_ip_object_hostname_classification_rules(self):
        return self.weh.get_elements(self.ip_object_hostname_classification_rules)

    def get_ip_object_hostname_classification_rule_name(self, rule):
        return self.weh.get_element(self.ip_object_hostname_classification_rule_name, rule)

    def get_ip_object_hostname_classification_rule_page_link_button(self):
        return self.weh.get_element(self.ip_object_hostname_classification_rule_page_link_button)

    def get_ip_object_hostname_classification_rule_used_error(self):
        return self.weh.get_element(self.ip_object_hostname_classification_rule_used_error)

    def get_ip_object_hostname_classification_rule_used_error_close(self):
        return self.weh.get_element(self.ip_object_hostname_classification_rule_used_error_close)

    def get_ip_object_hostname_profile_objects_list_page_num_bottom(self):
        return  self.weh.get_element(self.ip_object_hostname_profile_objects_list_page_num_bottom)

    def get_ip_object_hostname_profile_objects_list_last_page(self):
        return self.weh.get_element(self.ip_object_hostname_profile_objects_list_last_page)



    def get_common_object_grid_rows(self):
        return self.weh.get_elements(self.common_object_grid_rows)

    def get_common_object_grid_row_cells(self, row, field='field-name'):
        cells = self.weh.get_elements(self.common_object_grid_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_common_object_supp_cli_grid_rows(self):
        return self.weh.get_elements(self.common_object_supp_cli_grid_rows)

    def get_common_object_supp_cli_grid_row_cells(self, row, field='field-name'):
        cells = self.weh.get_elements(self.common_object_supp_cli_grid_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("idx"):
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
        return self.weh.get_element(self.common_object_confirm_delete_button)

    def get_cwp_self_reg_employee_approval_button(self):
        return self.weh.get_element(self.cwp_self_reg_employee_approval_button)

    def get_cwp_save_button(self):
        elements = self.weh.get_elements(self.cwp_save_button)
        return self.get_dislayed_element(elements)

    def get_page_size_element(self, page_size='50'):
        if els := self.weh.get_elements(self.page_size_element):
            for el in els:
                if str(page_size) in el.text:
                    return el

    def get_page_numbers(self):
        return self.weh.get_elements(self.page_numbers)

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

    def get_common_object_basic_supp_cli_view_all_pages(self):
        """
        :return: get_common_object_basic_supp_cli_view_all_pages
        """
        return self.weh.get_element(self.common_object_basic_supp_cli_view_all_pages)

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

    def get_common_object_template_grid_row_href(self, cell):
        return self.weh.get_element(self.common_object_grid_row_cells_href, cell)

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

    def get_common_object_wifi0_radio_operating_mode_combox(self):
        return self.weh.get_element(self.common_object_wifi0_radio_operating_mode_combox)

    def get_common_object_wifi0_radio_operating_mode_combox_list(self):
        return self.weh.get_elements(self.common_object_wifi0_radio_operating_mode_combox_list)

    def get_common_object_wifi0_radio_profile_textbox(self):
        return self.weh.get_element(self.common_object_wifi0_radio_profile_textbox)

    def get_common_object_wifi1_radio_profile_textbox(self):
        return self.weh.get_element(self.common_object_wifi1_radio_profile_textbox)

    def get_common_object_wifi2_radio_profile_textbox(self):
        return self.weh.get_element(self.common_object_wifi2_radio_profile_textbox)

    def get_common_object_wifi1_radio_profile_button(self):
        return self.weh.get_element(self.common_object_wifi1_radio_profile_button)

    def get_common_object_wifi0_radio_profile_dropdown(self):
        return self.weh.get_elements(self.common_object_wifi0_radio_profile_dropdown)

    def get_common_object_wifi1_radio_profile_dropdown(self):
        return self.weh.get_elements(self.common_object_wifi1_radio_profile_dropdown)

    def get_common_object_wifi0_client_mode(self):
        return self.weh.get_element(self.common_object_wifi0_client_mode)

    def get_common_object_wifi0_add_client_mode_profile(self):
        return self.weh.get_element(self.common_object_wifi0_add_client_mode_profile)

    def get_common_object_wifi1_add_client_mode_profile(self):
        return self.weh.get_element(self.common_object_wifi1_add_client_mode_profile)

    def get_common_object_wifi0_1_client_mode_profile_name(self):
        return self.weh.get_element(self.common_object_wifi0_1_client_mode_profile_name)

    def get_common_object_wifi0_1_cm_local_web_page_checkbox(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_page_checkbox)

    def get_common_object_wifi0_1_cm_local_web_page_add(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_page_add)

    def get_common_object_wifi0_1_cm_local_web_page_ssid_textbox(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_page_ssid_textbox)

    def get_common_object_wifi0_1_cm_local_web_page_password_textbox(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_page_password_textbox)

    def get_common_object_wifi0_1_cm_local_web_page_auth_dropdown(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_page_auth_dropdown)

    def get_common_object_wifi0_1_cm_local_web_page_auth_dropdown_option(self):
        return self.weh.get_elements(self.common_object_wifi0_1_cm_local_web_page_auth_dropdown_option)

    def get_common_object_wifi0_1_cm_local_web_key_type_dropdown(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_key_type_dropdown)

    def get_common_object_wifi0_1_cm_local_web_key_type_dropdown_option(self):
        return self.weh.get_elements(self.common_object_wifi0_1_cm_local_web_key_type_dropdown_option)

    def get_common_object_wifi0_1_cm_local_web_page_add_button(self):
        return self.weh.get_element(self.common_object_wifi0_1_cm_local_web_page_add_button)

    def get_common_object_wifi0_1_client_mode_profile_dhcp_server_scope(self):
        return self.weh.get_element(self.common_object_wifi0_1_client_mode_profile_dhcp_server_scope)

    def get_common_object_wifi0_1_client_mode_profile_save(self):
        return self.weh.get_element(self.common_object_wifi0_1_client_mode_profile_save)

    def get_common_object_basic_client_mode_profiles_grid_rows_all(self):
        return self.weh.get_elements(self.common_object_basic_client_mode_profiles_grid_rows_all)

    def get_common_object_basic_client_mode_profiles_selectall(self):
        return self.weh.get_element(self.common_object_basic_client_mode_profiles_selectall)

    def get_common_object_basic_client_mode_profiles_delete(self):
        return self.weh.get_element(self.common_object_basic_client_mode_profiles_delete)

    def get_common_object_basic_client_mode_profiles_delete_confirm_ok_button(self):
        return self.weh.get_element(self.common_object_basic_client_mode_profiles_delete_confirm_ok_button)

    def get_common_object_wifi0_client_access(self):
        return self.weh.get_element(self.common_object_wifi0_client_access)

    def get_common_object_wifi0_mesh_link(self):
        return self.weh.get_element(self.common_object_wifi0_mesh_link)

    def get_common_object_wifi0_sensor(self):
        return self.weh.get_element(self.common_object_wifi0_sensor)

    def get_common_object_wifi2_sensor(self):
        return self.weh.get_element(self.common_object_wifi2_sensor)

    def get_common_object_wifi0_sensor_UI_disable(self):
        return self.weh.get_element(self.common_object_wifi0_sensor_UI_disable)

    def get_common_object_wifi1_sensor_UI_disable(self):
        return self.weh.get_element(self.common_object_wifi1_sensor_UI_disable)

    def get_common_object_wifi2_sensor_UI_disable(self):
        return self.weh.get_element(self.common_object_wifi2_sensor_UI_disable)

    def get_common_object_wifi1_client_mode(self):
        return self.weh.get_element(self.common_object_wifi1_client_mode)

    def get_common_object_wifi1_client_access(self):
        return self.weh.get_element(self.common_object_wifi1_client_access)

    def get_common_object_wifi1_mesh_link(self):
        return self.weh.get_element(self.common_object_wifi1_mesh_link)

    def get_common_object_wifi1_sensor(self):
        return self.weh.get_element(self.common_object_wifi1_sensor)

    def get_common_object_wifi2_client_access(self):
        return self.weh.get_element(self.common_object_wifi2_client_access)

    def get_common_object_wifi2_mesh_link(self):
        return self.weh.get_element(self.common_object_wifi2_mesh_link)

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

    def get_common_object_ap_template_eth0_port_type(self):
        return self.weh.get_element(self.common_object_ap_template_eth0_port_type)

    def get_common_object_ap_template_eth1_port_type(self):
        return self.weh.get_element(self.common_object_ap_template_eth1_port_type)

    def get_common_object_ap_template_eth0_transmission_type(self):
        return self.weh.get_element(self.common_object_ap_template_eth0_transmission_type)

    def get_common_object_ap_template_eth1_transmission_type(self):
        return self.weh.get_element(self.common_object_ap_template_eth1_transmission_type)

    def get_common_object_ap_template_eth0_speed(self):
        return self.weh.get_element(self.common_object_ap_template_eth0_speed)

    def get_common_object_ap_template_eth1_speed(self):
        return self.weh.get_element(self.common_object_ap_template_eth1_speed)

    def get_common_object_wifi2_primary_server_ip(self):
        return self.weh.get_element(self.common_object_wifi2_primary_server_ip)

    def get_common_object_wifi2_primary_server_port(self):
        return self.weh.get_element(self.common_object_wifi2_primary_server_port)

    def get_common_object_ap_template_save_button(self):
        return self.weh.get_element(self.common_object_ap_template_save_button)

    def get_common_object_ap_template_cancel_button(self):
        return self.weh.get_element(self.common_object_ap_template_cancel_button)

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

    def get_policy_port_types_confirmation_button(self):
        return self.weh.get_element(self.policy_port_types_confirmation_button)

    def get_ui_tipbox_error(self):
        return self.weh.get_element(self.ui_tipbox_error)

    def get_next_page_element_disabled(self):
        return self.weh.get_element(self.next_page_element_disabled)

    def get_common_object_policy_max_page_number(self):
        return self.weh.get_elements(self.common_object_policy_max_page_number)

    def get_common_object_policy_go_to_first_page(self):
        elements = self.weh.get_elements(self.common_object_policy_go_to_first_page)
        for el in elements:
            if el.is_displayed():
                return el

    def get_scli_grid_bottom(self):
        return self.weh.get_element(self.scli_grid_bottom)
