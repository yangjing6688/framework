import re
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.AlarmsWebElements import AlarmsWebElements


class Alarms(AlarmsWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()

    def _get_alarm_grid_row(self, search_string):
        """
        - Get the Alarm row from the grid row based on the search string
        :param search_string:
        :return:row information which matches search string row
        """
        for row in self.get_alarms_grid_rows():
            if search_string in row.text:
                return row

    def clear_alarm(self, search_string):
        """
        - Flow: Manage--> Alarms
        - Clear the generated alarms based on the search string
        - Keyword Usage:
         - ``Clear Alarm   ${DEVICE_MAC}``

        :param search_string: str to search the alarm in grid ex: it may be severity, host name, Device mac, category
        :return: 1 if alarm Cleared Successfully else -1
        """
        _tool_tip = ""
        self.navigator.navigate_to_manage_alarms()

        if row := self._get_alarm_grid_row(search_string):
            self.auto_actions.click(self.get_alarm_grid_row_check_box(row))
            sleep(2)
            self.auto_actions.click(self.get_alarm_clear_button())
            sleep(2)
            self.auto_actions.click(self.get_alarm_clear_confirm_yes_button())
            sleep(2)
            _tool_tip = self.get_alarm_clear_tool_tip().text

        if "Last alarms cleared" in _tool_tip:
            self.utils.print_info(f"{_tool_tip}")
            return 1
        else:
            self.utils.print_info(f"Alarm Row Not Cleared Successfully with Search string {search_string}")
            return -1

    def get_alarms_count_from_status_card(self, alarm_type='critical'):
        """
        - Flow: Manage--> Alarms
        - Get the alarms count from the status bar , based on alarms type
        - Keyword Usage:
         - ``Get Alarms Count From Status Card    ${ALARM_TYPE}``

        :param alarm_type: it will be critical, minor, major
        :return: Total alarm Count
        """
        self.navigator.navigate_to_manage_alarms()
        self.screen.save_screen_shot()
        sleep(2)

        alarm_type_count = {'critical': self.get_critical_alarm_count_status_bar,
                            'minor': self.get_minor_alarm_count_status_bar,
                            'major': self.get_major_alarm_count_status_bar
                            }
        count = alarm_type_count[alarm_type]().text
        self.utils.print_info(f"Alarms {alarm_type} count: {count}")
        return count

    def get_alarm_details(self, search_string):
        """
        - Flow: Manage--> Alarms
        - Get Alarm details based on search string
        - Keyword Usage:
         - ``Get Alarm Details   ${DEVICE_MAC}``

        :param search_string: str to search the alarm in grid ex: it may be severity, host name, Device mac, category
        :return: Alarm details in a dictionary
        """
        alarm_details = {}
        self.navigator.navigate_to_manage_alarms()

        self.auto_actions.click(self.get_alarms_grid_refresh_button())
        sleep(2)

        if row := self._get_alarm_grid_row(search_string):
            cells = self.get_alarms_grid_row_cells(row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    alarm_details[label] = cell.text
            self.utils.print_info(alarm_details)
            return alarm_details
