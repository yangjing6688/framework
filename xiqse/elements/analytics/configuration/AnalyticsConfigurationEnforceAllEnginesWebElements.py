from common.WebElementHandler import *
from xiqse.defs.analytics.configuration.AnalyticsConfigurationEnforceAllEnginesWebElementsDefinitions import *


class AnalyticsConfigurationEnforceAllEnginesWebElements(AnalyticsConfigurationEnforceAllEnginesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_enforce_all_engines_yes_button(self):
        """
        :return: Enforce Engines dialog Yes button
        """
        return self.weh.get_element(self.enforce_all_engines_yes_button)

    def get_enforce_all_engines_no_button(self):
        """
        :return: Enforce Engines dialog No button
        """
        return self.weh.get_element(self.enforce_all_engines_no_button)

    def get_enforce_engines_error_dialog(self):
        """
        :return: Gets the dialog for 'Enforce Engines Error'
        """
        return self.weh.get_element(self.enforce_engines_error_dialog)

    def get_enforce_engines_error_dialog_ok_button(self):
        """
        :return: Gets the OK button for the 'Enforce Engines Error' dialog
        """
        return self.weh.get_element(self.enforce_engines_error_dialog_ok_button)
