from extauto.common.WebElementHandler import *
from xiq.defs.AdvOnboardDefs import *


class AdvOnboardWebElements(AdvOnboardDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_devices_add_button(self):
        return self.weh.get_element(self.devices_add_button)

    def get_adv_onboard_add_menu_item(self):
        return self.weh.get_element(self.adv_onboard_add_menu_item)

    def get_onboard_icon(self):
        return self.weh.get_element(self.onboard_icon)

    def get_real_devices_radio_button(self):
        return self.weh.get_element(self.real_devices_radio_button)

    def get_add_dev_dev_type_sim(self):
        return self.weh.get_element(self.add_dev_dev_type_sim)

    def get_simulated_device_drop_down(self):
        return self.weh.get_element(self.simulated_device_drop_down)

    def get_simulated_device_drop_down_opts(self):
        return self.weh.get_elements(self.simulated_device_drop_down_opts)

    def get_extreme_aerohive_device_tab(self):
        return self.weh.get_element(self.extreme_aerohive_device_tab)

    def get_add_dev_dell_button(self):
        return self.weh.get_element(self.add_dev_dell_button)

    def get_exos_device_tab(self):
        return self.weh.get_element(self.exos_device_tab)

    def get_voss_device_tab(self):
        return self.weh.get_element(self.voss_device_tab)

    def get_add_dev_wing_button(self):
        return self.weh.get_element(self.add_dev_wing_button)

    def get_adv_onboard_serial_text_area(self):
        return self.weh.get_element(self.adv_serial_text_area)

    def get_add_dev_ext_aerohive_import_choose(self):
        return self.weh.get_element(self.add_dev_ext_aerohive_import_choose)

    def get_add_dev_dell_service_tag(self):
        return self.weh.get_element(self.add_dev_dell_service_tag)

    def get_add_dev_dell_serial_num(self):
        return self.weh.get_element(self.add_dev_dell_serial_num)

    def get_add_dev_dell_import_choose(self):
        return self.weh.get_element(self.add_dev_dell_import_choose)

    def get_exos_serial_text_area(self):
        return self.weh.get_element(self.exos_serial_text_area)

    def get_add_dev_exos_import_choose(self):
        return self.weh.get_element(self.add_dev_exos_import_choose)

    def get_add_dev_voss_sl_num_textarea(self):
        return self.weh.get_element(self.add_dev_voss_sl_num_teat_area)

    def get_add_dev_voss_import_choose(self):
        return self.weh.get_element(self.add_dev_voss_import_choose)

    def get_add_dev_wing_sl_num(self):
        return self.weh.get_element(self.add_dev_wing_sl_num)

    def get_add_dev_wing_mac(self):
        return self.weh.get_element(self.add_dev_wing_mac)

    def get_onboard_next_button(self):
        return self.weh.get_element(self.onboard_next_button)

    def get_assign_loc_ap_button(self):
        return self.weh.get_element(self.assign_loc_ap_button)

    def get_assign_loc_ap_button1(self):
        return self.weh.get_element(self.assign_loc_ap_button1)

    def get_assign_loc_switch_button(self):
        return self.weh.get_element(self.assign_loc_switch_button)

    def get_assign_loc_router_button(self):
        return self.weh.get_element(self.assign_loc_router_button)

    def get_assign_loc_vpn_gateway(self):
        return self.weh.get_element(self.assign_loc_vpn_gateway)

    def get_assign_loc_ap_grid_rows(self):
        return self.weh.get_elements(self.assign_loc_ap_grid_rows)

    def get_assign_loc_ap_grid_checkbox(self, row):
        return self.weh.get_element(self.assign_loc_ap_grid_checkbox, row)

    def get_assign_loc_button(self):
        return self.weh.get_element(self.assign_loc_button)

    def get_location_nodes(self):
        return self.weh.get_elements(self.location_nodes)

    def get_building_nodes(self):
        return self.weh.get_elements(self.building_nodes)

    def get_floor_nodes(self):
        return self.weh.get_elements(self.floor_nodes)

    def get_location_node_open_icon(self, node):
        return self.weh.get_element(self.location_node_open_icon, node)

    def get_assign_loc_search_box(self):
        return self.weh.get_element(self.assign_loc_search_box)

    def get_assign_loc_search_result(self):
        return self.weh.get_element(self.assign_loc_search_result)

    def get_assign_loc_assign_button(self):
        return self.weh.get_element(self.assign_loc_assign_button)

    def get_onboard_skip_button(self):
        return self.weh.get_element(self.onboard_skip_button)

    def get_onboard_finish_button(self):
        return self.weh.get_element(self.onboard_finish_button)

    def get_assign_branch_id_rounter_button(self):
        return self.weh.get_element(self.assign_branch_id_rounter_button)

    def get_assign_branch_id_button(self):
        return self.weh.get_element(self.assign_branch_id_button)

    def get_create_nw_policy_new_policy_radio_button(self):
        return self.weh.get_element(self.create_nw_policy_new_policy_radio_button)

    def get_create_nw_policy_use_existing_policy(self):
        return self.weh.get_element(self.create_nw_policy_use_existing_policy)

    def get_create_nw_policy_new_policy_name_input(self):
        return self.weh.get_element(self.create_nw_policy_new_policy_name_input)

    def get_create_nw_policy_type_internal_check_box(self):
        return self.weh.get_element(self.create_nw_policy_type_internal_check_box)

    def get_create_nw_policy_type_guest_check_box(self):
        return self.weh.get_element(self.create_nw_policy_type_guest_check_box)

    def get_create_nw_policy_use_existing_policy_dropdown(self):
        return self.weh.get_element(self.create_nw_policy_use_existing_policy_dropdown)

    def get_create_nw_policy_use_existing_policy_list(self):
        return self.weh.get_elements(self.create_nw_policy_use_existing_policy_list)

    def get_conf_internal_ssid_name(self):
        return self.weh.get_element(self.conf_internal_ssid_name)

    def get_internal_ssid_secure_nw_radio_btn(self):
        return self.weh.get_element(self.internal_ssid_secure_nw_radio_btn)

    def get_internal_ppsk_radio_btn(self):
        return self.weh.get_element(self.internal_ppsk_radio_btn)

    def get_internal_ppsk_usr_grp_select_dropdown(self):
        return self.weh.get_element(self.internal_ppsk_usr_grp_select_dropdown)

    def get_internal_ppsk_usr_grp_dropdown_opts(self):
        return self.weh.get_elements(self.internal_ppsk_usr_grp_dropdown_opts)

    def get_internal_ppsk_bulk_user_prefix(self):
        return self.weh.get_element(self.internal_ppsk_bulk_usr_prefix)

    def get_internal_ppsk_bulk_user_guest_number(self):
        return self.weh.get_element(self.internal_ppsk_bulk_user_guest_number)

    def get_internal_ssid_psk_radio_btn(self):
        return self.weh.get_element(self.internal_ssid_psk_radio_btn)

    def get_internal_ssid_psk_password(self):
        return self.weh.get_element(self.internal_ssid_psk_password)

    def get_internal_ssid_usr_credentials_radio_btn(self):
        return self.weh.get_element(self.internal_ssid_usr_credentials_radio_btn)

    def get_internal_ssid_usr_cred_radius_server(self):
        return self.weh.get_element(self.internal_ssid_usr_cred_radius_server)

    def get_internal_ssid_usr_cred_ip_addr(self):
        return self.weh.get_element(self.internal_ssid_usr_cred_ip_addr)

    def get_internal_ssid_usr_cred_shared_secret(self):
        return self.weh.get_element(self.internal_ssid_usr_cred_shared_secret)

    def get_internal_ssid_unsecure_nw_radio_btn(self):
        return self.weh.get_element(self.internal_ssid_unsecure_nw_radio_btn)

    def get_internal_ssid_open_nw_open_access_radio_btn(self):
        return self.weh.get_element(self.internal_ssid_open_nw_open_access_radio_btn)

    def get_guest_ssid_name(self):
        return self.weh.get_element(self.guest_ssid_name)

    def get_guest_ssid_unsecured_nw_radio_btn(self):
        return self.weh.get_element(self.guest_ssid_unsecured_nw_radio_btn)

    def get_guest_ssid_guest_access_without_login_radio_btn(self):
        return self.weh.get_element(self.guest_ssid_guest_access_without_login_radio_btn)

    def get_guest_ssid_open_nw_guest_accept_upa_radio_btn(self):
        return self.weh.get_element(self.conf_guest_ssid_open_nw_guest_accept_radio)

    def get_conf_guest_ssid_secured_nw(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw)

    def get_conf_guest_ssid_secured_nw_ppsk_radio(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_ppsk_radio)

    def get_conf_guest_ssid_secured_nw_ppsk_max_cli_checkbox(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_ppsk_max_cli_checkbox)

    def get_conf_guest_ssid_secured_nw_ppsk_max_cli_input(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_ppsk_max_cli_input)

    def get_conf_guest_ssid_secured_nw_ppsk_mac_checkbox(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_ppsk_mac_checkbox)

    def get_conf_guest_ssid_secured_nw_ppsk_mac_input(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_ppsk_mac_input)

    def get_conf_guest_ssid_secured_nw_psk_radio(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_psk_radio)

    def get_conf_guest_ssid_secured_nw_psk_cwp_checkbox(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_psk_cwp_checkbox)

    def get_conf_guest_ssid_secured_nw_psk_password(self):
        return self.weh.get_element(self.conf_guest_ssid_secured_nw_psk_password)

    def get_summary_device_success(self):
        return self.weh.get_element(self.summary_device_success)

    def get_summary_device_fail(self):
        return self.weh.get_element(self.summary_device_fail)

    def get_summary_location(self):
        return self.weh.get_element(self.summary_location)

    def get_summary_network(self):
        return self.weh.get_element(self.summary_network)

    def get_summary_device_details_link(self):
        return self.weh.get_element(self.summary_device_details_link)

    def get_summary_device_details_success(self):
        return self.weh.get_element(self.summary_device_details_success)

    def get_summary_device_details_failure(self):
        return self.weh.get_element(self.summary_device_details_failure)

    def get_add_dev_simulated_dev_model_dropdown(self):
        return self.weh.get_element(self.add_dev_simulated_dev_model_dropdown)

    def get_add_dev_simulated_dev_model_list(self):
        return self.weh.get_elements(self.add_dev_simulated_dev_model_list)

    def get_add_dev_simulated_add_more_dev(self):
        return self.weh.get_element(self.add_dev_simulated_add_more_dev)

    def get_adv_onboard_form_error(self):
        return self.weh.get_elements(self.adv_onboard_form_error)

