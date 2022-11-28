from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestAnalyzeUsersWebElements import ExtremeGuestAnalyzeUsersWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class AnalyzeUsers(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.users_web_elem = ExtremeGuestAnalyzeUsersWebElements()
        self.ext_guest = ExtremeGuest()

    def go_to_analyze_users_page(self):
        """
        - This keyword Will Navigate to Extreme Guest Analyze Users Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Analyze--> Users
        - Keyword Usage:
            ''Go to Analyze Users Page''

        :return: 1 if success
        """

        self.utils.print_info("Clicking on Extreme Guest Analyze > Users Page")
        self.auto_actions.click_reference(self.users_web_elem.get_extreme_guest_analyze_users_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def check_if_the_user_exists(self, username, location):
        """
        - This keyword Will Check if the mac address is present in the Extreme Guest Analyze Users Page
        - Keyword Usage:
            ''Check If The User Exists        ${USERNAME}        ${LOCATION_TREE}''

        :return: 1 if success
        """

        self.utils.print_info("Clicking on the Location")
        self.auto_actions.click(self.users_web_elem.get_extreme_guest_analyze_users_grid_location(location))
        sleep(2)

        self.utils.print_info("Checking the Username in the Analyze Users Grid")
        if self.users_web_elem.get_extreme_guest_analyze_users_grid_username(username):
            self.screen.save_screen_shot()
            sleep(2)
            return 1
        return -1