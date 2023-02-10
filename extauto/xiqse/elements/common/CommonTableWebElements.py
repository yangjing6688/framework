from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.common.CommonTableWebElementsDefinitions import CommonTableWebElementsDefinitions


class CommonTableWebElements(CommonTableWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_table_column_header_menu(self):
        """
        :return: Table's column header menu
        """
        elements = self.weh.get_elements(self.table_column_header_menu)
        return self.weh.get_displayed_element(elements)

    def get_table_column_selection_menu(self):
        """
        :return: Columns Selection menu for the table's column header menu
        """
        return self.weh.get_element(self.table_column_selection_menu)

    def get_table_column_selection_menu_item(self, col_name):
        """
        :param col_name: name of the column to get the column selection menu for
        :return: Column Selection menu item for the table's column header menu
        """
        return self.weh.get_template_element(self.table_column_selection_menu_item, element_name=col_name)

    def get_table_sort_ascending_menu(self):
        """
        :return: "Sort Ascending" column menu option for the table
        """
        return self.weh.get_element(self.table_sort_ascending_menu)

    def get_table_sort_descending_menu(self):
        """
        :return: "Sort Descending" column menu option for the table
        """
        return self.weh.get_element(self.table_sort_descending_menu)

    def get_table_column_filters_toolbar_button(self):
        """
        :return: Toolbar button to access the Column Filters dialog
        """
        return self.weh.get_element(self.table_column_filters_toolbar_button)

    def get_table_refresh_button(self):
        """
        :return: Refresh button under the currently-displayed table
        """
        elements = self.weh.get_elements(self.table_refresh_button)
        return self.weh.get_displayed_element(elements)

    def get_table_reset_button(self):
        """
        :return: Reset button under the currently-displayed table
        """
        elements = self.weh.get_elements(self.table_reset_button)
        return self.weh.get_displayed_element(elements)
