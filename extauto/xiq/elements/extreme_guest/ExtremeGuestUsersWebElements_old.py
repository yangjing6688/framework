from extauto.xiq.defs.extreme_guest.ExtremeGuestUsersWebElementsDefs_old import ExtremeGuestUsersWebElementsDefs
from extauto.common.WebElementHandler import WebElementHandler


class ExtremeGuestWebElements(ExtremeGuestUsersWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_users_add_button(self):
        return self.weh.get_element(self.extreme_guest_users_add_button)

    def get_extreme_guest_users_delete_button(self):
        return self.weh.get_element(self.extreme_guest_users_delete_button)

    def get_extreme_guest_users_refresh_button(self):
        return self.weh.get_element(self.extreme_guest_users_refresh_button)

    def get_extreme_guest_users_add_create_user_menu(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_user_menu)

    def get_extreme_guest_users_add_create_bulk_user_menu(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_menu)

    def get_extreme_guest_users_add_create_bulk_user_access_grp_dropdown(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_access_grp_dropdown)

    def get_extreme_guest_users_add_create_bulk_user_access_grp_dropdown_items(self):
        return self.weh.get_elements(self.extreme_guest_users_add_create_bulk_user_access_grp_dropdown_items)

    def get_extreme_guest_users_add_create_bulk_user_description(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_description)

    def get_extreme_guest_users_add_create_bulk_user_location_dropdown(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_location_dropdown)

    def get_extreme_guest_users_add_create_bulk_user_location_dropdown_items(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_location_dropdown_items)

    def get_extreme_guest_users_add_create_bulk_user_create_button(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_create_button)

    def get_extreme_guest_users_add_create_bulk_user_clear_button(self):
        return self.weh.get_element(self.extreme_guest_users_add_create_bulk_user_clear_button)