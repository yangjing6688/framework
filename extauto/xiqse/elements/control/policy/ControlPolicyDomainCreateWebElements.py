from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainCreateWebElementsDefinitions import *

class ControlPolicyDomainCreateWebElements(ControlPolicyDomainCreateWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_create_domain_domain_name_field(self):
        """
        :return:  "Domain Name field in Create Domain window"
        """
        return self.weh.get_element(self.create_domain_domain_name_field)

    def get_create_domain_ok_button(self):
        """
        :return:  "OK button in Create Domain window"
        """
        return self.weh.get_element(self.create_domain_ok_button)

    def get_create_domain_cancel_button(self):
        """
        :return:  "Cancel button in Create Domain window"
        """
        return self.weh.get_element(self.create_domain_cancel_button)

    def get_create_domain_success_msg(self):
        """
        :return:  "Create domain successful message"
        """
        return self.weh.get_element(self.create_domain_success_msg)

    def get_create_domain_success_ok_button(self):
        """
        :return:  "OK button in Create Domain Success dialog"
        """
        return self.weh.get_element(self.create_domain_success_ok_button)

    def get_create_domain_error_msg(self):
        """
        :return:  "Create domain error message"
        """
        return self.weh.get_element(self.create_domain_error_msg)

    def get_create_domain_error_ok_button(self):
        """
        :return:  "OK button in Create Domain error dialog"
        """
        return self.weh.get_element(self.create_domain_success_ok_button)