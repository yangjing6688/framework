import re
from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from robot.libraries.BuiltIn import BuiltIn
from xiq.flows.common.Navigator import Navigator
from xiq.elements.NavigatorWebElements import NavigatorWebElements
from xiq.elements.CommunicationsWebElements import CommunicationsWebElements
import common.CloudDriver


class Communications(CommunicationsWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = NavigatorWebElements()
        self.screen = Screen()
        self.navigate = Navigator()
        self.builtin = BuiltIn()
        self.driver = common.CloudDriver.cloud_driver

    def validate_communications_page(self):
        """
        - This Keyword Navigate to communications menu in Global settings page
        - Keyword Usage
          - ``Validate Communications Page``

        :return: 1 if Validation is Successful to Communications Page
        """
        self.utils.print_info("Navigate to Global Settings-->Communications page")
        self.navigate.navigate_to_communications_page()
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe(self.driver)
            comm_txt = self.get_communications_page_text().text
            sleep(2)
            self.utils.print_info("Communications text: ", comm_txt)
            self.utils.switch_to_default(self.driver)
            comm_url = self.get_iframe_url()
            sleep(2)
            self.utils.print_info("Communications url: ", comm_url)

        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to get Communications page header. Please check")
            return -1

        if "ExtremeCloud IQ" in comm_txt:
            self.utils.print_info("Communications page found.")
            return 1
        else:
            self.utils.print_info("Communications page is not displaying. Please check")
            return -2

    def validate_notifications_page(self):
        """
        - This Keyword Navigate to notifications page from communications page
        - Keyword Usage
          - ``Navigate To Notifications Page``

        :return: 1 if Navigation is Successful to notification page
        """

        self.utils.print_info("Selecting notifications menu on communications page..")
        self.auto_actions.click(self.get_notifications_nav())
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe_n(self.driver, 1)
            sleep(2)
            notification_txt = self.get_notifications_page_text().text
            sleep(5)
            self.utils.print_info("Notifications page header: ", notification_txt)
            self.utils.switch_to_default(self.driver)
            sleep(2)

        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to get Communications page header. Please check")
            return -1

        if "NOTIFICATION" in notification_txt:
            self.utils.print_info("Communications page found.")
            return 1
        else:
            self.utils.print_info("Notification page is not displaying. Please check Communications pages.")
            return -2

    def validate_preview_page(self):
        """
        - This Keyword Navigate to preview page in communications
        - Keyword Usage
          - ``Navigate To preview Page``
        :return: 1 if Navigation Successful to Preview Page
        """
        self.utils.print_info("Selecting preview menu on Communications page...")
        self.auto_actions.click(self.get_preview_nav())
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe_n(self.driver, 2)
            sleep(2)
            preview_txt = self.get_previews_page_text().text
            sleep(5)
            self.utils.print_info("Preview page header: ", preview_txt)
            self.utils.switch_to_default(self.driver)
            sleep(2)
        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to get Communications page header. Please check")
            return -1

        if "PREVIEW" in preview_txt:
            self.utils.print_info("Communications pages found.")
            return 1
        else:
            self.utils.print_info("Preview page is not displaying. Please check Communications pages.")
            return -2

    def validate_new_in_extremecloud_page(self):
        """
        - This Keyword Navigate to New in ExtremeCLoud IQ
        - Keyword Usage
          - ``Navigate To New In Extremecloud Page``

        :return: 1 if Navigation Successful to New in XIQ
        """

        self.utils.print_info("Selecting new in Extremecloud menu on Communications page..")
        self.auto_actions.click(self.get_new_updates_nav())
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe_n(self.driver, 2)
            sleep(2)
            new_comm_txt = self.get_new_in_extremecloud_page_text().text
            sleep(5)
            self.utils.print_info("New in XIQ Page header: ", new_comm_txt)
            self.utils.switch_to_default(self.driver)
            sleep(2)
        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to get Communications page header. Please check")
            return -1

        if "New In ExtremeCloud IQ" in new_comm_txt:
            self.utils.print_info("Communications pages found.")
            return 1
        else:
            self.utils.print_info("New in XIQ page is not displaying. Please check Communications pages.")
            return -2

