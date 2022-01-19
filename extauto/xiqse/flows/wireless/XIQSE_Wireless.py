from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.wireless.WirelessWebElements import WirelessWebElements


class XIQSE_Wireless(WirelessWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_wireless_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Tab    Dashboard``
          - ``XIQSE Wireless Select Tab    Network``
          - ``XIQSE Wireless Select Tab    Controllers``
          - ``XIQSE Wireless Select Tab    Access Points``
          - ``XIQSE Wireless Select Tab    Clients``
          - ``XIQSE Wireless Select Tab    Threats``
          - ``XIQSE Wireless Select Tab    Reports``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Dashboard":
            the_tab = self.get_dashboard_tab()
        elif tab_name == "Network":
            the_tab = self.get_network_tab()
        elif tab_name == "Controllers":
            the_tab = self.get_controllers_tab()
        elif tab_name == "Access Points":
            the_tab = self.get_access_points_tab()
        elif tab_name == "Clients":
            the_tab = self.get_clients_tab()
        elif tab_name == "Threats":
            the_tab = self.get_threats_tab()
        elif tab_name == "Reports":
            the_tab = self.get_reports_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Wireless page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Wireless page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wireless_select_dashboard_tab(self):
        """
         - This keyword selects the Dashboard tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Dashboard Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Dashboard")

    def xiqse_wireless_select_network_tab(self):
        """
         - This keyword selects the Network tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Network Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Network")

    def xiqse_wireless_select_controllers_tab(self):
        """
         - This keyword selects the Controllers tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Controllers Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Controllers")

    def xiqse_wireless_select_access_points_tab(self):
        """
         - This keyword selects the Access Points tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Access Points Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Access Points")

    def xiqse_wireless_select_clients_tab(self):
        """
         - This keyword selects the Clients tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Clients Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Clients")

    def xiqse_wireless_select_threats_tab(self):
        """
         - This keyword selects the Threats tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Threats Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Threats")

    def xiqse_wireless_select_reports_tab(self):
        """
         - This keyword selects the Reports tab of the Wireless page
         - Keyword Usage
          - ``XIQSE Wireless Select Reports Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_wireless_select_tab("Reports")
