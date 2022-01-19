from common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyServiceCreateWebElementsDefinitions import ControlPolicyServiceCreateWebElementsDefinitions


class ControlPolicyServiceCreateWebElements(ControlPolicyServiceCreateWebElementsDefinitions):
    
    def __init__(self):
        self.weh = WebElementHandler()

    def get_create_service_menu(self):
        return self.weh.get_element(self.create_service_menu)

    def get_window(self):
        return self.weh.get_element(self.create_service_window)

    def get_name_input(self):
        return self.weh.get_element(self.name_input)

    def get_ok_button(self):
        return self.weh.get_element(self.ok_button)

    def get_cancel_button(self):
        return self.weh.get_element(self.cancel_button)

    def get_name_in_use_error(self):
        return self.weh.get_element(self.name_in_use_error)

    def get_error_ok_button(self):
        return self.weh.get_element(self.error_ok_button)
