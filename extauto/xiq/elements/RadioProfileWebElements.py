from extauto.xiq.defs.RadioProfileWebElementsDefinitions import *
from extauto.common.WebElementHandler import *


class RadioProfileWebElements(RadioProfileWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_radio_profile_button(self):
        return self.weh.get_element(self.radio_profile_add_radio_profile)

    def get_radio_profile_name(self):
        return self.weh.get_element(self.radio_profile_name_textfield)

    def get_radio_profile_description(self):
        return self.weh.get_element(self.radio_profile_description)

    def get_radio_profile_radio_mode_dropdown(self):
        return self.weh.get_element(self.radio_profile_radio_mode_dropdown)

    def get_radio_profile_radio_mode_dropdown_opts(self):
        return self.weh.get_elements(self.radio_profile_radio_mode_dropdown_opts)

    def get_radio_profile_max_tx_power(self):
        return self.weh.get_element(self.radio_profile_maximum_transmit_power)

    def get_radio_profile_tx_power_floor(self):
        return self.weh.get_element(self.radio_profile_transmit_power_floor)

    def get_radio_profile_tx_power_max_drop(self):
        return self.weh.get_element(self.radio_profile_transmit_power_max_drop)

    def get_radio_profile_max_no_of_clients(self):
        return self.weh.get_element(self.radio_profile_maximum_number_of_clients)

    def get_radio_profile_deny_connection_requests_checkbox(self):
        return self.weh.get_element(self.radio_profile_deny_connection_requests_checkbox)

    def get_radio_profile_deny_connection_requests_802_11b_checkbox(self):
        return self.weh.get_element(self.radio_profile_deny_connection_requests_option_802_11b)

    def get_radio_profile_deny_connection_requests_802_11abg_checkbox(self):
        return self.weh.get_element(self.radio_profile_deny_connection_requests_option_802_11abg)

    def get_radio_profile_background_scan_interval(self):
        return self.weh.get_element(self.radio_profile_background_scan_interval)

    def get_radio_profile_bg_scan_interval_unit_dropdown(self):
        return self.weh.get_element(self.radio_profile_bg_scan_interval_unit_dropdown)

    def get_radio_profile_bg_scan_interval_unit_dropdown_opts(self):
        return self.weh.get_elements(self.radio_profile_bg_scan_interval_unit_dropdown_opts)

    def get_radio_profile_skip_bg_scan_clients_connected_checkbox(self):
        return self.weh.get_element(self.radio_profile_skip_bg_scan_clients_connected)

    def get_radio_profile_skip_bg_scan_clients_power_save_mode_checkbox(self):
        return self.weh.get_element(self.radio_profile_skip_bg_scan_clients_power_save_mode)

    def get_radio_profile_skip_bg_scan_nw_voice_priority_checkbox(self):
        return self.weh.get_element(self.radio_profile_skip_bg_scan_nw_voice_priority)

    def get_radio_profile_channel_selection(self):
        return self.weh.get_element(self.radio_profile_channel_selection)

    def get_radio_profile_channel_list_dropdown(self):
        return self.weh.get_element(self.radio_profile_channel_list_dropdown)

    def get_radio_profile_channel_list_dropdown_opts(self):
        return self.weh.get_elements(self.radio_profile_channel_list_dropdown_opts)

    def get_radio_profile_channel_width_dropdown(self):
        return self.weh.get_element(self.radio_profile_channel_width_dropdown)

    def get_radio_profile_channel_width_dropdown_opts(self):
        return self.weh.get_elements(self.radio_profile_channel_width_dropdown_opts)

    def get_radio_profile_enable_exclude_channels_button(self):
        return self.weh.get_element(self.radio_profile_enable_exclude_channels_button)

    def get_radio_profile_channels_avail_for_exclusion(self):
        return self.weh.get_element(self.radio_profile_channels_avail_for_exclusion)

    def get_radio_profile_select_channels_for_exclusion(self):
        return self.weh.get_element(self.radio_profile_select_channels_for_exclusion)

    def get_radio_profile_transmission_power(self):
        return self.weh.get_element(self.radio_profile_transmission_power)

    def get_radio_profile_transmission_power_auto(self):
        return self.weh.get_element(self.radio_profile_transmission_power_Auto)

    def get_radio_profile_transmission_power_manual(self):
        return self.weh.get_element(self.radio_profile_transmission_power_Manual)

    def get_radio_profile_tx_power_slider_24GHz(self):
        return self.weh.get_element(self.wifi0_transmission_power_slider_button)

    def get_radio_profile_tx_power_slider_5GHz(self):
        return self.weh.get_element(self.wifi1_transmission_power_slider_button)

    def get_radio_profile_enable_dfs_button(self):
        return self.weh.get_element(self.radio_profile_enable_DFS_button)

    def get_save_radio_profile(self):
        return self.weh.get_element(self.save_radio_profile)

    def get_cancel_radio_profile(self):
        return self.weh.get_element(self.cancel_radio_profile)


    def get_radio_profile_Mega_80_Hert(self):
        return self.weh.get_element(self.radio_profile_Mega_80_Hert)

    def get_radio_profile_Mega_160_Hert(self):
        return self.weh.get_element(self.radio_profile_Mega_160_Hert)

    def get_radio_profile_Mega_40_Hert(self):
        return self.weh.get_element(self.radio_profile_Mega_40_Hert)

    def get_radio_profile_Mega_20_Hert(self):
        return self.weh.get_element(self.radio_profile_Mega_20_Hert)

    def get_radio_profile_limit_channel_selection_button(self):
        return self.weh.get_element(self.radio_profile_limit_channel_selection)

    def get_enable_client_transmission_power_control_802_11h_button(self):
        return self.weh.get_element(self.enable_client_transmission_power_control_802_11h_button)

    def get_radio_profile_channel_width(self, channel):
        item = {}
        item['XPATH'] = self.radio_profile_channel_width['XPATH'] + channel + '"]'
        item['wait_for'] = 3

        return item

    def get_radio_profile_channel_model (self):
        return self.weh.get_element(self.radio_profile_channel_model)

    def get_radio_profile_region (self):
        return self.weh.get_element(self.radio_profile_region)

    def get_radio_profile_enable_background_scan_button(self):
        return self.weh.get_element(self.radio_profile_enable_background_scan_button)

    def get_channel_width_exclusions_uni_1(self):
        return self.weh.get_element(self.channel_width_exclusions_uni_1)

    def get_channel_width_exclusions_uni_2(self):
        return self.weh.get_element(self.channel_width_exclusions_uni_2)

    def get_channel_width_exclusions_uni_3(self):
        return self.weh.get_element(self.channel_width_exclusions_uni_3)

    def get_channel_width_exclusions_unii_2_extended(self):
        return self.weh.get_element(self.channel_width_exclusions_unii_2_extended)

    def get_channel_width_exclusions_unii_5(self):
        return self.weh.get_element(self.channel_width_exclusions_unii_5)

    def get_channel_width_exclusions_unii_6(self):
        return self.weh.get_element(self.channel_width_exclusions_unii_6)

    def get_channel_width_exclusions_unii_7(self):
        return self.weh.get_element(self.channel_width_exclusions_unii_7)

    def get_channel_width_exclusions_unii_8(self):
        return self.weh.get_element(self.channel_width_exclusions_unii_8)

    def get_radio_profile_page_size_100_link(self):
        return self.weh.get_element(self.radio_profile_page_size_100_link)

    def get_radio_profile_table_header(self):
        return self.weh.get_elements(self.radio_profile_table_header)

    def get_radio_profile_table_cells(self):
        return self.weh.get_elements(self.radio_profile_table_cells)

    def get_radio_profile_delete_button(self):
        return self.weh.get_element(self.radio_profile_delete_button)

    def get_radio_profile_no_button(self):
        return self.weh.get_element(self.radio_profile_dialog_no_button)

    def get_radio_profile_dialog_yes_button(self):
        return self.weh.get_element(self.radio_profile_dialog_yes_button)

    def get_enable_DFS_selection(self):
        return self.weh.get_element(self.enable_DFS_selection)