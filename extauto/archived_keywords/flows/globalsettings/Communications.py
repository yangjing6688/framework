""" This file contains code for keywords that have been archived.
    If the keywords need to be available again copy the code to xiq/flows/globalsettings/Communications.py
    and implement the keyword move process.
    Instructions for moving a keyword can be found here:
    https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords """

from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from robot.libraries.BuiltIn import BuiltIn
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.xiq.elements.CommunicationsWebElements import CommunicationsWebElements
from extauto.common.CloudDriver import CloudDriver
from extauto.common.CommonValidation import CommonValidation
from ExtremeAutomation.Utilities.deprecated import deprecated
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class Communications(object, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = NavigatorWebElements()
        self.screen = Screen()
        self.navigate = Navigator()
        self.builtin = BuiltIn()
        self.common_validation = CommonValidation()
        self.communications_web_elements = CommunicationsWebElements()

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def validate_notifications_page(self, **kwargs):
        """
        - This Keyword Navigate to notifications page from communications page
        - Keyword Usage
        - ``Navigate To Notifications Page``

        :return: 1 if Navigation is Successful to notification page
        """

        self.utils.print_info("Selecting notifications menu on communications page..")
        self.auto_actions.click_reference(self.get_notifications_nav)
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe_n(CloudDriver().cloud_driver, 1)
            sleep(2)
            notification_txt = self.communications_web_elements.get_notifications_page_text().text
            sleep(5)
            self.utils.print_info("Notifications page header: ", notification_txt)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            sleep(2)

        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Unable to get Communications page header. Please check"
            self.common_validation.fault(**kwargs)
            return -1

        if "NOTIFICATION" in notification_txt:
            kwargs['pass_msg'] = "Communications page found."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Notification page is not displaying. Please check Communications pages."
            self.common_validation.failed(**kwargs)
            return -2

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def validate_preview_page(self, **kwargs):
        """
        - This Keyword Navigate to preview page in communications
        - Keyword Usage
        - ``Navigate To preview Page``

        :return: 1 if Navigation Successful to Preview Page
        """
        self.utils.print_info("Selecting preview menu on Communications page...")
        self.auto_actions.click_reference(self.get_preview_nav)
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe_n(CloudDriver().cloud_driver, 2)
            sleep(2)
            preview_txt = self.communications_web_elements.get_previews_page_text().text
            sleep(5)
            self.utils.print_info("Preview page header: ", preview_txt)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            sleep(2)
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Unable to get Communications page header. Please check"
            self.common_validation.fault(**kwargs)
            return -1

        if "PREVIEW" in preview_txt:
            kwargs['pass_msg'] = "Communications page found."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Notification page is not displaying. Please check Communications pages."
            self.common_validation.failed(**kwargs)
            return -2

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def validate_new_in_extremecloud_page(self, **kwargs):
        """
        - This Keyword Navigate to New in ExtremeCLoud IQ
        - Keyword Usage
        - ``Navigate To New In Extremecloud Page``

        :return: 1 if Navigation Successful to New in XIQ
        """

        self.utils.print_info("Selecting new in Extremecloud menu on Communications page..")
        self.auto_actions.click_reference(self.get_new_updates_nav)
        sleep(5)

        try:
            self.utils.print_info("Switching to iframe and reading page header...")
            self.utils.switch_to_iframe_n(CloudDriver().cloud_driver, 2)
            sleep(2)
            new_comm_txt = self.communications_web_elements.get_new_in_extremecloud_page_text().text
            sleep(5)
            self.utils.print_info("New in XIQ Page header: ", new_comm_txt)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            sleep(2)
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Unable to get Communications page header. Please check"
            self.common_validation.fault(**kwargs)
            return -1

        if "New In ExtremeCloud IQ" in new_comm_txt:
            kwargs['pass_msg'] = "Communications page found."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "New in XIQ page is not displaying. Please check Communications pages.."
            self.common_validation.failed(**kwargs)
            return -2
