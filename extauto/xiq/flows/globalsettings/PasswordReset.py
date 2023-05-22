# Standard Keyword imports 
from extauto.common.CommonValidation import CommonValidation 
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.GmailHandler import GmailHandler
from extauto.common.Utils import Utils
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.PasswordResetWebElements import PasswordResetWebElements
from ExtremeAutomation.Utilities.deprecated import deprecated


class PasswordReset(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance 
        if hasattr(self, 'initialized'): 
            return 
        self.initialized = True 
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.pw_web_elements = PasswordResetWebElements()
        self.auto_actions = AutoActions()
        self.gm_handler = GmailHandler()
        self.utils = Utils()
        self.common_validation = CommonValidation()

    @deprecated('Please use the {add_account} keyword in keywords/gui/passwordreset/KeywordsPasswordReset.py'
                'This method can be removed after 7/1/2023')
    def add_account(self, name, _email, **kwargs):
        return self.gui_add_account(name, _email, **kwargs)
        
    def gui_add_account(self, name, _email, **kwargs):
        """
        - adds an account under account management
        - Adding administrative account
        - Flow Global Settings --> Account Management
        - Keyword Usage:
        - ``Add Account  ${NAME}   ${EMAIL``

        :param name:
        :param _email:
        :return: 1 if account created else -1
        """
        self.utils.print_info("clicking on account icon..")
        self.auto_actions.click_reference(self.pw_web_elements.get_account_icon)
        sleep(5)

        self.utils.print_info("clicking on global settings")
        self.auto_actions.click_reference(self.pw_web_elements.get_global_settings)
        sleep(5)

        self.utils.print_info("clicking on account management")
        self.auto_actions.click_reference(self.pw_web_elements.get_account_management)
        sleep(5)

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

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "already exists. Please try again using a different email address" in value:
                self.utils.print_info(value)
                kwargs['fail_msg'] = "Failed to  add(create) account"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['pass_msg'] = "Successfully added(created) account"
        self.common_validation.passed(**kwargs)
        return 1

    @deprecated('Please use the {get_link} keyword in keywords/gui/passwordreset/KeywordsPasswordReset.py'
                'This method can be removed after 7/1/2023')
    def get_link(self, _email, _password):
        return self.gui_get_link(_email, _password)

    def gui_get_link(self, _email, _password):
        """
        - Get the url link for password set to new account sent to email
        - Keyword Usage:
        - ``Get Link   ${EMAIL}   ${PASSWORD}``

        :param _email:
        :param _password:
        :return: password reset link
        """
        link = self.gm_handler.get_url_to_set_password_for_new_user(_email, _password)
        self.utils.print_info("Redirecting URL: ", link)
        return link
