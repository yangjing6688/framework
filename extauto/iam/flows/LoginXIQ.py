import threading
from time import sleep

from robot.libraries.BuiltIn import BuiltIn

from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.common.WebElementHandler import WebElementHandler
from extauto.common.WebElementController import WebElementController


import extauto.xiq.flows.common.ToolTipCapture
import extauto.xiq.flows.common.Navigator

from extauto.iam.elements.IAMWebElements import IAMWebElements

class LoginXIQ:

    def __init__(self):
        self.common_validation = CommonValidation()
        self.t1 = None
        self.utils = Utils()
        self.login_web_elements = IAMWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.driver = CloudDriver().cloud_driver
        self.web = WebElementHandler()
        self.web_element_controller = WebElementController()

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


    def login_xiq_by_sso(self, username, password, orgname, url="default", max_retries=3,**kwargs):
        """
        - Login to Xiq account by sso process (we will try up to 3 times)
        - By default url will load from the topology file
        - keyword Usage:
        - ``Login xiq By SSO   ${USERNAME}   ${PASSWORD}    ${OrgName}``

        Supported Modes:
            UI - default mode

        :param username: login account username that stored in ADFS
        :param password: login account password that stored in ADFS
        :param orgname: XIQ account who created the IDP configuration
        :param url: login url
        :param max_retries: the max retry times
        :param (**kwarg) expect_error: the keyword is expected to fail
        :return: 1 if login successful else -1
        """
        count = 0
        expect_error = self.common_validation.get_kwarg_bool(kwargs, "expect_error", False)
        result = self._login_xiq_by_sso(username, password, orgname,url, **kwargs)

        # Let's try again if we don't expect an error and the results were not good
        if not expect_error:
            while result != 1 and count < max_retries:
                self.utils.print_warning(f'Trying to log in again: {count} of {max_retries}')
                result = self._login_xiq_by_sso(username, password, orgname,url, **kwargs)
                count = count + 1
        if result != 1:
            kwargs['fail_msg'] = "'login_user()' -> Login was not successful"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Login was successful"
            self.common_validation.passed(**kwargs)
        return result

    def _login_xiq_by_sso(self, username, password, orgname, url="default", incognito_mode="False", **kwargs):
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
        if 'sso' in url:
            self.screen.save_screen_shot()
            self.utils.print_info("Click SSO button...")
            self.auto_actions.click_reference(self.login_web_elements.get_login_page_sso_button)
            sleep(3)
            self.utils.print_info("Entering Username...")
            self.auto_actions.send_keys(self.login_web_elements.get_saml_login_page_username_text(), username)
            self.utils.print_info("Click continue button...")
            self.auto_actions.click_reference(self.login_web_elements.get_saml_login_page_continue_button)
            sleep(3)
            if self.check_mutiple_idp_configured_same_domain() == 1:
                self.utils.print_info("Choose the username" + username)
                self.auto_actions.click(self.login_web_elements.get_saml_login_page_idp_server_item(username))
            self.utils.print_info("Entering Username")
            self.auto_actions.send_keys(self.login_web_elements.get_adfs_page_username_text(), username)
            self.auto_actions.send_keys(self.login_web_elements.get_adfs_page_password_text(), password)
            self.auto_actions.click_reference(self.login_web_elements.get_adfs_page_submit_button)
            sleep(2)
            self.screen.save_screen_shot()
            user = username.split('@')[0]
            for i in range(30):
                check_username = self.login_web_elements.get_xiq_page_account_orgname_title(user)
                check_orgname = self.login_web_elements.get_xiq_page_account_orgname_title(orgname)
                if check_username and check_orgname:
                    kwargs['pass_msg'] = "Login successful"
                    self.common_validation.passed(**kwargs)
                    return 1
                sleep(2)

            kwargs['pass_msg'] = "Login Failed or there is something wrong with the accout"
            self.common_validation.fault(**kwargs)
            return -1


    def gui_logout_user(self, **kwargs):
        """
        - Logout the current user
        - Keyword Usage:
        - ``Logout User``
        :return: 1 if logout success, -1 if logout not successful
        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ONLY=True (Will only support XAPI keywords in your test)
        :return: 1 if logout success
        """

        # stop tool tip text capture thread
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        if self.t1:
            try:
                if self.t1.is_alive():
                    self.t1.do_run = False
                    # t1 is a thread used to check for messages on the webpage.  It loops every second.  Wait 2
                    # seconds to give it time to shutdown
                    sleep(2)
            except Exception:
                print("t1.do_run not initialized")

        try:
            self.utils.print_info("Clicking on Logout Menu")
            self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
            self.auto_actions.click_reference(self.login_web_elements.get_logout_link)
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            kwargs['fail_msg'] = f"Error: {e}"
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

    def check_mutiple_idp_configured_same_domain(self, **kwargs):
        """
        - This can be used in saml account selection page,for example, xiq account1 has created an IDP with domain dev.com and account2 has created an IDP with domain dev.com,too.
          After clicking sso button and input email,the page will redirect to saml account selection page and the page will list the name of account1 and account2.If there is only
          one account with domain dev.com,after clicking sso button and input email,the page will redirect to ADFS login page. This keyword is to check whether the account selection
          page is shown.
        - Keyword Usage
        - ``if self.check_mutiple_idp_configured_same_domain() == 1:
            return 1``
        :return: returns 1 if the saml account selection page is exist else -1
        """
        self.utils.print_info("Check if the page redirect to account selection...")
        element = self.login_web_elements.get_saml_login_page_selecting_your_organization_title()
        if not element:
            kwargs['no_msg'] = "There is no mutiple idp with the same domain"
            self.common_validation.passed(**kwargs)
            return -1
        return 1

