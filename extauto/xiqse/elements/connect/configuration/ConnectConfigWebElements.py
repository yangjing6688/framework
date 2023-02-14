from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.connect.configuration.ConnectConfigWebElementsDefinitions import ConnectConfigWebElementsDefinitions


class ConnectConfigWebElements(ConnectConfigWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_services_tab(self):
        """
        :return: Services Sub Tab on the Connect> Configuration page
        """
        return self.weh.get_element(self.services_tab)

    def get_options_tab(self):
        """
        :return: Options Sub Tab on the Connect> Configuration page
        """
        return self.weh.get_element(self.options_tab)
