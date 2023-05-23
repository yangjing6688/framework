from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CloudDriver import CloudDriver
from extauto.xiq.flows.common.Login import Login



from extauto.iam.elements.IAMWebElements import IAMWebElements
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
        self.login = Login()
        self.driver = CloudDriver().cloud_driver


    def login_iam_console(self, **kwargs):
        """
        - This keyword is used to open global setting-> iam console link
        - Keyword Usage:
        -   Robot:
        -      Library     iam/flows/ConfigureIDP.py
        -      login iam console
        -   Pytest:
        -      Imports:
        -         from extauto.iam.flows.ConfigureIDP import ConfigureIDP
        -      Calling Keyword:
        -         keywords_configIDP = ConfigureIDP()
        -         keywords_configIDP.login_iam_console
            :return: returns 1 if iam console is opened successfully else -1
        """
        try:
            self.utils.print_info("Clicking on Identity and Access Management Menu")
            self.auto_actions.move_to_element(self.iam_web_elements.get_user_account_nav())
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_console_link)
            self.login.gui_switch_to_window(1)
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            kwargs['fail_msg'] = f"Error: {e}"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            return 1
    def add_idp(self,domain,description,email,group,meta_data_url,default_group="Administrator",**kwargs):
        """
        - This keyword can be used in idp list page,it will create a new idp
        - Keyword Usage:
        -   Robot:
        -      Library     iam/flows/ConfigureIDP.py
        -      add idp ${domain} ${description} ${email} ${group} ${meta_data_url}
        -   Pytest:
        -      Imports:
        -         from extauto.iam.flows.ConfigureIDP import ConfigureIDP
        -      Calling Keyword:
        -         keywords_configIDP = ConfigureIDP()
        -         keywords_configIDP.add_idp(domain,description,email,group,meta_data_url)
        :param domain: the domain of the new idp, which should be the same with the one configured in ADFS
        :param description: description about the new idp
        :param email: the attribute mapping(user profile attribute<->SAML attribute) value email
        :param group: the attribute mapping(user profile attribute<->SAML attribute) value group
        :param meta_data_url: the url of meta_data which is used for import the meta_data
        :param default_group: the attribute mapping(user profile attribute<->SAML attribute) defautl group which is mapped the roles of XIQ
        :return: returns 1 if successfully get the created user in USERS list else -1
        """
        try:
            self.utils.print_info("Open Identity and Access Management link")
            self.login_iam_console()
            self.utils.print_info("Click on add button")
            self.auto_actions.click_reference(self.iam_web_elements.get_add_idp_button)
            for i in range(7):
                element_status = self.web_element_controller.is_web_element_present(self.iam_web_elements.get_iam_idp_page_domain_text())
                if element_status:
                    break
                sleep(1)
            element_status = self.web_element_controller.is_web_element_present(self.iam_web_elements.get_iam_idp_page_domain_text())
            if not element_status:
                kwargs['fail_msg'] = "Not able to find the input 'Domain' which means the New Identity Provider Profile page may not open"
                self.common_validation.failed(**kwargs)
                return -1
            self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_domain_text(), domain)
            self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_description_text(), description)
            sleep(1)
            self.utils.print_info("Click on continue button")
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_profile_continue_button)
            sleep(1)
            self.utils.print_info("Import metadata by URL")
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_import_from_url_button)
            self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_idp_metadata_url_text(), meta_data_url)
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_import_button)
            sleep(1)
            element_status = self.web_element_controller.is_web_element_present(self.iam_web_elements.get_iam_idp_page_entity_id)
            if not element_status:
                kwargs['fail_msg'] = "Import metadate from url failed!"
                self.common_validation.failed(**kwargs)
                return -1
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_connection_continue_button)
            self.utils.print_info("Input Email and Group attribute")
            self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_email_text(), email)
            self.auto_actions.send_keys(self.iam_web_elements.get_iam_idp_page_group_text(), group)
            self.utils.print_info("Select Default Group")
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_default_group_dropdown)
            element = self.web.get_element(self.iam_web_elements.get_iam_idp_page_default_group_item(default_group))
            self.auto_actions.click(element)
            self.utils.print_info("Click Save & Finish button")
            self.auto_actions.click_reference(self.iam_web_elements.get_iam_idp_page_save_button)
            self.utils.print_info("Check the new idp is in the Identity Providers list")
            if self.check_idp_list(domain) != -1:
                kwargs['pass_msg'] = domain + " is in idp list page "
                self.common_validation.passed(**kwargs)
                return 1
        except Exception:
            kwargs['fail_msg'] = "Create idp failed!"
            self.common_validation.failed(**kwargs)
            return -1



    def check_idp_list(self, domain, **kwargs):
        """
        - This can be used in USERS page,it'll check whether the created user is in the page list
         - Keyword Usage:
        -   Robot:
        -      Library     iam/flows/ConfigureIDP.py
        -      check idp list       ${domain}
        -   Pytest:
        -      Imports:
        -         from extauto.iam.flows.ConfigureIDP import ConfigureIDP
        -      Calling Keyword:
        -         keywords_configIDP = ConfigureIDP()
        -         keywords_configIDP.check_idp_list(domain)
        :param: domain: the created idp's domain
        :return: returns 1 if the created user is in USERS list of current page else -1
        """
        try:
            element = self.iam_web_elements.get_iam_page_list_idp(domain)
            self.driver.find_element_by_xpath(element.get('XPATH'))
        except Exception as e:
            self.utils.print_debug("Error: ", e)
            kwargs['fail_msg'] = domain+" is not exist in this page"
            self.common_validation.failed(**kwargs)
            return -1
        return 1