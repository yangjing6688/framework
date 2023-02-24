from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.connect.ConnectWebElementsDefinitions import ConnectWebElementsDefinitions


class ConnectWebElements(ConnectWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_configuration_tab(self):
        """
        :return: Configuration Tab on the Connect page
        """
        return self.weh.get_element(self.configuration_tab)

    def get_diagnostics_tab(self):
        """
        :return: Diagnostics Tab on the Connect page
        """
        return self.weh.get_element(self.diagnostics_tab)

    def get_services_api_tab(self):
        """
        :return: Services API Tab on the Connect page
        """
        return self.weh.get_element(self.services_api_tab)
