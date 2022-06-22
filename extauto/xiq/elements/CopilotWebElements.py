from extauto.xiq.defs.CopilotDefs import *
from extauto.common.WebElementHandler import *


class CopilotWebElements(CopilotDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_wifi_capacity_widget(self):
        return self.weh.get_element(self.wifi_capacity_widget)

    def get_wifi_capacity_content(self):
        return self.weh.get_element(self.wifi_capacity_content)

    def get_wifi_capacity_status(self):
        return self.weh.get_element(self.wifi_capacity_status)

    def get_wifi_capacity_widget_location_grid_rows(self):
        grid_rows = self.weh.get_elements(self.wifi_capacity_widget_location_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wifi_capacity_widget_location_grid_rows_from_widget(self, widget):
        return self.weh.get_elements(self.wifi_capacity_widget_location_grid_rows, widget)

    def get_wifi_capacity_widget_location_grid_internal_rows(self):
        return self.weh.get_elements(self.wifi_capacity_widget_location_grid_internal_rows)

    def get_wifi_capacity_widget_location_grid_pin_rows(self):
        grid_rows = self.weh.get_elements(self.wifi_capacity_widget_location_grid_pin_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wifi_capacity_widget_location_pin_button(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_pin_button, row)

    def get_wifi_capacity_widget_location_already_pinned_status(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_already_pinned_status, row)

    def get_wifi_capacity_widget_location_more_options_button(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_more_options_button, row)

    def get_wifi_capacity_widget_location_more_options_mute_button(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_more_options_mute_button, row)

    def get_wifi_capacity_widget_location_muted_grid_rows(self):
        grid_rows = self.weh.get_elements(self.wifi_capacity_widget_location_grid_muted_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_dislayed_element(self, elements):
        for el in elements:
            if el.is_displayed():
                return el

    def get_wifi_capacity_widget_location_more_options_unmute_button(self):
        elements = self.weh.get_elements(self.wifi_capacity_widget_location_more_options_mute_button)
        return self.get_dislayed_element(elements)

    def get_wifi_capacity_widget_location_ap_status_info_pin_column(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_status_info_pin_column, row)

    def get_wifi_capacity_widget_location_ap_info_icon(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_info_icon, row)

    def get_wifi_capacity_anomaly_ap_issue_details(self):
        return self.weh.get_element(self.wifi_capacity_anomaly_ap_issue_details)

    def get_wifi_capacity_anomaly_ap_recommended_actions_details(self):
        return self.weh.get_element(self.wifi_capacity_anomaly_ap_recommended_actions_details)

    def get_total_anomalies_detected_from_icon(self):
        return self.weh.get_element(self.total_anomalies_detected_from_icon)

    def get_anomalies_detected_grid_rows(self):
        grid_rows = self.weh.get_elements(self.anomalies_detected_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wifi_capacity_more_options_btn(self, row):
        return self.weh.get_element(self.wifi_capacity_more_options_btn, row)

    def get_wifi_capacity_dismiss_option(self):
        return self.weh.get_element(self.wifi_capacity_dismiss_option)

    def get_wifi_capacity_dismiss_warning(self):
        return self.weh.get_element(self.wifi_capacity_dismiss_warning)

    def get_wifi_capacity_dismiss_no_option(self):
        return self.weh.get_element(self.wifi_capacity_dismiss_no_option)

    def get_wifi_capacity_dismiss_yes_option(self):
        return self.weh.get_element(self.wifi_capacity_dismiss_yes_option)

    def get_wifi_capacity_widget_location_grid_individual_ap_rows(self):
        grid_rows = self.weh.get_elements(self.wifi_capacity_widget_location_grid_individual_ap_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wifi_capacity_widget_location_individual_ap_pin_button(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_individual_ap_pin_button, row)

    def get_wifi_capacity_widget_location_individual_ap_unpin_button(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_individual_ap_unpin_button, row)

    def get_tooltip_content(self):
        return self.weh.get_element(self.tooltip_content)

    def get_wifi_capacity_widget_location_detailed_view_close_button(self):
        return self.weh.get_element(self.wifi_capacity_widget_location_detailed_view_close_button)

    def get_anomalies_view_all_btn(self):
        return self.weh.get_element(self.anomalies_view_all_btn)

    def get_copilot_branded_image(self):
        return self.weh.get_element(self.copilot_branded_image)

    def get_wifi_capacity_content(self):
        return self.weh.get_element(self.wifi_capacity_content)

    def get_assurance_scan_widget(self):
        return self.weh.get_element(self.assurance_scan_widget)

    def get_assurance_total_scan_count(self):
        return self.weh.get_element(self.assurance_total_scan_count)

    def get_show_or_hide_muted_button_in_wifi_capacity_widget(self):
        return self.weh.get_element(self.show_or_hide_muted_button_in_wifi_capacity_widget)

    def get_anomaly_notification_grid_rows(self):
        grid_rows = self.weh.get_elements(self.anomaly_notification_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wifi_capacity_video_help_icon(self):
        return self.weh.get_element(self.wifi_capacity_video_help_icon)

    def get_wifi_capacity_additional_resources_docs_links(self):
        return self.weh.get_elements(self.wifi_capacity_additional_resources_docs_links)

    def get_wifi_capacity_additional_resources_video_links(self):
        return self.weh.get_elements(self.wifi_capacity_additional_resources_video_links)

    def get_wifi_capacity_additional_resources_close_button(self):
        return self.weh.get_element(self.wifi_capacity_additional_resources_close_button)

    def get_wifi_capacity_widget_sort_options(self):
        return self.weh.get_elements(self.wifi_capacity_widget_sort_options)

    def get_wifi_capacity_widget_sort(self):
        return self.weh.get_elements(self.wifi_capacity_widget_sort)

    def get_wifi_capacity_widget_anomaly_pinned_status(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_anomaly_pinned_status, row)

    def get_wifi_efficiency_widget_content(self):
        return self.weh.get_element(self.wifi_efficiency_widget_content)

    def get_wifi_efficiency_widget(self):
        return self.weh.get_element(self.wifi_efficiency_widget)

    def get_wifi_efficiency_widget_location_grid_rows(self):
        grid_rows = self.weh.get_elements(self.wifi_efficiency_widget_location_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wifi_efficiency_widget_location_already_pinned_status(self, row):
        return self.weh.get_element(self.wifi_efficiency_widget_location_already_pinned_status, row)

    def get_wifi_efficiency_widget_location_pin_button(self, row):
        return self.weh.get_element(self.wifi_efficiency_widget_location_pin_button, row)

    def get_poe_stability_widget(self):
        return self.weh.get_element(self.poe_stability_widget)

    def get_poe_stability_content(self):
        return self.weh.get_element(self.poe_stability_content)

    def get_poe_stability_widget_location_grid_rows(self):
        grid_rows = self.weh.get_elements(self.poe_stability_widget_location_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_poe_stability_widget_location_grid_pin_rows(self):
        grid_rows = self.weh.get_elements(self.poe_stability_widget_location_grid_pin_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_poe_stability_widget_location_pin_button(self, row):
        return self.weh.get_element(self.poe_stability_widget_location_pin_button, row)

    def get_poe_stability_widget_location_already_pinned_status(self, row):
        return self.weh.get_element(self.poe_stability_widget_location_already_pinned_status, row)

    def get_port_efficiency_widget(self):
        return self.weh.get_element(self.poe_stability_widget)

    def get_port_efficiency_widget_details(self):
        return self.weh.get_element(self.port_efficiency_widget_details)

    def get_port_efficiency_widget_location_grid_rows(self):
        grid_rows = self.weh.get_elements(self.port_efficiency_widget_location_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_port_efficiency_widget_location_grid_pin_rows(self):
        grid_rows = self.weh.get_elements(self.port_efficiency_widget_location_grid_pin_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_port_efficiency_widget_location_pin_button(self, row):
        return self.weh.get_element(self.port_efficiency_widget_location_pin_button, row)

    def get_port_efficiency_widget_location_already_pinned_status(self, row):
        return self.weh.get_element(self.port_efficiency_widget_location_already_pinned_status, row)

    def get_dfs_recurrence_widget(self):
        return self.weh.get_element(self.dfs_recurrence_widget)

    def get_dfs_recurrence_widget_content(self):
        return self.weh.get_element(self.dfs_recurrence_widget_content)

    def get_dfs_recurrence_anomaly_list(self):
        return self.weh.get_elements(self.dfs_recurrence_anomaly_list)

    def get_anomaly_location(self, anomaly):
        return self.weh.get_element(self.anomaly_location, parent=anomaly)

    def get_anomaly_severity(self, anomaly):
        return self.weh.get_element(self.anomaly_severity, parent=anomaly)

    def get_anomaly_last_detected(self, anomaly):
        return self.weh.get_element(self.anomaly_last_detected, parent=anomaly)

    def get_anomaly_pinned(self, anomaly):
        return self.weh.get_element(self.anomaly_pinned, parent=anomaly)

    def get_anomaly_muted(self, anomaly):
        return self.weh.get_element(self.anomaly_muted, parent=anomaly)

    def get_anomaly_device_details(self):
        return self.weh.get_elements(self.anomaly_device_details)

    def get_anomaly_device_name(self, anomaly_device_detail):
        return self.weh.get_element(self.anomaly_device_name, parent=anomaly_device_detail)

    def get_anomaly_device_last_detected(self, anomaly_device_detail):
        return self.weh.get_element(self.anomaly_device_last_detected, parent=anomaly_device_detail)

    def get_anomaly_device_anomaly_severity(self, anomaly_device_detail):
        return self.weh.get_element(self.anomaly_device_anomaly_severity, parent=anomaly_device_detail)

    def get_anomaly_device_pinned_status(self, anomaly_device_detail):
        return self.weh.get_element(self.anomaly_device_pinned_status, parent=anomaly_device_detail)

    def get_dfs_recurrence_anomaly_muted(self):
        return self.weh.get_element(self.dfs_recurrence_anomaly_muted)

    def get_account_summary_widget(self):
        return self.weh.get_element(self.account_summary_widget)

    def get_account_summary_rows(self):
        return self.weh.get_elements(self.account_summary_row)

    def get_account_summary_row_key(self, row):
        return self.weh.get_element(self.account_summary_row_key, parent=row)

    def get_account_summary_row_value(self, row):
        return self.weh.get_element(self.account_summary_row_value, parent=row)

    def get_extremecloud_iq_applications_widget(self):
        return self.weh.get_element(self.extremecloud_iq_applications_widget)

    def get_extremecloud_iq_applications_rows(self,):
        return self.weh.get_elements(self.extremecloud_iq_applications_row)

    def get_extremecloud_iq_applications_row_key(self, row):
        return self.weh.get_element(self.extremecloud_iq_applications_row_key, parent=row)

    def get_extremecloud_iq_applications_row_value(self, row):
        return self.weh.get_element(self.extremecloud_iq_applications_row_value, parent=row)

    def get_devices_by_type_widget(self):
        return self.weh.get_element(self.devices_by_type_widget)

    def get_devices_by_type_rows(self, widget):
        return self.weh.get_elements(self.devices_by_type_row, parent=widget)

    def get_devices_by_type_row_key(self, row):
        return self.weh.get_element(self.devices_by_type_row_key, parent=row)

    def get_devices_by_type_row_value(self, row):
        return self.weh.get_element(self.devices_by_type_row_value, parent=row)

    def get_devices_by_os_widget(self):
        return self.weh.get_element(self.devices_by_os_widget)

    def get_devices_by_os_rows(self, widget):
        return self.weh.get_elements(self.devices_by_os_row, parent=widget)

    def get_devices_by_os_row_key(self, row):
        return self.weh.get_element(self.devices_by_os_row_key, parent=row)

    def get_devices_by_os_row_value(self, row):
        return self.weh.get_element(self.devices_by_os_row_value, parent=row)

    def get_devices_by_os_iqagent(self):
        return self.weh.get_element(self.devices_by_os_iqagent)

    def get_copilot_widget(self):
        return self.weh.get_element(self.copilot_widget)

    def get_copilot_widget_rows(self, widget):
        return self.weh.get_elements(self.copilot_widget_row, parent=widget)

    def get_copilot_widget_row_key(self, row):
        return self.weh.get_element(self.copilot_widget_row_key, parent=row)

    def get_copilot_widget_row_value(self, row):
        return self.weh.get_element(self.copilot_widget_row_value, parent=row)

    def get_dfs_recurrence_widget_location_grid_rows(self):
        grid_rows = self.weh.get_elements(self.dfs_recurrence_widget_location_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_dfs_recurrence_widget_location_grid_pin_rows(self):
        grid_rows = self.weh.get_elements(self.dfs_recurrence_widget_location_grid_pin_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_dfs_recurrence_widget_location_pin_button(self, row):
        return self.weh.get_element(self.dfs_recurrence_widget_location_pin_button, row)

    def get_dfs_recurrence_widget_location_already_pinned_status(self, row):
        return self.weh.get_element(self.dfs_recurrence_widget_location_already_pinned_status, row)

    def get_dfs_recurrence_widget_location_more_options_mute_button(self, row):
        elements = self.weh.get_elements(self.dfs_recurrence_widget_location_more_options_mute_button)
        return self.get_dislayed_element(elements)

    def get_dfs_recurrence_widget_location_grid_muted_rows(self):
        grid_rows = self.weh.get_elements(self.dfs_recurrence_widget_location_grid_muted_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_dfs_recurrence_widget_location_more_options_button(self, row):
        return self.weh.get_element(self.dfs_recurrence_widget_location_more_options_button, row)

    def get_dfs_recurrence_widget_location_grid_unmute_button(self, row):
        return self.weh.get_element(self.dfs_recurrence_widget_location_grid_unmute_button, row)

    def get_dfs_recurrence_widget_location_more_options_btn(self, row):
        return self.weh.get_element(self.dfs_recurrence_widget_location_more_options_btn, row)

    def get_dfs_recurrence_widget_location_dismiss_option(self):
        return self.weh.get_element(self.dfs_recurrence_widget_location_dismiss_option)

    def get_dfs_recurrence_widget_location_dismiss_warning(self):
        return self.weh.get_element(self.dfs_recurrence_widget_location_dismiss_warning)

    def get_dfs_recurrence_widget_location_dismiss_no_option(self):
        return self.weh.get_element(self.dfs_recurrence_widget_location_dismiss_no_option)

    def get_dfs_recurrence_widget_location_dismiss_yes_option(self):
        return self.weh.get_element(self.dfs_recurrence_widget_location_dismiss_yes_option)

    def get_dfs_recurrence_widget_location_grid_individual_ap_rows(self):
        grid_rows = self.weh.get_elements(self.dfs_recurrence_widget_location_grid_individual_ap_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_dfs_recurrence_widget_location_individual_ap_pin_button(self, row):
        return self.weh.get_element(self.wifi_capacity_widget_location_individual_ap_pin_button, row)

    def get_dfs_recurrence_widget_location_detailed_view_close_button(self):
        return self.weh.get_element(self.dfs_recurrence_widget_location_detailed_view_close_button)

    def get_dfs_recurrence_widget_location_individual_ap_unpin_button(self, row):
        return self.weh.get_element(self.dfs_recurrence_widget_location_individual_ap_unpin_button, row)

    def get_copilot_license_mange_link(self):
        return self.weh.get_element(self.copilot_license_mange_link)

    def get_license_page_heading(self):
        return self.weh.get_element(self.license_page_heading)

    def get_page_refresh_button(self):
        return self.weh.get_element(self.page_refresh_button)

    def get_adverse_traffic_patterns_widget_location_grid_rows(self):
        grid_rows = self.weh.get_elements(self.adverse_traffic_patterns_widget_location_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_adverse_traffic_patterns_widget_location_grid_pin_rows(self):
        grid_rows = self.weh.get_elements(self.adverse_traffic_patterns_widget_location_grid_pin_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_adverse_traffic_patterns_widget_location_pin_button(self, row):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_pin_button, row)

    def get_adverse_traffic_patterns_widget_location_already_pinned_status(self, row):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_already_pinned_status, row)

    def get_adverse_traffic_patterns_widget_anomaly_muted(self):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_anomaly_muted)

    def get_adverse_traffic_patterns_widget(self):
        return self.weh.get_element(self.adverse_traffic_patterns_widget)

    def get_adverse_traffic_patterns_list(self):
        return self.weh.get_elements(self.adverse_traffic_patterns_anomaly_list)

    def get_adverse_traffic_patterns_anomaly_location(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_location, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_severity(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_severity, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_last_detected(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_last_detected, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_pinned(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_pinned, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_muted(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_muted, parent=anomaly)

    def get_adverse_traffic_patterns_widget_location_grid_individual_ap_rows(self):
        grid_rows = self.weh.get_elements(self.adverse_traffic_patterns_widget_location_grid_individual_ap_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_adverse_traffic_patterns_device_list(self):
        return self.weh.get_elements(self.adverse_traffic_patterns_device_list)

    def get_adverse_traffic_patterns_anomaly_device_location(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_device_location_name, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_device_severity(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_device_severity, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_device_last_detected(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_device_last_detected, parent=anomaly)

    def get_adverse_traffic_patterns_anomaly_device_pinned(self, anomaly):
        return self.weh.get_element(self.adverse_traffic_patterns_anomaly_device_pinned, parent=anomaly)

    def get_adverse_traffic_patterns_widget_location_more_button(self, row):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_more_button, row)

    def get_adverse_traffic_patterns_widget_location_mute_and_dismiss_div(self):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_mute_and_dismiss_div)

    def get_adverse_traffic_patterns_widget_location_mute_button(self, panel):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_mute_button, panel)

    def get_adverse_traffic_patterns_widget_location_dismiss_button(self, panel):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_dismiss_button, panel)

    def get_adverse_traffic_patterns_widget_location_unmute_button(self, panel):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_unmute_button, panel)

    def get_adverse_traffic_patterns_widget_location_dismiss_confirm_dialog(self):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_dismiss_confirm_dialog)

    def get_adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_cancel(self, panel):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_cancel, panel)

    def get_adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_okay(self, panel):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_okay, panel)

    def get_adverse_traffic_patterns_widget_content(self):
        return self.weh.get_element(self.adverse_traffic_patterns_widget_content)

    def get_wifi_capacity_widget_location_ap_dislike(self):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_dislike)

    def get_wifi_capacity_widget_location_ap_dislike_send_feedback_textfield(self):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_dislike_send_feedback_textfield)

    def get_wifi_capacity_widget_location_ap_dislike_send_feedback_button(self):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_dislike_send_feedback_button)

    def get_wifi_capacity_widget_location_ap_like_tooltip(self):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_like_tooltip)

    def get_wifi_capacity_widget_location_ap_dislike_button_enabled_status(self):
        return self.weh.get_element(self.wifi_capacity_widget_location_ap_dislike_button_enabled_status)