from xiq.defs.MLInsightsPlanDefinitions import *
from common.AutoActions import *
from common.WebElementHandler import *


class MLInsightsPlanWebElements(MLInsightsPlanDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_create_new_map_btn(self):
        return self.weh.get_element(self.n360_plan_create_new_map_button)

    def get_n360_plan_map_organization_text(self):
        return self.weh.get_elements(self.n360_plan_create_map_organization)

    def get_n360_plan_create_map_street_address(self):
        return self.weh.get_elements(self.n360_plan_create_map_street_address)

    def get_n360_plan_map_city_text(self):
        return self.weh.get_elements(self.n360_plan_create_map_city_state)

    def get_n360_plan_map_save_btn(self):
        return self.weh.get_element(self.n360_plan_create_map_get_started)

    def get_n360_plan_map_close_btn(self):
        return self.weh.get_elements(self.n360_plan_map_close_button)

    def get_n360_plan_import_map_button(self):
        return self.weh.get_element(self.n360_plan_import_map_button)

    def get_n360_plan_import_save_button(self):
        return self.weh.get_element(self.n360_plan_import_map_save_button)

    def get_n360_plan_map_cancel_button(self):
        return self.weh.get_element(self.n360_plan_import_map_cancel_button)

    def get_n360_plan_n360_plan_add_location(self):
        return self.weh.get_element(self.n360_plan_add_location_button)

    def get_n360_plan_location_name(self):
        return self.weh.get_element(self.n360_plan_add_loc_name)

    def get_n360_plan_location_address(self):
        return self.weh.get_element(self.n360_plan_add_loc_address)

    def get_n360_plan_location_city(self):
        return self.weh.get_element(self.n360_plan_add_loc_city)

    def get_n360_plan_location_state_dropdown(self):
        return self.weh.get_element(self.n360_plan_add_loc_state_dropdown)

    def get_n360_plan_location_state_options(self):
        return self.weh.get_elements(self.n360_plan_add_loc_state_options)

    def get_n360_plan_location_outdoor_button(self):
        return self.weh.get_element(self.n360_plan_add_loc_outdoor_button)

    def get_n360_plan_location_associated_location_dropdown(self):
        return self.weh.get_element(self.n360_plan_add_loc_associated_loc_dropdown)

    def get_n360_plan_location_save(self):
        return self.weh.get_element(self.n360_plan_add_loc_save)

    def get_n360_plan_location_cancel(self):
        return self.weh.get_element(self.n360_plan_add_loc_cancel)

    def get_n360_plan_building_name(self):
        return self.weh.get_element(self.n360_plan_add_building_name)

    def get_n360_plan_building_addr(self):
        return self.weh.get_element(self.n360_plan_add_building_addr)

    def get_n360_plan_add_building_city(self):
        return self.weh.get_element(self.n360_plan_add_building_city)

    def get_n360_plan_building_state_drop_down(self):
        return self.weh.get_element(self.n360_plan_add_building_state_drop_down)

    def get_n360_plan_building_state_options(self):
        return self.weh.get_elements(self.n360_plan_add_building_state_options)

    def get_n360_plan_add_building_associated_loc_dropdown(self):
        return self.weh.get_element(self.n360_plan_add_building_associated_loc_dropdown)

    def get_n360_plan_building_associated_loc_options(self):
        return self.weh.get_elements(self.n360_plan_add_building_associated_loc_options)

    def get_n360_plan_building_save(self):
        return self.weh.get_element(self.n360_plan_add_building_save)

    def get_n360_plan_building_cancel(self):
        return self.weh.get_element(self.n360_plan_add_building_cancel)

    def get_n360_plan_floor_name(self):
        return self.weh.get_element(self.n360_plan_add_floor_name)

    def get_n360_plan_floor_association_dropdown(self):
        return self.weh.get_element(self.n360_plan_add_floor_association_dropdown)

    def get_n360_plan_floor_association_options(self):
        return self.weh.get_elements(self.n360_plan_add_floor_association_options)

    def get_n360_plan_floor_environment_dropdown(self):
        return self.weh.get_element(self.n360_plan_add_floor_environment_dropdown)

    def get_n360_plan_floor_environment_options(self):
        return self.weh.get_element(self.n360_plan_add_floor_environment_options)

    def get_n360_plan_floor_attenuation(self):
        return self.weh.get_element(self.n360_plan_add_floor_attenuation)

    def get_n360_plan_floor_height(self):
        return self.weh.get_element(self.n360_plan_add_floor_height)

    def get_n360_plan_floor_size_width(self):
        return self.weh.get_element(self.n360_plan_add_floor_size_width)

    def get_n360_plan_floor_size_height(self):
        return self.weh.get_element(self.n360_plan_add_floor_size_height)

    def get_n360_plan_floor_height_metric_drop_down(self):
        return self.weh.get_element(self.n360_plan_add_floor_height_metric_drop_down)

    def get_n360_plan_floor_size_metric_drop_down(self):
        return self.weh.get_element(self.n360_plan_add_floor_size_metric_drop_down)

    def get_n360_plan_floor_metric_option_feet(self):
        return self.weh.get_element(self.n360_plan_add_floor_metric_option_feet)

    def get_n360_plan_floor_metric_option_meter(self):
        return self.weh.get_element(self.n360_plan_add_floor_metric_option_meter)

    def get_n360_plan_floor_bgimg_dropdown(self):
        return self.weh.get_element(self.n360_plan_add_floor_bgimg_dropdown)

    def get_n360_plan_floor_bgimg_options(self):
        return self.weh.get_elements(self.n360_plan_add_floor_bgimg_options)

    def get_n360_plan_floor_bgimg_lib_floorpln_img(self):
        return self.weh.get_element(self.n360_plan_add_floor_bgimg_lib_floorpln_img)

    def get_n360_plan_floor_bgimg_lib_floorpln_choose(self):
        return self.weh.get_element(self.n360_plan_add_floor_bgimg_lib_floorpln_choose)

    def get_n360_plan_floor_save_button(self):
        return self.weh.get_element(self.n360_plan_floor_save_button)

    def get_n360_plan_network_summary(self):
        return self.weh.get_element(self.n360_plan_network_summary)

    def get_n360_plan_search_box(self):
        return self.weh.get_element(self.n360_plan_search_box)

    def get_n360_plan_edit(self):
        return self.weh.get_element(self.n360_plan_edit)

    def get_n360_plan_add(self):
        return self.weh.get_element(self.n360_plan_add)

    def get_n360_plan_more(self):
        return self.weh.get_element(self.n360_plan_more)

    def get_n360_plan_export(self):
        return self.weh.get_element(self.n360_plan_export)

    def get_n360_plan_delete(self):
        return self.weh.get_element(self. n360_plan_delete)

    def get_n360_plan_add_map_folder(self):
        return self.weh.get_element(self.n360_plan_add_map_folder)

    def get_n360_plan_ap_count(self):
        return self.weh.get_element(self.n360_plan_ap_count)

    def get_n360_plan_router_count(self):
        return self.weh.get_element(self.n360_plan_router_count)

    def get_n360_plan_switch_count(self):
        return self.weh.get_element(self.n360_plan_switch_count)

    def get_n360_plan_vgva_count(self):
        return self.weh.get_element(self.n360_plan_vgva_count)

    def get_n360_plan_device_name(self):
        return self.weh.get_elements(self.n360_plan_device_name)

    def get_n360_plan_search_grid(self):
        return self.weh.get_elements(self.n360_plan_search_grid)

    def get_n360_plan_router_count(self):
        return self.weh.get_element(self.n360_plan_router_count)

    def get_n360_plan_switch_count(self):
        return self.weh.get_element(self.n360_plan_switch_count)

    def get_n360_plan_vgva_count(self):
        return self.weh.get_element(self.n360_plan_vgva_count)

    def get_ml_insights_click(self):
        return self.weh.get_element(self.ml_insights_click)

    def get_network_360_plan_click(self):
        return self.weh.get_element(self.network_360_plan_click)

    def get_n360_plan_add_global_view(self):
        return self.weh.get_element(self.n360_plan_add_global_view)

    def get_n360_select_locn(self):
        return self.weh.get_element(self.n360_select_locn)

    def get_n360_add_building_btn(self):
        return self.weh.get_element(self.n360_add_building_btn)

    def get_n360_add_floor_btn(self):
        return self.weh.get_element(self.n360_add_floor_btn)

    def get_n360_select_building_tab(self):
        return self.weh.get_element(self.n360_select_building_tab)

    def get_n360_plan_select_bldg_tab(self):
        return self.weh.get_element(self.n360_plan_select_bldg_tab)

    def get_n360_plan_select_add_floor(self):
        return self.weh.get_element(self.n360_plan_select_add_floor)

    def get_n360_plan_select_floor_tab(self):
        return self.weh.get_element(self.n360_plan_select_floor_tab)

    def get_n360_plan_floor_tab_locate_associated_with(self):
        return self.weh.get_element(self.n360_plan_floor_tab_locate_associated_with)

    def get_n360_plan_floor_tab_select_bldg_in_associated_with(self):
        return self.weh.get_element(self.n360_plan_floor_tab_select_bldg_in_associated_with)

    def get_n360_plan_add_floor_size_width(self):
        return self.weh.get_element(self.n360_plan_add_floor_size_width)

    def get_n360_plan_add_floor_size_height(self):
        return self.weh.get_element(self.n360_plan_add_floor_size_height)

    def get_manage_left_pane_click(self):
        return self.weh.get_element(self.manage_left_pane_click)

    def get_manage_devices_click(self):
        return self.weh.get_element(self.manage_devices_click)

    def get_n360_select_floor_more(self):
        return self.weh.get_element(self.n360_select_floor_more)

    def get_n360_delete_floor(self):
        return self.weh.get_element(self.n360_delete_floor)

    def get_n360_select_building_more(self):
        return self.weh.get_element(self.n360_select_building_more)

    def get_n360_delete_building(self):
        return self.weh.get_element(self.n360_delete_building)

    def get_n360_select_location_more(self):
        return self.weh.get_element(self.n360_select_location_more)

    def get_n360_delete_location(self):
        return self.weh.get_element(self.n360_delete_location)

    def get_n360_delete_yes(self):
        return self.weh.get_element(self.n360_delete_yes)

    def get_n360_country_list_click(self):
        return self.weh.get_element(self.n360_country_list_click)

    def get_n360_country_change_item(self):
        return self.weh.get_elements(self.n360_country_change_item)

    def get_n360_click_x_button(self):
        return self.weh.get_element(self.n360_click_x_button)

    def get_n360_extend_floor(self):
        return self.weh.get_element(self.n360_extend_floor)

    def get_n360_click_floor(self):
        return self.weh.get_element(self.n360_click_floor)

    def get_n360_upload_floor_map(self):
        return self.weh.get_element(self.n360_upload_floor_map)

    def get_n360_choose_from_library(self):
        return self.weh.get_element(self.n360_choose_from_library)

    def get_n360_choose_image(self):
        return self.weh.get_element(self.n360_choose_image)

    def get_n360_save_button_floor(self):
        return self.weh.get_element(self.n360_save_button_floor)

    def get_n360_size_floor_plan(self):
        return self.weh.get_element(self.n360_size_floor_plan)

    def get_n360_width_floor(self):
        return self.weh.get_element(self.n360_width_floor)

    def get_n360_height_floor(self):
        return self.weh.get_element(self.n360_height_floor)

    def get_n360_apply_button(self):
        return self.weh.get_element(self.n360_apply_button)
