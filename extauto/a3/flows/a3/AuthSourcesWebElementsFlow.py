from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from common.AutoActions import AutoActions
from common.Screen import Screen
from common.Utils import Utils
from a3.elements.AuthSourcesWebElements import AuthSourcesWebElements
from a3.elements.GlobalSettingWebElements import GlobalSettingWebElements
from xiq.flows.common.DeviceCommon import DeviceCommon


class AuthSourcesWebElementsFlow(AuthSourcesWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.auth_source_web_elements = AuthSourcesWebElements()
        self.setting = GlobalSettingWebElements()
        self.driver = webdriver.Chrome()

    def create_auth_source(self, name_value, name_desc, host_name, host_pwd):
        """
        - This keyword will define the authentication source and create authentication rules
        - Keyword Usage
        - ``Select Auth Source``
        :return: 1 if auth source is created successfully -1
        """
        if self.auto_actions.click_reference(self.get_auth_source_menu) == 1:
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
            self.auto_actions.send_keys(name, name_value)
            sleep(5)
            self.utils.print_info("Enter Description")
            description = self.weh.get_element(self.ad_description)
            self.auto_actions.send_keys(description, name_desc)
            sleep(5)
            self.utils.print_info("Enter Host")
            description.send_keys(Keys.TAB)
            host = self.weh.get_element(self.host_input)
            self.auto_actions.send_keys(host, host_name)
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
            self.auto_actions.send_keys(password, host_pwd)
            sleep(5)
            self.utils.print_info("Test Password")
            test_passwd = self.weh.get_element(self.test_pwd)
            self.auto_actions.click(test_passwd)
            sleep(5)
            self.utils.print_info("Select associated Realm")
            a_realm = self.weh.get_element(self.associated_realms)
            self.auto_actions.click(a_realm)
            realm = self.weh.get_element(self.realm_value)
            self.auto_actions.click(realm)
            sleep(5)
            self.utils.print_info("Add Authentication Rule")
            auth_add_rule = self.weh.get_element(self.ad_auth_add_rule)
            self.auto_actions.click(auth_add_rule)
            sleep(5)
            self.utils.print_info("Click on Rule")
            add_rule_unknown = self.weh.get_element(self.auth_add_rule_unknown)
            self.auto_actions.click(add_rule_unknown)
            sleep(5)
            self.utils.print_info("Enter Rule Name")
            rule_name = self.weh.get_element(self.add_rule_name)
            self.auto_actions.send_keys(rule_name, "rule1")
            sleep(5)
            self.utils.print_info("Click on Add Action")
            action_button = self.weh.get_element(self.add_action)
            self.auto_actions.click(action_button)
            sleep(5)
            self.utils.print_info("Select action 1 for row 1")
            # Commented on 1/18/23 because variable is unused
            # auth_row1_act1 = self.weh.get_element(self.add_rule_row1_act1)
            self.weh.get_element(self.add_rule_row1_act1)
            sleep(5)
            option1 = self.weh.get_element(self.rule_row1_select_option)
            self.auto_actions.click(option1)
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            auth_row1_act2 = self.weh.get_element(self.add_rule_row1_act2)
            self.auto_actions.click(auth_row1_act2)
            option2 = self.weh.get_element(self.value_row1_select_option)
            self.auto_actions.click(option2)
            sleep(5)
            self.utils.print_info("Add another row")
            new_row = self.weh.get_element(self.add_row)
            self.auto_actions.click(new_row)
            sleep(5)
            self.utils.print_info("Select action 1 for row 2")
            # Commented on 1/18/23 because variable is unused
            # auth_row2_act1 = self.weh.get_element(self.add_rule_row2_act1)
            self.weh.get_element(self.add_rule_row2_act1)
            sleep(5)
            option3 = self.weh.get_element(self.rule_row2_select_option)
            self.auto_actions.click(option3)
            self.utils.print_info("Select action 2 for row 2")
            auth_row2_act2 = self.weh.get_element(self.add_rule_row2_act2)
            self.auto_actions.click(auth_row2_act2)
            option4 = self.weh.get_element(self.value_row2_select_option)
            self.auto_actions.click(option4)
            sleep(5)
            create_ad = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_ad)
            sleep(5)
            self.utils.print_info("Auth Source is created successfully")
            sleep(5)
            return 1
        else:
            self.utils.print_info("Auth Source is Not created ")
            return -1
