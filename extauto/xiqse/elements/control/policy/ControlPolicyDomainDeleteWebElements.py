from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainDeleteWebElementsDefinitions import *

class ControlPolicyDomainDeleteWebElements(ControlPolicyDomainDeleteWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_delete_domain_name_list(self):
        """
        :return:  "Delete domain name dropdown list"
        """
        return self.weh.get_element(self.delete_domain_name_list)

    def select_delete_domain_name(self, domain_name):
        """
        :return:  "domain name that is about to be deleted"
        """
        return self.weh.get_template_element(self.delete_domain_name_template, d_name=domain_name)

    def get_delete_domain_ok(self):
        """
        :return:  "OK button in the Delete Domain window"
        """
        return self.weh.get_element(self.delete_domain_ok)

    def get_delete_domain_close_button(self):
        """
        :return:  "Close button in the Delete Domain window"
        """
        return self.weh.get_element(self.delete_domain_close)

    def get_delete_domain_yes_button(self):
        """
        :return:  "Yes button in the Are You Sure? dialog during the Delete Domain process"
        """
        return self.weh.get_element(self.delete_domain_yes)

    def get_delete_domain_confirm_ok(self):
        """
        :return:  "OK button in the Domain Deleted Successfully dialog"
        """
        return self.weh.get_element(self.delete_domain_confirm_ok)