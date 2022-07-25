
from common.AutoActions import *
from a3.elements.RealmsWebElements import RealmsWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium import webdriver


class RealmsWebElementsFlow(RealmsWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.realms_web_elements = RealmsWebElements()
        #self.driver = common.CloudDriver.cloud_driver
        self.setting = GlobalSettingWebElements()
        self.driver = webdriver.Chrome()

    def create_realm(self):
        """
            - This keyword select the Realms from the menu Policies and Access Control and create a new realm
            - Keyword Usage
             - ``Create Realm``

        :return: 1 if realm created successfully else return -1
        """
        self.utils.print_info("Selecting Realm from menu...")

        if self.auto_actions.click(self.get_realms_ui()) == 1:
            sleep(2)
            self.utils.print_info("Clicking New Realm ")
            element = self.weh.get_element(self.realm_button)
            self.auto_actions.click(element)
            sleep(5)
            element1 = self.weh.get_element(self.realm_input)
            self.auto_actions.send_keys(element1, "a3154")
            sleep(5)
            realm_auth = self.weh.get_element(self.realm_ntlm_auth)
            self.auto_actions.click(realm_auth)
            sleep(5)
            self.utils.print_info("Switch to NTLM Auth and enter the domain")
            realm_domain = self.weh.get_element(self.realm_list)
            self.auto_actions.click(realm_domain)
            drop_options = self.driver.find_elements_by_xpath(
                "//ul[contains (@class,'multiselect__content')]//li/span")
            # search_string = "ad154"
            # for list_item in drop_options:
            #
            #     if search_string in list_item.text:
            #         self.utils.print_info(f"Found the Expected Row Text")
            #         list_item.click()
            #         self.utils.print_info(f"clicked on the selected --  ", search_string)
            #         break
            self.auto_actions.select_drop_down_options(drop_options, "ad154")
            sleep(10)
            element2 = self.weh.get_element(self.create_button)
            self.auto_actions.click(element2)
            sleep(5)
            element3 = self.weh.get_element(self.save_button)
            self.auto_actions.click(element3)
            sleep(5)
            element4 = self.weh.get_element(self.close_button)
            self.auto_actions.click(element4)
            sleep(5)
            self.utils.print_info("Select the radiusd-auth service ")
            sleep(10)
            self.driver.find_element_by_xpath("//button[text()=' radiusd-auth ']").click()
            sleep(5)
            self.utils.print_info("Selected Drop Down")
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath("//ul[@class='dropdown-menu show']//li/a")
            self.auto_actions.select_drop_down_options(drop_options, "Restart")
            sleep(5)
            self.utils.print_info("New Realm created successfully")
            return 1
        else:
            self.utils.print_info("Unable to navigate to Realm")
            self.screen.save_screen_shot()
            return -1