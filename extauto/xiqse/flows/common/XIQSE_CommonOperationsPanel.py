from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonOperationsPanelWebElements import CommonOperationsPanelWebElements
from xiqse.flows.common.XIQSE_CommonView import XIQSE_CommonView
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_CommonOperationsPanel(CommonOperationsPanelWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.the_view = XIQSE_CommonView()

    def xiqse_open_operations_panel(self):
        """
         - This keyword opens the Operations panel, if it is closed
         - Keyword Usage
          - ``XIQSE Open Operations Panel``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        the_btn = self.get_operations_button()
        if the_btn:
            btn_pressed = the_btn.get_attribute("aria-pressed")
            if btn_pressed == "false":
                self.utils.print_info("Clicking Operations button to open panel")
                self.auto_actions.click(the_btn)
            else:
                self.utils.print_info("Operations panel is already open")

            self.utils.print_info("Waiting for any outstanding refresh to complete")
            self.the_view.xiqse_wait_for_refresh_to_complete()

            ret_val = 1
        else:
            self.utils.print_info("Unable to find Operations button to open Operations panel")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_close_operations_panel(self):
        """
         - This keyword closes the Operations panel, if it is open
         - Keyword Usage
          - ``XIQSE Close Operations Panel``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        the_btn = self.get_operations_button()
        if the_btn:
            btn_pressed = the_btn.get_attribute("aria-pressed")
            if btn_pressed == "true":
                self.utils.print_info("Clicking Operations button to close panel")
                self.auto_actions.click(the_btn)
            else:
                self.utils.print_info("Operations panel is already closed")
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Operations button to close Operations panel")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_clear_operations_panel(self):
        """
         - This keyword clears the contents of the Operations panel
         - Keyword Usage
          - ``XIQSE Clear Operations Panel``

        :return: 1 if action successful, else -1
        """
        ret_val = -1

        self.xiqse_open_operations_panel()

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_operations_table_group_rows()
                if rows:
                    first_row = rows[0]
                    if first_row:
                        self.utils.print_info("Accessing right-click menu on the first row")
                        self.screen.save_screen_shot()
                        self.auto_actions.right_click(first_row)
                        clear_all = self.get_clear_all_menu()
                        if clear_all:
                            self.utils.print_info("Clicking Clear All")
                            self.auto_actions.click(clear_all)
                            self.screen.save_screen_shot()
                            ret_val = 1
                        else:
                            self.utils.print_info("Could not find 'Clear All' menu option")
                    else:
                        self.utils.print_info("Unable to obtain first row, so could not open right-click menu")
                else:
                    self.utils.print_info("Operations panel is already cleared")
                    ret_val = 1

                # Exit the StaleElementReferenceException handler loop
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_operations_expand_group(self, value):
        """
         - This keyword expands the specified group in the Operations panel, if it is not yet expanded.
         - If there is more than one matching entry in the panel, this will expand the first matching entry.
         - Keyword Usage
          - ``XIQSE Operations Expand Group  Discover Site``

        :param value:  name of the group to expand
        :return: 1 if action successful, else -1
        """
        ret_val = -1

        # Make sure the operations panel is open
        self.xiqse_open_operations_panel()

        stale_retry = 1
        while stale_retry <= 10:
            try:
                group_row = self.get_operations_table_group_row(value)
                if group_row:
                    row_class = group_row.get_attribute("class")
                    self.utils.print_debug(f"Row class is {row_class}")
                    if row_class and "collapsed" in row_class:
                        self.utils.print_info(f"Clicking row '{value}' to expand it")
                        self.auto_actions.click(group_row)
                    else:
                        self.utils.print_info(f"Row '{value}' is already expanded")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to find group row for '{value}'")

                # Exit the StaleElementReferenceException handler loop
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_operations_get_operation_complete(self, value):
        """
         - This keyword checks the progress of the specified operation in the Operations panel.
         - Keyword Usage
          - ``XIQSE Operations Get Operation Complete  Discover Site``

        :param value:  name of the operation to get the progress of
        :return: 1 if operation progress is at 100%, else -1
        """
        ret_val = -1

        # Make sure the group is expanded
        self.xiqse_operations_expand_group(value)

        stale_retry = 1
        while stale_retry <= 10:
            try:
                # Determine the progress value for the operation
                data_row = self.get_operations_table_group_data_row(value)
                if data_row:
                    row_progress = self.get_operations_table_data_row_progress(data_row)
                    if row_progress:
                        self.utils.print_debug(f"Row progress is {row_progress}")
                        if "100%" in row_progress:
                            self.utils.print_info("Operation is complete")
                            ret_val = 1
                        else:
                            self.utils.print_info(f"Operation '{value}' is not complete - progress is at {row_progress}")
                    else:
                        self.utils.print_info(f"Unable to determine progress for operation {value}")
                else:
                    self.utils.print_info(f"Could not find data row for {value}")

                # Exit the StaleElementReferenceException handler loop
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_operations_get_discovered_device_count(self):
        """
         - This keyword obtains the discovered device count from the last Site Discover operations panel entry.
         - Keyword Usage
          - ``XIQSE Operations Get Discovered Device Count``

        :return: returns the number of discovered devices as reported in the message for the Discover Site entry
        """
        ret_val = -1

        # Make sure the group is expanded
        self.xiqse_operations_expand_group("Discover Site")

        stale_retry = 1
        while stale_retry <= 10:
            try:
                # Determine the progress value for the operation
                data_row = self.get_operations_table_group_data_row("Discover Site")
                if data_row:
                    row_cells = self.get_operations_table_data_row_cells(data_row)
                    if row_cells:
                        for cell in row_cells:
                            cell_text = cell.get_attribute("data-qtip")
                            if cell_text:
                                self.utils.print_info(f"DATA FOR CELL IS {cell_text}")
                                if "Discovered Devices:" in cell_text:
                                    text_list = cell_text.split('Discovered Devices:')
                                    # The number of discovered devices should be the last element in the list,
                                    # since the data for this column ends with "Discovered Devices:##"
                                    device_count = text_list[-1]
                                    if device_count:
                                        self.utils.print_info(f"Returning device count {device_count}")
                                        ret_val = device_count
                                    break
                                elif "Discovered Device:" in cell_text:
                                    text_list = cell_text.split('Discovered Device:')
                                    # The number of discovered devices should be the last element in the list,
                                    # since the data for this column ends with "Discovered Device:##"
                                    device_count = text_list[-1]
                                    if device_count:
                                        self.utils.print_info(f"Returning device count {device_count}")
                                        ret_val = device_count
                                    break
                            else:
                                self.utils.print_info("Could not get data for cell")
                                self.screen.save_screen_shot()
                        else:
                            self.utils.print_info(f"Unable to determine progress for operation Discover Site")
                            self.screen.save_screen_shot()
                    else:
                        self.utils.print_info("Unable to obtain cells for row")
                        self.screen.save_screen_shot()

                    # Exit the StaleElementReferenceException handler loop
                    break
                else:
                    self.utils.print_info(f"Could not find data row for operation Discover Site")
                    self.screen.save_screen_shot()

                    # Exit the StaleElementReferenceException handler loop
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return ret_val

    def xiqse_operations_wait_until_operation_complete(self, op_type, retry_duration=30, retry_count=10):
        """
         - This keyword waits until the specified operation type has completed by checking for a progress value of 100%.
         - It is assumed the operations panel has been cleared prior to performing the operation in question, as the
         - first-found entry will be used for the progress check.
         - Keyword Usage
          - ``XIQSE Operations Wait Until Operation Complete    Inventory Audit``
          - ``XIQSE Operations Wait Until Operation Complete    Discover Site    retry_duration=10    retry_count=60``

        :param op_type: type of operation to check the progress of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for '{op_type}' to complete: loop {count}")
            if self.xiqse_operations_get_operation_complete(op_type) == 1:
                self.utils.print_info(f"'{op_type}' has completed")
                return 1
            else:
                self.utils.print_info(f"'{op_type}' is still in progress. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        self.utils.print_info(f"'{op_type}' did not complete within allotted time. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_confirm_operations_panel_message_for_type(self, op_type, the_message):
        """
         - This keyword confirms the message from the last operations panel type entry contains the expected text.
         - Keyword Usage
          - ``XIQSE Confirm Operations Panel Message For Type    ${OP_TYPE}    ${THE_MESSAGE}``

        :param op_type:       type of operation to check the message on
        :param the_message:   message to verify is present
        :return: 1 if message is found, else -1
        """
        ret_val = -1

        # Make sure the group is expanded
        self.xiqse_operations_expand_group(op_type)

        # Determine the progress value for the operation
        data_row = self.get_operations_table_group_data_row(op_type)
        if data_row:
            row_cells = self.get_operations_table_data_row_cells(data_row)
            for cell in row_cells:
                cell_text = cell.get_attribute("data-qtip")
                if cell_text:
                    if the_message in cell_text:
                        self.utils.print_info(f"Found matching message in cell:  {cell_text}")
                        ret_val = 1
                        break
                else:
                    self.utils.print_info("Could not get data for cell")
            else:
                self.utils.print_info("Did not find matching message in cell")
        else:
            self.utils.print_info(f"Could not find data row for operation {op_type}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_operations_panel_is_empty(self):
        """
         - This keyword confirms the Operations panel is empty
         - Keyword Usage
          - ``XIQSE Confirm Operations Panel Is Empty``

        :return: 1 if operations panel is empty, else -1
        """
        ret_val = -1

        self.xiqse_open_operations_panel()

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_operations_table_group_rows()
                if rows:
                    ret_val = -1
                    self.utils.print_info("Operations Panel is not empty")
                else:
                    ret_val = 1
                    self.utils.print_info("Operations panel is empty")

                # Exit the StaleElementReferenceException handler loop
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
