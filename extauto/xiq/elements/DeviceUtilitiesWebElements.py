from extauto.xiq.defs.DeviceUtilitiesWebElementsDefinitions import DeviceUtilitiesWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class DeviceUtilitiesWebElements(DeviceUtilitiesWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_manager_view(self):
        """
        :return: Device Utilities Manager View
        """
        return self.weh.get_element(self.device_utilities_manager_view)

    def get_client_info_view(self):
        """
        :return: Device Client Info View
        """
        return self.weh.get_element(self.device_client_info_view)

    def get_client_info_list(self):
        """
        :return: Device Client Info List/Grid
        """
        return self.weh.get_element(self.device_client_info_list)

    def get_client_info_dialog_close_button(self):
        """
        :return: Device Client Info Dialog Close Button
        """
        return self.weh.get_element(self.device_client_info_dialog_close_button)

    def get_tech_data_view(self):
        """
        :return: Tech Data View
        """
        return self.weh.get_element(self.tech_data_view)

    def get_tech_data_message(self):
        """
        :return: Tech Data Message
        """
        return self.weh.get_element(self.tech_data_message)

    def get_tech_data_download_button(self):
        """
        :return: Tech Data Download Button
        """
        return self.weh.get_element(self.tech_data_download_button)

    def get_tech_data_dialog_close_button(self):
        """
        :return: Tech Data Dialog Close Button
        """
        return self.weh.get_element(self.tech_data_dialog_close_button)

    def get_neighbor_info_view(self):
        """
        :return: Device Neighbor Info View
        """
        return self.weh.get_element(self.device_neighbor_info_view)

    def get_neighbor_info_list(self):
        """
        :return: Device Neighbor Info List/Grid
        """
        return self.weh.get_element(self.device_neighbor_info_list)

    def get_neighbor_info_dialog_close_button(self):
        """
        :return: Device Neighbor Info Dialog Close Button
        """
        return self.weh.get_element(self.device_neighbor_info_dialog_close_button)

    def get_locate_device_view(self):
        """
        :return: Locate Device View
        """
        return self.weh.get_element(self.locate_device_view)

    def get_locate_device_mode_checkbox(self):
        """
        :return: Locate Device Mode Checkbox
        """
        return self.weh.get_element(self.locate_device_mode_check)

    def get_locate_device_color_drop_down(self):
        """
        :return: Locate Device Color Dropdown
        """
        return self.weh.get_element(self.locate_device_color_drop_down)

    def get_locate_device_color_drop_down_items(self):
        """
        :return: Locate Device Color Dropdown Items
        """
        return self.weh.get_elements(self.locate_device_color_drop_down_items)

    def get_locate_device_blink_drop_down(self):
        """
        :return: Locate Device Blink Dropdown
        """
        return self.weh.get_element(self.locate_device_blink_drop_down)

    def get_locate_device_blink_drop_down_items(self):
        """
        :return: Locate Device Blink Dropdown Items
        """
        return self.weh.get_elements(self.locate_device_blink_drop_down_items)

    def get_locate_device_cancel_button(self):
        """
        :return: Locate Device Cancel Button
        """
        return self.weh.get_element(self.locate_device_cancel_button)

    def get_locate_device_submit_button(self):
        """
        :return: Locate Device Submit Button
        """
        return self.weh.get_element(self.locate_device_submit_button)

    def get_packet_capture_view(self):
        """
        :return: Packet Capture View
        """
        return self.weh.get_element(self.packet_capture_view)

    def get_packet_capture_interface_drop_down(self):
        """
        :return: Packet Capture Interface Dropdown
        """
        return self.weh.get_element(self.packet_capture_interface_drop_down)

    def get_packet_capture_interface_drop_down_items(self):
        """
        :return: Packet Capture Interface Dropdown Items
        """
        return self.weh.get_elements(self.packet_capture_interface_drop_down_items)

    def get_packet_capture_duration_input(self):
        """
        :return: Packet Capture Duration Input
        """
        return self.weh.get_element(self.packet_capture_duration_input)

    def get_packet_capture_count_input(self):
        """
        :return: Packet Capture Count Input
        """
        return self.weh.get_element(self.packet_capture_count_input)

    def get_packet_capture_add_token_button(self):
        """
        :return: Packet Capture Add Token Button
        """
        return self.weh.get_element(self.packet_capture_add_token_button)

    def get_packet_capture_cancel_button(self):
        """
        :return: Packet Capture Cancel Button
        """
        return self.weh.get_element(self.packet_capture_cancel_button)

    def get_packet_capture_start_button(self):
        """
        :return: Packet Capture Start Button
        """
        return self.weh.get_element(self.packet_capture_start_button)

    def get_show_cli_view(self):
        """
        :return: Show CLI View
        """
        return self.weh.get_element(self.show_cli_view)

    def get_show_cli_content(self):
        """
        :return: Show CLI Content
        """
        return self.weh.get_element(self.show_cli_content)

    def get_show_cli_dialog_close_button(self):
        """
        :return: Show CLI Dialog Close Button
        """
        return self.weh.get_element(self.show_cli_dialog_close_button)

    def get_show_ping_view(self):
        """
        :return: Show Ping View
        """
        return self.weh.get_element(self.show_ping_view)

    def get_show_ping_ip_address_input(self):
        """
        :return: Show Ping IP Address Input
        """
        return self.weh.get_element(self.show_ping_ip_address_input)

    def get_show_ping_refresh_button(self):
        """
        :return: Show Ping Refresh Button
        """
        return self.weh.get_element(self.show_ping_refresh_button)

    def get_show_ping_dialog_close_button(self):
        """
        :return: Show Ping Dialog Close Button
        """
        return self.weh.get_element(self.show_ping_dialog_close_button)

    def get_vlan_probe_view(self):
        """
        :return: VLAN Probe View
        """
        return self.weh.get_element(self.vlan_probe_view)

    def get_vlan_probe_results_collapser(self):
        """
        :return: VLAN Probe Results Collapser
        """
        return self.weh.get_element(self.vlan_probe_results_collapser)

    def get_vlan_probe_range_min_input(self):
        """
        :return: VLAN Probe Range Min Input
        """
        return self.weh.get_element(self.vlan_probe_range_min_input)

    def get_vlan_probe_range_max_input(self):
        """
        :return: VLAN Probe Range Max Input
        """
        return self.weh.get_element(self.vlan_probe_range_max_input)

    def get_vlan_probe_ranges_input(self):
        """
        :return: VLAN Probe Ranges Input
        """
        return self.weh.get_element(self.vlan_probe_ranges_input)

    def get_vlan_probe_retries_input(self):
        """
        :return: VLAN Probe Retries Input
        """
        return self.weh.get_element(self.vlan_probe_retries_input)

    def get_vlan_probe_timeout_input(self):
        """
        :return: VLAN Probe Timeout Input
        """
        return self.weh.get_element(self.vlan_probe_timeout_input)

    def get_vlan_probe_start_button(self):
        """
        :return: VLAN Probe Start Button
        """
        return self.weh.get_element(self.vlan_probe_start_button)

    def get_vlan_probe_stop_button(self):
        """
        :return: VLAN Probe Stop Button
        """
        return self.weh.get_element(self.vlan_probe_stop_button)

    def get_vlan_probe_clear_button(self):
        """
        :return: VLAN Probe Clear Button
        """
        return self.weh.get_element(self.vlan_probe_clear_button)

    def get_vlan_probe_dialog_close_button(self):
        """
        :return: VLAN Probe Dialog Close Button
        """
        return self.weh.get_element(self.vlan_probe_dialog_close_button)

    def get_select_stack_member_view(self):
        """
        :return: Select Stack Member View
        """
        return self.weh.get_element(self.select_stack_member_view)

    def get_select_stack_member_drop_down(self):
        """
        :return: Select Stack Member Dropdown
        """
        return self.weh.get_element(self.select_stack_member_drop_down)

    def get_select_stack_member_drop_down_items(self):
        """
        :return: Select Stack Member Dropdown Items
        """
        return self.weh.get_elements(self.select_stack_member_drop_down_items)

    def get_select_stack_member_cancel_button(self):
        """
        :return: Select Stack Member Cancel Button
        """
        return self.weh.get_element(self.select_stack_member_cancel_button)

    def get_select_stack_member_next_button(self):
        """
        :return: Select Stack Member Next Button
        """
        return self.weh.get_element(self.select_stack_member_next_button)

    def get_confirm_message_view(self):
        """
        :return: Confirm Message Dialog View
        """
        return self.weh.get_element(self.confirm_message_view)

    def get_confirm_message_no_button(self):
        """
        :return: Confirm Message Dialog No Button
        """
        return self.weh.get_element(self.confirm_message_no_button)

    def get_confirm_message_yes_button(self):
        """
        :return: Confirm Message Dialog Yes Button
        """
        return self.weh.get_element(self.confirm_message_yes_button)
