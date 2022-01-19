from extauto.xiq.defs.RouterTemplateWebElementsDefinitions import *
from extauto.common.WebElementHandler import WebElementHandler


class RouterTemplateWebElements(RouterTemplateWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_router_settings_tab_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_settings_tab)

    def get_router_settings_slider(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_settings_slider)

    def get_network_allocation_tab(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_allocation_tab)

    def get_device_template_tab(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_template_tab)

    def get_router_template_add_button(self):
        """

        :return:
        """
        elements = self.weh.get_elements(self.router_template_add_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_router_template_platform_from_drop_down(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.router_template_items_parent)
        return self.weh.get_elements(self.router_template_items, parent)

    def get_router_template_name_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_template_name_textfield)

    def get_router_template_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_template_save_button)

    def get_router_template_save_button1(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.router_template_save_btn_parent)
        return self.weh.get_element(self.router_template_save_btn, parent)

    def get_router_template_rows(self):
        """

        :return:
        """
        return self.weh.get_elements(self.router_device_template_grid_rows)

    def get_router_template_port_details_grid_rows(self):
        """
        :return: all the rows in the devices grid
        """
        grid_rows = self.weh.get_elements(self.router_template_port_details_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_router_template_add_port_type_link_button(self, row):
        """
        :return:
        """
        return self.weh.get_element(self.router_template_add_port_type_link_button, parent=row)

    def get_router_new_port_type_name_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_name_textfield)

    def get_router_new_port_type_description_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_description_textfield)

    def get_router_new_port_status_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_status_button)

    def get_router_new_port_type_access_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_access_radio_button)

    def get_router_new_port_type_trunk_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_trunk_radio_button)

    def get_router_new_port_type_wan_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_wan_radio_button)

    def get_router_new_port_mac_authentication_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_mac_authentication_button)

    def get_router_new_port_type_enable_ssh_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_enable_ssh_checkbox)

    def get_router_new_port_type_enable_telnet_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_enable_telnet_checkbox)

    def get_router_new_port_type_enable_ping_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_enable_ping_checkbox)

    def get_router_new_port_type_enable_snmp_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_type_enable_snmp_checkbox)

    def get_new_port_type_trunk_allowed_vlan_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.new_port_type_trunk_allowed_vlan_textfield)

    def get_new_port_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_new_port_save_button)

    def get_new_port_save_button1(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.router_new_port_save_btn_parent)
        return self.weh.get_element(self.router_new_port_save_btn, parent)

    def get_port_new_vlan_select_btn(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.port_new_vlan_select_btn_parent)
        return self.weh.get_element(self.port_new_vlan_select_btn, parent)

    def get_port_subnetwork_space_select_btn(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.port_subnetwork_space_select_btn_parent)
        return self.weh.get_element(self.port_subnetwork_space_select_btn, parent)

    def get_router_allocation_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_allocation_add_button)

    def get_router_allocation_vlan_select_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_vlan_select)

    def get_router_allocation_new_vlan_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_vlan_select_new_button)

    def get_router_allocation_new_vlan_name_input_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_vlan_object_name_textfield)


    def get_router_allocation_new_vlan_id_input_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_vlan_object_vlanid_textfield)

    def get_router_allocation_new_vlan_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_vlan_object_save_button)

    def get_router_allocation_subnetwork_select_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_subnetwork_select)

    def get_router_allocation_new_subnetwork_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_subnetwork_space_select_new_btn)

    def get_new_subnetwork_name_input_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_subnetwork_name_textfield)

    def get_new_subnetwork_description_input_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.port_new_subnetwork_description_textfield)

    def get_new_subnetwork_network_type_drop_down(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_type_drop_down)

    def get_new_subnetwork_network_type_drop_down_options(self):
        """

        :return:
        """
        return self.weh.get_elements(self.network_type_drop_down_options)

    def get_create_unique_subnetwork_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.create_unique_subnetwork_radio_button)

    def get_replicate_same_subnetwork_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.replicate_same_subnetwork_radio_button)

    def get_local_ip_address_space_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.local_ip_address_space_textfield)

    def get_first_ip_as_gateway_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.first_ip_as_gateway_radio_button)

    def get_last_ip_as_gateway_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.last_ip_as_gateway_radio_button)

    def get_enable_dhcp_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.enable_dhcp_checkbox)

    def get_enable_branch_router_as_dhcp_server_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.enable_branch_router_as_dhcp_server_radio_button)

    def get_lease_time_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.lease_time_textfield)

    def get_save_subnetwork_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.save_subnetwork_button)

    def get_cancel_subnetwork_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.cancel_subnetwork_button)

    def get_save_network_allocation_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.save_network_allocation_button)

    def get_default_router_template_select_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.default_router_template_select_button)

    def get_default_router_template_dialog_rsg_rows(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.default_router_template_dialog)
        return self.weh.get_elements(self.default_router_template_dialog_rsg_rows, parent)

    def get_default_router_template_dialog_cancel_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.default_router_template_dialog)
        return self.weh.get_element(self.default_router_template_dialog_cancel_button, parent)

    def get_default_router_template_dialog_rsg_row_checkbox(self, row):
        """

        :return:
        """
        return self.weh.get_element(self.default_router_template_dialog_rsg_row_checkbox, row)

    def get_router_template_delete_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.default_router_template_dialog)
        return self.weh.get_element(self.router_template_delete_button, parent)

    def get_router_template_delete_confirm_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.router_template_delete_confirm_button)
