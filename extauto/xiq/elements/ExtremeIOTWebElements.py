from common.WebElementHandler import *
from xiq.defs.ExtremeIOTWebElementsDefs import ExtremeIOTWebElementsDefs


class ExtremeIOTWebElements(ExtremeIOTWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_iot_add_button(self):
        return self.weh.get_element(self.extreme_iot_add_button)

    def get_extreme_iot_edit_button(self):
        return self.weh.get_element(self.extreme_iot_edit_button)

    def get_extreme_iot_user_profile_name(self):
        return self.weh.get_element(self.extreme_iot_user_profile_name)

    def get_extreme_iot_policy_group_name(self):
        return self.weh.get_element(self.extreme_iot_policy_group_name)

    def get_extreme_iot_policy_group_vlan_add(self):
        return self.weh.get_element(self.extreme_iot_policy_group_vlan_add)

    def get_extreme_iot_policy_group_vlan_name(self):
        return self.weh.get_element(self.extreme_iot_policy_group_vlan_name)

    def get_extreme_iot_policy_group_vlan_id(self):
        return self.weh.get_element(self.extreme_iot_policy_group_vlan_id)

    def get_extreme_iot_save_button(self):
        return self.weh.get_element(self.extreme_iot_save_button)

    def get_extreme_iot_usr_profile_firewall_enable(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_enable)

    def get_extreme_iot_usr_profile_firewall_ip_add(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_ip_add)

    def get_extreme_iot_usr_profile_firewall_service_dropdown(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_service_dropdown)

    def get_extreme_iot_usr_profile_firewall_service_options(self):
        return self.weh.get_elements(self.extreme_iot_usr_profile_firewall_service_options)

    def get_extreme_iot_usr_profile_firewall_service_save(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_service_save)

    def get_extreme_iot_usr_profile_firewall_applications(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_applications)

    def get_extreme_iot_usr_profile_firewall_applications_filter(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_applications_filter)

    def get_extreme_iot_usr_profile_firewall_applications_search(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_applications_search)

    def get_extreme_iot_usr_profile_firewall_applications_select_all(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_applications_select_all)

    def get_extreme_iot_usr_profile_firewall_type_dropdown(self):
        return self.weh.get_element(self.extreme_iot_usr_profile_firewall_type_dropdown)

    def get_extreme_iot_usr_profile_firewall_type_options(self):
        return self.weh.get_elements(self.extreme_iot_usr_profile_firewall_type_options)

    def get_extreme_iot_user_profile_save(self):
        return self.weh.get_element(self.extreme_iot_user_profile_save)

    def get_extreme_iot_user_profile_list(self):
        return self.weh.get_element(self.extreme_iot_user_profile_list)

    def get_extreme_iot_policy_group_user_profile_dropdown(self):
        return self.weh.get_element(self.extreme_iot_policy_group_user_profile_dropdown)

    def get_extreme_iot_policy_group_user_profile_options(self):
        return self.weh.get_elements(self.extreme_iot_policy_group_user_profile_options)

    def get_extreme_iot_policy_group_save(self):
        return self.weh.get_element(self.extreme_iot_policy_group_save)

    def get_extreme_iot_policy_group_list(self):
        return self.weh.get_elements(self.extreme_iot_policy_group_list)

    def get_extreme_iot_dev_change_extremeIOT_status(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status)

    def get_extreme_iot_dev_change_extremeIOT_status_assign(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_assign)

    def get_extreme_iot_dev_list(self):
        return self.weh.get_elements(self.extreme_iot_dev_list)

    def get_extreme_iot_dev_edit(self):
        return self.weh.get_displayed_element(self.extreme_iot_dev_edit)

    def get_extreme_iot_dev_delete(self):
        return self.weh.get_element(self.extreme_iot_dev_delete)

    def get_extreme_iot_dev_action_btn(self):
        return self.weh.get_element(self.extreme_iot_dev_action_btn)

    def get_extreme_iot_dev_extremeIOT_setup(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup)

    def get_extreme_iot_dev_change_extremeIOT_status_policy_name(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_policy_name)

    def get_extreme_iot_dev_change_extremeIOT_status_dev_timezone_dropdown(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_dev_timezone_dropdown)

    def get_extreme_iot_dev_change_extremeIOT_status_dev_timezone_options(self):
        return self.weh.get_elements(self.extreme_iot_dev_change_extremeIOT_status_dev_timezone_options)

    def get_extreme_iot_dev_change_extremeIOT_status_dev_template_name(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_dev_template_name)

    def get_extreme_iot_dev_change_extremeIOT_status_country_dropdown(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_country_dropdown)

    def get_extreme_iot_dev_change_extremeIOT_status_country_options(self):
        return self.weh.get_elements(self.extreme_iot_dev_change_extremeIOT_status_country_options)

    def get_extreme_iot_dev_change_extremeIOT_status_port_type_name(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_port_type_name)

    def get_extreme_iot_dev_change_extremeIOT_status_finish(self):
        return self.weh.get_element(self.extreme_iot_dev_change_extremeIOT_status_finish)

    def get_extreme_iot_dev_extremeIOT_setup_policy_dropdown(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_policy_dropdown)

    def get_extreme_iot_dev_extremeIOT_setup_policy_options(self):
        return self.weh.get_elements(self.extreme_iot_dev_extremeIOT_setup_policy_options)

    def get_extreme_iot_dev_extremeIOT_setup_policy_checkbox(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_policy_checkbox)

    def get_extreme_iot_dev_extremeIOT_setup_policy_name(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_policy_name)

    def get_extreme_iot_dev_extremeIOT_setup_dev_timezone_dropdown(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_dev_timezone_dropdown)

    def get_extreme_iot_dev_extremeIOT_setup_dev_timezone_options(self):
        return self.weh.get_elements(self.extreme_iot_dev_extremeIOT_setup_dev_timezone_options)

    def get_extreme_iot_dev_extremeIOT_setup_template_checkbox(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_template_checkbox)

    def get_extreme_iot_dev_extremeIOT_setup_template_dropdown(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_template_dropdown)

    def get_extreme_iot_dev_extremeIOT_setup_template_options(self):
        return self.weh.get_elements(self.extreme_iot_dev_extremeIOT_setup_template_options)

    def get_extreme_iot_dev_extremeIOT_setup_template_name(self):
        return self.weh.get_elements(self.extreme_iot_dev_extremeIOT_setup_template_name)

    def get_extreme_iot_dev_extremeIOT_setup_country_dropdown(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_country_dropdown)

    def get_extreme_iot_dev_extremeIOT_setup_country_options(self):
        return self.weh.get_elements(self.extreme_iot_dev_extremeIOT_setup_country_options)

    def get_extreme_iot_dev_extremeIOT_setup_port_type_checkbox(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_port_type_checkbox)

    def get_extreme_iot_dev_extremeIOT_setup_port_type_name(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_port_type_name)

    def get_extreme_iot_dev_extremeIOT_setup_finish(self):
        return self.weh.get_element(self.extreme_iot_dev_extremeIOT_setup_finish)

    def get_extreme_iot_clients_list(self):
        return self.weh.get_element(self.extreme_iot_clients_list)

    def get_extreme_iot_title_check(self):
        return self.weh.get_element(self.extreme_iot_title_check)
