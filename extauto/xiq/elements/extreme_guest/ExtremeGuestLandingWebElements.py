from extauto.xiq.defs.extreme_guest.ExtremeGuestLandingWebElementsDefs import ExtremeGuestLandingWebElementsDefs
from extauto.common.WebElementHandler import WebElementHandler


class ExtremeGuestLandingWebElements(ExtremeGuestLandingWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_landing_user_conversion_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_user_conversion_widget)

    def get_extreme_guest_landing_user_walkin_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_user_walkin_widget)

    def get_extreme_guest_landing_sessions_dwell_time_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_sessions_dwell_time_widget)

    def get_extreme_guest_landing_visitors_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_visitors_widget)

    def get_extreme_guest_landing_new_users_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_new_users_widget)

    def get_extreme_guest_landing_client_distribution_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_client_distribution_widget)

    def get_extreme_guest_map_location_marker(self):
        return self.weh.get_element(self.extreme_guest_map_location_marker)

    def get_extreme_guest_map_location_marker_header(self):
        return self.weh.get_element(self.extreme_guest_map_location_marker_header)

    def get_extreme_guest_map_location_marker_online_users_count(self):
        return self.weh.get_element(self.extreme_guest_map_location_marker_online_users_count)

    def get_extreme_guest_map_location_marker_total_users_count(self):
        return self.weh.get_element(self.extreme_guest_map_location_marker_total_users_count)

    def get_extreme_guest_map_location_marker_online_table_rows_today(self, row_title):
        return self.weh.get_template_element(self.extreme_guest_map_location_marker_online_table_rows_today, row=row_title)

    def get_extreme_guest_map_location_marker_online_table_rows_yesterday(self, row_title):
        return self.weh.get_template_element(self.extreme_guest_map_location_marker_online_table_rows_yesterday, row=row_title)