from a3.defs.LicenseManagementDefs import LicenseManagementDefs
from common.AutoActions import AutoActions
from common.WebElementHandler import WebElementHandler


class LicenseManagementElements(LicenseManagementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_cluster_id(self):
        return self.weh.get_element(self.cluster_id)

    def get_system_id(self):
        return self.weh.get_element(self.system_id)

    def get_licensed_capacity(self):
        return self.weh.get_element(self.licensed_capacity)

    def get_used_capacity(self):
        return self.weh.get_element(self.used_capacity)

    def get_average_used_capacity(self):
        return self.weh.get_element(self.average_used_capacity)

    def get_license_management_table(self):
        return self.weh.get_element(self.license_management_table)

    def get_license_management_table_row(self):
        return self.weh.get_element(self.license_management_table_row)

    def get_license_management_table_cell(self):
        return self.weh.get_element(self.license_management_table_cell)
