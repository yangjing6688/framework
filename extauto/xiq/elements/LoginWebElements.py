from extauto.xiq.defs.LoginWebElementsDefinitions import LoginWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler
from selenium.common.exceptions import NoSuchElementException


class LoginWebElements(LoginWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_login_page_username_text(self):
        return self.weh.get_element(self.login_page_username_text_ids)

    def get_login_page_password_text(self):
        return self.weh.get_element(self.login_page_password_text_ids)

    def get_login_page_login_button(self):
        return self.weh.get_element(self.login_page_login_button_ids)

    def get_logout_account_info(self):
        return self.weh.get_element(self.logout_account_info)

    def get_logout_user_menu_item(self):
        return self.weh.get_element(self.logout_user_menu_item)

    def get_account_info_menu_items(self):
        return self.weh.get_elements(self.menu_item)

    def get_dialog_message(self):
        try:
            db = self.weh.get_element(self.dialog_box)
            if db:
                if self.weh.get_element(self.dialog_box).is_displayed():
                    return True
                else:
                    return False
        except Exception:
            return False

    def get_dialog_box_close_button(self):
        try:
            parents = self.weh.get_elements(self.dialog_box)
            for parent in parents:
                if "CLOSE" in parent.text.upper():
                    children = self.weh.get_elements(self.dialog_box_close_button)

                    for child in children:
                        if "CLOSE" in child.text.upper():
                            return child
        except NoSuchElementException:
            return None

    def get_logout_link(self):
        menu = self.weh.get_element(self.logout_user_menu_item)
        menu_items = self.weh.get_elements(self.menu_item, menu)
        for menu_item in menu_items:
            if 'LOGOUT' in menu_item.text.upper():
                return menu_item

    def get_credentials_error_message(self):
        try:
            errors = self.weh.get_elements(self.login_page_wrong_password_message)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception:
            return "No Message"

    def get_welcome_page_done_button(self):
        buttons = self.weh.get_elements(self.welcome_page_done_button)
        for button in buttons:
            if "DONE" in button.text:
                return button

    def get_header_text(self):
        return self.weh.get_element(self.header_text).text

    def get_build_version_details(self):
        return self.weh.get_element(self.build_version_details).text

    def get_data_center_name(self):
        return self.weh.get_element(self.data_center_name).text

    def get_user_account_nav(self):
        return self.weh.get_element(self.user_account_nav)

    def get_about_extreme_cloudiq_link(self):
        return self.weh.get_element(self.click_about_extreme_cloudiq_link)

    def get_cancel_about_extremecloudiq_dialogue(self):
        elements = self.weh.get_elements(self.cancel_about_extremecloudiq_dialogue)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_switch_connection_host(self):
        return self.weh.get_element(self.switch_connection_host)

    def get_viq_id_field(self):
        return self.weh.get_element(self.viq_id_field)

    def get_30_days_trial_txt(self):
        return self.weh.get_element(self.txt_30_days_trial)

    ### Commented on 1/18/23 because this is a duplicate of a function below.
    ### The second function to be declared will be used. Thus, this function was commented
    #
    # def get_option_30_days_trial(self):
    #     return self.weh.get_element(self.option_30_days_trial)

    def get_drawer_trigger(self):
        return self.weh.get_element(self.drawer_trigger)

    def get_drawer_content(self):
        return self.weh.get_element(self.drawer_content)

    def get_right_arrow(self):
        return self.weh.get_element(self.right_arrow_displayed)

    def click_right_arrow(self):
        return self.weh.get_element(self.click_right_arrow_button)

    def get_wips_dialog_message(self):
        try:
            errors = self.weh.get_elements(self.wips_dialog_message)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception:
            return "No Message"

    def get_wips_popup_dialog_close_button(self):
        return self.weh.get_element(self.wips_popup_dialog_close_button)

    def get_wips_popup_dialog_dont_show_again_checkbox(self):
        return self.weh.get_element(self.wips_popup_dialog_dont_show_again_checkbox)

    def get_login_logo(self):
        return self.weh.get_element(self.login_logo)

    # There is a duplicate of this function above that was commented out on 1/18/23
    def get_option_30_days_trial(self):
        return self.weh.get_element(self.trial_30day_login_option)

    def get_extr_license_txt(self):
        return self.weh.get_element(self.txt_extr_license)

    def get_option_extr_cloudiq_license(self):
        return self.weh.get_element(self.extr_cloudiq_license_login_option)

    def get_legacy_license_txt(self):
        return self.weh.get_element(self.txt_legacy_license)

    def get_option_legacy_license(self):
        return self.weh.get_element(self.legacy_license_login_option)

    def get_extr_connect_txt(self):
        return self.weh.get_element(self.txt_extr_connect)

    def get_option_extr_connect(self):
        return self.weh.get_element(self.extr_connect_login_option)

    def get_get_started_button(self):
        return self.weh.get_element(self.get_started_btn)

    def get_next_button(self):
        return self.weh.get_element(self.get_next_btn)

    def get_finish_button(self):
        return self.weh.get_element(self.get_finish_button)

    def get_welcome_page_option(self):
        return self.weh.get_element(self.welcome_page_option)

    def get_cloud_tos_agree(self):
        return self.weh.get_element(self.cloud_tos_popup_agree)

    def get_cloud_tos_submit(self):
        return self.weh.get_element(self.cloud_tos_popup_submit)

    def get_first_tos_header(self):
        return self.weh.get_element(self.first_tos_header)

    def get_second_tos_header(self):
        return self.weh.get_element(self.second_tos_header)

    def get_upgrade_btn(self):
        return self.weh.get_element(self.upgrade_btn)

    def get_upgrade_link(self):
        return self.weh.get_element(self.upgrade_link)

    def get_legacy_ek_input_box(self):
        return self.weh.get_element(self.legacy_ek_input_box)

    def get_legacy_ek_invalid_err(self):
        return self.weh.get_element(self.legacy_ek_invalid_err)

    def get_legacy_ek_popup_hdr(self):
        return self.weh.get_element(self.legacy_ek_popup_hdr)

    def get_legacy_ek_popup_no_btn(self):
        return self.weh.get_element(self.legacy_ek_popup_no_btn)

    def get_legacy_ek_popup_submit_btn(self):
        return self.weh.get_element(self.legacy_ek_popup_submit_btn)

    def get_extr_license_tooltip(self):
        return self.weh.get_element(self.extr_license_tooltip)

    def get_sfdc_login_username(self):
        return self.weh.get_element(self.sfdc_login_email)

    def get_sfdc_login_pwd(self):
        return self.weh.get_element(self.sfdc_login_pwd)

    def get_sfdc_login_btn(self):
        return self.weh.get_element(self.sfdc_login_btn)

    def get_sfdc_login_err(self):
        return self.weh.get_element(self.sfdc_login_error)

    def get_shared_cuid_hdr(self):
        return self.weh.get_element(self.shared_cuid_hdr)

    def get_shared_cuid_input(self):
        return self.weh.get_element(self.shared_cuid_input)

    def get_shared_cuid_submit_btn(self):
        return self.weh.get_element(self.shared_cuid_submit_btn)

    def get_shared_cuid_cancel_btn(self):
        return self.weh.get_element(self.shared_cuid_cancel_btn)

    def get_shared_cuid_err(self):
        return self.weh.get_element(self.shared_cuid_error)

    def get_login_trail_30_days(self):
        return self.weh.get_element(self.login_trail_30_days)

    def get_login_license_option(self):
        return self.weh.get_element(self.login_license_option)

    def get_login_entitlement_radio(self):
        return self.weh.get_element(self.login_entitlement_radio)

    def get_login_entitlement_key(self):
        return self.weh.get_element(self.login_entitlement_key)

    def get_login_year_trail_option(self):
        return self.weh.get_element(self.login_year_trail_option)

    def get_login_iq_connect(self):
        return self.weh.get_element(self.login_iq_connect)

    def get_started_login_button(self):
        return self.weh.get_element(self.get_started_btn)

    def get_accept_terms_of_service_wizard(self):
        return self.weh.get_element(self.terms_accept_terms_btn)

    def get_submit_terms_of_service_wizard(self):
        return self.weh.get_element(self.submit_terms_btn)

    def get_accept_data_privacy(self):
        return self.weh.get_element(self.accept_data_privacy)

    def get_submit_data_privacy(self):
        return self.weh.get_element(self.submit_data_privacy)

    def get_deploy_cloud_radio_button(self):
        return self.weh.get_element(self.deploy_cloud_button)

    def get_lets_get_started(self):
        return self.weh.get_element(self.lets_get_started)

    def get_welcome_wizard_heading(self):
        return self.weh.get_element(self.welcome_wizard_heading)

    def get_agree_checkbox(self):
        return self.weh.get_element(self.agree_checkbox)

    def get_salesforce_username(self):
        return self.weh.get_element(self.salesforce_username)

    def get_salesforce_password(self):
        return self.weh.get_element(self.salesforce_password)

    def get_salesforce_submit(self):
        return self.weh.get_element(self.salesforce_submit)

    def get_entitlement_key_error(self):
        return self.weh.get_element(self.entitlement_key_error)

    def get_enter_shared_cuid(self):
        return self.weh.get_element(self.enter_shared_cuid)

    def get_submit_shared_cuid(self):
        return self.weh.get_element(self.submit_shared_cuid)

    def get_check_error_shared_cuid(self):
        return self.weh.get_element(self.check_error_shared_cuid)

    def get_login_portal_page_username_text(self):
        return self.weh.get_element(self.login_portal_page_username_text)

    def get_login_portal_page_password_text(self):
        return self.weh.get_element(self.login_portal_page_password_text)

    def get_login_portal_page_login_button(self):
        return self.weh.get_element(self.login_portal_page_login_button)

    def get_login_portal_check_error(self):
        elements = self.weh.get_elements(self.login_portal_check_error)
        if elements:
            for el in elements:
                if el.is_displayed():
                    return el
                else:
                    return None
        else:
            return None

    def get_add_button_portal(self):
        return self.weh.get_element(self.add_button_portal)

    def get_customer_name_field(self):
        return self.weh.get_element(self.customer_name_field)

    def get_admin_first_name_field(self):
        return self.weh.get_element(self.admin_first_name_field)

    def get_admin_last_name_field(self):
        return self.weh.get_element(self.admin_last_name_field)

    def get_admin_email_field(self):
        return self.weh.get_element(self.admin_email_field)

    def get_admin_password_field(self):
        return self.weh.get_element(self.admin_password_field)

    def get_data_center_dropdown(self):
        return self.weh.get_element(self.data_center_dropdown)

    def get_data_center_dropdown_options(self):
        return self.weh.get_elements(self.data_center_dropdown_options)

    def get_submit_button(self):
        return self.weh.get_element(self.submit_button)

    def get_cell_menu_button_name_section(self):
        return self.weh.get_element(self.cell_menu_button_name_section)

    def get_filter_type_dropdown(self):
        return self.weh.get_element(self.filter_type_dropdown)

    def get_filter_dropdown_option_equals(self):
        return self.weh.get_element(self.filter_dropdown_option_equals)

    def get_filter_text_box(self):
        return self.weh.get_element(self.filter_text_box)

    def get_user_found(self):
        return self.weh.get_elements(self.user_found)

    def get_delete_button(self):
        return self.weh.get_element(self.delete_button)

    def get_confirmation_option_yes(self):
        return self.weh.get_element(self.confirmation_option_yes)

    def get_delete_confirmation(self):
        return self.weh.get_element(self.delete_confirmation)

    def get_log_out_button_portal(self):
        return self.weh.get_element(self.log_out_button_portal)

    def get_cancel_button(self):
        return self.weh.get_element(self.cancel_button)

    def get_page_loading(self):
        return self.weh.get_element(self.page_loading)

    def get_external_admin_account_names(self):
        return self.weh.get_elements(self.external_admin_account_names)

    def get_admin_portal_page(self):
        return self.weh.get_element(self.admin_portal_page)

    def get_external_admin_manage_my_network_button(self):
        return self.weh.get_element(self.external_admin_manage_my_network_button)

    def get_external_admin_account_name_search_field(self):
        return self.weh.get_element(self.external_admin_account_name_search_field)

    def get_login_sso_page_username_text(self):
        return self.weh.get_element(self.login_sso_page_username_text)

    def get_login_sso_page_password_text(self):
        return self.weh.get_element(self.login_sso_page_password_text)

    def get_login_sso_page_login_button(self):
        return self.weh.get_element(self.login_sso_page_login_button)

    def get_login_sso_page_sign_in_error_message(self):
        try:
            errors = self.weh.get_elements(self.login_sso_page_login_error_message)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception:
            return "No Message"

    def get_iam_login_sso_page_username_text(self):
        return self.weh.get_element(self.iam_login_sso_page_username_text)

    def get_iam_login_sso_page_password_text(self):
        return self.weh.get_element(self.iam_login_sso_page_password_text)

    def get_iam_login_sso_page_login_button(self):
        return self.weh.get_element(self.iam_login_sso_page_login_button)