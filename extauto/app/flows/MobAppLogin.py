from time import sleep

from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn

from extauto.app.elements.MobAppLoginWebElements import MobAppLoginWebElements
from extauto.app.elements.NewDeviceOnboardWebElements import NewDeviceOnboardWebElements
from extauto.common.AutoActions import AutoActions
from extauto.common.CloudDriver import CloudDriver
from extauto.common.Utils import Utils


class MobAppLogin:
    def __init__(self):
        pass

    def init(self, url="default"):
        """
        This method initializes the driver object and makes it global
        :param url: if not default, will be read from the ${TEST_URL} variable
        :return: returns driver object
        """
        CloudDriver().start_browser(url=url, incognito_mode=incognito_mode)
        # extauto.common.CloudDriver.load_browser(url)
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.mob_login_web_elements = MobAppLoginWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        # return self.driver

    def login_user(self, username, password, url="default"):
        if url == "default":
            self.init()
        else:
            self.init(url)
        #import sys, pdb;
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()
        browser = BuiltIn().get_variable_value("${BROWSER}")

        self.utils.print_info("Browser: ", browser)

        self.utils.print_info("user entered into login screen")
        self.utils.print_info("Logging with username ", username, " and password ", password)
        self.auto_actions.send_keys(self.mob_login_web_elements.get_login_page_username_field(), username)
        self.utils.print_info("User entered the username")
        sleep(2)
        self.auto_actions.send_keys(self.mob_login_web_elements.get_login_page_pwd_field(), password)
        self.utils.print_info("User entered the password")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_login_page_button_id)
        self.utils.print_info("User clicked on login button")
        sleep(10)

        #if "Invalid username / password You have 3 more attempts of total 5" in wrong_password_msg:
            #self.utils.print_info("you entered wrong credentials")
            #return -2

    def qa_env(self, url_name):
        self.auto_actions.send_keys(self.mob_login_web_elements.get_qa_env_login_url(), url_name)
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_qa_env_save_button)

    def entry_onboard(self):
        self.auto_actions.click_reference(self.scan_web_elements.get_onboard_symbol)
        self.utils.print_info("user clicked on onboard screen entry")
        sleep(2)
        user_action = webdriver.TouchActions(CloudDriver())
        user_action.press(x=540, y=1138).move_to(x=521, y=443).release().perform()
        self.utils.print_info("User tap the screen up")

    def entry_mycloud_nw(self):
        self.auto_actions.click_reference(self.mob_login_web_elements.get_my_cloud_network)
        self.utils.print_info("user clicked on My cloud network")
        sleep(10)

    def entry_onboard_screen(self):
        self.auto_actions.click_reference(self.scan_web_elements.get_onboard_symbol)
        self.utils.print_info("user clicked on onboard screen entry symbol")
        #user_action = webdriver.TouchActions(CloudDriver().cloud_driver)
        #user_action.press(x=540, y=1138).move_to(x=521, y=443).release().perform()
        #self.utils.print_info("User tap the screen up")

    def tap_screen(self):
        user_action = webdriver.TouchActions(CloudDriver().cloud_driver)
        user_action.press(x=540, y=1138).move_to(x=521, y=443).release().perform()
        self.utils.print_info("User tap the screen up")
        sleep(2)

    def tap_device_list(self):
        user_action = webdriver.TouchActions(CloudDriver().cloud_driver)
        user_action.press(x=531, y=1808).move_to(x=543, y=802).release().perform()
        self.utils.print_info("User tap the device list")
        sleep(10)
        #self.auto_actions.click_reference(self.mob_login_web_elements.top_button)
        #self.utils.print_info("user clicked on TOP button")

    def return_to_top(self):
        self.auto_actions.click_reference(self.mob_login_web_elements.top_button)
        self.utils.print_info("user clicked on TOP button")
        sleep(2)

    def external_admin(self, network_name):
        self.auto_actions.click_reference(self.mob_login_web_elements.get_my_cloud_network)
        self.utils.print_info("user clicked on My cloud network")
        sleep(10)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_menu_item)
        self.utils.print_info("user clicked on menu item")
        sleep(3)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_switch_button)
        self.utils.print_info("user clicked on switch option")
        sleep(10)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_external)
        self.utils.print_info("user clicked on external networks option")
        sleep(3)
        self.auto_actions.send_keys(self.mob_login_web_elements.get_external_nw_search(), network_name)
        self.utils.print_info("user searched the external deployment name")
        sleep(5)
        nw_rows = self.mob_login_web_elements.get_external_nw_row()
        for nw_row in nw_rows:
            if network_name in nw_row.text:
                self.auto_actions.click(nw_row)
                sleep(2)
                return 1

    def my_cloud_switch(self):
        self.auto_actions.click_reference(self.mob_login_web_elements.get_menu_item)
        self.utils.print_info("user clicked on menu item")
        sleep(3)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_switch_button)
        self.utils.print_info("user clicked on switch option")
        sleep(10)



    def menu_items(self):
        self.auto_actions.click_reference(self.mob_login_web_elements.get_menu_item)
        self.utils.print_info("user clicked on menu item")
        customer = self.mob_login_web_elements.get_customer_id()
        self.utils.print_info("customer info:", customer)
        company = self.mob_login_web_elements.get_company_id()
        self.utils.print_info("company info:", company)
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_settings_item)
        self.utils.print_info("user is clicked on settings")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_settings_backward_link)
        self.utils.print_info("user is clicked on settings option backward link")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_menu_item)
        self.utils.print_info("user clicked on menu item")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_about_item)
        self.utils.print_info("user clicked on about option")
        sleep(2)
        data_center_name = self.mob_login_web_elements.get_data_center_name()
        self.utils.print_info("data center name:", data_center_name)
        app_version =  self.mob_login_web_elements.get_app_version_name()
        self.utils.print_info("app version:", app_version)
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.get_about_bw_link)
        self.utils.print_info("user clicked on about backward link")
        sleep(2)
        #self.auto_actions.click_reference(self.mob_login_web_elements.get_menu_item)
        #self.utils.print_info("user clicked on menu item")
        #sleep(2)
        #self.auto_actions.click_reference(self.mob_login_web_elements.get_menu_item_logout)
        #self.utils.print_info("user clicked on logout option")
        #sleep(2)
        #self.auto_actions.click_reference(self.mob_login_web_elements.logout_yes_button)
        #self.utils.print_info("user clicked on yes button")


    def multi_factor_auth(self, otp):
        self.utils.print_info("entering OTP for multifactor authentication")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_multi_factor_auth_text_field(), otp)
        sleep(2)
        self.utils.print_info("Logging successfully")
        self.auto_actions.click_reference(self.mob_login_web_elements.get_multi_factor_submit_button)
        sleep(7)

    def recovery_mf_auth(self):
        self.auto_actions.click(self.mob_login_web_elements.get_emergency_recovery_code)
        sleep(4)

    def account_block(self, usrname, passwords, url="default"):
        if url == "default":
            self.init()
        else:
            self.init(url)
        #import sys, pdb;
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()
        browser = BuiltIn().get_variable_value("${BROWSER}")

        self.utils.print_info("Browser: ", browser)

        self.utils.print_info("App is getting started")

        self.utils.print_info("Logging with username ", usrname, " and password ", passwords)
        for username in usrname:
            for password in passwords:
                self.utils.print_info("entering username")
                self.auto_actions.send_keys(self.mob_login_web_elements.get_login_page_username_field(), username)
                sleep(4)
                self.utils.print_info("entering  password")
                self.auto_actions.send_keys(self.mob_login_web_elements.get_login_page_pwd_field(), password)
                sleep(5)
                self.utils.print_info("clicking on login button")
                self.auto_actions.click_reference(self.mob_login_web_elements.get_login_page_button_id)
                sleep(6)

        account_block_msg = self.mob_login_web_elements.get_account_blocked_message()
        self.utils.print_info("account blocked", account_block_msg)
        if "You have exceeded the maximum number of login attempts. You account will be blocked for the next 5 minutes" in account_block_msg:
            self.utils.print_info("account blocked wait for 5 min")
            return -2

    def logout_device(self):
        self.auto_actions.click_reference(self.mob_login_web_elements.logout_from_device)
        self.utils.print_info("User clicked on logout option on device list screen")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.logout_cancel_button)
        self.utils.print_info("user clicked CANCEL button to cancel logout")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.logout_from_device)
        self.utils.print_info("User clicked on logout option on device list screen")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.logout_yes_button)
        self.utils.print_info("user clicked YES button to confirm logout")
        self.utils.print_info("User logged out from the app successfully")
        sleep(3)

    def password_toggle(self, username, password, email, url="default"):
        if url == "default":
            self.init()
        else:
            self.init(url)
        # import sys, pdb;
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.auto_actions.send_keys(self.mob_login_web_elements.get_login_page_username_field(), username)
        self.utils.print_info("User entered the user name")
        sleep(4)
        self.utils.print_info("User entered the password")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_login_page_pwd_field(), password)
        self.utils.print_info("User entered the password")
        sleep(5)
        self.auto_actions.click(self.mob_login_web_elements.get_login_pwd_toggle)
        self.utils.print_info("User clicked on password toggle option")
        sleep(3)

    def trouble_logging(self, email, url="default"):
        if url == "default":
            self.init()
        else:
            self.init(url)
        #import sys, pdb;
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.auto_actions.click_reference(self.mob_login_web_elements.trouble_login_device)
        self.utils.print_info("User clicked on trouble login device option")
        sleep(3)
        trouble_login_text = self.mob_login_web_elements.trouble_login_text()
        self.utils.print_info("Text: ", trouble_login_text)
        self.auto_actions.send_keys(self.mob_login_web_elements.support_email_text_field(), email)
        self.utils.print_info("User entered the email address")
        self.auto_actions.click_reference(self.mob_login_web_elements.reset_password_button)
        self.utils.print_info("User clicked on reset password button")
        self.auto_actions.click_reference(self.mob_login_web_elements.back_to_login)
        self.utils.print_info("user clicked on back to login button")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.trouble_login_device)
        self.utils.print_info("User clicked on trouble login device option")
        sleep(2)
        self.auto_actions.click_reference(self.mob_login_web_elements.trouble_login_close_link)
        self.utils.print_info("user clicked on trouble login close link")
        self.utils.print_info("user is back to login screen")
        sleep(2)
