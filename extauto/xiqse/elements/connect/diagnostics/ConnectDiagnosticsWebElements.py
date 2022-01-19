from common.WebElementHandler import *
from xiqse.defs.connect.diagnostics.ConnectDiagnosticsWebElementsDefinitions import *


class ConnectDiagnosticsWebElements(ConnectDiagnosticsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_iframe_attr(self):
        """
        :return: String  Attribute to identify the iframe on the Connect> Diagnostics page
        """
        return 'contains(@src, "diagnostics")'

    def get_end_systems_tab(self):
        """
        :return: End-Systems Sub Tab on the Connect> Diagnostics page
        """
        return self.weh.get_element(self.end_systems_tab)

    def get_end_system_groups_tab(self):
        """
        :return: End-System Groups Sub Tab on the Connect> Diagnostics page
        """
        return self.weh.get_element(self.end_system_groups_tab)

    def get_statistics_tab(self):
        """
        :return: Statistics Sub Tab on the Connect> Diagnostics page
        """
        return self.weh.get_element(self.statistics_tab)

