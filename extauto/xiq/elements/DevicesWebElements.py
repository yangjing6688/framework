import time
from extauto.xiq.defs.DevicesWebElementsDefinitions import DevicesWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class DevicesWebElements(DevicesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_grid(self):
        """
        :return: devices grid's handler
        """
        return self.weh.get_element(self.devices_page_grid_ids)

    def get_grid_rows(self):
        """
        :return: all the rows in the devices grid
        """
        grid_rows = self.weh.get_elements(self.devices_page_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_grid_rows_next(self):
        grid_rows = self.weh.get_elements(self.devices_page_grid_rows_next)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_page_numbers(self):
        return self.weh.get_elements(self.devices_page_numbers)

    def get_devices_page_number_one(self):
        return self.weh.get_element(self.devices_page_number_one)

    def get_refresh_devices_page(self):
        refresh_icon = self.weh.get_element(self.refresh_devices_page)
        return refresh_icon

    def get_grid_cells(self):
        """
        :return: all the cells in the devices grid
        """
        grid_cells = self.weh.get_elements(self.devices_page_grid_cells)
        if grid_cells:
            return grid_cells
        else:
            return False

    def get_status_cell(self, row):
        el = self.weh.get_element(self.device_status_cell, parent=row)
        if el:
            return el.get_attribute("class")
        else:
            return None

    def get_stack_status_cell(self, row):
        el = self.weh.get_element(self.device_stack_status, row)
        if el:
            return el.get_attribute("class")
        else:
            return None

    def get_stack_status_cell_icon(self, row):
        blue = self.weh.get_element(self.device_stack_status, row)
        red = self.weh.get_element(self.device_stack_status_warning, row)
        if blue:
            return blue.get_attribute("class")
        elif red:
            return red.get_attribute("Class")
        else:
            return None

    def get_stack_status_icon(self, row):
        return self.weh.get_element(self.device_stack_status, row)

    def get_device_config_audit(self, row):
        el = self.weh.get_element(self.device_config_audit, parent=row)
        if el:
            return el.get_attribute("class")
        else:
            return None

    def get_device_config_audit_button(self, row):
        return self.weh.get_element(self.device_config_audit, row)

    def get_device_conn_status_after_ten_min(self, row):
        return self.weh.get_element(self.device_conn_status_after_ten_min, row)

    def get_devices_add_button(self):
        """
        :return: device add button
        """
        return self.weh.get_element(self.devices_add_button)

    def get_devices_quick_add_menu_item(self):
        """
        :return: device quick add menu item
        """
        menus = self.weh.get_elements(self.devices_add_menu)
        for menu in menus:
            if menu.is_displayed():
                return self.weh.get_element(self.devices_quick_add_menu_item, parent=menu)

    def get_devices_serial_text_area(self):
        """
        :return: device on-boarding text area where we can enter device serial numbers
        """
        return self.weh.get_element(self.devices_serial_text_area)

    def get_devices_add_devices_button(self):
        """
        :return: device on-boarding add button
        """
        return self.weh.get_element(self.devices_add_devices_button)

    def get_devices_drawer_open(self):
        return self.weh.get_element(self.devices_drawer_open)

    def get_devices_drawer_trigger(self):
        return self.weh.get_element(self.devices_drawer_trigger)

    def get_delete_button(self):
        """
        :return: device delete button
        """
        return self.weh.get_element(self.device_delete_button)

    def get_download_button(self):
        """
        :return: device download button
        """
        return self.weh.get_element(self.device_download_button)

    def get_bulk_edit_button(self):
        """
        :return: device bulk edit button
        """
        return self.weh.get_element(self.device_bulk_edit_button)

    def get_action_button(self):
        """
        :return: device action button
        """
        return self.weh.get_element(self.device_action_button)

    def get_os_change_error_message(self):
        """
        :return error message
        """
        return self.weh.get_element(self.device_os_change_error_message)

    def get_device_update_error_message(self):
        """
        :return error message
        """
        return self.weh.get_element(self.device_update_error_message)

    def get_device_delete_confirm_ok_button(self):
        """
        :return: device delete button triggers confirmation dialog
                this method returns the "Yes" button's handle
        """
        return self.weh.get_element(self.device_delete_confirm_ok_button)

    def get_ap_select_checkbox(self, row):
        """
        :return: device select checkbox
        """
        return self.weh.get_element(self.device_select_check_box, parent=row)

    def get_ap_name_cell(self):
        return self.weh.get_element(self.devices_page_grid_cells)

    def get_devices_page_grid_ap_name_href(self, ap_name):
        ap_cells = self.weh.get_elements(self.devices_page_grid_ap_name_cells)
        for ap_cell in ap_cells:
            if ap_name in ap_cell.text:
                return self.weh.get_a_href(ap_cell)

    def get_device_details_wireless_interfaces(self):
        return self.weh.get_element(self.device_details_wireless_interfaces)

    def get_device_details_wireless_interfaces_surrounding_aps_grid(self):
        return self.weh.get_element(self.device_details_wireless_interfaces_surrounding_aps_grid)

    def get_device_row_cells(self, row):
        """
        :return: device row cell elements
        """
        return self.weh.get_elements(self.device_row_celss, row)

    def get_device_details_refresh_button(self):
        return self.weh.get_elements(self.device_details_refresh_button)

    def get_update_device_button(self):
        return self.weh.get_element(self.update_devices_button)

    def get_delta_config_update_button(self):
        return self.weh.get_element(self.update_config_delta_radio_button)

    def get_full_config_update_button(self):
        return self.weh.get_element(self.update_devices_full_radio_button)

    def get_perform_update_button(self):
        return self.weh.get_element(self.devices_perform_update_button)

    def get_devices_config_update_message(self):
        return self.weh.get_element(self.devices_config_update_message)

    def get_adv_onboard_serial_text_area(self):
        return self.weh.get_element(self.device_adv_onboard_serial_text_area)

    def get_adv_onboard_next_button(self):
        return self.weh.get_element(self.device_adv_onboard_next_button)

    def get_adv_onboard_finish_button(self):
        return self.weh.get_element(self.device_adv_onboard_finish_button)

    def get_adv_onboard_add_menu_item(self):
        """
        :return: device quick add menu item
        """
        menus = self.weh.get_elements(self.devices_add_menu)
        for menu in menus:
            if menu.is_displayed():
                menu_items = self.weh.get_elements(self.devices_quick_add_menu_item, parent=menu)
                for menu_item in menu_items:
                    if "Advanced Onboarding" in menu_item.text:
                        return menu_item

    def get_device_type_dropdown(self):
        weh = self.weh.get_element(self.device_type_dropdown)
        if weh is None:
            return self.weh.get_element(self.device_type_dropdown2)
        return weh

    def get_quick_onboard_simulated(self):
        return self.weh.get_element(self.quick_onboard_simulated)

    def get_device_filter_button(self):
        return self.weh.get_element(self.device_filter_button)

    def get_device_filter_select_all_checkbox(self):
        return self.weh.get_element(self.device_filter_select_all_checkbox)

    def get_simulated_devices_dropdown(self):
        return self.weh.get_element(self.simulated_device_dropdown)

    def get_simulated_device_dropdown_table(self):
        return self.weh.get_element(self.simulated_device_dropdown_table)

    def get_simulated_device_dropdown_table_rows(self, table):
        return self.weh.get_elements(self.simulated_device_dropdown_table_rows, table)

    def get_simulated_devices_dropdown_items(self):
        parent = self.get_simulated_devices_dropdown()
        return self.weh.get_elements(self.simulated_device_dropdown_items, parent)

    def get_simulation_device_count_input_field(self):
        return self.weh.get_element(self.simulation_device_count_input_field)

    def get_add_another_device(self):
        return self.weh.get_element(self.add_another_device)

    def get_simulated_device_dropdown_options(self):
        return self.weh.get_elements(self.simulated_device_dropdown_options)

    def get_simulated_devices_grid_rows(self):
        sim_rows = []
        rows = self.get_grid_rows()
        for row in rows:
            if "SIM" in row.text:
                sim_rows.append(row)
        return sim_rows

    def get_manage_device_actions_button(self):
        return self.weh.get_element(self.manage_device_actions_button)

    def get_manage_device_actions_change_management_status(self):
        return self.weh.get_element(self.manage_device_actions_change_management_status)

    def get_manage_device_actions_change_management_status_manage(self):
        return self.weh.get_element(self.manage_device_actions_change_management_status_manage)

    def get_manage_device_actions_change_management_status_unmanage(self):
        return self.weh.get_element(self.manage_device_actions_change_management_status_unmanage)

    def get_manage_device_actions_change_management_status_yes_button(self):
        return self.weh.get_element(self.manage_device_actions_change_management_status_yes_button)

    def get_manage_device_actions_change_management_status_no_button(self):
        return self.weh.get_element(self.manage_device_actions_change_management_status_no_button)

    def get_manage_device_actions_change_management_status_close_dialog(self):
        return self.weh.get_element(self.manage_device_actions_change_management_status_close_dialog)

    def get_manage_device_utilities_button(self):
        return self.weh.get_element(self.manage_device_utilities_button)

    def get_manage_device_utilities_wan_access(self):
        return self.weh.get_element(self.manage_device_utilities_wan_access())

    def get_actions_assign_network_policy_combo(self):
        elements = self.weh.get_elements(self.actions_assign_network_policy)
        return self.get_dislayed_element(elements)

    def get_action_assign_network_policy_dialog(self):
        return self.weh.get_element(self.action_assign_network_policy_dialog)

    def get_action_assign_network_policy_dialog_cancel_button(self):
        return self.weh.get_element(self.action_assign_network_policy_dialog_cancel_button)

    def get_nw_policy_drop(self):
        return self.weh.get_element(self.nw_policy_drop)

    def get_actions_assign_network_policy_drop_down(self):
        dialog = self.get_action_assign_network_policy_dialog()
        return self.weh.get_element(self.actions_assign_network_policy_drop_down, parent=dialog)

    def get_actions_assign_network_policy_drop_down2(self):
        dialog = self.get_action_assign_network_policy_dialog()
        return self.weh.get_element(self.actions_assign_network_policy_drop_down2, parent=dialog)

    def get_actions_assign_network_policy_drop_down_router(self):
        dialog = self.get_action_assign_network_policy_dialog()
        return self.weh.get_element(self.actions_assign_network_policy_drop_down_router, parent=dialog)

    def get_actions_network_policy_drop_down_items(self):
        return self.weh.get_elements(self.actions_network_policy_drop_down_items)

    def get_actions_network_policy_assign_button(self):
        return self.weh.get_element(self.actions_network_policy_assign_button)

    def get_ui_banner_error_message(self):
        return self.weh.get_element(self.ui_banner_error_message)

    def get_ui_banner_error_close_button(self):
        return self.weh.get_element(self.ui_banner_error_close_button)

    def get_ui_banner_warning_message(self):
        return self.weh.get_element(self.ui_banner_warning_message)

    def get_ui_banner_warning_close_button(self):
        return self.weh.get_element(self.ui_banner_warning_close_button)

    def get_ui_banner_notice_message(self):
        return self.weh.get_element(self.ui_banner_notice_message)

    def get_ui_banner_notice_close_button(self):
        return self.weh.get_element(self.ui_banner_notice_close_button)

    def get_actions_network_policy_assign_cancel_button(self):
        return self.weh.get_element(self.actions_network_policy_assign_cancel_button)

    def get_country_code_cell(self, row):
        return self.weh.get_element(self.country_code_cell, row)

    def get_hostname_code_cell(self, row):
        return self.weh.get_element(self.devices_page_grid_ap_name_cells, row)

    def get_actions_country_code_menu_item(self):
        return self.weh.get_element(self.actions_country_code_menu_item)

    def get_actions_country_code_dialog(self):
        return self.weh.get_element(self.actions_country_code_dialog)

    def get_actions_country_code_dropdown(self):
        return self.weh.get_element(self.actions_country_code_dropdown)

    def get_actions_country_code_dropdown_option(self, country):
        dropdown = self.get_actions_country_code_dropdown()
        options = self.weh.get_elements(self.actions_country_code_dropdown_option, parent=dropdown)
        for option in options:
            if country in option.text:
                return option

    def get_actions_country_code_save_button(self):
        return self.weh.get_element(self.actions_country_code_save_button)

    def get_actions_country_code_error_message(self):
        try:
            dialog = self.get_actions_country_code_dialog()
            return self.weh.get_element(self.actions_country_code_error_message, parent=dialog).text
        except AttributeError:
            return False

    def get_actions_country_code_close_button(self):
        dialog = self.get_actions_country_code_dialog()
        return self.weh.get_element(self.actions_country_code_close_button, parent=dialog)

    def get_actions_country_code_confirm_button(self):
        return self.weh.get_element(self.actions_country_code_confirm_button)

    def get_device_configure_tab(self):
        return self.weh.get_element(self.device_level_configure_tab)

    def get_device_configure_interface_settings(self):
        return self.weh.get_element(self.device_level_configure_interface_settings)

    def get_device_configure_interface_settings_wireless_toggle(self):
        return self.weh.get_element(self.device_level_configure_interface_settings_wireless_toggle)

    def get_device_configure_interface_settings_wifi0_ssid(self):
        return self.weh.get_elements(self.device_level_configure_interface_settings_wifi0_ssid)

    def get_device_configure_interface_settings_wifi1_ssid(self):
        return self.weh.get_elements(self.device_level_configure_interface_settings_wifi1_ssid)

    def get_device_level_page_refresh(self):
        return self.weh.get_element(self.device_level_page_refresh)

    def get_device_level_page_close_icon(self):
        return self.weh.get_element(self.device_level_page_close_icon)

    def get_ap_device_config_tab(self):
        return self.weh.get_element(self.ap_device_config_tab)

    def get_ap_description_button1(self):
        ap_desc_btn = self.weh.get_element(self.ap_description_button)
        if ap_desc_btn.is_displayed():
            return self.weh.get_element(self.ap_description_button)

    def get_ap_description_button(self):
        elements = self.weh.get_elements(self.ap_description_button)
        return self.get_dislayed_element(elements)

    def get_dislayed_element(self, elements):
        for el in elements:
            if el.is_displayed():
                return el

    def get_save_device_config(self):
        return self.weh.get_element(self.save_device_config)

    def get_edit_button(self):
        return self.weh.get_element(self.device_edit_button)

    def get_actions_network_policy_close_button(self):
        return self.weh.get_element(self.assign_policy_close_btn)

    def get_actions_network_policy_close_button_md(self):
        return self.weh.get_elements(self.assign_policy_close_btn)

    def get_device_select_checkbox(self, row):
        return self.weh.get_element(self.device_select_check_box, parent=row)

    def get_advanced_onboard_simulated_button(self):
        return self.weh.get_element(self.adv_onboard_simulated_button)

    def get_adv_simulated_devices_dropdown(self):
        return self.weh.get_element(self.adv_simulated_device_dropdown)

    def get_actions_assign_network_policy_router_combo(self):
        return self.weh.get_element(self.actions_assign_network_policy_to_router)

    def get_updated_status_cell(self, row):
        return self.weh.get_element(self.devices_ap_updated_status_cell, row)

    def get_column_picker_icon(self):
        return self.weh.get_element(self.column_picker_icon)

    def get_column_picker_row(self):
        return self.weh.get_elements(self.column_picker_row)

    def get_column_picker_row_input(self):
        return self.weh.get_elements(self.column_picker_row_input)

    def get_country_code_column_header(self):
        return self.weh.get_element(self.country_code_column_header)

    def get_network_policy_column_header(self):
        return self.weh.get_element(self.network_policy_column_header)

    def get_device_actions_reboot_button(self):
        # The identifier differs depending on which type of device is selected,
        # so need to get all and select the displayed element
        elements = self.weh.get_elements(self.device_actions_reboot_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device_actions_reboot_confirm_bttn(self):
        return self.weh.get_element(self.device_actions_reboot_confirm_bttn)

    def get_manage_device_search_field(self):
        return self.weh.get_element(self.manage_device_search_field)

    def get_devices_column_header_cell(self, field):
        field_def = {'XPATH': '//th[contains(@class, "' + field + '")]',
                     'wait_for': 10}
        return self.weh.get_element(field_def)

    def get_device_column_header_sorting_attr(self, field):
        field_def = {'XPATH': '//th[contains(@class, "' + field + '")]/div[contains(@class, "dgrid-resize-header-container")]',
                     'wait_for': 10}
        return self.weh.get_element(field_def).get_attribute('class')

    def get_device_grid_column7(self):
        return self.weh.get_element(self.device_grid_column7)

    def get_manage_devices_select_all_devices_checkbox(self):
        return self.weh.get_element(self.manage_devices_select_all_devices_checkbox)

    def get_devices_quick_add_device_make_dropdown(self):
        return self.weh.get_element(self.devices_quick_add_device_make_dropdown)

    def get_devices_quick_add_device_make_controllers(self):
        return self.weh.get_element(self.devices_quick_add_device_make_controllers)

    def get_wing_devices_serial_text_area(self):
        return self.weh.get_element(self.wing_devices_serial_text_area)

    def get_wing_devices_mac_text_area(self):
        return self.weh.get_element(self.wing_devices_mac_text_area)

    def get_switch_update_policy_and_config_check_button(self):
        return self.weh.get_element(self.update_policy_and_config)

    def get_switch_upgrade_engine_and_images_check_button(self):
        return self.weh.get_element(self.upgrade_engine_and_images)

    def get_switch_update_reboot_and_revert_warning_dialog(self):
        return self.weh.get_element(self.reboot_and_revert_warning_dialog)

    def get_switch_update_reboot_and_revert_warning_dialog_yes_button(self):
        return self.weh.get_element(self.reboot_and_revert_warning_dialog_yes_button)

    def get_device_update_close_button(self):
        return self.weh.get_element(self.device_update_close_button)

    def get_actions_assign_network_policy_combo_switch(self):
        elements = self.weh.get_elements(self.actions_assign_network_policy_switch)
        return self.get_dislayed_element(elements)

    def get_devices_exos_serial_text_area(self):
        """
        :return: device on-boarding text area to enter device serial numbers for EXOS devices
        """
        return self.weh.get_element(self.devices_exos_serial_text_area)

    def get_devices_voss_serial_text_area(self):
        """
        :return: device on-boarding text area to enter device serial numbers for VOSS devices
        """
        return self.weh.get_element(self.devices_voss_serial_text_area)

    def get_devices_xiqse_serial_text_area(self):
        """
        :return: device on-boarding text area to enter serial numbers for XIQ Site Engines
        """
        return self.weh.get_element(self.devices_xiqse_serial_text_area)

    def get_devices_quick_add_device_panel(self):
        """
        :return: quick add device panel
        """
        return self.weh.get_element(self.devices_quick_add_device_panel)

    def get_devices_quick_add_device_make_drop_down(self):
        """
        :return: quick add device make drop down to select the make of device (aerohive, voss, etc.)
        """
        return self.weh.get_element(self.devices_quick_add_device_make_drop_down)

    def get_devices_advanced_add_device_make_drop_down(self):
        """
        :return: advanced add device make drop down to select the make of device (aerohive, voss, etc.)
        """
        return self.weh.get_element(self.devices_advanced_add_device_make_drop_down)

    def get_devices_quick_add_block_show(self):
        return self.weh.get_element(self.devices_quick_add_block_show)

    def get_devices_quick_add_device_make_aerohive_choice(self):
        """
        :return: quick add device make drop down Extreme - Aerohive selection
        """
        return self.weh.get_element(self.devices_quick_add_device_make_aerohive_choice)

    def get_devices_quick_add_device_make_exos_choice(self):
        """
        :return: quick add device make drop down EXOS selection
        """
        return self.weh.get_element(self.devices_quick_add_device_make_exos_choice)

    def get_devices_quick_add_device_make_voss_choice(self):
        """
        :return: quick add device make drop down VOSS selection
        """
        return self.weh.get_element(self.devices_quick_add_device_make_voss_choice)

    def get_devices_advanced_add_device_make_voss_choice(self):
        """
        :return: advanced add device make drop down selection
        """
        return self.weh.get_element(self.devices_advanced_add_device_make_voss_choice)

    def get_devices_quick_add_device_make_xmc_choice(self):
        """
        :return: quick add device make drop down XMC selection
        """
        return self.weh.get_element(self.devices_quick_add_device_make_xmc_choice)

    def get_devices_quick_add_location_field(self):
        """
        :return: quick add location field
        """
        return self.weh.get_element(self.devices_quick_add_location_field)

    def get_devices_quick_add_policy_drop_down(self):
        """
        :return: quick add policy drop down to select the policy to assign
        """
        return self.weh.get_element(self.devices_quick_add_policy_drop_down)

    def get_devices_quick_add_policy_drop_down_items(self):
        """
        :return: quick add policy drop down item
        """
        parent = self.get_devices_quick_add_policy_drop_down()
        return self.weh.get_elements(self.devices_quick_add_policy_drop_down_items, parent)

    def get_devices_add_devices_cancel_button(self):
        """
        :return: quick add device cancel button
        """
        return self.weh.get_element(self.devices_add_devices_cancel_button)

    def get_cell_href(self, cell):
        return self.weh.get_element(self.device360_cells_href, parent=cell)

    def get_device_type_drop_down(self):
        """
        :return:
        """
        return self.weh.get_element(self.device_type_drop_down)

    def get_device_type_drop_down_options(self):
        """
        :return:
        """
        return self.weh.get_elements(self.device_type_drop_down_options)

    def get_device_make_drop_down(self):
        """
        :return:
        """
        return self.weh.get_element(self.device_make_drop_down)

    def get_device_make_drop_down_options(self):
        """
        :return:
        """
        return self.weh.get_elements(self.device_make_drop_down_options)

    def get_device_entry_type_drop_down(self):
        """
        :return:
        """
        return self.weh.get_element(self.device_entry_type_drop_down)

    def get_device_entry_type_drop_down_options(self):
        """
        :return:
        """
        return self.weh.get_elements(self.device_entry_type_drop_down_options)

    def get_device_entry_csv_upload_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.device_entry_csv_upload_button)

    def get_device_entry_voss_csv_upload_button(self):
        """
        :return:  CSV upload file input element related to the VOSS device
        """
        return self.weh.get_element(self.device_entry_voss_csv_upload_button)

    def get_device_entry_exos_csv_upload_button_advanced_onboard(self):
        """
        :return:  CSV upload file input element related to the advanced onboard        """
        return self.weh.get_element(self.device_entry_exos_csv_upload_button_advanced_onboard)

    def get_devices_table_view_type_drop_down(self):
        """
        :return: view type drop down for the devices table
        """
        return self.weh.get_element(self.devices_table_view_type_drop_down)

    def get_devices_table_view_type_drop_down_items(self):
        """
        :return: view type drop down items for the devices table view type selector drop down
        """
        parent = self.get_devices_table_view_type_drop_down()
        return self.weh.get_elements(self.devices_table_view_type_drop_down_items, parent)

    def get_devices_switch_assign_policy(self):
        return self.weh.get_element(self.devices_switch_assign_policy)

    def get_devices_switch_assign_policy_dropdown(self):
        return self.weh.get_element(self.devices_switch_assign_policy_dropdown)

    def get_devices_switch_assign_policy_list(self):
        return self.weh.get_elements(self.devices_switch_assign_policy_list)

    def get_devices_switch_assign_policy_assign_btn(self):
        return self.weh.get_element(self.devices_switch_assign_policy_assign_btn)

    def get_devices_switch_update_nw_policy(self):
        return self.weh.get_element(self.devices_switch_update_nw_policy)

    def get_devices_switch_update_btn(self):
        return self.weh.get_element(self.devices_switch_update_btn)

    def get_all_device_rows(self):
        """
        :return: all the rows in the devices grid
        """
        return self.weh.get_elements(self.devices_page_grid_rows_all)

    def get_selected_device_rows(self):
        """
        :return: all the rows in the devices grid which are selected
        """
        return self.weh.get_elements(self.devices_page_grid_rows_selected)

    def get_deselected_device_rows(self):
        """
        :return: all the rows in the devices grid which are not selected
        """
        return self.weh.get_elements(self.devices_page_grid_rows_deselected)

    def get_manage_devices_select_all_devices_checkbox_selected(self):
        """
        :return: True if the checkbox for selecting all device rows is selected, False if not
        """
        element = self.weh.get_element(self.manage_devices_select_all_devices_checkbox_selected)
        if element:
            return True
        else:
            return False

    def get_manage_devices_select_all_devices_checkbox_deselected(self):
        """
        :return: True if the checkbox for selecting all device rows is not selected, False if selected
        """
        element = self.weh.get_element(self.manage_devices_select_all_devices_checkbox_deselected)
        if element:
            return True
        else:
            return False

    def get_device_row_selection_checkbox_selected(self, row):
        """
        :return: True if the checkbox for the specified device row is selected, False if not
        """
        element = self.weh.get_element(self.device_row_selection_checkbox_selected, row)
        if element:
            return True
        else:
            return False

    def get_device_row_selection_checkbox_deselected(self, row):
        """
        :return: True if the checkbox for the specified device row is not selected, False if selected
        """
        element = self.weh.get_element(self.device_row_selection_checkbox_deselected, row)
        if element:
            return True
        else:
            return False

    def get_last_refreshed_tooltip(self):
        """
        :return: Returns the "Last Refreshed at" tooltip
        """
        return self.weh.get_element(self.last_refreshed_tooltip)

    def get_total_count_label(self):
        """
        :return: returns the total count label for the grid
        """
        return self.weh.get_element(self.total_count_label)

    def get_devices_display_count_per_page_selection_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.devices_display_count_per_page_selection_button)

    def get_devices_pagination_next_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.devices_pagination_next_button)

    def get_devices_display_count_per_page_buttons(self):
        """
        :return:
        """
        return self.weh.get_element(self.devices_display_count_per_page_buttons)

    def get_devices_pagination_buttons(self):
        """
        :return:
        """
        return self.weh.get_element(self.devices_pagination_buttons)

    def get_manage_device_search_clear_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.manage_device_search_clear_button)

    def get_device_entry_exos_csv_upload_button(self):
        """
        :return:  CSV upload file input element related to the EXOS device
        """
        return self.weh.get_element(self.device_entry_exos_csv_upload_button)

    def get_devices_page_stack_slot_rows(self, row):
        return self.weh.get_elements(self.devices_page_stack_slot_rows, parent=row)

    def get_devices_stack_update_policy_dropdown_btn(self):
        return self.weh.get_element(self.devices_stack_update_policy_dropdown_btn)

    def get_devices_stack_update_policy_dropdown_items(self):
        return self.weh.get_elements(self.devices_stack_update_policy_dropdown_items)

    def get_device_stack_toggle(self, row):
        el = self.weh.get_element(self.device_stack_toggle, row)
        if el:
            return el.get_attribute("class")
        else:
            return None

    def get_devices_close_button_update(self):
        return self.weh.get_element(self.devices_close_button_update)

    def get_devices_perform_update_button_d360(self):
        return self.weh.get_element(self.devices_perform_update_button_d360)

    def get_actions_open_site_engine_menu_option(self):
        return self.weh.get_element(self.actions_open_site_engine_menu_option)

    def get_devices_service_tag_textbox(self):
        return self.weh.get_element(self.device_service_tag_textbox)

    def get_devices_quick_add_devices_menu_item(self):
        return self.weh.get_element(self.devices_quick_add_devices_menu_item)

        # jefjones - removed for now
        menus = self.weh.get_elements(self.devices_add_devices_menu)
        for menu in menus:
            if menu.is_displayed():
                menu_items = self.weh.get_elements(self.devices_quick_add_devices_menu_item, parent=menu)
                for menu_item in menu_items:
                    if "Quick Add Devices" in menu_item.text:
                        return menu_item

    def get_deploy_devices_to_cloud_menu_item(self):
        return self.weh.get_element(self.deploy_devices_to_cloud_menu_item)

    def get_device_type_real_radio_button(self):
        return self.weh.get_element(self.device_type_real_radio_button)

    def get_entry_type_manual_radio_button(self):
        return self.weh.get_element(self.entry_type_manual_radio_button)

    def get_entry_type_csv_radio_button(self):
        return self.weh.get_element(self.entry_type_csv_radio_button)

    def get_device_make_dropdownoption(self):
        return self.weh.get_element(self.device_make_dropdownoption)

    def get_device_os_radio(self):
        return self.weh.get_element(self.device_os_radio)

    def get_devices_quick_add_device_os_radio(self):
        return self.weh.get_element(self.devices_quick_add_device_os_radio)

    def get_location_button(self):
        return self.weh.get_element(self.location_button)

    def get_location_select_button(self):
        return self.weh.get_element(self.location_select_button)

    def get_devices_serial_text_area_error(self):
        a = self.weh.get_element(self.devices_serial_text_area_error)
        time.sleep(5)
        return a.get_attribute("data-tooltip")

    def get_devices_mac_text_area_error(self):
        a = self.weh.get_element(self.devices_mac_text_area_error)
        time.sleep(5)
        _error = self.weh.get_element(self.mac_error, parent=a)
        return _error.get_attribute("data-tooltip")

    def get_add_button(self):
        return self.weh.get_element(self.add_button)

    def get_quick_add_devices(self):
        return self.weh.get_element(self.quick_add_devices)

    def get_deploy_to_cloud(self):
        return self.weh.get_element(self.deploy_to_cloud)

    def get_insert_sn(self):
        elements = self.weh.get_elements(self.insert_sn)
        for el in elements:
            if el.is_displayed():
                return el

    def get_add_location_button(self):
        return self.weh.get_element(self.devices_add_location_button)

    def get_select_location(self):
        return self.weh.get_element(self.devices_select_location)

    def get_cancel_location_button(self):
        return self.weh.get_element(self.devices_cancel_location_button)

    def get_no_location_button(self):
        return self.weh.get_element(self.devices_no_location_button)

    def get_add_devices_button(self):
        return self.weh.get_element(self.add_devices_button)

    def get_device_make_list(self):
        device_make_list = self.weh.get_element(self.device_make_list)
        if device_make_list.is_displayed():
            return device_make_list

    def get_device_make_voss(self):
        return self.weh.get_element(self.device_make_voss)

    def get_device_make_exos(self):
        return self.weh.get_element(self.device_make_exos)

    def get_device_make_aerohive(self):
        return self.weh.get_element(self.device_make_aerohive)

    def get_quick_onboard_failure_panel(self):
        return self.weh.get_element(self.quick_onboard_failure_panel)

    def get_quick_onboard_failure_reason(self):
        return self.weh.get_element(self.quick_onboard_failure_reason)

    def get_quick_onboard_failure_ok_button(self):
        return self.weh.get_element(self.quick_onboard_failure_ok_button)

    def get_device_auto_detection_voss(self):
        return self.weh.get_element(self.device_auto_detection_voss)

    def get_device_auto_detection_exos(self):
        return self.weh.get_element(self.device_auto_detection_exos)

    def get_deploy_locally(self):
        return self.weh.get_element(self.deploy_locally)

    def get_sn_error_message(self):
        el = self.weh.get_element(self.sn_error_message)
        if el.is_displayed():
            return el.get_attribute("data-tooltip")
        else:
            return None

    def get_policy_drop_down(self):
        return self.weh.get_element(self.policy_drop_down)

    def get_policy_drop_down_items(self):
        return self.weh.get_elements(self.policy_drop_down_items)

    def get_device_auto_detection_cloudIqEngineRadio(self):
        el = self.weh.get_element(self.device_auto_detection_cloudIqEngineRadio)
        if el.is_displayed():
            return el
        else:
            return None

    def get_select_csv(self):
        el = self.weh.get_element(self.select_csv)
        if el.is_displayed():
            return el
        else:
            return None

    def get_device_csv_upload_button(self):
        return self.weh.get_element(self.device_csv_upload_button)

    def get_items(self):
        return self.weh.get_elements(self.items)

    def get_port_click(self, el):
        return self.weh.get_element(self.port_click, el)

    def get_device_auto_detection_wingRadio(self):
        el = self.weh.get_element(self.device_auto_detection_cloudIqEngineRadio)
        if el.is_displayed():
            return el
        else:
            return None

    def get_device_stack_template(self, row):
        el = self.weh.get_element(self.device_stack_template, row)
        if el:
            return el
        else:
            return None

    def get_device_stack_template_click(self,row):
        return self.weh.get_element(self.device_stack_template_click, row)

    def get_create_template_click(self):
        return self.weh.get_element(self.create_template_click)

    def get_create_auto_template_update_device_click(self):
        return self.weh.get_element(self.create_auto_template_update_device_click)

    def get_device_os_voss_radio(self):
        return self.weh.get_element(self.device_os_voss_radio)

    def get_device_os_exos_radio(self):
        return self.weh.get_element(self.device_os_exos_radio)

    def get_device_os_cloudiq_engine_radio(self):
        return self.weh.get_element(self.device_os_cloudiq_engine_radio)

    def get_device_os_wing_radio(self):
        return self.weh.get_element(self.device_os_wing_radio)

    def get_assign_policy_device_selected(self):
        return self.weh.get_element(self.assign_policy_device_selected)

    def get_devices_switch_update_network_policy(self):
        return self.weh.get_element(self.devices_switch_update_network_policy)

    def get_devices_switch_update_reboot_rollback(self):
        return self.weh.get_element(self.devices_switch_update_reboot_rollback)

    def get_devices_update_yes_btn(self):
        elements = self.weh.get_elements(self.devices_update_yes_btn)
        for el in elements:
            if el.is_displayed():
                return el

    def get_update_status_failed_selected_device(self):
        return self.weh.get_element(self.update_status_failed_selected_device)

    def get_status_update_failed_after_reboot(self):
        return self.weh.get_element(self.status_update_failed_after_reboot)

    def get_check_pop_message(self):
        return self.weh.get_element(self.check_pop_message)

    def get_check_double_verification_display_rollback(self):
        return self.weh.get_element(self.check_double_verification_display_rollback)

    def get_devices_update_no_btn(self):
        return self.weh.get_element(self.devices_update_no_btn)

    def get_device_np_header(self):
        return self.weh.get_element(self.device_np_header)

    def get_ui_tool_tip_inner(self):
        return self.weh.get_element(self.ui_tool_tip_inner)

    def get_devices_grid_column_headers(self):
        return self.weh.get_elements(self.devices_grid_column_headers)

    def get_devices_page_horizontal_end(self):
        return self.weh.get_element(self.devices_page_horizontal_end)

    def get_all_messages_banner(self):
        return self.weh.get_elements(self.all_messages_banner)

    def get_upgrade_to_free_pilot_link(self):
        return self.weh.get_element(self.upgrade_to_free_pilot_link)

    def get_yes_button_upgrade_to_free_pilot(self):
        return self.weh.get_element(self.yes_button_upgrade_to_free_pilot)

    def get_check_portal_page(self):
        return self.weh.get_element(self.check_portal_page)

    def get_license_form_error(self, row):
        return self.weh.get_element(self.license_form_error, row)

    def get_field_license_stat(self, row):
        return self.weh.get_element(self.field_license_stat, row)

    def get_check_unmanage_box(self):
        el = self.weh.get_element(self.check_unmanage_box)
        if el:
            if el.is_displayed():
                return el
            else:
                return None
        else:
            return None

    def get_pilot_lic_inventory(self):
        return self.weh.get_elements(self.pilot_lic_inventory)

    def get_sn_button(self):
        return self.weh.get_element(self.sn_button)

    def get_sn_xiq_list(self):
        return self.weh.get_elements(self.sn_xiq_list)

    def get_sn_close(self):
        return self.weh.get_element(self.sn_close)

    def get_link_my_account(self):
        return self.weh.get_element(self.link_my_account)

    def get_add_a_license(self):
        return self.weh.get_element(self.add_a_license)

    def get_link_my_account_agree(self):
        return self.weh.get_element(self.link_my_account_agree)

    def get_link_my_account_continue(self):
        return self.weh.get_element(self.link_my_account_continue)

    def get_upgrade_account_to_pilot(self):
        el = self.weh.get_element(self.upgrade_account_to_pilot)
        if el.is_displayed():
            return el
        else:
            return None

    def get_sfdc_username(self):
        return self.weh.get_element(self.sfdc_username)

    def get_sfdc_password(self):
        return self.weh.get_element(self.sfdc_password)

    def get_sfdc_submit(self):
        return self.weh.get_element(self.sfdc_submit)

    def get_sfdc_submit_check_error(self):
        return self.weh.get_element(self.sfdc_submit_check_error)

    def get_enter_shared_cuid(self):
        return self.weh.get_element(self.enter_shared_cuid)

    def get_check_error_shared_cuid(self):
        return self.weh.get_element(self.check_error_shared_cuid)

    def get_submit_shared_cuid(self):
        return self.weh.get_element(self.submit_shared_cuid)

    def get_sfdc_unlink(self):
        return self.weh.get_element(self.sfdc_unlink)

    def get_yes_button_unlink(self):
        return self.weh.get_element(self.yes_button_unlink)

    def get_subscription_rows(self):
        return self.weh.get_elements(self.subscription_rows)

    def get_subscription_available(self, row):
        return self.weh.get_element(self.subscription_available, row)

    def get_subscription_activated(self, row):
        return self.weh.get_element(self.subscription_activated, row)

    def get_message_unlink_button(self):
        return self.weh.get_element(self.message_unlink_button)

    def get_license_button(self):
        return self.weh.get_element(self.license_button)

    def get_user_button(self):
        return self.weh.get_element(self.user_button)

    def get_global_settings(self):
        return self.weh.get_element(self.global_settings)

    def get_audit_button(self):
        return self.weh.get_element(self.audit_button)

    def get_audit_rows(self):
        return self.weh.get_elements(self.audit_rows)

    def get_audit_time_stamp(self, row):
        return self.weh.get_element(self.audit_time_stamp, row)

    def get_field_description(self, row):
        return self.weh.get_element(self.field_description, row)

    def get_sort_time_stamp(self):
        return self.weh.get_element(self.sort_time_stamp)

    def get_field_description_more_button(self, row):
        el = self.weh.get_element(self.field_description_more_button, row)
        if el:
            return el
        else:
            return None

    def get_more_row_description(self):
        elements = self.weh.get_elements(self.more_row_description)
        return elements

    def get_more_row_description_close(self):
        elements = self.weh.get_elements(self.more_row_description_close)
        return elements

    def get_number_of_rows(self):
        return self.weh.get_elements(self.number_of_rows)

    def get_manage_all_devices_progress_status(self):
        return self.weh.get_elements(self.manage_devices_progress_status)

    def get_device_page_size_100(self):
        return self.weh.get_element(self.device_page_size_100)

    def get_upgrade_IQ_engine_and_extreme_network_switch_images_checkbox(self):
        return self.weh.get_element(self.upgrade_IQ_engine_and_extreme_network_switch_images_checkbox)

    def get_license_mgmt(self):
        return self.weh.get_element(self.license_mgmt)

    def get_license_unmanage_box(self):
        el = self.weh.get_element(self.license_unmanage_box)
        if el.is_displayed():
            return el
        else:
            return None

    def get_update_reboot_revert_checkbox(self):
        return self.weh.get_element(self.update_reboot_revert_checkbox)

    def get_update_image_checkbox(self):
        return self.weh.get_element(self.update_image_checkbox)

    def get_events_text(self):
        return self.weh.get_elements(self.get_events)

    def get_update_config_checkbox(self):
        return self.weh.get_element(self.update_config_checkbox)

    def get_device_actions_button(self):
        """
        :return: Device Actions Button
        """
        return self.weh.get_element(self.device_actions_button)

    def get_license_action_button(self):
        return self.weh.get_element(self.license_action_button)

    def get_port_details_info(self):
        return self.weh.get_elements(self.port_details_info)

    def get_digital_twin_container_feature(self):
        """
        :return: quick add > digital twin radio button field
        """
        return self.weh.get_element(self.digital_twin_container_feature)

    def get_device_type_digital_twin_radio_button(self):
        """
        :return: quick add > digital twin radio button field
        """
        return self.weh.get_element(self.device_type_digital_twin_radio_button)

    def get_digital_twin_os_persona_dropdown(self):
        """
        :return: quick add > digital twin OS persona dropdown to select the OS persona to assign
        """
        return self.weh.get_element(self.digital_twin_os_persona_dropdown)

    def get_digital_twin_os_persona_dropdown_items(self):
        """
        :return: quick add > digital twin OS persona dropdown item
        """
        parent = self.get_digital_twin_os_persona_dropdown()
        return self.weh.get_elements(self.digital_twin_os_persona_dropdown_items, parent)

    def get_digital_twin_device_model_dropdown(self):
        """
        :return: quick add > digital twin device model dropdown to select the device model to assign
        """
        return self.weh.get_element(self.digital_twin_device_model_dropdown)

    def get_digital_twin_device_model_dropdown_items(self):
        """
        :return: quick add > digital twin device model dropdown item
        """
        parent = self.get_digital_twin_device_model_dropdown()
        return self.weh.get_elements(self.digital_twin_device_model_dropdown_items, parent)

    def get_digital_twin_os_version_dropdown(self):
        """
        :return: quick add > digital twin OS version dropdown to select the OS version to assign
        """
        return self.weh.get_element(self.digital_twin_os_version_dropdown)

    def get_digital_twin_os_version_dropdown_items(self):
        """
        :return: quick add > digital twin OS version dropdown item
        """
        parent = self.get_digital_twin_os_version_dropdown()
        return self.weh.get_elements(self.digital_twin_os_version_dropdown_items, parent)

    def get_digital_twin_expansion_slot_dropdown(self):
        """
        :return: quick add > digital twin Expansion Slot dropdown to select a VIM module
        """
        return self.weh.get_element(self.digital_twin_expansion_slot_dropdown)

    def get_digital_twin_expansion_slot_dropdown_items(self):
        """
        :return: quick add > digital twin Expansion Slot dropdown item
        """
        parent = self.get_digital_twin_expansion_slot_dropdown()
        return self.weh.get_elements(self.digital_twin_expansion_slot_dropdown_items, parent)

    def get_digital_twin_license_type_dropdown(self):
        """
        :return: quick add > digital twin License Type dropdown to select a Feature License
        """
        return self.weh.get_element(self.digital_twin_license_type_dropdown)

    def get_digital_twin_license_type_dropdown_items(self):
        """
        :return: quick add > digital twin License Type dropdown item
        """
        parent = self.get_digital_twin_license_type_dropdown()
        return self.weh.get_elements(self.digital_twin_license_type_dropdown_items, parent)

    def get_100_rows_per_page_button(self):
        """
        :return: Devices > 100 rows per page button
        """
        return self.weh.get_element(self.one_hundred_rows_per_page_button)

    def get_device_model(self, device_row):
        """
        :param device_row: the device parent row
        :return: Devices -> Device Row -> Device's 'Model' column -> Device model element
        """
        return self.weh.get_element(self.device_model, parent=device_row)

    def get_device_serial_number(self, row, field='field-serialNumber'):
        """
        :param row: the device parent row
        :param field: serial number field in attribute
        :return: Devices -> Device Row -> serial # column
        """
        cells = self.weh.get_elements(self.devices_page_grid_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_global_settings_management_dialog(self):
        return self.weh.get_element(self.global_settings_management_dialog)

    def get_global_settings_management_dialog_yes_button(self):
        return self.weh.get_element(self.global_settings_management_dialog_yes_button)

    def device_actions_change_os_button(self):
        """
        :return: change os button
        """
        elements = self.weh.get_elements(self.device_actions_change_os)
        for el in elements:
            if el.is_displayed():
                return el

    def utilities_button(self):
        return self.weh.get_element(self.utilities_path)

    def restart_pse(self):
        return self.weh.get_element(self.restart_pse_path)

    def pse_yes(self):
        return self.weh.get_element(self.pse_yes_path)

    def loading_bar(self):
        elements = self.weh.get_elements(self.loading_bar_path)
        for el in elements:
            if el.is_displayed():
                return el

    def closing_window(self):
        el = self.weh.get_element(self.closing_window_path)
        if el.is_displayed():
            return el

    def get_pse_reset_status(self):
        el = self.weh.get_element(self.pse_reset_status)
        if el.is_displayed():
            return el

