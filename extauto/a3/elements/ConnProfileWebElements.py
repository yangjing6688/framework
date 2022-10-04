from a3.defs.ConnProfileWebElementDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class ConnProfileWebElements(ConnProfileWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def select_conn_profile_menu(self):
        return self.weh.get_element(self.conn_profile_menu)

    def get_radius_audit_log_ui(self):
        return self.weh.get_element(self.radius_audit_log_ui)

    def get_clients_search_ui(self):
        return self.weh.get_element(self.clients_search_ui)

    def get_audit_logs_grid_rows(self):
        """
        :return: all the rows in the Radius Audit Logs grid
        """
        grid_rows = self.weh.get_elements(self.audit_logs_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_clients_search_rows(self):
        """
        :return: all the rows in the Radius Audit Logs grid
        """
        grid_rows = self.weh.get_elements(self.clients_search_rows)
        if grid_rows:
            return grid_rows
        else:
            return False



