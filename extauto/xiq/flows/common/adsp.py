import re
import extauto.common.CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.AdspWebElements import AdspWebElements


class Adsp(AdspWebElements):
    def __init__(self):
        super().__init__()
        self.driver = extauto.common.CloudDriver.cloud_driver
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()

    def get_adsp_alarm_details(self, search_string):
        """
        - Get Alarm details based on search string
        - Flow: Manage--> Alarms
        - Keyword Usage:
         - ``Get Alarm Details   ${DEVICE_MAC}``
         - ``Get Alarm Details   ${DEVICE_NAME}``
         - ``Get Alarm Details   ${ALARM_CATEGORY}``

        :param search_string: str to search the alarm in grid ex: it may be severity, host name, Device mac, category
        :return:(dict) Alarm Details in dictionary Format
        """
        alarm_details = {}
        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()

        self.utils.switch_to_iframe(self.driver)
        sleep(5)

        self.utils.print_info("Click More Insights button")
        self.auto_actions.click(self.get_adsp_more_insights_button())
        sleep(2)

        self.utils.print_info("Switch to New ADSP Tab")
        self.driver.switch_to.window(self.driver.window_handles[1])

        if row := self.get_adsp_alarm_grid_row(search_string):
            cells = self.get_adsp_alarms_grid_row_cells(row)
            for cell in cells:
                if re.search(r'cdk-column-\w*', cell.get_attribute("class")):
                    label = re.search(r'cdk-column-\w*', cell.get_attribute("class")).group().split("cdk-column-")[-1]
                    alarm_details[label] = cell.text
            self.utils.print_info(alarm_details)
            return alarm_details

    def get_adsp_alarm_grid_row(self, search_string):
        """
        - Get the Adsp Alarm row from the grid row based on the search string
        - Assumes that already navigated to the Manage--> Alarms page

        :param search_string: str to search the alarm in grid ex: it may be severity, host name, Device mac, category
        :return:Alarm row information if row present with Search String
        """
        for row in self.get_adsp_alarm_grid_rows():
            if search_string in row.text:
                return row


