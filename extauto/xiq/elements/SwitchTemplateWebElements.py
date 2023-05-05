from extauto.xiq.defs.SwitchTemplateWebElementsDefinitions import SwitchTemplateWebElementDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class SwitchTemplateWebElements(SwitchTemplateWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_sw_template_tab_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_template_switch_template_tab)

    def get_sw_template_rows(self):
        rows = []
        for el in self.weh.get_elements(self.sw_device_template_grid_rows) or []:  
            if el.is_displayed():          
                rows.append(el)   
        return rows

    def get_sw_template_platform_from_drop_down(self):
        """

        :return:
        """
        return self.weh.get_elements(self.device_sw_template_items)

    def get_sw_template_add_button(self):
        """

        :return:
        """
        return self.weh.get_elements(self.sw_template_add_button)

    def get_sw_template_save_button(self):
        return self.weh.get_elements(self.sw_template_save_btn)

    def get_sw_template_name_textfield(self):
        return self.weh.get_element(self.sw_template_name_textfield)

    def get_sw_template_enable_spanningtree(self):
        return self.weh.get_element(self.sw_template_enable_spanningtree)

    def get_sw_template_enable_stp(self):
        return self.weh.get_element(self.sw_template_enable_stp)

    def get_sw_template_enable_rstp(self):
        return self.weh.get_element(self.sw_template_enable_rstp)

    def get_sw_template_enable_mstp(self):
        return self.weh.get_element(self.sw_template_enable_mstp)

    def get_sw_template_port_configuration_tab(self):
        return self.weh.get_element(self.sw_template_port_configuration_tab)

    def get_sw_template_row_cell(self, row, field='field-name'):
        cells = self.weh.get_elements(self.sw_template_row_cells, row)
        return cells

    def get_sw_template_select_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_select_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_search_textfield(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_search_textfield)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_search_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_search_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_grid(self):
        """
        :return: Switch template selection grid
        """
        return self.weh.get_element(self.sw_template_selection_grid)

    def get_sw_template_table_rows(self, table):
        """
        :return: all the rows in the specified switch template selection grid
        """
        return self.weh.get_elements(self.sw_template_table_rows, parent=table)

    def get_sw_template_selection_grid_rows(self, table):
        """
        :return: all the rows in the specified switch template selection grid
        """
        return self.weh.get_elements(self.sw_template_selection_grid_rows, parent=table)

    def get_sw_template_selection_row_checkbox(self, row):
        """
        :return: selection check box for the specified row
        """
        return self.weh.get_element(self.sw_template_selection_row_checkbox, parent=row)

    def get_sw_template_selection_select_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_select_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_cancel_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_cancel_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_assign_button(self):
        """
        :return: 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_button)

    def get_sw_template_assign_choose_existing(self):
        """
        :return: 'Choose Existing' option of 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_choose_existing)

    def get_sw_template_assign_create_new(self):
        """
        :return: 'Create New' option of 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_create_new)

    def get_sw_template_assign_advanced_actions(self):
        """
        :return: 'Advanced Actions' option of 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_advanced_actions)

    def get_sw_template_assign_advanced_actions_aggr(self):
        """
        :return: 'Advanced Actions Aggregate' option of 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_advanced_actions_aggr)

    def get_sw_template_all_port_type_list_radio(self):
        """
        :return:  Radio buttons of the Port Types shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_elements(self.sw_template_port_type_list_radio)

    def get_sw_template_all_port_type_list_label(self):
        """
        :return:  Port Type labels of the Port Types shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_elements(self.sw_template_port_type_list_label)

    def get_sw_template_port_type_list_save_button(self):
        """
        :return:  SAVE button of the Port Type list shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_element(self.sw_template_port_type_list_save_button)

    def get_sw_template_port_type_list_cancel_button(self):
        """
        :return:  CANCEL button of the Port Type list shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_element(self.sw_template_port_type_list_cancel_button)

    def get_sw_template_select_all_ports_button(self):
        """
        :return: 'Select All Ports' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_select_all_ports_button)

    def get_sw_template_deselect_all_ports_button(self):
        """
        :return: 'Deselect All Ports' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_deselect_all_ports_button)

    def get_sw_template_wireframe_net_ports(self, list):
        """
        :return: list of selected ports on the wireframe of Port Configuration page in the switch template view
        """
        port_list = []
        elements = self.weh.get_elements(self.sw_template_wireframe_net_ports)
        for i in range(len(elements)):
            if i+1 in list:
                port_list.append(elements[i])
        return port_list

    def get_sw_template_selected_ports(self):
        """
        :return: list of selected ports on the wireframe of Port Configuration page in the switch template view
        """
        port_list = []
        elements = self.weh.get_elements(self.sw_template_port_selected_ports)
        for el in elements:
            if el.is_displayed():
                port_list.append(el)
        return port_list

    def get_sw_template_all_edit_port_type(self):
        return self.weh.get_elements(self.sw_template_edit_port_type)

    def get_sw_template_all_port_usage(self):
        return self.weh.get_elements(self.sw_template_port_usage)
        port_list = []
        elements = self.weh.get_elements(self.sw_template_all_port_usage)
        for el in elements:
            port_list.append(el)
        return port_list

    def get_sw_template_all_port_desc(self):
        return self.weh.get_elements(self.sw_template_port_desc)
        port_list = []
        elements = self.weh.get_elements(self.sw_template_port_desc)
        for el in elements:
            port_list.append(el)
        return port_list

    def get_sw_template_all_port_status(self):
        return self.weh.get_elements(self.sw_template_port_status)
        port_list = []
        elements = self.weh.get_elements(self.sw_template_port_status)
        for el in elements:
            port_list.append(el)
        return port_list

    def get_sw_template_stack_add_button(self):
        return self.weh.get_element(self.sw_template_stack_add_button)

    def get_sw_template_stack_delete_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_stack_delete_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_select_delete_button(self):
        return self.weh.get_element(self.sw_template_select_delete_button)

    def get_sw_template_sel_row_checkbox(self, row):
        """
        :return: selection check box for the specified row
        """
        return self.weh.get_element(self.sw_template_sel_row_checkbox, parent=row)

    def get_sw_template_selection_tipbox_text2(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_tipbox_text)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_close_button(self):
        return self.weh.get_element(self.sw_template_selection_close_button)

    def get_sw_template_check_box(self, row):
        """
        :return: selection check box for the specified row
        """
        return self.weh.get_element(self.sw_template_check_box, parent=row)

    def get_port_details_all_rows(self):
        return self.weh.get_template_elements(self.port_details_all_rows)

    def get_port_details_row_label(self, row):
        return self.weh.get_element(self.port_details_row_label, parent=row)

    def get_port_details_row_add_button(self, row):
        return self.weh.get_element(self.port_details_row_add_button, parent=row)

    def get_port_type_text_field(self):
        return self.weh.get_element(self.port_type_text_field)

    def get_port_details_vlan_ui_ip_button(self):
        return self.weh.get_element(self.port_details_vlan_ui_ip_button)

    def get_port_details_vlan_pop_up_all_entries(self):
        return self.weh.get_elements(self.port_details_vlan_pop_up_all_entries)

    def get_port_details_vlan_single_entry(self):
        return self.weh.get_element(self.port_details_vlan_pop_up_single_entry)

    def get_port_details_add_vlan_button(self):
        return self.weh.get_element(self.port_details_add_vlan_button)

    def get_port_details_vlan_name(self):
        return self.weh.get_element(self.port_details_vlan_name)

    def get_port_details_vlan_id(self):
        return self.weh.get_element(self.port_details_vlan_id)

    def get_port_details_vlan_cancel_button(self):
        return self.weh.get_element(self.port_details_vlan_cancel_button)

    def get_port_details_vlan_save_button(self):
        return self.weh.get_element(self.port_details_vlan_save_button)

    def get_port_type_cancel_button(self):
        return self.weh.get_element(self.port_type_cancel_button)

    def get_port_type_save_button(self):
        return self.weh.get_element(self.port_new_type_save_button)

    def get_switch_temp_cancel_button(self):
        return self.weh.get_element(self.switch_temp_cancel_button)

    def get_switch_temp_save_button(self):
        return self.weh.get_element(self.switch_temp_save_button)

    def get_port_details_vlan_input_obj(self):
        return self.weh.get_element(self.port_details_vlan_input_obj)

    def get_complete_stack_list(self):
        return self.weh.get_element(self.complete_stack_list)

    def get_complete_stack_all_rows(self, web_list):
        return self.weh.get_elements(self.complete_stack_all_rows, parent=web_list)

    def get_aggr_ports_across_stack_button(self):
        return self.weh.get_element(self.aggr_ports_across_stack_button)

    def get_aggr_ports_standalone_button(self):
        return self.weh.get_elements(self.aggr_ports_standalone_button)

    def poe_button(self):
        return self.weh.get_element(self.poe_status)

    def port_config_template(self):
        return self.weh.get_element(self.device_template_port_configuration)

    def all_ports_selected(self):
        return self.weh.get_element(self.select_all_ports_button)

    def assign_all_ports_selected(self):
        return self.weh.get_element(self.assign_all_ports_device_template)

    def port_type_template_create_new(self):
        return self.weh.get_element(self.port_type_template)

    def port_name(self):
        return self.weh.get_element(self.port_type_name_template)

    def port_type_save_button(self):
        return self.weh.get_element(self.save_button_port_type)

    def save_device_template(self):
        return self.weh.get_element(self.save_button_template)

    def pse_profile_user_option(self):
        return self.weh.get_element(self.pse_profile_tab)

    def pse_profile_name_tab(self):
        return self.weh.get_element(self.pse_profile_name)

    def pse_profile_power_limit(self):
        return self.weh.get_element(self.pse_power_limit)

    def priority_dropdown(self):
        return self.weh.get_element(self.priority_options)

    def low_value(self):
        return self.weh.get_elements(self.low_value_option)

    def high_value(self):
        return self.weh.get_elements(self.high_value_option)

    def critical_value(self):
        return self.weh.get_elements(self.critical_value_option)

    def get_priority_items_select_container(self):
        return self.weh.get_element(self.priority_items_select_container)

    def priority_items(self, table):
        return self.weh.get_elements(self.priority_items_select, parent=table)

    def power_mode_items(self):
        return self.weh.get_elements(self.power_mode_items_select)

    def power_mode_dropdown(self):
        return self.weh.get_element(self.power_mode_dropdown_button)

    def save_button_template_pse_profile(self):
        return self.weh.get_element(self.save_button_pse)

    def existing_port_type_button(self):
        return self.weh.get_element(self.existing_port_type)

    def port_type_list(self):
        return self.weh.get_elements(self.switch_template_port_types_list)

    def save_btn_existing_port(self):
        return self.weh.get_element(self.save_btn)

    def edit_port_button(self):
        return self.weh.get_element(self.edit_port_button_template)

    def port_list(self):
        return self.weh.get_elements(self.poe_verification_for_port_list)

    def get_sw_template_supplemental_cli_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_supplemental_cli_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_supplemental_cli_on_button(self):
        return self.weh.get_element(self.sw_template_supplemental_cli_on_button)

    def get_sw_template_supplemental_cli_name_text(self):
        return self.weh.get_element(self.sw_template_supplemental_cli_name_text)

    def get_sw_template_supplemental_cli_commands_text(self):
        return self.weh.get_element(self.sw_template_supplemental_cli_commands_text)

    def get_sw_template_scli_save_btn(self):
        elements = self.weh.get_elements(self.sw_template_scli_save_btn)
        for el in elements:
            if el.is_displayed():
                return el
        return None

    def get_mgmt_toggle_check_box(self):
        return self.weh.get_element(self.mgmt_checkbox)

    def get_mgmt_vlan_text_field(self):
        return self.weh.get_element(self.mgmt_vlan_text_field)

    def get_select_all_rows(self):
        return self.weh.get_element(self.select_all_rows)

    def get_sw_template_adv_settings_tab(self):
        return self.weh.get_element(self.sw_template_adv_settings_tab)

    def get_sw_template_adv_tab_textfield(self):
        return self.weh.get_element(self.sw_template_adv_tab_textfield)

    def get_sw_template_save_button_adv_tab(self):
        return self.weh.get_elements(self.sw_template_save_btn_adv_tab)

    def get_confirm_message_yes_button(self):
        return self.weh.get_element(self.confirm_message_yes_button)

    def get_sw_template_adv_settings_upgrade_device_text(self):
        return self.weh.get_element(self.sw_template_adv_settings_upgrade_device_text)

    def get_sw_template_adv_settings_upgrade_device_on_off_button(self):
        return self.weh.get_element(self.sw_template_adv_settings_upgrade_device_on_off_button)

    def get_sw_template_adv_settings_upload_config_text(self):
        return self.weh.get_element(self.sw_template_adv_settings_upload_config_text)

    def get_sw_template_adv_settings_upload_configuration_on_off_button(self):
        return self.weh.get_element(self.sw_template_adv_settings_upload_configuration_on_off_button)

    def get_sw_template_adv_settings_upgr_firm_latest_button(self):
        return self.weh.get_element(self.sw_template_adv_settings_upgr_firm_latest_button)

    def get_sw_template_adv_settings_upgr_firm_specific_button(self):
        return self.weh.get_element(self.sw_template_adv_settings_upgr_firm_specific_button)

    def get_sw_template_device_sett_forward_delay_drop_down(self):
        elements = self.weh.get_elements(self.sw_template_device_sett_forward_delay_drop_down)
        for el in elements:
            if el.is_displayed():
                return el

    def get_sw_template_device_sett_forward_delay_drop_down_container(self):
        elements = self.weh.get_elements(self.sw_template_device_sett_forward_delay_drop_down_container)
        for el in elements:
            if el.is_displayed():
                return el

    def get_sw_template_device_sett_forward_delay_drop_down_item16(self):
        elements = self.weh.get_elements(self.sw_template_device_sett_forward_delay_drop_down_item16)
        for el in elements:
            if el.is_displayed():
                return el

    def get_sw_template_device_sett_forward_delay_drop_down_item15(self):
        return self.weh.get_element(self.sw_template_device_sett_forward_delay_drop_down_item15)

    def get_sw_template_device_sett_forward_delay_drop_down_items(self):
        return self.weh.get_element(self.sw_template_device_sett_forward_delay_drop_down_items)

    def get_sw_template_device_sett_forward_delay_drop_down_items_container(self):
        return self.weh.get_element(self.sw_template_device_sett_forward_delay_drop_down_items_container)

    def get_sw_template_device_sett_forward_delay_drop_down_items_all_items(self, parent):
        return self.weh.get_elements(self.sw_template_device_sett_forward_delay_drop_down_items_all_items, parent=parent)

    def get_sw_template_adv_settings_download_specific_firmware_drop_down_button(self):
        return self.weh.get_elements(self.sw_template_adv_settings_download_specific_firmware_drop_down_button)

    def get_sw_template_adv_settings_download_specific_firmware_drop_down_items(self):
        return self.weh.get_elements(self.sw_template_adv_settings_download_specific_firmware_drop_down_items)

    def get_sw_template_row_cells(self, row):
        cells = self.weh.get_elements(self.sw_template_row_cells, row)
        return cells

    def get_sw_template_row_table_cells(self, row):
        cells = self.weh.get_elements(self.sw_template_row_table_cells, row)
        return cells

    def get_sw_template_row_cells_hyperlink(self, cell):
        value = self.weh.get_elements(self.sw_template_row_cells_hyperlink, cell)
        return value

    def get_sw_template_assign_choose_existing_trunk_choice_second_dialog_box(self):
        return self.weh.get_element(self.sw_template_assign_choose_existing_trunk_choice_second_dialog_box)

    def get_sw_template_check_box_row(self, row):
        return self.weh.get_elements(self.sw_template_check_box_row, parent=row)

    def get_sw_template_delete_button(self):
        return self.weh.get_element(self.sw_template_delete_button)

    def get_new_sw_template_add_button(self):
        return self.weh.get_element(self.new_sw_template_add_button)

    def get_sw_template_save_button_bottom(self):
        return self.weh.get_elements(self.sw_template_save_btn_bottom)

    def get_lacp_toggle_button(self):
        return self.weh.get_element(self.lacp_toggle_button)

    def get_lag_remove_port_button(self):
        return self.weh.get_element(self.lag_remove_port_button)

    def get_lag_add_port_button(self):
        return self.weh.get_element(self.lag_add_port_button)

    def get_select_ports_available(self):
        return self.weh.get_elements(self.select_ports_available)

    def get_cancel_button(self):
        return self.weh.get_element(self.cancel_button)

    def get_save_port_type_button(self):
        return self.weh.get_element(self.save_port_type_button)

    def get_switch_temp_save_button_v2(self):
        return self.weh.get_element(self.switch_temp_save_button_v2)

    def get_lag_span(self, lag):
        elements = self.weh.get_template_elements(self.lag_span, lag=lag)
        if elements:
            for el in elements:
                if el.is_displayed():
                    return el

    def get_available_port(self, port):
        return self.weh.get_template_element(self.available_port, port=port)

    def get_selected_port(self, port):
        return self.weh.get_template_element(self.selected_port, port=port)

    def get_port_settings_tab(self):
        return self.weh.get_element(self.port_settings_tab)

    def get_available_slot(self, slot):
        return self.weh.get_template_element(self.available_slot, slot=slot)

    def get_error_message(self):
        return self.weh.get_template_element(self.error_message)

    def get_template_link(self, template):
        return self.weh.get_template_element(self.template_link, template=template)

    def get_sw_template_stp_tab(self):
        return self.weh.get_element(self.sw_template_stp_tab)

    def get_sw_template_port_details_tab(self):
        return self.weh.get_element(self.sw_template_port_details_tab)

    def get_sw_template_stp_port_rows(self):
        return self.weh.get_elements(self.sw_template_stp_port_rows)

    def get_sw_template_path_cost_row(self, row):
        return self.weh.get_element(self.sw_template_path_cost_row, parent=row)

    def get_template_slot(self, slot):
        return self.weh.get_template_element(self.template_slot, slot=slot)

    def get_aggregated_ports(self):
        return self.weh.get_template_element(self.aggregated_ports)

    def get_port_in_agg(self):
        return self.weh.get_template_elements(self.port_in_agg)

    def get_sw_template_hyperlink(self):
        return self.weh.get_element(self.sw_template_hyperlink)

    def get_sw_template_enable_mac_locking(self):
        return self.weh.get_element(self.sw_template_enable_mac_locking)

    def get_sw_template_enable_mac_locking_confirm_message_yes_button(self):
        return self.weh.get_element(self.sw_template_enable_mac_locking_confirm_message_yes_button)

    def get_sw_template_auto_cfg(self):
        return self.weh.get_element(self.sw_template_auto_cfg)

    def get_sw_template_auto_revert_enabled(self):
        return self.weh.get_element(self.sw_template_auto_revert_enabled)

    def get_sw_template_auto_revert_msg(self):
        return self.weh.get_element(self.sw_template_auto_revert_msg)

    def get_sw_template_notification_yes_btn(self):
        return self.weh.get_element(self.sw_template_notification_yes_btn)

    def get_sw_template_assign_existing_trunk_choice_second_dialog_box_save_button(self):
        return self.weh.get_element(self.sw_template_assign_existing_trunk_choice_second_dialog_box_save_button)

    def get_sw_template_error_message(self):
        rez = []
        elements = self.weh.get_elements(self.pse_error_message)
        for el in elements:
            if el.is_displayed():
                rez.append(el)
        if len(rez) != 0:
            return rez
        return None

    def get_sw_template_port_details_interface_all_rows(self):
        return self.weh.get_elements(self.sw_template_port_details_interface_all_rows)

    def get_sw_template_port_details_row_combo(self, parent):
        return self.weh.get_elements(self.sw_template_port_details_row_combo, parent)

    def get_sw_template_port_details_row_interface_value(self, parent):
        return self.weh.get_element(self.sw_template_port_details_row_interface_value, parent)

    def get_sw_template_port_details_combo_list(self, parent):
        return self.weh.get_elements(self.sw_template_port_details_combo_list, parent)

    def get_sw_template_port_details_row_port_type_list(self):
        return self.weh.get_elements(self.sw_template_port_details_row_port_type_list)

    def get_sw_template_port_details_port_type_editor_name(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_name)

    def get_sw_template_port_details_port_type_editor_description(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_description)

    def get_sw_template_port_details_port_type_editor_status(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_status)

    def get_sw_template_port_details_port_type_editor_auto_sense_status(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_auto_sense_status)

    def get_sw_template_port_details_port_type_editor_access(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_access)

    def get_sw_template_port_details_port_type_editor_trunk(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_trunk)

    def get_sw_template_port_details_port_type_editor_cancel(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_cancel)

    def get_sw_template_port_details_port_type_editor_previous(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_previous)

    def get_sw_template_port_details_port_type_editor_next(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_next)

    def get_sw_template_port_details_port_type_editor_save(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_save)

    def get_sw_template_port_details_port_type_editor_duplex_arrow(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_duplex_arrow)

    def get_sw_template_port_details_port_type_editor_duplex_option(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_options)

    def get_sw_template_port_details_port_type_editor_speed_arrow(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_speed_arrow)

    def get_sw_template_port_details_port_type_editor_speed_option(self, parent):
        return self.weh.get_element(self.sw_template_port_details_port_type_options, parent)

    def get_sw_template_port_details_port_type_editor_client_reporting(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_client_reporting)

    def get_sw_template_port_details_port_type_editor_cdp_receive(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_cdp_receive)

    def get_sw_template_port_details_port_type_editor_lldp_transmit(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_lldp_transmit)

    def get_sw_template_port_details_port_type_editor_lldp_receive(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_lldp_receive)

    def get_sw_template_port_details_port_type_editor_sc_broadcast(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_sc_broadcast)

    def get_sw_template_port_details_port_type_editor_sc_unicast(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_sc_unicast)

    def get_sw_template_port_details_port_type_editor_sc_multicast(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_sc_multicast)

    def get_sw_template_port_details_port_type_editor_sc_threshold(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_sc_threshold)

    def get_sw_template_port_details_port_type_editor_sc_rate_limit_type(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_sc_rate_limit_type)

    def get_sw_template_port_details_port_type_editor_sc_rate_limit_value(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_sc_rate_limit_value)

    def get_device_switch_select_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_switch_select_button)

    def get_sw_template_port_details_port_type_editor_port_name_and_usage_tab(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_port_name_and_usage_tab)

    def get_sw_template_port_details_port_type_editor_transmission_tab(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_transmission_tab)

    def get_sw_template_port_details_port_type_editor_storm_control_tab(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_storm_control_tab)

    def get_sw_template_port_details_port_type_editor_summary_tab(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_summary_tab)

    def get_sw_template_port_details_port_type_editor_vlan_tab(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_vlan_tab)

    def get_sw_template_port_details_port_type_editor_stp_tab(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_stp_tab)

    def get_switch_template_device_configuration_igmp_settings(self):
        return self.weh.get_element(self.switch_template_device_configuration_igmp_settings)

    def get_switch_template_device_configuration_igmp_immediate_leave(self):
        return self.weh.get_element(self.switch_template_device_configuration_igmp_immediate_leave)

    def get_switch_template_device_configuration_igmp_suppress_independent(self):
        return self.weh.get_element(self.switch_template_device_configuration_igmp_suppress_independent)

    def get_switch_template_device_configuration_mtu_1522(self):
        return self.weh.get_element(self.switch_template_device_configuration_mtu_1522)

    def get_switch_template_device_configuration_mtu_1950(self):
        return self.weh.get_element(self.switch_template_device_configuration_mtu_1950)

    def get_switch_template_device_configuration_mtu_9600(self):
        return self.weh.get_element(self.switch_template_device_configuration_mtu_9600)

    def get_switch_template_device_configuration_pse_enable(self):
        return self.weh.get_element(self.switch_template_device_configuration_pse_enable)

    def get_switch_template_device_configuration_pse_budget(self):
        return self.weh.get_element(self.switch_template_device_configuration_pse_budget)

    def get_sw_template_port_details_port_type_editor_spanning_tree_stp_enable(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_spanning_tree_stp_enable)

    def get_sw_template_port_details_port_type_editor_spanning_tree_edge_port_enable(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_spanning_tree_edge_port_enable)

    def get_sw_template_port_details_port_type_editor_spanning_tree_path_cost(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_spanning_tree_path_cost)

    def get_sw_template_port_details_port_type_editor_spanning_tree_bdu_protection(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_spanning_tree_bdu_protection)

    def get_sw_template_port_details_port_type_editor_spanning_tree_priority(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_spanning_tree_priority)

    def get_sw_template_port_details_port_type_editor_vlan_native_vlan(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_vlan_native_vlan)

    def get_sw_template_port_details_port_type_editor_vlan_add_button(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_vlan_add_button)

    def get_sw_template_port_details_port_type_editor_vlan_allowed_vlans(self):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_vlan_allowed_vlans)

    def get_sw_template_port_details_port_type_editor_duplex_options_container(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_duplex_options_container)

    def get_sw_template_port_details_port_type_editor_duplex_arrow_options(self, table):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_duplex_arrow_options, parent=table)

    def get_sw_template_port_details_port_type_editor_speed_options_container(self):
        return self.weh.get_element(self.sw_template_port_details_port_type_editor_speed_options_container)

    def get_sw_template_port_details_port_type_editor_speed_arrow_options(self, table):
        return self.weh.get_elements(self.sw_template_port_details_port_type_editor_speed_arrow_options, parent=table)

    def get_sw_template_device_max_age_drop_down_items(self):
        return self.weh.get_element(self.sw_template_device_max_age_drop_down_items)

    def get_sw_template_device_max_age_delay_items_container(self):
        return self.weh.get_element(self.sw_template_device_max_age_delay_items_container)

    def get_sw_template_device_max_age_drop_down_all_items(self, table):
        return self.weh.get_elements(self.sw_template_device_max_age_drop_down_all_items, parent=table)

    def get_device_template_no_of_ports(self):
        return self.weh.get_elements(self.device_template_no_of_ports)

    def get_device_template_override_policy(self):
        return self.weh.get_element(self.device_template_override_policy)

    def get_sw_template_enable_mac_locking_confirm_message(self):
        return self.weh.get_element(self.sw_template_enable_mac_locking_confirm_message)