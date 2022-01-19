from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.alarms_events.events.AlarmsEventsEventsWebElements import AlarmsEventsEventsWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_AlarmsEventsEvents(AlarmsEventsEventsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_table = XIQSE_CommonTable()

    def xiqse_events_select_time_range(self, value):
        """
         - This keyword selects the time range on the Alarms & Events> Events Tab
         - Keyword Usage
          - ``XIQSE Events Select Time Range    Custom``
          - ``XIQSE Events Select Time Range    All``
          - ``XIQSE Events Select Time Range    Today``
          - ``XIQSE Events Select Time Range    Yesterday``
          - ``XIQSE Events Select Time Range    Last 30 Minutes``
          - ``XIQSE Events Select Time Range    Last Hour``
          - ``XIQSE Events Select Time Range    Last 2 Hours``
          - ``XIQSE Events Select Time Range    Last 6 Hours``
          - ``XIQSE Events Select Time Range    Last 12 Hours``
          - ``XIQSE Events Select Time Range    Last 24 Hours``
          - ``XIQSE Events Select Time Range    Last 3 Days``
          - ``XIQSE Events Select Time Range    Last Week``
          - ``XIQSE Events Select Time Range    Last 2 Weeks``
          - ``XIQSE Events Select Time Range    Last 4 Weeks``

        :param value: item to select in the time range dropdown
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_time_range_dropdown()
        if the_field:
            self.utils.print_info("Opening the Time Range dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Time Range items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, value):
                    self.utils.print_info(f"Selected {value} in the Time Range dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {value} in the Time Range dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Time Range dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Time Range dropdown")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_events_select_type(self, values):
        """
         - This keyword selects the specified types on the Alarms & Events> Events Tab.
         - NOTE: to clear existing selections, first select "All"; otherwise, each call to this method will
         -       select the additional values in addition to the current selections.
         - Keyword Usage
          - ``XIQSE Events Select Type    All``
          - ``XIQSE Events Select Type    Console,Console View,Inventory``
          - ``XIQSE Events Select Type    Admin``

        :param values: comma-separated list of items to select in the Type dropdown
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_field = self.get_type_dropdown()
        if the_field:
            self.utils.print_info("Opening the Type dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_combo_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Type items count is {len(the_items)}")
                value_list = values.split(",")
                for value in value_list:
                    # The items have to be re-retrieved each time since selecting an item changes the elements and would
                    # otherwise lead to a StaleElementException
                    if self.auto_actions.select_drop_down_options(self.view_el.get_combo_dropdown_items(the_id), value):
                        self.utils.print_info(f"Selected type {value} in the Type dropdown")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Did not find {value} in the Type dropdown")
                    sleep(2)
                self.utils.print_info(f"Closing 'Type' dropdown")
                self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Type dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the 'Type' dropdown")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_events_open_search(self):
        """
         - This keyword opens the search box on the Alarms & Events> Events Tab
         - Keyword Usage
          - ``XIQSE Events Open Search``

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

    def xiqse_events_enter_search_text(self, value):
        """
         - This keyword enters text into the search field on the Alarms & Events> Events Tab
         - Keyword Usage
          - ``XIQSE Events Enter Search Text    My Event To Find``

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

    def xiqse_events_trigger_search(self):
        """
         - This keyword clicks the search button in the search box on the Alarms & Events> Events Tab to perform the search
         - Keyword Usage
          - ``XIQSE Events Trigger Search``

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

    def xiqse_events_clear_search(self):
        """
         - This keyword clicks the clear button in the search box on the Alarms & Events> Events Tab to perform the search
         - Keyword Usage
          - ``XIQSE Events Clear Search``

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

    def xiqse_events_wait_for_search_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the search to complete on the Alarms & Events> Events Tab
         - Keyword Usage
          - ``XIQSE Events Wait For Search To Complete``

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

    def xiqse_events_perform_search(self, value, retry_duration=10, retry_count=30):
        """
         - This keyword performs a search on the Alarms & Events> Events Tab
         - Keyword Usage
          - ``XIQSE Events Perform Search   My Search String``
          - ``XIQSE Events Perform Search   My Search String  retry_duration=5  retry_count=10``

        :param value:          string to search for
        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_events_open_search() == 1:
            if self.xiqse_events_enter_search_text(value) == 1:
                if self.xiqse_events_trigger_search() == 1:
                    if self.xiqse_events_wait_for_search_to_complete(retry_duration, retry_count) == 1:
                        ret_val = 1
                        self.utils.print_info(f"Completed search for {value}")

        if ret_val == -1:
            self.utils.print_info(f"Unable to perform search for {value}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_find_event_with_text(self, value):
        """
        - Searches for an event containing the specified value

        :param value: Value to search for in the event row
        :return: return 1 if event with specified value is found, else -1
        """
        ret_val = -1

        sleep(5)

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_table_rows()
                if rows:
                    for row in rows:
                        self.utils.print_info(f"Row data: {self.xiqse_table.format_table_row(row.text)}")
                        if value in row.text:
                            self.utils.print_info(f"Found event with value '{value}'")
                            ret_val = 1
                            break
                    if ret_val == -1:
                        self.utils.print_info(f"Did not find event with value '{value}'")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Could not obtain rows from Events table")
                    self.screen.save_screen_shot()

                # Break out of the Stale Element Exception loop
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return ret_val
