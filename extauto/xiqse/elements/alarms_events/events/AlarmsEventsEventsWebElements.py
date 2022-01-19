from common.WebElementHandler import *
from xiqse.defs.alarms_events.events.AlarmsEventsEventsWebElementsDefinitions import *


class AlarmsEventsEventsWebElements(AlarmsEventsEventsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_time_range_dropdown(self):
        """
        :return: Time Range dropdown on the Alarms & Events> Events page
        """
        return self.weh.get_element(self.time_range_dropdown)

    def get_type_dropdown(self):
        """
        :return: Type dropdown on the Alarms & Events> Events page
        """
        return self.weh.get_element(self.type_dropdown)

    def get_search_open_button(self):
        """
        :return: Button to open the Search panel on the Alarms & Events> Events page
        """
        return self.weh.get_element(self.search_open_button)

    def get_search_text_field(self):
        """
        :return: Search field on the Alarms & Events> Events page
        """
        return self.weh.get_element(self.search_text_field)

    def get_search_trigger_button(self):
        """
        :return: Button to perform the Search on the Alarms & Events> Events page
        """
        return self.weh.get_element(self.search_trigger_button)

    def get_search_clear_button(self):
        """
        :return: Button to clear the Search field on the Alarms & Events> Events page
        """
        return self.weh.get_element(self.search_clear_button)

    def get_events_table(self):
        """
        :return: The Events table
        """
        return self.weh.get_element(self.events_table)

    def get_table_rows(self):
        """
        :return: All the rows in the Events table
        """
        return self.weh.get_elements(self.events_table_rows)
