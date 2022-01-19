from xiq.defs.MLInsightsDefinitions import *
from extauto.common.WebElementHandler import *


class MLInsightsWebElements(MLInsightsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_ml_insights_button(self):
        return self.weh.get_element(self.ml_insights_button)

    def get_n360_plan_button(self):
        return self.weh.get_element(self.n360_plan_button)

    def get_n360_monitor_button(self):
        return self.weh.get_element(self.n360_monitor_button)

    def get_n360_scorecard_button(self):
        return self.weh.get_element(self.n360_scorecard_button)

    def get_n360_client_360_button(self):
        return self.weh.get_element(self.n360_client_360_button)

    def get_n360_comparative_analytics(self):
        return self.weh.get_element(self.n360_comparative_analytics)

    def get_n360_proximity_and_presence(self):
        return self.weh.get_element(self.n360_proximity_and_presence)
