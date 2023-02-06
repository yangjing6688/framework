# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
import re
from time import sleep
from robot.libraries.BuiltIn import BuiltIn

from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions

from xiqse.elements.common.CommonAccountWebElements import CommonAccountWebElements
from xiqse.elements.common.CommonErrorWebElements import CommonErrorWebElements
from xiqse.elements.common.CommonLoginWebElements import CommonLoginWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements

from selenium.common.exceptions import JavascriptException


class XIQSE_CommonLogin():

    def __init__(self):
        pass

    def _init(self, url="default", incognito_mode="False", window_index=0):
        """
        This method initializes the driver object and makes it global

        :param url: if not default, will be read from the ${TEST_URL} variable
        :param incognito_mode: indicates whether or not to open the browser in incognito/private mode
        :param window_index: The Child Window Index value.
        :return: returns driver object
        """
        self.utils = Utils()
        try:
            if CloudDriver().cloud_driver == None:
                self.utils.print_info("Creating new cloud driver")
                CloudDriver().start_browser(url=url, program="xiqse", incognito_mode=incognito_mode)
                # extauto.common.CloudDriver.load_browser(url, program="xiqse", incognito_mode=incognito_mode)
                self.window_index = 0
            elif window_index != 0:
                self.utils.print_info(f"Initializing window with index: {window_index}")
                self.window_index = window_index
            else:
                self.utils.print_info("Cloud driver already exists - opening new window using same driver")
                self.window_index = CloudDriver().open_window(url, program="xiqse")
        except Exception as e:
            self.utils.print_info("Error: ", e)
            self.window_index = -1

        self.utils.print_info(f"Window Handle Index is {self.window_index}")
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.login_web_elements = CommonLoginWebElements()
        self.acct_web_elements = CommonAccountWebElements()
        self.error_web_elements = CommonErrorWebElements()
        self.view_web_elements = CommonViewWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        # return self.driver

    def xiqse_get_page_title(self):
        """
        - Get the title of the page

        :return: page title
        """
        return CloudDriver().cloud_driver.title

    def xiqse_get_window_index(self):
        """
        - Get the index of the window handle for this session

        :return: index of window handle
        """
        return self.window_index

    def xiqse_confirm_login_page_displayed(self):
        """
        - This keyword confirms the XIQ-SE Login page is being displayed.
        - Keyword Usage
        - ``XIQSE Confirm Login Page Displayed``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        page_title = self.login_web_elements.get_login_page_title()
        user_field = self.login_web_elements.get_login_page_username_text()
        pwd_field = self.login_web_elements.get_login_page_password_text()
        login_btn = self.login_web_elements.get_login_page_login_button()
        copyright_label = self.login_web_elements.get_login_page_copyright_label()
        support_link = self.login_web_elements.get_login_page_support_link()
        about_link = self.login_web_elements.get_login_page_about_link()
        if page_title and user_field and pwd_field and login_btn and copyright_label and support_link and about_link:
            self.utils.print_info("XIQ-SE Login page is displayed")
            ret_val = 1
        else:
            self.utils.print_info("XIQ-SE Login page is not properly displayed")
            if not page_title:
                self.utils.print_info("  Unable to find 'Extreme Cloud IQ Site Engine' title")
            if not user_field:
                self.utils.print_info("  Unable to find 'Username' field")
            if not pwd_field:
                self.utils.print_info("  Unable to find 'Password' field")
            if not login_btn:
                self.utils.print_info("  Unable to find 'Login' button")
            if not copyright_label:
                self.utils.print_info("  Unable to find copyright label")
            if not support_link:
                self.utils.print_info("  Unable to find 'Support' link")
            if not about_link:
                self.utils.print_info("  Unable to find 'About' link")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_user_logged_in(self):
        """
        - This keyword confirms the user has successfully logged into XIQSE.
        - Keyword Usage
        - ``XIQSE Confirm User Logged In``

        :return: 1 if user is logged in, else -1
        """
        ret_val = -1

        main_application = self.view_web_elements.get_main_application_body()
        if main_application:
            self.utils.print_info("User is successfully logged into XIQSE")
            ret_val = 1
        else:
            self.utils.print_info("User is not logged into XIQSE")

        return ret_val

    def xiqse_load_page(self, url="default", incognito_mode="False"):
        """
        - Loads the specified URL.
        - By default url will load from the topology file
        - keyword Usage:
        - ``XIQSE Load Page   ${URL}``

        :param url: url to load
        :param incognito_mode: indicates whether or not to open the browser in incognito/private mode
        :return: 1 if login successful else -1
        """
        if url == "default":
            self._init(incognito_mode=incognito_mode)
        else:
            self._init(url, incognito_mode)

        browser = BuiltIn().get_variable_value("${BROWSER}")

        self.utils.print_info("Browser: ", browser)

        try:
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['version'])
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['browserVersion'])

        return 1

    def xiqse_load_page_and_log_in(self, username, password, url="default", incognito_mode="False", check_credentials="true"):
        """
        - Load the Login page specified by the passed URL, and enter login credentials.
        - By default url will load from the topology file
        - keyword Usage:
        - ``XIQSE Load Page and Log In   ${USERNAME}   ${PASSWORD}``
        - ``XIQSE Load Page and Log In   ${USERNAME}   ${PASSWORD}   ${URL}``
        - ``XIQSE Load Page and Log In   ${USERNAME}   ${PASSWORD}    incognito_mode=True``
        - ``XIQSE Load Page and Log In   ${USERNAME}   ${PASSWORD}   ${URL}   incognito_mode=True``
        - ``XIQSE Load Page and Log In   ${USERNAME}   ${PASSWORD}   ${URL}   incognito_mode=True   check_credentials=True``

        :param username: login account username
        :param password: login account password
        :param url: url to load
        :param incognito_mode: indicates whether or not to open the browser in incognito/private mode
        :param check_credentials: check for invalid credentials
        :return: 1 if login successful else -1
        """
        self.xiqse_load_page(url, incognito_mode)
        return self.xiqse_login_user(username, password, check_credentials)

    def xiqse_login_user(self, username, password, check_credentials="true"):
        """
        - Log into the XIQ-SE account with the specified username and password
        - keyword Usage:
        - ``XIQSE Login User   ${USERNAME}   ${PASSWORD}``
        - ``XIQSE Login User   ${USERNAME}   ${PASSWORD}   check_credentials=True``

        :param username: login account username
        :param password: login account password
        :param check_credentials: check for invalid credentials
        :return: 1 if login successful else -1
        """
        self.utils.print_info(f"Logging in with Username: {username} -- Password: {password}")

        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_username_text(), username)

        self.utils.print_info("Entering Password...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_password_text(), password)

        self.utils.print_info("Clicking on Login button")
        self.auto_actions.click_reference(self.login_web_elements.get_login_page_login_button)

        if check_credentials.lower() == "true":
            self.utils.print_info("Checking for invalid credentials..")
            credential_warnings = self.login_web_elements.get_credentials_error_message()
            self.utils.print_info(f"Error logging in: {credential_warnings}")
            if "Unable to authenticate" in credential_warnings:
                self.utils.print_info("Wrong Credentials. Try Again")
                return -1
        else:
            self.utils.print_info("Skipping the check for invalid credentials")

        return 1

    def xiqse_logout_user(self):
        """
        - Logout the current user
        - Keyword Usage:
        - ``XIQSE Logout User``

        :return: None
        """
        ret_val = -1
        try:
            account_menu_btn = self.acct_web_elements.get_account_menu_button()
            if account_menu_btn:
                self.utils.print_info("Clicking Account menu")
                self.auto_actions.click(account_menu_btn)
                sleep(1)
                logout_menu_item = self.acct_web_elements.get_logout_menu_item()
                if logout_menu_item:
                    self.utils.print_info("Clicking Logout menu item")
                    self.auto_actions.click(logout_menu_item)
                    ret_val = 1
                else:
                    self.utils.print_info("Could not find Logout menu item")
            else:
                self.utils.print_info("Could not find Account menu button")
        except Exception as e:
            self.utils.print_info(f"Error: {e}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_handle_connection_lost_error(self, username, password):
        """
        - Closes the "Connection to server lost" error dialog, if displayed, and logs the user back in.
        - Keyword Usage:
        - ``XIQSE Handle Connection Lost Error   ${USERNAME}   ${PASSWORD}``

        :param username: login account username
        :param password: login account password
        :return: None
        """
        ret_val = -1
        try:
            error_dlg = self.error_web_elements.get_connection_lost_error_dialog()
            if error_dlg:
                ok_btn = self.error_web_elements.get_message_box_ok_button()
                if ok_btn:
                    self.utils.print_info("Clicking OK button in Connection Lost error dialog")
                    self.auto_actions.click(ok_btn)
                    sleep(1)
                    self.utils.print_info("Logging back into XIQ-SE")
                    ret_val = self.xiqse_login_user(username, password)
                else:
                    self.utils.print_info("Could not find OK button for message box")
            else:
                self.utils.print_info("Connection Lost error dialog was not displayed")
                ret_val = 1
        except Exception as e:
            self.utils.print_info("Error: ", e)

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_quit_browser(self, _driver=None):
        """
        - Closes all the browser windows and ends the WebDriver session gracefully.
        - if the driver object is passed, quits and returns
        - Keyword Usage:
        - ``XIQSE Quit Browser``

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
            # CloudDriver().cloud_driver = None
            return 1
        except Exception as e:
            self.utils.print_info("Error: ", e)
            self.utils.print_debug("Error: ", e)
            return -1

    def xiqse_get_base_url_of_current_page(self):
        """
        - This Keyword is used to get the url of current loaded page
        :return: url
        """
        base_url = re.search(r'^(http:\/\/|https:\/\/)?([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]*', CloudDriver().cloud_driver.current_url)
        return base_url.group()

    def xiqse_get_version(self):
        """
        - This Keyword is used to get the XIQSE version
        :return: version of XIQSE
        """
        version = ""
        # Get the version
        try:
            version = CloudDriver().cloud_driver.execute_script("return fullVersion")
            self.utils.print_info(f"Version of XIQSE is {version}")
        except JavascriptException:
            self.utils.print_info("Unable to obtain the version of XIQSE")

        return version

    def xiqse_switch_to_window(self, win_index):
        """
        - Switches to the specified window

        :param win_index: Index of the window to switch to
        :return: None
        """
        CloudDriver().switch_to_window(win_index)

    def xiqse_close_window(self, win_index):
        """
        - Closes the specified window

        :param win_index: Index of the window to close
        :return: None
        """
        CloudDriver().close_window(win_index)

    def xiqse_refresh_page(self):
        """
        - Refreshes the browser page

        :return: None
        """
        CloudDriver().refresh_page()

    def xiqse_logout_user_child_window(self, win_index=0):
        """
        - Logout the XIQ-SE user from a session opened in a Child Window.
        - Keyword Usage:
        - ``XIQSE Logout User Child Window   win_index``

        :param win_index: Index of the XIQ-SE Child Window
        :return: 1 if successful else -1
        """
        ret_val = -1

        self._init(window_index=win_index)
        self.screen.save_screen_shot()
        try:
            account_menu_btn = self.acct_web_elements.get_account_menu_button()
            if account_menu_btn:
                self.utils.print_info("Clicking Account menu")
                self.auto_actions.click(account_menu_btn)
                sleep(1)
                logout_menu_item = self.acct_web_elements.get_logout_menu_item()
                if logout_menu_item:
                    self.utils.print_info("Clicking Logout menu item")
                    self.auto_actions.click(logout_menu_item)
                    ret_val = 1
                else:
                    self.utils.print_info("Could not find Logout menu item")
            else:
                self.utils.print_info("Could not find Account menu button")
        except Exception as e:
            self.utils.print_info("Error: ", e)

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_child_window_indexes(self, win_index):
        """
        - Obtain a list of Child Window Indexes.
        - A list of Child Window Index(es) is returned.
        - Each Child Window is initialized.
        - Keyword Usage:
        - ``XIQSE Child Window Indexes``

        :param:  win_index - Index of the parent window
        :return: Return List containing the Child Window Indexes
        """
        window_index_list = CloudDriver().get_child_window_list(win_index)

        for window_index in window_index_list:
            self.xiqse_init_child_window(window_index)

        return window_index_list

    def xiqse_init_child_window(self, win_index):
        """
        - This method initializes the driver object and makes it global.
        - This initialization is specific to XIQ-SE.
        - Keyword Usage:
        - ``XIQSE Init Child Window   win_index``

        :param win_index: child window index that will be initialized
        """
        self._init(window_index=win_index)
        self.utils.print_info(f"xiqse_init_child_window: Window Handle Index is {self.window_index}")

    def xiqse_get_username(self):
        """
        - This keyword obtains the user logged into XIQ-SE.
        - Keyword Usage
        - ``XIQSE Get Username``

        :return: XIQ-SE Username if found, else None
        """
        ret_val = None

        xiqse_username_field = self.acct_web_elements.get_xiqse_username()
        xiqse_username = xiqse_username_field.text
        self.utils.print_debug(f"xiqse_get_username: xiqse_username value: {xiqse_username}")
        if xiqse_username:
            self.utils.print_info(f"xiqse_get_username: {xiqse_username} is logged into XIQSE")
            ret_val = xiqse_username
        else:
            self.utils.print_info("xiqse_get_username: Could not obtain XIQSE username")

        return ret_val

    def xiqse_get_authorization_group(self):
        """
        - This keyword obtains the Authorization Group for the XIQ-SE User.
        - Keyword Usage
        - ``XIQSE Get Authorization Group``

        :return: XIQ-SE Authorization Group if found, else None
        """
        ret_val = None

        xiqse_authorization_group_field = self.acct_web_elements.get_xiqse_authorization_group()
        xiqse_authorization_group = xiqse_authorization_group_field.text
        self.utils.print_debug(f"xiqse_get_authorization_group: Authorization Group value: {xiqse_authorization_group}")
        if xiqse_authorization_group:
            self.utils.print_info(f"xiqse_get_authorization_group: XIQ-SE User is assigned to {xiqse_authorization_group}")
            ret_val = xiqse_authorization_group
        else:
            self.utils.print_info("xiqse_get_authorization_group: Could not obtain XIQSE Authorization Group")

        return ret_val
