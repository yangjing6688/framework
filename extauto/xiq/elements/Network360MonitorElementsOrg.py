from extauto.common.WebElementHandler import *
from extauto.xiq.defs.Network360MonitorDefinitions import *


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

    def get_device_health_overal_score_availability_score(self):
        return self.weh.get_element(self.device_health_overal_score_availability_score)

    def get_device_health_overal_score_hw_health(self):
        return self.weh.get_element(self.device_health_overal_score_hw_health)

    def get_device_health_overal_score_fw_score(self):
        return self.weh.get_element(self.device_health_overal_score_fw_score)

    def get_n360_monitor_map(self):
        return self.weh.get_element(self.n360_monitor_map)

