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


    def create_user(self,role,username,useremail,**kwargs):
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
            self.common_validation.fault(**kwargs)
            return -1
        if self.check_role_type(role) == -1:
            return -1
        self.screen.save_screen_shot()
        self.utils.print_info("Entering Username...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_users_page_fullname_text(), username)
        sleep(1)
        self.utils.print_info("Entering Email...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_users_page_email_text(), useremail)
        sleep(1)
        if(role == "MSP"):
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
                kwargs['pass_msg'] = username+" is in USERS list page " + str(number)
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.auto_actions.click_reference(self.portal_web_elements.get_users_page_nextpage_button)
                sleep(1)
                number = number + 1
                element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        self.utils.print_info("filter users with Name in page" + str(number))
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_name_filter_item)
        sleep(1)
        self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), username)
        sleep(2)
        if self.check_users_list(username) != -1:
            kwargs['pass_msg'] = username + " is in USERS list page " + str(number)
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = fail_msg
            self.common_validation.failed(**kwargs)
            return -1

    def create_xiq_account(self,customerName,firstName,lastName,adminEmail,adminPassword,**kwargs):
        """
        - This keyword can be used in USERS page,it will create a msp-admin account on Portal
        - Keyword Usage
        - ``Create MSP User  ${username}  ${user_email}``
        :param username: - the username of msp-admin
        :param useremail: - the email of msp-amin
        :return: returns 1 if successfully get the created user in USERS list else -1
        """
        self.utils.print_info("Click on Add button")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_add_button)
        element_status = self.web_element_controller.is_web_element_present(self.portal_web_elements.get_add_customers_page_customername_text())
        if not element_status:
            kwargs['fail_msg'] = "Not able to find the input 'Customer Name' which means the create customer account page may not open"
            self.common_validation.fault(**kwargs)
            return -1
        self.screen.save_screen_shot()
        self.utils.print_info("Entering Customer Name...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_customers_page_customername_text(), customerName)
        sleep(1)
        self.utils.print_info("Entering Admin First Name...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_customers_page_firstname_text(), firstName)
        sleep(1)
        self.utils.print_info("Entering Admin Last Name...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_customers_page_lastname_text(), lastName)
        sleep(1)
        self.utils.print_info("Entering Admin Email Address...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_customers_page_adminemail_text(), adminEmail)
        sleep(1)
        self.utils.print_info("Entering Admin Password...")
        self.auto_actions.send_keys(self.portal_web_elements.get_add_customers_page_adminpasswored_text(), adminPassword)
        sleep(1)
        self.utils.print_info("Clicking on submit button")
        self.auto_actions.click_reference(self.portal_web_elements.get_add_customers_page_submit_button)
        sleep(2)
        self.utils.print_info("check whether the new customer is in the customer list")
        fail_msg = "The created user" + customerName + " is not in the customer list"
        self.utils.print_info("Filter the customer by name...")
        self.auto_actions.send_keys(self.portal_web_elements.get_customers_page_filter_text(), customerName)
        sleep(2)
        if self.check_users_list(customerName) != -1:
            kwargs['pass_msg'] = customerName + " is in customers list page "
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = fail_msg
            self.common_validation.failed(**kwargs)
            return -1

    def check_role_type(self, user_type, **kwargs):
        """
        - This keyword can be used in Create User Account page,it'll check the role's type that present in the page
        - Keyword Usage
        - `` if self.check_role_type("MSP") == -1:
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

    def edit_user(self, username, oldemail, newemail, **kwargs):
        """
            - This can be used in USERS page
            - Keyword Usage
            - ``edit User    ${MSP_USER}      ${MSP_USER_EMAIL}        ${MSP_USER_EMAIL_1}``
            :param: username - the user who will be edited
            :param: oldemail - the email that filled when create the user
            :param: newemail - the email that will be changed to
            :return: returns 1 if the the user's email is edited successfully and displayed correctly on USERS page list,else -1
        """
        self.utils.print_info("Click on USERS menu")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_menu_item)
        element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        number = 1
        while element_status:
            self.utils.print_info("filter users with Name in page" + str(number))
            sleep(1)
            self.auto_actions.click_reference(self.portal_web_elements.get_users_page_name_filter_item)
            sleep(2)
            self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), username)
            sleep(2)
            if self.check_users_list(username) != -1:
                self.utils.print_info(username + " is in USERS list page " + str(number))
                self.utils.print_info("Click Edit button...")
                element = self.web.get_element(self.portal_web_elements.get_users_page_displayName_item(username))
                print(self.portal_web_elements.get_users_page_displayName_item(username))
                print(element)
                self.auto_actions.click(element)
                sleep(1)
                self.auto_actions.click_reference(self.portal_web_elements.get_edit_button_portal)
                sleep(1)
                if self.edit_user_email(oldemail,newemail) == -1:
                    kwargs['fail_msg'] = "Edit user email failed!"
                    self.common_validation.failed(**kwargs)
                    return -1
                elif self.check_edit_result_on_users_page(username,newemail) == -1:
                    kwargs['fail_msg'] = "The new email on user page list is not correct"
                    self.common_validation.failed(**kwargs)
                    return -1
                else:
                    kwargs['success_msg'] = "Email is edited successfully"
                    self.common_validation.passed(**kwargs)
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
            self.utils.print_info("Click Edit button...")
            self.auto_actions.click_reference(self.portal_web_elements.get_edit_button_portal)
            sleep(1)
            if self.edit_user_email(oldemail,newemail) == -1:
                kwargs['fail_msg'] = "Edit user email failed!"
                self.common_validation.failed(**kwargs)
                return -1
            elif self.check_edit_result_on_users_page(username, newemail) == -1:
                kwargs['fail_msg'] = "The new email on user page list is not correct"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                kwargs['success_msg'] = "Email is edited successfully"
                self.common_validation.passed(**kwargs)
                return 1
        else:
            kwargs['fail_msg'] = username + " is not in USERS list"
            self.common_validation.failed(**kwargs)
            return -1



    def delete_user(self, username):
        """
            - This can be used in USERS page
            - Keyword Usage
            - ``Delete User    ${MSP_USER}``
            :param: username - the created user's name
            :return: returns 1 if the created user is in USERS list of current page else -1
        """
        self.utils.print_info("Click on USERS menu")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_menu_item)
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

    def delete_customer(self, username, **kwargs):
        """
            - This can be used in USERS page
            - Keyword Usage
            - ``Delete User    ${MSP_USER}``
            :param: username - the created user's name
            :return: returns 1 if the created user is in USERS list of current page else -1
        """
        self.utils.print_info("Click on customer menu")
        self.auto_actions.click_reference(self.portal_web_elements.get_customers_menu_item)
        sleep(1)
        self.utils.print_info("Filter the customer by name...")
        self.auto_actions.send_keys(self.portal_web_elements.get_customers_page_filter_text(), username)
        number = 1
        if self.check_users_list(username) != -1:
            self.utils.print_info(username + " is in USERS list page " + str(number))
            element = self.web.get_element(self.portal_web_elements.get_users_page_displayName_item(username))
            self.auto_actions.click(element)
            sleep(1)
            self.auto_actions.click_reference(self.portal_web_elements.get_delete_button_portal)
            sleep(1)
            self.auto_actions.click_reference(self.portal_web_elements.get_delete_confirm_yes_item)
            sleep(2)
            kwargs['delete_success_msg'] = username + "is deleted"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info(username + " is not in USERS list")
            return -1

    def edit_user_email(self, oldemail, newemail, **kwargs):
        """
            - This can be used in USERS edit page.It's to change user's email from 'oldemail' to 'newemail'.
            - Keyword Usage
            - ``if self.edit_user_email(oldemail,newemail) != -1:
            return 1``
            :param: oldemail - the email that filled when create the user
            :param: newemail - the email that will be changed to
            :return: returns 1 if the user's email is edited successfully and displayed correctly on USERS page list,else -1
        """
        element = self.portal_web_elements.get_edit_users_page_email_text(oldemail)
        element_status = self.web_element_controller.is_web_element_present(element)
        if not element_status:
            kwargs['fail_msg'] = " edit page open failed!"
            self.common_validation.failed(**kwargs)
            return -1
        self.utils.print_info("Clicking old Email...")
        element = self.web.get_element(self.portal_web_elements.get_edit_users_page_email_text(oldemail))
        self.auto_actions.double_click(element)
        sleep(2)
        self.utils.print_info("Entering New Email...")
        self.auto_actions.send_keys(self.portal_web_elements.get_edit_users_page_email_input(), newemail)
        sleep(1)
        self.auto_actions.click_reference(self.portal_web_elements.get_edit_users_page_edit_accept_button)
        sleep(1)
        element = self.portal_web_elements.get_edit_users_page_email_text(newemail)
        element_status = self.web_element_controller.is_web_element_present(element)
        if not element_status:
            kwargs['fail_msg'] = " change email failed!"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def check_edit_result_on_users_page(self, username, newemail,**kwargs):
        """
            - This can be used in USERS page.It's to check whether the new message is displayed correctly in the list。
            - Keyword Usage
            - ``if self.check_edit_result_on_users_page(username，newemail) != -1:
            return 1``
            :param: oldemail - the email that filled when create the user
            :param: newemail - the email that will be changed to
            :return: returns 1 if the email is not in the list,else -1
        """
        self.utils.print_info("Start to check the new email on users page...")
        self.utils.print_info("Click on USERS menu")
        self.auto_actions.click_reference(self.portal_web_elements.get_users_menu_item)
        element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        number = 1
        while element_status:
            self.utils.print_info("filter users with email in page" + str(number))
            self.auto_actions.click_reference(self.portal_web_elements.get_users_page_email_filter_item)
            sleep(1)
            self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), newemail)
            sleep(2)
            if self.check_users_list(username) != -1:
                kwargs['pass_msg'] = username + " is in USERS list page " + str(number)
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.auto_actions.click_reference(self.portal_web_elements.get_users_page_nextpage_button)
                number = number + 1
                element_status = self.portal_web_elements.get_users_page_nextpage_button().is_enabled()
        self.utils.print_info("filter users with Name in page" + str(number))
        self.auto_actions.click_reference(self.portal_web_elements.get_users_page_email_filter_item)
        sleep(1)
        self.auto_actions.send_keys(self.portal_web_elements.get_users_page_name_filter_text(), newemail)
        sleep(2)
        fail_msg = "The created user" + username + " is not in the users list"
        if self.check_users_list(username) != -1:
            kwargs['pass_msg'] = username + " is in USERS list page " + str(number)
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = fail_msg
            self.common_validation.failed(**kwargs)
            return -1





