from extauto.app.elements.NewDeviceOnboardWebElements import *
from extauto.common.AutoActions import *
import time


class NewDeviceOnboard:
    def __init__(self):
        self.mob_login_web_elements = NewDeviceOnboardWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def device_list(self, device_name):
        time.sleep(2)
        self.utils.print_info("user entered device list screen")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_device_search(), device_name)
        devices = self.mob_login_web_elements.get_device_list_grid_rows()
        print("devices")
        for device in devices:
            print("devices")
            print(device.text)
            if device_name in device.text:
                self.auto_actions.click(device)
                return 1
        self.utils.print_info("user entered the AP details screen")
        time.sleep(5)

    def device_list_return(self):
        self.auto_actions.click(self.mob_login_web_elements.return_to_device_list())
        self.utils.print_info("user clicked on backward button of AP device details screen")
        self.auto_actions.click(self.mob_login_web_elements.get_device_list_close_link())
        self.utils.print_info("user clicked on close link")

    def device_home_loc_policy(self):
        time.sleep(2)
        pol_name = self.mob_login_web_elements.get_device_hpolicy()
        self.utils.print_info("policy name in device home:", pol_name)
        time.sleep(2)
        location_name = self.mob_login_web_elements.get_device_hlocation()
        self.utils.print_info("location name in device home:", location_name)

    def grouping(self):
        self.auto_actions.click(self.mob_login_web_elements.get_grouping_icon())
        self.utils.print_info("User clicked on grouping icon")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_disconnected_first())
        self.utils.print_info("User clicked on disconnected first")
        hostname = self.mob_login_web_elements.get_device_hostname()
        self.utils.print_info("hostname:", hostname)
        sl_no = self.mob_login_web_elements.get_device_serial_no()
        self.utils.print_info("serial no:", sl_no)
        time.sleep(4)
        self.auto_actions.click(self.mob_login_web_elements.get_grouping_icon())
        self.utils.print_info("User clicked on grouping icon")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_connected_first())
        self.utils.print_info("user clicked on connected first")
        time.sleep(2)
        hostname = self.mob_login_web_elements.get_device_hostname()
        self.utils.print_info("hostname:", hostname)
        sl_no = self.mob_login_web_elements.get_device_serial_no()
        self.utils.print_info("serial no:", sl_no)
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_grouping_icon())
        self.utils.print_info("user clicked on grouping icon")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_default_first())
        self.utils.print_info("user clicked on default first")
        time.sleep(2)
        hostname = self.mob_login_web_elements.get_device_hostname()
        self.utils.print_info("hostname:", hostname)
        sl_no = self.mob_login_web_elements.get_device_serial_no()
        self.utils.print_info("serial no:", sl_no)
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_grouping_icon())
        self.utils.print_info("user clicked on grouping icon")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_group_close())
        self.utils.print_info("user cliked on group close symbol")
        time.sleep(2)

    def already_onboarded(self, serial_no):
        self.utils.print_info("Enter the serial number of the AP")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_serial_number_text_field(), serial_no)
        time.sleep(1)
        self.utils.print_info("User clicked on continue button")
        self.auto_actions.click(self.mob_login_web_elements.get_continue_button())
        time.sleep(2)

    def get_new_device(self, serial_no):
        self.utils.print_info("Enter the serial number of the AP")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_serial_number_text_field(), serial_no)
        time.sleep(1)
        self.utils.print_info("User clicked on continue button")
        self.auto_actions.click(self.mob_login_web_elements.get_continue_button())
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_onboard_button())
        self.utils.print_info("User clicked on continue button")
        time.sleep(5)
        model_num = self.mob_login_web_elements.get_device_model_no()
        self.utils.print_info("Model number of the device: ", model_num)
        serial_number = self.mob_login_web_elements.get_ap_serial_no()
        self.utils.print_info("Serial Number of AP: ", serial_number)

    def get_serial_no(self, serial_no):
        self.utils.print_info("Enter the serial number of the AP")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_serial_number_text_field(), serial_no)
        time.sleep(1)
        self.utils.print_info("User clicked on continue button")
        self.auto_actions.click(self.mob_login_web_elements.get_continue_button())
        time.sleep(2)

    def device_make(self, make):
        self.auto_actions.click(self.mob_login_web_elements.get_device_make())
        self.utils.print_info("user clicked on device make")
        rows = self.mob_login_web_elements.get_device_make_entry()
        for row in rows:
            print(row.text)
            if make in row.text:
                self.auto_actions.click(row)
                return 1

    def get_onboard(self):
        self.auto_actions.click(self.mob_login_web_elements.get_onboard_button())
        self.utils.print_info("User clicked on continue button")
        time.sleep(5)
        model_num = self.mob_login_web_elements.get_device_model_no()
        self.utils.print_info("Model number of the device: ", model_num)
        serial_number = self.mob_login_web_elements.get_ap_serial_no()
        self.utils.print_info("Serial Number of AP: ", serial_number)

    def re_enter_serial(self, serial_no, serial_no2):
        self.utils.print_info("Enter the serial number of the AP")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_serial_number_text_field(), serial_no)
        time.sleep(1)
        self.utils.print_info("User clicked on continue button")
        self.auto_actions.click(self.mob_login_web_elements.get_continue_button())
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_reenter_serial_number())
        time.sleep(2)
        self.auto_actions.send_keys(self.mob_login_web_elements.get_reenter_serial_number_field(), serial_no2)
        self.utils.print_info("user is onboarding the AP now")
        self.auto_actions.click(self.mob_login_web_elements.get_onboard_button())
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_onboard_button())
        time.sleep(3)
        model_num = self.mob_login_web_elements.get_device_model_no()
        self.utils.print_info("Model number of the device: ", model_num)
        serial_number = self.mob_login_web_elements.get_ap_serial_no()
        self.utils.print_info("Serial Number of AP: ", serial_number)

    def skip(self):
        self.auto_actions.click(self.mob_login_web_elements.get_skip_location())

    def location_complete(self, location):
        self.auto_actions.click(self.mob_login_web_elements.get_next_option())
        self.utils.print_info("user clicked on next:location option")
        self.utils.print_info("user entered location selection screen")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_location(), location)
        time.sleep(3)
        rows = self.mob_login_web_elements.get_loc_grid_rows()
        for row in rows:
            print(row.text)
            if location in row.text:
                self.auto_actions.click(row)
                return 1

    def building_complete(self,building):
        self.utils.print_info("user is selecting building")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_building(), building)
        build_rows = self.mob_login_web_elements.get_build_grid_rows()
        for build_row in build_rows:
            if building in build_row.text:
                self.auto_actions.click(build_row)
                return 1

    def floor_complete(self, floor):
        self.utils.print_info("user entered floor selection screen")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_floor(), floor)
        floor_rows = self.mob_login_web_elements.get_floor_grid_rows()
        for floor_row in floor_rows:
            if floor in floor_row.text:
                self.auto_actions.click(floor_row)
                time.sleep(4)
                return 1

    def next_location(self):
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_next_option())
        self.utils.print_info("user clicked on next:location option")

    def location(self, location):
        self.utils.print_info("user entered location selection screen")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_location(), location)
        time.sleep(3)
        rows = self.mob_login_web_elements.get_loc_grid_rows()
        for row in rows:
            print(row.text)
            if location in row.text:
                self.auto_actions.click(row)
                return 1

    def buildings(self, building, location):
        self.utils.print_info("user going back to location screen")
        self.auto_actions.click(self.mob_login_web_elements.get_building_backward_link())
        self.utils.print_info("user again selecting location")
        self.location(location)
        self.utils.print_info("user is selecting building")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_building(), building)
        build_rows = self.mob_login_web_elements.get_build_grid_rows()
        for build_row in build_rows:
            if building in build_row.text:
                self.auto_actions.click(build_row)
                return 1

    def floors(self, floor, building, location):
        self.utils.print_info("user going back to location screen")
        self.auto_actions.click(self.mob_login_web_elements.get_floor_backward_link())
        self.utils.print_info("user again selecting location")
        self.buildings(building, location)
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_floor(), floor)
        floor_rows = self.mob_login_web_elements.get_floor_grid_rows()
        for floor_row in floor_rows:
            if floor in floor_row.text:
                self.auto_actions.click(floor_row)
                return 1

    def exit_onboard(self):
        self.utils.print_info("user is trying to exit onboard process")
        self.auto_actions.click(self.mob_login_web_elements.get_exit_onboard_process())
        self.utils.print_info("user cancelled exiting from onboard process")
        self.auto_actions.click(self.mob_login_web_elements.get_exit_onboard_cancel())
        self.auto_actions.click(self.mob_login_web_elements.get_exit_onboard_process())
        self.utils.print_info("user confirmed exiting from onboard process")
        self.auto_actions.click(self.mob_login_web_elements.get_exit_onboard_confirm())

    def network_policy(self):
        self.utils.print_info("user is going back to device details screen")
        self.auto_actions.click(self.mob_login_web_elements.get_back_to_device_details())
        time.sleep(4)
        self.utils.print_info("user is entering to location screen")
        self.auto_actions.click(self.mob_login_web_elements.get_next_option())

    def np_complete(self, policy):
        time.sleep(3)
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_option())
        self.utils.print_info("user entered to network policy screen")
        #self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_dropdown())
        self.utils.print_info("user is clicking on dropdown")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_dropdown())
        time.sleep(3)
        self.utils.print_info("user is searching network policy")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_np(), policy)
        np_rows = self.mob_login_web_elements.get_np_grid_rows()
        for np_row in np_rows:
            print(np_row.text)
            if policy in np_row.text:
                self.auto_actions.click(np_row)
                print(np_row)
                time.sleep(2)
                return 1

    def get_np(self, policy):
        self.utils.print_info("user is entering to network policy screen")
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_option())
        self.utils.print_info("user entering network policy dropdown")
        #self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_dropdown())
        time.sleep(1)
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_dropdown())
        time.sleep(2)
        self.utils.print_info("user is returning from network policy list screen")
        self.auto_actions.click(self.mob_login_web_elements.get_np_backward_link())
        time.sleep(1)
        self.utils.print_info("user entering network policy list screen")
        #self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_dropdown())
        time.sleep(1)
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_dropdown())
        time.sleep(3)
        self.utils.print_info("user is searching network policy")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_searched_np(), policy)
        np_rows = self.mob_login_web_elements.get_np_grid_rows()
        for np_row in np_rows:
            print(np_row.text)
            if policy in np_row.text:
                self.auto_actions.click(np_row)
                print(np_row)
                time.sleep(2)
                return 1

    def done_flow(self):
        self.utils.print_info("user is going back to location selected screen")
        self.auto_actions.click(self.mob_login_web_elements.get_back_to_location_details())
        time.sleep(2)
        self.utils.print_info("user is entering to network policy screen")
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_option())
        time.sleep(2)
        self.utils.print_info("user clicked on done button")
        self.auto_actions.click(self.mob_login_web_elements.get_done_button())
        time.sleep(3)
        policy = self.mob_login_web_elements.get_policy_details()
        self.utils.print_info("Policy assigned during onboarding: ", policy)
        location = self.mob_login_web_elements.get_location_details()
        self.utils.print_info("Location assigned during onboarding: ", location)

    def done(self):
        self.utils.print_info("user clicked on done button")
        self.auto_actions.click(self.mob_login_web_elements.get_done_button())
        time.sleep(3)
        policy = self.mob_login_web_elements.get_policy_details()
        self.utils.print_info("Policy assigned during onboarding: ", policy)
        location = self.mob_login_web_elements.get_location_details()
        self.utils.print_info("Location assigned during onboarding: ", location)

    def finish(self):
        self.auto_actions.click(self.mob_login_web_elements.get_finish_button())
        time.sleep(10)

    def add_another_yes(self):
        self.utils.print_info("user clicked on add another button")
        self.auto_actions.click(self.mob_login_web_elements.get_add_another())
        time.sleep(6)
        self.utils.print_info("user clicked on yes button to save policy and location")
        self.auto_actions.click(self.mob_login_web_elements.get_policy_save_yes())
        time.sleep(10)

    def mul_onboard(self, serial_no):
        self.utils.print_info("Enter the serial number of the AP")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_serial_number_text_field(), serial_no)
        time.sleep(4)
        self.utils.print_info("User clicked on continue button")
        self.auto_actions.click(self.mob_login_web_elements.get_continue_button())
        time.sleep(7)
        self.utils.print_info("user is onboarding the AP now")
        self.auto_actions.click(self.mob_login_web_elements.get_onboard_button())
        time.sleep(10)
        model_num = self.mob_login_web_elements.get_device_model_no()
        self.utils.print_info("Model number of the device: ", model_num)
        serial_number = self.mob_login_web_elements.get_ap_serial_no()
        self.utils.print_info("Serial Number of AP: ", serial_number)
        self.auto_actions.click(self.mob_login_web_elements.get_next_option())
        time.sleep(3)
        location_info = self.mob_login_web_elements.get_loc_info()
        self.utils.print_info("location:", location_info)
        building_info = self.mob_login_web_elements.get_building_info()
        self.utils.print_info("building:", building_info)
        floor_info = self.mob_login_web_elements.get_floor_info()
        self.utils.print_info("floor:", floor_info)
        self.utils.print_info("user is entering to network policy screen")
        self.auto_actions.click(self.mob_login_web_elements.get_nw_policy_option())
        time.sleep(2)
        policy_info = self.mob_login_web_elements.get_dpolicy()
        self.utils.print_info("policy:", policy_info)
        self.auto_actions.click(self.mob_login_web_elements.get_done_button())
        time.sleep(3)
        policy = self.mob_login_web_elements.get_policy_details()
        self.utils.print_info("Policy assigned during onboarding: ", policy)
        location = self.mob_login_web_elements.get_location_details()
        self.utils.print_info("Location assigned during onboarding: ", location)

    def add_another_no(self):
        self.utils.print_info("user clicked on add another button")
        self.auto_actions.click(self.mob_login_web_elements.get_add_another())
        time.sleep(2)
        self.utils.print_info("user clicked on not button to not to save policy and location")
        self.auto_actions.click(self.mob_login_web_elements.get_policy_save_no())
        time.sleep(10)

    def skip_mul_onboard(self, serial_no):
        self.get_new_device(serial_no)
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_next_option())
        self.utils.print_info("User clicked on Next location option")
        time.sleep(3)
        self.skip()
        self.auto_actions.click(self.mob_login_web_elements.get_done_button())
        time.sleep(2)
        policy = self.mob_login_web_elements.get_policy_details()
        self.utils.print_info("Policy assigned during onboarding: ", policy)
        location = self.mob_login_web_elements.get_location_details()
        self.utils.print_info("Location assigned during onboarding: ", location)
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_finish_button())
        time.sleep(10)

    def sel_none_mul_onboard(self, serial_no, location, policy):
        self.utils.print_info("Enter the serial number of the AP")
        self.auto_actions.send_keys(self.mob_login_web_elements.get_serial_number_text_field(), serial_no)
        time.sleep(4)
        self.utils.print_info("User clicked on continue button")
        self.auto_actions.click(self.mob_login_web_elements.get_continue_button())
        time.sleep(7)
        self.utils.print_info("user is onboarding the AP now")
        self.auto_actions.click(self.mob_login_web_elements.get_onboard_button())
        time.sleep(10)
        model_num = self.mob_login_web_elements.get_device_model_no()
        self.utils.print_info("Model number of the device: ", model_num)
        serial_number = self.mob_login_web_elements.get_ap_serial_no()
        self.utils.print_info("Serial Number of AP: ", serial_number)
        self.auto_actions.click(self.mob_login_web_elements.get_next_option())
        time.sleep(2)
        self.utils.print_info("click on loc dropdown")
        #self.auto_actions.click(self.mob_login_web_elements.get_dloc())
        time.sleep(1)
        self.auto_actions.click(self.mob_login_web_elements.get_dloc())
        time.sleep(2)
        self.location(location)
        time.sleep(2)
        self.get_np(policy)
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_done_button())
        time.sleep(4)
        policy = self.mob_login_web_elements.get_policy_details()
        self.utils.print_info("Policy assigned during onboarding: ", policy)
        location = self.mob_login_web_elements.get_location_details()
        self.utils.print_info("Location assigned during onboarding: ", location)

    def refresh_popup(self):
        self.utils.print_info("click on checkbox")
        self.auto_actions.click(self.mob_login_web_elements.get_refresh_popup_checkbox())
        time.sleep(2)
        self.utils.print_info("click on dismiss")
        self.auto_actions.click(self.mob_login_web_elements.get_refresh_popup_dismiss())
        time.sleep(3)

    def refresh_device(self):
        self.utils.print_info("refresh cache")
        self.auto_actions.click(self.mob_login_web_elements.get_refresh_option())
        time.sleep(8)

    def return_from_device_home(self):
        self.utils.print_info("click on backward link on device home screen")
        self.auto_actions.click(self.mob_login_web_elements.get_device_home_backward())
        time.sleep(1)
