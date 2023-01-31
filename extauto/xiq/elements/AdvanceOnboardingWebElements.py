from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.defs.AdvanceOnboardingDefinitions import AdvanceOnboardingDefinitions


class AdvanceOnboardingWebElements(AdvanceOnboardingDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_deploy_devices_to_cloud_radio_button(self):
        return self.weh.get_element(self.deploy_devices_to_cloud_radio_button)

    def get_deploy_devices_locally_radio_button(self):
        return self.weh.get_element(self.deploy_devices_locally_radio_button)

    def get_deploy_devices_get_started_button(self):
        return self.weh.get_element(self.deploy_devices_get_started_button)

    def get_deploy_devices_next_location_button(self):
        return self.weh.get_element(self.deploy_devices_next_location_button)

    def get_location_input(self):
        return self.weh.get_element(self.deploy_location_textfield)

    def get_building_input(self):
        return self.weh.get_element(self.deploy_building_textfield)

    def get_building_address(self):
        return self.weh.get_element(self.deploy_building_address)

    def get_floor_input(self):
        return self.weh.get_element(self.deploy_floor_textfield)

    def get_floor_button(self):
        return self.weh.get_element(self.deploy_floor_button)

    def get_devices_type_real_radio_button(self):
        return self.weh.get_element(self.devices_type_real_radio_button)

    def get_devices_type_simulated_radio_button(self):
        return self.weh.get_element(self.devices_type_simulated_radio_button)

    def get_entry_type_manual_radio_button(self):
        return self.weh.get_element(self.entry_type_manual_radio_button)

    def get_entry_type_csv_radio_button(self):
        return self.weh.get_element(self.entry_type_csv_radio_button)

    def get_serial_number_textfield(self):
        return self.weh.get_element(self.serial_number_textfield)

    def get_device_make_dropdown(self):
        return self.weh.get_element(self.device_make_aerohive_dropdown)

    def get_device_make_select_one_dropdown(self):
        return self.weh.get_element(self.device_make_select_one_dropdown)

    def get_devices_make_drop_down_options(self):
        return self.weh.get_elements(self.device_make_drop_down_options)

    def get_devices_make_exos_radio_button(self):
        return self.weh.get_element(self.device_make_exos_radio_button)

    def get_devices_make_voss_radio_button(self):
        return self.weh.get_element(self.device_make_voss_radio_button)

    def get_assign_location_select_button(self):
        return self.weh.get_element(self.assign_location_select_button)

    def get_location_select_button(self):
        return self.weh.get_element(self.location_select_button)

    def get_onboard_devices_button(self):
        return self.weh.get_element(self.onboard_devices_button)

    def get_onboard_success_status_textfield(self):
        return self.weh.get_element(self.onboard_success_status_textfield)

    def get_onboard_device_finish_button(self):
        return self.weh.get_element(self.onboard_device_finish_button)

    def get_drawer_trigger(self):
        return self.weh.get_element(self.drawer_trigger)

    def get_drawer_content(self):
        return self.weh.get_element(self.drawer_content)

    def get_select_assign_location_button(self):
        return self.weh.get_element(self.select_assign_location_button)

    def get_locations_generic(self):
        return self.weh.get_elements(self.locations_generic)

    def get_locations_building(self):
        return self.weh.get_elements(self.locations_building)

    def get_locations_floors(self):
        return self.weh.get_elements(self.locations_floors)

    def get_deploy_devices_next_topology_button(self):
        return self.weh.get_element(self.deploy_devices_next_topology_button)

    def get_advance_onboard_device_finish_button(self):
        return self.weh.get_element(self.advance_onboard_device_finish_button)

    def get_advance_onboard_cloudiq_engine_button(self):
        return self.weh.get_element(self.advance_onboard_cloudiq_engine_button)

    def get_advance_onboard_mac_textfield(self):
        return self.weh.get_element(self.advance_onboard_mac_address_textfield)

    def get_advance_onboard_choose_org_continue_button(self):
        return self.weh.get_element(self.advance_onboard_choose_org_continue_button)