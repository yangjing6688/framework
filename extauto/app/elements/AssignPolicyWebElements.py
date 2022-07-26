from app.defs.AssignPolicyDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *


class AssignPolicyWebElements(AssignPolicyDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_assign_policy(self):
        return self.weh.get_element(self.assign_policy_id)

    def assign_policy_yes_button(self):
        return self.weh.get_element(self.assign_policy_yes_button_id)

    def assign_policy_cancel_button(self):
        return self.weh.get_element(self.assign_policy_cancel_button_id)

    def get_update_policy(self):
        return self.weh.get_element(self.update_policy_id)

    def get_update_policy_confirm(self):
        return self.weh.get_element(self.update_policy_confirm_id)

    def get_update_policy_cancel(self):
        return self.weh.get_element(self.update_policy_cancel_id)

    def get_np_backward_link(self):
        return self.weh.get_element(self.np_backward_link_id)