from extauto.common.WebElementHandler import *
from extauto.xiq.defs.MspWebElementsDefinitions import *


class MspWebElements(MspWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_view_organization_button(self):
        return self.weh.get_element(self.view_organizations_button)

    def get_select_all_organizations(self):
        return self.weh.get_element(self.view_organization_select)

    def get_view_organization_close_button(self):
        return self.weh.get_element(self.view_organization_close_button)

    def get_organization_grid_rows(self):
        grid_rows = self.weh.get_elements(self.organizations_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_organizations_select_check_box(self, row):
        return self.weh.get_element(self.organizations_select_check_box, parent=row)