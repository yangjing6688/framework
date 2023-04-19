from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.defs.FilterManageDeviceDefinitions import FilterManageDeviceDefinitions


class FilterManageDeviceWebElements(FilterManageDeviceDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_filter_toggle_link(self):
        return self.weh.get_element(self.toggle_filter_link)

    def get_location_filter_link(self):
        return self.weh.get_element(self.location_filter_link)

    def get_network_policy_filter_link(self):
        return self.weh.get_element(self.network_policy_filter_link)

    def get_my_saved_filter_list(self):
        return self.weh.get_elements(self.my_saved_list_filter)

    def get_device_serial_list(self):
        return self.weh.get_elements(self.device_serial_list)

    def get_device_policy_list(self):
        return self.weh.get_elements(self.device_policy_list)

    def get_list_del_index_filter(self):
        return self.weh.get_element(self.list_del_index_filter)

    def get_applied_filter_list(self):
        return self.weh.get_elements(self.applied_filter_list)

    def get_applied_filter_list_index(self):
        return self.weh.get_element(self.applied_filter_list_index)

    def get_applied_filter_link(self):
        return self.weh.get_element(self.applied_filter_link)

    def get_applied_filter_btn(self):
        item = {}
        item['XPATH'] = self.applied_filter_btn['XPATH']
        item['wait_for'] = 5
        return item

    def get_apply_filters_btn(self):
        return self.weh.get_element(self.apply_filters_btn)

    def get_applied_clear_filter_link(self):
        return self.weh.get_element(self.applied_filter_clear_link)

    def get_all_policy_filter(self):
        return self.weh.get_element(self.all_policies_filter)

    def get_policy_filter(self, policy):
        item = {}
        item['XPATH'] = self.network_policy_filter_chkbox['XPATH'] + '"' + policy + '"' +']'
        item['wait_for'] = 3
        return item

    def get_saved_filter_chkbox(self, filter_name):
        item = {}
        item['XPATH'] = self.saved_filter_chkbox['XPATH'] + '"' + filter_name + '"' + ']'
        item['wait_for'] = 3
        return item

    def get_save_filter_btn(self):
        return self.weh.get_element(self.save_filter_btn)

    def get_enter_filter_name_txt(self):
        return self.weh.get_element(self.dialog_input_filter_filename_txt)

    def get_dialog_save_btn(self):
        return self.weh.get_element(self.dialog_save_filter_btn)

    def get_del_yes_btn(self):
        return self.weh.get_element(self.dialog_yes_filter_btn)

    def get_device_type_filter_link(self):
        return self.weh.get_element(self.device_type_filter_link)

    def get_device_type_filter_link_expanded(self):
        return self.weh.get_element(self.device_type_filter_link_expanded)

    def get_device_type_filter_link_collapsed(self):
        return self.weh.get_element(self.device_type_filter_link_collapsed)

    def get_all_device_types_filter_chkbox(self):
        return self.weh.get_element(self.all_device_types_filter_chkbox)

    def get_plan_device_filter_chkbox(self):
        return self.weh.get_element(self.plan_device_filter_chkbox)

    def get_real_device_filter_chkbox(self):
        return self.weh.get_element(self.real_device_filter_chkbox)

    def get_simulated_device_filter_chkbox(self):
        return self.weh.get_element(self.simulated_device_filter_chkbox)

    def get_all_device_hosts(self):
        return self.weh.get_elements(self.device_host_filter_list)

    def get_device_state_filter_link(self):
        return self.weh.get_element(self.device_connection_state_filter_link)

    def get_device_state_filter_link_expanded(self):
        return self.weh.get_element(self.device_connection_state_filter_link_expanded)

    def get_device_state_filter_link_collapsed(self):
        return self.weh.get_element(self.device_connection_state_filter_link_collapsed)

    def get_device_state_all_filter_chkbox(self):
        return self.weh.get_element(self.device_state_all_filter_chkbox)

    def get_state_connected_filter_chkbox(self):
        return self.weh.get_element(self.device_state_connected_filter_chkbox)

    def get_state_disconnected_filter_chkbox(self):
        return self.weh.get_element(self.device_state_disconnected_filter_chkbox)

    def get_state_preprovisioned_filter_chkbox(self):
        return self.weh.get_element(self.device_state_preprovisioned_filter_chkbox)

    def get_connection_state_list(self):
        return self.weh.get_elements(self.state_status_filter_list)

    def get_device_prod_type_filter_link(self):
        return self.weh.get_element(self.device_prod_type_filter_link)

    def get_device_prod_type_filter_link_expanded(self):
        return self.weh.get_element(self.device_prod_type_filter_link_expanded)

    def get_device_prod_type_filter_link_collapsed(self):
        return self.weh.get_element(self.device_prod_type_filter_link_collapsed)

    def get_device_prod_type_all_filter_checkbox(self):
        return self.weh.get_element(self.device_prod_type_all_filter_chkbox)

    def get_device_prod_type_model_filter_checkbox(self, model):
        item = {}
        item['XPATH'] = self.device_prod_type_model_filter_chkbox['XPATH'] + '"' + model + '"' + ']'
        item['wait_for'] = 5
        return item

    # def get_device_prod_type_more_link(self):
    #     return self.weh.get_element(self.device_prod_type_more_link)

    # def get_device_prod_type_model_filter_checkbox(self):
    #     return self.weh.get_element(self.device_prod_type_model_filter_chkbox)

    def get_device_prod_type_model_list(self):
        return self.weh.get_elements(self.device_prod_type_model_list)

    def get_device_function_filter_link(self):
        return self.weh.get_element(self.device_function_link)

    def get_device_function_filter_link_expanded(self):
        return self.weh.get_element(self.device_function_link_expanded)

    def get_device_function_filter_link_collapsed(self):
        return self.weh.get_element(self.device_function_link_collapsed)

    def get_device_function_access_point_chkbox(self):
        return self.weh.get_element(self.device_function_access_point_filter_chkbox)

    def get_device_function_switch_chkbox(self):
        return self.weh.get_element(self.device_function_switch_filter_chkbox)

    def get_device_function_xiqse_chkbox(self):
        return self.weh.get_element(self.device_function_xiqse_filter_chkbox)

    def get_device_function_all_chkbox(self):
        return self.weh.get_element(self.device_function_all_filter_chkbox)

    # def get_device_function_more_link(self):
    #     return self.weh.get_element(self.device_function_filter_more_link)

    def get_device_data_management_state_filter_link(self):
        return self.weh.get_element(self.device_data_management_link )

    def get_device_data_management_state_filter_link_expanded(self):
        return self.weh.get_element(self.device_data_management_link_expanded)

    def get_device_data_management_state_filter_link_collapsed(self):
        return self.weh.get_element(self.device_data_management_link_collapsed)

    # def get_device_management_state_more_link(self):
    #     return self.weh.get_element(self.device_data_management_more_link)

    def get_device_management_state_device_list(self):
        return self.weh.get_elements(self.device_all_devices_list)

    def get_device_chk_list(self):
        return self.weh.get_elements(self.device_chk_list)

    def get_action_managed_device(self):
        return self.weh.get_element(self.action_managed_device_link)

    def get_action_unmanaged_device(self):
        return self.weh.get_element(self.action_unmanaged_device_link)

    def get_action_close_dialog(self):
        return self.weh.get_element(self.action_close_dialog)

    def get_device_management_unmanaged_state_chkbox(self):
        return self.weh.get_element(self.device_data_management_unmanaged_chkbox)

    def get_device_management_managed_state_chkbox(self):
        return self.weh.get_element(self.device_data_management_managed_chkbox)

    def get_device_management_new_state_chkbox(self):
        return self.weh.get_element(self.device_data_management_new_chkbox)

    def get_device_management_setting_up_state_chkbox(self):
        return self.weh.get_element(self.device_data_management_setting_up_chkbox)

    def get_device_management_all_state_chkbox(self):
        return self.weh.get_element(self.device_data_management_all_chkbox)

    def get_device_soft_version_link(self):
        return self.weh.get_element(self.device_soft_ver_link)

    def get_device_soft_version_link_expanded(self):
        return self.weh.get_element(self.device_soft_ver_link_expanded)

    def get_device_soft_version_link_collapsed(self):
        return self.weh.get_element(self.device_soft_ver_link_collapsed)

    def get_device_soft_version_all_chkbox(self):
        return self.weh.get_element(self.device_soft_ver_all_chkbox)

    def get_device_soft_version_chkbox(self, version):
        item = {}
        item['XPATH'] = self.device_soft_ver_chkbox['XPATH'] + '"' + version + '"' + ']'
        item['wait_for'] = 2
        return item

    def get_device_soft_version_chkbox_contains(self, version):
        item = {}
        item['XPATH'] = self.device_soft_ver_chkbox_contains['XPATH'] + '"' + version + '"' + ')]'
        item['wait_for'] = 2
        return item

    def get_device_soft_version_list(self):
        return self.weh.get_elements(self.device_soft_ver_list)

    def get_cloud_config_group_filter_link(self):
        return self.weh.get_element(self.cloud_config_group_link)

    def get_cloud_config_group_filter_link_expanded(self):
        return self.weh.get_element(self.cloud_config_group_link_expanded)

    def get_cloud_config_group_filter_link_collapsed(self):
        return self.weh.get_element(self.cloud_config_group_link_collapsed)

    def get_cloud_config_group_all_checkbox(self):
        return self.weh.get_element(self.cloud_config_group_all_checkbox)

    def get_cloud_config_group_checkbox(self, ccg):
        item = {}
        item['XPATH'] = self.cloud_config_group_checkbox['XPATH'] + '"' + ccg + '"' + ']'
        item['wait_for'] = 2
        return item

    def get_device_ssid_filter_link(self):
        return self.weh.get_element(self.device_ssid_filter_link)

    def get_network_filter_link(self):
        return self.weh.get_element(self.device_network_link)

    def get_device_ssid_filter_checkbox(self, ssid):
        item = {}
        item['XPATH'] = self.device_ssid_filter_chkbox['XPATH'] + '"' + ssid + '"' + ']'
        item['wait_for'] = 2
        return item

    def get_audit_state_filter_link(self):
        return self.weh.get_element(self.device_audit_status_link)

    def get_audit_all_filter_chkbox(self):
        return self.weh.get_element(self.device_audit_all_filter_chkbox)

    def get_audit_config_match_filter_chkbox(self):
        return self.weh.get_element(self.device_audit_config_match_filter_chkbox)

    def get_audit_config_mismatch_filter_chkbox(self):
        return self.weh.get_element(self.device_audit_config_mismatch_filter_chkbox)

    def get_audit_config_override_filter_chkbox(self):
        return self.weh.get_element(self.device_audit_config_overrride_filter_chkbox)

    def get_user_profile_filter_link(self):
        return self.weh.get_element(self.device_user_profile_link)

    def get_user_profile_default_guest_filter_chkbox(self):
        return self.weh.get_element(self.device_default_guest_profile_filter_chkbox)

    def get_user_default_profile_filter_chkbox(self):
        return self.weh.get_element(self.device_default_profile_filter_chkbox)

    def get_user_default_all_filter_chkbox(self):
        return self.weh.get_element(self.device_user_profile_all_filter_chkbox)

    def get_user_profiles_filter_link(self):
        return self.weh.get_element(self.user_profiles_filter_link)

    def get_user_profile_grid(self):
        return self.weh.get_elements(self.user_profile_grid)

    def get_user_check_box(self, row):
        self.weh.get_element(self.checkbox, parent=row)

    def get_filter_by_title(self):
        return self.weh.get_element(self.filter_by_title)

    def get_copilot_license_all_filter_chkbox(self):
        return self.weh.get_element(self.copilot_license_all_filter_chkbox)

    def get_copilot_license_all_copilot_eligible_filter_chkbox(self):
        return self.weh.get_element(self.copilot_license_all_copilot_eligible_filter_chkbox)

    def get_copilot_license_active_filter_chkbox(self):
        return self.weh.get_element(self.copilot_license_active_filter_chkbox)

    def get_copilot_license_expired_filter_chkbox(self):
        return self.weh.get_element(self.copilot_license_expired_filter_chkbox)

    def get_copilot_license_none_filter_chkbox(self):
        return self.weh.get_element(self.copilot_license_none_filter_chkbox)

    def get_copilot_license_filter_link(self):
        return self.weh.get_element(self.copilot_license_filter_link)

    def get_copilot_license_filter_link_expanded(self):
        return self.weh.get_element(self.copilot_license_filter_link_expanded)

    def get_copilot_license_filter_link_collapsed(self):
        return self.weh.get_element(self.copilot_license_filter_link_collapsed)
