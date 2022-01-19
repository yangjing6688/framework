from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.analytics.AnalyticsWebElements import AnalyticsWebElements


class XIQSE_Analytics(AnalyticsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_analytics_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Tab    Dashboard``
          - ``XIQSE Analytics Select Tab    Browser``
          - ``XIQSE Analytics Select Tab    Application Flows``
          - ``XIQSE Analytics Select Tab    Fingerprints``
          - ``XIQSE Analytics Select Tab    Packet Captures``
          - ``XIQSE Analytics Select Tab    Configuration``
          - ``XIQSE Analytics Select Tab    Reports``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Dashboard":
            the_tab = self.get_dashboard_tab()
        elif tab_name == "Browser":
            the_tab = self.get_browser_tab()
        elif tab_name == "Application Flows":
            the_tab = self.get_application_flows_tab()
        elif tab_name == "Fingerprints":
            the_tab = self.get_fingerprints_tab()
        elif tab_name == "Packet Captures":
            the_tab = self.get_packet_captures_tab()
        elif tab_name == "Configuration":
            the_tab = self.get_configuration_tab()
        elif tab_name == "Reports":
            the_tab = self.get_reports_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Analytics page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Analytics page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_select_dashboard_tab(self):
        """
         - This keyword selects the Dashboard tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Dashboard Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Dashboard")

    def xiqse_analytics_select_browser_tab(self):
        """
         - This keyword selects the Browser tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Browser Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Browser")

    def xiqse_analytics_select_application_flows_tab(self):
        """
         - This keyword selects the Application Flows tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Application Flows Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Application Flows")

    def xiqse_analytics_select_fingerprints_tab(self):
        """
         - This keyword selects the Fingerprints tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Fingerprints Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Fingerprints")

    def xiqse_analytics_select_packet_captures_tab(self):
        """
         - This keyword selects the Packet Captures tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Packet Captures Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Packet Captures")

    def xiqse_analytics_select_configuration_tab(self):
        """
         - This keyword selects the Configuration tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Configuration Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Configuration")

    def xiqse_analytics_select_reports_tab(self):
        """
         - This keyword selects the Reports tab of the Analytics page
         - Keyword Usage
          - ``XIQSE Analytics Select Reports Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_analytics_select_tab("Reports")
