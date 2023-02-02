from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.alarms_events.event_config.AlarmsEventsEventConfigWebElementsDefinitions import AlarmsEventsEventConfigWebElementsDefinitions


class AlarmsEventsEventConfigWebElements(AlarmsEventsEventConfigWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_event_logs_tab(self):
        """
        :return: Event Logs Sub Tab on the Alarms & Events> Event Configuration page
        """
        return self.weh.get_element(self.event_logs_tab)

    def get_event_patterns_tab(self):
        """
        :return: Event Patterns Sub Tab on the Alarms & Events> Event Configuration page
        """
        return self.weh.get_element(self.event_patterns_tab)
