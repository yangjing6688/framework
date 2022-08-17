import threading
import requests
import re
import random
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
            self.window_index = 0
        else:
            self.utils.print_info("Cloud driver already exists - opening new window using same driver")
            self.window_index = CloudDriver().open_window(url)

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
                   salesforce_password=False, saleforce_shared_cuid=False, quick=False, check_warning_msg=False,
                   max_retries=3, **kwargs):
        """
        - Login to Xiq account with username and password (we will try up to 3 times)
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
        :param saleforce_shared_cuid: Salesforce Shared CUID
        :param quick: Quick login without more sleep time while loading url
        :param check_warning_msg: Flag to Enable to Warning Messages validation during XIQ Login
        :param (**kwarg) expect_error: the keyword is expected to fail
        :return: 1 if login successful else -1
        """
        result = -1
        count = 0
        expect_error = self.common_validation.get_kwarg_bool(kwargs, "expect_error", False)
        result = self._login_user(username, password, capture_version, login_option, url,
                    incognito_mode, co_pilot_status, entitlement_key, salesforce_username,
                    salesforce_password, saleforce_shared_cuid, quick, check_warning_msg,
                    **kwargs)

        # Let's try again if we don't expect and error and the results were not good
        if not expect_error:
            while result != 1 and count < max_retries:
                self.utils.print_warning(f'Trying to log in again: {count}')
                result = self._login_user(username, password, capture_version, login_option, url,
                                          incognito_mode, co_pilot_status, entitlement_key, salesforce_username,
                                          salesforce_password, saleforce_shared_cuid, quick, check_warning_msg,
                                          **kwargs)
                count = count + 1
        self.common_validation.validate(result, 1, **kwargs)
        return result

    def _login_user(self, username, password, capture_version=False, login_option="30-day-trial", url="default",
                   incognito_mode="False", co_pilot_status=False, entitlement_key=False, salesforce_username=False,
                   salesforce_password=False, saleforce_shared_cuid=False, quick=False, check_warning_msg=False,
                   **kwargs):
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
        if 'portal' in url:
            self.screen.save_screen_shot()
            self.utils.print_info("Entering Username...")
            self.auto_actions.send_keys(self.login_web_elements.get_login_portal_page_username_text(), username)
            sleep(3)
            self.utils.print_info("Entering Password...")
            self.auto_actions.send_keys(self.login_web_elements.get_login_portal_page_password_text(), password)
            sleep(3)
            self.utils.print_info("Clicking on Sign In button")
            self.auto_actions.click(self.login_web_elements.get_login_portal_page_login_button())
            sleep(2)
            self.screen.save_screen_shot()
            check_error = self.login_web_elements.get_login_portal_check_error()
            if check_error:
                self.utils.print_info("Error is displayed at loging : ", check_error.text)
                return -1
            else:
                pass
            sleep(5)
            return 1
        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_username_text(), username)

        self.utils.print_info("Entering Password...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_password_text(), password)

        self.utils.print_info("Clicking on Sign In button")

        self.auto_actions.click(self.login_web_elements.get_login_page_login_button())
        if quick:
            sleep(2)
        else:
            sleep(5)

        self.utils.print_info("Check for wrong credentials..")
        credential_warnings = self.login_web_elements.get_credentials_error_message()
        self.utils.print_info("Wrong Credential Message: ", credential_warnings)
        if "Looks like the email or password does not match our records. Please try again." in credential_warnings:
            # self.utils.print_info("Wrong Credentials. Try Again")
            kwargs['fail_msg'] = "Wrong Credentials. Try Again"
            return -1

        if self.select_login_option(login_option, entitlement_key=entitlement_key, salesforce_username=salesforce_username,
                                    salesforce_password=salesforce_password, saleforce_shared_cuid=saleforce_shared_cuid) == -1:
            kwargs['fail_msg'] = "Wrong Credentials. Try Again"
            return -1

        if quick:
            sleep(2)
        else:
            sleep(10)
        self.utils.print_info("Capturing screenshot after logging")
        self.screen.save_screen_shot()
        if check_warning_msg:
            self.utils.print_info("Check for Warning Messages..")
            if self.login_web_elements.get_dialog_message():
                self.utils.print_info("Clicking Close button")
                self.auto_actions.click(self.login_web_elements.get_dialog_box_close_button())

            self.utils.print_info("Check for WIPS Warning Messages..")
            wips_warnings = self.login_web_elements.get_wips_dialog_message()
            self.utils.print_info("Check for WIPS Warning Message is : ", wips_warnings)
            if self.login_web_elements.get_wips_dialog_message():
                if "Please update existing WIPS policies" in wips_warnings:
                    self.utils.print_info("Clicking Don't show again Checkbox")
                    self.auto_actions.click(self.login_web_elements.get_wips_popup_dialog_dont_show_again_checkbox())
                    sleep(2)

                    self.utils.print_info("Clicking Close button")
                    self.auto_actions.click(self.login_web_elements.get_wips_popup_dialog_close_button())
                    sleep(2)

            self.utils.print_info("Check for Advance Onboard Popup page after login..")
            try:
                if self.login_web_elements.get_drawer_content().is_displayed():
                    self.auto_actions.click(self.login_web_elements.get_drawer_trigger())
            except Exception as e:
                pass
        # if self.login_web_elements.get_devices_list_check().is_displayed():
        #     self.utils.print_info("webelement exists in the mainpage")

        #self.get_version()
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
        
        try:
            if self.login_web_elements.get_right_arrow().is_displayed():
                self.utils.print_info("Clicking welcome popup")
                self.auto_actions.click(self.login_web_elements.click_right_arrow())
        except Exception as er:
            pass

        return 1

    def get_version(self):
        self.utils.print_info("Clicking on About Extreme cloudIQ link")
        self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
        self.auto_actions.click(self.login_web_elements.get_about_extreme_cloudiq_link())
        self.screen.save_screen_shot()
        viq_id = self.login_web_elements.get_viq_id_field().text
        build_id=self.login_web_elements.get_build_id().text
        xiq_version = self.login_web_elements.get_build_version_details()
        self.utils.print_info(f"VIQ ID Is: {viq_id}")
        self.utils.print_info("Build Id: ",build_id)
        self.utils.print_info("XIQ build Version Is: ", xiq_version)

        self.utils.print_info("Close About Extreme cloudIQ Link Dialogue Page")
        self.auto_actions.click(self.login_web_elements.get_cancel_about_extremecloudiq_dialogue())

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
            sleep(10)
        except:
            print("t1.do_run not initialized")

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

        if _driver:
            _driver.quit()
            return 1

        # stop tool tip text capture thread
        try:
            if self.t1.is_alive():
                self.t1.do_run = False
                sleep(10)
            return 1
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            return -1
        finally:
            CloudDriver().close_browser()
            self.utils.print_info("Resetting cloud driver to -1")

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
        """
        - This method is used to call the API requests using requests

        :param url: api complete url
        :return: response_code, json_response, total_time
        """
        self.utils.print_info("URL: ", url)

        try:
            r = requests.post(url)

            json_response = r.text
            response_code = r.status_code
            total_time = r.elapsed.total_seconds()
        except requests.exceptions.RequestException: # This catches any errors that requests raises. Bad HTTP responses(4xx, 5xx) are not raised as exceptions
            json_response = "No Output"
            response_code = None
            total_time = None


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

    def _capture_data_center_name(self):
        """
        - Get XIQ Data Center Name

        :return: data_center_name
        """
        self.utils.print_info("Clicking on About ExtremecloudIQ link")
        self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
        sleep(2)
        self.auto_actions.click(self.login_web_elements.get_about_extreme_cloudiq_link())
        sleep(2)

        data_center_name = self.login_web_elements.get_data_center_name()
        self.utils.print_info("XIQ Data Center Name Is: ", data_center_name)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Close About ExtremecloudIQ Link Dialogue Page")
        self.auto_actions.click(self.login_web_elements.get_cancel_about_extremecloudiq_dialogue())

        return data_center_name


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
        self.screen.save_screen_shot()
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

    def get_data_center_name(self):
        """
        - Get XIQ Data Center Name

        :return: data_center_name
        """
        return self._capture_data_center_name()

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
                self.utils.print_info("Clicking Don't show again Checkbox")
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
            sleep(10)
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
                    self.utils.print_info("Click on I Agree and Submit on Second TOS...")
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
            sleep(5)

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
        sleep(5)

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
        sleep(5)
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

    def click_advanced_onboard_popup(self):
           """
           This keyword just clicks the advanced Onboard popup sliding window that appears during the first login or after reset VIQ.
           - Keyword Usage:
         - ` click advanced popup`
            :return: None
           """
           self.utils.print_info("Check for Advance Onboard Popup page after login..")
           try:
               if self.login_web_elements.get_drawer_content().is_displayed():
                   self.auto_actions.click(self.login_web_elements.get_drawer_trigger())
           except Exception as e:
               pass

    def create_new_user_portal(self, customer_name, admin_first_name, admin_last_name, admin_password,
                               sw_connection_host):
        """
        Creates a fresh new user in portal
        :param customer_name: the name of the customer, written as an email
        :param admin_first_name: first name of the admin
        :param admin_last_name: last name of the admin
        :param admin_email: admin email, the email that is used to log in into xiq cloud
        :param admin_password: the password chosen to log in into xiq cloud
        :param sw_connection_host: the url of the RDC
        :return: returns 1 if the account was created succesfully or -1 if otherwise
        """
        cnt = 0
        while cnt < 3:
            random_nr = random.randrange(1, 10000)
            user = customer_name + "_" + str(random_nr) + "@gmail.com"
            self.utils.print_info("user:", user)
            check = self.check_if_xiq_user_exists(user)
            if check == 1:
                break
            elif check == -1:
                if cnt == 2:
                    self.utils.print_info("the users already existed")
                    return -1
                else:
                    self.utils.print_info("the user already existed . Try again")
            else:
                if cnt == 2:
                    self.utils.print_info("Error")
                    return -1
                else:
                    pass
            cnt = cnt + 1

        self.screen.save_screen_shot()
        self.utils.print_info("Creating new user...")
        self.utils.print_info("Clicking on add button...")
        sleep(10)
        found_page = False
        cnt = 0
        while cnt < 4:
            add_button = self.login_web_elements.get_add_button_portal()
            if add_button:
                self.utils.print_info("Found add button!")
                self.auto_actions.click(add_button)
                found_page = True
                break
            else:
                self.utils.print_info("Unable to find the add button.Try again:", cnt)
            sleep(20)
        if not found_page:
            self.utils.print_info("ADD BUTTON NOT FOUND")
            return -1
        sleep(5)
        self.screen.save_screen_shot()
        self.utils.print_info("Inserting customer name in the field...")
        customer_name_field = self.login_web_elements.get_customer_name_field()
        if customer_name_field:
            self.utils.print_info("Found customer name field!")
            self.utils.print_info("Inserting customer name: " + user)
            self.auto_actions.send_keys(customer_name_field, user)
        else:
            self.utils.print_info("Unable to find customer name field.")
            self.screen.save_screen_shot()
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin first name in the field...")
        first_name_field = self.login_web_elements.get_admin_first_name_field()
        if first_name_field:
            self.utils.print_info("Found admin first name field!")
            self.utils.print_info("Inserting admin first name: " + admin_first_name)
            self.auto_actions.send_keys(first_name_field, admin_first_name)
        else:
            self.utils.print_info("Unable to find admin first name field.")
            self.screen.save_screen_shot()
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin last name in the field...")
        last_name_field = self.login_web_elements.get_admin_last_name_field()
        if last_name_field:
            self.utils.print_info("Found admin last name field!")
            self.utils.print_info("Inserting admin last name: " + admin_last_name)
            self.auto_actions.send_keys(last_name_field, admin_last_name)
        else:
            self.utils.print_info("Unable to find admin last name field.")
            self.screen.save_screen_shot()
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin email in the field...")
        admin_email_field = self.login_web_elements.get_admin_email_field()
        if admin_email_field:
            self.utils.print_info("Found admin email field!")
            self.utils.print_info("Inserting admin email: " + user)
            self.auto_actions.send_keys(admin_email_field, user)
        else:
            self.utils.print_info("Unable to find admin email field.")
            self.screen.save_screen_shot()
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin password in the field...")
        admin_password_field = self.login_web_elements.get_admin_password_field()
        if admin_password_field:
            self.utils.print_info("Found admin password field!")
            self.utils.print_info("Inserting admin password: " + admin_password)
            self.auto_actions.send_keys(admin_password_field, admin_password)
        else:
            self.utils.print_info("Unable to find admin password field.")
            self.screen.save_screen_shot()
            return -1
        sleep(5)
        self.utils.print_info("Clicking on Data Center dropdown...")
        self.screen.save_screen_shot()
        data_center_dropdown = self.login_web_elements.get_data_center_dropdown()
        if data_center_dropdown:
            self.utils.print_info("Found the data center dropwdown!")
            sleep(2)
            self.auto_actions.click(data_center_dropdown)
            data_center_dropdown_options = self.login_web_elements.get_data_center_dropdown_options()
            if data_center_dropdown_options:
                self.utils.print_info("Found dropdown options!")
                sleep(2)
                pattern1 = "(\\w+)."
                gdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
                self.utils.print_info("RDC is : ", gdc[0])
                flag = False
                for option in data_center_dropdown_options:
                    if gdc[0] in option.text:
                        flag = True
                        self.auto_actions.click(option)
                        self.utils.print_info(option.text)
                        break
                if flag:
                    self.utils.print_info("Found the required datacenter: " + gdc[0])
                else:
                    self.utils.print_info("Unable to find the required datacenter.")
                    self.utils.print_info("Clicking on Cancel button...")
                    cancel_button = self.login_web_elements.get_cancel_button()
                    if cancel_button:
                        self.utils.print_info("Found Cancel button!")
                        self.auto_actions.click(cancel_button)
                        return -1
                    else:
                        self.utils.print_info("Unable to find the cancel button.")
                        return -1
            else:
                self.utils.print_info("Unable to find dropdown options.")
                return -1
        else:
            self.utils.print_info("Unable to find the dropdown menu.")
            return -1
        self.utils.print_info("Clicking on submit button...")
        self.screen.save_screen_shot()
        submit_button = self.login_web_elements.get_submit_button()
        if submit_button:
            self.utils.print_info("Found submit button!")
            sleep(2)
            self.auto_actions.click(submit_button)
            self.screen.save_screen_shot()
            return user
        else:
            self.utils.print_info("Unable to find submit button.")
            return -1

    def delete_user_portal(self, customer_name, check_delete_devices=-1):
        '''
        This function deletes the account created in portal
        :param customer_name:   the name of the customer under which the account was created
        :return: returns 1 if the account was deleted or -1 if otherwise
        '''
        sleep(20)
        if check_delete_devices == -1:
            print("There are still devices on this account!!!!")
            self.screen.save_screen_shot()
            return -1
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking on name cell menu button ...")
        cell_menu_button = self.login_web_elements.get_cell_menu_button_name_section()
        if cell_menu_button:
            self.utils.print_info("Cell menu button found!")
            self.auto_actions.click(cell_menu_button)
            self.utils.print_info("Clicking on filter type dropdown")
            filter_type_dropdown = self.login_web_elements.get_filter_type_dropdown()
            if filter_type_dropdown:
                self.utils.print_info("Found the filter type dropdown!")
                self.auto_actions.click(filter_type_dropdown)
                sleep(2)
                filter_dropdown_option_equals = self.login_web_elements.get_filter_dropdown_option_equals()
                if filter_dropdown_option_equals:
                    self.utils.print_info("Found filter dropdown option: Equals")
                    self.auto_actions.click(filter_dropdown_option_equals)
                else:
                    self.utils.print_info("Unable to find dropdown option: Equals")
                    self.screen.save_screen_shot()
                    return -1
            else:
                self.utils.print_info("Unable to click filter type dropdown.")
                self.screen.save_screen_shot()
                return -1
            filter_text_box = self.login_web_elements.get_filter_text_box()
            if filter_text_box:
                self.utils.print_info("Found the filter text box!")
                self.auto_actions.send_keys(filter_text_box, customer_name)
            else:
                self.utils.print_info("Unable to find the filter text box!")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("Unable to find cell menu button.")
            self.screen.save_screen_shot()
            return -1
        sleep(3)
        user_found = self.login_web_elements.get_user_found()
        if user_found:
            if len(user_found) == 1:
                self.utils.print_info(user_found[0].text)
                sleep(5)
                self.utils.print_info("Found user!")
                self.utils.print_info("Deleting user...")
                self.auto_actions.click(user_found[0])
            else:
                self.utils.print_info("Multiple users were found ")
                self.screen.save_screen_shot()
                return -1
            delete_button = self.login_web_elements.get_delete_button()
            if delete_button:
                self.utils.print_info("Found delete button!")
                sleep(2)
                self.auto_actions.click(delete_button)
                sleep(2)
                self.screen.save_screen_shot()
                confirmation_option_yes = self.login_web_elements.get_confirmation_option_yes()
                if confirmation_option_yes:
                    self.utils.print_info("Found the confirmation option!")
                    self.auto_actions.click(confirmation_option_yes)
                else:
                    self.utils.print_info("Unable to find confirmation option!")
                    return -1
                sleep(5)
                self.screen.save_screen_shot()
                delete_confirmation = self.login_web_elements.get_delete_confirmation()
                if delete_confirmation:
                    self.utils.print_info("Delete confirmation has been found!")
                    self.utils.print_info(delete_confirmation.text)
                    return 1
                else:
                    self.utils.print_info("Confirmation hasn't been found!")
            else:
                self.utils.print_info("Unable to find delete button.")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("The user has already been deleted or it hasn't been created.")
            self.screen.save_screen_shot()
            return 1
        return 1

    def log_out_portal(self):
        '''
        This function logs out from portal
        :return: returns 1 if logging out was succesfull or -1 if otherwise
        '''
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking LOGOUT button...")
        log_out_button_portal = self.login_web_elements.get_log_out_button_portal()
        if log_out_button_portal:
            self.utils.print_info("Found LOGOUT button!")
            self.auto_actions.click(log_out_button_portal)
            self.utils.print_info("Succesfully logged out!")
            return 1
        else:
            self.utils.print_info("Unable to find LOGOUT button.")
            return -1

    def get_portal_url(self, sw_connection_host):
        '''

        :param sw_connection_host: the url of the RDC
        :return: the url of portal page ; else -1 
        '''

        pattern1 = "(\\w+)r\\d+."
        gdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
        self.utils.print_info("GDC is : ", gdc[0])
        if isinstance(gdc,list):
            if isinstance(gdc[0],str):
                url = "https://" + gdc[0] + "-portal.qa.xcloudiq.com/portal/"
                self.utils.print_info("url is : ", url)
                return url
            else:
                return -1
        else:
            return -1
        return -1

    def check_if_xiq_user_exists(self, customer_name):
        '''
        This function check if the XIQ user exists into portal page
        :param customer_name:   the name of the customer under which the account was created
        :return: returns 1 if the account user doesn't exist; else -1
        '''

        self.screen.save_screen_shot()
        self.utils.print_info("Clicking on name cell menu button ...")
        cell_menu_button = self.login_web_elements.get_cell_menu_button_name_section()
        if cell_menu_button:
            self.utils.print_info("Cell menu button found!")
            self.auto_actions.click(cell_menu_button)
            self.utils.print_info("Clicking on filter type dropdown")
            filter_type_dropdown = self.login_web_elements.get_filter_type_dropdown()
            if filter_type_dropdown:
                self.utils.print_info("Found the filter type dropdown!")
                self.auto_actions.click(filter_type_dropdown)
                sleep(2)
                filter_dropdown_option_equals = self.login_web_elements.get_filter_dropdown_option_equals()
                if filter_dropdown_option_equals:
                    self.utils.print_info("Found filter dropdown option: Equals")
                    self.auto_actions.click(filter_dropdown_option_equals)
                else:
                    self.utils.print_info("Unable to find dropdown option: Equals")
                    self.screen.save_screen_shot()
                    return -1
            else:
                self.utils.print_info("Unable to click filter type dropdown.")
                self.screen.save_screen_shot()
                return -1
            filter_text_box = self.login_web_elements.get_filter_text_box()
            if filter_text_box:
                self.utils.print_info("Found the filter text box!")
                self.auto_actions.send_keys(filter_text_box, customer_name)
            else:
                self.utils.print_info("Unable to find the filter text box!")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("Unable to find cell menu button.")
            self.screen.save_screen_shot()
            return -1
        sleep(3)
        user_found = self.login_web_elements.get_user_found()
        if user_found:
            if len(user_found) == 1:
                self.utils.print_info(user_found[0].text)
                sleep(5)
                self.utils.print_info("Found user!")
                return -1
            else:
                self.utils.print_info("Multiple users were found ")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("The user has already been deleted or it hasn't been created.")
            self.screen.save_screen_shot()
            return 1
        return 1

    def switch_to_extreme_guest_window(self, win_index=1):
        """
        - Switches to the specified window

        :param:  win_index - Index of the window to switch to
        :return: None
        """
        CloudDriver().switch_to_window(win_index)

    def close_extreme_guest_window(self, win_index=1):
        """
        - Closes the specified window

        :param:  win_index - Index of the window to close
        :return: None
        """
        CloudDriver().close_window(win_index)
