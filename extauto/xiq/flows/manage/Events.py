from time import sleep
import datetime
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiq.elements.EventsWebElements import *
from xiq.flows.manage.Devices import *
from xiq.flows.common.Navigator import Navigator

class Events:

    def __init__(self):
        self.navigator = Navigator()
        self.EventsWebElements = EventsWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.devices = Devices()
        self.screen = Screen()

    def _get_events_grid_content(self):
        """
        - This keyword gets Events Page grid contents.
        :return: grid contents
        """
        self.utils.print_info("Getting Events grid content...")
        grid_content = self.EventsWebElements.get_events_content_grid()
        return grid_content

    def verify_events_grid_details(self, mac=None, events_details=None, nav=0):
        """
        - This keyword checks if Events page grid contains the list of strings(events_details) provided as argument and it also checks for MAC.
        -Flow: Manage --> Events --> Checks for events details and MAC.
        - Keyword Usage:
         - ``Verify Events Grid Details    mac=${MAC}       events_details=Client Connect Down,Connection Change    nav=1``
         - ``Verify Events Grid Details    events_details=Client Connect Down,Connection Change``
        :param mac: MAC of the device
        :param events_details: details to be checked, it needs to be provided in the above format(comma separated format).
        :param nav: Navigates to Events Page if nav=1
        :return: 1 if success else -1
        """
        if nav:
            self.navigator.navigate_manage_events()

        if self._get_events_grid_content():
            rows = self._get_events_grid_content()
            events_list = events_details.split(',')
            # self.utils.print_info("EVENTS LIST: ", events_list)
            for row in rows:
                # self.utils.print_info(">>Row: ", row.text)
                res = [ele for ele in events_list if (ele in row.text)]
                time_now = datetime.datetime.now().strftime("%Y-%m-%d %H")
                if time_now in row.text:
                    if res:
                        self.utils.print_info("Event details and time match")
                        if mac:
                            if mac in row.text:
                                self.utils.print_info("Events grid details verified")
                                return 1
                        else:
                            self.utils.print_info("Events grid details verified")
                            return 1
        return -1

    def verify_events_pagination(self, events_details, nav=0):
        """
        - This keyword verfies pagination by checking the events details on page 2 of Events Page.
        -Flow: Manage --> Events --> Checks for pagination.
        - Keyword Usage:
         - ``Verify Events Pagination    events_details=Client Connect Down,Connection Change    nav=1``
         - ``Verify Events Pagination    events_details=Client Connect Down,Connection Change``
        :param events_details: details to be checked, it needs to be provided in the above format(comma separated format).
        :param nav: Navigates to Events Page if nav=1
        :return: 1 if success else -1
        """
        if nav:
            self.navigator.navigate_manage_events()
        self.utils.print_info("events details: ", events_details)
        page = self.EventsWebElements.get_events_pagination()
        self.utils.print_info("Clicking on Page 2 in Events Page.")
        self.auto_actions.click(page)
        res = self.verify_events_grid_details(events_details=events_details)
        self.utils.print_info("Pagination verified.")
        return res

    def check_events_download(self):
        """
        - This keyword checks if download works on Events Page.
        -Flow: Manage --> Events --> Checks for Download.
        - Keyword Usage:
         - ``Check Events Download``
        :return: 1 if success else -1
        """
        try:
            self.utils.print_info("Clicking on download button.")
            download_btn = self.EventsWebElements.get_events_download_button()
            if download_btn.is_displayed() and download_btn.is_enabled():
                self.auto_actions.click(self.EventsWebElements.get_events_download_button())
                self.utils.print_info("Events Download verified.")
                return 1
            return -1
        except Exception as e:
            self.utils.print_info("Unable to verify Events Download", e)
            return -1