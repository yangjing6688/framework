from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.WebElementHandler import WebElementHandler
from xiq.defs.extreme_guest.MuGuestPortalWebElementsDefs import MuGuestPortalWebElementsDefs


class MuGuestPortalWebElements(MuGuestPortalWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.driver = None
        self.screen = Screen()
        self.utils = Utils()
        self.delay = 20

    @property
    def get_gp_page_title(self):
        return self.driver.title

    def get_gp_page_screen_shot(self):
        return self.screen.save_screen_shot(self.driver)

    def open_guest_portal_browser(self, mu_ip, url=None):
        """
        Open Guest portal browser on the remote mu
        :param mu_ip: Ip of the remote mu
        :param url: url to open
        :return:
        """
        if not url:
            url = 'http://www.cnn.com/'
        self.utils.print_info("Opening Guest Portal Web browser on MU")
        try:
            caps = webdriver.DesiredCapabilities.CHROME.copy()
            ops = Options()
            ops.add_argument('--disable-notifications')
            command_executor = "http://" + mu_ip + ":4444/wd/hub"
            self.utils.print_info(f"Command Executor:{command_executor}")
            self.driver = webdriver.Remote(desired_capabilities=caps, command_executor=command_executor, options=ops)
        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to load the URL.. Exiting..")
            sleep(2)

        self.utils.print_info("Loading Page with URL: ", url)
        self.driver.maximize_window()
        try:
            self.driver.get(url)
            sleep(10)
            self.utils.print_info("Refreshing Page URL")
            self.driver.refresh()
        except Exception as e:
            self.utils.print_info(e)

        got_title = self.driver.title
        self.utils.print_info("Page Title: ", got_title)
        self.get_gp_page_screen_shot()
        return got_title

    def open_gp_new_tab(self, url=None):
        """
        Open guest portal browser on the remote mu
        :param mu_ip: Ip of the remote mu
        :param url: url to open
        :return:
        """
        if not url:
            url = 'http://www.cnn.com/'
        self.utils.print_info("Loading Page with URL: ", url)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        sleep(3)
        self.driver.get(url)
        sleep(2)
        got_title = self.driver.title
        self.utils.print_info("Page Title: ", got_title)
        return got_title

    def close_gp_browser(self):
        self.utils.print_info("Close Guest Portal Browser")
        sleep(2)
        self.driver.quit()

    def get_social_wifi_all_facebook_icon(self):
        return self.weh.get_element(self.social_wifi_all_facebook_icon, self.driver)

    def get_social_wifi_all_facebook_username_field(self):
        return self.weh.get_element(self.social_wifi_all_facebook_username_field, self.driver)

    def get_social_wifi_all_facebook_password_field(self):
        return self.weh.get_element(self.social_wifi_all_facebook_password_field, self.driver)

    def get_social_wifi_all_facebook_login_button(self):
        return self.weh.get_element(self.social_wifi_all_facebook_login_button, self.driver)

    def get_social_wifi_all_facebook_login_error_page(self):
        return self.weh.get_element(self.social_wifi_all_facebook_login_error_page, self.driver)

    def get_social_wifi_all_login_success_page(self):
        return self.weh.get_element(self.social_wifi_all_login_success_page, self.driver)

    def get_social_wifi_max_count_error(self):
        return self.weh.get_element(self.social_wifi_max_count_error, self.driver)

    def get_social_wifi_all_google_icon(self):
        return self.weh.get_element(self.social_wifi_all_google_icon, self.driver)

    def get_social_wifi_all_linkedin_icon(self):
        return self.weh.get_element(self.social_wifi_all_linkedin_icon, self.driver)

    def get_social_wifi_all_linkedin_username_field(self):
        return self.weh.get_element(self.social_wifi_all_linkedin_username_field, self.driver)

    def get_social_wifi_all_linkedin_password_field(self):
        return self.weh.get_element(self.social_wifi_all_linkedin_password_field, self.driver)

    def get_social_wifi_all_linkedin_signin_button(self):
        return self.weh.get_element(self.social_wifi_all_linkedin_signin_button, self.driver)

    def get_social_wifi_all_linkedin_allow_button(self):
        return self.weh.get_element(self.social_wifi_all_linkedin_allow_button, self.driver)

    def get_social_wifi_all_linkedin_login_error_page(self):
        return self.weh.get_element(self.social_wifi_all_linkedin_login_error_page, self.driver)

    def get_social_wifi_all_google_username_field(self):
        return self.weh.get_element(self.social_wifi_all_google_username_field, self.driver)

    def get_social_wifi_all_google_password_field(self):
        return self.weh.get_element(self.social_wifi_all_google_password_field, self.driver)

    def get_social_wifi_all_google_next_button(self):
        return self.weh.get_element(self.social_wifi_all_google_next_button, self.driver)

    def get_social_wifi_all_google_login_error_page(self):
        return self.weh.get_element(self.social_wifi_all_google_login_error_page, self.driver)

    def get_user_registration_social_wifi_username_field(self):
        return self.weh.get_element(self.user_registration_social_wifi_username_field, self.driver)

    def get_user_registration_social_wifi_passcode_field(self):
        return self.weh.get_element(self.user_registration_social_wifi_passcode_field, self.driver)

    def get_user_registration_social_wifi_signin_button(self):
        return self.weh.get_element(self.user_registration_social_wifi_signin_button, self.driver)

    def get_user_registration_social_wifi_login_error_page(self):
        return self.weh.get_element(self.user_registration_social_wifi_login_error_page, self.driver)

    def get_default_template_page_company_logo(self):
        return self.weh.get_element(self.default_template_page_company_logo,self.driver)

    def get_default_template_page_acceptandconnect_button(self):
        return self.weh.get_element(self.default_template_page_acceptandconnect_button,self.driver)

    def get_sponsor_guest_access_username_field(self):
        return self.weh.get_element(self.sponsor_guest_access_username_field, self.driver)

    def get_sponsor_guest_access_password_field(self):
        return self.weh.get_element(self.sponsor_guest_access_password_field, self.driver)

    def get_sponsor_guest_access_signin_btn(self):
        return self.weh.get_element(self.sponsor_guest_access_signin_btn, self.driver)

    def get_sponsor_guest_access_clear_btn(self):
        return self.weh.get_element(self.sponsor_guest_access_clear_btn, self.driver)

    def get_sponsor_guest_access_registernow_btn(self):
        return self.weh.get_element(self.sponsor_guest_access_registernow_btn, self.driver)

    def get_sponsor_guest_access_register_employee_btn(self):
        return self.weh.get_element(self.sponsor_guest_access_register_employee_btn, self.driver)

    def get_sponsor_guest_access_register_vendor_btn(self):
        return self.weh.get_element(self.sponsor_guest_access_register_vendor_btn, self.driver)

    def get_sponsor_guest_access_register_guest_btn(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_btn, self.driver)

    def get_sponsor_guest_access_register_guest_name(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_name, self.driver)

    def get_sponsor_guest_access_register_guest_email(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_email, self.driver)

    def get_sponsor_guest_access_register_guest_mobile(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_mobile, self.driver)

    def get_sponsor_guest_access_register_guest_emailpreferred(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_emailpreferred, self.driver)

    def get_sponsor_guest_access_register_guest_mobilepreferred(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_mobilepreferred, self.driver)

    def get_sponsor_guest_access_register_guest_sponsor_name(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_sponsor_name, self.driver)

    def get_sponsor_guest_access_register_guest_sponsor_mobile(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_sponsor_mobile, self.driver)

    def get_sponsor_guest_access_register_guest_sponsor_email(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_sponsor_email, self.driver)

    def get_sponsor_guest_access_register_guest_purpose(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_purpose, self.driver)

    def get_sponsor_guest_access_register_guest_disclaimer(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_disclaimer, self.driver)

    def get_sponsor_guest_access_register_guest_register(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_register, self.driver)

    def get_sponsor_guest_access_register_guest_clear(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_clear, self.driver)

    def get_sponsor_guest_access_register_guest_sponsorlogin(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_sponsorlogin, self.driver)

    def get_sponsor_guest_access_register_guest_registration_status_text(self):
        return self.weh.get_element(self.sponsor_guest_access_register_guest_registration_status, self.driver).text

    def get_sponsor_guest_access_register_employee_registration_status_text(self):
        return self.weh.get_element(self.sponsor_guest_access_register_employee_registration_status, self.driver).text

    def get_sponsor_guest_access_register_vendor_registration_status_text(self):
        return self.weh.get_element(self.sponsor_guest_access_register_vendor_registration_status, self.driver).text

    def get_sponsor_guest_access_login_error_button(self):
        return self.weh.get_element(self.sponsor_guest_access_login_error_button, self.driver)

    def get_sponsor_guest_access_login_success_page(self):
        return self.weh.get_element(self.sponsor_guest_access_login_success_page, self.driver)

    def get_social_wifi_access_denied_error(self):
        return self.weh.get_element(self.social_wifi_access_denied_error, self.driver)

    def get_username_field(self):
        return self.weh.get_element(self.username_field, self.driver)

    def get_password_field(self):
        return self.weh.get_element(self.password_field, self.driver)

    def get_signin_btn(self):
        return self.weh.get_element(self.signin_btn, self.driver)

    def get_register_btn(self):
        return self.weh.get_element(self.register_btn, self.driver)

    def get_login_btn(self):
        return self.weh.get_element(self.login_btn, self.driver)

    def get_clear_btn(self):
        return self.weh.get_element(self.clear_btn, self.driver)

    def get_registernow_btn(self):
        return self.weh.get_element(self.registernow_btn, self.driver)

    def get_login_error_page(self):
        return self.weh.get_element(self.login_error_page, self.driver)

    def get_login_success_page(self):
        return self.weh.get_element(self.login_success_page, self.driver)

    def get_name_field(self):
        return self.weh.get_element(self.name_field, self.driver)

    def get_email_field(self):
        return self.weh.get_element(self.email_field, self.driver)

    def get_mobile_field(self):
        return self.weh.get_element(self.mobile_field, self.driver)

    def get_emailpreferred_check(self):
        return self.weh.get_element(self.emailpreferred_check, self.driver)

    def get_mobilepreferred_check(self):
        return self.weh.get_element(self.mobilepreferred_check, self.driver)

    def get_registration_status(self):
        return self.weh.get_element(self.registration_status, self.driver).text

    def get_disclaimer_check(self):
        return self.weh.get_element(self.disclaimer_check, self.driver)
