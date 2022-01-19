from extauto.common.WebElementHandler import *
from xiqse.defs.network.discovered.NetworkDiscoveredWebElementsDefinitions import *
import re


class NetworkDiscoveredWebElements(NetworkDiscoveredWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_discovered_table(self):
        """
        :return: The Discovered table
        """
        return self.weh.get_element(self.discovered_table)

    def get_displaying_rows_label(self):
        """
        :return: The "Displaying # rows" label for the Discovered table
        """
        return self.weh.get_element(self.displaying_rows_label)

    def get_table_rows(self):
        """
        :return: All the rows in the Discovered table
        """
        return self.weh.get_elements(self.discovered_table_rows)

    def get_discovered_ip_column_header(self):
        """
        :return: 'IP Address' column header of the Discovered table
        """
        return self.weh.get_element(self.discovered_table_ip_column_header)

    def get_discovered_serial_number_column_header(self):
        """
        :return: "Serial Number' column header of the Discovered table
        """
        return self.weh.get_element(self.discovered_table_serial_number_column_header)

    def get_show_in_groups_menu(self):
        """
        :return: "Show in Groups" column menu on the Network> Discovered page
        """
        return self.weh.get_element(self.show_in_groups_menu)

    def get_group_by_menu(self):
        """
        :return: "Group by This Field" column menu on the Network> Discovered page
        """
        return self.weh.get_element(self.group_by_menu)

    def get_clear_button(self):
        """
        :return: Clear button on the toolbar
        """
        return self.weh.get_element(self.clear_button)

    def get_clear_all_button(self):
        """
        :return: Clear All Devices button on the toolbar
        """
        return self.weh.get_element(self.clear_all_button)

    def get_pre_register_button(self):
        """
        :return: Pre-Register Device button on the toolbar
        """
        return self.weh.get_element(self.pre_register_button)

    def get_load_configuration_button(self):
        """
        :return: Load Configuration button on the toolbar
        """
        return self.weh.get_element(self.load_config_button)

    def get_add_devices_button(self):
        """
        :return: Add Devices button on the toolbar
        """
        return self.weh.get_element(self.add_devices_button)

    def get_configure_devices_button(self):
        """
        :return: Configure Devices button on the toolbar
        """
        return self.weh.get_element(self.configure_devices_button)

    def get_configure_devices_menu(self):
        """
        :return: Configure Devices menu item
        """
        return self.weh.get_element(self.configure_devices_menu)

    def get_discovered_column_by_name(self, col_name):
        """
        :param col_name: name of the column to return the web element of
        :return: Web Element for the specified column name in the Discovered table, else -1
        """
        return self.weh.get_template_element(self.discovered_column_by_name, element_name=col_name)

    def get_discovered_column_value(self, col_id, row):
        """
        :param col_id: ID of the column to return the value of
        :param row:    row to return the value for
        :return: Column value for the specified column id of the specified row in the Discovered table
        """
        return self.weh.get_template_element(self.discovered_column_value, parent=row, element_id=col_id)
