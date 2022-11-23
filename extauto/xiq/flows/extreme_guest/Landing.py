from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestLandingWebElements import ExtremeGuestLandingWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest
from extauto.common.CommonValidation import CommonValidation
from time import sleep



class Landing(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.landing_web_elem = ExtremeGuestLandingWebElements()
        self.ext_guest = ExtremeGuest()
        self.common_validation = CommonValidation()

    def check_all_landing_page_widgets(self, **kwargs):
        """
        -This keyword Will Navigate to Extreme Guest Page and check all widgets
        - Flow: XIQ--> Extreme Guest
        - Keyword Usage:
            ''check all landing page widgets''

        :return: 1 if all widgets are displayed

        :return:
        """
        all_displayed = True
        sleep(10)
        self.ext_guest.go_to_extreme_guest_landing_page()
        if self.landing_web_elem.get_extreme_guest_landing_client_distribution_widget().is_displayed():
            self.utils.print_info("client_distribution_widget is displayed")
        else:
            self.utils.print_info("client_distribution_widget is not displayed")
            all_displayed = False

        if self.landing_web_elem.get_extreme_guest_landing_new_users_widget().is_displayed():
            self.utils.print_info("new_users_widget is displayed")
        else:
            self.utils.print_info("new_users_widget is not displayed")
            all_displayed = False

        if self.landing_web_elem.get_extreme_guest_landing_user_conversion_widget().is_displayed():
            self.utils.print_info("user_conversion_widget is displayed")
        else:
            self.utils.print_info("user_conversion_widget is not displayed")
            all_displayed = False

        if self.landing_web_elem.get_extreme_guest_landing_sessions_dwell_time_widget().is_displayed():
            self.utils.print_info("sessions_dwell_time_widget is displayed")
        else:
            self.utils.print_info("sessions_dwell_time_widget is not displayed")
            all_displayed = False

        if self.landing_web_elem.get_extreme_guest_landing_user_walkin_widget().is_displayed():
            self.utils.print_info("user_walkin_widget is displayed")
        else:
            self.utils.print_info("user_walkin_widget is not displayed")
            all_displayed = False

        if self.landing_web_elem.get_extreme_guest_landing_visitors_widget().is_displayed():
            self.utils.print_info("visitors_widget is displayed")
        else:
            self.utils.print_info("visitors_widget is not displayed")
            all_displayed = False

        if all_displayed:
            kwargs['pass_msg'] = "Successfully Navigated to Extreme Guest Page and check all widgets"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"'check_all_landing_page_widgets()' -> {all_displayed}"
            self.common_validation.failed(**kwargs)
            return 0

    def check_map_location_widget(self, **kwargs):
        """
        -This keyword Will Navigate to Extreme Guest Page and check map widget marker
        - Flow: XIQ--> Extreme Guest
        - Keyword Usage:
            ''Check Map Location Widget''

        :return: 1 if widget is displayed
        """
        if self.auto_actions.click_reference(self.landing_web_elem.get_extreme_guest_map_location_marker):
            print("Online Users Count: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_users_count().text)
            print("Total Users Count: ", self.landing_web_elem.get_extreme_guest_map_location_marker_total_users_count().text)
            print("Total Users Today: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_table_rows_today('Total Users').text)
            print("Total Users Yesterday: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_table_rows_yesterday('Total Users').text)
            print("New Users Today: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_table_rows_today('New Users').text)
            print("New Users Yesterday: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_table_rows_yesterday('New Users').text)
            print("Return Users Today: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_table_rows_today('Return Users').text)
            print("Return Users Yesterday: ", self.landing_web_elem.get_extreme_guest_map_location_marker_online_table_rows_yesterday('Return Users').text)

            kwargs['pass_msg'] = "Successfully Navigated to Extreme Guest Page and check map widget marker"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "'check_map_location_widget()' -> Widget is not displayed"
        self.common_validation.failed(**kwargs)
        return -1