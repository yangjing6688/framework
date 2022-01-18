from time import sleep
import common.CloudDriver
from common.AutoActions import AutoActions
from common.GmailHandler import GmailHandler
from common.Utils import Utils
import xiq.flows.common.ToolTipCapture as tool_tip
from xiq.elements.PasswordResetWebElements import PasswordResetWebElements


class PasswordReset:
    def __init__(self):
        self.driver = common.CloudDriver.cloud_driver
        self.pw_web_elements = PasswordResetWebElements()
        self.auto_actions = AutoActions()
        self.gm_handler = GmailHandler()
        self.utils = Utils()

    def add_account(self, name, _email):
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
        self.auto_actions.click(self.pw_web_elements.get_account_icon())
        sleep(5)

        self.utils.print_info("clicking on global settings")
        self.auto_actions.click(self.pw_web_elements.get_global_settings())
        sleep(5)

        self.utils.print_info("clicking on account management")
        self.auto_actions.click(self.pw_web_elements.get_account_management())
        sleep(5)

        result = self.pw_web_elements.get_user_table()
        for res in result:
            if _email in res.text:
                self.utils.print_info("yes!....the email  is already present")
                self.auto_actions.click(res)
                self.auto_actions.click(self.pw_web_elements.get_delete_icon())
                sleep(5)

                self.auto_actions.click(self.pw_web_elements.get_delete_alert())
            self.utils.print_info("popup : ", res.text)

        self.utils.print_info("clicking on add account")
        self.auto_actions.click(self.pw_web_elements.get_add_account())
        sleep(3)

        self.utils.print_info("Entering Email: ", _email)
        self.auto_actions.send_keys(self.pw_web_elements.get_email_textbox(), _email)
        sleep(2)

        self.utils.print_info("Entering Name: ", name)
        self.auto_actions.send_keys(self.pw_web_elements.get_name_textbox(), name)
        sleep(2)

        self.utils.print_info("Clicking on save and close...")
        self.auto_actions.click(self.pw_web_elements.get_save_button())
        sleep(10)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "already exists. Please try again using a different email address" in value:
                self.utils.print_info(value)
                return -1
        return 1

    def get_link(self, _email, _password):
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

    def password_reset(self, name, _email, _password):
        """
        - Create administrative account and get the password reset link
        -  Flow Global Settings --> Account Management
        - Keyword Usage:
         - ``Password Reset   ${NAME}   ${EMAIL}   ${PASSWORD}

        :param name:
        :param _email:
        :param _password:
        :return: pasword reset link
        """

        self.utils.print_info("clicking on account icon")
        self.auto_actions.click(self.pw_web_elements.get_account_icon())
        sleep(3)

        self.utils.print_info("clicking on global settings")
        self.auto_actions.click(self.pw_web_elements.get_global_settings())
        sleep(3)

        self.utils.print_info("clicking on account management")
        self.auto_actions.click(self.pw_web_elements.get_account_management())
        sleep(3)

        result = self.pw_web_elements.get_user_table()
        for res in result:
            if _email in res.text:
                self.utils.print_info("yes!....the email  is already present")
                self.auto_actions.click(res)
                self.auto_actions.click(self.pw_web_elements.get_delete_icon())
                sleep(5)

                self.auto_actions.click(self.pw_web_elements.get_delete_alert())
            self.utils.print_info("popup : ", res.text)

        self.utils.print_info("clicking on add account")
        self.auto_actions.click(self.pw_web_elements.get_add_account())
        sleep(3)

        self.utils.print_info("Entering Email: ", _email)
        self.auto_actions.send_keys(self.pw_web_elements.get_email_textbox(), _email)
        sleep(2)

        self.utils.print_info("Entering Name: ", name)
        self.auto_actions.send_keys(self.pw_web_elements.get_name_textbox(), name)
        sleep(2)

        self.utils.print_info("Clicking on save and close...")
        self.auto_actions.click(self.pw_web_elements.get_save_button())
        sleep(10)

        reset_link = self.gm_handler.get_url_to_set_password_for_new_user(_email, _password)
        self.utils.print_info("Redirecting URL: ", reset_link)

        return reset_link
