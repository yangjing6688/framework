from extauto.common.WebElementHandler import *
from xiqse.defs.analytics.configuration.AnalyticsConfigurationAddEngineWebElementsDefinitions import *


class AnalyticsConfigurationAddEngineWebElements(AnalyticsConfigurationAddEngineWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_engine_ip_field(self):
        """
        :return: Add Engine dialog input field for ip address
        """
        return self.weh.get_element(self.add_engine_ip_address_field)

    def get_engine_name_field(self):
        """
        :return: Add Engine dialog input field for engine name
        """
        return self.weh.get_element(self.add_engine_name_field)

    def get_engine_profile_dropdown(self):
        """
        :return: Add Engine dialog input field for snmp profile
        """
        return self.weh.get_element(self.add_engine_snmp_profile_dropdown)

    def get_add_engine_ok_button(self):
        """
        :return: Add Engine dialog OK button
        """
        return self.weh.get_element(self.add_engine_ok_button)
    
    def get_add_engine_cancel_button(self):
        """
        :return: Add Engine dialog Cancel button
        """
        return self.weh.get_element(self.add_engine_cancel_button)
