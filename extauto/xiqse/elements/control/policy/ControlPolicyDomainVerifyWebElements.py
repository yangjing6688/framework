from common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainVerifyWebElementsDefinitions import *


class ControlPolicyDomainVerifyWebElements(ControlPolicyDomainVerifyWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Verify Domain
    def get_verify_domain_success_msg(self):
        """
        :return:  "Verify Domain success message"
        """
        return self.weh.get_element(self.verify_domain_success_msg)

    def get_verify_domain_success_ok_bttn(self):
        """
        :return:  "OK button in the Verify success dialog"
        """
        return self.weh.get_element(self.verify_domain_success_ok_bttn)

    def get_verify_domain_fail_msg(self):
        """
        :return:  "Verify errors message"
        """
        return self.weh.get_element(self.verify_domain_fail_msg)

    def get_verify_domain_fail_ok_bttn(self):
        """
        :return:  "OK button in the Verify Failure dialog"
        """
        return self.weh.get_element(self.verify_domain_fail_ok_bttn)

    def get_cannot_verify_domain_error_msg(self):
        """
        :return:  "Cannot verify domain errors message"
        """
        return self.weh.get_element(self.cannot_verify_domain_error_msg)

    def get_cannot_verify_domain_ok_bttn(self):
        """
        :return:  "OK button in the Cannot verify domain error dialog"
        """
        return self.weh.get_element(self.cannot_verify_domain_ok_bttn)
    # end of Verify Domain