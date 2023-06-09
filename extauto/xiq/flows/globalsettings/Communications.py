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

    # This method will not be deprecated until the keywords for the entire file have been moved and tested
    @deprecated('Please use the {validate_communications_page} keyword in keywords/gui/banner_top/KeywordsCommunications.py. This method can removed after 8/1/2023')
    def validate_communications_page(self, **kwargs):
        return self.gui_validate_communications_page(**kwargs)

    def gui_validate_communications_page(self, **kwargs):
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
            self.utils.switch_to_iframe(CloudDriver().cloud_driver)
            comm_txt = self.communications_web_elements.get_communications_page_text().text
            sleep(2)
            self.utils.print_info("Communications text: ", comm_txt)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            comm_url = self.communications_web_elements.get_iframe_url()
            sleep(2)
            self.utils.print_info("Communications url: ", comm_url)

        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Unable to get Communications page header. Please check"
            self.common_validation.fault(**kwargs)
            return -1

        if "ExtremeCloud IQ" or "NOTIFICATIONS" in comm_txt:
            kwargs['pass_msg'] = "Communications page found."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Communications page is not displaying. Please check"
            self.common_validation.failed(**kwargs)
            return -2
