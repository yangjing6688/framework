from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.elements.DeviceCommonElements import DeviceCommonElements


class DeviceCommon(DeviceCommonElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    def _get_device_grid_row_by_serial(self, device_serial=''):
        """
        - This method is used to get the device grid row where the serial number is a match

        :param device_serial: serial number of the device
        :return: row if match, else None
        """
        for row in self.get_device_grid_rows():
            if device_serial in row.text:
                self.utils.print_info("Found the row with the device serial: ", device_serial)
                return row

        self.utils.print_info("Device serial is not found in the Device grid")
        return None

    def _get_client_cell(self, row):
        """
        - This method is used to get the client cell

        :param row: device row object
        :return: cell if match, else None
        """
        for cell in self.get_device_row_cells_with_row(row):
            if "activeClientCount" in cell.get_attribute("class"):
                self.utils.print_info("Found the client cell")
                return cell

        self.utils.print_info("Connected Clients column is not found in the Device grid")
        return None

    def _get_hostname_cell(self, row):
        """
        - This method is used to get the host name cell

        :param row: device row object
        :return: cell if match, else None
        """
        for cell in self.get_device_row_cells_with_row(row):
            if "hostname" in cell.get_attribute("class"):
                self.utils.print_info("Found the host name cell")
                return cell

        self.utils.print_info("Host Name column is not found in the Device grid")
        return None

    def _get_mac_cell(self, row):
        """
        - This method is used to get the MAC cell

        :param row: device row object
        :return: cell if match, else None
        """
        for cell in self.get_device_row_cells_with_row(row):
            if "macAddress" in cell.get_attribute("class"):
                self.utils.print_info("Found the MAC cell")
                return cell

        self.utils.print_info("MAC column is not found in the Device grid")
        return None

    def _get_policy_cell(self, row):
        """
        - This method is used to get the Network Policy cell

        :param row: device row object
        :return: cell if match, else None
        """
        for cell in self.get_device_row_cells_with_row(row):
            if "networkPolicyName" in cell.get_attribute("class"):
                self.utils.print_info("Found the policy cell")
                return cell

        self.utils.print_info("Network Policy column is not found in the Device grid")
        return None

    def _get_location_cell(self, row):
        """
        - This method is used to get the Location cell

        :param row: device row object
        :return: cell if match, else None
        """
        for cell in self.get_device_row_cells_with_row(row):
            if "locationName" in cell.get_attribute("class"):
                self.utils.print_info("Found the location cell")
                return cell

        self.utils.print_info("Location column is not found in the Device grid")
        return None

    def _select_device_grid_row(self, row):
        """
        - This method is used to select the device grid row select check box
        - Check the row select status every 5 seconds with loop count of 50 seconds
        - within 50 seconds it should get select, otherwise there is issue with device grid refresh on Manage --> Device
          page

        :param row: device row object to select
        :return: True if device grid row selected else False
        """
        retry_loop_count = 0
        while True:
            self.utils.print_info("select device grid row check box")
            self.auto_actions.click(self.get_device_row_select_check_box(row))
            sleep(2)
            row_attr = row.get_attribute("class")
            self.utils.print_info(row_attr)
            if "dgrid-selected" in row_attr:
                return True
            elif retry_loop_count >= 50:
                return False
            sleep(5)
            retry_loop_count += 5

    def select_device_row(self, device_serial='', device_mac='', device_name='', **kwargs):
        """
        - This keyword is used to select the single device row in Manage --> Device page
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Select Device Row   device_serial=${DEVICE_SERIAL}``
        - ``Select Device Row   device_mac=${DEVICE_MAC}``
        - ``Select Device Row   device_name=${DEVICE_NAME}``

        :param device_serial: serial number of the device
        :param device_mac: MAC Address of the device
        :param device_name: name of the device
        :return: 1 if device row selected, -1 if device row not found in grid
        """
        search_str = ''
        search_criteria = ''

        if device_serial:
            search_str = device_serial
            search_criteria = "Serial Number"
        elif device_mac:
            search_str = device_mac
            search_criteria = "MAC Address"
        elif device_name:
            search_str = device_name
            search_criteria = "Name"

        if not search_str:
            kwargs['fail_msg'] = "Pass the Device Serial Number, MAC address, or Name."
            self.common_validation.fault(**kwargs)
            return -1

        sleep(10)
        for row in self.get_device_grid_rows():
            if search_str in row.text:
                self.utils.print_info(f"Selecting the device row: {search_str}")
                if self._select_device_grid_row(row):
                    kwargs['pass_msg'] = "Device grid row selected"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = "Device grid row is not selected"
                    self.common_validation.fault(**kwargs)
                    return -1

        kwargs['fail_msg'] = f"Device row not found with {search_criteria}: {search_str}"
        self.common_validation.failed(**kwargs)
        return -1

    def select_device_rows(self, device_serials='', device_macs='', device_names='', **kwargs):
        """
        - This keyword is used to select the multiple device row in Manage --> Device page
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Select Device Rows   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}``
        - ``Select Device Rows   device_macs=${DEVICE1_MAC},${DEVICE2_MAC}``
        - ``Select Device Rows   device_names=${DEVICE1_NAME},${DEVICE2_NAME}``

        :param device_serials:  comma separated list of device serial numbers
        :param device_macs:  comma separated list of device MAC addresses
        :param device_names:  comma separated list of device names
        :return: 1 if devices rows selected Successfully else -1
        """
        if device_serials:
            device_list = device_serials.split(',')
            for device in device_list:
                if self.select_device_row(device_serial=device) == -1:
                    kwargs['fail_msg'] = f"The Device with Serial Number {device} was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
            return 1
        elif device_macs:
            device_list = device_macs.split(',')
            for device in device_list:
                if self.select_device_row(device_mac=device) == -1:
                    kwargs['fail_msg'] = f"The Device with MAC Address {device} was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
            return 1
        elif device_names:
            device_list = device_names.split(',')
            for device in device_list:
                if self.select_device_row(device_name=device) == -1:
                    kwargs['fail_msg'] = f"The Device with Name {device} was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
            return 1
        else:
            kwargs['fail_msg'] = "Pass the Device Serial Number, MAC address, or Name."
            self.common_validation.fault(**kwargs)
            return -1

    def edit_device(self, device_serial, **kwargs):
        """
        - This keyword is used to select the single device and click on the edit but in Manage --> Device page
        - Assumes that navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Edit Device   ${DEVICE_SERIAL}``

        :param device_serial:
        :return: 1 if device selected in grid and able to click edit button else -1
        """
        if self.select_device_row(device_serial):
            self.utils.print_info("Click on device tab edit button")
            self.auto_actions.click_reference(self.get_device_table_edit_button)
            kwargs['pass_msg'] = "The device is selected in grid and able to click edit button"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "The device is not selected in grid"
        self.common_validation.failed(**kwargs)
        return -1

    def edit_devices(self, device_serials=''):
        """
        - This keyword is used to select the multiple device and click on the edit but in Manage --> Device page
        - Assumes that navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Edit Device   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}``

        :param device_serials: device serial numbers with comma separated
        :return: 1 if Multiple devices selected in grid and able to click edit button else -1
        """
        self.select_device_rows(device_serials)
        sleep(4)
        self.utils.print_info("Click on device tab edit button")
        self.auto_actions.click_reference(self.get_device_table_edit_button)
        return 1

    def go_to_device360_window(self, device_mac='', device_host='', **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword click on device MAC or device host name hyper link based on the passed args
        - Keyword Usage:
        - ``Go To Device360 Window   ${DEVICE_MAC}``
        - ``Go To Device360 Window   ${DEVICE_HOST}``

        :param device_mac: device MAC
        :param device_host: Device host name
        :return: 1 if device 360 page Opened Successfully else -1
        """
        search_strg = ''

        if device_mac:
            search_strg = device_mac
        elif device_host:
            search_strg = device_host

        if not search_strg:
            kwargs['fail_msg'] = "Device MAC or Device host name is missing, please pass the args"
            self.common_validation.fault(**kwargs)
            return -1
        rows = self.get_device_grid_rows()
        if not rows:
            kwargs['fail_msg'] = "Can not obtain rows"
            self.common_validation.fault(**kwargs)
            return -1

        for row in rows:
            if search_strg in row.text:
                self.utils.print_info(f"found device with:{search_strg}")
                if self.get_device_row_cells_with_row(row):
                    for cell in self.get_device_row_cells_with_row(row):
                        if search_strg in cell.text:
                            self.utils.print_info("click on device cell")
                            sleep(5)
                            if self.get_cell_href(cell):
                                self.auto_actions.click(self.get_cell_href(cell))
                                sleep(5)
                                kwargs['pass_msg'] = "Clicked on device cell"
                                self.common_validation.passed(**kwargs)
                                return 1

        kwargs['fail_msg'] = f"Device not found in the grid with:{search_strg}"
        self.common_validation.failed(**kwargs)
        return -1

    def goto_device360_with_client(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and clicks on client hyperlink.
        - Keyword Usage:
        - ``Goto Device360 With Client   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if navigated to client page from manage devices grid else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_client_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Clicking on client hyperlink")
                self.auto_actions.click(self.get_cell_href(cell))
                sleep(5)
                kwargs['pass_msg'] = "Successfully navigated to client page from manage devices grid "
                self.common_validation.passed(**kwargs)
                return 1

            else:
                kwargs['fail_msg'] = "Could not navigate to client page and click on client hyperlink"
                self.common_validation.failed(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "Row with passed device serial is missing"
            self.common_validation.fault(**kwargs)
            return -1

    def goto_device360_with_mac(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and clicks on MAC hyperlink.
        - Keyword Usage:
        - ``Goto Device360 With Mac   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if navigated to D360 page from manage devices grid else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_mac_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Clicking on MAC hyperlink")
                self.auto_actions.click(self.get_cell_href(cell))
                sleep(5)
                kwargs['pass_msg'] = "Successfully navigated to D360 page from manage devices grid "
                self.common_validation.passed(**kwargs)
                return 1

            else:
                kwargs['fail_msg'] = "Could not navigate to D360 page and click on MAC hyperlink"
                self.common_validation.failed(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "Row with passed device serial is missing"
            self.common_validation.fault(**kwargs)
            return -1

    def goto_device360_with_hostname(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and clicks on host name hyperlink.
        - Keyword Usage:
        - ``Goto Device360 With Hostname   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if navigated to D360 page from manage devices grid else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_hostname_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Clicking on Host Name hyperlink")
                self.auto_actions.click(self.get_cell_href(cell))
                sleep(5)
                kwargs['pass_msg'] = "Successfully navigated to D360 page from manage devices grid "
                self.common_validation.passed(**kwargs)
                return 1

            else:
                kwargs['fail_msg'] = "Could not navigate to D360 page and click on host name hyperlink"
                self.common_validation.failed(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "Row with passed device serial is missing"
            self.common_validation.fault(**kwargs)
            return -1

    def get_select_device_checkbox_status(self, device_serial, **kwargs):
        """
        - This keyword is used to select the single device row in Manage --> Device page
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Select Device Row   ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device
        :return: 1 if device row selected, -1 if device row not found in grid
        """
        sleep(10)
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            self.utils.print_info(f"Checking Select Device Checkbox Status for the device row: {device_serial}")
            if self._select_device_checkbox_status_row(row):
                kwargs['pass_msg'] = "Clicked on device cell"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Select Device Checkbox not selected"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['fail_msg'] = f"Select Device Checkbox is Checked with serial number:{device_serial}"
        self.common_validation.fault(**kwargs)
        return -1

    def _select_device_checkbox_status_row(self, row):
        """
        - This method is used to select the device grid row select check box
        - Check the row select status every 5 seconds with loop count of 50 seconds
        - within 50 seconds it should get select, otherwise there is issue with device grid refresh on Manage --> Device
          page

        :param row: device row object to select
        :return: True f device grid row selected else False
        """
        retry_loop_count = 0
        while True:
            row_attr = row.get_attribute("class")
            self.utils.print_info(row_attr)
            if "dgrid-selected" in row_attr:
                return True
            elif retry_loop_count >= 50:
                return False
            sleep(5)
            retry_loop_count += 5

    def check_select_all_devices_checkbox_status(self, device_serials='', **kwargs):
        """
        - This keyword is used to click on select all check box and validate devices are selected
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Check Select All Devices Checkbox Status   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}``

        :param device_serials:  device serial numbers with comma separated
        :return: 1 if all Devices Selected Successfully else -1
        """
        self.utils.print_info("Click on Select All Devices Button")
        self.auto_actions.click_reference(self.get_manage_devices_select_all_devices_checkbox)
        sleep(2)

        device_sr_nums = device_serials.split(',')
        for sr in device_sr_nums:
            if self.get_select_device_checkbox_status(sr) == -1:
                kwargs['fail_msg'] = f"Device is not selected: {sr}"
                self.common_validation.failed(**kwargs)
                return -1
            sleep(2)

        kwargs['pass_msg'] = "All Devices Selected Successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def get_devices_per_page(self, **kwargs):
        """
        - This keyword is used to obtain the number of devices that are displayed per page.
        - Keyword Usage:
        - ``Get Devices Per Page``
        :return: the current Devices Per Page value, else -1
        """
        ret_val = -1
        the_field = self.get_devices_per_page_current()

        if the_field:
            self.auto_actions.move_to_element(the_field)
            current = the_field.text
            if current:
                self.utils.print_info(f"Devices Per Page value is set to {current}")
                ret_val = current
                self.screen.save_screen_shot()
            else:
                kwargs['fail_msg'] = "The Devices Per Page value could not be found."
                self.common_validation.failed(**kwargs)
        else:
            kwargs['fail_msg'] = "The Devices Per Page field could not be found."
            self.common_validation.fault(**kwargs)

        return ret_val

    def update_devices_per_page(self, device_count=10, **kwargs):
        """
        - This keyword is used to select the number of devices that are displayed on the page.
        - Keyword Usage:
        - ``Update Devices Per Page  ${DEVICE_COUNT}``
        :param device_count: the number of devices displayed per page - 10, 20, 50, or 100
        :return: None
        """
        ret_val = -1
        the_field = self.get_devices_per_page_value(device_count=device_count)

        if the_field:
            self.auto_actions.move_to_element(the_field)
            kwargs['pass_msg'] = f"Updating Devices Per Page value to {device_count}"
            self.auto_actions.click_reference(lambda: self.get_devices_per_page_value(device_count=device_count))
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"A Devices Per Page value of {device_count} is not supported."
            self.common_validation.fault(**kwargs)

        return ret_val

    def _is_client_link_available(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and checks if client hyperlink is available
        - Keyword Usage:
        - ``Is Client Link Available   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if available else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_client_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Client link is available")
                kwargs['pass_msg'] = "Client link is available"
                self.common_validation.passed(**kwargs)
                return 1

            else:
                self.utils.print_info("Client link is not available")
                return False

        else:
            kwargs['fail_msg'] = "Row with passed device serial is not found"
            self.common_validation.fault(**kwargs)
            return -1

    def verify_client_link_available(self, tag, **kwargs):
        """
        - This keyword verifies if client hyperlink is available
        - Keyword Usage:
         - ``Verify Client Link Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if error occurs
        """

        return self._is_client_link_available(tag, **kwargs)

    def verify_client_link_not_available(self, tag, **kwargs):
        """
        - This keyword verifies if client hyperlink is not available
        - Keyword Usage:
         - ``Verify Client Link Not Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if not visible else -1
        """
        if self._is_client_link_available(tag, **kwargs):
            kwargs['fail_msg'] = "Client link is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Client link is not available"
            self.common_validation.passed(**kwargs)
            return 1

    def _is_hostname_link_available(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and checks if host name hyperlink is available
        - Keyword Usage:
        - ``Is Hostname Link Available   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if available else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_hostname_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Host Name link is available")
                kwargs['pass_msg'] = "Hostname link is available"
                self.common_validation.passed(**kwargs)
                return 1

            else:
                self.utils.print_info("Host Name link is not available")
                return False

        else:
            kwargs['fail_msg'] = "Row with passed device serial is not found"
            self.common_validation.fault(**kwargs)
            return -1

    def verify_hostname_link_available(self, tag, **kwargs):
        """
        - This keyword verifies if host name hyperlink is available
        - Keyword Usage:
         - ``Verify Hostname Link Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if error occurs
        """

        return self._is_hostname_link_available(tag, **kwargs)

    def verify_hostname_link_not_available(self, tag, **kwargs):
        """
        - This keyword verifies if host name hyperlink is available
        - Keyword Usage:
         - ``Verify Hostname Link Not Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if not visible else -1
        """
        if self._is_hostname_link_available(tag, **kwargs):
            kwargs['fail_msg'] = "Host Name link is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Host Name link is not available"
            self.common_validation.passed(**kwargs)
            return 1

    def _is_mac_link_available(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and checks if mac hyperlink is available
        - Keyword Usage:
        - ``Is Mac Link Available   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if available else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_mac_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("MAC link is available")
                kwargs['pass_msg'] = "MAC link is available"
                self.common_validation.passed(**kwargs)
                return 1

            else:
                self.utils.print_info("MAC link is not available")
                return False

        else:
            kwargs['fail_msg'] = "Row with passed device serial is not found"
            self.common_validation.fault(**kwargs)
            return -1

    def verify_mac_link_available(self, tag, **kwargs):
        """
        - This keyword verifies if mac hyperlink is available
        - Keyword Usage:
         - ``Verify Mac Link Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if error occurs
        """

        return self._is_mac_link_available(tag, **kwargs)

    def verify_mac_link_not_available(self, tag, **kwargs):
        """
        - This keyword verifies if mac hyperlink is not available
        - Keyword Usage:
         - ``Verify Mac Link Not Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if not visible else -1
        """
        if self._is_mac_link_available(tag, **kwargs):
            kwargs['fail_msg'] = "MAC link is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "MAC link is not available"
            self.common_validation.passed(**kwargs)
            return 1

    def _is_policy_link_available(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and checks if network policy hyperlink is available
        - Keyword Usage:
        - ``Is Policy Link Available   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if available else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_policy_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Policy link is available")
                kwargs['pass_msg'] = "Policy link is available"
                self.common_validation.passed(**kwargs)
                return 1

            else:
                self.utils.print_info("Policy link is not available")
                return False

        else:
            kwargs['fail_msg'] = "Row with passed device serial is not found"
            self.common_validation.fault(**kwargs)
            return -1

    def verify_policy_link_available(self, tag, **kwargs):
        """
        - This keyword verifies if network policy hyperlink is available
        - Keyword Usage:
         - ``Verify Policy Link Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if error occurs
        """

        return self._is_policy_link_available(tag, **kwargs)

    def verify_policy_link_not_available(self, tag, **kwargs):
        """
        - This keyword verifies if network policy hyperlink is not available
        - Keyword Usage:
         - ``Verify Policy Link Not Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if not visible else -1
        """
        if self._is_policy_link_available(tag, **kwargs):
            kwargs['fail_msg'] = "Policy link is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Policy link is not available"
            self.common_validation.passed(**kwargs)
            return 1

    def _is_location_link_available(self, device_serial=None, **kwargs):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and checks if location hyperlink is available
        - Keyword Usage:
        - ``Is Location Link Available   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if available else -1
        """
        row = self._get_device_grid_row_by_serial(device_serial)
        if row:
            cell = self._get_location_cell(row)
            if cell and self.get_cell_href(cell):
                self.utils.print_info("Location link is available")
                kwargs['pass_msg'] = "Location link is available"
                self.common_validation.passed(**kwargs)
                return 1

            else:
                self.utils.print_info("Location link is not available")
                return False

        else:
            kwargs['fail_msg'] = "Row with passed device serial is not found"
            self.common_validation.fault(**kwargs)
            return -1

    def verify_location_link_available(self, tag, **kwargs):
        """
        - This keyword verifies if location hyperlink is available
        - Keyword Usage:
         - ``Verify Location Link Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if error occurs
        """

        return self._is_location_link_available(tag, **kwargs)

    def verify_location_link_not_available(self, tag, **kwargs):
        """
        - This keyword verifies if location hyperlink is available
        - Keyword Usage:
         - ``Verify Location Link Not Available``
        :param tag: automation tag for the nav menu item
        :return: 1 if not visible else -1
        """
        if self._is_location_link_available(tag, **kwargs):
            kwargs['fail_msg'] = "Location link is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Location link is not available"
            self.common_validation.passed(**kwargs)
            return 1
