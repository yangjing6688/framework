from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.wireless.clients.WirelessClientsWebElements import WirelessClientsWebElements


class XIQSE_WirelessClients(WirelessClientsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_wireless_clients_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Wireless> Clients page
         - Keyword Usage
          - ``XIQSE Wireless Clients Select Tab    Clients``
          - ``XIQSE Wireless Clients Select Tab    Client Events``
          - ``XIQSE Wireless Clients Select Tab    Event Analyzer``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Clients":
            the_tab = self.get_clients_tab()
        elif tab_name == "Client Events":
            the_tab = self.get_client_events_tab()
        elif tab_name == "Event Analyzer":
            the_tab = self.get_event_analyzer_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Wireless> Clients page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Wireless> Clients page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wireless_clients_select_clients_tab(self):
        """
         - This keyword selects the Clients tab on the Wireless> Clients Tab
         - Keyword Usage
          - ``XIQSE Wireless Clients Select Clients Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_clients_select_tab("Clients")

    def xiqse_wireless_clients_select_client_events_tab(self):
        """
         - This keyword selects the Client Events tab on the Wireless> Clients Tab
         - Keyword Usage
          - ``XIQSE Wireless Clients Select Client Events Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_clients_select_tab("Client Events")

    def xiqse_wireless_clients_select_event_analyzer_tab(self):
        """
         - This keyword selects the Event Analyzer tab on the Wireless> Clients Tab
         - Keyword Usage
          - ``XIQSE Wireless Clients Select Event Analyzer Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_clients_select_tab("Event Analyzer")

    def xiqse_wireless_clients_close_event_collection_disabled_dialog(self):
        """
         - This keyword closes the Event Collection Disabled dialog, if it is displayed.
         - Keyword Usage
          - ``XIQSE Wireless Clients Close Event Collection Disabled Dialog``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        try:
            msg_dlg = self.get_event_collection_disabled_dialog()
            if msg_dlg:
                ok_btn = self.get_event_collection_disabled_dialog_ok_button()
                if ok_btn:
                    self.utils.print_info("Clicking OK button in Event Collection Disabled dialog")
                    self.auto_actions.click(ok_btn)
                    sleep(1)

                else:
                    self.utils.print_info("Could not find OK button for message box")
            else:
                self.utils.print_info("Event Collection Disabled dialog was not displayed")
                ret_val = 1
        except Exception as e:
            self.utils.print_info("Error: ", e)

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
