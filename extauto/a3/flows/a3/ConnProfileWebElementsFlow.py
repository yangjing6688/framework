
from common.AutoActions import *
from a3.elements.RolesWebElements import RolesWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *


class RolesWebElementsFlow(RolesWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.roles_web_elements = RolesWebElements()
        #self.driver = common.CloudDriver.cloud_driver
        self.setting = GlobalSettingWebElements()

    def create_new_conn_profile(self):
        """
        - This keyword will create the connection profile
        - Keyword Usage
        - ``Create New Conn Profile``
        :return: 1 if connection profile is created successfully else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(5)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            self.driver.find_element_by_xpath("//a[contains(@href,'#/configuration/connection_profiles/new')]").click()
            sleep(5)
            self.utils.print_info("profile name ")
            description = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(description, "802.1X")
            sleep(10)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            self.utils.print_info("Select action 1 for row 1")
            self.driver.find_element_by_xpath('//*[@data-automation-tag="automation-filter,0,type"]//input').click()
            sleep(10)
            self.driver.maximize_window()
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-filter,0,type"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "Connection Type")
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            self.driver.find_element_by_xpath('//*[@data-automation-tag="automation-filter,0,match"]//input').click()
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-filter,0,match"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "Wireless-802.11-EAP")
            sleep(5)
            self.utils.print_info("Click on Add Source")
            add_src_btn = self.weh.get_element(self.add_source)
            self.auto_actions.click(add_src_btn)
            sleep(5)
            self.utils.print_info("Select Source")
            self.driver.find_element_by_xpath('//*[@data-automation-tag="automation-sources,0"]//input').click()
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-sources,0"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "AS154")
            sleep(5)
            self.utils.print_info("Created Connection Profile")
            create_conn_profile = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_conn_profile)
            sleep(5)
            self.utils.print_info("Connection Profile is created successfully")
            return 1
        else:
            self.utils.print_info("Connection Profile is not created")
            return -1
