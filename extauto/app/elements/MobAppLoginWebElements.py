from app.defs.MobAppWebElementsDefinition import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *
from selenium.common.exceptions import NoSuchElementException


class MobAppLoginWebElements(MobAppWebElementsDefinition):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_qa_env_login_url(self):
        return self.weh.get_element(self.qa_env_login_url_id)

    def get_qa_env_save_button(self):
        return self.weh.get_element(self.qa_env_save_button_id)

    def get_login_page_username_field(self):
        return self.weh.get_element(self.login_page_uname_id)

    def get_login_page_pwd_field(self):
        return self.weh.get_element(self.login_page_password_id)

    def get_login_pwd_toggle(self):
        return self.weh.get_element(self.password_toggle_id)

    def get_login_page_button_id(self):
        return self.weh.get_element(self.login_page_button_id)

    def get_image_title_text(self):
        title_text = self.weh.get_element(self.image_description_text_id)
        if title_text.is_displayed():
            return title_text.text

    def get_image_description_text(self):
        desc_text = self.weh.get_element(self.image_description_text_id)
        if desc_text.is_displayed():
            return desc_text.text

    def get_multi_factor_auth_text_field(self):
        return self.weh.get_element(self.multi_factor_auth_textfield_id)

    def get_multi_factor_submit_button(self):
        return self.weh.get_element(self.multi_factor_auth_submit_button)

    def get_cannot_enter_code_text(self):
        multi_factor = self.weh.get_element(self.cannot_enter_code_text_id)
        if multi_factor.is_displayed():
            return multi_factor.text

    def get_emergency_recovery_code(self):
        return self.weh.get_element(self.emergency_recovery_code_id)

    def get_up_bottom_sheet(self):
        return self.weh.get_element(self.bottom_sheet_id)

    def logout_from_device(self):
        return self.weh.get_element(self.logout_device_id)

    def top_button(self):
        return self.weh.get_element(self.top_button_id)

    def logout_yes_button(self):
        return self.weh.get_element(self.logout_yes_button_id)

    def logout_cancel_button(self):
        return self.weh.get_element(self.logout_cancel_button_id)

    def trouble_login_device(self):
        return self.weh.get_element(self.trouble_logging_id)

    def support_email_text_field(self):
        return self.weh.get_element(self.support_email_id_text_field)

    def reset_password_button(self):
        return self.weh.get_element(self.reset_password_button_id)

    def back_to_login(self):
        return self.weh.get_element(self.back_to_login_button_id)

    def get_email_sent_confirmation(self):
        email_confirmation = self.weh.get_element(self.email_sent_confirmation_id)
        if email_confirmation.is_displayed():
            return email_confirmation.text

    def trouble_login_text(self):
        trouble_login = self.weh.get_element(self.trouble_login_text_id)
        if trouble_login.is_displayed():
            return trouble_login.text

    def trouble_login_close_link(self):
        return self.weh.get_element(self.trouble_logging_close_link_id)

    def get_menu_item(self):
        return self.weh.get_element(self.menu_item_id)

    def get_settings_item(self):
        return self.weh.get_element(self.settings_item_id)

    def get_settings_backward_link(self):
        return self.weh.get_element(self.settings_backward_link_id)

    def get_about_item(self):
        return self.weh.get_element(self.about_item_id)

    def get_about_bw_link(self):
        return self.weh.get_element(self.about_bw_link_id)

    def get_data_center_name(self):
        name = self.weh.get_element(self.data_center_name_id)
        if name.is_displayed():
            return name.text

    def get_app_version_name(self):
        app_name = self.weh.get_element(self.app_version_name_id)
        if app_name.is_displayed():
            return app_name.text

    def get_menu_item_logout(self):
        return self.weh.get_element(self.menu_item_logout_id)

    def get_customer_id(self):
        customer = self.weh.get_element(self.customer_info_id_)
        if customer.is_displayed():
            return customer.text

    def get_company_id(self):
        company = self.weh.get_element(self.company_info_id)
        if company.is_displayed():
            return company.text

    def get_wrong_message(self):
        msg = self.weh.get_element(self.login_wrong_password_msg_id)
        if msg.is_displayed():
            return msg.text

    def get_wrong_password_message(self):
        try:
            errors = self.weh.get_elements(self.login_wrong_password_msg_id)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception as e:
            return "No Message"

    def get_account_blocked_message(self):
        try:
            errors = self.weh.get_elements(self.login_page_account_blocked_id)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception as e:
            return "No Message"

    def get_my_cloud_network(self):
         return self.weh.get_element(self.my_cloud_network_id)

    def get_external(self):
        return self.weh.get_element(self.external_networks_id)

    def get_switch_button(self):
        return self.weh.get_element(self.switch_button_id)

    def get_external_nw_search(self):
        return self.weh.get_element(self.external_nw_search_field)

    def get_external_nw_table(self):
         return self.weh.get_element(self.external_nw_table_id)

    def get_external_nw_row(self):
        nw = self.get_external_nw_table()
        return self.weh.get_elements(self.external_nw_row_id, parent=nw)











