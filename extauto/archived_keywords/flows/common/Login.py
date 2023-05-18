""" This file contains code for keywords that have been archived.
    If the keywords need to be available again copy the code to xiq/flows/common/Login.py and implement the keyword move process.
    Instructions for moving a keyword can be found here: https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords """

# All Archived keywords will be deleted after December 2023

import random
from ExtremeAutomation.Utilities.deprecated import deprecated
from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.xapi.common.XapiLogin import XapiLogin
from extauto.xiq.elements.LoginWebElements import LoginWebElements
from extauto.xiq.elements.PasswordResetWebElements import PasswordResetWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.xiq.elements.MspWebElements import MspWebElements
from ExtremeAutomation.Library.Utils.Singleton import Singleton

class Login(object, metaclass=Singleton):

    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        self.common_validation = CommonValidation()
        self.record = False
        self.t1 = None
        self.window_index = -1
        self.utils = Utils()
        self.login_web_elements = LoginWebElements()
        self.pw_web_elements = PasswordResetWebElements()
        self.msp_web_elements = MspWebElements()
        self.nav_web_elements = NavigatorWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xapiLogin = XapiLogin()

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def reset_password_for_new_customer(self, password, url="default", **kwargs):
        """
        - Reset password for xiq account with passed reset password url link
        - Keyword Usage:
        - ``Reset Password For New Account  ${RESET_PASSWORD}   ${RESET_URL_LINK}``
        :param password:  password to reset
        :param url: reset password url link
        :return: 1
        """
        if url == "default":
            self._init()
        else:
            self._init(url)

        got_title = CloudDriver().cloud_driver.title
        self.utils.print_info("Page Title on Reset password Page: ", got_title)
        self.utils.print_info(" entering the password")
        sleep(5)
        self.auto_actions.send_keys(self.pw_web_elements.get_password_textbox(), password)
        sleep(5)
        self.utils.print_info(" entering the confirm password")
        self.auto_actions.send_keys(self.pw_web_elements.get_conf_password_texbox(), password)
        sleep(5)
        self.utils.print_info(" saving the password")
        self.auto_actions.click_reference(self.pw_web_elements.get_save_button)

        got_title = CloudDriver().cloud_driver.title
        self.utils.print_info("Page Title on Reset password Page: ", got_title)
        kwargs['pass_msg'] = "Reset the Password For New Account Successfully"
        self.common_validation.passed(**kwargs)
        return 1

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def skip_if_account_90_days(self, **kwargs):
        """
        - This keyword detects a license of 90 days and clicks on the option of 90 days
        - Keyword Usage:
        - ``skip_if_account_90_days``
        :return: None
        """
        self.utils.print_info(" Select the option of 90 days trial if exists")
        status = self.login_web_elements.get_30_days_trial_txt()
        try:
            if status != None:
                self.auto_actions.click_reference(self.login_web_elements.get_option_30_days_trial)
                self.auto_actions.click_reference(self.login_web_elements.get_get_started_button)
                self.auto_actions.click_reference(self.login_web_elements.get_drawer_trigger)
        except Exception:
            kwargs['fail_msg'] = "Could not select the option of 90 days trial "
            self.common_validation.failed(**kwargs)
            return -1, "Could not select the option of 90 days trial "
        return str(1), None

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def xiq_get_child_window_list(self, win_index):
        """
        - Obtain the Child Window Index List
        - Keyword Usage:
        - ``XIQ Get Child Window List``
        :param:  win_index - Index of the window to close
        :return: Return List containing the Child Window Indexes
        """
        window_index_list = CloudDriver().get_child_window_list(win_index)
        return window_index_list

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def login_for_first_time(self, **kwargs):
        """
        - This keyword used to login for the first time user based on option provided in test case
        - If option is not specified, default option of "30-days trial" is selected.
        - Getting started with license is not supported through Automation as it depends on Gemalto license.
        - Assumes that user already in login option selection page
        - Keyword Usage:
        - ``Login For First Time``
        :return: 1
        """

        login_option = BuiltIn().get_variable_value("${LOGIN_OPTION}")
        self.utils.print_info("Selecting option : ", login_option)

        if "30-day trial" in login_option:
            self.auto_actions.click_reference(self.login_web_elements.get_login_trail_30_days)

        elif "ExtremeCloud IQ license" in login_option:
            # self.auto_actions.click_reference(self.login_web_elements.get_login_license_option)
            self.utils.print_info("we are not supporting this option proceeding with default option")

        elif "entitlement key" in login_option:
            self.auto_actions.click_reference(self.login_web_elements.get_login_entitlement_radio)

            entitlement_key = BuiltIn().get_variable_value("${ENTITLEMENT_KEY}")

            self.utils.print_info("Entering entitlement key ", entitlement_key)
            self.auto_actions.send_keys(self.login_web_elements.get_login_entitlement_key(), entitlement_key)

        elif "1 year included Pilot license" in login_option:
            self.auto_actions.click_reference(self.login_web_elements.get_login_year_trail_option)

        elif "IQ Connect" in login_option:
            self.auto_actions.click_reference(self.login_web_elements.get_login_iq_connect)

        else:
            self.utils.print_info("proceeding with default option of 30-days trail")
            self.auto_actions.click_reference(self.login_web_elements.get_login_trail_30_days)

        self.utils.print_info("Clicking on Get Started button...")
        self.auto_actions.click_reference(self.login_web_elements.get_started_login_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Accepting Terms of service...")
        self.auto_actions.click_reference(self.login_web_elements.get_accept_terms_of_service_wizard)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Submitting Terms of service...")
        self.auto_actions.click_reference(self.login_web_elements.get_submit_terms_of_service_wizard)
        sleep(1)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Accepting data privacy policy...")
        self.auto_actions.click_reference(self.login_web_elements.get_accept_data_privacy)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Submitting data privacy policy...")
        self.auto_actions.click_reference(self.login_web_elements.get_submit_data_privacy)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)
        kwargs['pass_msg'] = "Login for the first time is sucessful"
        self.common_validation.passed(**kwargs)
        return 1

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def create_new_user_portal(self, customer_name, admin_first_name, admin_last_name, admin_password,
                               sw_connection_host, **kwargs):
        """
        Creates a fresh new user in portal
        :param customer_name: the name of the customer, written as an email
        :param admin_first_name: first name of the admin
        :param admin_last_name: last name of the admin
        :param admin_email: admin email, the email that is used to log in into xiq cloud
        :param admin_password: the password chosen to log in into xiq cloud
        :param sw_connection_host: the url of the RDC
        :return: returns 1 if the account was created successfully or -1 if otherwise
        """
        cnt = 0
        while cnt < 3:
            random_nr = random.randrange(1, 10000)
            user = customer_name + "_" + str(random_nr) + "@gmail.com"
            self.utils.print_info("user:", user)
            check = self.check_if_xiq_user_exists(user)
            if check == 1:
                break
            elif check == -1:
                if cnt == 2:
                    kwargs['fail_msg'] = "The users already existed"
                    self.common_validation.failed(**kwargs)
                    return -1
                else:
                    self.utils.print_info("The user already existed. Try again")
            else:
                if cnt == 2:
                    kwargs['fail_msg'] = "Error"
                    self.common_validation.fault(**kwargs)
                    return -1
                else:
                    pass
            cnt = cnt + 1

        self.screen.save_screen_shot()
        self.utils.print_info("Creating new user...")
        self.utils.print_info("Clicking on add button...")
        sleep(10)
        found_page = False
        cnt = 0
        while cnt < 4:
            add_button = self.login_web_elements.get_add_button_portal()
            if add_button:
                self.utils.print_info("Found add button!")
                self.auto_actions.click(add_button)
                found_page = True
                break
            else:
                self.utils.print_info("Unable to find the add button.Try again:", cnt)
            sleep(20)
        if not found_page:
            kwargs['fail_msg'] = "ADD BUTTON NOT FOUND"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)
        self.screen.save_screen_shot()
        self.utils.print_info("Inserting customer name in the field...")
        customer_name_field = self.login_web_elements.get_customer_name_field()
        if customer_name_field:
            self.utils.print_info("Found customer name field!")
            self.utils.print_info("Inserting customer name: " + user)
            self.auto_actions.send_keys(customer_name_field, user)
        else:
            kwargs['fail_msg'] = "Unable to find customer name field."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin first name in the field...")
        first_name_field = self.login_web_elements.get_admin_first_name_field()
        if first_name_field:
            self.utils.print_info("Found admin first name field!")
            self.utils.print_info("Inserting admin first name: " + admin_first_name)
            self.auto_actions.send_keys(first_name_field, admin_first_name)
        else:
            kwargs['fail_msg'] = "Unable to find admin first name field."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin last name in the field...")
        last_name_field = self.login_web_elements.get_admin_last_name_field()
        if last_name_field:
            self.utils.print_info("Found admin last name field!")
            self.utils.print_info("Inserting admin last name: " + admin_last_name)
            self.auto_actions.send_keys(last_name_field, admin_last_name)
        else:
            self.screen.save_screen_shot()
            kwargs['fail_msg'] = "Unable to find admin last name field."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin email in the field...")
        admin_email_field = self.login_web_elements.get_admin_email_field()
        if admin_email_field:
            self.utils.print_info("Found admin email field!")
            self.utils.print_info("Inserting admin email: " + user)
            self.auto_actions.send_keys(admin_email_field, user)
        else:
            self.screen.save_screen_shot()
            kwargs['fail_msg'] = "Unable to find admin email field."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)
        self.utils.print_info("Inserting admin password in the field...")
        admin_password_field = self.login_web_elements.get_admin_password_field()
        if admin_password_field:
            self.utils.print_info("Found admin password field!")
            self.utils.print_info("Inserting admin password: " + admin_password)
            self.auto_actions.send_keys(admin_password_field, admin_password)
        else:
            self.screen.save_screen_shot()
            kwargs['fail_msg'] = "Unable to find admin password field."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)
        self.utils.print_info("Clicking on Data Center dropdown...")
        self.screen.save_screen_shot()
        data_center_dropdown = self.login_web_elements.get_data_center_dropdown()
        if data_center_dropdown:
            self.utils.print_info("Found the data center dropwdown!")
            sleep(2)
            self.auto_actions.click(data_center_dropdown)
            data_center_dropdown_options = self.login_web_elements.get_data_center_dropdown_options()
            if data_center_dropdown_options:
                self.utils.print_info("Found dropdown options!")
                sleep(2)
                pattern1 = "(\\w+)."
                gdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
                self.utils.print_info("RDC is : ", gdc[0])
                flag = False
                for option in data_center_dropdown_options:
                    if gdc[0] in option.text:
                        flag = True
                        self.auto_actions.click(option)
                        self.utils.print_info(option.text)
                        break
                if flag:
                    self.utils.print_info("Found the required datacenter: " + gdc[0])
                else:
                    self.utils.print_info("Unable to find the required datacenter.")
                    self.utils.print_info("Clicking on Cancel button...")
                    cancel_button = self.login_web_elements.get_cancel_button()
                    if cancel_button:
                        self.auto_actions.click(cancel_button)
                        kwargs['fail_msg'] = "Found Cancel button!"
                        self.common_validation.fault(**kwargs)
                        return -1
                    else:
                        kwargs['fail_msg'] = "Unable to find the cancel button."
                        self.common_validation.fault(**kwargs)
                        return -1
            else:
                kwargs['fail_msg'] = "Unable to find dropdown options."
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to find the dropdown menu."
            self.common_validation.fault(**kwargs)
            return -1
        self.utils.print_info("Clicking on submit button...")
        self.screen.save_screen_shot()
        submit_button = self.login_web_elements.get_submit_button()
        if submit_button:
            self.utils.print_info("Found submit button!")
            sleep(2)
            self.auto_actions.click(submit_button)
            self.screen.save_screen_shot()
            return user
        else:
            kwargs['fail_msg'] = "Unable to find submit button."
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def delete_user_portal(self, customer_name, check_delete_devices=-1, **kwargs):
        """
        This function deletes the account created in portal
        :param customer_name:   the name of the customer under which the account was created
        :return: returns 1 if the account was deleted or -1 if otherwise
        """
        sleep(20)
        if check_delete_devices == -1:
            kwargs['fail_msg'] = "There are still devices on this account!!!!"
            self.common_validation.failed(**kwargs)
            return -1
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking on name cell menu button ...")
        cell_menu_button = self.login_web_elements.get_cell_menu_button_name_section()
        if cell_menu_button:
            self.utils.print_info("Cell menu button found!")
            self.auto_actions.click(cell_menu_button)
            self.utils.print_info("Clicking on filter type dropdown")
            filter_type_dropdown = self.login_web_elements.get_filter_type_dropdown()
            if filter_type_dropdown:
                self.utils.print_info("Found the filter type dropdown!")
                self.auto_actions.click(filter_type_dropdown)
                sleep(2)
                filter_dropdown_option_equals = self.login_web_elements.get_filter_dropdown_option_equals()
                if filter_dropdown_option_equals:
                    self.utils.print_info("Found filter dropdown option: Equals")
                    self.auto_actions.click(filter_dropdown_option_equals)
                else:
                    kwargs['fail_msg'] = "Unable to find dropdown option: Equals"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to click filter type dropdown."
                self.common_validation.fault(**kwargs)
                return -1
            filter_text_box = self.login_web_elements.get_filter_text_box()
            if filter_text_box:
                self.utils.print_info("Found the filter text box!")
                self.auto_actions.send_keys(filter_text_box, customer_name)
            else:
                kwargs['fail_msg'] = "Unable to find the filter text box!"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to find cell menu button."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(3)
        user_found = self.login_web_elements.get_user_found()
        if user_found:
            if len(user_found) == 1:
                self.utils.print_info(user_found[0].text)
                sleep(5)
                self.utils.print_info("Found user!")
                self.utils.print_info("Deleting user...")
                self.auto_actions.click(user_found[0])
            else:
                kwargs['fail_msg'] = "Multiple users were found "
                self.common_validation.failed(**kwargs)
                return -1
            delete_button = self.login_web_elements.get_delete_button()
            if delete_button:
                self.utils.print_info("Found delete button!")
                sleep(2)
                self.auto_actions.click(delete_button)
                sleep(2)
                self.screen.save_screen_shot()
                confirmation_option_yes = self.login_web_elements.get_confirmation_option_yes()
                if confirmation_option_yes:
                    self.utils.print_info("Found the confirmation option!")
                    self.auto_actions.click(confirmation_option_yes)
                else:
                    self.utils.print_info("Unable to find confirmation option!")
                    kwargs['fail_msg'] = "Unable to find confirmation option!"
                    self.common_validation.fault(**kwargs)
                    return -1
                sleep(5)
                self.screen.save_screen_shot()
                delete_confirmation = self.login_web_elements.get_delete_confirmation()
                if delete_confirmation:
                    self.utils.print_info("Delete confirmation has been found!")
                    self.utils.print_info(delete_confirmation.text)
                    return 1
                else:
                    self.utils.print_info("Confirmation hasn't been found!")
            else:
                kwargs['fail_msg'] = "Unable to find delete button."
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['pass_msg'] = "The user has already been deleted or it hasn't been created."
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['pass_msg'] = "The account is deleted"
        self.common_validation.passed(**kwargs)
        return 1

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def log_out_portal(self, **kwargs):
        """
        This function logs out from portal
        :return: returns 1 if logging out was succesfull or -1 if otherwise
        """
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking LOGOUT button...")
        log_out_button_portal = self.login_web_elements.get_log_out_button_portal()
        if log_out_button_portal:
            self.utils.print_info("Found LOGOUT button!")
            self.auto_actions.click(log_out_button_portal)
            self.utils.print_info("Successfully logged out!")
            kwargs['pass_msg'] = "Successfully logged out!"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Unable to find LOGOUT button.")
            kwargs['fail_msg'] = "Unable to find LOGOUT button."
            self.common_validation.failed(**kwargs)
            return -1

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def get_portal_url(self, sw_connection_host, **kwargs):
        """
        :param sw_connection_host: the url of the RDC
        :return: the url of portal page ; else -1
        """

        pattern1 = "(\\w+)r\\d+."
        gdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
        self.utils.print_info("GDC is : ", gdc[0])
        if isinstance(gdc, list):
            if isinstance(gdc[0], str):
                url = "https://" + gdc[0] + "-portal.qa.xcloudiq.com/portal/"
                self.utils.print_info("url is : ", url)
                return url
            else:
                kwargs['fail_msg'] = "Can not return url of RDC"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not get gdc"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated, to use it please move it to keywords/gui/login/KeywordsLogin.py')
    def check_if_xiq_user_exists(self, customer_name, **kwargs):
        """
        This function check if the XIQ user exists into portal page
        :param customer_name:   the name of the customer under which the account was created
        :return: returns 1 if the account user doesn't exist; else -1
        """

        self.screen.save_screen_shot()
        self.utils.print_info("Clicking on name cell menu button ...")
        cell_menu_button = self.login_web_elements.get_cell_menu_button_name_section()
        if cell_menu_button:
            self.utils.print_info("Cell menu button found!")
            self.auto_actions.click(cell_menu_button)
            self.utils.print_info("Clicking on filter type dropdown")
            filter_type_dropdown = self.login_web_elements.get_filter_type_dropdown()
            if filter_type_dropdown:
                self.utils.print_info("Found the filter type dropdown!")
                self.auto_actions.click(filter_type_dropdown)
                sleep(2)
                filter_dropdown_option_equals = self.login_web_elements.get_filter_dropdown_option_equals()
                if filter_dropdown_option_equals:
                    self.utils.print_info("Found filter dropdown option: Equals")
                    self.auto_actions.click(filter_dropdown_option_equals)
                else:
                    kwargs['fail_msg'] = "Unable to find dropdown option: Equals"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Unable to click filter type dropdown."
                self.common_validation.fault(**kwargs)
                return -1
            filter_text_box = self.login_web_elements.get_filter_text_box()
            if filter_text_box:
                self.utils.print_info("Found the filter text box!")
                self.auto_actions.send_keys(filter_text_box, customer_name)
            else:
                kwargs['fail_msg'] = "Unable to find the filter text box!"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to find cell menu button."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(3)
        user_found = self.login_web_elements.get_user_found()
        if user_found:
            if len(user_found) == 1:
                self.utils.print_info(user_found[0].text)
                sleep(5)
                kwargs['fail_msg'] = "Found user!"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                kwargs['fail_msg'] = "Multiple users were found"
                self.common_validation.failed(**kwargs)
                self.screen.save_screen_shot()
                return -1
        else:
            kwargs['pass_msg'] = "The user has already been deleted or it hasn't been created."
            self.common_validation.passed(**kwargs)
            return 1
        # return 1 < This code is unreachable?