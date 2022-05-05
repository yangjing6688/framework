from sys import builtin_module_names
from extauto.xiq.defs.extreme_guest.ExtremeGuestAnalyzeClientsWebElementsDefs import ExtremeGuestAnalyzeClientsWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestAnalyzeClientsWebElements(ExtremeGuestAnalyzeClientsWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_analyze_clients_tab(self):
        return self.weh.get_element(self.extreme_guest_analyze_clients_tab)

    def get_extreme_guest_analyze_clients_total_clients(self):
        return self.weh.get_element(self.extreme_guest_analyze_clients_total_clients)

    def get_extreme_guest_analyze_clients_grid(self):
        return self.weh.get_element(self.extreme_guest_analyze_clients_grid)

    def get_extreme_guest_analyze_clients_grid_location(self, search_string):
        org, site, building, floor = search_string.split(',')
        location = site.strip() + '/' + building.strip() + '/' + floor.strip()
        cell = self.weh.get_element(self.extreme_guest_analyze_clients_grid_location_column)
        if location in cell.text:
            return cell

    def get_extreme_guest_analyze_clients_grid_macaddress(self, search_string):
        cell = self.weh.get_element(self.extreme_guest_analyze_clients_grid_macaddress_column)
        macaddress=cell.text
        macaddress.replace("-","")
        if search_string in macaddress:
            return cell