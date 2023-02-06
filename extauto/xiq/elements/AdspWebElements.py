from extauto.xiq.defs.AdspWebElementsDefinitions import AdspWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class AdspWebElements(AdspWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_adsp_alarm_grid_rows(self):
        return self.weh.get_elements(self.adsp_alarm_grid_rows)

    def get_adsp_alarms_grid_row_cells(self, row):
        return self.weh.get_elements(self.adsp_alarms_grid_row_cells, row)

    def get_adsp_more_insights_button(self):
        return self.weh.get_element(self.adsp_more_insights_tab)

    def get_adsp_alarm_grid_row_check_box(self, row):
        return self.weh.get_element(self.adsp_alarm_grid_row_check_box, row)

    def get_adsp_alarm_clear_button(self):
        return self.weh.get_element(self.adsp_alarm_clear_button)

    def get_adsp_alarm_clear_confirm_yes_button(self):
        return self.weh.get_element(self.adsp_alarm_clear_confirm_yes_button)

    def get_adsp_alarm_search_button(self):
        return self.weh.get_element(self.adsp_alarm_search_button)

    def go_to_adsp_sensor_page(self):
        return self.weh.get_element(self.to_adsp_sensor_page)

    def get_search_adsp_sensor_page(self):
        return self.weh.get_element(self.search_adsp_sensor_page)

    def get_serial_to_adsp_sensor_page(self):
        return self.weh.get_element(self.serial_to_adsp_sensor_page)

    def get_device_location_from_adsp(self):
        return self.weh.get_element(self.device_location_from_adsp)

    def get_ap_serial_from_adsp(self):
        return self.weh.get_element(self.ap_serial_from_adsp)

    def get_auth_error_from_adess(self):
        return  self.weh.get_element(self.auth_error_from_adess)

    def get_adsp_alarm_search_text_field(self):
        return self.weh.get_element(self.adsp_alarm_search_text_field)

    def get_all_adsp_alarm_grid_check_boxes(self):
        return self.weh.get_element(self.adsp_select_all_alarm_checkbox)

    def get_adsp_alarm_page_size_options(self):
        return self.weh.get_elements(self.adsp_alarm_page_size_options)

    def get_adsp_alarm_page_size_label(self):
        return self.weh.get_element(self.adsp_alarm_page_size_label)

    def get_adsp_alarm_page_size_drop_down(self):
        return self.weh.get_element(self.adsp_alarm_page_size_botton)

    def get_total_adsp_alarm_count_on_grid(self):
        return self.weh.get_element(self.adsp_total_alarm_count_text)

    def get_adsp_alarms_overview_widget_count(self):
        return self.weh.get_element(self.adsp_alarms_overview_widget_count)

    def get_adsp_alarms_by_severity_widget_count(self):
        return self.weh.get_element(self.adsp_alarms_by_severity_widget_count)

    def get_adsp_subscribe_page(self):
        return self.weh.get_element(self.adsp_subscribe_page)

    def get_adsp_subscribe_button(self):
        return self.weh.get_element(self.adsp_subscribe_button)

    def get_adsp_subscribe_apply_button(self):
        return self.weh.get_element(self.adsp_subscribe_apply_button)

    def get_adsp_widget_refresh_button(self):
        return self.weh.get_element(self.adsp_widget_refresh_button)

    def get_adsp_alarm_refresh_button(self):
        return self.weh.get_element(self.adsp_alarm_refresh_button)

    def get_adsp_settings_button(self):
        return self.weh.get_element(self.adsp_settings_button)

    def get_adsp_wireless_thread_detection_button(self, row):
        """
        :return: device wireless thread detection Button
        """
        return self.weh.get_element(self.adsp_wireless_thread_detection_button, parent=row)

    def get_adsp_wireless_thread_detection_apply_button(self):
        return self.weh.get_element(self.adsp_wireless_thread_detection_apply_button)

    def get_adsp_wireless_thread_detection_ok_button(self):
        return self.weh.get_element(self.adsp_wireless_thread_detection_ok_button)

    def get_adsp_page_wips_policy_grid_rows(self):
        grid = self.weh.get_element(self.adsp_page_wips_policy_grid)
        return self.weh.get_elements(self.adsp_page_wips_policy_grid_rows, parent=grid)

    def get_adsp_page_wips_policy_grid_checkbox_cells(self, row):
        return self.weh.get_elements(self.adsp_page_wips_policy_grid_checkbox_cells, row)



    def get_adsp_user_role_not_supported(self):
        return self.weh.get_elements(self.adsp_user_role_not_supported)