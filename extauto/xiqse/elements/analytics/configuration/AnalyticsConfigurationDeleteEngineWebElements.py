from common.WebElementHandler import *
from xiqse.defs.analytics.configuration.AnalyticsConfigurationDeleteEngineWebElementsDefinitions import *


class AnalyticsConfigurationDeleteEngineWebElements(AnalyticsConfigurationDeleteEngineWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_delete_engine_yes_button(self):
        """
        :return: Delete Engine dialog Yes button
        """
        return self.weh.get_element(self.delete_engine_yes_button)
    
    def get_delete_engine_no_button(self):
        """
        :return: Delete Engine dialog No button
        """
        return self.weh.get_element(self.delete_engine_no_button)
