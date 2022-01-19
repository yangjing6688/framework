from extauto.common.WebElementHandler import *
from xiqse.defs.network.devices.NetworkDevicesWebElementsDefinitions import *


class NetworkDevicesWebElements(NetworkDevicesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_devices_tab(self):
        """
        :return: Devices Sub Tab on the Network> Devices page
        """
        return self.weh.get_element(self.devices_tab)

    def get_site_tab(self, site="World"):
        """
        :param site: optional name of the site tab;  default is "World"
        :return: Site Sub Tab on the Network> Devices page
        """
        return self.weh.get_template_element(self.site_tab, element_name=site)

    def get_site_summary_tab(self):
        """
        :return: Site Summary Sub Tab on the Network> Devices page
        """
        return self.weh.get_element(self.site_summary_tab)

    def get_endpoint_locations_tab(self):
        """
        :return: Endpoint Locations Sub Tab on the Network> Devices page
        """
        return self.weh.get_element(self.endpoint_locations_tab)

    def get_flexreports_tab(self):
        """
        :return: FlexReports Sub Tab on the Network> Devices page
        """
        return self.weh.get_element(self.flexreports_tab)
