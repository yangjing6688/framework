from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.control.policy.ControlPolicyDomainOpenWebElementsDefinitions import ControlPolicyDomainOpenWebElementsDefinitions

class ControlPolicyDomainOpenWebElements(ControlPolicyDomainOpenWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_domain_name(self, domain_name):
        """
        :return:  "Open domain dropdown list"
        """
        return self.weh.get_template_element(self.domain_els_active_template, d_name=domain_name)
