from xiq.defs.SwitchTemplateWebElementsDefinitions import *
from extauto.common.WebElementHandler import *


class SwitchTemplateWebElements(SwitchTemplateWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_sw_template_tab_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.device_template_switch_template_tab)

    def get_sw_template_rows(self):
        """

        :return:
        """
        return self.weh.get_elements(self.sw_device_template_grid_rows)

    def get_sw_template_platform_from_drop_down(self):
        """

        :return:
        """
        return self.weh.get_elements(self.device_sw_template_items)

    def get_sw_template_add_button(self):
        """

        :return:
        """
        return self.weh.get_elements(self.sw_template_add_button)

    def get_sw_template_save_button(self):
        return self.weh.get_elements(self.sw_template_save_btn)

    def get_sw_template_name_textfield(self):
        return self.weh.get_element(self.sw_template_name_textfield)

    def get_sw_template_enable_spanningtree(self):
        return self.weh.get_element(self.sw_template_enable_spanningtree)

    def get_sw_template_enable_stp(self):
        return self.weh.get_element(self.sw_template_enable_stp)

    def get_sw_template_enable_rstp(self):
        return self.weh.get_element(self.sw_template_enable_rstp)

    def get_sw_template_port_configuration_tab(self):
        return self.weh.get_element(self.sw_template_port_configuration_tab)

    def get_sw_template_row_cell(self, row, field='field-name'):
        cells = self.weh.get_elements(self.sw_template_row_cells, row)
        return cells

    def get_sw_template_select_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_select_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_search_textfield(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_search_textfield)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_search_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_search_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_grid(self):
        """
        :return: Switch template selection grid
        """
        return self.weh.get_element(self.sw_template_selection_grid)

    def get_sw_template_selection_grid_rows(self, table):
        """
        :return: all the rows in the specified switch template selection grid
        """
        return self.weh.get_elements(self.sw_template_selection_grid_rows, parent=table)

    def get_sw_template_selection_row_checkbox(self, row):
        """
        :return: selection check box for the specified row
        """
        return self.weh.get_element(self.sw_template_selection_row_checkbox, parent=row)

    def get_sw_template_selection_select_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_select_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_cancel_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_cancel_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_assign_button(self):
        """
        :return: 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_button)

    def get_sw_template_assign_choose_existing(self):
        """
        :return: 'Choose Existing' option of 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_choose_existing)

    def get_sw_template_assign_create_new(self):
        """
        :return: 'Create New' option of 'ASSIGN' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_assign_create_new)

    def get_sw_template_all_port_type_list_radio(self):
        """
        :return:  Radio buttons of the Port Types shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_elements(self.sw_template_port_type_list_radio)

    def get_sw_template_all_port_type_list_label(self):
        """
        :return:  Port Type labels of the Port Types shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_elements(self.sw_template_port_type_list_label)

    def get_sw_template_port_type_list_save_button(self):
        """
        :return:  SAVE button of the Port Type list shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_element(self.sw_template_port_type_list_save_button)

    def get_sw_template_port_type_list_cancel_button(self):
        """
        :return:  CANCEL button of the Port Type list shown om ASSIGN -> Chooose Existing
        """
        return self.weh.get_element(self.sw_template_port_type_list_cancel_button)

    def get_sw_template_select_all_ports_button(self):
        """
        :return: 'Select All Ports' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_select_all_ports_button)

    def get_sw_template_deselect_all_ports_button(self):
        """
        :return: 'Deselect All Ports' button of the Port Configuration page in the switch template view
        """
        return self.weh.get_element(self.sw_template_deselect_all_ports_button)

    def get_sw_template_wireframe_net_ports(self, list):
        """
        :return: list of selected ports on the wireframe of Port Configuration page in the switch template view
        """
        port_list = []
        elements = self.weh.get_elements(self.sw_template_wireframe_net_ports)
        for i in range(len(elements)):
            if i+1 in list:
                port_list.append(elements[i])
        return port_list

    def get_sw_template_selected_ports(self):
        """
        :return: list of selected ports on the wireframe of Port Configuration page in the switch template view
        """
        port_list = []
        elements = self.weh.get_elements(self.sw_template_port_selected_ports)
        for el in elements:
            if el.is_displayed():
                port_list.append(el)
        return port_list

    def get_sw_template_all_edit_port_type(self):
        return self.weh.get_elements(self.sw_template_edit_port_type)

    def get_sw_template_all_port_usage(self):
        return self.weh.get_elements(self.sw_template_port_usage)
        port_list = []
        elements = self.weh.get_elements(self.sw_template_all_port_usage)
        for el in elements:
            port_list.append(el)
        return port_list

    def get_sw_template_all_port_desc(self):
        return self.weh.get_elements(self.sw_template_port_desc)
        port_list = []
        elements = self.weh.get_elements(self.sw_template_port_desc)
        for el in elements:
            port_list.append(el)
        return port_list

    def get_sw_template_all_port_status(self):
        return self.weh.get_elements(self.sw_template_port_status)
        port_list = []
        elements = self.weh.get_elements(self.sw_template_port_status)
        for el in elements:
            port_list.append(el)
        return port_list

    def get_sw_template_stack_add_button(self):
        return self.weh.get_element(self.sw_template_stack_add_button)

    def get_sw_template_stack_delete_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_stack_delete_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_select_delete_button(self):
        return self.weh.get_element(self.sw_template_select_delete_button)

    def get_sw_template_sel_row_checkbox(self, row):
        """
        :return: selection check box for the specified row
        """
        return self.weh.get_element(self.sw_template_sel_row_checkbox, parent=row)

    def get_sw_template_selection_tipbox_text2(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_selection_tipbox_text)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_selection_close_button(self):
        return self.weh.get_element(self.sw_template_selection_close_button)

    def get_sw_template_check_box(self, row):
        """
        :return: selection check box for the specified row
        """
        return self.weh.get_element(self.sw_template_check_box, parent=row)

    def get_port_details_all_rows(self):
        return self.weh.get_template_elements(self.port_details_all_rows)

    def get_port_details_row_label(self, row):
        return self.weh.get_element(self.port_details_row_label, parent=row)

    def get_port_details_row_add_button(self, row):
        return self.weh.get_element(self.port_details_row_add_button, parent=row)

    def get_port_type_text_field(self):
        return self.weh.get_element(self.port_type_text_field)

    def get_port_details_vlan_ui_ip_button(self):
        return self.weh.get_element(self.port_details_vlan_ui_ip_button)

    def get_port_details_vlan_pop_up_all_entries(self):
        return self.weh.get_elements(self.port_details_vlan_pop_up_all_entries)

    def get_port_details_vlan_single_entry(self):
        return self.weh.get_element(self.port_details_vlan_pop_up_single_entry)

    def get_port_details_add_vlan_button(self):
        return self.weh.get_element(self.port_details_add_vlan_button)

    def get_port_details_vlan_name(self):
        return self.weh.get_element(self.port_details_vlan_name)

    def get_port_details_vlan_id(self):
        return self.weh.get_element(self.port_details_vlan_id)

    def get_port_details_vlan_cancel_button(self):
        return self.weh.get_element(self.port_details_vlan_cancel_button)

    def get_port_details_vlan_save_button(self):
        return self.weh.get_element(self.port_details_vlan_save_button)

    def get_port_type_cancel_button(self):
        return self.weh.get_element(self.port_type_cancel_button)

    def get_port_type_save_button(self):
        return self.weh.get_element(self.port_type_save_button)

    def get_switch_temp_cancel_button(self):
        return self.weh.get_element(self.switch_temp_cancel_button)

    def get_switch_temp_save_button(self):
        return self.weh.get_element(self.switch_temp_save_button)

    def get_port_details_vlan_input_obj(self):
        return self.weh.get_element(self.port_details_vlan_input_obj)

    def get_complete_stack_list(self):
        return self.weh.get_element(self.complete_stack_list)

    def get_complete_stack_all_rows(self, web_list):
        return self.weh.get_elements(self.complete_stack_all_rows, parent=web_list)

    def poe_button(self):
        return self.weh.get_element(self.poe_status)

    def port_config_template(self):
        return self.weh.get_element(self.device_template_port_configuration)

    def all_ports_selected(self):
        return self.weh.get_element(self.select_all_ports_button)

    def assign_all_ports_selected(self):
        return self.weh.get_element(self.assign_all_ports_device_template)

    def port_type_template_create_new(self):
        return self.weh.get_element(self.port_type_template)

    def port_name(self):
        return self.weh.get_element(self.port_type_name_template)

    def port_type_save_button(self):
        return self.weh.get_element(self.save_button_port_type)

    def save_device_template(self):
        return self.weh.get_elements(self.save_button_template)

    def pse_profile_user_option(self):
        return self.weh.get_element(self.pse_profile_tab)

    def pse_profile_name_tab(self):
        return self.weh.get_element(self.pse_profile_name)

    def pse_profile_power_limit(self):
        return self.weh.get_element(self.pse_power_limit)

    def priority_dropdown(self):
        return self.weh.get_elements(self.priority_options)

    def low_value(self):
        return self.weh.get_elements(self.low_value_option)

    def high_value(self):
        return self.weh.get_elements(self.high_value_option)

    def critical_value(self):
        return self.weh.get_elements(self.critical_value_option)

    def priority_items(self):
        return self.weh.get_elements(self.priority_items_select)

    def power_mode_items(self):
        return self.weh.get_elements(self.power_mode_items_select)

    def power_mode_dropdown(self):
        return self.weh.get_element(self.power_mode_dropdown_button)

    def save_button_template_pse_profile(self):
        return self.weh.get_element(self.save_button_pse)

    def existing_port_type_button(self):
        return self.weh.get_elements(self.existing_port_type)

    def port_type_list(self):
        return self.weh.get_elements(self.switch_template_port_types_list)

    def save_btn_existing_port(self):
        return self.weh.get_element(self.save_btn)

    def edit_port_button(self):
        return self.weh.get_element(self.edit_port_button_template)

    def port_list(self):
        return self.weh.get_elements(self.poe_verification_for_port_list)

    def get_sw_template_supplemental_cli_button(self):
        ret_val = None
        elements = self.weh.get_elements(self.sw_template_supplemental_cli_button)
        for el in elements:
            if el.is_displayed():
                ret_val = el
        return ret_val

    def get_sw_template_supplemental_cli_on_button(self):
        return self.weh.get_element(self.sw_template_supplemental_cli_on_button)

    def get_sw_template_supplemental_cli_name_text(self):
        return self.weh.get_element(self.sw_template_supplemental_cli_name_text)

    def get_sw_template_supplemental_cli_commands_text(self):
        return self.weh.get_element(self.sw_template_supplemental_cli_commands_text)

    def get_sw_template_scli_save_btn(self):
        elements = self.weh.get_elements(self.sw_template_scli_save_btn)
        for el in elements:
            if el.is_displayed():
                return el
        return None
