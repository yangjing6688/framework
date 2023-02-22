from extauto.xiq.defs.extreme_location.ExtremeLocationWebElementsDefs import ExtremeLocationWebElementsDefs
from extauto.common.WebElementHandler import WebElementHandler


class ExtremeLocationWebElements(ExtremeLocationWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_location_more_insights_tab(self):
        return self.weh.get_element(self.extreme_location_more_insights_tab)

    def get_extreme_location_subscribe_page(self):
        return self.weh.get_element(self.extreme_location_subscribe_page)

    def get_extreme_location_subscribe_button(self):
        return self.weh.get_element(self.extreme_location_subscribe_button)

    def get_extreme_location_subscribe_apply_button(self):
        return self.weh.get_element(self.extreme_location_subscribe_apply_button)

    def get_devices_wireless_devices_sites_dropdown_items(self):
        return self.weh.get_elements(self.devices_wireless_devices_sites_dropdown_items)

    def get_search_xloc_ap_page(self):
        return self.weh.get_element(self.search_xloc_ap_page)

    def get_host_to_xloc_ap_page(self):
        return self.weh.get_element(self.host_to_xloc_ap_page)

    def get_device_building_from_xloc(self):
        return self.weh.get_element(self.device_building_from_xloc)

    def get_device_floor_from_xloc(self):
        return self.weh.get_element(self.device_floor_from_xloc)

    def get_devices_wireless_devices_sites_dropdown_button(self):
        return self.weh.get_element(self.extreme_location_devices_wireless_devices_sites_dropdown)

    def get_bss_device_button(self):
        return self.weh.get_element(self.bss_device_button)
    
    def get_devices_bss_devices_sites_dropdown_button(self):
        return self.weh.get_element(self.devices_bss_devices_sites_dropdown_button)
    
    def get_devices_bss_search_textfield(self):
        return self.weh.get_element(self.devices_bss_search_textfield)
    
    def get_devices_wireless_devices_search_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_search_textfield)

    def get_devices_wireless_devices_client_mac_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_client_mac_textfield)

    def get_devices_wireless_devices_host_name_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_host_name_textfield)

    def get_devices_wireless_devices_ip_address_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_ip_address_textfield)
    
    def get_devices_bss_devices_bss_textfield(self):
        return self.weh.get_element(self.devices_bss_devices_bss_textfield)
    
    def get_devices_bss_devices_ssid_textfield(self):
        return self.weh.get_element(self.devices_bss_devices_ssid_textfield)
    
    def get_devices_bss_devices_floor_name_textfield(self):
        return self.weh.get_element(self.devices_bss_devices_floor_name_textfield)
    
    def get_devices_wireless_devices_user_name_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_user_name_textfield)

    def get_devices_wireless_devices_device_type_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_device_type_textfield)

    def get_devices_wireless_devices_floor_name_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_floor_name_textfield)

    def get_devices_wireless_devices_category_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_category_textfield)

    def get_devices_wireless_devices_site_enter_time_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_site_enter_time_textfield)

    def get_devices_wireless_devices_category_enter_time_textfield(self):
        return self.weh.get_element(self.devices_wireless_devices_category_enter_time_textfield)

    def get_grid_row(self):
        grid_row = self.weh.get_element(self.wireless_devices_grid_row)
        if grid_row:
            return grid_row
        else:
            return False

    def get_extreme_location_sites_menu_dropdown_button(self):
        return self.weh.get_element(self.extreme_location_sites_menu_dropdown_button)

    def get_extreme_location_sites_menu_dropdown_items(self):
        return self.weh.get_elements(self.extreme_location_sites_menu_dropdown_items)

    def get_xloc_search_name_field(self):
        return self.weh.get_element((self.xloc_search_name_field))

    def get_common_object_grid_rows(self):
        return self.weh.get_element((self.common_object_grid_rows))

    def get_common_object_grid_ap_status(self):
        return self.weh.get_element((self.common_object_grid_ap_status))

    def get_view_ibeacon_details_button(self):
        return self.weh.get_element((self.view_ibeacon_details_button))

    def get_xloc_third_party_beacon_edit_button(self):
        return self.weh.get_element((self.xloc_third_party_beacon_edit_button))

    def get_xloc_third_party_beacon_settings(self):
        return self.weh.get_element((self.xloc_third_party_beacon_settings))

    def get_xloc_third_party_beacon_uuid_text(self):
        return self.weh.get_element((self.xloc_third_party_beacon_uuid_text))

    def get_xloc_third_party_beacon_major_minor_version(self):
        return self.weh.get_element((self.xloc_third_party_beacon_major_minor_version))

    def get_xloc_third_party_beacon_save_btn(self):
        return self.weh.get_element((self.xloc_third_party_beacon_save_btn))

    def get_xloc_third_party_success_message(self):
        return self.weh.get_element((self.xloc_third_party_success_message))

    def get_xloc_third_party_major_minor_error_message(self):
        return self.weh.get_element((self.xloc_third_party_major_minor_error_message))

    def get_xloc_third_party_beacon_delete_button(self):
        return self.weh.get_element((self.xloc_third_party_beacon_delete_button))

    def get_xloc_third_party_beacon_confirm_button(self):
        return self.weh.get_element((self.xloc_third_party_beacon_confirm_button))

    def get_xloc_third_party_beacon_download_button(self):
        return self.weh.get_element((self.xloc_third_party_beacon_download_button))

    def get_xloc_third_party_beacon_refresh_button(self):
        return self.weh.get_elements(self.xloc_third_party_beacon_refresh_button)

    def get_extreme_location_sites_name_icon(self):
        return self.weh.get_element(self.extreme_location_sites_name_icon)

    def get_extreme_location_sites_name_floor_link(self):
        return self.weh.get_element(self.extreme_location_sites_name_floor_link)

    def get_extreme_location_sites_client_mac_search_textfield(self):
        return self.weh.get_element(self.extreme_location_sites_client_mac_search_textfield)

    def get_extreme_location_sites_client_mac_radio_button(self):
        return self.weh.get_element(self.extreme_location_sites_client_mac_radio_button)

    def get_extreme_location_sites_device_preference_apply_button(self):
        return self.weh.get_element(self.extreme_location_sites_device_preference_apply_button)

    def get_extreme_location_sites_client_mac_search_suggestions_textfield(self):
        return self.weh.get_element(self.extreme_location_sites_client_mac_search_suggestions_textfield)

    def get_extreme_location_sites_client_mac_search_entered_textfield(self):
        return self.weh.get_element(self.extreme_location_sites_client_mac_search_entered_textfield)

    def get_extreme_location_sites_device_preference_apply_button_disabled(self):
        return self.weh.get_element(self.extreme_location_sites_device_preference_apply_button_disabled)

    def get_extreme_location_sites_menu_floor_name_dropdown_button(self):
        return self.weh.get_element(self.extreme_location_sites_menu_floor_name_dropdown_button)

    def get_extreme_location_sites_menu_floor_name_dropdown_items(self):
        return self.weh.get_elements(self.extreme_location_sites_menu_floor_name_dropdown_items)

    def refresh_button_eloc_sites_page(self):
        return self.weh.get_element(self.refresh_eloc_sites_page)

    def refresh_button_eloc_devices_page(self):
        return self.weh.get_element(self.refresh_eloc_devices_page)

    def get_extreme_location_subscribe_async_presence_button(self):
        return self.weh.get_element(self.async_window_presence_button)

    def get_extreme_location_subscribe_async_ibeacon_button(self):
        return self.weh.get_element(self.async_window_ibeacon_button)

    def get_xloc_authentication_error(self):
        return self.weh.get_elements(self.xloc_authentication_error)

    def get_extreme_location_asset_add_button(self):
        return self.weh.get_element(self.extreme_location_asset_add_button)

    def get_xloc_assetname_textfield(self):
        return self.weh.get_element(self.xloc_assetname_textfield)

    def get_xloc_asset_sites_click(self):
        return self.weh.get_element(self.xloc_asset_sites_click)

    def get_xloc_asset_sites_search_field(self):
        return self.weh.get_element(self.xloc_asset_sites_search_field)

    def get_xloc_asset_sites_search_click(self):
        return self.weh.get_element(self.xloc_asset_sites_search_click)

    def get_xloc_asset_assetcategory_click(self):
        return self.weh.get_element(self.xloc_asset_assetcategory_click)

    def get_xloc_asset_assetcategory_dropdown_items(self):
        return self.weh.get_elements(self.xloc_asset_assetcategory_dropdown_items)

    def enable_wifi_button(self):
        return self.weh.get_element(self.enable_wifi_radio_button)

    def get_xloc_wifi_asset_mac(self):
        return self.weh.get_element(self.xloc_wifi_asset_mac)

    def enable_ble_button(self):
        return self.weh.get_element(self.enable_ble_radio_button)

    def get_xloc_asset_ibeacon_click(self):
        return self.weh.get_element(self.xloc_asset_ibeacon_click)

    def get_xloc_asset_ibeacon_dropdown_items(self):
        return self.weh.get_elements(self.xloc_asset_ibeacon_dropdown_items)

    def enable_none_button(self):
        return self.weh.get_element(self.enable_none_radio_button)

    def get_xloc_asset_cc_click(self):
        return self.weh.get_element(self.xloc_asset_cc_click)

    def get_xloc_asset_cc_dropdown_items(self):
        return self.weh.get_elements(self.xloc_asset_cc_dropdown_items)

    def get_xloc_asset_pc_click(self):
        return self.weh.get_element(self.xloc_asset_pc_click)

    def get_xloc_asset_pc_dropdown_items(self):
        return self.weh.get_elements(self.xloc_asset_pc_dropdown_items)

    def get_extreme_location_asset_save_button(self):
        return self.weh.get_element(self.extreme_location_asset_save_button)

    def get_assets_search_textfield(self):
        return self.weh.get_element(self.assets_search_textfield)

    def get_grid_row_assets(self):
        grid_row_assets = self.weh.get_element(self.grid_row_assets)
        if grid_row_assets:
            return grid_row_assets
        else:
            return False

    def get_delete_asset(self):
        return self.weh.get_element(self.delete_asset)

    def get_delete_asset_yes(self):
        return  self.weh.get_element(self.delete_asset_yes)

    def get_actions_asset(self):
        return self.weh.get_element(self.actions_asset)

    def get_actions_edit_asset(self):
        return self.weh.get_element(self.actions_edit_asset)

    def get_datapoint1_value_xloc(self):
        return self.weh.get_element(self.get_datapoint1_value)

    def click_refresh_xloc_summary_page(self):
        return self.weh.get_element(self.click_refresh_xloc_summary)

    def get_datapoint2_value_xloc(self):
        return self.weh.get_element(self.get_datapoint2_value)

    def get_xloc_ibeacon_add_button(self):
        return self.weh.get_element(self.xloc_ibeacon_add_button)

    def get_xloc_ibeacon_name(self):
        return self.weh.get_element(self.xloc_ibeacon_name)

    def get_xloc_uuid_name(self):
        return self.weh.get_element(self.xloc_uuid_name)

    def get_xloc_major_version(self):
        return self.weh.get_element(self.xloc_major_version)

    def get_xloc_minor_version(self):
        return self.weh.get_element(self.xloc_minor_version)

    def get_xloc_ibeacon_site_dropdown(self):
        return self.weh.get_element(self.xloc_ibeacon_site_dropdown)

    def get_xloc_ibeacon_site_name(self):
        return self.weh.get_elements(self.xloc_ibeacon_site_name)

    def get_xloc_ibeacon_as_category_dropdown(self):
        return self.weh.get_element(self.xloc_ibeacon_as_category_dropdown)

    def get_xloc_ibeacon_as_category_name(self):
        return self.weh.get_elements(self.xloc_ibeacon_as_category_name)

    def get_xloc_ibeacon_ibeacon_mac_address(self):
        return self.weh.get_element(self.xloc_ibeacon_ibeacon_mac_address)

    def get_xloc_ibeacon_rssi(self):
        return self.weh.get_element(self.xloc_ibeacon_rssi)

    def get_xloc_ibeacon_advertisement_interval(self):
        return self.weh.get_element(self.xloc_ibeacon_advertisement_interval)

    def get_device_type_sites_page_drop_down_list(self):
        return self.weh.get_elements(self.device_type_sites_page_drop_down_list)

    def get_device_classification_edit_btn(self):
        grid_row = self.weh.get_elements(self.device_classification_edit_btn)
        if grid_row:
            return grid_row
        else:
            return False

    def get_provide_ssid_checkbox(self):
        return self.weh.get_element(self.provide_ssid_checkbox)

    def get_visitor_duration_checkbox(self):
        return self.weh.get_element(self.visitor_duration_checkbox)

    def get_device_classification_ssid_text_field(self):
        return self.weh.get_element(self.device_classification_ssid_text_field)

    def get_device_classification_ssid_dropdown_button(self):
        return self.weh.get_element(self.device_classification_ssid_drop_down)

    def get_device_classification_ssid_dropdown_items(self):
        return self.weh.get_elements(self.device_classification_ssid_dropdown_items)

    def get_device_classification_ssid_list(self):
        return self.weh.get_elements(self.device_classification_ssid_list)

    def get_device_classification_ssid_close_btn(self):
        return self.weh.get_elements(self.device_classification_ssid_close_btn)

    def get_visitor_duration_hrs_textbox(self):
        return self.weh.get_element(self.visitor_duration_hrs_textbox)

    def get_visitor_duration_min_textbox(self):
        return self.weh.get_element(self.visitor_duration_min_textbox)

    def get_device_classification_edit_disabled_btn(self):
        return self.weh.get_element(self.device_classification_edit_disabled_btn)

    def get_xloc_ibeacon_save(self):
        return self.weh.get_element(self.xloc_ibeacon_save)

    def get_xloc_device_classification_add_button(self):
        return self.weh.get_element(self.xloc_device_classification_add_button)

    def get_xloc_device_classification_add_device_rule_menu_button(self):
        return self.weh.get_element(self.xloc_device_classification_add_device_rule_menu_button)

    def get_xloc_device_classification_user_type_drop_down_button(self):
        return self.weh.get_element(self.xloc_device_classification_user_type_drop_down_button)

    def get_xloc_device_classification_user_type_drop_down_options(self):
        return self.weh.get_elements(self.xloc_device_classification_user_type_drop_down_options)

    def get_xloc_device_classification_duration_hours_textfield(self):
        return self.weh.get_element(self.xloc_device_classification_duration_hours_textfield)

    def get_xloc_device_classification_visitor_duration_radio_button(self):
        return self.weh.get_element(self.xloc_device_classification_visitor_duration_radio_button)

    def get_xloc_device_classification_save_button(self):
        return self.weh.get_element(self.xloc_device_classification_save_button)

    def get_xloc_device_classification_duration_minutes_textfield(self):
        return self.weh.get_element(self.xloc_device_classification_duration_minutes_textfield)

    def get_xloc_device_classification_success_message(self):
        return self.weh.get_element(self.xloc_device_classification_success_message)

    def get_xloc_device_classification_rows(self):
        """
        :return: all the rows in the clients grid
        """
        grid_rows = self.weh.get_elements(self.xloc_device_classification_rows)
        if grid_rows:
            return grid_rows
        else:
            return False

    def get_device_classification_save_btn(self):
        return self.weh.get_elements(self.device_classification_save_btn)

    def get_device_classification_grid_row(self):
        grid_row = self.weh.get_elements(self.device_classification_grid_row)
        if grid_row:
            return grid_row
        else:
            return False

    def get_device_classification_ssid_radio_btn(self):
        return self.weh.get_element(self.device_classification_ssid_radio_btn)

    def get_enter_subscriber_url(self):
        return self.weh.get_element(self.enter_subscriber_url)

    def get_enter_subscriber_url_username(self):
        return self.weh.get_element(self.enter_subscriber_url_username)

    def get_enter_subscriber_url_password(self):
        return self.weh.get_element(self.enter_subscriber_url_password)

    def get_click_presence_event(self):
        return self.weh.get_element(self.click_presence_event)

    def get_click_category_event(self):
        return self.weh.get_element(self.click_category_event)

    def get_click_location_event(self):
        return self.weh.get_element(self.click_location_event)

    def get_click_rssi_event(self):
        return self.weh.get_element(self.click_rssi_event)

    def get_click_crowding_event(self):
        return self.weh.get_element(self.click_crowding_event)

    def get_click_alarm_event(self):
        return self.weh.get_element(self.click_alarm_event)

    def get_click_save_third_party_btn(self):
        return self.weh.get_element(self.click_save_third_party_btn)

    def get_click_reset_third_party_btn(self):
        return self.weh.get_element(self.click_reset_third_party_btn)

    def get_click_test_connection_btn_third_party(self):
        return self.weh.get_element(self.click_test_connection_btn_third_party)

    def get_test_connection_xloc_status_textfield(self):
        return self.weh.get_element(self.test_connection_xloc_status_textfield)

    def get_click_xloc_test_connection_close_btn(self):
        return self.weh.get_element(self.click_xloc_test_connection_close_btn)

    def click_xloc_engagement_category(self):
        return self.weh.get_element(self.click_engagement_category)

    def click_xloc_engagement_category_add(self):
        return self.weh.get_element(self.click_engagement_category_add)

    def click_xloc_engagement_category_name(self):
        return self.weh.get_element(self.click_engagement_category_name)

    def click_xloc_engagement_category_threshold(self):
        return self.weh.get_element(self.click_engagement_category_threshold)

    def click_xloc_engagement_category_save(self):
        return self.weh.get_element(self.click_engagement_category_save)

    def click_xloc_engagement_category_site(self):
        return self.weh.get_element(self.click_engagement_category_site)

    def click_xloc_engagement_category_site_edit(self):
        return self.weh.get_element(self.click_engagement_category_site_edit)

    def click_xloc_engagement_category_site_map(self):
        return self.weh.get_element(self.click_engagement_category_site_map)

    def get_xloc_category_site_list(self):
        return self.weh.get_elements(self.xloc_category_site_list)

    def click_xloc_category_site_select_next(self):
        return self.weh.get_element(self.click_category_site_select_next)

    def click_xloc_category_site_map_final(self):
        return self.weh.get_element(self.click_category_site_map_final)

    def click_xloc_asset_category(self):
        return self.weh.get_element(self.click_asset_category)

    def click_xloc_asset_category_add(self):
        return self.weh.get_element(self.click_asset_category_add)

    def click_xloc_asset_category_name(self):
        return self.weh.get_element(self.click_asset_category_name)

    def click_xloc_asset_category_save(self):
        return self.weh.get_element(self.click_asset_category_save)

    def click_xloc_asset_category_site(self):
        return self.weh.get_element(self.click_asset_category_site)

    def click_xloc_asset_category_site_edit(self):
        return self.weh.get_element(self.click_asset_category_site_edit)

    def click_xloc_asset_category_site_map(self):
        return self.weh.get_element(self.click_asset_category_site_map)
