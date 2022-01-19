from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.flows.network.discovered.XIQSE_NetworkDiscoveredAddDevices import XIQSE_NetworkDiscoveredAddDevices
from xiqse.elements.network.discovered.NetworkDiscoveredWebElements import NetworkDiscoveredWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements


class XIQSE_NetworkDiscovered(NetworkDiscoveredWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.add_devices_dlg = XIQSE_NetworkDiscoveredAddDevices()
        self.xiqse_table = XIQSE_CommonTable()
        self.view_el = CommonViewWebElements()

    def xiqse_discovered_do_not_show_in_groups(self):
        """
         - This keyword deselects the "Show in Groups" checkbox on the column menu on the Network> Discovered tab.
         - Keyword Usage
          - ``XIQSE Discovered Do Not Show In Groups``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        ip_col = self.get_discovered_ip_column_header()
        if ip_col:
            if self.xiqse_table.xiqse_table_open_column_header_menu(ip_col) == 1:
                menu_el = self.get_show_in_groups_menu()
                if menu_el:
                    if menu_el.get_attribute("aria-checked") == "true":
                        self.utils.print_info("Deselecting 'Show in Groups' option'")
                        self.auto_actions.click(menu_el)
                    else:
                        self.utils.print_info("'Show in Groups' option is already deselected")
                    ret_val = 1
                else:
                    self.utils.print_info("Did not find 'Show in Groups' Menu")
        else:
            self.utils.print_info("Did not find IP Address column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_sort_ascending(self, column_name):
        """
         - This keyword selects the Sort Ascending menu option for the provided column name.
         - Keyword Usage
          - ``XIQSE Discovered Sort Ascending  Status``

        :param column_name: column name to sort ascending
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        column_el = self.get_discovered_column_by_name(column_name)
        if column_el:
            if self.xiqse_table.xiqse_table_sort_ascending(column_el) == 1:
                self.utils.print_info(f"{column_name} column: Clicking the 'Sort Ascending' menu option.")
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find the 'Sort Ascending' menu option.")
        else:
            self.utils.print_info(f"Did not find the {column_name} column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_sort_descending(self, column_name):
        """
         - This keyword selects the Sort Descending menu option for the provided column name.
         - Keyword Usage
          - ``XIQSE Discovered Sort Descending  Status``

        :param column_name: column name to sort descending
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        column_el = self.get_discovered_column_by_name(column_name)
        if column_el:
            if self.xiqse_table.xiqse_table_sort_descending(column_el) == 1:
                self.utils.print_info(f"{column_name} column: Clicking the 'Sort Descending' menu option.")
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find the 'Sort Descending' menu option.")
        else:
            self.utils.print_info(f"Did not find the {column_name} column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_add_columns(self, column_name, *columns):
        """
         - This keyword selects the Columns menu option for the provided column name and enables the provided columns
         - Keyword Usage
          - ``XIQSE Discovered Add Columns  Status  Connector``

        :param column_name: column name to access
        :param columns: List of columns to display
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        column_el = self.get_discovered_column_by_name(column_name)
        if column_el:
            if self.xiqse_table.xiqse_table_show_columns(column_el, *columns) == 1:
                self.utils.print_info(f"{column_name} column: Clicking the 'Columns' menu option.")
                ret_val = 1
            else:
                self.utils.print_info(f"Did not find the 'Columns' menu option.")
        else:
            self.utils.print_info(f"Did not find the {column_name} column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_select_row_by_ip(self, ip):
        """
         - This keyword selects the specified IP in the Network> Discovered table.
         - Keyword Usage
          - ``XIQSE Discovered Select Row By IP    1.2.3.4``

        :param ip:  IP address to select in the table
        :return:    1 if action was successful, else -1
        """
        ret_val = -1
        self.utils.print_info(f"Selecting row with IP {ip}")
        row = self.xiqse_discovered_get_row_by_ip(ip)
        if row:
            row_selected = row.get_attribute("aria-selected")
            if row_selected and row_selected == "true":
                self.utils.print_info(f"Row for IP {ip} is already selected")
            else:
                self.utils.print_info(f"Selecting row with IP {ip}")
                self.auto_actions.click(row)
            ret_val = 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to select row with IP {ip}")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_discovered_select_rows_by_ips(self, ip_list):
        """
         - This keyword selects the specified IPs in the Network> Discovered table.
         - Keyword Usage
          - ``XIQSE Discovered Select Rows By IPs    1.1.1.1,2.2.2.2,3.3.3.3``

        :param ip_list:  comma-separated list of IP addresses to select in the table
        :return:    1 if action was successful, else -1
        """
        ret_val = -1

        sel_count = 0
        # Select the rows with the specified IP addresses
        ip_items = ip_list.split(",")
        ip_count = len(ip_items)
        for ip in ip_items:
            row = self.xiqse_discovered_get_row_by_ip(ip)
            if row:
                row_selected = row.get_attribute("aria-selected")
                if row_selected and row_selected == "true":
                    self.utils.print_info(f"Row for IP {ip} is already selected")
                else:
                    self.utils.print_info(f"Selecting row with IP {ip}")
                    self.auto_actions.shift_click(row)
                sel_count = sel_count + 1
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find row with IP {ip}")

        if sel_count != ip_count:
            self.utils.print_info("Unable to select all rows")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_find_row_with_ip(self, ip):
        """
        - Searches for row matching the specified IP Address

        :param ip: IP Address to search for
        :return:   return 1 if row with specified IP address is found, else -1
        """
        ret_val = -1
        row = self.xiqse_discovered_get_row_by_ip(ip)
        if row:
            ret_val = 1
        return ret_val

    def xiqse_discovered_get_row_by_ip(self, ip):
        """
        - This keyword returns the row containing the specified IP address

        :param ip: IP address of the device to obtain the row for
        :return:   returns the row object if found, else None
        """
        self.utils.print_info(f'Getting row for IP address {ip}')
        rows = self.get_table_rows()
        if rows:
            for row in rows:
                if ip in row.text:
                    self.utils.print_info(f"Found row for IP address {ip}: {self.xiqse_table.format_table_row(row.text)}")
                    return row

        self.utils.print_info(f"Unable to find row for IP address {ip}")
        self.screen.save_screen_shot()
        return None

    def xiqse_discovered_add_device(self, ip):
        """
         - This keyword adds the device by selecting the row matching the specified IP address, clicking Add Devices on
           the toolbar, then clicking Add in the Add Device dialog.
         - Keyword Usage
          - ``XIQSE Discovered Add Device    ${DEVICE_IP}``

        :param ip: IP Address of the device to add
        :return:   1 if action was successful, else -1
        """
        ret_val = -1

        # Select the row with the specified IP address
        self.utils.print_info(f"Selecting row with IP {ip}")
        if self.xiqse_discovered_select_row_by_ip(ip) == 1:
            # Click Add Devices on the toolbar
            add_tb_btn = self.get_add_devices_button()
            if add_tb_btn:
                self.utils.print_info("Clicking Add Devices toolbar button to display the Add Devices dialog")
                self.auto_actions.click(add_tb_btn)
                sleep(2)

                # Click Add in the Add Device dialog
                ret_val = self.add_devices_dlg.xiqse_discovered_add_devices_dialog_click_add()
            else:
                self.utils.print_info("Unable to find Add Devices toolbar button")

        if ret_val == -1:
            self.utils.print_info(f"Unable to add device with IP {ip}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_add_devices(self, ip_list):
        """
         - This keyword adds the list of devices by selecting the specified IP addresses, clicking 'Add Devices' on the
         - toolbar, then clicking 'Add' in the Add Device dialog.
         - Keyword Usage
          - ``XIQSE Discovered Add Devices    ${DEVICE_IP1}.${DEVICE_IP2},${DEVICE_IP3}``

        :param ip_list: comma-separated list of IP Addresses to add
        :return:   1 if action was successful, else -1
        """
        ret_val = -1

        # Select the rows with the specified IP addresses
        if self.xiqse_discovered_select_rows_by_ips(ip_list) == 1:
            # Click Add Devices on the toolbar
            add_tb_btn = self.get_add_devices_button()
            if add_tb_btn:
                btn_disabled = add_tb_btn.get_attribute("aria-disabled")
                if btn_disabled == "false":
                    self.utils.print_info("Clicking Add Devices toolbar button to display the Add Devices dialog")
                    self.auto_actions.click(add_tb_btn)
                    sleep(2)

                    # Click Add in the Add Device dialog
                    ret_val = self.add_devices_dlg.xiqse_discovered_add_devices_dialog_click_add()
                else:
                    self.utils.print_info("Add Devices toolbar button is disabled - check for device selections")
            else:
                self.utils.print_info("Unable to find Add Devices toolbar button")
        else:
            self.utils.print_info(f"Unable to select the specified list of IPs {ip_list}")

        if ret_val == -1:
            self.utils.print_info(f"Unable to add devices with IPs {ip_list}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_clear_row_by_ip(self, ip):
        """
         - This keyword clears the row matching the specified IP address.
         - Keyword Usage
          - ``XIQSE Discovered Clear By IP    ${DEVICE_IP}``

        :param ip: IP Address of the row to clear
        :return:   1 if action was successful, else -1
        """
        ret_val = -1
        self.utils.print_info(f"Selecting row with IP {ip}")
        if self.xiqse_discovered_select_row_by_ip(ip) == 1:
            clear_btn = self.get_clear_button()
            if clear_btn:
                self.utils.print_info("Clicking Clear toolbar button")
                self.auto_actions.click(clear_btn)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find Clear toolbar button")

        if ret_val == -1:
            self.utils.print_info(f"Unable to clear row with IP {ip}")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_discovered_clear_all_devices(self):
        """
         - This keyword clears all devices from the Discovered table.
         - Keyword Usage
          - ``XIQSE Discovered Clear All Devices``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        clear_btn = self.get_clear_all_button()
        if clear_btn:
            self.utils.print_info("Clicking Clear All Devices toolbar button")
            self.auto_actions.click(clear_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Clear All Devices toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_confirm_table_not_empty(self):
        """
         - This keyword confirms the table is not empty.
         - Keyword Usage
          - ``XIQSE Discovered Confirm Table Not Empty``

        :return: 1 if table is not empty, else -1
        """
        ret_val = -1
        rows = self.get_table_rows()
        if rows:
            row_count = len(rows)
            self.utils.print_info(f"Table not empty - {row_count} rows present")
            ret_val = 1
        else:
            self.utils.print_info("Table is empty")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_confirm_table_empty(self):
        """
         - This keyword confirms the table is empty.
         - Keyword Usage
          - ``XIQSE Discovered Confirm Table Empty``

        :return: 1 if table is empty, else -1
        """
        ret_val = 1
        rows = self.get_table_rows()
        if rows:
            row_count = len(rows)
            self.utils.print_info(f"Table not empty - {row_count} rows present")
            self.screen.save_screen_shot()
            ret_val = -1
        else:
            self.utils.print_info("Table is empty")

        return ret_val

    def xiqse_get_discovered_table_row_count(self):
        """
         - This keyword returns the number of rows in the Discovered table based on the "Displaying # rows" label.
         - Keyword Usage
          - ``XIQSE Get Discovered Table Row Count``

        :return: 1 if table contains the expected number of rows, else -1
        """
        ret_val = -1

        rows_label = self.get_displaying_rows_label()
        if rows_label:
            rows_text = rows_label.text
            self.utils.print_debug(f"Got Rows label text {rows_text}")
            text_list = rows_text.split(' ')
            # The number of total devices should be the second element in the list,
            # since this label is in the format "Displaying # rows"
            row_count = text_list[1]
            if row_count:
                self.utils.print_info(f"Returning row count {row_count}")
                ret_val = row_count
            else:
                self.utils.print_info(
                    "Unable to parse text from 'Displaying # rows' label to determine total row count")
        else:
            self.utils.print_info("Unable to find 'Displaying # Rows' label for the XIQ Device Message Details table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_discovered_confirm_table_row_count(self, value):
        """
         - This keyword confirms the table contains the expected number of rows.
         - Keyword Usage
          - ``XIQSE Discovered Confirm Table Row Count    5``

        :param value: expected number of rows to check for
        :return:      1 if table contains the expected number of rows, else -1
        """
        ret_val = -1

        row_count = self.xiqse_get_discovered_table_row_count()
        if row_count != -1:
            if row_count == value:
                self.utils.print_info(f"Table contains {value} rows, as expected")
                ret_val = 1
            else:
                self.utils.print_info(f"Table contains {row_count} rows, not the expected {value} rows")
        else:
            self.utils.print_info("Unable to obtain table row count")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_discovered_table_empty(self, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the Discovered table to be empty.
        - This keyword by default loops 10 times every 30 seconds to check if the table is empty.
        - It is assumed the Network> Discovered tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Discovered Table Empty    retry_duration=30    retry_count=12``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking if Discovered table is empty: loop {count}")
            if self.xiqse_discovered_confirm_table_empty() == 1:
                self.utils.print_info("Table is empty")
                return 1
            else:
                self.utils.print_info(f"Discovered table not yet empty. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_table.xiqse_refresh_table()
            count += 1

        # Check one last time
        self.xiqse_table.xiqse_refresh_table()
        if self.xiqse_discovered_confirm_table_empty() == 1:
            self.utils.print_info("Discovered table is empty")
            return 1

        self.utils.print_info("Discovered table is not empty. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_until_discovered_device_added(self, ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the Discovered table to contain the specified device.
        - This keyword by default loops 10 times every 30 seconds to check if the device is present.
        - It is assumed the Network> Discovered tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Discovered Device Added    1.2.3.4    retry_duration=30    retry_count=12``

        :param ip: ip address of the device to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking if Discovered table contains device with IP {ip}: loop {count}")
            if self.xiqse_discovered_find_row_with_ip(ip) == 1:
                self.utils.print_info(f"Device with IP {ip} is present in Discovered table")
                return 1
            else:
                self.utils.print_info(f"Discovered table does not contain device with IP {ip}. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_table.xiqse_refresh_table()
            count += 1

        # Check one last time
        self.xiqse_table.xiqse_refresh_table()
        if self.xiqse_discovered_find_row_with_ip(ip) == 1:
            self.utils.print_info(f"Device with IP {ip} is present in Discovered table")
            return 1

        self.utils.print_info(f"Discovered table does not contain device with IP {ip}. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_until_discovered_device_removed(self, ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the Discovered table to no longer contain the specified device.
        - This keyword by default loops 10 times every 30 seconds to check if the device is present.
        - It is assumed the Network> Discovered tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Discovered Device Removed    1.2.3.4    retry_duration=30    retry_count=12``

        :param ip: ip address of the device to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking if Discovered table contains device with IP {ip}: loop {count}")
            if self.xiqse_discovered_find_row_with_ip(ip) == -1:
                self.utils.print_info(f"Device with IP {ip} is not present in Discovered table")
                return 1
            else:
                self.utils.print_info(f"Discovered table still contains device with IP {ip}. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_table.xiqse_refresh_table()
            count += 1

        # Check one last time
        self.xiqse_table.xiqse_refresh_table()
        if self.xiqse_discovered_find_row_with_ip(ip) == -1:
            self.utils.print_info(f"Device with IP {ip} is not present in Discovered table")
            return 1

        self.utils.print_info(f"Discovered table still contains device with IP {ip}. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_until_discovered_table_contains_row_count(self, value, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the Discovered table to contain the expected number of rows.
        - This keyword by default loops 10 times every 30 seconds to check if the table is empty.
        - It is assumed the Network> Discovered tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Discovered Table Contains Row Count    5    retry_duration=30    retry_count=12``

        :param value: number of expected rows to wait for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking if Discovered table is empty: loop {value}")
            if self.xiqse_discovered_confirm_table_row_count(value) == 1:
                self.utils.print_info(f"Table contains the expected number of rows {value}")
                return 1
            else:
                self.utils.print_info(f"Discovered table does not contain expected number of rows. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_table.xiqse_refresh_table()
            count += 1

        # Check one last time
        self.xiqse_table.xiqse_refresh_table()
        if self.xiqse_discovered_confirm_table_row_count(value) == 1:
            self.utils.print_info(f"Table contains the expected number of rows {value}")
            return 1

        row_count = 0
        rows = self.get_table_rows()
        if rows:
            row_count = len(rows)
        self.utils.print_info(f"Discovered table contains {row_count} rows, not the expected number of {value} rows. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_discovered_refresh_table(self):
        """
         - This keyword clicks the refresh icon under the table.
         - Keyword Usage
          - ``XIQSE Discovered Refresh Table``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_table.xiqse_refresh_table()

    def xiqse_wait_until_device_staged(self, device_ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the device to show up as having staged config in the discovered table.
        - This keyword by default loops 10 times every 30 seconds to check if the device exists.
        - It is assumed the Network> Discovered tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Staged    ${DEVICE_IP}    retry_duration=30    retry_count=12``
        :param device_ip: device IP to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        self.xiqse_discovered_refresh_table()
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for device {device_ip}: loop {count}")
            device_row = self.xiqse_discovered_get_row_by_ip(device_ip)
            if device_row:
                self.utils.print_info(f"Device {device_ip} has been located")
                return 1
            else:
                self.utils.print_info(f"Device is not yet present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_discovered_refresh_table()
            count += 1

        # Check for device one last time
        self.xiqse_discovered_refresh_table()
        if self.xiqse_discovered_find_row_with_ip(device_ip) == 1:
            self.utils.print_info(f"Device {device_ip} has been added")
            return 1

        self.utils.print_info(f"Device does not exist. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_discovered_configure_devices_toolbar(self):
        """
         - This keyword clicks the Configure Devices... button on the Discovered table toolbar.
         - Keyword Usage
          - ``XIQSE Discovered Configure Devices Toolbar``
        :return: 1 if action was successful, else -1
        """
        ret_val = 1
        configure_devices_btn = self.get_configure_devices_button()
        if configure_devices_btn:
            self.utils.print_info("Clicking Configure Devices button")
            self.auto_actions.click(configure_devices_btn)
        else:
            self.utils.print_info("Could not find Configure Devices button in Discovered tab")
            self.screen.save_screen_shot()
            ret_val = -1
        return ret_val

    def xiqse_discovered_open_configure_devices_by_serial_number(self, serial_number):
        """
         - This keyword selects Configure Devices from the Discovered Toolbar for the row matching the specified Serial Number.
         - Keyword Usage
          - ``XIQSE Discovered Open Configure Devices By Serial Number  Serial Number``

        :param serial_number: Serial Number of the Device
        :return:   1 if action was successful, else -1
        """
        ret_val = -1
        self.utils.print_info(f"Selecting row with Serial Number {serial_number}")
        if self.xiqse_discovered_select_row_by_serial_number(serial_number) == 1:
            configure_btn = self.get_configure_devices_button()
            if configure_btn:
                self.utils.print_info(f"Clicking Configure Devices... button on the toolbar.")
                self.auto_actions.click(configure_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find Configure Devices... button on the toolbar.")

        if ret_val == -1:
            self.utils.print_info(f"Unable to select row with Serial Number {serial_number}")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_discovered_open_configure_devices_menu_by_serial_number(self, serial_number):
        """
         - This keyword clicks the Configure Devices menu item based on the device Serial Number
         - This assumes that the OneView > Network > Discovered view is selected.
         - Keyword Usage
          - ''XIQSE Discovered Open Configure Devices Menu Serial Number  Serial Number``

        :param serial_number: Serial Number for the Device
        :return: return 1 if action was successful, else -1
        """

    def xiqse_discovered_find_row_with_serial_number(self, serial_number):
        """
        - Searches for row matching the specified Serial Number
        - Keyword Usage
         - ``XIQSE Discovered Find Row With Serial Number  Serial Number``

        :param serial_number: Serial Number to search for
        :return:   return 1 if row with specified IP address is found, else -1
        """
        ret_val = -1
        row = self.xiqse_discovered_get_row_by_serial_number(serial_number)
        if row:
            ret_val = 1
        return ret_val

    def xiqse_discovered_get_row_by_serial_number(self, serial_number):
        """
        - This keyword returns the row containing the specified Serial Number
        - Keyword Usage
         - ``XIQSE Discovered Get Row By Serial Number  Serial Number``

        :param serial_number: Serial Number of the device to obtain the row for
        :return:   returns the row object if found, else None
        """
        self.utils.print_info(f"Get row for Serial Number {serial_number}")
        rows = self.get_table_rows()
        if rows:
            for row in rows:
                if serial_number.lower() in row.text.lower():
                    self.utils.print_info(f"Found row for Serial Number {serial_number}: {self.xiqse_table.format_table_row(row.text)}")
                    return row

        self.utils.print_info(f"Unable to find row for Serial Number {serial_number}")
        self.screen.save_screen_shot()
        return None

    def xiqse_discovered_select_row_by_serial_number(self, serial_number):
        """
         - This keyword selects the row containing the specified Serial Number in the Network> Discovered table.
         - Keyword Usage
          - ``XIQSE Discovered Select Row By Serial Number  Serial Number``

        :param serial_number:  Serial Number to select in the table
        :return:    1 if action was successful, else -1
        """
        ret_val = -1
        self.utils.print_info(f"Finding row with Serial Number {serial_number}")
        row = self.xiqse_discovered_get_row_by_serial_number(serial_number)
        if row:
            row_selected = row.get_attribute("aria-selected")
            if row_selected and row_selected == "true":
                self.utils.print_info(f"Row for Serial Number {serial_number} is already selected")
            else:
                self.utils.print_info(f"Selecting row with Serial Number {serial_number}")
                self.auto_actions.click(row)
            ret_val = 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to select row with Serial Number {serial_number}")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_discovered_get_device_column_value(self, serial_number, col_name):
        """
        - This keyword is used to get the desired column value for the specified device in the discovered table.
        - It is assumed the Network> Devices> Discovered tab is already selected.
        - Keyword Usage:
         - ``XIQSE Discovered Get Device Column Value    ${SERIAL_NUMBER}    Profile``
         - ``XIQSE Discovered Get Device Column Value    ${SERIAL_NUMBER}    Status``

        :param serial_number: device Serial Number to get the value for
        :param col_name:  name of the column to get the value of
        :return: column value for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_discovered_get_row_by_serial_number(serial_number)
        if device_row:
            the_col = self.get_discovered_column_by_name(col_name)
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_discovered_column_value(col_id, device_row)
            if col_val:
                the_value = col_val.text
                self.utils.print_info(f"Returning {col_name} value '{the_value}' for device {serial_number}")
                ret_val = the_value
            else:
                self.utils.print_info(f"Unable to determine {col_name} value for device {serial_number}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {serial_number}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
