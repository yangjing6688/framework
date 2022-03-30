from extauto.xiq.elements.extreme_guest.MuSponsorWebElements import MuSponsorWebElements
from extauto.common.GmailHandler import GmailHandler
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from time import sleep


class MuGuestPortalSponsorAccess(MuSponsorWebElements):
    def __init__(self):
        super().__init__()
        self.cli = Cli()
        self.auto_actions = AutoActions()
        self.gmail = GmailHandler()

    def register_sponsored_guest_user(self, visitor_name, visitor_email, visitor_mobile, sponsor_name, sponsor_email, access_purpose):
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
        self.auto_actions.click(self.get_sponsor_guest_access_register_guest_btn())
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
        self.auto_actions.click(self.get_sponsor_guest_access_register_guest_disclaimer())

        self.utils.print_info("Clicking Register Button")
        self.auto_actions.click(self.get_sponsor_guest_access_register_guest_register())
        sleep(2)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_register_guest_registration_status_text() == 'Successfully registered!':
            self.utils.print_info("Registration Successful!")
            self.utils.print_info("Clicking Login Button")
            self.auto_actions.click(self.get_sponsor_guest_access_register_guest_sponsorlogin())
            sleep(2)
            return 1
        else:
            self.utils.print_info(self.get_sponsor_guest_access_register_guest_registration_status_text())
        return -1

    def validate_sponsored_guest_access(self, email, password, onboarding_action, login_email = 'null'):
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
        self.auto_actions.click(self.get_sponsor_guest_access_signin_btn())
        sleep(2)

        if self.get_sponsor_guest_access_login_error_button():
            self.utils.print_info("Click Send Anyway after login in button")
            self.auto_actions.click(self.get_sponsor_guest_access_login_error_button())
            sleep(3)

        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_login_success_page():
            return 1
        else:
            return -1

    def check_if_sponsor_mobile_is_displayed(self):
        """
        - Check if the sponsor mobile field is present in Sponsor Form
        - Keyword Usage:
         - ``Check If Sponsor Mobile Is Displayed``
        :return: 1 if sponsor field is not present else -1
        """
        self.utils.print_info("Click Guest Register button")
        self.auto_actions.click(self.get_sponsor_guest_access_register_guest_btn())
        self.get_gp_page_screen_shot()
        sleep(2)

        if self.get_sponsor_guest_access_register_guest_sponsor_mobile():
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