from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.license.LicenseOnboardWebElements import LicenseOnboardWebElements
from xiqse.elements.license.LicenseCommonWebElements import LicenseCommonWebElements


class XIQSE_LicenseOnboard(LicenseOnboardWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.common_els = LicenseCommonWebElements()

    def xiqse_confirm_onboard_page_displayed(self):
        """
         - This keyword confirms the Onboard to ExtremeCloud IQ page is being displayed.
         - Keyword Usage
          - ``XIQSE Confirm Onboard Page Displayed``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        welcome_title = self.common_els.get_welcome_title()
        onboard_title = self.get_onboard_title()
        email_field = self.get_email_field()
        pwd_field = self.get_password_field()
        advanced_link = self.get_advanced_link()
        onboard_btn = self.get_onboard_button()
        copyright_label = self.common_els.get_copyright_label()
        if welcome_title and onboard_title and email_field and pwd_field and advanced_link and onboard_btn and copyright_label:
            self.utils.print_info("Onboard to ExtremeCloud IQ page is properly displayed")
            ret_val = 1
        else:
            self.utils.print_info("Onboard to ExtremeCloud IQ page is not properly displayed")
            if not welcome_title:
                self.utils.print_info("  Unable to find 'Welcome to Extreme Cloud IQ - Site Engine' title")
            if not onboard_title:
                self.utils.print_info("  Unable to find 'Onboard to ExtremeCloud IQ' title")
            if not email_field:
                self.utils.print_info("  Unable to find 'Email' field")
            if not pwd_field:
                self.utils.print_info("  Unable to find 'Password' field")
            if not onboard_btn:
                self.utils.print_info("  Unable to find 'Onboard' button")
            if not copyright_label:
                self.utils.print_info("  Unable to find copyright label")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def get_xiqse_serial_number_from_onboard_page(self):
        """
         - This keyword returns the XIQ-SE serial number listed on the Advanced section of the Welcome/Onboard page.
         - Keyword Usage
          - ``Get XIQSE Serial Number from Onboard Page``

        :return: XIQ-SE serial number, if found;  else, -1
        """
        ret_val = ""
        advanced_link = self.get_advanced_link()
        if advanced_link:
            self.utils.print_info("Clicking 'Advanced' link...")
            self.auto_actions.click(advanced_link)
            # Get the XIQ-SE Serial Number label value
            sleep(2)
            ret_val = self.get_xiqse_serial_number_label_value_from_onboard_page()

            # Hide the Advanced section
            hide_link = self.get_hide_advanced_link()
            if hide_link:
                self.utils.print_info("Clicking 'Hide Advanced' link...")
                self.auto_actions.click(hide_link)
            else:
                self.utils.print_info("Unable to find the 'Hide Advanced' link")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the 'Advanced' link")
            self.screen.save_screen_shot()

        return ret_val

    def get_xiqse_serial_number_label_value_from_onboard_page(self):
        """
         - This keyword returns the XIQ-SE serial number, found on the Welcome/Onboard page.
         - It is assumed the Welcome/Onboard page is displayed and the Advanced section is expanded.
         - Keyword Usage
          - ``Get XIQSE Serial Number Label Value from Onboard Page``

        :return: XIQ-SE serial number, if found;  else, empty string
        """
        ret_val = ""
        the_label = self.get_serial_number_label()
        if the_label:
            label_text = the_label.text
            if label_text:
                self.utils.print_info(f"Label text is {label_text}")

                # Split the string to get the serial number component
                prefix, serial_number = label_text.split(":")
                self.utils.print_debug(f"Prefix is '{prefix}'")
                self.utils.print_info(f"Serial Number is '{serial_number.strip()}'")
                ret_val = serial_number.strip()
            else:
                self.utils.print_info("Unable to obtain the XIQ-SE Serial Number label text")
        else:
            self.utils.print_info("Unable to find the XIQ-SE Serial Number label")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_onboard_to_xiq(self, email, pwd):
        """
         - This keyword enters the email and password and clicks the Onboard button on the Onboard to XIQ page.
         - It is assumed the Onboard to ExtremeCloud IQ page is displayed.
         - NOTE: this keyword does not check that the onboard itself was successful.
         - Keyword Usage
          - ``XIQSE Onboard to XIQ``

        :param email: value to enter in the Email field
        :param pwd: value to enter in the Password field
        :return: 1 if action successful, else -1
        """
        ret_val = -1
        email_field = self.get_email_field()
        pwd_field = self.get_password_field()
        onboard_btn = self.get_onboard_button()
        if email_field and pwd_field and onboard_btn:
            self.utils.print_info("Entering Email value")
            self.auto_actions.send_keys(email_field, email)
            self.utils.print_info("Entering Password value")
            self.auto_actions.send_keys(pwd_field, pwd)
            self.utils.print_info("Clicking Onboard")
            self.auto_actions.click(onboard_btn)

            self.utils.print_info("Checking for errors...")
            error_label = self.get_error_label()
            if error_label and error_label.text:
                self.utils.print_info(f"Error text is '{error_label.text}'")
                ret_val = -1
            else:
                self.utils.print_info("Successfully entered XIQ credentials and clicked Onboard")
                self.screen.save_screen_shot()
                ret_val = 1
        else:
            self.utils.print_info("Unable to onboard to XIQ")
            if not email_field:
                self.utils.print_info("  Unable to find 'Email' field")
            if not pwd_field:
                self.utils.print_info("  Unable to find 'Password' field")
            if not onboard_btn:
                self.utils.print_info("  Unable to find 'Onboard' button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
