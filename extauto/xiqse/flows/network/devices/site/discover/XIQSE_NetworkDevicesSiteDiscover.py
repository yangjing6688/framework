from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.site.discover.NetworkDevicesSiteDiscoverWebElements import NetworkDevicesSiteDiscoverWebElements
from xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscoverAddAddress import XIQSE_NetworkDevicesSiteDiscoverAddAddress
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable


class XIQSE_NetworkDevicesSiteDiscover(NetworkDevicesSiteDiscoverWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.add_address_dlg = XIQSE_NetworkDevicesSiteDiscoverAddAddress()

    def xiqse_discover_click_add_address_button(self):
        """
        - This keyword clicks the Add button in the Addresses panel on the Network> Devices> Site> Discover Tab
        - It is assumed the view is already navigated to the Discover tab.
        - Keyword Usage
        - ``XIQSE Discover Click Add Address Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_address_add_button()
        if the_button:
            self.utils.print_info("Clicking Add Address Button")
            self.auto_actions.click(the_button)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to find the Add Address button")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_discover_addresses_add_subnet(self, subnet_mask):
        """
        - This keyword adds the specified subnet address on the Network> Devices> Site> Discover Tab.
        - It is assumed the view is currently navigated to the Discover tab.
        - Keyword Usage
        - ``XIQSE Discover Addresses Add Subnet   1.2.3.4/24`

        :param subnet_mask: subnet/mask value to enter
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_address_add_button()
        if add_btn:
            self.utils.print_info("Clicking Add Address button")
            self.auto_actions.click(add_btn)

            # Select Discover Type
            ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_select_type("Subnet")

            # Enter Subnet/Mask value
            if ret_val != -1:
                ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_set_subnet_mask(subnet_mask)

            # Click OK if input was valid
            if ret_val == 1:
                sleep(2)  # Give the OK button time to become enabled
                ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_click_ok()
        else:
            self.utils.print_info("Unable to find 'Add' button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_add_seed_address(self, seed_address):
        """
        - This keyword adds the specified seed address on the Network> Devices> Site> Discover Tab.
        - It is assumed the view is currently navigated to the Discover tab.
        - Keyword Usage
        - ``XIQSE Discover Addresses Add Seed Address   1.2.3.4`

        :param seed_address: seed address to enter
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_address_add_button()
        if add_btn:
            self.utils.print_info("Clicking Add Address button")
            self.auto_actions.click(add_btn)

            # Select Discover Type
            ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_select_type("Seed Address")

            # Enter Seed Address value
            if ret_val != -1:
                ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_set_seed_address(seed_address)

            # Click OK if input was valid
            if ret_val == 1:
                sleep(2)  # Give the OK button time to become enabled
                ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_click_ok()

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_add_address_range(self, start_address, end_address):
        """
        - This keyword adds the specified address range on the Network> Devices> Site> Discover Tab.
        - It is assumed the view is currently navigated to the Discover tab.
        - Keyword Usage
        - ``XIQSE Discover Add Address Range   1.2.3.1    1.2.3.255`

        :param start_address: value to enter for the starting IP address range
        :param end_address: value to enter for the ending IP address range
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        add_btn = self.get_address_add_button()
        if add_btn:
            self.utils.print_info("Clicking Add Address button")
            self.auto_actions.click(add_btn)

            # Select Discover Type
            ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_select_type("Address Range")

            # Enter Start Address and End Address values
            if ret_val != -1:
                ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_set_address_range(start_address, end_address)

            # Click OK if input was valid
            if ret_val == 1:
                sleep(2)    # Give the OK button time to become enabled
                ret_val = self.add_address_dlg.xiqse_discover_add_address_dialog_click_ok()

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_select_subnet(self, subnet_mask):
        """
        - This keyword selects the specified subnet address in the Addresses panel.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Addresses Select Subnet    1.2.3.1/24``

        :param subnet_mask: value of the subnet/mask to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_info(f"Selecting Subnet {subnet_mask}")
        rows = self.get_addresses_table_rows()
        if rows:
            for row in rows:
                if "Subnet" in row.text and subnet_mask in row.text:
                    self.utils.print_debug(f"Found subnet {subnet_mask} in row {self.xiqse_table.format_table_row(row.text)}")
                    row_selected = row.get_attribute("aria-selected")
                    if row_selected and row_selected == "true":
                        self.utils.print_info(f"Row for Subnet {subnet_mask} is already selected")
                    else:
                        self.utils.print_info(f"Selecting Subnet {subnet_mask}")
                        self.auto_actions.click(row)
                    ret_val = 1
                    break
        else:
            self.utils.print_info("No rows are present")

        if ret_val == -1:
            self.utils.print_info(f"Unable to select subnet address {subnet_mask}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_select_seed_address(self, seed_address):
        """
        - This keyword selects the specified seed address in the Addresses panel.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Addresses Select Seed Address    1.2.3.4``

        :param seed_address: value of the seed address to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_info(f"Selecting Seed Address {seed_address}")
        rows = self.get_addresses_table_rows()
        if rows:
            for row in rows:
                if "Seed Address" in row.text and seed_address in row.text:
                    self.utils.print_debug(f"Found seed address {seed_address} in row {self.xiqse_table.format_table_row(row.text)}")
                    row_selected = row.get_attribute("aria-selected")
                    if row_selected and row_selected == "true":
                        self.utils.print_info(f"Row for Seed Address {seed_address} is already selected")
                    else:
                        self.utils.print_info(f"Selecting Seed Address {seed_address}")
                        self.auto_actions.click(row)
                    ret_val = 1
                    break
        else:
            self.utils.print_info("No rows are present")

        if ret_val == -1:
            self.utils.print_info(f"Unable to select seed address {seed_address}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_select_address_range(self, start_address, end_address):
        """
        - This keyword selects the specified address range in the Addresses panel.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Addresses Select Address Range    1.2.3.4    1.2.3.5``

        :param start_address: value of the starting IP address range to select
        :param end_address: value of the ending IP address range to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        addr_range = start_address + " - " + end_address
        self.utils.print_info(f"Selecting Address Range {addr_range}")
        rows = self.get_addresses_table_rows()
        if rows:
            for row in rows:
                if "Address Range" in row.text and addr_range in row.text:
                    self.utils.print_debug(f"Found address range {addr_range} in row {self.xiqse_table.format_table_row(row.text)}")
                    row_selected = row.get_attribute("aria-selected")
                    if row_selected and row_selected == "true":
                        self.utils.print_info(f"Row for Address Range {addr_range} is already selected")
                    else:
                        self.utils.print_info(f"Selecting Address Range {addr_range}")
                        self.auto_actions.click(row)
                    ret_val = 1
                    break
        else:
            self.utils.print_info("No rows are present")

        if ret_val == -1:
            self.utils.print_info(f"Unable to select address range {addr_range}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_delete_subnet(self, subnet_mask):
        """
        - This keyword selects the specified subnet/mask in the Addresses panel and clicks the Delete toolbar button.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Addresses Delete Seed Address    1.2.3.4``

        :param subnet_mask: value of the subnet/mask to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_discover_addresses_select_subnet(subnet_mask):
            ret_val = self.xiqse_discover_delete_selected_address()
        else:
            self.utils.print_info("Unable to select the subnet to delete")

        if ret_val == -1:
            self.utils.print_info(f"Unable to delete subnet {subnet_mask}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_delete_seed_address(self, seed_address):
        """
        - This keyword selects the specified seed address in the Addresses panel and clicks the Delete toolbar button.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Addresses Delete Seed Address    1.2.3.4``

        :param seed_address: value of the seed address to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_discover_addresses_select_seed_address(seed_address):
            ret_val = self.xiqse_discover_delete_selected_address()
        else:
            self.utils.print_info("Unable to select the seed address to delete")

        if ret_val == -1:
            self.utils.print_info(f"Unable to delete seed address {seed_address}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_addresses_delete_address_range(self, start_address, end_address):
        """
        - This keyword selects the specified address range in the Addresses panel and clicks the Delete toolbar button.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Addresses Delete Address Range    1.2.3.4    1.2.3.5``

        :param start_address: value of the starting IP address range to delete
        :param end_address: value of the ending IP address range to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_discover_addresses_select_address_range(start_address, end_address):
            ret_val = self.xiqse_discover_delete_selected_address()
        else:
            self.utils.print_info("Unable to select the address range to delete")

        if ret_val == -1:
            self.utils.print_info(f"Unable to delete address range {start_address} - {end_address}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_delete_selected_address(self):
        """
        - This keyword deletes the currently-selected address in the Addresses panel.
        - It is assumed the Site> Discover tab is visible and the address entry to delete is selected.
        - Keyword Usage
        - ``XIQSE Discover Delete Selected Address``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        delete_btn = self.get_address_delete_button()
        if delete_btn:
            self.utils.print_info("Clicking the 'Delete' toolbar button")
            self.auto_actions.click(delete_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the 'Delete' toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_clear_all_profile_selections(self):
        """
        - This keyword clears the selected state of the Accept and Reject columns for all profiles in the Profiles panel.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Clear All Profile Selections``
        """
        accept_cbs = self.get_profile_selected_accept_check_buttons()
        if accept_cbs:
            self.utils.print_info("Deselect all selected Accept check buttons")
            for cb in accept_cbs:
                self.utils.print_info("  deselecting...")
                self.auto_actions.click(cb)
        else:
            self.utils.print_info("There were no selected Accept check buttons")

        reject_cbs = self.get_profile_selected_reject_check_buttons()
        if reject_cbs:
            self.utils.print_info("Deselect all selected Reject check buttons")
            for cb in reject_cbs:
                self.utils.print_info("  deselecting...")
                self.auto_actions.click(cb)
        else:
            self.utils.print_info("There were no selected Reject check buttons")

    def xiqse_discover_set_accept_profile(self, profile_name, accept_val="true"):
        """
        - This keyword sets the selected state of the Accept column for the specified profile in the Profiles panel.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Set Accept Profile  public_v1_Profile  true``
        - ``XIQSE Discover Set Accept Profile  public_v2_Profile  false``

        :param profile_name: name of the profile to mark
        :param accept_val: indicates whether to select or deselect the Accept check box
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        rows = self.get_profiles_table_rows()
        if rows:
            for row in rows:
                if profile_name in row.text:
                    self.utils.print_info(f"Found profile {profile_name} in row {self.xiqse_table.format_table_row(row.text)}")
                    accept_cell = self.get_profile_accept_cell(row)
                    if accept_cell:
                        accept_checked = self.get_profile_accept_cell_checked(row)
                        if accept_val == "true":
                            if accept_checked:
                                self.utils.print_info(f"Accept checkbox already selected for profile {profile_name}")
                            else:
                                self.utils.print_info(f"Selecting Accept checkbox for profile {profile_name}")
                                self.auto_actions.click(accept_cell)
                        else:
                            if accept_checked:
                                self.utils.print_info(f"Deselecting Accept checkbox for profile {profile_name}")
                                self.auto_actions.click(accept_cell)
                            else:
                                self.utils.print_info(f"Accept checkbox already deselected for profile {profile_name}")

                        ret_val = 1
                    else:
                        self.utils.print_info(f"Unable to find Accept checkbox for profile {profile_name}")
                    break
        else:
            self.utils.print_info("No rows in the Profiles table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discover_set_reject_profile(self, profile_name, reject_val="true"):
        """
        - This keyword checks the Reject column for the specified profile in the Profiles panel.
        - It is assumed the Site> Discover tab is visible.
        - Keyword Usage
        - ``XIQSE Discover Set Reject Profile  public_v1_Profile  true``
        - ``XIQSE Discover Set Reject Profile  public_v2_Profile  false``

        :param profile_name: name of the profile to mark
        :param reject_val: indicates whether to select or deselect the Reject check box
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        rows = self.get_profiles_table_rows()
        if rows:
            for row in rows:
                if profile_name in row.text:
                    self.utils.print_info(f"Found profile {profile_name} in row {self.xiqse_table.format_table_row(row.text)}")
                    reject_cell = self.get_profile_reject_cell(row)
                    if reject_cell:
                        reject_checked = self.get_profile_reject_cell_checked(row)
                        if reject_val == "true":
                            if reject_checked:
                                self.utils.print_info(f"Reject checkbox already selected for profile {profile_name}")
                            else:
                                self.utils.print_info(f"Selecting Reject checkbox for profile {profile_name}")
                                self.auto_actions.click(reject_cell)
                        else:
                            if reject_checked:
                                self.utils.print_info(f"Deselecting Reject checkbox for profile {profile_name}")
                                self.auto_actions.click(reject_cell)
                            else:
                                self.utils.print_info(f"Reject checkbox already deselected for profile {profile_name}")

                        ret_val = 1
                    else:
                        self.utils.print_info(f"Unable to find Reject checkbox for profile {profile_name}")
                    break
        else:
            self.utils.print_info("No rows in the Profiles table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
