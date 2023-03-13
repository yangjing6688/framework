from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.defs.MLInsightsMonitorDefinitions import MLInsightsMonitorDefinitions


class MLInsighstMonitorWebElements(MLInsightsMonitorDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_n360_monitor_click_create_map(self):
        return self.weh.get_element(self.n360_monitor_click_create_map)

    def get_n360_monitor_create_new_map_button(self):
        return self.weh.get_element(self.n360_monitor_create_new_map_button)

    def get_monitor_import_map_button(self):
        return self.weh.get_element(self.n360_monitor_import_map_button)

    def get_monitor_import_save_button(self):
        return self.weh.get_element(self.n360_monitor_import_map_save_button)

    def get_monitor_map_cancel_button(self):
        return self.weh.get_element(self.n360_monitor_import_map_cancel_button)

    def get_n360_monitor_add_location(self):
        return self.weh.get_element(self.n360_monitor_add_location_button)

    def get_n360_monitor_location_name(self):
        return self.weh.get_element(self.n360_monitor_add_loc_name)

    def get_n360_monitor_location_address(self):
        return self.weh.get_element(self.n360_monitor_add_loc_address)

    def get_n360_monitor_location_city(self):
        return self.weh.get_element(self.n360_monitor_add_loc_city)

    def get_n360_monitor_location_state_dropdown(self):
        return self.weh.get_element(self.n360_monitor_add_loc_state_dropdown)

    def get_n360_monitor_location_state_options(self):
        return self.weh.get_elements(self.n360_monitor_add_loc_state_options)

    def get_n360_monitor_location_outdoor_button(self):
        return self.weh.get_element(self.n360_monitor_add_loc_outdoor_button)

    def get_n360_monitor_location_associated_location_dropdown(self):
        return self.weh.get_element(self. n360_monitor_add_loc_associated_loc_dropdown)

    def get_n360_monitor_location_save(self):
        return self.weh.get_element(self.n360_monitor_add_loc_save)

    def get_n360_monitor_location_cancel(self):
        return self.weh.get_element(self.n360_monitor_add_loc_cancel)

    def get_n360_monitor_building_name(self):
        return self.weh.get_element(self.n360_monitor_add_building_name)

    def get_n360_monitor_building_addr(self):
        return self.weh.get_element(self. n360_monitor_add_building_addr)

    def get_n360_monitor_add_building_city(self):
        return self.weh.get_element(self.n360_monitor_add_building_city)

    def get_n360_monitor_add_building_state_drop_down(self):
        return self.weh.get_element(self.n360_monitor_add_building_state_drop_down)

    def get_n360_monitor_add_building_state_options(self):
        return self.weh.get_elements(self.n360_monitor_add_building_state_options)

    def get_n360_monitor_add_building_associated_loc_dropdown(self):
        return self.weh.get_element(self.n360_monitor_add_building_associated_loc_dropdown)

    def get_n360_monitor_building_associated_loc_options(self):
        return self.weh.get_elements(self.n360_monitor_add_building_associated_loc_options)

    def get_n360_monitor_building_save(self):
        return self.weh.get_element(self.n360_monitor_add_building_save)

    def get_n360_monitor_building_cancel(self):
        return self.weh.get_element(self.n360_monitor_add_building_cancel)

    def get_n360_monitor_floor_name(self):
        return self.weh.get_element(self.n360_monitor_add_floor_name)

    def get_n360_monitor_floor_association_dropdown(self):
        return self.weh.get_element(self.n360_monitor_add_floor_association_dropdown)

    def get_n360_monitor_floor_association_options(self):
        return self.weh.get_elements(self.n360_monitor_add_floor_association_options)

    def get_n360_monitor_floor_environment_dropdown(self):
        return self.weh.get_element(self.n360_monitor_add_floor_environment_dropdown)

    def get_n360_monitor_floor_environment_options(self):
        return self.weh.get_element(self.n360_monitor_add_floor_environment_options)

    def get_n360_monitor_floor_attenuation(self):
        return self.weh.get_element(self.n360_monitor_add_floor_attenuation)

    def get_n360_monitor_floor_height(self):
        return self.weh.get_element(self.n360_monitor_add_floor_height)

    def get_n360_monitor_floor_size_width(self):
        return self.weh.get_element(self.n360_monitor_add_floor_size_width)

    def get_n360_monitor_floor_size_height(self):
        return self.weh.get_element(self.n360_monitor_add_floor_size_height)

    def get_n360_monitor_floor_height_metric_drop_down(self):
        return self.weh.get_element(self.n360_monitor_add_floor_height_metric_drop_down)

    def get_n360_monitor_floor_size_metric_drop_down(self):
        return self.weh.get_element(self.n360_monitor_add_floor_size_metric_drop_down)

    def get_n360_monitor_floor_metric_option_feet(self):
        return self.weh.get_element(self.n360_monitor_add_floor_metric_option_feet)

    def get_n360_monitor_floor_metric_option_meter(self):
        return self.weh.get_element(self.n360_monitor_add_floor_metric_option_meter)

    def get_n360_monitor_floor_bgimg_dropdown(self):
        return self.weh.get_element(self.n360_monitor_add_floor_bgimg_dropdown)

    def get_n360_monitor_floor_bgimg_options(self):
        return self.weh.get_elements(self.n360_monitor_add_floor_bgimg_options)

    def get_n360_monitor_floor_bgimg_lib_floorpln_img(self):
        return self.weh.get_element(self.n360_monitor_add_floor_bgimg_lib_floorpln_img)

    def get_n360_monitor_floor_bgimg_lib_floorpln_choose(self):
        return self.weh.get_element(self.n360_monitor_add_floor_bgimg_lib_floorpln_choose)

    def get_n360_monitor_floor_save_button(self):
        return self.weh.get_element(self.n360_monitor_floor_save_button)

    def get_n360_network_summary(self):
        return self.weh.get_element(self.n360_monitor_net_summary)

    def get_n360_monitor_search_box(self):
        return self.weh.get_element(self.n360_monitor_search_box)

    def get_n360_monitor_device_view(self):
        return self.weh.get_element(self.n360_monitor_device_view)

    def get_n360_monitor_zone_view(self):
        return self.weh.get_element(self.n360_monitor_zone_view)

    def get_n360_monitor_net_summary_loc_count(self):
        return self.weh.get_element(self.n360_monitor_net_summary_loc_count)

    def get_n360_monitor_net_summary_alarm(self):
        return self.weh.get_element(self.n360_monitor_net_summary_alarm)

    def get_n360_monitor_refresh_icon(self):
        return self.weh.get_element(self.n360_monitor_refresh_icon)

    def get_n360_monitor_refresh_setting(self):
        return self.weh.get_element(self.n360_monitor_refresh_setting)

    def get_n360_monitor_device_number(self):
        return self.weh.get_element(self.n360_monitor_device_number)

    def get_n360_monitor_device_status(self):
        return self.weh.get_element(self.n360_monitor_device_status)

    def get_n360_monitor_client_number(self):
        return self.weh.get_element(self.n360_monitor_client_number)

    def get_n360_monitor_client_status(self):
        return self.weh.get_element(self.n360_monitor_client_status)

    def get_n360_monitor_wifi_number(self):
        return self.weh.get_element(self.n360_monitor_wifi_number)

    def get_n360_monitor_wifi_status(self):
        return self.weh.get_element(self.n360_monitor_wifi_status)

    def get_n360_monitor_network_number(self):
        return self.weh.get_element(self.n360_monitor_network_number)

    def get_n360_monitor_network_status(self):
        return self.weh.get_element(self.n360_monitor_network_status)

    def get_n360_monitor_service_number(self):
        return self.weh.get_element(self.n360_monitor_service_number)

    def get_n360_monitor_service_status(self):
        return self.weh.get_element(self.n360_monitor_service_status)

    def get_n360_monitor_app_number(self):
        return self.weh.get_element(self.n360_monitor_app_number)

    def get_n360_monitor_app_usage(self):
        return self.weh.get_element(self.n360_monitor_app_usage)

    def get_n360_monitor_security_number(self):
        return self.weh.get_element(self.n360_monitor_security_number)

    def get_n360_monitor_security_total_rogues(self):
        return self.weh.get_element(self.n360_monitor_security_total_rogues)

    def get_n360_monitor_select_bt_button(self):
        return self.weh.get_element(self.n360_monitor_select_bt_button)

    def get_n360_monitor_ap_name(self):
        return self.weh.get_element(self.n360_monitor_ap_name)

    def get_n360_monitor_ap_count(self):
        return self.weh.get_element(self.n360_monitor_ap_count)

    def get_n360_monitor_search_grid(self):
        return self.weh.get_elements(self.n360_monitor_search_grid)


