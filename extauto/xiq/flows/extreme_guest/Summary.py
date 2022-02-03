import common.CloudDriver
from common.Screen import Screen
from common.Utils import Utils
from common.AutoActions import AutoActions
from xiq.flows.common.Navigator import Navigator
from xiq.elements.extreme_guest.ExtremeGuestSummaryWebElements import ExtremeGuestSummaryWebElements
from xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class Summary(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.driver = common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.summary_web_elem = ExtremeGuestSummaryWebElements()
        self.ext_guest = ExtremeGuest()

    def check_all_summary_page_widgets(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check all widgets
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check all summary page widgets''

        :return: 1 if all widgets are displayed
        """
        all_displayed = True
        self.ext_guest.go_to_extreme_guest_page()
        if self.summary_web_elem.get_extreme_guest_summary_age_widget().is_displayed():
            self.utils.print_info("summary_age_widget is displayed")
        else:
            self.utils.print_info("summary_age_widget is not displayed")
            all_displayed = False

        if self.summary_web_elem.get_extreme_guest_summary_conversion_widget().is_displayed():
            self.utils.print_info("conversion_widget is displayed")
        else:
            self.utils.print_info("conversion_widget is not displayed")
            all_displayed = False

        if self.summary_web_elem.get_extreme_guest_summary_dwell_time_widget().is_displayed():
            self.utils.print_info("dwell_time_widget is displayed")
        else:
            self.utils.print_info("dwell_time_widget is not displayed")
            all_displayed = False

        if self.summary_web_elem.get_extreme_guest_summary_gender_widget().is_displayed():
            self.utils.print_info("gender_widget is displayed")
        else:
            self.utils.print_info("gender_widget is not displayed")
            all_displayed = False

        if self.summary_web_elem.get_extreme_guest_summary_new_user_widget().is_displayed():
            self.utils.print_info("new_user_widget is displayed")
        else:
            self.utils.print_info("new_user_widget is not displayed")
            all_displayed = False

        if self.summary_web_elem.get_extreme_guest_summary_user_walkin_widget().is_displayed():
            self.utils.print_info("user_walkin_widget is displayed")
        else:
            self.utils.print_info("user_walkin_widget is not displayed")
            all_displayed = False

        if self.summary_web_elem.get_extreme_guest_summary_visitors_widget().is_displayed():
            self.utils.print_info("visitors_widget is displayed")
        else:
            self.utils.print_info("visitors_widget is not displayed")
            all_displayed = False

        if all_displayed:
            return 1
        else:
            return 0


    def check_summary_page_visitor_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check visitor widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page visitor widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_visitors_widget().is_displayed():
            self.utils.print_info("visitors_widget is displayed")
        else:
            self.utils.print_info("visitors_widget is not displayed")
            return -1

        self.utils.print_info("Checking Visitor widget data")
        if today_visitors := self.summary_web_elem.get_extreme_guest_summary_visitors_widget_today():
            if today_visitors.text:
                self.utils.print_info(f"Today's Visitor widget data: {today_visitors.text}")
        if yesterday_visitors := self.summary_web_elem.get_extreme_guest_summary_visitors_widget_yesterday():
            if yesterday_visitors.text:
                self.utils.print_info(f"Yesterdays's Visitor widget data: {yesterday_visitors.text}")

        return 1

    def check_summary_page_new_user_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check new user widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page new user widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_new_user_widget().is_displayed():
            self.utils.print_info("new_user_widget is displayed")
        else:
            self.utils.print_info("new_user_widget is not displayed")
            return -1

        self.utils.print_info("Checking New User widget data")
        if today_new_users := self.summary_web_elem.get_extreme_guest_summary_new_user_widget_today():
            if today_new_users.text:
                self.utils.print_info(f"Today's New User widget data: {today_new_users.text}")
        if yesterday_new_users := self.summary_web_elem.get_extreme_guest_summary_new_user_widget_yesterday():
            if yesterday_new_users.text:
                self.utils.print_info(f"Yesterdays's New User widget data: {yesterday_new_users.text}")

        return 1

    def check_summary_page_conversion_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check conversion widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page conversion widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_conversion_widget().is_displayed():
            self.utils.print_info("conversion_widget is displayed")
        else:
            self.utils.print_info("conversion_widget is not displayed")
            return -1

        self.utils.print_info("Checking Conversion widget data")
        if connected_users := self.summary_web_elem.get_extreme_guest_summary_conversion_widget_connected():
            if connected_users.text:
                self.utils.print_info(f"Today's New User widget data: {connected_users.text}")
        if onboarded_users := self.summary_web_elem.get_extreme_guest_summary_conversion_widget_onboarded():
            if onboarded_users.text:
                self.utils.print_info(f"Yesterdays's New User widget data: {onboarded_users.text}")

        return 1

    def check_summary_page_gender_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check gender widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page gender widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_gender_widget().is_displayed():
            self.utils.print_info("gender_widget is displayed")
        else:
            self.utils.print_info("gender_widget is not displayed")
            return -1

        self.utils.print_info("Checking Gender widget data")
        if gender_unspecified := self.summary_web_elem.get_extreme_guest_summary_gender_widget_unspecified():
            if gender_unspecified.text:
                self.utils.print_info(f"Today's gender unspecified widget data: {gender_unspecified.text}")

        return 1

    def check_summary_page_facebook_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check facebook widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page facebook widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_facebook_widget().is_displayed():
            self.utils.print_info("Facebook widget is displayed")
        else:
            self.utils.print_info("Facebook widget is not displayed")
            return -1

        self.utils.print_info("Checking Facebook widget data")
        if facebook_data := self.summary_web_elem.get_extreme_guest_summary_facebook_widget():
            if facebook_data.text:
                self.utils.print_info(f"Today's Facebook widget data: {facebook_data.text}")

        return 1

    def check_summary_page_google_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check google widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page google widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_google_widget().is_displayed():
            self.utils.print_info("Google widget is displayed")
        else:
            self.utils.print_info("Google widget is not displayed")
            return -1

        self.utils.print_info("Checking Google widget data")
        if google_data := self.summary_web_elem.get_extreme_guest_summary_google_widget():
            if google_data.text:
                self.utils.print_info(f"Today's Google widget data: {google_data.text}")

        return 1

    def check_summary_page_linkedin_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page linkedin widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_linkedin_widget().is_displayed():
            self.utils.print_info("linkedin widget is displayed")
        else:
            self.utils.print_info("linkedin widget is not displayed")
            return -1

        self.utils.print_info("Checking linkedin widget data")
        if linkedin_data := self.summary_web_elem.get_extreme_guest_summary_linkedin_widget():
            if linkedin_data.text:
                self.utils.print_info(f"Today's linkedin widget data: {linkedin_data.text}")

        return 1

    def check_summary_page_total_users_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page total users widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_total_users_widget().is_displayed():
            self.utils.print_info("total_users widget is displayed")
        else:
            self.utils.print_info("total_users widget is not displayed")
            return -1

        self.utils.print_info("Checking total_users widget data")
        if total_users_data := self.summary_web_elem.get_extreme_guest_summary_total_users_widget():
            if total_users_data.text:
                self.utils.print_info(f"Today's total_users widget data: {total_users_data.text}")

        return 1

    def check_summary_page_online_users_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page online users widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_online_users_widget().is_displayed():
            self.utils.print_info("online_users widget is displayed")
        else:
            self.utils.print_info("online_users widget is not displayed")
            return -1

        self.utils.print_info("Checking online_users widget data")
        if online_users_data := self.summary_web_elem.get_extreme_guest_summary_online_users_widget():
            if online_users_data.text:
                self.utils.print_info(f"Today's online_users widget data: {online_users_data.text}")

        return 1

    def check_summary_page_total_clients_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page total clients widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_total_clients_widget().is_displayed():
            self.utils.print_info("total_clients widget is displayed")
        else:
            self.utils.print_info("total_clients widget is not displayed")
            return -1

        self.utils.print_info("Checking total_clients widget data")
        if total_clients_data := self.summary_web_elem.get_extreme_guest_summary_total_clients_widget():
            if total_clients_data.text:
                self.utils.print_info(f"Today's total_clients widget data: {total_clients_data.text}")

        return 1
    
    def check_summary_page_online_clients_widget_data(self):
        """
        -This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''check summary page total clients widget data''

        :return: 1 if all widgets are displayed
        """
        if self.summary_web_elem.get_extreme_guest_summary_online_clients_widget().is_displayed():
            self.utils.print_info("online_clients widget is displayed")
        else:
            self.utils.print_info("online_clients widget is not displayed")
            return -1

        self.utils.print_info("Checking online_clients widget data")
        if online_clients_data := self.summary_web_elem.get_extreme_guest_summary_online_clients_widget():
            if online_clients_data.text:
                self.utils.print_info(f"Today's online_clients widget data: {online_clients_data.text}")

        return 1
