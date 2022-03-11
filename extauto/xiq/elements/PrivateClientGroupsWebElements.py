from xiq.defs.PrivateClientGroupsDefinitions import *
from common.WebElementHandler import WebElementHandler


class PrivateClientGroupsWebElements(PrivateClientGroupsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()


    def get_private_client_grp_default_network_policy(self):
        return self.weh.get_element(self.private_client_grp_default_network_policy)

    def get_private_client_grp_network_policy_drop_down_list_items(self):
        return self.weh.get_elements(self.private_client_grp_network_policy_drop_down_list_items)

    def get_private_client_grp_ap_based_groups_tab(self):
        return self.weh.get_element(self.private_client_grp_ap_based_groups_tab)

    def get_private_client_grp_key_based_groups_tab(self):
        return self.weh.get_element(self.private_client_grp_key_based_groups_tab)

    def get_private_client_grp_enable_ap_based_on_off_button(self):
        return self.weh.get_element(self.private_client_grp_enable_ap_based_on_off_button)

    def get_private_client_grp_enable_key_based_on_off_button(self):
        return self.weh.get_element(self.private_client_grp_enable_key_based_on_off_button)

    def get_private_delete_room_button(self):
        return self.weh.get_element(self.private_client_grp_delete_room_button)

    def get_private_client_grp_add_room_button(self):
        return self.weh.get_element(self.private_client_grp_add_room_button)

    def get_private_client_grp_all_rooms_checkbox(self):
        return self.weh.get_element(self.private_client_grp_all_rooms_checkbox)

    def get_private_ap_based_room_table_headers(self):
        return self.weh.get_elements(self.private_ap_based_room_table_headers)

    def get_private_ap_based_room_table_cells(self):
        return self.weh.get_elements(self.private_ap_based_room_total_cells)

    def get_ap_based_room_input(self):
        return self.weh.get_element(self.private_ap_based_room_input_text)

    def get_private_ap_based_room_user_assigned_drop_down(self):
        return self.weh.get_elements(self.private_ap_based_room_user_assigned_drop_down)

    def get_private_ap_based_room_user_assigned_enter_text(self):
        return self.weh.get_elements(self.private_ap_based_room_user_assigned_enter_text)

    def get_room_user_assigned_drop_down_items(self):
        return self.weh.get_elements(self.room_user_assigned_drop_down_items)

    def get_diag_confirm_yes_button(self):
        return self.weh.get_element(self.diag_confirm_yes_button)

    def get_private_client_grp_save_setting_button(self):
        return self.weh.get_element(self.private_client_grp_save_setting_button)

    def get_private_key_based_group_add_button(self):
        return self.weh.get_element(self.private_key_based_group_add_button)

    def get_private_key_based_group_delete_button(self):
        return self.weh.get_element(self.private_key_based_group_delete_button)

    def get_private_key_based_save_info_button(self):
        return self.weh.get_element(self.private_key_based_save_info_button)

    def get_private_key_based_delete_checkbox_all(self):
        return self.weh.get_element(self.private_key_based_delete_checkbox_all)

    def get_private_key_based_table_header(self):
        return self.weh.get_elements(self.private_key_based_table_header)

    def get_private_key_based_all_cells(self):
        return self.weh.get_elements(self.private_key_based_all_cells)

    def get_private_user_select_dropdown(self):
        return self.weh.get_elements(self.private_user_select_key_based_group)

    def get_private_user_search_key_based_group_text(self):
        return self.weh.get_element(self.private_user_search_key_based_group_text)

    def get_private_user_key_based_group_items(self):
        return self.weh.get_element(self.private_user_key_based_group_items)