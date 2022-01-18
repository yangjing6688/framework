from common.WebElementHandler import *
from xiqse.defs.analytics.flows.AnalyticsApplicationFlowsWebElementsDefinitions import *


class AnalyticsApplicationFlowsWebElements(AnalyticsApplicationFlowsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_search_open_button(self):
        """
        :return: Button to open the Search panel on the Application Flows page
        """
        return self.weh.get_element(self.search_open_button)

    def get_search_text_field(self):
        """
        :return: Search field on the Application flows page
        """
        return self.weh.get_element(self.search_text_field)

    def get_search_trigger_button(self):
        """
        :return: Button to perform the Search on the Application flows page
        """
        return self.weh.get_element(self.search_trigger_button)

    def get_search_clear_button(self):
        """
        :return: Button to clear the Search field on the Application flows page
        """
        return self.weh.get_element(self.search_clear_button)

    def get_application_flows_table(self):
        """
        :return: The Application Flows table
        """
        return self.weh.get_element(self.application_flows_table)

    def get_table_rows(self):
        """
        :return: All the rows in the Application Flows table
        """
        return self.weh.get_elements(self.application_flows_table_rows)
