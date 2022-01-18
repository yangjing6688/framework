from xiq.defs.UserGroupsWebElementsDefinitions import *
from common.WebElementHandler import WebElementHandler


class UserGroupsWebElements(UserGroupsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_user_group_grid_rows(self):
        return self.weh.get_elements(self.user_groups_grid_rows)

    def get_user_group_row_cell(self, row, field='field-name'):
        cells = self.weh.get_elements(self.user_group_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_user_management_side_menu(self):
        return self.weh.get_element(self.user_management_side_menu)

    def get_user_group_side_menu(self):
        return self.weh.get_element(self.user_group_side_nav_item)

    def get_user_group_add_button(self):
        if self.weh.get_element(self.user_group_add_button):
            return self.weh.get_element(self.user_group_add_button)
        elif self.weh.get_element(self.deutcshe_user_group_add_button):
            return self.weh.get_element(self.deutcshe_user_group_add_button)

    def get_user_group_name_field(self):
        return self.weh.get_element(self.user_group_name_field)

    def get_password_db_loc_drop_down_button(self):
        return self.weh.get_element(self.password_db_loc_drop_down_button)

    def get_password_db_loc_items(self):
        return self.weh.get_elements(self.password_db_loc_drop_down_items)

    def get_password_type_drop_down_button(self):
        return self.weh.get_element(self.password_type_drop_down_button)

    def get_password_type_items(self):
        return self.weh.get_elements(self.password_type_drop_down_items)

    def get_max_num_of_clients_per_ppsk_check_box(self):
        return self.weh.get_element(self.max_num_of_clients_per_ppsk_check_box)

    def get_max_num_of_clients_per_ppsk_input_field(self):
        return self.weh.get_element(self.max_num_of_clients_per_ppsk_input_field)

    def get_client_per_ppsk_error_field(self):
        return self.weh.get_elements(self.input_field_form_error)

    def get_pcg_use_checkbox(self):
        return self.weh.get_element(self.pcg_use_checkbox)

    def get_ap_based_radio_button(self):
        return self.weh.get_element(self.ap_based_radio_button)

    def get_key_based_radio_button(self):
        return self.weh.get_element(self.key_based_radio_button)

    def get_ppsk_classification_use_checkbox(self):
        return self.weh.get_element(self.ppsk_classification_use_checkbox)

    def get_cwp_register_checkbox(self):
        return self.weh.get_element(self.cwp_register_check_box)

    def get_add_user_toggle_button(self):
        return self.weh.get_element(self.add_user_toggle_button)

    def get_single_user_add_button(self):
        return self.weh.get_element(self.single_user_add_button)

    def get_bulk_user_add_button(self):
        return self.weh.get_element(self.bulk_user_add_button)

    def get_bulk_create_users_username_prefix(self):
        return self.weh.get_element(self.bulk_create_users_username_prefix)

    def get_bulk_create_users_number_of_accounts(self):
        return self.weh.get_element(self.bulk_create_users_number_of_accounts)

    def get_bulk_create_users_email_user_account_info_to(self):
        return self.weh.get_element(self.bulk_create_users_email_user_account_info_to)

    def get_bulk_create_users_done_button(self):
        return self.weh.get_element(self.bulk_create_users_done_button)

    def get_bulk_user_create_text_field_error(self):
        return self.weh.get_elements(self.bulk_user_create_text_field_error)

    def get_bulk_create_users_cancel_button(self):
        return self.weh.get_element(self.bulk_create_users_cancel_button)

    def get_user_group_save_button(self):
        return self.weh.get_element(self.user_group_save_button)

    def get_user_group_delete_button(self):
        return self.weh.get_element(self.user_group_delete_button)

    def get_user_group_delete_confirm_yes_button(self):
        return self.weh.get_element(self.user_group_delete_confirm_yes_button)

    def get_single_user_name_field(self):
        return self.weh.get_element(self.single_user_name_text_field)

    def get_single_user_org_filed(self):
        return self.weh.get_element(self.single_user_org_text_field)

    def get_single_user_purpose_of_visit_field(self):
        return self.weh.get_element(self.single_user_purpose_of_visit_field)

    def get_single_user_email_address_field(self):
        return self.weh.get_element(self.single_user_email_address_field)

    def get_single_user_country_code_drop_down(self):
        return self.weh.get_element(self.single_user_country_code_drop_down)

    def get_single_user_country_code_items(self):
        return self.weh.get_elements(self.single_user_country_code_items)

    def get_single_user_phone_number(self):
        return self.weh.get_element(self.single_user_phone_number)

    def get_single_user_user_name_drop_down(self):
        return self.weh.get_element(self.single_user_user_name_drop_down)

    def get_single_user_user_name_items(self):
        return self.weh.get_elements(self.single_user_user_name_items)

    def get_single_user_password_field(self):
        return self.weh.get_element(self.single_user_password_field)

    def get_single_user_password_generate_button(self):
        return self.weh.get_element(self.single_user_password_generate_button)

    def get_single_user_description(self):
        return self.weh.get_element(self.single_user_description)

    def get_single_user_deliver_password_check_box(self):
        return self.weh.get_element(self.single_user_deliver_password_check_box)

    def get_single_user_deliver_password(self):
        return self.weh.get_element(self.single_user_deliver_password_field)

    def get_single_user_create_done_button(self):
        return self.weh.get_element(self.single_user_create_done_button)

    def get_single_user_create_cancel_button(self):
        return self.weh.get_element(self.single_user_create_cancel_button)

    def get_single_user_create_text_field_error(self):
        return self.weh.get_elements(self.single_user_create_text_field_error)

    def get_user_group_text_field_form_error(self):
        return self.weh.get_elements(self.user_group_text_field_form_error)

    def get_paze_size_element(self, page_size='50'):
        els = self.weh.get_elements(self.page_size_element)
        if not els:
            return None
        for el in els:
            if el.text == page_size:
                return el

    def get_wireless_user_group_select_button(self):
        return self.weh.get_element(self.wireless_user_group_select_button)

    def get_wireless_usr_grp_select_wind_local_tab(self):
        return self.weh.get_element(self.wireless_usr_grp_select_wind_local_tab)

    def get_wireless_usr_grp_select_wind_cloud_tab(self):
        return self.weh.get_element(self.wireless_usr_grp_select_wind_cloud_tab)

    def get_wireless_user_group_select_window_group_rows(self):
        return self.weh.get_elements(self.wireless_user_group_select_window_group_rows)

    def get_wireless_usr_grp_select_wind_grp_row_check_box(self, row):
        return self.weh.get_element(self.wireless_usr_grp_select_wind_grp_row_check_box, row)

    def get_wireless_usr_grp_select_wind_select_button(self):
        return self.weh.get_element(self.wireless_usr_grp_select_wind_select_button)

    def get_wireless_usr_grp_select_wind_cancel_button(self):
        return self.weh.get_element(self.wireless_usr_grp_select_wind_cancel_button)

    def get_wireless_usr_group_add_button(self):
        return self.weh.get_element(self.wireless_usr_group_add_button)

    def get_guest_mgmt_account_single_usr_add_button(self):
        return self.weh.get_element(self.guest_mgmt_account_single_usr_add_button)

    def get_guest_mgmt_account_create_acct_user_grp_drop_down(self):
        return self.weh.get_element(self.guest_mgmt_account_create_acct_user_grp_drop_down)

    def get_add_user_button_users_sub_tab(self):
        return self.weh.get_element(self.add_user_button_users_sub_tab)

    def get_select_user_group_from_dropdown(self):
        return self.weh.get_elements(self.select_user_group_from_dropdown)

    def get_user_group_dropdown(self):
        return self.weh.get_element(self.user_group_dropdown)

    def get_users_subtab_user_row(self):
        return self.weh.get_elements(self.users_subtab_user_row)

    def get_username_in_users_subtab(self, row):
        return self.weh.get_element(self.username_in_users_subtab, parent=row)

    def get_select_user_in_users_subtab(self, row):
        return self.weh.get_element(self.select_user_in_users_subtab, parent=row)

    def get_delete_user_from_users_subtab(self):
        return self.weh.get_element(self.delete_user_from_users_subtab)

    def get_edit_user_from_users_subtab(self):
        return self.weh.get_element(self.edit_user_from_users_subtab)

    def get_user_delete_confirm_yes_button(self):
        return self.weh.get_element(self.user_delete_confirm_yes_button)

    def get_wireless_user_profile_select_button(self):
        return self.weh.get_element(self.wireless_user_profile_select_button)

    def get_wireless_user_profile_select_window_group_rows(self):
        return self.weh.get_elements(self.wireless_user_profile_select_window_group_rows)

    def get_wireless_usr_profile_select_wind_grp_row_check_box(self, row):
        return self.weh.get_element(self.wireless_usr_profile_select_wind_grp_row_check_box, row)

    def get_wireless_usr_profile_select_wind_select_button(self):
        return self.weh.get_element(self.wireless_usr_profile_select_wind_select_button)

    def get_wireless_usr_profile_select_wind_cancel_button(self):
        return self.weh.get_element(self.wireless_usr_profile_select_wind_cancel_button)