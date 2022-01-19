from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainEnforceWebElementsDefinitions import *


class ControlPolicyDomainEnforceWebElements(ControlPolicyDomainEnforceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Enforce Domain
    def get_enforce_domain_data_question(self):
        """
        :return:  "'Enforce domain data' message in the popup dialog"
        """
        return self.weh.get_element(self.enforce_domain_data_question)

    def get_enforce_domain_data_yes_button(self):
        """
        :return:  "'Yes' button in the popup Confirmation dialog"
        """
        return self.weh.get_element(self.enforce_domain_data_yes_button)

    def get_enforce_domain_data_no_button(self):
        """
        :return:  "'No' button in the popup Confirmation dialog"
        """
        return self.weh.get_element(self.enforce_domain_data_no_button)

    def get_enforce_domain_success_msg(self):
        """
        :return:  "Enforce success message"
        """
        return self.weh.get_element(self.enforce_domain_success_msg)

    def get_enforce_domain_success_ok_bttn(self):
        """
        :return:  "OK button in the Enforce success dialog"
        """
        return self.weh.get_element(self.enforce_domain_success_ok_bttn)

    def get_enforce_domain_errors_warnings_msg(self):
        """
        :return:  "Enforce errors/warnings message"
        """
        return self.weh.get_element(self.enforce_domain_errors_warnings_msg)

    def get_enforce_domain_errors_warnings_ok_bttn(self):
        """
        :return:  "OK button in the Enforce Errors/Warnings dialog"
        """
        return self.weh.get_element(self.enforce_domain_errors_warnings_ok_bttn)
    # end of Enforce Domain
