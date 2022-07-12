from extauto.xiq.defs.WirelessNetworksDefinitions import *
from extauto.common.WebElementHandler import *


class WirelessWebElements(WirelessNetworksDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_wireless_networks_tab(self):
        """
        :return: Get Wireless networks Tab on Network Policy
        """
        return self.weh.get_element(self.wireless_nw_tab_button)

    def get_wireless_nw_grid_rows(self):
        """

        :return:
        """
        grid_rows = self.weh.get_elements(self.wireless_nw_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wireless_nw_row_cell(self, row, field='field-name'):
        """
        Get the cell from the row
        :param row: web element handler of the row
        :param field: it is the cell attribute which we need to get the handler
        :return:
        """
        cells = self.weh.get_elements(self.wireless_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_wireless_nw_add_button(self):
        return self.weh.get_element(self.wireless_nw_add_button)

    def get_standard_nw_menu(self):
        return self.weh.get_element(self.all_other_nw_menu_item)

    def get_wireless_ssid_field(self):
        """
        :return: Get Wireless networks Tab ssid input field on Network Policy
        """
        return self.weh.get_element(self.wireless_ssid_name_input_field)

    def get_wireless_broadcast_name_field(self):
        """
        :return: Get Wireless networks Tab broadcast name input field on Network Policy
        """
        return self.weh.get_element(self.wireless_broadcast_ssid_name_input_field)

    def get_wireless_wifi0_checkbox(self):
        """
        :return: Get Wireless networks Tab wifi0 checkbox on Network Policy
        """
        return self.weh.get_element(self.wireless_wifi0_checkbox)

    def get_wireless_wifi0_checkbox_status(self):
        """
        :return: Get Wireless networks Tab wifi0 checkbox on Network Policy
        """
        return self.weh.get_element(self.wireless_wifi0_checkbox).is_selected()

    def get_wireless_wifi1_checkbox(self):
        """
        :return: Get Wireless networks Tab wifi1 checkbox on Network Policy
        """
        return self.weh.get_element(self.wireless_wifi1_checkbox)

    def get_wireless_wifi1_checkbox_status(self):
        """
        :return: Get Wireless networks Tab wifi1 checkbox on Network Policy
        """
        return self.weh.get_element(self.wireless_wifi1_checkbox).is_selected()

    def get_wireless_authtype_open(self):
        """
        :return: Get Wireless auth type open on Network Policy
        """
        return self.weh.get_element(self.wireless_select_open_ssid_auth)

    def get_wireless_authtype_enterprise(self):
        """
        :return: Get Wireless auth type enterprise on Network Policy
        """
        return self.weh.get_element(self.wireless_select_enterprise_ssid_auth)

    def get_wireless_authtype_personal(self):
        """
        :return: Get Wireless auth type personal on Network Policy
        """
        return self.weh.get_element(self.wireless_select_personal_ssid_auth)

    def get_wireless_authtype_ppsk(self):
        """
        :return: Get Wireless auth type ppsk on Network Policy
        """
        return self.weh.get_element(self.wireless_select_ppsk_ssid_auth)

    def get_wireless_authtype_enhanced(self):
        """
        :return: Get Wireless auth type wep on Network Policy
        """
        return self.weh.get_element(self.wireless_select_enhanced_ssid_auth)

    def get_transition_mode_for_2ghz_and_5ghz(self):
        return self.weh.get_element(self.transition_mode_for_2ghz_and_5ghz)


    def get_wireless_ssid_authentication(self):
        """
        :return: Get Wireless ssid authentication on Network Policy
        """
        return self.weh.get_element(self.wireless_ssid_auth_tab)

    def get_key_management_drop_down(self):
        return self.weh.get_element(self.key_management_drop_down)

    def get_key_management_options(self):
        return self.weh.get_elements(self.key_management_options)

    def get_encryption_method_drop_down(self):
        return self.weh.get_element(self.encryption_method_drop_down)

    def get_encryption_method_options(self):
        return self.weh.get_elements(self.encryption_key_method_options)

    def get_auth_with_extiq_auth_service_slider_button(self):
        return self.weh.get_element(self.auth_with_extiq_auth_service_slider_button)

    def get_wireless_network_save_button(self):
        return self.weh.get_element(self.wireless_network_save_button)

    def get_cwp_radio_button(self):
        """
        :return: Get Wireless cloud captive portal radio button on Network Policy
        """
        return self.weh.get_element(self.policy_enable_captive_web_portal_button)

    def get_open_template_cloud_cwp_radio_button(self):
        return self.weh.get_element(self.open_template_cloud_cwp_radio_button)

    def get_max_num_of_clients_per_ppsk_check_box(self):
        return self.weh.get_element(self.max_num_of_clients_per_ppsk_check_box)

    def get_max_num_of_clients_per_ppsk_input_field(self):
        return self.weh.get_element(self.max_num_of_clients_per_ppsk_input_field)

    def get_pcg_use_checkbox(self):
        return self.weh.get_element(self.pcg_use_checkbox)

    def get_ap_based_radio_button(self):
        return self.weh.get_element(self.ap_based_radio_button)

    def get_key_based_radio_button(self):
        return self.weh.get_element(self.key_based_radio_button)

    def get_ppsk_classification_use_checkbox(self):
        return self.weh.get_element(self.ppsk_classification_use_checkbox)

    def get_personal_wpa2_key_type_drop_down(self):
        return self.weh.get_element(self.personal_wpa2_key_type_drop_down)

    def get_personal_wpa2_key_type_options(self):
        return self.weh.get_elements(self.personal_wpa2_key_type_options)

    def get_personal_wpa2_key_value_input_field(self):
        return self.weh.get_element(self.personal_wpa2_key_value_input_field)

    def get_sae_group_drop_down(self):
        return self.weh.get_element(self.sae_group_drop_down)

    def get_sae_group_options(self):
        return self.weh.get_elements(self.sae_group_options)

    def get_transition_mode_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.transition_mode_button)

    def get_personal_wpa3_key_value_input_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.personal_wpa3_key_value_input_field)

    def get_anti_logging_threshold(self):
        """

        :return:
        """
        return self.weh.get_element(self.anti_logging_threshold)

    def get_wireless_network_cancel_button(self):
        return self.weh.get_element(self.wireless_network_cancel_button)

    def get_ssid_list(self):
        return self.weh.get_elements(self.wireless_ssid_list)

    def get_ssid_chkbox(self, row):
        return self.weh.get_element(self.wireless_chkbox, parent=row)

    def get_wireless_delete_button(self):
        return self.weh.get_element(self.wireless_delete_button)

    def get_wireless_ssid_select_button(self):
        return self.weh.get_element(self.wireless_nw_select_button)

    def get_wireless_ssid_select_window_rows(self):
        return self.weh.get_elements(self.wireless_nw_select_ssid_rows)

    def get_wireless_select_ssid_row_check_box(self, row):
        return self.weh.get_element(self.wireless_select_ssid_row_check_box, row)

    def get_wireless_ssid_select_option_button(self):
        return self.weh.get_element(self.wireless_ssid_select_option_button)

    def get_wireless_ssid_select_cancel_button(self):
        return self.weh.get_element(self.wireless_ssid_select_cancel_button)

    def get_wireless_wifi2_checkbox(self):
        return self.weh.get_element(self.wireless_wifi2_checkbox)

    def get_wireless_wifi2_checkbox_status(self):
        return self.weh.get_element(self.wireless_wifi2_checkbox).is_selected()

    def get_wireless_wifi2_checkbox_dialog_yes_button(self):
        return self.weh.get_element(self.wireless_wifi2_checkbox_dialog_yes_button)

    def get_confirm_dialog_yes_button(self):
        return self.weh.get_element(self.confirm_dialog_yes_button)

    def get_wireless_re_use_button(self):
        return self.weh.get_element(self.wireless_re_use_button)

    def get_wireless_re_use_delete_button(self):
        return self.weh.get_element(self.wireless_re_use_delete_button)

    def get_wireless_re_use_cancel_button(self):
        return self.weh.get_element(self.wireless_re_use_cancel_button)
