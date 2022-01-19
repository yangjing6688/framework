from extauto.common.WebElementHandler import *
from xiqse.defs.wireless.threats.WirelessThreatsWebElementsDefinitions import *


class WirelessThreatsWebElements(WirelessThreatsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_threats_tab(self):
        """
        :return: Threats Sub Tab on the Wireless> Threats page
        """
        return self.weh.get_element(self.threats_tab)

    def get_threat_events_tab(self):
        """
        :return: Threat Events Sub Tab on the Wireless> Threats page
        """
        return self.weh.get_element(self.threat_events_tab)

    def get_interference_tab(self):
        """
        :return: Interference Sub Tab on the Wireless> Threats page
        """
        return self.weh.get_element(self.interference_tab)

    def get_interference_events_tab(self):
        """
        :return: Interference Events Sub Tab on the Wireless> Threats page
        """
        return self.weh.get_element(self.interference_events_tab)
