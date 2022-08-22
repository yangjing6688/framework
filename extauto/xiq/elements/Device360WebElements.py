from extauto.xiq.defs.Device360WebElementDefs import *
from extauto.common.WebElementHandler import *


class Device360WebElements(Device360WebElementDefs):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_ports_from_device360_up_lldp_neighbour(self):
        return self.weh.get_element(self.ports_from_device360_up_lldp_neighbour)

    def get_ports_from_device360_up(self):
        return self.weh.get_elements(self.ports_from_device360_up)

    def get_lldp_neigbour_from_table(self):
        return self.weh.get_element(self.lldp_neigbour_from_table)

    def get_system_info_button(self):
        return self.weh.get_element(self.system_info_button)

    def get_system_info_device_host_name(self):
        return self.weh.get_element(self.system_info_device_host_name)

    def get_system_info_network_policy(self):
        return self.weh.get_element(self.system_info_network_policy)

    def get_system_info_device_model(self):
        return self.weh.get_element(self.system_info_device_model)

    def get_system_info_device_function(self):
        return self.weh.get_element(self.system_info_device_function)

    def get_system_info_device_template(self):
        return self.weh.get_element(self.system_info_device_template)

    def get_system_info_conf_type(self):
        return self.weh.get_element(self.system_info_conf_type)

    def get_system_info_serial_num(self):
        return self.weh.get_element(self.system_info_serial_num)

    def get_system_info_iq_engine(self):
        return self.weh.get_element(self.system_info_iq_engine)

    def get_system_info_dev_status(self):
        return self.weh.get_element(self.system_info_dev_status)

    def get_system_info_mgt0_ipv4(self):
        return self.weh.get_element(self.system_info_mgt0_ipv4)

    def get_system_info_mgt0_ipv6(self):
        return self.weh.get_element(self.system_info_mgt0_ipv6)

    def get_system_info_ipv6_subnet(self):
        return self.weh.get_element(self.system_info_ipv6_subnet)

    def get_system_info_ipv4_subnet(self):
        return self.weh.get_element(self.system_info_ipv4_subnet)

    def get_system_info_ipv4_default(self):
        return self.weh.get_element(self.system_info_ipv4_default)

    def get_system_info_ipv6_default(self):
        return self.weh.get_element(self.system_info_ipv6_default)

    def get_system_info_mgt0_mac(self):
        return self.weh.get_element(self.system_info_mgt0_mac)

    def get_system_info_dns(self):
        return self.weh.get_element(self.system_info_dns)

    def get_system_info_ntp(self):
        return self.weh.get_element(self.system_info_ntp)

    def get_close_dialog(self):
        return self.weh.get_element(self.close_dialog)

    def get_actions_adv_cli_access_cmd_input(self):
        return self.weh.get_element(self.actions_adv_cli_access_cmd_input)

    def get_actions_adv_cli_access_cmd_apply(self):
        return self.weh.get_element(self.actions_adv_cli_access_cmd_apply)

    def get_actions_adv_cli_access_cmd_output(self):
        return self.weh.get_element(self.actions_adv_cli_access_cmd_output)

    def get_cell_href(self, cell):
        return self.weh.get_element(self.device360_cells_href, parent=cell)

    def get_device_active_clients_grid(self):
        return self.weh.get_element(self.device_active_clients_grid)

    def get_device_active_clients_grid_rows(self, cell):
        return self.weh.get_elements(self.device_active_clients_grid_rows, parent=cell)

    def get_utilities_status_wifi_status_summary(self):
        return self.weh.get_element(self.utilities_status_wifi_status_summary)

    def get_utilities_status_interface_name_dropdown(self):
        return self.weh.get_element(self.utilities_status_interface_name_dropdown)

    def get_utilities_status_interface_name_dropdown_opt(self):
        return self.weh.get_elements(self.utilities_status_interface_name_dropdown_opt)

    def get_utilities_status_interface_contents(self):
        return self.weh.get_element(self.utilities_status_interface_contents)

    def get_utilities_status_adv_channel_sel_contents(self):
        return self.weh.get_element(self.utilities_status_adv_channel_sel_contents)

    def get_utilities_status_wifi_summary_station_btn(self):
        return self.weh.get_element(self.utilities_status_wifi_summary_station_btn)

    def get_utilities_status_wifi_summary_station_content(self):
        return self.weh.get_element(self.utilities_status_wifi_summary_station_content)

    def get_device360_configure_button(self):
        return self.weh.get_element(self.device360_configure_button)

    def get_device360_configure_ssh_cli_tab(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_tab)

    def get_device360_configure_ssh_web_tab(self):
        return self.weh.get_element(self.device360_configure_ssh_web_tab)

    def get_device360_configure_ssh_cli_5min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_5min_radio)

    def get_device360_configure_ssh_cli_30min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_30min_radio)

    def get_device360_configure_ssh_cli_60min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_60min_radio)

    def get_device360_configure_ssh_cli_120min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_120min_radio)

    def get_device360_configure_ssh_cli_240min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_240min_radio)

    def get_device360_configure_ssh_cli_enable_button(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_enable_button)

    def get_device360_configure_ssh_cli_ip(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_ip).text

    def get_device360_configure_ssh_cli_port(self):
        return self.weh.get_element(self.device360_configure_ssh_cli_port).text

    def get_device360_configure_ssh_web_enable_button(self):
        return self.weh.get_element(self.device360_configure_ssh_web_enable_button)

    def get_device360_configure_ssh_web_disable_button(self):
        return self.weh.get_element(self.device360_configure_ssh_web_disable_button)

    def get_device360_configure_ssh_web_url(self):
        return self.weh.get_element(self.device360_configure_ssh_web_url).text

    def get_device360_configure_ssh_web_ip(self):
        return self.weh.get_element(self.device360_configure_ssh_web_ip).text

    def get_device360_configure_ssh_web_port(self):
        return self.weh.get_element(self.device360_configure_ssh_web_port).text

    def get_device360_configure_ssh_web_5min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_web_5min_radio)

    def get_device360_configure_ssh_web_30min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_web_30min_radio)

    def get_device360_configure_ssh_web_60min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_web_60min_radio)

    def get_device360_configure_ssh_web_120min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_web_120min_radio)

    def get_device360_configure_ssh_web_240min_radio(self):
        return self.weh.get_element(self.device360_configure_ssh_web_240min_radio)

    def get_device360_device_configuration_button(self):
        return self.weh.get_element(self.device360_device_configuration_button)

    def get_device360_configure_device_host_name(self):
        return self.weh.get_element(self.device360_configure_device_host_name)

    def get_device360_configure_device_snmp_location(self):
        return self.weh.get_element(self.device360_configure_device_snmp_location)

    def get_device360_configure_device_network_policy(self):
        return self.weh.get_element(self.device360_configure_device_network_policy)

    def get_device360_configure_device_device_template(self):
        return self.weh.get_element(self.device360_configure_device_device_template)

    def get_device360_configure_device_cancel_button(self):
        return self.weh.get_element(self.device360_configure_device_cancel_button)

    def get_device360_configure_device_save_button(self):
        return self.weh.get_element(self.device360_configure_device_save_button)

    def get_device360_port_configuration_button(self):
        return self.weh.get_element(self.device360_port_configuration_button)

    def get_device360_port_configuration_title(self):
        return self.weh.get_element(self.device360_port_configuration_title)

    def get_device_info_ip_address(self):
        return self.weh.get_element(self.device_info_ip_address)

    def get_device_info_mac_address(self):
        return self.weh.get_element(self.device_info_mac_address)

    def get_device_info_software_version(self):
        return self.weh.get_element(self.device_info_software_version)

    def get_device_info_model(self):
        return self.weh.get_element(self.device_info_model)

    def get_device_info_serial(self):
        return self.weh.get_element(self.device_info_serial)

    def get_device_info_make(self):
        return self.weh.get_element(self.device_info_make)

    def get_device_info_iqagent_version(self):
        return self.weh.get_element(self.device_info_iqagent_version)

    def get_device_info_device_policy(self):
        return self.weh.get_element(self.device_info_device_policy)

    def get_device360_configure_ssh_disable_button(self):
        return self.weh.get_element(self.device360_configure_ssh_disable_button)

    def get_device360_events_link(self):
        return self.weh.get_element(self.device360_events_link)

    def get_device360_events_grid(self):
        """
        :return: Device360 Events grid
        """
        return self.weh.get_element(self.device360_events_grid)

    def get_device360_events_grid_rows(self, table):
        """
        :return: all the rows in the specified Device360 Events grid
        """
        return self.weh.get_elements(self.device360_events_grid_rows, parent=table)

    def get_device360_events_grid_cells(self, row):
        """
        :return: all the cells in the Device360 Events grid for the specified row
        """
        return self.weh.get_elements(self.device360_events_grid_cells, parent=row)

    def get_device360_event_timestamp_cell_value(self, row):
        """
        :return: value of the time stamp cell in the Device360 Events grid for the specified row
        """
        el = self.weh.get_element(self.device360_event_timestamp, parent=row)
        return el.get_attribute("innerText")

    def get_device360_event_description_cell_value(self, row):
        """
        :return: value of the description cell in the Device360 Events grid for the specified row
        """
        el = self.weh.get_element(self.device360_event_description, parent=row)
        return el.get_attribute("innerText")

    def get_device360_event_severity_cell_value(self, row):
        """
        :return: value of the description cell in the Device360 Events grid for the specified row
        """
        el = self.weh.get_element(self.device360_event_severity, parent=row)
        return el.get_attribute("innerText")

    def get_device360_alarms_link(self):
        return self.weh.get_element(self.device360_alarms_link)

    def get_device360_alarms_grid(self):
        """
        :return: Device360 Alarms grid
        """
        return self.weh.get_element(self.device360_alarms_grid)

    def get_device360_alarms_grid_rows(self, table):
        """
        :return: all the rows in the specified Device360 Alarms grid
        """
        return self.weh.get_elements(self.device360_alarms_grid_rows, parent=table)

    def get_device360_alarms_grid_cells(self, row):
        """
        :return: all the cells in the Device360 Alarms grid for the specified row
        """
        return self.weh.get_elements(self.device360_alarms_grid_cells, parent=row)

    def get_device360_alarm_timestamp_cell_value(self, row):
        """
        :return: value of the time stamp cell in the Device360 Alarms grid for the specified row
        """
        el = self.weh.get_element(self.device360_alarm_timestamp, parent=row)
        return el.get_attribute("innerText")

    def get_device360_alarm_category_cell_value(self, row):
        """
        :return: value of the category cell in the Device360 Alarms grid for the specified row
        """
        el = self.weh.get_element(self.device360_alarm_category, parent=row)
        return el.get_attribute("innerText")

    def get_device360_configure_port_list(self):
        return self.weh.get_element(self.device360_configure_port_list)

    def get_device360_configure_port_rows(self):
        return self.weh.get_elements(self.device360_configure_port_rows)

    def get_device360_configure_port_row_cells(self, row):
        """
        :return: port configuration row cell elements
        """
        return self.weh.get_elements(self.device360_configure_port_row_cells, row)

    def get_device360_configure_port_row_state_toggle(self, row):
        """
        :return: returns the port state toggle control for the specified row
        """
        return self.weh.get_element(self.device360_configure_port_row_state_toggle, row)

    def get_device360_configure_port_row_state_enabled(self, row):
        """
        :return: returns the cell if the row has an enabled port state
        """
        return self.weh.get_element(self.device360_configure_port_row_state_enabled, row)

    def get_device360_configure_port_row_state_disabled(self, row):
        """
        :return: returns the cell if the row has an disabled port state
        """
        return self.weh.get_element(self.device360_configure_port_row_state_disabled, row)

    def get_device360_configure_port_save_button(self):
        """
        :return: returns the 'Save Port Configuration' button in the Port Configuration view
        """
        elements = self.weh.get_elements(self.device360_configure_port_save_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_refresh_page_button(self):
        """
        :return: returns the 'Refresh Page' button for the Device 360 view
        """
        elements = self.weh.get_elements(self.device360_refresh_page_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_monitor_button(self):
        return self.weh.get_element(self.device360_monitor_button)

    def get_device360_monitor_overview_button(self):
        return self.weh.get_element(self.device360_monitor_overview_button)

    def get_device360_switch_system_info_button(self):
        return self.weh.get_element(self.device360_switch_system_info_button)

    def get_device360_monitor_clients_button(self):
        return self.weh.get_element(self.device360_monitor_clients_button)

    def get_device360_monitor_diagnostics_button(self):
        return self.weh.get_element(self.device360_monitor_diagnostics_button)

    def get_device360_time_range_drop_down(self):
        """
        :return: Time Range drop down for the device360 view
        """
        elements = self.weh.get_elements(self.device360_time_range_drop_down)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_time_range_drop_down_selection(self):
        """
        :return: Time Range drop down selection for the device360 view
        """
        elements = self.weh.get_elements(self.device360_time_range_drop_down_selection)
        for el in elements:
            if el.is_displayed():
                return el.text

    def get_device360_time_range_drop_down_items(self):
        """
        :return: drop down items for the device360 Time Range drop down
        """
        return self.weh.get_elements(self.device360_time_range_drop_down_items)

    def get_device360_day_time_range_one_hour_button(self):
        """
        :return: Day Time Range "1 Hour" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_day_time_range_one_hour_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_day_time_range_two_hour_button(self):
        """
        :return: Day Time Range "2 Hours" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_day_time_range_two_hour_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_day_time_range_four_hour_button(self):
        """
        :return: Day Time Range "4 Hours" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_day_time_range_four_hour_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_day_time_range_eight_hour_button(self):
        """
        :return: Day Time Range "8 Hours" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_day_time_range_eight_hour_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_day_time_range_twenty_four_hour_button(self):
        """
        :return: Day Time Range "24 Hours" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_day_time_range_twenty_four_hour_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_week_time_range_one_day_button(self):
        """
        :return: Week Time Range "1 Day" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_week_time_range_one_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_week_time_range_two_days_button(self):
        """
        :return: Week Time Range "2 Days" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_week_time_range_two_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_week_time_range_seven_days_button(self):
        """
        :return: Week Time Range "7 Days" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_week_time_range_seven_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_month_time_range_seven_days_button(self):
        """
        :return: Month Time Range "7 Days" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_month_time_range_seven_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_month_time_range_fourteen_days_button(self):
        """
        :return: Month Time Range "14 Days" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_month_time_range_fourteen_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_month_time_range_thirty_days_button(self):
        """
        :return: Month Time Range "30 Days" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_month_time_range_thirty_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_month_time_range_ninety_days_button(self):
        """
        :return: Month Time Range "90 Days" button in the device360 view
        """
        elements = self.weh.get_elements(self.device360_month_time_range_ninety_day_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_device360_port_diagnostics_select_all_ports_button(self):
        """
        :return: 'Select All Ports' button of the Port Diagnostics page in the device360 view
        """
        return self.weh.get_element(self.device360_port_diagnostics_select_all_ports_button)

    def get_device360_port_diagnostics_deselect_all_ports_button(self):
        """
        :return: 'Deselect All Ports' button of the Port Diagnostics page in the device360 view
        """
        return self.weh.get_element(self.device360_port_diagnostics_deselect_all_ports_button)

    def get_device360_port_diagnostics_selected_ports(self):
        """
        :return: list of selected ports on the Port Diagnostics page in the device360 view
        """
        port_list = []
        elements = self.weh.get_elements(self.device360_port_diagnostics_selected_ports)
        if elements:
            for el in elements:
                if el.is_displayed():
                    port_list.append(el)
        return port_list

    def get_device360_port_diagnostics_deselected_ports(self):
        """
        :return: list of deselected ports on the Port Diagnostics page in the device360 view
        """
        port_list = []
        elements = self.weh.get_elements(self.device360_port_diagnostics_deselected_ports)
        if elements:
            for el in elements:
                if el.is_displayed():
                    port_list.append(el)
        return port_list

    def get_device360_monitor_overview_chart_graph(self):
        """
        :return: chart graph of the Monitor> Overview page in the device360 view
        """
        return self.weh.get_element(self.device360_monitor_overview_chart_graph)

    def get_device360_monitor_clients_chart_graph(self):
        """
        :return: chart graph of the Monitor> Clients page in the device360 view
        """
        return self.weh.get_element(self.device360_monitor_clients_chart_graph)

    def get_device360_monitor_diagnostics_chart_graph(self):
        """
        :return: Top chart graph of the Monitor> Port Diagnostics page in the device360 view
        """
        # There is currently no unique identifier for the top graph; obtain the three graphs and return the first
        graphs = self.weh.get_elements(self.device360_monitor_diagnostics_chart_graph)
        if graphs:
            return graphs[0]
        else:
            return None

    def get_device360_monitor_diagnostics_chart_graph_port_errors(self):
        """
        :return: Errors chart graph of the Monitor> Port Diagnostics page in the device360 view
        """
        return self.weh.get_element(self.device360_monitor_diagnostics_chart_graph_port_errors)

    def get_device360_monitor_diagnostics_chart_graph_port_casts(self):
        """
        :return: Uni-, Multi-, and Broadcasts chart graph of the Monitor> Port Diagnostics page in the device360 view
        """
        return self.weh.get_element(self.device360_monitor_diagnostics_chart_graph_port_casts)

    def get_overview_ip_address(self):
        return self.weh.get_element(self.overview_ip_address)

    def get_overview_mac_address(self):
        return self.weh.get_element(self.overview_mac_address)

    def get_overview_software_version(self):
        return self.weh.get_element(self.overview_software_version)

    def get_overview_model(self):
        return self.weh.get_element(self.overview_model)

    def get_overview_serial(self):
        return self.weh.get_element(self.overview_serial)

    def get_overview_make(self):
        return self.weh.get_element(self.overview_make)

    def get_device360_configure_device_function_dropdown(self):
        return self.weh.get_element(self.device360_configure_device_function_dropdown)

    def get_device360_configure_device_function_dropdown_items(self):
        """
        :return: device function drop down items for the Device Configuration tab in the Device 360 view
        """
        parent = self.get_device360_configure_device_function_dropdown()
        return self.weh.get_elements(self.device360_configure_device_function_dropdown_items, parent)

    def get_device360_device_title(self):
        """
        :return: device title element in the Device 360 view
        """
        return self.weh.get_element(self.device360_device_title)

    def get_sidebar_model(self):
        return self.weh.get_element(self.device360_sidebar_model)

    def get_sidebar_device_image(self):
        return self.weh.get_element(self.device360_sidebar_device_image)

    def get_sidebar_host_name(self):
        return self.weh.get_element(self.device360_sidebar_host_name)

    def get_sidebar_enabled_ports(self):
        return self.weh.get_element(self.device360_sidebar_enabled_ports)

    def get_sidebar_disabled_ports(self):
        return self.weh.get_element(self.device360_sidebar_disabled_ports)

    def get_sidebar_connected_state(self):
        return self.weh.get_element(self.device360_sidebar_connected_state)

    def get_sidebar_active_since(self):
        return self.weh.get_element(self.device360_sidebar_active_since)

    def get_sidebar_active_alarms(self):
        return self.weh.get_element(self.device360_sidebar_active_alarms)

    def get_sidebar_unique_clients(self):
        return self.weh.get_element(self.device360_sidebar_unique_clients)

    def get_sidebar_cpu_usage(self):
        return self.weh.get_element(self.device360_sidebar_cpu_usage)

    def get_sidebar_memory_usage(self):
        return self.weh.get_element(self.device360_sidebar_memory_usage)

    def get_tooltip_content(self):
        return self.weh.get_element(self.device360_tooltip_content)

    def get_topbar_cpu(self):
        elements = self.weh.get_elements(self.device360_topbar_cpu)
        for el in elements:
            if el.is_displayed():
                return el

    def get_topbar_memory(self):
        elements = self.weh.get_elements(self.device360_topbar_memory)
        for el in elements:
            if el.is_displayed():
                return el

    def get_topbar_mac_usage(self):
        return self.weh.get_element(self.device360_topbar_mac_usage)

    def get_topbar_uptime(self):
        return self.weh.get_element(self.device360_topbar_uptime)

    def get_topbar_temperature(self):
        return self.weh.get_element(self.device360_topbar_temperature)

    def get_topbar_power(self):
        return self.weh.get_element(self.device360_topbar_power)

    def get_topbar_fan(self):
        return self.weh.get_element(self.device360_topbar_fan)

    def get_topbar_ip_address(self):
        return self.weh.get_element(self.device360_topbar_ip_address)

    def get_topbar_mac_address(self):
        return self.weh.get_element(self.device360_topbar_mac_address)

    def get_topbar_software_version(self):
        return self.weh.get_element(self.device360_topbar_software_version)

    def get_topbar_model(self):
        return self.weh.get_element(self.device360_topbar_model)

    def get_topbar_serial(self):
        return self.weh.get_element(self.device360_topbar_serial)

    def get_topbar_make(self):
        return self.weh.get_element(self.device360_topbar_make)

    def get_device360_open_site_engine_link(self):
        return self.weh.get_element(self.device360_open_site_engine_link)

    def get_overview_port_icons(self):
        port_list = []
        elements = self.weh.get_elements(self.device360_overview_port_icons)
        if elements:
            for el in elements:
                if el.is_displayed():
                    port_list.append(el)
        return port_list

    def get_overview_port_details_table(self):
        return self.weh.get_element(self.device360_overview_port_details_table)

    def get_overview_total_active_alarms(self):
        return self.weh.get_element(self.device360_overview_total_active_alarms)

    def get_system_info_device_ssids(self):
        return self.weh.get_element(self.system_info_device_ssids)

    # Elements on the System Information page for a switch
    def get_switch_system_info_archived(self):
        return self.weh.get_element(self.switch_system_info_archived)

    def get_switch_system_info_asset_tag(self):
        return self.weh.get_element(self.switch_system_info_asset_tag)

    def get_switch_system_info_user_data_1(self):
        return self.weh.get_element(self.switch_system_info_user_data_1)

    def get_switch_system_info_user_data_2(self):
        return self.weh.get_element(self.switch_system_info_user_data_2)

    def get_switch_system_info_user_data_3(self):
        return self.weh.get_element(self.switch_system_info_user_data_3)

    def get_switch_system_info_user_data_4(self):
        return self.weh.get_element(self.switch_system_info_user_data_4)

    def get_switch_system_info_note(self):
        return self.weh.get_element(self.switch_system_info_note)

    def get_hyper_link_system_information(self, row):
        return self.weh.get_element(self.hyper_link_device_template, row)

    def get_switch_sidebar_active_alarms(self):
        return self.weh.get_element(self.device360_switch_sidebar_active_alarms)

    def get_switch_sidebar_unique_clients(self):
        return self.weh.get_element(self.device360_switch_sidebar_unique_clients)

    def get_device360_stack_configure_device_snmp_location(self):
        return self.weh.get_element(self.device360_stack_configure_device_snmp_location)

    def get_device360_dev_config_save_button(self):
        return self.weh.get_element(self.device360_dev_config_save_button)
      
    def get_device360_title_stack_info(self):
        """
        :return: stack info present in title element in the Device 360 view
        """
        return self.weh.get_element(self.device360_title_stack_info)

    def get_stack_members_status(self):
        """
        :return: a list of stack members elements in the Device 360 view
        """
        stack_members = []
        elements = self.weh.get_elements(self.device360_topbar_stack_mem_status)
        if elements:
            for el in elements:
                if el.is_displayed():
                    stack_members.append(el)
        return stack_members

    def get_stack_topbar_mac_usage(self):
        return self.weh.get_elements(self.device360_topbar_mac_usage)

    def get_stack_topbar_uptime(self):
        return self.weh.get_elements(self.device360_topbar_uptime)

    def get_stack_topbar_temperature(self):
        return self.weh.get_elements(self.device360_topbar_temperature)

    def get_stack_topbar_power(self):
        return self.weh.get_elements(self.device360_stack_topbar_power)

    def get_stack_topbar_fan(self):
        return self.weh.get_elements(self.device360_stack_topbar_fan)

    def get_fan_tooltip_content(self):
        return self.weh.get_element(self.device360_fan_tooltip_content)

    def get_stack_topbar_ip_address(self):
        return self.weh.get_elements(self.device360_topbar_ip_address)

    def get_stack_topbar_mac_address(self):
        return self.weh.get_elements(self.device360_topbar_mac_address)

    def get_stack_topbar_software_version(self):
        return self.weh.get_elements(self.device360_topbar_software_version)

    def get_stack_topbar_model(self):
        return self.weh.get_elements(self.device360_topbar_model)

    def get_stack_topbar_serial(self):
        return self.weh.get_elements(self.device360_topbar_serial)

    def get_stack_topbar_make(self):
        return self.weh.get_elements(self.device360_topbar_make)

    def get_stack_topbar_iqagent_version(self):
        return self.weh.get_elements(self.device360_topbar_iqagent_version)

    def get_stack_topbar_stack_mem_status(self):
        return self.weh.get_elements(self.device360_topbar_stack_mem_status)

    def get_stack_system_info_button(self):
        return self.weh.get_element(self.device360_stack_system_info_button)

    def get_stack_system_info_unit_number(self):
        return self.weh.get_elements(self.stack_system_info_unit_number)

    def get_stack_system_info_ip_address(self):
        return self.weh.get_elements(self.stack_system_info_ip_address)

    def get_stack_system_info_netmask(self):
        return self.weh.get_elements(self.stack_system_info_netmask)

    def get_stack_system_info_mac(self):
        return self.weh.get_elements(self.stack_system_info_mac)

    def get_stack_system_info_serial_num(self):
        return self.weh.get_elements(self.stack_system_info_serial_num)

    def get_stack_system_info_prod_type(self):
        return self.weh.get_elements(self.stack_system_info_prod_type)

    def get_stack_system_info_make(self):
        return self.weh.get_elements(self.stack_system_info_make)

    def get_stack_system_info_admin_state(self):
        return self.weh.get_elements(self.stack_system_info_admin_state)

    def get_stack_system_info_software_ver(self):
        return self.weh.get_elements(self.stack_system_info_software_ver)

    def get_stack_system_info_stack_mgmt_status(self):
        return self.weh.get_elements(self.stack_system_info_stack_mgmt_status)

    def get_stack_overview_port_icons(self):
        port_list = []
        elements = self.weh.get_elements(self.device360_stack_overview_port_icons)
        if elements:
            for el in elements:
                if el.is_displayed():
                    port_list.append(el)
        return port_list

    def get_stack_overview_slot_ports_row(self):
        return self.weh.get_elements(self.device360_stack_overview_sl_ports_row)

    def get_stack_overview_select_port(self):
        return self.weh.get_elements(self.device360_stack_overview_sl_ports_row)

    def get_device360_stack_overview_slot_ports(self, row):
        return self.weh.get_elements(self.device360_stack_overview_slot_ports, parent=row)

    def get_device360_stack_port_table_port_name(self):
        return self.weh.get_element(self.device360_stack_port_table_port_name)

    def get_device360_stack_port_table_port_type(self):
        return self.weh.get_element(self.device360_stack_port_table_port_type)

    def get_device360_stack_port_table_port_status(self):
        return self.weh.get_element(self.device360_stack_port_table_port_status)

    def get_device360_stack_port_table_port_mode(self):
        return self.weh.get_element(self.device360_stack_port_table_port_mode)

    def get_device360_stack_port_table_port_speed(self):
        return self.weh.get_element(self.device360_stack_port_table_port_speed)

    def get_sw_template_stack_add_items(self):
        return self.weh.get_elements(self.sw_template_stack_add_items)

    def get_sw_template_stack_added_items(self):
        return self.weh.get_elements(self.sw_template_stack_added_items)

    def get_sw_template_stack_first_page(self):
        return self.weh.get_elements(self.sw_template_stack_first_page)

    def get_device360_device_configuration_stack_template_button(self):
        return self.weh.get_element(self.device360_device_configuration_stack_template_button)

    def get_device360_device_configuration_stack_template_items(self):
        return self.weh.get_elements(self.device360_device_configuration_stack_template_items)

    def get_device360_device_configuration_save_button(self):
        elements = self.weh.get_elements(self.device360_device_configuration_save_button)
        for el in elements:
            if el.is_displayed():
                return el
        else:
            return False

    def get_device360_device_configuration_update_button(self):
        return self.weh.get_element(self.device360_device_configuration_update_button)

    def get_device360_device_configuration_exit_button(self):
        return self.weh.get_element(self.device360_device_configuration_exit_button)

    def get_d360Event_search_textbox(self):
        return self.weh.get_element(self.d360Event_search_textbox)

    def get_device360_configure_vlan_port_one(self):
        return self.weh.get_element(self.device360_configure_vlan_port_one)
    
    def get_d360_configure_port_row_override_revert(self, row):
        return self.weh.get_element(self.d360_configure_port_row_override_revert, row)

    def get_d360_configure_port_row_revert_button(self, row):
        return self.weh.get_element(self.d360_configure_port_row_revert_button, row)

    def get_device360_configure_port_settings_aggregation_rows(self):
        return self.weh.get_elements(self.device360_configure_port_settings_aggregation_rows)

    def get_device360_configure_stp_rows(self):
        return self.weh.get_elements(self.device360_configure_stp_rows)

    def get_device360_configure_storm_control_rows(self):
        return self.weh.get_elements(self.device360_configure_storm_control_rows)

    def get_d360_configure_port_details_settings_aggregation_stp_storm_control_row_override_revert(self, select, row):

        # Port Details

        if select == 'port state':
            return self.weh.get_element(self.d360_configure_port_state_override_revert, row)

        if select == 'port usage':
            return self.weh.get_element(self.d360_configure_port_usage_override_revert, row)

        if select == 'vlan':
            return self.weh.get_element(self.d360_configure_vlan_override_revert, row)

        if select == 'description':
            return self.weh.get_element(self.d360_configure_description_override_revert, row)

        # Port Settings & Aggregation

        if select == 'transmission':
            return self.weh.get_element(self.d360_configure_transmission_override_revert, row)

        if select == 'speed':
            return self.weh.get_element(self.d360_configure_speed_override_revert, row)

        if select == 'flow':
            return self.weh.get_element(self.d360_configure_flow_override_revert, row)

        if select == 'transmit':
            return self.weh.get_element(self.d360_configure_transmit_override_revert, row)

        if select == 'receive':
            return self.weh.get_element(self.d360_configure_receive_override_revert, row)

        if select == 'cdp':
            return self.weh.get_element(self.d360_configure_cdp_override_revert, row)

        if select == 'client reporting':
            return self.weh.get_element(self.d360_configure_client_reporting_override_revert, row)

        # STP

        if select == 'stp status':
            return self.weh.get_element(self.d360_configure_stp_status_override_revert, row)

        if select == 'edge port':
            return self.weh.get_element(self.d360_configure_edge_port_override_revert, row)

        if select == 'bpdu protection':
            return self.weh.get_element(self.d360_configure_bpdu_protection_override_revert, row)

        if select == 'priority':
            return self.weh.get_element(self.d360_configure_priority_override_revert, row)

        if select == 'path cost':
            return self.weh.get_element(self.d360_configure_path_cost_override_revert, row)

        # Storm Control

        if select == 'broadcast':
            return self.weh.get_element(self.d360_configure_broadcast_override_revert, row)

        if select == 'unknown unicast':
            return self.weh.get_element(self.d360_configure_unknown_unicast_override_revert, row)

        if select == 'multicast':
            return self.weh.get_element(self.d360_configure_multicast_override_revert, row)

        if select == 'value':
            return self.weh.get_element(self.d360_configure_value_override_revert, row)

        return -1

    def get_d360_configure_port_details_tab_button(self):
        return self.weh.get_element(self.d360_configure_port_details_tab_button)

    def get_d360_configure_port_settings_aggregation_tab_button(self):
        return self.weh.get_element(self.d360_configure_port_settings_aggregation_tab_button)

    def get_d360_configure_port_stp_tab_button(self):
        return self.weh.get_element(self.d360_configure_port_stp_tab_button)

    def get_d360_configure_port_storm_control_tab_button(self):
        return self.weh.get_element(self.d360_configure_port_storm_control_tab_button)

    def get_d360_configure_port_details_settings_aggregation_stp_storm_control_row_click_on_checkbox_or_button(self, select, row):
        # Port Details
        if select == 'port state':
            return self.weh.get_element(self.d360_configure_port_state_click_button, row)
        # Port Settings & Aggregation
        if select == 'transmit':
            return self.weh.get_element(self.d360_configure_transmit_click_checkbox, row)
        if select == 'receive':
            return self.weh.get_element(self.d360_configure_receive_click_checkbox, row)
        if select == 'cdp':
            return self.weh.get_element(self.d360_configure_cdp_click_checkbox, row)
        if select == 'client reporting':
            return self.weh.get_element(self.d360_configure_client_reporting_click_checkbox, row)
        # STP
        if select == 'stp status':
            return self.weh.get_element(self.d360_configure_stp_status_click_button, row)
        if select == 'edge port':
            return self.weh.get_element(self.d360_configure_edge_port_click_button, row)
        # Storm Control
        if select == 'broadcast':
            return self.weh.get_element(self.d360_configure_broadcast_click_checkbox, row)
        if select == 'unknown unicast':
            return self.weh.get_element(self.d360_configure_unknown_unicast_click_checkbox, row)
        if select == 'multicast':
            return self.weh.get_element(self.d360_configure_multicast_click_checkbox, row)
        return -1

    def get_d360_switch_port_view_all_pages_button(self):
        return self.weh.get_element(self.d360_switch_port_view_all_pages_button)

    def get_d360_switch_ports_table_grid_rows(self):
        grid_rows = self.weh.get_elements(self.d360_switch_ports_table_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_d360_switch_ports_table_interface_port_name_cell(self, row):
        return self.weh.get_element(self.d360_switch_ports_table_port_name_cell, parent=row)

    def get_device360_switch_port_table_port_name(self, row):
        return self.weh.get_element(self.device360_switch_port_table_port_name, parent=row)

    def get_device360_switch_port_table_port_type(self, row):
        return self.weh.get_element(self.device360_switch_port_table_port_type, parent=row)

    def get_device360_switch_port_table_lacp_neighbor(self, row):
        return self.weh.get_element(self.device360_switch_port_table_lacp_neighbor, parent=row)

    def get_device360_switch_port_table_lacp_status(self, row):
        return self.weh.get_element(self.device360_switch_port_table_lacp_status, parent=row)

    def get_device360_switch_port_table_port_status(self, row):
        return self.weh.get_element(self.device360_switch_port_table_port_status, parent=row)

    def get_device360_switch_port_table_transmission_mode(self, row):
        return self.weh.get_element(self.device360_switch_port_table_transmission_mode, parent=row)

    def get_device360_switch_port_table_port_mode(self, row):
        return self.weh.get_element(self.device360_switch_port_table_port_mode, parent=row)

    def get_device360_switch_port_table_access_vlan(self, row):
        return self.weh.get_element(self.device360_switch_port_table_access_vlan, parent=row)

    def get_device360_switch_port_table_tagged_vlans(self, row):
        return self.weh.get_element(self.device360_switch_port_table_tagged_vlans, parent=row)

    def get_device360_switch_port_table_traffic_received(self, row):
        return self.weh.get_element(self.device360_switch_port_table_traffic_received, parent=row)

    def get_device360_switch_port_table_traffic_transmitted(self, row):
        return self.weh.get_element(self.device360_switch_port_table_traffic_transmitted, parent=row)

    def get_device360_switch_port_table_power_used(self, row):
        return self.weh.get_element(self.device360_switch_port_table_power_used, parent=row)

    def get_device360_switch_port_table_port_speed(self, row):
        return self.weh.get_element(self.device360_switch_port_table_port_speed, parent=row)

    def get_d360_monitor_items_rows(self):
        return self.weh.get_elements(self.d360_monitor_items_rows)

    def get_d360_monitor_transmission_mode(self, row):
        return self.weh.get_element(self.d360_monitor_transmission_mode, row)

    def get_d360_monitor_port_speed(self, row):
        return self.weh.get_element(self.d360_monitor_port_speed, row)

    def get_device360_port_settings_button(self):
        return self.weh.get_element(self.device360_port_settings_button)

    def get_icon_ports_items(self):
        return self.weh.get_elements(self.icon_ports_items)

    def get_port_click(self, el):
        return self.weh.get_element(self.port_click, el)

    def get_d360_interface_transmission_mode(self):
        return self.weh.get_element(self.d360_interface_transmission_mode)

    def get_d360_interface_port_speed(self):
        return self.weh.get_element(self.d360_interface_port_speed)

    def get_d360_view_100_rows_on_page(self):
        return self.weh.get_element(self.d360_view_100_rows_on_page)

    def get_d360_monitor_interface_name(self, row):
        return self.weh.get_element(self.d360_monitor_interface_name, row)

    def get_d360_monitor_lldp_neighbor_header(self):
        return self.weh.get_element(self.d360_monitor_lldp_neighbor_header)

    def get_d360_vim_model(self):
        return self.weh.get_element(self.d360_vim_model)

    def get_d360_vim_ports(self):
        return self.weh.get_elements(self.d360_vim_ports)

    def get_device360_wireframe_port(self):
        port_list = []
        elements = self.weh.get_elements(self.d360_wireframe_port)
        for el in elements:
            if el.is_displayed():
                port_list.append(el)
        return port_list

    def get_device360_automation_port(self):
        port_list = []
        elements = self.weh.get_elements(self.d360_automation_port)
        for el in elements:
            if el.is_displayed():
                port_list.append(el)
        return port_list

    def get_device360_port_leftclick_interface_name(self):
        return self.weh.get_element(self.d360_port_leftclick_interface_name)

    def get_device360_port_leftclick_interface_type(self):
        return self.weh.get_element(self.d360_port_leftclick_interface_type)

    def get_device360_port_leftclick_port_mode(self):
        return self.weh.get_element(self.d360_port_leftclick_port_mode)

    def get_device360_port_leftclick_access_vlan(self):
        return self.weh.get_element(self.d360_port_leftclick_access_vlan)

    def get_device360_port_leftclick_tagged_vlan(self):
        return self.weh.get_element(self.d360_port_leftclick_tagged_vlan)

    def get_device360_port_leftclick_port_status(self):
        return self.weh.get_element(self.d360_port_leftclick_port_status)

    def get_device360_create_auto_template_button(self):
        return self.weh.get_element(self.device360_create_auto_template_button)
      
    def get_device360_pagination_next_button(self):
        return self.weh.get_element(self.d360_pagination_next_button)

    def get_device360_pagination_page_button(self):
        return self.weh.get_element(self.d360_pagination_page_button)

    def get_device360_port_configuration_content(self):
        return self.weh.get_element(self.device360_port_configuration_content)

    def get_policy_configure_port_rows(self):
        return self.weh.get_elements(self.policy_configure_port_rows)

    def get_device360_configure_port_configuration_button(self):
        return self.weh.get_element(self.device360_configure_port_configuration_button)

    def get_sw_template_stack_sw_item(self):
        return self.weh.get_element(self.sw_template_stack_sw_item)

    def get_device360_configure_port_usage_drop_down_button(self, row):
        return self.weh.get_element(self.device360_configure_port_usage_drop_down_button, row)

    def get_device360_configure_port_usage_drop_down_options(self, row):
        return self.weh.get_elements(self.device360_configure_port_usage_drop_down_options, row)

    def get_device360_configure_port_access_vlan_textfield(self, row):
        return self.weh.get_element(self.device360_configure_port_access_vlan_textfield, row)

    def get_device360_configure_onboarding_port_vlan_textfield(self, row):
        return self.weh.get_element(self.device360_configure_onboarding_port_vlan_textfield, row)

    def get_device360_configure_disabled_port_vlan_textfield(self, row):
        return self.weh.get_element(self.device360_configure_disabled_port_vlan_textfield, row)

    def get_device360_configure_port_trunk_native_vlan_textfield(self, row):
        return self.weh.get_element(self.device360_configure_port_trunk_native_vlan_textfield, row)

    def get_device360_configure_port_trunk_vlan_textfield(self, row):
        return self.weh.get_element(self.device360_configure_port_trunk_vlan_textfield, row)

    def get_device360_port_configuration_port_settings_tab(self):
        return self.weh.get_element(self.device360_port_configuration_port_settings_tab)

    def get_device360_port_settings_transmission_mode_drop_down_button(self, row):
        return self.weh.get_element(self.device360_port_settings_transmission_mode_drop_down_button, row)

    def get_device360_port_settings_transmission_mode_drop_down_options(self, row):
        return self.weh.get_elements(self.device360_port_settings_transmission_mode_drop_down_options, row)

    def get_device360_port_settings_speed_drop_down_button(self, row):
        return self.weh.get_element(self.device360_port_settings_speed_drop_down_button, row)

    def get_device360_port_settings_speed_drop_down_options(self, row):
        return self.weh.get_elements(self.device360_port_settings_speed_drop_down_options, row)

    def get_device360_configure_port_pse_poe_state_enabled(self, row):
        return self.weh.get_element(self.device360_configure_port_pse_poe_state_enabled, row)

    def get_device360_configure_port_pse_poe_state_disabled(self, row):
        return self.weh.get_element(self.device360_configure_port_pse_poe_state_disabled, row)

    def get_device360_port_configuration_pse_tab(self):
        return self.weh.get_element(self.device360_port_configuration_pse_tab)

    def get_device360_port_configuration_pse_profile_select_button(self, row):
        return self.weh.get_element(self.device360_port_configuration_pse_profile_select_button, row)

    def get_device360_port_configuration_pse_profile_select_options(self):
        return self.weh.get_elements(self.device360_port_configuration_pse_profile_drop_down_options)

    def get_device360_wireframe_cpu_utilization_tooltip_content(self):
        return self.weh.get_element(self.device360_wireframe_cpu_utilization_tooltip_content)

    def get_device360_wireframe_cpu_utilization_piechart(self):
        return self.weh.get_element(self.device360_wireframe_cpu_utilization_piechart)

    def get_result_area(self):
        return self.weh.get_element(self.result_area)

    def get_advanced_button(self):
        return self.weh.get_elements(self.advanced_button)

    def get_cli_button(self):
        return self.weh.get_element(self.cli_button)

    def get_actions_button(self):
        return self.weh.get_element(self.actions_button)

    def get_cli_command_line(self):
        return self.weh.get_element(self.cli_command_line)

    def get_device_rows(self):
        return self.weh.get_elements(self.device_rows)

    def get_row_check_box(self, row):
        return self.weh.get_element(self.row_check_box, parent=row)

    def get_cli_close_button(self):
        return self.weh.get_element(self.cli_close_button)

    def get_cli_apply(self):
        return self.weh.get_element(self.cli_apply)

    def get_device360_select_supplemental_cli(self):
        return self.weh.get_element(self.device360_select_supplemental_cli)

    def get_device360_supplemental_cli_list(self):
        return self.weh.get_elements(self.device360_supplemental_cli_list)

    def get_device_360_supplemental_cli_new_profile(self):
        return self.weh.get_element(self.device_360_supplemental_cli_new_profile)

    def get_device_360_supplemental_cli_profile_name(self):
        return self.weh.get_element(self.device_360_supplemental_cli_profile_name)

    def get_device_360_supplemental_cli_profile_commands(self):
        return self.weh.get_element(self.device_360_supplemental_cli_profile_commands)

    def get_device360_supplemental_cli_save_profile(self):
        return self.weh.get_element(self.device360_supplemental_cli_save_profile)

    def get_device360_supplemental_cli_edit_profile(self):
        return self.weh.get_element(self.device360_supplemental_cli_edit_profile)

    def get_device360_thunderbold_icon(self):
        return self.weh.get_element(self.device360_thunderbold_icon)

    def get_device360_power_details(self):
        return self.weh.get_element(self.device360_power_details)

    def get_device360_pse_settings_for_device_button(self):
        return self.weh.get_element(self.device360_pse_settings_for_device_button)

    def get_device360_edit_threshold_poe(self):
        return self.weh.get_element(self.device360_edit_threshold_poe)

    def get_device360_device_config_description(self):
        return self.weh.get_element(self.device360_device_configuration_description)

    def get_device360_device_config_mac_address(self):
        return self.weh.get_element(self.device360_device_configuration_mac_address)

    def get_device360_device_config_device_model(self):
        return self.weh.get_element(self.device360_device_configuration_device_model)

    def get_device360_device_config_iq_engine(self):
        return self.weh.get_element(self.device360_device_configuration_iq_engine)

    def get_device360_device_config_override_acsp_network_policy(self):
        return self.weh.get_element(self.device360_device_configuration_override_acsp_network_policy)

    def get_device360_device_config_production_option(self):
        return self.weh.get_element(self.device360_device_configuration_production_option)

    def get_device360_device_config_pre_provision_option(self):
        return self.weh.get_element(self.device360_device_configuration_pre_provision_option)

    def get_device360_device_configuration_device_template(self):
        return self.weh.get_element(self.device360_device_configuration_device_template)

    def get_device360_configure_device_network_policy_items(self):
        return self.weh.get_elements(self.device360_configure_device_network_policy_items)

    def get_device360_configure_dhcp_ip_address_link(self):
        return self.weh.get_element(self.device360_configure_dhcp_ip_address_link)

    def get_device360_configure_subnetworks_tol_cells(self):
        return self.weh.get_elements(self.device360_configure_subnetworks_all_cells)

    def get_device360_configure_subnetworks_header(self):
        return self.weh.get_elements(self.device360_configure_subnetworks_header)

    def get_device360_save_threshold_poe_value(self):
        return self.weh.get_element(self.device360_save_threshold_poe_value)

    def get_device360_click_particular_client(self):
        return self.weh.get_element(self.device360_click_particular_client)

    def get_client360_close_dialog(self):
        return self.weh.get_element(self.close_client360_dialog)

    def get_device360_hyperlink_client(self):
        return self.weh.get_element(self.device360_hyperlink_client)

    def get_device360_column_picker_icon(self):
        elements = self.weh.get_elements(self.device360_column_picker_icon)
        for el in elements:
            if el.is_displayed():
                return el
        else:
            return False

    def get_d360_create_port_type(self, port_row):
        return self.weh.get_element(self.d360_create_port_type, port_row)

    def get_policy_edit_port_type(self, port_row):
        return self.weh.get_element(self.policy_edit_port_type, port_row)

    def get_close_port_type_box(self):
        return self.weh.get_element(self.close_port_type_box)

    def get_select_element_port_type(self, element, value=None):
        if element == "tab_vlan":
            return self.weh.get_element(self.select_element_port_type_tab_vlan)
        elif element == "usagePage":
            return self.weh.get_element(self.select_element_port_type_tab_usage)
        elif element == "transmissionSettingsPage":
            return self.weh.get_element(self.select_element_port_type_tab_transmission)
        elif element == "stpPage":
            return self.weh.get_element(self.select_element_port_type_tab_stp)
        elif element == "stormControlSettingsPage":
            return self.weh.get_element(self.select_element_port_type_tab_storm_control)
        elif element == "pseSettingsPage":
            return self.weh.get_element(self.select_element_port_type_tab_pse_settings)
        elif element == "summaryPage":
            return self.weh.get_element(self.select_element_port_type_tab_summary)
        elif element == "elrdp":
            return self.weh.get_element(self.select_element_port_type_name)
        # page Port Name
        elif element == "name":
            return self.weh.get_element(self.select_element_port_type_name)
        elif element == "description":
            return self.weh.get_element(self.select_element_port_type_description)
        elif element == "status":
            return self.weh.get_element(self.select_element_port_type_status)
        elif element == "auto-sense":
            return self.weh.get_element(self.select_element_port_type_auto_sense)
        elif element == "port usage" and value == "access port":
            return self.weh.get_element(self.select_element_port_type_port_usage_access)
        elif element == "port usage" and value == "trunk port":
            return self.weh.get_element(self.select_element_port_type_port_usage_trunk)
        # page Access Vlan
        elif element == "next_button":
            return self.weh.get_element(self.select_element_port_type_next_button)
        elif element == "add_vlan":
            return self.weh.get_element(self.select_element_port_type_vlan_add_vlan)
        elif element == "name_vlan":
            return self.weh.get_element(self.select_element_port_type_vlan_name_vlan)
        elif element == "id_vlan":
            return self.weh.get_element(self.select_element_port_type_vlan_id_vlan)
        elif element == "select_button":
            return self.weh.get_element(self.select_element_port_type_vlan_select_button)
        elif element == "dropdown_items":
            return self.weh.get_elements(self.select_element_port_type_vlan_dropdown_items)
        # page Trunk vlan
        elif element == "native_vlan_add_vlan":
            return self.weh.get_element(self.select_element_port_type_native_vlan_add_vlan)
        elif element == "native_vlan_name_vlan":
            return self.weh.get_element(self.select_element_port_type_native_vlan_name_vlan)
        elif element == "native_vlan_id_vlan":
            return self.weh.get_element(self.select_element_port_type_native_vlan_id_vlan)
        elif element == "native_vlan_select_button":
            return self.weh.get_element(self.select_element_port_type_native_vlan_select_button)
        elif element == "native_vlan_dropdown_items":
            return self.weh.get_elements(self.select_element_port_type_native_vlan_dropdown_items)
        elif element == "save_vlan":
            return self.weh.get_element(self.select_element_port_type_save_vlan)
        elif element == "allowed vlans":
            return self.weh.get_element(self.select_element_port_type_allowed_vlans)
        # page Transmission
        elif element == "transmission type":
            return self.weh.get_element(self.select_element_port_type_transmission_type)
        elif element == "transmission_type_dropdown_items":
            return self.weh.get_elements(self.select_element_port_type_transmission_type_dropdown_items)
        elif element == "transmission speed":
            return self.weh.get_element(self.select_element_port_type_transmission_speed)
        elif element == "transmission_speed_dropdown_items":
            return self.weh.get_elements(self.select_element_port_type_transmission_speed_dropdown_items)
        elif element == "cdp receive":
            return self.weh.get_element(self.select_element_port_type_cdp_receive)
        elif element == "lldp transmit":
            return self.weh.get_element(self.select_element_port_type_lldp_transmit)
        elif element == "lldp receive":
            return self.weh.get_element(self.select_element_port_type_lldp_receive)
        # page STP
        elif element == "stp enable":
            return self.weh.get_element(self.select_element_port_type_stp_enable)
        elif element == "edge port":
            return self.weh.get_element(self.select_element_port_type_edge_port)
        elif element == "bpdu protection":
            return self.weh.get_element(self.select_element_port_type_bpdu_protection)
        elif element == "bpdu_protection_items":
            return self.weh.get_elements(self.select_element_port_type_bpdu_protection_items)
        elif element == "priority":
            return self.weh.get_element(self.select_element_port_type_priority)
        elif element == "priority_items":
            return self.weh.get_elements(self.select_element_port_type_priority_items)
        elif element == "path cost":
            return self.weh.get_element(self.select_element_port_type_path_cost)
        # page Storm
        elif element == "broadcast":
            return self.weh.get_element(self.select_element_port_type_broadcast)
        elif element == "unknown unicast":
            return self.weh.get_element(self.select_element_port_type_unknown_unicast)
        elif element == "multicast":
            return self.weh.get_element(self.select_element_port_type_multicast)
        elif element == "rate limit value":
            return self.weh.get_element(self.select_element_port_type_rate_limit_value)
        # page ELRP (ONLY FOR EXOS)
        elif element == "elrp status":
            return self.weh.get_element(self.select_element_port_type_elrp_status)
        # page PSE
        elif element == "pse profile":
            return self.weh.get_element(self.select_element_port_type_pse_profile)
        elif element == "pse_profile_items":
            return self.weh.get_elements(self.select_element_port_type_pse_profile_items)
        elif element == "pse_profile_add":
            return self.weh.get_element(self.select_element_port_type_pse_profile_add)
        elif element == "pse_profile_name":
            return self.weh.get_element(self.select_element_port_type_pse_profile_name)
        elif element == "pse_profile_power_mode_items":
            return self.weh.get_elements(self.select_element_port_type_pse_profile_power_mode_items)
        elif element == "pse_profile_priority":
            return self.weh.get_element(self.select_element_port_type_pse_profile_priority)
        elif element == "pse_profile_priority_items":
            return self.weh.get_elements(self.select_element_port_type_pse_profile_priority_items)
        elif element == "pse_profile_description":
            return self.weh.get_elements(self.select_element_port_type_pse_profile_description)
        elif element == "pse_profile_save":
            return self.weh.get_elements(self.select_element_port_type_pse_profile_save)
        elif element == "poe status":
            return self.weh.get_element(self.select_element_port_type_poe_status)
        return -1

    def get_select_element_port_type_summary(self, element):
        if element == "name":
            return self.weh.get_element(self.select_element_port_type_name_summary)
        elif element == "description":
            return self.weh.get_element(self.select_element_port_type_description_summary)
        elif element == "status":
            return self.weh.get_element(self.select_element_port_type_status_summary)
        elif element == "port usage":
            return self.weh.get_element(self.select_element_port_type_port_usage_access_summary)
        elif element == "vlan":
            return self.weh.get_element(self.select_element_port_type_vlan_summary)
        elif element == "native vlan":
            return self.weh.get_element(self.select_element_port_type_native_vlan_summary)
        elif element == "allowed vlans":
            return self.weh.get_element(self.select_element_port_type_allowed_vlans_summary)
        elif element == "transmission type":
            return self.weh.get_element(self.select_element_port_type_transmission_type_summary)
        elif element == "transmission speed":
            return self.weh.get_element(self.select_element_port_type_transmission_speed_summary)
        elif element == "cdp receive":
            return self.weh.get_element(self.select_element_port_type_cdp_receive_summary)
        elif element == "lldp transmit":
            return self.weh.get_element(self.select_element_port_type_lldp_transmit_summary)
        elif element == "lldp receive":
            return self.weh.get_element(self.select_element_port_type_lldp_receive_summary)
        elif element == "stp":
            return self.weh.get_element(self.select_element_port_type_stp_summary)
        elif element == "edge port":
            return self.weh.get_element(self.select_element_port_type_edge_port_summary)
        elif element == "bpdu protection":
            return self.weh.get_element(self.select_element_port_type_bpdu_protection_summary)
        elif element == "priority":
            return self.weh.get_element(self.select_element_port_type_priority_summary)
        elif element == "path cost":
            return self.weh.get_element(self.select_element_port_type_path_cost_summary)
        elif element == "broadcast":
            return self.weh.get_element(self.select_element_port_type_broadcast_summary)
        elif element == "unknown unicast":
            return self.weh.get_element(self.select_element_port_type_unknown_unicast_summary)
        elif element == "multicast":
            return self.weh.get_element(self.select_element_port_type_multicast_summary)
        elif element == "rate limit type":
            return self.weh.get_element(self.select_element_port_type_rate_limit_type_summary)
        elif element == "rate limit value":
            return self.weh.get_element(self.select_element_port_type_rate_limit_value_summary)
        elif element == "elrp status":
            return self.weh.get_element(self.select_element_port_type_elrp_status_summary)
        elif element == "pse profile":
            return self.weh.get_element(self.select_element_port_type_pse_profile_summary)
        elif element == "poe status":
            return self.weh.get_element(self.select_element_port_type_poe_status_summary)
        return None

    def get_device_d360_save_port_configuration(self):
        return self.weh.get_element(self.device_d360_save_port_configuration)

    def get_device_d360_cancel_port_configuration(self):
        return self.weh.get_element(self.device_d360_cancel_port_configuration)

    def get_device360_configure_port_usage_drop_down_options_presence(self, row):
        return self.weh.get_element(self.device360_configure_port_usage_drop_down_options_presence, parent=row)

    def get_device360_port_configuration_stack_units_dropdown(self):
        return self.weh.get_element(self.device360_port_configuration_stack_units_dropdown)

    def get_device360_port_configuration_stack_units_rows(self):
        return self.weh.get_elements(self.device360_port_configuration_stack_units_rows)

    def get_device360_port_config_pse_tab_slot_stack(self):
        return self.weh.get_element(self.device360_port_config_pse_tab_slot_stack)

    def get_device360_pse_settings_for_device_button_stack(self):
        return self.weh.get_element(self.device360_pse_settings_for_device_button_stack)

    def get_device360_edit_threshold_poe_stack(self):
        return self.weh.get_element(self.device360_edit_threshold_poe_stack)

    def get_device360_save_threshold_poe_value_stack(self):
        return self.weh.get_element(self.device360_save_threshold_poe_value_stack)

    def get_device360_configure_port_save_button_stack(self):
        return self.weh.get_element(self.device360_configure_port_save_button_stack)

    def get_device360_stack_overview_slot_details_rows(self):
        return self.weh.get_element(self.device360_stack_overview_slot_details_rows)

    def get_device360_thunderbold_icon_stack(self, row):
        return self.weh.get_elements(self.device360_thunderbold_icon_stack, parent=row)

    def get_device360_port_config_pse_tab_slot_stack(self):
        return self.weh.get_element(self.device360_port_config_pse_tab_slot_stack)

    def get_device360_pse_settings_for_device_button_stack(self):
        return self.weh.get_element(self.device360_pse_settings_for_device_button_stack)

    def get_device360_edit_threshold_poe_stack(self):
        return self.weh.get_element(self.device360_edit_threshold_poe_stack)

    def get_device360_save_threshold_poe_value_stack(self):
        return self.weh.get_element(self.device360_save_threshold_poe_value_stack)

    def get_device360_configure_port_save_button_stack(self):
        return self.weh.get_element(self.device360_configure_port_save_button_stack)

    def get_device360_stack_overview_slot_details_rows(self):
        return self.weh.get_element(self.device360_stack_overview_slot_details_rows)

    def get_device360_thunderbold_icon_stack(self,row):
        return self.weh.get_elements(self.device360_thunderbold_icon_stack, parent=row)
    def get_device360_cpu_utilized_button(self):
        return self.weh.get_element(self.device360_cpu_utilized_button)

    def get_device360_memory_utilized_button(self):
        return self.weh.get_element(self.device360_memory_utilized_button)

    def get_device360_rx_counter_button(self):
        return self.weh.get_element(self.device360_rx_counter_button)

    def get_device360_tx_counter_button(self):
        return self.weh.get_element(self.device360_tx_counter_button)

    def get_device360_ports_list_graph(self):
        return self.weh.get_elements(self.device360_ports_list_graph)

    def get_device360_columns_toggle_button(self):
        return self.weh.get_element(self.device360_columns_toggle_button)

    def get_device360_coluns_toggle_checkboxes(self):
        return self.weh.get_elements(self.device360_coluns_toggle_checkboxes)

    def get_device360_ports_description_table_header(self):
        header_element = self.weh.get_element(self.device360_ports_description_table_header)
        return [h.strip() for h in header_element.text.split("\n")]

    def get_device360_ports_description_table_row(self):
        return self.weh.get_element(self.device360_ports_description_table_header)

    def get_device360_all_checkboxes(self):
        checkboxes = self.get_device360_coluns_toggle_checkboxes()
        results = {}
        for checkbox in checkboxes:
            label_xpath = f'//label[@for="{checkbox.get_attribute("id")}"]'
            label = self.weh.get_element({"XPATH": label_xpath}).text
            results[label] = {"element": checkbox, "is_selected": checkbox.is_selected()}
        return results

    def get_device360_all_marked_checkboxes(self):
        checkboxes = self.get_device360_coluns_toggle_checkboxes()
        results = {}
        for checkbox in checkboxes:
            label_xpath = f'//label[@for="{checkbox.get_attribute("id")}"]'
            label = self.weh.get_element({"XPATH": label_xpath}).text
            if checkbox.is_selected():
                results[label] = {"element": checkbox, "is_selected": checkbox.is_selected()}
        return results

    def get_device360_port_table_rows(self):
        scroll_element = self.get_device360_ports_table_scroll()
        if scroll_element:
            from common.AutoActions import AutoActions
            auto_actions = AutoActions()
            auto_actions.click(scroll_element)
            for _ in range(10):
                auto_actions.scroll_down()
        return self.get_d360_switch_ports_table_grid_rows()

    def get_device360_ports_table_pagination_sizes(self):
        return self.weh.get_elements(self.device360_ports_table_pagination_sizes)

    def get_device360_ports_table_current_pagination_size(self):
        return self.weh.get_element(self.device360_ports_table_current_pagination_size)

    def get_device360_ports_table_th_columns(self):
        header_row = self.get_device360_ports_description_table_row()
        ths = self.weh.get_elements(self.device360_ports_table_th_columns, parent=header_row)
        return {th.text.strip(): th for th in ths if th.text.strip()}

    def get_device360_ports_table(self):

        header_row = self.get_device360_ports_description_table_row()
        ths = self.weh.get_elements(self.device360_ports_table_th_columns, parent=header_row)

        table_rows = self.get_device360_port_table_rows()[1:]
        results = []
        for row in table_rows:
            result = {}
            tds = self.weh.get_elements(self.device360_ports_table_td_gridcell, parent=row)
            for th, td in zip(ths, tds):
                if th.text.strip():
                    result[th.text.strip()] = td.text.strip()
            results.append(result)
        return results

    def get_device360_pagination_page_buttons(self):
        return self.weh.get_elements(self.d360_pagination_page_button)

    def get_device360_ah_icon(self, index):
        return self.weh.get_template_element(self.device360_ah_icons, index=index)

    def get_device360_ports_table_scroll(self):
        return self.weh.get_element(self.device360_ports_table_scroll)

    def get_device360_ports_table_current_pagin_number(self):
        return self.weh.get_element(self.device360_ports_table_current_pagin_number)

    def get_device360_configure_port_access_vlan_textfield_VOSS(self, row):
        return self.weh.get_element(self.device360_configure_port_access_vlan_textfield_VOSS, row)

    def get_device360_configure_port_trunk_native_vlan_textfield_VOSS(self, row):
        return self.weh.get_element(self.device360_configure_port_trunk_native_vlan_textfield_VOSS, row)

    def get_device360_configure_port_trunk_vlan_textfield_VOSS(self, row):
        return self.weh.get_element(self.device360_configure_port_trunk_vlan_textfield_VOSS, row)
