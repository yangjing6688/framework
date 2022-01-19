from xiq.defs.AdditionalSettingsEebElememtsDefs import *
from extauto.common.WebElementHandler import *

class AdditionalSettingsWebElements(AdditionalSettingsEebElememtsDefs):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_nw_policy_additional_settings_tab(self):
        return self.weh.get_element(self.nw_policy_additional_settings_tab)

    def get_ntp_server_classification_rule_grid_rows(self):
        grid_rows = self.weh.get_elements(self.ntp_server_classification_rule_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_ntp_server_classification_rule_grid_row_cells(self):
        grid_cells = self.weh.get_elements(self.ntp_server_classification_rule_grid_row_cells)
        if grid_cells:
            return grid_cells
        else:
            return False

    def get_nw_policy_additional_settings_ntp_server_tab(self):
        return self.weh.get_element(self.nw_policy_additional_settings_ntp_server_tab)