from xiq.defs.extreme_guest.ExtremeGuestWebElementsDefs import ExtremeGuestWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestWebElements(ExtremeGuestWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_subscription_page(self):
        return self.weh.get_element(self.extreme_guest_subscription_page)

    def get_extreme_guest_subscription_page_subscribe_button(self):
        return self.weh.get_element(self.extreme_guest_subscription_page_subscribe_button)

    def get_extreme_guest_subscription_page_help_information(self):
        return self.weh.get_element(self.extreme_guest_subscription_page_help_information)

    def get_extreme_guest_subscription_page_open_ssid_checkbox(self):
        return self.weh.get_element(self.extreme_guest_subscription_page_open_ssid_checkbox)

    def get_extreme_guest_subscription_page_open_ssid_grid_rows(self):
        return self.weh.get_elements(self.extreme_guest_subscription_page_open_ssid_grid_rows)

    def get_extreme_guest_subscription_page_open_ssid_grid_row_cells(self, row, field='field-name'):
        cells = self.weh.get_elements(self.extreme_guest_subscription_page_open_ssid_grid_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_extreme_guest_subscription_page_apply_button(self):
        return self.weh.get_element(self.extreme_guest_subscription_page_apply_button)

    def get_extreme_guest_more_insights_tab(self):
        return self.weh.get_element(self.extreme_guest_more_insights_tab)

    def get_extreme_guest_monitor_page(self):
        return self.weh.get_element(self.extreme_guest_monitor_page)

    def get_extreme_guest_configure_page(self):
        return self.weh.get_element(self.extreme_guest_configure_page)

    def get_extreme_guest_analyze_page(self):
        return self.weh.get_element(self.extreme_guest_analyze_page)

    def get_extreme_guest_configure_splash_template_tab(self):
        return self.weh.get_element(self.extreme_guest_configure_splash_template_tab)

    def get_extreme_guest_configure_users_tab(self):
        return self.weh.get_element(self.extreme_guest_configure_users_tab)

    def get_extreme_guest_monitor_dashboard_tab(self):
        return self.weh.get_element(self.extreme_guest_monitor_dashboard_tab)
