import re
import os
import copy
from time import sleep
from datetime import datetime

from selenium.common.exceptions import StaleElementReferenceException
from robot.libraries.BuiltIn import BuiltIn

from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.flows.common.Login import Login
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from extauto.common.CloudDriver import CloudDriver
from extauto.common.CommonValidation import CommonValidation
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.WebElementController import WebElementController
from extauto.common.WebElementHandler import WebElementHandler
from ExtremeAutomation.Utilities.deprecated import deprecated
from extauto.xiq.xapi.manage.XapiDevices import XapiDevices
from extauto.xiq.elements.ClientWebElements import ClientWebElements



class Devices:
    def __init__(self):
        self.utils = Utils()
        self.common_validation = CommonValidation()
        self.auto_actions = AutoActions()
        self.devices_web_elements = DevicesWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.switch_web_elements = SwitchWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.common_validation = CommonValidation()
        self.navigator = Navigator()
        self.cobj_web_elements = CommonObjectsWebElements()
        self.device_actions = DeviceActions()
        self.device_update = DeviceUpdate()
        self.device_common = DeviceCommon()
        self.cli = Cli()
        self.screen = Screen()
        self.robot_built_in = BuiltIn()
        self.custom_file_dir = os.getcwd() + '/onboard_csv_files/'
        self.login = Login()
        self.cli = Cli()
        self.web_element_ctrl = WebElementController()
        self.web_elements_handler = WebElementHandler()
        self.cloud_driver = CloudDriver()
        self.xapiDevices = XapiDevices()

    @deprecated("Please use onboard_device_quick(...)")
    def _onboard_ap(self, ap_serial, device_make, location, device_os=False, **kwargs):
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
        if self.search_device(device_serial=ap_serial, skip_navigation=True, ignore_failure=True) == 1:
            self.utils.print_info(f"Ap with {ap_serial} serial number already onboarded")
            return 1

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), ap_serial)

        if device_os:
            sleep(5)
            self.utils.print_info("Verify Device OS")
            device_os = self.devices_web_elements.get_device_os_radio().text
            self.utils.print_info("Device OS: ", device_os)
            if 'Cloud IQ Engine' in device_os:
                self.utils.print_info("Device OS matched")

        if 'Extreme - Aerohive' in device_make:
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_dropdownoption)
            self.auto_actions.select_drop_down_options(
                self.devices_web_elements.get_device_make_drop_down_options(), device_make)

        if location:
            self.utils.print_info("Selecting location")
            self.auto_actions.click_reference(self.devices_web_elements.get_location_button)
            self._select_location(location)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_button)

        quick_add_ongoing = True
        while quick_add_ongoing:
            if self.devices_web_elements.get_devices_quick_add_block_show():
                self.utils.print_info("Still in adding device process, wait for finishing ...")
                sleep(2)
            else:
                quick_add_ongoing = False
                self.utils.print_info("Finish device adding process ...")

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                kwargs['fail_msg'] = f"Error: {dialog_message}"
                self.common_validation.failed(**kwargs)
                return -1
            if "A stake record of the device was found in the redirector." in dialog_message:
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                kwargs['fail_msg'] = f"Error: {dialog_message}"
                self.common_validation.failed(**kwargs)
                return -2
        else:
            kwargs['pass_msg'] = "No Errors while onboarding"
            self.common_validation.passed(**kwargs)

        serials = ap_serial.split(",")
        self.utils.print_info("Device Serials Numbers: ", serials)

        for serial in serials:
            if self.search_device(device_serial=serial) == 1:
                kwargs['pass_msg'] = f"Successfully Onboarded AP(s): {serials}"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "The AP(s) couldn't be onboarded"
                self.common_validation.failed(**kwargs)
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

    def get_os_change(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        if device_mac:
            search_result = self.search_device(device_mac)
            if search_result != -1:
                if self.select_device(device_mac):
                    self.utils.print_info("Click ACTION button")
                    self.auto_actions.click_reference(self.devices_web_elements.get_action_button)
                    self.utils.print_info("Click change os Button")
                    self.auto_actions.click_reference(self.devices_web_elements.device_actions_change_os_button)
                    self.screen.save_screen_shot()
                    sleep(2)
                    self.utils.print_info("Check for error message")
                    device_error_message = self.devices_web_elements.get_os_change_error_message()
                    self.utils.print_info("Error message: ", device_error_message.text)
                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button)
                    sleep(2)
                    self.screen.save_screen_shot()
                    kwargs['pass_msg'] = f"Successfully Selected NOS change for device having MAC address {device_mac}"
                    self.common_validation.passed(**kwargs)
                    return 1
            else:
                kwargs['fail_msg'] = f"Device with device mac {device_mac} is not EXOS or VOSS device"
                self.common_validation.failed(**kwargs)
                return -1
        if device_serial:
            search_result = self.search_device(device_serial)
            if search_result != -1:
                if self.select_device(device_serial):
                    self.utils.print_info("Click ACTION button")
                    self.auto_actions.click_reference(self.devices_web_elements.get_action_button)
                    self.utils.print_info("Click change os Button")
                    self.auto_actions.click_reference(self.devices_web_elements.device_actions_change_os_button)
                    self.screen.save_screen_shot()
                    sleep(3)
                    self.utils.print_info("Check for error message")
                    device_error_message = self.devices_web_elements.get_os_change_error_message()
                    self.utils.print_info("Error message: ", device_error_message.text)
                    self.utils.print_info("Click confirmation Yes Button")
                    sleep(3)
                    self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button)
                    sleep(2)
                    self.screen.save_screen_shot()
                    kwargs['pass_msg'] = f"Successfully Selected NOS change for device having serial {device_serial} "
                    self.common_validation.passed(**kwargs)
                    return 1
            else:
                kwargs['fail_msg'] = f"Device with device serial {device_serial} is not EXOS or VOSS device"
                self.common_validation.failed(**kwargs)
                return -1
        if device_name:
            search_result = self.search_device(device_name)
            if search_result != -1:
                if self.select_device(device_name):
                    self.utils.print_info("Click ACTION button")
                    self.auto_actions.click_reference(self.devices_web_elements.get_action_button)
                    self.utils.print_info("Click change os Button")
                    self.auto_actions.click_reference(self.devices_web_elements.device_actions_change_os_button)
                    self.screen.save_screen_shot()
                    sleep(2)
                    self.utils.print_info("Check for error message")
                    device_error_message = self.devices_web_elements.get_os_change_error_message()
                    self.utils.print_info("Error message: ", device_error_message.text)
                    self.utils.print_info("Click confirmation Yes Button")
                    self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button)
                    sleep(2)
                    self.screen.save_screen_shot()
                    kwargs['pass_msg'] = f"Successfully Selected NOS change for device named {device_name} "
                    self.common_validation.passed(**kwargs)
                    return 1
            else:
                kwargs['fail_msg'] = f"Device with device name {device_name} is not EXOS or VOSS device"
                self.common_validation.failed(**kwargs)
                return -1

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
        self.auto_actions.click_reference(self.devices_web_elements.get_device_details_wireless_interfaces)
        sleep(5)
        self.auto_actions.move_to_element(
            self.devices_web_elements.get_device_details_wireless_interfaces_surrounding_aps_grid())
        sleep(5)
        return 1

    def get_manage_device_row(self, search_string, **kwargs):
        """
        - Get the device row object from the Manage --> Device page
        - Based on the search string it will search the device row
        - Search string should be device serial, device mac, device host name

        :param search_string: it should be anything which is searched on the row cell
                         example search_string be like device_name, Device Model, Mac Address or Serial number
        :return: row element if row exists else return False
        """
        device_keys = {}
        if search_string:
            device_keys['search_string'] = search_string
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "You must pass a string to search for!"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(f"Getting the device row matching the search parameter: {device_keys}")
        row = self._find_device_row(device_keys)
        if row:
            kwargs['pass_msg'] = f"Found device row using {device_keys}"
            self.common_validation.passed(**kwargs)
            return row

        kwargs['fail_msg'] = f"Didn't find the device row matching the search parameter: {device_keys} in the grid"
        self.common_validation.failed(**kwargs)
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
                      UPTIME, MODEL, SERIAL, UPDATED, MGT VLAN, COPILOT
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
                     'DEVICE LICENSE': 'subscriptionLicense',
                     'COPILOT': 'copilotLicenseStatus'
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
                device_row = self.get_manage_device_row(search_string, ignore_failure=True)
                device_row = copy.copy(device_row)
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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: network policy name applied to the AP
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        network_policy = self.get_device_details(search_string, 'POLICY')
        if network_policy:
            return network_policy
        else:
            self.utils.print_info("Can not get network policy")

    def check_device_reboot_message(self, device_serial, config_update_option, reboot_message, **kwargs):
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
        self.auto_actions.click_reference(self.switch_web_elements.get_devices_search_button)
        sleep(5)

        self.utils.print_info("Clicking Device Checkbox")
        self.auto_actions.click_reference(self.switch_web_elements.get_devices_select_checkbox_field)
        sleep(2)

        self.utils.print_info("Clicking Update Devices Button For The Device: ", device_serial)
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
        sleep(2)

        if config_update_option == 'delta':
            self.utils.print_info("Clicking Delta Configuration Update Radio Button")
            self.auto_actions.click_reference(self.devices_web_elements.get_delta_config_update_button)
            sleep(1)

        if config_update_option == 'full':
            self.utils.print_info("Clicking Full Configuration Update Radio Button")
            self.auto_actions.click_reference(self.devices_web_elements.get_full_config_update_button)
            sleep(1)

        self.utils.print_info("Clicking Perform update Button")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
        sleep(3)

        count = 0
        while count < 10:
            self.utils.print_info("Checking for For update Configuration Messages")
            if self.devices_web_elements.get_devices_config_update_message():
                config_update_msg = self.devices_web_elements.get_devices_config_update_message().text
                self.utils.print_info(config_update_msg)
                if reboot_message in config_update_msg:
                    kwargs['pass_msg'] = "Device is Rebooting after update configuration"
                    self.common_validation.passed(**kwargs)
                    return True
            sleep(1)
            count += 1
        kwargs['fail_msg'] = "Device is not Rebooting after update configuration"
        self.common_validation.failed(**kwargs)
        return False

    def get_device_serial_numbers(self, device_type, **kwargs):
        """
        - gets all existing devices serials with the same device_type
        - Keyword Usage:
        - ``Get Device Serial Numbers   ${DEVICE_TYPE}``

        :param device_type: type of device to
        :return: serial number(s) with same device type
        """
        try:
            prev_dev_list = []
            sleep(5)
            rows = self.devices_web_elements.get_grid_rows()
            if rows:
                for row in rows:
                    if device_type and device_type in row.text:
                        self.utils.print_info(f"{row.text}")
                        try:
                            cells = self.devices_web_elements.get_device_row_cells(row)
                            self.utils.print_info(f"found cells {len(cells)}")
                        except Exception:
                            self.utils.print_info(f"Could not get Row Cells - {row}")
                            continue
                        device_detail_dict = {}
                        for cell in cells:
                            try:
                                cell.get_attribute("class")
                            except Exception:
                                print("cell print error")
                                continue
                            if re.search(r'field-\w*', cell.get_attribute("class")):
                                try:
                                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                                except Exception:
                                    label = 'OOPS'
                                device_detail_dict[label] = cell.text
                            else:
                                self.utils.print_info("missed class match " + cell.get_attribute("class"))
                        res = device_detail_dict.get("serialNumber")
                        prev_dev_list.append(res)
                self.utils.print_info(f"List of Serial Numbers of Devices with device type {device_type}: {prev_dev_list}")
            else:
                self.utils.print_info("No rows present")
            return prev_dev_list
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = f"Unable to get Device Serial Numbers with Device Type {device_type}"
            self.common_validation.fault(**kwargs)
            return -1

    def _search_simulated_devices(self, device_model):
        """
        Searches for AP matching AP's Serial Number

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found
        """
        self.refresh_devices_page()

        rows = self.devices_web_elements.get_simulated_devices_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info("row data: ", self.format_row(row.text))
                if device_model in row.text:
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
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)
        sleep(3)
        if self.device_actions.get_device_actions_dropdown():
            self.utils.print_info("Move to Assign Network policy action")
            self.auto_actions.move_to_element(self.devices_web_elements.get_actions_assign_network_policy_combo())
            self.utils.print_info("Click on Assign Network policy action")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_combo)
            sleep(4)
            select_is_shown = self.devices_web_elements.get_nw_policy_drop()
            if select_is_shown:
                self.utils.print_info("Click on network policy drop down")
                self.auto_actions.click(select_is_shown)
                sleep(3)
                network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
                if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                    self.utils.print_info(f"Selected Network policy from drop down:{policy_name}")
                else:
                    self.utils.print_info("Network policy is not present in drop down")
                    self.screen.save_screen_shot()
                    return False

                sleep(5)
                self.utils.print_info("Click on network policy assign button")
                self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_button)
                sleep(10)

                tooltip_text = self.dialogue_web_elements.get_tooltip_text()
                sleep(2)

                self.utils.print_info("tooltip_text: ", tooltip_text)
                if tooltip_text:
                    if "Your account does not have permission to perform that action" in tooltip_text:
                        self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_close_button)
                        sleep(5)
                        return False
                return True
            else:
                self.utils.print_info("Nothing is shown in network policy drop list")
                return False
        else:
            self.screen.save_screen_shot()
            self.utils.print_info("Actions dropdown is NOT shown")
            return False

    def _update_network_policy(self, update_method="Delta", **kwargs):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices

        :param update_method:  Delta, Complete
        :return:
        """
        update_tooltip_msg1 = "a device mode change is not supported with a delta configuration update"
        update_tooltip_msg2 = "This change is not supported with a Delta Configuration Update, " \
                              "you must select a Complete Configuration Update."
        update_tooltip_msg3 = "Please first upgrade device to the supported OS version and then try configuration update."
        update_tooltip_msg = "Please first upgrade device to the supported OS version and then try configuration update."
        update_tooltip_msg4 = "To avoid conflict, please try your operation after some time."

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
        sleep(2)
        self.screen.save_screen_shot()

        if update_method == "Delta":
            self.utils.print_info("click on delta config radio button")
            self.auto_actions.click_reference(self.devices_web_elements.get_delta_config_update_button)
            sleep(2)
            self.utils.print_info("click on perform update button")
            self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
            sleep(30)
            self.screen.save_screen_shot()

            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)

            if update_tooltip_msg2 in tool_tp_text or update_tooltip_msg1 in tool_tp_text:
                self.utils.print_info('Convert to Complete. Delta not supported')
                update_method = "Complete"

            if update_tooltip_msg3 in tool_tp_text:
                self.utils.print_info(f"Getting Device Update Error Message : {tool_tp_text}")
                self.screen.save_screen_shot()
                self.utils.print_info("click on Device Update Cancel Button")
                self.auto_actions.click_reference(self.devices_web_elements.get_action_assign_network_policy_dialog_cancel_button)
                self.utils.print_info("Error: ", tool_tp_text)
                return -1

            if update_tooltip_msg4 in tool_tp_text[-1]:
                self.utils.print_info(f"The device is currently in update progress : {tool_tp_text}")
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.dialogue_web_elements.get_tooltip_close_button)
                self.utils.print_info("Wait for few minutes and perform update")
                sleep(120)
                self.utils.print_info("click on perform update button")
                self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
                sleep(30)
                self.screen.save_screen_shot()

        if update_method == "Complete":
            self.utils.print_info("click on complete config radio button")
            self.auto_actions.click_reference(self.devices_web_elements.get_full_config_update_button)
            sleep(2)
            self.utils.print_info("click on perform update button")
            self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
            sleep(30)
            self.screen.save_screen_shot()

            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)

            if update_tooltip_msg in tool_tp_text:
                self.utils.print_info(f"Getting Device Update Error Message : {tool_tp_text}")
                self.screen.save_screen_shot()
                self.utils.print_info("click on Device Update Cancel Button")
                self.auto_actions.click_reference(self.devices_web_elements.get_action_assign_network_policy_dialog_cancel_button)
                self.utils.print_info("Error: ", tool_tp_text)
                return -1

            if update_tooltip_msg4 in tool_tp_text[-1]:
                self.utils.print_info(f"The device is currently in update progress : {tool_tp_text}")
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.dialogue_web_elements.get_tooltip_close_button)
                self.utils.print_info("Wait for few minutes and perform update")
                sleep(120)
                self.utils.print_info("click on perform update button")
                self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
                sleep(30)
                self.screen.save_screen_shot()

        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        for tooltip_msg in [update_tooltip_msg, update_tooltip_msg1, update_tooltip_msg2, update_tooltip_msg3, update_tooltip_msg4]:
            if tooltip_msg in tool_tp_text:
                tool_tp_text.remove(tooltip_msg)

        if "Deployed devices successfully." in tool_tp_text:
            self.utils.print_info("Device update Successfully Triggered")
            return 1
        else:
            kwargs['fail_msg'] = f"Error: {tool_tp_text}"
            self.common_validation.failed(**kwargs)
            return -1

    def _check_update_network_policy_status(self, policy_name, device_serial, **kwargs):
        """
        - This keyword is used to check the network policy applied status to the device
        - It will poll the "update status" every 30 seconds to get the status of the network policy applied
        - Assuming that config push will take the maximum five minutes,

        :param device_serial: device serial number to check the config push status
        :return: 1 if config push success else -1
        """
        retry_count = 0
        update_time = 0

        self.utils.print_info("Enable the Updated On column")
        self.column_picker_select("Updated On")

        max_config_push_wait = self.robot_built_in.get_variable_value("${MAX_CONFIG_PUSH_TIME}")
        while True:
            self.utils.print_info(f"Time elapsed for device update: {update_time} seconds")
            device_update_status = self.get_device_updated_status(device_serial)
            self.utils.print_info(f"Status returned: {device_serial}")
            if re.search(r'\d+-\d+-\d+', device_update_status):
                break
            elif 'Rebooting' in device_update_status:
                reboot_res = self.wait_until_device_reboots(device_serial, retry_duration=15, retry_count=12)
                if reboot_res == 1:
                    self.utils.print_info(
                        'Reboot for device with serial number: {} is successful'.format(device_serial))
                else:
                    self.utils.print_info('Reboot for device with serial number: {} is NOT successful: {}'.format(
                        device_serial, reboot_res))
                    return -1
            elif 'Certification' in device_update_status or 'Application' in device_update_status:
                # Some other random push to the device is blocking my policy update!
                self.utils.print_info("Non-update text in status :{}".format(device_update_status))
                self.screen.save_screen_shot()
                sleep(30)
                update_time += 30
                if update_time >= 300:
                    self.utils.print_info("Config push to AP BLOCKED for more than 300 seconds")
                    return -1
                continue
            elif retry_count >= int(max_config_push_wait):
                self.utils.print_info(f"Config push to AP taking more than {max_config_push_wait} seconds")
                return -1
            sleep(30)
            update_time += 30
            retry_count += 30

        policy_applied = self.get_ap_network_policy(ap_serial=device_serial)
        if policy_name.upper() == policy_applied.upper():
            self.utils.print_info("Applied network policy:{}".format(policy_applied))
            return 1
        self.utils.print_info(f"Policy applied:{policy_name} is not matching with policy updated:{policy_applied}")
        return -1

    def assign_and_update_network_policy_to_exos(self, policy_name=None, serial=None, update_method='PolicyAndConfig',
                                                 **kwargs):
        """
        - By default this keyword do delta config push
        - Go To MANAGE-->Devices-->Select EXOS SW row  to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - select Switch -->Update device
        - Keyword Usage:
        - ``Assign and Update Network Policy To EXOS   policy_name=${POLICY_NAME}    serial=${SW1_SERIAL}``
        - ``Assign and Update Network Policy To EXOS   policy_name=${POLICY_NAME}    serial=${SW1_SERIAL}  update_method=Complete``

        :param policy_name: name of the network to deploy, by default set to None
        :param serial: serial number of the switch to select, by default set to None
        :param update_method: Perform Complete update or delta update, by default set to 'PolicyAndConfig'
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Switch row")
        if not self.select_device(serial, skip_refresh=True, skip_navigation=True):
            kwargs['fail_msg'] = f"Switch {serial} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        if not self._assign_network_policy(policy_name):
            kwargs['fail_msg'] = "Didn't assigned network policy"
            self.common_validation.failed(**kwargs)
            return -1
        sleep(30)

        return self.update_network_policy_to_exos(serial=serial)

    def update_network_policy_to_exos(self, serial=None, update_method="PolicyAndConfig", **kwargs):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the device
        - Keyword Usage:
        - ``Update Network Policy To Exos      serial=${SW1_SERIAL}     update_method="PolicyAndConfig"``

        :param update_method:
            PolicyAndConfig - selects the "Update Network Policy and Configuration" check button
        :param serial: serial number of the device, by default set to None
        :return:  1 if update was performed, -1 if not
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Switch row")
        self.select_device(serial, skip_navigation=True)
        sleep(5)

        # Handle the case where a tooltip / popup is covering the Update Device button
        self.close_last_refreshed_tooltip()

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
        sleep(2)

        pol_config_cb = self.devices_web_elements.get_switch_update_policy_and_config_check_button()
        engine_img_cb = self.devices_web_elements.get_switch_upgrade_engine_and_images_check_button()

        if pol_config_cb is None:
            self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
            kwargs['fail_msg'] = "ERROR: Unable to obtain 'Update Network Policy and Configuration' check button"
            self.common_validation.fault(**kwargs)
            return -1
        if engine_img_cb is None:
            self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
            kwargs['fail_msg'] = "ERROR: Unable to obtain 'Upgrade IQ Engine and Extreme Network'. " \
                                 "Switch Images' check button"
            self.common_validation.fault(**kwargs)
            return -1

        # TO DO: Handle the two check buttons to specify the type of update to perform
        if update_method == "PolicyAndConfig":
            self.utils.print_info("Only enable 'Update Network Policy and Configuration' check button")
            # self.auto_actions.enable_check_box(pol_config_cb)
            self.auto_actions.disable_check_box(engine_img_cb)
            sleep(2)

        else:
            self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
            kwargs['fail_msg'] = f"Unknown update method {update_method}. Please specify 'PolicyAndConfig'"
            self.common_validation.fault(**kwargs)
            return -1

        # Perform the update
        self.utils.print_info("Click on perform update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)

        self.screen.save_screen_shot()
        sleep(2)

        update_status = self._check_device_update_status(serial)
        if update_status == -1:
            device_update_state = self.get_device_updated_status(serial)
            if device_update_state == "Device Update Failed":
                device_row = self.get_manage_device_row(serial)
                ConfigErrorToolTip = self.device_update.get_device_update_form_error(device_row)
                self.utils.print_info("There is a failure during config push")
                return update_status, ConfigErrorToolTip
        return update_status

    def update_network_policy_to_ap_if_needed(self, policy_name=None, ap_serial=None, update_method="Delta"):
        dev_policy = self.get_device_details(ap_serial, 'POLICY')
        if dev_policy == policy_name:
            dev_status = self.get_device_status(device_serial=ap_serial)
            if dev_status == 'green':
                return 1
            else:
                return self.update_network_policy_to_ap(policy_name, ap_serial, update_method)
        else:
            return self.update_network_policy_to_ap(policy_name, ap_serial, update_method)

    def update_network_policy_to_ap(self, policy_name=None, ap_serial=None, update_method="Delta", **kwargs):
        """
        - By default this keyword do delta config push
        - Go To MANAGE-->Devices-->Select AP row  to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - select AP-->Update device
        - Keyword Usage:
        - ``Update Network Policy To Ap   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}``
        - ``Update Network Policy To Ap   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}  update_method=Complete``

        :param policy_name: name of the network to deploy, by default set to None
        :param ap_serial: serial number of the ap to select, by default set to None
        :param update_method: Perform Complete update or delta update, by default set to 'Delta'
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)
        network_policy_assigned = False
        try_cnt = 0
        while not network_policy_assigned:
            self.utils.print_info("Select ap row for network policy assignment")
            if not self.select_device(device_serial=ap_serial):
                kwargs['fail_msg'] = f"AP {ap_serial} is not present in the grid"
                self.common_validation.fault(**kwargs)
                return -1
            sleep(2)

            if self._assign_network_policy(policy_name):
                network_policy_assigned = True
            else:
                try_cnt += 1
                self.utils.print_info(f"{try_cnt} attempts to select device --> click action --> "
                                      f"click assign network policy --> select the policy and assign it to device")
                if try_cnt == 10:
                    kwargs['fail_msg'] = f"Max {try_cnt} attempts are reached, return -1"
                    self.common_validation.fault(**kwargs)
                    return -1
                self.utils.print_info("Cancel Network Policy assignment dialog")
                self.auto_actions.click_reference(self.devices_web_elements.get_action_assign_network_policy_dialog_cancel_button)
                sleep(2)
        self.utils.print_info("Select ap row")
        self.select_device(device_serial=ap_serial)

        self._update_network_policy(update_method)
        return self._check_update_network_policy_status(policy_name, ap_serial)

    def update_network_policy_to_multiple_ap(self, policy_name='', ap_serial='', update_method="Delta", **kwargs):
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

        self.navigator.enable_page_size()
        self.utils.print_info("Selecting the device rows")
        ap_serial = ap_serial.split(',')
        for ap_sr in ap_serial:
            if ap_sr == ap_serial[0]:
                self.select_device(ap_sr, skip_navigation=True)
            else:
                self.select_device(ap_sr, skip_refresh=True, skip_navigation=True)

        if not self._assign_network_policy(policy_name):
            kwargs['fail_msg'] = f"Can not assign network policy {policy_name}"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Selecting the device rows")
        for ap_sr in ap_serial:
            if ap_sr == ap_serial[0]:
                self.select_device(ap_sr)
            else:
                self.select_device(ap_sr, skip_refresh=True, skip_navigation=True)

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

    def change_country(self, ap_serial, country, **kwargs):
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

        if self.select_device(device_serial=ap_serial,  skip_refresh=True, skip_navigation=True):
            self.utils.print_info("Click on Actions button")
            self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)

            self.utils.print_info("Selecting Assign Country Code menu item")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_country_code_menu_item)
            sleep(5)

            self.utils.print_info("Clicking on Country Code dropdown")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_country_code_dropdown)
            self.screen.save_screen_shot()
            sleep(2)

            _country = country.replace("_", " ")
            self.utils.print_info("Selecting Country Code: ", _country)
            self.auto_actions.click(self.devices_web_elements.get_actions_country_code_dropdown_option(_country))
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Saving Country Code settings")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_country_code_save_button)
            sleep(2)

            self.utils.print_info("Confirming AP reboot on Country Code settings...")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_country_code_confirm_button)
            sleep(2)

            error_msg = self.devices_web_elements.get_actions_country_code_error_message()
            if error_msg:
                self.auto_actions.click_reference(self.devices_web_elements.get_actions_country_code_close_button)
                sleep(5)
                kwargs['fail_msg'] = f"Errors: {error_msg}"
                self.common_validation.failed(**kwargs)
                return -1
        return 1

    def get_ap_flag(self, ap_serial, **kwargs):
        """
        - This method gets the country cell element from Devices page and saves the screenshot of it.
        - Keyword Usage:
        - ``Get AP Flag    ${AP_SERIAL}``

        :param ap_serial: ap serial number
        :return: 1 if flag saved else -1
        """
        device_keys = {}
        if ap_serial:
            device_keys['ap_serial'] = ap_serial
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "You must pass the serial number!"
            self.common_validation.fault(**kwargs)
            return -1

        self.refresh_devices_page()
        row = self._find_device_row(device_keys)
        if row:
            flag_cell = self.devices_web_elements.get_country_code_cell(row)
            if flag_cell:
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = "Saved the flag successfully"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Unable to save the flag"
        self.common_validation.failed(**kwargs)
        return -1

    def get_ap_country(self, ap_serial, **kwargs):
        """
        - This method gets the country name from country cell from Devices page.
        - Keyword Usage:
        - ``Get Ap Country   ${AP_SERIAL}``

        :param ap_serial: serial number of AP
        :return: country name
        """
        device_keys = {}
        if ap_serial:
            device_keys['ap_serial'] = ap_serial
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "You must pass the serial number!"
            self.common_validation.fault(**kwargs)
            return -1

        flag_cell = False
        self.refresh_devices_page()
        row = self._find_device_row(device_keys)
        if row:
            flag_cell = self.devices_web_elements.get_country_code_cell(row)
            if flag_cell:
                return flag_cell.text.replace(" ", "_")

        kwargs['fail_msg'] = "Unable to get ap country"
        self.common_validation.failed(**kwargs)
        return -1

    def reboot_device(self, device_serial=None, device_mac=None, **kwargs):
        """
        - Assumes that already navigated to Manage --> Devices
        - This method reboots a device matching the serial(s)
        - Keyword Usage:
        - ``Reboot Device  ${DEVICE_SERIAL}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device serial number, by default set to None
        :param device_mac: device mac address, by default set to None
        :return: None
        """

        # Execute the XAPI call and return the value
        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_reboot_device(device_serial, device_mac, **kwargs)

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        if device_serial:
            self.utils.print_info("Selecting Device with serial: ", device_serial)
            self.select_device(device_serial=device_serial)
        elif device_mac:
            self.utils.print_info("Selecting Device with mac-address: ", device_mac)
            self.select_device(device_mac=device_mac)
        else:
            kwargs['fail_msg'] = 'Device Serial Number or Device Mac Address was not provided'
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Click on device actions button")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)

        self.utils.print_info("click on device actions reboot button")
        self.auto_actions.click_reference(self.devices_web_elements.get_device_actions_reboot_button)

        self.utils.print_info("Click on reboot confirm yes button")
        self.auto_actions.click_reference(self.devices_web_elements.get_device_actions_reboot_confirm_bttn)

        kwargs['pass_msg'] = "Device was rebooted successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def upgrade_device(self, *device_dict, version=None, action="upgrade", activate_time=60, **kwargs):
        """
        - This method will update the software image the device is using
        - device_dict - dictionary from .yaml testbed file (ex: ap1, netelem1}
        - Keyword Usage:
        - ``Upgrade Device   ${ap1}``
        - ``Upgrade Device   ${netelem1}  version=8.8.0.0``

        :param version: - version=None - means latest version
                        - version="" - to which device should get upgraded, ex: version="8.8.0.0"
        :param action: - action="upgrade" - will update the software image of the device
                       - action="close" - will check if the firmware upgrade option is available for the device
                        and close the image upgrade without perform the upgrade.
        :param activate_time: activation time for Extreme Networks devices running images, by default set to 60 seconds
        :return: returned_version of the device, or -1 if it was unable to perform the upgrade
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        returned_version = -1
        device_selected = 0
        device_dict = device_dict[0]
        device_serial = device_dict.get("serial")
        device_mac = device_dict.get("mac")

        # Let's make sure we can get the device selected
        counter = 0
        while device_selected != 1:
            if counter > 10:
                self.utils.print_info(f'We reached the limit of trying to selecting the device, counter: {counter}')
                break
            else:
                counter = counter + 1
            self.utils.print_info(f'Selecting the device, counter: {counter}')
            device_selected = self.select_device(device_mac=device_mac, device_serial=device_serial)


        # we have selected a device
        if device_selected == 1:
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click_reference(self.device_update.get_update_devices_button)
            sleep(5)

            uptd = self.devices_web_elements.get_devices_switch_update_network_policy()
            if uptd:
                if uptd.is_selected():
                    self.utils.print_info("uncheck the update configuration checkbox")
                    self.auto_actions.click(uptd)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click_reference(self.device_update.get_upgrade_iq_engine_checkbox)
            sleep(5)

            if version is None:
                self.utils.print_info("Selecting upgrade to latest version checkbox")
                self.auto_actions.click_reference(self.device_update.get_upgrade_to_latest_version_radio)
                sleep(5)

                if not self.device_update.get_upgrade_even_if_versions_are_same_button().is_selected():
                    self.utils.print_info("Click on Upgrade even if the versions are the same button")
                    self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_are_same_button)
                    sleep(5)

                returned_version = self.device_update.get_latest_version()
                self.utils.print_info("Device Latest Version: ", returned_version)
                sleep(5)

            else:
                self.utils.print_info("Selecting upgrade to specific version checkbox")
                self.auto_actions.click_reference(self.device_update.get_upgrade_to_specific_version_radio)
                sleep(2)

                if not self.device_update.get_upgrade_even_if_versions_are_same_button().is_selected():
                    self.utils.print_info("Click on Upgrade even if the versions are the same button")
                    self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_are_same_button)
                    sleep(5)

                self.utils.print_info("Click specific version Dropdown")
                self.auto_actions.click_reference(self.device_update.get_actions_update_version_drop_down)
                sleep(2)

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
                            if "patch" not in version and "patch" in opt.text:
                                continue
                            self.utils.print_info("Image version {} match the image {} from "
                                                  "drop down".format(version, opt.text))
                            cont_images_found += 1
                            image_select = opt.text
                        else:
                            self.utils.print_info("Image version {} doesn't match the "
                                                  "image {} from drop down".format(version, opt.text))
                if cont_images_found == 1:
                    if self.auto_actions.select_drop_down_options(update_version_items, image_select):
                        returned_version = version
                        self.utils.print_info("Device Specific Version: ", returned_version)
                elif cont_images_found > 1:
                    kwargs['fail_msg'] = "Multiple images were found in drop down"
                    self.common_validation.fault(**kwargs)
                    return -1
                else:
                    kwargs['fail_msg'] = f"Image version {version} doesn't match the images from drop down."
                    self.common_validation.fault(**kwargs)
                    return -1

            activate_bttn = self.device_update.get_activate_after_radio()
            if activate_bttn:
                self.utils.print_info("Selecting Activate After radio button")
                self.auto_actions.click_reference(self.device_update.get_activate_after_radio)

                self.utils.print_info(f"Setting Activate time to {activate_time} seconds")
                self.auto_actions.send_keys(self.device_update.get_activate_after_textfield(), activate_time)

            if action == "upgrade":
                self.auto_actions.click_reference(self.device_update.get_perform_update_button)
                kwargs['pass_msg'] = "Upgrade was successfully"
                self.common_validation.passed(**kwargs)
                return returned_version
            elif action == "close":
                self.auto_actions.click_reference(self.device_update.get_update_close_button)
                kwargs['pass_msg'] = "Closed upgrade window successfully"
                self.common_validation.passed(**kwargs)
                return returned_version
            else:
                self.auto_actions.click_reference(self.device_update.get_update_close_button)
                kwargs['fail_msg'] = f"Selected action {action} is unavailable"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['fail_msg'] = f"Device using MAC: {device_mac} or serial number: {device_serial} was not found " \
                             f"thus failed to upgrade it"
        self.common_validation.failed(**kwargs)
        return -1

    def refresh_devices_page(self, **kwargs):
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
            returnValue = self.auto_actions.click_reference(self.devices_web_elements.get_refresh_devices_page)
            if returnValue == -1:
                kwargs['fail_msg'] = "Device page was NOT refreshed"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                # Wait until 'loading' mask is cleared
                self.navigator.wait_until_devices_load_spinner_cleared(retry_duration=1, retry_count=180)
                kwargs['pass_msg'] = "Device page refreshed successfully"
                self.common_validation.passed(**kwargs)
                return 1
        except Exception:
            kwargs['fail_msg'] = "Unable to refresh devices page. Capturing screenshot"
            self.common_validation.failed(**kwargs)
            return -1

    def edit_ap_description(self, ap_desc, ap_serial=None, ap_name=None, ap_mac=None, **kwargs):
        """
        - Edits AP matching either any of either one of serial, name, MAC
        - Keyword Usage:
        - ``Edit Ap Description   ${AP_DESC}   ap_serial=${AP_SERIAL}``

        :param ap_desc: AP's Description
        :param ap_serial: AP Serial, by default set to None
        :param ap_name: AP Name, by default set to None
        :param ap_mac: AP MAC, by default set to None
        :return: 1 if success else -1
        """

        self.utils.print_info("Editing AP: ", ap_serial)
        search_result = self.search_device(device_serial=ap_serial)

        if search_result:
            if self.select_device(device_serial=ap_serial):
                self.auto_actions.click_reference(self.devices_web_elements.get_edit_button)
                sleep(5)
                self.auto_actions.click_reference(self.devices_web_elements.get_ap_configure_button)
                sleep(2)
                self.auto_actions.click_reference(self.devices_web_elements.get_ap_device_config_tab)
                sleep(2)
                self.auto_actions.send_keys(self.devices_web_elements.get_ap_description_button(), ap_desc)
                sleep(2)
                self.auto_actions.click_reference(self.devices_web_elements.get_save_device_config)
                sleep(2)
                return 1

        kwargs['fail_msg'] = "Unable to edit AP's description"
        self.common_validation.failed(**kwargs)
        return -1

    def onboard_device_quick(self, *device_dict, policy_name=None, **kwargs):
        """
        - This keyword onboards: an aerohive device [AP or Switch], Exos Switch and Voss devices using Quick onboarding flow.
        - Keyword Usage:
        - ``Onboard Device Quick  ${ap1}``
                {ap1} - dictionary from .yaml file of the testbed ( 'ap1' is only an example )
                Example:
                {'name': 'bui-flo-1996',
                'connection_method': 'telnet',
                'ip': '10.16.171.71',
                'port': 22,
                'username': 'admin',
                'password': 'Aerohive123',
                'serial': '01301506171996',
                'type': 'Real',
                'entry_type': 'Manual',
                'csv_file_name': '',
                'os': 'Cloud IQ Engine',
                'service_tag': False,
                'model': 'AP130',
                'mac': '885BDD3E0280',
                'cli_type': 'AH-AP',
                'platform': 'aerohive',
                'template': 'AP130-default-template',
                'make': 'Extreme - Aerohive',
                'mgmt_vlan': 10,
                'country': 'United States',
                'location': 'Santa Jose, building_01, floor001',
                'power_strip':
                    {'ip': None, '
                    port': None,
                    'username': None,
                    'password': None,
                    'plug':
                        {'plug_a': None,
                        'plug_b': None},
                    'type': None},
                'extra': {'country': 'United Kingdom',
                          'network_policy': 'Test_np',
                          'ssid': 'AP130_01',
                          'version': 6.5,
                          'neighbour_serial': '06301908310556',
                          'neighbour_mac': '7C95B1005700'}
                }

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param policy_name: Name of policy that would be used when onboarding a device, by default set to None
        :return:  1 if onboarding success
        :return: -1 for errors
        """
        device_dict = device_dict[0]
        device_type = device_dict.get("onboard_device_type")
        name = device_dict.get("name")

        # Arguments for device_type == "Real"
        device_serial = device_dict.get("serial")
        device_make = device_dict.get("make")
        device_mac = device_dict.get("mac")
        location = device_dict.get("location")
        device_platform = device_dict.get("platform")
        service_tag = device_dict.get("service_tag")  # argument for Real device ---> Dell
        csv_location = device_dict.get("csv_location")
        device_os = device_dict.get("os")

        # Arguments for device_type == "Simulated"
        device_model = device_dict.get("model")
        device_count = device_dict.get("simulated_count", 1)

        # Arguments for device_type == "Digital Twin"
        os_version = device_dict.get("digital_twin_version")
        os_persona = device_dict.get("digital_twin_persona")

        # Execute the XAPI call and return the value
        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_onboard_device_quick(device_dict, **kwargs)

        if "csv_location" in device_dict:
            return self.quick_onboarding_cloud_csv(device_make=device_dict.get("device_make"),
                                                   csv_location=device_dict.get("csv_location"))
        else:
            entry_type = "Manual"

        if self.check_onboard_device_quick_parameters(device_type, entry_type, device_serial, device_make, location,
                                                      csv_location, device_model, os_version, os_persona,
                                                      **kwargs) == -1:
            kwargs['fail_msg'] = "The Mandatory arguments for onboard device quick method missing."
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Onboarding: ", device_make)
        self.navigator.navigate_to_devices()

        self.utils.print_info("Clicking on +/ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        attempt_count = 3
        while attempt_count > 0:
            if attempt_count != 3:
                self.utils.print_info("Menu selection failed. Making another attempt...")
                self.utils.print_info("Clicking on +/ADD button...")
                self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)
                self.utils.print_info("Selecting Quick Add Devices menu")
                sleep(4)
            try:
                quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
                self.auto_actions.move_to_element(quick_add_devices_button)
                break
            except Exception:
                attempt_count = attempt_count - 1
        if attempt_count == 0:
            kwargs['fail_msg'] = "Unable to get / click the menu option"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)

        if device_type.lower() == "real":
            if self.set_onboard_values_for_real(device_serial, device_make, entry_type, device_os, service_tag,
                                                device_mac, location) != 1:
                kwargs['fail_msg'] = "Fail onboarded device with device_type == Real"
                self.common_validation.fault(**kwargs)
                return -1

        elif device_type.lower() == "simulated":
            list_initial_simulated_serial = self.get_device_serial_numbers(device_model)
            if self.set_onboard_values_for_simulated(device_model, device_count) != 1:
                kwargs['fail_msg'] = "Fail onboarded device with device_type == Simulated"
                self.common_validation.fault(**kwargs)
                return -1

        elif device_type.lower() == "digital twin":
            list_initial_serial_dt = self.get_device_serial_numbers(device_model)
            if self.set_onboard_values_for_digital_twin(os_persona, device_model, os_version) != 1:
                kwargs['fail_msg'] = "Fail onboarded device with device_type == Digital Twin"
                self.common_validation.fault(**kwargs)
                return -1

        if location and self.devices_web_elements.get_location_button().is_displayed():
            self.auto_actions.click_reference(self.devices_web_elements.get_location_button)
            self._select_location(location)
            self.screen.save_screen_shot()
            sleep(2)

        if policy_name and self.devices_web_elements.get_devices_quick_add_policy_drop_down().is_displayed():
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_quick_add_policy_drop_down)
            sleep(2)
            self.screen.save_screen_shot()
            self.auto_actions.select_drop_down_options(self.devices_web_elements.
                                                       get_devices_quick_add_policy_drop_down_items(), policy_name)
            sleep(2)


        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_button)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                kwargs['fail_msg'] = "Fail Onboarded - Device already onboarded"
                self.common_validation.failed(**kwargs)
                return -1

            elif "License limit exceeded for managed device" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                kwargs['fail_msg'] = "Fail Onboarded - License limit exceeded for managed device"
                self.common_validation.failed(**kwargs)
                return -1

            elif "A stake record of the device was found in the redirector." in dialog_message:
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                kwargs['fail_msg'] = "Fail Onboarded - A stake record of the device was found in the redirector."
                self.common_validation.failed(**kwargs)
                return -1

            else:
                kwargs['fail_msg'] = f"Dialog Message: {dialog_message}"
                self.common_validation.failed(**kwargs)
                return -1
        else:

            # Code taken from the ap_onboard code.
            # This code was need because it took a longer to onboard an AP on an AIO
            # Updated logic to use a whil loop with a timer so that if the process nerver finishes we will abort and throw an error
            check_process_count = 90
            retry_duration = 2
            count = 1
            while check_process_count > 0:
                # If the quick add block is present, this inidcates the process is not done, then sleep a second and try again
                self.utils.print_info(f"Checking to see if adding device process has completeed: loop {count}")
                if self.devices_web_elements.get_devices_quick_add_block_show():
                    self.utils.print_info(f"Still in adding device process, Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                else:
                    kwargs['pass_msg'] = "Finish device adding process ..."
                    self.common_validation.passed(**kwargs)
                    break
                check_process_count = check_process_count - 1
                count = count + 1
            if check_process_count == 0:
                kwargs['fail_msg'] = "Adding device process never completed"
                self.common_validation.fault(**kwargs)
                return -1

        if "real" in device_type.lower():
            '''
            Nov 22, 2022 - JPS
            The following check is a hack, this was put here until we understand how to work with exos stack devices
            The whole if/else should be removed once we understand how to handle exos stacks
            The current assumption made now, is the device was added to cloud without an error.
            '''

            if device_platform.lower() != "stack":
                if entry_type.lower() == "manual":
                    serials = device_serial.split(",")
                    self.utils.print_info("Serials: ", serials)
                    for serial in serials:
                        if self.search_device(device_serial=serial, ignore_failure=True) == 1:
                            kwargs['pass_msg'] = f"Successfully Onboarded {device_make} Device(s) with {serials}"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['fail_msg'] = f"Fail Onboarded {device_make} device(s) with {serials}"
                            self.common_validation.failed(**kwargs)
                            return -1
            else:
                kwargs[
                    'pass_msg'] = f"Successfully Onboarded a stack of exos Device(s) with serial numbers {device_serial}"
                self.common_validation.passed(**kwargs)
                return 1

        elif "simulated" in device_type.lower():
            models = device_model.split(",")
            self.utils.print_info("Models: ", models)
            for model in models:
                list_final_simulated_serial = self.get_device_serial_numbers(model)
                simulated_global_variable = "${" + name + ".serial}"
                simulated_global_variable_list = []
                for i in list_final_simulated_serial:
                    if i not in list_initial_simulated_serial:
                        simulated_global_variable_list.append(i)
                if len(simulated_global_variable_list) == 1:
                    BuiltIn().set_global_variable(simulated_global_variable, simulated_global_variable_list[0])
                    kwargs['pass_msg'] = f"Successfully Onboarded Device with model : {model}"
                    self.common_validation.passed(**kwargs)
                    return 1
                elif len(simulated_global_variable_list) == 0:
                    kwargs['fail_msg'] = f"Failed to Onboard Device with {model}"
                    self.common_validation.failed(**kwargs)
                    return -1
                elif len(simulated_global_variable_list) > 1:
                    BuiltIn().set_global_variable(simulated_global_variable, simulated_global_variable_list)
                    kwargs['pass_msg'] = f"Successfully Onboarded {device_count} Devices with model : {model}"
                    self.common_validation.passed(**kwargs)
                    return 1

        elif "digital twin" in device_type.lower():
            self.refresh_devices_page()
            list_final_dt_serial = self.get_device_serial_numbers(device_model)
            dt_global_variable = "${" + name + ".serial}"
            for i in list_final_dt_serial:
                if i not in list_initial_serial_dt:
                    BuiltIn().set_global_variable(dt_global_variable, i)
            if len(list_final_dt_serial) - len(list_initial_serial_dt) == 1:
                kwargs['pass_msg'] = f"Successfully Onboarded {device_make} Device with model : {device_model}"
                self.common_validation.passed(**kwargs)
                return 1
            elif len(list_final_dt_serial) - len(list_initial_serial_dt) == 0:
                kwargs['fail_msg'] = f"Failed to onboard device {device_make} with {device_model}"
                self.common_validation.failed(**kwargs)
                return -1
            elif len(list_final_dt_serial) - len(list_initial_serial_dt) > 1:
                kwargs['fail_msg'] = "Failed to determine serial number because multiple devices have been onboarded."
                self.common_validation.failed(**kwargs)
                return -1

    def check_onboard_device_quick_parameters(self, device_type, entry_type, device_serial, device_make, location,
                                              csv_location, device_model, os_version, os_persona, **kwargs):
        """
        This methods is created for validate the Mandatory arguments for onboard device quick method

        :param device_serial: serial number of Device
        :param device_make: Model of the Device ex:aerohive
        :param device_type: Real/Simulated
        :param entry_type: Manual/CSV
        :param csv_location: CSV File Name
        :param device_os: verifies the Device OS automatically selected after entering device serial
        :param location: device location
        :param device_model: device model ex: AP460S6C
        :param os_persona: for Digital Twin
        :return:  1 if validate success
        :return: -1 for error : one or more arguments are missing
        """
        support_onboard_device_types = ["real", "simulated", "digital twin"]

        if device_type is None or device_type.lower() not in support_onboard_device_types:
            kwargs['fail_msg'] = f"The onboarding device type '[{device_type}]' is not not a supported type." \
                                 " onboarding_device_type should be one of the following types:" \
                                 f" {support_onboard_device_types}"
            self.common_validation.fault(**kwargs)
            return -1

        if device_type.lower() == "real":
            if entry_type.lower() == "manual":
                if device_serial is None or device_make is None or location is None:
                    kwargs['fail_msg'] = f"The 'serial': [{device_serial}], 'make': [{device_make}] and 'location': " \
                                         f"[{location}] are required when onboarding 'Real' devices without using a CSV" \
                                         " file. One or more of the required values are missing."
                    self.common_validation.failed(**kwargs)
                    return -1
            elif entry_type.lower() == "csv":
                if device_make is None or csv_location is None:
                    kwargs['fail_msg'] = f"The 'make': [{device_make}] and 'CSV file': [{csv_location}] are required " \
                                         "when onboarding 'Real' devices with using a CSV file. One or more of the " \
                                         "required values are missing."
                    self.common_validation.failed(**kwargs)
                    return -1

        elif device_type.lower() == "simulated":
            if device_model is None or location is None:
                kwargs['fail_msg'] = f"The 'model': [{device_model}] and 'location': [{location}] are required when " \
                                     "onboarding 'Simulated' devices. One or more of the required values are missing."
                self.common_validation.failed(**kwargs)
                return -1

        elif device_type.lower() == "digital twin":
            if device_model is None or os_version is None or os_persona is None:
                kwargs['fail_msg'] = f"The 'model': [{device_model}], 'OS version': [{os_version}] and 'OS persona': " \
                                  f"[{os_persona}] are required when onboarding 'Digital Twin' devices. " \
                                  f"One or more of the required values are missing."
                self.common_validation.failed(**kwargs)
                return -1
        return 1

    def set_onboard_values_for_real(self, device_serial, device_make, entry_type, device_os, service_tag, device_mac, location):
        """
        This method is create for onboard device with device_type == Real
        """

        self.auto_actions.click_reference(self.devices_web_elements.get_device_type_real_radio_button)

        if entry_type:
            if 'Manual' in entry_type:
                self.utils.print_info("Selecting Entry Type : Manual")
                self.auto_actions.click_reference(self.devices_web_elements.get_entry_type_manual_radio_button)

        self.utils.print_info("Entering Serial Number...", device_serial)
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
        sleep(5)

        # Depending of the serial number enter the user will see 2 options
        # 1 - Drop Down menu
        # 2 - radio buttons one for 'Cloud IQ Engine' and one for 'WING'
        # Check to see if the drop-down-menu is present if it is use else click on one of the radio buttons
        if 'Extreme - Aerohive' in device_make:
            if self.switch_web_elements.get_switch_make_drop_down().is_displayed():
                self.utils.print_info("Selecting Device Type : Extreme - Aerohive")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options()
                                                           , "Extreme - Aerohive")
                self.screen.save_screen_shot()
            else:
                if self.devices_web_elements.get_device_os_radio():
                    self.utils.print_info("Verify Cloud IQ Engine Device OS Radio Button Status")
                    device_os = self.devices_web_elements.get_device_os_radio().text
                    self.utils.print_info("Device OS: ", device_os)
                    if 'Cloud IQ Engine' in device_os:
                        self.utils.print_info("Device OS matched")
                    else:
                        self.utils.print_info("Selecting Device OS: Cloud IQ Engine")
                        self.auto_actions.click_reference(self.devices_web_elements.get_device_os_radio)
                    self.screen.save_screen_shot()

            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        # Depending of the serial number enter the user will see 2 options
        # 1 - Drop Down menu
        # 2 - radio buttons one for SwitchEngine and one for FabricEngine
        # Check to see if the drop-down-menu is present if it is use else click on one of the radio buttons
        elif "VOSS" in device_make.upper():
            self.utils.print_info("Selecting Switch Type/Device OS : VOSS/Fabric Engine")
            if self.switch_web_elements.get_switch_make_drop_down().is_displayed():
                self.utils.print_info("Selecting Switch Type : VOSS")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.screen.save_screen_shot()
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options()
                                                           , "VOSS")
                self.screen.save_screen_shot()

            else:
                self.utils.print_info(f"Select {device_make} Radio Button")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_voss_radio)
                sleep(2)
                self.screen.save_screen_shot()
        elif "EXOS" in device_make.upper():
            self.utils.print_info("Selecting Switch Type/Device OS : EXOS/Switch Engine")
            if self.switch_web_elements.get_switch_make_drop_down().is_displayed():
                self.utils.print_info("Selecting Switch Type : EXOS")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.screen.save_screen_shot()
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options(),
                                                           "EXOS")
                self.screen.save_screen_shot()
            else:
                self.utils.print_info(f"Select {device_make} Radio Button")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_exos_radio)
                sleep(2)
                self.screen.save_screen_shot()

        elif 'DELL' in device_make.upper():
            if self.switch_web_elements.get_switch_make_drop_down().is_displayed():
                self.utils.print_info("Selecting Switch Type : DELL")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options(),
                                                           "DELL")
                self.screen.save_screen_shot()

            self.utils.print_info(f"Entering Service Tag {service_tag}")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_service_tag_textbox(), service_tag)

            # Please not the check_negative_combinations does throw an error if an invalid service tag is entered
            # If that is needed please update check_negative_combinations
            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        elif 'Universal Appliance' in device_make:
            if self.switch_web_elements.get_switch_make_drop_down().is_displayed():
                self.utils.print_info("Selecting Device Type : Universal Appliance")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.screen.save_screen_shot()
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options()
                                                           , "Universal Appliance")
            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        elif 'XMC' in device_make.upper():
            # JPS - Feb 15th 2023 not sure why we are adding a serial number a second time
            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        elif 'CONTROLLERS' in device_make.upper() or 'XCC' in device_make.upper() or 'WING' in device_make.upper():
            self.utils.print_info("Selecting Device Make Controller")
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_drop_down)
            sleep(2)

            self.utils.print_info("Selecting Device Make: ", device_make)
            self.auto_actions.select_drop_down_options(
            self.devices_web_elements.get_device_make_drop_down_options(), "CONTROLLERS")
            self.auto_actions.send_keys(self.devices_web_elements.get_wing_devices_mac_text_area(), device_mac)

            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        if 'DUAL BOOT' in device_make.upper():
            # The assumption here is this type of system can be either:
            # - Cloud IQ Engine
            # - Wing
            # I have added logic if the OS type is WING we should enable the wing radio button*
            # *As of Feb 24 2023, I can find a SERIAL Number that enables the wing radio button
            # So this code is untested.
            if 'Cloud IQ Engine' in device_os:
                self.utils.print_info("Selecting Device Type : Cloud IQ Engine")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_radio)
            elif 'WING' in device_os.upper():
                self.utils.print_info("Selecting Device Type : WING")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_wing_radio)

        return 1

    def set_onboard_values_for_simulated(self, device_model, device_count):
        """
        This method sets the onboard device options when the device_type == Simulated
        """

        # Code copied from 'onboard_simulated_device'
        self.utils.print_info("Selecting 'Simulated' Device Type radio button")
        self.auto_actions.click_reference(self.devices_web_elements.get_quick_onboard_simulated)
        self.auto_actions.click_reference(self.devices_web_elements.get_simulated_devices_dropdown)
        options = self.devices_web_elements.get_simulated_devices_dropdown_items()
        for option in options:
            if device_model in option.text:
                self.utils.print_info("Simulated device option: ", option.text)
                self.auto_actions.click(option)

        self.utils.print_info(f"Entering Device Count: {device_count}")
        self.auto_actions.send_keys(self.devices_web_elements.get_simulation_device_count_input_field(), device_count)
        return 1

    def set_onboard_values_for_digital_twin(self, os_persona, device_model, os_version, **kwargs):
        """
        This method sets the onboard device options when the device_type == Digital Twin
        """

        # Code specific to Digital Twin devices - Code copied from 'onboard_device_dt'
        self.retries = 3
        count = 0
        while count < self.retries:
            # Commented on 1/18/23 because it is unused
            # add_device_button = "Launch Digital Twin"
            sleep(1)
            attribute = self.devices_web_elements.get_digital_twin_container_feature().get_attribute("class")
            try:
                assert attribute == "fn-hidden"
            except AssertionError:
                count += 1
        if count == self.retries:
            self.utils.print_warning("Unable to get the attribute...")

        if "fn-hidden" not in attribute:
            self.utils.print_info("Selecting 'Digital Twin' radio button")
            self.auto_actions.click_reference(self.devices_web_elements.get_device_type_digital_twin_radio_button)

            self.utils.print_debug(f"Selecting OS Persona: {os_persona}")
            self.auto_actions.click_reference(self.devices_web_elements.get_digital_twin_os_persona_dropdown)
            sleep(2)
            if self.auto_actions.select_drop_down_options(
                    self.devices_web_elements.get_digital_twin_os_persona_dropdown_items(), os_persona):
                self.utils.print_info(f"OS Persona set to: {os_persona}")
            else:
                kwargs['fail_msg'] = f"Could not select OS Persona: {os_persona}"
                self.common_validation.failed(**kwargs)
                return -1
            self.utils.print_debug(f"Selecting Device Model: {device_model}")
            self.auto_actions.click_reference(self.devices_web_elements.get_digital_twin_device_model_dropdown)
            sleep(2)
            if self.auto_actions.select_drop_down_options(
                    self.devices_web_elements.get_digital_twin_device_model_dropdown_items(), device_model):
                self.utils.print_info(f"Device Model set to: {device_model}")
            else:
                kwargs['fail_msg'] = f"Could not select Device Model: {device_model}"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_debug(f"Selecting OS Version: {os_version}")
            self.auto_actions.click_reference(self.devices_web_elements.get_digital_twin_os_version_dropdown)
            sleep(2)
            if self.auto_actions.select_drop_down_options(
                    self.devices_web_elements.get_digital_twin_os_version_dropdown_items(), os_version):
                self.utils.print_info(f"OS Version set to: {os_version}")
            else:
                kwargs['fail_msg'] = f"Could not select OS Version: {os_version}"
                self.common_validation.failed(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "Digital Twin option is not available..."
            self.common_validation.failed(**kwargs)
            return -1

        return 1

    @deprecated("Please use onboard_device_quick(...)")
    def onboard_device(self, device_serial, device_make, device_mac=False, device_type="Real", entry_type="Manual",
                       csv_file_name='', device_os=False, location=False, policy_name=False, service_tag=False,
                       **kwargs):
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
        :param policy_name: network policy
        :param service_tag: Dell Service Tag
        :return:  1 if onboarding success
        :return: -2 for error - Serial numbers entered are from different platform families. Please enter serial numbers that are part of the same platform family. Please remove serial number
        :return: -3 for error - Could not recognize 166A129943554583. Please onboard 166A129943554583 separately.
        :return: -4 for error - No more than 10 serial numbers could be entered at once.
        :return: -5 for error - When onboarding multiple devices, serial numbers must be separated by ", " (Commas).
        :return: -6 for error - The number of MAC Addresses must match the number of Serial Numbers
        :return: -7 for error - Please enter a valid MAC Address
        :return: -8 for error - Unable to get pop-up menu item
        """

        self.utils.print_info("Onboarding: ", device_make)

        if 'Controllers' in device_make or 'XCC' in device_make:
            return self._onboard_wing_ap(device_serial, device_mac, device_make, location)

        if 'Dual Boot' in device_make:
            return self._onboard_ap(device_serial, device_make, location, device_os)

        self.navigator.navigate_to_devices()

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        quick_add_devices_button = ''
        attempt_count = 3
        while attempt_count > 0:
            if attempt_count != 3:
                self.utils.print_info("Menu selection failed. Making another attempt...")
                self.utils.print_info("Clicking on ADD button...")
                self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)
                self.utils.print_info("Selecting Quick Add Devices menu")
                sleep(4)
            try:
                quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
                self.auto_actions.move_to_element(quick_add_devices_button)
                break
            except Exception:
                attempt_count = attempt_count - 1
        if attempt_count == 0:
            self.utils.print_info("Unable to get / click the menu option")
            return -8

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)

        if device_type:
            self.utils.print_info("Selecting Real/Simulated Device Type Dropdown")
            sleep(2)
            self.auto_actions.click_reference(self.devices_web_elements.get_device_type_real_radio_button)

        self.utils.print_info("Entering Serial Number...", device_serial)
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)
        sleep(5)

        if 'Extreme - Aerohive' in device_make:
            if entry_type:
                if 'Manual' in entry_type:
                    self.auto_actions.click_reference(self.devices_web_elements.get_entry_type_manual_radio_button)

                if 'CSV' in entry_type:
                    self.auto_actions.click_reference(self.devices_web_elements.get_entry_type_csv_radio_button)

                if entry_type == "CSV":
                    upload_button = self.devices_web_elements.get_device_entry_csv_upload_button()
                    csv_location = self.custom_file_dir + csv_file_name
                    self.auto_actions.send_keys(upload_button, csv_location)

            self.utils.print_info("Entering Serial Number...")
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)

            if self.devices_web_elements.get_device_os_radio():
                self.utils.print_info("Verify Cloud IQ Engine Device OS Radio Button Status")
                device_os = self.devices_web_elements.get_device_os_radio().text
                self.utils.print_info("Device OS: ", device_os)
                if 'Cloud IQ Engine' in device_os:
                    self.utils.print_info("Device OS matched")
                else:
                    self.utils.print_info("Selecting Device OS: Cloud IQ Engine")
                    self.auto_actions.click_reference(self.devices_web_elements.get_device_os_radio)

            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors
        # Select the 'Device Make' field value and enter the serial number depending on which device type is being added
        if "VOSS" in device_make.upper():
            self.utils.print_info("Selecting Switch Type/Device OS : VOSS/Fabric Engine")
            if self.switch_web_elements.get_switch_make_drop_down():
                self.utils.print_info("Selecting Switch Type : VOSS")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.screen.save_screen_shot()
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options()
                                                           , "VOSS")
                self.screen.save_screen_shot()

            if self.devices_web_elements.get_device_os_voss_radio():
                self.utils.print_info("Selecting Device OS : Fabric Engine")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_voss_radio)
                self.screen.save_screen_shot()

            if entry_type == "CSV":
                if csv_location:
                    upload_button = self.devices_web_elements.get_device_entry_voss_csv_upload_button()
                    if upload_button:
                        self.utils.print_info("Specifying CSV file '" + csv_location + "' for VOSS device")
                        self.auto_actions.send_keys(upload_button, csv_location)
                    else:
                        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
                        kwargs['fail_msg'] = "CSV file could not be specified - upload button not located"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
                    kwargs['fail_msg'] = "CSV file was not specified - device NOT on-boarded"
                    self.common_validation.failed(**kwargs)
                    return -1

        if "EXOS" in device_make.upper():
            self.utils.print_info("Selecting Switch Type/Device OS : EXOS/Switch Engine")
            if self.switch_web_elements.get_switch_make_drop_down():
                self.utils.print_info("Selecting Switch Type : EXOS")
                self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
                self.screen.save_screen_shot()
                self.auto_actions.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options(),"EXOS")
                self.screen.save_screen_shot()

            if self.devices_web_elements.get_device_os_exos_radio():
                self.utils.print_info("Selecting Device OS : Switch Engine")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_exos_radio)
                self.screen.save_screen_shot()

            if entry_type == "CSV":
                if csv_location:
                    upload_button = self.devices_web_elements.get_device_entry_exos_csv_upload_button()
                    if upload_button:
                        self.utils.print_info("Specifying CSV file '" + csv_location + "' for EXOS device")
                        self.auto_actions.send_keys(upload_button, csv_location)
                    else:
                        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
                        kwargs['fail_msg'] = "CSV file could not be specified - upload button not located"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
                    kwargs['fail_msg'] = "CSV file was not specified - device NOT on-boarded"
                    self.common_validation.failed(**kwargs)
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
            self.auto_actions.click_reference(self.devices_web_elements.get_location_button)
            self._select_location(location)

        if policy_name:
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_quick_add_policy_drop_down)
            sleep(2)
            self.screen.save_screen_shot()
            self.auto_actions.select_drop_down_options(self.devices_web_elements.
                                                       get_devices_quick_add_policy_drop_down_items(), policy_name)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_button)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}", default='-200'))
                self._exit_here(BuiltIn().get_variable_value("${EXIT_LEVEL}"))
                kwargs['fail_msg'] = "Fail Onboarded - Device already onboarded"

            elif "License limit exceeded for managed device" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}", default='-200'))
                self._exit_here(BuiltIn().get_variable_value("${EXIT_LEVEL}"))
                kwargs['fail_msg'] = "Fail Onboarded - License limit exceeded for managed device"

            else:
                self.utils.print_info(f"Dialog Message: {dialog_message}")
                kwargs['fail_msg'] = f"Dialog Message: {dialog_message}"

            self.common_validation.failed(**kwargs)
            return -1
        else:
            self.utils.print_info("No Dialog box")

        serials = device_serial.split(",")
        self.utils.print_info("Serials: ", serials)

        max_retries = 3
        count = 0
        while max_retries != count:
            for serial in serials:
                if self.search_device(device_serial=serial, ignore_failure=True) == 1:
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = f"Fail Onboarded {device_make} device(s) with {serials}"
                    if count != max_retries:
                        self.utils.print_info(f"The {serial} was not found, sleeping for 10 seconds")
                        sleep(10)
                        count += 1
                        self.utils.print_info(f"new count value {count} of max reties {max_retries}")

        self.common_validation.failed(**kwargs)
        return -1

    def wait_for_device_to_finish_update(self, device_serial=None, device_name=None, device_mac=None, retry_duration=10,
                                         retry_count=30, **kwargs):
        """
        - This keyword waits for the device to finish updates
        - This keyword by default loop over every 10 seconds for up to 5 minutes to check the device updated status
        - Flow:
        - check the device status for a device based on passed device serial/device mac/device_name
        - Keyword Usage:
        - ``wait_for_device_to_finish_update       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12``
        - ``wait_for_device_to_finish_update       ${DEVICE_MAC}           retry_duration=15       retry_count=5``

        :param device_serial: device serial number to check the device update status, by default set to None
        :param device_mac: device mac to check the device update status, by default set to None
        :param device_name: device name to check the device update status, by default set to None
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device finished update, else -1
        """
        update_status = ['Querying', 'IQ Engine Firmware Updating', 'User Configuration Updating', 'Rebooting',
                         'Certification Updating', 'Firmware Updating']
        device_update_status = ""
        for delay in range(retry_count):
            self.utils.print_info(f"Device Update Status Check - Loop: {delay+1}")
            device_update_status = self.get_device_updated_status(device_serial=device_serial, device_mac=device_mac,
                                                                  device_name=device_name)

            if device_update_status not in update_status:
                kwargs['pass_msg'] = f"Device status is {device_update_status}. Device finished update!"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Device status is {device_update_status}. Waiting for {retry_duration}s")
                sleep(retry_duration)
                if delay == retry_count - 1:
                    kwargs['fail_msg'] = f"Device status is still {device_update_status}. " \
                                         "Device didn't finish update within time!"
                    self.common_validation.failed(**kwargs)
                    return -1

        kwargs['fail_msg'] = "Failed to get device update status. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def delete_device(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        - Deletes Device matching either any of either one of serial, name, MAC
        - Keyword Usage:
        - ``Delete Device    device_serial=${DEVICE_SERIAL}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device serial number, by default set to None
        :param device_name: name of the device, by default set to None
        :param device_mac: mac address of the device, by default set to None
        :param kwargs: keyword arguments XAPI_ENABLE
        :return: 1 if device deleted successfully or is already deleted/does not exist, else -1
        """
        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_delete_device( device_serial=device_serial,
                                                        device_name=device_name,
                                                        device_mac=device_mac,
                                                        **kwargs)

        num_device_params = 0
        search_device = None
        search_type = None
        self.navigator.enable_page_size()

        if device_serial:
            num_device_params += 1
            search_type = "device_serial"
            search_device = device_serial
        if device_name:
            num_device_params += 1
            search_type = "device_name"
            search_device = device_name
        if device_mac:
            num_device_params += 1
            search_type = "device_mac"
            search_device = device_mac

        if num_device_params != 1:
            kwargs['fail_msg'] = f"Expected one device parameter to delete. Instead received {num_device_params}"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            self.utils.print_info(f"Deleting device with {search_type}: {search_device}")
            search_result = self.search_device(device_serial=device_serial, device_name=device_name,
                                               device_mac=device_mac, ignore_failure=True)

            if search_result != -1:
                if self.wait_until_device_update_done(device_serial=device_serial, device_mac=device_mac, device_name=device_name):
                    if self.select_device(device_serial=device_serial, device_name=device_name, device_mac=device_mac):
                        self.utils.print_info("Click delete button")
                        self.auto_actions.click_reference(self.devices_web_elements.get_delete_button)

                        self.utils.print_info("Click confirmation Yes Button")
                        self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button)
                        self.screen.save_screen_shot()

                        # Wait until 'loading' mask is cleared
                        self.navigator.wait_until_devices_load_spinner_cleared(retry_duration=1, retry_count=180)

                        # Wait until the device is removed from the view
                        result = self.wait_until_device_removed(device_serial=device_serial, device_name=device_name,
                                                                device_mac=device_mac, retry_duration=10, retry_count=6)
                        # If result is 1 then the device was deleted and could not be found by wait_until_device_removed
                        if result == 1:
                            kwargs['pass_msg'] = f"Deleted device successfully with {search_type}: {search_device}"
                            self.common_validation.passed(**kwargs)
                            return 1

                        # Confirm device was deleted successfully
                        if self.search_device(device_serial=device_serial, device_name=device_name,
                                              device_mac=device_mac, ignore_failure=True) == 1:
                            kwargs['fail_msg'] = f"Unable to delete the device with {search_type}: {search_device}"
                            self.common_validation.failed(**kwargs)
                            return -1
                        else:
                            kwargs['pass_msg'] = "Deleted Device Successfully!"
                            self.common_validation.passed(**kwargs)
                            return 1
            else:
                kwargs['pass_msg'] = f"Device with {search_type}: {search_device} does not exist / is already deleted"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Device was not deleted. Make sure to specify a serial, name, or MAC"
        self.common_validation.failed(**kwargs)
        return -1

    def _select_and_delete(self, device_dict):
        """
        - This helper is used in delete_device_by_object() only to select and click on delete button

        :param device_dict: data passed as a dictionary

        :return: 1 if device deleted successfully, False if it was unable to delete the device
        """

        self.select_device_by_object(device_dict, skip_refresh=True, skip_navigation=True)
        self.utils.print_info("Click delete button")
        self.auto_actions.click_reference(self.devices_web_elements.get_delete_button)

        self.utils.print_info("Click confirmation Yes Button")
        self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button)
        self.screen.save_screen_shot()

        # Wait until 'loading' mask is cleared
        self.navigator.wait_until_devices_load_spinner_cleared(retry_duration=1, retry_count=180)

        # Wait until the device is removed from the view
        result = self.wait_until_device_removed_by_object(device_dict, retry_duration=10, retry_count=6)
        # If result is 1 then the device was deleted and could not be found by wait_until_device_removed
        if result == 1:
            self.utils.print_info(f"Deleted device successfully with {device_dict}")
            return 1

        # Confirm device was deleted successfully
        if self.search_device_by_object(device_dict, skip_navigation=True, ignore_failure=True) == 1:
            self.utils.print_info(f"Unable to delete the device with {device_dict}")
            return False
        else:
            self.utils.print_info(f"Device with {device_dict} was deleted successfully!")
            return 1

    def delete_device_by_object(self, *device_dict, **kwargs):
        """
        - Deletes Device matching either any of either one of serial, name, MAC
        - Keyword Usage:
        - ``Delete Device    device_serial=${ap1}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1)
        :param kwargs: keyword arguments XAPI_ENABLE
        :return: 1 if device deleted successfully or is already deleted/does not exist, else -1
        """
        device_dict = device_dict[0]
        device_serial = device_dict.get("serial")
        device_mac = device_dict.get("mac")
        device_name = device_dict.get("name")
        device_type = device_dict.get("platform")

        device_keys = {
            "mac": device_dict.get("mac"),
            "serial": device_dict.get("serial"),
            "name": device_dict.get("name"),
            "platform": device_dict.get("platform")
        }
        device_keys = {key: value for key, value in device_keys.items() if value}

        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "Invalid args. You must pass in at least one of the following: serial, name, or mac!"
            self.common_validation.fault(**kwargs)
            return -1

        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_delete_device(device_serial=device_serial, device_name=device_name,
                                                       device_mac=device_mac, **kwargs)

        self.navigator.enable_page_size()
        self.utils.print_info(f"Deleting device with {device_keys}")

        if device_type == "Stack":
            dict_stack = {'mac': device_mac}
            search_result = self.search_device_by_object(dict_stack, ignore_failure=True)
            if search_result != -1:
                if self.wait_until_device_update_done(device_mac=device_mac, skip_navigation=True, skip_refresh=True):
                    if self._select_and_delete(dict_stack):
                        kwargs['pass_msg'] = "Deleted Device Successfully!"
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"Unable to delete the device with {dict_stack}"
                        self.common_validation.failed(**kwargs)
                        return -1

            elif "," in device_serial:
                serials = device_serial.split(",")
                device_found = -1
                for serial in serials:
                    dict_serial = {'serial': serial}
                    if self.search_device_by_object(dict_serial, skip_refresh=True, skip_navigation=True, ignore_failure=True) != -1:
                        device_found = 1
                        if self.wait_until_device_update_done(device_serial=serial, skip_navigation=True, skip_refresh=True):
                            if not self._select_and_delete(dict_serial):
                                kwargs['fail_msg'] = f"Unable to delete the device with {dict_serial}"
                                self.common_validation.failed(**kwargs)
                                return -1

                if device_found == 1:
                    kwargs['pass_msg'] = "Device(s) successfully deleted!"
                    self.common_validation.passed(**kwargs)
                    return 1

            kwargs['pass_msg'] = f"Device with {device_keys} does not exist / is already deleted!"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            search_result = self.search_device_by_object(device_keys, ignore_failure=True)
            if search_result != -1:
                if self.wait_until_device_update_done(device_serial=device_serial, device_mac=device_mac,
                                                      device_name=device_name, skip_navigation=True, skip_refresh=True):
                    if self._select_and_delete(device_keys):
                        kwargs['pass_msg'] = "Deleted Device Successfully!"
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"Unable to delete the device with {device_keys}"
                        self.common_validation.failed(**kwargs)
                        return -1

            else:
                kwargs['pass_msg'] = f"Device with {device_keys} does not exist / is already deleted"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Device was not deleted. Make sure to pass a data as a dictionary!"
        self.common_validation.fault(**kwargs)
        return -1

    def delete_devices(self, *device_list, **kwargs):
        """
        - Deletes the list of devices denoted by serial numbers
        - Keyword Usage:
        - ``Delete Devices    ${DEVICE_SERIAL1}  ${DEVICE_SERIAL2}  ${DEVICE_SERIAL3}``

        :param device_list: list of device serial numbers to delete
        :return: 1 if devices deleted successfully or are already deleted/do not exist, else -1
        """
        ret_val = 1
        deleted_devices = []
        not_deleted_devices = []

        self.navigator.enable_page_size()

        # Select all the specified devices
        self.utils.print_info("Deleting devices: ", device_list)
        for device_ in device_list:
            if device_ == device_list[0]:
                self.select_device(device_)
                self.utils.print_info(f"Selected device {device_}")
            else:
                self.select_device(device_, skip_refresh=True, skip_navigation=True)
                self.utils.print_info(f"Selected device {device_}")

        sleep(2)
        # Now that all devices to delete are selected, perform the delete action
        self.utils.print_info("Click delete button")
        self.auto_actions.scroll_up()
        sleep(2)
        self.auto_actions.click_reference(self.devices_web_elements.get_delete_button)
        sleep(2)

        self.utils.print_info("Click confirmation Yes Button")
        self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button)
        sleep(2)
        self.screen.save_screen_shot()

        # Confirm devices were deleted successfully
        self.refresh_devices_page()
        for device_ in device_list:
            search_result = self.search_device(device_serial=device_, ignore_failure=True)
            if search_result == 1:
                self.utils.print_info(f"Device {device_} was not deleted")
                not_deleted_devices.append(device_)
                ret_val = -1
            else:
                self.utils.print_info(f"Device {device_} was deleted")
                deleted_devices.append(device_)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Devices were not deleted: {not_deleted_devices}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Devices were deleted: {deleted_devices}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def _find_device_row(self, device_keys, **kwargs):
        """
        - This helper function searches for the device in all of the pages and returns its row
        :param device_keys: dictionary of the device. Key-value pairs. E.g: serial: 01501707240150, mac: 885BDD4BE380
        
        :return: row if device found else False
        """

        # reset the page number to 1
        pageOne = self.devices_web_elements.get_devices_page_number_one()
        if pageOne != None:
            self.utils.print_info("Clicking on Page 1 in devices page.")
            self.auto_actions.click(pageOne)

        device_page_numbers = self.devices_web_elements.get_page_numbers()
        if device_page_numbers and device_page_numbers.text:
            page_len = int(max(device_page_numbers.text))
        else:
            page_len = int(1)

        num_pages = page_len
        try:
            while page_len:
                page_num = num_pages - page_len + 1
                self.utils.print_debug(f"Searching Page #{page_num} of {num_pages} pages")
                retry = 2
                while retry > 0:
                    try:
                        rows = self.devices_web_elements.get_grid_rows()
                        if rows:
                            self.utils.print_debug(f"Searching {len(rows)} rows")
                            for key, value in device_keys.items():
                                self.utils.print_info(f"Searching for the device using {key} : {value}")
                                for row in rows:
                                    self.utils.print_info("row data: ", self.format_row(row.text))
                                    if value in row.text:
                                        self.utils.print_info(f"Found device with {key}: {value}")
                                        return row
                        else:
                            self.utils.print_debug(f"No rows returned for page #{page_num}")
                        retry = 0 # no exceptions on rows, set to retry to 0
                    except StaleElementReferenceException:
                        self.utils.print_info("Exception in row data (usually caused by XIQ device grid not finished), sleeping and retrying")
                        sleep(1)
                        retry = retry - 1
                page_len = page_len - 1

                if page_len:
                    self.utils.print_info("Searching in next page")
                    self.auto_actions.click_reference(self.devices_web_elements.get_grid_rows_next)
                    sleep(5)

            self.utils.print_info(f"Did not find device row with {device_keys}")
            return False

        except StaleElementReferenceException:
            self.utils.print_info(f"Handling StaleElementReferenceException - loop {page_len}")

        kwargs['fail_msg'] = "Unable to find the device"
        self.common_validation.fault(**kwargs)
        return -1

    def search_device(self, device_serial=None, device_name=None, device_mac=None, select_device=False,
                      skip_refresh=False, skip_navigation=False, **kwargs):
        """
        - Searches for the device using serial, name, MAC and selects it if desired
        - Supported Modes:
          - UI - default mode
          - XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)


        :param device_serial: serial number of the device, by default set to None
        :param device_name: name of the device, by default set to None
        :param device_mac: MAC of the device, by default set to None
        :param select_device: True - to select the device, default set to False
        :param skip_refresh: True - to skip the refresh of the devices page, default set to False
        :param skip_navigation: True - to skip the navigation to the devices page, default set to False
        :param kwargs: keyword arguments XAPI_ENABLE

        :return: 1 if device found else -1
        """

        # We need to skip this when we are selecting a device
        if self.xapiDevices.is_xapi_enabled(**kwargs) and not select_device:
            return self.xapiDevices.xapi_search_device(device_serial=device_serial,
                                                       device_name=device_name,
                                                       device_mac=device_mac,
                                                       **kwargs)

        device_keys = {}
        if device_mac:
            device_keys['device_mac'] = device_mac
        if device_serial:
            device_keys['device_serial'] = device_serial
        if device_name:
            device_keys['device_name'] = device_name
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "Invalid args. You must pass in at least one of the following: device_serial, " \
                                 "device_name, or device_mac!"
            self.common_validation.fault(**kwargs)
            return -1

        # navigate to devices page and refresh
        if not skip_navigation:
            self.navigator.navigate_to_devices()
        if not skip_refresh:
            self.refresh_devices_page()

        row = self._find_device_row(device_keys)
        if row:
            kwargs['pass_msg'] = f"Device with {device_keys} was found!"
            if select_device:
                self.screen.save_screen_shot()
                self.utils.print_info(f"Selecting device: '{device_keys}'")
                # Is the device already selected?  If not select it
                checkbox = self.devices_web_elements.get_device_select_checkbox(row)
                if checkbox:
                    if checkbox.is_selected() == False:
                        self.utils.print_info(f"Device: '{device_keys}' is not currently selected.  Clicking now to select the device")
                        self.auto_actions.click_reference(lambda: self.devices_web_elements.get_device_select_checkbox(row))
                    else:
                        self.utils.print_info(f"Device: '{device_keys}' is already selected")

                    # Make sure the device is currently selected.  Try 3 times because we could be checking too soon
                    for attempt in range(3):
                        checkbox = self.devices_web_elements.get_device_select_checkbox(row)
                        if checkbox and checkbox.is_selected():
                            break
                        sleep(1)
                    if checkbox and checkbox.is_selected():
                        kwargs['pass_msg'] = f"Device: '{device_keys}' was found and selected"
                    else:
                        kwargs['fail_msg'] = f"Unable to get checkbox for row: '{row}' and device '{device_keys}'"
                        if checkbox:
                            kwargs['fail_msg'] = f"Checkbox for device: '{device_keys}' is_selected = {checkbox.is_selected()}"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = f"Unable to get element for device '{device_keys}'"
                    self.common_validation.fault(**kwargs)
                    return -1

            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = f"Did not find device row with {device_keys}"
        self.common_validation.failed(**kwargs)
        return -1

    def search_device_by_object(self, *device_dict, select_device=False, skip_refresh=False, skip_navigation=False, **kwargs):
        """
        - Searches for the device using serial, name or MAC, and selects it if desired
        - Supported Modes:
          - UI - default mode
          - XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1)
        :param select_device: True - to select the device, default set to False
        :param skip_refresh: True - to skip the refresh of the devices page, default set to False
        :param skip_navigation: True - to skip the navigation to the devices page, default set to False
        :param kwargs: keyword arguments XAPI_ENABLE

        :return: 1 if device found else -1
        """
        device_dict = device_dict[0]
        device_serial = device_dict.get("serial")
        device_mac = device_dict.get("mac")
        device_name = device_dict.get("name")

        device_keys = {
            "mac": device_dict.get("mac"),
            "serial": device_dict.get("serial"),
            "name": device_dict.get("name")
        }

        device_keys = {key: value for key, value in device_keys.items() if value}
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "Invalid args. You must pass in at least one of the following: serial, name, or mac!"
            self.common_validation.fault(**kwargs)
            return -1

        # We need to skip this when we are selecting a device
        if self.xapiDevices.is_xapi_enabled(**kwargs) and not select_device:
            return self.xapiDevices.xapi_search_device(device_serial=device_serial, device_name=device_name,
                                                       device_mac=device_mac, **kwargs)

        # navigate to devices page and refresh
        if not skip_navigation:
            self.navigator.navigate_to_devices()
        if not skip_refresh:
            self.refresh_devices_page()

        row = self._find_device_row(device_keys)
        if row:
            kwargs['pass_msg'] = f"Device with {device_keys} was found!"
            if select_device:
                self.auto_actions.click_reference(lambda: self.devices_web_elements.get_device_select_checkbox(row))
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = f"Device with {device_keys} was found and selected"
            self.common_validation.passed(**kwargs)
            return 1

        if device_serial:
            if "," in device_serial:
                serials = device_serial.split(",")
                serials_found = []
                for serial in serials:
                    dict_serial = {'serial': serial}
                    row = self._find_device_row(dict_serial)
                    if row:
                        self.utils.print_info(f"Device with {dict_serial} was found!")
                        if select_device:
                            self.auto_actions.click_reference(lambda: self.devices_web_elements.get_device_select_checkbox(row))
                            self.screen.save_screen_shot()
                            self.utils.print_info(f"Device with {dict_serial} was found and selected")
                        serials_found.append(serial)

                kwargs['pass_msg'] = f"Device serials found: {serials_found}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = f"Did not find device row with {device_keys}"
        self.common_validation.failed(**kwargs)
        return -1

    def select_device(self, device_serial=None, device_name=None, device_mac=None,
                      skip_refresh=False, skip_navigation=False, **kwargs):
        """
        - Selects the device matching device's Serial Number,Device Mac address and device mane
        - Keyword Usage:
        - ``Select Device      device_serial=${DEVICE_SERIAL}``
        - ``Select Device      device_name=${DEVICE_NAME}``
        - ``Select Device      device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial, by default set to None
        :param device_name: device host name, by default set to None
        :param device_mac: device MAC address, by default set to None
        :param skip_refresh: True - to skip the refresh of the devices page, default set to False
        :param skip_navigation: True - to skip the navigation to the devices page, default set to False

        :return: return 1 if device found else -1
        """
        return self.search_device(device_serial=device_serial, device_mac=device_mac, device_name=device_name,
                                  select_device=True, skip_refresh=skip_refresh, skip_navigation=skip_navigation, **kwargs)

    def select_device_by_object(self, *device_dict, skip_refresh=False, skip_navigation=False, **kwargs):
        """
        - Selects the device matching device's Serial Number,Device Mac address and device mane
        - Keyword Usage:
        - ``Select Device      device_serial=${ap1}``

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1):
        :param skip_refresh: True - to skip the refresh of the devices page, default set to False
        :param skip_navigation: True - to skip the navigation to the devices page, default set to False

        :return: return 1 if device found else -1
        """
        return self.search_device_by_object(*device_dict, select_device=True, skip_refresh=skip_refresh,
                                            skip_navigation=skip_navigation, **kwargs)

    def _get_row(self, key, value):
        device_row = -1
        if key == "device_serial":
            device_row = self.get_device_row(device_serial=value)
        elif key == "device_mac":
            device_row = self.get_device_row(device_mac=value)
        elif key == "device_name":
            device_row = self.get_device_row(device_name=value)
        return device_row

    def get_device_status(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        - This keyword returns the device's connection status, audit log status
        - Keyword Usage:
        - ``Get Device Status   device_serial=${DEVICE_SERIAL}``
        - ``Get Device Status   device_name=${DEVICE_NAME}``
        - ``Get Device Status   device_mac=${DEVICE_MAC}``
        - ``Get Device Status   device_serial=${DEVICE_SERIAL}  device_mac=${DEVICE_MAC}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device Serial, by default set to None
        :param device_name: device host name, by default set to None
        :param device_mac: device MAC address, by default set to None
        :return:
        - 'green' if device connected and config audit match
        - 'config audit mismatch' if device connected and config audit mismatch
        - 'disconnected' if device disconnected and unable to connect after 10 minutes
        - 'unknown' if device connection status is 'Unknown'

        """

        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_get_device_status(device_serial=device_serial, device_name=device_name,
                                                       device_mac=device_mac, **kwargs)

        # UI Support
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        device_row = ''
        device_keys = {}
        device_status = ''
        audit_config_status = ''
        if device_mac:
            device_keys['device_mac'] = device_mac
        if device_serial:
            device_keys['device_serial'] = device_serial
        if device_name:
            device_keys['device_name'] = device_name
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "No valid args passed. Must be device_serial, device_name, device_mac!"
            self.common_validation.fault(**kwargs)
            return "Unknown"

        if self.cobj_web_elements.get_page_size_element():
            self.auto_actions.click_reference(self.cobj_web_elements.get_page_size_element)
            self.screen.save_screen_shot()
            sleep(5)

        # Refresh the devices table before printing contents and before searching for our row
        self.refresh_devices_page()

        # Printing all the rows in the table for troubleshooting
        self.utils.print_info("*** Print all rows in devices table: START ***")
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info("row data: ", self.format_row(row.text))
        else:
            self.utils.print_info("No rows present")
        self.utils.print_info("*** Print all rows in devices table: END ***")

        # Get the device status and the audit config status which are the two icon on the left of the row
        device_status = None
        audit_config_status
        for key, value in device_keys.items():
            self.utils.print_info(f"Getting device row from devices table using {key} : {value}")
            device_row = self._get_row(key, value)
            device_row = copy.copy(device_row)

            # If we didn't find a row using the current key move on to the next key
            if device_row == -1:
                self.utils.print_info(f"Unable to get device row from devices table using {key} : {value}")
                continue

            # Attempt to get device status from the row we got from the devices table
            attempt_count = 1
            attempt_max   = 3
            while attempt_count <= attempt_max:
                self.utils.print_info(f"Trying to get device status from table cell. Attempt {attempt_count} of {attempt_max} attempts")
                try:
                    device_status = self.devices_web_elements.get_status_cell(device_row)
                except Exception as err:
                    self.utils.print_info(f"Getting status from cell failed with Exception: '{err}'")

                # If we got a status then break out of the attempt loop
                if device_status:
                    self.utils.print_info(f"Got device status during attempt {attempt_count} of {attempt_max} attempts")
                    break

                # If we get here then we were unable to get a status
                self.utils.print_info(f"Getting status from cell failed during attempt {attempt_count} of {attempt_max} attempts.  status = '{device_status}'")
                self.screen.save_screen_shot()
                attempt_count += 1

            # The config audit icon is the icon right next to the status icon
            self.utils.print_info("Getting audit_config_status")
            audit_config_status = self.devices_web_elements.get_device_config_audit(device_row)
            self.screen.save_screen_shot()
            sleep(2)

            if device_status:
                self.utils.print_info(f"Device status is: {device_status}")
                self.utils.print_info(f"Audit config status is: {audit_config_status}")
                break

        if device_status:
            if "hive-status-true" in device_status:
                if audit_config_status:
                    if "ui-icon-sprite-match" in audit_config_status:
                        kwargs['pass_msg'] = "Device Status: Connected, audit status matched"
                        self.common_validation.passed(**kwargs)
                        return 'green'
                    if "ui-icon-sprite-mismatch" in audit_config_status:
                        kwargs['pass_msg'] = "Device Status: Connected, configuration audit status mismatched"
                        self.common_validation.passed(**kwargs)
                        return "config audit mismatch"
                else:
                    kwargs['pass_msg'] = "Unable to obtain audit config status for the row - returning connection " \
                                         "status 'green'"
                    self.common_validation.passed(**kwargs)
                    return 'green'

            if "local-managed-icon" in device_status:
                kwargs['pass_msg'] = "Device Status: Connected, locally managed"
                self.common_validation.passed(**kwargs)
                return 'green'

            if "hive-status-false" in device_status:
                if self.devices_web_elements.get_device_conn_status_after_ten_min(device_row):
                    kwargs['pass_msg'] = "Device has not yet established connection after 10 minutes"
                    self.common_validation.passed(**kwargs)
                    return "disconnected"
                kwargs['pass_msg'] = "Device is disconnected!"
                self.common_validation.passed(**kwargs)
                return "disconnected"

            if "local-icon" in device_status:
                kwargs['pass_msg'] = "Device Status: Disconnected, locally managed"
                self.common_validation.passed(**kwargs)
                return 'disconnected'

            if "device-status-unknown" in device_status:
                kwargs['pass_msg'] = "Device Status: Unknown"
                self.common_validation.passed(**kwargs)
                return 'unknown'
        else:
            kwargs['fail_msg'] = "Unable to obtain device status for the device row!"
            self.common_validation.fault(**kwargs)
            return "Unknown"

        kwargs['fail_msg'] = "Unable to obtain device status!"
        self.common_validation.fault(**kwargs)
        return "Unknown"

    def verify_device_status(self, device_serial=None, device_name=None, device_mac=None,
                             status=None):
        """
        - This keyword returns 1 if device status expected matches the status passed as argument
        - Keyword Usage:
        - ``Verify Device Status   device_serial=${DEVICE_SERIAL}    status=green``
        - ``Verify Device Status   device_name=${DEVICE_NAME}    status=green``
        - ``Verify Device Status   device_mac=${DEVICE_MAC}    status=green``

        :param device_serial: device Serial, by default set to None
        :param device_name: device Name, by default set to None
        :param device_mac: device MAC, by default set to None
        :param status: green, red, or amber as of now - may change in future, by default set to None

        :return:
        """
        if device_serial:
            if status in self.get_device_status(device_serial):
                return 1
        if device_name:
            if status in self.get_device_status(device_name):
                return 1
        if device_mac:
            if status and status in self.get_device_status(device_mac):
                return 1

    def get_device_row(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        - This keyword returns the row of matched device

        :param device_serial: device Serial, by default set to None
        :param device_name: device Name, by default set to None
        :param device_mac: device MAC, by default set to None

        :return: returns the row object or -1 if unable to find row
        """
        device_keys = {}
        if device_mac:
            device_keys['device_mac'] = device_mac
        if device_serial:
            device_keys['device_serial'] = device_serial
        if device_name:
            device_keys['device_name'] = device_name
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "Invalid args. You must pass in at least one of the following: device_serial, " \
                                 "device_name, or device_mac!"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info('Getting device row...')
        row = self._find_device_row(device_keys)
        if row:
            kwargs['pass_msg'] = f"Found device row using {device_keys}"
            self.common_validation.passed(**kwargs)
            return row

        kwargs['fail_msg'] = f"Didn't find the device with {device_keys} in the grid"
        self.common_validation.failed(**kwargs)
        return -1

    def get_device_model_serial_numbers(self, device_model, device_type):
        rows = self.devices_web_elements.get_grid_rows()
        list_serial = []
        if rows:
            for row in rows:
                if device_model in row.text:
                    formated_row = self.format_row(row.text)
                    if "digital twin" in device_type.lower():
                        if "New" in formated_row:
                            list_serial.append(formated_row[10])
                        elif "Managed" or "setting up..." in formated_row:
                            list_serial.append(formated_row[11])
                    elif "simulated" in device_type.lower():
                        if "Managed" in formated_row:
                            list_serial.append(formated_row[8])
                        else:
                            list_serial.append(formated_row[7])
        return list_serial

    def format_row(self, row):
        cell_values = row.split("\n")
        formatted_row = list()
        for cell_value in cell_values:
            formatted_row.append(cell_value)
        return formatted_row

    def update_network_policy_to_router(self, policy_name=None, router_serial=None, update_method="Delta", **kwargs):
        """
        - Go To MANAGE-->Devices-->Select Device row  to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - select AP-->Update device
        - By default Delta config push will happen
        - Keyword Usage:
        - ``Update Network Policy To Router   policy_name=${POLICY_NAME}``
        - ``Update Network Policy To Router   router_serial=${ROUTER_SERIAL}``

        :param policy_name: name of the network to deploy, by default set to None
        :param router_serial: serial number of the ap to select, by default set to None
        :param update_method: Perform Complete update or delta update, by default set to 'Delta'
        :return: 1 if policy updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select Router row")
        if not self.select_device(router_serial, skip_navigation=True):
            kwargs['fail_msg'] = f"Router {router_serial} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        self.utils.print_info("Click on actions button")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)
        sleep(2)

        self.utils.print_info("Click on Assign Network policy action")
        self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_router_combo)
        sleep(2)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_drop_down_router)
        self.auto_actions.scroll_down()
        sleep(2)

        self.auto_actions.click_reference(self.devices_web_elements.get_nw_policy_drop)
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
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_cancel_button)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy assign button")
        self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_button)
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_close_button)
                sleep(5)
                kwargs['fail_msg'] = "Your account does not have permission to perform that action"
                self.common_validation.fault(**kwargs)
                return -2

        self.utils.print_info("Select Device row")
        self.select_device(router_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

        count = 0
        if update_method == "Delta":
            self.auto_actions.click_reference(self.devices_web_elements.get_delta_config_update_button)
            sleep(2)
            self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
            count = 5
            tool_tp_text_error = self.devices_web_elements.get_ui_banner_error_message()
            self.screen.save_screen_shot()
            tool_tp_text = tool_tip.tool_tip_text
            if tool_tp_text_error:
                if "a configuration related action is currently in progress for device" in tool_tp_text_error.text.lower():
                    self.utils.print_info(tool_tp_text_error.text)
                    kwargs['fail_msg'] = "A configuration related action is currently in progress for device"
                    self.common_validation.fault(**kwargs)
                    return -1
            if tool_tp_text:
                for value in tool_tp_text:
                    if "a device mode change is not supported with a delta configuration update" in value.lower():
                        self.utils.print_info(value)
                        update_method = "Complete"

        if update_method == "Complete":
            self.auto_actions.click_reference(self.devices_web_elements.get_full_config_update_button)
            sleep(2)
            self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
            tool_tp_text_error = self.devices_web_elements.get_ui_banner_error_message()
            self.screen.save_screen_shot()
            tool_tp_text = tool_tip.tool_tip_text
            if tool_tp_text_error:
                if "a configuration related action is currently in progress for device" in tool_tp_text_error.text.lower():
                    self.utils.print_info(tool_tp_text_error.text)
                    kwargs['fail_msg'] = "A configuration related action is currently in progress for device"
                    self.common_validation.fault(**kwargs)
                    return -1
            count = 10

        self.screen.save_screen_shot()
        sleep(2)
        while count > 0:
            policy_applied = self.get_router_network_policy(router_serial=router_serial)
            if policy_name.upper() == policy_applied.upper():
                kwargs['pass_msg'] = f"Applied network policy {policy_applied}"
                self.common_validation.passed(**kwargs)
                return 1
            count -= 1

        kwargs['fail_msg'] = "Failed to update network policy to router"
        self.common_validation.failed(**kwargs)
        return -1

    def get_router_network_policy(self, router_serial=None, router_name=None, router_mac=None):
        """
        - Get router network policy applied to the router
        - Keyword Usage:
        - ``Get Router Network Policy  router_serial=${ROUTER_SERIAL}``
        - ``Get ROuter Network Policy  router_name=${ROUTER_NAME}``
        - ``Get ROuter Network Policy  router_mac=${ROUTER_MAC}``

        :param router_serial: router serial number, by default set to None
        :param router_name: router host name, by default set to None
        :param router_mac: router mac address, by default set to None
        :return: nw policy applied to the router
        """

        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [router_serial, router_mac, router_name] if value][0]
        nw_policy = self.get_device_details(search_string, 'POLICY')
        if nw_policy:
            return nw_policy

    def get_device_updated_status(self, device_serial=None, device_name=None, device_mac=None):
        """
        - This keyword returns the device updated status by searching device row using serial, name or mac address
        - Assumes that already navigated to the manage-->device page
        - Keyword Usage:
        - ``Get Device Updated Status   device_serial=${DEVICE_SERIAL}``
        - ``Get Device Updated Status   device_name=${DEVICE_NAME}``
        - ``Get Device Updated Status   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial, by default set to None
        :param device_name: device Name, by default set to None
        :param device_mac: device MAC, by default set to None
        :return: 'updated Time' if the device is updated correctly else return updating status message
        """
        device_row = -1

        self.navigator.enable_page_size()
        self.utils.print_info("Enable the Updated On column")
        self.column_picker_select("Updated On")

        self.utils.print_info("Refresh the devices page")
        self.utils.wait_till(self.refresh_devices_page)
        self.utils.print_info('Getting device Updated Status using ', *[x for x in {device_serial, device_name, device_mac} if x is not None])

        device_row = self.get_device_row(device_serial=device_serial, device_mac=device_mac, device_name=device_name)

        # get a snap shot of the object at this instant, so values can't change or become undefined.
        device_row = copy.copy(device_row)

        if device_row != -1:
            device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
            self.utils.print_info("Device Updated Status is :", device_updated_status)
            if "Querying" in device_updated_status:
                self.utils.print_info("Device Updating Status: Querying")
                return 'Querying'

            if "IQ Engine Firmware Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: IQ Engine Firmware Updating")
                return 'IQ Engine Firmware Updating'

            if "Firmware Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: IQ Engine Firmware Updating")
                return 'Firmware Updating'

            if "User Configuration Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: User Configuration Updating")
                return 'User Configuration Updating'

            if "Configuration Updating" in device_updated_status:
                self.utils.print_info("Device Updating Status: User Configuration Updating")
                return 'Configuration Updating'

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

    def column_picker_select(self, *columns, **kwargs):
        """
        - This keyword checks the device column picker if it is not checked
        - Keyword Usage:
        - ``Column Picker Select        Zone   Branch ID   Host Name   Network Policy``
        - ``Column Picker Select        Stack Unit``

        :param columns: list of device columns that can be checked
        :return: returns 1 if successful
        """
        ret_val = 1
        selected_columns = []
        unselected_columns = []

        # To extract the list of columns if 'columns' arg vaule is ist or tuple
        if isinstance(columns, tuple) and (isinstance(columns[0], list) or isinstance(columns[0], tuple)):
            columns = columns[0]

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        self.screen.save_screen_shot()
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
                            self.screen.save_screen_shot()
                            selected_columns.append(filter_)
                        else:
                            self.auto_actions.click(filter_row)
                            self.screen.save_screen_shot()
                            self.utils.print_info(f"Column Picker Filter {filter_} is not already checked - checking")
                            selected_columns.append(filter_)
            else:
                self.utils.print_info("Unable to select the Column Picker Filter ", filter_)
                unselected_columns.append(filter_)
                ret_val = -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        self.screen.save_screen_shot()
        sleep(2)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Column Picker Filter is not selected: {unselected_columns}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Column Picker Filter is selected: {selected_columns}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def column_picker_unselect(self, *columns, **kwargs):
        """
        - This keyword unchecks the device column picker if it is checked
        - Keyword Usage:
        - ``Column Picker Unselect      Branch ID  Host Name   Cloud Config Groups``
        - ``Column Picker Unselect       Network Policy``

        :param columns: list of device columns that can be unchecked
        :return: returns 1 if successful
        """
        ret_val = 1
        selected_columns = []
        unselected_columns = []

        # To extract the list of columns if 'columns' arg vaule is ist or tuple
        if isinstance(columns, tuple) and (isinstance(columns[0], list) or isinstance(columns[0], tuple)):
            columns = columns[0]

        self.utils.print_info("Clicking on Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
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
                                                  "- unchecking")
                            unselected_columns.append(filter_)
                        else:
                            self.utils.print_info(f"Column Picker Filter {filter_} is already unchecked")
                            unselected_columns.append(filter_)
            else:
                self.utils.print_info("Unable to unselect the Column Picker Filter ", filter_)
                selected_columns.append(filter_)
                ret_val = -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Column Picker Filter is selected: {selected_columns}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Column Picker Filter is not selected: {unselected_columns}"
            self.common_validation.passed(**kwargs)
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

    def delete_all_devices(self, **kwargs):
        """
        - This Keyword will Delete All the Devices in the Manage--> Devices Grid
        - Keyword Usage:
        - ``Delete All devices``

        :return: 1 if Devices Deleted Successfully else -1
        """

        self.navigator.enable_page_size()
        check_page = self.devices_web_elements.get_delete_button()
        if check_page:
            if check_page.is_displayed():
                self.utils.print_info("this is the device page ")
                self.screen.save_screen_shot()
            else:
                kwargs['fail_msg'] = "The page is not device page"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "The page is not device page"
            self.common_validation.fault(**kwargs)
            return -1

        if self.get_device_count() == 0:
            kwargs['pass_msg'] = "No devices present in the Devices grid"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            try:
                self.utils.print_info("Waiting for page to refresh...")
                sleep(20)

                # grid = self.devices_web_elements.get_grid()

                self.utils.print_info("Selecting Device grid checkbox...")
                # self.auto_actions.click(self.devices_web_elements.get_ap_select_checkbox(grid))
                self.auto_actions.click_reference(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox)
                sleep(5)

                self.utils.print_info("Clicking Delete button")
                self.auto_actions.click_reference(self.devices_web_elements.get_delete_button)
                sleep(5)

                self.utils.print_info("Confirming delete...")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_delete_confirm_ok_button)
                sleep(2)
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = "ALl devices were deleted successfully"
                self.common_validation.passed(**kwargs)
                return 1

            except Exception as e:
                kwargs['fail_msg'] = f"Unable to delete devices {e}"
                self.common_validation.fault(**kwargs)
                return -1

    def update_network_policy_to_all_devices(self, policy_name=None, update_method="Delta", **kwargs):
        """
        - By default this keyword do delta config push
        - Flow: MANAGE-->Devices-->Select All Devices to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - Select All Devices--> Update device
        - Keyword Usage:
        - ``Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}``
        - ``Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}  update_method=Complete``

        :param policy_name: name of the network to deploy, by default set to None
        :param update_method: Perform Complete update or delta update, by default set to 'Delta'
        :return: 1 if policy is updated else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info("Select All Devices Checkbox")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox)

        if not self._assign_network_policy(policy_name):
            kwargs['fail_msg'] = f"Can not assign network policy {policy_name}"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Select All Devices Checkbox")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox)
        sleep(2)

        self._update_network_policy(update_method)
        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Deployed devices successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Deployed devices successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Update policy to all devices failed"
            self.common_validation.failed(**kwargs)
            return -1

    def get_ap_wifi0_power(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi0 power applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
        - ``Get Ap WIFI0 Power   ap_serial=${AP_SERIAL}``
        - ``Get Ap WIFI0 Power   ap_name=${AP_NAME}``
        - ``Get Ap WIFI0 Power   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Transmission power value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Transmission power value of wifi1 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Channel value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Channel value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        wifi1_channel = self.get_device_details(search_string, 'WIFI1 CHANNEL')
        if wifi1_channel:
            return wifi1_channel

    def update_override_configuration_to_multiple_devices(self, device_serials='', update_method="Delta", **kwargs):
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
            kwargs['fail_msg'] = "Pass the device serial numbers with comma separated"
            self.common_validation.fault(**kwargs)
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
        kwargs['pass_msg'] = "Devices Updated successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def update_override_configuration_to_device(self, device_serial='', update_method="Delta", **kwargs):
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
        if not self.select_device(device_serial, skip_navigation=True):
            kwargs['fail_msg'] = f"AP {device_serial} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        self._update_network_policy(update_method)
        tool_tip_text = tool_tip.tool_tip_text

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Deployed devices successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Deployed devices successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to update config to device"
            self.common_validation.failed(**kwargs)
            return -1

    def get_device_count(self):
        """
        - Gets the device count from the Devices grid
        - Keyword Usage:
        - ``Get Device Count``

        :return: returns the number of devices in the table
        """
        device_count = 0
        self.navigator.enable_page_size()
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
                self.utils.print_info("sorted device column values are ascending")
                return gui_sorted_values
            else:
                self.utils.print_info("sorted device grid column values are not ascending")
                return -1

        if sorting.upper() == "DESCENDING":
            gui_unsorted_values.sort(reverse=True)
            sorted_values = gui_unsorted_values

            self.utils.print_info(f"Sorted device grid values from logic:{sorted_values}")
            self.utils.print_info(f"GUI sorted device grid descending values:{gui_sorted_values}")
            if sorted_values == gui_sorted_values:
                self.utils.print_info("sorted device column values are descending")
                return gui_sorted_values
            else:
                self.utils.print_info("sorted device grid column values not are descending")
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
        - Here "logic sorted values" means taking the unsorted device grid values and applying the sort method over those values
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

    def _onboard_wing_ap(self, device_serial, device_mac, device_make, location=False):
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

        if self.search_device(device_serial=device_serial, skip_navigation=True, ignore_failure=True) == 1:
            self.utils.print_info(f"Device with {device_serial} serial number already onboarded")
            return 1

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)

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
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_drop_down)
            sleep(2)

            self.utils.print_info("Selecting Device Make: ", device_make)
            self.auto_actions.select_drop_down_options(self.devices_web_elements.get_device_make_drop_down_options(),
                                                       device_make)

            self.auto_actions.send_keys(self.devices_web_elements.get_wing_devices_mac_text_area(), device_mac)

            _errors = self.check_negative_combinations()
            if _errors != 1:
                return _errors

        if location:
            self.auto_actions.click_reference(self.devices_web_elements.get_location_button)
            self._select_location(location)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_button)

        _errors = self.check_negative_combinations()
        if _errors != 1:
            return _errors

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                return -1
            if "A stake record of the device was found in the redirector." in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                return -2
        else:
            self.utils.print_info("No Errors while onboarding")

        serials = device_serial.split(",")
        self.utils.print_info("Device Serials Numbers: ", serials)

        for serial in serials:
            if self.search_device(device_serial=serial, ignore_failure=True) == 1:
                self.utils.print_info("Successfully Onboarded Device(s): ", serials)
                return 1
            else:
                return -1

    def get_device_connected_status(self, device_serial, **kwargs):
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
            device_row = self.get_device_row(device_serial=device_serial)
            if "hive-status-true" in self.devices_web_elements.get_status_cell(device_row):
                kwargs['pass_msg'] = "Device status is connected"
                self.common_validation.passed(**kwargs)
                return 1
            elif "local-managed-icon" in self.devices_web_elements.get_status_cell(device_row):
                kwargs['pass_msg'] = "Device status is connected - locally managed"
                self.common_validation.passed(**kwargs)
                return 1
            elif retry_time >= int(device_connect_wait):
                kwargs['fail_msg'] = f"Device status is disconnected after wait of {device_connect_wait}"
                self.common_validation.failed(**kwargs)
                return -1
            sleep(30)
            retry_time += 30

    def get_device_column_information(self, device_serial, column_array, **kwargs):
        """
        - This keyword is used to get the column data for the device
        - Keyword Usage:
        - ``@{column_list}=    Create List    MGT IP ADDRESS    MAC``
        - ``get_device_column_information   ${DEVICE_SERIAL}  ${column_array}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device serial number to check the device connected status
        :param column_array: The device array of columns to get data for
        :return: object map of data columns to data, spaces are replaced with _
        """
        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_get_device_column_information(device_serial, column_array)

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        return_array_data = {}
        self.refresh_devices_page()

        # Commented on 1/18/23 because variable is unused
        # device_row = self.get_device_row(device_serial)
        self.get_device_row(device_serial=device_serial)
        for column in column_array:
            data = self.get_device_details(device_serial, column)
            return_array_data[column.replace(' ', "_")] = data
        return return_array_data

    def get_device_configuration_audit_status(self, device_serial=None, device_name=None,
                                              device_mac=None, **kwargs):
        """
        - This keyword is used to get the device configuration audit status
        - Flow:
        - Navigate to Manage --> Devices  --> Get the configuration audit status under status column of the device row
        - Keyword Usage:
        - ``Get Device Configuration Audit Status    ${DEVICE_SERIAL}``

        :param device_serial: device serial number to check the device configuration audit status, by default set to None
        :param device_name: device Name, by default set to None
        :param device_mac: device MAC, by default set to None
        :return:
        - audit match : if configuration audit matched
        - audit mismatch : if configuration audit mismatch
        - -1 if device not found in the device grid

        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        device_row = self.get_device_row(device_serial=device_serial, device_name=device_name, device_mac=device_mac)

        if device_row:
            audit_config_status = self.devices_web_elements.get_device_config_audit(device_row)
            if "ui-icon-sprite-match" in audit_config_status:
                self.utils.print_info("device configuration audit matched")
                return 'audit match'

            if "ui-icon-sprite-mismatch" in audit_config_status:
                self.utils.print_info("device configuration audit mismatched")
                return "audit mismatch"

        kwargs['fail_msg'] = "Device not found in the device grid rows"
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_device_online(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=20,
                                 **kwargs):
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
        - ``Wait Until Device Online       device_serial=${DEVICE_SERIAL}   ``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device serial number to check the device connected status, by default set to None
        :param device_mac: device mac to check the device connected status, by default set to None
        :param retry_duration: duration between each retry, by default set to 30
        :param retry_count: retry count, by default set to 20
        :param kwargs: keyword arguments XAPI_ENABLE
        :return: 1 if device connected within time else -1
        """

        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_wait_until_device_online(device_serial=device_serial, device_mac=device_mac, retry_duration=retry_duration, retry_count=retry_count, **kwargs)

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        count = 1
        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Device Online Status Check - Loop: {count}")
                    self.utils.print_info(f"Time elapsed for device connection {retry_duration} seconds")
                    self.refresh_devices_page()

                    device_row = self.get_device_row(device_serial=device_serial, device_mac=device_mac)

                    if device_row and device_row != -1:
                        status = self.devices_web_elements.get_status_cell(device_row)
                        self.utils.print_info(f"Found Device status: {status}")
                        if status is not None:
                            if "hive-status-true" in status:
                                kwargs['pass_msg'] = "Device status is connected!"
                                self.common_validation.passed(**kwargs)
                                return 1
                            elif "local-managed-icon" in status:
                                kwargs['pass_msg'] = "Device status is connected - locally managed"
                                self.common_validation.passed(**kwargs)
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

        kwargs['fail_msg'] = "Device failed to come ONLINE. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_device_offline(self, device_serial=None, device_mac=None, retry_duration=30, retry_count=10,
                                  **kwargs):

        """
        - This keyword waits until the device status in XIQ is "Disconnected" or "Unknown".
        - After Configuring the CAPWAP client server in device cli, check the device connected status
        - This keyword by default loop over every 30 seconds for 10 times to check the device connected status
        - Flow:
        - Navigate to Manage --> Devices
        - check the device status for a device based on passed device serial
        - Keyword Usage:
        - ``Wait Until Device Offline       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12``
        - ``Wait Until Device Offline       ${DEVICE_MAC}           retry_duration=15       retry_count=5``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device serial number to check the device connected status, by default set to None
        :param device_mac: device mac to check the device connected status, by default set to None
        :param retry_duration: duration between each retry, by default set to 30
        :param retry_count: retry count, by default set to 10
        :return: 1 if device disconnected within time, else -1
        """

        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_wait_until_device_offline(device_serial=device_serial, device_mac=device_mac, retry_duration=retry_duration, retry_count=retry_count, **kwargs)

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        count = 1

        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Device Offline Status Check - Loop: {count}")
                    self.utils.print_info(f"Time elapsed for device connection {retry_duration} seconds")
                    self.refresh_devices_page()
                    self.screen.save_screen_shot()

                    device_row = self.get_device_row(device_serial=device_serial, device_mac=device_mac)

                    if device_row and device_row != -1:
                        device_status = self.devices_web_elements.get_status_cell(device_row)
                        if "hive-status-false" in device_status:
                            kwargs['pass_msg'] = "Device status is disconnected"
                            self.common_validation.passed(**kwargs)
                            return 1
                        elif "local-icon" in device_status:
                            kwargs['pass_msg'] = "Device status is disconnected (locally managed)"
                            self.common_validation.passed(**kwargs)
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

        kwargs['fail_msg'] = "Device failed to go OFFLINE. Please check."
        self.common_validation.failed(**kwargs)
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
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

        if update_method == "Delta":
            self.utils.print_info("Using Delta method...")
            self.auto_actions.click_reference(self.devices_web_elements.get_delta_config_update_button)
            sleep(2)
            self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
            sleep(5)
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for value in tool_tp_text:
                if "a device mode change is not supported with a delta configuration update" in value.lower():
                    self.utils.print_info(value)
                    update_method = "Complete"
                    self.utils.print_info("There was an issue with Delta method...")

        if update_method == "Complete":
            self.utils.print_info("Using Complete method...")
            self.auto_actions.click_reference(self.devices_web_elements.get_full_config_update_button)
            sleep(2)
            self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)

        self.screen.save_screen_shot()
        return 1

    def wait_until_device_reboots(self, device_serial, retry_duration=30, retry_count=10, **kwargs):
        """
        - This Keyword will wait until device reboots based on device update status message
        - Keyword Usage:
        - `` Wait Until Device Reboots  ${DEVICE_SERIAL}``

        :param device_serial: Device Serial Number
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        If the reboot message has a date value, the assumption the device hase finished rebooting
        :return: 1 if Device wait till reboots else -1
        """

        count = 0
        self.utils.print_info("Checking to see if the device has completed the reboot action")
        date_regex = r"(\d{4})-((0[1-9])|(1[0-2]))-(0[1-9]|[12][0-9]|3[01]) ([0-2]*[0-9]\:[0-6][0-9]\:[0-6][0-9])"
        while count < retry_count:
            reboot_message = self.get_device_details(device_serial, "UPDATED")
            if "Rebooting" in reboot_message:
                self.utils.print_info(f"Device is rebooting. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            elif re.match(date_regex, reboot_message):
                kwargs['pass_msg'] = f"Device has finished rebooting at {reboot_message}"
                self.common_validation.passed(**kwargs)
                return 1
            count += 1
        kwargs['fail_msg'] = "Device didn't finish the reboot"
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_country_discovered(self, device_serial, retry_duration=30, retry_count=10, **kwargs):
        """
        - This Keyword will wait until device finishes Discovering Country Code based on device update status message
        - Keyword Usage:
        - `` Wait Until Country Discovered  ${DEVICE_SERIAL}``

        :param device_serial: Device Serial Number
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        If the message has a date value, the assumption the device hase finished rebooting
        :return: 1 if Device wait till reboots else -1
        """

        count = 0
        self.utils.print_info("Checking to see if the device has completed Discovering Country Code")
        date_regex = r"(\d{4})-((0[1-9])|(1[0-2]))-(0[1-9]|[12][0-9]|3[01]) ([0-2]*[0-9]\:[0-6][0-9]\:[0-6][0-9])"
        while count < retry_count:
            reboot_message = self.get_device_details(device_serial, "UPDATED")
            if "Discovering" in reboot_message:
                self.utils.print_info(f"Device is discovering country code. Waiting for {retry_duration} seconds...")
                self.utils.print_info(f"Message: {reboot_message} :...")
                sleep(retry_duration)
            elif "Failed" in reboot_message:
                kwargs['pass_msg'] = f"Operation Failed {reboot_message}"
                self.common_validation.passed(**kwargs)
                return 1
            elif "Timeout" in reboot_message:
                kwargs['pass_msg'] = f"Operation Timeout {reboot_message}"
                self.common_validation.passed(**kwargs)
                return 1
            elif re.match(date_regex, reboot_message):
                kwargs['pass_msg'] = f"Device has finished discovering country code at {reboot_message}"
                self.common_validation.passed(**kwargs)
                return 1
            count += 1

        kwargs['fail_msg'] = f"Loop Count: {count}. Retry Count: {retry_count}"
        self.common_validation.failed(**kwargs)
        return -1

    def assign_network_policy_to_switch(self, policy_name, serial, update_device=True, **kwargs):
        """
        - This keyword does a config push for a switch
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Actions-->Assign Network Policy -->Select the network policy to assign
        - Select Switch-->Update device
        - Keyword Usage:
        - ``Assign Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}``

        :param policy_name: name of the network policy to deploy
        :param serial: serial number of the switch to select
        :param update_device: True - if the policy to be pushed to the device ; False - if not
        :return: 1 if policy is assigned, else -1
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info(f"Select switch row with serial {serial}")
        if not self.select_device(serial, skip_navigation=True):
            kwargs['fail_msg'] = f"Switch {serial} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        if not self._assign_policy_to_switch(policy_name):
            kwargs['fail_msg'] = "Failed to assign network policy to switch"
            self.common_validation.failed(**kwargs)
            return -1

        if update_device:
            policy_applied = self.get_ap_network_policy(ap_serial=serial)
            if policy_name.upper() == policy_applied.upper():
                kwargs['pass_msg'] = f"Applied network policy {policy_applied}"
                self.common_validation.passed(**kwargs)
                return 1

            kwargs['fail_msg'] = f"Policy applied:{policy_name} is not matching with policy updated:{policy_applied}"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def update_network_policy_to_switch(self, policy_name=None, serial=None, update_method="PolicyAndConfig", **kwargs):
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

        :param policy_name: name of the network policy to deploy, by default set to None
        :param serial: serial number of the switch to select, by default set to None
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
        if not self.select_device(serial, skip_navigation=True):
            kwargs['fail_msg'] = f"Switch {serial} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        if not self._assign_policy_to_switch(policy_name):
            kwargs['fail_msg'] = "Failed to update network policy to switch"
            self.common_validation.failed(**kwargs)
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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Location applied to the AP
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

    def update_switch_policy_and_configuration(self, device_serial=None, device_name=None, device_mac=None):
        """
        - This keyword does a config push for a switch, selecting just the "Update Network Policy and Configuration" check button in the Device Update dialog.
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Select Switch-->Update device
        - Keyword Usage:
        - ``Update Switch Policy and Configuration  ${SWITCH_SERIAL}``

        :param device_serial: serial number of the switch to update, by default set to None
        :param device_name: device Name, by default set to None
        :param device_mac: device MAC, by default set to None
        :return: 1
        """
        self.utils.print_info("Select Switch row")
        self.select_device(device_serial=device_serial, device_name=device_name, device_mac=device_mac)

        self._update_switch(update_method="PolicyAndConfig")

        self.screen.save_screen_shot()

        return self._check_device_update_status(device_serial=device_serial, device_name=device_name,
                                                device_mac=device_mac)

    def update_switch_iq_engine_and_images(self, serial):
        """
        - This keyword does a config push for a switch, selecting just the "Upgrade IQ Engine and Extreme Network Switch Images" check button in the Device Update dialog.
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

    def update_switch_complete(self, serial, **kwargs):
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
        if not self.select_device(serial):
            kwargs['fail_msg'] = "Failed to select the device"
            self.common_validation.fault(**kwargs)
            return -1

        if not self._update_switch(update_method="Complete") == 1:
            kwargs['fail_msg'] = "Update device failed"
            self.common_validation.failed(**kwargs)
            return -1

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
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)
        sleep(3)

        self.utils.print_info("Click on Assign Network policy action for selected switch")
        self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_combo_switch)
        sleep(4)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_drop_down)
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
        self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_button)
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_close_button)
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

        update_button = self.devices_web_elements.get_update_device_button()
        if update_button:
            self.utils.print_info("Click on device update button")
            self.auto_actions.click(update_button)
        else:
            self.utils.print_info("update button not found")
            return -1

        sleep(2)

        pol_config_cb = self.devices_web_elements.get_switch_update_policy_and_config_check_button()
        engine_img_cb = self.devices_web_elements.get_switch_upgrade_engine_and_images_check_button()

        if pol_config_cb is None:
            self.utils.print_info("ERROR: Unable to obtain 'Update Network Policy and Configuration' check button")
            self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
            return -1
        if engine_img_cb is None:
            self.utils.print_info(
                "ERROR: Unable to obtain 'Upgrade IQ Engine and Extreme Network Switch Images' check button")
            self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
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
        #     self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
        #     return -1
        #
        # elif update_method == "Complete":
        #     self.utils.print_info("Enable both check buttons")
        #     self.auto_actions.enable_check_box(pol_config_cb)
        #     self.auto_actions.enable_check_box(engine_img_cb)
        #     sleep(2)
        #     self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
        #     return -1
        #
        # else:
        #     self.utils.print_info(f"Unknown update method {update_method}. Please specify 'PolicyAndConfig', 'EngineAndImages', or 'Complete'")
        #     self.auto_actions.click_reference(self.devices_web_elements.get_device_update_close_button)
        #     return -1

        # Perform the update
        perform_update_button = self.devices_web_elements.get_perform_update_button()
        if perform_update_button:
            self.utils.print_info("Click on perform update button")
            self.auto_actions.click(perform_update_button)
        else:
            self.utils.print_info("Not able to click on perform update button")
            return -1

        # In case the warning dialog is displayed about the reboot and revert option being selected, click Yes to close it
        self._handle_reboot_and_revert_warning()
        self._handle_credentials_global_popup()
        self.screen.save_screen_shot()
        sleep(2)
        return 1

    def _handle_credentials_global_popup(self):
        ret_val = 1

        self.utils.print_info("Check to see if the account credential managed by global setting pop-up is displayed")
        sleep(5)

        the_dlg = self.devices_web_elements.get_global_settings_management_dialog()

        if the_dlg:
            self.utils.print_debug("The account credential managed by global setting pop-up is displayed")
            yes_btn = self.devices_web_elements.get_global_settings_management_dialog_yes_button()
            if yes_btn:
                self.utils.print_info("Clicking 'Yes' in the account credential managed by global setting pop-up dialog")
                self.auto_actions.click_reference(self.devices_web_elements.get_global_settings_management_dialog_yes_button)
            else:
                self.utils.print_info("Unable to find the Yes button in the account credential managed by global setting pop-up dialog")
                ret_val = -1
        else:
            self.utils.print_debug("The account credential managed by global setting pop-up is not displayed")

        return ret_val

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

    def _check_device_update_status(self, device_serial=None, device_name=None, device_mac=None):
        """
        - This keyword is used to check the status of the device update
        - It will poll the "update status" every 30 seconds
        - Assuming that config push will take a maximum of five minutes

        :param  device_serial_mac_or_name: device serial number, device mac or device name to check the config push status,
                                           by default set to None
        :return: 1 if config push success else -1
        """
        retry_count = 0
        while retry_count <= 300:
            device_update_status = self.get_device_updated_status(device_serial=device_serial, device_name=device_name,
                                                                  device_mac=device_mac)
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

    def revert_device_to_template(self, device_serial, **kwargs):
        """
        - Assumes already navigated to Manage --> Devices
        - This method accesses the "Revert Device to Template" action for a device matching the specified serial
        - Keyword Usage:
        - ``Revert Device to Template  ${DEVICE_SERIAL}``

        :param device_serial: serial number of the device to perform the action on
        :return: 1 if action succeeds, else -1
        """
        self.utils.print_info("Reverting Device to Template for device with serial: ", device_serial)

        if self.select_device(device_serial=device_serial):
            self.utils.print_info("Selecting 'Actions' button")
            actions_btn = self.device_actions.get_device_actions_button()
            if actions_btn:
                self.auto_actions.click(actions_btn)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Could not click 'Actions' button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Selecting 'Revert Device to Template' menu item")
            revert_menu = self.device_actions.get_device_actions_revert_device_to_template_menu_item()
            if revert_menu:
                self.auto_actions.click(revert_menu)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Could not click 'Revert Device to Template' menu item"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Clicking 'Save' button")
            save_btn = self.dialogue_web_elements.get_confirm_yes_button()
            if save_btn:
                self.auto_actions.click(save_btn)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Could not click 'Save' button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Clicking 'Deploy' button")
            deploy_btn = self.dialogue_web_elements.get_confirm_deploy_button()
            if deploy_btn:
                self.auto_actions.click(deploy_btn)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Could not click 'Deploy' button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Waiting for device update to complete")
            self._check_device_update_status(device_serial)

            return 1
        else:
            kwargs['fail_msg'] = f"Could not select device with serial {device_serial}"
            self.common_validation.fault(**kwargs)
            return -1

    def confirm_column_picker_contains_column(self, *columns, **kwargs):
        """
        - This keyword confirms the list of columns are all present in the column picker
        - Keyword Usage:
        - `Confirm Column Picker Contains Column  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be present in the column picker list
        :return: returns 1 if all columns are present in the column picker; else, -1
        """
        ret_val = 1
        present_filter = []
        not_present_filter = []

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)
        self.utils.print_info("Column list to check for presence: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                self.utils.print_info(f"Column Picker Filter '{filter_}' is present")
                present_filter.append(filter_)
            else:
                self.utils.print_info(f"Column Picker Filter '{filter_}' is not present")
                not_present_filter.append(filter_)
                ret_val = -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Column Picker Filter is not present: {not_present_filter}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Column Picker Filter is present: {present_filter}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_column_picker_does_not_contain_column(self, *columns, **kwargs):
        """
        - This keyword confirms the list of columns are NOT present in the column picker
        - Keyword Usage:
        - `Confirm Column Picker Does Not Contain Column  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should not be present in the column picker list
        :return: returns 1 if none of the columns are present in the column picker; else, -1
        """
        ret_val = 1
        present_filter = []
        not_present_filter = []

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)
        self.utils.print_info("Column list to check for no presence: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            if filter_row != "":
                self.utils.print_info(f"Column Picker Filter '{filter_}' is present")
                present_filter.append(filter_)
                ret_val = -1
            else:
                self.utils.print_info(f"Column Picker Filter '{filter_}' is not present")
                not_present_filter.append(filter_)

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Column Picker Filter is present: {present_filter}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Column Picker Filter is not present: {not_present_filter}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_column_picker_column_selected(self, *columns, **kwargs):
        """
        - This keyword confirms the list of columns are all selected in the column picker
        - Keyword Usage:
        - `Confirm Column Picker Column Selected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be selected
        :return: returns 1 if all columns are selected in the column picker; else, -1
        """
        ret_val = 1
        selected_columns = []
        unselected_columns = []

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)
        self.utils.print_info("Column list to check for selected items: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            try:
                row_inputs = self.devices_web_elements.get_column_picker_row_input()
                row_input_count = 0
                for row_inp in row_inputs:
                    row_input_count += 1
                    if row_input_count == row_num:
                        ans = row_inp.get_attribute("checked")
                        if ans == "true":
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is selected")
                            selected_columns.append(filter_)
                        else:
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is not selected")
                            unselected_columns.append(filter_)
                            ret_val = -1
            except Exception as e:
                kwargs['fail_msg'] = f"Unable to obtain status of the column {e} "
                self.common_validation.failed(**kwargs)
                return -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Column Picker Filter is not selected: {unselected_columns}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Column Picker Filter is selected: {selected_columns}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_column_picker_column_unselected(self, *columns, **kwargs):
        """
        - This keyword confirms the list of columns are all unselected in the column picker
        - Keyword Usage:
        - `Confirm Column Picker Column Unselected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be selected - passed in as multiple arguments
        :return: returns 1 if all columns are selected in the column picker; else, -1
        """
        ret_val = 1
        selected_columns = []
        unselected_columns = []

        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)
        self.utils.print_info("Column list to check for unselected items: ", columns)
        for filter_ in columns:
            filter_row, row_num = self._get_column_picker_filter_exact(filter_)
            try:
                row_inputs = self.devices_web_elements.get_column_picker_row_input()
                row_input_count = 0
                for row_inp in row_inputs:
                    row_input_count += 1
                    if row_input_count == row_num:
                        ans = row_inp.get_attribute("checked")
                        if ans == "true":
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is selected")
                            selected_columns.append(filter_)
                            ret_val = -1
                        else:
                            self.utils.print_info(f"Column Picker Filter '{filter_}' is not selected")
                            unselected_columns.append(filter_)
            except Exception as e:
                kwargs['fail_msg'] = f"Unable to obtain status of the column {e}"
                self.common_validation.failed(**kwargs)
                return -1

        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.close_last_refreshed_tooltip()
        self.auto_actions.click_reference(self.devices_web_elements.get_column_picker_icon)
        sleep(2)

        if ret_val != 1:
            kwargs['fail_msg'] = f"Column Picker Filter is selected: {selected_columns}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Column Picker Filter is not selected: {unselected_columns}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def select_table_view_type(self, view_type="Default View", **kwargs):
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

        if ret_val != 1:
            kwargs['fail_msg'] = "Could not find Devices Table View Type Selector"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Devices Table View Type Selector was found/selected"
            self.common_validation.passed(**kwargs)
        return ret_val

    def _assign_network_policy_to_switch(self, policy_name):
        """
        """
        self.utils.print_info("Click on actions button")
        self.auto_actions.click_reference(self.devices_web_elements.get_manage_device_actions_button)
        sleep(3)

        self.utils.print_info("Click on Assign Network policy action")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_switch_assign_policy)
        sleep(4)

        self.utils.print_info("Click on network policy drop down")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_switch_assign_policy_dropdown)
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
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_switch_assign_policy_assign_btn)
        sleep(10)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_close_button)
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
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
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
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_switch_update_btn)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

    def select_all_devices(self, **kwargs):
        """
        - This keyword selects all devices in the table by clicking the Select All check box column header
        - Keyword Usage:
        - `Select All Devices`

        :return: returns 1 if the Select All checkbox was clicked; else, -1
        """
        if self.get_device_count() == 0:
            kwargs['pass_msg'] = "No devices present in the Devices grid"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            try:
                sel_checked = self.devices_web_elements.get_manage_devices_select_all_devices_checkbox_selected()
                if sel_checked:
                    self.utils.print_info("Select All checkbox already selected")
                else:
                    self.utils.print_info("Clicking Select All checkbox")
                    self.auto_actions.click_reference(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox)
                return 1

            except Exception as e:
                kwargs['fail_msg'] = f"Unable to select all devices {e}"
                self.common_validation.failed(**kwargs)
                return -1

    def deselect_all_devices(self, **kwargs):
        """
        - This keyword deselects all devices in the table by clicking the Select All check box column header
        to deselect it if it is already selected, or clicking the Select All check button twice (once to select all,
        once to deselect all) if it is not already selected.
        - Keyword Usage:
        - `Deselect All Devices`
        :return: returns 1 if the action was successful; else, -1
        """
        if self.get_device_count() == 0:
            kwargs['pass_msg'] = "No devices present in the Devices grid"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            try:
                sel_unchecked = self.devices_web_elements.get_manage_devices_select_all_devices_checkbox_deselected()
                if sel_unchecked:
                    self.utils.print_info("Select All checkbox not already selected - clicking to select all first")
                    self.auto_actions.click_reference(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox)
                self.utils.print_info("Clicking to deselect all devices")
                self.auto_actions.click_reference(self.devices_web_elements.get_manage_devices_select_all_devices_checkbox)
                return 1

            except Exception as e:
                kwargs['fail_msg'] = f"Unable to select all devices {e}"
                self.common_validation.failed(**kwargs)
                return -1

    def confirm_devices_selected(self, *device_list, **kwargs):
        """
        - This keyword confirms the list of devices are all selected in the table
        - Keyword Usage:
        - `Confirm Devices Selected  ${SERIAL_1}  ${SERIAL_2}  ${SERIAL_3}`

        :param device_list: list of device serial numbers to check the selection state of
        :return: returns 1 if all specified devices are selected; else, -1
        """
        ret_val = 1
        selected_device = []
        unselected_device = []
        unknown_state = []

        self.utils.print_info("Device list to check for selection: ", device_list)
        for device_ in device_list:
            device_row = self.get_manage_device_row(device_, ignore_failure=True)
            if device_row:
                if self.devices_web_elements.get_device_row_selection_checkbox_selected(device_row):
                    self.utils.print_info(f"DEVICE {device_} IS SELECTED")
                    selected_device.append(device_)
                else:
                    self.utils.print_info(f"DEVICE {device_} IS NOT SELECTED")
                    unselected_device.append(device_)
                    ret_val = -1
            else:
                self.utils.print_info(f"Unable to obtain selection state for device {device_}")
                unknown_state.append(device_)
                ret_val = -1

        if ret_val != 1:
            if unknown_state != '':
                kwargs['fail_msg'] = f"Device state is unknown: {unknown_state}"
                self.common_validation.failed(**kwargs)
            elif unselected_device != '':
                kwargs['fail_msg'] = f"Device is not selected: {unselected_device}"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Device is selected: {selected_device}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_devices_deselected(self, *device_list, **kwargs):
        """
        - This keyword confirms the list of devices are all deselected in the table
        - Keyword Usage:
        - `Confirm Devices Deselected  ${SERIAL_1}  ${SERIAL_2}  ${SERIAL_3}`

        :param device_list: list of device serial numbers to check the selection state of
        :return: returns 1 if all specified devices are deselected; else, -1
        """
        ret_val = 1
        selected_device = []
        unselected_device = []
        unknown_state = []

        self.utils.print_info("Device list to check for deselection: ", device_list)
        for device_ in device_list:
            device_row = self.get_manage_device_row(device_, ignore_failure=True)
            if device_row:
                if self.devices_web_elements.get_device_row_selection_checkbox_deselected(device_row):
                    self.utils.print_info(f"DEVICE {device_} IS DESELECTED")
                    unselected_device.append(device_)
                else:
                    self.utils.print_info(f"DEVICE {device_} IS NOT DESELECTED")
                    selected_device.append(device_)
                    ret_val = -1
            else:
                self.utils.print_info(f"Unable to obtain selection state for device {device_}")
                unknown_state.append(device_)
                ret_val = -1

        if ret_val != 1:
            if unknown_state != '':
                kwargs['fail_msg'] = f"Device state is unknown: {unknown_state}"
                self.common_validation.failed(**kwargs)
            elif unselected_device != '':
                kwargs['fail_msg'] = f"Device is selected: {selected_device}"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Device is not selected: {unselected_device}"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_all_devices_selected(self, **kwargs):
        """
        - This keyword confirms all devices in the table are selected
        - Keyword Usage:
        - `Confirm All Devices Selected`

        :return: returns 1 if all devices are selected; else, -1
        """

        device_count = self.get_device_count()
        selected_device_count = self.get_selected_device_count()
        self.utils.print_debug(f"Total number of devices in table is {device_count}")
        self.utils.print_debug(f"Total number of selected devices in table is {selected_device_count}")
        if device_count != selected_device_count:
            kwargs['fail_msg'] = "Some devices are not selected"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "All devices are selected"
            self.common_validation.passed(**kwargs)
        return 1

    def confirm_all_devices_deselected(self, **kwargs):
        """
        - This keyword confirms all devices in the table are deselected
        - Keyword Usage:
        - `Confirm All Devices Unselected`

        :return: returns 1 if no devices are selected; else, -1
        """

        device_count = self.get_device_count()
        deselected_device_count = self.get_deselected_device_count()
        self.utils.print_debug(f"Total number of devices in table is {device_count}")
        self.utils.print_debug(f"Total number of deselected devices in table is {deselected_device_count}")
        if device_count != deselected_device_count:
            kwargs['fail_msg'] = "Some devices are selected"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "All devices are deselected"
            self.common_validation.passed(**kwargs)
        return 1

    def wait_until_device_added(self, device_serial=None, device_name=None, device_mac=None, retry_duration=30,
                                retry_count=10, **kwargs):
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

        :param device_serial: device serial number to look for, by default set to None
        :param device_name: device name to look for, by default set to None
        :param device_mac: device MAC address to look for, by default set to None
        :param retry_duration: duration between each retry, by default set to 30
        :param retry_count: retry count, by default set to 10
        :return: 1 if device added within time; else -1
        """
        self.utils.print_info("Navigate to Manage> Devices")
        self.navigator.navigate_to_devices()

        # Search by Serial
        if device_serial:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Serial Number: loop {count}")
                if self.search_device(device_serial=device_serial, ignore_failure=True) == 1:
                    kwargs['pass_msg'] = f"Device with serial {device_serial} has been added"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.utils.print_info(
                        f"Device with serial {device_serial} is not yet present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                count += 1

        # Search by Name
        elif device_name:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Name: loop {count}")
                if self.search_device(device_name=device_name, ignore_failure=True) == 1:
                    kwargs['pass_msg'] = f"Device with name {device_name} has been added"
                    self.common_validation.passed(**kwargs)
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
                if self.search_device(device_mac=device_mac, ignore_failure=True) == 1:
                    kwargs['pass_msg'] = f"Device with MAC {device_mac} has been added"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.utils.print_info(
                        f"Device with MAC {device_mac} is not yet present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                count += 1

        # Unknown device search parameter
        else:
            kwargs['fail_msg'] = "Unknown device search parameter sent; please use Serial, Name, or MAC Address"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['fail_msg'] = "Device does not exist. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_device_removed(self, device_serial=None, device_name=None, device_mac=None, retry_duration=10,
                                  retry_count=30, **kwargs):
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

        :param device_serial: device serial number to look for, by default set to None
        :param device_name: device name to look for, by default set to None
        :param device_mac: device MAC address to look for, by default set to None
        :param retry_duration: duration between each retry, by default set to 10
        :param retry_count: retry count, by default set to 30
        :return: 1 if device removed within time; else -1
        """
        self.utils.print_info("Navigate to Manage> Devices")
        self.navigator.navigate_to_devices()

        # Search by Serial
        if device_serial:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Serial Number: loop {count}")
                if self.search_device(device_serial=device_serial, ignore_failure=True) == 1:
                    self.utils.print_info(
                        f"Device with serial {device_serial} is still present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                else:
                    kwargs['pass_msg'] = f"Device with serial {device_serial} has been removed"
                    self.common_validation.passed(**kwargs)
                    return 1
                count += 1

        # Search by Name
        elif device_name:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by Name: loop {count}")
                if self.search_device(device_name=device_name, ignore_failure=True) == 1:
                    self.utils.print_info(
                        f"Device with name {device_name} is still present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                else:
                    kwargs['pass_msg'] = f"Device with name {device_name} has been removed"
                    self.common_validation.passed(**kwargs)
                    return 1
                count += 1

        # Search by MAC address
        elif device_mac:
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Searching for device by MAC Address: loop {count}")
                if self.search_device(device_mac=device_mac, ignore_failure=True) == 1:
                    self.utils.print_info(
                        f"Device with MAC {device_mac} is still present. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                    self.refresh_devices_page()
                else:
                    kwargs['pass_msg'] = f"Device with MAC address {device_mac} has been removed"
                    self.common_validation.passed(**kwargs)
                    return 1
                count += 1

        # Unknown device search parameter
        else:
            kwargs['fail_msg'] = "Unknown device search parameter sent;  please use either Serial Number or MAC Address"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['fail_msg'] = "Device still exists in the view. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_device_removed_by_object(self, *device_dict, retry_duration=10, retry_count=30, **kwargs):
        """
        - This keyword is used to wait for the device to be removed from extauto.xiq.
        - This keyword by default loops 10 times every 30 seconds to check if the device exists
        - Flow:
        - Navigate to Manage --> Devices
        - search for the device based on specified device criteria
        - Keyword Usage:
        - ``Wait Until Device Removed    device_serial=${device_dict}    retry_duration=15    retry_count=20``

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1)
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device removed within time; else -1
        """

        device_keys = {
            "mac": device_dict[0].get("mac"),
            "serial": device_dict[0].get("serial"),
            "name": device_dict[0].get("name")
        }
        device_keys = {key: value for key, value in device_keys.items() if value}

        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "Invalid args. You must pass in at least one of the following: serial, name, or mac!"
            self.common_validation.fault(**kwargs)
            return -1

        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for device using {device_keys} --- Loop {count}")
            if self.search_device_by_object(device_keys, skip_refresh=True, skip_navigation=True, ignore_failure=True) == 1:
                self.utils.print_info(f"Device with: {device_keys} is still present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.refresh_devices_page()
            else:
                kwargs['pass_msg'] = f"Device with {device_keys} has been removed"
                self.common_validation.passed(**kwargs)
                return 1
            count += 1

        kwargs['fail_msg'] = "Device still exists in the view. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_device_managed(self, device_serial, retry_duration=30, retry_count=10, **kwargs):
        """
        - This keyword waits until the MANAGED column for the specified device to contains 'Managed' state.
        - This keyword by default loops every 30 seconds for 10 times to check the MANAGED column data
        - Flow:
        - Navigate to Manage --> Devices
        - check the specified device MANAGED column for data
        - Keyword Usage:
        - ``Wait Until Device Managed  ${DEVICE_SERIAL}   retry_duration=10    retry_count=12``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device serial number to check the device 'managed' state
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :param kwargs: keyword arguments XAPI_ENABLE
        :return: 1 if MANAGED column contains 'Managed' within the specified time, else -1
        """

        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_wait_until_device_managed(device_serial=device_serial, retry_duration=retry_duration, retry_count=retry_count)

        # UI Support
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        # Enable the 'Managed' Column
        self.column_picker_select('Managed')

        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Searching for device {device_serial}: loop {count}")
            col_value = self.get_device_details(device_serial, 'MANAGED')
            if col_value == "Managed":
                kwargs['pass_msg'] = f"MANAGED column for device {device_serial} contains expected data: '{col_value}"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(
                    f"MANAGED column for device {device_serial} contains value: '{col_value}' "
                    f"still not matching expected value 'Managed'. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.refresh_devices_page()
            count += 1

        kwargs['fail_msg'] = f"MANAGED column for device {device_serial} does not contain expected value 'Managed'"
        self.common_validation.failed(**kwargs)
        return -1

    def wait_until_device_data_present(self, device_serial, col, retry_duration=30, retry_count=10, **kwargs):
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
                kwargs['pass_msg'] = f"{col} column contains data: '{col_value}'"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"{col} column is still empty. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.refresh_devices_page()
            count += 1

        kwargs['fail_msg'] = f"{col} column for device {device_serial} still does not contain data. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def get_device_management_ip_address(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        - Get Management IP Assigned to the AP
        - Keyword Usage:
        - ``Get Device Management IP Address   device_serial=${DEVICE_SERIAL}``
        - ``Get Device Management IP Address   device_name=${DEVICE_NAME}``
        - ``Get Device Management IP Address   device_mac=${DEVICE_MAC}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: Serial number of Device Ex:11301810220048, by default set to None
        :param device_name: Device name Ex: AP1130, by default set to None
        :param device_mac: Device mac Ex: F09CE9F89600, by default set to None
        :return: Device Management IP Address
        """

        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_get_device_management_ip_address(device_serial=device_serial, device_mac=device_mac, **kwargs)

        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [device_serial, device_mac, device_name] if value][0]
        management_ip = self.get_device_details(search_string, 'MGT IP ADDRESS')
        if management_ip:
            kwargs['pass_msg'] = f"MGMT IP ADDRESS is {management_ip} using {search_string}"
            self.common_validation.passed(**kwargs)
            return management_ip
        else:
            kwargs['fail_msg'] = f"Did not get MGMT IP ADDRESS using {search_string}"
            self.common_validation.failed(**kwargs)
            return -1

    @deprecated("Please use get_device_management_ip_address(...)")
    # This was put into deprecated mode on March 9th 2023
    def get_ap_management_ip_address(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get Management IP Assigned to the AP
        - Keyword Usage:
        - ``Get Ap Management IP Address   ap_serial=${AP_SERIAL}``
        - ``Get Ap Management IP Address   ap_name=${AP_NAME}``
        - ``Get Ap Management IP Address   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: AP Management IP Address
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        management_ip = self.get_device_details(search_string, 'MGT IP ADDRESS')
        if management_ip:
            return management_ip

    def confirm_device_disconnected(self, device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        - This keyword confirms the device is disconnected
        - Keyword Usage:
        - ``Confirm Device Disconnected   device_serial=${DEVICE_SERIAL}``
        - ``Confirm Device Disconnected   device_name=${DEVICE_NAme}``
        - ``Confirm Device Disconnected   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial, by default set to None
        :param device_name: device host name, by default set to None
        :param device_mac: device MAC address, by default set to None

        :return: 1 if device is currently disconnected, else -1
        """

        device_row = -1
        self.refresh_devices_page()

        if device_serial:
            self.utils.print_info(f"Getting status of device with serial {device_serial}")
            device_row = self.get_device_row(device_serial=device_serial)
        elif device_name:
            self.utils.print_info(f"Getting status of device with name {device_name}")
            device_row = self.get_device_row(device_name=device_name)
        elif device_mac:
            self.utils.print_info(f"Getting status of device with MAC {device_mac}")
            device_row = self.get_device_row(device_mac=device_mac)
        else:
            self.utils.print_info("Please specify a serial #, device name, or MAC address")

        if device_row:
            sleep(5)
            device_status = self.devices_web_elements.get_status_cell(device_row)
            self.screen.save_screen_shot()
            sleep(2)

            if "hive-status-false" in device_status:
                kwargs['pass_msg'] = "hive-status-false - device disconnected"
                self.common_validation.passed(**kwargs)
                return 1
            elif "local-icon" in device_status:
                kwargs['pass_msg'] = "local-icon - device disconnected"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Device didn't disconnect"
        self.common_validation.failed(**kwargs)
        return -1

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
                        map_value = label_map.get(label_str)
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

        self.utils.print_info("****************** DEVICE ROW VALUES ************************")
        for key, value in device_detail_dict.items():
            self.utils.print_info(f"{key}:{value}")

        return device_detail_dict

    def confirm_no_duplicate_rows(self, search_string, **kwargs):
        """
        - Searches for device rows containing the search_string and confirms only one row exists with the value.
        - This is useful for confirming only one device with a specified MAC Address exists in the table, but
        - should not be used for search strings where multiple rows could contain the same value (e.g., a certain
        - name value, or a serial number which is also used in another row, like CLOUD CONFIG GROUPS in XIQ-SE).

        :param search_string: String to look for in each row
        :return: return 1 if none or only one row with the search string is found (no duplicates); -1 if more than one row contains the search string
        """

        ret_val = 1
        matching_rows = 0
        self.navigator.enable_page_size()
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

        if ret_val == 1:
            if matching_rows == 0:
                kwargs['pass_msg'] = f"No rows contain the value {search_string}"
                self.common_validation.passed(**kwargs)
            elif matching_rows == 1:
                kwargs['pass_msg'] = f"Found one row with the value {search_string}"
                self.common_validation.passed(**kwargs)
        else:
            kwargs['fail_msg'] = f"Found more then one row {matching_rows} with the value {search_string}"
            self.common_validation.failed(**kwargs)
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
                self.utils.print_info("Move mouse over ADD button...")
                add_button = self.devices_web_elements.get_devices_add_button()
                if add_button:
                    self.auto_actions.move_to_element(add_button)
            else:
                self.utils.print_debug("'Last Refreshed at:' tooltip is not displayed")
        else:
            self.utils.print_info("Could not find 'Last Refreshed at:' tooltip element")

    def confirm_xiqse_managed_device_not_onboarded_by_xiq(self, device_serial, device_make, location, **kwargs):
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
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), device_serial)

        self.utils.print_info("Selecting Make")
        self.auto_actions.click_reference(self.switch_web_elements.get_switch_make_drop_down)
        sleep(2)
        self.switch_web_elements.select_drop_down_options(self.switch_web_elements.get_switch_make_drop_down_options(),
                                                          device_make)

        if location:
            self.auto_actions.click_reference(self.devices_web_elements.get_location_button)
            self._select_location(location)
        else:
            kwargs['fail_msg'] = "LOCATION NOT SPECIFIED BUT IS A REQUIRED FIELD"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_button)

        self.screen.save_screen_shot()
        sleep(2)

        # Commented on 1/18/23 because variable is unused
        # tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        self.dialogue_web_elements.get_tooltip_text()
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

    def check_tooltip_message_presence(self, tooltip_message, **kwargs):
        """
        - This Keyword will validate whether given Tooltip Message Displayed on Manage--> Devices Page
        - Keyword Usage:
        - ``check tooltip message presence  ${TOOLTIP_MESSAGE}``

        :param tooltip_message: Tooltip message to check on devices page
        :return: 1 if tooltip message appears, else -1
        """
        self.navigator.navigate_to_devices()
        self.refresh_devices_page()

        self.screen.save_screen_shot()
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if tooltip_message in tool_tip_text:
            kwargs['pass_msg'] = "Tooltip message appeared on the page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Tooltip message not seen"
            self.common_validation.failed(**kwargs)
            return -1

    def get_ap_wifi0_radio_profile(self, ap_serial=None, ap_name=None, ap_mac=None):
        """
        - Get the Wifi0 Radio Profile applied on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
        - ``Get Ap WIFI0 Radio Profile   ap_serial=${AP_SERIAL}``
        - ``Get Ap WIFI0 Radio Profile   ap_name=${AP_NAME}``
        - ``Get Ap WIFI0 Radio Profile   ap_mac=${AP_MAC}``

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Radio Profile value of wifi0 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Radio Profile value of wifi1 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Ap Public IP Address
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("Public IP Address")
        ap_public_ip = self.get_device_details(search_string, 'PUBLIC IP ADDRESS')
        if ap_public_ip:
            return ap_public_ip

    def device_update_progress(self, device_serial=None, retry_duration=30, retry_count=900, **kwargs):
        """
        - This keyword is used to check the status of the device update and also shows device update progress status
        such as 19%...etc
        - It will poll the "update status" every retry_duration seconds
        - Assuming that config push will take a maximum of fiften minutes
        - Flow:
        - Navigate to Manage --> Devices
        - check the device status and device update prograss for a device based on passed device serial
        - Keyword Usage:
        - `Device Update Progress       ${DEVICE_SERIAL}   retry_duration=30       retry_count=800``

        :param device_serial: device serial number to check the config push status, by default set to None
        :param retry_duration: duration between each retry, by default set to 30
        :param retry_count: retry count, by default set to 900
        :return: device update status if config push success else -1
        """
        device_updated_status = -1
        device_row = ""
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        self.utils.print_info('Getting device Updated Status using')
        if device_serial:
            self.utils.print_info("Getting Updated status of device with serial: ", device_serial)
            device_row = self.get_device_row(device_serial=device_serial)

        if device_row:
            count = 0
            while count <= retry_count:
                device_updated_status = self.get_device_updated_status(device_serial)
                self.refresh_devices_page()
                if re.search(r'\d+-\d+-\d+', device_updated_status):
                    break
                elif device_updated_status == "Device Update Failed.":
                    device_row = self.get_device_row(device_serial=device_serial)
                    device_updated_status = self.device_update.get_device_update_form_error(device_row)
                    kwargs['fail_msg'] = "Device Update Failed"
                    self.common_validation.failed(**kwargs)
                    return -1
                sleep(retry_duration)
                self.utils.print_info(f"Time elapsed for device update: {count} seconds")
                count += retry_duration

        return device_updated_status

    def get_stack_status(self, device_mac=None, **kwargs):
        """
        - This keyword returns the Stack icon status is blue or red
        - 'blue' means all the stack members are in managed state
        - 'red' means one or more slot is not in managed state
        - '-1' means the device is not a stack device
        - Keyword Usage:
        - ``Get Stack Status   device_mac=${DEVICE_MAC}``

       :param device_mac: device MAC address, by default set to None

       :return:
       - 'blue' if all the stack members are in managed state else 'red'
       - '-1' if the stack icon is not in the device row

       """
        device_row = -1
        self.refresh_devices_page()

        self.utils.print_info('Getting Stack Status ')

        if device_mac:
            self.utils.print_info("Getting status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac=device_mac)

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
                kwargs['fail_msg'] = "Could not get stack status"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not get device row of the device"
            self.common_validation.fault(**kwargs)
            return -1

    def verify_stack_devices_managed(self, stack_mac, slot_serial_list, **kwargs):
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
        :return: 1 if column contains data within the specified time, else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        self.refresh_devices_page()
        self.screen.save_screen_shot()

        self.utils.print_info("Search Stack row")
        stack_row = self.get_device_row(device_mac=stack_mac)

        if stack_row:
            sleep(5)
            self.utils.print_info("Click on stack icon")
            self.auto_actions.click(self.devices_web_elements.get_stack_status_icon(stack_row))
            self.screen.save_screen_shot()

        slot_rows = self.devices_web_elements.get_devices_page_stack_slot_rows(stack_row)
        if slot_rows:
            self.utils.print_info("Stack Slot Rows Found..")
        count = 0
        self.utils.print_info("Searching for slot entry in stack")
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

        if count == len(slot_serial_list):
            kwargs['pass_msg'] = "All the Slots are in Managed state"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Not all the slots are in managed state"
            self.common_validation.failed(**kwargs)
            return -1

    def update_device_using_hostname(self, device_name):
        """
        - Update the network policy to the selected devices
        - Based on the update method, update the devices
        - Keyword Usage:
        - ``Update Device Using Hostname    name=${SW_HOST}     '`
        :param device_name: name of the device

            PolicyAndConfig - selects the "Update Network Policy and Configuration" check button
        :return:  1 if update was performed, -1 if not
        """
        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
        sleep(2)

        # Perform the update
        self.utils.print_info("Click on perform update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)

        self.screen.save_screen_shot()
        sleep(2)

        return self._check_device_update_status(device_name)

    def update_network_policy_to_stack(self, device_mac, policy_name, template_policy_name, **kwargs):
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

        if not self.select_device(device_mac=device_mac, skip_navigation=True):
            kwargs['fail_msg'] = f"Switch {device_mac} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        if not self._assign_network_policy(policy_name):
            kwargs['fail_msg'] = "Failed to assign network policy"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(30)

        self.utils.print_info("Select Switch row")
        self.select_device(device_mac=device_mac)
        sleep(5)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
        sleep(2)

        # Select from dropdown
        if template_policy_name is not None:
            click_dropdown = self.devices_web_elements.get_devices_stack_update_policy_dropdown_btn()
            if click_dropdown:
                self.utils.print_info("Click on dropdown")
                self.auto_actions.click(click_dropdown)
            else:
                self.utils.print_info("Not able to find dropdown")
            dropdown_items = self.devices_web_elements.get_devices_stack_update_policy_dropdown_items()
            if dropdown_items:
                self.utils.print_info("The templates from dropdown are: ")
                for elem in dropdown_items:
                    self.utils.print_info(elem.text)
                for el in dropdown_items:
                    if template_policy_name in el.text:
                        self.utils.print_info(f"Select {el.text} from dropdown")
                        self.auto_actions.select_drop_down_options(dropdown_items, el.text)
                    else:
                        self.utils.print_info("The template name was not found in dropdown")
            else:
                self.utils.print_info("Not able to find dropdown items")
        else:
            kwargs['fail_msg'] = "Didn't pass the template policy name"
            self.common_validation.fault(**kwargs)
            return -1

        # Perform the update
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        self.utils.print_info("Click on perform update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_perform_update_button_d360)

        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_after = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_after)

        for item_after in tool_tp_text_after:
            if item_after in tool_tp_text_before:
                pass
            else:
                self.utils.print_info("Below error message is displayed after press update button")
                self.utils.print_info(item_after)
                if self.devices_web_elements.get_devices_close_button_update():
                    self.utils.print_info("Click on exit button")
                    self.auto_actions.click_reference(self.devices_web_elements.get_devices_close_button_update)
                else:
                    self.utils.print_info("The exit button was not found")
                return item_after
        return self.check_device_update_status_by_using_mac(device_mac)

    def check_device_update_status_by_using_mac(self, device_mac, **kwargs):
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
                kwargs['fail_msg'] = "Config push to switch taking more than 5 minute"
                self.common_validation.fault(**kwargs)
                return -1
            if 'Failed' in device_update_status:
                kwargs['fail_msg'] = f"Device Update Failed: {device_update_status}"
                self.common_validation.failed(**kwargs)
                return -1
            sleep(30)
            self.utils.print_info(f"Time elapsed for device update: {retry_count} seconds")
            retry_count += 30
        self.utils.print_info("return 1  ", device_update_status)
        return 1

    def get_device_stack_status(self, device_mac=None, device_serial=None, duration_retry=300, **kwargs):
        """
        - This keyword returns the device's connection status, audit log status
        - Keyword Usage:
        - ``Get Device Stack Status   device_serial=${DEVICE_SERIAL}``
        - ``Get Device Stack Status   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial, by default set to None
        :param device_mac: device MAC address, by default set to None
        :param duration_retry : duration of retry in seconds, by default set to 300

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
            device_row = self.get_device_row(device_mac=device_mac, ignore_failure=True)
            if device_row != -1:
                self.utils.print_info("Found a raw with mac :", device_mac)
                self.utils.print_info("Check if stack toggle icon is present")
                stack_toggle = self.devices_web_elements.get_device_stack_toggle(device_row)
                if stack_toggle:
                    device_row = -1
                    if device_serial:
                        device_row = self.get_device_row(device_serial, ignore_failure=True)
                    if device_row == -1:
                        if "ui-icon-stack" in stack_toggle.split(" "):
                            self.utils.print_info("The stack toogle icon is blue. Now check the connection status   ")
                            connected_status = self.get_device_status(device_mac=device_mac)
                            if connected_status:
                                if connected_status == 'green':
                                    status = 'blue'
                                    self.utils.print_info("Return :", status)
                                    self.screen.save_screen_shot()
                                    return status
                                elif connected_status == 'disconnected':
                                    self.utils.print_info(
                                        "Status is disconnected ,try again until duration_retry expired:",
                                        connected_status)
                                    status = connected_status
                                else:
                                    self.utils.print_info("Return :", connected_status)
                                    self.screen.save_screen_shot()
                                    return connected_status
                            else:
                                self.utils.print_info("Cannot read the conection status")
                        elif "ui-icon-stack-warning" in stack_toggle.split(" "):
                            self.utils.print_info(
                                "The stack toogle icon is red. Continue to check until duration_retry expired ")
                            status = 'red'
                        else:
                            kwargs['fail_msg'] = "Stack_toggle icon is present but the status can not be read"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        pass
                else:
                    if try_one_more_time_mac:
                        try_one_more_time_mac = False
                    else:
                        kwargs['fail_msg'] = "Found a raw with mac but stack_toggle icon was not found"
                        self.common_validation.fault(**kwargs)
                        return -1
            else:
                self.utils.print_info("No found a raw with mac :", device_mac)
                self.utils.print_info("Search device with serial: ", device_serial)
                device_row = self.get_device_row(device_serial, ignore_failure=True)
                if device_row != -1:
                    self.utils.print_info("Found a raw with serial {}.The stack is not formed yet. "
                                          "Continue to check until duration_retry expired ".format(device_serial))
                    status = -1
                    self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Did not found a raw with serial or mac ; Try one more time  ")
                    if try_one_more_time_serial:
                        try_one_more_time_serial = False
                    else:
                        kwargs['fail_msg'] = f"Not found a raw with serial {device_serial} or mac {device_mac}"
                        self.common_validation.fault(**kwargs)
                        return -1
            retry_count += 30
            self.utils.print_info("Try again after {} seconds:".format(duration_retry / 10))
            sleep(duration_retry / 10)
        self.screen.save_screen_shot()
        self.utils.print_info("duration_retry expired ; Return :", status)
        return status

    def actions_xiqse_open_site_engine(self, **kwargs):
        """
        - This keyword clicks on the ACTIONS > OPEN SITE ENGINE link
        - It is assumed that the Manage > Device window is open and an XIQ-SE managed device is selected.
        - Keyword Usage
        - ``Actions XIQSE Open Site Engine``

        :return: 1 if action was successful (or the field is disabled), else -1
        """

        self.utils.print_info("Clicking on Actions Button")
        self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
        sleep(2)

        ose_link = self.devices_web_elements.get_actions_open_site_engine_menu_option()
        if ose_link:
            hidden = ose_link.get_attribute("style")
            self.utils.print_debug(f"Open Site Engine link Style value: {hidden}")
            if hidden == "display: none;":
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = "The 'Open Site Engine' link is hidden."
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.screen.save_screen_shot()
                self.auto_actions.click(ose_link)
                kwargs['pass_msg'] = "Clicking the 'Open Site Engine' link."
                self.common_validation.passed(**kwargs)
                return 1
        else:
            self.utils.print_info("Could not find the 'Open Site Engine' link.")

        kwargs['fail_msg'] = "Could not find the 'Open Site Engine' link. "
        self.common_validation.failed(**kwargs)
        return -1

    def _is_xiqse_maximum_site_engine_message_displayed(self):
        """
        - This helper function checks if the 'Maximum 5 Site Engine > Device View' message banner is displayed.
        - The message banner will be closed, if displayed.

        :return: True if the message banner is displayed, else False
        """
        self.utils.print_info("Checking for the 'Maximum 5 Site Engine > Device View...` message")
        self.screen.save_screen_shot()
        if self.devices_web_elements.get_ui_banner_warning_message():
            banner_warning_text = self.devices_web_elements.get_ui_banner_warning_message().text
            if "Maximum 5 Site Engine" in banner_warning_text:
                self.utils.print_info(f"Warning Message: {banner_warning_text}")
                self.auto_actions.click_reference(self.devices_web_elements.get_ui_banner_warning_close_button)
                return True

        self.utils.print_info("Expected Warning Message Banner not found.")
        return False

    def verify_xiqse_maximum_site_engine_message_displayed(self, **kwargs):
        """
        - This keyword checks if the 'Maximum 5 Site Engine > Device View' message banner is displayed.
        - Keyword Usage
        - ``Verify XIQSE Maximum Site Engine Message Displayed``

        :return: True if the message banner is displayed, else False
        """
        if self._is_xiqse_maximum_site_engine_message_displayed():
            kwargs['pass_msg'] = "'Maximum 5 Site Engine > Device View' message banner is displayed"
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "Expected Warning Message Banner not found."
            self.common_validation.failed(**kwargs)
            return False

    def verify_xiqse_maximum_site_engine_message_not_displayed(self, **kwargs):
        """
        - This keyword checks if the 'Maximum 5 Site Engine > Device View' message banner is NOT displayed.
        - Keyword Usage
        - ``Verify XIQSE Maximum Site Engine Message Not Displayed``

        :return: True if the message banner is NOT displayed, False if the message is displayed
        """
        if not self._is_xiqse_maximum_site_engine_message_displayed():
            kwargs['pass_msg'] = "'Maximum 5 Site Engine > Device View' message banner is NOT displayed"
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "'Maximum 5 Site Engine > Device View' message banner is displayed"
            self.common_validation.failed(**kwargs)
            return False

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

    def rbac_user_multiple_location_search_AP_serial(self, ap_serial, **kwargs):
        """
        - Searches for AP matching AP's Serial Number based on
        - Keyword Usage:
        - ``Search AP Serial  ${AP_SERIAL}``

        :param ap_serial: AP's Serial Number
        :return: return 1 if AP found else False
        """
        device_keys = {}
        if ap_serial:
            device_keys['ap_serial'] = ap_serial
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "You must pass the serial number!"
            self.common_validation.fault(**kwargs)
            return -1

        # Commented on 1/18/23 because variable is unused
        # page_size_field = self.devices_web_elements.get_devices_display_count_per_page_buttons()
        # page_number_field = self.devices_web_elements.get_devices_pagination_buttons()

        # Commented on 3/3/23 because they are unnecessary
        # self.devices_web_elements.get_devices_display_count_per_page_buttons()
        # self.devices_web_elements.get_devices_pagination_buttons()

        self.navigator.navigate_to_devices()
        self.navigator.enable_page_size()
        self.refresh_devices_page()

        row = self._find_device_row(device_keys)
        if row:
            self.utils.print_info(f"Found row for device {device_keys}")
            return 1

        kwargs['fail_msg'] = f"Didn't find the device {device_keys}"
        self.common_validation.failed(**kwargs)
        return False

    def _select_location(self, sel_loc):
        """
        - This keyword selects a location in the location dialog and clicks the "Assign" button.
        - It is assumed the location dialog is already open.
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
                self.auto_actions.click_reference(self.devices_web_elements.get_location_select_button)
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

    def select_location_quick_onboarding(self, sel_loc, **kwargs):
        """
        - This keyword selects a location in the location dialog and clicks the "Select" button.
        - It is assumed the location dialog is already open.
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
                self.auto_actions.click_reference(self.devices_web_elements.get_cancel_location_button)
            else:
                self.utils.print_info("Cancel button was not found")
                sleep(3)
            kwargs['fail_msg'] = "Location has not been found"
            self.common_validation.failed(**kwargs)
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
            kwargs['fail_msg'] = "Building has not been found"
            self.common_validation.failed(**kwargs)
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
            kwargs['fail_msg'] = "Floor has not been found"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def quick_onboarding_cloud_manual(self, device_sn, device_make, location, policy_name=None, **kwargs):
        """
        This keyword on boards your devices directly to cloud by using new onboarding flow
        Can on boards an aerohive device [AP or Switch], Universal APs , Exos Switch, Exos Stack and Voss devices
        using Quick onboarding flow.
        - Keyword Usage:
        - quick_onboarding_cloud_manual          ${DUT_SERIAL}    voss      Bucharest,address,Floor 1

        :param device_sn: serial number of Device; single SN or a list of SNs
        :param device_make: Model of the Device e.g. :aerohive/universal_ap/voss/exos
        :param location: The location, building and floor separated by comma ; e.g. Bucharest,address,Floor 1
        :param policy_name: The policy name, by default set to None
        :return: 1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message will be returned ; else -1
        """

        self.navigator.navigate_to_devices()
        add_button = self.devices_web_elements.get_add_button()
        if add_button:
            self.utils.print_info("Click on '+' button")
            self.auto_actions.click(add_button)
        else:
            kwargs['fail_msg'] = "'+' button not found"
            self.common_validation.fault(**kwargs)
            return -1
        quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
        if quick_add_devices_button:
            self.utils.print_info("Click on 'Quick Add Devices'")
            self.auto_actions.move_to_element(quick_add_devices_button)
        else:
            kwargs['fail_msg'] = "'Quick Add Devices' button not found"
            self.common_validation.fault(**kwargs)
            return -1
        deploy_to_cloud_button = self.devices_web_elements.get_deploy_to_cloud()
        if deploy_to_cloud_button:
            self.utils.print_info("Click on 'Deploy to the cloud'")
            self.auto_actions.click(deploy_to_cloud_button)
        else:
            kwargs['fail_msg'] = "'Deploy to the cloud' button not found"
            self.common_validation.fault(**kwargs)
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
            kwargs['fail_msg'] = "'Serial number' box not found"
            self.common_validation.fault(**kwargs)
            return -1
        if location:
            if self.devices_web_elements.get_add_location_button():
                self.utils.print_info("Click on 'Location'")
                self.auto_actions.click_reference(self.devices_web_elements.get_add_location_button)
                self.utils.print_info("Selecting location " + location)
                if self.select_location_quick_onboarding(location) == 1:
                    self.utils.print_info("Location selected ")
                    self.utils.print_info("Clicking on select location Button")
                    self.auto_actions.click_reference(self.devices_web_elements.get_select_location)
                else:
                    self.auto_actions.click_reference(self.devices_web_elements.get_cancel_location_button)
                    self.utils.print_info("Selecting Cancel button")
                    return -1
            else:
                kwargs['fail_msg'] = "'Location' button not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("The location will not be selected")
        if policy_name != None:
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            if self.devices_web_elements.get_policy_drop_down():
                self.auto_actions.click_reference(self.devices_web_elements.get_policy_drop_down)
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
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_list)
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_voss)
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_voss():
                    self.utils.print_info("'VOSS' autodetection is working")
                    self.utils.print_info("Selecting 'VOSS' from the 'Device OS' checkbox...")
                    self.auto_actions.click_reference(self.devices_web_elements.get_device_auto_detection_voss)
                else:
                    kwargs['fail_msg'] = "Button 'VOSS' not found"
                    self.common_validation.fault(**kwargs)
                    return -1
        elif 'exos' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.utils.print_info("'EXOS' found in 'Device Make' list")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_list)
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_exos)
                sleep(2)
            else:
                if self.devices_web_elements.get_device_auto_detection_exos():
                    self.utils.print_info("'EXOS' autodetection is working ")
                    self.utils.print_info("Selecting 'EXOS' from the 'Device OS' checkbox...")
                    self.auto_actions.click_reference(self.devices_web_elements.get_device_auto_detection_exos)
                else:
                    kwargs['fail_msg'] = "Button 'EXOS' not found"
                    self.common_validation.fault(**kwargs)
                    return -1
        elif 'aerohive' in device_make.lower():
            self.utils.print_info("Selecting 'Extreme - Aerohive' from the 'Device Make' drop down...")
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_list)
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_aerohive)
            sleep(2)
        elif 'universal_ap' in device_make.lower():
            if self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio():
                self.utils.print_info("'cloudIqEngine' autodetection is working ")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio)
            else:
                kwargs['fail_msg'] = "'cloudIqEngine' autodetection is not working "
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "'Device make' list not found"
            self.common_validation.failed(**kwargs)
            return -1
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)
        if self.devices_web_elements.get_add_devices_button():
            self.utils.print_info("Click on Add Devices")
            self.auto_actions.click_reference(self.devices_web_elements.get_add_devices_button)
            # Check the already onboarded error
            if self.devices_web_elements.get_quick_onboard_failure_panel():
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
            kwargs['fail_msg'] = "'Add Devices' button not found or the button is not active"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def quick_onboarding_cloud_csv(self, device_make, csv_location, location=None, policy_name=None, **kwargs):
        """
        This keyword on boards your devices directly to cloud by using new onboarding flow
        Can on boards an aerohive device [AP or Switch], Universal APs , Exos Switch, Exos Stack and Voss devices
        using Quick onboarding flow.
        - Keyword Usage:
        - quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}

        :param device_sn: serial number of Device; single SN or a list of SNs
        :param device_make: Model of the Device e.g. :aerohive/universal_ap/voss/exos
        :param location: The location, building and floor separated by comma ; e.g. Bucharest,address,Floor 1, by default set to None
        :param csv_location: csv file path
        e.g. ${DUT_CSV_FILE}             /automation/xiq/cw_automation/testsuites/xiq/topologies/${TESTBED}/MultipleVossDevices.csv
        :param policy_name: The policy name, by default set to None
        :return: 1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message will be returned ; else -1
        """

        self.navigator.navigate_to_devices()
        add_button = self.devices_web_elements.get_add_button()
        if add_button:
            self.utils.print_info("Click on '+' button")
            self.auto_actions.click(add_button)
        else:
            kwargs['fail_msg'] = "'+' button not found"
            self.common_validation.fault(**kwargs)
            return -1
        quick_add_devices_button = self.devices_web_elements.get_quick_add_devices()
        if quick_add_devices_button:
            self.utils.print_info("Click on 'Quick Add Devices'")
            self.auto_actions.move_to_element(quick_add_devices_button)
        else:
            kwargs['fail_msg'] = "'Quick Add Devices' button not found"
            self.common_validation.fault(**kwargs)
            return -1
        deploy_to_cloud_button = self.devices_web_elements.get_deploy_to_cloud()
        if deploy_to_cloud_button:
            self.utils.print_info("Click on 'Deploy to the cloud'")
            self.auto_actions.click(deploy_to_cloud_button)
        else:
            kwargs['fail_msg'] = "'Deploy to the cloud' button not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        if self.devices_web_elements.get_select_csv():
            self.utils.print_info("Select CSV")
            self.auto_actions.click_reference(self.devices_web_elements.get_select_csv)
        else:
            kwargs['fail_msg'] = "CSV checkbox was not found"
            self.common_validation.fault(**kwargs)
            return -1
        if 'voss' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'VOSS' from the 'Device Make' drop down...")
                self.utils.print_info("'VOSS' found in 'Device Make' list")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_list)
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_voss)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Button 'VOSS' not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif 'exos' in device_make.lower():
            if self.devices_web_elements.get_device_make_list():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.utils.print_info("'EXOS' found in 'Device Make' list")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_list)
                self.auto_actions.click_reference(self.devices_web_elements.get_device_make_exos)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Button 'EXOS' not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif 'aerohive' in device_make.lower():
            self.utils.print_info("Selecting 'Extreme - Aerohive' from the 'Device Make' drop down...")
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_list)
            self.auto_actions.click_reference(self.devices_web_elements.get_device_make_aerohive)
            sleep(2)
        elif 'universal_ap' in device_make.lower():
            if self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio():
                self.utils.print_info("'cloudIqEngine' autodetection is working ")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_auto_detection_cloudIqEngineRadio)
            else:
                pass
        else:
            kwargs['fail_msg'] = "'Device make' list not found"
            self.common_validation.fault(**kwargs)
            return -1
        if csv_location:
            upload_button = self.devices_web_elements.get_device_csv_upload_button()
            if upload_button:
                self.utils.print_info("Specifying CSV file '" + csv_location)
                self.auto_actions.send_keys(upload_button, csv_location)
            else:
                self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
                return -1
        else:
            self.utils.print_info(">>> CSV file was not specified")
            self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
            kwargs['fail_msg'] = "CSV file was not specified."
            self.common_validation.fault(**kwargs)
            return -1
        if location != None:
            if self.devices_web_elements.get_add_location_button():
                self.utils.print_info("Click on 'Location'")
                self.auto_actions.click_reference(self.devices_web_elements.get_add_location_button)
                self.utils.print_info("Selecting location '" + location + "'")
                if self.select_location_quick_onboarding(location) == 1:
                    self.utils.print_info("Location selected ")
                    self.utils.print_info("Clicking on select location Button")
                    self.auto_actions.click_reference(self.devices_web_elements.get_select_location)
                else:
                    self.auto_actions.click_reference(self.devices_web_elements.get_cancel_location_button)
                    self.utils.print_info("Selecting Cancel button")
                    kwargs['fail_msg'] = "Didn't select location"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "'Location' button not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("The location will not be selected")
        if policy_name != None:
            self.utils.print_info("Selecting policy '" + policy_name + "'")
            if self.devices_web_elements.get_policy_drop_down():
                self.auto_actions.click_reference(self.devices_web_elements.get_policy_drop_down)
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
            self.auto_actions.click_reference(self.devices_web_elements.get_add_devices_button)
            # Check the already onboarded error
            if self.devices_web_elements.get_quick_onboard_failure_panel():
                kwargs['fail_msg'] = "SN already onboarded"
                self.common_validation.fault(**kwargs)
                return -1
            else:
                pass
            """
            JPS -- Dec 20, 2022
            The following code did not work as desired, it would find a tool tip that was just an
            info message and fail the keyword. In the future there should be a common error checker
            used by all onboard keywords. In the future the onboard_device_quick should be able
            onboard a device with a CSV and this should whol keyword should be removed.
            """
            # Check the banner error
            # sleep(3)
            # tool_tp_text_after = tool_tip.tool_tip_text.copy()
            # self.utils.print_info(tool_tp_text_after)
            # for item_after in tool_tp_text_after:
            #    if item_after in tool_tp_text_before:
            #        pass
            #    else:
            #        if 'successfully' in item_after:
            #            pass
            #        else:
            #            self.utils.print_info(" Below error message is displayed after press ADD button")
            #            self.utils.print_info(item_after)
            #            return item_after
        else:
            kwargs['fail_msg'] = "'Add Devices' button not found or the button is not active"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def get_device_template_status(self, device_mac=None, duration_retry=50, **kwargs):
        """
        - This keyword returns the device's connection status, audit log status
        - Keyword Usage:
        - ``Get Template Status   device_mac=${DEVICE_MAC}``

        :param device_mac: device MAC address, by default set to None
        :param duration_retry : duration of retry in seconds, by default set to 50
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
            if device_mac:
                self.utils.print_info("Getting status of Template with MAC: ", device_mac)
                device_row = self.get_device_row(device_mac=device_mac)

            if device_row != -1:
                self.utils.print_info("Found a raw with mac :", device_mac)
                self.utils.print_info("Check if Template column is present")
                # Commented on 1/18/23 because variable is unused
                # stack_template = self.devices_web_elements.get_device_stack_template(device_row)
                self.devices_web_elements.get_device_stack_template(device_row)

            if device_row:
                sleep(5)
                device_updated_status = self.devices_web_elements.get_device_stack_template(device_row)
                self.utils.print_info("Device Template Column Status is :", device_updated_status)
                if "Assign/Create Template" in device_updated_status.text:
                    kwargs['pass_msg'] = "Device Template Column Status: Assign/Create Template"
                    self.common_validation.passed(**kwargs)
                    return 3

                elif "default-template" in device_updated_status.text:
                    kwargs['pass_msg'] = "Device Template Column Status: Device default-template"
                    self.common_validation.passed(**kwargs)
                    return 2
                else:
                    return 1

    def create_stack_auto_template(self, device_mac=None, name_stack_template=None, **kwargs):
        """
        - This Keyword will create EXOS Stack Auto Template after assigned a policy to the stack
        - Keyword Usage
        - ``Get Template Status   device_mac=${DEVICE_MAC}``
        - ``Name Stack Template   ${Stack_TEMPLATE_NAME}``

        :param device_mac: device MAC address, by default set to None
        :param name_stack_template: Name of the stack_template, by default set to None
        :return: 1 If successfully Switch Stack template
        """
        device_keys = {}
        if device_mac:
            device_keys['device_mac'] = device_mac
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "You must pass the device mac!"
            self.common_validation.fault(**kwargs)
            return -1
        if name_stack_template == None:
            kwargs['fail_msg'] = "You must pass the stack template name!"
            self.common_validation.fault(**kwargs)
            return -1

        self.navigator.navigate_to_devices()
        self.refresh_devices_page()

        row = self._find_device_row(device_keys)
        if row:
            self.utils.print_debug("Found device Row: ", self.format_row(row.text))
            assign_template = self.devices_web_elements.get_device_stack_template_click(row)
            if assign_template:
                self.utils.print_info("Click on Template Column button")
                self.auto_actions.click(assign_template)
            else:
                kwargs['fail_msg'] = "Unable to click on Template Column button"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = f"Didn't find the device {device_keys}"
            self.common_validation.fault(**kwargs)
            return -1

        if self.auto_actions.click_reference(self.devices_web_elements.get_create_template_click) == -1:
            kwargs['fail_msg'] = "Unable to click on Create template based on currently selected device button"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.utils.print_info("Click on Create template based on currently selected device button")

        self.utils.wait_till(self.sw_template_web_elements.get_sw_template_name_textfield,
                             timeout=30, delay=5, is_logging_enabled=True)
        self.utils.print_info("Enter the switch Template Name: ", name_stack_template)
        self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                    name_stack_template)
        self.auto_actions.send_enter(self.sw_template_web_elements.get_sw_template_name_textfield())
        sleep(10)
        return 1

    def assign_network_policy_to_switch_mac(self, policy_name, mac, **kwargs):
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

        self.refresh_devices_page()
        self.utils.print_info(f"Select switch row with serial {mac}")
        if not self.select_device(device_mac=mac, skip_refresh=True, skip_navigation=True):
            kwargs['fail_msg'] = f"Switch {mac} is not present in the grid"
            self.common_validation.fault(**kwargs)
            return -1

        if not self._assign_policy_to_switch(policy_name):
            kwargs['fail_msg'] = "Failed to assign policy to switch"
            self.common_validation.fault(**kwargs)
            return -1

        policy_applied = self.get_ap_network_policy(ap_mac=mac)
        if policy_name.upper() == policy_applied.upper():
            kwargs['pass_msg'] = f"Applied network policy:{policy_applied}"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = f"Policy applied:{policy_name} is not matching with policy updated:{policy_applied}"
        self.common_validation.failed(**kwargs)
        return -1

    def update_device_auto_template(self, device_mac, name_stack_template, **kwargs):
        """
        This function will go to Device Update and press create auto template and name the template

        :param device_mac: Mac of device
        :param name_stack_template: Policy template name
        :return: 1 if remain in the Create auto Template ; -1 else
        """

        if self.select_device(device_mac=device_mac) == -1:
            kwargs['fail_msg'] = "Device raw was not selected"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.utils.print_info("Select Device row")

        if self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button) == -1:
            kwargs['fail_msg'] = "Unable to click on device update button"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.utils.print_info("Click on device update button")

        if self.auto_actions.click_reference(self.devices_web_elements.get_create_auto_template_update_device_click) == -1:
            kwargs['fail_msg'] = "Unable to click on Create template button"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.utils.print_info("Click on Create template based on currently selected device button")

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Transmission power value of wifi2 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Channel value of wifi2 interface, by default set to None
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

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

        :param ap_serial: Serial number of AP Ex:11301810220048, by default set to None
        :param ap_name: Ap name Ex: AP1130, by default set to None
        :param ap_mac: Ap mac Ex: F09CE9F89600, by default set to None
        :return: Radio Profile value of wifi2 interface
        """
        self.navigator.navigate_to_manage_tab()
        sleep(5)
        self.refresh_devices_page()

        search_string = [value for value in [ap_serial, ap_mac, ap_name] if value][0]
        self.column_picker_select("WiFi2 Radio Profile")
        wifi2_radio_profile = self.get_device_details(search_string, 'WIFI2 RADIO PROFILE')
        if wifi2_radio_profile:
            return wifi2_radio_profile

    def perform_search_on_devices_table(self, the_value, **kwargs):
        """
        - Enters the search string value into the Search box on the Manage> Devices page.
        - Note: currently, search is only supported for Serial Number, MAC Address, Host Name, or Ip Address.
        - Keyword Usage:
        - ``Perform Search On Devices Table  ${SERIAL}``
        - ``Perform Search On Devices Table  ${HOST_NAME}``
        - ``Perform Search On Devices Table  ${MAC}``
        - ``Perform Search On Devices Table  ${IP_ADDRESS}``

        :param the_value: value to enter in the search box above the Devices table (Serial, MAC Address, or Host Name)
        :return  1 if action was successful, else -1
        """
        search_field = self.devices_web_elements.get_manage_device_search_field()
        if search_field and the_value:
            self.utils.print_info(f"Entering '{the_value}' into search box")
            self.auto_actions.send_keys(search_field, the_value)
            sleep(5)
        else:
            kwargs['fail_msg'] = "Unable to perform search"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def clear_search_on_devices_table(self, **kwargs):
        """
        - Clears the search field on the Manage> Devices page, if it is populated.
        - Keyword Usage:
        - ``Clear Search On Devices Table``

        :return  1 if action was successful, else -1
        """

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
            kwargs['fail_msg'] = "Unable to find search field's clear button"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def verify_network_policy_column_is_not_sortable(self, **kwargs):
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
                kwargs['pass_msg'] = "Network Policy - This column is not sortable"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Verify if the network policy column is not sortable failed"
        self.common_validation.failed(**kwargs)
        return -1

    def get_column_header_tooltip(self, column_name, **kwargs):
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
            kwargs['fail_msg'] = "Attribute error"
            self.common_validation.fault(**kwargs)
            return -1
        except Exception as e:
            self.utils.print_info(f"Element not fond {e}")
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
                        self.utils.print_info("Column Tooltip: ", self.devices_web_elements.get_ui_tool_tip_inner().text)

                        return self.devices_web_elements.get_ui_tool_tip_inner().text
            except AttributeError:
                kwargs['fail_msg'] = "Attribute error"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['fail_msg'] = "Failed to get the column header tooltip"
        self.common_validation.failed(**kwargs)
        return -1

    def check_status_rebooting_cli(self, spawn, device_serial=None, device_mac=None, **kwargs):
        """
        This keyword gets status about the rebooting information from CLI .First will check the update status from the
         XIQ if IQagent loses connectivity during configuration in 10 minutes.
        - Keyword Usage:
        - ``Check status rebooting cli   ${SPAWN}       ${DEVICE_SERIAL}      ${DEVICE_MAC}``

        :param spawn: device spawn
        :param device_serial: serial number(s) of the device(s), by default set to None
        :param device_mac:  device MAC address, by default set to None
        :return: 1 if gets information about rebooting from CLI else -1
        """

        check_status_update = self.check_device_update_status_rollback_reboot(device_serial=device_serial,
                                                                              device_mac=device_mac, duration_retry=600)
        if check_status_update == 1:
            pass
        else:
            kwargs['fail_msg'] = "Time expired"
            self.common_validation.fault(**kwargs)
            return -1
        retry = 0
        while retry <= 10:
            self.cli.send(spawn, "")
            self.utils.print_info(check_status_update)
            if 'Rebooting switch as configuration caused disconnect' in check_status_update:
                kwargs['pass_msg'] = "VOSS : 'CLOUD_AGENT INFO Rebooting switch as configuration caused disconnect"
                self.common_validation.passed(**kwargs)
                return 1
            elif 'Requesting system reboot' in check_status_update:
                kwargs['pass_msg'] = "EXOS : Requesting system reboot"
                self.common_validation.passed(**kwargs)
                return 1
            elif retry == 10:
                kwargs['fail_msg'] = "No rebooting switch information not found or revert/reboot was not selected"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                self.utils.print_info("Retrying")
                retry += 1
        return 1

    def check_device_update_status_rollback_reboot(self, device_serial=None, device_mac=None, duration_retry=300,
                                                   **kwargs):
        """
        - This keyword is used to check the status of the device update in XIQ
        - It will poll the "update status" every 30 seconds
        - Assuming that config push will take a maximum of five minutes

        :param device_serial: device serial number to check the config push status, by default set to None
        :param device_mac: mac of the device, by default set to None
        :param duration_retry: default set to 300 seconds
        :return: 1 if config push success else -1
        """
        retry_count = 0
        while retry_count <= 300:
            device_update_status = self.get_device_updated_status(device_serial=device_serial, device_mac=device_mac)
            if re.search(r'\d+-\d+-\d+', device_update_status):
                self.utils.print_info("Device updated successfully")
                break
            elif device_update_status == "Device Update Failed":
                kwargs['pass_msg'] = "Device Update Failed"
                self.common_validation.passed(**kwargs)
                return 1
            elif retry_count == 300:
                self.select_device(device_serial)
                self.auto_actions.click(self.devices_web_elements.get_update_status_failed_selected_device)
                kwargs['fail_msg'] = "Check the status of the device update in XIQ failed."
                self.common_validation.failed(**kwargs)
                return -1
            sleep(duration_retry / 10)
            retry_count += 30
        return 1

    def get_update_devices_reboot_rollback(self, policy_name, option, device_serial=None, device_mac=None, **kwargs):
        """
        - This Keyword will Update Device Configuration with Reboot/Rollback option if the IQagent loses connectivity with XIQ during configuration
        - Keyword Usage:
        - ``Get update devices reboot rollback   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}``

        :param policy_name: Assign a policy for device
        :param option: Enable/Disable reboot/rollback option in Update Devices
        :param device_serial: serial number(s) of the device(s), by default set to None
        :param device_mac:  device MAC address, by default set to None
        :return: 1 if update configuration is pushed on the device with Reboot/Rollback option
        """

        self.utils.print_info("Navigate to Manage-->Devices")

        def _navigate_to_devices():
            return self.navigator.navigate_to_devices()

        self.utils.wait_till(_navigate_to_devices)

        self.utils.print_info("Check the Device is up")

        if device_serial or device_mac:
            device_status = self.get_device_status(device_serial=device_serial, device_mac=device_mac)
            self.utils.print_info("Result is:", device_status)
            if device_status == 'green' or device_status == 'config audit mismatch':
                self.utils.print_info("Selecting the device")
                self.select_device(device_serial=device_serial, device_mac=device_mac)
            else:
                kwargs['fail_msg'] = "Device is down"
                self.common_validation.fault(**kwargs)
                return -1

        self.utils.print_info("Check if device has policy")
        if self.devices_web_elements.get_assign_policy_device_selected():
            self.utils.print_info("Click on Assign Policy")
            self.auto_actions.click_reference(self.devices_web_elements.get_assign_policy_device_selected)
            self.utils.print_info("Selecting '{}' policy".format(policy_name))
            self.utils.print_info("Click on network policy drop down")
            sleep(5)
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_drop_down)
            sleep(5)
            network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
            # self.auto_actions.scroll_down()
            sleep(5)
            if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                self.utils.print_info("Selected Network policy from drop down:{}".format(policy_name))
                sleep(2)
            else:
                kwargs['fail_msg'] = "Network policy is not present in drop down"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Click on network policy assign button")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_button)
            sleep(5)
            if device_serial:
                self.select_device(device_serial=device_serial)
            if device_mac:
                self.select_device(device_mac=device_mac)
        else:
            self.utils.print_info("Device has already a policy")
            pass

        sleep(5)
        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)
        self.auto_actions.move_to_element(self.devices_web_elements.get_update_device_button())
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
            kwargs['fail_msg'] = "Network policy and configuration checkbox not found"
            self.common_validation.fault(**kwargs)
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
            kwargs['fail_msg'] = "Reboot and revert switch configuration checkbox not found"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Click on perform update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_switch_update_btn)
        sleep(3)
        if option.lower() == "enable":
            self.utils.print_info("Proceed yes that user wants to continue with reboot/revert option")
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_update_yes_btn)
            sleep(2)
        else:
            pass
        return 1

    def get_check_update_failed_after_reboot(self, device_serial=None, device_mac=None, **kwargs):
        """
        This keyword gets information of the update failed status in XIQ for a device after reboot/rollback configuration
        - Keyword Usage:
        - ``Get check update failed after reboot   ${DEVICE_SERIAL} ``
        - ``Get check update failed after reboot   ${DEVICE_MAC} ``

        :param device_serial: Gets the information of the update failed status based on serial number, by default set to None
        :param device_mac:  Gets the information of the update failed status based on address MAC, by default set to None
        :return: 1 if the information was found else -1
        """

        self.select_device(device_serial=device_serial, device_mac=device_mac)
        self.utils.print_info("Checking the update the status")
        sleep(5)
        status = self.devices_web_elements.get_status_update_failed_after_reboot()
        if status != None and "The device was rebooted and reverted to previous configuration" in status:
            self.utils.print_info("Update status: ", status)
        else:
            kwargs['fail_msg'] = "Update status not found"
            self.common_validation.failed(**kwargs)
            return -1
        return 1

    def check_pop_up_message_reboot_revert(self, policy_name, option, device_serial=None, device_mac=None, **kwargs):
        """
        - This Keyword will check the Reboot/Rollback option in Update Device Configuration has a pop-up message
        - Keyword Usage:
        - ``Check pop up message reboot revert   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}``

        :param policy_name: Assign a policy for device
        :param option: Enable/Disable reboot/rollback option in Update Devices
        :param device_serial: serial number(s) of the device(s), by default set to None
        :param device_mac:  device MAC address, by default set to None
        :return: 1 if the pop-up message has been found else -1
        """
        self.navigator.navigate_to_devices()
        self.utils.print_info("Check the Device is up")
        if device_serial or device_mac:
            device_status = self.get_device_status(device_serial=device_serial, device_mac=device_mac)

        self.utils.print_info("Result is:", device_status)
        if device_status == 'green' or device_status == 'config audit mismatch':
            self.utils.print_info("Select the device")
            if device_serial or device_mac:
                self.select_device(device_serial=device_serial, device_mac=device_mac)
        else:
            kwargs['fail_msg'] = "Device is down"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Check if device has policy")
        if self.devices_web_elements.get_assign_policy_device_selected():
            self.utils.print_info("Click on Assign Policy")
            self.auto_actions.click_reference(self.devices_web_elements.get_assign_policy_device_selected)
            self.utils.print_info("Selecting '{}' policy".format(policy_name))
            self.utils.print_info("Click on network policy drop down")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_drop_down)
            network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
            self.auto_actions.scroll_down()
            sleep(5)
            if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                self.utils.print_info("Selected Network policy from drop down:{}".format(policy_name))
                sleep(2)
            else:
                kwargs['fail_msg'] = "Network policy is not present in drop down"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Click on network policy assign button")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_button)
            sleep(5)
            self.select_device(device_serial=device_serial)
        else:
            self.utils.print_info("Device has already a policy")
            pass

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

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
            kwargs['fail_msg'] = "Network policy and configuration checkbox not found"
            self.common_validation.fault(**kwargs)
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
            kwargs['fail_msg'] = "Reboot and revert switch configuration checkbox not found"
            self.common_validation.fault(**kwargs)
            return -1

        pop_up_message = self.devices_web_elements.get_check_pop_message()
        pop_up_message_text = pop_up_message.text()

        if pop_up_message_text != None and "Not supported on Dell/SR" in pop_up_message_text:
            self.utils.print_info("", pop_up_message_text)
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_cancel_button)
            kwargs['pass_msg'] = "Pop-up message has been found"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_cancel_button)
            kwargs['fail_msg'] = "Pop-up message didn't find"
            self.common_validation.failed(**kwargs)
            return -1

    def check_double_verification_display_rollback(self, policy_name, option, device_serial=None, device_mac=None,
                                                   **kwargs):
        """
        - This Keyword will check the double verification is displayed for the Reboot/Rollback option in Update Device Configuration
        - Keyword Usage:
        - ``Check pop up message reboot revert   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}``

        :param policy_name: Assign a policy for device
        :param option: Enable/Disable reboot/rollback option in Update Devices
        :param device_serial: serial number(s) of the device(s), by default set to None
        :param device_mac:  device MAC address, by default set to None
        :return: 1 if the double verification is displayed else -1
        """

        self.navigator.navigate_to_devices()
        self.utils.print_info("Check the Device is up")
        if device_serial or device_mac:
            device_status = self.get_device_status(device_serial=device_serial, device_mac=device_mac)

        self.utils.print_info("Result is:", device_status)
        if device_status == 'green' or device_status == 'config audit mismatch':
            self.utils.print_info("Select the device")
            if device_serial or device_mac:
                self.select_device(device_serial=device_serial, device_mac=device_mac)
        else:
            kwargs['fail_msg'] = "Device is down"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Check if device has policy")
        if self.devices_web_elements.get_assign_policy_device_selected():
            self.utils.print_info("Click on Assign Policy")
            self.auto_actions.click_reference(self.devices_web_elements.get_assign_policy_device_selected)
            self.utils.print_info("Selecting '{}' policy".format(policy_name))
            self.utils.print_info("Click on network policy drop down")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_assign_network_policy_drop_down)
            network_policy_items = self.devices_web_elements.get_actions_network_policy_drop_down_items()
            self.auto_actions.scroll_down()
            sleep(5)
            if self.auto_actions.select_drop_down_options(network_policy_items, policy_name):
                self.utils.print_info("Selected Network policy from drop down:{}".format(policy_name))
                sleep(2)
            else:
                kwargs['fail_msg'] = "Network policy is not present in drop down"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Click on network policy assign button")
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_button)
            sleep(5)
            self.select_device(device_serial=device_serial)
        else:
            self.utils.print_info("Device has already a policy")
            pass

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

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
            kwargs['fail_msg'] = "Network policy and configuration checkbox not found"
            self.common_validation.fault(**kwargs)
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
            kwargs['fail_msg'] = "Reboot and revert switch configuration checkbox not found"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Click on perform update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_switch_update_btn)
        sleep(3)

        double_verification = self.devices_web_elements.get_check_double_verification_display_rollback()

        if double_verification:
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_update_no_btn)
            self.auto_actions.click_reference(self.devices_web_elements.get_actions_network_policy_assign_cancel_button)
            kwargs['pass_msg'] = "Displayed double verification"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Double verification doesn't appear"
            self.common_validation.failed(**kwargs)
            return -1

    def change_device_onboarding_date(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, days, serial_number, owner_id,
                                      sw_connection_host, **kwargs):
        """
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
        """
        pattern1 = "(\\w+)."
        rdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        if spawn == -1:
            kwargs['fail_msg'] = "Couldn't open the spawn connection"
            self.common_validation.fault(**kwargs)
            return -1
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            kwargs['fail_msg'] = "No such file or directory"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if "ahqa_id_rsa" not in output_cmd_ls:
            # self.robot_built_in.skip('No ssh certificate exist on jump station')
            kwargs['fail_msg'] = "NO shh certificate"
            self.common_validation.fault(**kwargs)
            return -1

        output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc[0]))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlconfigdb_1")
        output_cmd3 = self.cli.send_pxssh(spawn, "select created_at,updated_at,agent_id,owner_id from hm_device where owner_id={};".format(owner_id))
        output_cmd4 = ''
        if isinstance(serial_number, list) and isinstance(days, list):
            cnt = 0
            for el in serial_number:
                output_cmd4 = output_cmd4 + self.cli.send_pxssh(spawn,
                                                                "update hm_device set created_at = DATE_TRUNC('DAY', "
                                                                "NOW() - INTERVAL '{} DAY'),"
                                                                "updated_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY')"
                                                                "where serial_number = '{}' and owner_id = {};".format(
                                                                    days[cnt], days[cnt], el, owner_id))
                cnt = cnt + 1
        else:
            output_cmd4 = self.cli.send_pxssh(spawn,
                                              "update hm_device set created_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY'),"
                                              "updated_at = DATE_TRUNC('DAY', NOW() - INTERVAL '{} DAY')"
                                              "where serial_number = '{}' and owner_id = {};".format(days, days,
                                                                                                     serial_number,
                                                                                                     owner_id))
        output_cmd5 = self.cli.send_pxssh(spawn,
                                          "select created_at,updated_at,agent_id,"
                                          "owner_id from hm_device where owner_id={};".format(owner_id))

        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)
        self.utils.print_info(output_cmd4)
        self.utils.print_info(output_cmd5)
        self.cli.close_spawn(spawn)
        return 1

    def max_device_num_from_hm_vhm_account_table(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, vhm_id,
                                                 sw_connection_host, **kwargs):
        """
        This function returns the number of devices which can be onboarded
        To use this function you need to have access to RDC database

        :param ip_dest_ssh: ip of 'Jump station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param vhm_id: VHM Id for XIQ account
        :param rdc: RDC name : e.g w1r1 , g2r1
        :return: number of devices which can be onboarded  ; else -1
        """

        pattern1 = "(\\w+)."
        rdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            kwargs['fail_msg'] = "No such file or directory"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if "ahqa_id_rsa" not in output_cmd_ls:
            # self.robot_built_in.skip('No ssh certificate exist on jump station')
            kwargs['fail_msg'] = "No ssh certificate"
            self.common_validation.fault(**kwargs)
            return -1
        output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc[0]))
        self.utils.print_info(output_cmd)
        # output_cmd1 = self.cli.send_pxssh(spawn, "yes")
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlsystemdb")
        output_cmd3 = self.cli.send_pxssh(spawn,
                                          "select id, customer_id, customer_mode, managed_device_num,max_device_num,"
                                          "vhm_id from hm_vhm_account where vhm_id ='{}';".format(vhm_id))
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

    def check_update_time_on_rdc(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, sw_connection_host, **kwargs):
        """
        This function returns the update time interval for RDC

        :param ip_dest_ssh: ip of 'bastion station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param sw_connection_host: The RDC DNS
        :return: interval time and interval unit ; else -1
        """
        pattern1 = "(\\w+)."
        rdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)

        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            kwargs['fail_msg'] = "No such file or directory"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if "ahqa_id_rsa" not in output_cmd_ls:
            kwargs['fail_msg'] = "No ssh certificate"
            self.common_validation.fault(**kwargs)
            return -1
        output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlscheduledb")
        output_cmd3 = self.cli.send_pxssh(spawn,
                                          "select id,interval,interval_unit from hm_job_trigger where id in "
                                          "(select job_trigger_id from hm_job where name = 'validate Gemalto "
                                          "license for Cloud task');")

        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)

        pattern1 = "\\d+\\s+\\|\\s+(\\d+)\\s+\\|\\s+\\w+"
        pattern2 = "\\d+\\s+\\|\\s+\\d+\\s+\\|\\s+(\\w+)"
        update_time = self.utils.get_regexp_matches(output_cmd3, pattern1, 1)
        update_unit = self.utils.get_regexp_matches(output_cmd3, pattern2, 1)
        self.utils.print_info(update_time[0])
        self.utils.print_info(update_unit[0])
        self.cli.close_spawn(spawn)
        if update_time[0] and update_unit[0]:
            return update_time[0], update_unit[0]
        else:
            kwargs['fail_msg'] = "Interval time was not found"
            self.common_validation.fault(**kwargs)
            return -1

    def get_banner_messages(self, expected_message, **kwargs):
        """
        This function compares a message from banner with expected_message

        :param expected_message:
        :return: 1 if expected message was found in banner ; else -1
        """

        all_error_messages = self.devices_web_elements.get_all_messages_banner()
        self.utils.print_info(all_error_messages)
        if all_error_messages:
            for el2 in all_error_messages:
                self.utils.print_info("Messages from banner are : ", el2.text)
        else:
            kwargs['fail_msg'] = f"No message was found: {expected_message}"
            self.common_validation.failed(**kwargs)
            return -1
        for el in all_error_messages:
            if str(expected_message) in el.text:
                self.utils.print_info("Message found")
                self.screen.save_screen_shot()
                return 1
            else:
                pass

        kwargs['fail_msg'] = f"No message was found: {expected_message}"
        self.common_validation.failed(**kwargs)
        return -1

    def move_to_free_pilot_from_trial_or_connect(self, **kwargs):
        """
        This function moves XIQ account into free pilot mode by using the link from banner

        :return: 1 if account was moved ; else -1
        """

        update_button = self.devices_web_elements.get_upgrade_to_free_pilot_link()
        if update_button:
            self.utils.print_info("Upgrade ... ")
            self.auto_actions.click(update_button)
            yes_button = self.devices_web_elements.get_yes_button_upgrade_to_free_pilot()
            if yes_button:
                self.utils.print_info("press yes ... ")
                self.auto_actions.click(yes_button)
            else:
                kwargs['fail_msg'] = "Yes button not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Upgrade button not found"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def activate_device_license(self, device_serial, license_type, username=None, password=None, shared_cuid=None,
                                warning_msg=None, skip_warning_check=False, **kwargs):
        """
        This function activate premier or macsec license on a device

        :param device_serial: Serial of device
        :param license_type: premier or macsec
        :param username: username, by default set to None
        :param password: password, by default set to None
        :param shared_cuid: shared cuid, by default set to None
        :param warning_msg: warning message, by default set to None
        :param skip_warning_check: flag, by default set to False
        :return: 1 if license was activated ; else -1
        """

        select_flag = False
        device_serial = device_serial.split(',')

        self.navigator.enable_page_size()
        for el in device_serial:
            if el == device_serial[0]:
                self.select_device(el)
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True
            else:
                self.select_device(device_serial=el, skip_refresh=True, skip_navigation=True)
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
            sleep(2)

        self.utils.print_info("Select Manage Device License ")
        manage_license = self.device_actions.get_device_actions_manage_license()
        self.utils.print_info(manage_license)
        if manage_license:
            self.utils.print_info("Select Manage Device License ")
            self.auto_actions.move_to_element(manage_license)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Manage Device License not found"
            self.common_validation.fault(**kwargs)
            return -1

        premier_button = self.device_actions.get_activate_license()
        if premier_button:
            self.utils.print_info("Activate license")
            self.auto_actions.move_to_element(premier_button)
        else:
            kwargs['fail_msg'] = "Button not found"
            self.common_validation.fault(**kwargs)
            return -1

        if license_type == 'premier' or license_type == 'PREMIER':
            premier_act_button = self.device_actions.get_act_premier_btn()
            self.utils.print_info(premier_act_button)
            if premier_act_button:
                self.utils.print_info("Press Premier button")
                self.auto_actions.click(premier_act_button)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif license_type == 'macsec' or license_type == 'MACSEC':
            macsec_button = self.device_actions.get_act_macsec_btn()
            if macsec_button:
                self.utils.print_info("Press Macsec license")
                self.auto_actions.click(macsec_button)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif license_type == 'FOURPORT10G':
            act_10g_4p_btn = self.device_actions.get_act_10g_4p_btn()
            if act_10g_4p_btn:
                self.utils.print_info("Press 10G 4P license")
                self.auto_actions.click(act_10g_4p_btn)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif license_type == 'EIGHTPORT10G':
            act_10g_8p_btn = self.device_actions.get_act_10g_8p_btn()
            if act_10g_8p_btn:
                self.utils.print_info("Press 10G 8P license")
                self.auto_actions.click(act_10g_8p_btn)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "Activate the device license failed."
            self.common_validation.failed(**kwargs)
            return -1
        sleep(3)
        yes_confirmation = self.device_actions.get_yes_confirmation()
        if yes_confirmation:
            self.utils.print_info("yes confirmation button was found ")
            self.auto_actions.click(yes_confirmation)
            sleep(4)
            if license_type == 'FOURPORT10G' or license_type == 'EIGHTPORT10G':
                if skip_warning_check:
                    confirm_msg_yes = self.device_actions.get_confirm_msg_yes()
                    if confirm_msg_yes:
                        self.utils.print_info("confirm_msg_yes button was found")
                        self.auto_actions.click(confirm_msg_yes)
                        return 1
                    else:
                        self.utils.print_info("confirm_msg_yes button not found")
                else:
                    pass
                if warning_msg:
                    warning_xiq_text = self.device_actions.get_warning_xiq_text()
                    if warning_xiq_text:
                        self.utils.print_info("Expected message is  :", warning_msg)
                        self.utils.print_info("Message from XIQ is :", warning_xiq_text.text)
                        if warning_msg in warning_xiq_text.text:
                            self.utils.print_info("Message match")
                            confirm_msg_yes = self.device_actions.get_confirm_msg_yes()
                            if confirm_msg_yes:
                                self.utils.print_info("confirm_msg_yes button was found")
                                self.auto_actions.click(confirm_msg_yes)
                                return 1
                            else:
                                kwargs['fail_msg'] = "Confirm_msg_yes button not found"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "Message doesn't match"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Warning message was not found."
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    warning_xiq_text = self.device_actions.get_warning_xiq_text()
                    if warning_xiq_text:
                        self.utils.print_info("Warning message is displayed. Warning message should not be displayed .")
                        confirm_msg_yes = self.device_actions.get_confirm_msg_yes()
                        if confirm_msg_yes:
                            self.utils.print_info("confirm_msg_yes button was found")
                            self.auto_actions.click(confirm_msg_yes)
                        else:
                            kwargs['fail_msg'] = "Confirm_msg_yes button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                        kwargs['fail_msg'] = "Activate the device license failed."
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                pass
            sleep(20)
            check_portal_page = self.devices_web_elements.get_check_portal_page()
            if check_portal_page:
                if self.login_to_extreme_portal(username, password, shared_cuid) == 1:
                    self.utils.print_info("Login to extreme portal")
                    return 1
                else:
                    kwargs['fail_msg'] = "Failed to login to extreme portal"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                self.utils.print_info("Login to extreme portal page was not displayed ")
        else:
            kwargs['fail_msg'] = "Yes confirmation button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def revoke_device_license(self, device_serial, license_type, username=None, password=None, shared_cuid=None,
                              warning_msg=None, skip_warning_check=False, **kwargs):
        """
        This function revoke premier or macsec license on a device

        :param device_serial: Serial of device
        :param license_type: premier or macsec
        :param username: username, by default set to None
        :param password: password, by default set to None
        :param shared_cuid: shared cuid, by default set to None
        :param warning_msg: warning message, by default set to None
        :param skip_warning_check: flag, by default set to False
        :return: 1 if license was revoked ; else -1
        """

        select_flag = False
        device_serial = device_serial.split(',')

        self.navigator.enable_page_size()
        for el in device_serial:
            if el == device_serial[0]:
                self.select_device(el)
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True
            else:
                self.select_device(el, skip_refresh=True, skip_navigation=True)
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
            sleep(2)

        manage_license = self.device_actions.get_device_actions_manage_license()
        if manage_license:
            self.utils.print_info("Select Manage Device License ")
            self.auto_actions.move_to_element(manage_license)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Manage Device License not found"
            self.common_validation.fault(**kwargs)
            return -1

        premier_button = self.device_actions.get_revoke_license()
        if premier_button:
            self.utils.print_info("Revoke license")
            self.auto_actions.move_to_element(premier_button)
        else:
            kwargs['fail_msg'] = "Button not found"
            self.common_validation.fault(**kwargs)
            return -1
        if license_type == 'premier' or license_type == 'PREMIER':
            premier_rev_button = self.device_actions.get_rev_premier_btn()
            if premier_rev_button:
                self.utils.print_info("Press Premier button")
                self.auto_actions.click(premier_rev_button)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif license_type == 'macsec' or license_type == 'MACSEC':
            macsec_button = self.device_actions.get_rev_macsec_btn()
            if macsec_button:
                self.utils.print_info("Press Macsec license")
                self.auto_actions.click(macsec_button)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1
        elif license_type == 'FOURPORT10G':
            rev_10g_4p_btn = self.device_actions.get_rev_10g_4p_btn()
            if rev_10g_4p_btn:
                self.utils.print_info("Press 10G 4P license")
                self.auto_actions.click(rev_10g_4p_btn)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1

        elif license_type == 'EIGHTPORT10G':
            rev_10g_8p_btn = self.device_actions.get_rev_10g_8p_btn()
            if rev_10g_8p_btn:
                self.utils.print_info("Press 10G 8P license")
                self.auto_actions.click(rev_10g_8p_btn)
            else:
                kwargs['fail_msg'] = "Button not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Revoke the device license failed."
            self.common_validation.failed(**kwargs)
            return -1
        sleep(3)
        yes_confirmation = self.device_actions.get_yes_confirmation()
        if yes_confirmation:
            self.utils.print_info("yes confirmation button was found ")
            self.auto_actions.click(yes_confirmation)
            sleep(4)
            if license_type == 'FOURPORT10G' or license_type == 'EIGHTPORT10G':
                if skip_warning_check:
                    confirm_msg_yes = self.device_actions.get_confirm_msg_yes()
                    if confirm_msg_yes:
                        self.utils.print_info("confirm_msg_yes button was found")
                        self.auto_actions.click(confirm_msg_yes)
                        return 1
                    else:
                        self.utils.print_info("confirm_msg_yes button not found")
                else:
                    pass

                if warning_msg:
                    warning_xiq_text = self.device_actions.get_warning_rvk_xiq_text()
                    if warning_xiq_text:
                        self.utils.print_info("Message is  :", warning_msg)
                        self.utils.print_info("Message is XIQ :", warning_xiq_text.text)
                        if warning_msg in warning_xiq_text.text:
                            self.utils.print_info("Message match")
                            confirm_msg_yes = self.device_actions.get_confirm_msg_yes()
                            if confirm_msg_yes:
                                self.utils.print_info("confirm_msg_yes button was found")
                                self.auto_actions.click(confirm_msg_yes)
                                self.utils.print_info("Return 1")
                                self.screen.save_screen_shot()
                                return 1
                            else:
                                kwargs['fail_msg'] = "Confirm_msg_yes button not found"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "Message doesn't match"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Warning message was not found."
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    warning_xiq_text = self.device_actions.get_warning_rvk_xiq_text()
                    if warning_xiq_text:
                        kwargs['fail_msg'] = "Warning message is displayed. " \
                                             "The revocation warning should not be displayed"
                        self.common_validation.fault(**kwargs)
                        return -1
                    else:
                        pass
            else:
                pass
            sleep(20)
            check_portal_page = self.devices_web_elements.get_check_portal_page()
            if check_portal_page:
                if self.login_to_extreme_portal(username, password, shared_cuid) == 1:
                    self.utils.print_info("Login to extreme portal")
                    return 1
                else:
                    kwargs['fail_msg'] = "Failed to login to extreme portal"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                pass
        else:
            kwargs['fail_msg'] = "Yes confirmation button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def check_license_status(self, device_sn, max_time=180, time_interval=10, **kwargs):
        """
        - This keyword is used to check the status of the device license
        - It will poll the "license status" at every time_interval seconds

        :param device_sn: Device serial
        :param max_time: Maximum duration of check
        :param time_interval: Time interval between two consecutive checks
        :return: returns the status displayed into device license field (NONE; PREMIER; MACSEC; FOURPORT10G;EIGHTPORT10G) + error message if it is present ;else -1
        """
        self.utils.print_info("Start checking the status for device license")
        sleep(20)
        retry_count = 0
        error = None
        error_before = None
        options_list = ['PREMIER', 'MACSEC', 'FOURPORT10G', 'EIGHTPORT10G', 'None']
        check_list_before = [None] * 5
        check_list = [None] * 5
        flag_try_again = False
        list_return = []
        while retry_count <= max_time or flag_try_again:
            flag_try_again = False
            rows = self.devices_web_elements.get_grid_rows()
            if rows:
                for row in rows:
                    if device_sn in row.text:
                        license_form_error = self.devices_web_elements.get_license_form_error(row)
                        if license_form_error:
                            if isinstance(license_form_error.get_attribute("title"), str):
                                error = ' ' + license_form_error.get_attribute("title")
                                self.utils.print_info("ERROR FOUND:", error)
                            else:
                                error = None
                        else:
                            self.utils.print_info("ERROR not FOUND")
                        field_license_stat = self.devices_web_elements.get_field_license_stat(row)
                        if field_license_stat:
                            if '%' in field_license_stat.text:
                                self.utils.print_info("Still loading. Will try again ")
                                check_list_before = [None] * 5
                                error_before = None
                            else:
                                field_license_stat_list = field_license_stat.text.split(',')
                                self.utils.print_info("License status is :", field_license_stat_list)
                                for el in field_license_stat_list:
                                    if el in options_list:
                                        self.utils.print_info("{} is valid value".format(el))
                                    else:
                                        kwargs['fail_msg'] = "Check the license status failed."
                                        self.common_validation.failed(**kwargs)
                                        return -1
                                cnt = 0
                                for lic in options_list:
                                    if lic in field_license_stat.text:
                                        check_list[cnt] = lic
                                    else:
                                        pass
                                    cnt = cnt + 1
                                self.utils.print_info("Current status for license field : ", check_list)
                        else:
                            kwargs['fail_msg'] = "License field status not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                        if error:
                            if error_before == error:
                                pass
                            else:
                                error_before = error
                                flag_try_again = True
                        else:
                            pass
                        if not check_list == [None] * 5:
                            if check_list_before == check_list:
                                first_el = True
                                for el in check_list:
                                    if el:
                                        if first_el:
                                            list_return = el
                                            first_el = False
                                        else:
                                            list_return = list_return + "," + el
                                    else:
                                        pass
                                if error:
                                    if error_before == error and flag_try_again == False:
                                        self.utils.print_info("Return :", list_return + error)
                                        self.screen.save_screen_shot()
                                        return list_return + error
                                    else:
                                        pass
                                else:
                                    self.utils.print_info("Return :", list_return)
                                    self.utils.print_info("Return type :", type(list_return))
                                    self.screen.save_screen_shot()
                                    return list_return
                            else:
                                check_list_before = check_list.copy()
                                flag_try_again = True
                        else:
                            check_list_before = check_list.copy()
                        if flag_try_again:
                            self.utils.print_info(
                                "Will try again to confirm the result: {} and Error : {}".format(check_list, error))
                        check_list = [None] * 5
                        error = None
                    else:
                        pass
                self.refresh_devices_page()
                self.utils.print_info(f"Time elapsed for license update: {retry_count} seconds")
                retry_count += time_interval
            else:
                kwargs['fail_msg'] = "No row found"
                self.common_validation.fault(**kwargs)
                return -1

        kwargs['fail_msg'] = "Check the license status failed."
        self.common_validation.failed(**kwargs)
        return -1

    def pilot_lic_inventory_from_unmanage_box(self, max_time=120, interval_time=20, **kwargs):
        """
        This function returns the number of license which should be consumed and the number of license available from
        unmanage box. These are displayed into this format   e.g.  1/0

        :param max_time: Maximum duration of check
        :param interval_time: Time interval between two consecutive checks
        :return: the number of license which should be consumed and the number of license available from unmanage box. These are displayed into this format   e.g.  1/0  ; else -1
        """

        pilot_inventory_found = False
        cnt = 0
        self.screen.save_screen_shot()
        while cnt < max_time:
            check_unmanage_box = self.devices_web_elements.get_check_unmanage_box()
            self.utils.print_info(check_unmanage_box)
            if check_unmanage_box:
                pilot_lic_inventory = self.devices_web_elements.get_pilot_lic_inventory()
                if pilot_lic_inventory:
                    for el in pilot_lic_inventory:
                        if 'Pilot' in el.text:
                            if '/' in el.text:
                                pilot_inventory_found = el.text
                                break
                            else:
                                pass
                        else:
                            self.utils.print_info(el.text)
                else:
                    self.utils.print_info("The inventory box not found  ")
            else:
                self.utils.print_info("The unmanage box not found  ")
            sleep(interval_time)
            cnt = cnt + interval_time
            self.utils.print_info("Time", cnt)
            if pilot_inventory_found:
                break
            else:
                pass
        self.screen.save_screen_shot()
        if pilot_inventory_found:
            self.utils.print_info("The unmanage box was found: ", pilot_inventory_found)
            return pilot_inventory_found
        else:
            kwargs['fail_msg'] = f"The unmanage box not found {pilot_inventory_found}"
            self.common_validation.failed(**kwargs)
            return -1

    def check_serial_list(self, serial, **kwargs):
        """
        This function checks if a device or more need a Pilot License in next 15 days. The list from banner is cheked

        :param serial: a serial or more
        :return: 1 if the SN or SNs are into serial list from banner ; else -1
        """

        serial_list = serial.split(",")
        self.utils.print_info(len(serial_list))
        self.screen.save_screen_shot()
        sn_button = self.devices_web_elements.get_sn_button()
        if sn_button:
            self.utils.print_info("Sn button was found ")
            self.auto_actions.click(sn_button)
        else:
            kwargs['fail_msg'] = "Sn button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(3)
        self.screen.save_screen_shot()
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
                            kwargs['fail_msg'] = f"The serial {serial_list[cnt2]} was found twice"
                            self.common_validation.fault(**kwargs)
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
                            kwargs['fail_msg'] = f"The serial {serial} was found twice"
                            self.common_validation.fault(**kwargs)
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
                        kwargs['fail_msg'] = "Close button was not found"
                        self.common_validation.fault(**kwargs)
                        return -1
                    return 1
                else:
                    kwargs['fail_msg'] = f"The serial {serial} was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            kwargs['fail_msg'] = "The list is empty or it was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sn_close = self.devices_web_elements.get_sn_close()
        if sn_close:
            self.utils.print_info("Close button was found")
            self.auto_actions.click(sn_close)
        else:
            kwargs['fail_msg'] = "Close button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def link_to_sfdc_from_unmanage_box(self, username, password, shared_cuid=None, **kwargs):
        """
        This function links the XIQ account to SFDC by using the 'ADD LICENSE' button from unmanage dialog

        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid, by default set to None
        :return: 1 if account was linked ; else -1
        """
        self.screen.save_screen_shot()
        add_a_license = self.devices_web_elements.get_add_a_license()
        if add_a_license:
            self.utils.print_info("ADD a license button was found ")
            self.auto_actions.click(add_a_license)
        else:
            kwargs['fail_msg'] = "ADD a license button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        sleep(2)
        get_link_my_account = self.devices_web_elements.get_link_my_account()
        if get_link_my_account:
            self.utils.print_info("'Link my extreme portal' button was found ")
            self.auto_actions.click(get_link_my_account)
        else:
            kwargs['fail_msg'] = "'Link my extreme portal' button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        sleep(2)
        get_link_my_account_agree = self.devices_web_elements.get_link_my_account_agree()
        if get_link_my_account_agree:
            self.utils.print_info(" Checkbox Agree was found ")
            self.auto_actions.click(get_link_my_account_agree)
        else:
            kwargs['fail_msg'] = "Checkbox Agree was not found"
            self.common_validation.fault(**kwargs)
            return -1

        link_my_account_continue = self.devices_web_elements.get_link_my_account_continue()
        if link_my_account_continue:
            self.utils.print_info("Continue button was found ")
            self.auto_actions.click(link_my_account_continue)
        else:
            kwargs['fail_msg'] = "Continue  button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(10)
        return self.login_to_extreme_portal(username, password, shared_cuid)

    def move_to_pilot_mode_from_unmanage_box(self, **kwargs):
        """
        This function move the XIQ account from free pilot or trial mode into pilot mode by using the 'ADD LICENSE'
        button from unmanage dialog
        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid
        :return: 1 if account was moved into Pilot mode  ; else -1
        """
        self.screen.save_screen_shot()
        add_a_license = self.devices_web_elements.get_add_a_license()
        if add_a_license:
            self.utils.print_info("ADD a license button was found ")
            self.auto_actions.click(add_a_license)
        else:
            kwargs['fail_msg'] = "ADD a license button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        self.screen.save_screen_shot()
        upgrade_account_to_pilot = self.devices_web_elements.get_upgrade_account_to_pilot()
        if upgrade_account_to_pilot:
            self.utils.print_info("'UPGRADE ACCOUNT' button was found")
            self.auto_actions.click(upgrade_account_to_pilot)
        else:
            kwargs['fail_msg'] = "'UPGRADE ACCOUNT' button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        self.screen.save_screen_shot()
        get_link_my_account_agree = self.devices_web_elements.get_link_my_account_agree()
        if get_link_my_account_agree:
            self.utils.print_info("Checkbox Agree was found")
            self.auto_actions.click(get_link_my_account_agree)
        else:
            kwargs['fail_msg'] = "Checkbox Agree was not found"
            self.common_validation.fault(**kwargs)
            return -1
        self.screen.save_screen_shot()
        link_my_account_continue = self.devices_web_elements.get_link_my_account_continue()
        if link_my_account_continue:
            self.utils.print_info("Continue button was found")
            self.auto_actions.click(link_my_account_continue)
        else:
            kwargs['fail_msg'] = "Continue button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(10)
        return 1

    def check_upgrade_account_button(self, **kwargs):
        """
        This function presses the upgrade account button

        :return: 1 if account button was pressed  ; else -1
        """
        self.screen.save_screen_shot()
        upgrade_account_to_pilot = self.devices_web_elements.get_upgrade_account_to_pilot()
        if upgrade_account_to_pilot:
            self.utils.print_info("'UPGRADE ACCOUNT' button was found ")
            self.auto_actions.click(upgrade_account_to_pilot)
        else:
            kwargs['fail_msg'] = "'UPGRADE ACCOUNT' button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "'UPGRADE ACCOUNT' button was found"
        self.common_validation.passed(**kwargs)
        return 1

    def login_to_extreme_portal(self, username, password, shared_cuid=None, **kwargs):
        """
        This function enters the credentials when SFDC page is displayed

        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid, by default set to None
        :return: 1 if the credentials were entered ; else -1
        """

        sfdc_username = self.devices_web_elements.get_sfdc_username()
        if sfdc_username:
            self.utils.print_info("Entering Salesforce username")
            self.auto_actions.send_keys(sfdc_username, username)
            sleep(2)
            self.screen.save_screen_shot()
        else:
            kwargs['fail_msg'] = "Entering Salesforce page was not found"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Entering Salesforce password")
        self.auto_actions.send_keys(self.devices_web_elements.get_sfdc_password(), password)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Submitting")
        self.auto_actions.click_reference(self.devices_web_elements.get_sfdc_submit)
        sleep(2)
        self.screen.save_screen_shot()

        sfdc_submit_check_error = self.devices_web_elements.get_sfdc_submit_check_error()
        if sfdc_submit_check_error:
            kwargs['fail_msg'] = f"The below error was displayed {sfdc_submit_check_error.text}"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            pass

        sleep(20)
        self.screen.save_screen_shot()
        enter_shared_cuid = self.devices_web_elements.get_enter_shared_cuid()
        if enter_shared_cuid:
            self.auto_actions.send_keys(enter_shared_cuid, shared_cuid)
            submit_shared_cuid = self.devices_web_elements.get_submit_shared_cuid()
            if submit_shared_cuid:
                self.utils.print_info("submit button was found")
                self.auto_actions.click(submit_shared_cuid)
            else:
                kwargs['fail_msg'] = "Submit button not found"
                self.common_validation.fault(**kwargs)
                return -1
            self.screen.save_screen_shot()
            check_error_shared_cuid = self.devices_web_elements.get_check_error_shared_cuid()
            if check_error_shared_cuid:
                kwargs['fail_msg'] = f"The below error was displayed when enter " \
                                     f"shared CUID {check_error_shared_cuid.text}"
                self.common_validation.fault(**kwargs)
                return -1
            else:
                return 1
        else:
            self.utils.print_info("shared cuid dialog is not displayed ")
            self.screen.save_screen_shot()
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
                        kwargs['fail_msg'] = "Submit button not found"
                        self.common_validation.fault(**kwargs)
                        return -1
                    check_error_shared_cuid = self.devices_web_elements.get_check_error_shared_cuid()
                    if check_error_shared_cuid:
                        kwargs['fail_msg'] = f"The below error was displayed when enter " \
                                             f"shared CUID {check_error_shared_cuid.text}"
                        self.common_validation.fault(**kwargs)
                        return -1
                    else:
                        return 1
                else:
                    pass
            else:
                pass
        return 1

    def check_unlink_button(self, **kwargs):
        """
        This function checks if the unlink button is present

        :return: 1 if unlink button is present ; else -1
        """
        self.screen.save_screen_shot()
        sfdc_unlink = self.devices_web_elements.get_sfdc_unlink()
        if sfdc_unlink:
            kwargs['pass_msg'] = "Unlink button is present"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unlink button is not present"
            self.common_validation.failed(**kwargs)
            return -1

    def unlink_sfdc_account(self, **kwargs):
        """
        This function presses the unlink button from License Management page

        :return: 1 if the account was unlinked ; else -1
        """
        self.utils.print_info("Starting unlink")
        sleep(3)
        sfdc_unlink = self.devices_web_elements.get_sfdc_unlink()
        if sfdc_unlink:
            self.auto_actions.click(sfdc_unlink)
            sleep(3)
            yes_button_unlink = self.devices_web_elements.get_yes_button_unlink()
            if yes_button_unlink:
                self.utils.print_info("press yes confirmation")
                self.auto_actions.click(yes_button_unlink)
                sleep(3)
            else:
                self.utils.print_info("confirmation button was not found ")
            self.login.refresh_page()
            sleep(3)
            if self.check_unlink_button(ignore_failure=True) == -1:
                kwargs['pass_msg'] = "The account was unlinked"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "The account was not unlinked"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unlink button was not found"
            self.common_validation.fault(**kwargs)
            return -1

    def check_pilot_license_consumption(self, expected_available, expected_activated, license_type="PRD-XIQ-PIL-S-C",
                                        max_time=660, interval_check_time=60, **kwargs):
        """
        This function checks if the available and activated licenses are displayed as expected into License Management page

        :param expected_available: Number of expected available licenses
        :param expected_activated: Number of expected activated license
        :param license_type: type of license
        :param max_time: Maximum duration of check
        :param interval_check_time: time interval between two consecutive checks
        :return:
        """

        cnt = 0
        still_loading = False
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

            subscription_rows = self.devices_web_elements.get_subscription_rows()
            if subscription_rows:
                still_loading = False
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
                            kwargs['fail_msg'] = "Subscription_available element was not found "
                            self.common_validation.fault(**kwargs)
                            return -1
                        subscription_activated = self.devices_web_elements.get_subscription_activated(el)
                        if subscription_activated:
                            self.utils.print_info("Pilot license activated : ", subscription_activated.text)
                            activated += int(subscription_activated.text)
                        else:
                            kwargs['fail_msg'] = "Subscription_activated element was not found "
                            self.common_validation.fault(**kwargs)
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
                    self.screen.save_screen_shot()
                    return 1
                else:
                    pass
            else:
                if still_loading:
                    kwargs['fail_msg'] = "License_mgmt button was not found"
                    self.common_validation.fault(**kwargs)
                    return -1
                else:
                    self.utils.print_info("license_mgmt button was not found. Adding delay and try again ")
                    still_loading = True
            sleep(interval_check_time)
            cnt = cnt + interval_check_time
            self.utils.print_info("Waited {} sec".format(cnt))
            self.login.refresh_page()
            if still_loading:
                sleep(20)
        self.utils.print_info("Available and activated values from XIQ do not match with the expected values ")
        self.utils.print_info("Available Expected {} ; Displayed in XIQ {}: ".format(expected_available, available))
        self.utils.print_info("Activated Expected {} ; Displayed in XIQ {}: ".format(expected_activated, activated))

        kwargs['fail_msg'] = "Check the pilot license consumption failed."
        self.common_validation.failed(**kwargs)
        return -1

    def check_long_sn_or_legacy_sn_mapping(self, device_serial, ip_dest_ssh, user_dest_ssh, pass_dest_ssh,
                                           sw_connection_host, **kwargs):
        """
        This function checks if the SN for 5520 has short or long format . If the function has short format the sn will be
        searched into extr_legacy_sn_mapping table

        :param ip_dest_ssh: ip of 'Jump Station'
        :param user_dest_ssh: SFDC username account
        :param pass_dest_ssh: SFDC password account
        :param sw_connection_host: The RDC DNS
        :return: 1 if SN has long format or if it is into db ; else -1
        """

        pattern1 = "(\\w+)."
        rdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)

        if len(device_serial) > 11:
            kwargs['pass_msg'] = "Device SN has long format"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
            output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
            output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
            if "No such file or directory" in output_cmd_cd:
                kwargs['fail_msg'] = "No such file or directory"
                self.common_validation.fault(**kwargs)
                return -1
            else:
                self.cli.send_pxssh(spawn, "cd ..")
            if "ahqa_id_rsa" not in output_cmd_ls:
                # self.robot_built_in.skip('No ssh certificate exist on jump station')
                kwargs['fail_msg'] = "No ssh certificate"
                self.common_validation.fault(**kwargs)
                return -1
            output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc))
            self.utils.print_info(output_cmd)
            output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
            output_cmd2 = self.cli.send_pxssh(spawn, "psqlsystemdb")
            output_cmd3 = self.cli.send_pxssh(spawn, "select * from extr_legacy_sn_mapping where serial_number='{}';".format(device_serial))
            self.utils.print_info(output_cmd)
            self.utils.print_info(output_cmd1)
            self.utils.print_info(output_cmd2)
            self.utils.print_info(output_cmd3)
            pattern1 = "\\((\\d+)\\s+row"
            rows = self.utils.get_regexp_matches(output_cmd3, pattern1, 1)
            self.utils.print_info(rows)
            self.cli.close_spawn(spawn)
            if int(rows[0]) == 1:
                kwargs['pass_msg'] = "Device Sn is into extr_legacy_sn_mapping table"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Device Sn is not into extr_legacy_sn_mapping table or multiple entries were found"
                self.common_validation.failed(**kwargs)
                return -1

    def check_message_unlink_button(self, expected_message, **kwargs):
        """
        This function checks if the message is correct when try to unlink

        :param expected_message: Expected message
        :return: 1 if expected message was found; else -1
        """

        sfdc_unlink_button = self.devices_web_elements.get_sfdc_unlink()
        if sfdc_unlink_button:
            self.auto_actions.move_to_element(sfdc_unlink_button)
            sleep(10)
        else:
            kwargs['fail_msg'] = "'Unlink' button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        message_unlink_button = self.devices_web_elements.get_message_unlink_button()
        if message_unlink_button:
            self.utils.print_info("Message was found :", message_unlink_button.text)
            if expected_message in message_unlink_button.text:
                kwargs['pass_msg'] = "Messages match"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "The messages are not matching"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("Message was not found ")

        kwargs['fail_msg'] = "Message was not found"
        self.common_validation.failed(**kwargs)
        return -1

    def link_to_sfdc_from_license_management_page(self, username, password, shared_cuid=None, **kwargs):
        """
        This function links the XIQ account to SFDC and will move the account to Pilot mode from License Management page

        :param username: SFDC username account
        :param password: SFDC password account
        :param shared_cuid: SFDC shared cuid, by default set to None
        :return: 1 if account was linked ; else -1
        """

        if not self.navigator.navigate_to_license_management() == 1:
            kwargs['fail_msg'] = "Failed to navigate to license page"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        get_link_my_account = self.devices_web_elements.get_link_my_account()
        if get_link_my_account:
            self.utils.print_info("'Link my extreme portal' button was found")
            self.auto_actions.click(get_link_my_account)
        else:
            kwargs['fail_msg'] = "'Link my extreme portal' button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        get_link_my_account_agree = self.devices_web_elements.get_link_my_account_agree()
        if get_link_my_account_agree:
            self.utils.print_info("Checkbox Agree was found ")
            self.auto_actions.click(get_link_my_account_agree)
        else:
            kwargs['fail_msg'] = "Checkbox Agree was not found"
            self.common_validation.fault(**kwargs)
            return -1
        link_my_account_continue = self.devices_web_elements.get_link_my_account_continue()
        if link_my_account_continue:
            self.utils.print_info("Continue button was found ")
            self.auto_actions.click(link_my_account_continue)
        else:
            kwargs['fail_msg'] = "Continue button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(10)
        return self.login_to_extreme_portal(username, password, shared_cuid)

    def get_audit_log(self, **kwargs):
        """
        This function returns the date for the last log from audit

        :return: the date of last log ; else -1
        """

        user_button = self.devices_web_elements.get_user_button()
        if user_button:
            self.utils.print_info("User button was found")
            self.auto_actions.move_to_element(user_button)
        else:
            kwargs['fail_msg'] = "User button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        global_settings = self.devices_web_elements.get_global_settings()
        if global_settings:
            self.utils.print_info("Global_settings was found")
            self.auto_actions.click(global_settings)
        else:
            kwargs['fail_msg'] = "Global_setting was not found"
            self.common_validation.fault(**kwargs)
            return -1

        audit_button = self.devices_web_elements.get_audit_button()
        if audit_button:
            self.utils.print_info("Audit_button was found")
            self.auto_actions.click(audit_button)
        else:
            kwargs['fail_msg'] = "Audit_button was not found"
            self.common_validation.fault(**kwargs)
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
                kwargs['fail_msg'] = "Time_stamp was not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Audit_rows were not found "
            self.common_validation.fault(**kwargs)
            return -1

    def _is_delete_button_visible(self):
        """
        - This helper function verify if the delete button is visible or not
        :return: True if delete button is visible, False if it's hidden
        """
        delete_button = self.devices_web_elements.get_delete_button()
        if delete_button is not None and delete_button.is_displayed():
            self.utils.print_info("Delete button is displayed")
            return True
        else:
            self.utils.print_info("Delete button is hidden")
            return False

    def validate_delete_button_visible(self, **kwargs):
        """
        - This Keyword validates if the delete button is visible
        - Keyword Usage:
        - ``Validate Delete Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_delete_button_visible():
            kwargs['pass_msg'] = "Delete button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Delete button is hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_delete_button_hidden(self, **kwargs):
        """
        - This Keyword validates if the delete button is hidden
        - Keyword Usage:
        - ``Validate Delete Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_delete_button_visible():
            kwargs['pass_msg'] = "Delete button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Delete button is displayed"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_download_button_visible(self):
        """
        - This helper function verify if the download button is visible or not
        :return: True if download button is visible, False if hidden
        """
        download_button = self.devices_web_elements.get_download_button()
        if download_button is not None and download_button.is_displayed():
            self.utils.print_info("Download button is displayed")
            return True
        else:
            self.utils.print_info("Download button is hidden")
            return False

    def validate_download_button_visible(self, **kwargs):
        """
        - This Keyword validates if the download button is visible
        - Keyword Usage:
        - ``Validate Download Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_download_button_visible():
            kwargs['pass_msg'] = "Download button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Download button is hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_download_button_hidden(self, **kwargs):
        """
        - This Keyword validates if the download button is hidden
        - Keyword Usage:
        - ``Validate Download Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_download_button_visible():
            kwargs['pass_msg'] = "Download button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Download button is visible"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_bulk_edit_button_visible(self):
        """
        - This helper function verify if the bulk edit button is visible or not
        :return: True if bulk edit button is visible, False if it's hidden
        """
        edit_button = self.devices_web_elements.get_bulk_edit_button()
        if edit_button is not None and edit_button.is_displayed():
            self.utils.print_info("Bulk edit button is displayed")
            return True
        else:
            self.utils.print_info("Bulk edit button is hidden")
            return False

    def validate_bulk_edit_button_visible(self, **kwargs):
        """
        - This Keyword validates if the bulk edit button is visible
        - Keyword Usage:
        - ``Validate Bulk Edit Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_bulk_edit_button_visible():
            kwargs['pass_msg'] = "Bulk edit button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Bulk edit button is hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_bulk_edit_button_hidden(self, **kwargs):
        """
        - This Keyword validates if the bulk edit button is hidden
        - Keyword Usage:
        - ``Validate Bulk Edit Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_bulk_edit_button_visible():
            kwargs['pass_msg'] = "Bulk edit button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Bulk edit button is visible"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_add_button_visible(self):
        """
        - This helper function verify if the add button is visible or not
        :return: True if visible, False if it's hidden
        """
        add_button = self.devices_web_elements.get_devices_add_button()
        if add_button is not None and add_button.is_displayed():
            self.utils.print_info("Add button is displayed")
            return True
        else:
            self.utils.print_info("Add button is hidden")
            return False

    def validate_add_button_visible(self, **kwargs):
        """
        - This Keyword validates if the add button is visible
        - Keyword Usage:
        - ``Validate Add Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_add_button_visible():
            kwargs['pass_msg'] = "Add button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Add button is hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_add_button_hidden(self, **kwargs):
        """
        - This Keyword validates if the add button is hidden
        - Keyword Usage:
        - ``Validate Add Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_add_button_visible():
            kwargs['pass_msg'] = "Add button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Add button is visible"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_update_device_button_visible(self):
        """
        - This helper function checks if the device update button is visible or not`
        :return: True if device update button is visible, False if not
        """
        update_device_button = self.devices_web_elements.get_update_device_button()
        if update_device_button is not None and update_device_button.is_displayed():
            self.utils.print_info("Update button is displayed")
            return True
        else:
            self.utils.print_info("Update button is hidden")
            return False

    def validate_update_device_button_visible(self, **kwargs):
        """
        - This Keyword validates if the device update button is visible
        - Keyword Usage:
        - ``Validate Update Device Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_update_device_button_visible():
            kwargs['pass_msg'] = "Update button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Update button is hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_update_device_button_hidden(self, **kwargs):
        """
        - This Keyword checks if the device update button is hidden
        - Keyword Usage:
        - ``Validate Update Device Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_update_device_button_visible():
            kwargs['pass_msg'] = "Update button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Update button is visible"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_actions_button_visible(self):
        """
        - This helper functions verify if the actions button is visible or not
        :return: True if devices action button visible, False if not
        """
        device_actions_button = self.devices_web_elements.get_manage_device_actions_button()
        if device_actions_button is not None and device_actions_button.is_displayed():
            self.utils.print_info("Actions button is displayed")
            return True
        else:
            self.utils.print_info("Actions button is hidden")
            return False

    def validate_actions_button_visible(self, **kwargs):
        """
        - This Keyword checks if the actions button is visible
        - Keyword Usage:
        - ``Validate Actions Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_actions_button_visible():
            kwargs['pass_msg'] = "Actions button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Actions button is  hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_actions_button_hidden(self, **kwargs):
        """
        - This Keyword checks if the actions button is hidden
        - Keyword Usage:
        - ``Validate Actions Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_actions_button_visible():
            kwargs['pass_msg'] = "Actions button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Actions button is visible"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_utilities_button_visible(self):
        """
        - This helper function verify if the utilities button is visible or not
        :return: True if visible, False if hidden, fail if exception occurs
        """
        try:
            if self.devices_web_elements.get_manage_device_utilities_button().is_displayed():
                self.utils.print_info("Utilities button is displayed")
                return True

            self.utils.print_info("Utilities button is hidden")
            return False

        except Exception:
            kwargs = {'fail_msg': "Exception"}
            self.common_validation.fault(**kwargs)
            return -1

    def validate_utilities_button_visible(self, **kwargs):
        """
        - This Keyword validates if the utilities button is visible
        - Keyword Usage:
        - ``Validate Utilities Button Visible``

        :return: 1 if visible, -1 if not
        """
        if self._is_utilities_button_visible():
            kwargs['pass_msg'] = "Utilities button is displayed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Utilities button is hidden"
            self.common_validation.failed(**kwargs)
            return -1

    def validate_utilities_button_hidden(self, **kwargs):
        """
        - This Keyword checks if the utilities button is hidden
        - Keyword Usage:
        - ``Validate Utilities Button Hidden``

        :return: 1 if hidden, -1 if visible
        """
        if not self._is_utilities_button_visible():
            kwargs['pass_msg'] = "Utilities button is hidden"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Utilities button is displayed"
            self.common_validation.failed(**kwargs)
            return -1

    def update_network_device_firmware(self, device_mac=None, version='default', forceDownloadImage="true",
                                       performUpgrade="true", saveDefault="false", updateTo="latest",
                                       updatefromD360Page="false", retry_duration=30, retry_count=1200, **kwargs):

        """
        - This method update device to latest version or to a specific version from the dropdown
        - This method needs import datetime as dt
        - Variables and it's possible values
        :param updateTo = {"latest"|"anything other than latest"}
                        - This will hold either "latest" or anything other than latest will be treated
                           as a "specific version" except NULL
        :param saveDefault = {true| false}
        :param performUpgrade = {true| false}                   # 'false' will be treated as 'closing' the update window
        :param forceDownloadImage = {true| false}
        :param version = {'default'|'first'|'last'|'latest'|'noncurrent'|'specific version'}
                        - version to which device should get upgraded. This string should contain into image name
                        -  e.g VOSS: "8.3.0.0", EXOS "31.6.1.2"
        :param device_mac = {"mac adress of the device"}, by default set to None
        :param updatefromD360Page= {false|true}                  # Update page will be launched from D360 if it is true
        :param retry_duration: will check for the firmware upgrade status as per these variable values
        :param retry_count: will check for the firmware upgrade status as per these variable values

        - keyword Usage:
        - Select Version And Upgrade Device To Latest Version    ${DEVICE_MAC}
        - Select Version And Upgrade Device To Specific Version    ${DEVICE_MAC}   version=${VERSION}   updateTo=${"specific"}

        :return: updateToVersion if success else -1
        """

        device_row = -1
        updateToVersion = -1
        initial_timestamp = 0
        initial_updated_status = ""

        # Get the Updated cell data timestamp to validate the update process
        self.utils.print_info("Navigate to Manage --> Devices")
        self.navigator.navigate_to_devices()

        self.utils.print_info("Enable the Updated On column")
        self.column_picker_select("Updated On")

        self.refresh_devices_page()
        self.close_last_refreshed_tooltip()

        if device_mac:
            self.utils.print_info("Getting Updated Status of Device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac=device_mac)
        else:
            kwargs['fail_msg'] = "Invalid device mac"
            self.common_validation.fault(**kwargs)
            return -1
        if device_row:
            device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
            self.utils.print_info("Device Updated Status : ", device_updated_status)
            initial_updated_status = device_updated_status
            if re.search(r'\d+-\d+-\d+', device_updated_status):
                initial_timestamp = int(datetime.timestamp(datetime.strptime(device_updated_status, "%Y-%m-%d %H:%M:%S")))
            os_version = self.get_device_row_values(device_mac, 'OS VERSION')
            nos_version = str(os_version['OS VERSION'])
            sleep(10)
        else:
            kwargs['fail_msg'] = f"Device with mac '{device_mac}' is not found"
            self.common_validation.failed(**kwargs)
            return -1

        try:
            if self.select_device(device_mac=device_mac):
                self.close_last_refreshed_tooltip()
                self.utils.print_info("Closing the last refreshed tool tip")

                if updatefromD360Page.lower() == "false":
                    self.utils.print_info("Selecting Update Devices Button")
                    self.auto_actions.click_reference(self.device_update.get_update_devices_button)
                    sleep(5)
                elif updatefromD360Page.lower() == "true":
                    self.navigator.navigate_to_device360_page_with_mac(device_mac)
                    sleep(5)
                    self.auto_actions.click_reference(self.device_update.get_update_devices_button_from_d360)

                # Unchecking the Update Network Policy and Configuration checkbox if it is already checked
                config_download_checkbox = self.device_update.get_config_download_options_checkbox()
                if config_download_checkbox.is_selected():  # Is selected method will return bool True or False depending upon the selection of the checkbox
                    self.utils.print_info("Update Network Policy and Configuration checkbox is checked - Unchecking")
                    self.auto_actions.click(config_download_checkbox)
                else:
                    self.utils.print_info("Update Network Policy and Configuration checkbox is already unchecked")

                # Check if the Upgrade IQ Engine and Extreme Network Switch Images checkbox is already checked
                checkbox_status = self.device_update.get_upgrade_IQ_engine_and_extreme_network_switch_images_checkbox_status()
                if checkbox_status == "true":  # If checkbox is selected we get string "true" otherwise we get None
                    self.utils.print_info("Upgrade IQ Engine and Extreme Network Switch Images checkbox is already checked")
                else:
                    self.utils.print_info("Selecting upgrade IQ Engine checkbox")
                    self.auto_actions.click_reference(self.device_update.get_upgrade_iq_engine_checkbox)

                # Case-1 : This flow is to perform firmware upgrade to a latest version and return the latest version if success else -1
                if updateTo.lower() == "latest":
                    self.utils.print_info("Selecting upgrade to latest version radio button")
                    self.auto_actions.click_reference(self.device_update.get_upgrade_to_latest_version_radio)
                    sleep(2)

                    updateToVersion = self.device_update.get_latest_version()

                    self.utils.print_info("Device Latest Version: ", updateToVersion)
                    sleep(5)

                    # Perform upgrade if the versions are the same is true and the option is unchecked then enable the checkbox
                    forceDownloadImage_checkbox_status = self.device_update.get_perform_upgrade_if_the_versions_are_the_same_checkbox_status()
                    if forceDownloadImage.lower() == "true":
                        if forceDownloadImage_checkbox_status is not None:   # If checkbox is selected we get string "true" otherwise we get None
                            self.utils.print_info("Perform upgrade if the versions are the same checkbox is already checked")
                        else:
                            self.utils.print_info("Selecting perform upgrade if the versions are the same checkbox")
                            self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_same_checkbox)
                    else:
                        if forceDownloadImage_checkbox_status is not None:
                            self.utils.print_info("Perform upgrade if the versions are the same checkbox is checked - Unchecking")
                            self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_same_checkbox)
                        else:
                            self.utils.print_info("Perform upgrade if the versions are the same checkbox is already unchecked")
                    sleep(2)

                    if saveDefault.lower() == "true":
                        self.utils.print_info("Selecting Save Default button...")

                    self.screen.save_screen_shot()
                    if performUpgrade.lower() == "true":
                        self.utils.print_info("Selecting Perform Update button...")
                        self.auto_actions.click_reference(self.device_update.get_perform_update_button)
                    else:
                        self.utils.print_info("Selecting Cancel and Close button...")
                        self.auto_actions.click_reference(self.device_update.get_update_close_button)
                    sleep(10)

                    if updatefromD360Page.lower() == "true":
                        closebutton = self.device_update.get_d360_close_button()
                        sleep(2)
                        if closebutton:
                            self.auto_actions.click_reference(self.device_update.get_d360_close_button)
                            self.screen.save_screen_shot()
                            sleep(5)
                            self.utils.print_info("Closing the D360 window...")
                        else:
                            kwargs['fail_msg'] = "Unable to close D360 window or is not opened"
                            self.common_validation.fault(**kwargs)
                            return -1

                # Case-2 : This flow is to perform firmware upgrade to a specific version if fails return -1
                elif updateTo.lower() != "latest":

                    self.auto_actions.click_reference(self.device_update.get_upgrade_to_latest_version_radio)
                    sleep(5)
                    latest_version = self.device_update.get_latest_version()
                    self.utils.print_info("Device Latest Version: ", latest_version)
                    sleep(5)

                    self.utils.print_info("Selecting upgrade to specific version radio button")
                    self.auto_actions.click_reference(self.device_update.get_upgrade_to_specific_version_radio)
                    sleep(5)

                    # This is needed to get the list from the dropdown box
                    self.utils.print_info("Selecting perform upgrade if the versions are the same")
                    self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_same_checkbox)
                    sleep(5)

                    self.utils.print_info("Click on version drop down")
                    self.auto_actions.click_reference(self.device_update.get_xiq_upgrade_to_specific_version_dropdown)
                    sleep(2)

                    update_version_items = self.device_update.get_upgrade_to_specific_version_dropdown_list()
                    self.auto_actions.scroll_down()
                    sleep(2)

                    avilableImagesList = []
                    if update_version_items:
                        self.utils.print_info(f"Total number of images found from the drop down list :{len(update_version_items)}")
                        for opt in update_version_items:
                            avilableImagesList.append(opt.text)
                            self.utils.print_info(f"One of the list image is : '{opt.text}'")
                    else:
                        kwargs['fail_msg'] = "Unable to get the list of images from drop down option"
                        self.common_validation.fault(**kwargs)
                        return -1

                    if avilableImagesList == []:
                        kwargs['fail_msg'] = "Image list from the drop down is empty!"
                        self.common_validation.fault(**kwargs)
                        return -1

                    # Case-2.1 : Specific version is passed as an argument e.g version = "8.6.1.0" or "31.6.1.2"
                    if re.search(r'\d+.\d+.\d+.\d+', version):
                        self.utils.print_info("Specific version {} is given ".format(version))
                        match_count = 0
                        for opt in avilableImagesList:
                            if version in opt:
                                self.utils.print_info("Version {} match the image {} from drop down".format(version, opt))
                                match_count += 1
                                updateToVersion = opt
                            else:
                                self.utils.print_info("Version {} doesn't match the image {} from drop down".format(version, opt))

                        if match_count > 0 and updateToVersion != -1:
                            # If more than one match then last match will be used to upgrade the image
                            self.utils.print_info(f"Last successfull match version '{updateToVersion}'")
                        else:
                            kwargs['fail_msg'] = f"Image version {version} doesn't match the images from drop down."
                            self.common_validation.fault(**kwargs)
                            return -1

                    # Case-2.2 : If there is no version specified but opted to upgrade from specific
                    elif version == '':
                        kwargs['fail_msg'] = "Version cannot be empty, specify the version to upgrade."
                        self.common_validation.fault(**kwargs)
                        return -1

                    # Case-2.3 : Specific version is either 'default/first', first version in the list will be used
                    elif version == 'default' or version == 'first':
                        self.utils.print_info("First image version in the specific version drop down will be selected")
                        updateToVersion = avilableImagesList[0]
                        self.utils.print_info("Very first version in the image list {}".format(updateToVersion))

                    # Case-2.4 : Specific version is 'last', last version in the list will be used
                    elif version == 'last':
                        self.utils.print_info("Last image version in the specific version drop down will be selected")
                        updateToVersion = avilableImagesList[-1]
                        self.utils.print_info("Last version in the image list {}".format(updateToVersion))

                    # Case-2.5 : Latest version selected from specific,  e.g version="latest"
                    elif version == 'latest' and latest_version != "":
                        self.utils.print_info(f"Latest version {latest_version} will be selected from the "
                                              f"specific version if it is available")
                        match_count = 0
                        for opt in avilableImagesList:
                            if latest_version in opt:
                                self.utils.print_info("Latest version {} match the "
                                                      "image {} from drop down".format(latest_version, opt))
                                match_count += 1
                                updateToVersion = opt
                            else:
                                self.utils.print_info("Latest version {} doesn't match the "
                                                      "image {} from drop down".format(latest_version, opt))

                        if match_count > 0 and updateToVersion != -1:
                            # If more than one match then last match will be used to upgrade the image
                            self.utils.print_info(f"Last successful match version '{updateToVersion}'")
                        else:
                            kwargs['fail_msg'] = f"Image version {version} doesn't match the images from drop down."
                            self.common_validation.fault(**kwargs)
                            return -1

                    # Case-2.6 : Specific version from the list but different from current NOS version e.g version = "noncurrent"
                    elif version == 'noncurrent' and nos_version != "":
                        self.utils.print_info("Specific version from drop down but different from the current "
                                              "NOS version will be selected")
                        match_count = 0
                        for opt in avilableImagesList:
                            if nos_version not in opt:
                                self.utils.print_info("Device version {} match the image {} from drop down".format(nos_version, opt))
                                match_count += 1
                                updateToVersion = opt
                                break
                            else:
                                self.utils.print_info("Device version {} match the image {} from drop down".format(nos_version, opt))

                        if match_count > 0 and updateToVersion != -1:
                            # If more than one match then last match will be used to upgrade the image
                            self.utils.print_info(f"Last successful match version '{updateToVersion}'")
                        elif match_count == 0:
                            updateToVersion = avilableImagesList[0]
                            self.utils.print_info("First image version in the image list {} is picked since no match found".format(updateToVersion))
                        else:
                            kwargs['fail_msg'] = f"Image version {nos_version} match the images from drop down."
                            self.common_validation.fault(**kwargs)
                            return -1

                    # common block to perform upgade for use case 2.x, once the updateToVersion version is obtained
                    if self.auto_actions.select_drop_down_options(update_version_items, updateToVersion):
                        self.utils.print_info(f"Selected update version from drop down :{updateToVersion}")
                        if saveDefault.lower() == "true":
                            self.utils.print_info("Selecting Save Default button...")

                        # Perform upgrade if the versions are the same is true and the option is unchecked then enable the checkbox
                        forceDownloadImage_checkbox_status = self.device_update.get_perform_upgrade_if_the_versions_are_the_same_checkbox_status()
                        if forceDownloadImage.lower() == "true":
                            if forceDownloadImage_checkbox_status is not None:
                                self.utils.print_info("Perform upgrade if the versions are the same checkbox is already checked")
                            else:
                                self.utils.print_info("Selecting perform upgrade if the versions are the same checkbox")
                                self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_same_checkbox)
                        else:
                            if forceDownloadImage_checkbox_status is not None:
                                self.utils.print_info("Perform upgrade if the versions are the same checkbox is checked - Unchecking")
                                self.auto_actions.click_reference(self.device_update.get_upgrade_even_if_versions_same_checkbox)
                            else:
                                self.utils.print_info("Perform upgrade if the versions are the same checkbox is already unchecked")

                        if performUpgrade.lower() == "true":
                            self.screen.save_screen_shot()
                            self.utils.print_info("Selecting Perform Update button...")
                            self.auto_actions.click_reference(self.device_update.get_perform_update_button)
                        else:
                            self.utils.print_info("Selecting Close button...")
                            self.auto_actions.click_reference(self.device_update.get_update_close_button)
                        sleep(10)

                        if updatefromD360Page.lower() == "true":
                            closebutton = self.device_update.get_d360_close_button()
                            sleep(2)
                            if closebutton:
                                self.auto_actions.click_reference(self.device_update.get_d360_close_button)
                                self.screen.save_screen_shot()
                                sleep(5)
                                self.utils.print_info("Closing the D360 window...")
                            else:
                                kwargs['fail_msg'] = "Unable to close D360 window or is not opened"
                                self.common_validation.fault(**kwargs)
                                return -1

                # Case-3 : Invalid option passed to 'updateTo' arg, neither 'latest' nor 'specific'
                else:
                    kwargs['fail_msg'] = f"Invalid UpdateTo Option '{updateTo}', Unable to perform upgrade operation"
                    self.common_validation.fault(**kwargs)
                    return -1

            else:
                kwargs['fail_msg'] = f"Unable to find a device with mac '{device_mac}'"
                self.common_validation.fault(**kwargs)
                return -1

        # If there is an exception then this block of code will be executed
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Exception occurred, unable to perform upgrade operation."
            self.common_validation.fault(**kwargs)
            return -1

        # If there is no exception then this block of code will be executed to get the Updated cell data
        else:
            device_updated_status = ""
            self.utils.print_info("Navigate to Manage --> Devices")
            self.navigator.navigate_to_devices()
            self.refresh_devices_page()

            device_row = self.get_device_row(device_mac=device_mac)
            device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
            self.utils.print_info("Device Updated Status : ", device_updated_status)

            # Incase close option is selected then will return 1
            if performUpgrade.lower() != "true" and "Firmware Updating" not in device_updated_status:
                self.utils.print_info("Firmware update is not triggered when clicking the close button...")
                return 1  # This is where we return the updated status as 1
            elif performUpgrade.lower() != "true" and "Firmware Updating" in device_updated_status:
                kwargs['fail_msg'] = "Firmware update is trigger for clicking the close button"
                self.common_validation.fault(**kwargs)
                return -1

            if (forceDownloadImage.lower() == "true") or (nos_version not in str(updateToVersion)):
                self.utils.print_info("Check for the device updated status when force image download is enabled...")
                # Checking for the update column to reflect the firmware updating status max timer is 300 seconds
                count = 0
                while "Firmware Updating" not in device_updated_status:
                    sleep(retry_duration)
                    count += retry_duration
                    self.refresh_devices_page()
                    device_row = self.get_device_row(device_mac=device_mac)
                    device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
                    self.utils.print_info(f"Time elapsed for firmware update '{count}' seconds and status '{device_updated_status}'")
                    if ("Device Update Failed" in device_updated_status) or (count > 300):
                        kwargs['fail_msg'] = "Firmware Update failed"
                        self.common_validation.failed(**kwargs)
                        return -1
                # Checking firmware update status every 30 seconds upto 900 seconds max
                while ("Firmware Updating" in device_updated_status) or ("Rebooting" in device_updated_status):
                    sleep(retry_duration)
                    count += retry_duration
                    self.refresh_devices_page()
                    device_row = self.get_device_row(device_mac=device_mac)
                    device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
                    self.utils.print_info(f"Time elapsed for firmware update '{count}' seconds and status '{device_updated_status}'")
                    if ("Device Update Failed" in device_updated_status) or (count > retry_count):
                        kwargs['fail_msg'] = "Firmware Update failed"
                        self.common_validation.failed(**kwargs)
                        return -1
                    elif re.search(r'\d+-\d+-\d+', device_updated_status):
                        self.utils.print_info("Firmware Update 100% Completed!")
                        break
            else:
                self.utils.print_info("Check for the device updated status when force image download is disabled...")
                self.utils.print_info("Initial Device Updated Status : ", initial_updated_status)
                sleep(30)
                self.refresh_devices_page()
                device_row = self.get_device_row(device_mac=device_mac)
                device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
                self.utils.print_info("Current Device Updated Status : ", device_updated_status)
                if re.search(r'\d+-\d+-\d+', device_updated_status) or (device_updated_status == "") or (device_updated_status == "Device Update Failed."):
                    count = 0
                    while True:
                        latest_timestamp = int(datetime.timestamp(datetime.strptime(device_updated_status, "%Y-%m-%d %H:%M:%S")))
                        if latest_timestamp > initial_timestamp:
                            self.utils.print_info("Device update is finished by just updating the timestamp to : ", str(datetime.fromtimestamp(latest_timestamp)))
                            self.screen.save_screen_shot()
                            sleep(5)
                            break
                        elif count > 60:
                            kwargs['fail_msg'] = f"Device Update Failed due to max wait of '{count}' seconds reached."
                            self.common_validation.fault(**kwargs)
                            return -1
                        elif ((device_updated_status == "Device Update Failed.") or (
                                not re.search(r'\d+-\d+-\d+', device_updated_status))) and (count > 60):
                            device_row = self.get_device_row(device_mac=device_mac)
                            kwargs['fail_msg'] = f"Device Update Failed due to {device_updated_status}"
                            self.common_validation.failed(**kwargs)
                            return -1
                        sleep(retry_duration)
                        count += retry_duration
                        device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
                        sleep(5)
                else:
                    kwargs['fail_msg'] = f"Device Update Failed due to {device_updated_status}"
                    self.common_validation.failed(**kwargs)
                    return -1

            # Comparing the DUT version and XIQ version post successfull upgrade max wait time 300 seconds
            sleep(5)
            self.refresh_devices_page()
            os_version = self.get_device_row_values(device_mac, 'OS VERSION')
            deviceImageVersion = '-'.join(os_version['OS VERSION'].split(" "))
            count = 0
            while True:
                self.utils.print_info(f"Time elapsed in comparing the firmware version : {count} seconds ...")
                if str(deviceImageVersion) in str(updateToVersion):
                    self.utils.print_info(f"Device firmware successfully updated to version : '{deviceImageVersion}'")
                    self.screen.save_screen_shot()
                    sleep(5)
                    return deviceImageVersion  # This is where we return the updated status with updated firmware version
                elif (count > 600) and (str(deviceImageVersion) not in str(updateToVersion)):
                    kwargs['fail_msg'] = f"Firmware Update Failed! " \
                                         f"Expected version is '{updateToVersion}' but found '{deviceImageVersion}'"
                    self.common_validation.failed(**kwargs)
                    return -1
                self.refresh_devices_page()
                sleep(30)
                count += 30
                os_version = self.get_device_row_values(device_mac, 'OS VERSION')
                deviceImageVersion = '-'.join(os_version['OS VERSION'].split(" "))

    def wait_until_all_devices_update_done(self, wait_time_in_min):
        """
        - This Keyword checks if all devices are done with updating
        - Keyword Usage:
        - ``wait_until_all_devices_update_done``

        :param  wait_time_in_min: time to wait
        :return: 1 if done, -1 if not
        """
        n_time = 0
        self.utils.print_info("Checking all device progress status ")
        while n_time < int(wait_time_in_min) * 2:  # waits for 30s instead of 1 min before the next loop
            rows = self.devices_web_elements.get_manage_all_devices_progress_status()
            if rows == None:
                break
            else:
                self.utils.print_info(str(len(rows)) + ' device(s) still updating ')
                n_time = n_time + 1
                sleep(30)
                self.utils.print_info("time has waited so far:  " + str(round(int(n_time) / 2, 2)) + " min(s)")

    def wait_until_device_update_done(self, device_serial=None, device_mac=None, device_name=None, wait_time_in_min=15,
                                      skip_navigation=False, skip_refresh=False, **kwargs):
        """
        - This keyword checks if the expected device is done with updating - even if the update failed
        - Keyword Usage:
        - ``wait_until_device_update_done   device_serial=${DEVICE_SERIAL}``
        - ``wait_until_device_update_done   device_mac=${DEVICE_MAC}``
        - ``wait_until_device_update_done   device_name=${DEVICE_NAME}``

        :param device_serial: serial number of the device. Example: "01301511060005", by default set to None
        :param device_mac: mac of the device. Example: 885BDD4BE380, by default set to None
        :param device_name: name of the device. Example: bui-flo-0005, by default set to None
        :param wait_time_in_min: time to wait in min, by default set to 15
        :param skip_refresh: skipping the refresh of the devices page, by default set to False
        :param skip_navigation: skipping the navigation to the devices page, by default set to False
        :return: 1 if done, -1 if not
        """
        if not skip_navigation:
            self.navigator.navigate_to_manage_tab()
        if not skip_refresh:
            self.refresh_devices_page()

        complete = False
        n_time = 0
        update_status = -1
        date_regex = r"(\d{4})-((0[1-9])|(1[0-2]))-(0[1-9]|[12][0-9]|3[01]) ([0-2]*[0-9]\:[0-6][0-9]\:[0-6][0-9])"

        while n_time <= int(wait_time_in_min * 4):
            n_time = n_time + 1
            if device_serial:
                update_status = self.get_device_details(device_serial, 'UPDATED')
                self.utils.print_info("Updated status is: '" + str(update_status) + "' for the device_serial: " + str(device_serial))
            elif device_mac:
                update_status = self.get_device_details(device_mac, 'UPDATED')
                self.utils.print_info("Updated status is: '" + str(update_status) + "' for the device_mac: " + str(device_mac))
            elif device_name:
                update_status = self.get_device_details(device_name, 'UPDATED')
                self.utils.print_info("Updated status is: '" + str(update_status) + "' for the device_name: " + str(device_name))

            # There are multiple conditions were a device can be decalared that the update has completed
            # 1) There is no update to do
            # 2) The update was attempted but failed
            # 3) The update was completed
            if update_status == '':
                kwargs['pass_msg'] = "Device is not in the process of updating thus it is considered updated"
                self.common_validation.passed(**kwargs)
                complete = True
                break
            # If there are other 'Failed' conditions please add them here
            elif update_status == 'Device Update Failed.' or update_status == 'Device Update Failed To Proceed.':
                kwargs['pass_msg'] = "Device has finished updating but with a failed condition"
                self.common_validation.passed(**kwargs)
                complete = True
                break
            elif (re.match(date_regex, update_status)):
                kwargs['pass_msg'] = "Device has finished updating"
                self.common_validation.passed(**kwargs)
                complete = True
                break

            sleep(15)

        if not complete:
            kwargs['fail_msg'] = "Device has not finished updating"
            self.common_validation.failed(**kwargs)
            return -1

        return 1

    def assign_network_policy_to_all_devices(self, policy_name, **kwargs):
        """
        - This keyword will assign the network policy to the all devices
        - flow:
        - If Not in devices page, go to it
        - Select all devices
        - Actions
        - Assign Network Policy
        - Select the network policy from drop down window
        - Assign
        - Keyword Usage:
        - ``Assign Network Policy To All Devices    ${policy_name}``

        :param policy_name: policy name to be applied
        :return: Success 1 else -1
        """
        if not self.navigator.get_devices_page():
            self.utils.print_info("Not in Devices page, now to navigate this page...")
            if self.navigator.navigate_to_devices() == 1:
                self.utils.print_info("To navigate the Devices page successfully...")
            else:
                kwargs['fail_msg'] = "Failed to navigate the Devices page"
                self.common_validation.fault(**kwargs)
                return -1
        self.select_all_devices()
        if self._assign_network_policy(policy_name):
            kwargs['pass_msg'] = "Assigned network policy to all devices"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to assign policy to all devices"
            self.common_validation.failed(**kwargs)
            return -1

    def navigate_to_device_configure(self, ap_name, **kwargs):
        """
        - Click on the AP Rows host name --> Configure

        :param ap_name: AP's name
        :return: success 1 else -1
        """
        if not self.navigator.get_devices_page():
            self.utils.print_info("Not in Devices page, now to navigate this page...")
            if self.navigator.navigate_to_devices() == 1:
                self.utils.print_info("To navigate the Devices page successfully...")
            else:
                kwargs['fail_msg'] = "Failed to navigate the Devices page"
                self.common_validation.fault(**kwargs)
                return -1
        ap_name_href = self.devices_web_elements.get_devices_page_grid_ap_name_href(ap_name)
        if ap_name_href:
            self.utils.print_info(f"Click AP name {ap_name} to go to AP device level page...")
            self.auto_actions.click(ap_name_href)
        else:
            kwargs['fail_msg'] = "No ap_name found."
            self.common_validation.fault(**kwargs)
            return -1
        self.utils.print_info("Click Configure button to go to configure page...")
        device_level_configure_button = self.devices_web_elements.get_device_configure_tab()
        if device_level_configure_button:
            self.auto_actions.click(device_level_configure_button)
            return 1
        else:
            kwargs['fail_msg'] = "No Configure button found"
            self.common_validation.fault(**kwargs)
            return -1

    def get_ap_wifi0and1_configured_ssids(self, ap_name, **kwargs):
        """
        - This keyword will get wifi0 and wifi1 ssids from interface settings page behind Configure tab in AP device level
        - flow:
        - Go to configure tab in AP device level based on AP hostname
        - Click Configure tab
        - Click Interface Settings
        - Get wifi0 ssids and wifi1 ssids
        - Put them to a ssid dictionary, as example {'wifi0':['ssid1','ssid2'], 'wifi1':['ssid1','ssid2']}
        - return the ssid dictionary
        - Keyword Usage:
        - ``Get Ap Wifi0and1 Configured Ssids    ${ap_name}``

        :param ap_name: AP hostname
        :return: Success ssid dictionary whatever it is null
        """
        wifi0_1_lists = {}
        if self.navigate_to_device_configure(ap_name) == 1:
            self.auto_actions.click_reference(self.devices_web_elements.get_device_configure_interface_settings)
            while not self.devices_web_elements.get_device_configure_interface_settings_wireless_toggle():
                self.utils.print_info("Wireless Interfaces toggle is NOT shown, click to refresh page ...")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_level_page_refresh)
                self.utils.print_info("Wireless toggle is still NOT loaded successfully, try to refresh...")
            wifi0_ssids_list = []
            wifi0_ssid_rows = self.devices_web_elements.get_device_configure_interface_settings_wifi0_ssid()
            if wifi0_ssid_rows:
                for wifi0_ssid_row in wifi0_ssid_rows:
                    wifi0_ssids_list.append(wifi0_ssid_row.get_attribute('value'))
                wifi0_1_lists['wifi0'] = wifi0_ssids_list
            else:
                self.utils.print_info("No WiFi0 SSID row found, set wifi0_1lists as empty...")
                wifi0_1_lists['wifi0'] = wifi0_ssids_list

            wifi1_ssids_list = []
            wifi1_ssid_rows = self.devices_web_elements.get_device_configure_interface_settings_wifi1_ssid()
            if wifi1_ssid_rows:
                for wifi1_ssid_row in wifi1_ssid_rows:
                    wifi1_ssids_list.append(wifi1_ssid_row.get_attribute('value'))
                wifi0_1_lists['wifi1'] = wifi1_ssids_list
            else:
                self.utils.print_info("No WiFi1 SSID row found, set wifi0_1lists as empty...")
                wifi0_1_lists['wifi1'] = wifi1_ssids_list
            self.auto_actions.click_reference(self.devices_web_elements.get_device_level_page_close_icon)
            self.utils.print_info(f"The WiFi0 and WiFi1 SSID list is: {wifi0_1_lists}")
            return wifi0_1_lists
        else:
            kwargs['fail_msg'] = "Unsuccessfully ssid dictionary whatever it is null"
            self.common_validation.failed(**kwargs)
            return -1

    def get_hostname(self, device_serial, **kwargs):
        """
        - This method gets hostname assigned to the device based on device serial
        - Keyword Usage:
        - ``Get Hostname  ${SERIAL}``

        :param device_serial: serial number of a device
        :If the device is found the hostname will be returned else -1
        """
        device_keys = {}
        if device_serial:
            device_keys['device_serial'] = device_serial
        if len(device_keys.keys()) == 0:
            kwargs['fail_msg'] = "You must pass the serial number!"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(f"Getting hostname for device '{device_serial}'")
        row = self._find_device_row(device_keys)
        if row:
            hostname = self.devices_web_elements.get_hostname_code_cell(row).text
            kwargs['pass_msg'] = f"Hostname for '{device_serial}' is '{hostname}' "
            self.common_validation.passed(**kwargs)
            return hostname
        else:
            kwargs['fail_msg'] = f"Device {device_serial} was not found"
            self.common_validation.failed(**kwargs)
            return -1

    def check_voss_image_version(self, output_image_version, os_version, operator='less'):
        """
        Check is os_version is equal, less or greater than on version from cli
        :param output_image_version: image version
        :param os_version: 8.6.0.0
        :param operator: equal, less or greater than on version from cli
        :return: True or False if os_version is equal, less or greater than on version from cli ; else -1
        """

        pattern1 = "Version[\\s\\:\\w]+\\s+(\\d+.\\d+.\\d+.\\d+)"
        cli_os_version = self.utils.get_regexp_matches(output_image_version, pattern1, 1)
        if cli_os_version:
            self.utils.print_info(cli_os_version)
            split_cli_os_version = cli_os_version[0].split('.')
            self.utils.print_info(split_cli_os_version)

            split_os_version = os_version.split('.')
            self.utils.print_info(split_os_version)
            cnt = 0
            for el in split_os_version:
                if int(el) > int(split_cli_os_version[cnt]):
                    if operator == 'equal':
                        return False
                    elif operator == 'less':
                        return False
                    elif operator == 'greater':
                        return True
                    else:
                        return -1

                elif int(el) < int(split_cli_os_version[cnt]):
                    if operator == 'equal':
                        return False
                    elif operator == 'less':
                        return True
                    elif operator == 'greater':
                        return False
                    else:
                        return -1
                elif int(el) == int(split_cli_os_version[cnt]):
                    pass
                else:
                    return -1
                cnt = cnt + 1
        else:
            return -1
        if operator == 'equal':
            return True
        elif operator == 'less':
            return False
        elif operator == 'greater':
            return False
        else:
            return -1

    def teardown_check_and_revoke_license(self, device_sn, **kwargs):
        """
        This function revoke all device license

        :param device_sn: Sn of device
        :return: 1 if device license status in "None" ; else -1
        """
        flag_revoke = False
        error = None
        cnt = 0
        while cnt < 2:
            status = self.check_license_status(device_sn)
            list_status_lic_and_error = status.split(" ", maxsplit=1)
            if len(list_status_lic_and_error) == 1:
                if list_status_lic_and_error[0] == 'None':
                    return 1
                else:
                    pass
                if flag_revoke:
                    kwargs['fail_msg'] = f"There are still active licenses {list_status_lic_and_error[0]}"
                    self.common_validation.fault(**kwargs)
                    return -1
                list_status_lic = list_status_lic_and_error[0].split(",")
                for lic in list_status_lic:
                    self.revoke_device_license(device_sn, lic, skip_warning_check=True)
                    self.check_license_status(device_sn)
                flag_revoke = True

            elif len(list_status_lic_and_error) == 2:
                if list_status_lic_and_error[0] == 'None':
                    return 1
                if error:
                    kwargs['fail_msg'] = f"There are still active licenses {list_status_lic_and_error[0]} " \
                                         f"and error is displayed: {error}"
                    self.common_validation.fault(**kwargs)
                    return -1
                list_status_lic = list_status_lic_and_error[0].split(",")
                for lic in list_status_lic:
                    self.revoke_device_license(device_sn, lic, skip_warning_check=True)
                    self.check_license_status(device_sn)
                flag_revoke = True
                error = list_status_lic_and_error[1]
            else:
                kwargs['fail_msg'] = "Teardown check and revoke the license failed."
                self.common_validation.failed(**kwargs)
                return -1
            cnt = cnt + 1
        kwargs['fail_msg'] = "Teardown check and revoke the license failed."
        self.common_validation.failed(**kwargs)
        return -1

    def change_manage_device_status(self, manage_type='MANAGE', device_serial=None, device_mac=None,
                                    device_name=None, **kwargs):
        """
        This Keyword changes the management status of the device.
        - Keyword Usage:
        - ``Change Manage Device Status    MANAGE      device_serial=${DEVICE_SERIAL}``
        - ``Change Manage Device Status    UNMANAGE    device_mac=${DEVICE_MAC}``
        - ``Change Manage Device Status    MANAGE    device_mac=${DEVICE_NAME}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param device_serial: device Serial, by default set to None
        :param device_mac: device MAC address, by default set to None
        :param device_name: device name, by default set to None
        :param manage_type: Manage/Unmanage device
        :return: 1 if the management status was changed
        """
        if self.xapiDevices.is_xapi_enabled(**kwargs):
            return self.xapiDevices.xapi_change_manage_device_status(manage_type=manage_type, device_serial=device_serial, device_mac=device_mac, device_name=device_name, **kwargs)

        # Commented on 1/18/23 because it is unused
        # manage_setting = 'MANAGE'
        # unmanage_setting = 'UNMANAGE'
        select_flag = False
        self.navigator.enable_page_size()
        if device_serial:
            select_flag = False
            device_serial = device_serial.split(',')
            for device in device_serial:
                if device == device_serial[0]:
                    self.select_device(device_serial=device)
                    self.utils.print_info("Device with serial {} was selected".format(device))
                    select_flag = True
                else:
                    self.select_device(device_serial=device, skip_refresh=True, skip_navigation=True)
                    self.utils.print_info("Device with serial {} was selected".format(device))
                    select_flag = True

        elif device_mac:
            select_flag = False
            if self.select_device(device_mac=device_mac):
                self.utils.print_info("Device with mac {} was selected".format(device_mac))
                select_flag = True
            else:
                kwargs['fail_msg'] = f"Device with mac {device_mac} has not been selected"
                self.common_validation.fault(**kwargs)
                return -1
        elif device_name:
            select_flag = False
            if self.select_device(device_name=device_name):
                self.utils.print_info("Device with name {} was selected".format(device_name))
                select_flag = True
            else:
                kwargs['fail_msg'] = f"Device with name {device_name} has not been selected"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "No device serial, device mac or device name has been given."
            self.common_validation.fault(**kwargs)
            return -1
        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
            sleep(2)
        self.utils.print_info("Trying to Change Management Status")
        sleep(2)
        manage_status = self.device_actions.get_device_actions_change_manage_status()
        self.utils.print_info("Change Management Status")
        if manage_status:
            self.utils.print_info("Selecting Change management status ")
            self.auto_actions.move_to_element(manage_status)
            sleep(2)
            self.utils.print_info("Trying to select manage/unmanage.")
            if str(manage_type).upper() in 'MANAGE':
                manage_btn = self.device_actions.get_manage_device_btn()
                if manage_btn:
                    self.utils.print_info("Select Manage device")
                    self.auto_actions.click(manage_btn)
                    sleep(2)
                    self.screen.save_screen_shot()
                    confirm_btn = self.device_actions.get_confirm_manage_btn_yes()
                    if confirm_btn:
                        self.utils.print_info("Confirm manage device")
                        self.auto_actions.click(confirm_btn)
                        sleep(2)
                    else:
                        kwargs['fail_msg'] = "Confirm button not found"
                        self.common_validation.fault(**kwargs)
                        return -1
                    sleep(10)
                    self.screen.save_screen_shot()
                    confirm_msg = self.device_actions.get_confirm_manage_message()
                    if not confirm_msg:
                        kwargs['fail_msg'] = "Confirm manage message was not found"
                        self.common_validation.fault(**kwargs)
                        return -1
                    else:
                        pass
                    confirm_msg_txt = confirm_msg.text
                    self.utils.print_info("Text: ", confirm_msg_txt)

                    if "successfully changed to MANAGED" in confirm_msg_txt:
                        self.utils.print_info("Managed status successfully changed")

                        close_confirm_tab = self.device_actions.get_close_message_btn()
                        if close_confirm_tab:
                            self.utils.print_info("Closing the manage confirmation tab")
                            self.auto_actions.click(close_confirm_tab)
                            return 1
                        else:
                            kwargs['fail_msg'] = "Could not close the manage confirmation tab"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("Expected message: The device was successfully changed to MANAGED.")
                        self.utils.print_info("Actual message: ", confirm_msg_txt)
                        kwargs['fail_msg'] = "Managed status was not changed"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "Manage button not found"
                    self.common_validation.fault(**kwargs)
                    return -1
            elif str(manage_type).upper() in 'UNMANAGE':
                unmanage_btn = self.device_actions.get_unmanage_device_btn()
                if unmanage_btn:
                    self.utils.print_info("Select Unmanage device")
                    self.auto_actions.click(unmanage_btn)
                    sleep(2)

                    confirm_btn = self.device_actions.get_confirm_manage_btn_yes()
                    if confirm_btn:
                        self.utils.print_info("Confirm unmanage device")
                        self.auto_actions.click(confirm_btn)
                        sleep(2)
                    else:
                        kwargs['fail_msg'] = "Confirm button not found"
                        self.common_validation.fault(**kwargs)
                        return -1
                    sleep(10)
                    confirm_msg = self.device_actions.get_confirm_manage_message()
                    confirm_msg_txt = confirm_msg.text
                    self.utils.print_info("Text: ", confirm_msg_txt)

                    if "successfully changed to UNMANAGED" in confirm_msg_txt:
                        self.utils.print_info("Unmanaged status successfully changed")
                        close_confirm_tab = self.device_actions.get_close_message_btn()
                        if close_confirm_tab:
                            self.utils.print_info("Closing the unmanage confirmation tab")
                            self.auto_actions.click(close_confirm_tab)
                            return 1
                        else:
                            kwargs['fail_msg'] = "Could not close the unmanage confirmation tab"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("Expected message: The device was successfully changed to UNMANAGED.")
                        self.utils.print_info("Actual message: ", confirm_msg_txt)
                        kwargs['fail_msg'] = "Managed status was not changed"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "Unmanage button not found"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Manage status unknown"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Change management status not found"
            self.common_validation.fault(**kwargs)
            return -1

    def check_unmanage_message_on_device(self, **kwargs):
        """
        This Keyword verifies if the unmanage message was shown.

        :return: 1 if the unmanaged message was shown
        """

        unmanage_msg = self.device_actions.get_unmanage_msg_text()
        if unmanage_msg:
            self.utils.print_info("Error message is shown. Checking if it's unmanage message.")
            unmanage_msg_txt = unmanage_msg.text
            self.utils.print_info("Unmanage text: ", unmanage_msg_txt)
            self.utils.print_info("Checking if the error message is from unmanage")
            if "was marked as unmanaged on" in unmanage_msg_txt:
                self.utils.print_info("Unmanage message is present")
                close_msg_btn = self.device_actions.get_close_message_btn()
                if close_msg_btn:
                    self.utils.print_info("Closing the device tab")
                    self.auto_actions.click(close_msg_btn)
                    return 1
                else:
                    kwargs['fail_msg'] = "Could not close the device tab"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                self.utils.print_info("Error message does not contain the unmanage message.")
                self.utils.print_info("Error message shown is: ", unmanage_msg_txt)
                self.screen.save_screen_shot()

                close_msg_btn = self.device_actions.get_close_message_btn()
                if close_msg_btn:
                    self.utils.print_info("Closing the device tab")
                    self.auto_actions.click(close_msg_btn)
                else:
                    self.utils.print_info("Could not close the device tab")
                    self.screen.save_screen_shot()

                kwargs['fail_msg'] = "Check the unmanage message on the device failed."
                self.common_validation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("Unmanage message not found.")
            self.screen.save_screen_shot()

            close_msg_btn = self.device_actions.get_close_message_btn()
            if close_msg_btn:
                self.utils.print_info("Closing the device tab")
                self.auto_actions.click(close_msg_btn)
                return 1
            else:
                kwargs['fail_msg'] = "Could not close the device tab"
                self.common_validation.fault(**kwargs)
                return -1

    def change_device_onboarding_date_for_each_stack_member(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, days,
                                                            serial_number, owner_id, sw_connection_host, **kwargs):
        """
        This function change the onboarding date with specific number of days behind
        To use this function you need to have access to RDC database

        :param ip_dest_ssh: ip of 'Jump station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param days: The number of days passed from onboarding date
        :param serial_number: Serial number of device
        :param owner_id: Owner Id for XIQ account
        :param rdc: RDC name : e.g w1r1 , g2r1
        :param sw_connection_host
        :return: 1 if onboarding date has been changed ; else -1
        """
        if not isinstance(serial_number, list):
            serial_number = serial_number.split(",")

        if isinstance(serial_number, list):
            self.utils.print_info("Trying to change the onboarding date for each serial...")
            for serial in serial_number:
                self.utils.print_info("Changing onboarding date for serial {}.".format(serial))
                change_date_status = self.change_device_onboarding_date(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, days,
                                                                        serial, owner_id, sw_connection_host)
                if change_date_status != 1:
                    kwargs['fail_msg'] = f"For this serial the onboarding date was not changed {serial}"
                    self.common_validation.failed(**kwargs)
                    return -1
            return 1
        else:
            kwargs['fail_msg'] = "The serial number given is not a list!"
            self.common_validation.fault(**kwargs)
            return -1

    def actions_change_os(self, device_serial, os, max_time=300, time_interval=10, **kwargs):
        """
        This function change the os on switch by using ACTIONS->CHANGE OS button . Return 1 when "Rebooting" status is displayed

        :param device_serial: SN of device
        :param os: exos or voss
        :param max_time:  maximum time waited for "Rebooting" status
        :param time_interval: check interval
        :return: 1 when "Rebooting" status is displayed; else -1
        """
        select_flag = False
        device_serial = device_serial.split(',')

        self.navigator.enable_page_size()
        for el in device_serial:
            if el == device_serial[0]:
                self.select_device(el)
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True
            else:
                self.select_device(el, skip_refresh=True, skip_navigation=True)
                self.utils.print_info("Device with serial {} was selected".format(el))
                select_flag = True

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
            sleep(2)

        self.utils.print_info("Select Change OS ")
        if 'voss' in os.lower():
            change_os_actions = self.device_actions.get_change_os_actions_exos()
        elif 'exos' in os.lower():
            change_os_actions = self.device_actions.get_change_os_actions_exos()
        self.utils.print_info(change_os_actions)
        if change_os_actions:
            self.utils.print_info("Change OS")
            self.auto_actions.click(change_os_actions)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Change OS not found"
            self.common_validation.failed(**kwargs)
            return -1

    def get_device_updated_status_percentage(self, device_serial=None, device_name=None,
                                             device_mac=None, **kwargs):
        """
        - This keyword returns the device updated status in percentage by searching device row using serial, name or mac address
        - Assumes that already navigated to the manage-->device page
        - Keyword Usage:
        - ``Get Device Updated Status   device_serial=${DEVICE_SERIAL}``
        - ``Get Device Updated Status   device_name=${DEVICE_NAME}``
        - ``Get Device Updated Status   device_mac=${DEVICE_MAC}``

        :param device_serial: device Serial, by default set to None
        :param device_name: device Name, by default set to None
        :param device_mac: device MAC, by default set to None
        :return: 'device_update_status_strip' status number without '%'
        """
        device_row = -1

        # Select the correct column
        self.utils.print_info("Enable the Updated On column")
        self.column_picker_select("Updated On")

        self.utils.print_info('Getting device Updated Status using')
        if device_serial:
            self.utils.print_info("Getting Updated status of device with serial: ", device_serial)
            device_row = self.get_device_row(device_serial=device_serial)

        if device_name:
            self.utils.print_info("Getting Updated status of device with name: ", device_name)
            device_row = self.get_device_row(device_name=device_name)

        if device_mac:
            self.utils.print_info("Getting Updated status of device with MAC: ", device_mac)
            device_row = self.get_device_row(device_mac=device_mac)

        if device_row:
            sleep(10)
            device_updated_status = self.devices_web_elements.get_updated_status_cell(device_row).text
            if re.search(r'\d+-\d+-\d+\s\d+:\d+:\d+', device_updated_status):
                device_updated_status_replace_100 = re.sub(r'\d+-\d+-\d+\s\d+:\d+:\d+', "100", device_updated_status)
                # self.utils.print_info(f"Device Updated Status is: {device_updated_status_replace_100} % ")
                return device_updated_status_replace_100
            elif "Device Update Failed" in device_updated_status:
                self.utils.print_info("Device updating status is: Device Update Failed")
                return 'Device Update Failed'
            else:
                device_update_status_replace = device_updated_status.replace("%", "")
                if 'Configuration Updating' in device_update_status_replace:
                    device_update_status_strip = device_update_status_replace.strip("\nConfiguration Updating")
                elif 'Waiting Switch Execution Result' in device_update_status_replace:
                    device_update_status_strip = device_update_status_replace.strip("\nWaiting Switch Execution Result")
                elif 'Configuration Audit Clear' in device_update_status_replace:
                    device_update_status_strip = device_update_status_replace.strip("\nConfiguration Audit Clear")
                self.utils.print_info(f"Device Updated Status is: {device_update_status_strip}%")
                return device_update_status_strip
        else:
            kwargs['fail_msg'] = "Device row not found"
            self.common_validation.failed(**kwargs)
            return -1

        # Commented on 1/18/23 because code is unreachable
        # yes_confirmation = self.device_actions.get_yes_confirmation()
        # if yes_confirmation:
        #     self.utils.print_info("yes confirmation button was found ")
        #     self.auto_actions.click(yes_confirmation)
        # else:
        #     self.utils.print_info("yes confirmation button was not found ")
        #     self.screen.save_screen_shot()
        #     return -1
        # self.utils.print_info("Start checking the status")
        # retry_count = 0
        # while retry_count <= max_time:
        #     sleep(5)
        #     if device_serial != 'default':
        #         self.utils.print_info("Getting Updated status of device with serial: ", device_serial)
        #         device_row = self.get_device_row(device_serial)
        #     else:
        #         return -1
        #     device_update_status = self.devices_web_elements.get_updated_status_cell(device_row).text
        #     if device_update_status:
        #         if 'Rebooting' in device_update_status:
        #             self.utils.print_info("Rebooting status was found  ", device_update_status)
        #             return 1
        #         elif 'Failed' in device_update_status:
        #             self.utils.print_info("Device Update Failed: ", device_update_status)
        #             return -1
        #         else:
        #             self.utils.print_info("Waiting for Rebooting status; Now the status is :  ", device_update_status)
        #     else:
        #         pass
        #     sleep(time_interval)
        #     self.utils.print_info(f"Time elapsed for device update: {retry_count} seconds")
        #     retry_count += time_interval
        # self.utils.print_info("return -1  ", device_update_status)
        # self.screen.save_screen_shot()
        # return -1

    def get_cuid_and_viq_id(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, owner_id, sw_connection_host):
        """
        This functions returns VHM ID an CUID ID.

        :param ip_dest_ssh: ip/dns destination of bastion host
        :param user_dest_ssh: user for bastion host account
        :param pass_dest_ssh: password for bastion host account
        :param owner_id: Owner id
        :param sw_connection_host: RDC environment
        :return: CUID and VIQ_IQ; else return None
        """

        pattern1 = "(\\w+)r\\d."
        gdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        output_cmd = self.cli.send_pxssh(spawn, "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(gdc[0]))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlaccountdb", expected_output="Password for user accountuser:")
        output_cmd3 = self.cli.send_pxssh(spawn, "aerohive")
        self.cli.send_pxssh(spawn, ";")
        output_cmd5 = self.cli.send_pxssh(spawn,
                                          "select viq_id,system_cuid from viqid_to_cuid where owner_id ={};".format(
                                              owner_id))
        output_cmd4 = self.cli.send_pxssh(spawn,
                                          "select * from viqid_to_cuid where owner_id ={};".format(
                                              owner_id))
        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)
        self.utils.print_info(output_cmd4)
        self.utils.print_info(output_cmd5)

        pattern = "(VHM[\\w\\-]+)\\s+\\|\\s+\\w+"
        pattern2 = "VHM[\\w\\-]+\\s+\\|\\s+(\\w+)"
        viq_id = self.utils.get_regexp_matches(output_cmd5, pattern, 1)
        system_cuid = self.utils.get_regexp_matches(output_cmd5, pattern2, 1)
        self.utils.print_info(viq_id)
        self.utils.print_info(system_cuid)

        self.cli.close_spawn(spawn)
        return viq_id[0], system_cuid[0]

    def unmanage_device_when_license_expired(self, device_sn, **kwargs):
        """
        This function unmanage a device when unmanage box is displayed

        :param device_sn: Sn of device
        :return: 1 when device was unmanage ; else -1
        """

        if self.select_device(device_sn) == 1:
            unmanage_button = self.devices_web_elements.get_license_unmanage_box()
            if unmanage_button:
                self.auto_actions.click(unmanage_button)
                confirm_btn = self.device_actions.get_confirm_manage_btn_yes()
                if confirm_btn:
                    self.utils.print_info("Confirm manage device")
                    self.auto_actions.click(confirm_btn)
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Confirm button not found"
                    self.common_validation.fault(**kwargs)
                    return -1
                sleep(10)
                confirm_msg = self.device_actions.get_confirm_manage_message()
                if confirm_msg:
                    if "The device was successfully changed to UNMANAGED." in confirm_msg.text:
                        self.utils.print_info("The device was successfully changed to UNMANAGED.")
                        close_confirm_tab = self.device_actions.get_close_message_btn()
                        if close_confirm_tab:
                            self.utils.print_info("Closing the manage confirmation tab")
                            self.auto_actions.click(close_confirm_tab)
                            return 1
                        else:
                            kwargs['fail_msg'] = "Could not close the manage confirmation tab"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("The unmanage message is not correct")
                        self.utils.print_info("Actual message: ", confirm_msg.text)
                        close_confirm_tab = self.device_actions.get_close_message_btn()
                        if close_confirm_tab:
                            self.utils.print_info("Closing the manage confirmation tab")
                            self.auto_actions.click(close_confirm_tab)
                        else:
                            kwargs['fail_msg'] = "Could not close the manage confirmation tab"
                            self.common_validation.fault(**kwargs)
                            return -1
            else:
                kwargs['fail_msg'] = "Unmanage button not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Device not selected"
            self.common_validation.fault(**kwargs)
            return -1

    def check_license_update_frequency(self, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, sw_connection_host, **kwargs):
        """
        This function checks the update frequency for license job

        :param ip_dest_ssh: ip of 'Jump station'
        :param user_dest_ssh: extreme account user
        :param pass_dest_ssh: extreme account password
        :param sw_connection_host: RDC DNS
        :return: 1 if update time is less or equal than 10 minutes ; else -1
        """

        pattern1 = "(\\w+)."
        rdc = self.utils.get_regexp_matches(sw_connection_host, pattern1, 1)
        spawn = self.cli.open_pxssh_spawn(ip_dest_ssh, user_dest_ssh, pass_dest_ssh)
        output_cmd_cd = self.cli.send_pxssh(spawn, "cd .ssh")
        output_cmd_ls = self.cli.send_pxssh(spawn, "ls")
        if "No such file or directory" in output_cmd_cd:
            kwargs['fail_msg'] = "No such file or directory"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.cli.send_pxssh(spawn, "cd ..")
        if "ahqa_id_rsa" not in output_cmd_ls:
            # self.robot_built_in.skip('No ssh certificate exist on jump station')
            kwargs['fail_msg'] = "No ssh certificate"
            self.common_validation.fault(**kwargs)
            return -1
        output_cmd = self.cli.send_pxssh(spawn,
                                         "ssh -i .ssh/ahqa_id_rsa ahqa@{}-console.qa.xcloudiq.com".format(rdc[0]))
        self.utils.print_info(output_cmd)
        output_cmd1 = self.cli.send_pxssh(spawn, "sudo su -")
        output_cmd2 = self.cli.send_pxssh(spawn, "psqlscheduledb")

        output_cmd4 = self.cli.send_pxssh(spawn,
                                          "select id,interval from hm_job_trigger where id in (select job_trigger_id from hm_job where name = "
                                          "'validate Gemalto license for Cloud task');")

        output_cmd3 = self.cli.send_pxssh(spawn,
                                          "select id,cron,end_time from hm_job_trigger where id in (select job_trigger_id from "
                                          "hm_job where name = 'validate Gemalto license for Cloud task');")
        self.cli.close_spawn(spawn)
        # output_cmd5 = self.cli.send_pxssh(spawn,
        # "select interval from hm_job_trigger where id in (select job_trigger_id from hm_job where name =
        # 'validate Gemalto license for Cloud task');")

        self.utils.print_info(output_cmd)
        self.utils.print_info(output_cmd1)
        self.utils.print_info(output_cmd2)
        self.utils.print_info(output_cmd3)
        self.utils.print_info(output_cmd4)
        # self.utils.print_info(output_cmd5)
        # output_cmd3 = " 324384 | 0 0/5 * * * ?"
        # output_cmd3 = " 324384 | 0 0 1 * * ?"
        pattern3 = "\\s+\\d+\\s+\\|\\s+([\\d\\W]+\\s+[\\d\\W]+\\s+[\\d\\W]+\\s+[\\d\\W]+\\s+[\\d\\W]+\\s+[\\d\\W]+)\\s+\\|"
        # pattern3 = "\\s+([\\d\\W]\\s[\\d\\W]+\\s[\\d\\W]\\s[\\d\\W]\\s[\\d\\W]\\s[\\d\\W])"
        cron = self.utils.get_regexp_matches(output_cmd3, pattern3, 1)
        self.utils.print_info("cron", cron)

        # output_cmd4 = "        0"
        pattern4 = "\\s+\\d+\\s+\\|\\s+(\\d+)"
        interval = self.utils.get_regexp_matches(output_cmd4, pattern4, 1)
        self.utils.print_info("interval", interval)

        # output_cmd5 = "SECONDS"
        # pattern5 = "(\\w+)"
        # interval_unit = self.utils.get_regexp_matches(output_cmd5, pattern5, 1)
        # self.utils.print_info(interval_unit)

        if '0 0 1 * * ?' in cron[0]:
            if int(interval[0]) == 0:
                kwargs['fail_msg'] = "The update license job is running once at each 24 hours. Skip the test"
                self.common_validation.failed(**kwargs)
                return -1
            elif int(interval[0]) <= 10 and not int(interval[0]) == 0:
                self.utils.print_info("The update license job is running once at less than 10 minutes")
                return 1
            else:
                kwargs['fail_msg'] = "Checking the update frequency for license job failed"
                self.common_validation.failed(**kwargs)
                return -1
        elif '0 0/10 * * * ?' in cron[0]:
            self.utils.print_info("The update license job is running once at each 10 minutes  ")
            return 1
        elif '0 0/5 * * * ?' in cron[0]:
            self.utils.print_info("The update license job is running once at each 5 minutes  ")
            return 1
        else:
            kwargs['fail_msg'] = "Checking the update frequency for license job failed"
            self.common_validation.failed(**kwargs)
            return -1

    def get_pilot_license_consumption(self, license_type="PRD-XIQ-PIL-S-C", max_time=120, interval_check_time=60, **kwargs):
        """
        This functions gets the available and activated licenses

        :param license_type:
        :param max_time:
        :param interval_check_time:
        :return: available and activated licenses
        """

        cnt = 0
        still_loading = False
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

            subscription_rows = self.devices_web_elements.get_subscription_rows()
            if subscription_rows:
                still_loading = False
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
                            kwargs['fail_msg'] = "Subscription_available element was not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                        subscription_activated = self.devices_web_elements.get_subscription_activated(el)
                        if subscription_activated:
                            self.utils.print_info("Pilot license activated : ", subscription_activated.text)
                            activated += int(subscription_activated.text)
                        else:
                            kwargs['fail_msg'] = "Subscription_available element was not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        pass
            else:
                if still_loading:
                    kwargs['fail_msg'] = "License_mgmt button was not found"
                    self.common_validation.fault(**kwargs)
                    return -1
                else:
                    self.utils.print_info("license_mgmt button was not found. Adding delay and try again ")
                    still_loading = True
            sleep(interval_check_time)
            cnt = cnt + interval_check_time
            self.utils.print_info("Waited {} sec".format(cnt))
            self.login.refresh_page()
            if still_loading:
                sleep(20)
        self.screen.save_screen_shot()
        return [available, activated]

    def update_device_policy_config_simple(self, device_serial):
        self.utils.print_info("Select Device row")
        self.select_device(device_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

        self.utils.print_info("Clicking on perform update")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)

        # self.auto_actions.click_reference(self.devices_web_elements.get_devices_update_yes_btn)

    def update_device_policy_config_reboot(self, device_serial):
        self.utils.print_info("Select Device row")
        self.select_device(device_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

        self.utils.print_info("Selecting reboot option")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_reboot_revert_checkbox)

        self.utils.print_info("Clicking on perform update")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)
        sleep(2)
        # self.auto_actions.click_reference(self.devices_web_elements.get_devices_update_yes_btn)
        sleep(2)
        self.auto_actions.click_reference(self.devices_web_elements.get_switch_update_reboot_and_revert_warning_dialog_yes_button)

    def get_device_events_list(self, device_model, **kwargs):
        self.utils.print_info("Getting events list")
        events_list = []
        events_elements = self.devices_web_elements.get_events_text()
        sleep(2)
        for element in events_elements:
            events_list.append(element.text)

        if ("Configuration upgrade process is canceled by the user" and device_model) in events_list:
            kwargs['pass_msg'] = f"{events_list}"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Getting the device events list failed."
            self.common_validation.failed(**kwargs)
            return -1

    def update_device_policy_config_image(self, device_serial):
        self.utils.print_info("Select Device row")
        self.select_device(device_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

        self.utils.print_info("Selecting image option")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_image_checkbox)

        self.utils.print_info("Clicking on perform update")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)

    def update_device_policy_image(self, device_serial):
        self.utils.print_info("Select Device row")
        self.select_device(device_serial)

        self.utils.print_info("Click on device update button")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_device_button)

        self.utils.print_info("Selecting image option")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_image_checkbox)

        self.utils.print_info("Deselecting upgrade configuration option")
        self.auto_actions.click_reference(self.devices_web_elements.get_update_config_checkbox)

        self.utils.print_info("Clicking on perform update")
        self.auto_actions.click_reference(self.devices_web_elements.get_perform_update_button)

    def reboot_device_while_update(self, device_serial):
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
            self.auto_actions.click_reference(self.device_actions.get_device_actions_button)

            self.utils.print_info("Clicking on Reboot")
            self.auto_actions.click_reference(self.device_actions.get_device_actions_reboot_menu_item)

            self.utils.print_info("Confirming...")
            self.auto_actions.click_reference(self.dialogue_web_elements.get_confirm_yes_button_reboot)
            return 1

    def check_device_license_action(self, device_serial, **kwargs):
        """
        - Assumes that already navigated to Manage --> Devices
        - This method checks if License action is available for a device matching the serial(s)
        - Keyword Usage:
        - ``Check Device License Action ${DEVICE_SERIAL}``

        :param device_serial: device serial number
        :return: int
        """
        self.utils.print_info("Looking for device with serial: ", device_serial)
        self.select_device(device_serial)
        if self.select_device(device_serial):
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.devices_web_elements.get_device_actions_button)

        self.utils.print_info("Checking if License option is displayed")
        license_button = self.devices_web_elements.get_license_action_button()
        if license_button.is_displayed():
            kwargs['fail_msg'] = "License action is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "License action is not available"
            self.common_validation.passed(**kwargs)
            return 1

    def check_device_reboot_action(self, device_serial, **kwargs):
        """
        - Assumes that already navigated to Manage --> Devices
        - This method checks if License action is available for a device matching the serial(s)
        - Keyword Usage:
        - ``Check Device License Action ${DEVICE_SERIAL}``

        :param device_serial: device serial number
        :return: int
        """
        self.utils.print_info("Looking for device with serial: ", device_serial)
        self.select_device(device_serial)
        if self.select_device(device_serial):
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.devices_web_elements.get_device_actions_button)

        self.utils.print_info("Checking if License option is displayed")
        reboot_button = self.device_actions.get_device_actions_reboot_menu_item()
        if reboot_button.is_displayed():
            kwargs['fail_msg'] = "Reboot button is available"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Reboot button is not available"
            self.common_validation.passed(**kwargs)
            return 1

    def update_policy_and_configuration_stack(self,  device_serial=None, device_name=None, device_mac=None, **kwargs):
        """
        - This keyword does a config push for a switch, selecting just the "Update Network Policy and Configuration"
        check button in the Device Update dialog.
        - Go To Manage-->Devices-->Select switch row to apply the network policy
        - Select Switch-->Update device
        - Keyword Usage:
        - ``Update Policy and Configuration  ${SWITCH_SERIAL}``
        - ``Update Policy and Configuration  ${SWITCH_MAC}``
        - ``Update Policy and Configuration  ${SWITCH_NAME}``

        :param device_mac: MAC address of the device, by default set to None
        :param device_name: name of the device, by default set to None
        :param device_serial: serial of the device, by default set to None
        :return: 1 if config push success else -1
        """
        self.utils.print_info("Select Stack")
        if not self.select_device(device_serial=device_serial, device_name=device_name, device_mac=device_mac):
            kwargs['fail_msg'] = "The device cannot be selected"
            self.common_validation.fault(**kwargs)
            return -1

        if self._update_switch(update_method="PolicyAndConfig") == -1:
            kwargs['fail_msg'] = "The update cannot be performed"
            self.common_validation.failed(**kwargs)
            return -1

        self.screen.save_screen_shot()
        return self._check_device_update_status(device_serial=device_serial, device_name=device_name, device_mac=device_mac)

    def enable_device_wan_access(self, device_serial, **kwargs):
        """
        - This keyword will enable WAN access for XR or AP as Router mode

        :param device_serial:   The serial of the device
        :return: success 1 else -1
        """
        if not self.navigator.get_devices_page():
            self.utils.print_info("Not in Devices page, now to navigate this page...")
            if self.navigator.navigate_to_devices() == 1:
                self.utils.print_info("To navigate the Devices page successfully...")
            else:
                kwargs['fail_msg'] = "Failed to navigate the Devices page"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("enable_device_wan_access: Already in Devices page, go to next step")
        actions_disabled = False
        try_cnt = 0
        while not actions_disabled:
            if self.select_device(device_serial):
                self.utils.print_info("Check if Actions button is enable")
                if self.device_actions.get_device_actions_button_disable():
                    try_cnt += 1
                    self.utils.print_info(f"Actions button is grayed, can NOT click it, {try_cnt} attempts to try")
                    self.utils.wait_till(self.cloud_driver.refresh_page(), is_logging_enabled=True)
                    actions_disabled = True
                    if try_cnt == 10:
                        kwargs['fail_msg'] = f"Max {try_cnt} attempts reach for active Action button"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    cli_access_none = True
                    try_cnt1 = 0
                    while cli_access_none:
                        self.utils.print_info("Click Actions button ...")
                        self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
                        action_dropdown = self.device_actions.get_device_actions_dropdown()
                        if action_dropdown:
                            self.utils.print_info("Move to Advance button ...")
                            self.auto_actions.move_to_element(self.device_actions.get_device_actions_advance())
                            cli_access = self.device_actions.get_device_actions_advance_cli_access()
                            self.utils.print_info(f"CLI access element: {cli_access}")
                            if cli_access:
                                cli_access_none = False
                                self.utils.print_info(f"Move to CLI Access button {cli_access}...")
                                self.auto_actions.move_to_element(cli_access)
                                self.utils.print_info("Click CLI Access button ...")
                                self.auto_actions.click_reference(self.device_actions.get_device_actions_advance_cli_access)
                                if self.device_actions.get_device_actions_cli_windows():
                                    self.utils.print_info("Send command 'exec bypass-wan-hardening' CLI to input block")
                                    self.auto_actions.send_keys(self.device_actions.get_device_actions_cli_windows_input(), "exec bypass-wan-hardening")
                                    self.utils.print_info("Click Apply button to send CLI to AP ...")
                                    self.auto_actions.click_reference(self.device_actions.get_device_actions_cli_windows_input_apply)
                                    self.utils.print_info("Close CLI windows ...")
                                    self.auto_actions.click_reference(self.device_actions.get_device_actions_cli_windows_close)
                                    return 1
                                else:
                                    kwargs['fail_msg'] = "There is no CLI window popup"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                            else:
                                self.utils.print_info(f"Cli access button is got: {cli_access}, refresh page and try again")
                                try_cnt1 += 1
                                self.utils.wait_till(self.cloud_driver.refresh_page(), is_logging_enabled=True)
                                if try_cnt1 == 10:
                                    kwargs['fail_msg'] = f"Max {try_cnt1} attempts reach for going to cli_access"
                                    self.common_validation.fault(**kwargs)
                                    return -1

                        else:
                            kwargs['fail_msg'] = f"Actions dropdown is NOT shown {action_dropdown}"
                            self.common_validation.fault(**kwargs)
                            return -1
            else:
                kwargs['fail_msg'] = "No device is selected"
                self.common_validation.fault(**kwargs)
                return -1

    def wait_for_policy_config_push_to_complete(self, device_serial, boot_wait_time=60, **kwargs):
        """
        - This method waits until the device is online & managed with status green after a config push
        - Keyword Usage:
        - ``Wait For Policy Config Push To Complete ${DEVICE_SERIAL} ${BOOT_WAIT_TIME}``

        :param device_serial: device serial number
        :param boot_wait_time: time to wait until the device is supposed to have completed the reboot
        :return: 1 if reboot was successful, device is online & managed, status is green else -1
        """

        self.utils.print_info("Sleeping for {} seconds to allow device to come back on line".format(boot_wait_time))
        sleep(boot_wait_time)

        reboot_res = self.wait_until_device_reboots(device_serial, retry_duration=15, retry_count=12)
        if reboot_res == 1:
            self.utils.print_info('Reboot for device with serial number: {} is successful'.format(device_serial))
        else:
            kwargs['fail_msg'] = 'Reboot for device with serial number: {} is NOT successful: {}'.format(device_serial,reboot_res)
            self.common_validation.failed(**kwargs)
            return -1

        online_res = self.wait_until_device_online(device_serial, retry_duration=15, retry_count=12)
        if online_res == 1:
            self.utils.print_info('Device with serial number: {} is online'.format(device_serial))
        else:
            kwargs['fail_msg'] = 'Device with serial number: {} is NOT online: {}'.format(device_serial, online_res)
            self.common_validation.failed(**kwargs)
            return -1

        managed_res = self.wait_until_device_managed(device_serial)
        if managed_res == 1:
            self.utils.print_info('Status for device with serial number: {} is equal to managed'.format(device_serial))
        else:
            kwargs['fail_msg'] = 'Status for device with serial number: {} is NOT equal to managed: {}'.format(device_serial, managed_res)
            self.common_validation.failed(**kwargs)
            return -1

        status_res = self.get_device_status(device_serial=device_serial)
        if status_res == 'green':
            self.utils.print_info('Status for device with serial number: {} is equal to green'.format(device_serial))
        else:
            kwargs['fail_msg'] = 'Status for device with serial number: {} is NOT equal to green: {}'.format(device_serial, status_res)
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = 'Wait for policy config push to device with serial number: {} is complete'
        self.common_validation.passed(**kwargs)
        return 1

    def assign_network_policy_to_a_device(self, device_serial, policy_name, **kwargs):
        """
        - This keyword will assign the network policy to single device
        - flow:
            -- If Not in devices page, go to it
            -- Select the device
            -- Actions
            -- Assign Network Policy
            -- Select the network policy from drop-down window
            -- Assign
        - Keyword Usage:
        - ``Assign Network Policy To A Device  ${device_serial}   ${policy_name}``

        :param policy_name: policy name to be applied
        :param device_serial: serial number of the device
        :return: Success 1 else -1
        """
        if not self.navigator.get_devices_page():
            self.utils.print_info("Not in Devices page, Navigating to devices page now")
            if self.navigator.navigate_to_devices() == 1:
                self.utils.print_info("Navigated to the devices page successfully")
            else:
                kwargs['fail_msg'] = "Failed to navigate to the Devices page"
                self.common_validation.fault(**kwargs)
                return -1
        if self.select_device(device_serial):
            self.utils.print_info("Device is selected ...")
        else:
            kwargs['fail_msg'] = "Failed to Select the device"
            self.common_validation.fault(**kwargs)
            return -1
        if self._assign_network_policy(policy_name):
            kwargs['pass_msg'] = "Network Policy is assigned to selected device"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to assign Network Policy to the device."
            self.common_validation.failed(**kwargs)
            return -1

    def _is_digital_twin_option_visible(self):
        """
        - Add -> Quick Add Devices -> Deploy your devices directly to the cloud -> Cancel button
        - The 'Quick Add Devices' panel will be closed.
        - This helper function returns True if the digital twin option is visible in the Quick Add Devices panel
        else returns False if the digital twin option is hidden in the Quick Add Devices panel, otherwise will fail

        :return: True if visible, False if hidden, fail otherwise
        """
        ret_val = -1
        # Wait until 'loading' mask is cleared
        self.navigator.wait_until_devices_load_spinner_cleared(retry_duration=1, retry_count=180)

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        web_element = self.devices_web_elements.get_devices_quick_add_devices_menu_item()
        self.auto_actions.move_to_element(web_element)

        self.utils.print_info("Selecting Deploy your devices directly to the cloud")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)
        sleep(3)

        if self.devices_web_elements.get_digital_twin_container_feature():
            attribute = self.devices_web_elements.get_digital_twin_container_feature().get_attribute("class")
            self.utils.print_info(f"Class Attribute Value: {attribute}")
            if "fn-hidden" in attribute:
                self.screen.save_screen_shot()
                ret_val = False
            else:
                self.screen.save_screen_shot()
                ret_val = True
        else:
            self.utils.print_info("Digital Twin option not found in Quick Add Devices panel.")
            self.screen.save_screen_shot()

        self.utils.print_info("Click the Quick Add Devices > Cancel button")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)

        if ret_val == True:
            return True
        elif ret_val == False:
            return False
        else:
            kwargs = {'fail_msg': "Failed to check digital twin option"}
            self.common_validation.fault(**kwargs)
            return -1

    def validate_digital_twin_option_visible(self, **kwargs):
        """
        - This Keyword validates if the Digital Twin option is visible within the 'Quick Add Devices' panel.
        - The 'Quick Add Devices' panel will be closed.
        - Keyword Usage:
        - ``Validate Digital Twin Option Visible``

        :return: True if visible, False if not visible
        """
        if self._is_digital_twin_option_visible():
            kwargs['pass_msg'] = "Digital Twin Option is visible"
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "Digital Twin Option is hidden"
            self.common_validation.failed(**kwargs)
            return False

    def validate_digital_twin_option_hidden(self, **kwargs):
        """
        - This Keyword validates if the Digital Twin option is hidden within the 'Quick Add Devices' panel.
        - The 'Quick Add Devices' panel will be closed.
        - Keyword Usage:
        - ``Validate Digital Twin Option Hidden``

        :return: True if hidden, False if visible
        """
        if not self._is_digital_twin_option_visible():
            kwargs['pass_msg'] = "Digital Twin Option is hidden"
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "Digital Twin Option is visible"
            self.common_validation.failed(**kwargs)
            return False

    def get_device_model_list(self, device_type="digital_twin", os_persona="SwitchEngine", **kwargs):
        """
        - This keyword will return a list of Device Models available for Digital Twin or Simulated.
        - It is assumed that the XIQ > Manage > Devices view is already open.
        - Keyword Usage:
         - ''Get Device Model List    device_type="simulated" ''
         - ''Get Device Model List    device_type="digital_twin"    os_persona="FabricEngine" ''

        :param device_type: digital_twin or simulated
        :param os_persona: Digital Twin OS Persona - SwitchEngine or FabricEngine. Not used for Simulated.
        :return: list of device models
        """
        device_model_list = []

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)
        sleep(2)

        if device_type.lower() == "simulated":
            # Based on Code from 'set_onboard_values_for_simulated'
            self.utils.print_info("Selecting 'Simulated' Device Type radio button")
            self.auto_actions.click_reference(self.devices_web_elements.get_quick_onboard_simulated)
            self.utils.print_info("Selecting 'Simulated' Device Model field")
            self.auto_actions.click_reference(self.devices_web_elements.get_simulated_devices_dropdown)
            options = self.devices_web_elements.get_simulated_devices_dropdown_items()
            self.screen.save_screen_shot()
            if options:
                for option in options:
                    self.utils.print_debug(f"Device Model: {option.text}")
                    if option.text.upper() != "--":
                        self.utils.print_debug(f"Adding model: {option.text}")
                        device_model_list.append(option.text)

        elif device_type.lower() == "digital twin":
            attribute = self.devices_web_elements.get_digital_twin_container_feature().get_attribute("class")
            self.utils.print_info(f"attribute value: {attribute}")
            if "fn-hidden" not in attribute:
                self.utils.print_info("Selecting 'Digital Twin' radio button")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_type_digital_twin_radio_button)

                if os_persona and os_persona != "":
                    self.utils.print_info(f"Selecting OS Persona: {os_persona}")
                    self.auto_actions.click_reference(self.devices_web_elements.get_digital_twin_os_persona_dropdown)
                    if self.auto_actions.select_drop_down_options(
                            self.devices_web_elements.get_digital_twin_os_persona_dropdown_items(), os_persona):
                        self.utils.print_info(f"OS Persona set to: {os_persona}")
                    else:
                        kwargs['fail_msg'] = f"Could not select OS Persona: {os_persona}"
                        self.common_validation.fault(**kwargs)
                else:
                    kwargs['fail_msg'] = "Invalid OS Persona value provided..."
                    self.common_validation.fault(**kwargs)

                self.utils.print_info("Clicking Device Model field...")
                self.auto_actions.click_reference(self.devices_web_elements.get_digital_twin_device_model_dropdown)
                sleep(2)
                options = self.devices_web_elements.get_digital_twin_device_model_dropdown_items()
                if options:
                    for option in options:
                        self.utils.print_debug(f"Device Model: {option.text}")
                        if option.text.upper() != "--":
                            self.utils.print_debug(f"Adding model: {option.text}")
                            device_model_list.append(option.text)
                else:
                    kwargs['fail_msg'] = "Could not find the Device Model Field..."
                    self.common_validation.fault(**kwargs)
            else:
                kwargs['fail_msg'] = "Digital Twin option is not available..."
                self.common_validation.fault(**kwargs)
        else:
            kwargs['fail_msg'] = f"Could not select the Device Type: {device_type}"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Click the Quick Add Devices > Cancel button")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)

        if len(device_model_list) > 0:
            kwargs['pass_msg'] = f"Returning Device Model List: {device_model_list}"
            self.common_validation.passed(**kwargs)
            return device_model_list
        elif len(device_model_list) == 0:
            kwargs['fail_msg'] = "Device Model List is empty..."
            self.common_validation.fault(**kwargs)

    def get_device_status_icon(self, device_serial=None):
        """
        - This keyword returns the Device Status icon.
        - Keyword Usage:
        - ``Get Device Status Icon   device_serial=${DEVICE_SERIAL}``

        :param device_serial: device serial number, by default set to None
        :return:
        - 'digital_twin' if Device Status icon is 'Digital Twin'.
        - 'simulated' if Device Status icon is 'Simulated'.
        - 'local_managed' if Device Status icon is 'Local Managed'.
        - 'cloud_managed' if Device Status icon is 'Cloud Managed'.
        - 'unknown' if Device Status icon is 'Unknown'.

        """
        device_row = -1
        self.refresh_devices_page()

        if device_serial and device_serial != "":
            self.utils.print_info("Get Device Status icon for serial: ", device_serial)
            device_row = self.get_device_row(device_serial)

        if device_row:
            sleep(5)
            device_status = self.devices_web_elements.get_status_cell(device_row)
            self.screen.save_screen_shot()

            if device_status:
                if "dt-icon" in device_status:
                    return 'digital_twin'
                elif "sim-icon" in device_status:
                    return 'simulated'
                elif "local" in device_status:
                    return 'local_managed'
                elif "dashboard-icon" in device_status:
                    return 'cloud_managed'
                else:
                    self.utils.print_info("Unable to determine Device Status icon.")
                    return 'unknown'
            else:
                self.utils.print_info("Device Status field was not found.")
                return 'unknown'
        else:
            self.utils.print_info(f"Device row was not found for serial: {device_serial}")
            return 'unknown'

    def cancel_quick_add_devices_panel(self, **kwargs):
        """
        - This Keyword clicks the Cancel button within the 'Quick Add Devices' panel.
        - It is assumed that the 'Quick Add Devices' panel is already visible.
        - Keyword Usage:
        - ``Cancel Quick Add Devices Panel``

        :return: 1 if successful, -1 if not
        """
        self.utils.print_info("Check if the Quick Add Devices panel is visible.")
        attribute = self.devices_web_elements.get_devices_quick_add_device_panel().get_attribute("class")
        self.utils.print_info(f"Class Attribute Value: {attribute}")

        if "show-quick-add" in attribute:
            self.utils.print_info("Click the Quick Add Devices > Cancel button")
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_cancel_button)
            return 1
        else:
            kwargs['fail_msg'] = "The Quick Add Devices panel is not visible"
            self.common_validation.fault(**kwargs)
            return -1

    def select_clone_device(self, device_serial, replacement_device_type, replacement_serial, option="disable", **kwargs):
        """
        - This Keyword clones (Actions -> Clone Device) a single Switch Engine or Fabric Engine switch using device
        level config to another same type SKU switch.

        :param device_serial: Select the device (first device) that you want to clone the configuration for
        the replacement device (second device)
        :param replacement_device_type: Select the type option for replacement device in Cloning process ('Onboarded')
        :param replacement_serial: Select the serial number for replacement device
        :param option: 'enable'/'disable' the checkbox for reboot and rollback the configuration if the IQagent
        loses connectivity during updating the configuration
        :return: 1 if the cloning process is done else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")

        def _navigate_to_devices():
            return self.navigator.navigate_to_devices()

        self.utils.wait_till(_navigate_to_devices)
        select_flag = False
        if device_serial:
            self.select_device(device_serial, skip_navigation=True)
            select_flag = True
        else:
            kwargs['fail_msg'] = "Device is not there"
            self.common_validation.fault(**kwargs)
            return -1

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())

        clone_device = self.device_actions.get_clone_device_btn()

        if clone_device:
            self.utils.print_info("Select Clone device")
            self.auto_actions.click(clone_device)
            replacement_device_dropdown = self.device_actions.get_replacement_device_dropdown()
            if replacement_device_dropdown:
                self.utils.print_info("Select replacement device drop down")
                self.auto_actions.click(replacement_device_dropdown)
                replacement_device_items = self.device_actions.get_replacement_device_items()
                self.utils.print_info(f"Select {replacement_device_type} option")
                if self.auto_actions.select_drop_down_options(replacement_device_items, replacement_device_type):
                    pass
                else:
                    kwargs['fail_msg'] = f"No {replacement_device_type} option selected"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "No replacement device option found"
                self.common_validation.fault(**kwargs)
                return -1

            replacement_serial_number_dropdown = self.device_actions.get_replacement_serial_number_dropdown()
            if replacement_serial_number_dropdown:
                self.utils.print_info("Select Replacement serial number")
                self.auto_actions.click(replacement_serial_number_dropdown)
                replacement_serial_number_items = self.device_actions.get_replacement_serial_number_items()
                self.utils.print_info(f"Select {replacement_serial} serial number")
                if self.auto_actions.select_drop_down_options(replacement_serial_number_items, replacement_serial):
                    pass
                else:
                    kwargs['fail_msg'] = f"No {replacement_serial} serial selected"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "No replacement serial number option found"
                self.common_validation.fault(**kwargs)
                return -1

            clone_button = self.device_actions.get_clone_button()
            if clone_button:
                self.utils.print_info("Select Clone button")
                self.auto_actions.click(clone_button)
                yes_confirmation_button = self.device_actions.get_yes_confirmation_button()
                if yes_confirmation_button:
                    self.utils.print_info(f"Select yes to clone {replacement_serial} serial")
                    self.auto_actions.click(yes_confirmation_button)
                else:
                    kwargs['fail_msg'] = "No confirm message buttons found"
                    self.common_validation.fault(**kwargs)
                    return -1

            def _loading_clone():
                loading_clone_configuration = self.device_actions.get_loading_clone_configuration()
                while loading_clone_configuration and "fn-hidden" not in loading_clone_configuration.get_attribute("class"):
                    print("Still loading configuration")
                    sleep(2)
                    loading_clone_configuration = self.device_actions.get_loading_clone_configuration()
                return 1
            self.utils.wait_till(_loading_clone, exp_func_resp=1)
            try:
                warning_message_disconnected = self.device_actions.get_warning_message_disconnected()
                while warning_message_disconnected and "fn-hidden" in warning_message_disconnected.get_attribute("class"):
                    print("Still in loading clone configuration window..Waiting for Perform Update window or Warning window.")
                    warning_message_disconnected = self.device_actions.get_warning_message_disconnected()
                    sleep(2)
                if "fn-hidden" not in warning_message_disconnected.get_attribute("class"):
                    warning_message_disconnected = True
            except Exception:
                warning_message_disconnected = False

            if not warning_message_disconnected:
                self.utils.print_info("Performing Update")
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
                    kwargs['fail_msg'] = "Network policy and configuration checkbox not found"
                    self.common_validation.fault(**kwargs)
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
                    kwargs['fail_msg'] = "Reboot and revert switch configuration checkbox not found"
                    self.common_validation.fault(**kwargs)
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
            else:
                kwargs['fail_msg'] = "The device clone - successfully completed, but the device " \
                                     "cannot be updated at this time as it's disconnected or in the unmanaged state"
                cancel_button = self.device_actions.get_cancel_button()
                self.utils.print_info("Closing the Clone window")
                self.screen.save_screen_shot()
                self.auto_actions.click(cancel_button)
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "No clone device button from Actions found"
            self.common_validation.fault(**kwargs)
            return -1

    def clone_device_quick_onboard(self, device_serial, replacement_device_type, replacement_serial,
                                   perform_update=False, option="disable", continue_if_replacement_disconnected=False,
                                   **kwargs):
        """
        - This Keyword clones (Actions -> Clone Device) a single Switch Engine or Fabric Engine switch using device
        level config to another same type SKU switch.
        :param device_serial: Select the device (first device) that you want to clone the configuration for
                              the replacement device (second device)
        :param replacement_device_type: Select the type option for replacement device in Cloning process
                                        ('Onboarded', 'Quick Onboard')
        :param replacement_serial: The serial number for replacement device
        :param perform_update: if True, the config cloned will be pushed to device. By default is false.
        :param option: "enable"/"disable" the checkbox for reboot and rollback the configuration if the IQagent loses
                        connectivity during updating the configuration. Used only if perform_update=True.
                        By default is "disable"
        :param continue_if_replacement_disconnected: if True, if the replacement does not connect within 40 sec to
                                                    cloud, cloning process will continue
                                                    if False, if the replacement does not connect within 40 sec to
                                                    cloud, cloning process will not continue and return -1
                                                    By default is False
        :return: 1 if the cloning process is done else -1
        """

        self.utils.print_info("Navigate to Manage-->Devices")

        def _navigate_to_devices():
            return self.navigator.navigate_to_devices()

        self.utils.wait_till(_navigate_to_devices)
        select_flag = False
        if device_serial:
            self.select_device(device_serial)
            select_flag = True
        else:
            kwargs['fail_msg'] = "Device is not there"
            self.common_validation.fault(**kwargs)
            return -1

        if select_flag:
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())

        clone_device = self.device_actions.get_clone_device_btn()

        if clone_device:
            self.utils.print_info("Select Clone device")
            self.auto_actions.click(clone_device)
            replacement_device_dropdown = self.device_actions.get_replacement_device_dropdown()
            if replacement_device_dropdown:
                self.utils.print_info("Select replacement device drop down")
                self.auto_actions.click(replacement_device_dropdown)
                replacement_device_items = self.device_actions.get_replacement_device_items()
                self.utils.print_info(f"Select {replacement_device_type} option")
                if self.auto_actions.select_drop_down_options(replacement_device_items, replacement_device_type):
                    pass
                else:
                    kwargs['fail_msg'] = f"No {replacement_device_type} option selected"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "No replacement device option found"
                self.common_validation.fault(**kwargs)
                return -1

            if replacement_device_type == "Onboarded":
                replacement_serial_number_dropdown = self.device_actions.get_replacement_serial_number_dropdown()
                if replacement_serial_number_dropdown:
                    self.utils.print_info("Select Replacement serial number")
                    self.auto_actions.click(replacement_serial_number_dropdown)
                    replacement_serial_number_items = self.device_actions.get_replacement_serial_number_items()
                    self.utils.print_info(f"Select {replacement_serial} serial number")
                    if self.auto_actions.select_drop_down_options(replacement_serial_number_items, replacement_serial):
                        pass
                    else:
                        kwargs['fail_msg'] = f"No {replacement_serial} serial selected"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "No replacement serial number option found"
                    self.common_validation.fault(**kwargs)
                    return -1

                clone_button = self.device_actions.get_clone_button()
                if clone_button:
                    self.utils.print_info("Select Clone button")
                    self.auto_actions.click(clone_button)

                    clone_inform_window = self.device_actions.get_clone_inform_window()
                    if clone_inform_window:
                        yes_confirmation_button = self.device_actions.get_yes_confirmation_button()
                        if yes_confirmation_button:
                            self.utils.print_info(f"Select yes to clone {replacement_serial} serial")
                            self.auto_actions.click(yes_confirmation_button)
                        else:
                            kwargs['fail_msg'] = "No confirm message buttons found"
                            self.common_validation.fault(**kwargs)
                            return -1

                    self.utils.wait_till()

                warning_message_disconnected = self.device_actions.get_warning_message_disconnected()
                if warning_message_disconnected:
                    if 'disconnected or in the unmanaged state' not in warning_message_disconnected.text:
                        if perform_update:
                            self.utils.print_info("Performing Update")
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
                                kwargs['fail_msg'] = "Network policy and configuration checkbox not found"
                                self.common_validation.fault(**kwargs)
                                return -1

                            if reboot_rollback_check:
                                if option.lower() == "enable":
                                    if not reboot_rollback_check.is_selected():
                                        self.utils.print_info("Check reboot and revert switch configuration option")
                                        self.auto_actions.click(reboot_rollback_check)
                                        self.utils.wait_till(timeout=2)

                                    else:
                                        self.utils.print_info("Reboot/revert already checked")
                                if option.lower() == "disable":
                                    if not reboot_rollback_check.is_selected():
                                        self.utils.print_info("Reboot/revert option already unchecked")
                                        self.utils.wait_till(timeout=2)

                                    else:
                                        self.utils.print_info("Uncheck reboot and revert switch configuration option")
                                        self.auto_actions.click(reboot_rollback_check)
                                        self.utils.wait_till(timeout=2)

                            else:
                                kwargs['fail_msg'] = "Reboot and revert switch configuration checkbox not found"
                                self.common_validation.fault(**kwargs)
                                return -1

                            self.utils.print_info("Click on perform update button")
                            self.auto_actions.click(self.devices_web_elements.get_devices_switch_update_btn())
                            self.utils.wait_till(timeout=3)

                            if option.lower() == "enable":
                                self.utils.print_info("Proceed yes that user wants to continue with reboot/revert option")
                                self.auto_actions.click(self.devices_web_elements.get_devices_update_yes_btn())
                                self.utils.wait_till(timeout=2)

                            else:
                                pass
                            kwargs['pass_msg'] = "Clone successful"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:

                            close_button = self.device_actions.get_close_button()
                            self.utils.print_info("Closing the Clone window")
                            self.screen.save_screen_shot()
                            self.auto_actions.click(close_button)
                            self.utils.print_info("Navigate to Manage-->Devices")

                            def _navigate_to_devices():
                                return self.navigator.navigate_to_devices()

                            self.utils.wait_till(_navigate_to_devices)
                            kwargs['pass_msg'] = "Clone successful"
                            self.common_validation.passed(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("The device clone has been successfully completed, but the device cannot "
                                              "be updated at this time as it's disconnected or in the unmanaged state.")
                        cancel_button = self.device_actions.get_cancel_button()
                        if cancel_button:
                            self.utils.print_info("Closing the Device Update window")
                            self.screen.save_screen_shot()
                            self.auto_actions.click(cancel_button)

                        else:
                            kwargs['fail_msg'] = "No Close button found"
                            self.common_validation.fault(**kwargs)
                            return -1

                        self.utils.print_info("Navigate to Manage-->Devices")

                        def _navigate_to_devices():
                            return self.navigator.navigate_to_devices()

                        self.utils.wait_till(_navigate_to_devices)
                        kwargs['pass_msg'] = "Clone successful"
                        self.common_validation.passed(**kwargs)

            elif replacement_device_type == "Quick Onboard":
                replacement_serial_number_field = self.device_actions.get_replacement_serial_number_field()
                if replacement_serial_number_field:
                    self.utils.print_info("Entering  Replacement Serial Number...")
                    self.auto_actions.send_keys(replacement_serial_number_field, replacement_serial)
                    self.utils.print_info(f"Entering {replacement_serial} SN")
                else:
                    kwargs['fail_msg'] = "No replacement serial number field found"
                    self.common_validation.fault(**kwargs)
                    return -1

                clone_button = self.device_actions.get_clone_button_quick_onboard()
                if clone_button:
                    self.utils.print_info("Select Clone button")
                    self.auto_actions.click(clone_button)

                    self.utils.wait_till(timeout=55, delay=10)

                    warning_replacement_different_type = self.device_actions.get_warning_replacement_different_type()
                    if warning_replacement_different_type:
                        self.screen.save_screen_shot()
                        x_button_clone_window = self.device_actions.get_x_button_clone_window()
                        self.auto_actions.click(x_button_clone_window)
                        self.utils.print_info("Navigate to Manage-->Devices")
                        kwargs['fail_msg'] = "Original Device Product type and Replacement Device Product Type does " \
                                             "not match. Cannot proceed with Device Cloning."
                        self.common_validation.fault(**kwargs)
                        return -1
                    else:
                        pass

                    clone_inform_window_replacement_not_connected = self.device_actions.\
                        get_clone_inform_window_replacement_not_connected()
                    if clone_inform_window_replacement_not_connected:
                        if continue_if_replacement_disconnected:
                            yes_confirmation_button = self.device_actions.get_yes_confirmation_button()
                            if yes_confirmation_button:
                                self.utils.print_info(f"Select yes to clone {replacement_serial} serial")
                                self.auto_actions.click(yes_confirmation_button)
                            else:
                                kwargs['fail_msg'] = "No confirm message buttons found"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            no_confirmation_button = self.device_actions.get_no_confirmation_button()
                            if no_confirmation_button:
                                self.utils.print_info(f"Select No to clone {replacement_serial} serial, "
                                                      "because doesn't connect in time")
                                self.auto_actions.click(no_confirmation_button)
                                self.utils.wait_till()
                                kwargs['fail_msg'] = "Clonning process unsuccessful. Replacement device doesn't " \
                                                     "connect in time and process has been aborted."
                                self.common_validation.fault(**kwargs)
                                return -1
                            else:
                                kwargs['fail_msg'] = "No confirm message buttons found"
                                self.common_validation.fault(**kwargs)
                                return -1
                    else:
                        clone_inform_window = self.device_actions.get_clone_inform_window()
                        if clone_inform_window:
                            yes_confirmation_button = self.device_actions.get_yes_confirmation_button()

                            if yes_confirmation_button:
                                self.utils.print_info(f"Select yes to clone {replacement_serial} serial")
                                self.auto_actions.click(yes_confirmation_button)
                            else:
                                kwargs['fail_msg'] = "No confirm message buttons found"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            pass
                else:
                    kwargs['fail_msg'] = "No clone button found"
                    self.common_validation.fault(**kwargs)
                    return -1

                if perform_update:
                    self.utils.print_info("Performing Update")
                    self.utils.print_info("Select the network policy and configuration checkbox")
                    update_cb = self.devices_web_elements.get_devices_switch_update_network_policy()
                    reboot_rollback_check = self.devices_web_elements.get_devices_switch_update_reboot_rollback()
                    self.utils.wait_till(timeout=3)

                    if update_cb:
                        if update_cb.is_selected():
                            self.utils.print_info("Network policy and configuration checkbox is already selected")
                            self.utils.wait_till(timeout=2)

                        else:
                            self.utils.print_info("Clicking network policy and configuration checkbox")
                            self.auto_actions.click(update_cb)
                            self.utils.wait_till(timeout=2)

                    else:
                        kwargs['fail_msg'] = "Network policy and configuration checkbox not found"
                        self.common_validation.fault(**kwargs)
                        return -1

                    if reboot_rollback_check:
                        if option.lower() == "enable":
                            if not reboot_rollback_check.is_selected():
                                self.utils.print_info("Check reboot and revert switch configuration option")
                                self.auto_actions.click(reboot_rollback_check)
                                self.utils.wait_till(timeout=2)

                            else:
                                self.utils.print_info("Reboot/revert already checked")
                        if option.lower() == "disable":
                            if not reboot_rollback_check.is_selected():
                                self.utils.print_info("Reboot/revert option already unchecked")
                                self.utils.wait_till(timeout=2)

                            else:
                                self.utils.print_info("Uncheck reboot and revert switch configuration option")
                                self.auto_actions.click(reboot_rollback_check)
                                self.utils.wait_till(timeout=2)

                    else:
                        kwargs['fail_msg'] = "Reboot and revert switch configuration checkbox not found"
                        self.common_validation.fault(**kwargs)
                        return -1

                    self.utils.print_info("Click on perform update button")
                    self.auto_actions.click(self.devices_web_elements.get_devices_switch_update_btn())
                    self.utils.wait_till(timeout=3)

                    if option.lower() == "enable":
                        self.utils.print_info("Proceed yes that user wants to continue with reboot/revert option")
                        self.auto_actions.click(self.devices_web_elements.get_devices_update_yes_btn())
                        self.utils.wait_till(timeout=2)

                    else:
                        pass
                    kwargs['pass_msg'] = "Clone successful"
                    self.common_validation.passed(**kwargs)
                    return 1

                else:
                    self.utils.wait_till()
                    close_button = self.device_actions.get_close_button()
                    if close_button:

                        self.utils.print_info("Closing the Device Update window")
                        self.screen.save_screen_shot()
                        self.auto_actions.click(close_button)
                        kwargs['pass_msg'] = "Clone successful"
                        self.common_validation.passed(**kwargs)
                    else:
                        kwargs['fail_msg'] = "No Close button found"
                        self.common_validation.fault(**kwargs)
                        return -1

                    self.utils.print_info("Navigate to Manage-->Devices")

                    def _navigate_to_devices():
                        return self.navigator.navigate_to_devices()

                    self.utils.wait_till(_navigate_to_devices)
                    self.refresh_devices_page()

            else:
                kwargs['fail_msg'] = "No replacement type was selected"
                self.common_validation.fault(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "No clone device button from Actions found"
            self.common_validation.fault(**kwargs)
            return -1

    def confirm_not_enough_copilot_licenses_message_displayed(self, **kwargs):
        """
        - This keyword confirms if the "CoPilot licenses" warning banner message is displayed or not
        - Keyword Usage
        - ``Confirm Not Enough CoPilot Licenses Message Displayed``

        :return: true if banner is displayed and return false if banner is not displayed
        """

        if self.devices_web_elements.get_ui_banner_warning_message():
            tool_tp_text_warning = self.devices_web_elements.get_ui_banner_warning_message()
            message = tool_tp_text_warning.text
            if "add CoPilot licenses" in message:
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = f" Banner message: {message}"
                self.common_validation.passed(**kwargs)
                return True
            else:
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = f"Banner message: {message}"
                self.common_validation.failed(**kwargs)
                return False

        else:
            kwargs['fail_msg'] = "CoPilot License warning message banner not displayed"
            self.common_validation.failed(**kwargs)
            return False

    def check_100_rows_per_page_button(self):
        """
        - This keyword check if 100 rows per page button is present in Devices
        - If the button is present, it will be clicked
        - If the button is not present, it will ignore
        - It is assumed that 'Devices' page is open

        :return:
        """
        self.utils.print_info("Searching for 100 rows per page button")
        one_hundred_devices_per_page = self.devices_web_elements.get_100_rows_per_page_button()
        if one_hundred_devices_per_page:
            self.utils.print_info("Found 100 rows per page button")
            self.auto_actions.click(one_hundred_devices_per_page)
        else:
            self.utils.print_info("Didn't find 100 rows per page button... Continuing run...")

    def get_device_updated_fail_message_after_reboot(self, device_serial=None, device_mac=None, **kwargs):
        """
        This keyword gets information of the update failed status in XIQ for a device after reboot/rollback
        configuration

        :param device_serial: Gets the information of the update failed status based on serial number, by default set to None
        :param device_mac:  Gets the information of the update failed status based on address MAC, by default set to None
        :return: status if the information was found else -1
        """
        if device_serial:
            self.select_device(device_serial=device_serial)
        if device_mac:
            self.select_device(device_mac=device_mac)
        self.utils.print_info("Checking the update the status")
        sleep(5)
        status = self.devices_web_elements.get_status_update_failed_after_reboot()
        if status is not None and "The device was rebooted and reverted to previous configuration" in status:
            kwargs['pass_msg'] = f"Update status: {status}"
            self.common_validation.passed(**kwargs)
            return status
        else:
            kwargs['fail_msg'] = "Update status not found"
            self.common_validation.failed(**kwargs)
            return -1

    def get_device_model(self, mac, **kwargs):
        """
        - This keyword will get the device model string from a device row using the mac
        - This string returned can be used to create a template for the device
        - It is assumed that 'Devices' page is already open

        :param mac: The mac address of the device
        :return: a string containing the name of the model [Ex: Fabric Engine 5520-24T]; -1 if getting the string fails
        """

        if self.navigator.navigate_to_devices() != 1:
            kwargs['fail_msg'] = "Failed on navigating to the Devices page."
            self.common_validation.fault(**kwargs)
            return -1

        # Enable the 'Model' Column
        self.column_picker_select('Model')

        self.utils.print_info(f"Searching for the device row with mac address: {mac}")
        device_row = self.get_device_row(device_mac=mac)
        if device_row:
            self.utils.print_info(f'Found the device row with mac address: {mac}')
            device_model = self.devices_web_elements.get_device_model(device_row).text
            print("Device model: ", device_model)
            if device_model:
                kwargs['pass_msg'] = f"Found the device model: {device_model} for the device with " \
                                     f"MAC address: {mac}"
                self.common_validation.passed(**kwargs)
                return device_model
            else:
                kwargs['fail_msg'] = f"Failed on getting the device model from the device with mac: {mac} "
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = f"Did not find any rows with mac address: {mac}"
            self.common_validation.failed(**kwargs)
            return -1

    def revert_device_to_template_but_donot_update(self, device_mac, **kwargs):
        """
        - Assumes already navigated to Manage --> Devices
        - This method accesses the "Revert Device to Template" action but it will not deploy for a device matching
        the specified mac
        - Keyword Usage:
        - ``Revert Device to Template  ${DEVICE_SERIAL}``
        :param device_mac: mac of the device to perform the action on

        :return: 1 if action succeeds, else -1
        """
        self.utils.print_info("Reverting Device to Template for device with serial: ", device_mac)

        if self.device_common.select_device_row(device_mac=device_mac):
            self.utils.print_info("Selecting 'Actions' button")
            actions_btn = self.device_actions.get_device_actions_button()
            if actions_btn:
                self.auto_actions.click(actions_btn)
                # sleep(2)
            else:
                kwargs['fail_msg'] = "Could not click 'Actions' button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Selecting 'Revert Device to Template' menu item")
            revert_menu = self.device_actions.get_device_actions_revert_device_to_template_menu_item()
            if revert_menu:
                self.auto_actions.click(revert_menu)
                # sleep(4)
                self.utils.wait_till(delay=2, timeout=4)
            else:
                kwargs['fail_msg'] = "Could not click 'Revert Device to Template' menu item"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Clicking 'Save' button")
            save_btn = self.dialogue_web_elements.get_confirm_yes_button()
            if save_btn:
                self.auto_actions.click(save_btn)
                self.utils.wait_till(delay=2, timeout=4)
            else:
                kwargs['fail_msg'] = "Could not click 'Save' button"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Clicking 'cancel' button")
            cancel_btn = self.devices_web_elements.get_more_row_description_close()

            self.utils.print_info("Cancel Button==> ", cancel_btn)
            if type(cancel_btn) != list:
                if cancel_btn:
                    self.auto_actions.click(cancel_btn)

                    # sleep(3)

                    def check_revert_box_available():
                        return not bool(self.dialogue_web_elements.get_confirm_yes_button())

                    self.utils.wait_till(check_revert_box_available, timeout=3, delay=1,
                                         is_logging_enabled=True)
                else:
                    kwargs['fail_msg'] = "Could not click 'Cancel' button"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                for eachbutton in cancel_btn:
                    try:
                        if eachbutton.is_enabled() and eachbutton.is_displayed():
                            eachbuttonclick = self.auto_actions.click(eachbutton)
                            self.utils.print_info("Trying to click the button ", eachbuttonclick)
                            if eachbuttonclick:
                                return 1
                    except Exception as e:
                        self.utils.print_info(f"Cannot click the button {e}")

            return 1
        else:
            kwargs['fail_msg'] = f"Could not select device with mac {device_mac}"
            self.common_validation.fault(**kwargs)
            return -1

    def get_latest_version_from_device_update(self, dut, **kwargs):
        """
        - This method returns the latest os version from device update

        :param device_serial: dut object
        :return: latest version
        """

        device_serial = dut.serial
        latest_version = -1
        sleep(5)

        if self.select_device(device_serial):
            def _click_update_devices_button():
                return self.auto_actions.click(DeviceUpdate().get_update_devices_button())

            self.utils.wait_till(_click_update_devices_button, timeout=30, delay=20,
                                 msg="Selecting Update Devices button")

            checkbox_status = DeviceUpdate().get_upgrade_IQ_engine_and_extreme_network_switch_images_checkbox_status()

            if checkbox_status == "true":
                self.utils.print_info("Upgrade IQ Engine and Extreme Network Switch Images checkbox is already checked")
            else:
                def _click_upgrade_iq_engine_button():
                    return self.auto_actions.click(DeviceUpdate().get_upgrade_iq_engine_checkbox())

                self.utils.wait_till(_click_upgrade_iq_engine_button, timeout=30, delay=20,
                                     msg="Selecting upgrade IQ Engine checkbox")

            self.utils.print_info("Selecting upgrade to latest version checkbox")
            self.auto_actions.click(DeviceUpdate().get_upgrade_to_latest_version_radio())
            sleep(2)

            latest_version = DeviceUpdate().get_latest_version()
            sleep(3)

            self.utils.print_info("Selecting Close button...")
            self.auto_actions.click_reference(ClientWebElements().get_client_dialog_window_close_button)
            sleep(3)

            kwargs["pass_msg"] = f"Successfully found the latest version: {latest_version}"
            self.common_validation.passed(**kwargs)

            return latest_version

        kwargs["fail_msg"] = f"Couldn't select device with serial: {dut.serial}"
        self.common_validation.failed(**kwargs)
        return None

    def check_update_column_by_failure_message(self, device_serial, failure_message, **kwargs):
        """
        This function is used to check the UPDATED column from device grid from a device with device_serial given as
        parameter. Check if the update process failed with the same message as failure_message given as parameter

        :param device_serial: device serial number to check the config push status
        :param failure_message: failure message that is expected to appear after Device Update Failed
        :return: 1 - if the update process failed with the same message as failure_message ; -1 - if not
        """
        current_status = self.get_device_updated_status(device_serial=device_serial)
        count = 0
        max_wait = 900
        current_date = datetime.now()
        update_text = str(current_date).split()[0]

        while "Device Update Failed" != current_status:

            sleep(10)
            count += 10
            self.utils.print_info(f"\nINFO \t Time elapsed in the Update process is '{count} seconds'\n")

            current_status = self.get_device_updated_status(device_serial=device_serial)

            if update_text in current_status:
                kwargs["fail_msg"] = "Update process ended up successfully which is not expected"
                self.common_validation.failed(**kwargs)
                return -1

            if count > max_wait:
                kwargs["fail_msg"] = f"Max time {max_wait} seconds exceeded which is not expected"
                self.common_validation.failed(**kwargs)
                return -1

        current_message = self.get_device_updated_fail_message_after_reboot(device_serial=device_serial, ignore_failure=True)

        if failure_message != current_message:
            kwargs["fail_msg"] = f"Update process ended up with another failure message: {current_message}"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = f"Successfully found the expected failure message: {failure_message}"
        self.common_validation.passed(**kwargs)
        return 1

    def wait_for_update_column_status_change(self, device_serial):
        """
        - This method waits for the device update column to cahnge status and keeps track of how much time it took

        :param device_serial: serial number of the device
        :param status_before: the status before the update began
        """
        # Foremerly check_update_column_2
        count = 0
        max_wait = 300
        status = self.get_device_updated_status(device_serial=device_serial)
        while not status and count < max_wait:
            sleep(10)
            count += 10
            status = self.get_device_updated_status(device_serial=device_serial)
            print(
                f"\nINFO \t Time elapsed in the update column to reflect the firmware updating is '{count} seconds'\n")

    def update_and_wait_device(self, policy_name, dut, wait=True, **kwargs):
        """Method that updates the switch and then wait for the update to finish.

        Args:
            policy_name (str): the name of the policy
            dut (dict): the dut (e.g. tb.dut1)
            wait (bool): if True then the function waits for the update to end

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.wait_till(timeout=10)
        self._goto_devices()
        self.utils.wait_till(timeout=10)

        self.utils.print_info(f"Select switch row with serial {dut.mac}")

        if self.select_device(device_mac=dut.mac) != 1:
            kwargs["fail_msg"] = f"Switch {dut.mac} is not present in the grid"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info(f"Successfully selected {dut.mac} in the grid")
        self.utils.wait_till(timeout=2)

        if self._update_switch(update_method="PolicyAndConfig") != 1:
            kwargs["fail_msg"] = f"Failed to push the update to switch {dut.mac}"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info(f"Successfully pushed the update to switch {dut.mac}")

        if wait:

            self.utils.print_info("Wait for the update to end")

            if self._check_update_network_policy_status(policy_name, dut.mac) != 1:
                kwargs["fail_msg"] = f"The update for switch {dut.mac} is not successful"
                self.common_validation.failed(**kwargs)
                return -1

        kwargs["pass_msg"] = f"Successfully updated the switch {dut.mac}"
        self.common_validation.passed(**kwargs)
        return 1

    def check_update_column_change(self, device_serial, status_before, **kwargs):
        '''
        - Check to see that the update column changes status

        :param device_serial: the dut serial
        :param status_before: the dut status before change
        '''

        print(f"Status before: {status_before}")
        status_after = self.get_device_updated_status(device_serial=device_serial)
        count = 0
        max_wait = 900
        current_date = datetime.now()
        update_text = str(current_date).split()[0]

        while update_text not in status_after:
            sleep(10)
            count += 10
            status_after = self.get_device_updated_status(device_serial=device_serial)
            print(
                f"\nINFO \t Time elapsed in the update column to reflect the firmware updating is '{count} seconds'\n")
            if ("Failed" in status_after) or ("failed" in status_after) or (count > max_wait):
                kwargs["fail_msg"] = "Device update failed"
                self.common_validation.fault(**kwargs)

        print(f"Status after: {status_after}")
        if status_before != status_after:
            kwargs["pass_msg"] = "Successfully changed the UPDATED status"
            self.common_validation.passed(**kwargs)
        else:
            kwargs["fail_msg"] = f"Failed to change the status from {status_before}"
            self.common_validation.failed(**kwargs)

    def deploy_switch_network_policy_with_complete_update(self, device_serial, policy_name):
        """
        - Deploy Switch Network Policy With Complete Update
        - Will deploy a policy to a device assuming policy exists
        - Keyword Usage:
          - ``Deploy Switch Network Policy With Complete Update   ${POLICY_NAME}    ${DEVICE_MAC}``
        :param policy_name: Name of the policy
        :param device_serial: Device serial number
        :return: 1 if success else -1
        """
        return_value = self.assign_network_policy_to_a_device(device_serial, policy_name)
        if return_value == 1:
            return_value = self.update_switch_policy_and_configuration(device_serial)
        return return_value

    def restart_pse_function(self, dut, **kwargs):
        """
        - This method restarts the PSE profile
        - Selecting the Switch Engine device -> Utilities -> Restart PSE
        :param dut: DUT Device
        :return: 1 if the PSE reset have been completed else -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        self.refresh_devices_page()

        if dut.cli_type.upper() in ["EXOS", "SWITCH ENGINE"]:
            self.utils.print_info("Select the device")
            if dut.platform.lower() == "stack":
                self.select_device(device_mac=dut.mac)
            elif dut.platform.lower() != "stack":
                self.select_device(device_serial=dut.serial)
            elif dut is None:
                kwargs['fail_msg'] = "Unable to select device because device_serial or device_mac was not provided"
                self.common_validation.failed(**kwargs)
                return -1
            self.utils.print_info("Selecting the Utilities Function")
            self.auto_actions.click_reference(self.devices_web_elements.utilities_button)
            self.utils.print_info("Selecting RESTART PSE Function...")
            self.auto_actions.click_reference(self.devices_web_elements.restart_pse)
            self.utils.print_info("Confirmation Pending..")
            self.auto_actions.click_reference(self.devices_web_elements.pse_yes)

            def _widget_loading():
                widget_loading = self.devices_web_elements.loading_bar()
                try:
                    if widget_loading.is_displayed():
                        self.utils.print_info("Please wait.. Restarting PSE in progress")
                except AttributeError:
                    return 1
            self.utils.wait_till(func=_widget_loading, timeout=100, delay=5, exp_func_resp=1)

            closing_dialog = self.devices_web_elements.closing_window
            if closing_dialog:
                pse_reset_status = self.devices_web_elements.get_pse_reset_status()
                if pse_reset_status:
                    kwargs['pass_msg'] = "PSE reset has been completed."
                    self.common_validation.passed(**kwargs)
                self.utils.print_info("Closing PSE Window..")
                self.auto_actions.click_reference(closing_dialog)
                kwargs['pass_msg'] = "Window Closed"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Something went wrong. User should check..."
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = f"The function was not designed for {dut.cli_type} OS System"
            self.common_validation.fault(**kwargs)
            return -1

    def get_device_latest_version(self, dut, **kwargs):
        """
        - This method is used to get the device latest version
        - dut - dut from .yaml testbed file (ex: ap1, netelem1}
        - Keyword Usage:
        - ``Get Device Latest Version   ${device1}``

        :return: returned_version of the device
        """
        latest_version = -1
        device_selected = False

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        self.refresh_devices_page()

        if self.select_device(device_mac=dut.mac):
            device_selected = True
        elif self.select_device(device_serial=dut.serial):
            device_selected = True

        if device_selected:
            self.utils.print_info("Selecting Update Devices button")
            self.auto_actions.click_reference(self.device_update.get_update_devices_button)

            found_element_upnp = None
            for tries in range(10):
                found_element_upnp = self.devices_web_elements.get_devices_switch_update_network_policy()
                if found_element_upnp:
                    break
                sleep(1)
            if found_element_upnp.is_selected():
                self.utils.print_info("uncheck the update configuration checkbox")
                self.auto_actions.click(found_element_upnp)

            self.utils.print_info("Selecting upgrade IQ Engine checkbox")
            self.auto_actions.click_reference(self.device_update.get_upgrade_iq_engine_checkbox)

            self.utils.print_info("Selecting upgrade to latest version checkbox")
            self.auto_actions.click_reference(self.device_update.get_upgrade_to_latest_version_radio)

            found_element_latest_version = None
            for tries in range(10):
                found_element_latest_version = self.device_update.get_latest_version()
                if found_element_latest_version:
                    break
                sleep(1)

            latest_version = found_element_latest_version
            self.utils.print_info("Device Latest Version: ", latest_version)
            self.auto_actions.click_reference(self.device_update.get_update_close_button)
            return latest_version

        kwargs['fail_msg'] = f"get_device_latest_version() failed. Device using MAC: {dut.mac} " \
                             f"or serial number: {dut.serial} was not found thus failed to get it"
        self.common_validation.failed(**kwargs)
        return latest_version

    def delete_simulated_device(self, device_model, **kwargs):
        """
        - Deletes Simulated Device from the device grid based on device model
        - Keyword Usage:
         - ``Delete Simulated device   ${DEVICE_MODEL}``
        :param device_model: Model of the Device Example: AP410C, AP460C
        :return: 1 if simulated device deleted successfully else -1
        """
        self.utils.print_info("Searching Simulated Device with Model: ", device_model)
        search_result = self._search_simulated_devices(device_model)

        if search_result:
            if self.select_device(device_model):
                self.auto_actions.click(self.devices_web_elements.get_delete_button())
                self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())

                if self._search_simulated_devices(device_model) != 1:
                    kwargs['fail_msg'] = f"Unable to find the Simulated Device with Model{device_model}"
                    self.common_validation.failed(**kwargs)
                    return -1
                else:
                    kwargs['pass_msg'] = f"Deleted Simulated Device with Model {device_model} Successfully"
                    self.common_validation.passed(**kwargs)
                    return 1
        else:
            kwargs['fail_msg'] = f"Unable to find the Simulated Device with Model{device_model} in Devices Grid"
            self.common_validation.failed(**kwargs)
            return -1

    def delete_simulated_devices(self, device_model, **kwargs):
        """
        - Delete all Simulated devices from the device grid based on device model
        - Keyword Usage:
         - ``Delete Simulated devices    ${DEVICE_MODEL}``
        :param device_model: model of the Device Example: AP410C, AP460C
        :return: 1 if simulated devices deleted  successfully else -1
        """
        self.utils.print_info("Searching Simulated Device with Model: ", device_model)
        search_result = self._search_simulated_devices(device_model)

        self.utils.print_info("Getting Simulated Devices Row with Model: ", device_model)
        rows = self.devices_web_elements.get_simulated_devices_grid_rows()
        if search_result and rows:
            for row in rows:
                self.utils.print_info("Selecting Simulated Device Row ", self.format_row(row.text))
                self.auto_actions.click_reference(lambda: self.devices_web_elements.get_device_select_checkbox(row))
                self.screen.save_screen_shot()
            self.utils.print_info("Clicking Delete Button")
            self.auto_actions.click(self.devices_web_elements.get_delete_button())
            self.utils.print_info("Clicking Delete Confirmation Button")
            self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())

        self.refresh_devices_page()
        if self._search_simulated_devices(device_model) == 1:
            kwargs['fail_msg'] = f"Simulated Device with Model {device_model} still exists in Devices Page"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = f"Deleted Simulated Device with Model {device_model} Successfully"
            self.common_validation.passed(**kwargs)
            return 1
