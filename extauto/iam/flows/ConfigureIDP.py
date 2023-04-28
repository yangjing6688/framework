from time import sleep
from selenium.common.exceptions import NoSuchElementException
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CloudDriver import CloudDriver



from extauto.portal.elements.PortalWebElements import IAMWebElements
from extauto.common.WebElementController import WebElementController

class ConfigureIDP():
    def __init__(self):
        self.common_validation = CommonValidation()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.iam_web_elements = IAMWebElements()
        self.web = WebElementHandler()
        self.web_element_controller = WebElementController()
        self.driver = CloudDriver().cloud_driver


    def add_idp(self,domain,description,email,group,meta_data_url=default,default_group=Administrator,**kwargs):
        """
        - This keyword can be used in USERS page,it will create a msp-admin account on Portal
        - Keyword Usage
        - ``Create MSP User  ${username}  ${user_email}``
        :param username: - the username of msp-admin
        :param useremail: - the email of msp-amin
        :return: returns 1 if successfully get the created user in USERS list else -1
        """
        self.utils.print_info("Click on add button")
        self.auto_actions.click_reference(self.iam_web_elements.get_add_idp_button)
        sleep(2)
        element_status = self.web_element_controller.is_web_element_present(self.iam_web_elements.get_iam_idp_page_domain_text())
        if not element_status:
            kwargs['fail_msg'] = "Not able to find the input 'Domain' which means the New Identity Provider Profile page may not open"
            self.common_validation.failed(**kwargs)
            return -1
        self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_domain_text(), domain)
        self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_description_text(), description)
        self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_continue_buttondd_idp_button)
        sleep(1)
        element_status = self.web_element_controller.is_web_element_present(self.iam_web_elements.get_iam_idp_page_import_from_url_button)
        if not element_status:
            kwargs['fail_msg'] = "Not able to find the input 'Import From URL' which means the New Identity Provider Import From URL page may not open"
            self.common_validation.failed(**kwargs)
            return -1
        self.utils.print_info("Import metadata by URL")
        self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_import_from_url_button)
        sleep(1)
        self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_idp_metadata_url_text(), meta_data_url)
        self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_import_button)
        sleep(1)
        element_status = self.web_element_controller.is_web_element_present(self.iam_web_elements.get_iam_idp_page_entity_id)
        if not element_status:
            kwargs[
                'fail_msg'] = "Import metadate from url failed!"
            self.common_validation.failed(**kwargs)
            return -1
        self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_continue_button)
        sleep(2)
        self.utils.print_info("Input Email and Group attribute")
        self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_email_text(), email)
        self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_group_text(), group)
        self.utils.print_info("Select Default Group")
        self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_default_group_dropdown)
        self.auto_actions.click(self.iam_web_elements.get_iam_idp_page_default_group_item)
        sleep(1)
        self.utils.print_info("Click Save & Finish button")
        self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_save_button)
        sleep(3)
        self.utils.print_info("Check the new idp is in the Identity Providers list")
        if self.check_idp_list(domain) != -1:
            kwargs['pass_msg'] = domain + " is in idp list page "
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Create idp failed!
            self.common_validation.failed(**kwargs)
            return -1


    def check_idp_list(self, domain, **kwargs):
        """
        - This can be used in USERS page,it'll check whether the created user is in the page list
        - Keyword Usage
        - ``if self.check_users_list(username) != -1:
            return 1``
        :param: username - the created user's name
        :return: returns 1 if the created user is in USERS list of current page else -1
        """
        element = self.iam_web_elements.get_iam_page_list_idp(domain)
        try:
            self.driver.find_element_by_xpath(element.get('XPATH'))
        except NoSuchElementException:
            print(username+" is not exist in this page")
            return -1
        return 1



