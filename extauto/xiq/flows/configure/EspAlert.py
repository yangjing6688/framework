from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.EspAlertWebElements import EspAlertWebElements
import re


class EspAlert(EspAlertWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
    def enable_esp_alert(self,url):
        """
        - Keyword Usage:
         - ``Enable Esp Alert   ${URL}``

        :param url: url to load for enabling esp alert on cloud UI
        :return: 1 if loaded the url successfully
        """
        self.utils.print_info("Refresh Page")
        CloudDriver().cloud_driver.get(url)
        CloudDriver().cloud_driver.refresh()
        sleep(5)
        return 1
    def go_to_policy_and_check_tab(self,configred_title,not_configured_title):
        """
        - Go to policy page and check configured policies and not configured policies tab"
        - Keyword Usage
         - ``Go To Policy And Check Tab  ${configred_title}  ${not_configured_title}``
        :return: returns 1 if successfully show configred policies and not configured policies tab else -1
        """
        self.utils.print_info("Navigating to Alert menu..")
        self.navigator.navigate_configure_alert()

        sleep(5)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.click(self.get_go_to_policy())
        self.utils.print_info("Going to Policy page")
        sleep(2)
        self.screen.save_screen_shot()
        self.utils.print_info("Confired tab title")
        configured_tab_title = self.get_configred_tab_txt().text
        self.utils.print_info(configured_tab_title)

        self.utils.print_info("Not Confired tab title")
        not_configured_tab_title = self.get_not_configred_tab_txt().text
        self.utils.print_info(not_configured_tab_title)

        if configured_tab_title == configred_title and not_configured_tab_title == not_configured_title:
            return 1
        else:
            return -1