from extauto.xiq.defs.GlobalSettingWebElementDefinitions import *
from extauto.common.WebElementHandler import *


class GlobalSettingWebElements(GlobalSettingWebElementDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_authentication_logs_grid_rows(self):
        """
        :return: all the rows in the authentication Logs grid
        """
        grid_rows = self.weh.get_elements(self.authentication_logs_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_authentication_logs_row_cells(self, row):
        """
        :return: authentication_logs row cell elements
        """
        return self.weh.get_elements(self.authentication_logs_grid_row_cells, row)

    def get_authentication_logs_auth_status_cell(self, cell):
        return self.weh.get_element(self.authentication_logs_auth_status_cell, cell)

    def get_organization_drop_down_button(self):
        """
        :return: get_organization_drop_down_button
        """
        return self.weh.get_element(self.global_settings_organization_name_colour_scroll_button)

    def get_organization_drop_down_items(self):
        """
        :return:
        """
        parent = self.weh.get_element(self.global_settings_organization_scroll_all_items)
        return self.weh.get_elements(self.global_settings_organization_scroll_get_colour, parent)

    def get_global_settings_account_organizations_add_button(self):
        return self.weh.get_elements(self.global_settings_account_organizations_add_button)

    def get_global_settings_account_organizations_save_button(self):
        return self.weh.get_element(self.global_settings_account_organization_save_button)

    def get_global_settings_account_organization_name_inputfield(self):
        return self.weh.get_element(self.global_settings_account_organization_name_inputfield)

    def get_global_settings_create_account_organization_scroll_button(self):
        """
        :return: get_global_settings_create_account_organization_scroll_button
        """
        return self.weh.get_element(self.global_settings_create_account_organization_scroll_button)

    def get_create_account_organization_drop_down_items(self):
        """
        :return: get_create_account_organization_drop_down_items
        """
        parent = self.weh.get_element(self.global_settings_create_account_organization_scroll_all_items)
        return self.weh.get_elements(self.global_settings_create_account_organization_scroll_get_name, parent)

    def get_global_settings_account_organization_section(self):
        """
        :return: get_global_settings_account_organization_section
        """

        return self.weh.get_element(self.global_settings_create_account_organization_section)

    def get_organization_grid_rows(self):
        """
        :return: all the rows in the authentication Logs grid
        """
        grid_rows = self.weh.get_elements(self.organization_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_organization_grid_rows_cells(self, row, field='field-name'):
        cells = self.weh.get_elements(self.organization_grid_rows_cell, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_global_settings_account_enable_hiq_button(self):
        """
        :return: get_global_settings_account_enable_hiq_button
        """
        return self.weh.get_element(self.global_settings_account_enable_hiq_button)

    def get_global_settings_account_enable_hiq_confirm_button(self):
        """
        :return: get_global_settings_account_enable_hiq_confirm_button
        """
        return self.weh.get_element(self.global_settings_account_enable_hiq_confirm_button)

    def get_global_settings_account_enable_hiq_status(self):
        """
        :return: all the rows in the authentication Logs grid
        """
        hiq_status_on_account = self.weh.get_element(self.global_settings_account_enable_hiq_button).get_attribute("disabled")
        if hiq_status_on_account == "true":
            return True
        else:
            return False

    def get_opt_out_copilot_beta_status(self):
        return self.weh.get_element(self.opt_out_copilot_beta_status_btn)

    def get_authentication_logs_view_all_pages_button(self):
        """
        :return: get_global_settings_account_enable_hiq_confirm_button
        """
        return self.weh.get_element(self.authentication_logs_view_all_pages)

    def get_authentication_logs_search_text_field(self):
        """
        :return: get_global_settings_account_enable_hiq_confirm_button
        """
        return self.weh.get_element(self.authentication_logs_search_text_field)

    def get_device_management_settings_menu(self):
        return self.weh.get_element(self.device_management_settings_menu)

    def get_device_management_settings_password(self):
        return self.weh.get_element(self.device_management_settings_password)

    def get_device_management_settings_password_confirm(self):
        return self.weh.get_element(self.device_management_settings_password_confirm)

    def get_device_management_settings_show_password_checkbox(self):
        return self.weh.get_element(self.device_management_settings_show_password_checkbox)

    def get_device_management_settings_save_button(self):
        return self.weh.get_element(self.device_management_settings_save_button)

    def get_authentication_logs_unknown_error_close_icon(self):
        """
        :return: get_authentication_logs_unknown_error_close_icon
        """
        return self.weh.get_element(self.authentication_logs_unknown_error_close_icon)

    def get_account_select_language_drop_down(self):
        return self.weh.get_element(self.account_select_language_drop_down)

    def get_account_select_language_drop_down_options(self):
        return self.weh.get_elements(self.account_select_language_drop_down_options)

    def get_account_language_apply_button(self):
        return self.weh.get_element(self.account_language_apply_button)

    def get_account_icon(self):
        return self.weh.get_element(self.account_icon)

    def get_global_settings(self):
        return self.weh.get_element(self.global_settings)

    def get_ssh_availability(self):
        return self.weh.get_element(self.SSH_availability)

    def get_enable_ssh(self):
        return self.weh.get_element(self.enable_ssh)

    def get_api_access_token_rows(self):
        return self.weh.get_elements(self.api_access_token_rows)

    def get_api_access_token_row_cells(self, row):
        return self.weh.get_elements(self.api_access_token_row_cells, row)

    def get_api_access_tokens_select_check_box(self):
        return self.weh.get_element(self.api_access_tokens_select_check_box)

    def get_api_access_tokens_delete_button(self):
        return self.weh.get_element(self.api_access_tokens_delete_button)

    def get_api_access_tokens_delete_cnfm_button(self):
        return self.weh.get_element(self.api_access_tokens_delete_cnfm_button)

    def get_account_time_zone_drop_down(self):
        return self.weh.get_element(self.account_time_zone_drop_down)

    def get_account_time_zone_drop_down_options(self):
        return self.weh.get_elements(self.account_time_zone_drop_down_options)

    def get_account_time_zone_apply_button(self):
        return self.weh.get_element(self.account_time_zone_apply_button)

    def get_viq_backup_now_button(self):
        return self.weh.get_element(self.viq_backup_now_button)

    def get_viq_last_backup_time_textfield(self):
        return self.weh.get_element(self.viq_last_backup_time_textfield)

    def get_viq_delete_data_button(self):
        return self.weh.get_element(self.viq_delete_data_button)

    def get_viq_backup_confirm_button(self):
        return self.weh.get_element(self.viq_backup_yes_button)

    def get_reset_viq_confirm_button(self):
        return self.weh.get_element(self.reset_viq_confirm_button)

    def get_industry_drop_down_button(self):
        return self.weh.get_element(self.account_industry_drop_down)

    def get_account_industry_drop_down_options(self):
        return self.weh.get_elements(self.account_industry_drop_down_options)

    def get_industry_apply_button(self):
        return self.weh.get_element(self.account_industry_apply_button)

    def get_audit_logs_view_all_pages_button(self):
        return self.weh.get_element(self.audit_logs_view_all_pages)

    def get_viq_export_button(self):
        return self.weh.get_element(self.viq_export_button)

    def get_viq_export_now_button(self):
        return self.weh.get_element(self.viq_export_now_button)

    def get_viq_export_yes_button(self):
        return self.weh.get_element(self.viq_export_yes_button)

    def get_viq_export_ok_button(self):
        return self.weh.get_element(self.viq_export_ok_button)

    def get_export_status_textfield_success(self):
        return self.weh.get_element(self.export_status_textfield_success)

    def get_export_status_textfield_fail(self):
        return self.weh.get_element(self.export_status_textfield_fail)

    def get_supplemental_cli_option_status(self):
        return self.weh.get_element(self.viq_supplemental_status)

    def get_ssh_availability_option_status(self):
        return self.weh.get_element(self.ssh_availability_option_status)

    def get_exos_device_management_settings_status(self):
        return self.weh.get_element(self.exos_device_management_settings_status)

    def get_exos_device_management_settings_save_button(self):
        return self.weh.get_element(self.exos_device_management_settings_save_button)