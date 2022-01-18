from common.WebElementHandler import *
from xiqse.defs.license.LicenseOnboardWebElementsDefinitions import LicenseOnboardWebElementsDefinitions


class LicenseOnboardWebElements(LicenseOnboardWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_onboard_title(self):
        """
        :return: Gets the "Onboard to ExtremeCloud IQ" title
        """
        return self.weh.get_element(self.onboard_title)

    def get_advanced_link(self):
        """
        :return: Gets the "Advanced" link
        """
        return self.weh.get_element(self.advanced_link)

    def get_hide_advanced_link(self):
        """
        :return: Gets the "Hide Advanced" link
        """
        return self.weh.get_element(self.hide_advanced_link)

    def get_email_field(self):
        """
        :return: Gets the "Email" field text box
        """
        return self.weh.get_element(self.email_field)

    def get_password_field(self):
        """
        :return: Gets the "Password" field text box
        """
        return self.weh.get_element(self.password_field)

    def get_viq_id_field(self):
        """
        :return: Gets the "VIQ ID" field text box
        """
        return self.weh.get_element(self.viq_id_field)

    def get_specify_proxy_server_checkbox(self):
        """
        :return: Gets the "Specify Proxy Server" check button
        """
        return self.weh.get_element(self.specify_proxy_checkbox)

    def get_proxy_server_field(self):
        """
        :return: Gets the "Proxy Server" field text box
        """
        return self.weh.get_element(self.proxy_server_field)

    def get_port_id_field(self):
        """
        :return: Gets the "Port ID" field text box
        """
        return self.weh.get_element(self.port_id_field)

    def get_proxy_authentication_checkbox(self):
        """
        :return: Gets the "Proxy Authentication" checkbox
        """
        return self.weh.get_element(self.proxy_auth_checkbox)

    def get_proxy_username_field(self):
        """
        :return: Gets the "Proxy Username" field text box
        """
        return self.weh.get_element(self.proxy_username_field)

    def get_proxy_password_field(self):
        """
        :return: Gets the "Proxy Password" field text box
        """
        return self.weh.get_element(self.proxy_password_field)

    def get_serial_number_label(self):
        """
        :return: Gets the serial number label
        """
        return self.weh.get_element(self.serial_label)

    def get_onboard_button(self):
        """
        :return: Gets the "Onboard" button
        """
        return self.weh.get_element(self.onboard_button)

    def get_error_label(self):
        """
        :return: Gets the error label
        """
        return self.weh.get_element(self.error_label)
