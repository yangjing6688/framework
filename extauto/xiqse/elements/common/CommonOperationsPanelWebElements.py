from common.WebElementHandler import *
from xiqse.defs.common.CommonOperationsPanelWebElementsDefinitions import *


class CommonOperationsPanelWebElements(CommonOperationsPanelWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_operations_button(self):
        """
        :return: Gets the Operations button
        """
        return self.weh.get_element(self.operations_button)

    def get_operations_table_group_rows(self):
        """
        :return: Gets the group table rows in the Operations panel
        """
        return self.weh.get_elements(self.operations_table_group_rows)

    def get_operations_table_group_data_rows(self):
        """
        :return: Gets the table rows for the expanded group(s) in the Operations panel
        """
        return self.weh.get_elements(self.operations_table_group_data_rows)

    def get_operations_table_group_row(self, value):
        """
        :param value:  Name of the group to get the table row for
        :return: Gets the specified group table row in the Operations panel
        """
        return self.weh.get_template_element(self.operations_table_group_row, element_id=value)

    def get_operations_table_group_data_row(self, value):
        """
        :param value:  Name of the data to get the table row for
        :return: Gets the specified table row for the expanded group in the Operations panel
        """
        return self.weh.get_template_element(self.operations_table_group_data_row, element_id=value)

    def get_operations_table_data_row_progress(self, row):
        """
        :param row: row to return the information for
        :return: Returns the progress value for the specified row
        """
        el = self.weh.get_element(self.operations_table_data_row_progress, row)
        if el:
            return el.text
        else:
            return None

    def get_operations_table_data_row_cells(self, row):
        """
        :param row: row to return the information for
        :return: Returns the progress value for the specified row
        """
        return self.weh.get_elements(self.operations_table_data_row_cells, row)

    def get_clear_all_menu(self):
        """
        :return: Clear All menu when right clicking on a row
        """
        elements = self.weh.get_elements(self.clear_all_menu)
        return self.weh.get_displayed_element(elements)
