
from common.AutoActions import *
from a3.elements.AuthSourcesWebElements import AuthSourcesWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium import webdriver



class AuthSourcesWebElementsFlow(AuthSourcesWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.auth_source_web_elements = AuthSourcesWebElements()
        #self.driver = common.CloudDriver.cloud_driver
        self.setting = GlobalSettingWebElements()
        self.driver = webdriver.Chrome()

    def create_auth_source(self):
        """
        - This keyword will define the authentication source and create authentication rules
        - Keyword Usage
        - ``Select Auth Source``
        :return: 1 if auth source is created successfully -1
        """
        if self.auto_actions.click(self.get_auth_source_menu()) == 1:
            sleep(2)
            self.utils.print_info("Select the Internal source & expand the menu ")
            sleep(10)
            b1 = self.weh.get_element(self.auth_source_button)
            b1.click()
            self.utils.print_info("Selected Drop Down")
            sleep(10)
            b2 = self.weh.get_elements(self.auth_source_options)
            sleep(5)
            self.auto_actions.select_drop_down_options(b2, "Active Directory")
            sleep(5)
            self.utils.print_info("Enter Active Directory name")
            name = self.weh.get_element(self.ad_name)
            self.auto_actions.send_keys(name, "AS154")
            sleep(5)
            self.utils.print_info("Enter Description")
            description = self.weh.get_element(self.ad_description)
            self.auto_actions.send_keys(description, "AS154")
            sleep(10)
            self.utils.print_info("Enter Host")
            description.send_keys(Keys.TAB)
            host = self.weh.get_element(self.host_input)
            self.auto_actions.send_keys(host, "10.234.63.27")
            host.send_keys(Keys.ENTER)
            sleep(5)
            self.utils.print_info("Enter Base DN")
            base_dn = self.weh.get_element(self.ad_base_dn)
            self.auto_actions.send_keys(base_dn, "CN=Users,DC=amra3,DC=local")
            sleep(5)
            self.utils.print_info("Enter Bind DN")
            bind_dn = self.weh.get_element(self.ad_bind_dn)
            self.auto_actions.send_keys(bind_dn, "CN=Administrator,CN=Users,DC=amra3,DC=local")
            sleep(5)
            self.utils.print_info("Enter Password")
            password = self.weh.get_element(self.passwd)
            self.auto_actions.send_keys(password, "Aquaman123")
            sleep(5)
            self.utils.print_info("Test Password")
            test_passwd = self.weh.get_element(self.test_pwd)
            self.auto_actions.click(test_passwd)
            sleep(5)
            self.utils.print_info("Add Authentication Rule")
            auth_add_rule = self.weh.get_element(self.ad_auth_add_rule)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            self.utils.print_info("Click on Rule")
            add_rule_unknown = self.weh.get_element(self.auth_add_rule_unknown)
            self.auto_actions.click(add_rule_unknown)
            sleep(10)
            self.utils.print_info("Enter Rule Name")
            rule_name = self.weh.get_element(self.add_rule_name)
            self.auto_actions.send_keys(rule_name, "rule1")
            sleep(10)
            self.utils.print_info("Click on Add Action")
            action_button = self.weh.get_element(self.add_action)
            self.auto_actions.click(action_button)
            sleep(5)
            self.utils.print_info("Select action 1 for row 1")
            auth_rule1_act1 = self.weh.get_elements(self.add_rule_row1_act1)
            self.utils.print_info(auth_rule1_act1)
            option = self.weh.get_element(self.rule_row1_select_option)
            self.auto_actions.click(option)
            #
            # drop_options = self.driver.find_elements_by_xpath(
            #      '//*[@data-automation-tag="automation-authentication_rules,0,actions,0,type"]//ul')
            #     #self.driver.find_elements_by_xpath(
            #      #'.//*[@data-automation-tag="automation-authentication_rules,0,actions,0,type"]//ul/li')
            # self.utils.print_info("Print the drop options ", drop_options)
            # self.auto_actions.select_drop_down_options(drop_options, "Role")
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            auth_rule1_act2 = self.weh.get_elements(self.add_rule_row1_act2)
            # self.driver.find_element_by_xpath(
            #     '//*[@data-automation-tag="automation-authentication_rules,0,actions,0,value"]//input').click()
            drop_options = self.driver.find_elements_by_xpath(
                 '//*[@data-automation-tag="automation-authentication_rules,0,actions,0,value"]//span/span')
            self.auto_actions.select_drop_down_options(drop_options, "roleE")
            self.utils.print_info("Add another row")
            new_row = self.weh.get_element(self.add_row)
            self.auto_actions.click(new_row)
            sleep(10)
            self.utils.print_info("Select action 1 for row 2")
            self.driver.find_element_by_xpath(
                '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,type"]//input').click()
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,type"]//span/span')
            self.auto_actions.select_drop_down_options(drop_options, "Access Duration")
            sleep(10)
            self.utils.print_info("Select action 2 for row 2")
            self.driver.find_element_by_xpath(
                '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,value"]//input').click()
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,value"]//span/span')
            self.auto_actions.select_drop_down_options(drop_options, "5 days")
            sleep(10)
            create_ad = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_ad)
            sleep(5)
            self.utils.print_info("Auth Source is created successfully")
            sleep(5)
            return 1
        else:
            self.utils.print_info("Auth Source is Not created ")
            return -1
