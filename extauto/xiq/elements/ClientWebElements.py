from extauto.xiq.defs.ClientWebElementsDefinitions import *
from extauto.common.WebElementHandler import *


class ClientWebElements(ClientWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_monitor_tab(self):
        """
        :return: get Monitor Tab
        """
        return self.weh.get_element(self.get_monitor_tab_menu)

    def get_monitor_client_tab(self):
        """
        :return: get Monitor-->client Menu Tab
        """
        return self.weh.get_element(self.get_monitor_clients_tab_menu)

    def get_grid_rows(self):
        """
        :return: all the rows in the clients grid
        """
        grid_rows = self.weh.get_elements(self.client_page_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_connection_status(self, row):
        """
        :param row:
        :return: status cell of the row in the clients grid
        """
        return self.weh.get_element(self.client_connection_status, row).text

    def get_clients_real_time_tab(self):
        return self.weh.get_element(self.clients_real_time_tab)

    def get_clients_historical_tab(self):
        return self.weh.get_element(self.clients_historical_tab)

    def get_client_row_cells(self, row):
        return self.weh.get_elements(self.client_row_cells, row)

    def get_client_mac_cell(self, cell):
        return self.weh.get_element(self.client_mac_cell, cell)

    def get_client_gdpr_delete_button(self):
        return self.weh.get_element(self.client_gdpr_delete_button)

    def get_client_gdpr_delete_yes_confirm_button(self):
        return self.weh.get_element(self.client_gdpr_delete_yes_confirm_button)

    def get_client_dialog_window_close_button(self):
        return self.weh.get_element(self.client_dialog_window_close_button)

    def get_client_page_refresh_button(self):
        return self.weh.get_element(self.client_page_refresh_button)

    def get_client_health_status(self, cell):
        return self.weh.get_element(self.client_health_status, cell)

    def get_client_page_size_100(self):
        return self.weh.get_element(self.client_page_size_100)

    def get_client360_os_type_field(self):
        return self.weh.get_element(self.client360_os_type_field)

    def get_client360_ip_address_field(self):
        return self.weh.get_element(self.client360_ip_address_field)

    def get_client360_mac_address_field(self):
        return self.weh.get_element(self.client360_mac_address_field)

    def get_client360_connected_ap_info_field(self):
        return self.weh.get_element(self.client360_connected_ap_info_field)

    def get_client360_vlan_field(self):
        return self.weh.get_element(self.client360_vlan_field)

    def get_client360_captive_web_portal_field(self):
        return self.weh.get_element(self.client360_captive_web_portal_field)

    def get_client360_user_profile_field(self):
        return self.weh.get_element(self.client360_user_profile_field)

    def get_client360_user_name_field(self):
        return self.weh.get_element(self.client360_user_name_field)

    def get_client360_ssid_field(self):
        return self.weh.get_element(self.client360_ssid_field)

    def get_client360_radio_mac_protocol_field(self):
        return self.weh.get_element(self.client360_radio_mac_protocol_field)

    def get_client360_radio_field(self):
        return self.weh.get_element(self.client360_radio_field)

    def get_client360_channel_field(self):
        return self.weh.get_element(self.client360_channel_field)
