from xiq.defs.extreme_guest.ExtremeGuestSummaryWebElementsDefs import ExtremeGuestSummaryWebElementsDefs
from extauto.common.WebElementHandler import *


class ExtremeGuestSummaryWebElements(ExtremeGuestSummaryWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_extreme_guest_summary_user_walkin_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_user_walkin_widget)

    def get_extreme_guest_summary_dwell_time_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_dwell_time_widget)

    def get_extreme_guest_summary_visitors_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_visitors_widget)

    def get_extreme_guest_summary_visitors_widget_today(self):
        return self.weh.get_element(self.extreme_guest_summary_visitors_widget_today)

    def get_extreme_guest_summary_visitors_widget_yesterday(self):
        return self.weh.get_element(self.extreme_guest_summary_visitors_widget_yesterday)

    def get_extreme_guest_summary_new_user_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_new_user_widget)

    def get_extreme_guest_summary_new_user_widget_today(self):
        return self.weh.get_element(self.extreme_guest_summary_new_user_widget_today)

    def get_extreme_guest_summary_new_user_widget_yesterday(self):
        return self.weh.get_element(self.extreme_guest_summary_new_user_widget_yesterday)

    def get_extreme_guest_summary_conversion_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_conversion_widget)

    def get_extreme_guest_summary_conversion_widget_connected(self):
        return self.weh.get_element(self.extreme_guest_summary_conversion_widget_connected)

    def get_extreme_guest_summary_conversion_widget_onboarded(self):
        return self.weh.get_element(self.extreme_guest_summary_conversion_widget_onboarded)

    def get_extreme_guest_summary_gender_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_gender_widget)

    def get_extreme_guest_summary_gender_widget_unspecified(self):
        return self.weh.get_element(self.extreme_guest_summary_gender_widget_unspecified)

    def get_extreme_guest_summary_age_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_age_widget)

    def get_extreme_guest_summary_facebook_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_facebook_widget)

    def get_extreme_guest_summary_google_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_google_widget)

    def get_extreme_guest_summary_linkedin_widget(self):
        return self.weh.get_element(self.extreme_guest_summary_linkedin_widget)