from xiq.defs.extreme_guest.ExtremeGuestLandingWebElementsDefs import ExtremeGuestLandingWebElementsDefs
from common.WebElementHandler import *


class ExtremeGuestLandingWebElements(ExtremeGuestLandingWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_landing_user_conversion_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_user_conversion_widget)

    def get_extreme_guest_landing_user_walkin_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_user_walkin_widget)

    def get_extreme_guest_landing_user_dwell_time_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_user_dwell_time_widget)

    def get_extreme_guest_landing_visitors_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_visitors_widget)

    def get_extreme_guest_landing_new_users_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_new_users_widget)

    def get_extreme_guest_landing_client_distribution_widget(self):
        return self.weh.get_element(self.extreme_guest_landing_client_distribution_widget)
