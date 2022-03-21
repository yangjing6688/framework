from extauto.xiq.defs.extreme_guest.ExtremeGuestNotificationWebElementsDefs import ExtremeGuestNotificationWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestNotificationWebElements(ExtremeGuestNotificationWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_notification_policy_tab(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_tab)

    def get_extreme_guest_notification_policy_add_policy(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_policy)

    def get_extreme_guest_notification_policy_refresh_policy(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_refresh_policy)

    def get_extreme_guest_notification_policy_delete_policy(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_delete_policy)

    def get_extreme_guest_notification_policy_grid(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_grid)

    def get_extreme_guest_notification_grid_rows(self):
        return self.weh.get_elements(self.extreme_guest_notification_grid_rows)

    def get_extreme_guest_notification_grid_row_cells_user_name_list(self, search_string):
        cells = self.weh.get_elements(self.extreme_guest_notification_grid_row_cells_name_list)
        for cell in cells:
            if search_string in cell.text:
                return cell

    def get_extreme_guest_notification_policy_add_name(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_name)

    def get_extreme_guest_notification_policy_add_description(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_description)

    def get_extreme_guest_notification_policy_add_policy_type_user(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_policy_type_user)

    def get_extreme_guest_notification_policy_add_policy_type_sponsor(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_policy_type_sponsor)

    def get_extreme_guest_notification_policy_add_sms_enable(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_sms_enable)

    def get_extreme_guest_notification_policy_add_sms_sponsor_phone_number(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_sms_sponsor_phone_number)

    def get_extreme_guest_notification_policy_add_sms_message(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_sms_message)

    def get_extreme_guest_notification_policy_add_email_enable(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_email_enable)

    def get_extreme_guest_notification_policy_add_email_subject(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_email_subject)

    def get_extreme_guest_notification_policy_add_email_message(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_email_message)

    def get_extreme_guest_notification_policy_add_save_button(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_save_button)

    def get_extreme_guest_notification_policy_add_cancel_button(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_cancel_button)

    def get_extreme_guest_notification_policy_add_save_ok_button(self):
        return self.weh.get_element(self.extreme_guest_notification_policy_add_save_ok_button)