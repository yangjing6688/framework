import re
import os
import copy
from time import sleep
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.flows.common.Login import Login
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements

from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
from extauto.common.Cli import Cli


class Devices:
    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.devices_web_elements = DevicesWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.switch_web_elements = SwitchWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()

        self.navigator = Navigator()
        self.device_actions = DeviceActions()
        self.device_update = DeviceUpdate()
        self.device_common = DeviceCommon()
        self.cli = Cli()
        self.screen = Screen()
        self.robot_built_in = BuiltIn()
        self.custom_file_dir = os.getcwd() + '/onboard_csv_files/'
        self.login = Login()
        self.cli = Cli()


    def onboard_ap(self, ap_serial, device_make, location, device_os=False):
        """
        - This keyword on-boards an aerohive device [AP or Switch] using Quick on-boarding flow.
        - Keyword Usage:
         - ``Onboard Ap   ${AP_SERIAL}   ${AP_TYPE}``

        :param ap_serial: serial number of AP
        :param device_make: Model of the AP i.e aerohive
        :param device_os: verifies the Device OS automatically selected after entering device serial
        :param location: location of the device Ex: San Jose, building_01, floor_02
        :return: 1 if on boarded else -1
        """
        self.navigator.navigate_to_devices()
        if self.search_ap_serial(ap_serial) == 1:
            self.utils.print_info(f"Ap with {ap_serial} serial number already onboarded")
            return 1

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), ap_serial)

        if device_os:
            sleep(5)
            self.utils.print_info("Verify Device OS")
            device_os = self.devices_web_elements.get_device_os_radio().text
            self.utils.print_info("Device OS: ", device_os)
            if 'Cloud IQ Engine' in device_os:
                self.utils.print_info("Device OS matched")

        if location:
            self.utils.print_info("Selecting location")
            self.auto_actions.click(self.devices_web_elements.get_location_button())
            self._select_location(location)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -1
            if "A stake record of the device was found in the redirector." in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -2
        else:
            self.utils.print_info("No Errors while onboarding")

        serials = ap_serial.split(",")
        self.utils.print_info("Device Serials Numbers: ", serials)

        for serial in serials:
            if self.search_ap_serial(serial):
                self.utils.print_info("Successfully Onboarded AP(s): ", serials)
                return 1
            else:
                return -1

    def _goto_devices(self):
        self.navigator.navigate_to_devices()
        sleep(2)

    def _exit_here(self, level):
        """
        This keyword exits the test-case or test-suite depending on the exit level

        :param level: can be test_suite or test_case
        :return: 1
        """
        if level:
            if 'test_suite' in level:
                self.robot_built_in.fatal_error("Aborting TEST SUITE...")
            elif 'test_case' in level:
                self.robot_built_in.fail('Aborting TEST CASE...')
            else:
                self.utils.print_info(f'Unexpected exit level {level}')
                return 1
        else:
            self.utils.print_info('No exit level defined')
            return 1

    def get_ap_status(self, ap_serial='default', ap_name='default', ap_mac='default'):
        """
        - This keyword returns the AP's status by searching AP using serial, name or mac address
        - Keyword Usage:
         - ``Get Ap Status    ap_serial=${AP_SERIAL}``
         - ``Get Ap Status    ap_name=${AP_NAME}``
         - ``Get Ap Status    ap_mac=${AP_MAC}``

        :param ap_serial: AP Serial
        :param ap_name: AP Name ie AP Host name in GUI ex: AH-2aa840
        :param ap_mac: AP MAC
        :return: 'green' if the AP is online else return -1
        """
        ap_row = -1
        self.utils.print_info('Getting AP Status using')
        if ap_serial != 'default':
            self.utils.print_info("Getting status of AP with serial: ", ap_serial)
            ap_row = self.get_ap_row(ap_serial=ap_serial)

        if ap_name != 'default':
            self.utils.print_info("Getting status2 of AP with name: ", ap_name)
            ap_row = self.get_ap_row(ap_name=ap_name)

        if ap_mac != 'default':
            self.utils.print_info("Getting status of AP with MAC: ", str(ap_mac).upper())
            ap_row = self.get_ap_row(ap_mac=str(ap_mac).upper())

        if ap_row:
            sleep(10)
            ap_status = self.devices_web_elements.get_status_cell(ap_row)
            self.utils.print_info("ap status " + ap_status)

            if self.devices_web_elements.get_manage_device_search_clear_button().is_displayed():
                self.utils.print_info("Clear search filter option")
                self.auto_actions.click(self.devices_web_elements.get_manage_device_search_clear_button())
                sleep(5)

            if 'true' in ap_status:
                self.utils.print_info("AP Status: Connected")
                return 'green'

        self.screen.save_screen_shot()

        return -1

    def _verify_ap_status(self, ap_serial='default', ap_name='default', ap_mac='default', status='default'):
        """
        - This keyword returns 1 if AP status expected matches the status passed as argument

        :param ap_serial: AP Serial
        :param ap_name: AP Name
        :param ap_mac: AP MAC
        :param status: green, red, or amber as of now - may change in future

        :return:
        """
        if ap_serial != 'default':
            if status in self.get_ap_status(ap_serial):
                return 1
        if ap_name != 'default':
            if status in self.get_ap_status(ap_name):
                return 1
        if ap_mac != 'default':
            if status in self.get_ap_status(ap_mac):
                return 1

    def get_os_change(self, device_serial=None, device_name=None, device_mac=None):
        self.voss = False
        self.exos = False
        if device_mac:
            search_result = self.search_exos_device(device_mac)
            if search_result != -1:
                if self.select_device(device_mac):
                    self.utils.print_info("Click ACTION button")
                    self.auto_actions.click(self.devices_web_elements.get_action_button())
                    self.utils.print_info("Click change os Button")
                    if self.voss:
                        self.auto_actions.click(self.devices_web_elements.get_os_change_exos())
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info("Check for error message")
                        device_error_message = self.devices_web_elements.get_os_change_error_message()
                        self.utils.print_info("Error message: ", device_error_message.text)
                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                        sleep(2)
                        self.screen.save_screen_shot()

                    if self.exos:
                        self.auto_actions.click(self.devices_web_elements.get_os_change_voss())
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info("Check for error message")
                        device_error_message = self.devices_web_elements.get_os_change_error_message()
                        self.utils.print_info("Error message: ", device_error_message.text)
                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                        sleep(2)
                        self.screen.save_screen_shot()

            else:
                self.utils.print_info(f"Device with MAC is not EXOS or VOSS device")
                return 1
        if device_serial:
            search_result = self.search_exos_device(device_serial)
            if search_result != -1:
                if self.select_device(device_serial):
                    self.utils.print_info("Click ACTION button")
                    self.auto_actions.click(self.devices_web_elements.get_action_button())
                    self.utils.print_info("Click change os Button")
                    if self.voss:
                        self.auto_actions.click(self.devices_web_elements.get_os_change_exos())
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info("Check for error message")
                        device_error_message = self.devices_web_elements.get_os_change_error_message()
                        self.utils.print_info("Error message: ", device_error_message.text)
                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                        sleep(2)
                        self.screen.save_screen_shot()
                    if self.exos:
                        self.auto_actions.click(self.devices_web_elements.get_os_change_voss())
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info("Check for error message")
                        device_error_message = self.devices_web_elements.get_os_change_error_message()
                        self.utils.print_info("Error message: ", device_error_message.text)
                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                        sleep(2)
                        self.screen.save_screen_shot()
            else:
                self.utils.print_info(f"Device with serial is not EXOS or VOSS device")
                return 1
        if device_name:
            search_result = self.search_exos_device(device_name)
            if search_result != -1:
                if self.select_device(device_name):
                    self.utils.print_info("Click ACTION button")
                    self.auto_actions.click(self.devices_web_elements.get_action_button())
                    self.utils.print_info("Click change os Button")
                    if self.voss:
                        self.auto_actions.click(self.devices_web_elements.get_os_change_exos())
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info("Check for error message")
                        device_error_message = self.devices_web_elements.get_os_change_error_message()
                        self.utils.print_info("Error message: ", device_error_message.text)
                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                        sleep(2)
                        self.screen.save_screen_shot()
                    if self.exos:
                        self.auto_actions.click(self.devices_web_elements.get_os_change_voss())
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info("Check for error message")
                        device_error_message = self.devices_web_elements.get_os_change_error_message()
                        self.utils.print_info("Error message: ", device_error_message.text)
                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                        sleep(2)
                        self.screen.save_screen_shot()
            else:
                self.utils.print_info(f"Device with device name is not EXOS or VOSS device")
                return 1

    def search_exos_device(self, EXOS_VOSS_device):
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)
        device_tag = False
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            self.utils.print_debug(f"Searching {len(rows)} rows")
            for row in rows:
                if EXOS_VOSS_device in row.text and 'VOSS' in row.text:
                    self.utils.print_info("Found VOSS device: ", self.format_row(row.text))
                    self.voss = True
                    device_tag = True
                    return 1
                if EXOS_VOSS_device in row.text and 'EXOS' in row.text:
                    self.utils.print_info("Found EXOS device: ", self.format_row(row.text))
                    device_tag = True
                    self.exos = True
                    return 1
        else:
            self.utils.print_info("No rows present")

        if device_tag == False:
            self.utils.print_info("Device is not EXOS or VOSS ")
            return -1
        self.utils.print_info(f"Did not find device row {EXOS_VOSS_device}")
        return -1

    def get_ap_row_with_search_option(self, ap_serial='default', ap_name='default', ap_mac='default'):
        """
        - Get the AP row object from the Devices grid
        - Keyword Usage:
         - ``Get AP Row With Search Option  ap_serial=${AP_SERIAL}``
         - ``Get AP Row With Search Option  ap_name=${AP_NAME}``
         - ``Get AP Row With Search Option  ap_mac=${AP_MAC}``

        :param ap_serial: AP Serial
        :param ap_name: AP Name
        :param ap_mac: AP MAC
        :return: returns the row object
        """
        if ap_serial != 'default':
            self.utils.print_info("Searching Device Entry with AP Serial : ", ap_serial)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_serial)
            self.screen.save_screen_shot()
            sleep(5)

        if ap_name != 'default':
            self.utils.print_info("Searching Device Entry with AP Name : ", ap_name)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_name)
            self.screen.save_screen_shot()
            sleep(5)

        if ap_mac != 'default':
            self.utils.print_info("Searching Device Entry with AP Mac : ", ap_mac)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_mac)
            self.screen.save_screen_shot()
            sleep(5)

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_serial != 'default':
                    if ap_serial in row.text:
                        self.utils.print_info("Found AP row: ", self.format_row(row.text))
                        return row
                if ap_name != 'default':
                    if ap_name in row.text:
                        self.utils.print_info("Found AP row: ", self.format_row(row.text))
                        sleep(5)
                        return row
                if ap_mac != 'default':
                    if ap_mac in row.text:
                        self.utils.print_info("Found AP row: ", self.format_row(row.text))
                        return row
        else:
            self.utils.print_info("No rows present")

    def get_ap_row_without_search_option(self, ap_serial='default', ap_name='default', ap_mac='default'):
        """
        - Get the AP row object from the Devices grid
        - Keyword Usage:
         - ``Get AP Row Without Search Option  ap_serial=${AP_SERIAL}``
         - ``Get AP Row Without Search Option  ap_name=${AP_NAME}``
         - ``Get AP Row Without Search Option  ap_mac=${AP_MAC}``

        :param ap_serial: AP Serial
        :param ap_name: AP Name
        :param ap_mac: AP MAC
        :return: returns the row object
        """

        self.utils.print_info('Getting AP row on Devices Page...')
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_serial != 'default':
                    if ap_serial in row.text:
                        self.utils.print_info("Found AP row: ", self.format_row(row.text))
                        return row
                if ap_name != 'default':
                    if ap_name in row.text:
                        self.utils.print_info("Found AP row: ", self.format_row(row.text))
                        return row
                if ap_mac != 'default':
                    if str(ap_mac) in row.text:
                        self.utils.print_info("Found AP row: ", self.format_row(row.text))
                        return row
        else:
            self.utils.print_info("No rows present")

    def get_ap_row(self, ap_serial='default', ap_name='default', ap_mac='default'):
        """
        - Get the AP row object from the Devices grid
        - Keyword Usage:
         - ``Get AP Row  ap_serial=${AP_SERIAL}``
         - ``Get AP Row  ap_name=${AP_NAME}``
         - ``Get AP Row  ap_mac=${AP_MAC}``

        :param ap_serial: AP Serial
        :param ap_name: AP Name
        :param ap_mac: AP MAC
        :return: returns the row object
        """
        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info('Getting AP row with Pagination Enabled on Devices Page...')
            if ap_serial != 'default':
                self.utils.print_info("Getting status of AP with serial: ", ap_serial)
                ap_row = self.get_ap_row_with_search_option(ap_serial=ap_serial)
                return ap_row

            if ap_name != 'default':
                self.utils.print_info("Getting status of AP with name: ", ap_name)
                ap_row = self.get_ap_row_with_search_option(ap_name=ap_name)
                return ap_row

            if ap_mac != 'default':
                self.utils.print_info("Getting status of AP with MAC: ", ap_mac)
                ap_row = self.get_ap_row_with_search_option(ap_mac=ap_mac)
                return ap_row
        else:
            self.utils.print_info('Getting AP row on Devices Page without Pagination Enabled...')
            if ap_serial != 'default':
                self.utils.print_info("Getting status of AP with serial: ", ap_serial)
                ap_row = self.get_ap_row_without_search_option(ap_serial=ap_serial)
                return ap_row

            if ap_name != 'default':
                self.utils.print_info("Getting status of AP with name: ", ap_name)
                ap_row = self.get_ap_row_without_search_option(ap_name=ap_name)
                return ap_row

            if ap_mac != 'default':
                self.utils.print_info("Getting status of AP with MAC: ", ap_mac)
                ap_row = self.get_ap_row_without_search_option(ap_mac=ap_mac)
                return ap_row

        self.utils.print_info("Unable to find AP row in grid")
        return -1

    def search_ap(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Searches for the AP matching either one of serial, name or MAC
        - Keyword Usage:
         - ``Search AP  ap_serial=${AP_SERIAL}``
         - ``Search AP  ap_name=${AP_NAME}``
         - ``Search AP  ap_mac=${AP_MAC}``

        :param ap_serial: AP Serial
        :param ap_name: AP Name
        :param ap_mac: AP MAC
        :return: 1 if ap present in the grid else False
        """
        if ap_serial:
            self.utils.print_info("Searching AP with Serial: ", ap_serial)
            return self.search_ap_serial(ap_serial)
        if ap_name:
            self.utils.print_info("Searching AP with Name: ", ap_name)
            return self.search_ap_name(ap_name)
        if ap_mac:
            self.utils.print_info("Searching AP with MAC: ", ap_mac)
            return self.search_ap_mac(ap_mac)
        return False

    def search_ap_serial(self, ap_serial):
        """
        - Searches for AP matching AP's Serial Number
        - Keyword Usage:
         - ``Search AP Serial  ${AP_SERIAL}``

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found else False
        """
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(10)

        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info("Searching Device Entry with AP Serial : ", ap_serial)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_serial)
            self.screen.save_screen_shot()
            sleep(5)

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info("row data: ", self.format_row(row.text))
                if ap_serial in row.text:
                    self.utils.print_info("Found AP Row: ", self.format_row(row.text))
                    return 1
            self.utils.print_info("Did not find AP")
        else:
            self.utils.print_info("No rows present")
        return False

    def search_ap_mac(self, ap_mac=None):
        """
        - Searches for AP matching AP's MAC
        - Keyword Usage
         - ``Search Ap Mac   ${AP_MAC}``

        :param ap_mac: AP's MAC
        :return: return 1 if AP found else -1
        """
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(10)

        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info("Searching Device Entry with AP Mac : ", ap_mac)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_mac)
            self.screen.save_screen_shot()
            sleep(5)

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_mac in row.text:
                    self.utils.print_info("Found AP Row: ", self.format_row(row.text))
                    return 1
            self.utils.print_info("Did not find AP")
        else:
            self.utils.print_info("No rows present")
        return -1

    def search_ap_name(self, ap_name):
        """
        - Searches for AP matching AP's Host NAME
        - Keyword Usage:
         - ``Search AP Name  ${AP_NAME}``

        :param ap_name: AP's Name
        :return: return 1 if AP found
        """
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(10)

        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info("Searching Device Entry with AP Name : ", ap_name)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_name)
            self.screen.save_screen_shot()
            sleep(5)

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_name in row.text:
                    self.utils.print_info("Found AP Row: ", self.format_row(row.text))
                    return 1
            self.utils.print_info("Did not find AP")
        else:
            self.utils.print_info("No rows present")
        return -1

    def search_ap_model(self, ap_model):
        """
        - Searches for AP matching AP's Model
        - Keyword Usage:
         - ``Search AP Model ${AP_MODEL}``

        :param ap_model: AP's Name
        :return: return 1 if AP found else -1
        """
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_model in row.text:
                    self.utils.print_info("Found AP Row with Model: ", ap_model)
                    return 1
            self.utils.print_info("Did not find AP")
        else:
            self.utils.print_info("No rows present")
        return -1

    def delete_ap(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Assumes that already navigated to manage --> Devices Page
        - Deletes AP matching either one of serial, name, MAC
        - Keyword Usage:
         - ``Delete AP   ap_serial=${AP_SERIAL}``
         - ``Delete AP   ap_name=${AP_NAME}``
         - ``Delete AP   ap_mac=${AP_MAC}``

        :param ap_serial: ap serial number
        :param ap_name: host name of the AP
        :param ap_mac: ap Mac address
        :return: 1 if deleted else -1
        """
        if ap_serial:
            self.utils.print_info("Deleting AP: ", ap_serial)
            search_result = self.search_ap(ap_serial=ap_serial)

            if search_result:
                if self.select_ap(ap_serial):
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())
                    if self.search_ap_serial(ap_serial=ap_serial) == 1:
                        self.utils.print_info("Unable to find the AP")
                        return -1
                    else:
                        self.utils.print_info("Deleted AP Successfully: ", ap_serial)
                        return 1

        if ap_name:
            self.utils.print_info("Deleting AP: ", ap_name)
            search_result = self.search_ap(ap_name=ap_name)

            if search_result:
                if self.select_ap(ap_name):
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())
                    if self.search_ap_name(ap_name=ap_name) == 1:
                        self.utils.print_info("Unable to find the AP")
                        return -1
                    else:
                        self.utils.print_info("Deleted AP Successfully: ", ap_name)
                        return 1
        if ap_mac:
            self.utils.print_info("Deleting AP: ", ap_mac)
            search_result = self.search_ap(ap_mac=ap_mac)

            if search_result:
                if self.select_ap(ap_mac):
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())
                    if self.search_ap_mac(ap_mac=ap_mac) == 1:
                        self.utils.print_info("Unable to find the AP")
                        return -1
                    else:
                        self.utils.print_info("Deleted AP Successfully: ", ap_mac)
                        return 1
        else:
            self.utils.print_info("Not Found")
            return -1

    def select_ap(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Selects the AP row marching with AP's Serial Number
        - Keyword USage:
         - ``Select AP   ${AP_SERIAL}``

        :param ap_serial: AP's Serial Number
        :param ap_name: host name of the AP
        :param ap_mac: ap Mac address
        :return: return 1 if AP found and selected else -1
        """

        self.refresh_devices_page()
        sleep(10)

        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info("Searching Device Entry with AP Serial : ", ap_serial)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_serial)
            self.screen.save_screen_shot()
            sleep(5)

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_serial:
                    if str(ap_serial) in row.text:
                        self.utils.print_info("Selecting Device with AP Serial: ", ap_serial)
                        self.utils.print_debug("Found AP Row: ", self.format_row(row.text))
                        self.auto_actions.click(self.devices_web_elements.get_ap_select_checkbox(row))
                        sleep(2)
                        return 1

                if ap_name:
                    if str(ap_name) in row.text:
                        self.utils.print_info("Selecting Device with AP Name: ", ap_name)
                        self.utils.print_debug("Found AP Row: ", self.format_row(row.text))
                        self.auto_actions.click(self.devices_web_elements.get_ap_select_checkbox(row))
                        sleep(2)
                        return 1

                if ap_mac:
                    if str(ap_mac) in row.text:
                        self.utils.print_info("Selecting Device with AP MAC: ", ap_mac)
                        self.utils.print_debug("Found AP Row: ", self.format_row(row.text))
                        self.auto_actions.click(self.devices_web_elements.get_ap_select_checkbox(row))
                        sleep(2)
                        return 1
            self.utils.print_info("Did not find specified AP")
        else:
            self.utils.print_info("No rows present")
        return False

    def clear_search_field(self):
        """
        - Clears the search field is necessary
        """
        clear_btn = self.devices_web_elements.get_manage_device_search_clear_button()
        if clear_btn and clear_btn.is_displayed():
            self.utils.print_info("Clicking Clear in Search Field")
            self.auto_actions.click(clear_btn)
        return 1

    def navigate_to_wireless_interface_details(self, ap_name):
        """
        - Assumes that already navigated to the Manage --> Devices
        - Click on the AP Rows host name --> Wireless Interfaces

        :param ap_name: AP's Serial Number
        :return: 1
        """

        self.auto_actions.click(self.devices_web_elements.get_devices_page_grid_ap_name_href(ap_name))
        sleep(5)
        self.auto_actions.click(self.devices_web_elements.get_device_details_wireless_interfaces())
        sleep(5)
        self.auto_actions.move_to_element(
            self.devices_web_elements.get_device_details_wireless_interfaces_surrounding_aps_grid())
        sleep(5)
        return 1

    def get_manage_device_row(self, search_string):
        """
        - Get the device row object from the Manage --> Device page
        - Based on the search string it will search the device row
        - Search string should be device serial, device mac, device host name

        :param search_string: it should be anything which is searched on the row cell
                         example search_string be like device_name, Device Model, Mac Address or Serial number
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting the Device rows from deploy policy page")
        rows = self.devices_web_elements.get_grid_rows()
        if not rows:
            self.utils.print_info(f"Device rows are not available in the manage device page Number")
        for row in rows:
            if search_string in row.text:
                return row
        return False

    def get_device_details(self, search_string, label_str):
        """
        - Gets the device row label value based on the passed label_str
        - Supported label_str are Column headers like IQ ENGINE, POLICY, NTP STATE, MGT IP ADDRESS
        - If the Column is not visible also it will get the value for particular  column header
        - Keyword Usage:
         - ``${POLICY}        Get Device Details    ${AP1_MAC}     POLICY``
         - ``${UPDATED}       Get Device Details    ${AP1_MAC}     UPDATED``
         - ``${MGT_IP_ADDR}   Get Device Details    ${AP1_MAC}     MGT IP ADDRESS``
         - ``${MAC}           Get Device Details    ${AP1_MAC}     MAC``

        :param search_string: string to uniquely identify the row in device grid
        :param label_str: supported labels are Column headers ex: LOCATION, IQ ENGINE, POLICY, NTP STATE, MGT IP ADDRESS
                          MAC, CLIENTS
                      UPTIME, MODEL, SERIAL, UPDATED, MGT VLAN,
        :return: column header value
        """
        label_map = {'LOCATION': 'locationName',
                     'NTP STATE': 'ntp_state',
                     'MGT IP ADDRESS': 'ipAddress',
                     'MAC': 'macAddress',
                     'CLIENTS': 'activeClientCount',
                     'HOST NAME': 'hostname',
                     'MODEL': 'productType',
                     'MAKE': 'make',
                     'UPDATED': 'updatedOn',
                     'UPTIME': 'systemUpTime',
                     'SERIAL': 'serialNumber',
                     'MGT VLAN': 'mgtVlan',
                     'POLICY': 'networkPolicyName',
                     'COUNTRY': 'countryCode',
                     'WIFI0 POWER': 'power24g',
                     'WIFI1 POWER': 'power5g',
                     'WIFI0 CHANNEL': 'channel24g',
                     'WIFI1 CHANNEL': 'channel5g',
                     'WIFI2 POWER': 'power6g',
                     'WIFI2 CHANNEL': 'channel6g',
                     'WIFI0 RADIO PROFILE': 'radioProfile24g',
                     'WIFI1 RADIO PROFILE': 'radioProfile5g',
                     'WIFI2 RADIO PROFILE': 'radioProfile6g',
                     'OS VERSION': 'displayVer',
                     'OS': 'os',
                     'IQAGENT': 'agentVersion',
                     'MANAGED': 'adminState',
                     'MANAGED BY': 'managedBy',
                     'CLOUD CONFIG GROUPS': 'cloudConfigGroups',
                     'WAN IP ADDRESS': 'wanIpAddress',
                     'PUBLIC IP ADDRESS': 'extIpAddress',
                     'DEVICE LICENSE': 'subscriptionLicense'
                     }

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info("Searching Device Entry with Search String : ", search_string)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), search_string)
            self.screen.save_screen_shot()
            sleep(5)

        stale_retry = 1
        while stale_retry <= 10:
            try:
                device_detail_dict = {}
                device_row = self.get_manage_device_row(search_string)
                if device_row:
                    cells = self.devices_web_elements.get_device_row_cells(device_row)
                    for cell in cells:
                        if re.search(r'field-\w*', cell.get_attribute("class")):
                            label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                            if label == "productType":
                                if cell.text:
                                    device_detail_dict[label] = cell.text
                            else:
                                device_detail_dict[label] = cell.text
                    return device_detail_dict[label_map[label_str]]
                else:
                    self.utils.print_info(f"Unable to retrieve device row for {search_string}")
                    self.screen.save_screen_shot()

                    # Break out of the StaleElementReferenceException loop
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return None

    def get_ap_network_policy(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the network policy deployed to the AP
        - Keyword Usage:
         - ``Get Ap Network Policy   ap_serial=${AP_SERIAL}``
         - ``Get Ap Network Policy   ap_name=${AP_NAME}``
         - ``Get Ap Network Policy   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: network policy name applied to the AP
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        network_policy = self.get_device_details(search_string, 'POLICY')
        if network_policy:
            return network_policy

    def check_device_reboot_message(self, device_serial, config_update_option, reboot_message):
        """
        - check device reboot status
        - keyword Usage:
         - ``Check Device Reboot Message   ${DEVICE_SERIAL}   ${CFG_UPDATE_OPT}   ${REBOOT_MSG}``

        :param device_serial:  device serial number
        :param config_update_option: Config update option Delta/Full Config update
        :param reboot_message: Reboot Status Message "Rebooting"
        :return: True If reboot status Message found on device updating Status else False
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Searching Device with Serial: ", device_serial)
        self.auto_actions.send_keys(self.switch_web_elements.get_devices_search_field(), device_serial)

        self.utils.print_info("Clicking Device Search Button")
        self.auto_actions.click(self.switch_web_elements.get_devices_search_button())
        sleep(5)

        self.utils.print_info("Clicking Device Checkbox")
        self.auto_actions.click(self.switch_web_elements.get_devices_select_checkbox_field())
        sleep(2)

        self.utils.print_info("Clicking Update Devices Button For The Device: ", device_serial)
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        if config_update_option == 'delta':
            self.utils.print_info("Clicking Delta Configuration Update Radio Button")
            self.auto_actions.click(self.devices_web_elements.get_delta_config_update_button())
            sleep(1)

        if config_update_option == 'full':
            self.utils.print_info("Clicking Full Configuration Update Radio Button")
            self.auto_actions.click(self.devices_web_elements.get_full_config_update_button())
            sleep(1)

        self.utils.print_info("Clicking Perform update Button")
        self.auto_actions.click(self.devices_web_elements.get_perform_update_button())
        sleep(3)

        count = 0
        while count < 10:
            self.utils.print_info("Checking for For update Configuration Messages")
            if self.devices_web_elements.get_devices_config_update_message():
                config_update_msg = self.devices_web_elements.get_devices_config_update_message().text
                self.utils.print_info(config_update_msg)
                if reboot_message in config_update_msg:
                    self.utils.print_info("Device is Rebooting after update configuration ")
                    return True
            sleep(1)
            count += 1
        self.utils.print_info("Device is not Rebooting after update configuration")
        return False

    def onboard_multiple_devices(self, serials, device_make):
        """
        - This Keyword will Onboard Multiple Devices with Serial Numbers and AP type
        - Keyword Usage:
         - `Onboard Multiple Devices  ${SERIALS}  {AP_TYPE}``

        :param serials: Serial Numbers seperated by comma
        :param ap_type: AP Type ie aerohive,wing
        :return: 1 if on boarded else -1
        """
        if "aerohive" in device_make.lower():
            return self.onboard_ap(serials, device_make)

        if "exos" in device_make.lower():
            return self.onboard_switch_device(serials, device_make)

    def delete_aps(self, ap_serials=None, ap_names=None, ap_macs=None):
        """
        - Assumes that already navigated to Manage --> Devices
        - Delete the multiple AP one by one
        - Keyword Usage:
         - ``Delete APs   ap_serials=${AP1_SERIAL},${AP2_SERIAL}``
         - ``Delete APs   ap_serials=${AP1_SERIAL}``

        :param ap_serials: AP serial number
        :param ap_names: Host name of the AP
        :param ap_macs: MAC of the AP
        :return: 1 if deleted else -1
        """
        aps = -1
        try:
            aps = ap_serials.split(",")
            result = -1

            self.utils.print_info("Delete APs: ", aps)
            for ap in aps:
                result = self.delete_ap(ap_serial=ap.strip())

            return result
        except Exception as e:
            self.utils.print_info("Unable to delete APs: ", aps)
            self.utils.print_info("Exception: ", e)

    def onboard_simulated_device(self, device_model, count=1, location=None, policy=None):
        """
        - onboard multiple simulated devices of same type and returns their serial number(s)
        - Keyword Usage:
         - ``Onboard Simulated Devices  ${DEVICE_TYPE}   count=2``
         - For supported ${DEVICE_TYPE} look the device type drop down in quick add

        :param device_model: device model to onboard
        :param count: number of devices to onboard
        :param location: device location
        :param policy: network policy - optional parameter
        :return: returns the serial number(s) of newly onboarded devices
        """

        self.navigator.navigate_to_devices()

        try:
            prev_serials = self.get_device_serial_numbers(device_model)
            self.utils.print_info("Previously onboarded simulated device serials: ", prev_serials)

            self.utils.print_info("Clicking on ADD button...")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

            self.utils.print_info("Selecting Quick Add Devices menu")
            self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

            self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
            self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

            self.utils.print_info("Selecting Simulated Device Type radio button")
            self.auto_actions.click(self.devices_web_elements.get_quick_onboard_simulated())

            self.auto_actions.click(self.devices_web_elements.get_simulated_devices_dropdown())

            # options = self.devices_web_elements.get_simulated_device_dropdown_options()
            # get table
            table_of_aps = self.devices_web_elements.get_simulated_device_dropdown_table()
            # get all rows in table (of APs)
            options = self.devices_web_elements.get_simulated_device_dropdown_table_rows(table_of_aps)

            for option in options:
                if device_model in option.text:
                    self.utils.print_info("Simulated device option: ", option.text)
                    self.auto_actions.click(option)

            count -= 1
            while count:
                self.auto_actions.click(self.devices_web_elements.get_add_another_device())
                sleep(2)
                count -= 1

            if location:
                self.utils.print_info("Device OS matched")
                self.auto_actions.click(self.devices_web_elements.get_location_button())
                self._select_location(location)

            self.utils.print_info("Clicking on ADD DEVICES button...")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())
            sleep(5)

            cur_serials = self.get_device_serial_numbers(device_model)
            self.utils.print_info("prev ", prev_serials, "cur ", cur_serials)
            new_serials = list(set(cur_serials) - set(prev_serials))
            self.utils.print_info(f"Successfully Onboarded Simulated Device: {device_model} with Serial Number "
                                  f"{new_serials}")
            if len(new_serials) == 1:
                return new_serials[0]
            return new_serials

        except Exception as e:
            self.utils.print_info("Error: ", e)
            self.utils.print_info("Unable to Onboard Simulated Device")
            return -1

    def get_device_serial_numbers(self, device_type):
        """
        - gets all existing devices serials with the same device_type
        - Keyword Usage:
         - Get Device Serial Number   ${DEVICE_TYPE}``

        :param device_type: type of device to onboard
        :return: serial number(s) with same device type
        """
        try:
            # self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
            prev_dev_list = []
            sleep(5)
            rows = self.devices_web_elements.get_grid_rows()
            if rows:
                for row in rows:
                    if device_type in row.text:
                        self.utils.print_info(f"{row.text}")
                        try:
                            cells = self.devices_web_elements.get_device_row_cells(row)
                            self.utils.print_info(f"found cells {len(cells)}")
                        except:
                            self.utils.print_info(f"Could not get Row Cells - {row}")
                            continue
                        device_detail_dict = {}
                        for cell in cells:
                            try:
                                self.utils.print_info(f"pre cell match {cell.text} class="+cell.get_attribute("class"))
                            except:
                                print("cell print error")
                                continue
                            if re.search(r'field-\w*', cell.get_attribute("class")):
                                self.utils.print_info(f"cell match {cell.text}")
                                try:
                                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                                except:
                                    label = 'OOPS'
                                self.utils.print_info(f"got label -- {label}")
                                device_detail_dict[label] = cell.text
                            else:
                                self.utils.print_info(f"missed class match " + cell.get_attribute("class"))
                        res = device_detail_dict.get("serialNumber")
                        prev_dev_list.append(res)
                self.utils.print_info(f"List of Serial Numbers of Devices with device type {device_type}: {prev_dev_list}")
            else:
                self.utils.print_info("No rows present")
            return prev_dev_list
        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info(f"Unable to get Device Serial Numbers with Device Type {device_type}")
            return -1

    def delete_simulated_ap(self, ap_model):
        """
        - Deletes Simulated AP from the device grid based on ap model
        - Keyword Usage:
         - ``Delete Simulated Aps    ${AP_MODEL}``

        :param ap_model: model of the AP
        :return: 1 if deleted successfully else -1
        """
        self.utils.print_info("Deleting AP: ", ap_model)
        search_result = self._search_simulated_devices(ap_model)

        if search_result:
            if self.select_ap(ap_model):
                self.auto_actions.click(self.devices_web_elements.get_delete_button())
                self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())
                if self.search_ap_serial(ap_serial=ap_model) == 1:
                    self.utils.print_info("Unable to find the AP")
                    return -1
                else:
                    self.utils.print_info("Deleted AP Successfully: ", ap_model)
                    return 1

    def _search_simulated_devices(self, ap_serial):
        """
        Searches for AP matching AP's Serial Number

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found
        """
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(5)

        rows = self.devices_web_elements.get_simulated_devices_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info("row data: ", self.format_row(row.text))
                if ap_serial in row.text:
                    return 1
        else:
            return False

    def _assign_network_policy(self, policy_name):
        """
        - This keyword will assign the network policy to the selected devices
        - Assumes that already selected the devices to assign the network policy
        - flow: Actions --> Assign Network Policy -->Select the network policy from drop down window --> Assign
        :param policy_name: policy to be applly
        :return:
        """
        self.utils.print_info("Click on actions button")
        self.auto_actions.click(self.devices_web_elements.get_manage_device_actions_button())
        sleep(3)

        self.utils.print_info("Click on Assign Network policy action")
        self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_combo())
        sleep(4)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_drop_down())
        sleep(5)

        network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
        sleep(2)

        if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
            self.utils.print_info(f"Selected Network policy from drop down:{policy_name}")
        else:
            self.utils.print_info("Network policy is not present in drop down")
            return False

        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Click on network policy assign button")
        self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_button())
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_close_button())
                sleep(5)
                return False
        return True

    def _update_network_policy(self, update_method="Delta"):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices
        :param update_method:  Delta, Complete
        :return:
        """
        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        if update_method == "Delta":
            self.utils.print_info("click on delta config radio button")
            self.auto_actions.click(self.devices_web_elements.get_delta_config_update_button())
            sleep(2)
            self.utils.print_info("click on perform update button")
            self.auto_actions.click(self.devices_web_elements.get_perform_update_button())
            sleep(2)
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for value in tool_tp_text:
                update_tooltip_msg1 = "a device mode change is not supported with a delta configuration update"
                update_tooltip_msg2 = "This change is not supported with a Delta Configuration Update, " \
                                      "you must select a Complete Configuration Update."
                if update_tooltip_msg2 in value or update_tooltip_msg1 in value:
                    self.utils.print_info(value)
                    update_method = "Complete"

        if update_method == "Complete":
            self.utils.print_info("click on complete config radio button")
            self.auto_actions.click(self.devices_web_elements.get_full_config_update_button())
            sleep(2)
            self.utils.print_info("click on perform update button")
            self.auto_actions.click(self.devices_web_elements.get_perform_update_button())
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

    def _check_update_network_policy_status(self, policy_name, device_serial):
        """
        - This keyword is used to check the network policy applied status to the device
        - It will poll the "update status" every 30 seconds to get the status of the network policy applied
        - Assuming that config push will take the maximum five minutes,

        :param device_serial: device serial number to check the config push status
        :return: 1 if config push success else -1
        """
        retry_count = 0
        max_config_push_wait = self.robot_built_in.get_variable_value("${MAX_CONFIG_PUSH_TIME}")
        while True:
            self.utils.print_info(f"Time elapsed for device update: {retry_count} seconds")
            device_update_status = self.get_device_updated_status(device_serial)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                break
            elif retry_count >= int(max_config_push_wait):
                self.utils.print_info(f"Config push to AP taking more than {max_config_push_wait}seconds")
                return -1
            sleep(30)
            retry_count += 30

        policy_applied = self.get_ap_network_policy(ap_serial=device_serial)
        if policy_name.upper() == policy_applied.upper():
            self.utils.print_info("Applied network policy:{}".format(policy_applied))
            return 1
        self.utils.print_info(f"Policy applied:{policy_name} is not matching with policy updated:{policy_applied}")
        return -1

    def assign_and_update_network_policy_to_exos(self, policy_name=None, serial=None, update_method='PolicyAndConfig'):
        """
        - By default this keyword do delta config push
        - Go To MANAGE-->Devices-->Select EXOS SW row  to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - select Switch -->Update device
        - Keyword Usage:
         - ``Assign and Update Network Policy To EXOS   policy_name=${POLICY_NAME}    serial=${SW1_SERIAL}``
         - ``Assign and Update Network Policy To EXOS   policy_name=${POLICY_NAME}    serial=${SW1_SERIAL}  update_method=Complete``
        :param policy_name: name of the network to deploy
        :param serial: serial number of the switch to select
        :param update_method: Perform Complete update or delta update
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Switch row")
        if not self.select_device(serial):
            self.utils.print_info(f"Switch {serial} is not present in the grid")
            return -1
        sleep(2)

        if not self._assign_network_policy(policy_name):
            return -1
        sleep(30)

        return self.update_network_policy_to_exos(serial=serial)

    def update_network_policy_to_exos(self, serial=None, update_method="PolicyAndConfig"):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices
        - Keyword Usage:
        - ``Update Network Policy To Exos      serial=${SW1_SERIAL}     update_method="PolicyAndConfig"``
        :param update_method:
            PolicyAndConfig - selects the "Update Network Policy and Configuration" check button
        :return:  1 if update was performed, -1 if not
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Switch row")
        self.select_device(serial)
        sleep(5)

        # Handle the case where a tooltip / popup is covering the Update Device button
        self.close_last_refreshed_tooltip()

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        pol_config_cb = self.devices_web_elements.get_switch_update_policy_and_config_check_button()
        engine_img_cb = self.devices_web_elements.get_switch_upgrade_engine_and_images_check_button()

        if pol_config_cb is None:
            self.utils.print_info("ERROR: Unable to obtain 'Update Network Policy and Configuration' check button")
            self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
            return -1
        if engine_img_cb is None:
            self.utils.print_info(
                "ERROR: Unable to obtain 'Upgrade IQ Engine and Extreme Network Switch Images' check button")
            self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
            return -1

        # TO DO: Handle the two check buttons to specify the type of update to perform
        if update_method == "PolicyAndConfig":
            self.utils.print_info("Only enable 'Update Network Policy and Configuration' check button")
            # self.auto_actions.enable_check_box(pol_config_cb)
            self.auto_actions.disable_check_box(engine_img_cb)
            sleep(2)

        else:
            self.utils.print_info(f"Unknown update method {update_method}. Please specify 'PolicyAndConfig'")
            self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
            return -1

        # Perform the update
        self.utils.print_info("Click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_perform_update_button())

        self.screen.save_screen_shot()
        sleep(2)

        UpdateStatus = self._check_device_update_status(serial)
        if UpdateStatus == -1:
            device_update_state = self.get_device_updated_status(serial)
            if device_update_state == "Device Update Failed":
                device_row = self.get_manage_device_row(serial)
                ConfigErrorToolTip = self.device_update.get_device_update_form_error(device_row)
                self.utils.print_info("There is a failure during config push")
                return UpdateStatus, ConfigErrorToolTip
        return UpdateStatus

    def update_network_policy_to_ap(self, policy_name=None, ap_serial=None, update_method="Delta"):
        """
        - By default this keyword do delta config push
        - Go To MANAGE-->Devices-->Select AP row  to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - select AP-->Update device
        - Keyword Usage:
         - ``Update Network Policy To Ap   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}``
         - ``Update Network Policy To Ap   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}  update_method=Complete``

        :param policy_name: name of the network to deploy
        :param ap_serial: serial number of the ap to select
        :param update_method: Perform Complete update or delta update
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select ap row")
        if not self.select_ap(ap_serial):
            self.utils.print_info(f"AP {ap_serial} is not present in the grid")
            return -1
        sleep(2)

        if not self._assign_network_policy(policy_name):
            return -1

        self.utils.print_info("Select ap row")
        self.select_ap(ap_serial)

        self._update_network_policy(update_method)
        return self._check_update_network_policy_status(policy_name, ap_serial)

    def update_network_policy_to_multiple_ap(self, policy_name='', ap_serial='', update_method="Delta"):
        """
        - This keyword is used to update/config push the network policy to the multiple AP's
        - By default this keyword do delta config push
        - Procedure:
         - Navigate to the Manage --> Device page
         - Select the multiple AP's rows
         - Click on ACTIONS --> Assign Network Policy --> Select the network policy from drop down --> Assign
         - select the multiple AP's
         - click on UPDATE DEVICES --> Update the delta or complete configuration update based on update method
        - Keyword Usage:
         - ``Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serials=${AP1_SERIAL},${AP2_SERIALS}``
         - ``Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serials=${AP1_SERIAL},${AP2_SERIALS}   update_method=Complete``

        :param policy_name: name of the network to deploy
        :param ap_serial: comma separated ap serial numbers
        :param update_method: Perform Complete update or delta update
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Selecting the device rows")
        for ap_sr in ap_serial.split(','):
            self.select_device(ap_sr)

        if not self._assign_network_policy(policy_name):
            return -1

        self.utils.print_info("Selecting the device rows")
        for ap_sr in ap_serial.split(','):
            self.select_device(ap_sr)

        self._update_network_policy(update_method)
        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        """
        if "Deployed devices successfully." in tool_tip_text:
            return 1
        else:
            return -1
        """
        return 1

    def change_country(self, ap_serial, country):
        """
        - Sets the country code of a AP to selected one.
        - In case of SKU incompatibility, following is an example error we get
        - The region code AH-13ad80 is set for "world", and cannot be changed on an FCC coded device.
        - Keyword Usage:
         - ``Change Country    ${AP1_SERIAL}    ${COUNTRY}``

        :param ap_serial: AP Serial Number
        :param country: Country Code
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Changing country: ", country)
        self.utils.print_info("*****************************")

        self.column_picker_select("Country Code")

        self.refresh_devices_page()

        source_column = self.devices_web_elements.get_country_code_column_header()
        destination_column = self.devices_web_elements.get_network_policy_column_header()
        self.utils.print_info("Source: ", source_column.text)
        self.utils.print_info("Destination: ", destination_column.text)

        self.auto_actions.drag_and_drop_element(source_column, destination_column)

        self.refresh_devices_page()

        if self.select_ap(ap_serial):
            self.utils.print_info("Click on Actions button")
            self.auto_actions.click(self.devices_web_elements.get_manage_device_actions_button())

            self.utils.print_info("Selecting Assign Country Code menu item")
            self.auto_actions.click(self.devices_web_elements.get_actions_country_code_menu_item())
            sleep(5)

            self.utils.print_info("Clicking on Country Code dropdown")
            self.auto_actions.click(self.devices_web_elements.get_actions_country_code_dropdown())
            self.screen.save_screen_shot()
            sleep(2)

            _country = country.replace("_", " ")
            self.utils.print_info("Selecting Country Code: ", _country)
            self.auto_actions.click(self.devices_web_elements.get_actions_country_code_dropdown_option(_country))
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Saving Country Code settings")
            self.auto_actions.click(self.devices_web_elements.get_actions_country_code_save_button())
            sleep(2)

            self.utils.print_info("Confirming AP reboot on Country Code settings...")
            self.auto_actions.click(self.devices_web_elements.get_actions_country_code_confirm_button())
            sleep(2)

            error_msg = self.devices_web_elements.get_actions_country_code_error_message()
            if error_msg:
                self.utils.print_info("Errors: ", error_msg)
                self.auto_actions.click(self.devices_web_elements.get_actions_country_code_close_button())
                sleep(5)
                return -1
        return 1

    def get_ap_flag(self, ap_serial):
        """
        - This method gets the country cell element from Devices page and saves the screenshot of it.
        - Keyword Usage:
         - ``Get AP Flag    ${AP_SERIAL}``

        :param ap_serial: ap serial number
        :return: 1 if flag saved else -1
        """
        flag_cell = -1
        self.refresh_devices_page()

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_serial in row.text:
                    flag_cell = self.devices_web_elements.get_country_code_cell(row)
                    if flag_cell:
                        self.screen.save_screen_shot()
                        self.utils.print_info("Saved the flag successfully")
                        return 1
            self.utils.print_info("Did not find row")
        else:
            self.utils.print_info("No rows present")

        self.utils.print_info("Unable to save the flag")
        return flag_cell

    def get_ap_country(self, ap_serial):
        """
        - This method gets the country name from country cell from Devices page.
        - Keyword Usage:
         - ``Get Ap Country   ${AP_SERIAL}``

        :param ap_serial: serial number of AP
        :return: country name
        """
        flag_cell = -1
        sleep(5)
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if ap_serial in row.text:
                    flag_cell = self.devices_web_elements.get_country_code_cell(row)
                    if flag_cell:
                        return flag_cell.text.replace(" ", "_")
            self.utils.print_info("Did not find row")
        else:
            self.utils.print_info("No rows present")
        return flag_cell

    def reboot_device(self, device_serial):
        """
        - Assumes that already navigated to Manage --> Devices
        - This method reboots a device matching the serial(s)
        - Keyword Usage:
         - ``Reboot Device  ${DEVICE_SERIAL}``

        :param device_serial: device serial number
        :return: None
        """
        self.utils.print_info("Rebooting Device with serial: ", device_serial)

        if self.select_device(device_serial):
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())
            sleep(2)

            self.utils.print_info("Selecting Reboot menu item")
            self.auto_actions.click(self.device_actions.get_device_actions_reboot_menu_item())
            sleep(2)

            self.utils.print_info("Confirming...")
            self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())

            return 1

    def upgrade_device_to_latest_version(self, device_serial):
        """
        - This method update device(s) to latest version from the dropdown
        - Keyword Usage:
         - ``Upgrade Device To Latest Version   ${DEVICE_SERIAL}``

        :param device_serial: serial number(s) of the device(s)
        :return: 1 if success else -1
        """
        latest_version = -1

        if self.select_ap(device_serial):
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click(self.device_update.get_update_devices_button())
            sleep(5)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_iq_engine_checkbox())
            sleep(5)

            self.utils.print_info("Selecting upgrade to latest version checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_to_latest_version_radio())
            sleep(2)

            latest_version = self.device_update.get_latest_version()

            self.utils.print_info("Device Latest Version: ", latest_version)
            sleep(5)

            self.utils.print_info("Selecting Activate After radio button")
            self.auto_actions.click(self.device_update.get_activate_after_radio())

            self.utils.print_info("Setting Activate time to 60 seconds")
            self.auto_actions.send_keys(self.device_update.get_activate_after_textfield(), '60')

            self.utils.print_info("Selecting Perform Update button...")
            self.auto_actions.click(self.device_update.get_perform_update_button())

        return latest_version

    def xiq_upgrade_device_to_latest_version(self, device_serial, action = "perform upgrade"):
        """
        - This method update device(s) to latest version from the XIQ 
        - Keyword Usage:
         - ``XIQ Upgrade Device To Latest Version   ${DEVICE_SERIAL}``
         - xiq_upgrade_device_to_latest_version(device_serial, action = "perform upgrade")

        :param device_serial: serial number(s) of the device(s)
        :return: Latest firmware version if success else -1
        """
        latest_version = -1

        if self.select_ap(device_serial):
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click(self.device_update.get_update_devices_button())
            sleep(5)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_iq_engine_checkbox())
            sleep(5)

            self.utils.print_info("Selecting upgrade to latest version radio button")
            self.auto_actions.click(self.device_update.get_upgrade_to_latest_version_radio())
            sleep(2)

            latest_version = self.device_update.get_latest_version()

            self.utils.print_info("Device Latest Version: ", latest_version)
            sleep(5)

            self.utils.print_info("Selecting Perform upgrade if the versions are the same or "
                                  "upgrading to same version which includes a patch")
            self.auto_actions.click(self.device_update.get_upgrade_even_if_versions_same_checkbox())
            sleep(5)

            if (action == "perform upgrade"):
                self.utils.print_info("Selecting Perform Update button...")
                self.auto_actions.click(self.device_update.get_perform_update_button())

            elif (action == "close"):
                self.utils.print_info("Selecting Cancel and Close button...")
                self.auto_actions.click(self.device_update.get_update_close_button())
            
            else:
                self.utils.print_error("Selected action {action} is unavailable, hence closing the update window...")
                self.auto_actions.click(self.device_update.get_update_close_button())

        return latest_version

    def upgrade_device_to_specific_version(self, device_serial, version=None):
        """
        - This method update device(s) to specific version from the dropdown
        - keyword Usage:
         - ``Upgrade Device To Specific Version    ${DEVICE_SERIAL}   version=${VERSION}``

        :param device_serial: serial number(s) of the device(s)
        :param version: version to which device(s) should get upgraded

        :return: 1 if success
        """
        specific_version = -1

        if self.select_ap(device_serial):
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click(self.device_update.get_update_devices_button())
            sleep(5)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_iq_engine_checkbox())
            sleep(5)

            self.utils.print_info("Selecting upgrade to specific version checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_to_specific_version_radio())
            sleep(2)

            specific_version = self.device_update.get_specific_version()
            sleep(2)

            self.utils.print_info("Device Specific Version: ", specific_version)

            self.utils.print_info("Selecting Activate After radio button")
            self.auto_actions.click(self.device_update.get_activate_after_radio())

            self.utils.print_info("Setting Activate time to 60 seconds")
            self.auto_actions.send_keys(self.device_update.get_activate_after_textfield(), '60')

            self.utils.print_info("Selecting Perform Update button...")
            self.auto_actions.click(self.device_update.get_perform_update_button())

        return specific_version

    def xiq_upgrade_device_to_specific_version(self, device_serial, version=None):
        """
        - This method update device(s) to specific version from the dropdown
        - keyword Usage:
         - ``XIQ Upgrade Device To Specific Version    ${DEVICE_SERIAL}   version=${VERSION}``

        :param device_serial: serial number(s) of the device(s)
        :param version: version to which device(s) should get upgraded

        :return: 1 if success
        """
        specific_version = -1

        if self.select_ap(device_serial):
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click(self.device_update.get_update_devices_button())
            sleep(5)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_iq_engine_checkbox())
            sleep(5)

            self.utils.print_info("Selecting upgrade to specific version radio button")
            self.auto_actions.click(self.device_update.get_upgrade_to_specific_version_radio())
            sleep(2)

            self.utils.print_info("Selecting specific upgrade version Dropdown")
            self.auto_actions.click(self.device_update.get_xiq_upgrade_to_specific_version_dropdown())
            sleep(5)

            self.utils.print_info(f"Selected specific upgrade version as '{version}' from drop down")
            self.auto_actions.click(self.device_update.get_upgrade_to_specific_version_dropdown_options(version))
            sleep(5)

            specific_version = self.device_update.get_exos_specific_version()

            self.utils.print_info("Specific Upgrade Version: ", specific_version)

            self.utils.print_info("Selecting Perform upgrade if the versions are the same or "
                                  "upgrading to same version which includes a patch")
            self.auto_actions.click(self.device_update.get_upgrade_even_if_versions_same_checkbox())
            sleep(5)

            self.utils.print_info("Selecting Perform Update button...")
            self.auto_actions.click(self.device_update.get_perform_update_button())

        return specific_version

    def refresh_devices_page(self):
        """
        - This Keyword will Refresh the Devices Page
        - keyword Usage:
         - ``Refresh Devices Page``

        :return: 1 if device page refreshed successfully else -1
        """

        try:
            self.utils.print_info("Refreshing devices page...")
            self.auto_actions.scroll_up()
            self.clear_search_field()
            self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
            sleep(5)
            return 1
        except Exception as e:
            self.utils.print_info("Unable to refresh devices page. Capturing screenshot")
            self.screen.save_screen_shot()
            return -1

    def edit_ap_description(self, ap_desc, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Edits AP matching either any of either one of serial, name, MAC
        - Keyword Usage:
         - ``Edit Ap Description   ${AP_DESC}   ap_serial=${AP_SERIAL}``

        :param ap_desc: AP's Description
        :param ap_serial: AP Serial
        :param ap_name: AP Name
        :param ap_mac: AP MAC
        :return: 1 if success else -1
        """

        self.utils.print_info("Editing AP: ", ap_serial)
        search_result = self.search_ap(ap_serial=ap_serial)

        if search_result:
            if self.select_ap(ap_serial):
                self.auto_actions.click(self.devices_web_elements.get_edit_button())
                sleep(5)
                self.auto_actions.click(self.devices_web_elements.get_ap_configure_button())
                sleep(2)
                self.auto_actions.click(self.devices_web_elements.get_ap_device_config_tab())
                sleep(2)
                self.auto_actions.send_keys(self.devices_web_elements.get_ap_description_button(), ap_desc)
                sleep(2)
                self.auto_actions.click(self.devices_web_elements.get_save_device_config())
                sleep(2)
                return 1
        return -1

    def onboard_device(self, device_serial, device_make, device_mac=False, device_type="Real", entry_type="Manual",
                       csv_file_name='', device_os=False, location=False, service_tag=False):
        """
        - This keyword on boards an aerohive device [AP or Switch] , Exos Switch and Voss devices using Quick on boarding flow.
        - Keyword Usage:
         - ``Onboard Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}``
         - ``Onboard Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}  device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}``

        :param device_serial: serial number of Device
        :param device_make: Model of the Device ex:aerohive
        :param device_mac: Device MAC
        :param device_type: Real/Simulated
        :param entry_type: Manual/CSV
        :param csv_file_name: CSV File Name
        :param device_os: verifies the Device OS automatically selected after entering device serial
        :param location: device location
        :return:  1 if onboarding success
        :return: -2 for error - Serial numbers entered are from different platform families. Please enter serial numbers that are part of the same platform family. Please remove serial number
        :return: -3 for error - Could not recognize 166A129943554583. Please onboard 166A129943554583 separately.
        :return: -4 for error - No more than 10 serial numbers could be entered at once.
        :return: -5 for error - When onboarding multiple devices, serial numbers must be separated by ", " (Commas).
        :return: -6 for error - The number of MAC Addresses must match the number of Serial Numbers
        :return: -7 for error - Please enter a valid MAC Address
        """
        self.utils.print_info("Onboarding: ", device_make)

        if 'Controllers' in device_make or 'XCC' in device_make:
            return self.onboard_wing_ap(device_serial, device_mac, device_make, location)

        if 'Dual Boot' in device_make:
            return self.onboard_ap(device_serial, device_make, location, device_os)

        self.navigator.navigate_to_devices()

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

        if device_type:
            self.utils.print_info("Selecting Real/Simulated Device Type Dropdown")
            sleep(2)
            self.auto_actions.click(self.devices_web_elements.get_device_type_real_radio_button())

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
        sleep(5)

        if 'Extreme - Aerohive' in device_make:
            if entry_type:
                if 'Manual' in entry_type:
                    self.auto_actions.click(self.devices_web_elements.get_entry_type_manual_radio_button())

                if 'CSV' in entry_type:
                    self.auto_actions.click(self.devices_web_elements.get_entry_type_csv_radio_button())

                if entry_type == "CSV":
                    upload_button = self.devices_web_elements.get_device_entry_csv_upload_button()
                    csv_location = self.custom_file_dir + csv_file_name
                    self.auto_actions.send_keys(upload_button, csv_location)

            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        # Select the 'Device Make' field value and enter the serial number depending on which device type is being added
        if "VOSS" in device_make.upper():
            self.utils.print_info("Selecting Switch Type/Device OS : VOSS")
            try:
                self.auto_actions.click(self.switch_web_elements.get_switch_make_drop_down())
                sleep(2)
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options()
                                                           , "VOSS")
            except Exception as e:
                self.utils.print_debug("Exception: ", e)
                self.auto_actions.click(self.devices_web_elements.get_device_os_voss_radio())

            if entry_type == "CSV":
                if csv_location:
                    upload_button = self.devices_web_elements.get_device_entry_voss_csv_upload_button()
                    if upload_button:
                        self.utils.print_info("Specifying CSV file '" + csv_location + "' for VOSS device")
                        self.auto_actions.send_keys(upload_button, csv_location)
                    else:
                        self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                        self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                        return -1
                else:
                    self.utils.print_info(">>> CSV file was not specified")
                    self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                    self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                    return -1

        if "EXOS" in device_make.upper():
            self.utils.print_info("Selecting Switch Type/Device OS : EXOS")
            try:
                self.auto_actions.click(self.switch_web_elements.get_switch_make_drop_down())
                sleep(2)
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options(), "EXOS")
            except Exception as e:
                self.utils.print_debug("Exception: ", e)
                self.auto_actions.click(self.devices_web_elements.get_device_os_exos_radio())

            if entry_type == "CSV":
                if csv_location:
                    upload_button = self.devices_web_elements.get_device_entry_exos_csv_upload_button()
                    if upload_button:
                        self.utils.print_info("Specifying CSV file '" + csv_location + "' for EXOS device")
                        self.auto_actions.send_keys(upload_button, csv_location)
                    else:
                        self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                        self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                        return -1
                else:
                    self.utils.print_info(">>> CSV file was not specified")
                    self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                    self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                    return -1
            else:
                _errors = self.check_negative_combinations()
                if _errors != 1:
                    return _errors

        if 'Dell' in device_make:
            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)

            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

            self.utils.print_info("Entering Service Tag...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_service_tag_textbox(), service_tag)

        if 'Universal Appliance' in device_make:
            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        if 'XMC' in device_make.upper():
            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        if device_make:
            sleep(5)
            self.utils.print_info("Verifying Device Make...")
            ui_device_make = self.devices_web_elements.get_device_make_dropdownoption().text
            self.utils.print_info("Device Make from UI: ", ui_device_make)
            if device_make in ui_device_make:
                self.utils.print_info("Device Make matched")
            else:
                self.utils.print_info("Device Make NOT matched")

        if location:
            self.auto_actions.click(self.devices_web_elements.get_location_button())
            self._select_location(location)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}"))
                self._exit_here(BuiltIn().get_variable_value("${EXIT_LEVEL}"))

            return -1
        else:
            self.utils.print_info("No Dialog box")

        serials = device_serial.split(",")
        self.utils.print_info("Serials: ", serials)

        for serial in serials:
            if self.search_device_serial(serial) == 1:
                self.utils.print_info(f"Successfully Onboarded {device_make} Device(s) with {serials}")
                return 1
            else:
                return -1

    def onboard_voss_device(self, device_serial, device_type="Real", entry_type="Manual",
                            csv_location='', policy_name=None, loc_name=None):
        """
        - This keyword onboards a VOSS device using Quick on boarding flow.
        - Keyword Usage:
         - ``Onboard VOSS Device  ${DEVICE_SERIAL}``
         - ``Onboard VOSS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}``
         - ``Onboard VOSS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    policy_name=${POLICY_NAME}    loc_name=${LOCATION_NAME}``
         - ``Onboard VOSS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}

        :param device_serial: serial number of Device
        :param device_make: Model of the Device (e.g., voss, etc.)
        :param device_type: Real/Simulated
        :param entry_type: Manual/CSV
        :param csv_location: Absolute Path of Device onboarding CSV File Location on remote Machine
        :param policy_name: Name of the policy to assign to the device (if not specified, policy will not be assigned)
        :param loc_name: Location to assign to the device (if not specified, location will not be assigned)
        :return: 1
        """
        return self.onboard_switch_device(device_serial, "voss", device_type, entry_type, csv_location, policy_name,
                                          loc_name)

    def onboard_exos_device(self, device_serial, device_make="exos", device_type="Real", entry_type="Manual",
                            csv_file_name='', policy_name=None, loc_name=None):
        """
        - This keyword onboards an EXOS device using Quick on boarding flow.
        - Keyword Usage:
         - ``Onboard EXOS Device  ${DEVICE_SERIAL}``
         - ``Onboard EXOS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}``
         - ``Onboard EXOS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    policy_name=${POLICY_NAME}    loc_name=${LOCATION_NAME}``
         - ``Onboard EXOS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}

        :param device_serial: serial number of Device
        :param device_make: Model of the Device (e.g., exos, etc.)
        :param device_type: Real/Simulated
        :param entry_type: Manual/CSV
        :param csv_file_name: Csv File name  from folder testsuites/xiq/functional/onboard_csv_files
        :param policy_name: Name of the policy to assign to the device (if not specified, policy will not be assigned)
        :param loc_name: Location to assign to the device (if not specified, location will not be assigned)
        :return: 1
        """
        self.navigator.navigate_to_devices()

        if 'exos' in device_make.lower():
            self.utils.print_info("Clicking on ADD button...")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

            self.utils.print_info("Selecting Quick Add menu")
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_menu_item())
            self.screen.save_screen_shot()
            sleep(2)

            if device_type:
                self.utils.print_info("Selecting Real/Simulated DEvice Type Dropdown")
                self.auto_actions.click(self.devices_web_elements.get_device_type_dropdown())
                sleep(2)
                self.auto_actions.select_drop_down_options(self.devices_web_elements.get_device_type_drop_down_options()
                                                           , device_type)

            self.utils.print_info("Selecting Device Make as EXOS")
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_device_make_drop_down())
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_device_make_exos_choice())
            sleep(1)

            if entry_type:
                self.utils.print_info("Selecting Entry Type")
                self.auto_actions.click(self.devices_web_elements.get_device_entry_type_drop_down())
                sleep(2)
                self.auto_actions.select_drop_down_options(self.devices_web_elements.
                                                           get_device_entry_type_drop_down_options(), entry_type)
                sleep(2)

            if entry_type == "CSV":
                upload_button = self.devices_web_elements.get_device_entry_exos_csv_upload_button()
                csv_location = self.custom_file_dir + csv_file_name
                self.auto_actions.send_keys(upload_button, csv_location)

            else:
                self.utils.print_info("Entering Serial Number for EXOS device...")
                self.auto_actions.send_keys(self.devices_web_elements.get_devices_exos_serial_text_area(),
                                            device_serial)

            self.screen.save_screen_shot()
            sleep(2)

            if policy_name != None and policy_name != '':
                self.utils.print_info("Selecting policy '" + policy_name + "'")
                self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_policy_drop_down())
                self.auto_actions.select_drop_down_options(
                    self.devices_web_elements.get_devices_quick_add_policy_drop_down_items(),
                    policy_name)

            if loc_name != None and loc_name != '':
                self.utils.print_info("Selecting location '" + loc_name + "'")
                self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_location_field())
                self.location_dialog_select_location(loc_name)
                self.utils.print_info("Clicking Select button")
                self.auto_actions.click(self.device_actions.get_assign_location_select_button())

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Clicking on ADD DEVICES button...")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

            self.screen.save_screen_shot()
            sleep(2)

            tooltip_text = self.dialogue_web_elements.get_tooltip_text()
            sleep(2)

            self.utils.print_info("Checking for Errors...")
            dialog_message = self.dialogue_web_elements.get_dialog_message()

            if dialog_message:
                self.utils.print_info("Dialog Message: ", dialog_message)
                if "Device already onboarded" in dialog_message:
                    self.utils.print_info("Error: ", dialog_message)
                    self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                    self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}"))

                    self._exit_here(BuiltIn().get_variable_value("${EXIT_LEVEL}"))

                return -1
            else:
                self.utils.print_info("No Dialog box")

            serials = device_serial.split(",")
            self.utils.print_info("Serials: ", serials)

            for serial in serials:
                if self.search_device_serial(serial) == 1:
                    self.utils.print_info("Successfully Onboarded EXOS Device(s): ", serials)
                    return 1
                else:
                    return -1

    def onboard_switch_device(self, device_serial, device_make, device_type="Real", entry_type="Manual",
                              csv_location='', policy_name=None, loc_name=None):
        """
        - This keyword onboards a switch device (exos/voss) using Quick on boarding flow.
        - Keyword Usage:
         - ``Onboard Switch Device  ${DEVICE_SERIAL}   EXOS``
         - ``Onboard Switch Device  ${DEVICE_SERIAL}   VOSS``
         - ``Onboard Switch Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    policy_name=${POLICY_NAME}    loc_name=${LOCATION_NAME}``
         - ``Onboard Switch Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}

        :param device_serial: serial number of Device
        :param device_make: Model of the Device (e.g., exos, voss, etc.)
        :param device_type: Real/Simulated
        :param entry_type: Manual/CSV
        :param csv_location: Absolute Path of Device onboarding CSV File Location on remote Machine
        :param policy_name: Name of the policy to assign to the device (if not specified, policy will not be assigned)
        :param loc_name: Location to assign to the device (if not specified, location will not be assigned)
        :return: 1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

        if 'voss' in device_make.lower():
            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)

            if device_make:
                sleep(5)
                self.utils.print_info("Verify Device Make")
                ui_device_make = self.devices_web_elements.get_device_make_dropdownoption().text

                self.utils.print_info("Device Make: ", ui_device_make)
                if 'Select One' in ui_device_make:
                    self.utils.print_info("Device Make not selected automatically")
                    self.auto_actions.click(self.devices_web_elements.get_device_make_dropdownoption())
                    self.auto_actions.select_drop_down_options(
                        self.devices_web_elements.get_device_make_drop_down_options(), device_make)

            if loc_name:
                self.auto_actions.click(self.devices_web_elements.get_location_button())
                self._select_location(loc_name)

        elif 'exos' in device_make.lower():
            self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_device_make_drop_down())
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_device_make_exos_choice())
            sleep(1)

            if entry_type:
                self.utils.print_info("Selecting Entry Type")
                self.auto_actions.click(self.devices_web_elements.get_device_entry_type_drop_down())
                sleep(2)
                self.auto_actions.select_drop_down_options(self.devices_web_elements.
                                                           get_device_entry_type_drop_down_options(), entry_type)
            if entry_type == "CSV":
                if csv_location:
                    upload_button = self.devices_web_elements.get_device_entry_exos_csv_upload_button()
                    if upload_button:
                        self.utils.print_info("Specifying CSV file '" + csv_location + "' for EXOS device")
                        self.auto_actions.send_keys(upload_button, csv_location)
                    else:
                        self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                        self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                        return -1
                else:
                    self.utils.print_info(">>> CSV file was not specified")
                    self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                    self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                    return -1
            else:
                self.utils.print_info("Entering Serial Number for EXOS device...")
                self.auto_actions.send_keys(self.devices_web_elements.get_devices_exos_serial_text_area(),
                                            device_serial)

        else:
            self.utils.print_info(">>> Unsupported device type " + device_make)
            self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
            return -1

        if policy_name != None and policy_name != '':
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_policy_drop_down())
            sleep(2)
            self.screen.save_screen_shot()
            self.auto_actions.select_drop_down_options(self.devices_web_elements.
                                                       get_devices_quick_add_policy_drop_down_items(), policy_name)
            sleep(2)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        self.screen.save_screen_shot()
        sleep(2)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            # self.utils.print_info("MSG_DUPLICATE_DEVICE: ", BuiltIn().get_variable_value('${MSG_DUPLICATE_DEVICE}'))
            # if BuiltIn().get_variable_value('${MSG_DUPLICATE_DEVICE}') in dialog_message:
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}"))

                self._exit_here(BuiltIn().get_variable_value("${EXIT_LEVEL}"))

            return -1
        else:
            self.utils.print_info("No Dialog box")

        serials = device_serial.split(",")
        self.utils.print_info("Serials: ", serials)

        for serial in serials:
            if self.search_device_serial(serial) == 1:
                self.utils.print_info("Successfully Onboarded Device(s): ", serials)
                return 1
            else:
                return -1

    def onboard_xiq_site_engine(self, xiqse_serial):
        """
        - This keyword on boards an XIQ Site Engine using the Quick Add Devices flow.
        - Keyword Usage:
         - ``Onboard XIQ Site Engine  ${XIQSE_SERIAL}

        :param xiqse_serial: serial number of the XIQ Site Engine
        :return: 1
        """
        self.navigator.navigate_to_devices()

        # Access the Quick Add panel
        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add menu")
        self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_menu_item())
        self.screen.save_screen_shot()
        sleep(2)

        # Select 'XMC' from the 'Device Make' field
        self.utils.print_info("Selecting 'XMC' from the 'Device Make' drop down...")
        self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_device_make_drop_down())
        self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_device_make_xmc_choice())
        sleep(1)

        # Enter the XIQ Site Engine's serial number
        self.utils.print_info("Entering Serial Number for XIQ Site Engine...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_xiqse_serial_text_area(), xiqse_serial)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        self.screen.save_screen_shot()
        sleep(2)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}"))

                self._exit_here(BuiltIn().get_variable_value("${EXIT_LEVEL}"))

            return -1
        else:
            self.utils.print_info("No Dialog box")

        serials = xiqse_serial.split(",")
        self.utils.print_info("Serials: ", serials)

        ret_val = 1
        for serial in serials:
            if self.search_device_serial(serial) == 1:
                self.utils.print_info(f"Successfully Onboarded XIQ Site Engine {serial}")
            else:
                self.utils.print_info(f"ERROR: XIQ Site Engine {serial} was not onboarded")
                ret_val = -1
        return ret_val

    def delete_device(self, device_serial=None, device_name=None, device_mac=None):
        """
        - Deletes Device matching either any of either one of serial, name, MAC
        - Keyword Usage:
         - ``Delete Device    device_serial=${DEVICE_SERIAL}``

        :param device_serial: device serial number
        :param device_name: name of the device
        :param device_mac: mac address of the device
        :return: 1 if device deleted successfully or is already deleted/does not exist, else -1
        """

        if device_serial:
            self.utils.print_info("Deleting device: ", device_serial)
            search_result = self.search_device(device_serial=device_serial)

            if search_result != -1:
                if self.select_device(device_serial=device_serial):
                    self.utils.print_info("Click delete button")
                    sleep(2)
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    sleep(2)

                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    sleep(2)
                    self.screen.save_screen_shot()

                    # Wait until the device is removed from the view
                    self.wait_until_device_removed(device_serial=device_serial, retry_duration=10, retry_count=6)

                    # Confirm device was deleted successfully
                    if self.search_device_serial(device_serial) == 1:
                        self.utils.print_info("Unable to delete the device")
                        return -1
                    else:
                        self.utils.print_info("Deleted Device Successfully with Serial: ", device_serial)
                        return 1
            else:
                self.utils.print_info(f"Device with serial {device_serial} does not exist / is already deleted")
                return 1

        if device_name:
            self.utils.print_info("Deleting device: ", device_name)
            search_result = self.search_device(device_name=device_name)

            if search_result != -1:
                if self.select_device(device_name=device_name):
                    self.utils.print_info("Click delete button")
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    sleep(2)

                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    sleep(2)
                    self.screen.save_screen_shot()

                    # Wait until the device is removed from the view
                    self.wait_until_device_removed(device_name=device_name, retry_duration=10, retry_count=6)

                    # Confirm device was deleted successfully
                    if self.search_device_name(device_name) == 1:
                        self.utils.print_info("Unable to delete the device")
                        return -1
                    else:
                        self.utils.print_info("Deleted Device Successfully with Name: ", device_name)
                        return 1
            else:
                self.utils.print_info(f"Device with name {device_name} does not exist / is already deleted")
                return 1

        if device_mac:
            self.utils.print_info("Deleting device: ", device_mac)
            search_result = self.search_device(device_mac=device_mac)

            if search_result != -1:
                if self.select_device(device_mac=device_mac):
                    self.utils.print_info("Click delete button")
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    sleep(2)

                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    sleep(2)
                    self.screen.save_screen_shot()

                    # Wait until the device is removed from the view
                    self.wait_until_device_removed(device_mac=device_mac, retry_duration=10, retry_count=6)

                    # Confirm device was deleted successfully
                    if self.search_device_mac(device_mac) == 1:
                        self.utils.print_info("Unable to delete the device")
                        return -1
                    else:
                        self.utils.print_info("Deleted Device Successfully with Mac: ", device_mac)
                        return 1
            else:
                self.utils.print_info(f"Device with MAC {device_mac} does not exist / is already deleted")
                return 1

        self.utils.print_info("Device was not deleted.  Make sure to specify a serial, name, or MAC")
        return -1

    def delete_devices(self, *device_list):
        """
        - Deletes the list of devices denoted by serial numbers
        - Keyword Usage:
         - ``Delete Devices    ${DEVICE_SERIAL1}  ${DEVICE_SERIAL2}  ${DEVICE_SERIAL3}``

        :param device_list: list of device serial numbers to delete
        :return: 1 if devices deleted successfully or are already deleted/do not exist, else -1
        """
        ret_val = 1

        # Select all the specified devices
        self.utils.print_info("Deleting devices: ", device_list)
        for device_ in device_list:
            if self.select_device(device_):
                self.utils.print_info(f"Selected device {device_}")
            else:
                self.utils.print_info(f"Unable to select device {device_}")
        sleep(2)
        # Now that all devices to delete are selected, perform the delete action
        self.utils.print_info("Click delete button")
        self.auto_actions.scroll_up()
        sleep(2)
        self.auto_actions.click(self.devices_web_elements.get_delete_button())
        sleep(2)

        self.utils.print_info("Click confirmation Yes Button")
        self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
        sleep(2)
        self.screen.save_screen_shot()

        # Confirm devices were deleted successfully
        self.refresh_devices_page()
        for device_ in device_list:
            search_result = self.search_device(device_serial=device_)
            if search_result == 1:
                self.utils.print_info(f"Device {device_} was not deleted")
                ret_val = -1
            else:
                self.utils.print_info(f"Device {device_} was deleted")

        return ret_val

    def delete_device_and_wait(self, device_serial=None, device_name=None, device_mac=None):
        """
        - Deletes the device matching the specified device search parameter and waits until it is removed.
        - Keyword Usage:
         - ``Delete Device and Wait    device_serial=${DEVICE_SERIAL}``
         - ``Delete Device and Wait    device_name=${DEVICE_NAME}``
         - ``Delete Device and Wait    device_mac=${DEVICE_MAC}``

        :param device_serial: serial number of the device to delete
        :param device_name: Name of the device to delete
        :param device_mac: MAC Address of the device to delete
        :return: 1 if device deleted successfully or is already deleted/does not exist, else -1
        """
        ret_val = -1

        # Delete using device serial number
        if device_serial:
            self.utils.print_info(f"Deleting device with serial {device_serial}")
            search_result = self.search_device(device_serial=device_serial)

            if search_result == 1:
                if self.select_device(device_serial=device_serial):
                    self.utils.print_info("Clicking delete button")
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    sleep(2)

                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    sleep(2)

                    # Wait until the device is removed from the view
                    ret_val = self.wait_until_device_removed(device_serial=device_serial)
            else:
                self.utils.print_info(f"Device with serial {device_serial} does not exist / is already deleted")
                ret_val = 1

        # Delete using device name
        elif device_name:
            self.utils.print_info(f"Deleting device with name {device_name}")
            search_result = self.search_device(device_name=device_name)

            if search_result == 1:
                if self.select_device(device_name=device_name):
                    self.utils.print_info("Clicking delete button")
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    sleep(2)

                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    sleep(2)

                    # Wait until the device is removed from the view
                    ret_val = self.wait_until_device_removed(device_name=device_name)

        # Delete using device MAC address
        elif device_mac:
            self.utils.print_info(f"Deleting device with MAC address {device_mac}")
            search_result = self.search_device(device_mac=device_mac)

            if search_result == 1:
                if self.select_device(device_mac=device_mac):
                    self.utils.print_info("Clicking delete button")
                    self.auto_actions.click(self.devices_web_elements.get_delete_button())
                    sleep(2)

                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    sleep(2)

                    # Wait until the device is removed from the view
                    ret_val = self.wait_until_device_removed(device_mac=device_mac)
            else:
                self.utils.print_info(f"Device with MAC address {device_mac} does not exist / is already deleted")
                ret_val = 1

        # Unknown device search parameter
        else:
            self.utils.print_info(
                f"Unknown device search parameter sent; please use Serial Number, Name, or MAC Address")
            ret_val = -1

        if ret_val == -1:
            self.utils.print_info("Device was not deleted - please check")
            self.screen.save_screen_shot()

        return ret_val

    def search_device(self, device_serial=None, device_name=None, device_mac=None):
        """
        - Searches for the device matching either one of serial, name or MAC

        :param device_serial: device Serial
        :param device_name: device Name
        :param device_mac: device MAC
        :return: 1 if device found else -1
        """
        if device_serial:
            self.utils.print_info("Searching device with Serial: ", device_serial)
            return self.search_device_serial(device_serial)
        if device_name:
            self.utils.print_info("Searching device with Name: ", device_name)
            return self.search_device_name(device_name)
        if device_mac:
            self.utils.print_info("Searching device with MAC: ", device_mac)
            return self.search_device_mac(device_mac)

        return -1

    def search_device_serial(self, device_serial):
        """
        - Searches for Device matching Device's Serial Number

        :param device_serial: Device Serial Number
        :return: return 1 if Device found, else -1
        """

        if not device_serial:
            self.utils.print_info("No serial number provided to search for")
            return -1
        else:
            self.utils.print_info(f"Searching for serial number '{device_serial}'")

        sleep(2)
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.devices_web_elements.get_grid_rows()
                if rows:
                    self.utils.print_debug(f"Searching {len(rows)} rows")
                    for row in rows:
                        self.utils.print_info("row data: ", self.format_row(row.text))
                        if device_serial in row.text:
                            self.utils.print_info("Found Device Row: ", self.format_row(row.text))
                            return 1
                    self.utils.print_info(f"Did not find device row with serial {device_serial}")
                    return -1
                else:
                    self.utils.print_info(f"Did not find device row with serial {device_serial} - no rows present")
                    return -1
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return -1

    def search_device_mac(self, device_mac):
        """
        - Searches for device matching device's MAC

        :param device_mac: device's MAC
        :return: return 1 if device found, else -1
        """

        if not device_mac:
            self.utils.print_info("No MAC provided to search for")
            return -1
        else:
            self.utils.print_info(f"Searching for MAC '{device_mac}'")

        sleep(2)
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.devices_web_elements.get_grid_rows()
                if rows:
                    self.utils.print_debug(f"Searching {len(rows)} rows")
                    for row in rows:
                        if device_mac in row.text:
                            self.utils.print_info("Found device Row: ", self.format_row(row.text))
                            return 1
                    self.utils.print_info(f"Did not find device row with MAC address {device_mac}")
                    return -1
                else:
                    self.utils.print_info(f"Did not find device row with MAC address {device_mac} - no rows present")
                    return -1
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return -1

    def search_device_name(self, device_name):
        """
        - Searches for device matching device's NAME

        :param device_name: device's Name
        :return: return 1 if device found, else -1
        """

        if not device_name:
            self.utils.print_info("No device name provided to search for")
            return -1
        else:
            self.utils.print_info(f"Searching for device name '{device_name}'")

        sleep(2)
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.devices_web_elements.get_grid_rows()
                if rows:
                    self.utils.print_debug(f"Searching {len(rows)} rows")
                    for row in rows:
                        if device_name in row.text:
                            self.utils.print_info("Found device Row: ", self.format_row(row.text))
                            return 1
                    self.utils.print_info(f"Did not find device row with name {device_name}")
                    return -1
                else:
                    self.utils.print_info(f"Did not find device row with name {device_name} - no rows present")
                    return -1
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        return -1

    def select_device(self, device_serial=None, device_name=None, device_mac=None):
        """
        - Selects the device matching device's Serial Number,Device Mac address and device mane
        - Keyword Usage:
         - ``Select Device      device_serial=${DEVICE_SERIAL}``
         - ``Select Device      device_name=${DEVICE_NAME}``
         - ``Select Device      device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial
        :param device_name: device host name
        :param device_mac: device MAC address
        :return: return 1 if device found else False
        """
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            if device_serial:
                self.utils.print_info("Selecting Device with serial: ", device_serial)
                for row in rows:
                    if device_serial in row.text:
                        self.utils.print_debug("Found device Row: ", self.format_row(row.text))
                        self.auto_actions.click(self.devices_web_elements.get_device_select_checkbox(row))
                        self.screen.save_screen_shot()
                        sleep(2)
                        return 1

            if device_name:
                self.utils.print_info("Selecting Device with Name: ", device_name)
                for row in rows:
                    if device_name in row.text:
                        self.utils.print_debug("Found device Row: ", self.format_row(row.text))
                        self.auto_actions.click(self.devices_web_elements.get_device_select_checkbox(row))
                        self.screen.save_screen_shot()
                        sleep(2)
                        return 1

            if device_mac:
                self.utils.print_info("Selecting Device with MAC: ", device_mac)
                for row in rows:
                    if device_mac in row.text:
                        self.utils.print_debug("Found device Row: ", self.format_row(row.text))
                        self.auto_actions.click(self.devices_web_elements.get_device_select_checkbox(row))
                        self.screen.save_screen_shot()
                        sleep(2)
                        return 1
        else:
            self.utils.print_info("No rows present")

        self.utils.print_info("Did not find specified row")
        self.screen.save_screen_shot()

        return False

    def get_device_status(self, device_serial='default', device_name='default', device_mac='default'):
        """
        - This keyword returns the device's connection status, audit log status
        - Keyword Usage:
         - ``Get Device Status   device_serial=${DEVICE_SERIAL}``
         - ``Get Device Status   device_name=${DEVICE_NAme}``
         - ``Get Device Status   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial
        :param device_name: device host name
        :param device_mac: device MAC address

        :return:
        - 'green' if device connected and config audit match
        - 'config audit mismatch' if device connected and config audit mismatch
        - 'disconnected' if device disconnected and unable to connect after 10 minutes
        - 'unknown' if device connection status is 'Unknown'

        """
        device_row = -1
        self.refresh_devices_page()

        self.utils.print_info('Getting device Status using')
        if device_serial != 'default':
            self.utils.print_info("Getting status of device with serial: ", device_serial)
            device_row = self.get_device_row(device_serial)

        if device_name != 'default':
            self.utils.print_info("Getting status of device with name: ", device_name)
            device_row = self.get_device_row(device_name)

        if device_mac != 'default':
            self.utils.print_info("Getting status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac)

        if device_row:
            sleep(5)
            device_status = self.devices_web_elements.get_status_cell(device_row)
            audit_config_status = self.devices_web_elements.get_device_config_audit(device_row)
            self.screen.save_screen_shot()
            sleep(2)

            if device_status:
                if "hive-status-true" in device_status:
                    if audit_config_status:
                        if "ui-icon-sprite-match" in audit_config_status:
                            self.utils.print_info("Device Status: Connected, audit status matched")
                            return 'green'
                        if "ui-icon-sprite-mismatch" in audit_config_status:
                            self.utils.print_info("Device Status: Connected, configuration audit status mis matched")
                            return "config audit mismatch"
                    else:
                        self.utils.print_info(
                            "Unable to obtain audit config status for the row - returning connection status 'green'")
                        return 'green'

                if "local-managed-icon" in device_status:
                    self.utils.print_info("Device Status: Connected, locally managed")
                    return 'green'

                if "hive-status-false" in device_status:
                    if self.devices_web_elements.get_device_conn_status_after_ten_min(device_row):
                        self.utils.print_info("Device has not yet established connection after 10 minutes")
                        return "disconnected"
                    return "disconnected"

                if "local-icon" in device_status:
                    self.utils.print_info("Device Status: Disconnected, locally managed")
                    return 'disconnected'

                if "device-status-unknown" in device_status:
                    self.utils.print_info("Device Status: Unknown")
                    return 'unknown'
            else:
                self.utils.print_info("Unable to obtain device status for the device row")
                return -1

        return -1

    def verify_device_status(self, device_serial='default', device_name='default', device_mac='default',
                             status='default'):
        """
        - This keyword returns 1 if device status expected matches the status passed as argument
        - Keyword Usage:
         - ``Verify Device Status   device_serial=${DEVICE_SERIAL}    status=green``
         - ``Verify Device Status   device_name=${DEVICE_NAME}    status=green``
         - ``Verify Device Status   device_mac=${DEVICE_MAC}    status=green``

        :param device_serial: device Serial
        :param device_name: device Name
        :param device_mac: device MAC
        :param status: green, red, or amber as of now - may change in future

        :return:
        """
        if device_serial != 'default':
            if status in self.get_device_status(device_serial):
                return 1
        if device_name != 'default':
            if status in self.get_device_status(device_name):
                return 1
        if device_mac != 'default':
            if status in self.get_device_status(device_mac):
                return 1

    def get_device_row(self, device_serial='default', device_name='default', device_mac='default'):
        """
        - This keyword returns the row of matched device

        :param device_serial: device Serial
        :param device_name: device Name
        :param device_mac: device MAC

        :return: returns the row object
        """
        self.utils.print_info('Getting device row...')

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.devices_web_elements.get_grid_rows()
                if rows:
                    self.utils.print_debug(f"Found {len(rows)} rows")
                    for row in rows:
                        self.utils.print_debug(f"Looking at row {self.format_row(row.text)}")
                        if device_serial != 'default':
                            self.utils.print_debug(f"Looking at Device Serial {device_serial}")
                            if device_serial in row.text:
                                self.utils.print_info("Found device row: ", self.format_row(row.text))
                                return row
                        if device_name != 'default':
                            self.utils.print_debug(f"Looking at Device Name {device_name}")
                            if device_name in row.text:
                                self.utils.print_info("Found device row: ", self.format_row(row.text))
                                return row
                        if device_mac != 'default':
                            self.utils.print_debug(f"Looking at Device MAC {device_mac}")
                            if device_mac in row.text:
                                self.utils.print_info("Found device row: ", self.format_row(row.text))
                                return row
                    # Device row not found in table so break out of the StaleElementException loop
                    break
                else:
                    self.utils.print_debug("No device rows found in grid")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info("Unable to find device row in grid")
        return -1

    def search_device_model(self, device_model):
        """
        - Searches for Device matching Device's name in device grid
        - Keyword Usage:
         - ``Search Device Model  ${DEVICE_MODEL}``

        :param device_model: Device's Name
        :return: return 1 if Device found
        """
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                if device_model in row.text:
                    self.utils.print_info(f"Found Device Row with Model {device_model}")
                    return 1
            self.utils.print_info(f"Did not find row with model {device_model}")
        else:
            self.utils.print_info("No rows present")
        return -1

    def format_row(self, row):
        cell_values = row.split("\n")
        formatted_row = list()
        for cell_value in cell_values:
            formatted_row.append(cell_value)
        return formatted_row

    def update_network_policy_to_router(self, policy_name=None, router_serial=None, update_method="Delta"):
        """
        - Go To MANAGE-->Devices-->Select Device row  to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - select AP-->Update device
        - By default Delta config push will happen
        - Keyword Usage:
         - ``Update Network Policy To Router   policy_name=${POLICY_NAME}``
         - ``Update Network Policy To Router   router_serial=${ROUTER_SERIAL}``

        :param policy_name: name of the network to deploy
        :param router_serial: serial number of the ap to select
        :param update_method: Perform Complete update or delta update
        :return: 1 if policy updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Router row")
        if not self.select_device(router_serial):
            self.utils.print_info("Router {} is not present in the grid".format(router_serial))
            return -1
        sleep(2)

        self.utils.print_info("Click on actions button")
        self.auto_actions.click(self.devices_web_elements.get_manage_device_actions_button())
        sleep(2)

        self.utils.print_info("Click on Assign Network policy action")
        self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_router_combo())
        sleep(2)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_drop_down())
        self.auto_actions.scroll_down()
        sleep(2)

        network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
        policy_status = False
        for item in network_policy_items:
            if policy_name.upper() in item.text.upper():
                self.utils.print_info("Selecting Network policy from drop down")
                self.auto_actions.click(item)
                policy_status = True
                sleep(2)
                break
        if not policy_status:
            self.utils.print_info("Network policy is not present in drop down")
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_cancel_button())

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy assign button")
        self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_button())
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_close_button())
                sleep(5)
                return -2

        self.utils.print_info("Select Device row")
        self.select_device(router_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())

        count = 0
        if update_method == "Delta":
            self.auto_actions.click(self.devices_web_elements.get_delta_config_update_button())
            sleep(2)
            self.auto_actions.click(self.devices_web_elements.get_perform_update_button())
            count = 5
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for value in tool_tp_text:
                if "a device mode change is not supported with a delta configuration update" in value.lower():
                    self.utils.print_info(value)
                    update_method = "Complete"

        if update_method == "Complete":
            self.auto_actions.click(self.devices_web_elements.get_full_config_update_button())
            sleep(2)
            self.auto_actions.click(self.devices_web_elements.get_perform_update_button())
            count = 10

        self.screen.save_screen_shot()
        sleep(2)

        while count > 0:
            policy_applied = self.get_router_network_policy(router_serial=router_serial)
            if policy_name.upper() == policy_applied.upper():
                self.utils.print_info("Applied network policy:{}".format(policy_applied))
                return 1
            count -= 1
        return -1

    def get_router_network_policy(self, router_serial=None, router_name=None, router_mac=None):
        """
        - Get router network policy applied to the router
        - Keyword Usage:
         - ``Get Router Network Policy  router_serial=${ROUTER_SERIAL}``
         - ``Get ROuter Network Policy  router_name=${ROUTER_NAME}``
         - ``Get ROuter Network Policy  router_mac=${ROUTER_MAC}``

        :param router_serial: router serial number
        :param router_name: router host name
        :param router_mac: router mac address
        :return: nw policy applied to the router
        """

        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [router_serial, router_mac, router_name] if value][0]
        nw_policy = self.get_device_details(search_string, 'POLICY')
        if nw_policy:
            return nw_policy

    def get_device_updated_status(self, device_serial='default', device_name='default', device_mac='default'):
        """
        - This keyword returns the device updated status by searching device row using serial, name or mac address
        - Assumes that already navigated to the manage-->device page
        - Keyword Usage:
         - ``Get Device Updated Status   device_serial=${DEVICE_SERIAL}``
         - ``Get Device Updated Status   device_name=${DEVICE_NAME}``
         - ``Get Device Updated Status   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial
        :param device_name: device Name
        :param device_mac: device MAC
        :return: 'updated Time' if the device is updated correctly else return updating status message
        """
        device_row = -1
        self.refresh_devices_page()

        self.utils.print_info('Getting device Updated Status using')
        if device_serial != 'default':
            self.utils.print_info("Getting Updated status of device with serial: ", device_serial)
            device_row = self.get_device_row(device_serial)

        if device_name != 'default':
            self.utils.print_info("Getting Updated status of device with name: ", device_name)
            device_row = self.get_device_row(device_name)

        if device_mac != 'default':
            self.utils.print_info("Getting Updated status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac)

        if device_row:
            sleep(5)
            device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
            self.utils.print_info("Device Updated Status is :", device_updated_status)
            if "Querying" in device_updated_status:
                self.utils.print_info("Device Updating Status: Querying")
                return 'Querying'

            if "IQ Engine Firmware Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: IQ Engine Firmware Updating")
                return 'IQ Engine Firmware Updating'

            if "User Configuration Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: User Configuration Updating")
                return 'User Configuration Updating'

            if "Rebooting" in device_updated_status:
                self.utils.print_info("Device Updating Status: Rebooting")
                return 'Rebooting'

            if "Certification Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: Certification Updating")
                return 'Certification Updating'

            if "Application Signature Downloading" in device_updated_status:
                self.utils.print_info("Device Updating Status: Application Signature Downloading")
                return 'Application Signature Downloading'
            if "Device Update Failed" in device_updated_status:
                self.utils.print_info("Device updating status: Device update failed")
                return 'Device Update Failed'
            else:
                return device_updated_status

    def column_picker_select(self, *columns):
        """
        - This keyword checks the device column picker if it is not checked
        -  Keyword Usage:
         - ``Column Picker Select        Zone   Branch ID   Host Name   Network Policy``
         -``Column Picker Select        Stack Unit``

        :param columns: list of device columns that can be checked
        :return: returns 1 if successful
        """
        ret_val = 1

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)
        self.utils.print_info("Column list to select: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                row_inputs = self.devices_web_elements.get_column_picker_row_input()
                row_input_count = 0
                for row_inp in row_inputs:
                    row_input_count += 1
                    if row_input_count == row_num:
                        ans = row_inp.get_attribute("checked")
                        if ans == "true":
                            self.utils.print_info(f"Column Picker Filter {filter_} is already checked")
                        else:
                            self.auto_actions.click(filter_row)
                            self.utils.print_info(f"Column Picker Filter {filter_} is not already checked - checking")
                        break
            else:
                self.utils.print_info("Unable to select the Column Picker Filter ", filter_)
                ret_val = -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)

        return ret_val

    def column_picker_unselect(self, *columns):
        """
        - This keyword unchecks the device column picker if it is checked
        -  Keyword Usage:
         - ``Column Picker Unselect      Branch ID  Host Name   Cloud Config Groups``
         -``Column Picker Unselect       Network Policy``

        :param columns: list of device columns that can be unchecked
        :return: returns 1 if successful
        """
        ret_val = 1

        self.utils.print_info("Clicking on Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)
        self.utils.print_info("Column list to unselect: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                row_inputs = self.devices_web_elements.get_column_picker_row_input()
                row_input_count = 0
                for row_inp in row_inputs:
                    row_input_count += 1
                    if row_input_count == row_num:
                        ans = row_inp.get_attribute("checked")
                        if ans == "true":
                            self.auto_actions.click(filter_row)
                            self.utils.print_info(f"Column Picker Filter {filter_} is not already unchecked "
                                                  f"- unchecking")
                        else:
                            self.utils.print_info(f"Column Picker Filter {filter_} is already unchecked")
                        break
            else:
                self.utils.print_info("Unable to unselect the Column Picker Filter ", filter_)
                ret_val = -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)

        return ret_val

    def _get_column_picker_filter_exact(self, column):
        """
        This keyword gets the row of matched filter, using an exact match
        :param column: column
        :return: returns the row and row number of matched filter
        """
        rows = self.devices_web_elements.get_column_picker_row()
        filter_row = ""
        row_num = 0
        for row in rows:
            row_num += 1
            if column == row.text:
                self.utils.print_info(f"Column Picker Filter '{column}' is present")
                filter_row = row
                break
        if filter_row == "":
            self.utils.print_info(f"Column Picker Filter '{column}' is not present")
        return filter_row, row_num

    def get_ap_country_cli(self, cli_output):
        """
        - This keyword gets country code of AP from CLI output
        - Keyword Usage:
         - ``Get Ap Country Cli    ${CLI_OUTPUT}``

        :param cli_output: output of show boot-param command
        :return: returns country code
        """
        res = ''.join(re.findall("Country Code.*", cli_output))
        country_code = ''.join(re.findall("[0-9].*", res))
        self.utils.print_info(f"Country Code of AP:{country_code}")
        return country_code

    def delete_all_aps(self):
        """
        - This Keyword will Delete All the Devices in the Manage--> Devices Grid
        - Keyword Usage:
         - ``Delete All Aps``

        :return: 1 if Devices Deleted Successfully else -1
        """

        if self.get_device_count() == 0:
            self.utils.print_info("No devices present in the Devices grid")
            return 1
        else:
            try:
                self.utils.print_info("Waiting for page to refresh...")
                sleep(20)

                # grid = self.devices_web_elements.get_grid()
                self.utils.print_info("Selecting Device grid checkbox...")
                # self.auto_actions.click(self.devices_web_elements.get_ap_select_checkbox(grid))
                self.auto_actions.click(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox())
                sleep(2)

                self.utils.print_info("Clicking Delete button")
                self.auto_actions.click(self.devices_web_elements.get_delete_button())
                sleep(2)

                self.utils.print_info("Confirming delete...")
                self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())
                sleep(2)
                self.screen.save_screen_shot()
                return 1

            except Exception as e:
                self.screen.save_screen_shot()
                self.utils.print_info("Unable to delete devices")
                return -1

    def update_network_policy_to_all_devices(self, policy_name=None, update_method="Delta"):
        """
        - By default this keyword do delta config push
        - Flow: MANAGE-->Devices-->Select All Devices to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - Select All Devices--> Update device
        - Keyword Usage:
         - ``Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}``
         - ``Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}  update_method=Complete``

        :param policy_name: name of the network to deploy
        :param update_method: Perform Complete update or delta update
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select All Devices Checkbox")
        self.auto_actions.click(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox())

        if not self._assign_network_policy(policy_name):
            return -1

        self.utils.print_info("Select All Devices Checkbox")
        self.auto_actions.click(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox())
        sleep(2)

        self._update_network_policy(update_method)
        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Deployed devices successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def get_ap_wifi0_power(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi0 power applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI0 Power   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI0 Power   ap_name=${AP_NAME}``
         - ``Get Ap WIFI0 Power   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Transmission power value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("WiFi0 Power")
        wifi0_power = self.get_device_details(search_string, 'WIFI0 POWER')
        if wifi0_power:
            return wifi0_power

    def get_ap_wifi1_power(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi1 power applied on AP using AP's serial number,Name or Mac address.
        - Flow : Manage ---> Devices
        - Keyword Usage:
         - ``Get Ap WIFI1 Power   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI1 Power   ap_name=${AP_NAME}``
         - ``Get Ap WIFI1 Power   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Transmission power value of wifi1 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        wifi1_power = self.get_device_details(search_string, 'WIFI1 POWER')
        if wifi1_power:
            return wifi1_power

    def get_ap_wifi0_channel(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi0 Channel applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI0 Channel   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI0 Channel   ap_name=${AP_NAME}``
         - ``Get Ap WIFI0 Channel   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Channel value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        wifi0_channel = self.get_device_details(search_string, 'WIFI0 CHANNEL')
        if wifi0_channel:
            return wifi0_channel

    def get_ap_wifi1_channel(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi1 Channel applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI1 Channel   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI1 Channel   ap_name=${AP_NAME}``
         - ``Get Ap WIFI1 Channel   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Channel value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        wifi1_channel = self.get_device_details(search_string, 'WIFI1 CHANNEL')
        if wifi1_channel:
            return wifi1_channel

    def update_override_configuration_to_multiple_devices(self, device_serials='', update_method="Delta"):
        """
        - This keyword uses to update configuration with Multiple devices for Device override configuration.
        - Assumes that Devices already assigned Network Policy and Need to update Device Override Configuration.
        - By default this keyword do delta config push
        - Flow: MANAGE-->Devices-->Select Multiple Devices -->Update Devices
        - Keyword Usage:
         - ``Update Override Configuration To Multiple Devices   device_serials=${AP1_SERIAL},${AP2_SERIAL}``
         - ``Update Override Configuration To Multiple Devices   device_serials=${AP1_SERIAL},${AP2_SERIAL}   update_method=Delta``
         - ``Update Override Configuration To Multiple Devices   device_serials=${AP1_SERIAL},${AP2_SERIAL}   update_method=Complete``

        :param device_serials: device serial  numbers
        :param update_method: Perform Complete update or delta update
        :return: 1 if Devices Updated successfully else -1
        """

        if len(device_serials.split(',')) == 1:
            self.utils.print_info("This keyword works with multiple devices")
            self.utils.print_info("Pass the device serial numbers with comma separated")
            return -1

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Device Serial Checkboxes to Update Configuration ")
        self.device_common.select_device_rows(device_serials)
        self._update_network_policy(update_method)

        """
        tool_tip_text = tool_tip.tool_tip_text

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Deployed devices successfully." in tool_tip_text:
            return 1
        else:
            return -1
        """
        return 1

    def update_override_configuration_to_device(self, device_serial='', update_method="Delta"):
        """
        - This keyword uses to update configuration to the device using Device Serial Number
        - Assume that Device already assigned Network Policy and Need to update Device Override Configuration.
        - By default this keyword do delta config push
        - Flow: MANAGE-->Devices-->Select a Device -->Update Devices
        - Keyword Usage:
         - ``Update Override Configuration To Device   ap_serial=${AP1_SERIAL}``
         - ``Update Override Configuration To Device   ap_serial=${AP1_SERIAL}  update_method=Delta``
         - ``Update Override Configuration To Device   ap_serial=${AP1_SERIAL}  update_method=Complete``

        :param device_serial: device serial number to update the override policy
        :param update_method: Perform Complete update or delta update
        :return: 1 if Device Updated successfully else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Device row")
        if not self.select_device(device_serial):
            self.utils.print_info(f"AP {device_serial} is not present in the grid")
            return -1
        sleep(2)

        self._update_network_policy(update_method)
        tool_tip_text = tool_tip.tool_tip_text

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Deployed devices successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def get_device_count(self):
        """
        - Gets the device count from the Devices grid
        - Keyword Usage:
         - ``Get Device Count``

        :return: returns the number of devices in the table
        """
        device_count = 0
        self.utils.print_info('Getting all device rows...')
        rows = self.devices_web_elements.get_all_device_rows()
        if rows:
            device_count = len(rows)
        self.utils.print_info("Devices count: ", device_count)

        return device_count

    def get_total_device_count(self):
        """
        - Gets the total device count using the "Showing X of Y" label at the top of the view (since more devices
        - may exist than are currently being displayed).
        - Keyword Usage:
         - ``Get Total Device Count``

        :return: returns the total number of devices
        """
        total_count = 0

        total_label = self.devices_web_elements.get_total_count_label()
        if total_label:
            total_str = total_label.text
            self.utils.print_info(f"Got {total_str} from label")
            total_count = int(total_str)
        else:
            self.utils.print_info("Could not find total count label")
        self.utils.print_info(f"Total device count is {total_count}")

        return total_count

    def get_selected_device_count(self):
        """
        - Gets the number of selected devices from the Devices grid
        - Keyword Usage:
         - ``Get Selected Device Count``

        :return: returns the number of selected rows
        """
        sel_count = 0
        self.utils.print_info('Getting all selected device rows...')
        rows = self.devices_web_elements.get_selected_device_rows()
        if rows:
            sel_count = len(rows)
        self.utils.print_info("Selected device count: ", sel_count)

        return sel_count

    def get_deselected_device_count(self):
        """
        - Gets the number of deselected devices from the Devices grid
        - Keyword Usage:
         - ``Get Deselected Device Count``

        :return: returns the number of deselected rows
        """
        desel_count = 0
        self.utils.print_info('Getting all deselected device rows...')
        rows = self.devices_web_elements.get_deselected_device_rows()
        if rows:
            desel_count = len(rows)
        self.utils.print_info("Unselected device count: ", desel_count)

        return desel_count

    def _get_device_column_values(self, field=''):
        """
        - It is used to read the specified column field values
        :param field: device column field values
        :return: return list of field values
        """
        self.refresh_devices_page()
        device_rows = self.devices_web_elements.get_grid_rows()
        if not device_rows:
            self.utils.print_info("Devices grid is empty")
            return -1

        self.utils.print_info(f"Row count is {len(device_rows)}")
        device_column_values = []
        for row in device_rows:
            self.utils.print_debug(f"Row: {row.text}")
            cells = self.devices_web_elements.get_device_row_cells(row)
            for cell in cells:
                self.utils.print_debug(f"Cell: {cell.text}")
                if re.search(field, cell.get_attribute("class")):
                    device_column_values.append(cell.text)
        return device_column_values

    def _sort_device_columns(self, field, direction):
        """
        - sort the device grid column to ascending or descending direction based on the field name
        :param field: column header field name
        :param direction: ascending or descending
        :return: True if sorted based on the direction else False
        """
        # make the column to be visible in the GUI by dragging it to column 8
        if not self.devices_web_elements.get_devices_column_header_cell(field).is_displayed():
            source_el = self.devices_web_elements.get_devices_column_header_cell(field)
            target_el = self.devices_web_elements.get_device_grid_column7()
            self.auto_actions.drag_and_drop_element(source_el, target_el)
            sleep(10)

        click_count = 3
        while click_count > 0:
            self.utils.print_info("Clicking the column header")
            self.auto_actions.click(self.devices_web_elements.get_devices_column_header_cell(field))
            sleep(2)

            sorting_attr = self.devices_web_elements.get_device_column_header_sorting_attr(field)
            self.utils.print_info(f"sorting attributes:{sorting_attr}")
            if direction.upper() == "ASCENDING":
                if "dgrid-sort-up" in sorting_attr:
                    return True
            if direction.upper() == "DESCENDING":
                if "dgrid-sort-down" in sorting_attr:
                    return True
            click_count -= 1
        self.utils.print_info(f"unable to sort the {field}")
        return False

    def _validate_sorting_column_values(self, sorting, gui_unsorted_values, gui_sorted_values):
        """
        - Validating the gui sorted grid values with sorting the gui unsorted values.
        - Check gui sorted values and logic sorted values

        :param sorting: sorting direction "ASCENDING" or "DESCENDING"
        :param gui_unsorted_values: column values before sorting
        :param gui_sorted_values:  sorted values from GUI after sorted from the column header
        :return: list of sorted values
        """
        if sorting.upper() == "ASCENDING":
            gui_unsorted_values.sort()
            sorted_values = gui_unsorted_values

            self.utils.print_info(f"Sorted device grid values from logic:{sorted_values}")
            self.utils.print_info(f"GUI sorted device grid column ascending values:{gui_sorted_values}")
            if sorted_values == gui_sorted_values:
                self.utils.print_info(f"sorted device column values are ascending")
                return gui_sorted_values
            else:
                self.utils.print_info(f"sorted device grid column values are not ascending")
                return -1

        if sorting.upper() == "DESCENDING":
            gui_unsorted_values.sort(reverse=True)
            sorted_values = gui_unsorted_values

            self.utils.print_info(f"Sorted device grid values from logic:{sorted_values}")
            self.utils.print_info(f"GUI sorted device grid descending values:{gui_sorted_values}")
            if sorted_values == gui_sorted_values:
                self.utils.print_info(f"sorted device column values are descending")
                return gui_sorted_values
            else:
                self.utils.print_info(f"sorted device grid column values not are descending")
                return -1

    def sort_device_grid_with_mgmt_ip_address(self, sort="ascending"):
        """
        - This keyword is used to sort up or sort down the device grid with MGMT IP ADDRESS column
        - This sorting apply the all device present in the device grid
        - By default this keyword sort the device grid in ascending order
        - Flow:
         - Navigate to the Device page
         - Click on MGT IP ADDRESS Column to sort up or sort down based on the sorting parameter
        - Keyword Usage:
         - ``Sort Device Grid With Mgmt Ip Address  ascending``
         - ``Sort Device Grid With Mgmt Ip Address  descending``

        :param sort: sorting method i.e ascending, descending
        :return:
        - sorted list values if sorting is matched with GUI sorted the grid values by logic sorted values
         - - Here "logic sorted values" means taking the unsorted device grid values and applying the sort method over those values
        - -1 if  sorting is not matched with GUI sorted the grid values by logic sorted values
        """
        self.navigator.navigate_to_devices()
        self.refresh_devices_page()

        self.utils.print_info("Get unsorted device grid Management IP Address")
        unsorted_values = self._get_device_column_values('field-ipAddress')
        self.utils.print_info(f"Unsorted Management IP Address:{unsorted_values}")

        if self._sort_device_columns('field-ipAddress', sort):
            gui_sorted_values = self._get_device_column_values('field-ipAddress')
            return self._validate_sorting_column_values(sort, unsorted_values, gui_sorted_values)

    def sort_device_grid_with_updated(self, sort="ascending"):
        """
        - This keyword is used to sort ascending(up) or sort descending(down) the device grid with "UPDATED" column
        - This sorting apply the all device present in the device grid
        - By default this keyword sort the device grid in ascending order
        - Flow:
         - Navigate to the Device page
         - Click on "UPDATED" column to sort ascending or sort descending based on the sorting parameter
        - Keyword Usage:
         - ``Sort Device Grid With Updated  ascending``
         - ``Sort Device Grid With Updated  descending``

        :param sort: sorting method i.e ascending, descending
        :return:
        - sorted list values if sorting is matched with GUI sorted grid values with logic sorted values
         - Here "logic sorted values" means taking the unsorted device grid values and applying the sort method over those values
        - -1 if  sorting is not matched with GUI sorted grid values with logic sorted values
        """
        self.navigator.navigate_to_devices()
        self.refresh_devices_page()

        self.utils.print_info("Get unsorted device grid UPDATED column values ")
        unsorted_values = self._get_device_column_values('field-updatedOn')
        self.utils.print_info(f"Unsorted device grid UPDATED column values:{unsorted_values}")

        if self._sort_device_columns('field-updatedOn', sort):
            gui_sorted_values = self._get_device_column_values('field-updatedOn')
            return self._validate_sorting_column_values(sort, unsorted_values, gui_sorted_values)

    def device_reboot(self, device_serial):
        """
        - This keyword is used to reboot the device from Actions --> Reboot
        - Flow:
         - Navigate to Manage --> Devices
         - Select the device row based on the passed device serial number
         - Click on ACTIONS --> Reboot
        - Keyword Usage:
         - ``Device Reboot   ${DEVICE_SERIAL}``

        :param device_serial: device serial number to reboot
        :return: 1
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        self.refresh_devices_page()
        self.select_device(device_serial)

        self.utils.print_info("Click on device actions button")
        self.auto_actions.click(self.devices_web_elements.get_manage_device_actions_button())

        self.utils.print_info("click on device actions reboot button")
        self.auto_actions.click(self.devices_web_elements.get_device_actions_reboot_button())

        self.utils.print_info("Click on reboot confirm yes button")
        self.auto_actions.click(self.devices_web_elements.get_device_actions_reboot_confirm_bttn())
        return 1

    def onboard_wing_ap(self, device_serial, device_mac, device_make, location=False):
        """
        - This keyword on-boards an WiNG device [AP or Switch] using Quick on-boarding flow.
        - Keyword Usage:
         - ``Onboard Ap   ${AP_SERIAL}   ${AP_MAC}``

        :param device_serial: serial number of AP
        :param device_make: Model of the AP i.e WiNG
        :param device_mac: Device MAC
        :param location: Device location
        :return: 1 if on boarded else -1
        """
        self.navigator.navigate_to_devices()

        if self.search_ap_serial(device_serial) == 1:
            self.utils.print_info(f"Device with {device_serial} serial number already onboarded")
            return 1

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)

        _errors = self.check_negative_combinations()
        if _errors != 1:
            return _errors

        if device_make == "XMC":
            self.utils.print_info("Verify Device Make")
            device_make = self.devices_web_elements.get_device_os_radio().text
            self.utils.print_info("Device Make: ", device_make)
            if 'XMC' in device_make:
                self.utils.print_info("Device Make matched")

        if device_make == "wing" or device_make == "Controllers":
            self.utils.print_info("Selecting Device Make Controller")
            self.auto_actions.click(self.devices_web_elements.get_device_make_drop_down())
            sleep(2)

            self.utils.print_info("Selecting Device Make: ", device_make)
            self.auto_actions.select_drop_down_options(self.devices_web_elements.get_device_make_drop_down_options(),
                                                       device_make)

            self.auto_actions.send_keys(self.devices_web_elements.get_wing_devices_mac_text_area(), device_mac)

            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        if location:
            self.auto_actions.click(self.devices_web_elements.get_location_button())
            self._select_location(location)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        _errors = self.check_negative_combinations()
        if _errors != 1:
            return _errors

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -1
            if "A stake record of the device was found in the redirector." in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -2
        else:
            self.utils.print_info("No Errors while onboarding")

        serials = device_serial.split(",")
        self.utils.print_info("Device Serials Numbers: ", serials)

        for serial in serials:
            if self.search_ap_serial(serial):
                self.utils.print_info("Successfully Onboarded Device(s): ", serials)
                return 1
            else:
                return -1

    def get_device_connected_status(self, device_serial):
        """
        - This keyword is used to check the device connected status on XIQ.
        - After Configuring the CAPWAP client server in device cli, check the device connected status
        - This keyword loop over every 30 seconds to check the device connected status
        - This will wait maximum ${XIQ_DEVICE_CONNECT_WAIT} defined in waits.robot to check the device connected status
        - Flow:
         - Navigate to Manage --> Devices
         - check the device status for a device based on passed device serial
        - Keyword Usage:
         - ``Get Device Connected Status   ${DEVICE_SERIAL}``

        :param device_serial: device serial number to check the device connected status
        :return: 1 if device connected within ${XIQ_DEVICE_CONNECT_WAIT} time else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        retry_time = 0
        device_connect_wait = self.robot_built_in.get_variable_value("${XIQ_DEVICE_CONNECT_WAIT}")
        while True:
            self.utils.print_info(f"Time elapsed for device connection {retry_time} seconds")
            self.refresh_devices_page()
            device_row = self.get_device_row(device_serial)
            if "hive-status-true" in self.devices_web_elements.get_status_cell(device_row):
                self.utils.print_info("Device status is connected")
                return 1
            elif "local-managed-icon" in self.devices_web_elements.get_status_cell(device_row):
                self.utils.print_info("Device status is connected - locally managed")
                return 1
            elif retry_time >= int(device_connect_wait):
                self.utils.print_info(f"Device status is disconnected after wait of {device_connect_wait}")
                return -1
            sleep(30)
            retry_time += 30

    def get_device_configuration_audit_status(self, device_serial):
        """
        - This keyword is used to get the device configuration audit status
        - Flow:
         - Navigate to Manage --> Devices  --> Get the configuration audit status under status column of the device row
        - Keyword Usage:
         - ``Get Device Configuration Audit Status    ${DEVICE_SERIAL}``

        :param device_serial: device serial number to check the device configuration audit status
        :return:
        - audit match : if configuration audit matched
        - audit mismatch : if configuration audit mismatch
        - -1 if device not found in the device grid
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        device_row = self.get_device_row(device_serial)

        if device_row:
            audit_config_status = self.devices_web_elements.get_device_config_audit(device_row)
            if "ui-icon-sprite-match" in audit_config_status:
                self.utils.print_info("device configuration audit matched")
                return 'audit match'

            if "ui-icon-sprite-mismatch" in audit_config_status:
                self.utils.print_info("device configuration audit mismatched")
                return "audit mismatch"

        self.utils.print_info(f"device with serial:{device_serial} not found in the device grid rows")
        self.screen.save_screen_shot()
        sleep(2)

        return -1

    def wait_until_device_online(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=10):
        """
        - This keyword is used to check the device connected status on XIQ.
        - After Configuring the CAPWAP client server in device cli, check the device connected status
        - This keyword by default loop over every 30 seconds for 10 times to check the device connected status
        - Flow:
         - Navigate to Manage --> Devices
         - check the device status for a device based on passed device serial
        - Keyword Usage:
         - ``Wait Until Device Online       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12``
         - ``Wait Until Device Online       ${DEVICE_MAC}           retry_duration=15       retry_count=5``

        :param device_serial: device serial number to check the device connected status
        :param device_mac: device mac to check the device connected status
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device connected within time else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        count = 1

        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Device Online Status Check - Loop: ", count)
                    self.utils.print_info(f"Time elapsed for device connection {retry_duration} seconds")
                    self.refresh_devices_page()
                    sleep(2)

                    device_row = None
                    if device_serial:
                        device_row = self.get_device_row(device_serial=device_serial)
                    elif device_mac:
                        device_row = self.get_device_row(device_mac=device_mac)

                    if device_row and device_row != -1:
                        if "hive-status-true" in self.devices_web_elements.get_status_cell(device_row):
                            self.utils.print_info("Device status is connected")
                            return 1
                        elif "local-managed-icon" in self.devices_web_elements.get_status_cell(device_row):
                            self.utils.print_info("Device status is connected - locally managed")
                            return 1
                        else:
                            self.utils.print_info(
                                f"Device status is still Disconnected. Waiting for {retry_duration} seconds")
                            sleep(retry_duration)
                    else:
                        self.utils.print_info(f"Did not find device row. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)
                    count += 1
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info(f"Device failed to come ONLINE. Please check.")
        self.screen.save_screen_shot()
        sleep(2)

        return -1

    def wait_until_device_offline(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=10):
        """
        - This keyword waits until the device status in XIQ is "Disconnected" or "Unknown".
        - After Configuring the CAPWAP client server in device cli, check the device connected status
        - This keyword by default loop over every 30 seconds for 10 times to check the device connected status
        - Flow:
         - Navigate to Manage --> Devices
         - check the device status for a device based on passed device serial
        - Keyword Usage:
         - ``Wait Until Device Offline       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12``
         - ``Wait Until Device Online       ${DEVICE_MAC}           retry_duration=15       retry_count=5``

        :param device_serial: device serial number to check the device connected status
        :param device_mac: device mac to check the device connected status
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device disconnected within time, else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        count = 1

        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Device Offline Status Check - Loop: ", count)
                    self.utils.print_info(f"Time elapsed for device connection {retry_duration} seconds")
                    self.refresh_devices_page()
                    self.screen.save_screen_shot()
                    sleep(2)

                    device_row = None
                    if device_serial:
                        device_row = self.get_device_row(device_serial=device_serial)
                    elif device_mac:
                        device_row = self.get_device_row(device_mac=device_mac)

                    if device_row and device_row != -1:
                        device_status = self.devices_web_elements.get_status_cell(device_row)
                        if "hive-status-false" in device_status:
                            self.utils.print_info("Device status is disconnected")
                            return 1
                        elif "local-icon" in device_status:
                            self.utils.print_info("Device status is disconnected (locally managed)")
                            return 1
                        else:
                            if "device-status-unknown" in device_status:
                                self.utils.print_info(
                                    f"Device Status is Unknown. Waiting for {retry_duration} seconds...")
                            else:
                                self.utils.print_info(
                                    f"Device status is still Connected. Waiting for {retry_duration} seconds...")
                            sleep(retry_duration)
                    else:
                        self.utils.print_info(f"Did not find device row. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)
                    count += 1
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info(f"Device failed to go OFFLINE. Please check.")
        self.screen.save_screen_shot()
        sleep(2)

        return -1

    def update_device_delta_configuration(self, device_serial, update_method="Delta"):
        """
        - This Keyword will Update Device Configuration based on device serial number
        - Keyword Usage:
         - ``Update Device Delta Configuration  ${DEVICE_SERIAL}``
         - ``Update Device Delta Configuration  ${DEVICE_SERIAL}  ${UPDATE_METHOD}=Complete``

        :param device_serial: Device Serial Number
        :param update_method: Delta/Complete
        :return:
        """
        self.utils.print_info("Select Device row")
        self.select_device(device_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())

        if update_method == "Delta":
            self.auto_actions.click(self.devices_web_elements.get_delta_config_update_button())
            sleep(2)
            self.auto_actions.click(self.devices_web_elements.get_perform_update_button())
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for value in tool_tp_text:
                if "a device mode change is not supported with a delta configuration update" in value.lower():
                    self.utils.print_info(value)
                    update_method = "Complete"

        if update_method == "Complete":
            self.auto_actions.click(self.devices_web_elements.get_full_config_update_button())
            sleep(2)
            self.auto_actions.click(self.devices_web_elements.get_perform_update_button())

        self.screen.save_screen_shot()

        return 1

    def wait_until_device_reboots(self, device_serial):
        """
        - This Keyword will wait until device reboots based on device update status message
        - Keyword Usage:
         - `` Wait Until Device Reboots  ${DEVICE_SERIAL}``

        :param device_serial: Device Serial Number
        :return: 1 if Device wait till reboots else -1
        """

        count = 0
        reboot_flag = False
        self.utils.print_info("Checking for update Configuration Messages")
        while count < 10:
            if "Rebooting" in self.get_device_details(device_serial, "UPDATED"):
                self.utils.print_info("Device is rebooting. Waiting for 30 seconds...")
                reboot_flag = True
                sleep(30)
            else:
                if reboot_flag:
                    self.utils.print_info("Device rebooted")
                    return 1
            count += 1

        self.screen.save_screen_shot()

        return -1

    def assign_network_policy_to_switch(self, policy_name, serial):
        """
        - This keyword does a config push for a switch
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - Select Switch-->Update device
        - Keyword Usage:
         - ``Assign Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}``

        :param policy_name: name of the network policy to deploy
        :param serial: serial number of the switch to select
        :return: 1 if policy is assigned, else -1
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info(f"Select switch row with serial {serial}")
        if not self.select_device(serial):
            self.utils.print_info(f"Switch {serial} is not present in the grid")
            return -1
        sleep(2)

        if not self._assign_policy_to_switch(policy_name):
            return -1

        policy_applied = self.get_ap_network_policy(ap_serial=serial)
        if policy_name.upper() == policy_applied.upper():
            self.utils.print_info("Applied network policy:{}".format(policy_applied))
            return 1
        self.utils.print_info(f"Policy applied:{policy_name} is not matching with policy updated:{policy_applied}")
        return -1

    def update_network_policy_to_switch(self, policy_name=None, serial=None, update_method="PolicyAndConfig"):
        """
        - This keyword does a config push for a switch
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - Select Switch-->Update device
        - Keyword Usage:
         - ``Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}``
         - ``Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}  update_method=PolicyAndConfig``
         - ``Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}  update_method=EngineAndImages``
         - ``Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}  update_method=Complete``

        :param policy_name: name of the network policy to deploy
        :param serial: serial number of the switch to select
        :param update_method:
            PolicyAndConfig - selects just the "Update Network Policy and Configuration" check button
            EngineAndImages - selects just the "Upgrade IQ Engine and Extreme Network Switch Images" check button
            Complete        - selects both check buttons
        :return: 1 if policy is updated else -1
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info(f"Select switch row with serial {serial}")
        if not self.select_device(serial):
            self.utils.print_info(f"Switch {serial} is not present in the grid")
            return -1
        sleep(2)

        if not self._assign_policy_to_switch(policy_name):
            return -1

        self.utils.print_info(f"Re-select switch row with serial {serial}")
        self.select_device(serial)

        self._update_switch(update_method)
        return self._check_update_network_policy_status(policy_name, serial)

    def get_ap_assigned_location(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Location Assigned to the AP
        - Keyword Usage:
         - ``Get Ap Assigned Location   ap_serial=${AP_SERIAL}``
         - ``Get Ap Assigned Location   ap_name=${AP_NAME}``
         - ``Get Ap Assigned Location   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Location applied to the AP
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("Location")
        assigned_location = self.get_device_details(search_string, 'LOCATION')
        if assigned_location:
            return assigned_location

    def location_dialog_select_location(self, dev_location='default'):
        """
        - This keyword selects the specified location in the Select Location dialog
        - Keyword Usage:
         - ``Location Dialog Select Location    San Jose, building_01, floor_02``
        :param dev_location: location where the device is to be assigned in the above format
        """
        location_list = dev_location.split(',')
        location_generics = self.device_actions.get_locations_generic()
        location_buildings = self.device_actions.get_locations_building()
        location_floors = self.device_actions.get_locations_floors()

        for location_item in location_list:
            self.utils.print_info("Location items ", location_item)

        for location_generic in location_generics:
            self.utils.print_info("Generic locations on UI:", location_generic.text)

        for location_building in location_buildings:
            self.utils.print_info("Building locations on UI:", location_building.text)

        for location_floor in location_floors:
            self.utils.print_info("Floor locations on UI:", location_floor.text)

        generic_set = False
        building_set = False
        floor_set = False

        for location_item in location_list:

            if not generic_set:
                self.utils.print_info("Selecting Generic location: ", location_item)
                for location_generic in location_generics:
                    if location_item.strip() in location_generic.text:
                        self.utils.print_info("Match found for location type Generic:", location_generic.text)
                        self.auto_actions.click(location_generic)
                        generic_set = True
                        sleep(5)

            if not building_set:
                self.utils.print_info("Selecting Building: ", location_item)
                for location_building in location_buildings:
                    if location_item.strip() in location_building.text:
                        self.utils.print_info("Match found for location type Building:", location_building.text)
                        self.auto_actions.click(location_building)
                        building_set = True
                        sleep(5)

            if not floor_set:
                self.utils.print_info("Selecting Floor: ", location_item)
                for location_floor in location_floors:
                    if location_item.strip() in location_floor.text:
                        self.utils.print_info("Match found for location type Generic:", location_floor.text)
                        self.auto_actions.click(location_floor)
                        floor_set = True
                        sleep(5)

    def update_switch_policy_and_configuration(self, serial):
        """
        - This keyword does a config push for a switch, selecting just the "Update Network Policy and Configuration"
          check button in the Device Update dialog.
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Select Switch-->Update device
        - Keyword Usage:
         - ``Update Switch Policy and Configuration  ${SWITCH_SERIAL}``
        :param serial: serial number of the switch to update
        :return: 1
        """
        self.utils.print_info("Select Switch row")
        self.select_device(serial)

        self._update_switch(update_method="PolicyAndConfig")

        self.screen.save_screen_shot()

        return self._check_device_update_status(serial)

    def update_switch_iq_engine_and_images(self, serial):
        """
        - This keyword does a config push for a switch, selecting just the "Upgrade IQ Engine and Extreme Network
          Switch Images" check button in the Device Update dialog.
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Select Switch-->Update device
        - Keyword Usage:
         - ``Update Switch IQ Engine and Images  ${SWITCH_SERIAL}``

        :param serial: serial number of the switch to update
        :return: 1
        """
        self.utils.print_info("Select Switch row")
        self.select_device(serial)

        self._update_switch(update_method="EngineAndImages")

        self.screen.save_screen_shot()

        return self._check_device_update_status(serial)

    def update_switch_complete(self, serial):
        """
        - This keyword does a config push for a switch, selecting both check buttons in the Device Update dialog.
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Select Switch-->Update device
        - Keyword Usage:
         - ``Update Switch Complete  ${SWITCH_SERIAL}``

        :param serial: serial number of the switch to update
        :return: 1
        """
        self.utils.print_info("Select Switch row")
        self.select_device(serial)

        self._update_switch(update_method="Complete")

        self.screen.save_screen_shot()

        return self._check_device_update_status(serial)

    def _assign_policy_to_switch(self, policy_name):
        """
        - This keyword will assign the network policy to the selected switch
        - Assumes the switches to assign the network policy to are already selected
        - flow: Actions --> Assign Network Policy -->Select the network policy from drop down window --> Assign
        :param policy_name: policy to be applied
        :return:
        """
        self.utils.print_info("Click on actions button")
        self.auto_actions.click(self.devices_web_elements.get_manage_device_actions_button())
        sleep(3)

        self.utils.print_info("Click on Assign Network policy action for selected switch")
        self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_combo_switch())
        sleep(4)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_drop_down())
        sleep(5)

        network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
        sleep(2)

        if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
            self.utils.print_info(f"Selected Network policy from drop down:{policy_name}")
        else:
            self.utils.print_info("Network policy is not present in drop down")
            self.screen.save_screen_shot()
            return False

        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Click on network policy assign button")
        self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_button())
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_close_button())
                sleep(5)
                return False
        return True

    def _update_switch(self, update_method="PolicyAndConfig"):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices
        :param update_method:
            PolicyAndConfig - selects the "Update Network Policy and Configuration" check button
            EngineAndImages - selects the "Upgrade IQ Engine and Extreme Network Switch Images" check button
            Complete        - selects both check buttons
        :return:  1 if update was performed, -1 if not
        """
        # Handle the case where a tooltip / popup is covering the Update Device button
        self.close_last_refreshed_tooltip()

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        pol_config_cb = self.devices_web_elements.get_switch_update_policy_and_config_check_button()
        engine_img_cb = self.devices_web_elements.get_switch_upgrade_engine_and_images_check_button()

        if pol_config_cb is None:
            self.utils.print_info("ERROR: Unable to obtain 'Update Network Policy and Configuration' check button")
            self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
            return -1
        if engine_img_cb is None:
            self.utils.print_info(
                "ERROR: Unable to obtain 'Upgrade IQ Engine and Extreme Network Switch Images' check button")
            self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
            return -1

        # TO DO: Handle the two check buttons to specify the type of update to perform
        # if update_method == "PolicyAndConfig":
        #     self.utils.print_info("Only enable 'Update Network Policy and Configuration' check button")
        #     self.auto_actions.enable_check_box(pol_config_cb)
        #     self.auto_actions.disable_check_box(engine_img_cb)
        #     sleep(2)
        #
        # elif update_method == "EngineAndImages":
        #     self.utils.print_info("Only enable 'Upgrade IQ Engine and Extreme Network Switch Images' check button")
        #     self.auto_actions.disable_check_box(pol_config_cb)
        #     self.auto_actions.enable_check_box(engine_img_cb)
        #     sleep(2)
        #     self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
        #     return -1
        #
        # elif update_method == "Complete":
        #     self.utils.print_info("Enable both check buttons")
        #     self.auto_actions.enable_check_box(pol_config_cb)
        #     self.auto_actions.enable_check_box(engine_img_cb)
        #     sleep(2)
        #     self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
        #     return -1
        #
        # else:
        #     self.utils.print_info(f"Unknown update method {update_method}. Please specify 'PolicyAndConfig', 'EngineAndImages', or 'Complete'")
        #     self.auto_actions.click(self.devices_web_elements.get_device_update_close_button())
        #     return -1

        # Perform the update
        self.utils.print_info("Click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_perform_update_button())

        # In case the warning dialog is displayed about the reboot and revert option being selected, click Yes to close it
        self._handle_reboot_and_revert_warning()

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def _handle_reboot_and_revert_warning(self):
        """
        - Handles the warning dialog when the reboot and revert option is selected in the Device Update dialog
        - by clicking Yes.

        :return:  1 if the dialog is not displayed or the Yes button was clicked successfully;  else, -1
        """
        ret_val = 1

        self.utils.print_info("Check if the Reboot and Revert warning dialog is displayed; if it is, click Yes")
        sleep(5)

        the_dlg = self.devices_web_elements.get_switch_update_reboot_and_revert_warning_dialog()
        if the_dlg:
            self.utils.print_debug("Reboot and Revert warning dialog is displayed")
            yes_btn = self.devices_web_elements.get_switch_update_reboot_and_revert_warning_dialog_yes_button()
            if yes_btn:
                self.utils.print_info("Clicking 'Yes' in the Reboot and Revert warning dialog")
                self.auto_actions.click(yes_btn)
            else:
                self.utils.print_info("Unable to find the Yes button in the Reboot and Revert warning dialog")
                ret_val = -1
        else:
            self.utils.print_debug("Reboot and Revert warning dialog is not displayed")

        return ret_val

    def _check_device_update_status(self, device_serial):
        """
        - This keyword is used to check the status of the device update
        - It will poll the "update status" every 30 seconds
        - Assuming that config push will take a maximum of five minutes
        :param device_serial: device serial number to check the config push status
        :return: 1 if config push success else -1
        """
        retry_count = 0
        while retry_count <= 300:
            device_update_status = self.get_device_updated_status(device_serial)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                break
            elif device_update_status == "Device Update Failed":
                return -1
            elif retry_count == 300:
                self.utils.print_info("Config push to AP taking more than 5 minutes")
                return -1
            sleep(30)
            self.utils.print_info(f"Time elapsed for device update: {retry_count} seconds")
            retry_count += 30
        return 1

    def revert_device_to_template(self, device_serial):
        """
        - Assumes already navigated to Manage --> Devices
        - This method accesses the "Revert Device to Template" action for a device matching the specified serial
        - Keyword Usage:
         - ``Revert Device to Template  ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device to perform the action on
        :return: 1 if action succeeds, else -1
        """
        self.utils.print_info("Reverting Device to Template for device with serial: ", device_serial)

        if self.select_ap(device_serial):
            self.utils.print_info("Selecting 'Actions' button")
            actions_btn = self.device_actions.get_device_actions_button()
            if actions_btn:
                self.auto_actions.click(actions_btn)
                sleep(2)
            else:
                self.utils.print_info("Could not click 'Actions' button")
                return -1

            self.utils.print_info("Selecting 'Revert Device to Template' menu item")
            revert_menu = self.device_actions.get_device_actions_revert_device_to_template_menu_item()
            if revert_menu:
                self.auto_actions.click(revert_menu)
                sleep(2)
            else:
                self.utils.print_info("Could not click 'Revert Device to Template' menu item")
                return -1

            self.utils.print_info("Clicking 'Save' button")
            save_btn = self.dialogue_web_elements.get_confirm_yes_button()
            if save_btn:
                self.auto_actions.click(save_btn)
                sleep(2)
            else:
                self.utils.print_info("Could not click 'Save' button")
                return -1

            self.utils.print_info("Clicking 'Deploy' button")
            deploy_btn = self.dialogue_web_elements.get_confirm_deploy_button()
            if deploy_btn:
                self.auto_actions.click(deploy_btn)
                sleep(2)
            else:
                self.utils.print_info("Could not click 'Deploy' button")
                return -1

            self.utils.print_info("Waiting for device update to complete")
            self._check_device_update_status(device_serial)

            return 1
        else:
            self.utils.print_info("Could not select device with serial ", device_serial)
            return -1

    def confirm_column_picker_contains_column(self, *columns):
        """
        - This keyword confirms the list of columns are all present in the column picker
        - Keyword Usage:
            - `Confirm Column Picker Contains Column  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be present in the column picker list
        :return: returns 1 if all columns are present in the column picker; else, -1
        """
        ret_val = 1

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)
        self.utils.print_info("Column list to check for presence: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                self.utils.print_info(f"Column Picker Filter '{filter_}' is present")
            else:
                self.utils.print_info(f"Column Picker Filter '{filter_}' is not present")
                ret_val = -1
                break

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)

        return ret_val

    def confirm_column_picker_does_not_contain_column(self, *columns):
        """
        - This keyword confirms the list of columns are NOT present in the column picker
        - Keyword Usage:
            - `Confirm Column Picker Does Not Contain Column  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should not be present in the column picker list
        :return: returns 1 if none of the columns are present in the column picker; else, -1
        """
        ret_val = 1

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)
        self.utils.print_info("Column list to check for no presence: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                self.utils.print_info(f"Column Picker Filter '{filter_}' is present")
                ret_val = -1
                break
            else:
                self.utils.print_info(f"Column Picker Filter '{filter_}' is not present")

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)

        return ret_val

    def confirm_column_picker_column_selected(self, *columns):
        """
        - This keyword confirms the list of columns are all selected in the column picker
        - Keyword Usage:
            - `Confirm Column Picker Column Selected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be selected
        :return: returns 1 if all columns are selected in the column picker; else, -1
        """
        ret_val = 1

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)
        self.utils.print_info("Column list to check for selected items: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                row_inputs = self.devices_web_elements.get_column_picker_row_input()
                row_input_count = 0
                for row_inp in row_inputs:
                    row_input_count += 1
                    if row_input_count == row_num:
                        ans = row_inp.get_attribute("checked")
                        if ans == "true":
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is selected")
                        else:
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is not selected")
                            ret_val = -1
                        break
                if ret_val == -1:
                    break
            else:
                self.utils.print_info("Unable to obtain status of the column ", filter_)
                ret_val = -1
                break

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)

        return ret_val

    def confirm_column_picker_column_unselected(self, *columns):
        """
        - This keyword confirms the list of columns are all unselected in the column picker
        - Keyword Usage:
            - `Confirm Column Picker Column Unselected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be selected - passed in as multiple arguments
        :return: returns 1 if all columns are selected in the column picker; else, -1
        """
        ret_val = 1

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)
        self.utils.print_info("Column list to check for unselected items: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                row_inputs = self.devices_web_elements.get_column_picker_row_input()
                row_input_count = 0
                for row_inp in row_inputs:
                    row_input_count += 1
                    if row_input_count == row_num:
                        ans = row_inp.get_attribute("checked")
                        if ans == "true":
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is selected")
                            ret_val = -1
                        else:
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is not selected")
                        break
                if ret_val == -1:
                    break
            else:
                self.utils.print_info("Unable to obtain status of the column ", filter_)
                ret_val = -1
                break

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click(self.devices_web_elements.get_column_picker_icon())
        sleep(2)

        return ret_val

    def select_table_view_type(self, view_type="Default View"):
        """
        - This keyword selects the view type for the Manage> Devices view.
        - Keyword Usage:
            - `Select Table View Type   ${VIEW_TYPE}`

        :param view_type: view type to select (Default View, Wireless View, LAN View, WAN View)
        :return: returns 1 if the specified view type was selected; else, -1
        """
        ret_val = 1

        # Append "View" so the choice will match if the view type was not passed with "View" as a suffix
        self.utils.print_debug("Select Table View Type: ", view_type)
        if not view_type.endswith(" View"):
            view_type += " View"
            self.utils.print_debug("  -- appended ' View' to the view type to be selected: ", view_type)

        view_type_drop_down = self.devices_web_elements.get_devices_table_view_type_drop_down()
        if view_type_drop_down:
            self.utils.print_info("Clicking on Devices Table View Type Selector")
            sleep(5)
            self.auto_actions.click(view_type_drop_down)
            sleep(2)

            drop_down_items = self.devices_web_elements.get_devices_table_view_type_drop_down_items()
            if self.auto_actions.select_drop_down_options(drop_down_items, view_type):
                self.utils.print_info(f"Selected view type '{view_type}' from drop down")
            else:
                self.utils.print_info(f"View type '{view_type}' is not present in drop down")
                self.utils.print_info("Closing Devices Table View Type Selector")
                self.auto_actions.click(view_type_drop_down)
                ret_val = -1
        else:
            self.utils.print_info("Could not find Devices Table View Type Selector")
            ret_val = -1

        return ret_val

    def _assign_network_policy_to_switch(self, policy_name):
        """
        """
        self.utils.print_info("Click on actions button")
        self.auto_actions.click(self.devices_web_elements.get_manage_device_actions_button())
        sleep(3)

        self.utils.print_info("Click on Assign Network policy action")
        self.auto_actions.click(self.devices_web_elements.get_devices_switch_assign_policy())
        sleep(4)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click(self.devices_web_elements.get_devices_switch_assign_policy_dropdown())
        sleep(5)

        network_policy_items = self.devices_web_elements.get_devices_switch_assign_policy_list()
        self.auto_actions.scroll_down()
        sleep(2)

        if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
            self.utils.print_info(f"Selected Network policy from drop down:{policy_name}")
        else:
            self.utils.print_info("Network policy is not present in drop down")
            return False

        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Click on network policy assign button")
        self.auto_actions.click(self.devices_web_elements.get_devices_switch_assign_policy_assign_btn())
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_close_button())
                sleep(5)
                return False
        return True

    def _update_network_policy_to_switch(self):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices
        :param update_method:  Delta, Complete
        :return:
        """
        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        self.utils.print_info("Select the network policy and configuration checkbox")
        update_cb = self.devices_web_elements.get_devices_switch_update_nw_policy()
        if update_cb:
            cb_sel = update_cb.get_attribute("checked")
            if cb_sel and cb_sel != "true":
                self.utils.print_info("Clicking network policy and configuration checkbox")
                self.auto_actions.click(update_cb)
            else:
                self.utils.print_info("Network policy and configuration checkbox is already selected")
        else:
            self.utils.print_info("Could not find network policy and configuration checkbox")
        self.utils.print_info("click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_devices_switch_update_btn())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

    def select_all_devices(self):
        """
        - This keyword selects all devices in the table by clicking the Select All check box column header
        - Keyword Usage:
            - `Select All Devices`

        :param None
        :return: returns 1 if the Select All checkbox was clicked; else, -1
        """
        if self.get_device_count() == 0:
            self.utils.print_info("No devices present in the Devices grid")
            return 1
        else:
            try:
                sel_checked = self.devices_web_elements.get_manage_devices_select_all_devices_checkbox_selected()
                if sel_checked:
                    self.utils.print_info("Select All checkbox already selected")
                else:
                    self.utils.print_info("Clicking Select All checkbox")
                    self.auto_actions.click(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox())
                return 1

            except Exception as e:
                self.screen.save_screen_shot()
                self.utils.print_info("Unable to select all devices")
                return -1

    def deselect_all_devices(self):
        """
        - This keyword deselects all devices in the table by clicking the Select All check box column header to deselect
          it if it is already selected, or clicking the Select All check button twice (once to select all, once to deselect
          all) if it is not already selected.
        - Keyword Usage:
            - `Deselect All Devices`

        :param None
        :return: returns 1 if the action was successful; else, -1
        """
        if self.get_device_count() == 0:
            self.utils.print_info("No devices present in the Devices grid")
            return 1
        else:
            try:
                sel_unchecked = self.devices_web_elements.get_manage_devices_select_all_devices_checkbox_deselected()
                if sel_unchecked:
                    self.utils.print_info("Select All checkbox not already selected - clicking to select all first")
                    self.auto_actions.click(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox())
                self.utils.print_info("Clicking to deselect all devices")
                self.auto_actions.click(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox())
                return 1

            except Exception as e:
                self.screen.save_screen_shot()
                self.utils.print_info("Unable to deselect all devices")
                return -1

    def confirm_devices_selected(self, *device_list):
        """
        - This keyword confirms the list of devices are all selected in the table
        - Keyword Usage:
            - `Confirm Devices Selected  ${SERIAL_1}  ${SERIAL_2}  ${SERIAL_3}`

        :param device_list: list of device serial numbers to check the selection state of
        :return: returns 1 if all specified devices are selected; else, -1
        """
        ret_val = 1

        self.utils.print_info("Device list to check for selection: ", device_list)
        for device_ in device_list:
            device_row = self.get_manage_device_row(device_)
            if device_row:
                if self.devices_web_elements.get_device_row_selection_checkbox_selected(device_row):
                    self.utils.print_info(f"DEVICE {device_} IS SELECTED")
                else:
                    self.utils.print_info(f"DEVICE {device_} IS NOT SELECTED")
                    ret_val = -1
            else:
                self.utils.print_info(f"Unable to obtain selection state for device {device_}")
                ret_val = -1

        return ret_val

    def confirm_devices_deselected(self, *device_list):
        """
        - This keyword confirms the list of devices are all deselected in the table
        - Keyword Usage:
            - `Confirm Devices Deselected  ${SERIAL_1}  ${SERIAL_2}  ${SERIAL_3}`

        :param device_list: list of device serial numbers to check the selection state of
        :return: returns 1 if all specified devices are deselected; else, -1
        """
        ret_val = 1

        self.utils.print_info("Device list to check for deselection: ", device_list)
        for device_ in device_list:
            device_row = self.get_manage_device_row(device_)
            if device_row:
                if self.devices_web_elements.get_device_row_selection_checkbox_deselected(device_row):
                    self.utils.print_info(f"DEVICE {device_} IS DESELECTED")
                else:
                    self.utils.print_info(f"DEVICE {device_} IS NOT DESELECTED")
                    ret_val = -1
            else:
                self.utils.print_info(f"Unable to obtain selection state for device {device_}")
                ret_val = -1

        return ret_val

    def confirm_all_devices_selected(self):
        """
        - This keyword confirms all devices in the table are selected
        - Keyword Usage:
            - `Confirm All Devices Selected`

        :return: returns 1 if all devices are selected; else, -1
        """
        ret_val = 1

        device_count = self.get_device_count()
        selected_device_count = self.get_selected_device_count()
        self.utils.print_debug(f"Total number of devices in table is {device_count}")
        self.utils.print_debug(f"Total number of selected devices in table is {selected_device_count}")
        if device_count != selected_device_count:
            self.utils.print_info("Some devices are not selected")
            ret_val = -1
        else:
            self.utils.print_info("All devices are selected")

        return ret_val

    def confirm_all_devices_deselected(self):
        """
        - This keyword confirms all devices in the table are deselected
        - Keyword Usage:
            - `Confirm All Devices Unselected`

        :return: returns 1 if no devices are selected; else, -1
        """
        ret_val = 1

        device_count = self.get_device_count()
        deselected_device_count = self.get_deselected_device_count()
        self.utils.print_debug(f"Total number of devices in table is {device_count}")
        self.utils.print_debug(f"Total number of deselected devices in table is {deselected_device_count}")
        if device_count != deselected_device_count:
            self.utils.print_info("Some devices are selected")
            ret_val = -1
        else:
            self.utils.print_info("All devices are deselected")

        return ret_val

    def wait_until_device_added(self, device_serial=None, device_name=None, device_mac=None, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to show up in XIQ.
        - This keyword by default loops 10 times every 30 seconds to check if the device exists
        - Flow:
         - Navigate to Manage --> Devices
         - search for the device based on specified device criteria
        - Keyword Usage:
         - ``Wait Until Device Added    device_serial=${DEVICE_SERIAL}    retry_duration=15    retry_count=20``
         - ``Wait Until Device Added    device_name=${DEVICE_NAME}        retry_duration=20    retry_count=15``
         - ``Wait Until Device Added    device_mac=${DEVICE_MAC}          retry_duration=30    retry_count=10``
        :param device_serial: device serial number to look for
        :param device_name: device name to look for
        :param device_mac: device MAC address to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        self.utils.print_info("Navigate to Manage> Devices")
        self.navigator.navigate_to_devices()

        # Search by Serial
        if device_serial:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Serial Number: loop {count}")
                if self.search_device_serial(device_serial) == 1:
                    self.utils.print_info(f"Device with serial {device_serial} has been added")
                    return 1
                else:
                    self.utils.print_info(f"Device with serial {device_serial} is not yet present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                count += 1

        # Search by Name
        elif device_name:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Name: loop {count}")
                if self.search_device_name(device_name) == 1:
                    self.utils.print_info(f"Device with name {device_name} has been added")
                    return 1
                else:
                    self.utils.print_info(
                        f"Device with name {device_name} is not yet present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                count += 1

        # Search by MAC address
        elif device_mac:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by MAC Address: loop {count}")
                if self.search_device_mac(device_mac) == 1:
                    self.utils.print_info(f"Device with MAC {device_mac} has been added")
                    return 1
                else:
                    self.utils.print_info(
                        f"Device with MAC {device_mac} is not yet present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                count += 1

        # Unknown device search parameter
        else:
            self.utils.print_info("Unknown device search parameter sent; please use Serial, Name, or MAC Address")
            return -1

        self.utils.print_info(f"Device does not exist. Please check.")
        return -1

    def wait_until_device_removed(self, device_serial=None, device_name=None, device_mac=None, retry_duration=10,
                                  retry_count=30):
        """
        - This keyword is used to wait for the device to be removed from extauto.xiq.
        - This keyword by default loops 10 times every 30 seconds to check if the device exists
        - Flow:
         - Navigate to Manage --> Devices
         - search for the device based on specified device criteria
        - Keyword Usage:
         - ``Wait Until Device Removed    device_serial=${DEVICE_SERIAL}    retry_duration=15    retry_count=20``
         - ``Wait Until Device Removed    device_name=${DEVICE_NAME}        retry_duration=20    retry_count=15``
         - ``Wait Until Device Removed    device_mac=${DEVICE_MAC}          retry_duration=30    retry_count=10``

        :param device_serial: device serial number to look for
        :param device_name: device name to look for
        :param device_mac: device MAC address to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device removed within time; else -1
        """
        self.utils.print_info("Navigate to Manage> Devices")
        self.navigator.navigate_to_devices()

        # Search by Serial
        if device_serial:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Serial Number: loop {count}")
                if self.search_device_serial(device_serial) == 1:
                    self.utils.print_info(
                        f"Device with serial {device_serial} is still present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                else:
                    self.utils.print_info(f"Device with serial {device_serial} has been removed")
                    return 1
                count += 1

        # Search by Name
        elif device_name:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Name: loop {count}")
                if self.search_device_name(device_name) == 1:
                    self.utils.print_info(
                        f"Device with name {device_name} is still present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                else:
                    self.utils.print_info(f"Device with name {device_name} has been removed")
                    return 1
                count += 1

        # Search by MAC address
        elif device_mac:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by MAC Address: loop {count}")
                if self.search_device_mac(device_mac) == 1:
                    self.utils.print_info(
                        f"Device with MAC {device_mac} is still present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                else:
                    self.utils.print_info(f"Device with MAC address {device_mac} has been removed")
                    return 1
                count += 1

        # Unknown device search parameter
        else:
            self.utils.print_info(
                "Unknown device search parameter sent;  please use either Serial Number or MAC Address")
            return -1

        self.utils.print_info(f"Device still exists in the view. Please check.")
        return -1

    def wait_until_device_managed(self, device_serial, col, retry_duration=30, retry_count=10):
        """
        - This keyword waits until the specified column for the specified device contains managed state.
        - This keyword by default loops every 30 seconds for 10 times to check the column data
        - Flow:
         - Navigate to Manage --> Devices
         - check the specified device column for data
        - Keyword Usage:
         - ``Wait Until Device Data Present  ${DEVICE_SERIAL}    MAC    retry_duration=10    retry_count=12``

        :param device_serial: device serial number to check the device connected status
        :param col: column name to check for data
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if column contains data within the specified time, else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Searching for device: loop {count}")
            col_value = self.get_device_details(device_serial, col)
            if col_value == "Managed":
                self.utils.print_info(f"{col} column contains data: '{col_value}'")
                return 1
            else:
                self.utils.print_info(
                    f"{col} column contains value: '{col_value}'  still not matching..Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.refresh_devices_page()
            count += 1

        self.utils.print_info(f"{col} column for device {device_serial} still does not contain data. Please check.")
        return -1

    def wait_until_device_data_present(self, device_serial, col, retry_duration=30, retry_count=10):
        """
        - This keyword waits until the specified column for the specified device contains data.
        - This keyword by default loops every 30 seconds for 10 times to check the column data
        - Flow:
         - Navigate to Manage --> Devices
         - check the specified device column for data
        - Keyword Usage:
         - ``Wait Until Device Data Present  ${DEVICE_SERIAL}    MAC    retry_duration=10    retry_count=12``

        :param device_serial: device serial number to check the device connected status
        :param col: column name to check for data
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if column contains data within the specified time, else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Searching for device: loop {count}")
            col_value = self.get_device_details(device_serial, col)
            if col_value:
                self.utils.print_info(f"{col} column contains data: '{col_value}'")
                return 1
            else:
                self.utils.print_info(f"{col} column is still empty. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.refresh_devices_page()
            count += 1

        self.utils.print_info(f"{col} column for device {device_serial} still does not contain data. Please check.")
        return -1

    def get_ap_management_ip_address(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get Management IP Assigned to the AP
        - Keyword Usage:
         - ``Get Ap Management IP Address   ap_serial=${AP_SERIAL}``
         - ``Get Ap Management IP Address   ap_name=${AP_NAME}``
         - ``Get Ap Management IP Address   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: AP Management IP Address
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        management_ip = self.get_device_details(search_string, 'MGT IP ADDRESS')
        if management_ip:
            return management_ip

    def confirm_device_disconnected(self, device_serial='default', device_name='default', device_mac='default'):
        """
        - This keyword confirms the device is disconnected
        - Keyword Usage:
         - ``Confirm Device Disconnected   device_serial=${DEVICE_SERIAL}``
         - ``Confirm Device Disconnected   device_name=${DEVICE_NAme}``
         - ``Confirm Device Disconnected   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial
        :param device_name: device host name
        :param device_mac: device MAC address

        :return: 1 if device is currently disconnected, else -1
        """
        ret_val = -1

        device_row = -1
        self.refresh_devices_page()

        if device_serial != 'default':
            self.utils.print_info(f"Getting status of device with serial {device_serial}")
            device_row = self.get_device_row(device_serial)
        elif device_name != 'default':
            self.utils.print_info(f"Getting status of device with name {device_name}")
            device_row = self.get_device_row(device_name)
        elif device_mac != 'default':
            self.utils.print_info(f"Getting status of device with MAC {device_mac}")
            device_row = self.get_device_row(device_mac)
        else:
            self.utils.print_info("Please specify a serial #, device name, or MAC address")

        if device_row:
            sleep(5)
            device_status = self.devices_web_elements.get_status_cell(device_row)
            self.screen.save_screen_shot()
            sleep(2)

            if "hive-status-false" in device_status:
                ret_val = 1
            elif "local-icon" in device_status:
                ret_val = 1

        return ret_val

    def get_device_row_values(self, search_string, col_list):
        """
        - Gets a dictionary of device row values based on the passed column label list
        - The column list should be a comma-separated list of column headers, like HOST NAME,MGT IP ADDRESS,MAC
        - Keyword Usage:
         - ``@{DEVICE_VALUES}=  Get Device Row Values   ${DEVICE_SERIAL}  HOST NAME,MGT IP ADDRESS,MAKE,MODEL``

        :param search_string: string to uniquely identify the row in the device grid
        :param col_list: comma-separated list of column headers (e.g., LOCATION,MAC,MGT IP ADDRESS)
        :return: dictionary containing the values for each of the specified columns
        """
        label_map = {'LOCATION': 'locationName',
                     'NTP STATE': 'ntp_state',
                     'MGT IP ADDRESS': 'ipAddress',
                     'MAC': 'macAddress',
                     'CLIENTS': 'activeClientCount',
                     'HOST NAME': 'hostname',
                     'MODEL': 'productType',
                     'MAKE': 'make',
                     'UPDATED': 'updatedOn',
                     'UPTIME': 'systemUpTime',
                     'SERIAL': 'serialNumber',
                     'MGT VLAN': 'mgtVlan',
                     'POLICY': 'networkPolicyName',
                     'COUNTRY': 'countryCode',
                     'WIFI0 POWER': 'power24g',
                     'WIFI1 POWER': 'power5g',
                     'WIFI0 CHANNEL': 'channel24g',
                     'WIFI1 CHANNEL': 'channel5g',
                     'WIFI0 RADIO PROFILE': 'radioProfile24g',
                     'WIFI1 RADIO PROFILE': 'radioProfile5g',
                     'OS VERSION': 'displayVer',
                     'OS': 'os',
                     'IQAGENT': 'agentVersion',
                     'MANAGED': 'adminState',
                     'MANAGED BY': 'managedBy',
                     'CLOUD CONFIG GROUPS': 'cloudConfigGroups',
                     'WAN IP ADDRESS': 'wanIpAddress',
                     'PUBLIC IP ADDRESS': 'extIpAddress'
                     }

        device_detail_dict = dict()

        device_row = self.get_manage_device_row(search_string)
        if device_row:
            col_labels = col_list.split(",")
            self.utils.print_info("Obtaining data for Column Labels: ", col_labels)

            cells = self.devices_web_elements.get_device_row_cells(device_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    for label_str in col_labels:
                        self.utils.print_debug(f"Getting Data For Column {label_str}")
                        map_value = label_map.get(label_str)
                        self.utils.print_debug(f"Comparing label {label} with map value {map_value}")
                        if label == map_value:
                            if label == "productType":
                                if cell.text:
                                    self.utils.print_debug(f"Got Data {cell.text} For Column {label_str}")
                                    device_detail_dict[label_str] = cell.text
                            else:
                                self.utils.print_debug(f"Got Data {cell.text} For Column {label_str}")
                                device_detail_dict[label_str] = cell.text
                            break
        else:
            self.utils.print_info(f"Could not find device row matching the search parameter {search_string}")

        self.utils.print_info(f"****************** DEVICE ROW VALUES ************************")
        for key, value in device_detail_dict.items():
            self.utils.print_info(f"{key}:{value}")

        return device_detail_dict

    def confirm_no_duplicate_rows(self, search_string):
        """
        - Searches for device rows containing the search_string and confirms only one row exists with the value.
        - This is useful for confirming only one device with a specified MAC Address exists in the table, but
        - should not be used for search strings where multiple rows could contain the same value (e.g., a certain
        - name value, or a serial number which is also used in another row, like CLOUD CONFIG GROUPS in XIQ-SE).

        :param search_string: String to look for in each row
        :return: return 1 if none or only one row with the search string is found (no duplicates);
                 -1 if more than one row contains the search string
        """

        ret_val = 1
        matching_rows = 0
        self.utils.print_info("Getting the Device rows from deploy policy page")
        rows = self.devices_web_elements.get_grid_rows()
        if not rows:
            self.utils.print_info("Device rows are not available in the manage device page")
        else:
            for row in rows:
                if search_string in row.text:
                    matching_rows = matching_rows + 1
                    if matching_rows > 1:
                        ret_val = -1
                        break

        if matching_rows == 0:
            self.utils.print_info(f"No rows contain the value {search_string}")
        elif matching_rows == 1:
            self.utils.print_info(f"Found one row with the value {search_string}")
        else:
            self.utils.print_info(f"Found more then one row with the value {search_string}")

        return ret_val

    def close_last_refreshed_tooltip(self):
        """
        - Closes the "Last Refreshed at:" tooltip by moving the mouse to the element, if it is displayed.
        """
        refresh_tt = self.devices_web_elements.get_last_refreshed_tooltip()
        if refresh_tt:
            if refresh_tt.is_displayed():
                self.utils.print_info("'Last Refreshed at:' tooltip is displayed")
                self.utils.print_info("  -- moving mouse to 'Last Refreshed at:' tooltip element to hide it")
                self.auto_actions.move_to_element(refresh_tt)
            else:
                self.utils.print_debug("'Last Refreshed at:' tooltip is not displayed")
        else:
            self.utils.print_info("Could not find 'Last Refreshed at:' tooltip element")

    def confirm_xiqse_managed_device_not_onboarded_by_xiq(self, device_serial, device_make, location):
        """
        - This keyword attempts to onboard a device which is currently managed by XIQ-SE and confirms the appropriate
        - error is displayed.
        - Keyword Usage:
         - ``Confirm XIQSE Managed Device Not Onboarded By XIQ    ${SERIAL}  ${MAKE}  ${LOCATION"``

        :param device_serial: serial number of Device
        :param device_make: Model of the Device (e.g., aerohive, voss, exos, etc.)
        :param location: Location of the Device (e.g., San Jose, building_01, floor_02)
        :return: 1 if expected error message appears, else -1
        """
        ret_val = 1

        self.navigator.navigate_to_devices()

        # Access the Quick Add panel
        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)

        self.utils.print_info("Selecting Make")
        self.auto_actions.click(self.switch_web_elements.get_switch_make_drop_down())
        sleep(2)
        self.switch_web_elements.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options(),
                                                          device_make)

        if location:
            self.auto_actions.click(self.devices_web_elements.get_location_button())
            self._select_location(location)
        else:
            self.utils.print_info("LOCATION NOT SPECIFIED BUT IS A REQUIRED FIELD")
            return -1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        self.screen.save_screen_shot()
        sleep(2)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message and device_serial in dialog_message:
                self.utils.print_info("Received expected error message 'Device already onboarded'")
                ret_val = 1
            else:
                self.utils.print_info("Did not receive expected message 'Device already onboarded'")
                ret_val = -1
            error_ok = self.dialogue_web_elements.get_dialog_box_ok_button()
            if error_ok:
                self.utils.print_info("Clicking OK button to close error dialog")
                self.auto_actions.click(error_ok)
            else:
                self.utils.print_info("Unable to find OK button to close error dialog")
                self.screen.save_screen_shot()
                ret_val = -1
            sleep(2)
        else:
            self.utils.print_info("No error occurred")
            ret_val = -1

        return ret_val

    def check_tooltip_message_presence(self, tooltip_message):
        """
        - This Keyword will validate whether given Tooltip Message Displayed on Manage--> Devices Page
        - Keyword Usage:
         - ``check tooltip message presence  ${TOOLTIP_MESSAGE}``

        :param tooltip_message: Tooltip message to check on devices page
        :return: 1 if tooltip message appears, else -1
        """
        self.navigator.navigate_to_devices()
        self.refresh_devices_page()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if tooltip_message in tool_tip_text:
            return 1
        else:
            return -1

    def get_ap_wifi0_radio_profile(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi0 Radio Profile applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI0 Radio Profile   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI0 Radio Profile   ap_name=${AP_NAME}``
         - ``Get Ap WIFI0 Radio Profile   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Radio Profile value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("WiFi0 Radio Profile")
        wifi0_radio_profile = self.get_device_details(search_string, 'WIFI0 RADIO PROFILE')
        if wifi0_radio_profile:
            return wifi0_radio_profile

    def get_ap_wifi1_radio_profile(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi1 Radio Profile applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI1 Radio Profile   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI1 Radio Profile   ap_name=${AP_NAME}``
         - ``Get Ap WIFI1 Radio Profile   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Radio Profile value of wifi1 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("WiFi1 Radio Profile")
        wifi1_radio_profile = self.get_device_details(search_string, 'WIFI1 RADIO PROFILE')
        if wifi1_radio_profile:
            return wifi1_radio_profile

    def get_ap_public_ip_address(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get AP Public IP address using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap Public IP Address   ap_serial=${AP_SERIAL}``
         - ``Get Ap Public IP Address   ap_name=${AP_NAME}``
         - ``Get Ap Public IP Address   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Ap Public IP Address
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("Public IP Address")
        ap_public_ip = self.get_device_details(search_string, 'PUBLIC IP ADDRESS')
        if ap_public_ip:
            return ap_public_ip

    def onboard_multiple_exos_switches(self, device_serials, device_make="exos"):
        """
        - This Keyword will Onboard Multiple Exos Devices with Serial Numbers
        - Keyword Usage:
         - `Onboard Multiple Exos Devices  ${SERIAL1},${SERIAL2},${SERIALS3}  {DEVICE_MAKE}``
         - `Onboard Multiple Exos Devices  ${SERIAL1},${SERIAL2},${SERIALS3}``

        :param device_serials: Serial Numbers seperated by comma
        :param device_make: Device Make Type ie EXOS
        :return: 1 if Exos Devices on boarded Successfully else -1
        """
        return self.onboard_switch_device(device_serials, device_make)

    def device_update_progress(self, device_serial='default', retry_duration=30, retry_count=900):
        """
        - This keyword is used to check the status of the device update and also shows device update progress status such as 19%...etc
        - It will poll the "update status" every retry_duration seconds
        - Assuming that config push will take a maximum of fiften minutes

        - Flow:
         - Navigate to Manage --> Devices
         - check the device status and device update prograss for a device based on passed device serial

        - Keyword Usage:
         - `Device Update Progress       ${DEVICE_SERIAL}   retry_duration=30       retry_count=800``

        :param device_serial: device serial number to check the config push status
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: device update status if config push success else -1
        """
        device_updated_status = -1
        device_row, device_update_status = "", ""
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        self.utils.print_info('Getting device Updated Status using')
        if device_serial != 'default':
            self.utils.print_info("Getting Updated status of device with serial: ", device_serial)
            device_row = self.get_device_row(device_serial)

        if device_row:
            count = 0
            while count <= retry_count:
                device_updated_status = self.get_device_updated_status(device_serial)
                self.refresh_devices_page()
                self.utils.print_info("Waiting for page to refresh...")
                sleep(2)
                if re.search(r'\d+-\d+-\d+', device_updated_status):
                    break
                elif device_updated_status == "Device Update Failed.":
                    device_row = self.get_device_row(device_serial)
                    device_updated_status = self.device_update.get_device_update_form_error(device_row)
                    self.utils.print_info("Device Update Failed due to ", device_updated_status)
                    return -1
                sleep(retry_duration)
                self.utils.print_info(f"Time elapsed for device update: {count} seconds")
                count += retry_duration

        return device_updated_status

    def get_stack_status(self, device_mac='default'):
        """
        - This keyword returns the Stack status
        - Keyword Usage:
        - ``Get Stack Status   device_mac=${DEVICE_MAC}``

       :param device_mac: device MAC address

       :return:
       - 'enabled' if stack is connected and enabled properly else 'disabled'

       """
        device_row = -1
        self.refresh_devices_page()

        self.utils.print_info('Getting Stack Status ')

        if device_mac != 'default':
            self.utils.print_info("Getting status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac)
        
        if device_row:
            sleep(5)
            stack_status = self.devices_web_elements.get_stack_status_cell(device_row)
            self.screen.save_screen_shot()
            sleep(2)

            if stack_status:
                if "ui-icon-stack" in stack_status:
                    return "enabled"
                else:
                    return "disabled"
            else:
                self.utils.print_info("Could not get Stack status")


    def get_exos_stack_status(self, device_mac='default'):
        """
        - This keyword returns the EXOS Stack icon status is blue or red 
        - 'blue' means all the stack members are in managed state
        - 'red' means one or more slot is not in managed state
        - '-1' means the device is not a stack device
        - Keyword Usage:
        - ``Get Exos Stack Status   device_mac=${DEVICE_MAC}``

       :param device_mac: device MAC address

       :return:
       - 'blue' if all the stack members are in managed state else 'red'
       - '-1' if the stack icon is not in the device row

       """
        device_row = -1
        self.refresh_devices_page()

        self.utils.print_info('Getting Stack Status ')

        if device_mac != 'default':
            self.utils.print_info("Getting status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac)

        if device_row:
            sleep(5)
            stack_status = self.devices_web_elements.get_stack_status_cell_icon(device_row)
            self.screen.save_screen_shot()
            sleep(2)

            if stack_status:
                if "ui-icon-stack-warning" in stack_status:
                    return "red"
                elif "ui-icon-stack" in stack_status:
                    return "blue"
            else:
                self.utils.print_error("Could not get stack status")
                return -1
        else:
            return -1


    def verify_stack_devices_managed(self, stack_mac, slot_serial_list):
        """
        - This keyword waits until the specified column for the specified device contains managed state.
        - This keyword by default loops every 30 seconds for 10 times to check the column data
        - Flow:
         - Navigate to Manage --> Devices
         - check the specified device column for data
        - Keyword Usage:
         - ``Verify Stack Devices Managed  ${STACK_MAC}  ${SLOT_SERIAL_LIST} ``

        :param stack_mac: stack mac in use with which stack is onboarded
        :param slot_serial_list: list of serial numbers of stack devices to check the devices managed status
        :param col: column name to check for data
        :return: 1 if column contains data within the specified time, else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        self.utils.print_info("Search Stack row")
        stack_row = self.get_device_row(device_mac=stack_mac)

        if stack_row:
            sleep(5)
            self.utils.print_info("Click on stack icon")
            self.auto_actions.click(self.devices_web_elements.get_stack_status_icon(stack_row))
            self.screen.save_screen_shot()

        slot_rows = self.devices_web_elements.get_devices_page_stack_slot_rows(stack_row)
        if slot_rows:
            self.utils.print_info(f"Stack Slot Rows Found..")
        count = 0
        self.utils.print_info(f"Searching for slot entry in stack")
        for serial in slot_serial_list:
            row_found = 0
            for row in slot_rows:
                if serial in row.text:
                    self.utils.print_info(f"Found Slot row of Serial '{serial}' :  '{row.text}'")
                    row_found = 1
                    if 'Managed' in row.text:
                        self.utils.print_info(f"Slot with Serial number '{serial}' is Managed state..")
                        count += 1
                    else:
                        self.utils.print_info(f"Slot with Serial number '{serial}' is NOT in Managed state")
            if not row_found:
                self.utils.print_info(f"Slot with Serial number '{serial}' is NOT FOUND")

        self.refresh_devices_page()
        self.screen.save_screen_shot()

        if count == len(slot_serial_list):
            self.utils.print_info(f"All the Slots are in Managed state")
            return 1
        else:
            return -1

    def update_device_using_hostname(self, device_name):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices
        - Keyword Usage:
        - ``Update Device Using Hostname    name=${SW_HOST}     '`
        :param update_method:
            PolicyAndConfig - selects the "Update Network Policy and Configuration" check button
        :return:  1 if update was performed, -1 if not
        """
        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        # Perform the update
        self.utils.print_info("Click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_perform_update_button())

        self.screen.save_screen_shot()
        sleep(2)

        return self._check_device_update_status(device_name)

    def update_network_policy_to_stack(self, device_mac, policy_name, template_policy_name):
        """
        - Update the network policy to the selected stack devices
        - Keyword Usage:
        - ``Update Network Policy To Stack      device_mac  policy_name template_policy_name
        :param: device_mac Device master MAC
        :param: policy_name Name of policy
        :param: template_policy_name Name of template
        :return:  1 if update was performed, -1 if not
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        if not self.select_device(device_mac=device_mac):
            self.utils.print_info(f"Switch {device_mac} is not present in the grid")
            return -1
        sleep(2)

        if not self._assign_network_policy(policy_name):
            return -1
        sleep(30)

        self.utils.print_info("Select Switch row")
        self.select_device(device_mac=device_mac)
        sleep(5)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())
        sleep(2)

        # Select from dropdown
        if template_policy_name is not None:
            click_dropdown = self.devices_web_elements.get_devices_stack_update_policy_dropdown_btn()
            if click_dropdown:
                self.utils.print_info(f" Click on dropdown ")
                self.auto_actions.click(click_dropdown)
            else:
                self.utils.print_info(f" Not able to find dropdown  ")
            dropdown_items = self.devices_web_elements.get_devices_stack_update_policy_dropdown_items()
            if dropdown_items:
                self.utils.print_info(f" The templates from dropdown are: ")
                for elem in dropdown_items:
                    self.utils.print_info(elem.text)
                for el in dropdown_items:
                    if template_policy_name in el.text:
                        self.utils.print_info(f" Select {el.text} from dropdown")
                        self.auto_actions.select_drop_down_options(dropdown_items, el.text)
                    else:
                        self.utils.print_info(f" The template name was not found in dropdown")
            else:
                self.utils.print_info(f" Not able to find dropdown items ")
        else:
            return -1

        # Perform the update
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        self.utils.print_info("Click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_devices_perform_update_button_d360())

        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_after = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_after)

        for item_after in tool_tp_text_after:
            if item_after in tool_tp_text_before:
                pass
            else:
                self.utils.print_info(" Below error message is displayed after press update button")
                self.utils.print_info(item_after)
                if self.devices_web_elements.get_devices_close_button_update():
                    self.utils.print_info("Click on exit button")
                    self.auto_actions.click(self.devices_web_elements.get_devices_close_button_update())
                else:
                    self.utils.print_info("The exit button was not found")
                return item_after
        return self.check_device_update_status_by_using_mac(device_mac)

    def check_device_update_status_by_using_mac(self, device_mac):
        """
        - This keyword is used to check the status of the device update
        - It will poll the "update status" every 30 seconds
        - Assuming that config push will take a maximum of five minutes
        - If Device Update Failed will return -1
        :param device_mac: device MAC to check the config push status
        :return: 1 if config push success else -1
        """
        self.utils.print_info("Start checking the status")
        sleep(20)
        retry_count = 0
        while retry_count <= 300:
            device_update_status = self.get_device_updated_status(device_mac=device_mac)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                break
            elif retry_count == 300:
                self.utils.print_info("Config push to switch taking more than 5 minutes")
                return -1
            if 'Failed' in device_update_status:
                self.utils.print_info("Device Update Failed: ", device_update_status)
                return -1
            sleep(30)
            self.utils.print_info(f"Time elapsed for device update: {retry_count} seconds")
            retry_count += 30
        self.utils.print_info("return 1  ", device_update_status)
        return 1

    def get_device_stack_status(self, device_mac='default', device_serial='default', duration_retry=300):
        """
        - This keyword returns the device's connection status, audit log status
        - Keyword Usage:
         - ``Get Device Status   device_serial=${DEVICE_SERIAL}``
         - ``Get Device Status   device_name=${DEVICE_NAme}``
         - ``Get Device Status   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial
        :param device_name: device host name
        :param device_mac: device MAC address
        :param duration_retry : duration of retry in seconds

        :return:
        - 'blue' if device connected and config audit match and stack toggle icon is blue
        - 'red' stack toggle icon is red
        - 'config audit mismatch' if device connected and config audit mismatch
        - 'disconnected' if device disconnected and unable to connect after 10 minutes
        - 'unknown' if device connection status is 'Unknown'
        """
        self.navigator.navigate_to_devices()
        status = -1
        device_row = -1
        try_one_more_time_serial = True
        try_one_more_time_mac = True
        self.refresh_devices_page()
        retry_count = 0
        while retry_count <= 300:
            self.refresh_devices_page()
            self.utils.print_info("Getting status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac)
            if device_row != -1:
                self.utils.print_info("Found a raw with mac :", device_mac)
                self.utils.print_info("Check if stack toggle icon is present")
                stack_toggle = self.devices_web_elements.get_device_stack_toggle(device_row)
                if stack_toggle:
                    device_row = self.get_device_row(device_serial)
                    if device_row == -1:
                        if "ui-icon-stack" in stack_toggle.split(" "):
                            self.utils.print_info("The stack toogle icon is blue. Now check the connection status   ")
                            connected_status = self.get_device_status(device_mac=device_mac)
                            if connected_status:
                                if connected_status == 'green':
                                    status = 'blue'
                                    self.utils.print_info("Return :", status)
                                    return status
                                elif connected_status == 'disconnected':
                                    self.utils.print_info(
                                        "Status is disconnected ,try again until duration_retry expired:",
                                        connected_status)
                                    status = connected_status
                                else:
                                    self.utils.print_info("Return :", connected_status)
                                    return connected_status
                            else:
                                self.utils.print_info("Cannot read the conection status")
                        elif "ui-icon-stack-warning" in stack_toggle.split(" "):
                            self.utils.print_info(
                                "The stack toogle icon is red. Continue to check until duration_retry expired ")
                            status = 'red'
                        else:
                            self.utils.print_info("stack_toggle icon is present but the status can not be read ")
                            return -1
                    else:
                        pass
                else:
                    if try_one_more_time_mac:
                        try_one_more_time_mac = False
                    else:
                        self.utils.print_info("Found a raw with mac but stack_toggle icon was not found ")
                        return -1
            else:
                self.utils.print_info("No found a raw with mac :", device_mac)
                self.utils.print_info("Search device with serial: ", device_serial)
                device_row = self.get_device_row(device_serial)
                if device_row != -1:
                    self.utils.print_info("Found a raw with serial {}.The stack is not formed yet. "
                                          "Continue to check until duration_retry expired ".format(device_serial))
                    status = -1
                else:
                    self.utils.print_info("Did not found a raw with serial or mac ; Try one more time  ")
                    if try_one_more_time_serial:
                        try_one_more_time_serial = False
                    else:
                        self.utils.print_info(
                            "Not found a raw with serial {} or mac {}  :".format(device_serial, device_mac))
                        return -1
            retry_count += 30
            self.utils.print_info("Try again after {} seconds:".format(duration_retry / 10))
            sleep(duration_retry / 10)
        self.utils.print_info("duration_retry expired ; Return :", status)
        return status

    def select_version_and_upgrade_device_to_specific_version(self, device_serial, version):
        """
        - This method update device to specific version from the dropdown
        - keyword Usage:
         - Select Version And Upgrade Device To Specific Version    ${DEVICE_SERIAL}   version=${VERSION}

        :param device_serial: serial number(s) of the device(s)
        :param version: version to which device(s) should get upgraded. This string should be contains into image name . e.g : 5520.8.3.0.0
        :return: 1 if success else -1
        """
        if self.select_device(device_serial):
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click(self.device_update.get_update_devices_button())
            sleep(5)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_iq_engine_checkbox())
            sleep(5)

            self.utils.print_info("Selecting upgrade to specific version checkbox")
            self.auto_actions.click(self.device_update.get_upgrade_to_specific_version_radio())
            sleep(2)

            self.utils.print_info("Selecting upgrade even if the versions are the same")
            self.auto_actions.click(self.device_update.get_upgrade_even_if_versions_same_checkbox())
            sleep(2)

            self.utils.print_info("Click on version drop down")
            self.auto_actions.click(self.device_update.get_actions_update_version_drop_down())
            sleep(5)

            update_version_items = self.device_update.get_actions_update_version_drop_down_items()
            self.auto_actions.scroll_down()
            sleep(2)
            cont_images_found = 0
            if update_version_items:
                item_count = len(update_version_items)
                self.utils.print_info(f"Iterating through {item_count} options")
                for opt in update_version_items:
                    self.utils.print_info("Image: {} is in drop down ".format(opt.text))
                    if version in opt.text:
                        self.utils.print_info(
                            "Image version {} match the image {} from drop down".format(version, opt.text))
                        cont_images_found += 1
                        image_select = opt.text
                    else:
                        self.utils.print_info(
                            "Image version {} doesn't match the image {} from drop down".format(version, opt.text))
            if cont_images_found == 1:
                if self.auto_actions.select_drop_down_options(update_version_items, image_select):
                    self.utils.print_info(f"Selected update version from drop down:{version}")
                    self.utils.print_info("Selecting Perform Update button...")
                    self.auto_actions.click(self.device_update.get_perform_update_button())
                    self.screen.save_screen_shot()
                    sleep(5)
                    return 1
            if cont_images_found > 1:
                self.utils.print_info("Multiple images were found into drop down ")
                return -1
            self.screen.save_screen_shot()
            sleep(5)
            self.utils.print_info("Image version {} doesn't match the images from drop down.".format(version))
            return -1
        return -1

    def actions_xiqse_open_site_engine(self):
        """
        - This keyword clicks on the ACTIONS > OPEN SITE ENGINE link
        - It is assumed that the Manage > Device window is open and an XIQ-SE managed device is selected.
        - Keyword Usage
         - ``Actions XIQSE Open Site Engine``
        :return: 1 if action was successful (or the field is disabled), else -1
        """
        ret_val = -1

        self.utils.print_info("Clicking on Actions Button")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        sleep(2)

        ose_link = self.devices_web_elements.get_actions_open_site_engine_menu_option()
        if ose_link:
            hidden = ose_link.get_attribute("style")
            self.utils.print_debug(f"Open Site Engine link Style value: {hidden}")
            if hidden == "display: none;":
                self.utils.print_info("The 'Open Site Engine' link is hidden.")
                self.screen.save_screen_shot()
                ret_val = 1
            else:
                self.utils.print_info("Clicking the 'Open Site Engine' link.")
                self.screen.save_screen_shot()
                self.auto_actions.click(ose_link)
                ret_val = 1
        else:
            self.utils.print_info("Could not find the 'Open Site Engine' link.")

        return ret_val

    def actions_xiqse_maximum_site_engine_message(self):
        """
        - This keyword checks if the 'Maximum 5 Site Engine > Device View' message banner is displayed.
        - The message banner will be closed, if displayed.
        - Keyword Usage
         - ``Actions XIQSE Maximum Site Engine Message``
        :return: 1 if the menu option is displayed, else -1
        """
        ret_val = -1

        self.utils.print_info("Checking for the 'Maximum 5 Site Engine > Device View...` message")
        max_ose_msg = self.devices_web_elements.get_actions_maximum_site_engine_message()
        if max_ose_msg:
            self.utils.print_info("`Maximum 5 Site Engine > Device view...' message is displayed")
            self.screen.save_screen_shot()
            sleep(2)
            max_ose_msg_btn = self.devices_web_elements.get_actions_maximum_site_engine_message_box()
            ret_val = 1
            if max_ose_msg_btn:
                self.utils.print_info("Closing the `Maximum 5 Site Engine > Device view...' message")
                self.auto_actions.click(max_ose_msg_btn)
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not find the 'Maximum 5 Site Engine > Device View...' message")
            self.screen.save_screen_shot()

        return ret_val

    def actions_menu_disabled(self):
        """
        - This keyword checks if the ACTIONS menu is disabled in the Manage > Devices table.
        - It is assumed that the Manage > Device window is open.
        - Keyword Usage
         - ``Actions Menu Disabled``
        :return: 1 if the field is disabled, else -1
        """
        ret_val = -1

        self.utils.print_info("Checking if Actions button is disabled.")
        actions_btn = self.device_actions.get_device_actions_button()
        if actions_btn:
            disabled = actions_btn.get_attribute("class")
            self.utils.print_info(f"Actions button Style value: {disabled}")
            if disabled == "btn btn-secondary-text btn-disabled":
                self.utils.print_info("The 'Actions' button is disabled.")
                self.screen.save_screen_shot()
                ret_val = 1
            else:
                self.utils.print_info("The 'Actions' button is disabled.")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not find the 'Actions' button.")

        return ret_val

    def rbac_user_multiple_location_search_AP_serial(self, ap_serial):
        """
        - Searches for AP matching AP's Serial Number based on
        - Keyword Usage:
         - ``Search AP Serial  ${AP_SERIAL}``

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found else False
        """
        self.navigator.navigate_to_devices()
        self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
        sleep(10)

        page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        if page_size_field and page_number_field.is_displayed():
            self.utils.print_info("Searching Device Entry with AP Serial : ", ap_serial)
            self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), ap_serial)
            self.screen.save_screen_shot()
            sleep(5)

        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info("row data: ", self.format_row(row.text))
                if not ap_serial in row.text:
                    self.utils.print_info("Did not Find AP Row: ", self.format_row(row.text))
                    return 1
            self.utils.print_info("Did not find AP")
        else:
            self.utils.print_info("No rows present")
        return False

    def _select_location(self, sel_loc):
        """
        - This keyword selects a location in the location dialog and clicks the "Assign" button.
          It is assumed the location dialog is already open.
        - Keyword Usage:
         - ``Select Location  ${LOCATION}``

        :param sel_loc: location to select, in a comma-separated list format; e.g., San Jose, building_01, floor_02
        :return: 1 if location is selected, else -1'
        """
        ret_val = -1
        if sel_loc:
            try:
                location_list = sel_loc.split(',')

                location_generics = self.device_actions.get_locations_generic()
                location_buildings = self.device_actions.get_locations_building()
                location_floors = self.device_actions.get_locations_floors()

                for location_item in location_list:
                    self.utils.print_info("Location items ", location_item)

                for location_generic in location_generics:
                    self.utils.print_info("Generic locations on UI:", location_generic.text)

                for location_building in location_buildings:
                    self.utils.print_info("Building locations on UI:", location_building.text)

                for location_floor in location_floors:
                    self.utils.print_info("Floor locations on UI:", location_floor.text)

                generic_set = False
                building_set = False
                floor_set = False

                for location_item in location_list:

                    if not generic_set:
                        self.utils.print_info("Selecting Generic location: ", location_item)
                        for location_generic in location_generics:
                            if location_item.strip() in location_generic.text:
                                self.utils.print_info("Match found for location type Generic:", location_generic.text)
                                self.auto_actions.click(location_generic)
                                generic_set = True
                                sleep(5)

                    if not building_set:
                        self.utils.print_info("Selecting Building: ", location_item)
                        for location_building in location_buildings:
                            if location_item.strip() in location_building.text:
                                self.utils.print_info("Match found for location type Building:", location_building.text)
                                self.auto_actions.click(location_building)
                                building_set = True
                                sleep(5)

                    if not floor_set:
                        self.utils.print_info("Selecting Floor: ", location_item)
                        for location_floor in location_floors:
                            if location_item.strip() in location_floor.text:
                                self.utils.print_info("Match found for location type Generic:", location_floor.text)
                                self.auto_actions.click(location_floor)
                                floor_set = True
                                sleep(5)

                self.utils.print_info("Placing The Device To FloorPlan")
                source_el = self.device_actions.get_device_location_ap_node()
                target_el = self.device_actions.get_device_location_floor_map_section()
                self.auto_actions.drag_and_drop_element(source_el, target_el)
                self.screen.save_screen_shot()

                self.utils.print_info("Clicking on Assign Location Button")
                self.auto_actions.click(self.devices_web_elements.get_location_select_button())
                sleep(5)

                ret_val = 1

            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to select location")
        else:
            self.utils.print_info("Cannot select location - location not specified")

        return ret_val

    def check_negative_combinations(self):
        sleep(5)
        tooltip_text = ""
        mac_error = ""
        sn_error = ""
        try:
            tooltip_text = self.dialogue_web_elements.get_tooltip_text()
            if tooltip_text:
                self.utils.print_info("Tooltip: ", tooltip_text)
            else:
                tooltip_text = ""

            sn_error = self.devices_web_elements.get_devices_serial_text_area_error()
            if "test message" in sn_error:
                self.utils.print_info("No Serial Number errors")
            else:
                self.utils.print_info("Serial Number error: ", sn_error)

            mac_error = self.devices_web_elements.get_devices_mac_text_area_error()
            self.utils.print_info("MAC error: ", mac_error)
        except AttributeError:
            self.utils.print_info("No Serial, MAC Error Observed")

        sn = None
        if 'Serial numbers entered are from different platform families. Please enter serial numbers that are part of the same platform family. Please remove serial number' in tooltip_text:
            try:
                sn = re.search("Please remove serial number (.*).", tooltip_text).group(1)
            except AttributeError:
                self.utils.print_info(
                    "Unable to extract serial number from Tooltip. Possible reason: change in error message")
            return sn, -2
        elif ('Could not recognize' in tooltip_text) and (' Please onboard ' in tooltip_text):
            try:
                sn = re.search("Could not recognize (.*). Please onboard (.*) separately.", tooltip_text).group(1)
            except AttributeError:
                self.utils.print_info(
                    "Unable to extract serial number from Tooltip. Possible reason: change in error message")
            return sn, -3
        elif 'No more than 10 serial numbers could be entered at once.' in sn_error:
            return -4
        elif 'When onboarding multiple devices, serial numbers must be separated by ", " (Commas)' in sn_error:
            return -5
        elif 'The number of MAC Addresses must match the number of Serial Numbers' in mac_error:
            return -6
        elif 'Please enter a valid MAC Address' in mac_error:
            return -7
        else:
            return 1

    def select_location_quick_onboarding(self, sel_loc):
        """
        - This keyword selects a location in the location dialog and clicks the "Select" button.
          It is assumed the location dialog is already open.
        - Keyword Usage:
         - ``Select Location  ${LOCATION}
        :param sel_loc: location to select, in a comma-separated list format; e.g., San Jose, building_01, floor_02
        :return: 1 if location is selected, else -1'
        """

        self.utils.print_info(sel_loc)
        location_list = sel_loc.split(',')
        self.utils.print_info(location_list)
        location_generics = self.device_actions.get_locations_generic()
        self.utils.print_info("These are the locations, but in the form of objects:", location_generics)
        location_buildings = self.device_actions.get_locations_building()
        location_floors = self.device_actions.get_locations_floors()
        if location_generics and location_buildings and location_floors:
            pass
        else:
            return -1
        for location_item in location_list:
            self.utils.print_info("Location items ", location_item)
        for location_generic in location_generics:
            self.utils.print_info("Generic locations on UI:", location_generic.text)
        for location_building in location_buildings:
            self.utils.print_info("Building locations on UI:", location_building.text)
        for location_floor in location_floors:
            self.utils.print_info("Floor locations on UI:", location_floor.text)
        generic_set = False
        building_set = False
        floor_set = False
        self.utils.print_info("Selecting Generic location: ", location_list[0])
        for location_generic in location_generics:
            if location_list[0] == location_generic.text:
                self.utils.print_info("Match found for location type Generic:", location_generic.text)
                self.auto_actions.click(location_generic)
                generic_set = True
                sleep(5)
            else:
                pass
        if generic_set:
            self.utils.print_info("Location has been selected")
        else:
            self.utils.print_info("Location has not been found")
            if self.devices_web_elements.get_cancel_location_button():
                self.utils.print_info("Selecting Cancel button")
                self.auto_actions.click(self.devices_web_elements.get_cancel_location_button())
            else:
                self.utils.print_info("Cancel button was not found")
                sleep(3)
            return -1
        self.utils.print_info("Selecting Building: ", location_list[1])
        for location_building in location_buildings:
            if location_list[1] == location_building.text:
                self.utils.print_info("Match found for location type Building:", location_building.text)
                self.auto_actions.click(location_building)
                building_set = True
                sleep(5)
        if building_set:
            self.utils.print_info("Building has been selected")
        else:
            self.utils.print_info("Building has not been found")
            return -1
        self.utils.print_info("Selecting Floor: ", location_list[2])
        for location_floor in location_floors:
            if location_list[2] == location_floor.text:
                self.utils.print_info("Match found for location type Generic:", location_floor.text)
                self.auto_actions.click(location_floor)
                floor_set = True
                sleep(5)
        if floor_set:
            self.utils.print_info("Floor has been selected")
        else:
            self.utils.print_info("Floor has not been found")
            return -1
        return 1

    def quick_onboarding_cloud_manual(self, device_sn, device_make, location, policy_name=None):
        '''
        This keyword on boards your devices directly to cloud by using new onboarding flow
        Can on boards an aerohive device [AP or Switch], Universal APs , Exos Switch, Exos Stack and Voss devices
        using Quick onboarding flow.
        - Keyword Usage:
         - quick_onboarding_cloud_manual          ${DUT_SERIAL}    voss      Bucharest,address,Floor 1
        :param device_sn: serial number of Device; single SN or a list of SNs
        :param device_make: Model of the Device e.g. :aerohive/universal_ap/voss/exos
        :param location: The location, building and floor separated by comma ; e.g. Bucharest,address,Floor 1
        :param policy_name: The policy name
        :return: 1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message
         will be returned ; else -1
        '''

        self.navigator.navigate_to_devices()
        add_button = self.devices_web_elements.get_add_button()
        if add_button:
            self.utils.print_info("Click on '+' button")
            self.auto_actions.click(add_button)
        else:
            self.utils.print_info("'+' button not found")
            return -1
        quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
        if quick_add_devices_button:
            self.utils.print_info("Click on 'Quick Add Devices'")
            self.auto_actions.move_to_element(quick_add_devices_button)
        else:
            self.utils.print_info("'Quick Add Devices' button not found")
            return -1
        deploy_to_cloud_button = self.devices_web_elements.get_deploy_to_cloud()
        if deploy_to_cloud_button:
            self.utils.print_info("Click on 'Deploy to the cloud'")
            self.auto_actions.click(deploy_to_cloud_button)
        else:
            self.utils.print_info("'Deploy to the cloud' button not found")
            return -1
        tool_tp_text_before_insert_sn = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before_insert_sn)
        insert_sn = self.devices_web_elements.get_insert_sn()
        if insert_sn:
            self.utils.print_info("Insert serial number: {}".format(device_sn))
            self.auto_actions.send_keys(insert_sn, device_sn)
            sleep(7)
            # Check the banner error
            tool_tp_text_after_insert_sn = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after_insert_sn)
            for item_after_sn in tool_tp_text_after_insert_sn:
                if item_after_sn in tool_tp_text_before_insert_sn:
                    pass
                else:
                    self.utils.print_info(" Below error message is displayed after insert SN")
                    self.utils.print_info(item_after_sn)
                    return item_after_sn
        else:
            self.utils.print_info("'Serial number' box not found")
            return -1
        if location:
            if self.devices_web_elements.get_add_location_button():
                self.utils.print_info("Click on 'Location'")
                self.auto_actions.click(self.devices_web_elements.get_add_location_button())
                self.utils.print_info("Selecting location '" + location + "'")
                if self.select_location_quick_onboarding(location) == 1:
                    self.utils.print_info("Location selected ")
                    self.utils.print_info("Clicking on select location Button")
                    self.auto_actions.click(self.devices_web_elements.get_select_location())
                else:
                    self.auto_actions.click(self.devices_web_elements.get_cancel_location_button())
                    self.utils.print_info("Selecting Cancel button")
                    return -1
            else:
                self.utils.print_info("'Location' button not found")
                return -1
        else:
            self.utils.print_info("The location will not be selected")
        if policy_name != None:
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            if self.devices_web_elements.get_policy_drop_down():
                self.auto_actions.click(self.devices_web_elements.get_policy_drop_down())
                sleep(2)
            else:
                self.utils.print_info("The policy drop down was not found")
            if self.devices_web_elements.get_policy_drop_down_items():
                if self.auto_actions.select_drop_down_options(self.devices_web_elements.get_policy_drop_down_items(),
                                                              policy_name):
                    self.utils.print_info("Select {} from drop down ".format(policy_name))
                    sleep(2)
                else:
                    self.utils.print_info(
                        "The policy name was not found into drop down. Will continue without policy assigned ")
            else:
                self.utils.print_info("The policy drop down items was not found")

        if 'voss' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'VOSS' from the 'Device Make' drop down...")
                self.utils.print_info("'VOSS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_voss())
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_voss():
                    self.utils.print_info("'VOSS' autodetection is working")
                    self.utils.print_info("Selecting 'VOSS' from the 'Device OS' checkbox...")
                    self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_voss())
                else:
                    self.utils.print_info("Button 'VOSS' not found")
                    return -1
        elif 'exos' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.utils.print_info("'EXOS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_exos())
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_exos():
                    self.utils.print_info("'EXOS' autodetection is working ")
                    self.utils.print_info("Selecting 'EXOS' from the 'Device OS' checkbox...")
                    self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_exos())
                else:
                    self.utils.print_info("Button 'EXOS' not found")
                    return -1
        elif 'aerohive' in device_make.lower():
            self.utils.print_info("Selecting 'Extreme - Aerohive' from the 'Device Make' drop down...")
            self.auto_actions.click(self.devices_web_elements.get_device_make_list())
            self.auto_actions.click(self.devices_web_elements.get_device_make_aerohive())
            sleep(2)
        elif 'universal_ap' in device_make.lower():
            if self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio():
                self.utils.print_info("'cloudIqEngine' autodetection is working ")
                self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio())
            else:
                self.utils.print_info("'cloudIqEngine' autodetection is not working ")
                return -1
        else:
            self.utils.print_info("'Device make' list not found")
            return -1
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)
        if self.devices_web_elements.get_add_devices_button():
            self.utils.print_info("Click on Add Devices")
            self.auto_actions.click(self.devices_web_elements.get_add_devices_button())
            # Check the already onboarded error
            if self.devices_web_elements.get_error_onboarding_message():
                self.utils.print_info("{} already onboarded ".format(device_sn))
                return -1
            else:
                pass
            # Check the banner error
            sleep(3)
            tool_tp_text_after = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after)
            for item_after in tool_tp_text_after:
                if item_after in tool_tp_text_before:
                    pass
                else:
                    if 'successfully' in item_after:
                        pass
                    else:
                        self.utils.print_info(" Below error message is displayed after press ADD button")
                        self.utils.print_info(item_after)
                        return item_after
            # Check the SN field error
            sn_error = self.devices_web_elements.get_sn_error_message()
            if sn_error:
                self.utils.print_info(sn_error)
                return sn_error
            else:
                self.utils.print_info("No SN error")
        else:
            self.utils.print_info("'Add Devices' button not found or the button is not active")
            return -1
        return 1

    def quick_onboarding_cloud_csv(self, device_make, location, csv_location, policy_name=None):
        '''
        This keyword on boards your devices directly to cloud by using new onboarding flow
        Can on boards an aerohive device [AP or Switch], Universal APs , Exos Switch, Exos Stack and Voss devices
        using Quick onboarding flow.
        - Keyword Usage:
         - quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}
        :param device_sn: serial number of Device; single SN or a list of SNs
        :param device_make: Model of the Device e.g. :aerohive/universal_ap/voss/exos
        :param location: The location, building and floor separated by comma ; e.g. Bucharest,address,Floor 1
        :param csv_location: csv file path
        e.g. ${DUT_CSV_FILE}             /automation/xiq/cw_automation/testsuites/xiq/topologies/${TESTBED}/MultipleVossDevices.csv
        :param policy_name: The policy name
        :return: 1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message
         will be returned ; else -1
        '''

        self.navigator.navigate_to_devices()
        add_button = self.devices_web_elements.get_add_button()
        if add_button:
            self.utils.print_info("Click on '+' button")
            self.auto_actions.click(add_button)
        else:
            self.utils.print_info("'+' button not found")
            return -1
        quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
        if quick_add_devices_button:
            self.utils.print_info("Click on 'Quick Add Devices'")
            self.auto_actions.move_to_element(quick_add_devices_button)
        else:
            self.utils.print_info("'Quick Add Devices' button not found")
            return -1
        deploy_to_cloud_button = self.devices_web_elements.get_deploy_to_cloud()
        if deploy_to_cloud_button:
            self.utils.print_info("Click on 'Deploy to the cloud'")
            self.auto_actions.click(deploy_to_cloud_button)
        else:
            self.utils.print_info("'Deploy to the cloud' button not found")
            return -1
        sleep(2)
        if self.devices_web_elements.get_select_csv():
            self.utils.print_info("Select CSV")
            self.auto_actions.click(self.devices_web_elements.get_select_csv())
        else:
            self.utils.print_info("CSV checkbox was not found")
            return -1
        if 'voss' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'VOSS' from the 'Device Make' drop down...")
                self.utils.print_info("'VOSS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_voss())
                sleep(2)
            else:
                self.utils.print_info("Button 'VOSS' not found")
                return -1
        elif 'exos' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.utils.print_info("'EXOS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_exos())
                sleep(2)
            else:
                self.utils.print_info("Button 'EXOS' not found")
                return -1
        elif 'aerohive' in device_make.lower():
            self.utils.print_info("Selecting 'Extreme - Aerohive' from the 'Device Make' drop down...")
            self.auto_actions.click(self.devices_web_elements.get_device_make_list())
            self.auto_actions.click(self.devices_web_elements.get_device_make_aerohive())
            sleep(2)
        elif 'universal_ap' in device_make.lower():
            if self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio():
                self.utils.print_info("'cloudIqEngine' autodetection is working ")
                self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio())
            else:
                pass
        else:
            self.utils.print_info("'Device make' list not found")
            return -1
        if csv_location:
            upload_button = self.devices_web_elements.get_device_csv_upload_button()
            if upload_button:
                self.utils.print_info("Specifying CSV file '" + csv_location)
                self.auto_actions.send_keys(upload_button, csv_location)
            else:
                self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                return -1
        else:
            self.utils.print_info(">>> CSV file was not specified")
            self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
            return -1
        if location:
            if self.devices_web_elements.get_add_location_button():
                self.utils.print_info("Click on 'Location'")
                self.auto_actions.click(self.devices_web_elements.get_add_location_button())
                self.utils.print_info("Selecting location '" + location + "'")
                if self.select_location_quick_onboarding(location) == 1:
                    self.utils.print_info("Location selected ")
                    self.utils.print_info("Clicking on select location Button")
                    self.auto_actions.click(self.devices_web_elements.get_select_location())
                else:
                    self.auto_actions.click(self.devices_web_elements.get_cancel_location_button())
                    self.utils.print_info("Selecting Cancel button")
                    return -1
            else:
                self.utils.print_info("'Location' button not found")
                return -1
        else:
            self.utils.print_info("The location will not be selected")
        if policy_name != None:
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            if self.devices_web_elements.get_policy_drop_down():
                self.auto_actions.click(self.devices_web_elements.get_policy_drop_down())
                sleep(2)
            else:
                self.utils.print_info("The policy drop down was not found")
            if self.devices_web_elements.get_policy_drop_down_items():
                if self.auto_actions.select_drop_down_options(self.devices_web_elements.get_policy_drop_down_items()
                        , policy_name):
                    self.utils.print_info("Select {} from drop down ".format(policy_name))
                    sleep(2)
                else:
                    self.utils.print_info(
                        "The policy name was not found into drop down. Will continue without policy assigned ")
            else:
                self.utils.print_info("The policy drop down items was not found")
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)
        if self.devices_web_elements.get_add_devices_button():
            self.utils.print_info("Click on Add Devices")
            self.auto_actions.click(self.devices_web_elements.get_add_devices_button())
            # Check the already onboarded error
            if self.devices_web_elements.get_error_onboarding_message():
                self.utils.print_info("{} already onboarded ".format(device_sn))
                return -1
            else:
                pass
            # Check the banner error
            sleep(3)
            tool_tp_text_after = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after)
            for item_after in tool_tp_text_after:
                if item_after in tool_tp_text_before:
                    pass
                else:
                    if 'successfully' in item_after:
                        pass
                    else:
                        self.utils.print_info(" Below error message is displayed after press ADD button")
                        self.utils.print_info(item_after)
                        return item_after
        else:
            self.utils.print_info("'Add Devices' button not found or the button is not active")
            return -1
        return 1

    def quick_onboarding_locally_manual(self, device_sn, device_make):
        '''
        This keyword on boards your devices locally by using new onboarding flow
        Can on boards an Universal APs, Exos Switch, Exos Stack and Voss devices
        using Quick onboarding flow.
        - Keyword Usage:
         - quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}
        :param device_make: Model of the Device e.g. :aerohive/universal_ap/voss/exos
        :return: 1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message
         will be returned ; else -1
        '''
        self.navigator.navigate_to_devices()
        add_button = self.devices_web_elements.get_add_button()
        if add_button:
            self.utils.print_info("Click on '+' button")
            self.auto_actions.click(add_button)
        else:
            self.utils.print_info("'+' button not found")
            return -1
        quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
        if quick_add_devices_button:
            self.utils.print_info("Click on 'Quick Add Devices'")
            self.auto_actions.move_to_element(quick_add_devices_button)
        else:
            self.utils.print_info("'Quick Add Devices' button not found")
            return -1
        deploy_locally = self.devices_web_elements.get_deploy_locally()
        if deploy_locally:
            self.utils.print_info("Click on 'Deploy your devices locally'")
            self.auto_actions.click(deploy_locally)
        else:
            self.utils.print_info("'Deploy your devices locally' button not found")
            return -1
        sleep(3)
        tool_tp_text_before_insert_sn = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before_insert_sn)
        insert_sn = self.devices_web_elements.get_insert_sn()
        if insert_sn:
            self.utils.print_info("Insert serial number: {}".format(device_sn))
            self.auto_actions.send_keys(insert_sn, device_sn)
            sleep(7)
            # Check the banner error
            tool_tp_text_after_insert_sn = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after_insert_sn)
            for item_after_sn in tool_tp_text_after_insert_sn:
                if item_after_sn in tool_tp_text_before_insert_sn:
                    pass
                else:
                    self.utils.print_info(" Below error message is displayed after insert SN")
                    self.utils.print_info(item_after_sn)
                    return item_after_sn
        else:
            self.utils.print_info("'Serial number' box not found")
            return -1
        if 'voss' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'VOSS' from the 'Device Make' drop down...")
                self.utils.print_info("'VOSS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_voss())
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_voss():
                    self.utils.print_info("'VOSS' autodetection is working")
                    self.utils.print_info("Selecting 'VOSS' from the 'Device OS' checkbox...")
                    self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_voss())
                else:
                    self.utils.print_info("Button 'VOSS' not found")
                    return -1
        elif 'exos' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.utils.print_info("'EXOS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_exos())
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_exos():
                    self.utils.print_info("'EXOS' autodetection is working ")
                    self.utils.print_info("Selecting 'EXOS' from the 'Device OS' checkbox...")
                    self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_exos())
                else:
                    self.utils.print_info("Button 'EXOS' not found")
                    return -1
        elif 'universal_ap' in device_make.lower():
            if self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio():
                self.utils.print_info("'cloudIqEngine' autodetection is working ")
            else:
                self.utils.print_info("'cloudIqEngine' autodetection is not working ")
                return -1
        else:
            self.utils.print_info("'Device make' list not found")
            return -1
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)
        if self.devices_web_elements.get_add_devices_button():
            self.utils.print_info("Click on Add Devices")
            self.auto_actions.click(self.devices_web_elements.get_add_devices_button())
            # Check the already onboarded error
            if self.devices_web_elements.get_error_onboarding_message():
                self.utils.print_info("{} already onboarded ".format(device_sn))
                return -1
            else:
                pass
            # Check the banner error
            sleep(3)
            tool_tp_text_after = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after)
            for item_after in tool_tp_text_after:
                if item_after in tool_tp_text_before:
                    pass
                else:
                    if 'successfully' in item_after:
                        pass
                    else:
                        self.utils.print_info(" Below error message is displayed after press ADD button")
                        self.utils.print_info(item_after)
                        return item_after
            # Check the SN field error
            sn_error = self.devices_web_elements.get_sn_error_message()
            if sn_error:
                self.utils.print_info(sn_error)
                return sn_error
            else:
                self.utils.print_info("No SN error")
        else:
            self.utils.print_info("'Add Devices' button not found or the button is not active")
            return -1
        return 1

    def quick_onboarding_locally_csv(self, device_make, csv_location):
        '''
        This keyword on boards your devices locally by using new onboarding flow
        Can on boards an Wing device, Exos Switch, Exos Stack and Voss devices
        using Quick onboarding flow.
        - Keyword Usage:
         - quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}
        :param device_make: Model of the Device e.g. :aerohive/universal_ap/voss/exos
        :param csv_location: csv file path
        e.g. ${DUT_CSV_FILE}             /automation/xiq/cw_automation/testsuites/xiq/topologies/${TESTBED}/MultipleVossDevices.csv
        :return: 1 if successfully onboarded; if any error occurs on banner the text of error message will be returned ;
         else -1
        '''
        self.navigator.navigate_to_devices()
        add_button = self.devices_web_elements.get_add_button()
        if add_button:
            self.utils.print_info("Click on '+' button")
            self.auto_actions.click(add_button)
        else:
            self.utils.print_info("'+' button not found")
            return -1
        quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
        if quick_add_devices_button:
            self.utils.print_info("Click on 'Quick Add Devices'")
            self.auto_actions.move_to_element(quick_add_devices_button)
        else:
            self.utils.print_info("'Quick Add Devices' button not found")
            return -1
        deploy_locally = self.devices_web_elements.get_deploy_locally()
        if deploy_locally:
            self.utils.print_info("Click on 'Deploy your devices locally'")
            self.auto_actions.click(deploy_locally)
        else:
            self.utils.print_info("'Deploy your devices locally' button not found")
            return -1
        if self.devices_web_elements.get_select_csv():
            self.utils.print_info("Select CSV")
            self.auto_actions.click(self.devices_web_elements.get_select_csv())
        else:
            self.utils.print_info("CSV checkbox was not found")
            return -1
        sleep(3)

        if 'voss' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'VOSS' from the 'Device Make' drop down...")
                self.utils.print_info("'VOSS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_voss())
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_voss():
                    self.utils.print_info("Selecting 'VOSS' from the 'Device OS' checkbox...")
                    self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_voss())
                else:
                    self.utils.print_info("Button 'VOSS' not found")
                    return -1
        elif 'exos' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.utils.print_info("'EXOS' found in 'Device Make' list")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_make_exos())
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_exos():
                    self.utils.print_info("Selecting 'VOSS' from the 'Device OS' checkbox...")
                    self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_exos())
                else:
                    self.utils.print_info("Button 'EXOS' not found")
                    return -1
        elif 'wing' in device_make.lower():
            if self.devices_web_elements.get_device_auto_detection_wingRadio():
                self.utils.print_info("Selecting 'WING' from the 'Device OS' checkbox...")
                self.auto_actions.click(self.devices_web_elements.get_device_make_list())
                self.auto_actions.click(self.devices_web_elements.get_device_auto_detection_wingRadio())
            else:
                self.utils.print_info("Button 'WING' not found")
                return -1
        else:
            self.utils.print_info("'Device make' list not found")
            return -1

        if csv_location:
            upload_button = self.devices_web_elements.get_device_csv_upload_button()
            if upload_button:
                self.utils.print_info("Specifying CSV file '" + csv_location)
                self.auto_actions.send_keys(upload_button, csv_location)
            else:
                self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                return -1
        else:
            self.utils.print_info(">>> CSV file was not specified")
            self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
            return -1

        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)
        if self.devices_web_elements.get_add_devices_button():
            self.utils.print_info("Click on Add Devices")
            self.auto_actions.click(self.devices_web_elements.get_add_devices_button())
            # Check the already onboarded error
            if self.devices_web_elements.get_error_onboarding_message():
                self.utils.print_info("Device(s) already onboarded ")
                return -1
            else:
                pass
            # Check the banner error
            sleep(3)
            tool_tp_text_after = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after)
            for item_after in tool_tp_text_after:
                if item_after in tool_tp_text_before:
                    pass
                else:
                    if 'successfully' in item_after:
                        pass
                    else:
                        self.utils.print_info(" Below error message is displayed after press ADD button")
                        self.utils.print_info(item_after)
                        return item_after
            # Check the SN field error
            sn_error = self.devices_web_elements.get_sn_error_message()
            if sn_error:
                self.utils.print_info(sn_error)
                return sn_error
            else:
                self.utils.print_info("No SN error")
        else:
            self.utils.print_info("'Add Devices' button not found or the button is not active")
            return -1
        return 1

    def get_device_template_status(self, device_mac='default', duration_retry=50):
        """
        - This keyword returns the device's connection status, audit log status
        - Keyword Usage:
         - ``Get Template Status   device_mac=${DEVICE_MAC}``

        :param device_mac: device MAC address
        :param duration_retry : duration of retry in seconds

        :return:
        - 1 for 'empty' if device is a EXOS Stack and don't have a policy
        - 2 for 'Device default-template' if device is a standalone device
        - 3 for 'Assign/Create Template' if device is a EXOS Stack and have a policy
        """
        self.navigator.navigate_to_devices()
        device_row = -1
        self.refresh_devices_page()

        retry_count = 0
        while retry_count <= 50:
            self.refresh_devices_page()
            if device_mac != 'default':
                self.utils.print_info("Getting status of Template with MAC: ", device_mac)
                device_row = self.get_device_row(device_mac)

            if device_row != -1:
                self.utils.print_info("Found a raw with mac :", device_mac)
                self.utils.print_info("Check if Template column is present")
                stack_template = self.devices_web_elements.get_device_stack_template(device_row)

            if device_row:
                sleep(5)
                device_updated_status = self.devices_web_elements.get_device_stack_template(device_row)
                self.utils.print_info("Device Template Column Status is :", device_updated_status)
                if "Assign/Create Template" in device_updated_status.text:
                    self.utils.print_info("Device Template Column Status: Assign/Create Template")
                    return 3

                elif "default-template" in device_updated_status.text:
                    self.utils.print_info("Device Template Column Status: Device default-template")
                    return 2
                else:
                    return 1

    def create_stack_auto_template(self, device_mac='default', name_stack_template='default'):
        """
        - This Keyword will create EXOS Stack Auto Template after assigned a policy to the stack
        - Keyword Usage
         - ``Get Template Status   device_mac=${DEVICE_MAC}``
         - ``Name Stack Template   ${Stack_TEMPLATE_NAME}``

        :param device_mac: device MAC address
        :param name_stack_template: Name of the stack_template
        :return: 1 If successfully Switch Stack template
        """

        self.navigator.navigate_to_devices()
        self.refresh_devices_page()
        device_row = -1

        if device_mac != 'default':

            if self.auto_actions.click(self.devices_web_elements.get_device_stack_template_click()) == -1:
                self.utils.print_info("Unable to click on Template Column button")
                return -1
            else:
                self.utils.print_info("Click on Template Column button")

            sleep(5)

            if self.auto_actions.click(self.devices_web_elements.get_create_template_click()) == -1:
                self.utils.print_info("Unable to click on Create template based on currently selected device button")
                return -1
            else:
                self.utils.print_info("Click on Create template based on currently selected device button")

            sleep(30)

            self.utils.print_info("Enter the switch Template Name: ", name_stack_template)
            self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                        name_stack_template)
            self.auto_actions.send_enter(self.sw_template_web_elements.get_sw_template_name_textfield())
            sleep(10)
        return 1

    def assign_network_policy_to_switch_mac(self, policy_name, mac):
        """
        - This keyword does a config push for a switch
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - Select Switch-->Update device
        - Keyword Usage:
         - ``Assign Policy To Switch  policy_name=${POLICY_NAME}  mac=${SWITCH_MAC}``

        :param policy_name: name of the network policy to deploy
        :param mac: mac number of the switch to select
        :return: 1 if policy is assigned, else -1
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info(f"Select switch row with serial {mac}")
        if not self.select_device(mac):
            self.utils.print_info(f"Switch {mac} is not present in the grid")
            return -1
        sleep(2)

        if not self._assign_policy_to_switch(policy_name):
            return -1

        policy_applied = self.get_ap_network_policy(ap_mac=mac)
        if policy_name.upper() == policy_applied.upper():
            self.utils.print_info("Applied network policy:{}".format(policy_applied))
            return 1
        self.utils.print_info(f"Policy applied:{policy_name} is not matching with policy updated:{policy_applied}")
        return -1

    def update_device_auto_template(self, device_mac, name_stack_template):
        """
        This function will go to Device Update and press create auto template and name the template

        :param device_mac: Mac of device

        :param name_stack_template: Policy template name
        :return: 1 if remain in the Create auto Template ; -1 else
        """

        if self.select_device(device_mac) == -1:
            self.utils.print_info("Device raw was not selected")
            return -1
        else:
            self.utils.print_info("Select Device row")

        if self.auto_actions.click(self.devices_web_elements.get_update_device_button()) == -1:
            self.utils.print_info("Unable to click on device update button")
            return -1
        else:
            self.utils.print_info("Click on device update button")

        if self.auto_actions.click(self.devices_web_elements.get_create_auto_template_update_device_click()) == -1:
            self.utils.print_info("Unable to click on Create template button")
            return -1
        else:
            self.utils.print_info("Click on Create template based on currently selected device button")

            sleep(10)

            self.utils.print_info("Enter the Device Template Name: ", name_stack_template)
            self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                        name_stack_template)
            self.auto_actions.send_enter(self.sw_template_web_elements.get_sw_template_name_textfield())

        return 1

    def get_ap_wifi2_power(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi2 power applied on AP using AP's serial number,Name or Mac address.
        - Flow : Manage ---> Devices
        - Keyword Usage:
         - ``Get Ap WIFI2 Power   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI2 Power   ap_name=${AP_NAME}``
         - ``Get Ap WIFI2 Power   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Transmission power value of wifi2 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        wifi2_power = self.get_device_details(search_string, 'WIFI2 POWER')
        if wifi2_power:
            return wifi2_power

    def get_ap_wifi2_channel(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi2 Channel applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI2 Channel   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI2 Channel   ap_name=${AP_NAME}``
         - ``Get Ap WIFI2 Channel   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Channel value of wifi2 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        wifi2_channel = self.get_device_details(search_string, 'WIFI2 CHANNEL')
        if wifi2_channel:
            return wifi2_channel

    def get_ap_wifi2_radio_profile(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi2 Radio Profile applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
         - ``Get Ap WIFI2 Radio Profile   ap_serial=${AP_SERIAL}``
         - ``Get Ap WIFI2 Radio Profile   ap_name=${AP_NAME}``
         - ``Get Ap WIFI2 Radio Profile   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048
        :param ap_name: Ap name Ex: AP1130
        :param ap_mac: Ap mac Ex: F09CE9F89600
        :return: Radio Profile value of wifi2 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()
        sleep(2)

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("WiFi2 Radio Profile")
        wifi2_radio_profile = self.get_device_details(search_string, 'WIFI2 RADIO PROFILE')
        if wifi2_radio_profile:
            return wifi2_radio_profile

    def perform_search_on_devices_table(self, the_value):
        """
        - Enters the search string value into the Search box on the Manage> Devices page.
        - Note: currently, search is only supported for Serial Number, MAC Address, or Host Name.
        - Keyword Usage:
         - ``Perform Search On Devices Table  ${SERIAL}``
         - ``Perform Search On Devices Table  ${HOST_NAME}``
         - ``Perform Search On Devices Table  ${MAC}``

        :param the_value: value to enter in the search box above the Devices table (Serial, MAC Address, or Host Name)
        :return  1 if action was successful, else -1
        """
        ret_val = 1
        search_field = self.devices_web_elements.get_manage_device_search_field()
        if search_field and the_value:
            self.utils.print_info(f"Entering '{the_value}' into search box")
            self.auto_actions.send_keys(search_field, the_value)
            sleep(5)
        else:
            self.utils.print_info("Unable to perform search")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def clear_search_on_devices_table(self):
        """
        - Clears the search field on the Manage> Devices page, if it is populated.
        - Keyword Usage:
         - ``Clear Search On Devices Table``

        :return  1 if action was successful, else -1
        """
        ret_val = 1

        clear_search_btn = self.devices_web_elements.get_manage_device_search_clear_button()
        if clear_search_btn:
            if clear_search_btn.is_displayed():
                self.utils.print_info("Clearing Devices table search field")
                self.auto_actions.click(clear_search_btn)
                sleep(5)
            else:
                self.utils.print_info("Search field's clear button is not displayed")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find search field's clear button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def verify_network_policy_column_is_not_sortable(self):
        """
        This keyword verifies whether the Devices grid's Network Policy column shows it is sortable or not in a tooltip
        :return 1 if we get a tool-tip message "Network Policy - This column is not sortable" else it returns -1
        """

        if self.devices_web_elements.get_device_np_header():
            self.auto_actions.move_to_element(self.devices_web_elements.get_device_np_header())

            sleep(5)
            self.screen.save_screen_shot()
            self.utils.print_info("Column Tooltip: ", self.devices_web_elements.get_ui_tool_tip_inner().text)

            if "Network Policy - This column is not sortable" in self.devices_web_elements.get_ui_tool_tip_inner().text:
                return 1

        return -1

    def get_column_header_tooltip(self, column_name):
        """
        This keyword verifies whether the Devices grid's Network Policy column shows it is sortable or not in a tooltip
        :return 1 if we get a tool-tip message eX: "Network Policy - This column is not sortable" else it returns -1
        """
        column_headers = self.devices_web_elements.get_devices_grid_column_headers()
        horizontal_scroll = False
        try:
            for column_header in column_headers:
                if column_name in column_header.text:
                    self.auto_actions.move_to_element(column_header)
                    sleep(5)
                    self.screen.save_screen_shot()
                    self.utils.print_info("Column Tooltip: ", self.devices_web_elements.get_ui_tool_tip_inner().text)

                    return self.devices_web_elements.get_ui_tool_tip_inner().text
        except AttributeError:
            return -1
        except:
            self.utils.print_info("Element not fond")
            horizontal_scroll = True

        if horizontal_scroll:
            horizontal_end_element = self.devices_web_elements.get_devices_page_horizontal_end()
            self.auto_actions.scroll_by_horizontal(horizontal_end_element)
            self.utils.print_info("Searching element by scrolling horizontal bar")
            try:
                for column_header in column_headers:
                    if column_name in column_header.text:
                        self.auto_actions.move_to_element(column_header)
                        sleep(5)
                        self.screen.save_screen_shot()
                        self.utils.print_info("Column Tooltip: ",self.devices_web_elements.get_ui_tool_tip_inner().text)

                        return self.devices_web_elements.get_ui_tool_tip_inner().text
            except AttributeError:
                return -1

        return -1

    def check_status_rebooting_cli(self, spawn, device_serial=None, device_mac=None):
        """
        This keyword gets status about the rebooting information from CLI .First will check the update status from the XIQ if IQagent loses connectivity during configuration in 10 minutes.
        - Keyword Usage:
        - ``Check status rebooting cli   ${SPAWN}       ${DEVICE_SERIAL}      ${DEVICE_MAC}``
        :param spawn: device spawn
        :param device_serial: serial number(s) of the device(s)
        :param device_mac:  device MAC address
        :return: 1 if gets information about rebooting from CLI else -1
        """
        if device_serial:
            check_status_update = self.check_device_update_status_rollback_reboot(device_serial, duration_retry=600)
        if device_mac:
            check_status_update = self.check_device_update_status_rollback_reboot(device_mac, duration_retry=600)

        if check_status_update == 1:
            pass
        else:
            self.utils.print_info("Expired time")
            return -1
        retry = 0
        while retry <= 10:
            output = self.cli.send_line_and_wait(spawn, "", 30)
            self.utils.print_info(output)
            if 'Rebooting switch as configuration caused disconnect' in output:
                self.utils.print_info("VOSS : 'CLOUD_AGENT INFO  Rebooting switch as configuration caused disconnect'")
                self.utils.print_info("Rebooting...")
                return 1
            elif 'Requesting system reboot' in output:
                self.utils.print_info("EXOS : 'Requesting system reboot'")
                self.utils.print_info("Rebooting...")
                return 1
            elif retry == 10:
                self.utils.print_info("No rebooting switch information not found or revert/reboot was not selected")
                return -1
            else:
                self.utils.print_info("Retrying")
                retry += 1
        return 1

    def check_device_update_status_rollback_reboot(self, device_serial=None, device_mac=None, duration_retry=300):
        """
        - This keyword is used to check the status of the device update in XIQ
        - It will poll the "update status" every 30 seconds
        - Assuming that config push will take a maximum of five minutes
        :param device_serial: device serial number to check the config push status
        :return: 1 if config push success else -1
        """
        retry_count = 0
        while retry_count <= 300:
            if device_serial:
                device_update_status = self.get_device_updated_status(device_serial)
            if device_mac:
                device_update_status = self.get_device_updated_status(device_mac)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                self.utils.print_info("Device updated successfully")
                break
            elif device_update_status == "Device Update Failed":
                self.utils.print_info("Device Update Failed")
                return 1
            elif retry_count == 300:
                self.select_device(device_serial)
                self.auto_actions.click(self.devices_web_elements.get_update_status_failed_selected_device)
                return -1
            sleep(duration_retry / 10)
            retry_count += 30
        return 1

    def get_update_devices_reboot_rollback(self, policy_name, option, device_serial=None, device_mac=None):
        """
        -This Keyword will Update Device Configuration with Reboot/Rollback option if the IQagent loses connectivity with XIQ during configuration
        - Keyword Usage:
         - ``Get update devices reboot rollback   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}``
        :param policy_name: Assign a policy for device
        :param option: Enable/Disable reboot/rollback option in Update Devices
        :param device_serial: serial number(s) of the device(s)
        :param device_mac:  device MAC address
        :return: 1 if update configuration is pushed on the device with Reboot/Rollback option
        """

        self.navigator.navigate_to_devices()
        self.utils.print_info("Check the Device is up")
        if device_serial:
            device_status = self.get_device_status(device_serial)
        if device_mac:
            device_status = self.get_device_status(device_mac)

        self.utils.print_info("Result is:", device_status)
        if device_status == 'green' or device_status == 'config audit mismatch':
            self.utils.print_info("Select the device")
            if device_serial:
                self.select_device(device_serial)
            if device_mac:
                self.select_device(device_mac)
        else:
            self.utils.print_info("Device is down")
            return -1

        self.utils.print_info("Check if device has policy")
        if self.devices_web_elements.get_assign_policy_device_selected():
            self.utils.print_info("Click on Assign Policy")
            self.auto_actions.click(self.devices_web_elements.get_assign_policy_device_selected())
            self.utils.print_info("Selecting '{}' policy".format(policy_name))
            self.utils.print_info("Click on network policy drop down")
            sleep(5)
            self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_drop_down())
            sleep(5)
            network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
            #self.auto_actions.scroll_down()
            sleep(5)
            if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                self.utils.print_info("Selected Network policy from drop down:{}".format(policy_name))
                sleep(2)
            else:
                self.utils.print_info("Network policy is not present in drop down")
                return -1
            self.utils.print_info("Click on network policy assign button")
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_button())
            sleep(5)
            if device_serial:
                self.select_device(device_serial)
            if device_mac:
                self.select_device(device_mac)
        else:
            self.utils.print_info("Device has already a policy")
            pass

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())

        self.utils.print_info("Select the network policy and configuration checkbox")
        update_cb = self.devices_web_elements.get_devices_switch_update_network_policy()
        reboot_rollback_check = self.devices_web_elements.get_devices_switch_update_reboot_rollback()
        sleep(3)
        if update_cb:
            if update_cb.is_selected():
                self.utils.print_info("Network policy and configuration checkbox is already selected")
                sleep(2)
            else:
                self.utils.print_info("Clicking network policy and configuration checkbox")
                self.auto_actions.click(update_cb)
                sleep(2)
        else:
            self.utils.print_info("Network policy and configuration checkbox not found")
            return -1

        if reboot_rollback_check:
            if option.lower() == "enable":
                if not reboot_rollback_check.is_selected():
                    self.utils.print_info("Check reboot and revert switch configuration option")
                    self.auto_actions.click(reboot_rollback_check)
                    sleep(2)
                else:
                    self.utils.print_info("Reboot/revert already checked")
            if option.lower() == "disable":
                if not reboot_rollback_check.is_selected():
                    self.utils.print_info("Reboot/revert option already unchecked")
                    sleep(2)
                else:
                    self.utils.print_info("Uncheck reboot and revert switch configuration option")
                    self.auto_actions.click(reboot_rollback_check)
                    sleep(2)
        else:
            self.utils.print_info("Reboot and revert switch configuration checkbox not found")
            return -1

        self.utils.print_info("Click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_devices_switch_update_btn())
        sleep(3)
        if option.lower() == "enable":
            self.utils.print_info("Proceed yes that user wants to continue with reboot/revert option")
            self.auto_actions.click(self.devices_web_elements.get_devices_update_yes_btn())
            sleep(2)
        else:
            pass
        return 1

    def get_check_update_failed_after_reboot(self, device_serial=None, device_mac=None):
        """
        This keyword gets information of the update failed status in XIQ for a device after reboot/rollback configuration
        - Keyword Usage:
         - ``Get check update failed after reboot   ${DEVICE_SERIAL} ``
         - ``Get check update failed after reboot   ${DEVICE_MAC} ``
        :param device_serial: Gets the information of the update failed status based on serial number
        :param device_mac:  Gets the information of the update failed status based on address MAC
        :return: 1 if the information was found else -1
        """
        if device_serial:
            self.select_device(device_serial)
        if device_mac:
            self.select_device(device_mac)
        self.utils.print_info("Checking the update the status")
        sleep(5)
        status = self.devices_web_elements.get_status_update_failed_after_reboot()
        if status != None and "The device was rebooted and reverted to previous configuration" in status:
            self.utils.print_info("Update status: ", status)
        else:
            self.utils.print_info("Update status not found")
            return -1
        return 1

    def check_pop_up_message_reboot_revert(self, policy_name, option, device_serial=None, device_mac=None):
        """
        -This Keyword will check the Reboot/Rollback option in Update Device Configuration has a pop-up message
        - Keyword Usage:
         - ``Check pop up message reboot revert   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}``
        :param policy_name: Assign a policy for device
        :param option: Enable/Disable reboot/rollback option in Update Devices
        :param device_serial: serial number(s) of the device(s)
        :param device_mac:  device MAC address
        :return: 1 if the pop-up message has been found else -1
        """
        self.navigator.navigate_to_devices()
        self.utils.print_info("Check the Device is up")
        if device_serial:
            device_status = self.get_device_status(device_serial)
        if device_mac:
            device_status = self.get_device_status(device_mac)

        self.utils.print_info("Result is:", device_status)
        if device_status == 'green' or device_status == 'config audit mismatch':
            self.utils.print_info("Select the device")
            if device_serial:
                self.select_device(device_serial)
            if device_mac:
                self.select_device(device_mac)
        else:
            self.utils.print_info("Device is down")
            return -1

        self.utils.print_info("Check if device has policy")
        if self.devices_web_elements.get_assign_policy_device_selected():
            self.utils.print_info("Click on Assign Policy")
            self.auto_actions.click(self.devices_web_elements.get_assign_policy_device_selected())
            self.utils.print_info("Selecting '{}' policy".format(policy_name))
            self.utils.print_info("Click on network policy drop down")
            self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_drop_down())
            network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
            self.auto_actions.scroll_down()
            sleep(5)
            if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                self.utils.print_info("Selected Network policy from drop down:{}".format(policy_name))
                sleep(2)
            else:
                self.utils.print_info("Network policy is not present in drop down")
                return -1
            self.utils.print_info("Click on network policy assign button")
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_button())
            sleep(5)
            self.select_device(device_serial)
        else:
            self.utils.print_info("Device has already a policy")
            pass

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())

        self.utils.print_info("Select the network policy and configuration checkbox")
        update_cb = self.devices_web_elements.get_devices_switch_update_network_policy()
        reboot_rollback_check = self.devices_web_elements.get_devices_switch_update_reboot_rollback()
        sleep(3)
        if update_cb:
            if update_cb.is_selected():
                self.utils.print_info("Network policy and configuration checkbox is already selected")
                sleep(2)
            else:
                self.utils.print_info("Clicking network policy and configuration checkbox")
                self.auto_actions.click(update_cb)
                sleep(2)
        else:
            self.utils.print_info("Network policy and configuration checkbox not found")
            return -1

        if reboot_rollback_check:
            if option.lower() == "enable":
                if not reboot_rollback_check.is_selected():
                    self.utils.print_info("Check reboot and revert switch configuration option")
                    self.auto_actions.click(reboot_rollback_check)
                    sleep(2)
                else:
                    self.utils.print_info("Reboot/revert already checked")
            if option.lower() == "disable":
                if not reboot_rollback_check.is_selected():
                    self.utils.print_info("Reboot/revert option already unchecked")
                    sleep(2)
                else:
                    self.utils.print_info("Uncheck reboot and revert switch configuration option")
                    self.auto_actions.click(reboot_rollback_check)
                    sleep(2)
        else:
            self.utils.print_info("Reboot and revert switch configuration checkbox not found")
            return -1

        pop_up_message = self.devices_web_elements.get_check_pop_message()
        pop_up_message_text = pop_up_message.text()

        if pop_up_message_text != None and "Not supported on Dell/SR" in pop_up_message_text:
            self.utils.print_info("", pop_up_message_text)
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_cancel_button())
            return 1
        else:
            self.utils.print_info("Pop-up message didn't find")
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_cancel_button())
            return -1

    def check_double_verification_display_rollback(self, policy_name, option, device_serial=None, device_mac=None):
        """
        -This Keyword will check the double verification is displayed for the Reboot/Rollback option in Update Device Configuration
        - Keyword Usage:
         - ``Check pop up message reboot revert   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}``
        :param policy_name: Assign a policy for device
        :param option: Enable/Disable reboot/rollback option in Update Devices
        :param device_serial: serial number(s) of the device(s)
        :param device_mac:  device MAC address
        :return: 1 if the double verification is displayed else -1
        """

        self.navigator.navigate_to_devices()
        self.utils.print_info("Check the Device is up")
        if device_serial:
            device_status = self.get_device_status(device_serial)
        if device_mac:
            device_status = self.get_device_status(device_mac)

        self.utils.print_info("Result is:", device_status)
        if device_status == 'green' or device_status == 'config audit mismatch':
            self.utils.print_info("Select the device")
            if device_serial:
                self.select_device(device_serial)
            if device_mac:
                self.select_device(device_mac)
        else:
            self.utils.print_info("Device is down")
            return -1

        self.utils.print_info("Check if device has policy")
        if self.devices_web_elements.get_assign_policy_device_selected():
            self.utils.print_info("Click on Assign Policy")
            self.auto_actions.click(self.devices_web_elements.get_assign_policy_device_selected())
            self.utils.print_info("Selecting '{}' policy".format(policy_name))
            self.utils.print_info("Click on network policy drop down")
            self.auto_actions.click(self.devices_web_elements.get_actions_assign_network_policy_drop_down())
            network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
            self.auto_actions.scroll_down()
            sleep(5)
            if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                self.utils.print_info("Selected Network policy from drop down:{}".format(policy_name))
                sleep(2)
            else:
                self.utils.print_info("Network policy is not present in drop down")
                return -1
            self.utils.print_info("Click on network policy assign button")
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_button())
            sleep(5)
            self.select_device(device_serial)
        else:
            self.utils.print_info("Device has already a policy")
            pass

        self.utils.print_info("Click on device update button")
        self.auto_actions.click(self.devices_web_elements.get_update_device_button())

        self.utils.print_info("Select the network policy and configuration checkbox")
        update_cb = self.devices_web_elements.get_devices_switch_update_network_policy()
        reboot_rollback_check = self.devices_web_elements.get_devices_switch_update_reboot_rollback()
        sleep(3)
        if update_cb:
            if update_cb.is_selected():
                self.utils.print_info("Network policy and configuration checkbox is already selected")
                sleep(2)
            else:
                self.utils.print_info("Clicking network policy and configuration checkbox")
                self.auto_actions.click(update_cb)
                sleep(2)
        else:
            self.utils.print_info("Network policy and configuration checkbox not found")
            return -1

        if reboot_rollback_check:
            if option.lower() == "enable":
                if not reboot_rollback_check.is_selected():
                    self.utils.print_info("Check reboot and revert switch configuration option")
                    self.auto_actions.click(reboot_rollback_check)
                    sleep(2)
                else:
                    self.utils.print_info("Reboot/revert already checked")
            if option.lower() == "disable":
                if not reboot_rollback_check.is_selected():
                    self.utils.print_info("Reboot/revert option already unchecked")
                    sleep(2)
                else:
                    self.utils.print_info("Uncheck reboot and revert switch configuration option")
                    self.auto_actions.click(reboot_rollback_check)
                    sleep(2)
        else:
            self.utils.print_info("Reboot and revert switch configuration checkbox not found")
            return -1

        self.utils.print_info("Click on perform update button")
        self.auto_actions.click(self.devices_web_elements.get_devices_switch_update_btn())
        sleep(3)

        double_verification = self.devices_web_elements.get_check_double_verification_display_rollback()

        if double_verification:
            self.utils.print_info("Display double verification")
            self.auto_actions.click(self.devices_web_elements.get_devices_update_no_btn())
            self.auto_actions.click(self.devices_web_elements.get_actions_network_policy_assign_cancel_button())
            return 1
        else:
            self.utils.print_info("Double verification doesn't appear")
            return -1

    def change_device_onboarding_date(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, days, serial_number, owner_id, rdc="g2r1"):
        '''
        This function change the onboarding date with specific number of days behind
        To use this function you need to have access to RDC database

        :param ip_dest_ssh: ip of 'Jump station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param days: The number of days passed from onboarding date
        :param serial_number: Serial number of device
        :param owner_id: Owner Id for XIQ account
        :param rdc: RDC name : e.g w1r1 , g2r1
        :return: 1 if onboarding date has been changed ; else -1
        '''
        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh,user_dest_ssh,pass_dest_ssh)
        if spawn == -1:
            return -1
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            self.robot_built_in.skip('The .ssh folder does not exist')
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if not "ahdev_id_rsa" in output_cmd_ls:
            self.robot_built_in.skip('No ssh certificate exist on jump station')
            return -1
        output_cmd = self.cli.send_pxssh(spawn ,"ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlconfigdb_1")
        output_cmd3 = self.cli.send_pxssh(spawn,
                "select created_at,updated_at,agent_id,owner_id from hm_device where owner_id={};".format(owner_id))
        output_cmd4 = ''
        if isinstance(serial_number, list) and isinstance(days, list):
            cnt = 0
            for el in serial_number:
                output_cmd4 =output_cmd4 + self.cli.send_pxssh(spawn,
                "update hm_device set created_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY'),"
                "updated_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY')"
                "where serial_number = '{}' and owner_id = {};".format(days[cnt],days[cnt],el,owner_id))
                cnt = cnt + 1
        else:
            output_cmd4 =self.cli.send_pxssh(spawn,
            "update hm_device set created_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY'),"
            "updated_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY')"
            "where serial_number = '{}' and owner_id = {};".format(days, days, serial_number, owner_id))
        output_cmd5 = self.cli.send_pxssh(spawn,
                    "select created_at,updated_at,agent_id,owner_id from hm_device where owner_id={};".format(owner_id))
        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)
        self.utils.print_info(output_cmd4)
        self.utils.print_info(output_cmd5)
        self.cli.close_spawn(spawn)
        return 1

    def max_device_num_from_hm_vhm_account_table(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, vhm_id, rdc="g2r1"):
        '''
        This function returns the number of devices which can be onboarded
        To use this function you need to have access to RDC database

        :param ip_dest_ssh: ip of 'Jump station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param vhm_id: VHM Id for XIQ account
        :param rdc: RDC name : e.g w1r1 , g2r1
        :return: number of devices which can be onboarded  ; else -1
        '''

        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            self.robot_built_in.skip('The .ssh folder does not exist')
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if not "ahdev_id_rsa" in output_cmd_ls:
            self.robot_built_in.skip('No ssh certificate exist on jump station')
            return -1
        output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlsystemdb")
        output_cmd3 = self.cli.send_pxssh(spawn,
                                          "select id, customer_id, customer_mode, managed_device_num,max_device_num,vhm_id from hm_vhm_account where vhm_id ='{}';".format(
                                              vhm_id))
        output_cmd4 = self.cli.send_pxssh(spawn,
                                          "select vhm_id,max_device_num from hm_vhm_account where vhm_id ='{}';".format(
                                              vhm_id))
        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)
        self.utils.print_info(output_cmd4)
        pattern = vhm_id + "\\s+\\|\\s+(\\d+)"
        max_devices = self.utils.get_regexp_matches(output_cmd4, pattern, 1)
        self.utils.print_info(max_devices)
        self.cli.close_spawn(spawn)
        return max_devices[0]

    def check_update_time_on_rdc(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, rdc="g2r1"):
        '''
        This function returns the update time interval for RDC

        :param ip_dest_ssh: ip of 'Jump station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param rdc: RDC name : e.g w1r1 , g2r1
        :return: interval time and interval unit ; else -1
        '''

        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            self.robot_built_in.skip('The .ssh folder does not exist')
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if not "ahdev_id_rsa" in output_cmd_ls:
            self.robot_built_in.skip('No ssh certificate exist on jump station')
            return -1
        output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlscheduledb")
        output_cmd3 = self.cli.send_pxssh(spawn,
                        "select id,interval,interval_unit from hm_job_trigger where id in "
                        "(select job_trigger_id from hm_job where name = 'validate Gemalto license for Cloud task');")

        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)

        pattern1 = "\\d+\\s+\\|\\s+(\\d+)\\s+\\|\\s+\\w+"
        pattern2 = "\\d+\\s+\\|\\s+\\d+\\s+\\|\\s+(\\w+)"
        update_time = self.u.get_regexp_matches(output_cmd3, pattern1, 1)
        update_unit = self.utils.get_regexp_matches(output_cmd3, pattern2, 1)
        self.utils.print_info(update_time[0])
        self.utils.print_info(update_unit[0])
        self.cli.close_spawn(spawn)
        if update_time[0] and update_unit[0]:
            return update_time[0], update_unit[0]
        else:
            self.utils.print_info("Interval time was not found")
            return -1

    def get_banner_messages(self, expected_message):
        '''
        This function compares a message from banner with expected_message

        :param expected_message:
        :return: 1 if expected message was found in banner ; else -1
        '''

        all_error_messages = self.devices_web_elements.get_all_messages_banner()
        self.utils.print_info(all_error_messages)
        if all_error_messages:
            for el2 in all_error_messages:
                self.utils.print_info("Messages from banner are : ",el2.text)
        else:
            self.utils.print_info("No message was found:",expected_message)
            self.screen.save_screen_shot()
            return -1
        for el in all_error_messages:
            if str(expected_message) in el.text:
                self.utils.print_info("Message found")
                return 1
            else:
                pass
        return -1

    def move_to_free_pilot_from_trial_or_connect(self):
        '''
        This function moves XIQ account into free pilot mode by using the link from banner
        :return: 1 if account was moved ; else -1
        '''

        update_button = self.devices_web_elements.get_upgrade_to_free_pilot_link()
        if update_button:
            self.utils.print_info("Upgrade ... ")
            self.auto_actions.click(update_button)
            yes_button = self.devices_web_elements.get_yes_button_upgrade_to_free_pilot()
            if yes_button:
                self.utils.print_info("press yes ... ")
                self.auto_actions.click(yes_button)
            else:
                self.utils.print_info("yes button not found  ... ")
                return -1
        else:
            self.utils.print_info("Upgrade button not found ")
            return -1
        return 1

    def activate_device_license(self, device_serial, license_type, username = None, password = None, shared_cuid = None):
        '''
        This function activate premier or macsec license on a device

        :param device_serial: Serial of device
        :param license_type: premier or macsec
        :return: 1 if license was activated ; else -1
        '''

        select_flag = False
        for el in device_serial.split(','):
            if self.select_device(el):
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True
            else:
                self.utils.print_info("Device with serial {} was not been selected".format(el))

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())
            sleep(2)

        self.utils.print_info("Select Manage Device License ")
        manage_license = self.device_actions.get_device_actions_manage_license()
        self.utils.print_info(manage_license)
        if manage_license:
            self.utils.print_info("Select Manage Device License ")
            self.auto_actions.move_to_element(manage_license)
            sleep(2)
        else:
            self.utils.print_info("Manage Device License not found")
            self.screen.save_screen_shot()
            return -1

        premier_button = self.device_actions.get_activate_license()
        if premier_button:
            self.utils.print_info("Activate license")
            self.auto_actions.move_to_element(premier_button)
        else:
            self.utils.print_info("Button not found ")
            return -1

        if license_type == 'premier':
            premier_act_button = self.device_actions.get_act_premier_btn()
            self.utils.print_info(premier_act_button)
            if premier_act_button:
                self.utils.print_info("Press Premier button")
                self.auto_actions.click(premier_act_button)
            else:
                self.utils.print_info("Button not found ")
                return -1
        elif license_type == 'macsec':
            macsec_button = self.device_actions.get_act_macsec_btn()
            if macsec_button:
                self.utils.print_info("Press Macsec license")
                self.auto_actions.click(macsec_button)
            else:
                self.utils.print_info("Button not found ")
                return -1
        else:
            return -1
        yes_confirmation = self.device_actions.get_yes_confirmation()
        if yes_confirmation:
            self.utils.print_info("yes confirmation button was found ")
            self.auto_actions.click(yes_confirmation)
            sleep(20)
            check_portal_page = self.devices_web_elements.get_check_portal_page()
            if check_portal_page:
                if self.login_to_extreme_portal(username, password, shared_cuid) == 1:
                    self.utils.print_info("Login to extreme portal")
                    return 1
                else:
                    return -1
            else:
                self.utils.print_info("Login to extreme portal page was not displayed ")
        else:
            self.utils.print_info("yes confirmation button was not found ")
            return -1
        return 1

    def revoke_device_license(self, device_serial,license_type, username = None, password = None, shared_cuid = None):
        '''
        This function revoke premier or macsec license on a device

        :param device_serial: Serial of device
        :param license_type: premier or macsec
        :return: 1 if license was revoked ; else -1
        '''

        select_flag = False
        for el in device_serial.split(','):
            if self.select_device(el):
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True
            else:
                self.utils.print_info("Device with serial {} was not been selected".format(el))

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())
            sleep(2)

        self.utils.print_info("Select Manage Device License ")
        manage_license = self.device_actions.get_device_actions_manage_license()
        if manage_license:
            self.utils.print_info("Select Manage Device License ")
            self.auto_actions.move_to_element(manage_license)
            sleep(2)
        else:
            self.utils.print_info("Manage Device License not found")
            self.screen.save_screen_shot()
            return -1

        premier_button = self.device_actions.get_revoke_license()
        if premier_button:
            self.utils.print_info("Revoke license")
            self.auto_actions.move_to_element(premier_button)
        else:
            self.utils.print_info("Button not found ")
            return -1
        if license_type == 'premier':
            premier_rev_button = self.device_actions.get_rev_premier_btn()
            if premier_rev_button:
                self.utils.print_info("Press Premier button")
                self.auto_actions.click(premier_rev_button)
            else:
                self.utils.print_info("Button not found ")
                return -1
        elif license_type == 'macsec':
            macsec_button = self.device_actions.get_rev_macsec_btn()
            if macsec_button:
                self.utils.print_info("Press Macsec license")
                self.auto_actions.click(macsec_button)
            else:
                self.utils.print_info("Button not found ")
                return -1
        else:
            return -1
        yes_confirmation = self.device_actions.get_yes_confirmation()
        if yes_confirmation:
            self.utils.print_info("yes confirmation button was found ")
            self.auto_actions.click(yes_confirmation)
            sleep(20)
            check_portal_page = self.devices_web_elements.get_check_portal_page()
            if check_portal_page:
                if self.login_to_extreme_portal(username, password, shared_cuid) == 1:
                    self.utils.print_info("Login to extreme portal")
                    return 1
                else:
                    return -1
            else:
                pass
        else:
            self.utils.print_info("yes confirmation button was not found ")
            return -1
        return 1

    def check_license_status(self, device_sn, max_time=180, time_interval=10):
        """
        - This keyword is used to check the status of the device license
        - It will poll the "license status" at every time_interval seconds
        :param device_sn: Device serial
        :param max_time: Maximum duration of check
        :param time_interval: Time interval between two consecutive checks
        :return: returns the status displayed into device license field (NONE; PREMIER; MACSEC or PREMIER,MACSEC ) +
        error message if it is present ;else -1
        """
        self.utils.print_info("Start checking the status for device license")
        sleep(20)
        retry_count = 0
        try_one_more_time_to_confirm_error = False
        try_one_more_time = None
        error = ''
        while retry_count <= max_time or try_one_more_time:
            rows = self.devices_web_elements.get_grid_rows()
            if rows:
                for row in rows:
                    if device_sn in row.text:
                        self.utils.print_debug("Found device Row: ", self.format_row(row.text))
                        license_form_error = self.devices_web_elements.get_license_form_error(row)
                        if license_form_error:
                            if try_one_more_time_to_confirm_error:
                                self.utils.print_info("Final status is {} ".format(license_form_error.get_attribute("title")))
                                error = ' ' + license_form_error.get_attribute("title")
                            else:
                                if try_one_more_time:
                                    try_one_more_time = None
                                    max_time += 2 * time_interval
                                else:
                                    pass
                                try_one_more_time_to_confirm_error = True
                                self.utils.print_info("Try one more time to confirm the result :", license_form_error.text)
                        else:
                            pass
                        field_license_stat = self.devices_web_elements.get_field_license_stat(row)
                        if field_license_stat:
                            self.utils.print_info("Actual status is {} ".format(field_license_stat.text + error))
                            if 'None' in field_license_stat.text:
                                if try_one_more_time == 'None':
                                    self.utils.print_info("Final status is {} ".format(field_license_stat.text + error))
                                    return 'None' + error
                                else:
                                    try_one_more_time = 'None'
                                    self.utils.print_info("Try one more time to confirm the result :", try_one_more_time)
                                    sleep(10)
                            elif '%' in field_license_stat.text:
                                self.utils.print_info("After {} sec the status is ".format(retry_count, field_license_stat.text))
                                sleep(10)
                            elif 'PREMIER' in field_license_stat.text and 'MACSEC' in field_license_stat.text:
                                if try_one_more_time == 'PREMIER,MACSEC':
                                    self.utils.print_info("Final status is {} ".format(field_license_stat.text + error))
                                    return 'PREMIER,MACSEC' + error
                                else:
                                    try_one_more_time = 'PREMIER,MACSEC'
                                    self.utils.print_info("Try one more time to confirm the result :", try_one_more_time)
                                    sleep(10)
                            elif 'MACSEC' == field_license_stat.text:
                                if try_one_more_time == 'MACSEC':
                                    self.utils.print_info("Final status is {} ".format(field_license_stat.text + error))
                                    return 'MACSEC' + error
                                else:
                                    try_one_more_time = 'MACSEC'
                                    self.utils.print_info("Try one more time to confirm the result :", try_one_more_time)
                                    sleep(10)
                            elif 'PREMIER' == field_license_stat.text:
                                if try_one_more_time == 'PREMIER':
                                    self.utils.print_info("Final status is {} ".format(field_license_stat.text + error))
                                    return 'PREMIER' + error
                                else:
                                    try_one_more_time = 'PREMIER'
                                    self.utils.print_info("Try one more time to confirm the result :", try_one_more_time)
                                    sleep(10)
                            else:
                                self.utils.print_info("field_license_stat has unexpected value")
                        else:
                            self.utils.print_info("field_license_stat not found")
                            return -1
                        break
                    else:
                        pass
                self.refresh_devices_page()
                sleep(time_interval)
                self.utils.print_info(f"Time elapsed for license update: {retry_count} seconds")
                retry_count += time_interval
            else:
                self.utils.print_debug("No row found")
                return -1
        self.utils.print_info("return -1  ")
        return -1

    def pilot_lic_inventory_from_unmanage_box(self, max_time=120, interval_time=20):
        '''
        This function returns the number of license which should be consumed and the number of license available from
        unmanage box. These are displayed into this format   e.g.  1/0
        :param max_time: Maximum duration of check
        :param interval_time: Time interval between two consecutive checks
        :return: the number of license which should be consumed and the number of license available from
        unmanage box. These are displayed into this format   e.g.  1/0  ; else -1
        '''

        pilot_inventory_found = False
        cnt = 0
        while cnt < max_time:
            check_unmanage_box = self.devices_web_elements.get_check_unmanage_box()
            self.utils.print_info(check_unmanage_box)
            if check_unmanage_box:
                pilot_lic_inventory = self.devices_web_elements.get_pilot_lic_inventory()
                if pilot_lic_inventory:
                    if '/' in pilot_lic_inventory.text:
                        self.utils.print_info("Am ajuns aici")
                        pilot_inventory_found = pilot_lic_inventory.text
                        break
                else:
                    self.utils.print_info("The unmanage box is displayed but device inventory not found  ")
            else:
                self.utils.print_info("The unmanage box not found  ")
            sleep(interval_time)
            cnt = cnt + interval_time
            self.utils.print_info("Time", cnt)
        if pilot_inventory_found:
            self.utils.print_info("The unmanage box was found: ", pilot_inventory_found)
            return pilot_inventory_found
        else:
            self.utils.print_info("The unmanage box not found: ", pilot_inventory_found)
            return -1

    def check_serial_list(self, serial):
        '''
        This function checks if a device or more need a Pilot License in next 15 days. The list from banner is cheked

        :param serial: a serial or more
        :return: 1 if the SN or SNs are into serial list from banner ; else -1
        '''

        serial_list = serial.split(",")
        self.utils.print_info(len(serial_list))

        sn_button = self.devices_web_elements.get_sn_button()
        if sn_button:
            self.utils.print_info("Sn button was found ")
            self.auto_actions.click(sn_button)
        else:
            self.utils.print_info("Sn button was not found ")
            return -1
        result_found = []
        result_duplicate = []
        sn_xiq_list = self.devices_web_elements.get_sn_xiq_list()
        self.utils.print_info(type(sn_xiq_list))
        if sn_xiq_list:
            if len(serial_list) > 1:
                cnt = 0
                for sn_input in serial_list:
                    result_found.append(False)
                    result_duplicate.append(False)
                    for sn_xiq in sn_xiq_list:
                        if sn_input == sn_xiq.text:
                            if result_found[cnt]:
                                result_duplicate[cnt] = True
                            else:
                                pass
                            result_found[cnt] = True
                        else:
                            pass
                    cnt = cnt + 1
                cnt2 = 0
                for el in result_found:
                    if el:
                        if result_duplicate[cnt2]:
                            self.utils.print_info("The serial {} was found twice ".format(serial_list[cnt2]))
                            return -1
                        else:
                            self.utils.print_info("The serial {} was found ".format(serial_list[cnt2]))
                    else:
                        self.utils.print_info("The serial {} was not found  ".format(serial_list[cnt2]))
                    cnt2 = cnt2 + 1
            else:
                sn_was_found = None
                for sn_xiq in sn_xiq_list:
                    if serial == sn_xiq.text:
                        if sn_was_found:
                            self.utils.print_info("The serial {} was found twice ".format(serial))
                            return -1
                        sn_was_found = True
                    else:
                        pass
                if sn_was_found:
                    self.utils.print_info("The serial {} was found ".format(serial))
                    sn_close = self.devices_web_elements.get_sn_close()
                    if sn_close:
                        self.utils.print_info("Close button was found")
                        self.auto_actions.click(sn_close)
                    else:
                        self.utils.print_info("Close button was not found")
                        return -1
                    return 1
                else:
                    self.utils.print_info("The serial {} was not found ".format(serial))
                    return -1
        else:
            self.utils.print_info("The list is empty or it was not found ")
            return -1
        sn_close = self.devices_web_elements.get_sn_close()
        if sn_close:
            self.utils.print_info("Close button was found")
            self.auto_actions.click(sn_close)
        else:
            self.utils.print_info("Close button was not found")
            return -1
        return 1

    def link_to_sfdc_from_unmanage_box(self, username, password, shared_cuid = None):
        '''
        This function links the XIQ account to SFDC by using the 'ADD LICENSE' button from unmanage dialog
        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid
        :return: 1 if account was linked ; else -1
        '''

        add_a_license = self.devices_web_elements.get_add_a_license()
        if add_a_license:
            self.utils.print_info("ADD a license button was found ")
            self.auto_actions.click(add_a_license)
        else:
            self.utils.print_info("ADD a license button was not found ")
            return -1

        sleep(2)
        get_link_my_account = self.devices_web_elements.get_link_my_account()
        if get_link_my_account:
            self.utils.print_info(" 'Link my extreme portal' button was found ")
            self.auto_actions.click(get_link_my_account)
        else:
            self.utils.print_info("'Link my extreme portal' button was not found ")
            return -1

        sleep(2)
        get_link_my_account_agree = self.devices_web_elements.get_link_my_account_agree()
        if get_link_my_account_agree:
            self.utils.print_info(" Checkbox Agree was found ")
            self.auto_actions.click(get_link_my_account_agree)
        else:
            self.utils.print_info("Checkbox Agree was not found ")
            return -1

        link_my_account_continue = self.devices_web_elements.get_link_my_account_continue()
        if link_my_account_continue:
            self.utils.print_info("Continue button was found ")
            self.auto_actions.click(link_my_account_continue)
        else:
            self.utils.print_info("Continue  button was not found ")
            return -1
        sleep(10)
        return self.login_to_extreme_portal(username, password, shared_cuid)

    def move_to_pilot_mode_from_unmanage_box(self):
        '''
        This function move the XIQ account from free pilot or trial mode into pilot mode by using the 'ADD LICENSE'
        button from unmanage dialog
        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid
        :return: 1 if account was moved into Pilot mode  ; else -1
        '''

        add_a_license = self.devices_web_elements.get_add_a_license()
        if add_a_license:
            self.utils.print_info("ADD a license button was found ")
            self.auto_actions.click(add_a_license)
        else:
            self.utils.print_info("ADD a license button was not found ")
            return -1
        sleep(2)
        upgrade_account_to_pilot = self.devices_web_elements.get_upgrade_account_to_pilot()
        if upgrade_account_to_pilot:
            self.utils.print_info(" 'UPGRADE ACCOUNT' button was found ")
            self.auto_actions.click(upgrade_account_to_pilot)
        else:
            self.utils.print_info("'UPGRADE ACCOUNT' button was not found ")
            return -1
        sleep(2)
        get_link_my_account_agree = self.devices_web_elements.get_link_my_account_agree()
        if get_link_my_account_agree:
            self.utils.print_info(" Checkbox Agree was found ")
            self.auto_actions.click(get_link_my_account_agree)
        else:
            self.utils.print_info("Checkbox Agree was not found ")
            return -1
        link_my_account_continue = self.devices_web_elements.get_link_my_account_continue()
        if link_my_account_continue:
            self.utils.print_info("Continue button was found ")
            self.auto_actions.click(link_my_account_continue)
        else:
            self.utils.print_info("Continue  button was not found ")
            return -1
        sleep(10)
        return 1

    def check_upgrade_account_button(self):
        '''
        This function presses the upgrade account button

        :return: 1 if account button was pressed  ; else -1
        '''

        upgrade_account_to_pilot = self.devices_web_elements.get_upgrade_account_to_pilot()
        if upgrade_account_to_pilot:
            self.utils.print_info(" 'UPGRADE ACCOUNT' button was found ")
            self.auto_actions.click(upgrade_account_to_pilot)
        else:
            self.utils.print_info("'UPGRADE ACCOUNT' button was not found ")
            return -1
        return 1

    def login_to_extreme_portal(self, username, password, shared_cuid = None):
        '''
        This function enters the credentials when SFDC page is displayed
        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid
        :return: 1 if the credentials were entered ; else -1
        '''

        sfdc_username = self.devices_web_elements.get_sfdc_username()
        if sfdc_username:
            self.utils.print_info("Entering Salesforce username")
            self.auto_actions.send_keys(sfdc_username, username)
            sleep(2)
            self.screen.save_screen_shot()
        else:
            self.utils.print_info("Entering Salesforce page was not found ")
            return -1

        self.utils.print_info("Entering Salesforce password")
        self.auto_actions.send_keys(self.devices_web_elements.get_sfdc_password(), password)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Submitting")
        self.auto_actions.click(self.devices_web_elements.get_sfdc_submit())
        sleep(2)
        self.screen.save_screen_shot()

        sfdc_submit_check_error = self.devices_web_elements.get_sfdc_submit_check_error()
        if sfdc_submit_check_error:
            self.utils.print_info("The below error was displayed:", sfdc_submit_check_error.text)
            self.screen.save_screen_shot()
            return -1
        else:
            pass

        sleep(10)
        enter_shared_cuid = self.devices_web_elements.get_enter_shared_cuid()
        if enter_shared_cuid:
            self.auto_actions.send_keys(enter_shared_cuid, shared_cuid)
            submit_shared_cuid = self.devices_web_elements.get_submit_shared_cuid()
            if submit_shared_cuid:
                self.utils.print_info("submit button was found")
                self.auto_actions.click(submit_shared_cuid)
            else:
                self.utils.print_info("submit button not found ")
                return -1
            check_error_shared_cuid = self.devices_web_elements.get_check_error_shared_cuid()
            if check_error_shared_cuid:
                self.utils.print_info("The below error was displayed when enter shared CUID:", check_error_shared_cuid.text)
                self.screen.save_screen_shot()
                return -1
            else:
                return 1
        else:
            self.utils.print_info("shared cuid dialog is not displayed ")
            license_button = self.devices_web_elements.get_license_button()
            if license_button:
                self.utils.print_info("submit button was found")
                self.auto_actions.click(license_button)
                sleep(10)
                self.screen.save_screen_shot()
                enter_shared_cuid = self.devices_web_elements.get_enter_shared_cuid()
                if enter_shared_cuid:
                    self.auto_actions.send_keys(enter_shared_cuid, shared_cuid)
                    submit_shared_cuid = self.devices_web_elements.get_submit_shared_cuid()
                    if submit_shared_cuid:
                        self.screen.save_screen_shot()
                        self.utils.print_info("submit button was found")
                        self.auto_actions.click(submit_shared_cuid)
                    else:
                        self.screen.save_screen_shot()
                        self.utils.print_info("submit button not found ")
                        return -1
                    check_error_shared_cuid = self.devices_web_elements.get_check_error_shared_cuid()
                    if check_error_shared_cuid:
                        self.utils.print_info("The below error was displayed when enter shared CUID:",
                                              check_error_shared_cuid.text)
                        self.screen.save_screen_shot()
                        return -1
                    else:
                        return 1
                else:
                    pass
            else:
                pass
        return 1

    def check_unlink_button(self):
        '''
        This function checks if the unlink button is present

        :return: 1 if unlink button is present ; else -1
        '''
        sfdc_unlink = self.devices_web_elements.get_sfdc_unlink()
        if sfdc_unlink:
            return 1
        else:
            return -1

    def unlink_sfdc_account(self):
        '''
        This function presses the unlink button from License Management page
        :return: 1 if the account was unlinked ; else -1
        '''
        self.utils.print_info("Starting unlink")
        sfdc_unlink = self.devices_web_elements.get_sfdc_unlink()
        if sfdc_unlink:
            self.auto_actions.click(sfdc_unlink)
            yes_button_unlink = self.devices_web_elements.get_yes_button_unlink()
            if yes_button_unlink:
                self.utils.print_info("press yes confirmation")
                self.auto_actions.click(yes_button_unlink)
            else:
                self.utils.print_info("confirmation button was not found ")
            self.login.refresh_page()
            if self.check_unlink_button() == -1:
                self.utils.print_info("the account was unlinked")
                return 1
            else:
                self.utils.print_info("the account was not unlinked ")
                return -1
        else:
            self.utils.print_info("unlink button was not found ")
            return -1


    def check_pilot_license_consumption(self, expected_available, expected_activated, license_type = "PRD-XIQ-PIL-S-C",
                                        max_time=600, interval_check_time=60):
        '''
        This function checks if the available and activated licenses are displayed as expected into License Management page
        :param expected_available: Number of expected available licenses
        :param expected_activated: Number of expected activated license
        :param license_type: type of license
        :param max_time: Maximum duration of check
        :param interval_check_time: time interval between two consecutive checks
        :return:
        '''

        cnt = 0
        while cnt < max_time:
            available = 0
            activated = 0
            sleep(5)
            license_mgmt = self.devices_web_elements.get_license_mgmt()
            if license_mgmt:
                self.utils.print_info("license_mgmt button was found ")
                self.auto_actions.click(license_mgmt)
            else:
                self.utils.print_info("license_mgmt button was not found ")
                return -1

            subscription_rows = self.devices_web_elements.get_subscription_rows()
            if subscription_rows:
                self.utils.print_info("Found {} subscription rows".format(len(subscription_rows)))
                if len(subscription_rows) > 1:
                    self.utils.print_info("Many subscription rows were found ")
                else:
                    pass
                for el in subscription_rows:
                    if license_type in el.text:
                        subscription_available = self.devices_web_elements.get_subscription_available(el)
                        if subscription_available:
                            self.utils.print_info("Pilot license available : ", subscription_available.text)
                            available += int(subscription_available.text)
                        else:
                            self.utils.print_info("subscription_available element was not found ")
                            return -1
                        subscription_activated = self.devices_web_elements.get_subscription_activated(el)
                        if subscription_activated:
                            self.utils.print_info("Pilot license activated : ", subscription_activated.text)
                            activated += int(subscription_activated.text)
                        else:
                            self.utils.print_info("subscription_activated element was not found ")
                            return -1
                    else:
                        pass
                if available == int(expected_available) and activated == int(expected_activated):
                    self.utils.print_info(
                        "Available Expected {} ; Displayed in XIQ {}: ".format(expected_available,
                                                                               subscription_available.text))
                    self.utils.print_info(
                        "Activated Expected {} ; Displayed in XIQ {}: ".format(expected_activated,
                                                                               subscription_activated.text))
                    return 1
                else:
                    pass
            else:
                self.utils.print_info("license_mgmt button was not found ")
                return -1
            sleep(interval_check_time)
            cnt = cnt + interval_check_time
            self.utils.print_info("Waited {} sec".format(cnt))
            self.login.refresh_page()
        self.utils.print_info("Available and activated values from XIQ do not match with the expected values ")
        self.utils.print_info("Available Expected {} ; Displayed in XIQ {}: ".format(expected_available, available))
        self.utils.print_info("Activated Expected {} ; Displayed in XIQ {}: ".format(expected_activated, activated))
        return -1

    def check_long_sn_or_legacy_sn_mapping(self, device_serial, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, rdc="g2r1"):
        '''
        This function checks if the SN for 5520 has short or long format . If the function has short format the sn will be
        searched into extr_legacy_sn_mapping table
        :param ip_dest_ssh: ip of 'Jump Station'
        :param user_dest_ssh: SFDC username account
        :param pass_dest_ssh: SFDC password account
        :param rdc: The RDC name . e.g. w1r1 ,w1r3 ,g2r1
        :return: 1 if SN has long format or if it is into db ; else -1
        '''

        if len(device_serial) > 11:
            self.utils.print_info("device SN has long format")
            return 1
        else:
            spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
            output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
            output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
            if "No such file or directory" in output_cmd_cd:
                self.robot_built_in.skip('The .ssh folder does not exist')
            else:
                self.cli.send_pxssh(spawn, "cd ..")
            if not "ahdev_id_rsa" in output_cmd_ls:
                self.robot_built_in.skip('No ssh certificate exist on jump station')
                return -1
            output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc))
            self.utils.print_info(output_cmd)
            output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
            output_cmd2 = self.cli.send_pxssh(spawn, "psqlsystemdb")
            output_cmd3 = self.cli.send_pxssh(spawn,
                            "select * from extr_legacy_sn_mapping where serial_number='{}';".format(device_serial))
            self.utils.print_info(output_cmd)
            self.utils.print_info(output_cmd1)
            self.utils.print_info(output_cmd2)
            self.utils.print_info(output_cmd3)
            pattern1 = "\\((\\d+)\\s+row"
            rows = self.utils.get_regexp_matches(output_cmd3, pattern1, 1)
            self.utils.print_info(rows)
            self.cli.close_spawn(spawn)
            if int(rows[0]) == 1:
                self.utils.print_info("device Sn is into extr_legacy_sn_mapping table")
                return 1
            else:
                self.utils.print_info("device Sn is not into extr_legacy_sn_mapping table or multiple entries were found")
                return -1

    def check_message_unlink_button(self, expected_message):
        '''
        This function checks if the message is correct when try to unlink
        :param expected_message: Expected message
        :return: 1 if expected message was found ; else -1
        '''

        sfdc_unlink_button = self.devices_web_elements.get_sfdc_unlink()
        if sfdc_unlink_button:
            self.auto_actions.move_to_element(sfdc_unlink_button)
            sleep(10)
        else:
            self.utils.print_info("'Unlink' button was not found ")
            return -1
        message_unlink_button = self.devices_web_elements.get_message_unlink_button()
        if message_unlink_button:
            self.utils.print_info("Message was found :", message_unlink_button.text)
            if expected_message in message_unlink_button.text:
                self.utils.print_info("Messages match")
                return 1
            else:
                self.utils.print_info("The messages are not matching")
                return -1
        else:
            self.utils.print_info("Message was not found ")
        return -1

    def link_to_sfdc_from_license_management_page(self, username, password, shared_cuid=None):
        '''
        This function links the XIQ account to SFDC and will move the account to Pilot mode from License Management page
        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid
        :return: 1 if account was linked ; else -1
        '''

        if not self.navigator.navigate_to_license_management() == 1:
            return -1

        sleep(2)
        get_link_my_account = self.devices_web_elements.get_link_my_account()
        if get_link_my_account:
            self.utils.print_info(" 'Link my extreme portal' button was found ")
            self.auto_actions.click(get_link_my_account)
        else:
            self.utils.print_info("'Link my extreme portal' button was not found ")
            return -1

        sleep(2)
        get_link_my_account_agree = self.devices_web_elements.get_link_my_account_agree()
        if get_link_my_account_agree:
            self.utils.print_info(" Checkbox Agree was found ")
            self.auto_actions.click(get_link_my_account_agree)
        else:
            self.utils.print_info("Checkbox Agree was not found ")
            return -1

        link_my_account_continue = self.devices_web_elements.get_link_my_account_continue()
        if link_my_account_continue:
            self.utils.print_info("Continue button was found ")
            self.auto_actions.click(link_my_account_continue)
        else:
            self.utils.print_info("Continue  button was not found ")
            return -1
        sleep(10)
        return self.login_to_extreme_portal(username, password, shared_cuid)

    def get_audit_log(self):
        '''
        This function returns the date for the last log from audit
        :return: the date of last log ; else -1
        '''

        user_button = self.devices_web_elements.get_user_button()
        if user_button:
            self.utils.print_info("User button was found ")
            self.auto_actions.move_to_element(user_button)
        else:
            self.utils.print_info("User button was not found ")
            return -1

        global_settings = self.devices_web_elements.get_global_settings()
        if global_settings:
            self.utils.print_info("global_settings was found ")
            self.auto_actions.click(global_settings)
        else:
            self.utils.print_info("global_setting was not found ")
            return -1

        audit_button = self.devices_web_elements.get_audit_button()
        if audit_button:
            self.utils.print_info("audit_button was found ")
            self.auto_actions.click(audit_button)
        else:
            self.utils.print_info("audit_button was not found ")
            return -1

        sort_time_stamp1 = self.devices_web_elements.get_sort_time_stamp()
        if sort_time_stamp1:
            self.utils.print_info("Clicking on sort time")
            self.auto_actions.click(sort_time_stamp1)
        else:
            self.utils.print_info("Clicking on sort time not found ")
        sleep(10)
        sort_time_stamp = self.devices_web_elements.get_sort_time_stamp()
        self.utils.print_debug(sort_time_stamp.get_attribute("class"))
        if sort_time_stamp:
            if 'dgrid-sort-down' in sort_time_stamp.get_attribute("class"):
                pass
            elif 'dgrid-sort-up' in sort_time_stamp.get_attribute("class"):
                self.utils.print_info("Clicking on sort time")
                self.auto_actions.click(sort_time_stamp)
            else:
                pass
        else:
            self.utils.print_info("Clicking on sort time not found ")
        sleep(10)
        audit_rows = self.devices_web_elements.get_audit_rows()
        if audit_rows:
            self.utils.print_info("audit_rows was found ")
            self.auto_actions.click(audit_rows)
            cnt = 0
            for el in audit_rows:
                self.utils.print_debug("rows {} is: {} ".format(cnt, el.text))
                cnt = cnt + 1
            time_stamp = self.devices_web_elements.get_audit_time_stamp(audit_rows[0])
            if time_stamp:
                self.utils.print_info("Log row is : ", audit_rows[0].text)
                self.utils.print_info("Time_stamp for last log is : ", time_stamp.text)
                return time_stamp.text
            else:
                self.utils.print_info("time_stamp was not found ")
                return -1
        else:
            self.utils.print_info("audit_rows was not found ")
            return -1
