import re
from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.ClientModeWebElements import ClientModeWebElements
import extauto.common.CloudDriver as CDr


class ClientMode:
    def __init__(self):
        self.utils = None
        self.driver = None
        self.screen = None
        self.auto_actions = None
        self.ClientModeWebElements = None

    def _init(self, url="default", incognito_mode="False"):
        """
        This method initializes the driver object and makes it global
        :param url: if not default, will be read from the ${TEST_URL} variable
        :return: returns driver object
        """
        self.utils = Utils()
        if CDr.cloud_driver == -1:
            self.utils.print_info("Creating new cloud driver")
            if CDr.load_browser(url, program='clientmode', incognito_mode=incognito_mode) == -2:
                assert False, "Selenium host/node  is not responding. Possible issues can be:" \
                              "Browser & webdriver versions mismatch or selenium standalone server stopped."
            self.window_index = 0
        else:
            self.utils.print_info("Cloud driver already exists - opening new window using same driver")
            self.window_index = CDr.open_window(url)
        self.utils.print_info(f"Window Handle Index is {self.window_index}")
        self.driver = CDr.cloud_driver
        self.ClientModeWebElements = ClientModeWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def login_user_client_mode(self, username, password, **kwargs):
        """
        - Login to client mode account with username and password
        - keyword Usage:
         - ``Client Mode Login User   ${USERNAME}   ${PASSWORD}``
        :param username: login account username
        :param password: login account password
        """

        self._init()
        browser = BuiltIn().get_variable_value("${BROWSER}")
        self.utils.print_info("Browser: ", browser)
        try:
            self.utils.print_info("Version: ", self.driver.capabilities['version'])
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info("Version: ", self.driver.capabilities['browserVersion'])

        try:
            self.utils.print_info("Logging with Username : ", username, " -- Password : ", password)
            self.utils.print_info("Entering Username...")
            self.auto_actions.send_keys(self.ClientModeWebElements.get_login_page_username_text(), username)
            self.utils.print_info("Entering Password...")
            self.auto_actions.send_keys(self.ClientModeWebElements.get_login_page_password_text(), password)
            self.screen.save_screen_shot()
            self.utils.print_info("Clicking on Login button")
            self.auto_actions.click(self.ClientModeWebElements.get_login_page_login_button())
            sleep(5)
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info( e + "\nCan not login user client mode.")
            return -1
        return 1

    def quit_browser_client_mode(self, _driver=None):
        """
        - Closes all the browser windows and ends the WebDriver session gracefully.
        - if the driver object is passed, quits and returns
        - Keyword Usage:
         - ``Quit Browser Client Mode``

        :param _driver
        :return: 1 if success
        """
        if _driver:
            _driver.quit()
            return 1

        try:
            self.driver.quit()
            self.utils.print_info("Resetting cloud driver to -1")
            extauto.common.CloudDriver.cloud_driver = -1
            return 1
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            return -1

    def navigator_client_mode_ssid(self):
        self.utils.print_info("Click Client Mode SSID tab")
        self.auto_actions.click(self.ClientModeWebElements.get_admin_page_client_mode_ssid_tab())
        self.ClientModeWebElements.get_wifi_connection_status()
        self.screen.save_screen_shot()

    def manual_passphrase_ssid_connect(self, ssid, password='aerohive', security='WPA2'):
        wifi_status = None
        self.utils.print_info("Click other SSIDs button.")
        self.auto_actions.click(self.ClientModeWebElements.get_other_ssids_button())
        self.utils.print_info("Input ssid.")
        self.auto_actions.send_keys(self.ClientModeWebElements.get_ssid_textbox(), ssid)
        self.utils.print_info("Select security type.")
        self.auto_actions.click(self.ClientModeWebElements.get_security_type_dropbox(security))
        self.utils.print_info("Input Password.")
        self.auto_actions.send_keys(self.ClientModeWebElements.get_password_textbox(), password)
        self.screen.save_screen_shot()
        self.utils.print_info("Click connect button.")
        self.auto_actions.click(self.ClientModeWebElements.get_connect_button())
        for i in range(1, 30):
            sleep(5)
            wifi_status = self.ClientModeWebElements.get_wifi_connection_status().text
            self.utils.print_info('Read Wifi Status: ' + str(i) + ' -- ' + wifi_status)
            if 'connected:' in wifi_status:
                x = re.search(r'[0-9]+(?:\.[0-9]+){3}', wifi_status)
                self.screen.save_screen_shot()
                return [1, x.group()]
            elif 'disconnected' in wifi_status:
                break
        self.screen.save_screen_shot()
        return [-1, wifi_status]





if __name__ == '__main__':
    cm = ClientMode()
    cm.login_user_client_mode('admin', 'Aerohive123')