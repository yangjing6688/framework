from a3.defs.GlobalSettingWebElementDefinitions import *
from common.WebElementHandler import *


class GlobalSettingWebElements(GlobalSettingWebElementDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()
        self.utils = Utils()
        #self.driver = common.CloudDriver.cloud_driver

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
        #grid_rows = self.driver.find_elements_by_css_selector("div.pf-table-sortable.hover.striped")
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_logs_grid_rows(self):
        """
        :return: all the rows in the authentication Logs grid
        """
        grid_rows = self.weh.get_elements(self.logs_grid_rows)
        #grid_rows = self.driver.find_elements_by_css_selector("div.pf-table-sortable.hover.striped")
        if grid_rows:
            return grid_rows
        else:
            return False



