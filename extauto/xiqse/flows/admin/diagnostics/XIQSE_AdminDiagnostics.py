from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.diagnostics.AdminDiagnosticsWebElements import AdminDiagnosticsWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.common.XIQSE_CommonNavigator import XIQSE_CommonNavigator
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_AdminDiagnostics(AdminDiagnosticsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_nav = XIQSE_CommonNavigator()
        self.xiqse_table = XIQSE_CommonTable()

    def xiqse_set_level_advanced(self):
        """
         - This keyword sets the Level dropdown to Advanced.
         - Keyword Usage
          - ``XIQSE Set Level Advanced``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        level_dd = self.get_level_dropdown()
        if level_dd:
            self.utils.print_info("Clicking 'Level' dropdown")
            self.auto_actions.click(level_dd)
            advanced_choice = self.get_level_advanced_choice()
            if advanced_choice:
                self.utils.print_info("Clicking 'Advanced' choice")
                self.auto_actions.click(advanced_choice)
                ret_val = 1
            else:
                self.utils.print_info("Could not find 'Advanced' choice from Level dropdown")
                self.screen.save_screen_shot()
                self.auto_actions.click(level_dd)
        else:
            self.utils.print_info("Unable to find the 'Level' dropdown'")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_expand_server_tree_node(self):
        """
         - This keyword expands the Server tree node in the panel on the left if not already expanded.
         - Keyword Usage
          - ``XIQSE Expand Server Tree Node``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        tree_node = self.get_server_tree_node()
        if tree_node:
            node_collapsed = self.get_server_tree_node_collapsed()
            if node_collapsed:
                self.utils.print_info("Expanding Server tree node")
                self.auto_actions.click(tree_node)
            else:
                self.utils.print_info("Server tree node is already expanded")
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Server tree node")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_expand_system_tree_node(self):
        """
         - This keyword expands the System tree node in the panel on the left if not already expanded.
         - Keyword Usage
          - ``XIQSE Expand System Tree Node``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        tree_node = self.get_system_tree_node()
        if tree_node:
            node_collapsed = self.get_system_tree_node_collapsed()
            if node_collapsed:
                self.utils.print_info("Expanding System tree node")
                self.auto_actions.click(tree_node)
            else:
                self.utils.print_info("System tree node is already expanded")
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the System tree node")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_server_log_tree_node(self):
        """
         - This keyword selects the Server Log tree node in the panel on the left.
         - If the parent "Server" node is not expanded, it will expand it first.
         - Keyword Usage
          - ``XIQSE Select Server Log Tree Node``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_expand_server_tree_node():
            tree_node = self.get_server_log_tree_node()
            if tree_node:
                self.utils.print_info("Selecting Server Log tree node")
                self.auto_actions.click(tree_node)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find the 'Server Log' tree node")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to expand parent 'Server' tree node")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_server_log_clear(self):
        """
         - This keyword clicks the Clear button in the Server Log view.
         - Assumes already navigated to the Administration> Diagnostics> Server> Server Log view.
         - Keyword Usage
          - ``XIQSE Server Log Clear``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        server_log_panel_title = self.get_server_log_panel_title()
        if server_log_panel_title:
            clear_btn = self.get_server_log_clear_button()
            if clear_btn:
                self.utils.print_info("Clicking Clear for Server Log View")
                self.auto_actions.click(clear_btn)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find the 'Clear' button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Server Log view is not currently displayed")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_server_log_refresh(self):
        """
         - This keyword clicks the Refresh button in the Server Log view.
         - Assumes already navigated to the Administration> Diagnostics> Server> Server Log view.
         - Keyword Usage
          - ``XIQSE Server Log Refresh``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        server_log_panel_title = self.get_server_log_panel_title()
        if server_log_panel_title:
            refresh_btn = self.get_server_log_refresh_button()
            if refresh_btn:
                self.utils.print_info("Clicking Refresh for Server Log View")
                self.auto_actions.click(refresh_btn)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find the 'Refresh' button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Server Log view is not currently displayed")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_server_log_contents_contains_string(self, value):
        """
         - This keyword checks for the specified string in the contents of the Server Log view.
         - Assumes already navigated to the Administration> Diagnostics> Server> Server Log view.
         - Keyword Usage
          - ``XIQSE Confirm Server Log Contents Contains String  ${STRING_TO_FIND}``

        :param value: string to look for in the server log
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        server_log_panel_title = self.get_server_log_panel_title()
        if server_log_panel_title:
            contents_panel = self.get_server_log_contents()
            if contents_panel:
                self.utils.print_info("Got contents panel")
                contents_text = contents_panel.text
                if contents_text:
                    self.utils.print_debug(f"Contents: {contents_text}")
                    if value in contents_text:
                        self.utils.print_info(f"Found {value} in server.log")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Did not find {value} in server.log")
                        self.utils.print_debug(f"Contents: {contents_text}")
                else:
                    self.utils.print_info("Unable to get contents of Server Log panel")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find the Server Log Contents panel")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Server Log view is not currently displayed")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_xiq_device_message_details_tree_node(self):
        """
         - This keyword selects the XIQ Device Message Details tree node in the panel on the left.
         - If the parent "System" node is not expanded, it will expand it first.
         - Keyword Usage
          - ``XIQSE Select XIQ Device Message Details Tree Node``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_set_level_advanced():
            if self.xiqse_expand_system_tree_node():
                tree_node = self.get_xiq_device_message_details_tree_node()
                if tree_node:
                    self.utils.print_info("Selecting XIQ Device Message Details tree node")
                    self.auto_actions.click(tree_node)
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to find the 'XIQ Device Message Details' tree node")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to expand parent 'System' tree node")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to set the level to Advanced")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_xiq_device_message_details_show_columns(self, *columns):
        """
        - This keyword shows the specified list of columns if they are currently hidden.
        - Assumes already navigated to the Administration> Diagnostics> System> XIQ Device Message Details view.
        -  Keyword Usage:
         - ``XIQSE XIQ Device Message Details Show Columns        Onboard Status  Onboard``

        :param columns: list of columns to show
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        self.utils.print_debug("Getting IP Address column header")
        ip_col = self.get_xiq_device_message_details_ip_address_column_header()
        if ip_col:
            ret_val = self.xiqse_table.xiqse_table_show_columns(ip_col, *columns)
        else:
            self.utils.print_info("Could not find IP Address column")
            self.screen.save_screen_shot()

        self.utils.print_debug("Closing Column Selection Menu")
        self.auto_actions.click(self.get_xiq_device_message_details_title())

        return ret_val

    def xiqse_xiq_device_message_details_hide_columns(self, *columns):
        """
        - This keyword hides the specified list of columns if they are currently shown.
        - Assumes already navigated to the Administration> Diagnostics> System> XIQ Device Message Details view.
        -  Keyword Usage:
         - ``XIQSE XIQ Device Message Details Hide Columns        Onboard Status  Onboard``

        :param columns: list of columns to hide
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        self.utils.print_debug("Getting IP Address column header")
        ip_col = self.get_xiq_device_message_details_ip_address_column_header()
        if ip_col:
            ret_val = self.xiqse_table.xiqse_table_hide_columns(ip_col, *columns)
        else:
            self.utils.print_info("Could not find IP Address column")
            self.screen.save_screen_shot()

        self.utils.print_debug("Closing Column Selection Menu")
        self.auto_actions.click(self.get_xiq_device_message_details_title())

        return ret_val

    def xiqse_confirm_onboard_status(self, device_ip, device_type, expected_value):
        """
        - Searches for row matching device's IP Address and Type and confirms the Onboard Status value is expected.
        - Assumes the XIQ Device Message Details view is open and the Onboard Status column is shown.

        :param device_ip: Device IP Address to search for
        :param device_type: Device Type to search for
        :param expected_value: expected value of the onboard status
        :return: returns 1 if onboard status matches the expected value, else -1
        """
        ret_val = -1

        onboard_status = self.xiqse_xiq_device_message_details_get_onboard_status(device_ip, device_type)
        if onboard_status != -1:
            if onboard_status == expected_value:
                self.utils.print_info(f"Device with IP {device_ip} and type {device_type} has expected Onboard Status {expected_value}")
                ret_val = 1
            else:
                self.utils.print_info(f"Device with IP {device_ip} and type {device_type} has Onboard Status {onboard_status}, not expected value of {expected_value}")
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_xiq_device_message_details_row(self, device_ip, device_type=None):
        """
        - This keyword returns the row for the device matching the IP address and optional type

        :param device_ip: IP address of the device to obtain the row for
        :param device_type: Device Type of the device to obtain the row for - optional
        :return: returns the row object if found, else None
        """
        if device_type:
            self.utils.print_info(f'Getting row for device with IP address {device_ip} and type {device_type}')
        else:
            self.utils.print_info(f'Getting row for device with IP address {device_ip}')
        rows = self.get_xiq_device_message_details_table_rows()
        if rows:
            for row in rows:
                self.utils.print_debug(f"Looking at row {self.xiqse_table.format_table_row(row.text)}")
                if device_ip in row.text:
                    if device_type:
                        if device_type in row.text:
                            self.utils.print_info(f"Found device row for ip {device_ip} and type {device_type}: {self.xiqse_table.format_table_row(row.text)}")
                            return row
                    else:
                        self.utils.print_info(f"Found device row for ip {device_ip}: {self.xiqse_table.format_table_row(row.text)}")
                        return row

        if device_type:
            self.utils.print_info(f'Unable to find device row in grid for IP address {device_ip} and type {device_type}')
        else:
            self.utils.print_info(f'Unable to find device row in grid for IP address {device_ip}')
        self.screen.save_screen_shot()
        return None

    def xiqse_xiq_device_message_details_refresh_table(self):
        """
        - Refreshes the table on the XIQ Device Message Details page.
        - Assumes the XIQ Device Message Details view is open.

        :return: returns 1 if action is successful, else -1
        """
        ret_val = -1

        refresh_btn = self.get_xiq_device_message_details_refresh_button()
        if refresh_btn:
            self.utils.print_info("Refreshing XIQ Device Message Details Table")
            self.auto_actions.click(refresh_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find refresh button for the XIQ Device Message Details table")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_xiq_device_message_details_row_count(self):
        """
        - Returns the number of rows displayed in the XIQ Device Message Details table, as reported by
        - the "Displaying # of rows" label.
        - Assumes the XIQ Device Message Details view is open.

        :return: number of rows in the table
        """
        ret_val = -1

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows_label = self.get_xiq_device_message_details_displaying_rows_label()
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
                        self.utils.print_info("Unable to parse text from 'Displaying # rows' label to determine total row count")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find 'Displaying # Rows' label for the XIQ Device Message Details table")
                    self.screen.save_screen_shot()
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return ret_val

    def xiqse_xiq_device_message_details_filter_table(self, value):
        """
        - Filters the XIQ Device Message Details table by the specified value.
        - Assumes the XIQ Device Message Details view is open.

        :param value: string to enter in the search field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        search_btn = self.get_xiq_device_message_details_search_button()
        if search_btn:
            self.utils.print_info("Clicking Search button")
            self.auto_actions.click(search_btn)
            search_text = self.get_xiq_device_message_details_search_text_field()
            action_btn = self.get_xiq_device_message_details_perform_search_button()
            if search_text and action_btn:
                self.utils.print_info(f"Sending {value} to Search field")
                self.auto_actions.send_keys(search_text, value)
                self.auto_actions.click(action_btn)
                sleep(2)
                ret_val = 1
            else:
                self.utils.print_info("Unable to find Search text field for the XIQ Device Message Details table")
        else:
            self.utils.print_info("Unable to find Search button for the XIQ Device Message Details table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_xiq_device_message_details_clear_filter(self):
        """
        - Clears the filter on the XIQ Device Message Details table.
        - Assumes the XIQ Device Message Details view is open and the search box is open.

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        search_text = self.get_xiq_device_message_details_search_text_field()
        if search_text:
            if search_text.is_displayed():
                clear_btn = self.get_xiq_device_message_details_search_clear_button()
                if clear_btn:
                    if clear_btn.is_displayed():
                        self.utils.print_info("Clicking clear button in the search field")
                        self.auto_actions.click(clear_btn)
                        panel_title = self.get_xiq_device_message_details_title()
                        if panel_title:
                            self.auto_actions.click(panel_title)
                        else:
                            self.utils.print_info("Could not close search field")
                    else:
                        self.utils.print_info("Clear search button is not displayed")
                    ret_val = 1
                else:
                    self.utils.print_info("Could not find clear button for search field")
            else:
                self.utils.print_info("Search text field for the XIQ Device Message Details table is not open")
                ret_val = 1
        else:
            self.utils.print_info("Unable to find Search text field for the XIQ Device Message Details table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_xiq_device_message_details_get_metric_from_device(self, device_ip, device_type, metric):
        """
        - Gets the specified metric value sent to XIQ for the specified device by using the Show XIQ Messages button
        - in the XIQ Device Message Details table.
        - Assumes the XIQ Device Message Details view is open.

        :param device_ip:    IP Address of the device to obtain the information for
        :param device_type:  Device Type of the device to obtain the information for
        :param metric:       Value of the metric to obtain the information for
        :return: metric value if action is successful, else -1
        """
        ret_val = -1

        # Select the row
        device_row = self.xiqse_get_xiq_device_message_details_row(device_ip, device_type)
        if device_row:
            self.utils.print_debug(f"Got row {device_row.text}")
            self.auto_actions.click(device_row)
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip} and type {device_type}")

        msg_btn = self.get_xiq_device_message_details_show_xiq_messages_button()
        if msg_btn:
            self.utils.print_info("Clicking 'Show XIQ Messages' button")
            self.auto_actions.click(msg_btn)
            sleep(2)
            dialog_title = self.get_show_xiq_messages_dialog_title()
            if dialog_title:
                dialog_content = self.get_show_xiq_messages_dialog_content()
                if dialog_content:
                    dialog_text = dialog_content.text
                    self.utils.print_debug(f"Dialog Text: {dialog_text}")
                    row_values = dialog_text.split(",")
                    metric_row = None
                    metric_string = '"' + metric + '":'
                    self.utils.print_debug(f"Looking for metric string: {metric_string}")
                    for row in row_values:
                        if metric_string in row:
                            self.utils.print_debug(f"FOUND ROW: {row}")
                            metric_row = row
                            break
                    if metric_row:
                        metric_values = metric_row.split(":")
                        if len(metric_values) == 2:
                            self.utils.print_debug(f"KEY: {metric_values[0]}")
                            self.utils.print_debug(f"VALUE: {metric_values[1]}")
                            ret_val = metric_values[1].strip()
                            self.utils.print_info(f"Returning value for {metric}: {ret_val}")
                        else:
                            self.utils.print_info(f"Unable to obtain value for {metric}")
                    else:
                        self.utils.print_info(f"Unable to obtain row for {metric}")
                else:
                    self.utils.print_info("Dialog content was empty")

                # Close the dialog
                close_btn = self.get_show_xiq_messages_dialog_close_button()
                if close_btn:
                    self.utils.print_info("Clicking 'Close' button")
                    self.auto_actions.click(close_btn)
                else:
                    self.utils.print_info("Could not find 'Close' button for Show XIQ Messages dialog")
            else:
                self.utils.print_info("Show XIQ Messages dialog is not displayed")
        else:
            self.utils.print_info("Unable to find 'Show XIQ Messages' button for the XIQ Device Message Details table")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_xiq_device_message_details_get_last_update_time(self, device_ip, device_type):
        """
        - Gets the value in the Last Update Time column for the specified device in the XIQ Device Message Details table.
        - Assumes the XIQ Device Message Details view is open.

        :param device_ip:    IP Address of the device to obtain the information for
        :param device_type:  Device Type of the device to obtain the information for
        :return: Value of the 'Last Update Time' column if action is successful, else -1
        """
        ret_val = -1

        # Make sure the Last Update Time column is displayed in the table
        if self.xiqse_xiq_device_message_details_show_columns("Last Update Time"):
            # Find the row
            device_row = self.xiqse_get_xiq_device_message_details_row(device_ip, device_type)
            if device_row:
                self.utils.print_debug(f"Got row {device_row.text}")
                the_col = self.get_xiq_device_message_details_last_update_time_col()
                col_id = self.view_el.get_column_id(the_col)
                self.utils.print_debug(f"Column ID: {col_id}")
                last_update_col = self.get_xiq_device_message_details_column(col_id, device_row)
                if last_update_col:
                    ret_val = last_update_col.text
                    self.utils.print_info(f"Last Update Time: {ret_val}")
                else:
                    self.utils.print_info("Unable to get 'Last Update Time' column value")
            else:
                self.utils.print_info(f"Unable to find row for device with IP {device_ip} and type {device_type}")
        else:
            self.utils.print_info("Unable to show 'Last Update Time' column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_xiq_device_message_details_get_onboard_status(self, device_ip, device_type):
        """
        - Gets the value in the Onboard Status column for the specified device in the XIQ Device Message Details table.
        - Assumes the XIQ Device Message Details view is open.

        :param device_ip:    IP Address of the device to obtain the information for
        :param device_type:  Device Type of the device to obtain the information for
        :return: Value of the 'Onboard Status' column if action is successful, else -1
        """
        ret_val = -1

        # Make sure the Onboard Status column is displayed in the table
        if self.xiqse_xiq_device_message_details_show_columns("Onboard Status"):
            stale_retry = 1
            while stale_retry <= 10:
                try:
                    # Find the row
                    device_row = self.xiqse_get_xiq_device_message_details_row(device_ip, device_type)
                    if device_row:
                        self.utils.print_debug(f"Got row {device_row.text}")
                        the_col = self.get_xiq_device_message_details_onboard_status_col()
                        col_id = self.view_el.get_column_id(the_col)
                        self.utils.print_debug(f"Column ID: {col_id}")
                        status_col = self.get_xiq_device_message_details_column(col_id, device_row)
                        if status_col:
                            ret_val = status_col.text
                            self.utils.print_info(f"Onboard Status: {ret_val}")
                        else:
                            self.utils.print_info("Unable to get 'Onboard Status' column value")
                    else:
                        self.utils.print_info(
                            f"Unable to find row for device with IP {device_ip} and type {device_type}")
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1
        else:
            self.utils.print_info("Unable to show 'Onboard Status' column")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_xiq_device_message_details_auto_onboard_xiqse(self, email_value, pwd_value):
        """
        - Clicks the Auto Onboard XIQ-SE button.
        - Assumes the XIQ Device Message Details view is open.

        :param email_value: Value to enter into the Email field
        :param pwd_value:   Value to enter into the Password field
        :return: 1 if successful, else -1
        """
        ret_val = -1

        onboard_btn = self.get_xiq_device_message_details_auto_onboard_xiqse_button()
        if onboard_btn:
            self.utils.print_info("Clicking 'Auto Onboard XIQ-SE' button")
            self.auto_actions.click(onboard_btn)
            dialog_title = self.get_auto_onboard_xiqse_dialog_title()
            if dialog_title:
                email_field = self.get_auto_onboard_xiqse_dialog_email_field()
                pwd_field = self.get_auto_onboard_xiqse_dialog_password_field()
                if email_field and pwd_field:
                    self.utils.print_info(f"Entering Email Value '{email_value}'")
                    self.auto_actions.send_keys(email_field, email_value)
                    self.utils.print_info(f"Entering Password Value '{pwd_value}'")
                    self.auto_actions.send_keys(pwd_field, pwd_value)

                    # Click Submit
                    submit_btn = self.get_auto_onboard_xiqse_dialog_submit_button()
                    if submit_btn:
                        self.utils.print_info("Clicking Submit")
                        self.auto_actions.click(submit_btn)
                    else:
                        self.utils.print_info("Could not find 'Submit' button for 'Auto Onboard XIQ-SE to XIQ' dialog")

                    # Confirm
                    ok_btn = self.get_auto_onboard_xiqse_dialog_confirm_ok()
                    if ok_btn:
                        self.utils.print_info("Clicking OK to confirm auto onboard action")
                        self.auto_actions.click(ok_btn)
                        ret_val = 1
                    else:
                        self.utils.print_info("Could not find 'OK' button to confirm auto onboard action")
                else:
                    self.utils.print_info("Could not find input fields for 'Auto Onboard XIQ-SE to XIQ' dialog")
            else:
                self.utils.print_info("'Auto Onboard XIQ-SE to XIQ' dialog is not displayed")
        else:
            self.utils.print_info("Unable to find 'Auto Onboard XIQ-SE' button in the XIQ Device Message Details view")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_auto_onboard_xiqse(self, email_value, pwd_value):
        """
        - Clicks the Auto Onboard XIQ-SE button, enters the email and password credentials, clicks Submit, and confirms
        - the onboard action.

        :param email_value: Value to enter into the Email field
        :param pwd_value:   Value to enter into the Password field
        :return: 1 if successful, else -1
        """
        ret_val = self.xiqse_nav.xiqse_navigate_to_admin_diagnostics_tab()
        if ret_val != -1:
            sleep(2)
            ret_val = self.xiqse_select_xiq_device_message_details_tree_node()
            if ret_val != -1:
                sleep(2)
                ret_val = self.xiqse_xiq_device_message_details_auto_onboard_xiqse(email_value, pwd_value)
                if ret_val == -1:
                    self.utils.print_info("Unable to onboard XIQ-SE to XIQ")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to select the XIQ Device Message Details node")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to the Diagnostics tab")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_device_has_expected_onboard_status(self, device_ip, device_type, expected_value,
                                                            retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to have the expected Onboard Status in the Device Message Details.
        - The column checked is "Onboarded Status".
        - This keyword by default loops 10 times every 30 seconds to check if the status is at the expected value.
        - It is assumed the Administration> Diagnostics tab is already selected and on the System> ExtremeCloud IQ Device
        - Message Details view.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Has Expected Onboard Status   1.1.1.1  X460-G2-48t-10G4  DEVICE_ALREADY_ONBOARDED``
         - ``XIQSE Wait Until Device Has Expected Onboard Status   2.2.2.2  XIQ_SE  SUCCESS  retry_duration=10  retry_count=12``

        :param device_ip: device IP to check the Onboard Status of
        :param device_type:  Device Type of the device to obtain the information for
        :param expected_value: expected value for the Onboard Status to wait for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device has expected onboard status within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Onboard Status Check - Loop: ", count)
            self.xiqse_table.xiqse_refresh_table()

            col_value = self.xiqse_xiq_device_message_details_get_onboard_status(device_ip, device_type)
            if col_value and col_value == expected_value:
                self.utils.print_info(f"Device has expected Onboard Status {expected_value}")
                ret_val = 1
                break
            else:
                if col_value:
                    self.utils.print_info(f"Current Onboard Status is {col_value}")
                else:
                    self.utils.print_info("Cannot determine current Onboard Status")
                self.utils.print_info(f"Device does not have expected Onboard Status. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device does not have expected onboard status of {expected_value}. Please check.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_onboard_xiqse_if_not_onboarded(self, xiqse_ip, email_value, pwd_value):
        """
        - Onboards XIQSE if it is not yet onboarded:
        -   Checks if XIQSE is present in the table and, if it is not, it sends the request to onboard.
        -   If XIQSE is present in the table with onboard status of UNKNOWN, it sends the request to onboard.

        :param xiqse_ip:    IP of XIQSE to check for
        :param email_value: Value to enter into the Email field
        :param pwd_value:   Value to enter into the Password field
        :return: 1 if successful, else -1
        """
        ret_val = self.xiqse_nav.xiqse_navigate_to_admin_diagnostics_tab()
        if ret_val != -1:
            sleep(2)
            ret_val = self.xiqse_select_xiq_device_message_details_tree_node()
            if ret_val != -1:
                sleep(2)
                xiqse_row = self.xiqse_get_xiq_device_message_details_row(xiqse_ip, "XIQ_SE")
                if not xiqse_row:
                    self.utils.print_info("XIQSE is not yet onboarded to XIQ - sending request to onboard")
                    ret_val = self.xiqse_xiq_device_message_details_auto_onboard_xiqse(email_value, pwd_value)
                    if ret_val == -1:
                        self.utils.print_info("Unable to onboard XIQ-SE to XIQ")
                        self.screen.save_screen_shot()
                else:
                    col_value = self.xiqse_xiq_device_message_details_get_onboard_status(xiqse_ip, "XIQ_SE")
                    if col_value and col_value == "UNKNOWN":
                        self.utils.print_info(f"XIQSE has UNKNOWN onboard status - sending request to onboard")
                        ret_val = self.xiqse_xiq_device_message_details_auto_onboard_xiqse(email_value, pwd_value)
                        if ret_val == -1:
                            self.utils.print_info("Unable to onboard XIQ-SE to XIQ")
                            self.screen.save_screen_shot()
                    else:
                        self.utils.print_info(f"XIQSE is present with onboard status of {col_value}")
                        ret_val = 1
            else:
                self.utils.print_info("Unable to select the XIQ Device Message Details node")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to navigate to the Diagnostics tab")
            self.screen.save_screen_shot()

        return ret_val
