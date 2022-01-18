from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.common.CommonColumnFiltersWebElements import CommonColumnFiltersWebElements


class XIQSE_CommonColumnFilters(CommonColumnFiltersWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()

    def xiqse_column_filters_dialog_add_filter(self, the_value):
        """
         - This keyword adds the specified filter to the Column Filters dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Column Filters Dialog Add Filter    IP Address``

        :param the_value:   name of the filter to add
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # This dropdown is not opened by clicking on the input area, so need to get the dropdown trigger arrow
        the_field_trigger = self.get_column_filters_dialog_add_filter_dropdown_trigger()
        if the_field_trigger:
            self.utils.print_info("Opening Add Filter dropdown")
            self.auto_actions.click(the_field_trigger)

            # Obtain the dropdown items
            the_field = self.get_column_filters_dialog_add_filter_dropdown()
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected '{the_value}' in the Add Filter dropdown")
                    filter_panel = self.get_column_filters_dialog_filter_panel(the_value)
                    if filter_panel:
                        self.utils.print_info(f"Filter for '{the_value}' was added")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find '{the_value}' in the Add Filter dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field_trigger)
            else:
                self.utils.print_info("Unable to get the Add Filter dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field_trigger)
        else:
            self.utils.print_info("Could not find Add Filter field in the Column Filters dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_column_filters_dialog_add_text_filter(self, column_name, filter_value):
        """
         - This keyword adds a text-type filter to the Column Filters dialog.  A "text-type" filter is one which
         - results in a text box to enter the filter value, as opposed to check buttons or radio buttons.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Column Filters Dialog Add Text Filter    IP Address    1.2.3.4``

        :param column_name:   name of the column to add the filter on
        :param filter_value:  value to enter for the filter field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # First, add the filter for the specified column
        if self.xiqse_column_filters_dialog_add_filter(column_name):
            # Next, populate the text field with the specified filter value
            the_field = self.get_column_filters_dialog_filter_text_field(column_name)
            if the_field:
                self.utils.print_info(f"Entering '{filter_value}' for the {column_name} filter")
                self.auto_actions.send_keys(the_field, filter_value)
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find text field for {column_name} filter")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info(f"Unable to add a filter for {column_name}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_column_filters_dialog_add_radio_filter(self, column_name, filter_value):
        """
         - This keyword adds a radio button type filter to the Column Filters dialog.  A "radio button type" filter
         - is one which results in radio buttons to select the value, like Yes/No for the Archived column of the
         - Devices table, as opposed to checkboxes or a text field.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Column Filters Dialog Add Radio Filter    Archived    Yes``

        :param column_name:   name of the column to add the filter on
        :param filter_value:  value of the radio button to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # First, add the filter for the specified column
        if self.xiqse_column_filters_dialog_add_filter(column_name):
            # Next, select the appropriate radio button
            the_field = self.get_column_filters_dialog_filter_radio_field(column_name, filter_value)
            if the_field:
                self.utils.print_info(f"Selecting radio button '{filter_value}' for the {column_name} filter")
                self.auto_actions.select_radio_button(the_field)
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find radio button {filter_value} for {column_name} filter")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info(f"Unable to add a filter for {column_name}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_column_filters_dialog_add_checkbox_filter(self, column_name, filter_values):
        """
         - This keyword adds a checkbox type filter to the Column Filters dialog.  A "checkbox type" filter
         - is one which results in checkboxes to select the values, like for the Status column of the Devices
         - table, as opposed to radio buttons or a text field.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Column Filters Dialog Add Checkbox Filter    Status    Critical Alarms,Device Down,Error Alarms``

        :param column_name:    name of the column to add the filter on
        :param filter_values:  comma-separated list of values to select
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        # First, add the filter for the specified column
        if self.xiqse_column_filters_dialog_add_filter(column_name):
            # Next, select the appropriate checkboxes
            value_list = filter_values.split(",")
            if len(value_list) == 0:
                self.utils.print_info("No values sent to filter on")
                ret_val = -1
            else:
                for value in value_list:
                    the_field = self.get_column_filters_dialog_filter_radio_field(column_name, value)
                    if the_field:
                        self.utils.print_info(f"Selecting checkbox '{value}' for the {column_name} filter")
                        self.auto_actions.enable_check_box(the_field)
                    else:
                        self.utils.print_info(f"Did not find radio button {value} for {column_name} filter")
                        self.screen.save_screen_shot()
                        ret_val = -1
        else:
            self.utils.print_info(f"Unable to add a filter for {column_name}")
            ret_val = -1

        return ret_val

    def xiqse_column_filters_dialog_remove_filter(self, the_value):
        """
         - This keyword removes the specified filter from the Column Filters dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Column Filters Dialog Remove Filter    IP Address``

        :param the_value:   name of the filter to remove
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        remove_btn = self.get_column_filters_dialog_remove_filter_button(the_value)
        if remove_btn:
            self.utils.print_info(f"Clicking the Remove Filter button for {the_value}")
            self.auto_actions.click(remove_btn)
            filter_panel = self.get_column_filters_dialog_filter_panel(the_value)
            if not filter_panel:
                self.utils.print_info(f"Filter for '{the_value}' was removed")
            ret_val = 1
        else:
            self.utils.print_info("Could not find Remove Filter button in the Column Filters dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_column_filters_dialog_click_close(self):
        """
         - This keyword clicks Close in the Column Filters dialog.
         - It is assumed the dialog is already opened.
         - Keyword Usage
          - ``XIQSE Column Filters Dialog Click Close``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        close_btn = self.get_column_filters_dialog_close_button()
        if close_btn:
            self.utils.print_info("Clicking Close button")
            self.auto_actions.click(close_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Close button in Column Filters dialog")
            self.screen.save_screen_shot()

        return ret_val
