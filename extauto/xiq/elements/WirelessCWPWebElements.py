from extauto.xiq.defs.WirelessCWPWebElementsDefinitions import WirelessCWPWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class WirelessCWPWebElements(WirelessCWPWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_enable_captive_web_portal(self):
        return self.weh.get_element(self.enable_captive_web_portal_slide_button)

    def get_enable_extreme_guest_essentials_slide_button(self):
        return self.weh.get_element(self.enable_extreme_guest_essentials_slide_button)

    def get_walled_garden_add_button(self):
        return self.weh.get_element(self.walled_garden_add_button)

    def get_walled_garden_text_area(self):
        return self.weh.get_element(self.walled_garden_text_area)

    def get_walled_garden_text_add_button(self):
        return self.weh.get_element(self.walled_garden_text_add_button)

    def get_cloud_cwp_radio_button(self):
        return self.weh.get_element(self.cloud_captive_web_portal_radio_button)

    def get_social_login_radio_button(self):
        return self.weh.get_element(self.cloud_cwp_social_login_radio_button)

    def get_default_cwp_add_button(self):
        return self.weh.get_element(self.default_cwp_add_button)

    def get_default_cwp_edit_link(self):
        return self.weh.get_element(self.default_cwp_edit_link)

    def get_default_cwp_name_field(self):
        return self.weh.get_element(self.default_cwp_name_field)

    def get_cloud_cwp_restrict_domain_field(self):
        return self.weh.get_element(self.open_template_cloud_cwp_restrict_domain)

    def get_cloud_cwp_cache_duration_field(self):
        return self.weh.get_element(self.open_template_cloud_cwp_cache_duration)

    def get_default_add_windows_cwp_save_cwp_button(self):
        return self.weh.get_element(self.default_cwp_add_dialog_save_cwp_button)

    def get_default_cwp_add_dialog_cwp_cancel_cwp_button(self):
        return self.weh.get_element(self.default_cwp_add_dialog_cancel_cwp_button)

    def get_cwp_dialog_window_cancel_button(self):
        return self.weh.get_element(self.cwp_dialog_window_cancel_button)

    def get_default_cwp_select_button(self):
        return self.weh.get_element(self.default_cwp_select_button)

    def get_default_select_window_cwp_rows(self):
        return self.weh.get_elements(self.default_select_window_cwp_rows)

    def get_default_cwp_select_window_select_button(self):
        return self.weh.get_element(self.default_cwp_select_window_select_button)

    def get_default_cwp_select_window_cancel_button(self):
        return self.weh.get_element(self.default_cwp_select_window_cancel_button)

    def get_default_cwp_select_window_row_select_check_box(self, row):
        return self.weh.get_element(self.default_cwp_select_window_row_select_check_box, row)

    def get_cloud_cwp_social_login_type_fb(self):
        return self.weh.get_element(self.cloud_cwp_social_login_type_facebook)

    def get_cloud_cwp_social_login_type_google(self):
        return self.weh.get_element(self.cloud_cwp_social_login_type_google)

    def get_cloud_cwp_social_login_type_linkedin(self):
        return self.weh.get_element(self.cloud_cwp_social_login_type_linkedin)

    def get_enable_captive_web_portal_cwp_radio_button(self):
        return self.weh.get_element(self.captive_web_portal_radio_button)

    def get_user_auth_on_captive_web_portal(self):
        return self.weh.get_element(self.user_auth_on_captive_web_portal)

    def get_enable_self_registration(self):
        return self.weh.get_element(self.enable_self_registration)

    def get_return_aerohive_private_psk(self):
        return self.weh.get_element(self.return_aerohive_private_psk)

    def get_enable_upa(self):
        return self.weh.get_element(self.enable_upa)

    def get_choose_access_ssid_drop_down(self):
        return self.weh.get_element(self.choose_access_ssid_drop_down)

    def get_choose_access_ssid_options(self):
        return self.weh.get_elements(self.choose_access_ssid_options)

    def get_choose_a_ppsk_server_drop_down(self):
        return self.weh.get_element(self.choose_a_ppsk_server_drop_down)

    def get_choose_a_ppsk_server_options(self):
        return self.weh.get_elements(self.choose_a_ppsk_server_options)

    def get_employee_approval_radio_button(self):
        return self.weh.get_element(self.employee_approval_radio_button)

    def get_approve_email_domain_list_rows(self):
        return self.weh.get_elements(self.approve_email_domain_list_rows)

    def get_approve_email_domain_list_row_cell(self, row, field='field-name'):
        cells = self.weh.get_elements(self.approve_email_domain_list_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_approve_email_domain_list_add_button(self):
        return self.weh.get_element(self.approve_email_domain_list_add_button)

    def get_approve_email_domain_list_domain_name(self):
        return self.weh.get_element(self.approve_email_domain_list_domain_name)

    def get_approve_email_domain_list_domain_add_button(self):
        return self.weh.get_element(self.approve_email_domain_list_domain_add_button)

    def get_request_pin_radio_button(self):
        return self.weh.get_element(self.request_pin_radio_button)

    def get_valid_pin_time_drop_down(self):
        return self.weh.get_element(self.valid_pin_time_drop_down)

    def get_valid_pin_time_option(self):
        return self.weh.get_elements(self.valid_pin_time_drop_down_options)

    def get_email_address_daily_report_field(self):
        return self.weh.get_element(self.email_address_daily_report_field)

    def get_daily_report_delivery_time_hour_drop_down(self):
        return self.weh.get_element(self.daily_report_delivery_time_hour)

    def get_daily_report_delivery_time_hour_options(self):
        return self.weh.get_elements(self.daily_report_delivery_time_hour_options)

    def get_daily_report_delivery_time_minutes_drop_down(self):
        return self.weh.get_element(self.daily_report_delivery_time_minutes)

    def get_daily_report_delivery_time_minutes_options(self):
        return self.weh.get_elements(self.daily_report_delivery_time_minutes_options)

    def get_customise_cwp_setting(self):
        return self.weh.get_element(self.customise_cwp_setting)

    def get_create_web_file_directory(self):
        return self.weh.get_element(self.create_web_file_directory_button)

    def get_directory_name(self):
        return self.weh.get_element(self.directory_name)

    def get_web_file_directory_create_button(self):
        return self.weh.get_element(self.web_file_directory_create_button)

    def get_web_file_directory_create_done_button(self):
        return self.weh.get_element(self.web_file_directory_create_done_button)

    def get_web_file_directory_drop_down(self):
        return self.weh.get_element(self.web_file_directory_drop_down)

    def get_web_file_directory_drop_down_options(self):
        return self.weh.get_elements(self.web_file_directory_drop_down_options)

    def get_manage_upload_remove_files(self):
        return self.weh.get_element(self.manage_upload_remove_files_button)

    def get_manage_file_choose_field(self):
        return self.weh.get_element(self.manage_file_choose_field)

    def get_manage_file_choose_done_button(self):
        return self.weh.get_element(self.manage_file_choose_done_button)

    def get_customise_login_page_drop_down(self):
        return self.weh.get_element(self.customise_login_page_drop_down)

    def get_customise_login_page_drop_down_option(self):
        return self.weh.get_elements(self.customise_login_page_drop_down_option)

    def get_customise_success_page_drop_down(self):
        return self.weh.get_element(self.customise_success_page_drop_down)

    def get_customise_success_page_drop_down_options(self):
        return self.weh.get_elements(self.customise_success_page_drop_down_options)

    def get_cwp_wireless_network_save_button(self):
        return self.weh.get_element(self.cwp_wireless_network_save_button)

    def get_customise_and_preview_button(self):
        return self.weh.get_element(self.customise_and_preview_button)

    def get_auth_method_drop_down(self):
        return self.weh.get_element(self.auth_method_drop_down)

    def get_auth_method_drop_down_options(self):
        return self.weh.get_elements(self.auth_method_drop_down_options)

    def get_wir_auth_with_extiq_auth_service_slider_button(self):
        return self.weh.get_element(self.wir_auth_with_extiq_auth_service_slider_button)

    def get_import_html_button(self):
        return self.weh.get_element(self.import_html_button)

    def get_user_auth_return_ppsk_link(self):
        return self.weh.get_element(self.user_auth_return_ppsk_link)

    def get_cwp_wireless_network_cancel_button(self):
        return self.weh.get_element(self.wireless_network_cancel_button)

    def get_cwp_error_message(self):
        """
        :return:
        """
        parent = self.weh.get_element(self.default_cwp_add_dialog_window)
        return self.weh.get_element(self.cwp_error_message, parent)

    def get_failure_page_container(self):
        return self.weh.get_element(self.failure_page_container)
