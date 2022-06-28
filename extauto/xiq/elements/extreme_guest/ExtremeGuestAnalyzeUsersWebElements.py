from sys import builtin_module_names

from cupshelpers import Printer
from extauto.xiq.defs.extreme_guest.ExtremeGuestAnalyzeUsersWebElementsDefs import ExtremeGuestAnalyzeUsersWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestAnalyzeUsersWebElements(ExtremeGuestAnalyzeUsersWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_analyze_users_tab(self):
        return self.weh.get_element(self.extreme_guest_analyze_users_tab)

    def get_extreme_guest_analyze_users_grid_location(self, search_string):
        org, site, building, floor = search_string.split(',')
        location = site.strip() + '/' + building.strip() + '/' + floor.strip()
        cell = self.weh.get_element(self.extreme_guest_analyze_users_grid_location_column)
        if location in cell.text:
            print(location)
            return cell

    def get_extreme_guest_analyze_users_grid_username(self, search_string):
        cell = self.weh.get_template_element(self.extreme_guest_analyze_users_grid_username_column, username=search_string)
        if search_string in cell.text:
            return cell