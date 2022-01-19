from extauto.common.WebElementHandler import *
from xiq.defs.PpskClassificationWebElementDefinition import *


class PpskClassificationWebElements(PpskClassificationWebElementDefinition):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_ppsk_classification_network_dropdown(self):
        return self.weh.get_element(self.get_network_dropdown)

    def get_all_networks_from_dropdown(self):
        return self.weh.get_elements(self.get_all_network_from_dropdown)

    def get_ppsk_classification_rule_add_button(self):
        return self.weh.get_element(self.get_ppsk_classification_add_button)

    def get_ppsk_classification_users_dropdown(self):
        return self.weh.get_element(self.get_ppsk_classification_user_dropdown)

    def get_ppsk_classification_users_list(self):
        return self.weh.get_elements(self.get_ppsk_classification_user_list)

    def get_add_user_button(self):
        return self.weh.get_element(self.add_user_button)

    def get_select_classification_rule_button(self):
        return self.weh.get_element(self.select_classification_rule_button)

    def get_classification_all_rule(self):
        return self.weh.get_elements(self.classification_all_rule)

    def get_link_button(self):
        return self.weh.get_element(self.link_button)

    def get_save_button(self):
        return self.weh.get_element(self.save_button)

    def get_ppsk_classification_users_row(self):
        return self.weh.get_elements(self.ppsk_classification_users_row)

    def get_edit_button(self, row):
        return self.weh.get_element(self.edit_button, row)

    def get_user_select_classification_rule_button(self, row):
        return self.weh.get_element(self.user_select_classification_rule_button, row)

    def get_user_assigned_classification_rule(self, row):
        return self.weh.get_element(self.user_assigned_classification_rule, row)

    def get_select_all_ppsk_users(self):
        return self.weh.get_element(self.select_all_ppsk_users)

    def get_delete_ppsk_user(self):
        return self.weh.get_element(self.delete_ppsk_user)

    def get_yes_confirmation_button(self):
        return self.weh.get_element(self.yes_confirmation_button)
