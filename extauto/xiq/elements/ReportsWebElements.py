from extauto.common.WebElementHandler import *
from xiq.defs.ReportsWebElementDefs import *


class ReportsWebElements(ReportsWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_network_summary_tab(self):
        return self.weh.get_element(self.network_summary_tab)

    def get_pci_dss_tab(self):
        return self.weh.get_element(self.pci_dss_tab)

    def get_wips_history_tab(self):
        return self.weh.get_element(self.wips_history_tab)

    def get_wifi_statistic_summary_tab(self):
        return self.weh.get_element(self.wifi_statistic_summary_tab)

    def get_select_widgets_drop_down(self):
        return self.weh.get_element(self.select_widgets_drop_down)

    def get_select_widgets_options(self):
        return self.weh.get_elements(self.select_widgets_options)

    def get_share_with_email_text_field(self):
        return self.weh.get_element(self.share_with_email_text_field)

    def get_generate_report_button(self):
        return self.weh.get_element(self.generate_report_button)
