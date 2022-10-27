import re
from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.elements.ClientModeWebElements import ClientModeWebElements


class ClientMode:
    def __init__(self):
        self.utils = Utils()
        self.ClientModeWebElements = ClientModeWebElements()
        self.common_validation = CommonValidation()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def _init(self, url="default", incognito_mode="False"):
        """
        This method initializes the driver object and makes it global
        :param url: if not default, will be read from the ${TEST_URL} variable
        :return: returns driver object
        """
        if CloudDriver().cloud_driver == None:
            self.utils.print_info("Creating new cloud driver")
            CloudDriver().start_browser(url=url, program="clientmode", incognito_mode=incognito_mode)
        else:
            self.utils.print_info("Cloud driver already exists - opening new window using same driver")
            self.window_index = CloudDriver().open_window(url)

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
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['version'])
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info("Version: ", CloudDriver().cloud_driver.capabilities['browserVersion'])

        try:
            self.utils.print_info("Logging with Username : ", username, " -- Password : ", password)
            self.utils.print_info("Entering Username...")
            self.auto_actions.send_keys(self.ClientModeWebElements.get_login_page_username_text(), username)
            self.utils.print_info("Entering Password...")
            self.auto_actions.send_keys(self.ClientModeWebElements.get_login_page_password_text(), password)
            self.screen.save_screen_shot()
            self.utils.print_info("Clicking on Login button")
            self.auto_actions.click_reference(self.ClientModeWebElements.get_login_page_login_button)
            sleep(5)
        except Exception as e:
            self.utils.print_debug(e)
            self.utils.print_info( e + "\nCan not login user client mode.")
            kwargs['fail_msg'] = "No Auto Provision Policy is present"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def quit_browser_client_mode(self, _driver=None, **kwargs):
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
            CloudDriver().close_browser()
            self.utils.print_info("Resetting cloud driver to -1")
            return 1
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            kwargs['fail_msg'] = f"Error: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def navigator_client_mode_ssid(self):
        self.utils.print_info("Click Client Mode SSID tab")
        self.auto_actions.click_reference(self.ClientModeWebElements.get_admin_page_client_mode_ssid_tab)
        self.ClientModeWebElements.get_wifi_connection_status()
        self.screen.save_screen_shot()

    def manual_passphrase_ssid_connect(self, ssid, password='aerohive', security='WPA2'):
        disconnect = 0
        wifi_status = None
        self.utils.print_info("Click other SSIDs button.")
        self.auto_actions.click_reference(self.ClientModeWebElements.get_other_ssids_button)
        self.utils.print_info("Input ssid.")
        self.auto_actions.send_keys(self.ClientModeWebElements.get_ssid_textbox(), ssid)
        self.utils.print_info("Select security type.")
        self.auto_actions.click(self.ClientModeWebElements.get_security_type_dropbox(security))
        self.utils.print_info("Input Password.")
        self.auto_actions.send_keys(self.ClientModeWebElements.get_password_textbox(), password)
        self.screen.save_screen_shot()
        self.utils.print_info("Click connect button.")
        self.auto_actions.click_reference(self.ClientModeWebElements.get_connect_button)
        for i in range(1, 30):
            sleep(5)
            wifi_status = self.ClientModeWebElements.get_wifi_connection_status().text
            self.utils.print_info('Read Wifi Status: ' + str(i) + ' -- ' + wifi_status)
            if 'connected:' in wifi_status:
                x = re.search(r'[0-9]+(?:\.[0-9]+){3}', wifi_status)
                self.screen.save_screen_shot()
                return [1, x.group()]
            elif 'disconnected' in wifi_status:
                disconnect += 1
            elif disconnect == 20:
                break
        self.screen.save_screen_shot()
        kwargs['fail_msg'] = f"Status: disconnected -> {wifi_status}"
        self.common_validation.failed(**kwargs)
        return [-1, wifi_status]

