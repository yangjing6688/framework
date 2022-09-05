from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions

from common.AutoActions import *
from a3.elements.A3WebElements import A3WebElements
from a3.elements.GlobalSettingWebElements import *
from a3.defs.GlobalSettingWebElementDefinitions import GlobalSettingWebElementDefinitions
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class A3WebElementsflow(A3WebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.a3_web_elements = A3WebElements()
        self.setting = GlobalSettingWebElements()

    def select_auth_source(self):
        """
        - This keyword will enter the values into SSH page tools
        - Keyword Usage
        - ``SSH Page Inputs``
        :return: 1 if Navigation Successful to SSH inputs else return -1
        """
        if self.auto_actions.click(self.select_auth_source_menu()) == 1:
            sleep(2)
            self.utils.print_info("Select the Internal source & expand the menu ")
            sleep(10)
            self.driver.find_element_by_xpath("//button[text()='New Internal Source']").click()
            sleep(5)
            self.utils.print_info("Selected Drop Down")
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath("//ul[@class='dropdown-menu show']//li/a")
            self.auto_actions.select_drop_down_options(drop_options,"Active Directory")
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            name = self.weh.get_element(self.ad_name)
            name.clear()
            self.auto_actions.send_keys(name,"AD174")
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            description = self.weh.get_element(self.ad_description)
            description.clear()
            self.auto_actions.send_keys(description,"AD174")
            sleep(10)
            self.utils.print_info("Selected Active Directory")
            sleep(15)
            host = self.driver.find_element_by_xpath("//*[@data-automation-tag='automation-host']")
            wait = WebDriverWait(self.driver, 17)
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-automation-tag='automation-host']")))
            self.auto_actions.send_keys(host, "10.234.63.27")
            self.auto_actions.send_enter(host)
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            base_dn = self.weh.get_element(self.ad_base_dn)
            base_dn.clear()
            self.auto_actions.send_keys(base_dn,"CN=Users,DC=amra3,DC=local")
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            bind_dn = self.weh.get_element(self.ad_bind_dn)
            bind_dn.clear()
            self.auto_actions.send_keys(bind_dn,"CN=Administrator,CN=Users,DC=amra3,DC=local")
            sleep(5)
            password = self.weh.get_element(self.passwd)
            self.auto_actions.send_keys(password,"Localsetup123")
            sleep(5)
            test_passwd = self.weh.get_element(self.test_pwd)
            self.auto_actions.click(test_passwd)
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            auth_add_rule = self.weh.get_element(self.ad_auth_add_rule)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            add_rule_unknown = self.weh.get_element(self.auth_add_rule_unknown)
            self.auto_actions.click(add_rule_unknown)
            sleep(10)
            rule_name = self.weh.get_element(self.add_rule_name)
            self.auto_actions.send_keys(rule_name,"rule1")
            sleep(10)
            self.utils.print_info("Click on Add Action")
            action_button = self.weh.get_element(self.add_action)
            self.auto_actions.click(action_button)
            sleep(5)
            self.utils.print_info("Select action 1 for row 1")
            row1_act1 = self.weh.get_elements(self.add_rule_row1_act1)
            self.auto_actions.select_drop_down_options(row1_act1,"Role")
            sleep(10)
            self.utils.print_info("Select action 2 for row 2")
            row1_act2 = self.weh.get_elements(self.add_rule_row1_act2)
            self.auto_actions.select_drop_down_options(row1_act2,"testrole")
            sleep(10)
            self.utils.print_info("Add another row")
            new_row = self.weh.get_element(self.add_row)
            self.auto_actions.click(new_row)
            sleep(10)
            self.utils.print_info("Select action 1 for row 2")
            row2_act1 = self.weh.get_elements(self.add_rule_row2_act1)
            self.auto_actions.select_drop_down_options(row2_act1,"Role")
            sleep(10)
            self.utils.print_info("Select action 2 for row 2")
            row2_act2 = self.weh.get_elements(self.add_rule_row2_act2)
            self.auto_actions.select_drop_down_options(row2_act2,"testrole")
            sleep(10)
            create_ad = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_ad)
            sleep(5)
            return 1
        else:
            return -1


    def create_new_conn_profile(self):
        """
        - This keyword will enter the values into SSH page tools
        - Keyword Usage
        - ``SSH Page Inputs``
        :return: 1 if Navigation Successful to SSH inputs else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(2)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            self.driver.find_element_by_xpath("//a[contains(@href,'#/configuration/connection_profiles/new')]").click()
            sleep(5)
            self.utils.print_info("profile name ")
            description = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(description,"802.1X")
            sleep(10)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            self.utils.print_info("Select action 1 for row 2")
            act1 = self.weh.get_elements(self.add_filter_act1)
            self.auto_actions.click(act1)
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath("//ul[@class='dropdown-menu show']//li/a")
            self.auto_actions.select_drop_down_options(drop_options,"Active Directory")
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            name = self.weh.get_element(self.ad_name)
            name.clear()
            self.auto_actions.send_keys(name,"AD174")
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            description = self.weh.get_element(self.ad_description)
            description.clear()
            self.auto_actions.send_keys(description, "AD174")
            sleep(10)
            self.utils.print_info("Selected Active Directory")
            sleep(15)
            host = self.driver.find_element_by_xpath("//*[@data-automation-tag='automation-host']")
            wait = WebDriverWait(self.driver, 17)
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-automation-tag='automation-host']")))
            #self.driver.execute_script("arguments[0].click();",host)
            #host.clear()
            self.auto_actions.send_keys(host,"10.234.63.27")
            self.auto_actions.send_enter(host)
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            base_dn = self.weh.get_element(self.ad_base_dn)
            base_dn.clear()
            self.auto_actions.send_keys(base_dn,"CN=Users,DC=amra3,DC=local")
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            bind_dn = self.weh.get_element(self.ad_bind_dn)
            bind_dn.clear()
            self.auto_actions.send_keys(bind_dn,"CN=Administrator,CN=Users,DC=amra3,DC=local")
            sleep(5)
            password = self.weh.get_element(self.passwd)
            self.auto_actions.send_keys(password,"Localsetup123")
            sleep(5)
            test_passwd = self.weh.get_element(self.test_pwd)
            self.auto_actions.click(test_passwd)
            sleep(5)
            self.utils.print_info("Selected Active Directory")
            auth_add_rule = self.weh.get_element(self.ad_auth_add_rule)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            add_rule_unknown = self.weh.get_element(self.auth_add_rule_unknown)
            self.auto_actions.click(add_rule_unknown)
            sleep(10)
            rule_name = self.weh.get_element(self.add_rule_name)
            self.auto_actions.send_keys(rule_name,"rule1")
            sleep(10)
            self.utils.print_info("Click on Add Action")
            action_button = self.weh.get_element(self.add_action)
            self.auto_actions.click(action_button)
            sleep(5)
            self.utils.print_info("Select action 1 for row 1")
            row1_act1 = self.weh.get_elements(self.add_rule_row1_act1)
            self.auto_actions.select_drop_down_options(row1_act1,"Role")
            sleep(10)
            self.utils.print_info("Select action 2 for row 2")
            row1_act2 = self.weh.get_elements(self.add_rule_row1_act2)
            self.auto_actions.select_drop_down_options(row1_act2,"testrole")
            sleep(10)
            self.utils.print_info("Add another row")
            new_row = self.weh.get_element(self.add_row)
            self.auto_actions.click(new_row)
            sleep(10)
            self.utils.print_info("Select action 1 for row 2")
            row2_act1 = self.weh.get_elements(self.add_rule_row2_act1)
            self.auto_actions.select_drop_down_options(row2_act1,"Role")
            sleep(10)
            self.utils.print_info("Select action 2 for row 2")
            row2_act2 = self.weh.get_elements(self.add_rule_row2_act2)
            self.auto_actions.select_drop_down_options(row2_act2,"testrole")
            sleep(10)
            create_ad = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_ad)
            sleep(5)
            return 1
        else:
            return -1






