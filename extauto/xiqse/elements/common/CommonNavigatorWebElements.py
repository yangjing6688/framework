from common.WebElementHandler import *
from xiqse.defs.common.CommonNavigatorWebElementsDefinitions import *


class CommonNavigatorWebElements(CommonNavigatorWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_network_tab(self):
        """
        :return: Network Tab navigation button
        """
        return self.weh.get_element(self.network_tab)

    def get_alarms_and_events_tab(self):
        """
        :return: Alarms & Events Tab navigation button
        """
        return self.weh.get_element(self.alarms_and_events_tab)

    def get_control_tab(self):
        """
        :return: Control Tab navigation button
        """
        return self.weh.get_element(self.control_tab)

    def get_analytics_tab(self):
        """
        :return: Analytics Tab navigation button
        """
        return self.weh.get_element(self.analytics_tab)

    def get_wireless_tab(self):
        """
        :return: Wireless Tab navigation button
        """
        return self.weh.get_element(self.wireless_tab)

    def get_compliance_tab(self):
        """
        :return: Compliance Tab navigation button
        """
        return self.weh.get_element(self.compliance_tab)

    def get_reports_tab(self):
        """
        :return: Reports Tab navigation button
        """
        return self.weh.get_element(self.reports_tab)

    def get_tasks_tab(self):
        """
        :return: Tasks Tab navigation button
        """
        return self.weh.get_element(self.tasks_tab)

    def get_administration_tab(self):
        """
        :return: Administration Tab navigation button
        """
        return self.weh.get_element(self.admin_tab)

    def get_connect_tab(self):
        """
        :return: Connect Tab navigation button
        """
        return self.weh.get_element(self.connect_tab)
