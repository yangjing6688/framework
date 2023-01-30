from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.alarms_events.alarms.AlarmsEventsAlarmsWebElementsDefinitions import AlarmsEventsAlarmsWebElementsDefinitions


class AlarmsEventsAlarmsWebElements(AlarmsEventsAlarmsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_search_open_button(self):
        """
        :return: Button to open the Search panel on the Alarms & Events> Alarms page
        """
        return self.weh.get_element(self.search_open_button)

    def get_search_text_field(self):
        """
        :return: Search field on the Alarms & Events> Alarms page
        """
        return self.weh.get_element(self.search_text_field)

    def get_search_trigger_button(self):
        """
        :return: Button to perform the Search on the Alarms & Events> Alarms page
        """
        return self.weh.get_element(self.search_trigger_button)

    def get_search_clear_button(self):
        """
        :return: Button to clear the Search field on the Alarms & Events> Alarms page
        """
        return self.weh.get_element(self.search_clear_button)

    def get_alarms_table(self):
        """
        :return: The Alarms table
        """
        return self.weh.get_element(self.alarms_table)

    def get_table_rows(self):
        """
        :return: All the rows in the Alarms table
        """
        return self.weh.get_elements(self.alarms_table_rows)
