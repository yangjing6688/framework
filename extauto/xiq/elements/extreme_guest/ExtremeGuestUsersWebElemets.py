from extauto.xiq.defs.extreme_guest.ExtremeGuestUsersWebElementsDefs import ExtremeGuestUsersWebElementsDefs
from extauto.common.WebElementHandler import *
from extauto.common.Utils import Utils


class ExtremeGuestUsersWebElements(ExtremeGuestUsersWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.utils = Utils()

    def get_extreme_guest_users_tab(self):
        return self.weh.get_element(self.extreme_guest_users_tab)

    def get_extreme_guest_users_add_button(self):
        return self.weh.get_element(self.extreme_guest_users_add_button)

    def get_extreme_guest_users_create_bulk_users_button(self):
        return self.weh.get_element(self.extreme_guest_users_create_bulk_users_button)

    def get_create_bulk_users_access_group_drop_down_button(self):
        return self.weh.get_element(self.create_bulk_users_access_group_drop_down_button)

    def get_create_bulk_users_access_group_drop_down_options(self):
        return self.weh.get_elements(self.create_bulk_users_access_group_drop_down_options)

    def get_create_bulk_users_number_of_vouchers_textfield(self):
        return self.weh.get_element(self.create_bulk_users_number_of_vouchers_textfield)

    def get_extreme_guest_users_locations_root_name(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_root_name)

    def get_extreme_guest_users_locations_city_name(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_city_name)

    def get_extreme_guest_users_locations_building_name(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_building_name)

    def get_extreme_guest_users_locations_floor_name(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_floor_name)

    def get_extreme_guest_users_locations_root_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_root_name_expand_button)

    def get_extreme_guest_users_locations_city_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_city_name_expand_button)

    def get_extreme_guest_users_locations_building_name_expand_button(self):
        return self.weh.get_elements(self.extreme_guest_users_locations_building_name_expand_button)

    def get_extreme_guest_users_create_bulk_users_close_button(self):
        return self.weh.get_element(self.extreme_guest_users_create_bulk_users_close_button)

    def get_extreme_guest_users_create_bulk_users_print_button(self):
        return self.weh.get_element(self.extreme_guest_users_create_bulk_users_print_button)

    def get_extreme_guest_users_create_bulk_users_create_button(self):
        return self.weh.get_element(self.extreme_guest_users_create_bulk_users_create_button)

    def get_extreme_guest_users_create_bulk_users_clear_button(self):
        return self.weh.get_element(self.extreme_guest_users_create_bulk_users_clear_button)

    def get_create_bulk_users_location_drop_down_button(self):
        return self.weh.get_element(self.create_bulk_users_location_drop_down_button)

    def get_extreme_guest_users_grid_rows(self):
        return self.weh.get_elements(self.extreme_guest_users_grid_rows)

    def get_extreme_facebook_guest_users(self):
        return self.weh.get_element(self.extreme_facebook_guest_users).text

    def get_extreme_linkedin_guest_users(self):
        return self.weh.get_element(self.extreme_linkedin_guest_users).text

    def get_extreme_guest_users_grid_row_cells(self, search_string):
        cells = self.weh.get_elements(self.extreme_guest_users_grid_row_cells)
        for cell in cells:
            if search_string in cell.text:
                return cell

    def get_extreme_guest_users_grid_row_cells_user_name_list(self):
        return self.weh.get_elements(self.extreme_guest_users_grid_row_cells_user_name_list)

    def get_extreme_guest_users_delete_button(self):
        return self.weh.get_element(self.extreme_guest_users_delete_button)

    def get_extreme_guest_users_delete_ok_button(self):
        return self.weh.get_element(self.extreme_guest_users_delete_ok_button)

    def get_extreme_guest_users_delete_ok_button_duplicate(self):
        return self.weh.get_element(self.extreme_guest_users_delete_ok_button_duplicate)

    def get_extreme_guest_users_delete_status_ok_button(self):
        return self.weh.get_element(self.extreme_guest_users_delete_status_ok_button)

    def get_extreme_guest_users_print_user_cells(self):
        return self.weh.get_elements(self.extreme_guest_users_print_user_cells)

    def get_extreme_guest_users_print_password_cells(self):
        return self.weh.get_elements(self.extreme_guest_users_print_password_cells)
