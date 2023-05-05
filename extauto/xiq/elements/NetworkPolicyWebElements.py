from extauto.xiq.defs.NetworkPolicyWebElementDefinition import NetworkPolicyWebElementDefinition
from extauto.common.WebElementHandler import WebElementHandler


class NetworkPolicyWebElements(NetworkPolicyWebElementDefinition):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_network_policy_list_view(self):
        return self.weh.get_element(self.list_view)

    def get_network_policy_card_view(self):
        return self.weh.get_element(self.card_view)

    def get_np_grid_rows(self):
        elements = self.weh.get_elements(self.np_grid_rows)
        return [] if elements is None else elements[1:]

    def get_np_row_cell(self, row, field='field-name'):
        """
        Get the cell from the row
        :param row: web element handler of the row
        :param field: it is the cell name which we need to get the handler ex:field-selector, field-name,
        field-description, field-updateAt
        :return:
        """
        cells = self.weh.get_elements(self.np_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_np_delete_button(self):
        return self.weh.get_element(self.np_delete_button)

    def get_np_delete_confirm_yes_button(self):
        return self.weh.get_element(self.np_delete_confirm_yes_button)

    def get_np_edit_button(self):
        return self.weh.get_element(self.np_edit_button)

    def get_np_add_button(self):
        return self.weh.get_element(self.np_add_button)

    def get_np_wireless_check_box(self):
        return self.weh.get_element(self.np_wireless_check_box)

    def get_np_name_text(self):
        return self.weh.get_element(self.policy_name_text)

    def get_np_save_button(self):
        return self.weh.get_element(self.policy_save_button)

    def get_np_save_tool_tip(self):
        return self.weh.get_element(self.np_save_tool_tip)

    def get_np_exit_button(self):
        return self.weh.get_element(self.policy_exit_button)

    def get_network_policy_card_item_edit_icon(self, policy_card):
        return self.weh.get_element(self.network_policy_card_item_edit_icon, parent=policy_card)

    def get_network_policy_wireless_networks_tab(self):
        return self.weh.get_element(self.network_policy_wireless_networks_tab)

    def get_network_policy_wireless_networks_grid(self):
        return self.weh.get_element(self.network_policy_wireless_networks_grid)

    def get_network_policy_wireless_networks_grid_rows(self):
        grid = self.get_network_policy_wireless_networks_grid()
        return self.weh.get_elements(self.netwrok_policy_wireless_networks_grid_rows, parent=grid)

    def get_network_policy_wireless_networks_grid_cells(self):
        grid = self.get_network_policy_wireless_networks_grid()
        return self.weh.get_elements(self.netwrok_policy_wireless_networks_grid_cells, parent=grid)

    def get_ssid_cell(self, ssid):
        grid_cells = self.get_network_policy_wireless_networks_grid_rows()
        for cell in grid_cells:
            if ssid in cell.text:
                return cell

    def get_ssid_href(self, ssid):
        cell = self.get_ssid_cell(ssid)
        return self.weh.get_element(self.netwrok_policy_wireless_networks_grid_ssid_href, parent=cell)

    def get_network_policy_wireless_ssid_name_textfield(self):
        return self.weh.get_element(self.network_policy_wireless_ssid_name_textfield)

    def get_network_policy_wireless_networks_save_button(self):
        elements = self.weh.get_elements(self.network_policy_wireless_networks_save_button)
        for element in elements:
            if "SAVE" in element.text.upper():
                return element

    def get_network_policy_grid_view(self):
        """
        :return: network policy grid view web element object
        """
        return self.weh.get_element(self.card_view)

    def get_network_policy_card_items(self):
        """

        :return:
        """
        return self.weh.get_elements(self.network_policy_card_item)

    def get_deploy_policy_tab(self):
        return self.weh.get_element(self.deploy_policy_tab)

    def get_np_policy_crumb_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.np_policy_crumb_button)

    def get_eligible_device_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.eligible_device_button)

    def get_device_grid_rows(self):
        """

        :return:
        """
        grid_rows = self.weh.get_elements(self.device_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_device_select_check_box(self, parent):
        """

        :param parent:
        :return:
        """
        return self.weh.get_element(self.device_select_check_box, parent=parent)

    def get_deploy_policy_upload_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.deploy_policy_upload_button)

    def get_perform_update_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.perform_update_button)

    def get_network_policy_cards(self):
        return self.weh.get_elements(self.network_policy_cards)

    def get_network_policy_card_ssids(self, card):
        return self.weh.get_elements(self.network_policy_card_ssids, parent=card)

    def get_network_policy_name_from_card_view(self, card):
        return self.weh.get_element(self.network_policy_name_from_card_view, parent=card)

    def check_np_add_button(self):
        np_add_ele = self.weh.get_element(self.np_add_button)
        if np_add_ele.is_displayed():
            return 1
        else:
            return -2

    def get_np_page_title(self):
        return self.weh.get_element(self.np_title)

    def get_network_policy_page_size(self, page_size='100'):
        if els := self.weh.get_elements(self.network_policy_page_size):
            for el in els:
                if str(page_size) in el.text:
                    return el

    def get_back_to_network_policy_list(self):
        """

        :return:
        """
        return self.weh.get_element(self.back_to_network_policy_list)

    def get_configure_to_network_policy_panel(self):
        """

        :return:
        """
        return self.weh.get_element(self.configure_to_network_policy_panel)

    def get_enable_presence_analytics_btn(self):
        return self.weh.get_element(self.enable_presence_analytics_btn)

    def get_network_policy_additional_settings_tab(self):
        return self.weh.get_element(self.network_policy_additional_settings_tab)

    def get_policy_settings_menu(self):
        return self.weh.get_element(self.policy_settings_menu)

    def get_additional_settings_ibeacon_menu(self):
        return self.weh.get_element(self.additional_settings_ibeacon_menu)

    def get_ibeacon_status_button(self):
        return self.weh.get_element(self.ibeacon_status_button)

    def get_ibeacon_service_name_textfield(self):
        return self.weh.get_element(self.ibeacon_service_name_textfield)

    def get_ibeacon_description_textfield(self):
        return self.weh.get_element(self.ibeacon_description_textfield)

    def get_ibeacon_uuid_textfield(self):
        return self.weh.get_element(self.ibeacon_uuid_textfield)

    def get_ibeacon_monitoring_checkbox(self):
        return self.weh.get_element(self.ibeacon_monitoring_checkbox)

    def get_ibeacon_services_save_button(self):
        return self.weh.get_element(self.ibeacon_services_save_button)

    def get_ibeacon_services_cancel_button(self):
        return self.weh.get_element(self.ibeacon_services_cancel_button)

    def get_access_security_pre_authentication_checkbox(self):
        return self.weh.get_element(self.access_security_pre_authentication_checkbox)

    def get_access_security_settings_save_button(self):
        return self.weh.get_element(self.access_security_settings_save_button)

    def get_ssid_authentication_additional_settings_option(self):
        return self.weh.get_element(self.ssid_authentication_additional_settings_option)

    def get_advance_access_security_customize_button(self):
        return self.weh.get_element(self.advance_access_security_customize_button)

    def get_np_ssid_save_button(self):
        return self.weh.get_element(self.np_ssid_save_button)

    def get_np_switches_check_box(self):
        return self.weh.get_element(self.np_switches_check_box)

    def get_np_routing_check_box(self):
        return self.weh.get_element(self.np_routing_check_box)

    def get_devices_stack_update_policy_dropdown_btn(self):
        return self.weh.get_element(self.devices_stack_update_policy_dropdown_btn)

    def get_devices_stack_update_policy_dropdown_items(self):
        return self.weh.get_elements(self.devices_stack_update_policy_dropdown_items)

    def get_perform_update_policy_button(self):
        return self.weh.get_element(self.perform_update_policy_button)

    def get_perform_after_select_update_policy_button(self):
        return self.weh.get_element(self.perform_after_select_update_policy_button)

    def get_yes_after_perform_update_button(self):
        return self.weh.get_element(self.yes_after_perform_update_button)

    def get_additional_settings_classifiermaps(self):
        return self.weh.get_element(self.additional_settings_classifiermaps)

    def get_classifiermaps_enable(self):
        return self.weh.get_element(self.classifiermaps_enable)

    def get_classifiermaps_name(self):
        return self.weh.get_element(self.classifiermaps_name)

    def get_classifiermaps_description(self):
        return self.weh.get_element(self.classifiermaps_description)

    def get_classifiermaps_add_button(self):
        return self.weh.get_element(self.classifiermaps_add_button)

    def get_classifiermaps_services_selectfromfollowing_link(self):
        return self.weh.get_element(self.classifiermaps_services_selectfromfollowing_link)

    def get_classifiermaps_services_select_service_bgp(self):
        return self.weh.get_element(self.classifiermaps_services_select_service_bgp)

    def get_classifiermaps_services_initial_save_button(self):
        return self.weh.get_element(self.classifiermaps_services_initial_save_button)

    def get_classifiermaps_services_save_button(self):
        return self.weh.get_element(self.classifiermaps_services_save_button)

    def get_classifiermaps_802_link(self):
        return self.weh.get_element(self.classifiermaps_802_link)

    def get_classifiermaps_macoui_link(self):
        return self.weh.get_element(self.classifiermaps_macoui_link)

    def get_classifiermaps_macoui_add(self):
        return self.weh.get_element(self.classifiermaps_macoui_add)

    def get_classifiermaps_macoui_dropdown(self):
        return self.weh.get_element(self.classifiermaps_macoui_dropdown)

    def get_classifiermaps_add_macoui_from_dropdown(self):
        return self.weh.get_element(self.classifiermaps_add_macoui_from_dropdown)

    def get_classifiermaps_macoui_save_button(self):
        return self.weh.get_element(self.classifiermaps_macoui_save_button)

    def get_classifiermaps_ssid_link(self):
        return self.weh.get_element(self.classifiermaps_ssid_link)

    def get_classifiermaps_add_ssid(self):
        return self.weh.get_element(self.classifiermaps_add_ssid)

    def get_classifiermaps_ssid_save_button(self):
        return self.weh.get_element(self.classifiermaps_ssid_save_button)

    def get_classifiermaps_802enable(self):
        return self.weh.get_element(self.classifiermaps_802enable)

    def get_classifiermaps_diffservenable(self):
        return self.weh.get_element(self. classifiermaps_diffservenable)

    def get_classifiermaps_80211enable(self):
        return self.weh.get_element(self.classifiermaps_80211enable)

    def get_Classifier_Maps_save_button(self):
        return self.weh.get_element(self.Classifier_Maps_save_button)

    def get_qos_options_menu(self):
        return self.weh.get_element(self.qos_options_menu)

    def get_additional_settings_marker_maps(self):
        return self.weh.get_element(self.additional_settings_marker_maps)

    def get_marker_maps_status_button(self):
        return self.weh.get_element(self.marker_maps_status_button)

    def get_marker_maps_name_textfield(self):
        return self.weh.get_element(self.marker_maps_name_textfield)

    def get_marker_maps_description(self):
        return self.weh.get_element(self.marker_maps_description)

    def get_marker_maps_services_save_button(self):
        return self.weh.get_element(self.marker_maps_services_save_button)

    def get_marker_maps_8021P(self):
        return self.weh.get_element(self.marker_maps_8021P)

    def get_marker_maps_NetworkControl_textfield(self):
        return self.weh.get_element(self.marker_maps_NetworkControl_textfield)

    def get_marker_maps_ControlledLoad_textfield(self):
        return self.weh.get_element(self.marker_maps_ControlledLoad_textfield)

    def get_marker_maps_Excellent_Effort_textfield(self):
        return self.weh.get_element(self.marker_maps_Excellent_Effort_textfield)

    def get_marker_maps_Best_Effort2_textfield(self):
        return self.weh.get_element(self.marker_maps_Best_Effort2_textfield)

    def get_marker_maps_Switch_to_diffServ(self):
        return self.weh.get_element(self.marker_maps_Switch_to_diffServ)

    def get_marker_maps_diffServ(self):
        return self.weh.get_element(self.marker_maps_diffServ)

    def get_marker_maps_NC_diffServ_textfield(self):
        return self.weh.get_element(self.marker_maps_NC_diffServ_textfield)

    def get_marker_maps_Voice_diffServ_textfield(self):
        return self.weh.get_element(self.marker_maps_Voice_diffServ_textfield)

    def get_marker_maps_Video_diffServ_textfield(self):
        return self.weh.get_element(self.marker_maps_Video_diffServ_textfield)

    def get_marker_maps_BG_diffServ_textfield(self):
        return self.weh.get_element(self.marker_maps_BG_diffServ_textfield)

    def get_additional_settings_QoS_Overview(self):
        return self.weh.get_element(self.additional_settings_QoS_Overview)

    def get_QoS_Dynamic_Airtime_Scheduling_Enable(self):
        return self.weh.get_element(self.QoS_Dynamic_Airtime_Scheduling_Enable)

    def get_QoS_services_save_button(self):
        return self.weh.get_element(self.QoS_services_save_button)

    def get_add_ssid_menu(self):
        return self.weh.get_element(self.add_ssid_menu)

    def get_select_all_other_networks(self):
        return self.weh.get_element(self.select_all_other_networks)

    def get_wireless_networks_ssid_textfield(self):
        return self.weh.get_element(self.wireless_networks_ssid_textfield)

    def get_OWE_wifi2_checkbox(self):
        return self.weh.get_element(self.OWE_wifi2_checkbox)

    def get_OWE_wifi2_dialogue_box_yes(self):
        return self.weh.get_element(self.OWE_wifi2_dialogue_box_yes)

    def get_Enhanced_Open_Authentication(self):
        return self.weh.get_element(self.Enhanced_Open_Authentication)

    def get_OWE_Transition_mode(self):
        return self.weh.get_element(self.OWE_Transition_mode)

    def get_enhanced_open_ssid_field(self):
        return self.weh.get_element(self.enhanced_open_ssid_field)

    def get_save_enhanced_open_ssid(self):
        return self.weh.get_element(self.save_enhanced_open_ssid)

    def get_network_policy_management_options(self):
        return self.weh.get_element(self.network_policy_management_options)

    def enable_management_options_button(self):
        return self.weh.get_element(self.enable_management_options)

    def management_option_name_textfield(self):
        return self.weh.get_element(self.management_option_name)

    def enable_legacy_http_redirect_checkbox(self):
        return self.weh.get_element(self.enable_legacy_http_redirect)

    def save_management_option_button(self):
        return self.weh.get_element(self.save_management_option)

    def get_mgmt_option_success(self):
        return self.weh.get_element(self.mgmt_option_success)

    def get_management_option_on_off_button(self):
        return self.weh.get_element(self.management_option_on_off_button)

    def get_re_use_management_options_setting_button(self):
        return self.weh.get_element(self.re_use_management_options_setting_button)

    def get_table_management_options_rows(self):
        return self.weh.get_elements(self.table_management_options_rows)

    def get_table_management_options_row_checkbox(self, row):
        return self.weh.get_elements(self.table_management_options_row_checkbox, parent=row)

    def get_management_options_select_button(self):
        return self.weh.get_element(self.management_options_select_button)

    def get_device_templates_tab(self):
        return self.weh.get_element(self.device_templates_tab)

    def get_nw_policy_port_types_view_all_pages(self):
        return self.weh.get_element(self.nw_policy_port_types_view_all_pages)

    def get_next_page_element_disabled(self):
        return self.weh.get_element(self.next_page_element_disabled)

    def get_next_page_element(self, page_size='50'):
        return self.weh.get_elements(self.next_page_element)

    def get_switching_tab(self):
        return self.weh.get_element(self.switching_tab)

    def get_common_settings_voss(self):
        return self.weh.get_element(self.common_settings_voss)

    def get_voss_parameters_text(self):
        elements = self.weh.get_elements(self.voss_parameters_text)
        for el in elements:
            if el.is_displayed():
                return el.text

    def get_port_types_section(self):
        return self.weh.get_element(self.port_types_section)

    def get_port_types_title_page(self):
        return self.weh.get_element(self.port_types_title_page)

    def get_add_new_port_type(self):
        return self.weh.get_element(self.add_new_port_type)

    def get_edit_port_type(self):
        return self.weh.get_element(self.edit_port_type)

    def get_delete_port_type(self):
        return self.weh.get_element(self.delete_port_type)

    def get_select_platform_voss(self):
        return self.weh.get_element(self.select_platform_voss)

    def get_select_platform_exos(self):
        return self.weh.get_element(self.select_platform_exos)

    def get_port_types_rows(self):
        return self.weh.get_elements(self.port_types_rows)[1:]

    def get_port_type_row_cells(self, row):
        """
        :return: device row cell elements
        """
        return self.weh.get_elements(self.port_type_row_cells, row)

    def get_nw_policy_additional_settings_dns_server_tab(self):
        return self.weh.get_element(self.nw_policy_additional_settings_dns_server_tab)

    def get_dns_server_status(self):
        return self.weh.get_element(self.dns_server_status)

    def get_dns_server_save_button(self):
        return self.weh.get_element(self.dns_server_save_button)

    def get_port_type_row_cell(self, row, field='field-name'):
        """
        Get the cell from the row
        :param row: web element handler of the row
        :param field: it is the cell name which we need to get the handler ex:field-selector, field-name,
        field-description,
        :return:
        """
        cells = self.weh.get_elements(self.port_type_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_network_policy_card_item(self):
        return self.weh.get_element(self.network_policy_card_item)

    def get_common_settings_exos(self):
        return self.weh.get_element(self.common_settings_exos)

    def get_common_settings_exos_stp_toogle(self):
        return self.weh.get_element(self.common_settings_exos_stp_toogle)

    def get_common_settings_voss_stp_toogle(self):
        return self.weh.get_element(self.common_settings_voss_stp_toogle)

    def get_common_settings_save_button(self):
        return self.weh.get_element(self.common_settings_save_button)

    def get_all_common_settings_configs(self):
        elems = []
        for el in self.weh.get_elements(self.all_common_settings_configs):
            if el.is_displayed():
                elems.append(el)
        return elems

