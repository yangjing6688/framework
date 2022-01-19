from extauto.common.WebElementHandler import *
from xiqse.defs.network.NetworkWebElementsDefinitions import *


class NetworkWebElements(NetworkWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_dashboard_tab(self):
        """
        :return: Dashboard Tab on the Network page
        """
        return self.weh.get_element(self.dashboard_tab)

    def get_devices_tab(self):
        """
        :return: Devices Tab on the Network page
        """
        return self.weh.get_element(self.devices_tab)

    def get_discovered_tab(self):
        """
        :return: Discovered Tab on the Network page
        """
        return self.weh.get_element(self.discovered_tab)

    def get_firmware_tab(self):
        """
        :return: Firmware Tab on the Network page
        """
        return self.weh.get_element(self.firmware_tab)

    def get_archives_tab(self):
        """
        :return: Archives Tab on the Network page
        """
        return self.weh.get_element(self.archives_tab)

    def get_configuration_templates_tab(self):
        """
        :return: Configuration Templates Tab on the Network page
        """
        return self.weh.get_element(self.config_templates_tab)

    def get_reports_tab(self):
        """
        :return: Reports Tab on the Network page
        """
        return self.weh.get_element(self.reports_tab)
