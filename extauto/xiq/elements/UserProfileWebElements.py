from extauto.xiq.defs.UserProfileWebElementsDef import *
from extauto.common.WebElementHandler import WebElementHandler


class UserProfileWebElements(UserProfileWebElementsDef):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_user_profile_grid_rows(self):
        return self.weh.get_elements(self.user_profile_grid_rows)

    def get_user_group_row_cell(self, row, field='field-name'):
        cells = self.weh.get_elements(self.user_profile_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_user_profile_add(self):
        return self.weh.get_element(self.user_profile_add)

    def get_user_profile_name(self):
        return self.weh.get_element(self.user_profile_name)

    def get_user_profile_vlan_add(self):
        return self.weh.get_element(self.user_profile_vlan_add)

    def get_user_profile_vlan_name(self):
        return self.weh.get_element(self.user_profile_vlan_name)

    def get_user_profile_vlan_id(self):
        return self.weh.get_element(self.user_profile_vlan_id)

    def get_user_profile_vlan_save(self):
        return self.weh.get_element(self.user_profile_vlan_save)

    def get_user_profile_save(self):
        return self.weh.get_element(self.user_profile_save)

    def get_user_profile_row_cells(self):
        return self.weh.get_element(self.user_profile_row_cells)

    def get_user_profile_delete(self):
        return self.weh.get_element(self.user_profile_delete)

    def get_user_profile_confirm_delete_no(self):
        return self.weh.get_element(self.user_profile_confirm_delete_no)

    def get_user_profile_confirm_delete_yes(self):
        return self.weh.get_element(self.user_profile_confirm_delete_yes)

    def get_all_profile_row_cells(self, row):
        cells = self.weh.get_elements(self.user_profile_row_cells, row)
        return cells
