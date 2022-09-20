from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import *
from a3.elements.CIWebElements import CIWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium import webdriver
from extauto.common.CommonValidation import CommonValidation


class CIWebElementsFlow(CIWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.cloud_web_elements = CIWebElements()
        self.driver = webdriver.Chrome()
        self.common_validation = CommonValidation()

    def select_cloud_integration(self, cloud_url, cloud_uname, cloud_pwd):
        """
            - This keyword select the Cloud Integration from the menu System Configuration ank link it to XIQ
            - Keyword Usage
             - ``Select cloud integration``

        :return: 1 if Navigation Successful to Cloud Integration else return -1
        """
        self.utils.print_info("Selecting Cloud Integration from menu...")

        if self.auto_actions.click(self.get_cloud()) == 1:
            sleep(2)
            self.utils.print_info("Entering Cloud account details ")
            element1 = self.weh.get_element(self.cloud_host_input)
            element1.clear()
            self.auto_actions.send_keys(element1, cloud_url)
            sleep(5)
            element2 = self.weh.get_element(self.cloud_admin)
            self.auto_actions.send_keys(element2, cloud_uname)
            sleep(5)
            element3 = self.weh.get_element(self.cloud_password)
            self.auto_actions.send_keys(element3, cloud_pwd)
            sleep(10)
            element4 = self.weh.get_element(self.cloud_link_button)
            self.auto_actions.click(element4)
            sleep(20)
            self.driver.get(self.driver.current_url)
            sleep(3)
            self.driver.refresh()
            sleep(15)
            self.utils.print_info("Unlinking from cloud ")
            element5 = self.weh.get_element(self.cloud_unlink_button)
            self.auto_actions.click(element5)
            sleep(10)
            self.utils.print_info("XIQ cloud linking & Unlinking is successfully done")
            sleep(5)
            return 1
        else:
            self.utils.print_info("Unable to perform Linking & unlinking to XIQ")
            self.screen.save_screen_shot()
            return -1

    def a3_link_with_extreme_cloud_iq_account(self, cloud_url, cloud_uname, cloud_pwd, **kwargs):
        """
            - This keyword link with Extreme Cloud IQ Account
            - Keyword Usage
             - ``A3 Link With Extreme Cloud Iq Account``

        :return: 1 if able to successfully link to extreme iq account else return -1
        """
        self.utils.print_info("Configuring Cloud Integration options")

        self.utils.print_info("Setting Cloud Host value to " + cloud_url)
        cloud_url_element = self.cloud_host()
        if not cloud_url_element:
            kwargs['fail_msg'] = "Unable to locate Cloud Host Web Element"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        self.auto_actions.send_keys(cloud_url_element, cloud_url)

        self.utils.print_info("Setting Cloud Admin value to " + cloud_uname)
        cloud_admin_element = self.get_cloud_admin()
        if not cloud_admin_element:
            kwargs['fail_msg'] = "Unable to locate Cloud Admin Web Element"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        self.auto_actions.send_keys(cloud_admin_element, cloud_uname)

        self.utils.print_info("Setting Password value to " + cloud_pwd)
        cloud_password_element = self.get_cloud_password()
        if not cloud_password_element:
            kwargs['fail_msg'] = "Unable to locate Cloud Password Web Element"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        self.auto_actions.send_keys(cloud_password_element, cloud_pwd)

        self.utils.print_info("Clicking Link with Extreme Cloud IQ Account button")
        link_to_button = self.get_cloud_link_button()
        if not link_to_button:
            kwargs['fail_msg'] = "Unable to locate Link with Extreme Cloud IQ Account button"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        self.auto_actions.click(link_to_button)

        kwargs['pass_msg'] = "Successfully configured Cloud Integration options"
        self.common_validation.passed(**kwargs)
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        return 1
