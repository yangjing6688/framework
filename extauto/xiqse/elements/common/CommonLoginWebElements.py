from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.common.CommonLoginWebElementsDefinitions import CommonLoginWebElementsDefinitions


class CommonLoginWebElements(CommonLoginWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_login_page_title(self):
        """
        :return: Title on the login page
        """
        return self.weh.get_element(self.login_page_title)

    def get_login_page_username_text(self):
        """
        :return: User Name text field on the login page
        """
        return self.weh.get_element(self.login_page_username_text)

    def get_login_page_password_text(self):
        """
        :return: Password text field on the login page
        """
        return self.weh.get_element(self.login_page_password_text)

    def get_login_page_login_button(self):
        """
        :return: Login button on the login page
        """
        return self.weh.get_element(self.login_page_login_button)

    def get_credentials_error_message(self):
        """
        :return: Error message, if any, on the login page
        """
        try:
            errors = self.weh.get_elements(self.login_page_error_message)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception:
            return "No Message"

    def get_login_page_copyright_label(self):
        """
        :return: Copyright label on the login page
        """
        return self.weh.get_element(self.login_copyright_label)

    def get_login_page_support_link(self):
        """
        :return: Support Link on the login page
        """
        return self.weh.get_element(self.login_support_link)

    def get_login_page_about_link(self):
        """
        :return: About Link on the login page
        """
        return self.weh.get_element(self.login_about_link)
