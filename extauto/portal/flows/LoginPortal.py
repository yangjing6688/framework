import threading
from time import sleep

from robot.libraries.BuiltIn import BuiltIn

from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation

import extauto.xiq.flows.common.ToolTipCapture
import extauto.xiq.flows.common.Navigator

from extauto.portal.elements.PortalWebElements import PortalWebElements

class LoginPortal:

    def __init__(self):
        self.common_validation = CommonValidation()
        self.t1 = None
        self.utils = Utils()
        self.login_web_elements = PortalWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def _init(self, url="default", incognito_mode="False"):
        """
        This method initializes the driver object and makes it global
        :param url: if not default, will be read from the ${TEST_URL} variable
        :return: returns driver object
        """

        if CloudDriver().cloud_driver is None:
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
    def login_user(self, username, password, url="default", max_retries=3,**kwargs):
        """
        - Login to Xiq account with username and password (we will try up to 3 times)
        - By default url will load from the topology file
        - keyword Usage:
        - ``Login User   ${USERNAME}   ${PASSWORD}``

        Supported Modes:
            UI - default mode

        :param username: login account username
        :param password: login account password
        :param url: login url
        :param max_retries: the max retry times
        :param (**kwarg) expect_error: the keyword is expected to fail
        :return: 1 if login successful else -1
        """
        result = -1
        count = 0
        expect_error = self.common_validation.get_kwarg_bool(kwargs, "expect_error", False)
        result = self._login_user(username, password, url, **kwargs)

        # Let's try again if we don't expect and error and the results were not good
        if not expect_error:
            while result != 1 and count < max_retries:
                self.utils.print_warning(f'Trying to log in again: {count}')
                result = self._login_user(username, password, url, **kwargs)
                count = count + 1
        if result != 1:
            kwargs['fail_msg'] = "'login_user()' -> Login was not successful"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Login was successful"
            self.common_validation.passed(**kwargs)
        return result

    def _login_user(self, username, password, url="default", incognito_mode="False", **kwargs):
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
        if url == "default":
            url = BuiltIn().get_variable_value("${TEST_URL}")
        if 'portal' in url:
            self.screen.save_screen_shot()
            self.utils.print_info("Entering Username...")
            self.auto_actions.send_keys(self.login_web_elements.get_login_portal_page_username_text(), username)
            sleep(3)
            self.utils.print_info("Entering Password...")
            self.auto_actions.send_keys(self.login_web_elements.get_login_portal_page_password_text(), password)
            sleep(3)
            self.utils.print_info("Clicking on Sign In button")
            self.auto_actions.click_reference(self.login_web_elements.get_login_portal_page_login_button)
            sleep(2)
            self.screen.save_screen_shot()
            check_error = self.login_web_elements.get_login_portal_check_error()
            if check_error:
                self.utils.print_info("Error is displayed at loging : ", check_error.text)
                kwargs['fail_msg'] = f"'_login_user()' -> Error is displayed at loging : {check_error.text}"
                self.common_validation.fault(**kwargs)
                return -1
            else:
                pass
            sleep(5)
            kwargs['pass_msg'] = "Login successful"
            self.common_validation.passed(**kwargs)
            return 1

    def logout_user(self, **kwargs):
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
        except Exception:
            print("t1.do_run not initialized")

        try:
            self.utils.print_info("Clicking on Logout Menu")
            self.auto_actions.click_reference(self.login_web_elements.get_logout_portal_user_menu_item)
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            kwargs['fail_msg'] = f"'logout_user()' -> Error: {e}"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Logout Successful"
        self.common_validation.passed(**kwargs)
        return 1

    def quit_browser(self, _driver=None, **kwargs):
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
            kwargs['pass_msg'] = "Quit browser Successfully"
            self.common_validation.passed(**kwargs)
            return 1

        # stop tool tip text capture thread
        try:
            if self.t1:
                if self.t1.is_alive():
                    self.t1.do_run = False
                    sleep(10)
                kwargs['pass_msg'] = "Quit browser Successfully"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                # nothing to do
                return 1
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            kwargs['fail_msg'] = f"'quit_browser()' -> Error: {e}"
            self.common_validation.failed(**kwargs)
            return -1
        finally:
            CloudDriver().close_browser()
            self.utils.print_info("Resetting cloud driver to -1")

