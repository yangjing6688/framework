from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.control.policy.ControlPolicyServiceDeleteWebElementsDefinitions import ControlPolicyServiceDeleteWebElementsDefinitions


class ControlPolicyServiceDeleteWebElements(ControlPolicyServiceDeleteWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_delete_service_menu(self):
        return self.weh.get_element(self.delete_service_menu)

    def get_confirm_window(self):
        return self.weh.get_element(self.confirm_window)

    def get_yes_button(self):
        return self.weh.get_element(self.yes_button)

    def get_no_button(self):
        return self.weh.get_element(self.no_button)
