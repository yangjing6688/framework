from extauto.xiq.defs.ClientModeDefinitions import ClientModeDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class ClientModeWebElements(ClientModeDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_login_page_username_text(self):
        return self.weh.get_element(self.login_page_username_text)

    def get_login_page_password_text(self):
        return self.weh.get_element(self.login_page_password_text)

    def get_login_page_login_button(self):
        return self.weh.get_element(self.login_page_login_button)

    def get_admin_page_client_mode_ssid_tab(self):
        return self.weh.get_element(self.admin_page_client_mode_ssid_tab)

    def get_wifi_connection_status(self):
        return self.weh.get_element(self.wifi_connection_status)

    def get_other_ssids_button(self):
        return self.weh.get_element(self.other_ssids_button)

    def get_ssid_textbox(self):
        return self.weh.get_element(self.ssid_textbox)

    def get_security_type_dropbox(self, security):
        self.security_type_dropbox['XPATH'] += security + '"]'
        return self.weh.get_element(self.security_type_dropbox)

    def get_password_textbox(self):
        return self.weh.get_element(self.password_textbox)

    def get_connect_button(self):
        return self.weh.get_element(self.connect_button)

    def get_cancel_button(self):
        return self.weh.get_element(self.cancel_button)
