from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestAnalyzeClientsWebElements import ExtremeGuestAnalyzeClientsWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest
from extauto.common.CommonValidation import CommonValidation


class AnalyzeClients(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.clients_web_elem = ExtremeGuestAnalyzeClientsWebElements()
        self.ext_guest = ExtremeGuest()
        self.common_validation = CommonValidation()

    def go_to_analyze_clients_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Analyze Clients Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Analyze--> Clients
        - Keyword Usage:
            ''Go to Analyze Clients Page''

        :return: 1 if success
        """
        
        self.utils.print_info("Clicking on Extreme Guest Analyze > Clients Page")
        self.auto_actions.click_reference(self.clients_web_elem.get_extreme_guest_analyze_clients_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def check_if_the_client_exists(self, mac, location, **kwargs):
        """
        -This keyword Will Check if the mac address is present in the Extreme Guest Analyze Clients Page
        - Keyword Usage:
            ''Check If The Client Exists        ${AP_MAC}        ${LOCATION_TREE}''

        :return: 1 if success
        """

        self.utils.print_info("Clicking on Total Clients Key Metrics")
        self.auto_actions.click_reference(self.clients_web_elem.get_extreme_guest_analyze_clients_total_clients)
        sleep(2)

        self.utils.print_info("Clicking on Location")
        self.auto_actions.click(self.clients_web_elem.get_extreme_guest_analyze_clients_grid_location(location))
        sleep(2)

        self.utils.print_info("Checking the Client mac address in the Analyze Clients Grid")
        if self.clients_web_elem.get_extreme_guest_analyze_clients_grid_macaddress(mac):
            self.screen.save_screen_shot()
            sleep(2)
            return 1

        kwargs['fail_msg'] = "Client mac address is not in the Analyze Clients Grid"
        self.common_validation.failed(**kwargs)
        return -1