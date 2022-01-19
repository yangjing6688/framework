from extauto.common.WebElementHandler import *
from xiqse.defs.analytics.configuration.AnalyticsConfigurationRestartCollectorWebElementsDefinitions import *


class AnalyticsConfigurationRestartCollectorWebElements(AnalyticsConfigurationRestartCollectorWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_restart_collector_yes_button(self):
        """
        :return: Restart Collector dialog Yes button
        """
        return self.weh.get_element(self.restart_collector_yes_button)
    
    def get_restart_collector_no_button(self):
        """
        :return: Restart Collector dialog No button
        """
        return self.weh.get_element(self.restart_collector_no_button)

    def get_restart_collector_error_dialog(self):
        """
        :return: Gets the dialog for 'Restart Collector Error'
        """
        return self.weh.get_element(self.restart_collector_error_dialog)

    def get_restart_collector_error_dialog_ok_button(self):
        """
        :return: Gets the OK button for the 'Restart Collector Error' dialog
        """
        return self.weh.get_element(self.restart_collector_error_dialog_ok_button)

