from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.alarms_events.AlarmsEventsWebElements import AlarmsEventsWebElements


class XIQSE_AlarmsEvents(AlarmsEventsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_alarmsevents_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Alarms & Events page
         - Keyword Usage
          - ``XIQSE AlarmsEvents Select Tab    Alarms``
          - ``XIQSE AlarmsEvents Select Tab    Alarm Configuration``
          - ``XIQSE AlarmsEvents Select Tab    Events``
          - ``XIQSE AlarmsEvents Select Tab    Event Configuration``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Alarms":
            the_tab = self.get_alarms_tab()
        elif tab_name == "Alarm Configuration":
            the_tab = self.get_alarm_configuration_tab()
        elif tab_name == "Events":
            the_tab = self.get_events_tab()
        elif tab_name == "Event Configuration":
            the_tab = self.get_event_configuration_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Alarms & Events page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Alarms & Events")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_alarmsevents_select_alarms_tab(self):
        """
         - This keyword selects the Alarms tab of the Alarms & Events page
         - Keyword Usage
          - ``XIQSE AlarmsEvents Select Alarms Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_alarmsevents_select_tab("Alarms")

    def xiqse_alarmsevents_select_alarm_configuration_tab(self):
        """
         - This keyword selects the Alarm Configuration tab of the Alarms & Events page
         - Keyword Usage
          - ``XIQSE AlarmsEvents Select Alarm Configuration Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_alarmsevents_select_tab("Alarm Configuration")

    def xiqse_alarmsevents_select_events_tab(self):
        """
         - This keyword selects the Events tab of the Alarms & Events page
         - Keyword Usage
          - ``XIQSE AlarmsEvents Select Events Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_alarmsevents_select_tab("Events")

    def xiqse_alarmsevents_select_event_configuration_tab(self):
        """
         - This keyword selects the Event Configuration tab of the Alarms & Events page
         - Keyword Usage
          - ``XIQSE AlarmsEvents Select Event Configuration Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_alarmsevents_select_tab("Event Configuration")
