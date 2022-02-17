from extauto.xiq.elements.extreme_guest.MuSocialWebElements import MuSocialWebElements
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from time import sleep


class MuGuestPortal(MuSocialWebElements):
    def __init__(self):
        super().__init__()
        self.cli = Cli()
        self.auto_actions = AutoActions()

    def validate_eguest_social_login_with_facebook(self, username, password):
        """
        - Register network via facebook login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
         - ``Validate EGuest Social Login With Facebook  ${FACEBOOK_USERNAME}   ${FACEBOOK_PASSWORD}``

        :param username: Facebook Username
        :param password: Facebook Password
        :return: 1 if successfully connected with internet with social login type facebook else -1
        """
        self.utils.print_info("Click Social Login facebook button")
        self.auto_actions.click(self.get_social_wifi_all_facebook_icon())
        self.get_gp_page_screen_shot()
        sleep(5)

        self.utils.print_info("Enter Facebook Username")
        self.auto_actions.send_keys(self.get_social_wifi_all_facebook_username_field(), username)

        self.utils.print_info("Enter Facebook Password")
        self.auto_actions.send_keys(self.get_social_wifi_all_facebook_password_field(), password)

        self.utils.print_info("Click Facebook Sign in button")
        self.auto_actions.click(self.get_social_wifi_all_facebook_login_button())
        sleep(5)

        if self.get_social_wifi_all_facebook_login_error_page():
            self.utils.print_info("Click Facebook error after login in button")
            self.auto_actions.click(self.get_social_wifi_all_facebook_login_error_page())
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            return -1

    def validate_eguest_social_login_with_linkedin(self, username, password):
        """
        - Register network via Linkedin login CWP
        - Validate Captive Web Portal social login with Linkedin credentials
        - Keyword Usage:
         - ``Validate EGuest Social Login With Linkedin  ${Linkedin_USERNAME}   ${Linkedin_PASSWORD}``
        :param username: Linkedin Username
        :param password: Linkedin Password
        :return: 1 if successfully connected with internet with social login type Linkedin else -1
        """
        self.utils.print_info("Click Social Login Linkedin button")
        self.auto_actions.click(self.get_social_wifi_all_linkedin_icon())
        self.get_gp_page_screen_shot()
        sleep(5)

        self.utils.print_info("Enter Linkedin Username")
        self.auto_actions.send_keys(self.get_social_wifi_all_linkedin_username_field(), username)

        self.utils.print_info("Enter Linkedin Password")
        self.auto_actions.send_keys(self.get_social_wifi_all_linkedin_password_field(), password)

        self.utils.print_info("Click Linkedin Sign in button")
        self.auto_actions.click(self.get_social_wifi_all_linkedin_signin_button())
        sleep(5)

        self.utils.print_info("Click Linkedin Allow button")
        self.auto_actions.click(self.get_social_wifi_all_linkedin_allow_button())
        sleep(5)

        if self.get_social_wifi_all_linkedin_login_error_page():
            self.utils.print_info("Click Linkedin error after login in button")
            self.auto_actions.click(self.get_social_wifi_all_linkedin_login_error_page())
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            return -1

    def validate_eguest_social_login_with_google(self, username, password):
        """
        - Register network via google login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
         - ``Validate EGuest Social Login With Google  ${GOOGLE_USERNAME}   ${GOOGLE_PASSWORD}``

        :param username: Google username
        :param password: Google password
        :return: 1 if successfully connected with internet with social login type facebook else -1
        """
        self.utils.print_info("Click Social Login facebook button")
        self.auto_actions.click(self.get_social_wifi_all_google_icon())
        self.get_gp_page_screen_shot()
        sleep(5)

        self.utils.print_info("Enter Google Username")
        self.auto_actions.send_keys(self.get_social_wifi_all_google_username_field(), username)

        self.utils.print_info("Click next button")
        self.auto_actions.click(self.get_social_wifi_all_google_next_button())

        self.utils.print_info("Enter Google Password")
        self.auto_actions.send_keys(self.get_social_wifi_all_google_password_field(), password)

        self.utils.print_info("Click next button")
        self.auto_actions.click(self.get_social_wifi_all_google_next_button())
        sleep(5)

        if self.get_social_wifi_all_google_login_error_page():
            self.utils.print_info("Click Google error after login in button")
            self.auto_actions.click(self.get_social_wifi_all_facebook_login_error_page())
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            return -1

    def validate_eguest_user_login_with_voucher_credentials(self, credentials):
        """
        - Register network via google login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
         - ``validate eguest user login with voucher credentials   ${CREDENTIALS}``

        :param credentials: Voucher credential dictionary
        :return: 1 if successfully connected with internet with social login type facebook else -1
        """

        username = list(credentials.keys())[0]
        sleep(2)
        self.utils.print_info("Entering voucher Username")
        self.auto_actions.send_keys(self.get_user_registration_social_wifi_username_field(), username)
        sleep(2)

        self.utils.print_info("Enter voucher Passcode")
        self.auto_actions.send_keys(self.get_user_registration_social_wifi_passcode_field(), credentials.get(username))
        sleep(2)

        self.utils.print_info("Click Sign In button")
        self.auto_actions.click(self.get_user_registration_social_wifi_signin_button())
        sleep(5)

        if self.get_user_registration_social_wifi_login_error_page():
            self.utils.print_info("Click error after login in button")
            self.auto_actions.click(self.get_user_registration_social_wifi_login_error_page())
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            return -1

    def validate_eguest_default_template_with_no_mapping(self):
        """
        - Register network via google login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
         - ``validate eguest default template with no mapping``

        :return: 1 if successfully connected with internet with social login type facebook else -1
        """

        if self.get_default_template_page_company_logo().is_displayed():
            self.utils.print_info("Default template is displayed")
            sleep(3)
            self.get_gp_page_screen_shot()
            return 1
        else:
            return -1


