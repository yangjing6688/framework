from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonTableWebElements import CommonTableWebElements
from xiqse.flows.common.XIQSE_CommonColumnFilters import XIQSE_CommonColumnFilters
from xiqse.flows.common.XIQSE_CommonView import XIQSE_CommonView
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_CommonTable(CommonTableWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.the_view = XIQSE_CommonView()
        self.column_filters_dialog = XIQSE_CommonColumnFilters()

    def xiqse_table_open_column_header_menu(self, anchor_col):
        """
        - This keyword opens the column header menu using the anchor column specified.
        -  Keyword Usage:
         - ``XIQSE Table Open Column Header Menu        Status``

        :param anchor_col: column to access the menu from; different depending on which view the table is in
        :return: returns 1 if successful. else -1
        """
        ret_val = 1

        if anchor_col:
            self.utils.print_info("Moving to anchor column header")
            self.auto_actions.move_to_element(anchor_col)
        else:
            self.utils.print_info("Could not find anchor column")
            self.screen.save_screen_shot()
            return -1

        self.utils.print_debug("Getting Column Header Menu")
        header_menu = self.get_table_column_header_menu()
        if header_menu:
            self.utils.print_info("Clicking on Column Header Menu")
            self.auto_actions.click(header_menu)
        else:
            self.utils.print_info("Could not find column header menu")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_table_open_column_selection_menu(self, anchor_col):
        """
        - This keyword opens the column selection menu from the column header using the anchor column specified.
        -  Keyword Usage:
         - ``XIQSE Table Open Column Selection Menu        Status``

        :param anchor_col: column to access the column menu from; different depending on which view the table is in
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        if self.xiqse_table_open_column_header_menu(anchor_col) == 1:
            self.utils.print_debug("Getting Column Selection Menu")
            columns_menu = self.get_table_column_selection_menu()
            if columns_menu:
                self.utils.print_info("Clicking on Column Selection Menu")
                self.auto_actions.click(columns_menu)
                ret_val = 1
            else:
                self.utils.print_info("Could not find column selection menu")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_show_columns(self, anchor_col, *columns):
        """
        - This keyword shows the specified list of columns if they are currently hidden.
        -  Keyword Usage:
         - ``XIQSE Table Show Columns        Status      Admin Profile  Context``

        :param anchor_col: column to access the column menu from; different depending on which view the table is in
        :param columns: list of columns to show
        :return: returns 1 if successful. else -1
        """

        ret_val = self.xiqse_table_open_column_selection_menu(anchor_col)
        if ret_val == 1:
            sleep(2)
            self.utils.print_info(f"Columns to show: {columns}")
            for col_name in columns:
                self.utils.print_debug(f"Getting Column Selection Menu Item for {col_name}")
                col_menu_item = self.get_table_column_selection_menu_item(col_name)
                if col_menu_item:
                    if col_menu_item.get_attribute("aria-checked") == "true":
                        self.utils.print_info(f"Column {col_name} is already being shown")
                    else:
                        self.utils.print_info(f"Selecting check box for column {col_name}")
                        self.auto_actions.click(col_menu_item)
                else:
                    self.utils.print_info(f"Unable to get menu item for column {col_name}")
                    ret_val = -1
        else:
            self.utils.print_info("Unable to open column selection menu, so unable to show columns")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_hide_columns(self, anchor_col, *columns):
        """
        - This keyword hides the specified list of columns if they are currently hidden.
        -  Keyword Usage:
         - ``XIQSE Table Hide Columns        Status      Admin Profile  Context``

        :param anchor_col: column to access the column menu from; different depending on which view the table is in
        :param columns: list of columns to hide
        :return: returns 1 if successful. else -1
        """

        ret_val = self.xiqse_table_open_column_selection_menu(anchor_col)
        if ret_val == 1:
            sleep(2)
            self.utils.print_info(f"Columns to show: {columns}")
            for col_name in columns:
                self.utils.print_debug(f"Getting Column Selection Menu Item for {col_name}")
                col_menu_item = self.get_table_column_selection_menu_item(col_name)
                if col_menu_item:
                    if col_menu_item.get_attribute("aria-checked") == "true":
                        self.utils.print_info(f"Deselecting check box for column {col_name}")
                        self.auto_actions.click(col_menu_item)
                    else:
                        self.utils.print_info(f"Column {col_name} is already hidden")
                else:
                    self.utils.print_info(f"Unable to get menu item for column {col_name}")
                    ret_val = -1
        else:
            self.utils.print_info("Unable to open column selection menu, so unable to show columns")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_sort_ascending(self, anchor_col):
        """
         - This keyword selects the Sort Ascending menu option for the column.
         - Provide the Web Element for the specified column.
         - Keyword Usage
          - ``XIQSE Table Sort Ascending  Serial Number``

        :param anchor_col: column web element to access the column menu from; different depending on which view the table is in
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_table_open_column_header_menu(anchor_col) == 1:
            column_menu = self.get_table_sort_ascending_menu()
            if column_menu:
                self.utils.print_info(f"Clicking the 'Sort Ascending' menu option.")
                self.auto_actions.click(column_menu)
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find the 'Sort Ascending' menu option.")
        else:
            self.utils.print_info(f"Could not find the {anchor_col} column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_sort_descending(self, anchor_col):
        """
         - This keyword selects the Sort Descending menu option for the column.
         - Provide the Web Element for the specified column.
         - Keyword Usage
          - ``XIQSE Table Sort Descending  Serial Number``

        :param anchor_col: column web element to access the column menu from; different depending on which view the table is in
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_table_open_column_header_menu(anchor_col) == 1:
            column_menu = self.get_table_sort_descending_menu()
            if column_menu:
                self.utils.print_info(f"Clicking the 'Sort Descending' menu option.")
                self.auto_actions.click(column_menu)
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find the 'Sort Descending' menu option.")
        else:
            self.utils.print_info(f"Could not find the {anchor_col} column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_set_column_filter(self, column_name, filter_value, filter_type="Text"):
        """
        - This keyword sets the specified filter on the specified column using the Column Filters dialog.
        - If the filter type is not a text field, the type should be specified (e.g., Radio, Checkbox).
        - Note that this keyword opens the Column Filters dialog, adds the single filter, and closes the dialog.
        - If multiple filters are desired during the same session, the dialog should be opened, the keyword
        - xiqse_table_add_column_filter() should be called for as many filters as needed, and then the dialog
        - should be closed.
        -  Keyword Usage:
         - ``XIQSE Table Set Column Filter     Source          ${DEVICE_IP}``
         - ``XIQSE Table Set Column Filter     Admin Profile   EXTR_v2_Profile   filter_type=Text``
         - ``XIQSE Table Set Column Filter     Archived        True              filter_type=Radio``
         - ``XIQSE Table Set Column Filter     Severity        Critical,Error    filter_type=Checkbox``

        :param column_name: name of the column to add a filter on
        :param filter_value: value to enter for the filter field
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        # Open the Column Filters dialog
        if self.xiqse_table_open_column_filters_dialog() == 1:
            # Add the specified filter
            ret_val = self.xiqse_table_add_column_filter(column_name, filter_value, filter_type)

            # Close the Column Filters dialog
            if self.xiqse_table_close_column_filters_dialog() == -1:
                # We don't want to overwrite the ret_val if closing the dialog was successful, in case adding
                # the filter was not successful. So check the close return value and set it to failure if the
                # close failed (in other words, we don't want to set the ret_val to success if the close works
                # but the add filter failed).
                self.utils.print_info("Unable to close Column Filters dialog")
                ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_add_column_filter(self, column_name, filter_value, filter_type="Text"):
        """
        - This keyword adds the specified filter on the specified column using the Column Filters dialog.
        - If the filter type is not a text field, the type should be specified (e.g., Radio, Checkbox).
        - This keyword assumes the dialog is already open, and can be used to add multiple filters.
        - Use xiqse_table_set_column_filter() to open, add one filter, and close the dialog in one shot.
        -  Keyword Usage:
         - ``XIQSE Table Add Column Filter     Source          ${DEVICE_IP}``
         - ``XIQSE Table Add Column Filter     Admin Profile   EXTR_v2_Profile   filter_type=Text``
         - ``XIQSE Table Add Column Filter     Archived        True              filter_type=Radio``
         - ``XIQSE Table Add Column Filter     Severity        Critical,Error    filter_type=Checkbox``

        :param column_name: name of the column to add a filter on
        :param filter_value: value to enter for the filter field
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        if filter_type.lower() == "text":
            self.utils.print_info("Handling a text type filter case")
            ret_val = self.column_filters_dialog.xiqse_column_filters_dialog_add_text_filter(column_name, filter_value)
        elif filter_type.lower() == "radio":
            self.utils.print_info("Handling a radio button type filter case")
            ret_val = self.column_filters_dialog.xiqse_column_filters_dialog_add_radio_filter(column_name, filter_value)
        elif filter_type.lower() == "checkbox":
            self.utils.print_info("Handling a checkbox type filter case")
            ret_val = self.column_filters_dialog.xiqse_column_filters_dialog_add_checkbox_filter(column_name, filter_value)
        else:
            self.utils.print_info(f"Unhandled filter type {filter_type}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_remove_column_filter(self, the_value):
        """
        - This keyword removes the specified filter from the Column Filters dialog.
        -  Keyword Usage:
         - ``XIQSE Table Remove Column Filter     Source``

        :param the_value: name of the filter to remove
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        # Open the Column Filters dialog
        if self.xiqse_table_open_column_filters_dialog() == 1:
            # Remove the specified filter
            ret_val = self.column_filters_dialog.xiqse_column_filters_dialog_remove_filter(the_value)

            # Close the Column Filters dialog
            if self.xiqse_table_close_column_filters_dialog() == -1:
                # We don't want to overwrite the ret_val if closing the dialog was successful, in case removing
                # the filter was not successful. So check the close return value and set it to failure if the
                # close failed (in other words, we don't want to set the ret_val to success if the close works
                # but the remove filter failed).
                self.utils.print_info("Unable to close Column Filters dialog")
                ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_remove_column_filters(self, the_values):
        """
        - This keyword removes the specified filters from the Column Filters dialog.
        -  Keyword Usage:
         - ``XIQSE Table Remove Column Filter     Source,Event Type,Client``

        :param the_values: list of filters to remove
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        # Open the Column Filters dialog
        if self.xiqse_table_open_column_filters_dialog() == 1:
            # Remove the specified filters
            value_list = the_values.split(",")
            for val in value_list:
                ret_val = 1
                if self.column_filters_dialog.xiqse_column_filters_dialog_remove_filter(val) != 1:
                    # if any of the values could not be removed, fail the keyword
                    self.utils.print_info(f"Unable to remove filter {val}")
                    self.screen.save_screen_shot()
                    ret_val = -1

            # Close the Column Filters dialog
            if self.xiqse_table_close_column_filters_dialog() == -1:
                # We don't want to overwrite the ret_val if closing the dialog was successful, in case removing
                # the filter was not successful. So check the close return value and set it to failure if the
                # close failed (in other words, we don't want to set the ret_val to success if the close works
                # but the remove filter failed).
                self.utils.print_info("Unable to close Column Filters dialog")
                ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_open_column_filters_dialog(self):
        """
         - This keyword clicks the toolbar button to open the Column Filters dialog.
         - Keyword Usage
          - ``XIQSE Table Close Column Filters Dialog``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_btn = self.get_table_column_filters_toolbar_button()
        if the_btn:
            self.utils.print_info("Clicking toolbar button to open Column Filters dialog")
            self.auto_actions.click(the_btn)
            sleep(5)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find toolbar button to open Column Filters dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_table_close_column_filters_dialog(self):
        """
         - This keyword clicks the toolbar button to open the Column Filters dialog.
         - Keyword Usage
          - ``XIQSE Table Close Column Filters Dialog``

        :return: 1 if action was successful, else -1
        """
        return self.column_filters_dialog.xiqse_column_filters_dialog_click_close()

    def xiqse_refresh_table(self):
        """
         - This keyword clicks the refresh icon under the table.
         - Keyword Usage
          - ``XIQSE Refresh Table``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_btn = self.get_table_refresh_button()
        if the_btn:
            self.utils.print_info("Clicking Refresh button")
            self.auto_actions.click(the_btn)
            ret_val = self.the_view.xiqse_wait_for_refresh_to_complete()
        else:
            self.utils.print_info("Unable to find Refresh button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_reset_table(self):
        """
         - This keyword clicks the Reset icon under the table, which clears the search field, filters, and refreshes
         - the table.
         - Keyword Usage
          - ``XIQSE Reset Table``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_btn = self.get_table_reset_button()
        if the_btn:
            self.utils.print_info("Clicking Reset button")
            self.auto_actions.click(the_btn)
            ret_val = self.the_view.xiqse_wait_for_refresh_to_complete()
        else:
            self.utils.print_info("Unable to find Reset button")
            self.screen.save_screen_shot()

        return ret_val

    def format_table_row(self, row):
        cell_values = row.split("\n")
        formatted_row = list()
        for cell_value in cell_values:
            formatted_row.append(cell_value)
        return formatted_row
