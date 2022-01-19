import extauto.common.CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestLandingWebElements import ExtremeGuestLandingWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class Landing(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.landing_web_elem = ExtremeGuestLandingWebElements()
        self.ext_guest = ExtremeGuest()

    def check_all_landing_page_widgets(self):
        """
        -This keyword Will Navigate to Extreme Guest Page and check all widgets
        - Flow: XIQ--> Extreme Guest
        - Keyword Usage:
            ''check all landing page widgets''

        :return: 1 if all widgets are displayed

        :return:
        """
        all_displayed = True
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

        if self.landing_web_elem.get_extreme_guest_landing_user_dwell_time_widget().is_displayed():
            self.utils.print_info("user_dwell_time_widget is displayed")
        else:
            self.utils.print_info("user_dwell_time_widget is not displayed")
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
            return 1
        else:
            return 0
