from common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainSaveWebElementsDefinitions import *


class ControlPolicyDomainSaveWebElements(ControlPolicyDomainSaveWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()


    # Save Domain
    def get_save_ok_bttn(self):
        """
        :return:  "OK button in the Save Domain confirmation dialog"
        """
        return self.weh.get_element(self.save_ok_bttn)

    def get_save_success_msg(self):
        """
        :return:  "Save Domain confirmation message"
        """
        return self.weh.get_element(self.save_success_msg)
    # end Save Domain
