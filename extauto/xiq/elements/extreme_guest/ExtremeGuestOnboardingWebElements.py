from extauto.xiq.defs.extreme_guest.ExtremeGuestOnboardingWebElementsDefs import ExtremeGuestOnboardingWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestOnboardingWebElements(ExtremeGuestOnboardingWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_onboarding_policy_tab(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_tab)

    def get_extreme_guest_onboarding_policy_add_policy(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_policy)

    def get_extreme_guest_onboarding_policy_refresh_policy(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_refresh_policy)

    def get_extreme_guest_onboarding_policy_delete_policy(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_delete_policy)

    def get_extreme_guest_onboarding_policy_add_name(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_name)

    def get_extreme_guest_onboarding_policy_add_condition_dropdown(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_condition_dropdown)

    def get_extreme_guest_onboarding_policy_add_condition_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_policy_add_condition_dropdown_items)

    def get_extreme_guest_onboarding_policy_add_condition_dropdown_value(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_condition_dropdown_value)

    def get_extreme_guest_onboarding_policy_add_action_dropdown(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_action_dropdown)

    def get_extreme_guest_onboarding_policy_add_action_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_policy_add_action_dropdown_items)

    def get_extreme_guest_onboarding_policy_add_group_select_dropdown(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_group_select_dropdown)

    def get_extreme_guest_onboarding_policy_add_group_select_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_policy_add_group_select_dropdown_items)

    def get_extreme_guest_onboarding_policy_add_save_button(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_save_button)

    def get_extreme_guest_onboarding_policy_add_cancel_button(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_cancel_button)

    def get_extreme_guest_onboarding_policy_add_save_ok_button(self):
        return self.weh.get_element(self.extreme_guest_onboarding_policy_add_save_ok_button)

    def get_extreme_guest_onboarding_rule_tab(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_tab)

    def get_extreme_guest_onboarding_rule_add_rule(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_rule)

    def get_extreme_guest_onboarding_rule_add_name(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_name)

    def get_extreme_guest_onboarding_rule_add_policy_dropdown(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_policy_dropdown)

    def get_extreme_guest_onboarding_rule_add_policy_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_add_policy_dropdown_items)

    def get_extreme_guest_onboarding_rule_add_network_dropdown(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_network_dropdown)

    def get_extreme_guest_onboarding_rule_add_network_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_add_network_dropdown_items)

    def get_extreme_guest_onboarding_rule_add_location_dropdown(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_location_dropdown)

    def get_extreme_guest_onboarding_rule_add_location_dropdown_items(self):
        # Need to update later
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_location_dropdown_items)

    def get_extreme_guest_onboarding_rule_add_save_button(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_save_button)

    def get_extreme_guest_onboarding_rule_add_save_ok_button(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_save_ok_button)

    def get_extreme_guest_onboarding_rule_add_cancel_button(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_add_cancel_button)

    def get_extreme_guest_onboarding_rule_refresh_rule(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_refresh_rule)

    def get_extreme_guest_onboarding_rule_delete_rule(self):
        return self.weh.get_element(self.extreme_guest_onboarding_rule_delete_rule)

    def get_extreme_guest_onboarding_rule_locations_root_name(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_root_name)

    def get_extreme_guest_onboarding_rule_locations_city_name(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_city_name)

    def get_extreme_guest_onboarding_rule_locations_building_name(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_building_name)

    def get_extreme_guest_onboarding_rule_locations_floor_name(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_floor_name)

    def get_extreme_guest_onboarding_rule_locations_root_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_root_name_expand_button)

    def get_extreme_guest_onboarding_rule_locations_city_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_city_name_expand_button)

    def get_extreme_guest_onboarding_rule_locations_building_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_onboarding_rule_locations_building_name_expand_button)

    def get_extreme_guest_users_add_create_bulk_vouchers_location_dropdown(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_vouchers_location_dropdown)