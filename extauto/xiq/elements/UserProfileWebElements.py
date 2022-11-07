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

    def get_vlan_profile_delete(self):
        return self.weh.get_element(self.vlan_profile_delete)

    def get_user_profile_confirm_delete_no(self):
        return self.weh.get_element(self.user_profile_confirm_delete_no)

    def get_user_profile_confirm_delete_yes(self):
        return self.weh.get_element(self.user_profile_confirm_delete_yes)

    def get_all_profile_row_cells(self, row):
        cells = self.weh.get_elements(self.user_profile_row_cells, row)
        return cells

    def get_user_profile_view_all_pages(self):
        return self.weh.get_element(self.user_profile_view_all_pages)

    def get_user_profile_row_href(self, cell):
        return self.weh.get_element(self.user_profile_row_cell_href, cell)

    def get_user_profile_vlan_edit_btn(self):
        return self.weh.get_element(self.user_profile_vlan_edit_btn)

    def get_user_profile_vlan_apply_vlans_to_device_chkbx(self):
        return self.weh.get_element(self.user_profile_vlan_apply_vlans_to_device_chkbx)

    def get_user_profile_vlan_apply_vlans_to_device_add(self):
        return self.weh.get_element(self.user_profile_vlan_apply_vlans_to_device_add)

    def get_user_profile_vlan_apply_vlans_to_device_vlanid_txtbx(self):
        return self.weh.get_element(self.user_profile_vlan_apply_vlans_to_device_vlanid_txtbx)

    def get_user_profile_vlan_apply_vlans_to_device_add_btn(self):
        return self.weh.get_element(self.user_profile_vlan_apply_vlans_to_device_add_btn)

    def get_user_profile_vlan_rows(self):
        return self.weh.get_elements(self.user_profile_vlan_rows)

    def get_user_profile_vlan_row_href(self, row):
        return self.weh.get_element(self.user_profile_vlan_row_cell_href, row)

    def get_user_profile_vlan_row_rule_rows(self):
        return self.weh.get_elements(self.user_profile_vlan_row_rule_rows)

    def get_user_profile_vlan_row_rule_link_btn(self):
        return self.weh.get_element(self.user_profile_vlan_row_rule_link_btn)

    def get_apply_different_user_profile_to_various_clients_chkbx(self):
        return self.weh.get_element(self.apply_different_user_profile_to_various_clients_chkbx)

    def get_different_user_profile_add_user_profile(self):
        return self.weh.get_element(self.apply_different_user_profile_add_user_profile)

    def get_different_user_profile_add_user_profile_vlan_addbtn(self):
        return self.weh.get_element(self.different_user_profile_add_user_profile_vlan_addbtn)

    def get_different_user_profile_add_user_profile_save_btn(self):
        return self.weh.get_element(self.different_user_profile_add_user_profile_save_btn)

    def get_different_user_profile_vlan_rows(self):
        return self.weh.get_elements(self.different_user_profile_vlan_rows)

    def get_different_user_profile_vlan_rule_optbox(self, row):
        return self.weh.get_element(self.different_user_profile_vlan_rule_optbox, row)
