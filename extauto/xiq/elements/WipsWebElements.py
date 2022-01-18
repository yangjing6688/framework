from xiq.defs.WipsWebElementsDefinitions import WipsWebElementDefinitions
from common.WebElementHandler import *


class WipsWebElements(WipsWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_network_policy_additional_settings_tab(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_additional_settings_tab)

    def get_network_policy_additional_settings_security_option(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_additional_settings_security_option)

    def get_network_policy_additional_settings_enable_wips_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_additional_settings_enable_wips_button)

    def get_network_policy_additional_settings_wips_menu_option(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_additional_settings_wips_menu_option)

    def get_network_policy_additional_settings_wips_name_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_additional_settings_wips_name_field)


    def get_wips_rogue_ap_detection_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_rogue_ap_detection_button)

    def get_determine_wips_enable_same_network_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.determine_wips_enable_same_network_checkbox)

    def get_wips_rogue_ap_mac_oui_detection_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_rogue_ap_mac_oui_detection_checkbox)

    def get_wips_rogue_ap_mac_oui_detection_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_rogue_ap_mac_oui_detection_add_button)


    def get_wips_rogue_ap_mac_oui_detection_delete_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_rogue_ap_mac_oui_detection_delete_button)


    def get_wips_select_mac_ouis_of_wireless_add_sign(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_mac_ouis_of_wireless_add_sign)


    def get_wips_mac_oui_add_sign(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_add_sign)


    def get_wips_mac_oui_name_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_name_textfield)


    def get_wips_mac_oui_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_textfield)

    def get_wips_mac_oui_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_save_button)

    def get_wips_mac_oui_cancel_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_cancel_button)

    def get_wips_add_mac_oui_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_add_mac_oui_button)

    def get_wips_enable_rogue_ssid_detection_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enable_rogue_ssid_detection_checkbox)

    def get_wips_enable_rogue_ssid_detection_add_sign_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enable_rogue_ssid_detection_add_sign_button)

    def get_wips_select_ssid_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_ssid_radio_button)

    def get_wips_enter_ssid_name_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enter_ssid_name_radio_button)

    def get_wips_wips_enter_ssid_name_text_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enter_ssid_name_text_field)

    def get_wips_select_ssid_encryption_type_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_ssid_encryption_type_checkbox)

    def get_wips_select_ssid_encryption_scroll_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_ssid_encryption_scroll_button)

    def get_wips_select_ssid_encryption_scroll_all_items(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_ssid_encryption_scroll_all_items)

    def get_wips_select_ssid_encryption_scroll_get_name(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_ssid_encryption_scroll_get_name)

    def get_wips_select_ssid_encryption_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_ssid_encryption_add_button)

    def get_wips_enable_rogue_ssid_detection_delete_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enable_rogue_ssid_detection_delete_button)

    def get_wips_enable_adhoc_network_detection_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enable_adhoc_network_detection_button)

    def get_wips_enable_rogue_client_reporting_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enable_rogue_client_reporting_checkbox)

    def get_wips_mitigation_mode_manual_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mitigation_mode_manual_radio_button)

    def get_wips_mitigation_mode_automatic_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mitigation_mode_automatic_radio_button)

    def get_wips_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_save_button)

    def get_authtype_drop_down_items(self):
        """
        :return:
        """
        parent = self.weh.get_element(self.wips_select_ssid_encryption_scroll_all_items)
        return self.weh.get_elements(self.wips_select_ssid_encryption_scroll_get_name, parent)

    def get_wips_select_mac_oui_drop_down_items(self):
        """
        :return:
        """
        parent = self.weh.get_element(self.wips_select_mac_oui_scroll_all_items)
        return self.weh.get_elements(self.wips_select_mac_oui_scroll_get_name, parent)

    def get_wips_select_mac_oui_scroll_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_select_mac_oui_scroll_button)

    def get_wips_mac_oui_select_checkbox(self, row):
        """
        :return: device select checkbox
        """
        return self.weh.get_element(self.wips_mac_oui_select_checkbox, parent=row)

    def get_wips_mac_oui_grid_rows(self):
        """
        :return: all the rows in the devices grid
        """
        grid_rows = self.weh.get_elements(self.wips_mac_oui_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_wips_mac_oui_select_all_checkbox_list(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_select_all_checkbox_list)

    def get_wips_mac_oui_delete_symbol_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_mac_oui_delete_symbol_button)

    def get_network_policy_back_list_link(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_back_list_link)

    def get_wips_common_object_policy_name_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_name_textfield)

    def get_wips_common_object_policy_description_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_description_textfield)

    def get_wips_common_object_policy_rogue_ap_detection_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_rogue_ap_detection_button)

    def get_wips_common_object_policy_enable_same_network_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_enable_same_network_checkbox)

    def get_wips_common_object_policy_rogue_ap_mac_oui_detection_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_rogue_ap_mac_oui_detection_checkbox)

    def get_wips_common_object_policy_enable_rogue_ssid_detection_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_enable_rogue_ssid_detection_checkbox)

    def get_wips_common_object_policy_enable_adhoc_network_detection_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_enable_adhoc_network_detection_button)

    def get_wips_common_object_policy_enable_rogue_client_reporting_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_enable_rogue_client_reporting_checkbox)

    def get_wips_common_object_mitigation_mode_manual_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_mitigation_mode_manual_radio_button)

    def get_wips_common_object_mitigation_mode_automatic_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_mitigation_mode_automatic_radio_button)

    def get_wips_common_object_enable_rogue_ssid_detection_add_sign_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_enable_rogue_ssid_detection_add_sign_button)

    def get_wips_common_object_select_ssid_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_select_ssid_radio_button)

    def get_wips_common_object_enter_ssid_name_radio_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_enter_ssid_name_radio_button)

    def get_wips_common_object_enter_ssid_name_text_field(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_enter_ssid_name_text_field)

    def get_wips_common_object_select_ssid_encryption_type_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_select_ssid_encryption_type_checkbox)

    def get_wips_common_object_select_ssid_encryption_scroll_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_select_ssid_encryption_scroll_button)

    def get_wips_common_object_select_ssid_encryption_scroll_all_items(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_select_ssid_encryption_scroll_all_items)

    def get_wips_common_object_select_ssid_encryption_scroll_get_name(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_select_ssid_encryption_scroll_get_name)

    def get_wips_common_object_select_ssid_encryption_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_select_ssid_encryption_add_button)

    def get_wips_common_object_enable_rogue_ssid_detection_delete_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_enable_rogue_ssid_detection_delete_button)

    def get_wips_common_object_save_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_save_button)

    def get_wips_common_object_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_add_button)

    def get_network_policy_reuse_wips_settings_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_reuse_wips_settings_button)

    def get_wips_policy_dialog_rsg_rows(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.network_policy_reuse_wips_policy_dialog)
        return self.weh.get_elements(self.network_policy_reuse_wips_policy_dialog_rsg_rows, parent)

    def get_wips_policy_dialog_cancel_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.network_policy_reuse_wips_policy_dialog)
        return self.weh.get_element(self.network_policy_reuse_wips_policy_dialog_cancel_button, parent)

    def get_wips_policy_dialog_select_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.network_policy_reuse_wips_policy_dialog)
        return self.weh.get_element(self.network_policy_reuse_wips_policy_dialog_select_button, parent)

    def get_wips_policy_dialog_rsg_row_checkbox(self, row):
        """

        :return:
        """
        return self.weh.get_element(self.network_policy_reuse_wips_policy_dialog_rsg_row_checkbox, row)

    def get_enable_wips_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.enable_wips_button)

    def get_rogue_ap_logs_grid_rows(self):
        """
        :return: all the rows in the rogue ap's grid
        """
        grid_rows = self.weh.get_elements(self.rogue_ap_logs_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_rogue_ap_logs_row_cells(self, row):
        """
        :return: rogue ap's row cell elements
        """
        return self.weh.get_elements(self.rogue_ap_logs_grid_row_cells, row)

    def get_rogue_ap_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.rogue_ap_button)

    def get_rogue_checkbox(self):
        """

        :return:
        """
        return self.weh.get_element(self.rogue_checkbox)

    def get_rogue_client_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.rogue_client_button)

    def get_rogue_client_logs_grid_rows(self):
        """
        :return: all the rows in the rogue Client's grid
        """
        grid_rows = self.weh.get_elements(self.rogue_client_logs_grid_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_rogue_client_logs_row_cells(self, row):
        """
        :return: rogue client's row cell elements
        """
        return self.weh.get_elements(self.rogue_client_logs_grid_row_cells, row)

    def get_wips_common_object_policy_wireless_threat_detection_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_common_object_policy_wireless_threat_detection_button)

    def get_network_policy_wips_policy_dialog_rsg_rows(self):
        """

        :return:
        """
        return self.weh.get_elements(self.network_policy_wips_policy_dialog_rsg_rows)

    def get_wips_enable_OnPrem_Airdefense_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_enable_OnPrem_Airdefense_button)

    def get_wips_primary_server_ip_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_primary_server_ip_textfield)

    def get_wips_primary_server_port_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_primary_server_port_textfield)

    def get_wips_secondary_server_ip_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_secondary_server_ip_textfield)

    def get_wips_secondary_server_port_textfield(self):
        """

        :return:
        """
        return self.weh.get_element(self.wips_secondary_server_port_textfield)


