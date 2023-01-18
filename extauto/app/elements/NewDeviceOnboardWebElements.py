from extauto.app.defs.NewDeviceOnboardDefinitions import NewDeviceOnboardDefinitions
from extauto.common.AutoActions import AutoActions
from extauto.common.WebElementHandler import WebElementHandler


class NewDeviceOnboardWebElements(NewDeviceOnboardDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_grouping_icon(self):
        return self.weh.get_element(self.grouping_icon_id)

    def get_connected_first(self):
        return self.weh.get_element(self.connected_first_id)

    def get_disconnected_first(self):
        return self.weh.get_element(self.disconnected_first_id)

    def get_default_first(self):
        return self.weh.get_element(self.default_first_id)

    def get_group_close(self):
        return self.weh.get_element(self.grouping_close_id)

    def get_device_hostname(self):
        hostname = self.weh.get_element(self.device_hostname_id)
        if hostname.is_displayed():
            return hostname.text

    def get_device_serial_no(self):
        sl_no = self.weh.get_element(self.device_sl_no_id)
        if sl_no.is_displayed():
            return sl_no.text

    def get_onboard_symbol(self):
        return self.weh.get_element(self.onboard_symbol_id)

    def get_device_search(self):
        return self.weh.get_element(self.device_search_field_id)

    def get_device_list_close_link(self):
        return self.weh.get_element(self.device_list_close_link_id)

    def return_to_device_list(self):
        return self.weh.get_element(self.return_to_device_list_id)

    def get_device_list_table(self):
        return self.weh.get_element(self.device_list_table_id)

    def get_device_list_grid_rows(self):
        table = self.get_device_list_table()
        return self.weh.get_elements(self.device_filter_id, parent=table)

    def get_refresh_option(self):
        return self.weh.get_element(self.refresh_option_id)

    def get_serial_number_text_field(self):
        return self.weh.get_element(self.serial_number_text_id)

    def get_device_make(self):
        return self.weh.get_element(self.device_make_dropdown_id)

    def get_device_make_table(self):
        return self.weh.get_element(self.device_make_table)

    def get_device_make_entry(self):
        build = self.get_device_make_table()
        return self.weh.get_elements(self.device_make_row, parent=build)

    def get_continue_button(self):
        return self.weh.get_element(self.continue_button_id)

    def get_reenter_serial_number(self):
        return self.weh.get_element(self.reenter_serial_no_id)

    def get_reenter_serial_number_field(self):
        return self.weh.get_element(self.reenter_serial_number_field_id)

    def get_onboard_button(self):
        return self.weh.get_element(self.onboard_button_id)

    def get_device_model_no(self):
        try:
            model_number = self.weh.get_element(self.device_model_no_id)
            if model_number.is_displayed():
                return model_number.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_ap_serial_no(self):
        try:
            serial_number = self.weh.get_element(self.serial_no_of_ap_id)
            if serial_number.is_displayed():
                return serial_number.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_next_option(self):
        return self.weh.get_element(self.next_location_option_id)

    def get_skip_location(self):
        return self.weh.get_element(self.skip_location_id)

    def get_searched_location(self):
        return self.weh.get_element(self.search_location_id)

    def get_loc_table(self):
        return self.weh.get_element(self.location_table_id)

    def get_loc_grid_rows(self):
        table = self.get_loc_table()
        return self.weh.get_elements(self.location_grid_rows, parent=table)

    def get_building_backward_link(self):
        return self.weh.get_element(self.building_backward_link_id)

    def get_searched_building(self):
        return self.weh.get_element(self.search_building_id)

    def get_building_table(self):
        return self.weh.get_element(self.building_table_id)

    def get_build_grid_rows(self):
        build = self.get_building_table()
        return self.weh.get_elements(self.building_grid_rows, parent=build)

    def get_floor_backward_link(self):
        return self.weh.get_element(self.floor_backward_link_id)

    def get_searched_floor(self):
        return self.weh.get_element(self.search_floor_id)

    def get_floor_table(self):
        return self.weh.get_element(self.floor_table_id)

    def get_floor_grid_rows(self):
        floor = self.get_floor_table()
        return self.weh.get_elements(self.floor_grid_rows, parent=floor)

    def get_back_to_device_details(self):
        return self.weh.get_element(self.go_previous_device_details_id)

    def get_exit_onboard_process(self):
        return self.weh.get_element(self.exit_onboard_id)

    def get_exit_onboard_confirm(self):
        return self.weh.get_element(self.exit_onboard_yes_button_id)

    def get_exit_onboard_cancel(self):
        return self.weh.get_element(self.exit_onboard_cancel_button_id)

    def get_nw_policy_option(self):
        return self.weh.get_element(self.next_network_option_id)

    def get_nw_policy_dropdown(self):
        return self.weh.get_element(self.network_policy_dropdown)

    def get_np_backward_link(self):
        return self.weh.get_element(self.np_backward_link_id)

    def get_searched_np(self):
        return self.weh.get_element(self.search_np_id)

    def get_np_table(self):
        return self.weh.get_element(self.np_table_id)

    def get_np_grid_rows(self):
        np = self.get_np_table()
        return self.weh.get_elements(self.np_grid_rows, parent=np)

    def get_back_to_location_details(self):
        return self.weh.get_element(self.go_previous_location_details_id)

    def get_done_button(self):
        return self.weh.get_element(self.done_button_id)

    def get_policy_details(self):
        policy = self.weh.get_element(self.policy_details_id)
        if policy.is_displayed():
            return policy.text
        else:
            return "None"

    def get_location_details(self):
        location = self.weh.get_element(self.location_details_id)
        if location.is_displayed():
            return location.text
        else:
            return "None"

    def get_finish_button(self):
        return self.weh.get_element(self.finish_button_id)

    def get_refresh_popup_checkbox(self):
        return self.weh.get_element(self.refresh_popup_checkbox_id)

    def get_refresh_popup_dismiss(self):
        return self.weh.get_element(self.refresh_popup_dismiss_button_id)

    def get_add_another(self):
        return self.weh.get_element(self.add_another_button_id)

    def get_policy_save_yes(self):
        return self.weh.get_element(self.policy_save_yes_id)

    def get_policy_save_no(self):
        return self.weh.get_element(self.policy_save_no_id)

    def get_loc_info(self):
        try:
            location = self.weh.get_element(self.loc_details_id)
            if location.is_displayed():
                return location.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_dloc(self):
        return self.weh.get_element(self.loc_dropdown_id)

    def get_building_info(self):
        try:
            building = self.weh.get_element(self.build_details_id)
            if building.is_displayed():
                return building.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_floor_info(self):
        try:
            floor = self.weh.get_element(self.floor_detail_id)
            if floor.is_displayed():
                return floor.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_dpolicy(self):
        try:
            policy = self.weh.get_element(self.network_policy_info_id)
            if policy.is_displayed():
                return policy.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_device_home_backward(self):
        return self.weh.get_element(self.device_home_backward_id)

    def get_device_hpolicy(self):
        try:
            policy = self.weh.get_element(self.device_home_policy_id)
            if policy.is_displayed():
                return policy.text
            else:
                return "None"
        except Exception:
            return "None"

    def get_device_hlocation(self):
        try:
            location =  self.weh.get_element(self.device_home_location_id)
            if location.is_displayed():
                return location.text
            else:
                return "None"
        except Exception:
            return "None"
