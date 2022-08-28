from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import *
from a3.elements.CIWebElements import CIWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium import webdriver


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

