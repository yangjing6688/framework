from extauto.common.WebElementHandler import *
from xiq.defs.PasswordResetWebElementsDefinition import *


class PasswordResetWebElements(PasswordResetWebElementsDefinition):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_account_icon(self):
        return self.weh.get_element(self.account_icon)

    def get_global_settings(self):
        return self.weh.get_element(self.global_settings)

    def get_account_management(self):
        return self.weh.get_element(self.account_management)

    def get_add_account(self):
        return self.weh.get_element(self.add_account)

    def get_email_textbox(self):
        return self.weh.get_element(self.email_textbox)

    def get_name_textbox(self):
        return self.weh.get_element(self.name_textbox)

    def get_save_button(self):
        return self.weh.get_element(self.save_button)

    def get_password_textbox(self):
        return self.weh.get_element(self.password_textbox)

    def get_conf_password_texbox(self):
        return self.weh.get_element(self.confirm_password_textbox)

    def get_set_password_button(self):
        return self.weh.get_element(self.set_password_button)

    def get_reset_password_button(self):
        return self.weh.get_element(self.reset_password_button)

    def get_user_table(self):
        return self.weh.get_elements(self.user_table)

    def get_delete_icon(self):
        return self.weh.get_element(self.delete_icon)

    def get_delete_alert(self):
        return self.weh.get_element(self.delete_alert)

    def get_forgot_password_reset_it_here_link(self):
        return self.weh.get_element(self.forgot_password_reset_it_here_link)

    def get_forgot_password_email_textfield(self):
        return self.weh.get_element(self.forgot_password_email_textfield)

    def get_forgot_password_reset_password_button(self):
        return self.weh.get_element(self.forgot_password_reset_password_button)

    def get_forgot_password_result_label(self):
        return self.weh.get_element(self.forgot_password_result_label).text