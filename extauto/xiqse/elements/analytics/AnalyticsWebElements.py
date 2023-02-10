from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.analytics.AnalyticsWebElementsDefinitions import AnalyticsWebElementsDefinitions


class AnalyticsWebElements(AnalyticsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_dashboard_tab(self):
        """
        :return: Dashboard Tab on the Analytics page
        """
        return self.weh.get_element(self.dashboard_tab)

    def get_browser_tab(self):
        """
        :return: Browser Tab on the Analytics page
        """
        return self.weh.get_element(self.browser_tab)

    def get_application_flows_tab(self):
        """
        :return: Application Flows Tab on the Analytics page
        """
        return self.weh.get_element(self.application_flows_tab)

    def get_fingerprints_tab(self):
        """
        :return: Fingerprints Tab on the Analytics page
        """
        return self.weh.get_element(self.fingerprints_tab)

    def get_packet_captures_tab(self):
        """
        :return: Packet Captures Tab on the Analytics page
        """
        return self.weh.get_element(self.packet_captures_tab)

    def get_configuration_tab(self):
        """
        :return: Configuration Tab on the Analytics page
        """
        return self.weh.get_element(self.configuration_tab)

    def get_reports_tab(self):
        """
        :return: Reports Tab on the Analytics page
        """
        return self.weh.get_element(self.reports_tab)
