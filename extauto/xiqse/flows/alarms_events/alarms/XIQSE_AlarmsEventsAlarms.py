from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.alarms_events.alarms.AlarmsEventsAlarmsWebElements import AlarmsEventsAlarmsWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable


class XIQSE_AlarmsEventsAlarms(AlarmsEventsAlarmsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_table = XIQSE_CommonTable()

    def xiqse_alarms_open_search(self):
        """
         - This keyword opens the search box on the Alarms & Events> Alarms Tab
         - Keyword Usage
          - ``XIQSE Alarms Open Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_btn = self.get_search_open_button()
        search_text = self.get_search_text_field()
        if search_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "true":
                self.utils.print_info(f"Clicking Search button")
                self.auto_actions.click(search_btn)
                sleep(2)
            else:
                self.utils.print_info(f"Search field already open")
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Search button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_alarms_enter_search_text(self, value):
        """
         - This keyword enters text into the search field on the Alarms & Events> Alarms Tab
         - Keyword Usage
          - ``XIQSE Alarms Enter Search Text    My Alarm To Find``

        :param value: string to enter in the search box
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_text = self.get_search_text_field()
        if search_text:
            if search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Entering {value} into search box")
                self.auto_actions.send_keys(search_text, value)
                ret_val = 1
            else:
                self.utils.print_info("Search text field is currently hidden")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Search text field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_alarms_trigger_search(self):
        """
         - This keyword clicks the search button in the search box on the Alarms & Events> Alarms Tab to perform the search
         - Keyword Usage
          - ``XIQSE Alarms Trigger Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_btn = self.get_search_trigger_button()
        search_text = self.get_search_text_field()
        if search_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Clicking Search button to perform the search")
                self.auto_actions.click(search_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Search field not open")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Search button to perform the search")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_alarms_clear_search(self):
        """
         - This keyword clicks the clear button in the search box on the Alarms & Events> Alarms Tab to perform the search
         - Keyword Usage
          - ``XIQSE Alarms Clear Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        clear_btn = self.get_search_clear_button()
        search_text = self.get_search_text_field()
        if clear_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Clicking Clear button")
                self.auto_actions.click(clear_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Search field not open")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Clear button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_alarms_wait_for_search_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the search to complete on the Alarms & Events> Alarms Tab
         - Keyword Usage
          - ``XIQSE Alarms Wait For Search To Complete``

        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for search to complete: loop {count}")
            load_mask = self.view_el.get_load_mask()
            if load_mask:
                self.utils.print_info(f"Search still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Search has completed")
                return 1
            count += 1

        self.utils.print_info("Search did not complete within specified time")
        self.screen.save_screen_shot()
        return -1

    def xiqse_alarms_perform_search(self, value, retry_duration=10, retry_count=30):
        """
         - This keyword performs a search on the Alarms & Events> Alarms Tab
         - Keyword Usage
          - ``XIQSE Alarms Perform Search   My Search String``
          - ``XIQSE Alarms Perform Search   My Search String  retry_duration=5  retry_count=10``

        :param value:          string to search for
        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_alarms_open_search() == 1:
            if self.xiqse_alarms_enter_search_text(value) == 1:
                if self.xiqse_alarms_trigger_search() == 1:
                    if self.xiqse_alarms_wait_for_search_to_complete(retry_duration, retry_count) == 1:
                        ret_val = 1
                        self.utils.print_info(f"Completed search for {value}")

        if ret_val == -1:
            self.utils.print_info(f"Unable to perform search for {value}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_alarm_with_text(self, value):
        """
        - Searches for an alarm containing the specified value

        :param value: Value to search for in the alarm row
        :return: return 1 if alarm with specified value is found, else -1
        """
        ret_val = -1

        sleep(5)
        rows = self.get_table_rows()
        if rows:
            for row in rows:
                self.utils.print_info(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                if value in row.text:
                    self.utils.print_info(f"Found alarm with value '{value}'")
                    ret_val = 1
                    break
            if ret_val == -1:
                self.utils.print_info(f"Did not find alarm with value '{value}'")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not obtain rows from Alarms table")
            self.screen.save_screen_shot()

        return ret_val
