from xiq.defs.ClientMonitorWebElementsDefs import *
from extauto.common.WebElementHandler import *


class ClientMonitorWebElements(ClientMonitorWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_client_monitor_tab(self):
        return self.weh.get_element(self.client_monitor_tab)

    def get_auth_issue_counts_status_card(self):
        return self.weh.get_element(self.auth_issue_counts_status_card)

    def get_issue_type_drop_down(self):
        return self.weh.get_element(self.issue_type_drop_down)

    def get_issue_type_drop_down_options(self, parent):
        return self.weh.get_elements(self.issue_type_drop_down_options, parent)

    def get_issue_status_drop_down(self):
        return self.weh.get_element(self.issue_status_drop_down)

    def get_issue_status_drop_down_options(self, parent):
        return self.weh.get_elements(self.issue_status_drop_down_options, parent)

    def get_troubleshoot_issue_aggregate_icon(self):
        return self.weh.get_element(self.troubleshoot_issue_aggregate_icon)

    def get_client_issue_grid_rows(self):
        return self.weh.get_elements(self.client_issue_grid_rows)

    def get_client_issue_grid_row_cell(self, row):
        return self.weh.get_elements(self.client_issue_grid_row_cell, row)