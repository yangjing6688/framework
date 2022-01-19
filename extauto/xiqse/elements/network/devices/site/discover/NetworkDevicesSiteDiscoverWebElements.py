from common.WebElementHandler import *
from xiqse.defs.network.devices.site.discover.NetworkDevicesSiteDiscoverWebElementsDefinitions import *


class NetworkDevicesSiteDiscoverWebElements(NetworkDevicesSiteDiscoverWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_address_add_button(self):
        """
        :return: Add button for the Addresses panel on the Network> Devices> Site> Discover page
        """
        return self.weh.get_element(self.address_add_button)

    def get_address_edit_button(self):
        """
        :return: Edit button for the Addresses panel on the Network> Devices> Site> Discover page
        """
        return self.weh.get_element(self.address_edit_button)

    def get_address_delete_button(self):
        """
        :return: Delete button for the Addresses panel on the Network> Devices> Site> Discover page
        """
        return self.weh.get_element(self.address_delete_button)

    def get_addresses_table_rows(self):
        """
        :return: All the rows in the Addresses table
        """
        return self.weh.get_elements(self.addresses_table_rows)

    def get_profiles_table_rows(self):
        """
        :return: All the rows in the Profiles table
        """
        return self.weh.get_elements(self.profiles_table_rows)

    def get_profile_selected_accept_check_buttons(self):
        """
        :return: All of the selected 'Accept' check buttons in the Profiles table
        """
        return self.weh.get_elements(self.profiles_table_selected_accept_check_buttons)

    def get_profile_selected_reject_check_buttons(self):
        """
        :return: All of the selected 'Reject' check buttons in the Profiles table
        """
        return self.weh.get_elements(self.profiles_table_selected_reject_check_buttons)

    def get_profile_accept_cell(self, row):
        """
        :param row: profile row to return the value of
        :return: 'Accept' cell in the Profiles table
        """
        return self.weh.get_element(self.profiles_table_accept_cell, row)

    def get_profile_accept_cell_checked(self, row):
        """
        :param row: profile row to return the value of
        :return: True if 'Accept' cell in the Profiles table for the specified row is checked
        """
        el = self.weh.get_element(self.profiles_table_accept_cell_checked, row)
        if el:
            return True
        else:
            return False

    def get_profile_reject_cell(self, row):
        """
        :param row: profile row to return the value of
        :return: 'Reject' cell in the Profiles table
        """
        return self.weh.get_element(self.profiles_table_reject_cell, row)

    def get_profile_reject_cell_checked(self, row):
        """
        :param row: profile row to return the value of
        :return: True if 'Reject' cell in the Profiles table for the specified row is checked
        """
        el = self.weh.get_element(self.profiles_table_reject_cell_checked, row)
        if el:
            return True
        else:
            return False
