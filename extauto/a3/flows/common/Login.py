import threading
from time import sleep
from robot.libraries.BuiltIn import BuiltIn

import common.CloudDriver
from common.Screen import Screen
from common.Utils import Utils
from common.AutoActions import AutoActions

import xiq.flows.common.ToolTipCapture

from a3.elements.LoginWebElements import LoginWebElements
from xiq.elements.PasswordResetWebElements import PasswordResetWebElements


class Login:

    def __init__(self):
        self.record = False
        self.t1 = None
        pass

    def _init(self, url="default", incognito_mode="False"):
        """
        This method initializes the driver object and makes it global
        :param url: if not default, will be read from the ${TEST_URL} variable
        :return: returns driver object
        """
        global driver
        self.utils = Utils()
        if common.CloudDriver.cloud_driver == -1:
            self.utils.print_info("Creating new cloud driver")
            common.CloudDriver.load_browser(url, incognito_mode=incognito_mode)
            self.window_index = 0
        else:
            self.utils.print_info("Cloud driver already exists - opening new window using same driver")
            self.window_index = common.CloudDriver.open_window(url)
        self.utils.print_info(f"Window Handle Index is {self.window_index}")
        self.driver = common.CloudDriver.cloud_driver
        self.login_web_elements = LoginWebElements()
        self.pw_web_elements = PasswordResetWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        return self.driver

    def get_page_title(self):
        """
        - Get the title of the page

        :return: page title
        """
        return self.driver.title

    def login_a3_user(self, username, password, capture_version=False, code="default", url="default", incognito_mode="False"):
        """
        - Login A3 account with username and password
        - By default url will load from the topology file
        - keyword Usage:
         - ``Login User   ${USERNAME}   ${PASSWORD}``
         - ``Login User   ${USERNAME}   ${PASSWORD}    capture_version=True``

        :param username: login account username
        :param password: login account password
        :param capture_version: true if want capture the a3 build version
        :param code:
        :param url: url to load
        :return: 1 if login successful else -1
        """

        my_driver = None
        if url == "default":
            my_driver = self._init(incognito_mode=incognito_mode)
        else:
            my_driver = self._init(url, incognito_mode)

        #start the thread to capture the tool tip text
        self.t1 = threading.Thread(target=xiq.flows.common.ToolTipCapture.tool_tip_capture, daemon=True)
        self.t1.start()

        browser = BuiltIn().get_variable_value("${BROWSER}")

        self.utils.print_info("Browser: ", browser)

        try:
         self.utils.print_info("Version: ", self.driver.capabilities['version'])
        except Exception as e:
         self.utils.print_debug(e)
         self.utils.print_info("Version: ", self.driver.capabilities['browserVersion'])

        self.utils.print_info("Logging with Username : ", username, " -- Password : ", password)

        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_username_text(my_driver), username)

        self.utils.print_info("Entering Password...")
        self.auto_actions.send_keys(self.login_web_elements.get_login_page_password_text(), password)

        self.utils.print_info("Clicking on Sign In button")

        self.auto_actions.click(self.login_web_elements.get_login_page_login_button())
        sleep(10)

        return 1

    def logout_a3_user(self):
        """
        - This keyword will Logout from A3 UI
        - Keyword Usage
        - ``Logout A3 User``
        :return: None
        """
        self.utils.print_info("Select the Logout menu ")
        sleep(10)
        self.driver.find_element_by_xpath('//a[contains(text(),"demo@demo.com")]').click()
        sleep(5)
        self.utils.print_info("Select the Logout option")
        sleep(10)
        drop_options = self.driver.find_elements_by_xpath('//ul[@class="dropdown-menu dropdown-menu-right show"]/li')
        self.auto_actions.select_drop_down_options(drop_options, "Log out")
        sleep(5)
        self.utils.print_info("User Logged out successfully")

    def quit_browser(self, _driver=None):
        """
        - Closes all the browser windows and ends the WebDriver session gracefully.
        - if the driver object is passed, quits and returns
        - Keyword Usage:
         - ``Quit Browser``

        :param _driver
        :return: None
        """

        if _driver:
            _driver.quit()
            return 1

        # stop tool tip text capture thread
        try:
            if self.t1.is_alive():
                self.t1.do_run = False
                sleep(10)

            self.driver.quit()
            self.utils.print_info("Resetting cloud driver to -1")
            common.CloudDriver.cloud_driver = -1
            return 1
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            return -1
