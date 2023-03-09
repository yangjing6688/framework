from time import sleep

from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from a3.elements.NavigatorWebElements import NavigatorWebElements
from a3.elements.GlobalSettingWebElements import GlobalSettingWebElements
from xiq.flows.common.DeviceCommon import DeviceCommon
from a3.flows.a3.CIWebElementsFlow import CIWebElementsFlow
from extauto.common.CommonValidation import CommonValidation


class Navigator(NavigatorWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.a3_web_elements = NavigatorWebElements()
        self.setting = GlobalSettingWebElements()
        self.cloud_integration_flow = CIWebElementsFlow()
        self.common_validation = CommonValidation()

    def navigate_to_configuration_tab(self):
        """
         - This keyword Navigates to Configuration Tab
         - Keyword Usage
          - ``Navigate To Configuration Tab``

        :return: 1 if Navigation Successful to Configuration Tab else return -1
        """
        self.utils.print_info("Selecting Configuration Tab...")
        if self.auto_actions.click_reference(self.get_configuration_tab) == 1:
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
        if self.auto_actions.click_reference(self.get_tools_tab) == 1:
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
        if self.auto_actions.click_reference(self.get_auditing_tab) == 1:
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
        if self.auto_actions.click_reference(self.get_clients_tab) == 1:
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
        if self.auto_actions.click_reference(self.get_policies_access_control) == 1:
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
        if self.auto_actions.click_reference(self.get_system_configuration) == 1:
            sleep(2)
            return 1
        else:
            self.utils.print_info("Unable to Navigate to System Configuration")
            self.screen.save_screen_shot()
            return -1

    def navigate_to_system_configuration(self):
        """
         - This keyword navigates to the system configuration page
         - Keyword Usage
          - ``Navigate To System Configuration``

        :return: 1 if Navigate To System Configuration is  successful else return -1
        """
        self.utils.print_info("Clicking Configuration Tab")
        self.navigate_to_configuration_tab()
        self.utils.print_info("Navigating to the System Configuration Page")
        system_button = self. get_system_configuration_menu_link()
        if system_button:
            self.auto_actions.click(system_button)
        sleep(5)
        return 1

    def navigate_to_cloud_integration_page(self):
        """
         - This keyword navigates to the cloud integration page
         - Keyword Usage
          - ``Navigate To Cloud Integration Page``

        :return: 1 if Navigate To Cloud Integration Page is successful else return -1
        """
        self.utils.print_info("Clicking Configuration Tab")
        self.navigate_to_configuration_tab()
        self.utils.print_info("Navigating to the System Configuration Page")
        system_button = self.get_system_configuration_menu_link()
        if not system_button:
            self.utils.print_info("Unable to navigate to the System Configuration Page")
            return -1
        self.auto_actions.click(system_button)
        sleep(5)
        self.utils.print_info("Navigating to the cloud integration page")
        cloud_integration_button = self.cloud_integration_flow.cloud_web_elements.get_cloud()
        if not cloud_integration_button:
            self.utils.print_info("Unable to navigate to the cloud integration page")
            return -1
        self.auto_actions.click(cloud_integration_button)
        sleep(5)
        return 1

    def navigate_to_license_management_page(self, **kwargs):
        """
         - This keyword navigates to the license management page
         - Keyword Usage
          - ``Navigate To License Management Page``

        :return: 1 if Navigate To License Management Page is successful else return -1
        """
        self.utils.print_info("Navigating to License Management Page")

        self.utils.print_info("Locating menu drop down icon button")
        menu_button = self.get_menu_popup_icon()
        if not menu_button:
            self.utils.print_info("Unable to locate menu drop down icon button")
            return -1
        self.auto_actions.click(menu_button)
        sleep(5)

        self.utils.print_info("Locating management menu popup")
        management_menu_element = self.get_management_menu_popup()
        if not management_menu_element:
            self.utils.print_info("Unable to locate management menu popup")
            return -1
        self.auto_actions.move_to_element(management_menu_element)
        sleep(5)
        self.auto_actions.click(management_menu_element)
        sleep(5)

        kwargs['pass_msg'] = "Successfully able to navigate to license management page"
        self.common_validation.passed(**kwargs)
        return 1
