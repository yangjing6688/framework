from extauto.common.WebElementHandler import *
from xiqse.defs.analytics.configuration.AnalyticsConfigurationEnforceEngineWebElementsDefinitions import *


class AnalyticsConfigurationEnforceEngineWebElements(AnalyticsConfigurationEnforceEngineWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_enforce_engine_yes_button(self):
        """
        :return: Enforce Engine dialog Yes button
        """
        return self.weh.get_element(self.enforce_engine_yes_button)
    
    def get_enforce_engine_no_button(self):
        """
        :return: Enforce Engine dialog No button
        """
        return self.weh.get_element(self.enforce_engine_no_button)

    def get_enforce_engine_error_dialog(self):
        """
        :return: Gets the dialog for 'Enforce Engine Error'
        """
        return self.weh.get_element(self.enforce_engine_error_dialog)

    def get_enforce_engine_error_dialog_ok_button(self):
        """
        :return: Gets the OK button for the Enforce Engine Error dialog
        """
        return self.weh.get_element(self.enforce_engine_error_dialog_ok_button)
