from extauto.xiq.defs.NetworkManagementOptionsDefinitions import NetworkManagementOptionsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class NetworkManagementOptionsElements(NetworkManagementOptionsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_network_management_options_entry(self):
        return self.weh.get_element(self.add_network_management_options_entry)

    def get_delete_network_management_options_entry(self):
        return self.weh.get_element(self.delete_network_management_options_entry)

    def get_network_management_grid_rows(self):
        return self.weh.get_elements(self.network_management_grid_rows)

    def get_network_management_grid_row_cells(self, row):
        return self.weh.get_elements(self.network_management_grid_row_cells, row)

    def get_new_management_option_name(self):
        return self.weh.get_element(self.new_management_option_name)

    def get_legacy_http_redirect(self):
        return self.weh.get_element(self.legacy_http_redirect)

    def get_cancel_button(self):
        return self.weh.get_element(self.cancel_button)

    def get_save_button(self):
        return self.weh.get_element(self.save_button)

    def get_confirm_yes(self):
        return self.weh.get_element(self.confirm_yes)

    def get_confirm_no(self):
        return self.weh.get_element(self.confirm_no)
