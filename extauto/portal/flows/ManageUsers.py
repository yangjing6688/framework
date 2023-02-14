from time import sleep
from selenium.common.exceptions import NoSuchElementException
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CloudDriver import CloudDriver


from extauto.portal.elements.PortalWebElements import PortalWebElements
from extauto.common.WebElementController import WebElementController


class ManageUsers():
    def __init__(self):
        self.common_validation = CommonValidation()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.portal_web_elements = PortalWebElements()
        self.web = WebElementHandler()
        self.web_element_controller = WebElementController()
        self.driver = CloudDriver().cloud_driver


    def create_MSP_user(self,username,useremail,**kwargs):
        """
        - This keyword can be used in USERS page,it will create a msp-admin account on Portal
        - Keyword Usage
        - ``Create MSP User  ${username}  ${user_email}``
        :param username: - the username of msp-admin
        :param useremail: - the email of msp-amin
        :return: returns 1 if successfully get the created user in USERS list else -1
        """
        self.utils.print_info("Click on USERS menu")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_menu_item)
        self.utils.print_info("Click on Add button")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_add_button)
        element_status = self.web_element_controller.is_web_element_present(self.portal_web_elements.get_add_users_page_fullname_text())
        if not element_status:
            kwargs['fail_msg'] = "Not able to find the input 'Full Name' which means the create users page may not open"
            self.common_validation.failed(**kwargs)
            return -1
        if self.check_role_type("MSP") == -1:
            return -1
        self.screen.save_screen_shot()
        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_users_page_fullname_text(), username)
        sleep(1)
        self.utils.print_info("Entering Email...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_users_page_email_text(), useremail)
        sleep(1)
        self.utils.print_info("Select a data center...")
        self.auto_actions.click_reference(self.portal_web_elements.get_add_users_page_datacenter_checkbox)
        sleep(1)
        self.utils.print_info("Clicking on submit button")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_submit_button)
        sleep(1)
        self.utils.print_info("check the fist page of USERS")
        fail_msg = "The created user" + username + " is not in the users list"
        element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        number = 1
        while element_status:
            self.utils.print_info("filter users with Name in page" + str(number))
            self.auto_actions.click_reference(self.portal_web_elements.get_users_page_name_filter_item)
            sleep(1)
            self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), username)
            sleep(2)
            if self.check_users_list(username) != -1:
                self.utils.print_info(username+" is in USERS list page " + str(number))
                return 1
            else:
                self.auto_actions.click_reference(self.portal_web_elements.get_users_page_nextpage_button)
                number = number + 1
                element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        self.utils.print_info("filter users with Name in page" + str(number))
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_name_filter_item)
        sleep(1)
        self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), username)
        sleep(2)
        if self.check_users_list(username) != -1:
            self.utils.print_info(username + " is in USERS list page " + str(number))
            return 1
        else:
            kwargs['fail_msg'] = fail_msg
            self.common_validation.failed(**kwargs)
            return -1

    def check_role_type(self, user_type, **kwargs):
        """
        - This keyword can be used in Create User Account page,it'll check the role's type that present in the page
        - Keyword Usage
        - `` if self.get_role_type("MSP") == -1:
            return -1``
        :param: user_type: - user_type=msp - will get the role of msp-admin item,if the item is not exist which means test is faile
                           - user_type=VIQ - will get the role of viq-admin item,if the item is not exist,check failed
        :return: returns 1 if the role type is correct in Create User Account page else -1
        """
        if user_type == "MSP":
            self.utils.print_info("The new user is a msp admin")
            element = self.portal_web_elements.get_add_users_page_role_msp_text()
        if user_type == "VIQ":
            self.utils.print_info("The new user is a viq admin")
            element = self.portal_web_elements.get_add_users_page_role_viq_text()
        element_status = self.web_element_controller.is_web_element_present(element)
        if not element_status:
            kwargs['fail_msg'] = "The displayed Role type of"+user_type + "is not correct"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def check_users_list(self, username, **kwargs):
        """
        - This can be used in USERS page,it'll check whether the created user is in the page list
        - Keyword Usage
        - ``if self.check_users_list(username) != -1:
            return 1``
        :param: username - the created user's name
        :return: returns 1 if the created user is in USERS list of current page else -1
        """
        self.utils.print_info("Check the created user in users list")
        element = self.portal_web_elements.get_filter_user_name_list(username)
        try:
            self.driver.find_element_by_xpath(element.get('XPATH'))
        except NoSuchElementException:
            print(username+" is not exist in this page")
            return -1
        return 1

    def delete_user(self, username):
        """
            - This can be used in USERS page
            - Keyword Usage
            - ``if self.check_users_list(username) != -1:
                return 1``
            :param: username - the created user's name
            :return: returns 1 if the created user is in USERS list of current page else -1
        """
        element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        number = 1
        while element_status:
            self.utils.print_info("filter users with Name in page" + str(number))
            self.auto_actions.click_reference(self.portal_web_elements.get_users_page_name_filter_item)
            sleep(1)
            self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), username)
            sleep(2)
            if self.check_users_list(username) != -1:
                self.utils.print_info(username + " is in USERS list page " + str(number))
                element = self.web.get_element(self.portal_web_elements.get_users_page_displayName_item(username))
                print(self.portal_web_elements.get_users_page_displayName_item(username))
                print(element)
                self.auto_actions.click(element)
                sleep(1)
                self.auto_actions.click_reference(self.portal_web_elements.get_delete_button_portal)
                sleep(1)
                self.auto_actions.click_reference(self.portal_web_elements.get_delete_confirm_yes_item)
                sleep(2)
                self.utils.print_info(username + " is deleted")
                return 1
            else:
                self.auto_actions.click_reference(self.portal_web_elements.get_users_page_nextpage_button)
                number = number + 1
                element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        self.utils.print_info("filter users with Name in page" + str(number))
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_name_filter_item)
        sleep(1)
        self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), username)
        sleep(2)
        if self.check_users_list(username) != -1:
            self.utils.print_info(username + " is in USERS list page " + str(number))
            element = self.web.get_element(self.portal_web_elements.get_users_page_displayName_item(username))
            self.auto_actions.click(element)
            sleep(1)
            self.auto_actions.click_reference(self.portal_web_elements.get_delete_button_portal)
            sleep(1)
            self.auto_actions.click_reference(self.portal_web_elements.get_delete_confirm_yes_item)
            sleep(2)
            self.utils.print_info(username + " is deleted")
            return 1
        else:
            self.utils.print_info(username + " is not in USERS list")
            return -1



