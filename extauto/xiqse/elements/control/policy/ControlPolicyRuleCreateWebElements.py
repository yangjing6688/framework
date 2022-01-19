from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyRuleCreateWebElementsDefinitions import ControlPolicyRuleCreateWebElementsDefinitions


class ControlPolicyRuleCreateWebElements(ControlPolicyRuleCreateWebElementsDefinitions):
    
    def __init__(self):
        self.weh = WebElementHandler()

    def get_create_rule_menu(self):
        return self.weh.get_element(self.create_rule_menu)

    def get_window(self):
        return self.weh.get_element(self.create_rule_window)

    def get_name_input(self):
        return self.weh.get_element(self.name_input)

    def get_ok_button(self):
        return self.weh.get_element(self.ok_button)

    def get_cancel_button(self):
        return self.weh.get_element(self.cancel_button)
