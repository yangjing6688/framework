from xiq.defs.CredDistrGrupWebElemntsDefs import *
from extauto.common.WebElementHandler import *


class CredDistrGrupWebElemnts(CredDistrGrupWebElemntsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_cred_distr_grps_grid_rows(self):
        return self.weh.get_elements(self.cred_distr_grps_grid_rows)

    def get_cred_dist_grps_grid_row_check_box(self, row):
        return self.weh.get_element(self.cred_distr_grps_grid_row_check_box, row)

    def get_cred_distr_grps_row_delete_button(self):
        return self.weh.get_element(self.cred_distr_grps_row_delete_button)

    def get_cred_distr_grps_row_delete_confirm_yes_button(self):
        return self.weh.get_element(self.cred_distr_grps_row_delete_confirm_yes_button)

    def get_cred_distr_grps_add_button(self):
        return self.weh.get_element(self.cred_distr_grps_add_button)

    def get_cred_distr_grps_name_field(self):
        return self.weh.get_element(self.cred_distr_grps_name_field)

    def get_cred_distr_grps_admin_acct_drop_down(self):
        return self.weh.get_element(self.cred_distr_grps_admin_acct_drop_down)

    def get_cred_distr_grps_admin_acct_drop_down_opts(self):
        return self.weh.get_elements(self.cred_distr_grps_admin_acct_drop_down_opts)

    def get_cred_distr_member_of_text_field(self):
        return self.weh.get_element(self.cred_distr_member_of_text_field)

    def get_cred_distr_guest_mgmt_usr_text_field(self):
        return self.weh.get_element(self.cred_distr_guest_mgmt_usr_text_field)

    def get_cred_restriction_check_box(self):
        return self.weh.get_element(self.cred_restriction_check_box)

    def get_cred_restriction_number(self):
        return self.weh.get_element(self.cred_restriction_number)

    def get_restriction_operation_check_box(self):
        return self.weh.get_element(self.restriction_operation_check_box)

    def get_enable_usr_grps_check_box(self):
        return self.weh.get_element(self.enable_usr_grps_check_box)

    def get_enable_usr_grps_list(self):
        return self.weh.get_elements(self.enable_usr_grps_list)

    def get_cred_distr_grp_save_button(self):
        return self.weh.get_element(self.cred_distr_grp_save_button)