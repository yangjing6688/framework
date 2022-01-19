from extauto.common.WebElementHandler import *
from xiqse.defs.alarms_events.AlarmsEventsWebElementsDefinitions import *


class AlarmsEventsWebElements(AlarmsEventsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_alarms_tab(self):
        """
        :return: Alarms Tab on the Alarms & Events page
        """
        return self.weh.get_element(self.alarms_tab)

    def get_alarm_configuration_tab(self):
        """
        :return: Alarm Configuration Tab on the Alarms & Events page
        """
        return self.weh.get_element(self.alarm_config_tab)

    def get_events_tab(self):
        """
        :return: Events Tab on the Alarms & Events page
        """
        return self.weh.get_element(self.events_tab)

    def get_event_configuration_tab(self):
        """
        :return: Event Configuration Tab on the Alarms & Events page
        """
        return self.weh.get_element(self.event_config_tab)
