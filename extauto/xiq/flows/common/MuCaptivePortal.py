__author__ = "ExtremeNetworks"
__version__ = "1.0.1"

from extauto.xiq.elements.MuCPWebElements import MuCPWebElement
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from time import sleep


class MuCaptivePortal(MuCPWebElement):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    def _get_registration_status(self, **kwargs):
        """
        - Get the user registration  status
        :return: 1 if login successful else -1
        """
        self.utils.print_info("Get the Registration status....")
        self.get_page_screen_shot()
        sleep(2)
        registration_status_el = self.get_user_registration_status()
        if registration_status_el:
            if "Registration Successful" in registration_status_el.text:
                self.utils.print_info(registration_status_el.text)
                return 1
            elif "Login Successful" in registration_status_el.text:
                self.utils.print_info(registration_status_el.text)
                return 1
            else:
                self.utils.print_info(registration_status_el.text)
                return -1

    def accept_user_acceptance_page(self):
        """
        - Accept User Acceptance page to get network access
        - Keyword Usage:
        - ``Accept User Acceptance Page``

        :return: 1 If successfully Accept User page Acceptance to get network access else -1
        """
        self.get_page_screen_shot()
        sleep(2)
        accept_button = self.get_acceptance_button()
        accept_button.click()
        page_title = self.get_page_title
        self.utils.print_info(page_title)
        return self._get_registration_status()

    def cancel_user_acceptance_policy(self):
        """
        - Cancel User page Acceptance Policy for getting network access
        - Keyword Usage:
        - ``Cancel User Acceptance Policy``

        :return: 1 if cancel user acceptance Policy for getting network access else None
        """
        cancel_button = self.get_user_acceptance_cancel_button()
        cancel_button.click()
        return 1

    def user_self_registration(self, **user_info):
        """
        - User Self Registration on captive web portal
        - Keyword Usage:
        - ``User Self Registration   &{USER_INFO}``
        - &{USER_INFO}    first_name=${FIRST_NAME}   last_name=${LAST_NAME}  email=${USERS_CRED_EMAIL}
           ...             ccode=${CCODE}   ph_num=${PHONE_NUMBER}    visitor_email=${VISITOR_EMAIL}

        :param user_info: user registration parameters ie First and Last Name, Email,Mobile number,visitor Email address
        :return: 1 If registration success else -1
        """
        # User registration variables
        first_name = user_info.get('first_name')
        last_name = user_info.get('last_name')
        email = user_info.get('email')
        ccode = user_info.get('ccode')
        ph_num = user_info.get('ph_num')
        visitor_email = user_info.get('visitor_email')

        self.utils.print_info("Enter First name:{}".format(first_name))
        self.auto_actions.send_keys(self.get_registration_user_first_name(), first_name)

        self.utils.print_info("Enter last name:{}".format(last_name))
        self.auto_actions.send_keys(self.get_registration_user_last_name(), last_name)

        self.utils.print_info("Enter user email :{}".format(email))
        self.auto_actions.send_keys(self.get_self_registration_user_email(), email)

        self.utils.print_info("Select country code:{}".format(ccode))
        self.auto_actions.select_options(self.get_registration_user_country_code_drop_down(), ccode)

        self.utils.print_info("Enter phone number:{}".format(ph_num))
        self.auto_actions.send_keys(self.get_registration_user_phone_number(), ph_num)

        self.utils.print_info("Enter Visiting person email:{}".format(visitor_email))
        self.auto_actions.send_keys(self.get_registration_user_visiting_person_email(), visitor_email)

        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click on registration Button")
        self.auto_actions.click_reference(self.get_registration_user_registration_button)
        sleep(2)

        self.utils.print_info("Check the registration error reason")
        if reg_error_reason_el := self.get_registration_error_reason():
            self.utils.print_info(reg_error_reason_el.text)

        return self._get_registration_status()

    def get_ppsk_passcode_user_registration(self, **kwargs):
        """
        - When user register with open network cwp and returning to aerohive ppsk network
        - Get the pass code from user self registration page
        - Keyword Usage:
        - ``Get PPSK Passcode User Registration``

        :return: if success ppsk pass code else -1
        """
        if passcode_el := self.get_ppsk_pascode():
            self.utils.print_info(f"User PPSK Passcode for PPSK Network:{passcode_el.text} ")
            return passcode_el.text

        kwargs['fail_msg'] = "Could not get PPSK Passcode for PPSK Network"
        self.common_validation.failed(**kwargs)
        return -1

    def social_login_user_acceptance_page(self):
        """
        - Accept the user acceptance button with social login types to get access to the network
        - Keyword Usage:
        - ``Social Login User Acceptance Page``

        :return: 1 if user acceptance button clicked else None
        """
        accept_button = self.social_login_accept_condition_checkbox()
        accept_button.click()
        page_title = self.get_page_title
        self.utils.print_info(page_title)
        if "Network Access Portal" in page_title:
            return 1

    def check_social_login_page_title(self):
        """
        - Get the social login cwp page title
        - Keyword Usage:
        - ``Check Social Login Page Title``

        :return: 1 if social login page loaded else None
        """
        page_title = self.get_page_title
        self.utils.print_info(page_title)
        self.get_page_screen_shot()
        if "Network Access Portal" in page_title:
            return 1

    def check_successful_page_title(self, **kwargs):
        """
        - Once social login successful it will redirect the url given while registration.
        - Check the page title of the loaded url
        - Keyword Usage:
        - ``Check Successful Page Title``

        :return: 1 if successfully loaded else -1
        """
        page_title = self.get_page_title
        self.utils.print_info(page_title)
        self.get_page_screen_shot()
        if "CNN International - Breaking News, US News, World News and Video" in page_title:
            return 1
        else:
            kwargs['fail_msg'] = "'CNN International - Breaking News, US News," \
                                 f" World News and Video' not in - {page_title}"
            self.common_validation.failed(**kwargs)
            return -1

    # This method will not be deprecated until the keywords for the entire file have been moved and tested
    # @deprecated('Please use the {validate_cwp_social_login_with_facebook} keyword in keywords/KeywordsLogin.py.
    # This method can be removed after 7/1/2023')
    def validate_cwp_social_login_with_facebook(self, username, password, **kwargs):
        return self.util_validate_cwp_social_login_with_facebook(username, password, **kwargs)

    def util_validate_cwp_social_login_with_facebook(self, username, password, **kwargs):
        """
        - Register network via facebook login CWP
        - Validate Captive Web Portal social login with facebook credentials
        - Keyword Usage:
        - ``Validate CWP Social Login With Facebook  ${FACEBOOK_USERNAME}   ${FACEBOOK_PASSWORD}``

        :return: 1 if successfully connected with internet with social login type facebook else -1
        """
        self.utils.print_info("Click Social Login User Acceptance Checkbox")
        self.auto_actions.click_reference(self.get_social_login_accept_condition_checkbox)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click Social Login facebook button")
        self.auto_actions.click_reference(self.get_social_login_with_facebook_button)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Enter Facebook Username")
        for getFB in range(0,2):
            if getFB < 2:
                sendres = self.auto_actions.send_keys(self.get_social_login_with_facebook_username_field(), username,
                                                  allow_fail=True)
            else:
                sendres = self.auto_actions.send_keys(self.get_social_login_with_facebook_username_field(), username,
                                                      allow_fail=False)
            if sendres != 1:
                self.utils.print_info(f"Attempt {getFB} failed. Delay 10 seconds and attempt to refresh the social page")
                sleep(10)
                self.refresh_cp_browser()
            else:
                self.utils.print_info(f"Break b/c result is {sendres}")
                break

        self.utils.print_info("Enter Facebook Password")
        self.auto_actions.send_keys(self.get_social_login_with_facebook_password_field(), password)

        self.utils.print_info("Click Facebook Sign in button")
        self.auto_actions.click_reference(self.get_social_login_with_facebook_login_button)
        sleep(5)

        self.get_page_screen_shot()
        sleep(2)

        page_title = self.get_page_title
        self.utils.print_info(page_title)
        if "Network Access Portal" in page_title:
            kwargs['pass_msg'] = "Successfully connected with internet with social login type facebook"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"'Network Access Portal' not in - {page_title}"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_cwp_social_login_with_google_account(self, username, password, **kwargs):
        """
        - Register network via google login CWP
        - Validate Captive Web Portal social login with google credentials
        - Keyword Usage:
        - ``Validate CWP Social Login With Facebook  ${GMAIL_USERNAME}   ${GMAIL_PASSWORD}``

        :return: 1 if successfully connected with internet with social login type google else -1
        """
        self.utils.print_info("Click Social Login User Acceptance Checkbox")
        self.auto_actions.click_reference(self.get_social_login_accept_condition_checkbox)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click Social Login google button")
        self.auto_actions.click_reference(self.get_social_login_with_google_button)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Enter Gmail Username")
        self.auto_actions.send_keys(self.get_social_login_with_google_username_field(), username)

        self.utils.print_info("Click Next button")
        self.auto_actions.click_reference(self.get_social_login_with_google_username_next_button)
        sleep(3)

        self.utils.print_info("Enter Gmail Password")
        self.auto_actions.send_keys(self.get_social_login_with_google_password_field(), password)

        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click Next button")
        self.auto_actions.click_reference(self.get_social_login_with_google_password_next_button)
        sleep(3)

        self.get_page_screen_shot()
        sleep(2)

       ####Workaround fix###
        self.utils.print_info("Open New Tab")
        self.open_cp_new_tab()
        self.utils.print_info("Click Social Login User Acceptance Checkbox")
        self.auto_actions.click_reference(self.get_social_login_accept_condition_checkbox)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click Social Login google button")
        self.auto_actions.click_reference(self.get_social_login_with_google_button)
        self.get_page_screen_shot()
        sleep(2)
        self.utils.print_info("Validating successful Page text")
        if self.get_cwp_successful_page_text():
            msg = self.get_cwp_successful_page_text().text
            self.utils.print_info(msg)

        if "Login Successful" and "connected to the network" in msg:
            kwargs['pass_msg'] = "Successfully connected with internet with social login type google"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"'Login Successful' and 'connected to the network' not in - {msg}"
            self.common_validation.failed(**kwargs)
            return -1

    # This method will not be deprecated until the keywords for the entire file have been moved and tested
    # @deprecated('Please use the {validate_cwp_social_login_with_linkedin_account} keyword in keywords/KeywordsLogin.py
    # This method can be removed after 7/1/2023')
    def validate_cwp_social_login_with_linkedin_account(self, username, password, **kwargs):
        return self.util_validate_cwp_social_login_with_linkedin_account(username, password, **kwargs)

    def util_validate_cwp_social_login_with_linkedin_account(self, username, password, **kwargs):
        """
        - Register network via Linkedin login CWP
        - Validate Captive Web Portal social login with linkedin credentials
        - Keyword Usage:
        - ``Validate CWP Social Login With Facebook  ${LINKEDIN_USERNAME}   ${LINKEDIN_PASSWORD}``

        :return: 1 if successfully connected with internet with social login type Linkedin else -1
        """
        self.utils.print_info("Click Social Login User Acceptance Checkbox")
        self.auto_actions.click_reference(self.get_social_login_accept_condition_checkbox)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click Social Login Linkedin button")
        self.auto_actions.click_reference(self.get_social_login_with_linkedin_button)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Enter Linkedin Username")
        self.auto_actions.send_keys(self.get_social_login_with_linkedin_username_field(), username)
        sleep(2)

        self.utils.print_info("Enter Linkedin Password")
        self.auto_actions.send_keys(self.get_social_login_with_linkedin_password_field(), password)
        sleep(2)

        self.utils.print_info("Click Linkedin Sign in button")
        self.auto_actions.click_reference(self.get_social_login_linkedin_signin_button)
        sleep(5)

        self.get_page_screen_shot()
        sleep(2)

        page_title = self.get_page_title
        self.utils.print_info(page_title)
        if "Network Access Portal" in page_title:
            kwargs['pass_msg'] = "Successfully connected with internet with social login type Linkedin"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"'Network Access Portal' not in - {page_title}"
            self.common_validation.failed(**kwargs)
            return -1

    def guest_user_self_registration(self, guest_user, **kwargs):
        """
        - Register the Guest User to access the network
        - Keyword Usage:
        - ``Guest USer Self Registration   &{GUEST_USER}``
        - &{GUEST_USER}   user_name=${USER_NAME}   email=${EMAIL}  ccode=${CCODE}  ph_num=${PHONE_NUMB}
           ...             visitor_email=${VISITOR_EMAIL}

        :param guest_user: guest user registration dictionary
        :return: 1 if registration success else -1
        """
        user_name = guest_user.get('user_name')
        email = guest_user.get('email')
        ccode = guest_user.get('ccode')
        ph_num = guest_user.get('ph_num')
        visitor_email = guest_user.get('visitor_email')

        self.utils.print_info("Enter user name:{}".format(user_name))
        self.auto_actions.send_keys(self.get_registration_user_first_name(), user_name)

        self.utils.print_info("Enter email :{}".format(email))
        self.auto_actions.send_keys(self.get_self_registration_user_email(), email)

        self.utils.print_info("Select country code:{}".format(ccode))
        self.auto_actions.select_options(self.get_registration_user_country_code_drop_down(), ccode)

        self.utils.print_info("Enter phone number:{}".format(ph_num))
        self.auto_actions.send_keys(self.get_registration_user_phone_number(), ph_num)

        self.utils.print_info("Enter Visiting person email:{}".format(visitor_email))
        self.auto_actions.send_keys(self.get_registration_user_visiting_person_email(), visitor_email)

        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click on registration Button")
        self.auto_actions.click_reference(self.get_guest_access_registration_button)
        sleep(2)

        self.utils.print_info("Check the registration error reason")
        if reg_error_reason_el := self.get_registration_error_reason():
            self.utils.print_info(reg_error_reason_el.text)

        self.utils.print_info("Validating the filed errors")
        if self.get_user_registration_reply_msg():
            reply_msg_text = self.get_user_registration_reply_msg().text
            if "The user name you filled exceeds required length" in reply_msg_text:
                self.utils.print_info(f'{reply_msg_text}')
                kwargs['fail_msg'] = f"'We are unable to' appears in - {reply_msg_text}"
                self.common_validation.fault(**kwargs)
                return -1, reply_msg_text
            if "We are unable to" in reply_msg_text:
                self.utils.print_info(f'{reply_msg_text}')
                kwargs['fail_msg'] = f"'We are unable to' appears in - {reply_msg_text}"
                self.common_validation.fault(**kwargs)
                return -1, reply_msg_text

        field_err_els = self.get_user_registration_field_err()
        for el in field_err_els:
            if el.is_displayed():
                self.utils.print_info(el.text)
                kwargs['fail_msg'] = f"{el.text}"
                self.common_validation.failed(**kwargs)
                return -1, el.text

        return self._get_registration_status(), reg_error_reason_el

    def login_guest_user(self, user_name, password):
        """
        - Login the the guest Access network using username and password
        - Keyword Usage:
        - ``Login Guest User  ${USER_NAME}   ${PASSWORD}``

        :param user_name: username to login to network
        :param password: password to login the network
        :return: 1 if Login success else -1
        """
        self.utils.print_info("Enter the Guest user name:{}".format(user_name))
        self.auto_actions.send_keys(self.get_guest_access_user_name(), user_name)

        self.utils.print_info("Enter the Guest User password:{}".format(password))
        self.auto_actions.send_keys(self.get_guest_access_user_passwd(), password)

        self.get_page_screen_shot()
        self.utils.print_info("Click on guest user login ")
        self.auto_actions.click_reference(self.get_guest_access_login_button)
        sleep(2)
        return self._get_registration_status()

    def config_cloud_pin_email_id(self, email):
        """
        - Enter the email id to get the cloud pin
        - cloud pin will get the the entered email ID
        - Keyword Usage:
        - ``Config Cloud Pin Email Id   ${EMAIL}``

        :param email: Email address
        :return: - 1 if "Success! Check your email for your new PIN" - else error message
        """
        msg = ''
        self.utils.print_info("enter your email to get a PIN:{}".format(email))
        self.auto_actions.send_keys(self.get_email_id_to_get_pin(), email)

        self.utils.print_info("accepts the term and conditions")
        self.auto_actions.click_reference(self.get_accept_terms_cond_check_box)

        self.get_page_screen_shot()
        self.utils.print_info("Click on Submit button")
        self.auto_actions.click_reference(self.get_submit_button)
        sleep(2)

        self.get_page_screen_shot()
        sleep(3)

        if self.get_pin_email_sent_success_text_area():
            msg = self.get_pin_email_sent_success_text_area().text

        if "Success! Check your email for your new PIN" in msg:
            return 1

    def enter_cloud_pin(self, pin, **kwargs):
        """
        - Enter the cloud pin to authenticate user
        - Keyword Usage:
        - ``Enter Cloud Pin  ${CLOUD_PIN}``

        :param pin: clodu pin got from email
        :return: 1 if Entered Cloud Pin Successfully else None
        """
        msg = ''
        self.utils.print_info("Enter the cloud pin:{}".format(pin))
        self.auto_actions.send_keys(self.get_pin_field(), pin)

        if not self.get_accept_terms_cond_check_box().is_selected():
            self.auto_actions.click_reference(self.get_accept_terms_cond_check_box)

        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click on Submit button")
        self.auto_actions.click_reference(self.get_submit_button)
        sleep(5)

        self.get_page_screen_shot()
        sleep(2)

        if self.get_pin_text_area():
            msg = self.get_pin_text_area().text
            self.utils.print_info(msg)
        if "PIN is not valid. Please request a new one" in msg:
            kwargs['fail_msg'] = f"'PIN is not valid. Please request a new one' is in message: {msg}"
            self.common_validation.failed(**kwargs)
            return -1

        if self.get_cloud_pin_success_text():
            msg = self.get_cloud_pin_success_text().text
            self.utils.print_info(msg)

        if "Login Successful" in msg:
            kwargs['pass_msg'] = "Login Successful"
            self.common_validation.passed(**kwargs)
            return 1

    def check_internet_connectivity(self, mu_ip, url="https://www.extremenetworks.com/"):
        """
        - By loading url check the internet connectivity
        - By default url is https://www.extremenetworks.com/
        - Keyword Usage:
        - ``Check Internet Connectivity   ${MU_IP}``
        - ``Check Internet Connectivity   ${MU_IP}   url=${URL}``

        :param mu_ip: mu ip to load the url
        :param url: url to load on the browser
        :return: url page title
        """
        page_title = self.open_cp_browser(mu_ip, url)
        self.close_cp_browser()
        return page_title

    def check_cwp_social_login_term_and_condition_page_text(self, **kwargs):
        """
        - Check Captive Web Portal social login term and condition page
        - Keyword Usage:
        - ``check cwp social login term and condition page``

        :return: 1 if successfully get the term and condition page text else -1
        """
        self.utils.print_info("Click Social Login User Acceptance Checkbox")
        self.auto_actions.click_reference(self.get_social_login_accept_condition_checkbox)
        self.get_page_screen_shot()
        sleep(2)

        self.utils.print_info("Click Term and Condition Link")
        self.auto_actions.click_reference(self.get_social_login_terms_and_condition_link)
        self.get_page_screen_shot()
        sleep(2)

        if self.get_social_login_terms_and_condition_page_text():
            self.utils.print_info("Click Term and Condition Link")
            msg = self.get_social_login_terms_and_condition_page_text().text
            self.utils.print_info(msg)
            self.utils.print_info("Click close Button")
            self.auto_actions.click_reference(self.get_social_login_terms_and_condition_close_button)

            if "Acceptable Use Policy" and "Terms of use" in msg:
                kwargs['pass_msg'] = f"Successfully get the term and condition page text - {msg}"
                self.common_validation.passed(**kwargs)
                return 1
        else:
            kwargs['fail_msg'] = "Could not get the term and condition page text"
            self.common_validation.failed(**kwargs)
            return -1
