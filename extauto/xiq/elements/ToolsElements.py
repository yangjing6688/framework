from xiq.defs.ToolsUtilitiesDefs import *
from extauto.common.WebElementHandler import *


class ToolsElements(ToolsUtilitiesDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_utilities_button(self):
        return self.weh.get_element(self.utilities_button)

    def get_utilities_menu(self):
        return self.weh.get_element(self.neighbor_info_menu)

    def get_neighbor_info_menu_item(self):
        menu = self.get_utilities_menu()

        menus = self.weh.get_elements(self.neighbor_info_menu_item, parent=menu)
        for menu in menus:
            if menu.is_displayed():
                if 'Neighbor Info' in menu.text:
                    return menu

    def get_device_diagnostics_menu_item(self):
        menu = self.get_utilities_menu()

        menus = self.weh.get_elements(self.neighbor_info_menu_item, parent=menu)
        for menu in menus:
            if menu.is_displayed():
                if 'Device Diagnostics' in menu.text:
                    return menu

    def get_neighbor_info_button(self):
        return self.weh.get_element(self.neighbor_info_button)

    def get_neighbor_page_body(self):
        return self.weh.get_element(self.dialog_page_body)

    def get_neighbor_page_body_grid_rows(self):
        page_body = self.get_neighbor_page_body()
        rows = self.weh.get_elements(self.neighbor_page_body_grid_rows, parent=page_body)
        return rows

    def get_neighbor_info_close_button(self):
        return self.weh.get_element(self.neighbor_info_close_button)

    def get_diagnostics_button(self):
        return self.weh.get_element(self.diagnostics_button)

    def get_diagnostics_ping_menu(self):
        return self.weh.get_element(self.diagnostics_menu)

    def get_diagnostics_ping_menu_item(self):
        menu = self.get_diagnostics_ping_menu()
        menu_items = self.weh.get_elements(self.diagnostics_menu_items, parent= menu)
        for menu_item in menu_items:
            if menu_item.is_displayed():
                if 'Ping' in menu_item.text:
                    return menu_item

    def get_diagnostics_ping_output(self):
        return self.weh.get_element(self.dialog_page_body)

    def get_account_icon(self):
        return self.weh.get_element(self.account_icon)

    def get_global_settings(self):
        return self.weh.get_element(self.global_settings)

    def get_ssh_availability(self):
        return self.weh.get_element(self.SSH_availability)

    def get_enable_ssh(self):
        return self.weh.get_element(self.enable_ssh)

    def get_manage_button(self):
        return self.weh.get_element(self.manage_button)

    def get_tool_button(self):
        return self.weh.get_element(self.tool_button)

    def get_utilities_ssh_availability(self):
        return self.weh.get_element(self.utilities_ssh_availability)

    def get_ap_results_table(self):
        return self.weh.get_element(self.ap_results_table)

    def get_ap_results_row(self,popup):
        return self.weh.get_elements(self.ap_results_rows, parent=popup)

    def get_run_button(self):
        return self.weh.get_element(self.run_button)

    def get_ssh_timeout_5_minutes_radio(self):
        return self.weh.get_element(self.ssh_timeout_5_minutes_radio)

    def get_ssh_timeout_30_minutes_radio(self):
        return self.weh.get_element(self.ssh_timeout_30_minutes_radio)

    def get_ssh_timeout_60_minutes_radio(self):
        return self.weh.get_element(self.ssh_timeout_60_minutes_radio)

    def get_ssh_timeout_120_minutes_radio(self):
        return self.weh.get_element(self.ssh_timeout_120_minutes_radio)

    def get_enable_ssh_button(self):
        return self.weh.get_element(self.enable_ssh_button)

    def get_ip_address(self):
        return self.weh.get_element(self.ip_address)

    def get_port_num(self):
        return self.weh.get_element(self.port_num)

    def get_command(self):
        return self.weh.get_element(self.command)

    def get_ssh_status(self):
        return self.weh.get_element(self.ssh_status)

    def get_locked_device_element_link(self):
        return self.weh.get_element(self.locked_device_link)

    def get_locked_device_element_btn(self):
        return self.weh.get_element(self.locked_device_unlock_btn)

    def get_locked_device_rows(self):
        return self.weh.get_element(self.locked_device_tbl)

    def get_device_list_element_link(self):
        return self.weh.get_element(self.device_list_link)

    def get_device_info_btn(self):
        return self.weh.get_element(self.device_info_btn)

    def get_device_info_device_name(self):
        return self.weh.get_element(self.device_title_lbl)

    def get_device_connect_status(self):
        return self.weh.get_element(self.device_connect_status)

    def get_device_close_dlg(self):
        return self.weh.get_element(self.device_close_dlg)

    def get_ap_connect_status(self):
        return self.weh.get_element(self.ap_status_connect)

    def get_ap_disconnect_status(self):
        return self.weh.get_element(self.ap_status_disconnect)

    def get_device_client_info_link(self):
        return self.weh.get_element(self.device_client_info_link)

    def get_device_client_info_btn(self):
        return self.weh.get_element(self.device_info_btn)

    def get_device_client_title_lbl(self):
        return self.weh.get_element(self.device_client_info_title)

    def get_device_client_ap_name(self):
        return self.weh.get_element(self.device_client_info_ap_name_txt)

    def get_device_client_ap_mac(self):
        return self.weh.get_element(self.device_client_info_ap_mac_txt)

    def get_device_client_close_btn(self):
        return self.weh.get_element(self.device_info_close_btn)

    def get_client_info_link(self):
        return self.weh.get_element(self.client_info_link)

    def get_client_info_list(self):
        return self.weh.get_elements(self.client_info_list)

    def get_device_diag_link(self):
        return self.weh.get_element(self.device_diag_link)

    def get_device_diag_btn(self):
        return self.weh.get_element(self.device_diag_btn)

    def get_device_diag_ping_btn1(self):
        return self.weh.get_element(self.device_diag_ping_btn1)

    def get_device_diag_ping_btn2(self):
        return self.weh.get_element(self.device_diag_ping_btn2)

    def get_device_diag_ping_txt_area(self):
        return self.weh.get_element(self.device_diag_ping_txt_area)

    def get_device_diag_ping_txt_input(self):
        return self.weh.get_element(self.device_diag_ping_input_txt)

    def get_device_diag_ping_close_dlg(self):
        return self.weh.get_element(self.device_diag_ping_close_dlg)

    def get_vlan_probe_link(self):
        return self.weh.get_element(self.vlan_probe_link)

    def get_vlan_probe_btn(self):
        return self.weh.get_element(self.vlan_probe_btn)

    def get_vlan_probe_range_input(self):
        return self.weh.get_element(self.vlan_probe_input_range_txt)

    def get_vlan_probe_timeout_input(self):
        return self.weh.get_element(self.vlan_probe_timeout_txt)

    def get_vlan_probe_start_btn(self):
        return self.weh.get_element(self.vlan_probe_start_btn)

    def get_vlan_probe_close_diag(self):
        return self.weh.get_element(self.vlan_probe_close_diag)

    def get_tech_data_link(self):
        return self.weh.get_element(self.tech_data_link)

    def get_tech_data_btn(self):
        return self.weh.get_element(self.tech_data_btn)

    def get_tech_data_yes_btn(self):
        return self.weh.get_element(self.tech_data_yes_btn)

    def get_tech_data_download_btn(self):
        return self.weh.get_element(self.tech_data_download_btn)

    def get_tech_data_close_dialog(self):
        return self.weh.get_element(self.tech_data_close_diaglog)
