from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.defs.Network360MonitorDefinitions import Network360MonitorDefinitions


class Network360MonitorElements(Network360MonitorDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_n360_monitor_location_search_box(self):
        return self.weh.get_element(self.n360_monitor_location_search_box)

    def get_n360_monitor_floors(self):
        return self.weh.get_elements(self.n360_monitor_floors)

    def get_n360_monitor_search_matches(self):
        return self.weh.get_elements(self.n360_monitor_search_matches)

    def get_n360_monitor_aps_on_floor(self):
        return self.weh.get_elements(self.n360_monitor_aps_on_floor)

    def get_n360_monitor_ap_count_on_floor(self):
        return self.weh.get_element(self.n360_monitor_ap_count_on_floor)

    def get_n360_monitor_connected_clients_tab(self):
        return self.weh.get_element(self.n360_monitor_connected_clients_tab)

    def get_n360_monitor_clients_on_floor(self):
        return self.weh.get_elements(self.n360_monitor_clients_on_floor)

    def get_n360_connected_client_macs(self):
        return self.weh.get_elements(self.n360_connected_client_macs)

    def get_devices_score(self):
        return self.weh.get_element(self.n360_monitor_devices_score)

    def get_n360_monitor_devices_card(self):
        return self.weh.get_element(self.n360_monitor_devices_card)

    def get_n360_monitor_clients_card(self):
        return self.weh.get_element(self.n360_monitor_clients_card)

    def get_device_health_overal_score_availability_score(self):
        return self.weh.get_element(self.device_health_overal_score_availability_score)

    def get_device_health_overal_score_hw_health(self):
        return self.weh.get_element(self.device_health_overal_score_hw_health)

    def get_device_health_overal_score_fw_score(self):
        return self.weh.get_element(self.device_health_overal_score_fw_score)

    def get_n360_monitor_map(self):
        return self.weh.get_element(self.n360_monitor_map)

    def get_client_health_clients_widget_count_2G(self):
        return self.weh.get_element(self.client_health_clients_widget_count_2G)

    def get_client_health_clients_widget_count_5G(self):
        return self.weh.get_element(self.client_health_clients_widget_count_5G)

    def get_client_health_clients_widget_count_6G(self):
        return self.weh.get_element(self.client_health_clients_widget_count_6G)

    def get_graph_point(self, index):
        return self.weh.get_template_element(self.graph_point, color=index)

    def get_graph_point_hover(self, index):
        return self.weh.get_template_element(self.graph_point_hover, color=index)

    def get_graph_line_color(self, index):
        return self.weh.get_template_element(self.graph_line_color, color=index)

    def get_graph_legend_names(self, index):
        return self.weh.get_template_element(self.graph_legend_names, color=index)

    def get_n360_back_to_timeline(self):
        return self.weh.get_element(self.n360_back_to_timeline)

    def get_n360_graph_tooltip(self):
        return self.weh.get_element(self.n360_graph_tooltip)

    def get_n360_graph_tooltip_info(self):
        return self.weh.get_elements(self.n360_graph_tooltip_info)

    def get_n360_device_health_refresh_btn(self):
        return self.weh.get_element(self.n360_device_health_refresh_btn)

    def get_n360_device_health_settings(self):
        return self.weh.get_element(self.n360_device_health_settings_btn)

    def get_n360_device_health_events_list(self):
        return self.weh.get_elements(self.n360_device_health_events_list)

    def get_n360_device_health_events_checkbox(self):
        return self.weh.get_elements(self.n360_device_health_events_checkbox)

    def get_n360_device_health_search_box(self):
        return self.weh.get_element(self.n360_device_health_search_box)

    def get_n360_device_health_column_headers(self):
        return self.weh.get_elements(self.n360_device_health_column_headers)

    def get_n360_device_health_column_header_hostname(self):
        return self.weh.get_elements(self.n360_device_health_column_header_hostname)

    def get_n360_device_health_column_header_mac(self):
        return self.weh.get_elements(self.n360_device_health_column_header_mac)

    def get_n360_device_health_total_usage(self):
        return self.weh.get_element(self.n360_device_health_total_usage)

    def get_n360_device_health_download_button(self):
        return self.weh.get_element(self.n360_device_health_download_button)

    def get_n360_device_health_column_header(self):
        return self.weh.get_element(self.n360_device_health_column_header)

    def get_n360_monitor_port_device_health_usage_table_rows(self):
        rows = []
        for row in self.weh.get_elements(self.n360_monitor_port_device_health_usage_table_rows):
            if row.is_displayed():
                rows.append(row)
        return rows

    def get_n360_monitor_health_selector_drop_down_arrow(self):
        return self.weh.get_element(self.n360_monitor_health_selector_drop_down_arrow)

    def get_n360_monitor_health_selector_drop_down_options(self, option):
        return self.weh.get_template_element(self.n360_monitor_health_selector_drop_down_options, option=option)

    def get_n360_monitor_port_connection_speed_container_down_arrow(self):
        return self.weh.get_element(self.n360_monitor_port_connection_speed_container_down_arrow)

    def get_n360_monitor_drop_down_options(self, option):
        return self.weh.get_template_element(self.n360_monitor_drop_down_options, option=option)

    def get_close_n360_dialog_box(self):
        return self.weh.get_element(self.close_n360_dialog_box)

    def get_n360_show_all_btn(self):
        return self.weh.get_element(self.n360_show_all_btn)

