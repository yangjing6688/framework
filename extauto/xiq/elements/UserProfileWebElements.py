from extauto.xiq.defs.UserProfileWebElementsDef import UserProfileWebElementsDef
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

    def get_user_profile_vlan_row_select_rule_href(self, row):
        return self.weh.get_element(self.user_profile_vlan_row_cell_select_rule_href, row)

    def get_user_profile_vlan_row_add_rule_href(self, row):
        return self.weh.get_element(self.user_profile_vlan_row_cell_add_rule_href, row)

    def get_user_profile_vlan_row_rule_rows(self):
        return self.weh.get_elements(self.user_profile_vlan_row_rule_rows)

    def get_user_profile_vlan_row_rule_link_btn(self):
        return self.weh.get_element(self.user_profile_vlan_row_rule_link_btn)

    def get_user_profile_vlan_row_rule_cancel_btn(self):
        return self.weh.get_element(self.user_profile_vlan_row_rule_cancel_btn)

    def get_user_profile_assignment_name(self):
        return self.weh.get_element(self.user_profile_assignment_name)

    def get_user_profile_assignment_description(self):
        return self.weh.get_element(self.user_profile_assignment_description)

    def get_user_profile_assignment_add_assignment_rule(self):
        return self.weh.get_element(self.user_profile_assignment_add_assignment_rule)

    def get_user_profile_assignment_add_user_group(self):
        return self.weh.get_element(self.user_profile_assignment_add_user_group)

    def get_user_profile_assignment_add_client_os_type(self):
        return self.weh.get_element(self.user_profile_assignment_add_client_os_type)

    def get_user_profile_assignment_add_user_group_rows(self):
        return self.weh.get_elements(self.user_profile_assignment_add_user_group_rows)

    def get_user_profile_assignment_add_client_os_type_rows(self):
        return self.weh.get_elements(self.user_profile_assignment_add_client_os_type_rows)

    def get_user_profile_assignment_add_client_os_type_checked_row(self, row):
        return self.weh.get_element(self.user_profile_assignment_add_client_os_type_checked_row, row)

    def get_user_profile_assignment_add_assignment_rule_select_btn(self):
        return self.weh.get_element(self.user_profile_assignment_add_asssignment_rule_select_btn)

    def get_user_profile_assignment_save_btn(self):
        return self.weh.get_element(self.user_profile_assignment_save_btn)

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
