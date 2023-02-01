from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.control.policy.ControlPolicyCreateRoleWebElementsDefinitions import ControlPolicyCreateRoleWebElementsDefinitions


class ControlPolicyCreateRoleWebElements(ControlPolicyCreateRoleWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_window(self):
        return self.weh.get_displayed_element(self.weh.get_elements(self.window))

    def get_name_input(self):
        return self.weh.get_displayed_element(self.weh.get_elements(self.name_input))

    def get_ok_button(self):
        return self.weh.get_displayed_element(self.weh.get_elements(self.ok_button))