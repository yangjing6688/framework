from xiq.elements.extreme_guest.MuSocialWebElements import MuSocialWebElements
from common.AutoActions import AutoActions
from common.Cli import Cli
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

        if self.get_social_wifi_all_facebook_login_error_page().is_displayed():
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

        if self.get_social_wifi_all_linkedin_login_error_page().is_displayed():
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
         - ``Validate EGuest Social Login With Facebook  ${FACEBOOK_USERNAME}   ${FACEBOOK_PASSWORD}``

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

        if self.get_social_wifi_all_google_login_error_page().is_displayed():
            self.utils.print_info("Click Google error after login in button")
            self.auto_actions.click(self.get_social_wifi_all_facebook_login_error_page())
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            return -1
