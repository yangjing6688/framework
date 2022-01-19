from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from xiq.defs.MuCPWebElemenetsDefinitions import *
from time import sleep
from extauto.common.WebElementHandler import *
from extauto.common.Screen import *


class MuCPWebElement(MuCPWebElementDefinitions):

    def __init__(self):
        self.delay = 20
        self.driver = None
        self.screen = Screen()
        self.utils = Utils()
        self.weh = WebElementHandler()
        self.locator = {"CSS_SELECTOR": By.CSS_SELECTOR,
                         "XPATH": By.XPATH,
                         "TAG_NAME": By.TAG_NAME,
                         "NAME": By.NAME,
                        "CLASS_NAME": By.CLASS_NAME,
                        }

    def open_cp_browser(self, mu_ip, url=None):
        """
        Open captive portal browser on the remote mu
        :param mu_ip: Ip of the remote mu
        :param url: url to open
        :return:
        """
        if not url:
            url = 'http://www.cnn.com/'
        self.utils.print_info("Opening CP Web browser on MU")
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
        self.get_page_screen_shot()
        return got_title

    def open_cp_new_tab(self, url=None):
        """
        Open captive portal browser on the remote mu
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

    def close_cp_browser(self):
        self.utils.print_info("Close Captive Portal Browser")
        sleep(2)
        self.driver.quit()

    @property
    def get_page_title(self):
        return self.driver.title

    def get_page_screen_shot(self):
        return self.screen.save_screen_shot(self.driver)

    def get_acceptance_button(self):
        """
        Get acceptance button element
        :return:
        """
        return self.weh.get_element(self.user_acceptance_page_accept_button, self.driver)

    def get_user_acceptance_cancel_button(self):
        return self.weh.get_element(self.user_acceptance_cancel_button, self.driver)

    def get_registration_user_first_name(self):
        return self.weh.get_element(self.self_registration_user_first_name, self.driver)

    def get_registration_user_last_name(self):
        return self.weh.get_element(self.self_registration_user_last_name, self.driver)

    def get_self_registration_user_email(self):
        return self.weh.get_element(self.self_registration_user_email_id, self.driver)

    def get_registration_user_country_code_drop_down(self):
        return self.weh.get_element(self.self_registration_user_country_code_drop_down, self.driver)

    def get_registration_user_phone_number(self):
        return self.weh.get_element(self.self_registration_user_phone_number, self.driver)

    def get_registration_user_visiting_person_email(self):
        return self.weh.get_element(self.self_registration_user_visiting_person_email, self.driver)

    def get_registration_user_registration_button(self):
        return self.weh.get_element(self.self_registration_user_registration_button, self.driver)

    def get_user_registration_status(self):
        return self.weh.get_element(self.self_user_registration_status, self.driver)

    def get_user_registration_reply_msg(self):
        return self.weh.get_element(self.user_registration_reply_msg, self.driver)

    def get_user_registration_field_err(self):
        return self.weh.get_elements(self.user_registration_field_err, self.driver)

    def get_ppsk_pascode(self):
        return self.weh.get_element(self.ppsk_passcode, self.driver)
    
    def get_social_login_accept_condition_checkbox(self):
        """
        Get user acceptance checkbox element
        :return:
        """
        return self.weh.get_element(self.social_login_accept_condition_checkbox, self.driver)

    def get_social_login_with_facebook_button(self):
        """
        Get social_login_with_facebook_button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_facebook_button, self.driver)

    def get_social_login_with_facebook_username_field(self):
        """
        Get social_login_with_facebook_username_field element
        :return:
        """
        return self.weh.get_element(self.social_login_with_facebook_username_field, self.driver)

    def get_social_login_with_facebook_password_field(self):
        """
        Get social_login_with_facebook_password_field element
        :return:
        """
        return self.weh.get_element(self.social_login_with_facebook_password_field, self.driver)

    def get_social_login_with_facebook_login_button(self):
        """
        Get social_login_with_facebook_login_button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_facebook_login_button, self.driver)

    def get_social_login_with_google_button(self):
        """
        Get social_login_with_google_button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_google_button, self.driver)

    def get_social_login_with_google_username_field(self):
        """
        Get social_login_with_google_username_field element
        :return:
        """
        return self.weh.get_element(self.social_login_with_google_username_field, self.driver)

    def get_social_login_with_google_password_field(self):
        """
        Get social_login_with_google_password_field element
        :return:
        """
        return self.weh.get_element(self.social_login_with_google_password_field, self.driver)

    def get_social_login_with_next_button(self):
        """
        Get social_login_with_google next button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_google_next_button, self.driver)

    def get_social_login_with_google_username_next_button(self):
        """
        Get social_login_with_google next button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_google_username_next_button, self.driver)

    def get_social_login_with_google_password_next_button(self):
        """
        Get social_login_with_google next button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_google_password_next_button, self.driver)


    def get_social_login_with_linkedin_button(self):
        """
        Get social_login_with_linkedin_button element
        :return:
        """
        return self.weh.get_element(self.social_login_with_linkedin_button, self.driver)

    def get_social_login_with_linkedin_username_field(self):
        """
        Get social_login_with_linkedin_username_field element
        :return:
        """
        return self.weh.get_element(self.social_login_with_linkedin_username_field, self.driver)

    def get_social_login_with_linkedin_password_field(self):
        """
        Get social_login_with_linkedin_password_field element
        :return:
        """
        return self.weh.get_element(self.social_login_with_linkedin_password_field, self.driver)

    def get_social_login_linkedin_allow_button(self):
        """
        Get social_login_with_linkedin_allow element
        :return:
        """
        return self.weh.get_element(self.social_login_allow_linkedin_button, self.driver)

    def get_social_login_linkedin_signin_button(self):
        """
        Get social login with Linkedin sign-in button
        :return:
        """
        return self.weh.get_element(self.social_login_signin_linkedin_button, self.driver)

    def get_guest_access_user_name(self):
        return self.weh.get_element(self.guest_access_user_name, self.driver)

    def get_guest_access_user_passwd(self):
        return self.weh.get_element(self.guest_access_user_passwd, self.driver)

    def get_guest_access_login_button(self):
        return self.weh.get_element(self.guest_access_login_button, self.driver)

    def get_guest_access_registration_button(self):
        return self.weh.get_element(self.guest_access_registration_button, self.driver)

    def get_registration_error_reason(self):
        return self.weh.get_element(self.registration_error_reason, self.driver)

    def get_email_id_to_get_pin(self):
        return self.weh.get_element(self.email_id_to_get_pin, self.driver)

    def get_accept_terms_cond_check_box(self):
        return self.weh.get_element(self.accept_terms_cond_check_box, self.driver)

    def get_submit_button(self):
        return self.weh.get_element(self.submit_button, self.driver)

    def get_pin_email_sent_success_text_area(self):
        return self.weh.get_element(self.pin_email_sent_success_text_area, self.driver)

    def get_pin_field(self):
        return self.weh.get_element(self.pin_field, self.driver)

    def get_pin_text_area(self):
        els = self.weh.get_elements(self.pin_not_valid_text_area, self.driver)
        if not els:
            return None
        for el in els:
            if el.is_displayed():
                return el

    def get_cloud_pin_success_text(self):
        return self.weh.get_element(self.cloud_pin_success_page, self.driver)

    def get_cwp_successful_page_text(self):
        return self.weh.get_element(self.cwp_success_page, self.driver)

    def get_social_login_terms_and_condition_link(self):
        """
        Get Social Login terms and condition link
        :return:
        """
        return self.weh.get_element(self.social_login_terms_and_condition_link, self.driver)

    def get_social_login_terms_and_condition_page_text(self):
        """
        Get Social Login terms and condition link page text
        :return:
        """
        return self.weh.get_element(self.social_login_terms_and_condition_page_text, self.driver)

    def get_social_login_terms_and_condition_close_button(self):
        """
        Get Social Login terms and condition link page close button
        """
        return self.weh.get_element(self.social_login_terms_and_condition_close_button, self.driver)

