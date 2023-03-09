from a3.defs.GlobalSettingWebElementDefinitions import GlobalSettingWebElementDefinitions
from common.Utils import Utils
from common.WebElementHandler import WebElementHandler


class GlobalSettingWebElements(GlobalSettingWebElementDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()
        self.utils = Utils()

    def get_backup_logs_grid_rows(self):
        """
        :return: all the rows in the authentication Logs grid
        """
        grid_rows = self.weh.get_elements(self.backup_logs_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

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

    def get_logs_grid_rows(self):
        """
        :return: all the rows in the authentication Logs grid
        """
        grid_rows = self.weh.get_elements(self.logs_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False
