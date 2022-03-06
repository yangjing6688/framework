from typing_extensions import Self
from extauto.xiq.defs.extreme_guest.MuSponsorWebElementsDefs import MuSponsorWebElementsDefs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from extauto.common.WebElementHandler import *
from extauto.common.Screen import *
from time import sleep


class MuSponsorWebElements(MuSponsorWebElementsDefs):
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