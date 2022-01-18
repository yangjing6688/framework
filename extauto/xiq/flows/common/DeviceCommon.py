from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiq.elements.DeviceCommonElements import DeviceCommonElements


class DeviceCommon(DeviceCommonElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()

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

    def select_device_row(self, device_serial='', device_mac='', device_name=''):
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
            self.utils.print_info("Pass the Device Serial Number, MAC address, or Name.")
            return -1

        sleep(10)
        for row in self.get_device_grid_rows():
            if search_str in row.text:
                self.utils.print_info(f"Selecting the device row: {search_str}")
                if self._select_device_grid_row(row):
                    return 1
                else:
                    self.utils.print_info(f"device grid row not selected")
                    return -1
        self.utils.print_info(f"Device row not found with {search_criteria}: {search_str}")
        return -1

    def select_device_rows(self, device_serials='', device_macs='', device_names=''):
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
                    self.utils.print_info(f"The Device with Serial Number {device} was not found")
            return 1
        elif device_macs:
            device_list = device_macs.split(',')
            for device in device_list:
                if self.select_device_row(device_mac=device) == -1:
                    self.utils.print_info(f"The Device with MAC Address {device} was not found")
            return 1
        elif device_names:
            device_list = device_names.split(',')
            for device in device_list:
                if self.select_device_row(device_name=device) == -1:
                    self.utils.print_info(f"The Device with Name {device} was not found")
            return 1
        else:
            self.utils.print_info("Pass the Device Serial Number, MAC address, or Name.")
            return -1

    def edit_device(self, device_serial):
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
            self.auto_actions.click(self.get_device_table_edit_button())
            return 1
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
        self.auto_actions.click(self.get_device_table_edit_button())
        return 1

    def go_to_device360_window(self, device_mac='', device_host=''):
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
            self.utils.print_info(f"Pass the device MAC or Device host name")
            return -1

        for row in self.get_device_grid_rows():
            if search_strg in row.text:
                self.utils.print_info(f"found device with:{search_strg}")
                for cell in self.get_device_row_cells():
                    if search_strg in cell.text:
                        self.utils.print_info(f"click on device cell")
                        self.auto_actions.click(self.get_cell_href(cell))
                        sleep(5)
                        return 1
        self.utils.print_info(f"Device not found in the grid with:{search_strg}")
        return -1

    def goto_device360_with_client(self, device_serial=None):
        """
        - Assume that navigated to the Manage --> Device
        - This keyword searches for the row with passed device serial and clicks on client hyperlink.
        - Keyword Usage:
         - ``Goto  Device360 With Client   ${DEVICE_SERIAL}``

        :param device_serial:  device serial number
        :return: 1 if navigated to client page from manage devices grid else -1
        """
        for row in self.get_device_grid_rows():
            if device_serial in row.text:
                self.utils.print_info("Selecting the row with the device serial: ", device_serial)
                for cell in self.get_device_row_cells_with_row(row):
                    if "activeClientCount" in cell.get_attribute("class"):
                        self.utils.print_info("Clicking on client hyperlink")
                        self.auto_actions.click(self.get_cell_href(cell))
                        sleep(5)

                        return 1

        self.utils.print_info("Device serial is not found in the Device grid")
        return -1

    def get_select_device_checkbox_status(self, device_serial):
        """
        - This keyword is used to select the single device row in Manage --> Device page
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Select Device Row   ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device
        :return: 1 if device row selected, -1 if device row not found in grid
        """
        sleep(10)
        for row in self.get_device_grid_rows():
            if device_serial in row.text:
                self.utils.print_info(f"Checking Select Device Checkbox Status for the device row: {device_serial}")
                if self._select_device_checkbox_status_row(row):
                    return 1
                else:
                    self.utils.print_info(f"Select Device Checkbox not selected")
                    return -1
        self.utils.print_info(f"Select Device Checkbox is Checked with serial number:{device_serial}")
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

    def check_select_all_devices_checkbox_status(self, device_serials=''):
        """
        - This keyword is used to click on select all check box and validate devices are selected
        - Assumes that already navigated to the Manage --> Device page
        - Keyword Usage:
         - ``Check Select All Devices Checkbox Status   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}``

        :param device_serials:  device serial numbers with comma separated
        :return: 1 if all Devices Selected Successfully else -1
        """
        self.utils.print_info("Click on Select All Devices Button")
        self.auto_actions.click(self.get_manage_devices_select_all_devices_checkbox())
        sleep(2)

        device_sr_nums = device_serials.split(',')
        for sr in device_sr_nums:
            if self.get_select_device_checkbox_status(sr) == -1:
                return -1
            sleep(2)
        return 1

    def get_devices_per_page(self):
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
                self.utils.print_info("The Devices Per Page value could not be found.")
        else:
            self.utils.print_info("The Devices Per Page field could not be found.")

        return ret_val

    def update_devices_per_page(self, device_count=10):
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
            self.utils.print_info(f"Updating Devices Per Page value to {device_count}")
            self.auto_actions.click(self.get_devices_per_page_value(device_count=device_count))
            return 1
        else:
            self.utils.print_info(f"A Devices Per Page value of {device_count} is not supported.")

        return ret_val
