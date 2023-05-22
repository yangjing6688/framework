""" This file contains code for keywords that have been archived.
    If the keywords need to be available again copy the code to xiq/flows/common/Login.py
    and implement the keyword move process.
    Instructions for moving a keyword can be found here:
    https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords """

# All Archived keywords will be deleted after December 2023

# Standard Keyword imports
from ExtremeAutomation.Utilities.deprecated import deprecated
from extauto.common.CommonValidation import CommonValidation
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.GmailHandler import GmailHandler
from extauto.common.Utils import Utils
from extauto.xiq.elements.PasswordResetWebElements import PasswordResetWebElements


class PasswordReset(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance 
        if hasattr(self, 'initialized'): 
            return 
        self.initialized = True
        self.pw_web_elements = PasswordResetWebElements()
        self.auto_actions = AutoActions()
        self.gm_handler = GmailHandler()
        self.utils = Utils()
        self.common_validation = CommonValidation()

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location '
                'and complete the keyword move process. Instructions for moving keywords can be found here:'
                'https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def password_reset(self, name, _email, _password):
        """
        - Create administrative account and get the password reset link
        -  Flow Global Settings --> Account Management
        - Keyword Usage:
        - ``Password Reset   ${NAME}   ${EMAIL}   ${PASSWORD}

        :param name:
        :param _email:
        :param _password:
        :return: password reset link
        """

        self.utils.print_info("clicking on account icon")
        self.auto_actions.click_reference(self.pw_web_elements.get_account_icon)
        sleep(3)

        self.utils.print_info("clicking on global settings")
        self.auto_actions.click_reference(self.pw_web_elements.get_global_settings)
        sleep(3)

        self.utils.print_info("clicking on account management")
        self.auto_actions.click_reference(self.pw_web_elements.get_account_management)
        sleep(3)

        result = self.pw_web_elements.get_user_table()
        for res in result:
            if _email in res.text:
                self.utils.print_info("yes!....the email  is already present")
                self.auto_actions.click(res)
                self.auto_actions.click_reference(self.pw_web_elements.get_delete_icon)
                sleep(5)

                self.auto_actions.click_reference(self.pw_web_elements.get_delete_alert)
            self.utils.print_info("popup : ", res.text)

        self.utils.print_info("clicking on add account")
        self.auto_actions.click_reference(self.pw_web_elements.get_add_account)
        sleep(3)

        self.utils.print_info("Entering Email: ", _email)
        self.auto_actions.send_keys(self.pw_web_elements.get_email_textbox(), _email)
        sleep(2)

        self.utils.print_info("Entering Name: ", name)
        self.auto_actions.send_keys(self.pw_web_elements.get_name_textbox(), name)
        sleep(2)

        self.utils.print_info("Clicking on save and close...")
        self.auto_actions.click_reference(self.pw_web_elements.get_save_button)
        sleep(10)

        reset_link = self.gm_handler.get_url_to_set_password_for_new_user(_email, _password)
        self.utils.print_info("Redirecting URL: ", reset_link)

        return reset_link
