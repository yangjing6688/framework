import threading
import pycurl
import re
from io import StringIO
from time import sleep
from robot.libraries.BuiltIn import BuiltIn

from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation

import extauto.xiq.flows.common.ToolTipCapture

from extauto.xiq.elements.LoginWebElements import LoginWebElements
from extauto.xiq.elements.PasswordResetWebElements import PasswordResetWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements

class Login:

    def __init__(self):
        self.common_validation = CommonValidation()
        self.record = False
        self.t1 = None
        self.utils = Utils()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.login_web_elements = LoginWebElements()
        self.pw_web_elements = PasswordResetWebElements()
        self.nav_web_elements = NavigatorWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        pass

    def _init(self, url="default", incognito_mode="False"):
        """
        This method initializes the driver object and makes it global
        :param url: if not default, will be read from the ${TEST_URL} variable
        :return: returns driver object
        """
        if CloudDriver().cloud_driver == None:
            self.utils.print_info("Creating new cloud driver")
            CloudDriver().start_browser(url=url, incognito_mode=incognito_mode)
        else:
            self.utils.print_info("Cloud driver already exists - opening new window using same driver")
            self.window_index = CloudDriver().open_window(url)

    def set_active_browser(self):
        global mydriver
        mydriver = self.driver
        return mydriver

    def get_page_title(self):
        """
        - Get the title of the page
        - Keyword Usage:
         - ``Get Page Title``

        :return: page title
        """
        return CloudDriver().cloud_driver.title

    def get_window_index(self):
        """
        - Get the index of the window handle for this session
        - Keyword Usage:
         - ``Get Window Index``

        :return: index of window handle
        """
        return self.window_index

    def enable_exos_status_on_xiq(self, url):
        """
        - for Exos switch to appear in UI we need to load the provided url
        - Keyword Usage:
         - ``Enable Exos Status On Xiq   ${URL}``

        :param url: url to load for enabling exos on cloud UI
        :return: 1 if loaded the url successfully
        """
        self.utils.print_info("Refresh Page")
        CloudDriver().cloud_driver.get(url)
        CloudDriver().cloud_driver.refresh()
        sleep(5)
        return 1

    def login_user(self, username, password, capture_version=False, login_option="30-day-trial", url="default",
                   incognito_mode="False", co_pilot_status=False, entitlement_key=False, salesforce_username=False,
                   salesforce_password=False, saleforce_shared_cuid=False, quick=False, **kwargs):
        """
        - Login to Xiq account with username and password
        - By default url will load from the topology file
        - keyword Usage:
         - ``Login User   ${USERNAME}   ${PASSWORD}``
         - ``Login User   ${USERNAME}   ${PASSWORD}    capture_version=True``
         - ``Login User   ${USERNAME}   ${PASSWORD}    co_pilot_status=True``

        :param username: login account username
        :param password: login account password
        :param capture_version: true if want capture the xiq build version
        :param login_option: login option to get started with any of options: 30-day-trial, License, Legacy Entitlement, Pilot License & Connect
        :param incognito_mode: Enable/Disable incognito_mode
        :param co_pilot_status: Enable Co-Pilot Status in XIQ Login Page
        :param url: url to load
        :param entitlement_key: Entitlement Key
        :param salesforce_username: Salesforce Username
        :param salesforce_password: Salesforce Password
        :return: 1 if login successful else -1
        """
        if url == "default":
            self._init(incognito_mode=incognito_mode)
        else:
            self._init(url=url, incognito_mode=incognito_mode)

        # start the thread to capture the tool tip text
        self.t1 = threading.Thread(target=extauto.xiq.flows.common.ToolTipCapture.tool_tip_capture, daemon=True)
        self.t1.start()

        browser = BuiltIn().get_variable_value("${BROWSER}")

        self.utils.print_info("Browser: ", browser)

        try:
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['version'])
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['browserVersion'])

        self.utils.print_info("Logging with Username : ", username, " -- Password : ", password)

        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_username_text(), username)

        self.utils.print_info("Entering Password...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_password_text(), password)

        self.utils.print_info("Clicking on Sign In button")

        self.auto_actions.click(self.login_web_elements.get_login_page_login_button())
        if quick:
            sleep(2)
        else:
            sleep(10)

        self.utils.print_info("Check for wrong credentials..")
        credential_warnings = self.login_web_elements.get_credentials_error_message()
        self.utils.print_info("Wrong Credential Message: ", credential_warnings)
        if "Looks like the email or password does not match our records. Please try again." in credential_warnings:
            # self.utils.print_info("Wrong Credentials. Try Again")
            kwargs['fail_msg'] = "Wrong Credentials. Try Again"
            self.common_validation.validate(-1,1, **kwargs)
            return -1

        if self.select_login_option(login_option, entitlement_key=entitlement_key, salesforce_username=salesforce_username,
                                    salesforce_password=salesforce_password, saleforce_shared_cuid=saleforce_shared_cuid) == -1:
            kwargs['fail_msg'] = "Wrong Credentials. Try Again"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1

        self.utils.print_info("Check for Warning Messages..")
        if self.login_web_elements.get_dialog_message():
            self.utils.print_info("Clicking Close button")
            self.auto_actions.click(self.login_web_elements.get_dialog_box_close_button())

        self.utils.print_info("Check for WIPS Warning Messages..")
        wips_warnings = self.login_web_elements.get_wips_dialog_message()
        self.utils.print_info("Check for WIPS Warning Message is : ", wips_warnings)
        if self.login_web_elements.get_wips_dialog_message():
            if "Please update existing WIPS policies" in wips_warnings:
                self.utils.print_info("Clicking Dont show again Checkbox")
                self.auto_actions.click(self.login_web_elements.get_wips_popup_dialog_dont_show_again_checkbox())
                sleep(2)

                self.utils.print_info("Clicking Close button")
                self.auto_actions.click(self.login_web_elements.get_wips_popup_dialog_close_button())
                sleep(2)

        self.utils.print_info("Check for Advance Onboard Popup page after login..")
        if quick:
            sleep(2)
        else:
            sleep(10)

        try:
            if self.login_web_elements.get_drawer_content().is_displayed():
                self.auto_actions.click(self.login_web_elements.get_drawer_trigger())
        except Exception as e:
            pass

        if co_pilot_status:
            url = BuiltIn().get_variable_value("${TEST_URL}")
            copilot_url = f"{url}/hm-webapp/?copilotBeta=true"
            self.utils.print_info(f"URL To Enable Co-Pilot Beta is : {copilot_url}")
            self._enable_copilot_status_on_xiq(copilot_url)
            self.utils.print_info("Added sleep for soft launch of copilot url")
            sleep(15)

        if capture_version:
            self._capture_xiq_version()
        kwargs['pass_msg'] = "User has been logged in"
        self.common_validation.validate(1, 1, **kwargs)
        return 1

    def logout_user(self):
        """
        - Logout the current user
        - Keyword Usage:
         - ``Logout User``

        :return: 1 if logout success
        """
        # stop tool tip text capture thread
        try:
            self.t1.do_run = False
        except:
            print("t1.do_run not available to set")
        sleep(10)
        try:
            self.utils.print_info("Clicking on Logout Menu")
            self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
            sleep(2)

            self.auto_actions.click(self.login_web_elements.get_logout_link())
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            return -1
        return 1

    def quit_browser(self, _driver=None):
        """
        - Closes all the browser windows and ends the WebDriver session gracefully.
        - if the driver object is passed, quits and returns
        - Keyword Usage:
         - ``Quit Browser``

        :param _driver
        :return: 1 if success
        """
        # temp fix until singleton driver in place
        global mydriver
        if mydriver:
            mydriver.quit()
            self.utils.print_info("SINGLETON ISSUE Resetting cloud driver to -1")
            extauto.common.CloudDriver.cloud_driver = -1
            return 1

        if _driver:
            _driver.quit()
            return 1

        # stop tool tip text capture thread
        try:
            if self.t1.is_alive():
                self.t1.do_run = False
                sleep(10)

            # CloudDriver().cloud_driver.quit()
            CloudDriver().close_browser()
            self.utils.print_info("Resetting cloud driver to -1")
            # extauto.common.CloudDriver.cloud_driver = -1
            return 1
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            return -1

    def start_video_record(self, record_sta_ip, test_name=None):
        """
        - This Keyword will Start Video Record on mentioned machine IP Address .

        :param record_sta_ip: Station IP address to Start the Video Recordings
        :param test_name: Test Name for Video Recordings
        :return: None
        """
        self.utils.print_info("WINDOWS 10 STA IP: {}".format(record_sta_ip))
        self.utils.print_info("test case name: {}".format(test_name))
        if BuiltIn().get_variable_value("${RECORD}"):
            start_record_url = "http://" + str(record_sta_ip) + ":5000/video_recording/start" + str(
                test_name.replace(" ", ""))
            self.utils.print_info("START RECORD URL:{}".format(start_record_url))
            self._post_url(start_record_url)
            self.record = True

    def stop_video_record(self, record_sta_ip):
        """
        - This Keyword will Stop Video Record on mentioned machine IP Address .

        :param record_sta_ip: Station IP address to Stop the Video Recordings
        :return: None
        """
        if self.record:
            stop_record_url = "http://" + str(record_sta_ip) + ":5000/video_recording/stop"
            self.utils.print_info("STOP RECORD URL:{}".format(stop_record_url))
            self._post_url(stop_record_url)

    def _post_url(self, url):
        self.utils.print_info("URL: ", url)
        buf = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.VERBOSE, True)
        c.perform()

        try:
            json_response = buf.getvalue()
        except ValueError:
            json_response = "No Output"

        response_code = c.getinfo(pycurl.RESPONSE_CODE)
        total_time = c.getinfo(pycurl.TOTAL_TIME)

        c.close()

        self.utils.print_info("HTTP Status Code: ", response_code)
        self.utils.print_info("Response : ", json_response)
        self.utils.print_info("Time: ", total_time)

        return response_code, json_response, total_time

    def load_web_page(self, url="default"):
        """
        - Loads web page with the passed URL
        - Keyword Usage:
         - ``Load Web Page    ${URL}``

        :param url: Proper URL
        :return: creates global driver object & returns
        """
        if url == "default":
            return self._init()
        else:
            return self._init(url)

    def set_password(self, new_pwd):
        """
        - Assumes that set password url is already opened
        - Set new password for the account
        - Keyword Usage:
         - ``Set Password   ${NEW_PASSWORD}``

        :param new_pwd: New Password string to set
        :return: 1 if Able to Set the Password Successfully for the Account else None
        """
        sleep(10)
        self.utils.print_info("Entering the password: ", new_pwd)
        pwd = self.pw_web_elements.get_password_textbox()
        if pwd is None:
            self.utils.print_info("Unable to find Password textbox")
        else:
            self.auto_actions.send_keys(pwd, new_pwd)

        confirm_pwd = self.pw_web_elements.get_conf_password_texbox()
        if confirm_pwd is None:
            self.utils.print_info("Unable to find Confirm Password textbox")
        else:
            self.auto_actions.send_keys(confirm_pwd, new_pwd)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Saving the password button")
        self.auto_actions.click(self.pw_web_elements.get_set_password_button())
        sleep(30)

        self.screen.save_screen_shot()
        sleep(2)
        return 1

    def reset_password(self, new_pwd):
        """
        - Assumes that reset password url browser is opened
        - Reset the user account password
        - Keyword Usage:
         - `` Reset Password  ${NEW_PASSWORD}``

        :param new_pwd:
        :return: 1 if able to Reset the Password Successfully
        """

        sleep(10)

        self.utils.print_info("Entering the password: ", new_pwd)
        self.auto_actions.send_keys(self.pw_web_elements.get_password_textbox(), new_pwd)
        sleep(2)

        self.utils.print_info("Entering the confirm password: ", new_pwd)
        self.auto_actions.send_keys(self.pw_web_elements.get_conf_password_texbox(), new_pwd)
        sleep(2)

        self.utils.print_info("Clicking Saving the password button")
        self.auto_actions.click(self.pw_web_elements.get_reset_password_button())
        sleep(2)

        return 1

    def forgot_password(self, _email, url='default'):
        """
        - Get the link to set the forget password
        - Keyword Usage:
         - ``Forget Password   ${EMAIL}``

        :param _email: Email Address
        :param url: Forget Password URL
        :return: 1 if reset password message displayed on Page else -1
        """
        if url == "default":
            self._init()
        else:
            self._init(url)

        self.utils.print_info("Clicking Forgot Password link...")
        self.auto_actions.click(self.pw_web_elements.get_forgot_password_reset_it_here_link())
        sleep(5)

        self.utils.print_info("Entering Tenant email id")
        self.auto_actions.send_keys(self.pw_web_elements.get_forgot_password_email_textfield(), _email)
        sleep(5)

        self.utils.print_info("Clicking reset password button")
        self.auto_actions.click(self.pw_web_elements.get_forgot_password_reset_password_button())
        sleep(5)

        self.utils.print_info("Confirm message: ", self.pw_web_elements.get_forgot_password_result_label())

        reset_message = self.pw_web_elements.get_forgot_password_result_label()
        if reset_message:
            if "sent you an email" in reset_message:
                if "with instructions for resetting your password" in reset_message:
                    return 1

        self.utils.print_info("Unable to find the reset message")
        return -1

    def _capture_xiq_version(self):
        """
        - Get XIQ Build version details

        :return: xiq_version
        """
        self.utils.print_info("Clicking on About ExtremecloudIQ link")
        self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
        sleep(2)
        self.auto_actions.click(self.login_web_elements.get_about_extreme_cloudiq_link())
        sleep(2)

        xiq_version = self.login_web_elements.get_build_version_details()
        self.utils.print_info("XIQ build Version Is: ", xiq_version)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Close About ExtremecloudIQ Link Dialogue Page")
        self.auto_actions.click(self.login_web_elements.get_cancel_about_extremecloudiq_dialogue())

        return xiq_version

    def reset_password_for_new_customer(self, password, url="default",):
        """
        - Reset password for xiq account with passed reset password url link
        - Keyword Usage:
         - ``Reset Password For New Account  ${RESET_PASSWORD}   ${RESET_URL_LINK}``

        :param password:  password to reset
        :param url: reset password url link
        :return: 1
        """
        if url == "default":
            self._init()
        else:
            self._init(url)

        got_title = CloudDriver().cloud_driver.title
        self.utils.print_info("Page Title on Reset password Page: ", got_title)
        self.utils.print_info(" entering the password")
        sleep(5)
        self.auto_actions.send_keys(self.pw_web_elements.get_password_textbox(), password)
        sleep(5)
        self.utils.print_info(" entering the confirm password")
        self.auto_actions.send_keys(self.pw_web_elements.get_conf_password_texbox(), password)
        sleep(5)
        self.utils.print_info(" saving the password")
        self.auto_actions.click(self.pw_web_elements.get_save_button())

        got_title = CloudDriver().cloud_driver.title
        self.utils.print_info("Page Title on Reset password Page: ", got_title)
        return 1

    def get_viq_id(self):
        """
        - This method is used to get the build id or owner id
        - Keyword Usage:
         - ``Get Viq Owner Id``

        :return: viq id
        """
        self.utils.print_info("Clicking on About Extreme cloudIQ link")
        self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
        sleep(2)
        self.auto_actions.click(self.login_web_elements.get_about_extreme_cloudiq_link())

        sleep(5)
        viq_id = self.login_web_elements.get_viq_id_field().text
        self.utils.print_info(f"VIQ ID Is: {viq_id}")

        sleep(2)
        self.utils.print_info("Close About Extreme cloudIQ Link Dialogue Page")
        self.auto_actions.click(self.login_web_elements.get_cancel_about_extremecloudiq_dialogue())

        return viq_id

    def get_base_url_of_current_page(self):
        """
        - This Keyword is used to get the url of current loaded page
        - Keyword Usage:
         - ``Get Base URL Of Current Page``
        :return: current page url
        """
        base_url = re.search(r'^(http:\/\/|https:\/\/)?([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]*', CloudDriver().cloud_driver.current_url)
        return base_url.group()

    def get_current_page_url(self):
        """
        - This Keyword returns URL of current page
        - Keyword Usage:
         - ``Get Current Page URL``
        :return: current page url
        """
        return CloudDriver().cloud_driver.current_url

    def skip_if_account_90_days(self):
        """
            - This keyword detects a license of 90 days and clicks on the option of 90 days
            - Keyword Usage:
             - ``skip_if_account_90_days``

            :return: None
        """
        self.utils.print_info(" Select the option of 90 days trial if exists")
        status = self.login_web_elements.get_30_days_trial_txt()
        try:
            if status != None:
                self.auto_actions.click(self.login_web_elements.get_option_30_days_trial())
                self.auto_actions.click(self.login_web_elements.get_get_started_button())
                self.auto_actions.click(self.login_web_elements.get_drawer_trigger())
        except:
            return -1, "Could not select the option of 90 days trial "
        return str(1), None

    def get_xiq_version(self):
        """
         - Get XIQ Build version details

        :return: xiq_version
        """
        return self._capture_xiq_version()

    def switch_to_window(self, win_index):
        """
        - Switches to the specified window

        :param:  win_index - Index of the window to switch to
        :return: None
        """
        CloudDriver().switch_to_window(win_index)

    def close_window(self, win_index):
        """
        - Closes the specified window

        :param:  win_index - Index of the window to close
        :return: None
        """
        CloudDriver().close_window(win_index)

    def xiq_quit_browser(self, _driver=None):
        """
        - Closes all the browser windows and ends the WebDriver session gracefully.
        - if the driver object is passed, quits and returns
        - Keyword Usage:
         - ``XIQ Quit Browser``

        :param _driver: specific driver to use; if not specified, default driver will be used
        :return: None
        """
        if _driver:
            _driver.quit()
            return 1

        try:
            self.utils.print_info("Closing Browser")
            # CloudDriver().cloud_driver.quit()
            CloudDriver().close_browser()
            self.utils.print_info("Resetting cloud driver to -1")
            # extauto.common.CloudDriver.cloud_driver = -1
            # CloudDriver().cloud_driver = None
            return 1

        except Exception as e:
            self.utils.print_info("Error: ", e)
            self.utils.print_debug("Error: ", e)
            return -1

    def xiq_get_child_window_list(self, win_index):
        """
        - Obtain the Child Window Index List
        - Keyword Usage:
          - ``XIQ Get Child Window List``
        :param:  win_index - Index of the window to close
        :return: Return List containing the Child Window Indexes
        """
        window_index_list = CloudDriver().get_child_window_list(win_index)
        return window_index_list

    def logo_check_on_login_screen(self):
        """
        - Get the login logo and save it as screenshot

        :return: login logo
        """
        sleep(5)
        _val = self.login_web_elements.get_login_logo()
        sleep(5)
        return self.screen.save_element_screen_shot(_val)

    def _enable_copilot_status_on_xiq(self, url):
        """
        - This keyword is to enable Co-Pilot Beta status on XIQ UI

        :param url: url to load for enabling Co-Pilot Beta status on XIQ UI
        :return: 1 if loaded the url successfully
        """
        self.utils.print_info(f"Loading url {url} to enable Co-Pilot Beta on XIQ UI")
        CloudDriver().cloud_driver.get(url)
        self.utils.print_info("Refreshing Page")
        CloudDriver().cloud_driver.refresh()
        sleep(5)
        return 1

    def welcome_page_login(self, username, password, login_option, ekey=None, sfdc_user_type=None, sfdc_email=None, sfdc_pwd=None, shared_cuid=None, capture_version=False, code="default", url="default", incognito_mode="False"):
        """
        - Login Xiq account with username and password
        - By default url will load from the topology file
        - keyword Usage:
         - ``Login User   ${USERNAME}   ${PASSWORD}``
         - ``Login User   ${USERNAME}   ${PASSWORD}    capture_version=True``
         - $login_type} : trial, connect, extremecloudiq license, legacy license

        :param username: login account username
        :param password: login account password
        :param login_type: trial, connect, extremecloudiq license, legacy license
        :param capture_version: true if want capture the xiq build version
        :param code:
        :param url: url to load
        :return: 1 if login successful else -1
        """
        if url == "default":
            self._init(incognito_mode=incognito_mode)
        else:
            self._init(url, incognito_mode)

        # start the thread to capture the tool tip text
        self.t1 = threading.Thread(target=extauto.xiq.flows.common.ToolTipCapture.tool_tip_capture, daemon=True)
        self.t1.start()

        browser = BuiltIn().get_variable_value("${BROWSER}")

        self.utils.print_info("Browser: ", browser)

        try:
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['version'])
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['browserVersion'])

        self.utils.print_info("Logging with Username : ", username, " -- Password : ", password)

        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_username_text(), username)

        self.utils.print_info("Entering Password...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_password_text(), password)

        self.utils.print_info("Clicking on Sign In button")

        self.auto_actions.click(self.login_web_elements.get_login_page_login_button())
        sleep(10)

        self.utils.print_info("Check for wrong credentials..")
        credential_warnings = self.login_web_elements.get_credentials_error_message()
        self.utils.print_info("Wrong Credential Message: ", credential_warnings)
        if "Looks like the email or password does not match our records. Please try again." in credential_warnings:
            self.utils.print_info("Wrong Credentials. Try Again")
            return -1

        self.utils.print_info("Check for welcome page options..")
        if self.login_web_elements.get_welcome_page_option().is_displayed():
            self.utils.print_info("Select login option on welcome page...")
            self.select_welcome_page_option(login_option, ekey, sfdc_user_type, sfdc_email, sfdc_pwd, shared_cuid)
        else:
            self.utils.print_info("Welcome Page with login options is not displayed..")

        self.utils.print_info("Check for Warning Messages..")
        if self.login_web_elements.get_dialog_message():
            self.utils.print_info("Clicking Close button")
            self.auto_actions.click(self.login_web_elements.get_dialog_box_close_button())

        self.utils.print_info("Check for WIPS Warning Messages..")
        wips_warnings = self.login_web_elements.get_wips_dialog_message()
        self.utils.print_info("Check for WIPS Warning Message is : ", wips_warnings)
        if self.login_web_elements.get_wips_dialog_message():
            if "Please update existing WIPS policies" in wips_warnings:
                self.utils.print_info("Clicking Dont show again Checkbox")
                self.auto_actions.click(self.login_web_elements.get_wips_popup_dialog_dont_show_again_checkbox())
                sleep(2)

                self.utils.print_info("Clicking Close button")
                self.auto_actions.click(self.login_web_elements.get_wips_popup_dialog_close_button())
                sleep(2)

        self.utils.print_info("Check for Advance Onboard Popup page after login..")
        sleep(10)
        try:
            if self.login_web_elements.get_drawer_content().is_displayed():
                self.auto_actions.click(self.login_web_elements.get_drawer_trigger())
        except Exception as e:
            pass

        if capture_version:
            self._capture_xiq_version()
        return 1

    def select_welcome_page_option(self, login_option, ekey, sfdc_user_type, sfdc_email, sfdc_pwd, shared_cuid):
            """
                - This keyword selects login option on welcome page as indicated by login_option
            :return: None
            """
            if login_option is not None:
                self.utils.print_info("Login type is: ", login_option)
                sleep(5)
                try:
                    ekpopup = self.login_web_elements.get_legacy_ek_popup_hdr()
                    if ekpopup.is_displayed():
                        self.utils.print_info("Dismiss legacy ek popup...")
                        self.auto_actions.click(self.login_web_elements.get_legacy_ek_popup_no_btn())
                except Exception as e:
                    pass
                if login_option.lower() == 'trial':
                    to = self.login_web_elements.get_30_days_trial_txt()
                    if to.is_displayed():
                        self.utils.print_info("trial option is displayed")
                        self.auto_actions.click(self.login_web_elements.get_option_30_days_trial())
                        sleep(5)
                        self.utils.print_info("trial option is selected.")
                    else:
                        return -2

                elif login_option.lower() == 'extremecloudiqlicense':
                    ec = self.login_web_elements.get_extr_license_txt()
                    if ec.is_displayed():
                        self.auto_actions.click(self.login_web_elements.get_option_extr_cloudiq_license())
                        sleep(5)
                        try:
                            ekpopup = self.login_web_elements.get_legacy_ek_popup_hdr()
                            if ekpopup.is_displayed():
                                self.auto_actions.click(self.login_web_elements.get_legacy_ek_popup_no_btn())
                        except Exception as e:
                            pass
                        tp = self.login_web_elements.get_extr_license_tooltip()
                        if tp.is_displayed():
                            self.utils.print_info("ExtremeCloud IQ License option is selected.")
                        else:
                            return -2

                elif login_option.lower() == 'legacylicense':
                    ll = self.login_web_elements.get_legacy_license_txt()
                    if ll.is_displayed():
                        self.auto_actions.click(self.login_web_elements.get_option_legacy_license())
                        sleep(2)
                        self.utils.print_info("Legacy License option is selected.")
                        # legacy_ek_in = self.login_web_elements.get_legacy_ek_input_box
                        self.auto_actions.send_keys(self.login_web_elements.get_legacy_ek_input_box(), ekey)
                        sleep(5)
                    else:
                        return -2

                elif login_option.lower() == 'connect':
                    conn = self.login_web_elements.get_extr_connect_txt()
                    if conn.is_displayed():
                        self.utils.print_info("connect option is displayed...")
                        self.auto_actions.click(self.login_web_elements.get_option_extr_connect())
                        self.utils.print_info("Extreme Connect option is selected.")
                        sleep(5)
                    else:
                        return -2
                else:
                    self.utils.print_info("Not a valid login option.")
                    return -1

                gs_btn = self.login_web_elements.get_get_started_button()
                if gs_btn is not None:
                    self.utils.print_info("Clicking on Get Started....")
                    self.auto_actions.click(self.login_web_elements.get_get_started_button())

                if login_option.lower() == 'extremecloudiqlicense':
                    sleep(10)
                    self.utils.print_info("Redirected to Extreme SFDC for OAuth.")
                    self.link_xiq_to_extreme_portal(sfdc_user_type, sfdc_email, sfdc_pwd, shared_cuid)

                if login_option.lower() == 'legacylicense':
                    try:
                        ek_invalid = self.login_web_elements.get_legacy_ek_invalid_err()
                        if ek_invalid.is_displayed():
                            self.utils.print_info("License Error has occurred...")
                            ek_err = self.login_web_elements.get_legacy_ek_invalid_err().text
                            self.utils.print_info(str(ek_err))
                            return -1
                    except Exception as e:
                        pass

                try:
                    agchk = self.login_web_elements.get_cloud_tos_agree()
                    if agchk is not None:
                        self.utils.print_info("Click on I Agree and Submit on First TOS...")
                        self.auto_actions.click(self.login_web_elements.get_cloud_tos_agree())
                        sleep(2)
                        self.auto_actions.click(self.login_web_elements.get_cloud_tos_submit())
                        sleep(5)
                    if agchk is not None:
                        self.utils.print_info("Click on I Agree and Submit on Seond TOS...")
                        self.auto_actions.click(self.login_web_elements.get_cloud_tos_agree())
                        self.auto_actions.click(self.login_web_elements.get_cloud_tos_submit())
                    return 1
                except Exception as e:
                    pass
                self.utils.print_info(login_option + " login is successful.")
                return 1
            else:
                self.utils.print_info("Not a valid login option.")
                return -1

    def verify_upgrade_option_for_connect_user(self):
        """
        - This keyword checks if upgrade button is displayed and clicking on upgrade button
        navigates connect user to license management UI
        :return: None
        """
        self.utils.print_info("verifying it is a connect user...")
        ug_btn = self.login_web_elements.get_upgrade_btn()
        sleep(2)
        if ug_btn.is_displayed():
            self.utils.print_info("Customer is logged in as a Connect Customer")
            self.auto_actions.move_to_element(ug_btn)
            self.auto_actions.click(self.login_web_elements.get_upgrade_link())
            sleep(5)
            self.utils.print_info("Clicking on Upgrade btn, navigates user to license management.")
            return 1
        else:
            self.utils.print_info("Upgrade Button is not shown for Connect User.")
            return -1

    def link_xiq_to_extreme_portal(self, sfdc_user_type, sfdc_email, sfdc_pwd, shared_cuid=None):
        self.utils.print_info("Redirected to SFDC to complete oauth...")
        sfdc_url = self.get_base_url_of_current_page()
        self.utils.print_info("Completing OAuth...", sfdc_url)
        if "force.com" in sfdc_url:
            self.utils.print_info("Extreme SFDC URL", sfdc_url)
            self.auto_actions.send_keys(self.login_web_elements.get_sfdc_login_username(), sfdc_email)
            self.auto_actions.send_keys(self.login_web_elements.get_sfdc_login_pwd(), sfdc_pwd)
            self.auto_actions.click(self.login_web_elements.get_sfdc_login_btn())
            try:
                sfdc_login_err = self.login_web_elements.get_sfdc_login_err()
                if sfdc_login_err.is_displayed():
                    sfdc_login_err_txt = self.login_web_elements.get_sfdc_login_err().text
                    self.utils.print_info("SFDC login Failed...", sfdc_login_err_txt)
                    return -1
            except Exception as e:
                pass
            sleep(10)
            xiq_url = self.get_base_url_of_current_page()
            self.utils.print_info("Redirected back to XIQ URL: ", xiq_url)
            try:
                license_mgmt_ele = self.nav_web_elements.get_license_mgmt()
                if license_mgmt_ele.is_displayed():
                    self.auto_actions.click(license_mgmt_ele)
                    sleep(3)
            except Exception as e:
                pass

            self.utils.print_info("Checking If XIQ linking is by Partner, enter shared CUID...")
            if sfdc_user_type == "partner":
                shared_cuid_popup_hdr = self.login_web_elements.get_shared_cuid_hdr()
                if shared_cuid_popup_hdr.is_displayed():
                    self.utils.print_info("Shared CUID: ", shared_cuid)
                    self.auto_actions.send_keys(self.login_web_elements.get_shared_cuid_input(), shared_cuid)
                    self.auto_actions.click(self.login_web_elements.get_shared_cuid_submit_btn())
                    sleep(10)
                    try:
                        sh_cuid_err_txt = self.login_web_elements.get_shared_cuid_err().text
                        if sh_cuid_err_txt.is_displayed():
                            self.utils.print_info("Shared CUID is not correct", sh_cuid_err_txt)
                    except Exception as e:
                        pass
                    self.utils.print_info("Partner linking XIQ to Extreme Portal is complete.")
            elif sfdc_user_type == "customer":
                self.utils.print_info("Customer linked XIQ to Extreme Portal is complete.")

            self.utils.print_info("Check for Advance Onboard Popup page after login..")
            sleep(5)
            try:
                if self.login_web_elements.get_drawer_content().is_displayed():
                    self.auto_actions.click(self.login_web_elements.get_drawer_trigger())
            except Exception as e:
                pass
            self.utils.print_info("Navigate to license mgt..")
            try:
                license_mgmt_ele = self.nav_web_elements.get_license_mgmt()
                if license_mgmt_ele.is_displayed():
                    self.auto_actions.click(license_mgmt_ele)
                    sleep(3)
            except Exception as e:
                pass
            return 1

        else:
            self.utils.print_info("Redirection to Extreme Portal ERROR. Linking is not successful.")
            return -1

    def login_for_first_time(self):
        """
            - This keyword used to login for the first time user based on option provided in test case
            - If option is not specified, default option of "30-days trial" is selected.
            - Getting started with license is not supported through Automation as it depends on Gemalto license.
            - Assumes that user already in login option selection page
            - Keyword Usage:
             - ``Login For First Time``
            :return: 1
        """

        login_option = BuiltIn().get_variable_value("${LOGIN_OPTION}")
        self.utils.print_info("Selecting option : ", login_option)

        if "30-day trial" in login_option:
            self.auto_actions.click(self.login_web_elements.get_login_trail_30_days())

        elif "ExtremeCloud IQ license" in login_option:
            # self.auto_actions.click(self.login_web_elements.get_login_license_option())
            self.utils.print_info("we are not supporting this option proceeding with default option")

        elif "entitlement key" in login_option:
            self.auto_actions.click(self.login_web_elements.get_login_entitlement_radio())

            entitlement_key = BuiltIn().get_variable_value("${ENTITLEMENT_KEY}")

            self.utils.print_info("Entering entitlement key ", entitlement_key)
            self.auto_actions.send_keys(self.login_web_elements.get_login_entitlement_key(), entitlement_key)

        elif "1 year included Pilot license" in login_option:
            self.auto_actions.click(self.login_web_elements.get_login_year_trail_option())

        elif "IQ Connect" in login_option:
            self.auto_actions.click(self.login_web_elements.get_login_iq_connect())

        else:
            self.utils.print_info("proceeding with default option of 30-days trail")
            self.auto_actions.click(self.login_web_elements.get_login_trail_30_days())

        self.utils.print_info("Clicking on Get Started button...")
        self.auto_actions.click(self.login_web_elements.get_started_login_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Accepting Terms of service...")
        self.auto_actions.click(self.login_web_elements.get_accept_terms_of_service_wizard())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Submitting Terms of service...")
        self.auto_actions.click(self.login_web_elements.get_submit_terms_of_service_wizard())
        sleep(1)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Accepting data privacy policy...")
        self.auto_actions.click(self.login_web_elements.get_accept_data_privacy())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Submitting data privacy policy...")
        self.auto_actions.click(self.login_web_elements.get_submit_data_privacy())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)
        return 1

    def select_login_option(self, login_option, entitlement_key, salesforce_username=False,
                            salesforce_password=False, saleforce_shared_cuid=False):
        if self.login_web_elements.get_welcome_wizard_heading():
            self.utils.print_info("Welcome page wizard found. Looks like you are logging in for the first time!")
            self.utils.print_info("Selecting login option: ", login_option)
            self.screen.save_screen_shot()

            if "30-day-trial" in login_option:
                return self._30_day_trial()

            if "ExtremeCloud IQ License" in login_option:
                return self._extreme_cloud_iq_license(salesforce_username, salesforce_password, saleforce_shared_cuid)

            if "Legacy Entitlement Key" in login_option:
                return self._legacy_entitlement_key(entitlement_key)

            if "Pilot License" in login_option:
                return self._pilot_license()

            if "ExtremeCloud IQ Connect" in login_option:
                return self._extremecloud_iq_connect()

            return 1

    def _30_day_trial(self):
        self.utils.print_info("Selecting Default Option: 30 Day Trial...")
        if self.login_web_elements.get_30_days_trial_txt().is_displayed():
            self.auto_actions.click(self.login_web_elements.get_option_30_days_trial())
            sleep(2)
            self.screen.save_screen_shot()

            self.utils.print_info("Clicking on Get Started...")
            self.auto_actions.click(self.login_web_elements.get_get_started_button())
            sleep(10)
            self.screen.save_screen_shot()

            self._agree_cloud_terms_and_conditions()
            sleep (5)

            self._agree_data_privacy_and_protection()
            sleep(5)

            return 1
        else:
            self.utils.print_info("No selecting menu ")
            return 1

    def _extreme_cloud_iq_license(self, salesforce_username, salesforce_password, saleforce_shared_cuid):
        self.utils.print_info("Selecting ExtremeCloud IQ License...")
        self.auto_actions.click(self.login_web_elements.get_option_extr_cloudiq_license())
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking on Get Started...")
        self.auto_actions.click(self.login_web_elements.get_get_started_button())
        sleep(10)
        self.screen.save_screen_shot()

        self.utils.print_info("Entering Salesforce username")
        self.auto_actions.send_keys(self.login_web_elements.get_salesforce_username(), salesforce_username)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Entering Salesforce password")
        self.auto_actions.send_keys(self.login_web_elements.get_salesforce_password(), salesforce_password)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Submitting")
        self.auto_actions.click(self.login_web_elements.get_salesforce_submit())
        sleep(2)
        self.screen.save_screen_shot()

        sleep(10)
        enter_shared_cuid = self.login_web_elements.get_enter_shared_cuid()
        if enter_shared_cuid:
            self.auto_actions.send_keys(enter_shared_cuid, saleforce_shared_cuid)
            submit_shared_cuid = self.login_web_elements.get_submit_shared_cuid()
            if submit_shared_cuid:
                self.utils.print_info("submit button was found")
                self.auto_actions.click(submit_shared_cuid)
            else:
                self.utils.print_info("submit button not found ")
                return -1
            check_error_shared_cuid = self.login_web_elements.get_check_error_shared_cuid()
            if check_error_shared_cuid:
                self.utils.print_info("The below error was displayed when enter shared CUID:",
                                      check_error_shared_cuid.text)
                self.screen.save_screen_shot()
                return -1
            else:
                return 1
        else:
            self.utils.print_info("shared cuid dialog is not displayed ")

        self._agree_cloud_terms_and_conditions()
        sleep (5)

        self._agree_data_privacy_and_protection()
        sleep(5)

        return 1

    def _legacy_entitlement_key(self, entitlement_key):
        self.utils.print_info("Entering entitlement key: ", entitlement_key)
        sleep(5)

        self.auto_actions.click(self.login_web_elements.get_option_legacy_license())
        sleep(5)
        self.screen.save_screen_shot()

        self.auto_actions.send_keys(self.login_web_elements.get_login_entitlement_key(), entitlement_key)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking on Get Started...")
        self.auto_actions.click(self.login_web_elements.get_get_started_button())
        sleep(5)
        self.screen.save_screen_shot()

        self._agree_cloud_terms_and_conditions()
        if self._check_legacy_entitlement_key_errors() == -1:
            return -1
        self._agree_data_privacy_and_protection()

        return 1

    def _pilot_license(self):
        self.utils.print_info("Selecting Pilot License..")
        self.auto_actions.click(self.login_web_elements.get_login_year_trail_option())
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking on Next button...")
        self.auto_actions.click(self.login_web_elements.get_next_button())
        sleep(5)
        self.screen.save_screen_shot()

        self._agree_cloud_terms_and_conditions()
        sleep (5)
        self._agree_data_privacy_and_protection()
        sleep(5)
        return 1

    def _extremecloud_iq_connect(self):
        self.utils.print_info("Selecting ExtremeCloud IQ Connect..")
        self.auto_actions.click(self.login_web_elements.get_login_iq_connect())
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking on Get Started...")
        self.auto_actions.click(self.login_web_elements.get_get_started_button())
        sleep(5)
        self.screen.save_screen_shot()

        self._agree_cloud_terms_and_conditions()
        sleep(5)

        self._agree_data_privacy_and_protection()
        sleep(5)
        return 1

    def _agree_cloud_terms_and_conditions(self):
        self.utils.print_info("Accepting Cloud Terms of Service..")
        try:
            agree_checkbox = self.login_web_elements.get_agree_checkbox()
            if agree_checkbox is not None and agree_checkbox.is_displayed():
                self.auto_actions.click(self.login_web_elements.get_cloud_tos_agree())
                sleep(2)
                self.screen.save_screen_shot()

                self.auto_actions.click(self.login_web_elements.get_cloud_tos_submit())
                sleep(2)
                self.screen.save_screen_shot()

                return 1
            else:
                self.utils.print_info("No Cloud Terms and Conditions popup")
        except Exception as e:
            self.utils.print_info(e)

    def _agree_data_privacy_and_protection(self):
        self.utils.print_info("Accepting Data Privacy and Protection..")
        try:
            agree_data = self.login_web_elements.get_cloud_tos_agree()
            if agree_data:
                self.auto_actions.click(agree_data)

                sleep(2)
                self.screen.save_screen_shot()

                self.auto_actions.click(self.login_web_elements.get_cloud_tos_submit())
                sleep(2)
                self.screen.save_screen_shot()

                return 1
            else:
                self.utils.print_info("No Accepting Data Privacy and Protection popup")
        except Exception as e:
            self.utils.print_info(e)

    def _check_legacy_entitlement_key_errors(self):
        self.utils.print_info("Checking for entitlement key errors")
        try:
            entitlement_error = self.login_web_elements.get_entitlement_key_error()
            if "This entitlement key has already been used by another system" in entitlement_error.text:
                self.screen.save_screen_shot()
                self.utils.print_info("This entitlement key has already been used by another system")
                return -1
        except Exception as e:
            self.utils.print_debug(e)
            return 1

    def refresh_page(self, refresh_delay=10):
        """
        This keyword refreshes the current page
        :param refresh_delay: delay needed to reload the page
        :return: None
        """
        try:
            self.utils.print_info("Refreshing Page...")
            CloudDriver().cloud_driver.refresh()
            sleep(refresh_delay)
        except Exception as e:
            self.utils.print_info("Unable to refresh the page...")
            self.utils.print_info(e)