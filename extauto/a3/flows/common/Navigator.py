from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions

from common.AutoActions import *
from a3.elements.NavigatorWebElements import NavigatorWebElements
from a3.elements.GlobalSettingWebElements import *
from a3.defs.GlobalSettingWebElementDefinitions import GlobalSettingWebElementDefinitions
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Navigator(NavigatorWebElements):
    def __init__(self):
        super().__init__()
        # self.CloudDriver = CloudDriver()
        # self.driver2 = None
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.a3_web_elements = NavigatorWebElements()
        #self.driver = common.CloudDriver.cloud_driver
        self.setting = GlobalSettingWebElements()

    def navigate_to_configuration_tab(self):
        """
         - This keyword Navigates to Configuration Tab
         - Keyword Usage
          - ``Navigate To Configuration Tab``

        :return: 1 if Navigation Successful to Configuration Tab else return -1
        """
        self.utils.print_info("Selecting Configuration Tab...")
        if self.auto_actions.click(self.get_configuration_tab()) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Configuration tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_tools_tab(self):
        """
         - This keyword Navigates to Tools Tab
         - Keyword Usage
          - ``Navigate To Tools Tab``

        :return: 1 if Navigation Successful to Tools Tab else return -1
        """
        self.utils.print_info("Selecting Tools Tab...")
        if self.auto_actions.click(self.get_tools_tab()) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Tools tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_auditing_tab(self):
        """
         - This keyword Navigates to Auditing Tab
         - Keyword Usage
          - ``Navigate To Auditing Tab``

        :return: 1 if Navigation Successful to Auditing Tab else return -1
        """
        self.utils.print_info("Selecting Auditing Tab...")
        if self.auto_actions.click(self.get_auditing_tab()) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Auditing tab")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_a3_clients_tab(self):
        """
         - This keyword Navigates to Clients Tab
         - Keyword Usage
          - ``Navigate To Clients Tab``

        :return: 1 if Navigation Successful to Clients Tab else return -1
        """
        self.utils.print_info("Selecting Clients Tab...")
        if self.auto_actions.click(self.get_clients_tab()) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Clients tab")
            self.screen.save_screen_shot()
            return -1

    def switch_policies_access_control(self):
        """
         - This keyword switches to Policies & Access Control and expand the menu
         - Keyword Usage
          - ``Switch To Policies Access Control``

        :return: 1 if Navigation Successful to Policies & Access Control else return -1
        """
        self.utils.print_info("Selecting Policies Access Control Tab...")
        if self.auto_actions.click(self.get_policies_access_control()) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to navigate to Policies & Access control")
            self.screen.save_screen_shot()
            return -1

    def switch_system_configuration(self):
        """
         - This keyword switches to System Configuration Page
         - Keyword Usage
          - ``Switch To System Configuration Page``

        :return: 1 if Navigation Successful to System Configuration else return -1
        """
        self.utils.print_info("Selecting System Configuration...")
        if self.auto_actions.click(self.get_system_configuration()) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to Navigate to System Configuration")
            self.screen.save_screen_shot()
            return -1