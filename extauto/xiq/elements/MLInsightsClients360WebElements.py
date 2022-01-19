from extauto.common.WebElementHandler import *
from extauto.xiq.defs.MLInsightsClient360Definitions import *


class MLInsightsClients360WebElements(MLInsightsClient360Definitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_n360_client_360_avg_rssi_drop_down(self):
        return self.weh.get_element(self.n360_client_360_avg_rssi_drop_down)

    def get_n360_client_360_avg_snr_drop_down(self):
        return self.weh.get_element(self.n360_client_360_avg_snr_drop_down)

    def get_n360_client_360_wifi_health_drop_down(self):
        return self.weh.get_element(self.n360_client_360_wifi_health_drop_down)

    def get_n360_client_360_avg_rssi_option(self):
        return self.weh.get_elements(self.n360_client_360_avg_rssi_option)

    def get_n360_client_360_avg_snr_option(self):
        return self.weh.get_elements(self.n360_client_360_avg_snr_option)

    def get_n360_client_360_wifi_health_option(self):
        return self.weh.get_elements(self.n360_client_360_wifi_health_option)

    def get_n360_client_360_supported_mode_loc(self):
        return self.weh.get_element(self.n360_client_360_supported_mode_loc)

    def get_n360_client_360_real_time_btn(self):
        return self.weh.get_element(self.n360_client_360_real_time_btn)

    def get_n360_client_360_historical_btn(self):
        return self.weh.get_element(self.n360_client_360_historical_btn)

    def get_n360_client_360_client_total_use(self):
        return self.weh.get_element(self.n360_client_360_client_total_use)

    def get_n360_client_360_client_last_con(self):
        return self.weh.get_element(self.n360_client_360_client_last_con)

    def get_n360_client_360_con_time(self):
        return self.weh.get_element(self.n360_client_360_con_time)

    def get_n360_client_360_avg_rssi(self):
        return self.weh.get_element(self.n360_client_360_avg_rssi)

    def get_n360_client_360_avg_snr(self):
        return self.weh.get_element(self.n360_client_360_avg_snr)

    def get_n360_client_360_wifi_health(self):
        return self.weh.get_element(self.n360_client_360_wifi_health)

    def get_n360_client_360_client_btn(self):
        return self.weh.get_element(self.n360_client_360_client_btn)

    def get_n360_client_360_client_grid_rows(self):
        return self.weh.get_element(self.n360_client_360_client_grid_rows)

    def get_n360_client_360_table_select_btn(self):
        return self.weh.get_element(self.n360_client_360_table_select_btn)

    def get_n360_client_360_table_sel_option(self):
        return self.weh.get_element(self.n360_client_360_table_sel_option)

    def get_n360_client_360_client_refresh(self):
        return self.weh.get_element(self.n360_client_360_client_refresh)

    def get_client_360_real_time_tab(self):
        return self.weh.get_element(self.client_360_real_time_tab)

    def get_client_360_real_time_grid_rows(self):
        return self.weh.get_elements(self.client_360_real_time_grid_rows)

    def get_client_360_real_time_grid_row_cells(self, row):
        return self.weh.get_elements(self.client_360_real_time_grid_row_cells, row)

    def get_client360_health_status(self, cell):
        return self.weh.get_element(self.client360_health_status, cell)
