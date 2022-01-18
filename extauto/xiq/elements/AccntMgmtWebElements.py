from xiq.defs.AccntMgmtWebElementsDefs import *
from common.WebElementHandler import *


class AccntMgmtWebElements(AccntMgmtWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_account_mgmt_grid_rows(self):
        return self.weh.get_elements(self.account_mgmt_grid_rows)

    def get_account_mgmt_grid_row_check_box(self, row):
        return self.weh.get_element(self.account_mgmt_grid_row_check_box, row)

    def get_account_mgmt_delete_button(self):
        return self.weh.get_element(self.account_mgmt_delete_button)

    def get_account_mgmt_delete_conf_yes_button(self):
        return self.weh.get_element(self.account_mgmt_delete_conf_yes_button)

    def get_account_mgmt_add_button(self):
        return self.weh.get_element(self.account_mgmt_add_button)

    def get_account_mgmt_email_text(self):
        return self.weh.get_element(self.account_mgmt_email_text)

    def get_account_mgmt_name_text(self):
        return self.weh.get_element(self.account_mgmt_name_text)

    def get_account_mgmt_organisation_sec(self):
        return self.weh.get_element(self.account_mgmt_organisation_sec)

    def get_account_mgmt_org_drop_down(self):
        return self.weh.get_element(self.account_mgmt_org_drop_down)

    def get_account_mgmt_org_drop_down_opt(self):
        return self.weh.get_elements(self.account_mgmt_org_drop_down_opt)

    def get_account_mgmt_timeout(self):
        return self.weh.get_element(self.account_mgmt_timeout)

    def get_administrator_role_radio_button(self):
        return self.weh.get_element(self.administrator_role_radio_button)

    def get_operator_role_radio_button(self):
        return self.weh.get_element(self.operator_role_radio_button)

    def get_monitor_role_radio_button(self):
        return self.weh.get_element(self.monitor_role_radio_button)

    def get_help_desk_role_radio_button(self):
        return self.weh.get_element(self.help_desk_role_radio_button)

    def get_guest_management_role_radio_button(self):
        return self.weh.get_element(self.guest_management_role_radio_button)

    def get_observer_role_radio_button(self):
        return self.weh.get_element(self.observer_role_radio_button)

    def get_account_mgmt_save_button(self):
        return self.weh.get_element(self.account_mgmt_save_button)

    def get_application_operator_role_radio_button(self):
        return self.weh.get_element(self.application_operator_role_radio_button)

    def get_Rbac_Assign_Location_checkbox(self):
        return self.weh.get_element(self.Rbac_Assign_Location_checkbox)

    def get_credential_distribution_groups_add_button(self):
        return self.weh.get_element(self.credential_distribution_groups_add_button)

    def get_credential_distribution_groups_name_textfield(self):
        return self.weh.get_element(self.credential_distribution_groups_name_textfield)

    def get_credential_distribution_groups_admin_account_dropdown(self):
        return self.weh.get_element(self.credential_distribution_groups_admin_account_dropdown)

    def get_credential_distribution_groups_credential_restriction_checkbox(self):
        return self.weh.get_element(self.credential_distribution_groups_credential_restriction_checkbox)

    def get_credential_distribution_groups_credential_restriction_count(self):
        return self.weh.get_element(self.credential_distribution_groups_credential_restriction_count)

    def get_credential_distribution_groups_registration_operation_checkbox(self):
        return self.weh.get_element(self.credential_distribution_groups_registration_operation_checkbox)

    def get_credential_distribution_groups_select_all_checkbox(self):
        return self.weh.get_element(self.credential_distribution_groups_select_all_checkbox)

    def get_credential_distribution_groups_save_button(self):
        return self.weh.get_element(self.credential_distribution_groups_save_button)

    def get_credential_distribution_groups_guest_management_role_user_option(self):
        return self.weh.get_element(self.credential_distribution_groups_guest_management_role_user_option)

    def get_credential_distribution_groups_active_directory_user_option(self):
        return self.weh.get_element(self.credential_distribution_groups_active_directory_user_option)

    def get_credential_distribution_groups_user_group_checkboxes(self):
        parent = self.weh.get_element(self.credential_distribution_groups_user_group_checkboxes_parent)
        return self.weh.get_elements(self.credential_distribution_groups_user_group_checkboxes, parent=parent)

    def get_credential_distribution_groups_member_of(self):
        parent = self.weh.get_element(self.credential_distribution_groups_member_of_parent)
        return self.weh.get_element(self.credential_distribution_groups_member_of, parent=parent)


