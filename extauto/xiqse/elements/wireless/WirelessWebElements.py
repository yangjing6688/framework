from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.wireless.WirelessWebElementsDefinitions import WirelessWebElementsDefinitions


class WirelessWebElements(WirelessWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_dashboard_tab(self):
        """
        :return: Dashboard Tab on the Wireless page
        """
        return self.weh.get_element(self.dashboard_tab)

    def get_network_tab(self):
        """
        :return: Network Tab on the Wireless page
        """
        return self.weh.get_element(self.network_tab)

    def get_controllers_tab(self):
        """
        :return: Controllers Tab on the Wireless page
        """
        return self.weh.get_element(self.controllers_tab)

    def get_access_points_tab(self):
        """
        :return: Access Points Tab on the Wireless page
        """
        return self.weh.get_element(self.access_points_tab)

    def get_clients_tab(self):
        """
        :return: Clients Tab on the Wireless page
        """
        return self.weh.get_element(self.clients_tab)

    def get_threats_tab(self):
        """
        :return: Threats Tab on the Wireless page
        """
        return self.weh.get_element(self.threats_tab)

    def get_reports_tab(self):
        """
        :return: Reports Tab on the Wireless page
        """
        return self.weh.get_element(self.reports_tab)
