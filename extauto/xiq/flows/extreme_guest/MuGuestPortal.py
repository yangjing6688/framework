from xiq.elements.extreme_guest.MuGuestPortalWebElements import MuGuestPortalWebElements
from extauto.common.GmailHandler import GmailHandler
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from time import sleep
from extauto.common.CommonValidation import CommonValidation


class MuGuestPortal(MuGuestPortalWebElements):
    def __init__(self):
        super().__init__()
        self.cli = Cli()
        self.auto_actions = AutoActions()
        self.gmail = GmailHandler()
        self.common_validation = CommonValidation()

    def validate_eguest_social_login_with_facebook(self, username, password, **kwargs):
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
        self.auto_actions.click_reference(self.get_social_wifi_all_facebook_icon)
        self.get_gp_page_screen_shot()
        sleep(5)

        self.utils.print_info("Enter Facebook Username")
        self.auto_actions.send_keys(self.get_social_wifi_all_facebook_username_field(), username)

        self.utils.print_info("Enter Facebook Password")
        self.auto_actions.send_keys(self.get_social_wifi_all_facebook_password_field(), password)

        self.utils.print_info("Click Facebook Sign in button")
        self.auto_actions.click_reference(self.get_social_wifi_all_facebook_login_button)
        sleep(5)

        if self.get_social_wifi_all_facebook_login_error_page():
            self.utils.print_info("Click Facebook error after login in button")
            self.auto_actions.click_reference(self.get_social_wifi_all_facebook_login_error_page)
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        try:
            if self.get_social_wifi_all_login_success_page().is_displayed():
                return 1
            else:
                kwargs['fail_msg'] = "Could not connect with internet with social login type facebook"
                self.common_validation.failed(**kwargs)
                return -1
        except Exception:
            return -1

    def validate_eguest_social_login_with_linkedin(self, username, password, **kwargs):
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
        self.auto_actions.click_reference(self.get_social_wifi_all_linkedin_icon)
        self.get_gp_page_screen_shot()
        sleep(5)

        self.utils.print_info("Enter Linkedin Username")
        self.auto_actions.send_keys(self.get_social_wifi_all_linkedin_username_field(), username)

        self.utils.print_info("Enter Linkedin Password")
        self.auto_actions.send_keys(self.get_social_wifi_all_linkedin_password_field(), password)

        self.utils.print_info("Click Linkedin Sign in button")
        self.auto_actions.click_reference(self.get_social_wifi_all_linkedin_signin_button)
        sleep(5)

        if self.get_social_wifi_all_linkedin_allow_button():
            self.utils.print_info("Click Linkedin Allow button")
            self.auto_actions.click_reference(self.get_social_wifi_all_linkedin_allow_button)
            sleep(5)

        if self.get_social_wifi_all_linkedin_login_error_page():
            self.utils.print_info("Click Linkedin error after login in button")
            self.auto_actions.click_reference(self.get_social_wifi_all_linkedin_login_error_page)
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            kwargs['fail_msg'] = "Could not connect with internet with social login type Linkedin"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_eguest_social_login_with_google(self, username, password, **kwargs):
        """
        - Register network via google login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
        - ``Validate EGuest Social Login With Google  ${GOOGLE_USERNAME}   ${GOOGLE_PASSWORD}``

        :param username: Google username
        :param password: Google password
        :return: 1 if successfully connected with internet with social login type facebook else -1
        """
        self.utils.print_info("Click Social Login google button")
        self.auto_actions.click_reference(self.get_social_wifi_all_google_icon)
        self.get_gp_page_screen_shot()
        sleep(5)

        self.utils.print_info("Enter Google Username")
        self.auto_actions.send_keys(self.get_social_wifi_all_google_username_field(), username)

        self.utils.print_info("Click next button")
        self.auto_actions.click_reference(self.get_social_wifi_all_google_next_button)

        self.utils.print_info("Enter Google Password")
        self.auto_actions.send_keys(self.get_social_wifi_all_google_password_field(), password)

        self.utils.print_info("Click next button")
        self.auto_actions.click_reference(self.get_social_wifi_all_google_next_button)
        sleep(5)

        if self.get_social_wifi_all_google_login_error_page():
            self.utils.print_info("Click Google error after login in button")
            self.auto_actions.click_reference(self.get_social_wifi_all_facebook_login_error_page)
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            kwargs['fail_msg'] = "Could not connect with internet via Google"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_eguest_user_login_with_voucher_credentials(self, credentials, **kwargs):
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
        self.auto_actions.click_reference(self.get_user_registration_social_wifi_signin_button)
        sleep(5)

        if self.get_user_registration_social_wifi_login_error_page():
            self.utils.print_info("Click error after login in button")
            self.auto_actions.click_reference(self.get_user_registration_social_wifi_login_error_page)
            sleep(3)

        if self.get_social_wifi_max_count_error():
            self.utils.print_info("Getting max count error")
            self.get_gp_page_screen_shot()
            sleep(2)
            return -1

        if self.get_social_wifi_access_denied_error():
            kwargs['pass_msg'] = "Getting access denied error"
            self.common_validation.passed(**kwargs)
            self.get_gp_page_screen_shot()
            sleep(2)
            return -1

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_social_wifi_all_login_success_page().is_displayed():
            return 1
        else:
            kwargs['fail_msg'] = "Could not connect with internet via Google"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_eguest_default_template_with_no_mapping(self, **kwargs):
        """
        - Register network via google login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
        - ``validate eguest default template with no mapping``

        :return: 1 if successfully connected with internet with social login type facebook else -1
        """

        if self.get_default_template_page_company_logo().is_displayed():
            self.utils.print_info("Default template is displayed")
            self.get_gp_page_screen_shot()
            kwargs['pass_msg'] = "Default template is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Default template is displayed"
            self.common_validation.failed(**kwargs)
            return -1

    def register_sponsored_guest_user(self, visitor_name, visitor_email, visitor_mobile, sponsor_name, sponsor_email, access_purpose, **kwargs):
        """
        - Register network via Sponsor Action CWP
        - Register User with Captive Web Portal Sponsor Form
        - Keyword Usage:
        - ``Register Sponsor Guest User  ${VISITOR_NAME}   ${VISITOR_EMAIL} ${VISITOR_MOBILE}  ${SPONSOR_NAME}     ${SPONSOR_EMAIL}     ${ACCESS_PURPOSE}``

        :param visitor_name: Visitor Name
        :param visitor_email: Visitor Email
        :param visitor_mobile: Visitor Mobile
        :param sponsor_name: Sponsor Name
        :param sponsor_email: Sponsor Email
        :param access_purpose: Access Purpose
        :return: 1 if successfully registered else -1
        """

        self.utils.print_info("Click Guest Register button")
        self.auto_actions.click_reference(self.get_sponsor_guest_access_register_guest_btn)
        self.get_gp_page_screen_shot()
        sleep(2)

        self.utils.print_info("Enter Guest Name")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_register_guest_name(), visitor_name)

        self.utils.print_info("Enter Guest Email")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_register_guest_email(), visitor_email)

        self.utils.print_info("Enter Guest Mobile")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_register_guest_mobile(), visitor_mobile)

        self.utils.print_info("Enter Sponsor Name")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_register_guest_sponsor_name(), sponsor_name)

        self.utils.print_info("Enter Sponsor Email")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_register_guest_sponsor_email(), sponsor_email)

        self.utils.print_info("Enter Purpose")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_register_guest_purpose(), access_purpose)

        self.utils.print_info("Clicking Disclaimer Checkbox")
        self.auto_actions.click_reference(self.get_sponsor_guest_access_register_guest_disclaimer)

        self.utils.print_info("Clicking Register Button")
        self.auto_actions.click_reference(self.get_sponsor_guest_access_register_guest_register)
        sleep(2)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_register_guest_registration_status_text() == 'Successfully registered!':
            self.utils.print_info("Registration Successful!")
            self.utils.print_info("Clicking Login Button")
            self.auto_actions.click_reference(self.get_sponsor_guest_access_register_guest_sponsorlogin)
            sleep(2)
            kwargs['pass_msg'] = "Registration Successful!"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info(self.get_sponsor_guest_access_register_guest_registration_status_text())

        kwargs['fail_msg'] = "Registration was not Successful!"
        self.common_validation.failed(**kwargs)
        return -1

    def validate_sponsored_guest_access(self, email, password, onboarding_action, login_email = 'null', **kwargs):
        """
        - Validate the Sponsor Action on the Guest Access
        - Validate User with Captive Web Portal Sponsor Form Login
        - Keyword Usage:
        - ``Validate Sponsored Guest Access  ${USER_EMAL}   ${USER_PASSWORD} ${ONBOARDING_ACTION}  ${LOGIN_EMAIL}``

        :param email: email to retrieve passcode
        :param password: email password
        :param onboarding_action: onboarding action to determine sponsor or user and passcode length
        :param login_email: Sponsor Name
        :return: 1 if successfully registered else -1
        """
        emailto = 'user'
        if onboarding_action == 'Send One-Time-Passcode to Sponsor' or onboarding_action == 'Send Passcode to Sponsor':
            emailto = 'sponsor'
        passcode_length = 8
        if 'One-Time-Passcode' in onboarding_action:
            passcode_length = 4
        password = self.gmail.get_sponsor_action_login_credential(email, password, emailto, passcode_length)
        if not(login_email == 'null'):
            email = login_email
        self.utils.print_info("Username: ", email)
        self.utils.print_info("Passcode: ", password)
        sleep(2)

        self.utils.print_info("Enter Guest Username")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_username_field(), email)

        self.utils.print_info("Enter Guest Password")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_password_field(), password)

        self.utils.print_info("Clicking Signin Button")
        self.auto_actions.click_reference(self.get_sponsor_guest_access_signin_btn)
        sleep(2)

        if self.get_sponsor_guest_access_login_error_button():
            self.utils.print_info("Click Send Anyway after login in button")
            self.auto_actions.click_reference(self.get_sponsor_guest_access_login_error_button)
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_login_success_page():
            kwargs['pass_msg'] = "Validated the Sponsor Action on the Guest Access"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Registration was not Successful!"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_sponsored_guest_access_wrong_password(self, email, password, onboarding_action, wrong_password,login_email = 'null', **kwargs):
        """
        - Validate the Sponsor Action on the Guest Access using wrong password
        - Validate User with Captive Web Portal Sponsor Form Login
        - Keyword Usage:
        - ``Validate Sponsored Guest Access  ${USER_EMAL}   ${USER_PASSWORD} ${ONBOARDING_ACTION}  ${LOGIN_EMAIL}    ${WRONG_PASSWORD}``

        :param email: email to retrieve passcode
        :param password: email password
        :param onboarding_action: onboarding action to determine sponsor or user and passcode length
        :param login_email: Sponsor Name
        :return: 1 if successfully registered else -1
        """
        emailto = 'user'
        if onboarding_action == 'Send One-Time-Passcode to Sponsor' or onboarding_action == 'Send Passcode to Sponsor':
            emailto = 'sponsor'
        passcode_length = 8
        if 'One-Time-Passcode' in onboarding_action:
            passcode_length = 4
        password = self.gmail.get_sponsor_action_login_credential(email, password, emailto, passcode_length)
        if not(login_email == 'null'):
            email = login_email
        self.utils.print_info("Username: ", email)
        self.utils.print_info("Passcode: ", wrong_password)
        sleep(2)

        self.utils.print_info("Enter Guest Username")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_username_field(), email)

        self.utils.print_info("Enter Guest Password")
        self.auto_actions.send_keys(self.get_sponsor_guest_access_password_field(), wrong_password)

        self.utils.print_info("Clicking Signin Button")
        self.auto_actions.click_reference(self.get_sponsor_guest_access_signin_btn)
        sleep(2)

        if self.get_sponsor_guest_access_login_error_button():
            self.utils.print_info("Click Send Anyway after login in button")
            self.auto_actions.click_reference(self.get_sponsor_guest_access_login_error_button)
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_login_success_page():
            kwargs['pass_msg'] = "Validated the Sponsor Action on the Guest Access"
            self.common_validation.passed(**kwargs)
            return 1

        elif self.get_social_wifi_access_denied_error():
            kwargs['pass_msg'] = "Getting access denied error"
            self.common_validation.passed(**kwargs)
            self.get_gp_page_screen_shot()
            sleep(2)
            return -1
        else:
            kwargs['fail_msg'] = "Registration was not Successful!"
            self.common_validation.failed(**kwargs)
            return -1

    def check_if_sponsor_mobile_is_displayed(self, **kwargs):
        """
        - Check if the sponsor mobile field is present in Sponsor Form
        - Keyword Usage:
        - ``Check If Sponsor Mobile Is Displayed``

        :return: 1 if sponsor field is not present else -1
        """
        self.utils.print_info("Click Guest Register button")
        self.auto_actions.click_reference(self.get_sponsor_guest_access_register_guest_btn)
        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_register_guest_sponsor_mobile():
            kwargs['fail_msg'] = "Sponsor field is not present"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def check_approval_success_text(self, driver):
        """
        - Check the Approval Success Text
        - Keyword Usage:
        - ``Check Approval Success Text``

        :return: success text
        """
        success_text = driver.find_element_by_xpath('//*[@class="success_text"]')
        self.utils.print_info(success_text.text)
        return success_text.text

    def register_device_for_guest_access(self, visitor_name, visitor_email, **kwargs):
        """
        - Register Device via Device registration CWP
        - Register Device with Captive Web Portal Device Registration Form
        - Keyword Usage:
        - ``Register Device for Guest Access  ${VISITOR_NAME}   ${VISITOR_EMAIL}``

        :param visitor_name: Visitor Name
        :param visitor_email: Visitor Email
        :return: 1 if successfully registered else -1
        """

        self.utils.print_info("Click Register button")
        self.auto_actions.click_reference(self.get_registernow_btn)
        sleep(2)

        self.utils.print_info("Enter Guest Name")
        self.auto_actions.send_keys(self.get_name_field(), visitor_name)

        self.utils.print_info("Enter Guest Email")
        self.auto_actions.send_keys(self.get_email_field(), visitor_email)

        self.utils.print_info("Disabling SMS Preferred Checkbox")
        self.auto_actions.click_reference(self.get_mobilepreferred_check)

        self.utils.print_info("Clicking Disclaimer Checkbox")
        self.auto_actions.click_reference(self.get_disclaimer_check)

        self.utils.print_info("Clicking Register Button")
        self.auto_actions.click_reference(self.get_register_btn)
        sleep(2)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_registration_status() == 'Successfully registered!':
            self.utils.print_info("Registration Successful!")
            self.utils.print_info("Clicking Login Button")
            self.auto_actions.click_reference(self.get_login_btn)
            sleep(2)
            kwargs['pass_msg'] = "Registration Successful!"
            self.common_validation.passed(**kwargs)
            return 1

        elif self.get_registration_status() == 'Onboarding Policy is not available':
            self.utils.print_info("Onboarding Policy is not available")
            sleep(2)
            kwargs['pass_msg'] = "Onboarding Policy is not available"
            self.common_validation.passed(**kwargs)
            return -1

        else:
            self.utils.print_info(self.get_sponsor_guest_access_register_guest_registration_status_text())
            kwargs['fail_msg'] = "Registration was not Successful!"
            self.common_validation.failed(**kwargs)
            return -1

    def register_device_with_email_for_guest_access(self, visitor_email, **kwargs):
        """
        - Register Device with email to receive offers
        - Register Device with Captive Web Portal Email Access Form
        - Keyword Usage:
        - ``Register Device with Email for Guest Access  ${VISITOR_EMAIL}``

        :param email: Visitor Email
        :return: 1 if successfully registered else -1
        """

        self.utils.print_info("Enter Guest Email")
        self.auto_actions.send_keys(self.get_email_field(), visitor_email)

        self.utils.print_info("Clicking Go Button")
        self.auto_actions.click_reference(self.get_register_btn)
        sleep(2)

        if self.get_sponsor_guest_access_login_error_button():
            self.utils.print_info("Click Send Anyway after login in button")
            self.auto_actions.click_reference(self.get_sponsor_guest_access_login_error_button)
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_login_success_page():
            kwargs['pass_msg'] = "Successfully registered"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Registration was not Successful!"
            self.common_validation.failed(**kwargs)
            return -1