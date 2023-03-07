from common.AutoActions import *
from a3.elements.ActiveDirectoryWebElements import ActiveDirectoryWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *


class ActiveDirectoryWebElementsFlow(ActiveDirectoryWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.ad_web_elements = ActiveDirectoryWebElements()
        self.setting = GlobalSettingWebElements()

    def create_active_directory_domains(self):
        """
            - This keyword select the Active Directory Domains option from the menu Policies and Access Control
              and will configure and create the domain
            - Keyword Usage
             - ``Select Active Directory Domains``

        :return: 1 if domain is created else return -1
        """
        self.utils.print_info("Selecting Active Directory Domains from menu...")

        if self.auto_actions.click_reference(self.get_ad_domains) == 1:
            sleep(2)
            self.utils.print_info("Creating domain ")
            element = self.weh.get_element(self.domain_button)
            self.auto_actions.click(element)
            sleep(5)
            self.utils.print_info("Enter ID")
            element1 = self.weh.get_element(self.identifier_input)
            self.auto_actions.send_keys(element1, "ad154")
            sleep(5)
            self.utils.print_info("Enter workgroup")
            element2 = self.weh.get_element(self.workgroup_input)
            self.auto_actions.send_keys(element2, "amra3")
            sleep(5)
            self.utils.print_info("Enter DNS name")
            element3 = self.weh.get_element(self.dns_name_input)
            self.auto_actions.send_keys(element3, "amra3.local")
            sleep(10)
            self.utils.print_info("Enter AD server IP")
            element4 = self.weh.get_element(self.ad_server_input)
            self.auto_actions.send_keys(element4, "10.234.63.27")
            sleep(10)
            self.utils.print_info("Enter DNS server IP")
            element5 = self.weh.get_element(self.dns_server_input)
            self.auto_actions.send_keys(element5, "10.234.63.27")
            sleep(10)
            element6 = self.weh.get_element(self.create_button)
            self.auto_actions.click(element6)
            sleep(10)
            element7 = self.weh.get_element(self.save_button)
            self.auto_actions.click(element7)
            sleep(10)
            self.utils.print_info("Created Domain successfully")
            return 1
        else:
            self.utils.print_info("Unable to navigate to Active Directory")
            self.screen.save_screen_shot()
            return -1

    def join_domain(self):
        """
            - This keyword will join the domain with inputs like username & password
            - Keyword Usage
             - ``Join Domain``

        :return: 1 if domain joined successfully  else return -1
        """
        self.utils.print_info("Selecting Active Directory Domains from menu...")

        if self.auto_actions.click_reference(self.get_ad_domains) == 1:
            sleep(2)
            self.utils.print_info("Click Join Button ")
            element = self.weh.get_element(self.join_ad)
            self.auto_actions.click(element)
            sleep(5)
            self.utils.print_info("Enter Username")
            element8 = self.weh.get_element(self.join_ad_domain_username)
            self.auto_actions.send_keys(element8, "Administrator")
            sleep(5)
            self.utils.print_info("Enter Password")
            element9 = self.weh.get_element(self.join_ad_domain_password)
            self.auto_actions.send_keys(element9, "Localsetup123")
            sleep(5)
            self.utils.print_info("Click Join Domain ")
            join = self.weh.get_element(self.join_domain_button)
            self.auto_actions.click(join)
            sleep(30)
            self.utils.print_info("Close ")
            close = self.weh.get_element(self.domain_close)
            self.auto_actions.click(close)
            self.utils.print_info("Domain Joined Successfully ")
            return 1
        else:
            self.utils.print_info("Unable to Join Domain")
            self.screen.save_screen_shot()
            return -1


