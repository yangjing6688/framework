from extauto.xiq.defs.ClassificationRuleWebElementDefinition import *
from extauto.common.WebElementHandler import *


class ClassificationRuleWebElements(ClassificationRuleWebElementDefinition):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_classification_rule_add_button(self):
        return self.weh.get_element(self.add_classification_rule)

    def get_classification_option_add_button(self):
        return self.weh.get_element(self.add_classification_option)

    def get_classification_rule_name_text(self):
        return self.weh.get_element(self.add_classification_rule_name)

    def get_classification_rule_description_text(self):
        return self.weh.get_element(self.add_classification_rule_desc)

    def get_classification_rule_option(self):
        return self.weh.get_elements(self.get_classification_all_option)

    def get_ccg_policy_drop_down_items(self):
        return self.weh.get_elements(self.get_ccg_policy_drop_down_item)

    def get_ccg_policy_select_option(self):
        return self.weh.get_element(self.get_ccg_policy_select_option_button)

    def get_continue_button(self):
        return self.weh.get_element(self.get_continue_buttons)

    def get_save_rule_button(self):
        return self.weh.get_element(self.get_save_rule)

    def get_org_loc_button(self):
        return self.weh.get_element(self.get_org_loc)

    def get_node_location(self):
        return self.weh.get_elements(self.get_country_locations)

    def get_location_node_open_icon(self, node):
        return self.weh.get_element(self.get_location_node_icon, node)

    def select_loc_assign_button(self):
        return self.weh.get_element(self.select_loc_assign)

    def get_ip_object_add_button(self):
        return self.weh.get_element(self.get_ip_object_add)

    def get_ip_object_name(self):
        return self.weh.get_element(self.get_ip_addr_object_name)

    def get_ip_object_ip(self):
        return self.weh.get_element(self.get_ip_addr_object_ip)

    def get_ip_object_save(self):
        return self.weh.get_element(self.get_ip_addr_object_save)

    def get_ip_object_subnet(self):
        return self.weh.get_element(self.get_ip_addr_object_subnet)

    def get_ip_object_mask(self):
        return self.weh.get_element(self.get_ip_addr_object_mask)

    def get_ip_range_from(self):
        return self.weh.get_element(self.get_ip_addr_range_from)

    def get_ip_range_to(self):
        return self.weh.get_element(self.get_ip_addr_range_to)

    def enable_classification_rule(self):
        return self.weh.get_element(self.enable_classification_rule_checkbox)

    def select_classification_rule(self, row):
        return self.weh.get_element(self.select_classification_rules, row)

    def get_classification_rule(self, row):
        return self.weh.get_elements(self.get_classification_rules, row)

    def get_all_classification_rule(self):
        return self.weh.get_elements(self.get_all_classification_rules)

    def view_all_classification_rule(self):
        return self.weh.get_elements(self.view_all_classification_rules)

    def view_all_pages(self):
        return self.weh.get_element(self.view_all_page)

    def get_link_button(self):
        return self.weh.get_element(self.get_rule_link_button)

    def get_next_button(self):
        return self.weh.get_element(self.click_next_button)

    def delete_classification_rule_from_ssid(self, row):
        return self.weh.get_element(self.delete_classification_rule_from_ssids, row)

    def select_classification_rule_from_common_object(self, row):
        return self.weh.get_element(self.select_classification_rule_from_common_obj, row)

    def delete_classification_rule_from_common_object(self):
        return self.weh.get_element(self.delete_classification_rule_from_common_obj)

    def get_confirmation_dialog_yes_button(self):
        return self.weh.get_element(self.confirmation_dialog_yes_button)
