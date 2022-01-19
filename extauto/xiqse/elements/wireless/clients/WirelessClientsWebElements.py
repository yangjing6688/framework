from extauto.common.WebElementHandler import *
from xiqse.defs.wireless.clients.WirelessClientsWebElementsDefinitions import *


class WirelessClientsWebElements(WirelessClientsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_clients_tab(self):
        """
        :return: Clients Sub Tab on the Wireless> Clients page
        """
        return self.weh.get_element(self.clients_tab)

    def get_client_events_tab(self):
        """
        :return: Client Events Sub Tab on the Wireless> Clients page
        """
        return self.weh.get_element(self.client_events_tab)

    def get_event_analyzer_tab(self):
        """
        :return: Event Analyzer Sub Tab on the Wireless> Clients page
        """
        return self.weh.get_element(self.event_analyzer_tab)

    def get_event_collection_disabled_dialog(self):
        """
        :return: "Event Collection Disabled" dialog
        """
        return self.weh.get_element(self.event_collection_disabled_dialog)

    def get_event_collection_disabled_dialog_ok_button(self):
        """
        :return: OK button for the message box
        """
        return self.weh.get_element(self.event_collection_disabled_dialog_ok_button)
