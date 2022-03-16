from extauto.xiq.defs.DeviceTemplateWebElementsDefinitions import *
from extauto.common.WebElementHandler import *


class DeviceTemplateWebElements(DeviceTemplateWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_device_template_menu(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_template_tab)

    def get_ap_template_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_ap_template_add_button)

    def get_ap_template_platform_from_drop_down(self):
        """

        :return:
        """
        return self.weh.get_elements(self.device_ap_template_items)

    def get_ap_template_text(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_template_ap_template_name_textfield)


    def get_ap_template_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.ap_template_save_button)

    def get_ap_template_rows(self):
        """

        :return:
        """
        return self.weh.get_elements(self.device_template_grid_rows)

    def get_ap_template_ap230_scroll_button(self):
        """

        :return:
        """
        return self.weh.get_elements(self.ap_template_ap230_scroll_button)

    def get_client_access_checkbox_wifi0(self):
        """
        :return: get_client_access_checkbox_wifi0
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi0_client_access_checkbox)

    def get_backhaul_mesh_link_checkbox_wifi0(self):
        """
        :return: get_backhaul_mesh_link_checkbox_wifi0
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi0_backhaul_mesh_checkbox)

    def get_sensor_checkbox_wifi0(self):
        """
        :return: get_backhaul_mesh_link_checkbox_wifi0
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi0_sensor_checkbox)

    def get_client_access_checkbox_wifi1(self):
        """
        :return: get_client_access_checkbox_wifi1
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi1_client_access_checkbox)

    def get_client_access_checkbox_wifi2(self):
        """
        :return: get_client_access_checkbox_wifi2
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi2_client_access_checkbox)

    def get_backhaul_mesh_link_checkbox_wifi1(self):
        """
        :return: get_backhaul_mesh_link_checkbox_wifi1
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi1_backhaul_mesh_checkbox)

    def get_backhaul_mesh_link_checkbox_wifi2(self):
        """
        :return: get_backhaul_mesh_link_checkbox_wifi2
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi2_backhaul_mesh_checkbox)

    def get_sensor_checkbox_wifi1(self):
        """
        :return: get_sensor_checkbox_wifi2
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi1_sensor_checkbox)

    def get_sensor_checkbox_wifi2(self):
        """
        :return: get_sensor_checkbox_wifi2
        """
        return self.weh.get_element(self.ap_template_radio_usage_wifi2_sensor_checkbox)

    def get_device_template_ap_template_wifi1_tab(self):
        """
        :return: get_device_template_ap_template_wifi1_tab
        """
        return self.weh.get_element(self.device_template_ap_template_wifi1_tab)

    def get_device_template_ap_template_wifi0_tab(self):
        """
        :return: get_device_template_ap_template_wifi0_tab
        """
        return self.weh.get_element(self.device_template_ap_template_wifi0_tab)

    def get_wifi0_radio_profile_drop_down_opts(self):
        return self.weh.get_elements(self.wireless_interface_wifi0_radio_profiles)

    def get_wifi1_radio_profile_drop_down_opts(self):
        return self.weh.get_elements(self.wireless_interface_wifi1_radio_profiles)

    def get_device_template_ap_template_wifi2_tab(self):
        """
        :return: get_device_template_ap_template_wifi2_tab
        """
        return self.weh.get_element(self.device_template_ap_template_wifi2_tab)

    def get_wifi2_primary_server_ip_textfield(self):
        """
        :return:
        """
        return self.weh.get_element(self.wifi2_primary_server_ip_textfield)

    def get_wifi2_primary_server_port_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wifi2_primary_server_port_textfield)

    def get_wifi2_radio_status_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wifi2_radio_status_button)

    def get_wifi0_sdr_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wifi0_sdr_checkbox)

    def get_ap_template_next_button(self):
        return self.weh.get_element(self.ap_template_next_button)

    def get_device_template_grid_checkbox(self, row):
        return self.weh.get_element(self.device_template_grid_checkbox, row)

    def get_delete_ap_template_button(self):
        return self.weh.get_element(self.delete_ap_template_button)

    def get_select_rule_in_templates_view_all_pages(self):
        return self.weh.get_element(self.select_rule_in_templates_view_all_pages)

    def get_wifi0_radio_profile_drop_down(self):
        return self.weh.get_element(self.wifi0_radio_profile_drop_down)

    def get_wifi1_radio_profile_drop_down(self):
        return self.weh.get_element(self.wifi1_radio_profile_drop_down)

    def get_ap_template_select_button(self):
        elements = self.weh.get_elements(self.ap_template_select_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_select_ap_templates_view_all_pages(self):
        return self.weh.get_element(self.select_ap_templates_view_all_pages)

    def get_select_ap_template_from_list(self):
        return self.weh.get_elements(self.select_ap_template_from_list)

    def get_click_selected_ap_template(self, row):
        return self.weh.get_element(self.click_selected_ap_template, row)

    def get_ap_template_dialog_select_button(self):
        return self.weh.get_element(self.ap_template_dialog_select_button)

    def get_ap_template_select_rule_button(self, row):
        return self.weh.get_element(self.ap_template_select_rule_button, row)

    def get_ap_template_rule_list(self):
        return self.weh.get_elements(self.ap_template_rule_list)

    def get_ap_template_rule_link_button(self):
        return self.weh.get_element(self.ap_template_rule_link_button)

    def get_select_ap_templates_rules_view_all_pages(self):
        return self.weh.get_element(self.select_ap_templates_rules_view_all_pages)

    def get_device_template_cancel_button(self):
        return self.weh.get_element(self.device_template_cancel_button)