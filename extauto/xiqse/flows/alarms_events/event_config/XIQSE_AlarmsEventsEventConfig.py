from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.alarms_events.event_config.AlarmsEventsEventConfigWebElements import AlarmsEventsEventConfigWebElements


class XIQSE_AlarmsEventsEventConfig(AlarmsEventsEventConfigWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_event_configuration_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Alarms & Events> Event Configuration page
        - Keyword Usage
        - ``XIQSE Event Configuration Select Tab    Event Logs``
        - ``XIQSE Event Configuration Select Tab    Event Patterns``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Event Logs":
            the_tab = self.get_event_logs_tab()
        elif tab_name == "Event Patterns":
            the_tab = self.get_event_patterns_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Alarms & Events> Event Configuration page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Alarms & Events> Event Configuration page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_event_configuration_select_event_logs_tab(self):
        """
        - This keyword selects the Event Logs tab on the Alarms & Events> Event Configuration Tab
        - Keyword Usage
        - ``XIQSE Event Configuration Select Event Logs Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_event_configuration_select_tab("Event Logs")

    def xiqse_event_configuration_select_event_patterns_tab(self):
        """
        - This keyword selects the Event Patterns tab on the Alarms & Events> Event Configuration Tab
        - Keyword Usage
        - ``XIQSE Event Configuration Select Event Patterns Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_event_configuration_select_tab("Event Patterns")
