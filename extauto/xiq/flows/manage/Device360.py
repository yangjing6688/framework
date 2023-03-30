import re
import time
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.Device360WebElements import Device360WebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
from extauto.xiq.flows.manage.DeviceConfig import DeviceConfig
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.manage.Tools import Tools
import random
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend


class Device360(Device360WebElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.screen = Screen()
        self.dev = Devices()
        self.navigator = Navigator()
        self.dev360 = Device360WebElements()
        self.deviceConfig = DeviceConfig()
        self.deviceCommon = DeviceCommon()
        self.devices_web_elements = DevicesWebElements()
        self.dialog_web_elements = DialogWebElements()
        self.wireless_web_elements = WirelessWebElements()
        self.device_template_web_elements = DeviceTemplateWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.nav_web_elements = NavigatorWebElements()
        self.common_validation = CommonValidation()
        self.tools = Tools()
        self.networkElementCliSend = NetworkElementCliSend()

    def get_system_info(self, **kwargs):
        """
        - This keyword gets system information from device360 page
        - Keyword Usage
        - ``Get System Info``

        :return: dictionary of system information
        """
        try:
            self.utils.print_info("Clicking on System Information")
            self.auto_actions.click_reference(self.dev360.get_system_info_button)
            sleep(5)

            self.screen.save_screen_shot()
            self.utils.print_info("Getting System Information.")
            sys_info = dict()
            sys_info["host_name"] = self.dev360.get_system_info_device_host_name().text
            sys_info["ssids"] = self.dev360.get_system_info_device_ssids().text
            sys_info["network_policy"] = self.dev360.get_system_info_network_policy().text
            sys_info["device_model"] = self.dev360.get_system_info_device_model().text
            sys_info["device_function"] = self.dev360.get_system_info_device_function().text
            sys_info["device_template"] = self.dev360.get_system_info_device_template().text
            sys_info["configuration_type"] = self.dev360.get_system_info_conf_type().text
            sys_info["serial_number"] = self.dev360.get_system_info_serial_num().text
            sys_info["IQ_engine"] = self.dev360.get_system_info_iq_engine().text
            sys_info["device_status"] = self.dev360.get_system_info_dev_status().text
            sys_info["mgt0_ipv4"] = self.dev360.get_system_info_mgt0_ipv4().text
            sys_info["mgt0_ipv6"] = self.dev360.get_system_info_mgt0_ipv6().text
            sys_info["ipv6_subnet"] = self.dev360.get_system_info_ipv6_subnet().text
            sys_info["ipv4_subnet"] = self.dev360.get_system_info_ipv4_subnet().text
            sys_info["ipv4_default"] = self.dev360.get_system_info_ipv4_default().text
            sys_info["ipv6_default"] = self.dev360.get_system_info_ipv6_default().text
            sys_info["mgt0_mac"] = self.dev360.get_system_info_mgt0_mac().text
            sys_info["info_dns"] = self.dev360.get_system_info_dns().text
            sys_info["info_ntp"] = self.dev360.get_system_info_ntp().text
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            return sys_info
        except Exception:
            kwargs['fail_msg'] = "Unable to get device360 details"
            self.common_validation.failed(**kwargs)
            return -1

    def get_hostname_name_from_device_360(self, device_mac=None, device_name=None):
        """
        - This keyword gets hostname from device360 page by clicking on hyperlink(MAC/hostname)
        -Flow: Manage -->Devices --> click on device MAC or Host name hyperlink.
        - Keyword Usage:
        - ``${HOST_NAME}=                Get Hostname Name From Device 360           ${DEVICE_MAC}``

        :param device_mac: MAC of the device
        :param device_name: Host name of the device
        :return: host name
        """
        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)
            sys_info = self.get_system_info()
            return sys_info['host_name']

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)
            sys_info = self.get_system_info()
            return sys_info['host_name']

    def get_device_system_information(self, device_mac=None, device_name=None):
        """
        - This keyword gets Device system information from device360 page using Device Mac and Name
        - Flow : Manage--> Devices -->click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Get Device System Information  device_mac=${AP1_MAC}``
        - ``Get Device System Information  device_name=${AP1_NAME}``

        :return: dictionary of system information
        """
        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        sys_info = self.get_system_info()
        return sys_info

    def check_devices_by_search_field(self, search_string, device_name='', device_mac=''):
        """
        - This keyword is used to Search devices Using Search String passed on devices page Search Option.
        - Flow : Manage --> Devices--> Enter Search String on Devices Search Field
        - Select the device and give the System information details
        - Keyword Usage:
        - ``Check Devices By Search Field  ${AP_NAME_PART_STRING1}   device_name=${AP1_NAME}``

        :param search_string: Partial String of AP Name
        :param device_mac: Device MAC Address
        :param device_name:  Device Host Name
        :return: dictionary of Device information
        """

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()

        self.utils.print_info("Entering Search String...")
        self.auto_actions.send_keys(self.devices_web_elements.get_manage_device_search_field(), search_string)
        self.screen.save_screen_shot()
        sleep(2)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sys_info = self.get_system_info()
                return sys_info
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sys_info = self.get_system_info()
                return sys_info

    def check_client_in_device360(self, device_serial=None, client_mac=None, **kwargs):
        """
        - This keyword is used to check the client in device360 page based on passed client mac address
        - Flow: Manage --> Devices --> click on the Clients hyperlink which is present in Device grid row based on device serial
        - Keyword Usage:
        - ``${RESULT}=        Check Client In Device360          ${DEVICE_SERIAL}       ${CLIENT _MAC}``

        :param device_serial: serial of the device
        :param client_mac:  MAC of the client
        :return: 1 if successful else -1
        """
        self.utils.print_info("Navigate to Mange-->Devices")
        self.navigator.navigate_to_device360_with_client(device_serial)
        sleep(5)

        table = self.dev360.get_device_active_clients_grid()
        rows = self.dev360.get_device_active_clients_grid_rows(table)
        self.utils.print_info("Getting the total number of rows: ", len(rows))
        self.screen.save_screen_shot()
        for row in rows:
            self.utils.print_info("Getting the clients rows: ", row.text)
            if client_mac in row.text and "CONNECTED" in row.text:
                self.utils.print_info("Client found")
                self.auto_actions.click_reference(self.dev360.get_close_dialog)
                return 1
        kwargs['fail_msg'] = "Client not found"
        self.auto_actions.click_reference(self.dev360.get_close_dialog)
        self.common_validation.failed(**kwargs)
        return -1

    def get_status_interface_list(self, device_serial=None):
        """
        - This keyword  gets interfaces list
        - Flow: Manage --> Devices --> Select the device row based on the passed device serial --> Utilities --> Status --> Interface --> interface menu
        - Keyword Usage:
        - ``${RESULT}=        Get Status Interface         ${DEVICE_SERIAL}``

        :param device_serial: serial of the device
        :return: returns the list of interface names
        """
        if device_serial:
            self.navigator.navigate_to_status_interface(device_serial)
            sleep(5)
            self.auto_actions.click_reference(self.dev360.get_utilities_status_interface_name_dropdown)
            sleep(2)
            options = self.dev360.get_utilities_status_interface_name_dropdown_opt()
            list_options = []
            for opt in options:
                if "All" not in opt.text:
                    list_options.append(opt.text)
            self.utils.print_info("Interfaces List: ", list_options)
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            return list_options

    def get_status_interface(self, device_serial=None, interface_name=None, **kwargs):
        """
        - This keyword  gets status interface
        - Flow: Manage --> Devices --> Select the device row based on the passed device serial --> Utilities --> Status --> Interface --> select interface and get the output
        - Keyword Usage:
        - ``${RESULT}=        Get Status Interface         ${DEVICE_SERIAL}       ${INTERFACE}``

        :param device_serial: serial of the device
        :param interface_name: name of the interface
        :return: returns the output of the interface
        """
        if device_serial and interface_name:
            self.navigator.navigate_to_status_interface(device_serial)
            sleep(5)
            self.auto_actions.click_reference(self.dev360.get_utilities_status_interface_name_dropdown)
            sleep(2)
            options = self.dev360.get_utilities_status_interface_name_dropdown_opt()
            for opt in options:
                if interface_name in opt.text:
                    self.auto_actions.click(opt)
                    sleep(5)
                    break

            content = self.dev360.get_utilities_status_interface_contents().text
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            return content
        else:
            kwargs['fail_msg'] = "Device serial and interface name are not provided"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_configure_device_vlan_for_port(self, vlan=1363, **kwargs):
        """
        This keyword is to configure vlan in D360
        Manage --> Devices --> Device360 --> Port Configuration --> Vlan for port 1
        It Assumes That Already Navigated to Device360 Page
        :param vlan: vlan to configure on port 1
        :return: returns 1 if successfully configured, else returns -1
        """
        port = 1
        ret_val = 0
        self.utils.print_info("*****************************")
        self.utils.print_info("Configure Vlan for a port : ", port)
        self.utils.print_info("*****************************")
        self.utils.print_info("configuring the vlan in port 1..")
        self.utils.print_info("Selecting existing values in port 1..")

        self.auto_actions.send_keys(self.get_device360_configure_vlan_port_one(), Keys.CONTROL + "a")
        self.utils.print_info("Deleting the selected values in port 1..")
        self.auto_actions.send_keys(self.get_device360_configure_vlan_port_one(), Keys.BACK_SPACE)
        self.utils.print_info("Configuring new vlan values %s in port 1" % (vlan))
        self.auto_actions.send_keys(self.get_device360_configure_vlan_port_one(), vlan)
        sleep(2)

        # Click the 'Save Port Configuration' button
        save_btn = self.get_device360_configure_port_save_button()
        if save_btn:
            self.utils.print_info("Clicking 'Save Port Configuration' button'")
            self.auto_actions.click(save_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not click Save button")
            ret_val = -1
        sleep(2)

        close_diag = self.get_close_dialog()
        if close_diag:
            self.utils.print_info("closing the dialogue ")
            self.auto_actions.click_reference(self.get_close_dialog)
            ret_val = 1
        else:
            self.utils.print_info("couldn't close the dialogue box")
            ret_val = -1
        sleep(2)

        if ret_val == -1:
            if save_btn:
                kwargs['fail_msg'] = "Couldn't close the dialogue box"
                self.common_validation.failed(**kwargs)
            elif close_diag:
                kwargs['fail_msg'] = "Could not click Save button"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Save Port Configuration' button' and closing the dialogue "
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_enable_ssh_cli_connectivity(self, device_mac='', device_name='', run_time=5, time_interval=30,
                                              retry_time=15, **kwargs):
        """
        - This keyword enables SSH CLI Connectivity
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Get Device360 Enable SSH CLI Connectivity  device_mac=${AP1_MAC}    run_time=5``
        - ``Get Device360 Enable SSH CLI Connectivity  device_name=${AP1_NAME}  run_time=10``

        :param device_mac: The device MAC address
        :param device_name: The device Name
        :param run_time: The run time value to keep the ssh open (5, 30, 60, 120, 240)
        :param time_interval: sleep time to read in the new ssh port / ip values
        :param retry_time: The number of times to try and read in the new ssh port / ip value

        :return: SSH String
        """
        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac.upper())
            self.navigator.navigate_to_device360_page_with_mac(device_mac.upper())

        elif device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)
        else:
            kwargs['fail_msg'] = "Missing the device name and MAC, can't navigate to device 360 page"
            self.common_validation.fault(**kwargs)
            return -1
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click_reference(self.get_device360_configure_button)
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 SSH CLI tab")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_tab)
        sleep(3)
        self.screen.save_screen_shot()

        unknown_error = self.nav_web_elements.get_unknown_tooltip_error()
        if unknown_error is not None and unknown_error.is_displayed():
            self.utils.print_info("Found Unknown Tooltip Error in Device360-->SSH Page.So Closing the Error Message")
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.self.nav_web_elements.get_unknown_error_tooltip_close_icon)

        self.utils.print_info("Clicking Device 360 SSH CLI Run Time: ", run_time)
        if run_time == 5:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_5min_radio)

        elif run_time == 30:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_30min_radio)

        elif run_time == 60:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_60min_radio)

        elif run_time == 120:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_120min_radio)

        elif run_time == 240:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_240min_radio)
        else:
            kwargs['fail_msg'] = f"Unsupported run_time: {run_time} supported numbers are: 5, 30, 60, 120, 240"
            self.common_validation.fault(**kwargs)
            return -1

        sleep(10)
        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 SSH CLI Enable SSH button...")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_enable_button)
        self.screen.save_screen_shot()

        sleep(time_interval)
        self.screen.save_screen_shot()
        if self.get_device_ssh_ui_tip_error() is not None:
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.get_device_ssh_ui_tip_close)
            kwargs['fail_msg'] = "Encountered an error. Clicking to exit the error window. Please see the screenshot"
            self.close_device360_window()
            self.common_validation.failed(**kwargs)
            return -1

        retry_count = 0
        while retry_count <= retry_time:
            self.utils.print_info(f"Checking SSH IP and Port Details after: {time_interval} seconds")
            ip = self.get_device360_configure_ssh_cli_ip()
            port = self.get_device360_configure_ssh_cli_port()
            self.screen.save_screen_shot()

            if ip and port:
                ip_port_info = dict()
                ip_port_info["ip"] = ip
                ip_port_info["port"] = port

                self.utils.print_info("****************** IP/Port Information ************************")
                for key, value in ip_port_info.items():
                    self.utils.print_info(f"{key}:{value}")

                kwargs['pass_msg'] = f"Got the SSH and port information: {ip}:{port}"
                self.common_validation.passed(**kwargs)
                self.close_device360_window()
                return ip_port_info
            else:
                self.utils.print_info(
                    f"****************** IP/Port Information is not available after {time_interval} seconds ************************")
                sleep(time_interval)
                retry_count += 1

    def device360_enable_ssh_web_connectivity(self, device_mac='', device_name='', run_time=5):
        """
        - This keyword enables SSH CLI Connectivity
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Device360 Enable SSH Web Connectivity  device_mac=${AP1_MAC}    run_time=5``
        - ``Device360 Enable SSH Web Connectivity  device_name=${AP1_NAME}  run_time=10``

        :return: SSH String
        """
        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac.upper())
            self.navigator.navigate_to_device360_page_with_mac(device_mac.upper())

        if device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click_reference(self.get_device360_configure_button)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH WEB tab")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_web_tab)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH WEB Run Time: ", run_time)

        sleep(5)

        if run_time == 5:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_5min_radio)

        if run_time == 30:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_30min_radio)

        if run_time == 60:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_60min_radio)

        if run_time == 120:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_120min_radio)

        if run_time == 240:
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_240min_radio)

        self.screen.save_screen_shot()

        sleep(5)
        self.utils.print_info("Clicking Device 360 SSH WEB Enable SSH button...")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_web_enable_button)

        sleep(60)

        url = self.get_device360_configure_ssh_web_url()

        self.utils.print_info("Device 360 SSH WEB URL: ", url)

        return url

    def device360_is_ssh_enabled(self, device_mac='', device_name='', **kwargs):
        """
        - This keyword verifies if SSH Web Connectivity is enabled
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Device360 Is SSH Enabled  device_mac=${AP1_MAC}``
        - ``Device360 Is SSH Enabled  device_name=${AP1_NAME}``
        :param device_mac: device MAC address
        :param device_name: device name
        :return: 1 if is enabled, else -1
        """
        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac)
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click_reference(self.get_device360_configure_button)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH tab")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_tab)
        self.screen.save_screen_shot()

        self.utils.print_info("Check if enabled based on first radio button")
        if self.get_device360_configure_ssh_cli_5min_radio().is_enabled():
            kwargs['pass_msg'] = "Device360 ssh is enabled"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "Device360 ssh is not enabled"
        self.common_validation.failed(**kwargs)
        return -1

    def device360_is_ssh_disabled(self, device_mac='', device_name='', **kwargs):
        """
        - This keyword verifies if SSH Web Connectivity is disabled
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Device360 Is SSH Disabled  device_mac=${AP1_MAC}``
        - ``Device360 Is SSH Disabled  device_name=${AP1_NAME}``
        :param device_mac: device MAC address
        :param device_name: device name
        :return: 1 if is disabled, else -1
        """
        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac)
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click_reference(self.get_device360_configure_button)
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH tab")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_tab)
        self.screen.save_screen_shot()

        self.utils.print_info("Check if disabled based on first radio button")
        if self.get_device360_configure_ssh_cli_5min_radio().is_enabled():
            kwargs['fail_msg'] = "Device360 ssh is enabled"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Device360 ssh is not enabled"
        self.common_validation.passed(**kwargs)
        return 1

    def get_switch_information(self):
        """
        - This keyword gets Switch information from device360 page
        - It Assumes That Already Navigated to Device360 Page
        - Flow : Device 360 Page
        - Keyword Usage
        - ``Get Switch Information``

        :return: dictionary of Switch information
        """

        self.utils.print_info("Getting device360 Information.")
        device360_info = dict()
        device360_info["host_name"] = self.dev360.get_system_info_device_host_name().text
        ip_address_field = self.dev360.get_device_info_ip_address().text
        device360_info["ip_address"] = ip_address_field.split('\n')[-1]
        mac_address_field = self.dev360.get_device_info_mac_address().text
        device360_info["mac_address"] = mac_address_field.split('\n')[-1]
        serial_number_field = self.dev360.get_device_info_serial().text
        device360_info["serial_number"] = serial_number_field.split('\n')[-1]
        device360_info["network_policy"] = self.dev360.get_device_info_device_policy().text
        device_model_field = self.dev360.get_device_info_model().text
        device360_info["device_model"] = device_model_field.split('\n')[-1]
        iq_agent_version_field = self.get_device_info_iqagent_version().text
        device360_info["IQAgent_version"] = iq_agent_version_field.split('\n')[-1]
        device_make_field = self.dev360.get_device_info_make().text
        device360_info["device_make"] = device_make_field.split('\n')[-1]
        software_version_field = self.dev360.get_device_info_software_version().text
        device360_info["software_version"] = software_version_field.split('\n')[-1]

        self.utils.print_info("******************ExOS Device360 Information************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        self.utils.print_info("Closing device360 Dialogue Window.")
        self.auto_actions.click_reference(self.dev360.get_close_dialog)
        self.screen.save_screen_shot()

        return device360_info

    def get_device_360_information(self, cli_type, device_mac='', device_name=''):
        if cli_type.upper() == 'EXOS' or cli_type.upper() == 'VOSS':
            return self.get_switch_360_information(device_mac, device_name)
        else:
            self.utils.print_info(f"The cli type {cli_type} is not supported for this keyword")
            return None

    def get_switch_360_information(self, device_mac='', device_name=''):
        """
        - This keyword gets Switch information from device360 page ie Model,Serial Number etc
        - Flow : Manage-->Devices-->click on Switch hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Get ExOS Switch 360 Information   device_name=${SW1_NAME}``
        - ``Get ExOS Switch 360 Information   device_mac=${SW1_MAC}``

        :param device_mac:  Switch MAC Address
        :param device_name:  Switch Name
        :return: dictionary of Switch information
        """
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac: ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)
                self.screen.save_screen_shot()
                exos_info = self.get_switch_information()
                return exos_info

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)
                self.screen.save_screen_shot()
                exos_info = self.get_switch_information()
                return exos_info

    def advance_channel_selection(self, device_serial=None, **kwargs):
        """
        - This keyword  gets advance channel selection details
        - Flow: Manage --> Devices --> Select the device row based on the passed device serial -->Utilities --> Status --> Advanced Channel Selection
        - Keyword Usage:
        - ``${RESULT}=        Advance Channel Selection         ${DEVICE_SERIAL} ``

        :param device_serial: serial of the device
        :return: returns the output of the advance channel selection
        """
        if device_serial:
            self.navigator.navigate_to_advance_channel_selection(device_serial)
            content = self.dev360.get_utilities_status_adv_channel_sel_contents().text
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            return content
        else:
            kwargs['fail_msg'] = "Device serial is not provided"
            self.common_validation.failed(**kwargs)
            return -1

    def wifi_status_summary(self, device_serial=None, **kwargs):
        """
        - This keyword  gets wifi status summary
        - Flow: Manage --> Devices -->Select the device row based on the passed device serial --> Click on Utilities --> Status --> Wifi Status Summary --> station
        - Keyword Usage:
        - ``${RESULT}=        Wifi Status Summary         ${DEVICE_SERIAL}  ``

        :param device_serial: serial of the device
        :return: returns the output of the wifi status summary
        """
        if device_serial:
            self.navigator.navigate_to_wifi_status_summary(device_serial)
            sleep(5)
            self.utils.print_info("Clicking on Station..")
            self.auto_actions.click_reference(self.dev360.get_utilities_status_wifi_summary_station_btn)
            sleep(2)

            self.screen.save_screen_shot()
            self.utils.print_info("Getting the contents..")
            content = self.dev360.get_utilities_status_wifi_summary_station_content().text
            self.utils.print_info("Content: ", content)
            self.utils.print_info("Clicking on close dialog")
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            return content
        else:
            self.utils.print_info("Device serial is not provided.")
            kwargs['fail_msg'] = "Device serial is not provided"
            self.common_validation.failed(**kwargs)
            return -1

    def get_voss_overview_information(self):
        """
        - This keyword gets VOSS Switch information from the Monitor> Overview page of the Device360 view
        - It is assumed that the Device360 window is open and on the Monitor> Overview page
        - Flow : Device 360 Page -> Monitor -> Overview
        - Keyword Usage
        - ``Get VOSS Overview Information``
        :return: dictionary of VOSS Switch information obtained from the Monitor> Overview page of the Device360 view
        """

        self.utils.print_info("Getting device360 Monitor> Overview Information.")
        device360_info = dict()
        device360_info["host_name"] = self.dev360.get_system_info_device_host_name().text
        ip_address_field = self.dev360.get_device_info_ip_address().text
        device360_info["ip_address"] = ip_address_field.split('\n')[-1]
        mac_address_field = self.dev360.get_device_info_mac_address().text
        device360_info["mac_address"] = mac_address_field.split('\n')[-1]
        serial_number_field = self.dev360.get_device_info_serial().text
        device360_info["serial_number"] = serial_number_field.split('\n')[-1]
        device360_info["network_policy"] = self.dev360.get_device_info_device_policy().text
        device_model_field = self.dev360.get_device_info_model().text
        device360_info["device_model"] = device_model_field.split('\n')[-1]
        iq_agent_version_field = self.get_device_info_iqagent_version().text
        device360_info["IQAgent_version"] = iq_agent_version_field.split('\n')[-1]
        device_make_field = self.dev360.get_device_info_make().text
        device360_info["device_make"] = device_make_field.split('\n')[-1]
        software_version_field = self.dev360.get_device_info_software_version().text
        device360_info["software_version"] = software_version_field.split('\n')[-1]

        self.utils.print_info("******************VOSS Device360 Overview Information************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        return device360_info

    def get_voss_device_configuration_information(self):
        """
        - This keyword gets VOSS Switch information from the Configure> Device Configuration page of the Device360 view
        - It is assumed that the Device360 window is open and on the Configure> Device Configuration page
        - Flow : Device 360 Page -> Configure -> Device Configuration
        - Keyword Usage
        - ``Get VOSS Device Configuration Information``
        :return: dictionary of VOSS Switch information obtained from the Configure> Device Configuration page of the Device360 view
        """

        self.utils.print_info("Getting device360 Configure> Device Configuration Information.")
        device360_info = dict()
        device360_info["host_name"] = self.dev360.get_device360_configure_device_host_name().get_attribute('value')
        device360_info["snmp_location"] = self.dev360.get_device360_configure_device_snmp_location().get_attribute(
            'value')
        device360_info["network_policy"] = self.dev360.get_device360_configure_device_network_policy().text
        device360_info["device_template"] = self.dev360.get_device360_configure_device_device_template().text

        self.utils.print_info(
            "******************VOSS Device360 Device Configuration Information************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        return device360_info

    def get_voss_device360_overview_information(self, device_mac='', device_name=''):
        """
        - This keyword gets VOSS Switch information from device360 page ie Model,Serial Number etc
        - Flow : Manage-->Devices-->click on VOSS Switch hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Get VOSS Switch 360 Information   device_mac=${SW1_MAC}``
        - ``Get VOSS Switch 360 Information   device_name=${SW1_NAME}``
        :param device_mac: VOSS Switch MAC Address
        :param device_name:  VOSS SWitch Name
        :return: dictionary of VOSS Switch information
        """

        voss_info = -1

        if device_mac:
            self.utils.print_info("Checking Search Result with Device MAC : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)
                voss_info = self.get_voss_overview_information()
                self.close_device360_window()

        elif device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)
                voss_info = self.get_voss_overview_information()
                self.close_device360_window()

        else:
            self.utils.print_info(
                "Unable to get VOSS overview information - please specify a device MAC or device name")

        return voss_info

    def get_voss_device360_device_configuration_information(self, device_mac='', device_name=''):
        """
        - This keyword gets VOSS Switch information from device360 page ie Model,Serial Number etc
        - Flow : Manage-->Devices-->click on VOSS Switch hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Get VOSS Switch 360 Information   device_mac=${SW1_MAC}``
        - ``Get VOSS Switch 360 Information   device_name=${SW1_NAME}``
        :param device_mac: VOSS Switch MAC Address
        :param device_name:  VOSS SWitch Name
        :return: dictionary of VOSS Switch information
        """

        voss_info = -1

        if device_mac:
            self.utils.print_info("Checking Search Result with Device MAC : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

                self.utils.print_info("Clicking Device360 Configure tab")
                self.auto_actions.move_to_element(self.get_sidebar_model())
                self.auto_actions.scroll_down()

                self.auto_actions.click_reference(self.get_device360_configure_button)
                sleep(8)

                self.utils.print_info("Clicking Device Configuration on the Device360 Configure tab")
                self.auto_actions.click_reference(self.get_device360_device_configuration_button)
                sleep(3)

                voss_info = self.get_voss_device_configuration_information()

                self.device360_device_configuration_click_cancel()
                self.close_device360_window()

        elif device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)

                self.utils.print_info("Clicking Device360 Configure tab")
                self.auto_actions.move_to_element(self.get_sidebar_model())
                self.auto_actions.scroll_down()

                self.auto_actions.click_reference(self.get_device360_configure_button)
                sleep(8)

                self.utils.print_info("Clicking Device Configuration on the Device360 Configure tab")
                self.auto_actions.click_reference(self.get_device360_device_configuration_button)
                sleep(3)
                voss_info = self.get_voss_device_configuration_information()
                self.device360_device_configuration_click_cancel()
                self.close_device360_window()

        else:
            self.utils.print_info(
                "Unable to get VOSS device configuration information - please specify a device MAC or device name")

        return voss_info

    def select_configure_tab(self, **kwargs):
        """
        - This keyword clicks the Configure tab in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Configure" tab
        - Keyword Usage:
        - ``Select Configure Tab``
        :return: 1 if the Configure tab was clicked, else -1
        """
        conf_tab = self.get_device360_configure_button()
        if conf_tab:
            self.utils.print_info("Clicking Device360 Configure tab")
            self.auto_actions.click(conf_tab)
            kwargs['pass_msg'] = "Clicking Device360 Configure tab"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Configure tab - make sure Device360 window is open"
            self.common_validation.failed(**kwargs)
            return -1

    def select_device_configuration_view(self, **kwargs):
        """
        - This keyword clicks the Device Configuration link on the Configure tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Configure tab.
        - Flow: Device 360 Window --> Configure tab --> Click "Device Configuration" link
        - Keyword Usage:
        - ``Select Device Configuration View``
        :return: 1 if the Device Configuration view was selected, else -1
        """
        dev_conf_link = self.get_device360_device_configuration_button()
        if dev_conf_link:
            self.utils.print_info("Clicking Device Configuration on the Device360 Configure tab")
            self.auto_actions.click(dev_conf_link)
            kwargs['pass_msg'] = "Clicking Device Configuration on the Device360 Configure tab"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Device Configuration link - make sure Device360 window is open " \
                                 "and on Configure tab"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_navigate_to_device_configuration(self):
        """
        - This keyword navigates to the Configure> Device Configuration view in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Configure" tab --> Click "Device Configuration" link
        - Keyword Usage:
        - ``Device360 Navigate to Device Configuration``
        :return: 1 if navigation was successful, else -1
        """
        ret_val = self.select_configure_tab()
        if ret_val != -1:
            ret_val = self.select_device_configuration_view()

        return ret_val

    def device360_device_configuration_click_cancel(self, **kwargs):
        """
        - This keyword clicks Cancel in the Configure> Device Configuration view in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Configure> Device Configuration page.
        - Flow: Device 360 Window --> Configure tab --> Device Configuration page --> Click Cancel
        - Keyword Usage:
        - ``Device360 Device Configuration Click Cancel``
        :return: 1 if navigation was successful, else -1
        """
        cancel_btn = self.get_device360_configure_device_cancel_button()
        if cancel_btn:
            self.utils.print_info("Clicking Cancel button in the Device Configuration view of Device360")
            self.auto_actions.click(cancel_btn)
            kwargs['pass_msg'] = "Clicking Cancel button in the Device Configuration view of Device360"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Device Configuration link - make sure Device360 window is open " \
                                 "and on Configure tab"
            self.common_validation.failed(**kwargs)
            return -1

    def close_device360_window(self, **kwargs):
        """
        - This keyword closes the Device360 dialog window.  It assumes the Device360 Window is open - if the close
          button cannot be found, a message is printed.
        - Flow: Device 360 Window --> Click "X" to close Device360 Window
        - Keyword Usage:
        - ``Close Device360 Window``
        :return: 1 if the device 360 window was closed, else -1
        """
        close_btn = self.dev360.get_close_dialog()
        if close_btn:
            self.utils.print_info("Closing device360 Dialog Window.")
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            kwargs['pass_msg'] = "Closing device360 Dialog Window.0"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not obtain Device360 close button - make sure Device360 window is open"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_disable_ssh_connectivity(self, device_mac='', device_name='', **kwargs):
        """
        - This keyword disables SSH Connectivity for the specified device
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname) -> Click Disable SSH button
        - Keyword Usage
        - ``Device360 Disable SSH CLI Connectivity  device_mac=${AP1_MAC}``
        - ``Device360 Disable SSH CLI Connectivity  device_name=${AP1_NAME}``
        :return: SSH String
        """
        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac)
            self.navigator.navigate_to_device360_page_with_mac(device_mac)
        elif device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)
        else:
            kwargs['fail_msg'] = "Missing the device name and MAC, can't navigate to device 360 page"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click_reference(self.get_device360_configure_button)

        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 SSH CLI tab")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_tab)
        sleep(3)

        self.screen.save_screen_shot()
        self.utils.print_info("Clicking Device 360 SSH Disable SSH button...")
        disable_ssh_btn = self.get_device360_configure_ssh_disable_button()
        if disable_ssh_btn:
            self.auto_actions.click(disable_ssh_btn)
        else:
            self.utils.print_info("SSH has been disabled")

        kwargs['pass_msg'] = "SSH has been disabled successfully!"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_disable_ssh_web_connectivity(self, device_mac='', device_name='', **kwargs):
        """
        - This keyword disables SSH WEB Connectivity
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Device360 Disable SSH Web Connectivity  device_mac=${AP1_MAC}``
        - ``Device360 Disable SSH Web Connectivity  device_name=${AP1_NAME}``

        :return: 1 if passed else -1
        """
        if self.get_device360_configure_ssh_web_disable_button():
            self.utils.print_info("Clicking Device 360 SSH CLI Disable SSH button...")
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_disable_button)
            sleep(5)
            self.screen.save_screen_shot()

            if self.get_device360_configure_ssh_web_url():
                kwargs['fail_msg'] = "Could not get device360 ssh web url"
                self.common_validation.fault(**kwargs)
                return -1
            return 1
        else:
            if device_mac:
                self.utils.print_info("Using device MAC: ", device_mac)
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

            if device_name:
                self.utils.print_info("Using device name: ", device_name)
                self.navigator.navigate_to_device360_page_with_host_name(device_name)

            self.utils.print_info("Clicking Device 360 Configure button")
            self.auto_actions.click_reference(self.get_device360_configure_button)

            self.utils.print_info("Clicking Device 360 SSH WEB tab")
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_tab)

            sleep(5)

            self.utils.print_info("Clicking Device 360 SSH CLI Disable SSH button...")
            self.auto_actions.click_reference(self.get_device360_configure_ssh_web_disable_button)

            if self.get_device360_configure_ssh_web_url():
                kwargs['fail_msg'] = "Could not get device360 ssh web url"
                self.common_validation.failed(**kwargs)
                return -1
            return 1

    def device360_confirm_ssh_enabled(self, device_mac='', device_name='', **kwargs):
        """
        - This keyword confirms if SSH is enabled for the specified device
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname) -> check if SSH is enabled
        - Keyword Usage
        - ``Device360 Confirm SSH Enabled  device_mac=${AP1_MAC}``
        - ``Device360 Confirm SSH Enabled  device_name=${AP1_NAME}``

        :return: 1 if SSH enabled, -1 if SSH is disabled
        """
        ret_val = -1

        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac)
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click_reference(self.get_device360_configure_button)

        self.utils.print_info("Clicking Device 360 SSH CLI tab")
        self.auto_actions.click_reference(self.get_device360_configure_ssh_cli_tab)
        sleep(3)

        disable_ssh_btn = self.get_device360_configure_ssh_disable_button()
        if disable_ssh_btn is None or disable_ssh_btn.get_attribute('visible') is False:
            self.utils.print_info("Disable button is not present - SSH is not enabled")
            ret_val = -1
        else:
            self.utils.print_info("Disable button is present - SSH is enabled")
            ret_val = 1

        if ret_val == -1:
            kwargs['fail_msg'] = "Disable button is not present - SSH is not enabled"
            self.common_validation.fault(**kwargs)
        else:
            kwargs['pass_msg'] = "Disable button is present - SSH is enabled"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_select_events_view(self, **kwargs):
        """
        - This keyword clicks the Events link on the Monitor tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor tab.
        - Flow: Device 360 Window --> Monitor tab --> Click "Events" link
        - Keyword Usage:
        - ``Device360 Select Events View``
        :return: 1 if the Events view was selected, else -1
        """
        events_link = self.get_device360_events_link()
        if events_link:
            self.utils.print_info("Clicking Events link on the Device360 Monitor tab")
            self.auto_actions.click(events_link)
            kwargs['pass_msg'] = "The Events view was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Events link - make sure Device360 window is open and on Monitor tab"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_select_alarms_view(self, **kwargs):
        """
        - This keyword clicks the Alarms link on the Monitor tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor tab.
        - Flow: Device 360 Window --> Monitor tab --> Click "Alarms" link
        - Keyword Usage:
        - ``Device360 Select Alarms View``
        :return: 1 if the Alarms view was selected, else -1
        """
        alarms_link = self.get_device360_alarms_link()
        if alarms_link:
            self.utils.print_info("Clicking Alarms link on the Device360 Monitor tab")
            self.auto_actions.click(alarms_link)
            kwargs['pass_msg'] = "The Alarms view was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Alarms link - make sure Device360 window is open and on Monitor tab"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_confirm_event_description_contains(self, event_str, after_time=None, **kwargs):
        """
        - This keyword confirms the specified event text is present in the description field of the event, after the
          specified time. If no time is specified, it just confirms the event is present.
          It assumes the Device360 Window is open and on the Monitor> Events tab.
        - Keyword Usage:
        - ``Device360 Confirm Event Exists  ${EVENT}  ${AFTER_TIME}``
        - ``Device360 Confirm Event Exists  ${EVENT}``
        :param  event_str:      String to look for in the event description
        :param  after_time:     Indicates at which point in time to start searching for the existence of the event
                                (if not specified, it just checks for the existence of the event in general)
        :return: 1 if the event is present (since "after_time", if specified), else -1
        """
        ret_val = -1

        events_table = self.dev360.get_device360_events_grid()
        if events_table:
            event_rows = self.dev360.get_device360_events_grid_rows(events_table)
            if event_rows:
                for row in event_rows:
                    desc_val = self.get_device360_event_description_cell_value(row)
                    self.utils.print_debug("Checking row with event description value '" + desc_val + "'")
                    # Check if the event description value for this row contains what we are looking for
                    if event_str in desc_val:
                        # If a time was specified, make sure the timestamp for the event is more recent
                        if after_time:
                            time_val = self.get_device360_event_timestamp_cell_value(row)
                            if time_val > after_time:
                                self.utils.print_debug(
                                    "Found a match for '" + event_str + ''" after "'' + after_time + "'")
                                ret_val = 1
                                break
                            else:
                                self.utils.print_debug(
                                    "Found a match for '" + event_str + "' but it has a timestamp before '" + after_time
                                    + "' (" + time_val + ") - looking at next row...")
                        else:
                            self.utils.print_debug("Found a match for '" + event_str + "'")
                            ret_val = 1
                            break
            else:
                self.utils.print_info("Events table does not contain any rows")
        else:
            self.utils.print_info(
                "Could not find Events table - make sure Device360 window is open to the Monitor> Alarms view")

        if ret_val == -1:
            if not events_table:
                kwargs['fail_msg'] = "Could not find Events table - make sure Device360 window is open to " \
                                     "the Monitor> Alarms view"
                self.common_validation.fault(**kwargs)
            elif not event_rows:
                kwargs['fail_msg'] = "Events table does not contain any rows"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The event is present"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_confirm_alarm_category_exists(self, alarm_cat, after_time=None, **kwargs):
        """
        - This keyword confirms the specified alarm category is present in the view, after the specified time.
          If no time is specified, it just confirms the alarm is present.
          It assumes the Device360 Window is open and on the Monitor> Alarms tab.
        - Keyword Usage:
        - ``Device360 Confirm Alarm CategoryExists  ${ALARM}  ${AFTER_TIME}``
        - ``Device360 Confirm Alarm CategoryExists  ${ALARM}``
        :param  alarm_cat:      Alarm category to look for
        :param  after_time:     Indicates at which point in time to start searching for the existence of the alarm
                                (if not specified, it just checks for the existence of the alarm in general)
        :return: 1 if the alarm is present (since "after_time", if specified), else -1
        """
        ret_val = -1

        alarms_table = self.dev360.get_device360_alarms_grid()
        if alarms_table:
            alarm_rows = self.dev360.get_device360_alarms_grid_rows(alarms_table)
            if alarm_rows:
                for row in alarm_rows:
                    category_val = self.get_device360_alarm_category_cell_value(row)
                    self.utils.print_debug("Checking row with alarm category value '" + category_val + "'")
                    # Check if the alarm category value for this row matches what we are looking for
                    if alarm_cat in category_val:
                        # If a time was specified, make sure the timestamp for the alarm is more recent
                        if after_time:
                            time_val = self.get_device360_alarm_timestamp_cell_value(row)
                            if time_val > after_time:
                                self.utils.print_debug(
                                    "Found a match for '" + alarm_cat + ''" after "'' + after_time + "'")
                                ret_val = 1
                                break
                            else:
                                self.utils.print_debug(
                                    "Found a match for '" + alarm_cat + "' but it has a timestamp before '" + after_time
                                    + "' (" + time_val + ") - looking at next row...")
                        else:
                            self.utils.print_debug("Found a match for '" + alarm_cat + "'")
                            ret_val = 1
                            break
            else:
                self.utils.print_info("Alarms table does not contain any rows")
        else:
            self.utils.print_info(
                "Could not find Alarms table - make sure Device360 window is open to the Monitor> Alarms view")

        if ret_val == -1:
            if not alarms_table:
                kwargs['fail_msg'] = "Could not find Alarms table" \
                                     " - make sure Device360 window is open to the Monitor> Alarms view"
                self.common_validation.fault(**kwargs)
            elif not alarm_rows:
                kwargs['fail_msg'] = "Alarms table does not contain any rows"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The event is present"
            self.common_validation.passed(**kwargs)
        return ret_val

    def select_port_configuration_view(self, **kwargs):
        """
        - This keyword clicks the Port Configuration link on the Configure tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Configure tab.
        - Flow: Device 360 Window --> Configure tab --> Click "Port Configuration" link
        - Keyword Usage:
        - ``Select Port Configuration View``
        :return: 1 if the Port Configuration view was selected, else -1
        """
        port_conf_link = self.get_device360_port_configuration_button()
        if port_conf_link:
            self.utils.print_info("Clicking Port Configuration on the Device360 Configure tab")
            self.auto_actions.click(port_conf_link)
            kwargs['pass_msg'] = "The event is present"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Port Configuration link - make sure Device360 window is open " \
                                 "and on Configure tab"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_navigate_to_port_configuration(self):
        """
        - This keyword navigates to the Configure> Port Configuration view in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Configure" tab --> Click "Port Configuration" link
        - Keyword Usage:
        - ``Device360 Navigate to Port Configuration``
        :return: 1 if navigation was successful, else -1
        """

        ret_val = self.select_configure_tab()
        if ret_val != -1:
            ret_val = self.select_port_configuration_view()

        return ret_val

    def device360_confirm_port_enabled(self, port_name, **kwargs):
        """
        - This keyword confirms the specified port is enabled/on.
          It assumes the Device360 Window is open and navigated to the Configure> Port Configuration view.
        - Flow: Device 360 Window --> Click "Configure" tab --> Click "Port Configuration" link --> Confirm specified port is enabled/on
        - Keyword Usage:
        - ``Device360 Confirm Port Enabled  ${PORT_NAME}``
        :param  port_name:  name of the port to confirm the state of
        :return: 1 if port is enabled, else -1
        """
        ret_val = -1

        # Make sure the correct view is selected
        port_conf_title = self.get_device360_port_configuration_title()
        if port_conf_title and port_conf_title.is_displayed():
            # Get the row for the port we want to work with
            port_row = self.device360_get_port_row(port_name)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)

                # Check if the port is currently enabled
                port_enabled = self.get_device360_configure_port_row_state_enabled(port_row)
                if port_enabled:
                    self.utils.print_info(f"Port {port_name} is enabled")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Port {port_name} is not enabled")
            else:
                self.utils.print_info(f"Could not find port row for port {port_name}")
        else:
            self.utils.print_info("Not navigated to Port Configuration on the Device360 Configure tab")

        if ret_val == -1:
            if not port_conf_title:
                kwargs['fail_msg'] = "Not navigated to Port Configuration on the Device360 Configure tab"
                self.common_validation.fault(**kwargs)
            elif not port_row:
                kwargs['fail_msg'] = "Alarms table does not contain any rows"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The event is present"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_confirm_port_disabled(self, port_name, **kwargs):
        """
        - This keyword confirms the specified port is disabked/off.
          It assumes the Device360 Window is open and navigated to the Configure> Port Configuration view.
        - Flow: Device 360 Window --> Click "Configure" tab --> Click "Port Configuration" link --> Confirm specified port is disabled/off
        - Keyword Usage:
        - ``Device360 Confirm Port Disabled  ${PORT_NAME}``
        :param  port_name:  name of the port to confirm the state of
        :return: 1 if port is disabled, else -1
        """
        ret_val = -1

        # Make sure the correct view is selected
        port_conf_title = self.get_device360_port_configuration_title()
        if port_conf_title and port_conf_title.is_displayed():
            # Get the row for the port we want to work with
            port_row = self.device360_get_port_row(port_name)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)

                # Check if the port is currently enabled
                port_disabled = self.get_device360_configure_port_row_state_disabled(port_row)
                if port_disabled:
                    self.utils.print_info(f"Port {port_name} is disabled")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Port {port_name} is not disabled")
            else:
                self.utils.print_info(f"Could not find the port row for port {port_name}")
        else:
            self.utils.print_info("Not navigated to Port Configuration on the Device360 Configure tab")

        if ret_val == -1:
            if not port_conf_title:
                kwargs['fail_msg'] = "Not navigated to Port Configuration on the Device360 Configure tab"
                self.common_validation.fault(**kwargs)
            elif not port_row:
                kwargs['fail_msg'] = f"Could not find the port row for port {port_name}"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Port {port_name} is disabled"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_disable_port(self, port_name):
        """
        - This keyword disables the specified port.
          It assumes the Device360 Window is open and navigated to the Configure> Port Configuration view.
        - Flow: Device 360 Window --> Click "Configure" tab --> Click "Port Configuration" link --> Toggle Port State to Off
        - Keyword Usage:
        - ``Device360 Disable Port  ${PORT_NAME}``
        :param  port_name:  name of the port to disable
        :return: 1 if port was disabled, 2 if port was already disabled, else -1
        """
        ret_val = -1

        # Make sure the correct view is selected
        port_conf_title = self.get_device360_port_configuration_title()
        if port_conf_title and port_conf_title.is_displayed():
            # Get the row for the port we want to work with
            port_row = self.device360_get_port_row(port_name)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)

                # Make sure the port is currently enabled
                port_enabled = self.get_device360_configure_port_row_state_enabled(port_row)
                if port_enabled:
                    # Click the Port State toggle to disable the port
                    port_state_toggle = self.get_device360_configure_port_row_state_toggle(port_row)
                    if port_state_toggle:
                        self.utils.print_info("Clicking Port State toggle to Off")
                        self.auto_actions.click(port_state_toggle)

                        # Click the 'Save Port Configuration' button
                        save_btn = self.get_device360_configure_port_save_button()
                        if save_btn:
                            self.utils.print_info("Clicking 'Save Port Configuration' button'")
                            self.auto_actions.click(save_btn)
                            ret_val = 1
                        else:
                            self.utils.print_info("Could not click Save button")
                    else:
                        self.utils.print_info("Could not find port state toggle")
                else:
                    self.utils.print_info("Port is already disabled for row ", port_row.text)
                    ret_val = 2
            else:
                self.utils.print_info("Could not find the port row for port ", port_name)
        else:
            self.utils.print_info("Not navigated to Port Configuration on the Device360 Configure tab")

        return ret_val

    def device360_get_port_row(self, port_name, **kwargs):
        """
        - Get the port row object matching the specified port_name from Device360 --> Configure --> Port Configuration

        :param port_name: name of the port to return the row for
        :return: row element if row exists else return None
        """
        ret_val = None
        self.utils.print_info("Getting the Port rows from the Device360 Port Configuration page")
        rows = self.get_device360_configure_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
        else:
            for row in rows:
                row_text = row.text
                if row_text.startswith(port_name):
                    ret_val = row
                    break

        if ret_val == -1:
            kwargs['fail_msg'] = "Could not obtain list of port rows"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Row object matching the specified {port_name} " \
                                 f"from Device360 --> Configure --> Port Configuration exists"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_refresh_page(self, **kwargs):
        """
        - Refreshes the Device 360 window by clicking the refresh page button.

        :return: 1 if page was refreshed, -1 if not
        """
        ret_val = -1
        refresh_btn = self.dev360.get_device360_refresh_page_button()
        if refresh_btn:
            self.utils.print_info("Clicking Refresh Page button")
            self.auto_actions.click(refresh_btn)
            sleep(5)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Refresh Page button")

        if ret_val == -1:
            kwargs['fail_msg'] = "Could not find Refresh Page button"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Page was refreshed"
            self.common_validation.passed(**kwargs)
        return ret_val

    def select_monitor_tab(self, **kwargs):
        """
        - This keyword clicks the Monitor tab in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Monitor" tab
        - Keyword Usage:
        - ``Select Monitor Tab``
        :return: 1 if the Monitor tab was clicked, else -1
        """
        monitor_tab = self.get_device360_monitor_button()
        if monitor_tab:
            self.utils.print_info("Clicking Device360 Monitor tab")
            self.auto_actions.click(monitor_tab)
            kwargs['pass_msg'] = "The Monitor tab was clicked"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Monitor tab - make sure Device360 window is open"
            self.common_validation.failed(**kwargs)
            return -1

    def select_monitor_overview(self, **kwargs):
        """
        - This keyword clicks the Overview button on the Monitor tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor tab.
        - Flow: Device 360 Window --> Monitor tab --> Click "Overview" button
        - Keyword Usage:
        - ``Select Monitor Overview``
        :return: 1 if Monitor> Overview was selected, else -1
        """
        overview_btn = self.get_device360_monitor_overview_button()
        if overview_btn:
            self.utils.print_info("Clicking Overview button on the Device360 Monitor tab")
            self.auto_actions.click(overview_btn)
            kwargs['pass_msg'] = "Monitor> Overview was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Overview button - make sure Device360 window is open " \
                                 "and on Monitor tab"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_navigate_to_monitor_overview(self):
        """
        - This keyword navigates to the Monitor> Overview view in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Monitor" tab --> Click "Overview" button
        - Keyword Usage:
        - ``Device360 Navigate to Monitor Overview``
        :return: 1 if navigation was successful, else -1
        """
        ret_val = self.select_monitor_tab()
        if ret_val != -1:
            ret_val = self.select_monitor_overview()

        return ret_val

    def select_switch_system_information(self, **kwargs):
        """
        - This keyword clicks the System Information button in the Monitoring view of the Device360 dialog window.
          This view applies to a switch, and is different from an AP which would have a Monitor and Configure tab.
          It assumes the Device360 Window is open and on the Monitoring view for a switch.
        - Flow: Device 360 Window --> Click "System Information" button
        - Keyword Usage:
        - ``Select Switch System Information``
        :return: 1 if System Information was selected, else -1
        """
        sys_btn = self.get_device360_switch_system_info_button()
        if sys_btn:
            self.utils.print_info("Clicking System Information button in the Device360 view")
            self.auto_actions.click(sys_btn)
            kwargs['pass_msg'] = "System Information was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find System Information button - make sure Device360 window is " \
                                 "open for a switch"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_navigate_to_switch_system_information(self):
        """
        - This keyword navigates to the System Information view in the Device360 dialog window.
          It assumes the Device360 Window is open for a switch.
        - Flow: Device 360 Window --> Click "System Information" button
        - Keyword Usage:
        - ``Device360 Navigate to Switch System Information``
        :return: 1 if navigation was successful, else -1
        """
        ret_val = self.select_switch_system_information()

        return ret_val

    def select_monitor_clients(self, **kwargs):
        """
        - This keyword clicks the Clients button on the Monitor tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor tab.
        - Flow: Device 360 Window --> Monitor tab --> Click "Clients" button
        - Keyword Usage:
        - ``Select Monitor Clients``
        :return: 1 if Monitor> Clients was selected, else -1
        """
        clients_btn = self.get_device360_monitor_clients_button()
        if clients_btn:
            self.utils.print_info("Clicking Clients button on the Device360 Monitor tab")
            self.auto_actions.click(clients_btn)
            kwargs['pass_msg'] = "Monitor> Clients was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find System Information button - make sure Device360 window is " \
                                 "open for a switch"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_navigate_to_monitor_clients(self):
        """
        - This keyword navigates to the Monitor> Clients view in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Monitor" tab --> Click "Clients" button
        - Keyword Usage:
        - ``Device360 Navigate to Monitor Clients``
        :return: 1 if navigation was successful, else -1
        """
        ret_val = self.select_monitor_tab()
        if ret_val != -1:
            ret_val = self.select_monitor_clients()

        return ret_val

    def select_monitor_diagnostics(self, **kwargs):
        """
        - This keyword clicks the Diagnostics button on the Monitor tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor tab.
        - Flow: Device 360 Window --> Monitor tab --> Click "Diagnostics" button
        - Keyword Usage:
        - ``Select Monitor Diagnostics``
        :return: 1 if Monitor> Diagnostics was selected, else -1
        """
        diag_btn = self.get_device360_monitor_diagnostics_button()
        if diag_btn:
            self.utils.print_info("Clicking Diagnostics button on the Device360 Monitor tab")
            self.auto_actions.click(diag_btn)
            kwargs['pass_msg'] = "Monitor> Diagnostics was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Could not find Diagnostics button -make sure Device360 window is open and on " \
                                 "Monitor tab"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_navigate_to_monitor_diagnostics(self):
        """
        - This keyword navigates to the Monitor> Diagnostics view in the Device360 dialog window.
          It assumes the Device360 Window is open.
        - Flow: Device 360 Window --> Click "Monitor" tab --> Click "Diagnostics" button
        - Keyword Usage:
        - ``Device360 Navigate to Monitor Diagnostics``
        :return: 1 if navigation was successful, else -1
        """
        ret_val = self.select_monitor_tab()
        if ret_val != -1:
            ret_val = self.select_monitor_diagnostics()

        return ret_val

    def confirm_device360_monitor_overview_chart_displayed(self, **kwargs):
        """
        - This keyword confirms the chart on the Monitor> Overview page in the Device360 dialog window is displayed.
          It assumes the Device360 Window is open and on the Monitor> Overview tab.
        - Keyword Usage:
        - ``Confirm Device360 Monitor Overview Chart Displayed``
        :return: 1 if the chart is displayed, else -1
        """
        the_chart = self.get_device360_monitor_overview_chart_graph()
        if the_chart:
            if the_chart.is_displayed():
                kwargs['pass_msg'] = "Monitor> Overview was selected"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Monitor> Overview chart is not displayed"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not find chart for Monitor> Overview page"
            self.common_validation.failed(**kwargs)
            return -1

    def confirm_device360_monitor_clients_chart_displayed(self, **kwargs):
        """
        - This keyword confirms the chart on the Monitor> Clients page in the Device360 dialog window is displayed.
          It assumes the Device360 Window is open and on the Monitor> Clients tab.
        - Keyword Usage:
        - ``Confirm Device360 Monitor Clients Chart Displayed``
        :return: 1 if the chart is displayed, else -1
        """
        the_chart = self.get_device360_monitor_clients_chart_graph()
        if the_chart:
            if the_chart.is_displayed():
                kwargs['pass_msg'] = "Monitor> Clients was selected"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Monitor> Clients chart is not displayed"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not find chart for Monitor> Clients page"
            self.common_validation.failed(**kwargs)
            return -1

    def confirm_device360_monitor_diagnostics_chart_displayed(self, **kwargs):
        """
        - This keyword confirms the chart on the Monitor> Diagnostics page in the Device360 dialog window is displayed.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Confirm Device360 Monitor Diagnostics Chart Displayed``
        :return: 1 if the chart is displayed, else -1
        """
        the_chart = self.get_device360_monitor_diagnostics_chart_graph()
        if the_chart:
            if the_chart.is_displayed():
                kwargs['pass_msg'] = "Monitor> Diagnostics was selected"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Monitor> Diagnostics chart is not displayed"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not find chart for Monitor> Diagnostics page"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_select_time_range(self, time_range, **kwargs):
        """
        - This keyword selects the specified time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.
        - Keyword Usage:
        - ``Device360 Select Time Range    Day``
        - ``Device360 Select Time Range    Week``
        - ``Device360 Select Time Range    Month``
        :param  time_range  indicates which time range value to select (e.g., Day, Week, Month)
        :return: 1 if the specified time range was selected, else -1
        """
        time_range_dd = self.get_device360_time_range_drop_down()
        if time_range_dd:
            self.utils.print_info("Opening Time Range drop down")
            self.auto_actions.click(time_range_dd)

            time_range_items = self.get_device360_time_range_drop_down_items()
            if time_range_items:
                if self.auto_actions.select_drop_down_options(time_range_items, time_range):
                    self.utils.print_info(f"Selected '{time_range}' from Time Range drop down")
                    ret_val = 1
                else:
                    self.utils.print_info(f"'{time_range}' option is not present in Time Range drop down")
                    self.utils.print_info("Closing Time Range drop down")
                    self.auto_actions.click(time_range_dd)
                    ret_val = -1
            else:
                self.utils.print_info("Unable to find Time Range drop down items")
                self.utils.print_info("Closing Time Range drop down")
                self.auto_actions.click(time_range_dd)
                ret_val = -1
        else:
            self.utils.print_info("Unable to find Time Range drop down")
            ret_val = -1

        if ret_val == -1:
            if not time_range_dd:
                kwargs['fail_msg'] = "Unable to find Time Range drop down"
                self.common_validation.fault(**kwargs)
            elif not time_range_items:
                kwargs['fail_msg'] = "Unable to find Time Range drop down items"
                self.common_validation.fault(**kwargs)
            else:
                kwargs['fail_msg'] = f"'{time_range}' option is not present in Time Range drop down"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The specified range was selected"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_device360_time_range_selected(self, time_range, **kwargs):
        """
        - This keyword confirms the specified time range is selected in the Device360 dialog window.
          It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.
        - Keyword Usage:
        - ``Confirm Device360 Time Range Selected    Day``
        - ``Confirm Device360 Time Range Selected    Week``
        - ``Confirm Device360 Time Range Selected    Month``
        :param  time_range  indicates which time range value to check for (e.g., Day, Week, Month)
        :return: 1 if the specified time range is currently selected, else -1
        """
        time_range_sel = self.get_device360_time_range_drop_down_selection()
        if time_range_sel:
            if time_range_sel == time_range:
                kwargs['pass_msg'] = f"Current time range selection is '{time_range_sel}'"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"Current time range selection is '{time_range_sel}', " \
                                     f"not the expected '{time_range}'"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not determine current time range selection"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_select_day_time_range(self):
        """
        - This keyword selects the 'Day' time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.
        - Keyword Usage:
        - ``Device360 Select Day Time Range``
        :return: 1 if selection was successful, else -1
        """
        return self.device360_select_time_range("Day")

    def device360_select_week_time_range(self):
        """
        - This keyword selects the 'Week' time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.
        - Keyword Usage:
        - ``Device360 Select Week Time Range``
        :return: 1 if selection was successful, else -1
        """
        return self.device360_select_time_range("Week")

    def device360_select_month_time_range(self):
        """
        - This keyword selects the 'Month' time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.
        - Keyword Usage:
        - ``Device360 Select Month Time Range``
        :return: 1 if selection was successful, else -1
        """
        return self.device360_select_time_range("Month")

    def device360_select_day_time_range_hours_button(self, hours_value, **kwargs):
        """
        - This keyword selects the specified Day time range hours button in the Device360 dialog window.
          It assumes the Device360 Window is open and a Day time range is selected.
        - Keyword Usage:
        - ``Device360 Select Day Time Range Hours Button    1``
        - ``Device360 Select Day Time Range Hours Button    2``
        - ``Device360 Select Day Time Range Hours Button    4``
        - ``Device360 Select Day Time Range Hours Button    8``
        - ``Device360 Select Day Time Range Hours Button    24``
        :param  hours_value  string indicating which hours value to select (e.g., 1, 2, 4, 8, 24)
        :return: 1 if the specified button was clicked, else -1
        """
        day_selected = self.confirm_device360_time_range_selected("Day")
        if day_selected == 1:
            hours_btn = None
            if hours_value == "1":
                hours_btn = self.get_device360_day_time_range_one_hour_button()
            elif hours_value == "2":
                hours_btn = self.get_device360_day_time_range_two_hour_button()
            elif hours_value == "4":
                hours_btn = self.get_device360_day_time_range_four_hour_button()
            elif hours_value == "8":
                hours_btn = self.get_device360_day_time_range_eight_hour_button()
            elif hours_value == "24":
                hours_btn = self.get_device360_day_time_range_twenty_four_hour_button()
            else:
                self.utils.print_info(f"Unexpected Day time range hours value: '{hours_value}'")

            if hours_btn:
                self.utils.print_info(f"Clicking {hours_value} Hour(s) button for Day time range")
                self.auto_actions.click(hours_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find {hours_value} Hour(s) button for Day time range")
                ret_val = -1
        else:
            self.utils.print_info("Incorrect time range selected;  please select 'Day' time range")
            ret_val = -1

        if ret_val == -1:
            if day_selected != 1:
                kwargs['fail_msg'] = "Incorrect time range selected;  please select 'Day' time range"
                self.common_validation.fault(**kwargs)
            else:
                kwargs['fail_msg'] = f"Unable to find {hours_value} Hour(s) button for Day time range"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Clicked {hours_value} Hour(s) button for Day time range"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_select_day_time_range_one_hour(self):
        """
        - This keyword selects the '1 Hour' Day time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Day" time range.
        - Keyword Usage:
        - ``Device360 Select Day Time Range One Hour``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_day_time_range_hours_button("1")

    def device360_select_day_time_range_two_hours(self):
        """
        - This keyword selects the '2 Hours' Day time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Day" time range.
        - Keyword Usage:
        - ``Device360 Select Day Time Range Two Hours``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_day_time_range_hours_button("2")

    def device360_select_day_time_range_four_hours(self):
        """
        - This keyword selects the '4 Hours' Day time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Day" time range.
        - Keyword Usage:
        - ``Device360 Select Day Time Range Four Hours``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_day_time_range_hours_button("4")

    def device360_select_day_time_range_eight_hours(self):
        """
        - This keyword selects the '8 Hours' Day time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Day" time range.
        - Keyword Usage:
        - ``Device360 Select Day Time Range Eight Hours``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_day_time_range_hours_button("8")

    def device360_select_day_time_range_twenty_four_hours(self):
        """
        - This keyword selects the '24 Hours' Day time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Day" time range.
        - Keyword Usage:
        - ``Device360 Select Day Time Range Twenty Four Hours``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_day_time_range_hours_button("24")

    def device360_select_week_time_range_days_button(self, days_value, **kwargs):
        """
        - This keyword selects the specified Week time range days button in the Device360 dialog window.
          It assumes the Device360 Window is open and a Week time range is selected.
        - Keyword Usage:
        - ``Device360 Select Week Time Range Days Button    1``
        - ``Device360 Select Week Time Range Days Button    2``
        - ``Device360 Select Week Time Range Days Button    7``
        :param  days_value  string indicating which days value to select (e.g., 1, 2, 7)
        :return: 1 if the specified button was clicked, else -1
        """
        days_btn = None
        week_selected = self.confirm_device360_time_range_selected("Week")
        if week_selected == 1:
            if days_value == "1":
                days_btn = self.get_device360_week_time_range_one_day_button()
            elif days_value == "2":
                days_btn = self.get_device360_week_time_range_two_days_button()
            elif days_value == "7":
                days_btn = self.get_device360_week_time_range_seven_days_button()
            else:
                self.utils.print_info(f"Unexpected Week time range days value: '{days_value}'")

            if days_btn:
                self.utils.print_info(f"Clicking {days_value} Day(s) button for Week time range")
                self.auto_actions.click(days_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find {days_value} Day(s) button for Week time range")
                ret_val = -1
        else:
            self.utils.print_info("Incorrect time range selected;  please select 'Week' time range")
            ret_val = -1

        if ret_val == -1:
            if week_selected != 1:
                kwargs['fail_msg'] = "Incorrect time range selected;  please select 'Week' time range"
                self.common_validation.fault(**kwargs)
            else:
                kwargs['fail_msg'] = f"Unable to find {days_value} Day(s) button for Week time range"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Clicked {days_value} Hour(s) button for Week time range"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_select_week_time_range_one_day(self):
        """
        - This keyword selects the '1 Day' Week time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Week" time range.
        - Keyword Usage:
        - ``Device360 Select Week Time Range One Day``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_week_time_range_days_button("1")

    def device360_select_week_time_range_two_days(self):
        """
        - This keyword selects the '2 Days' Week time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Week" time range.
        - Keyword Usage:
        - ``Device360 Select Week Time Range Two Days``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_week_time_range_days_button("2")

    def device360_select_week_time_range_seven_days(self):
        """
        - This keyword selects the '7 Days' Week time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Week" time range.
        - Keyword Usage:
        - ``Device360 Select Week Time Range Seven Days``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_week_time_range_days_button("7")

    def device360_select_month_time_range_days_button(self, days_value, **kwargs):
        """
        - This keyword selects the specified Month time range days button in the Device360 dialog window.
          It assumes the Device360 Window is open and a Month time range is selected.
        - Keyword Usage:
        - ``Device360 Select Month Time Range Days Button    7``
        - ``Device360 Select Month Time Range Days Button    14``
        - ``Device360 Select Month Time Range Days Button    30``
        - ``Device360 Select Month Time Range Days Button    90``
        :param  days_value  string indicating which days value to select (e.g., 7, 14, 30, 90)
        :return: 1 if the specified button was clicked, else -1
        """
        days_btn = None
        month_selected = self.confirm_device360_time_range_selected("Month")
        if month_selected == 1:
            if days_value == "7":
                days_btn = self.get_device360_month_time_range_seven_days_button()
            elif days_value == "14":
                days_btn = self.get_device360_month_time_range_fourteen_days_button()
            elif days_value == "30":
                days_btn = self.get_device360_month_time_range_thirty_days_button()
            elif days_value == "90":
                days_btn = self.get_device360_month_time_range_ninety_days_button()
            else:
                self.utils.print_info(f"Unexpected Month time range days value: '{days_value}'")

            if days_btn:
                self.utils.print_info(f"Clicking {days_value} Day(s) button for Month time range")
                self.auto_actions.click(days_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Unable to find {days_value} Day(s) button for Month time range")
                ret_val = -1
        else:
            self.utils.print_info("Incorrect time range selected;  please select 'Month' time range")
            ret_val = -1

        if ret_val == -1:
            if month_selected != 1:
                kwargs['fail_msg'] = "Incorrect time range selected;  please select 'Month' time range"
                self.common_validation.fault(**kwargs)
            else:
                kwargs['fail_msg'] = f"Unable to find {days_value} Day(s) button for Month time range"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Clicked {days_value} Day(s) button for Month time range"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_select_month_time_range_seven_days(self):
        """
        - This keyword selects the '7 Days' Month time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Month" time range.
        - Keyword Usage:
        - ``Device360 Select Month Time Range Seven Days``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_month_time_range_days_button("7")

    def device360_select_month_time_range_fourteen_days(self):
        """
        - This keyword selects the '14 Days' time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Month" time range.
        - Keyword Usage:
        - ``Device360 Select Month Time Range Fourteen Days``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_month_time_range_days_button("14")

    def device360_select_month_time_range_thirty_days(self):
        """
        - This keyword selects the '30 Days' time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Month" time range.
        - Keyword Usage:
        - ``Device360 Select Month Time Range Thirty Days``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_month_time_range_days_button("30")

    def device360_select_month_time_range_ninety_days(self):
        """
        - This keyword selects the '90 Days' time range in the Device360 dialog window.
          It assumes the Device360 Window is open and on the "Month" time range.
        - Keyword Usage:
        - ``Device360 Select Month Time Range Ninety Days``
        :return: 1 if button was clicked, else -1
        """
        return self.device360_select_month_time_range_days_button("90")

    def device360_port_diagnostics_select_all_ports(self, **kwargs):
        """
        - This keyword clicks the 'Select All Ports' button on the Port Diagnostics page in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics page.
        - Keyword Usage:
        - ``Device360 Port Diagnostics Select All Ports``
        :return: 1 if button was clicked, else -1
        """
        sel_btn = self.get_device360_port_diagnostics_select_all_ports_button()
        if sel_btn:
            self.utils.print_info("Clicking 'Select All Ports' button")
            self.auto_actions.click(sel_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Select All Ports' button")
            ret_val = -1

        if ret_val == -1:
            kwargs['fail_msg'] = "Unable to find 'Select All Ports' button"
            self.common_validation.fault(**kwargs)
        else:
            kwargs['pass_msg'] = "Clicked 'Select All Ports' button"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_port_diagnostics_deselect_all_ports(self, **kwargs):
        """
        - This keyword clicks the 'Deselect All Ports' button on the Port Diagnostics page in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics page.
        - Keyword Usage:
        - ``Device360 Port Diagnostics Deselect All Ports``
        :return: 1 if button was clicked, else -1
        """
        desel_btn = self.get_device360_port_diagnostics_deselect_all_ports_button()
        if desel_btn:
            self.utils.print_info("Clicking 'Deselect All Ports' button")
            self.auto_actions.click(desel_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Deselect All Ports' button")
            ret_val = -1

        if ret_val == -1:
            kwargs['fail_msg'] = "Unable to find 'Select All Ports' button"
            self.common_validation.fault(**kwargs)
        else:
            kwargs['pass_msg'] = "Clicked 'Deselect All Ports' button"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_port_diagnostics_select_port(self, port_num):
        """
        - This keyword selects the specified port on the Monitor> Diagnostics page.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Device360 Port Diagnostics Select Port    3``
        :param  port_num    specifies which port to select
        :return: none
        """
        port_list = self.get_device360_port_diagnostics_deselected_ports()
        port_clicked = self._click_port(port_list, port_num)
        if not port_clicked:
            self.utils.print_info(f"Port '{port_num}' is already selected")

    def device360_port_diagnostics_deselect_port(self, port_num):
        """
        - This keyword deselects the specified port on the Monitor> Diagnostics page.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Device360 Port Diagnostics Deselect Port    3``
        :param  port_num    specifies which port to deselect
        :return: none
        """
        port_list = self.get_device360_port_diagnostics_selected_ports()
        port_clicked = self._click_port(port_list, port_num)
        if not port_clicked:
            self.utils.print_info(f"Port '{port_num}' is already deselected")

    def _click_port(self, port_list, port_num):
        """
        - This internal keyword clicks the specified port in the specified port list.
        :param  port_list   list of ports
        :param  port_num    port number of the port to click
        :return: True if port was clicked, False if it was not clicked
        """
        port_clicked = False
        if port_list:
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                if str(data_jack_index) == port_num:
                    self.utils.print_info(f"Clicking port '{port_num}'")
                    self.auto_actions.click(port)
                    port_clicked = True
                    break
        else:
            self.utils.print_info("Empty port list specified")
        return port_clicked

    def confirm_device360_port_diagnostics_all_ports_selected(self, **kwargs):
        """
        - This keyword confirms all ports on the Monitor> Diagnostics page are selected in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Confirm Device360 Port Diagnostics All Ports Selected``
        :return: 1 if all ports are selected, else -1
        """
        port_list = self.get_device360_port_diagnostics_deselected_ports()
        port_count = len(port_list)
        if port_count == 0:
            self.utils.print_info("All ports are selected")
            kwargs['pass_msg'] = "All ports are selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info(f"{port_count} ports are not selected")
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                self.utils.print_info(f"-- deselected port: data jack index '{data_jack_index}'")

            kwargs['fail_msg'] = f"deselected port: data jack index '{data_jack_index}'"
            self.common_validation.failed(**kwargs)
            return -1

    def confirm_device360_port_diagnostics_all_ports_deselected(self, **kwargs):
        """
        - This keyword confirms all ports on the Monitor> Diagnostics page are deselected in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Confirm Device360 Port Diagnostics All Ports Deselected``
        :return: 1 if all ports are deselected, else -1
        """
        port_list = self.get_device360_port_diagnostics_selected_ports()
        port_count = len(port_list)
        if port_count == 0:
            self.utils.print_info("All ports are deselected")
            kwargs['pass_msg'] = "All ports are deselected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info(f"{port_count} ports are selected")
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                self.utils.print_info(f"-- selected port: data jack index '{data_jack_index}'")
            kwargs['fail_msg'] = f"selected port: data jack index '{data_jack_index}'"
            self.common_validation.failed(**kwargs)
            return -1

    def confirm_device360_port_diagnostics_port_selected(self, port_num, **kwargs):
        """
        - This keyword confirms the specified port on the Monitor> Diagnostics page is selected.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Confirm Device360 Port Diagnostics Port Selected    3``
        :param  port_num    specifies which port should be selected
        :return: 1 if the specified ports are selected, else -1
        """
        ret_val = -1

        self.utils.print_info(f"Checking if port {port_num} is selected")
        port_list = self.get_device360_port_diagnostics_selected_ports()
        if port_list:
            port_count = len(port_list)
            self.utils.print_info(f"There are {port_count} selected ports to check")
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                self.utils.print_debug(f"Looking at port index {str(data_jack_index)}")
                if str(data_jack_index) == port_num:
                    self.utils.print_info(f"Port '{port_num}' is selected'")
                    ret_val = 1
                    break
        else:
            self.utils.print_info("No ports are selected")

        if ret_val == -1:
            kwargs['fail_msg'] = f"Port {port_num} is not selected"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The specified ports are deselected"
            self.common_validation.passed(**kwargs)
        return ret_val

    def confirm_device360_port_diagnostics_port_deselected(self, port_num, **kwargs):
        """
        - This keyword confirms the specified port on the Monitor> Diagnostics page is deselected.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Confirm Device360 Port Diagnostics Port Deselected    3``
        :param  port_num    specifies which port should be deselected
        :return: 1 if the specified ports are selected, else -1
        """
        ret_val = -1

        self.utils.print_info(f"Checking if port {port_num} is deselected")
        port_list = self.get_device360_port_diagnostics_deselected_ports()
        if port_list:
            port_count = len(port_list)
            self.utils.print_info(f"There are {port_count} deselected ports to check")
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                self.utils.print_debug(f"Looking at port index {str(data_jack_index)}")
                if str(data_jack_index) == port_num:
                    self.utils.print_info(f"Port '{port_num}' is deselected'")
                    ret_val = 1
                    break
        else:
            self.utils.print_info("No ports are deselected")

        if ret_val == -1:
            kwargs['fail_msg'] = f"Port {port_num} is not deselected"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The specified ports are selected"
            self.common_validation.passed(**kwargs)
        return ret_val

    def get_device360_overview_information(self, device_mac='', device_name=''):
        """
        - This keyword gets information from device360 page eg Model, Serial Number, etc
        - Flow : Manage-->Devices-->click on XMC hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Get Device360 Overview Information   device_mac=${MAC}``
        - ``Get Device360 Overview Information   device_name=${DEVICE_NAME}``
        :param device_mac: MAC Address of the device to access the D360 view for
        :param device_name:  Host Name of the device to access the D360 view for
        :return: dictionary of information from the Overview tab of the Device360 view
        """

        device_info = -1

        if device_mac:
            self.utils.print_info(f"Checking Search Result with MAC address {device_mac}")
            xmc_row = self.dev.get_device_row(device_mac=device_mac)
            if xmc_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)
                device_info = self.get_overview_information()
                self.close_device360_window()

        elif device_name:
            self.utils.print_info(f"Checking Search Result with Host Name {device_name}")
            xmc_row = self.dev.get_device_row(device_name=device_name)
            if xmc_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)
                device_info = self.get_overview_information()
                self.close_device360_window()

        else:
            self.utils.print_info("Unable to get overview information - please specify a MAC address or host name")

        return device_info

    def get_overview_information(self):
        """
        - This keyword gets information from the Monitor> Overview page of the Device360 view
        - It is assumed that the Device360 window is open and on the Monitor> Overview page
        - Flow : Device 360 Page -> Monitor -> Overview
        - Keyword Usage
        - ``Get Overview Information``
        :return: dictionary of information obtained from the Monitor> Overview page of the Device360 view
        """

        self.utils.print_info("Getting device360 Monitor> Overview Information.")
        device360_info = dict()

        # Host Name
        host_name_field = self.dev360.get_system_info_device_host_name()
        if host_name_field:
            device360_info["host_name"] = host_name_field.text
        else:
            self.utils.print_info("Unable to obtain the Host Name field")

        # IP Address
        ip_address_field = self.dev360.get_overview_ip_address()
        if ip_address_field:
            ip_address = ip_address_field.text
            device360_info["ip_address"] = ip_address.split('\n')[-1]
        else:
            self.utils.print_info("Unable to obtain the IP Address field")

        # MAC Address
        mac_address_field = self.dev360.get_overview_mac_address()
        if mac_address_field:
            mac_address = mac_address_field.text
            device360_info["mac_address"] = mac_address.split('\n')[-1]
        else:
            self.utils.print_info("Unable to obtain the MAC Address field")

        # Serial Number
        serial_number_field = self.dev360.get_overview_serial()
        if serial_number_field:
            serial_number = serial_number_field.text
            device360_info["serial_number"] = serial_number.split('\n')[-1]
        else:
            self.utils.print_info("Unable to obtain the Serial Number field")

        # Device Model
        device_model_field = self.dev360.get_overview_model()
        if device_model_field:
            device_model = device_model_field.text
            device360_info["device_model"] = device_model.split('\n')[-1]
        else:
            self.utils.print_info("Unable to obtain the Device Model field")

        # Device Make
        device_make_field = self.dev360.get_overview_make()
        if device_make_field:
            device_make = device_make_field.text
            device360_info["device_make"] = device_make.split('\n')[-1]
        else:
            self.utils.print_info("Unable to obtain the Device Make field")

        # Software Version
        software_version_field = self.dev360.get_overview_software_version()
        if software_version_field:
            software_version = software_version_field.text
            device360_info["software_version"] = software_version.split('\n')[-1]
        else:
            self.utils.print_info("Unable to obtain the Software Version field")

        self.utils.print_info("****************** Device360 Overview Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        return device360_info

    def device360_set_device_function(self, value="AP", **kwargs):
        """
        - This keyword sets the Device Function value on the Device Configuration page.
        - It is assumed that the Device360 window is open.
        - Flow : Device 360 Page -> Configure -> Device Configuration
        - Keyword Usage
        - ``Device360 Set Device Function  AP``
        - ``Device360 Set Device Function  ApAsRouter``
        :return: 1 if the selection was made, -1 if not
        """
        if self.device360_navigate_to_device_configuration():
            sleep(2)
            device_function_drop_down = self.dev360.get_device360_configure_device_function_dropdown()
            if device_function_drop_down:
                self.utils.print_info("Clicking on Device Function selector")
                sleep(5)
                self.auto_actions.click(device_function_drop_down)
                sleep(2)

                drop_down_items = self.dev360.get_device360_configure_device_function_dropdown_items()
                if self.auto_actions.select_drop_down_options(drop_down_items, value):
                    self.utils.print_info(f"Selected view type '{value}' from drop down")
                    ret_val = 1
                else:
                    self.utils.print_info(f"View type '{value}' is not present in drop down")
                    self.utils.print_info("Closing Device Function selector")
                    self.auto_actions.click(device_function_drop_down)
                    ret_val = -1
            else:
                kwargs['fail_msg'] = "Could not find Device Function selector"
                self.common_validation.fault(**kwargs)
        else:
            kwargs['fail_msg'] = "Unable to navigate to the Device Configuration view"
            self.common_validation.fault(**kwargs)

        if ret_val == -1:
            kwargs['fail_msg'] = f"View type '{value}' is not present in drop down"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = f"Selected view type '{value}' from drop down"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_save_device_configuration(self, **kwargs):
        """
        - This keyword clicks the Save Device Configuration button on the Device Configuration page.
        - It is assumed that the Device360 window is open and on the Device Configuration page.
        - Flow : Device 360 Page -> Configure -> Device Configuration -> Save Device Configuration
        - Keyword Usage
        - ``Device360 Save Device Configuration``
        :return: 1 if the button was clicked, -1 if not
        """
        save_btn = self.dev360.get_device360_configure_device_save_button()
        if save_btn:
            self.utils.print_info("Clicking 'Save Device Configuration' button")
            self.auto_actions.click(save_btn)
            sleep(2)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the 'Save Device Configuration' button")
            ret_val = -1

        if ret_val == -1:
            kwargs['fail_msg'] = "Unable to find the 'Save Device Configuration' button"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Clicked 'Save Device Configuration' button"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_get_device_title(self):
        """
        - This keyword obtains the value of the device title in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Device Title``
        :return: value of the device title in the Device360 view
        """
        ret_val = ""
        device_title = self.dev360.get_device360_device_title()
        if device_title:
            self.utils.print_info(f"Returning device title {device_title.text}")
            ret_val = device_title.text
        else:
            self.utils.print_info("Unable to find the device title")

        return ret_val

    def device360_get_side_bar_information(self):
        """
        - This keyword gets information from the left sidebar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Side Bar Information``
        :return: dictionary of information obtained from the left side bar of the Device360 view
        """

        self.utils.print_info("Getting Device360 Left Side Bar Information")
        device360_info = dict()

        device_model_el = self.dev360.get_sidebar_model()
        device_image_el = self.dev360.get_sidebar_device_image()
        host_name_el = self.dev360.get_sidebar_host_name()
        enabled_ports_el = self.dev360.get_sidebar_enabled_ports()
        disabled_ports_el = self.dev360.get_sidebar_disabled_ports()
        connected_el = self.dev360.get_sidebar_connected_state()
        active_el = self.dev360.get_sidebar_active_since()
        alarms_el = self.dev360.get_sidebar_active_alarms()
        clients_el = self.dev360.get_sidebar_unique_clients()
        cpu_el = self.dev360.get_sidebar_cpu_usage()
        mem_el = self.dev360.get_sidebar_memory_usage()

        if device_model_el:
            device360_info["device_model"] = device_model_el.text
        else:
            self.utils.print_info("Could not determine value for Device Model")
            device360_info["device_model"] = ""

        if device_image_el:
            image_src = device_image_el.get_attribute("src")
            device360_info["device_image"] = image_src
        else:
            self.utils.print_info("Could not determine value for Device Image")
            device360_info["device_image"] = ""

        if host_name_el:
            device360_info["host_name"] = host_name_el.text
        else:
            self.utils.print_info("Could not determine value for Host Name")
            device360_info["host_name"] = ""

        if enabled_ports_el:
            device360_info["enabled_ports"] = enabled_ports_el.text
        else:
            self.utils.print_info("Could not determine value for Enabled Ports")
            device360_info["enabled_ports"] = ""

        if disabled_ports_el:
            device360_info["disabled_ports"] = disabled_ports_el.text
        else:
            self.utils.print_info("Could not determine value for Disabled Ports")
            device360_info["disabled_ports"] = ""

        if connected_el:
            device360_info["connected_state"] = connected_el.text
        else:
            self.utils.print_info("Could not determine value for Connected state")
            device360_info["connected_state"] = ""

        if active_el:
            active_text = active_el.text
            # This field is currently in the format "Active since: <Days> <Hrs> <Mins> <secs> Ago" so we want to strip
            # off the prefix label ("Active since:") and the suffix label ("Ago").
            self.utils.print_debug(f"Active Since field is {active_text}")
            active_text = re.sub('Active since: ', '', active_text)
            active_text = re.sub(' Ago', '', active_text)
            self.utils.print_debug(f"Stripped Active Since field is {active_text}")
            device360_info["active_since"] = active_text
        else:
            self.utils.print_info("Could not determine value for Active Since")
            device360_info["active_since"] = ""

        if alarms_el:
            device360_info["active_alarms"] = alarms_el.text
        else:
            self.utils.print_info("Could not determine value for Active Alarms")
            device360_info["active_alarms"] = ""

        if clients_el:
            device360_info["unique_clients"] = clients_el.text
        else:
            self.utils.print_info("Could not determine value for Unique Clients")
            device360_info["unique_clients"] = ""

        if cpu_el:
            device360_info["cpu_usage"] = cpu_el.text
        else:
            self.utils.print_info("Could not determine value for CPU Usage")
            device360_info["cpu_usage"] = ""

        if mem_el:
            device360_info["memory_usage"] = mem_el.text
        else:
            self.utils.print_info("Could not determine value for Memory Usage")
            device360_info["memory_usage"] = ""

        self.utils.print_info("****************** Device360 Left Side Bar Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}: {value}")

        return device360_info

    def device360_get_side_bar_cpu_usage(self):
        """
        - This keyword obtains the value of the CPU Usage from the left sidebar in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Side Bar CPU Usage``
        :return: value of the CPU Usage field from the left sidebar in the Device360 view
        """
        ret_val = ""

        cpu_el = self.dev360.get_sidebar_cpu_usage()
        if cpu_el:
            self.utils.print_info(f"Returning CPU Usage {cpu_el.text}")
            ret_val = cpu_el.text
        else:
            self.utils.print_info("Unable to find the CPU Usage value")

        return ret_val

    def device360_get_side_bar_memory_usage(self):
        """
        - This keyword obtains the value of the Memory Usage from the left sidebar in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Side Bar Memory Usage``
        :return: value of the Memory Usage field from the left sidebar in the Device360 view
        """
        ret_val = ""

        mem_el = self.dev360.get_sidebar_memory_usage()
        if mem_el:
            self.utils.print_info(f"Returning Memory Usage {mem_el.text}")
            ret_val = mem_el.text
        else:
            self.utils.print_info("Unable to find the Memory Usage value")

        return ret_val

    def device360_get_side_bar_active_since_information(self):
        """
        - This keyword gets the Active Since information from the left sidebar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Side Bar Active Since Information``
        :return: dictionary of "Active Since" information obtained from the left side bar of the Device360 view
        """

        self.utils.print_info("Getting Device360 Left Side Bar Active Since Information")
        active_info = dict()

        active_el = self.dev360.get_sidebar_active_since()

        if active_el:
            active_text = active_el.text
            # This field is currently in the format "Active since: <Days> <Hrs> <Mins> <secs> Ago" so we want to strip
            # off the prefix label ("Active since:") and the suffix label ("Ago").
            self.utils.print_debug(f"Active Since field is {active_text}")
            active_text = re.sub('Active since: ', '', active_text)
            active_text = re.sub(' Ago', '', active_text)
            self.utils.print_debug(f"Stripped Active Since field is {active_text}")

            # Parse the data into each component
            # Days
            days_split = active_text.split("Days")
            if "Days" in active_text:
                active_info["days"] = days_split[0].strip()
                active_text = days_split[1]
            else:
                active_info["days"] = "0"
            # Hours
            hours_split = active_text.split("Hrs")
            if "Hrs" in active_text:
                active_info["hours"] = hours_split[0].strip()
                active_text = hours_split[1]
            else:
                active_info["hours"] = "0"
            # Minutes
            mins_split = active_text.split("Mins")
            if "Mins" in active_text:
                active_info["minutes"] = mins_split[0].strip()
                active_text = mins_split[1]
            else:
                active_info["minutes"] = "0"
            # Seconds
            secs_split = active_text.split("Secs")
            if "Secs" in active_text:
                active_info["seconds"] = secs_split[0].strip()
                active_text = secs_split[1]
            else:
                active_info["seconds"] = "0"
        else:
            self.utils.print_info("Could not determine value for Active Since")
            active_info["days"] = "0"
            active_info["hours"] = "0"
            active_info["minutes"] = "0"
            active_info["seconds"] = "0"

        self.utils.print_info(
            "****************** Device360 Left Side Bar Active Since Information ************************")
        for key, value in active_info.items():
            self.utils.print_info(f"{key}: {value}")

        return active_info

    def device360_get_top_bar_information(self):
        """
        - This keyword gets information from the top bar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Top Bar Information``
        :return: dictionary of information obtained from the top bar of the Device360 view
        """

        self.utils.print_info("Getting Device360 Top Bar Information")
        device360_info = dict()

        cpu_el = self.dev360.get_topbar_cpu()
        mem_el = self.dev360.get_topbar_memory()
        mac_el = self.dev360.get_topbar_mac_usage()
        uptime_el = self.dev360.get_topbar_uptime()
        temp_el = self.dev360.get_topbar_temperature()
        # Commented on 1/18/23 because variable is unused
        # power_el = self.dev360.get_topbar_power()
        # fan_el = self.dev360.get_topbar_fan()
        ip_addr_el = self.dev360.get_topbar_ip_address()
        mac_addr_el = self.dev360.get_topbar_mac_address()
        version_el = self.dev360.get_topbar_software_version()
        model_el = self.dev360.get_topbar_model()
        serial_el = self.dev360.get_topbar_serial()
        make_el = self.dev360.get_topbar_make()

        # Workaround - first element moved to isn't being recognized, so move to Memory element first
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
        if cpu_el:
            self.auto_actions.move_to_element(cpu_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                self.utils.print_debug(f"Tooltip content for CPU Usage is {tt_text}")
                cpu_values = tt_text.split(":")
                if len(cpu_values) == 2 and cpu_values[0] == "CPU Usage":
                    cpu_value = cpu_values[1].strip()
                    device360_info["cpu_usage"] = cpu_value
                else:
                    self.utils.print_info("Unable to parse value for CPU Usage")
                    device360_info["cpu_usage"] = ""
            else:
                self.utils.print_info("Could not determine value for CPU Usage")
                device360_info["cpu_usage"] = ""
        else:
            self.utils.print_info("Could not find CPU Usage element")
            device360_info["cpu_usage"] = ""

        if mem_el:
            self.auto_actions.move_to_element(mem_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                self.utils.print_debug(f"Tooltip content for Memory is {tt_text}")
                mem_values = tt_text.split(":")
                if len(mem_values) == 2 and mem_values[0] == "Memory":
                    mem_value = mem_values[1].strip()
                    device360_info["memory_usage"] = mem_value
                else:
                    self.utils.print_info("Unable to parse value for Memory Usage")
                    device360_info["memory_usage"] = ""
            else:
                self.utils.print_info("Could not determine value for Memory Usage")
                device360_info["memory_usage"] = ""
        else:
            self.utils.print_info("Could not find Memory Usage element")
            device360_info["memory_usage"] = ""

        if mac_el:
            self.auto_actions.move_to_element(mac_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                self.utils.print_debug(f"Tooltip content for MAC Table Utilization is {tt_text}")
                mac_values = tt_text.split(":")
                if len(mac_values) == 2 and mac_values[0] == "MAC Table Utilization":
                    mac_value = mac_values[1].strip()
                    device360_info["mac_usage"] = mac_value
                else:
                    self.utils.print_info("Unable to parse value for MAC Table Utilization")
                    device360_info["mac_usage"] = ""
            else:
                self.utils.print_info("Could not determine value for MAC Table Utilization")
                device360_info["mac_usage"] = ""
        else:
            self.utils.print_info("Could not find MAC Table Utilization element")
            device360_info["mac_usage"] = ""

        if uptime_el:
            self.auto_actions.move_to_element(uptime_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                # This field is currently in the format "Uptime: Last seen: <date>, <time>" so we want to strip
                # off the label ("Uptime: Last seen:"), and remove the comma from the date and time portion.
                # NOTE: This may change when APC-45218 is addressed.
                self.utils.print_debug(f"Tooltip content for Uptime is {tt_text}")
                tt_text = re.sub('Uptime: Last seen: ', '', tt_text)
                self.utils.print_debug(f"Stripped tooltip content for Uptime is {tt_text}")
                uptime_values = tt_text.split(",")
                if len(uptime_values) == 2:
                    uptime_date = uptime_values[0].strip()
                    uptime_time = uptime_values[1].strip()
                    device360_info["uptime"] = uptime_date + " " + uptime_time
                else:
                    self.utils.print_info("Unable to parse value for Uptime")
                    device360_info["uptime"] = ""
            else:
                self.utils.print_info("Could not determine value for Uptime")
                device360_info["uptime"] = ""
        else:
            self.utils.print_info("Could not find Uptime element")
            device360_info["uptime"] = ""

        if temp_el:
            device360_info["temperature"] = temp_el.text
        else:
            self.utils.print_info("Could not determine value for Temperature")
            device360_info["temperature"] = ""

        if ip_addr_el:
            ip_addr_text = ip_addr_el.text
            device360_info["ip_address"] = ip_addr_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for IP Address")
            device360_info["ip_address"] = ""

        if mac_addr_el:
            mac_addr_text = mac_addr_el.text
            device360_info["mac_address"] = mac_addr_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for MAC Address")
            device360_info["mac_address"] = ""

        if version_el:
            version_text = version_el.text
            device360_info["software_version"] = version_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Software Version")
            device360_info["software_version"] = ""

        if model_el:
            model_text = model_el.text
            device360_info["device_model"] = model_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Device Model")
            device360_info["device_model"] = ""

        if serial_el:
            serial_text = serial_el.text
            device360_info["serial_number"] = serial_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Serial Number")
            device360_info["serial_number"] = ""

        if make_el:
            make_text = make_el.text
            device360_info["device_make"] = make_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Device Make")
            device360_info["device_make"] = ""

        for key, value in device360_info.items():
            self.utils.print_info(f"{key}: {value}")

        return device360_info

    def device360_get_top_bar_cpu_usage(self):
        """
        - This keyword obtains the value of the CPU Usage from the top bar in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Top Bar CPU Usage``
        :return: value of the CPU Usage field from the top bar in the Device360 view
        """
        ret_val = ""

        cpu_el = self.dev360.get_topbar_cpu()
        mem_el = self.dev360.get_topbar_memory()

        # Workaround - first element moved to isn't being recognized, so move to Memory element first
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
        if cpu_el:
            self.auto_actions.move_to_element(cpu_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                self.utils.print_debug(f"Tooltip content for CPU Usage is {tt_text}")
                cpu_values = tt_text.split(":")
                if len(cpu_values) == 2 and cpu_values[0] == "CPU Usage":
                    cpu_value = cpu_values[1].strip()
                    ret_val = cpu_value
                else:
                    self.utils.print_info("Unable to parse value for CPU Usage")
            else:
                self.utils.print_info("Could not determine value for CPU Usage")
        else:
            self.utils.print_info("Could not find CPU Usage element")

        return ret_val

    def device360_get_top_bar_memory_usage(self):
        """
        - This keyword obtains the value of the Memory Usage from the top bar in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Top Bar Memory Usage``
        :return: value of the Memory Usage field from the top bar in the Device360 view
        """
        ret_val = ""

        mem_el = self.dev360.get_topbar_memory()
        cpu_el = self.dev360.get_topbar_cpu()

        # Workaround - first element moved to isn't being recognized, so move to CPU element first
        if cpu_el:
            self.auto_actions.move_to_element(cpu_el)
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                self.utils.print_debug(f"Tooltip content for Memory is {tt_text}")
                mem_values = tt_text.split(":")
                if len(mem_values) == 2 and mem_values[0] == "Memory":
                    mem_value = mem_values[1].strip()
                    ret_val = mem_value
                else:
                    self.utils.print_info("Unable to parse value for Memory Usage")
            else:
                self.utils.print_info("Could not determine value for Memory Usage")
        else:
            self.utils.print_info("Could not find Memory Usage element")

        return ret_val

    def device360_get_top_bar_last_update_time(self):
        """
        - This keyword gets information from the left sidebar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Top Bar Last Update Time``
        :return: last update time if successful, otherwise None
        """
        ret_val = ""

        self.utils.print_info("Getting Device360 Last Update Time")
        uptime_el = self.dev360.get_topbar_uptime()

        # Workaround - first element moved to isn't being recognized, so move to Memory element first
        mem_el = self.dev360.get_topbar_memory()
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
        if uptime_el:
            # Workaround - first element moved to isn't being recognized, so move twice
            self.auto_actions.move_to_element(uptime_el)
            self.auto_actions.move_to_element(uptime_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                # This field is currently in the format "Uptime: Last seen: <date>, <time>" so we want to strip
                # off the label ("Uptime: Last seen:"), and remove the comma from the date and time portion.
                # NOTE: This may change when APC-45218 is addressed.
                self.utils.print_debug(f"Tooltip content for Uptime is {tt_text}")
                tt_text = re.sub('Uptime: Last seen: ', '', tt_text)
                self.utils.print_debug(f"Stripped tooltip content for Uptime is {tt_text}")
                uptime_values = tt_text.split(",")
                if len(uptime_values) == 2:
                    uptime_date = uptime_values[0].strip()
                    uptime_time = uptime_values[1].strip()
                    ret_val = uptime_date + " " + uptime_time
                    self.utils.print_info(f"Returning Last Update Time {ret_val}")
                else:
                    self.utils.print_info("Unable to parse value for Uptime")
            else:
                self.utils.print_info("Could not determine value for Uptime")
        else:
            self.utils.print_info("Could not find Uptime element")

        return ret_val

    def device360_get_top_bar_temperature(self):
        """
        - This keyword obtains the value of the Temperature field from the top bar in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Top Bar Temperature``
        :return: value of the Temperature field from the top bar in the Device360 view
        """
        ret_val = ""

        temp_el = self.dev360.get_topbar_temperature()
        if temp_el:
            ret_val = temp_el.text
        else:
            self.utils.print_info("Could not determine value for Temperature")

        return ret_val

    def device360_get_port_icon_count(self):
        """
        - This keyword gets the number of port icons displayed in the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Port Icon Count``
        :return: number of port icons displayed in the Device360 view
        """
        ret_val = 0

        self.utils.print_info("Getting Device360 Port Icon Count")

        port_icon_list = self.dev360.get_overview_port_icons()
        if port_icon_list:
            ret_val = len(port_icon_list)
        else:
            self.utils.print_info("Unable to get the list of port icons")

        self.utils.print_info(f"Returning port icon count {ret_val}")
        return ret_val

    def device360_is_port_details_table_displayed(self):
        """
        - This keyword determines if the port details table is displayed in the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Is Port Details Table Displayed``
        :return: 1 if port table is displayed, else 0
        """
        ret_val = 0

        self.utils.print_info("Getting Device360 Port Details Table")

        port_table = self.dev360.get_overview_port_details_table()
        if port_table:
            if port_table.is_displayed():
                ret_val = 1
            else:
                self.utils.print_info("Port Details Table is not being displayed")
        else:
            self.utils.print_info("Unable to find Port Details Table")

        return ret_val

    def device360_get_total_active_alarms_count(self):
        """
        - This keyword gets the total active alarms displayed in the Active Alarms panel of the Device360 view.
        - It is assumed that the Device360 window is open and on the Overview tab.
        - Keyword Usage
        - ``Device360 Get Total Active Alarms Count``
        :return: total number of active alarms displayed in the Device360 view
        """
        ret_val = 0

        self.utils.print_info("Getting Device360 Total Active Alarms Count")

        total_count = self.dev360.get_overview_total_active_alarms()
        if total_count:
            ret_val = total_count.text
        else:
            self.utils.print_info("Unable to get the total active alarms count")

        return ret_val

    def device360_check_events_is_in_order(self, **kwargs):
        """
        - This Keyword checks whether the events in D360 are on order

        :return 1 - if the Events severity are in order:
        :return -1 - if the Events severity are not in order:
        """

        severitylist = ["info", "critical", "minor", "major", "clear"]
        prev = None
        events_table = self.dev360.get_device360_events_grid()
        if events_table:
            event_rows = self.dev360.get_device360_events_grid_rows(events_table)
            if event_rows:
                for row in event_rows:
                    sev_val = self.get_device360_event_severity_cell_value(row)
                    if prev is None:
                        pass
                    elif prev != sev_val.lower():
                        severitylist.remove(prev)

                    if sev_val.lower() in severitylist:
                        prev = sev_val.lower()
                    else:
                        self.utils.print_debug("The severity are not in order")
                        kwargs['fail_msg'] = "The Events severity are not in order"
                        self.common_validation.failed(**kwargs)
                        return -1
        self.utils.print_debug("The severity are in order")
        kwargs['pass_msg'] = "The Events severity are in order"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_get_switch_system_information(self):
        """
        - This keyword gets the values from the system information page of the Device360 view for a switch.
        - It is assumed that the Device360 window is open for a switch.
        - Keyword Usage
        - ``Device360 Get Switch System Information``
        :return: dictionary of information obtained from the System Information page of the Device360 view
        """

        self.utils.print_info("Getting Device360 Switch System Information")
        device360_info = dict()

        info_archived_el = None
        info_asset_el = None
        info_ud1_el = None
        info_ud2_el = None
        info_ud3_el = None
        info_ud4_el = None
        info_note_el = None

        # Get the elements from the page
        stale_retry = 1
        while stale_retry <= 10:
            try:
                info_archived_el = self.dev360.get_switch_system_info_archived()
                info_asset_el = self.dev360.get_switch_system_info_asset_tag()
                info_ud1_el = self.dev360.get_switch_system_info_user_data_1()
                info_ud2_el = self.dev360.get_switch_system_info_user_data_2()
                info_ud3_el = self.dev360.get_switch_system_info_user_data_3()
                info_ud4_el = self.dev360.get_switch_system_info_user_data_4()
                info_note_el = self.dev360.get_switch_system_info_note()

                # Break out of the Stale Element Exception loop
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        # Extract the data from the elements
        if info_archived_el:
            device360_info["archived"] = info_archived_el.text
        else:
            self.utils.print_info("Could not determine value for 'Archived'")
            device360_info["archived"] = ""

        if info_asset_el:
            device360_info["asset_tag"] = info_asset_el.text
        else:
            self.utils.print_info("Could not determine value for 'Asset Tag'")
            device360_info["asset_tag"] = ""

        if info_ud1_el:
            device360_info["user_data_1"] = info_ud1_el.text
        else:
            self.utils.print_info("Could not determine value for 'User Data 1'")
            device360_info["user_data_1"] = ""

        if info_ud2_el:
            device360_info["user_data_2"] = info_ud2_el.text
        else:
            self.utils.print_info("Could not determine value for 'User Data 2'")
            device360_info["user_data_2"] = ""

        if info_ud3_el:
            device360_info["user_data_3"] = info_ud3_el.text
        else:
            self.utils.print_info("Could not determine value for 'User Data 3'")
            device360_info["user_data_3"] = ""

        if info_ud4_el:
            device360_info["user_data_4"] = info_ud4_el.text
        else:
            self.utils.print_info("Could not determine value for 'User Data 4'")
            device360_info["user_data_4"] = ""

        if info_note_el:
            device360_info["note"] = info_note_el.text
        else:
            self.utils.print_info("Could not determine value for 'Note'")
            device360_info["note"] = ""

        self.utils.print_info("****************** Device360 Switch System Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}: {value}")

        return device360_info

    def click_hyperlink_on_system_information(self, device_mac=None, device_name=None, Clickon=None, **kwargs):
        """
        - This keyword Clicks SSID or Device Template on system information from device360 page using DeviceMac or Name
        - Flow : Manage--> Devices --> Monitor --> SystemInformation --> click on hyperlink(MAC/hostname)
        - Keyword Usage
        - ``Click HyperLink on System Information  device_mac=${AP1_MAC} Clickon=Template``
        - ``Click HyperLink on System Information  device_name=${AP1_NAME} Clickon=SSID``

        :return: Name of device Template or SSID after navigation by clicking on hyperlink or -1 in case of error
        """
        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Clicking on System Information")
        self.auto_actions.click_reference(self.dev360.get_system_info_button())
        sleep(2)

        try:
            if Clickon == "Template":
                self.auto_actions.click(self.dev360.
                                        get_hyper_link_system_information(
                    self.dev360.get_system_info_device_template()))
                sleep(5)
                text = self.device_template_web_elements.get_ap_template_text().get_attribute("value")
                return text

            elif Clickon == "SSID":
                self.auto_actions.click(self.dev360.
                                        get_hyper_link_system_information(self.get_system_info_device_ssids()))
                sleep(2)
                text = self.wireless_web_elements.get_wireless_ssid_field().get_attribute("value")
                return text

        except Exception:
            kwargs['fail_msg'] = "Unable to Click HyperLink on System Information"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_standalone_devcfg_fetch_snmp_location(self):
        """
        - This keyword gets the value of snmp location from device configuration page of D360
        - Keyword Usage
        - ``Device360 Device Config Snmp Location``
        :return: assigned snmp location
        """

        self.utils.print_info("Getting SNMP location from device config of D360")
        snmp_locn = self.dev360.get_device360_configure_device_snmp_location().get_attribute('value')

        return snmp_locn

    def device360_stack_devcfg_fetch_snmp_location(self):
        """
        - This keyword gets the value of snmp location from device configuration page of D360
        - Keyword Usage
        - ``Device360 Device Config Snmp Location``
        :return: assigned snmp location
        """

        self.utils.print_info("Getting SNMP location from device config of D360")
        snmp_locn = self.dev360.get_device360_stack_configure_device_snmp_location().get_attribute('value')

        # info_note_el = self.dev360.get_switch_system_info_note()
        # self.auto_actions.click_reference(self.get_device360_configure_device_snmp_location)

        return snmp_locn

    def device360_device_configuration_select_template(self, device_mac, sw_template_name, **kwargs):
        """
        This function select the template into d360 and start update process

        :param device_mac: Mac of device
        :param sw_template_name: Policy template
        :return: 1 if update is completed ; -1 else
        """

        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
            self.utils.print_info("D360 page was not opened ")
            kwargs['fail_msg'] = "D360 page was not opened"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.utils.print_info("D360 page was opened ")

        if self.devices_web_elements.get_ap_configure_button():
            self.utils.print_info("Clicking on 'Configure' button  ")
            self.auto_actions.click_reference(self.devices_web_elements.get_ap_configure_button)
        else:
            self.utils.print_info("'Configure' button was not found ")
            kwargs['fail_msg'] = "'Configure' button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        if self.dev360.get_device360_device_configuration_button():
            self.auto_actions.click_reference(self.dev360.get_device360_device_configuration_button)
            self.utils.print_info("Clicking on 'Device Configuration 'button")
        else:
            kwargs['fail_msg'] = "'Device Configuration' button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        # Select from dropdown
        if sw_template_name is not None:
            click_dropdown = self.dev360.get_device360_device_configuration_stack_template_button()
            if click_dropdown:
                self.utils.print_info(" Click on dropdown ")
                self.auto_actions.click(click_dropdown)
                sleep(3)
            else:
                self.utils.print_info(" Not able to find dropdown  ")
            dropdown_items = self.dev360.get_device360_device_configuration_stack_template_items()
            if dropdown_items:
                self.utils.print_info(" The templates from dropdown are: ")
                for elem in dropdown_items:
                    self.utils.print_info(elem.text)
                for el in dropdown_items:
                    if sw_template_name in el.text:
                        self.utils.print_info(f" Select {el.text} from dropdown")
                        self.auto_actions.select_drop_down_options(dropdown_items, el.text)
                        sleep(3)
                    else:
                        self.utils.print_info(" The template name was not found in dropdown")
            else:
                self.utils.print_info(" Not able to find dropdown items ")
        else:
            self.utils.print_info(" The sw_template_name is None  ")

        # Press Save button
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        if self.dev360.get_device360_device_configuration_save_button():
            self.utils.print_info("Click on save button")
            self.auto_actions.click_reference(self.dev360.get_device360_device_configuration_save_button)
        else:
            self.utils.print_info("The save button was not found")

        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_after = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_after)

        for item_after in tool_tp_text_after:
            if item_after in tool_tp_text_before:
                pass
            else:
                if 'Device configuration was updated successfully' in item_after:
                    pass
                else:
                    self.utils.print_info(" Below error message is displayed after press save button")
                    self.utils.print_info(item_after)
                    return item_after
        sleep(10)
        # Press Update button
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        if self.dev360.get_device360_device_configuration_update_button():
            self.utils.print_info("Click on update button")
            self.auto_actions.click_reference(self.dev360.get_device360_device_configuration_update_button)

        else:
            self.utils.print_info("The update button was not found")

        if self.devices_web_elements.get_devices_perform_update_button_d360():
            self.utils.print_info("Click on update performe button")
            self.auto_actions.click_reference(self.devices_web_elements.get_devices_perform_update_button_d360)

        else:
            self.utils.print_info("The update button was not found")

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
                return item_after

        if self.dev360.get_device360_device_configuration_exit_button():
            self.utils.print_info("Click on exit button")
            self.auto_actions.click_reference(self.dev360.get_device360_device_configuration_exit_button)
        else:
            self.utils.print_info("The exit button was not found")

        if self.navigator.navigate_to_devices() == 1:
            self.utils.print_info("Navigate to device ")
        else:
            self.utils.print_info("Cannot navigate to device page")
        return self.dev.check_device_update_status_by_using_mac(device_mac)

    def return_stack_units_number(self, units_serials):
        list = units_serials.split(",")
        self.utils.print_info("The SNs are:", units_serials)
        self.utils.print_info("The dut have {} unit/units".format(len(list)))
        return len(list)

    def device360_search_event_and_confirm_event_description_contains(self, event_str, after_time=None, configuration_event=False, **kwargs):
        """
        - This keyword search event and then confirms that specified event text is present in the description field of the event, after the
          specified time. If no time is specified, it just confirms the event is present.
          It assumes the Device360 Window is open and on the Monitor> Events tab.
          After search is done it confirms that the log is present only on first page of event list. If more logs are matching it returns the number of them
        - Keyword Usage:
        - ``Device360 Search Event And Confirm Event Description Contains  ${EVENT}  ${AFTER_TIME}``
        - ``Device360 Search Event And Confirm Event Description Contains  ${EVENT}``
        :param  event_str:           String to look for in the event description
        :param  after_time:          Indicates at which point in time to start searching for the existence of the event
                                     (if not specified, it just checks for the existence of the event in general)
        :param configuration_event:  If this parameter is True then the search happens in the Configuration Events tab
        :return: 1 if only one log (row in table) is found; If more logs (rows) are found it will be return the number of them; else -1
        """

        if configuration_event:

            configuration_events_button = self.dev360.get_configuration_events_button()
            if not configuration_events_button:
                kwargs["fail_msg"] = "Did not find the configuration_events_button."
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully found the configuration_events_button.")

            if self.auto_actions.click(configuration_events_button) != 1:
                kwargs["fail_msg"] = "Failed to click the configuration_events_button."
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully clicked the configuration_events_button.")

        i = 0
        cont_rows_match = 0
        self.d360Event_search(event_str, **kwargs)
        events_table = self.dev360.get_device360_events_grid()
        if events_table:
            event_rows = self.dev360.get_device360_events_grid_rows(events_table)
            if event_rows:
                for row in event_rows:
                    self.utils.print_info(str(i))
                    i += 1
                    expand_more = self.dev360.get_device360_event_expand_more(row)
                    if expand_more:
                        self.utils.print_info("Clicking on ...more to expand event details.")
                        self.auto_actions.click(expand_more)
                        sleep(5)
                        desc_val = self.get_device360_event_more_expand_value().text
                        self.auto_actions.click_reference(self.get_device360_event_more_close_btn)
                        self.utils.print_debug("Checking row with event description value '" + desc_val + "'")
                        # Check if the event description value for this row contains what we are looking for
                        if event_str in desc_val:
                            # If a time was specified, make sure the timestamp for the event is more recent
                            if after_time:
                                time_val = self.get_device360_event_timestamp_cell_value(row)
                                if time_val > after_time:
                                    self.utils.print_debug(
                                        "Found a match for '" + event_str + ''" after "'' + after_time + "'")
                                    cont_rows_match += 1
                                else:
                                    self.utils.print_debug(
                                        "Found a match for '" + event_str + "' but it has a timestamp before '" + after_time
                                        + "' (" + time_val + ") - looking at next row...")
                            else:
                                self.utils.print_debug("Found a match for '" + event_str + "'")
                                cont_rows_match += 1

                    else:
                        desc_val = self.get_device360_event_description_cell_value(row)
                        self.utils.print_debug("Checking row with event description value '" + desc_val + "'")
                        # Check if the event description value for this row contains what we are looking for
                        if event_str in desc_val:
                            # If a time was specified, make sure the timestamp for the event is more recent
                            if after_time:
                                time_val = self.get_device360_event_timestamp_cell_value(row)
                                if time_val > after_time:
                                    self.utils.print_debug(
                                        "Found a match for '" + event_str + ''" after "'' + after_time + "'")
                                    cont_rows_match += 1
                                else:
                                    self.utils.print_debug(
                                        "Found a match for '" + event_str + "' but it has a timestamp before '" + after_time
                                        + "' (" + time_val + ") - looking at next row...")
                            else:
                                self.utils.print_debug("Found a match for '" + event_str + "'")
                                cont_rows_match += 1
                if cont_rows_match == 0:
                    self.utils.print_info("Not found a match for '" + event_str + "'")
                    kwargs['fail_msg'] = f"Not found a match for {event_str}"
                    self.common_validation.failed(**kwargs)
                    return -1
                else:
                    self.utils.print_info("Found a match for '" + event_str + "' on " + str(cont_rows_match) + " rows")
                    kwargs['pass_msg'] = f"Found a match for {event_str}"
                    self.common_validation.passed(**kwargs)
                    return cont_rows_match
            else:
                self.utils.print_info("Events table does not contain any rows")
        else:
            self.utils.print_info(
                "Could not find Events table - make sure Device360 window is open to the Monitor> Alarms view")
        kwargs['fail_msg'] = "Could not find " \
                             "Events table - make sure Device360 window is open to the Monitor> Alarms view"
        self.common_validation.failed(**kwargs)
        return -1

    def d360Event_search(self, search_value, **kwargs):
        """
        This keyword inserts info into event search text box. No button for search is present, the search will be done
        automatically after the text was inserted
        :param search_value:
        :param **kwargs: pass in the events of type configuration which are in another tab
        :return: 1 if the text was entered into search box and -1 if search text box was not found
        """
        event_type = kwargs.get("event_type", "")
        if event_type == "config":
            self.utils.print_info("Clicking on 'Configurations Events' tab!")
            self.auto_actions.click(self.dev360.get_d360_config_events())
        search_box = self.dev360.get_d360Event_search_textbox()
        if search_box:
            self.utils.print_info("Entering info to search : ", search_value)
            self.auto_actions.send_keys(self.dev360.get_d360Event_search_textbox(), search_value)
            sleep(10)
            kwargs['pass_msg'] = "The text was entered into search box"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to find search text box"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_revert_port_configuration(self, select_column, port_name, **kwargs):
        """
        This keyword press the revert button for the specific row and column into device360 Port Configuration window
        select_column : - Port Details : 'port state' , 'port usage' , 'vlan' , 'description'
            Port Settings & Aggregation: 'transmission' , 'speed' , 'flow' , 'transmit' , 'receive' , 'cdp' , 'client reporting'
            STP: 'stp status' , 'edge port' , 'bpdu protection' , 'priority' , 'path cost'
            Storm Control: 'broadcast' , 'unknown unicast' , 'multicast' , 'value'
        port_name: Number of port . e.g 1/1 ; 2:1
        E.g. :
        device360_revert_port_configuration          flow        1:3

        return: 1 if successful revert; else -1
        """
        port_row = False
        rows = False
        # Port Details
        if select_column in ['port state', 'port usage', 'vlan', 'description']:
            button_settings = self.dev360.get_d360_configure_port_details_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Port Details' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_port_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        # Port Settings & Aggregation
        if select_column in ['transmission', 'speed', 'flow', 'transmit', 'receive', 'cdp', 'client reporting']:
            button_settings = self.dev360.get_d360_configure_port_settings_aggregation_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Port Settings & Aggregation' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_port_settings_aggregation_rows()
            else:
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        # STP
        if select_column in ['stp status', 'edge port', 'bpdu protection', 'priority', 'path cost']:
            button_settings = self.get_d360_configure_port_stp_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'STP' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_stp_rows()
            else:
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        # Storm Control
        if select_column in ['broadcast', 'unknown unicast', 'multicast', 'value']:
            button_settings = self.get_d360_configure_port_storm_control_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Storm Control' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_storm_control_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        if rows:
            port_row = self.device360_get_row_specified_port_name(rows, port_name)
        else:
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.failed(**kwargs)
            return -1
        if port_row:
            self.utils.print_info("Found row for port: ", port_row.text)
            port_override_revert = self.get_d360_configure_port_details_settings_aggregation_stp_storm_control_row_override_revert(
                select_column, port_row)
            if port_override_revert:
                self.utils.print_info("move on 'override' button ")
                self.auto_actions.move_to_element(port_override_revert)
                port_revert = self.dev360.get_d360_configure_port_row_revert_button(port_row)
                if port_revert:
                    self.utils.print_info("Clicking 'Revert' button")
                    self.auto_actions.click(port_revert)
                    sleep(10)
                    kwargs['pass_msg'] = "Clicked 'Revert' button"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.utils.print_info("Could not click Revert button")
                    self.screen.save_screen_shot()
                # Click the 'Save Port Configuration' button
                save_btn = self.get_device360_configure_port_save_button()
                self.utils.print_info("rularea a trecut pe aici ")  # sters
                if save_btn:
                    kwargs['pass_msg'] = "Clicked 'Save Port Configuration' button"
                    self.auto_actions.click(save_btn)
                    self.common_validation.passed(**kwargs)
                    return 1
            else:
                self.utils.print_info("The override revert button was not found  ")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not find the port row for port ", port_name)

        kwargs['fail_msg'] = f"Could not find the port row for {port_name}"
        self.common_validation.failed(**kwargs)
        return -1

    def device360_get_row_specified_port_name(self, rows, port_name):
        """
        - Get the port row object matching the specified port_name

        :param rows: list of rows
        :param port_name: name of the port to return the row for
        :return: row element if row exists else return None
        """
        ret_val = None
        self.utils.print_info("Getting the Port rows from the Device360 Settings and Aggregation page")
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
        else:
            for row in rows:
                if row.text.startswith(port_name):
                    ret_val = row
                    break
        return ret_val

    def device360_click_on_checkbox_or_button_port_configuration(self, select_column, port_name, **kwargs):
        """
        This keyword click on checkbox for the specific row and column into device360 Port Configuration window
        select_column : - Port Details : 'port state'
            Port Settings & Aggregation: 'transmit' , 'receive' , 'cdp' , 'client reporting'
            STP: 'stp status' , 'edge port'
            Storm Control: 'broadcast' , 'unknown unicast' , 'multicast'
        port_name: Number of port . e.g 1/1 ; 2:1
        E.g. :
        device360_revert_port_configuration          flow        1:3

        return: 1 if successful revert; else -1
        """
        port_row = False
        rows = False
        # Port Details
        if select_column in ['port state']:
            button_settings = self.dev360.get_d360_configure_port_details_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Port Details' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_port_rows()
            else:
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        # Port Settings & Aggregation
        if select_column in ['transmit', 'receive', 'cdp', 'client reporting']:
            button_settings = self.dev360.get_d360_configure_port_settings_aggregation_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Port Settings & Aggregation' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_port_settings_aggregation_rows()
            else:
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        # STP
        if select_column in ['stp status', 'edge port']:
            button_settings = self.get_d360_configure_port_stp_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'STP' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_stp_rows()
            else:
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        # Storm Control
        if select_column in ['broadcast', 'unknown unicast', 'multicast']:
            button_settings = self.get_d360_configure_port_storm_control_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Storm Control' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_storm_control_rows()
            else:
                kwargs['fail_msg'] = "Cannot click on tab button"
                self.common_validation.fault(**kwargs)
                return -1
        if rows:
            port_row = self.device360_get_row_specified_port_name(rows, port_name)
        else:
            self.utils.print_info("Port rows are not displayed. Check the tab")
            return -1
        if port_row:
            self.utils.print_info("Found row for port: ", port_row.text)
            click_checkbox_or_button = self.get_d360_configure_port_details_settings_aggregation_stp_storm_control_row_click_on_checkbox_or_button(
                select_column, port_row)
            if click_checkbox_or_button:
                self.utils.print_info("Clicking on button ")
                self.auto_actions.click(click_checkbox_or_button)
                sleep(30)
                save_btn = self.get_device360_configure_port_save_button()
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)
                    return 1
            else:
                self.utils.print_info("The button was not found  ")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not find the port row for port ", port_name)

        kwargs['fail_msg'] = f"Could not find the port row for {port_name}"
        self.common_validation.failed(**kwargs)
        return -1

    def device360_port_configuration_click_save_button(self, **kwargs):
        """
        - This keyword clicks on the SAVE PORT CONFIGURATION button
        - It is assumed that the Device360 window is open in Configure in Port Configuration section.
        - Keyword Usage
        - ``Device360 Port Configuration Click Save Button``
        :return: Click on SAVE PORT CONFIGURATION
        """
        ret_val = None
        save_btn = self.get_device360_configure_port_save_button()
        if save_btn:
            self.utils.print_info("Clicking 'Save Port Configuration' button'")
            self.auto_actions.click(save_btn)
            ret_val = 1
        else:
            self.utils.print_info("Could not click Save button")
            ret_val = -1

        if ret_val == -1:
            kwargs['fail_msg'] = "Client is not present in the historical grid"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Clicked on SAVE PORT CONFIGURATION"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_click_open_site_engine_link(self, iteration=12, sleep_time=10, **kwargs):
        """
        - This keyword clicks on the OPEN SITE ENGINE link
        - It is assumed that the Device360 window is open and the Overview panel is selected.
        - Keyword Usage
        - ``Device360 Click Open Site Engine Link``
        :return: 1 if action was successful (or the field is disabled), else -1
        """
        ret_val = -1

        for eachiteration in range(0, iteration):
            ose_link = self.get_device360_open_site_engine_link()
            if ose_link:
                hidden = ose_link.get_attribute("class")
                self.utils.print_info(f"Open Site Engine link Class value: {hidden}")
                if hidden == "mr50 fn-hidden":
                    self.utils.print_info("The 'Open Site Engine' link is hidden.")
                    self.screen.save_screen_shot()
                    ret_val = 1
                else:
                    self.utils.print_info("Clicking the 'Open Site Engine' link.")
                    self.auto_actions.move_to_element(ose_link)
                    self.screen.save_screen_shot()
                    self.auto_actions.click(ose_link)
                    ret_val = 1
                break;
            else:
                self.utils.print_info("Could not find the 'Open Site Engine' link.")
                sleep(sleep_time)
                self.device360_refresh_page()

        if ret_val == -1:
            kwargs['fail_msg'] = "Could not find the 'Open Site Engine' link"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "The action was successful"
            self.common_validation.passed(**kwargs)
        return ret_val

    def get_switch_device360_port_table_information(self, device_mac="", device_name="", port_number="", **kwargs):
        """
        - This keyword gets EXOS/VOSS Switch Port table information from device360 page
        - Flow : Manage --> Devices--> Select Device-->Device 360 Page
        - Keyword Usage
        - ``Get Switch Device360 Port Table Information  device_mac={DEVICE_MAC}  port_number={PORT_NUMBER} ``
        - ``Get Switch Device360 Port Table Information  device_name={DEVICE_NAME}  port_number={PORT_NUMBER} ``
         :param device_mac: Device Mac Address
         :param device_name: Device Name
         :param port_number: Port Number of the Switch

        :return: Dictionary of Port Table Information if port found else -1
        """

        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        if view_log := self.get_d360_switch_port_view_all_pages_button():
            if view_log.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.get_d360_switch_port_view_all_pages_button)
                self.screen.save_screen_shot()
                sleep(4)

        try:
            rows = self.get_d360_switch_ports_table_grid_rows()
            for row in rows:
                port_name_cell = self.get_d360_switch_ports_table_interface_port_name_cell(row).text
                if port_number == port_name_cell:
                    switch_device360_info = dict()
                    self.utils.print_info("Getting Port Table Information")
                    switch_device360_info["port_name"] = self.dev360.get_device360_switch_port_table_port_name(row).text
                    switch_device360_info["port_type"] = self.dev360.get_device360_switch_port_table_port_type(row).text
                    switch_device360_info["lldp_neighbor"] = self.dev360.get_device360_switch_port_table_lacp_neighbor(
                        row).text
                    switch_device360_info["lacp_status"] = self.dev360.get_device360_switch_port_table_lacp_status(
                        row).text
                    switch_device360_info["port_status"] = self.dev360.get_device360_switch_port_table_port_status(
                        row).text
                    switch_device360_info[
                        "transmission_mode"] = self.dev360.get_device360_switch_port_table_transmission_mode(row).text
                    switch_device360_info["port_mode"] = self.dev360.get_device360_switch_port_table_port_mode(row).text
                    switch_device360_info["access_vlan"] = self.dev360.get_device360_switch_port_table_access_vlan(
                        row).text
                    if self.dev360.get_device360_switch_port_table_tagged_vlans(row):
                        switch_device360_info[
                            "tagged_vlans"] = self.dev360.get_device360_switch_port_table_tagged_vlans(row).text
                    switch_device360_info[
                        "traffic_received"] = self.dev360.get_device360_switch_port_table_traffic_received(row).text
                    switch_device360_info[
                        "traffic_transmitted"] = self.dev360.get_device360_switch_port_table_traffic_transmitted(
                        row).text
                    switch_device360_info["power_used"] = self.dev360.get_device360_switch_port_table_power_used(
                        row).text
                    switch_device360_info["port_speed"] = self.dev360.get_device360_switch_port_table_port_speed(
                        row).text

                    self.utils.print_info("****************** Switch Port Table Information ************************")
                    for key, value in switch_device360_info.items():
                        self.utils.print_info(f"{key}:{value}")

                    self.screen.save_screen_shot()
                    self.auto_actions.click_reference(self.dev360.get_close_dialog)
                    self.screen.save_screen_shot()
                    return switch_device360_info
        except Exception:
            self.auto_actions.click_reference(self.dev360.get_close_dialog)
            kwargs['fail_msg'] = "Unable to get Port Table Information"
            self.common_validation.fault(**kwargs)
            return -1

    def check_up_or_down_ports(self, port_list, port_state='down'):
        """
        This keyword check the list of ports and returns only ports with "OPERATE" status that are up/down
        (if port_state = 'down' the function will return a list with ports that are 'up' and the other ports will be
        deleted and will be replaced with '')
        (if port_state = 'up' the function will return a list with ports that are 'down' and the other ports will be
        deleted and will be replaced with '')
        :param port_list: a list with status of ports (up/down)
        -Keyword Usage
            check_up_or_down_ports    ${OPERATE STATE}
        :param port_state: specify the element which will be deleted from list
        :return: port_list - a list with the ports that are up/down
                 -1 - no port is up/down
        """
        if not isinstance(port_list, str):
            cnt = 0
            for el in port_list:
                if port_state in el:
                    port_list[cnt] = ''
                cnt = cnt + 1
            for el in port_list:
                if not '' == el:
                    return port_list
            return -1
        else:
            self.utils.print_info("List has only one element")
            if port_state in port_list:
                port_list = ''
                return -1
        return -1

    def compare_transmission_mode(self, port_index, port_state, port_duplex_cli, **kwargs):
        """
        This keyword compares the status for transmission mode between XIQ and CLI
        :param port_index: a string of a port or a list of ports
        :param port_state: a string or a list which contains the status UP/DOWN of ports. If an element of list is '', it will be ignored
        :param port_duplex_cli: the "OPERATE DUPLEX" status from CLI
        -Keyword Usage:
            compare_transmission_mode     1/7  up  full
            compare_transmission_mode     2/4  up  full
            compare_transmission_mode     ${PORTS_INDEX}   ${OPERATE_STATE_UP}   ${OPERATE_DUPLEX}
        :return: 1 if the status of transmission in XIQ and CLI are the same
                -1 if the status of transmission in XIQ and CLI are different
        """

        if isinstance(port_index, list) and isinstance(port_state, list) and isinstance(port_duplex_cli, list):
            cnt = 0
            for el in port_state:
                if not '' == el and not '' == port_duplex_cli[cnt]:
                    self.utils.print_info("Port {} is {} ".format(port_index[cnt], el))
                    first = port_index[cnt]
                    if '1' == first[0] and '/' in first:
                        self.utils.print_info(
                            "Port {} is {} interface number on XIQ".format(port_index[cnt], first[2:]))
                        result_from_menu = self.transmission_mode_right_click_menu(first[2:])
                        if result_from_menu != -1:
                            self.utils.print_info(
                                "Interface transmission mode result from right click menu : {}".format(
                                    result_from_menu))
                        else:
                            self.utils.print_info("result was not found in right click menu")
                            sleep(5)
                        result_from_table = self.transmission_mode_overview_table(first)
                        if result_from_table != -1:
                            self.utils.print_info(
                                "Interface transmission mode result from table for port {} is  {}".format(first,
                                                                                                          result_from_table))
                        else:
                            self.utils.print_info("Result was not found in table ")
                        result_CLI = port_duplex_cli[cnt]
                        self.utils.print_info("Operate Duplex CLI: {}".format(result_CLI))
                        if result_from_menu == result_from_table and result_CLI.upper() in result_from_menu.upper():
                            self.utils.print_info("All transmission status are the same for port ", first)
                        else:
                            kwargs['fail_msg'] = f"Transmission status are not the same for port {first}"
                            self.common_validation.failed(**kwargs)
                            return -1
                        sleep(5)
                    else:
                        if self.transmission_mode_right_click_menu(first) != -1:
                            result_from_menu = self.transmission_mode_right_click_menu(first)
                            self.utils.print_info(
                                "Interface transmission mode result from right click menu for port {} is  : {}".format(
                                    first, result_from_menu))
                        else:
                            self.utils.print_info("result was not found in right click menu ")
                            sleep(5)
                            if self.transmission_mode_overview_table(first) != -1:
                                result_from_table = self.transmission_mode_overview_table(first)
                                self.utils.print_info(
                                    "Interface transmission mode result from table: {}".format(result_from_table))
                            else:
                                self.utils.print_info("result was not found in table ")
                            result_CLI = port_duplex_cli[cnt]
                            self.utils.print_info("Operate Duplex CLI: {}".format(result_CLI))
                            if result_from_menu == result_from_table and result_CLI.upper() in result_from_menu.upper():
                                self.utils.print_info("All transmission status are the same for port ", first)
                            else:
                                self.utils.print_info("Transmission status are not the same for port ", first)

                            kwargs['fail_msg'] = "Transmission status are not the " \
                                                 f"same for port {first} "
                            self.common_validation.failed(**kwargs)
                            return -1
                        sleep(5)
                cnt = cnt + 1
        elif isinstance(port_index, str) and isinstance(port_state, str) and isinstance(port_duplex_cli, str):
            if not '' == port_state:
                self.utils.print_debug("Port {} is {} ".format(port_index, port_state))
                if '1' == port_index[0] and '/' in port_index:
                    self.utils.print_info("Port {} is {} interface number on XIQ".format(port_index, port_index[2:]))
                    result_from_menu = self.transmission_mode_right_click_menu(port_index[2:])
                    if result_from_menu != -1:
                        self.utils.print_info(
                            "Interface transmission mode result from right click menu for port {} is  : {}".format(
                                port_index, result_from_menu))
                    else:
                        self.utils.print_info("result was not found in right click menu for port {}".format(port_index))
                    sleep(5)
                    result_from_table = self.transmission_mode_overview_table(port_index)
                    if result_from_table != -1:
                        self.utils.print_info(
                            "Interface transmission mode result from table for port {} is  {}".format(port_index,
                                                                                                      result_from_table))
                    else:
                        self.utils.print_info("result was not found in right click menu for port {}".format(port_index))
                    result_CLI = port_duplex_cli
                    self.utils.print_info("Operate Duplex CLI: {}".format(result_CLI))
                    if result_from_menu == result_from_table and result_CLI.upper() in result_from_menu.upper():
                        self.utils.print_info("All transmission status are the same for port ", port_index)
                    else:
                        self.utils.print_info("Transmission status are not the same for port ", port_index)
                        kwargs['fail_msg'] = "Transmission status are not the same " \
                                             f"for port {port_index} "
                        self.common_validation.failed(**kwargs)
                        return -1
                    sleep(5)
                else:
                    result_from_menu = self.transmission_mode_right_click_menu(port_index)
                    if result_from_menu != -1:
                        self.utils.print_info(
                            "Interface transmission mode result from right click menu for port {} is  : {}".format(
                                port_index, result_from_menu))
                    else:
                        self.utils.print_info("Result was not found in right click menu for port {}".format(port_index))
                    sleep(5)
                    result_from_table = self.transmission_mode_overview_table(port_index)
                    if result_from_table != -1:
                        self.utils.print_info(
                            "Interface transmission mode result from table for port {} is  {}".format(port_index,
                                                                                                      result_from_table))
                    else:
                        self.utils.print_info("result was not found in right click menu for port {}".format(port_index))
                        self.utils.print_info("Operate Duplex CLI: {}".format(port_duplex_cli))
                    if result_from_menu == result_from_table and port_duplex_cli.upper() in result_from_menu.upper():
                        self.utils.print_info("All transmission status are the same for port ", port_index)
                    else:
                        self.utils.print_info("Transmission status are not the same for port ", port_index)
                        kwargs['fail_msg'] = "Transmission status are not the same " \
                                             f"for port {port_index} "
                        self.common_validation.failed(**kwargs)
                        return -1
                    sleep(5)
        else:
            kwargs['fail_msg'] = "One of the objects is not of the specified type"
            self.common_validation.fault(**kwargs)
            return -1

        return 1

    def transmission_mode_right_click_menu(self, interface, **kwargs):
        """
        - This keyword checks the status of transmission mode for an interface by click on interface in Device360
        - Keyword Usage:
        -  transmission_mode_right_click_menu        20
        -  transmission_mode_right_click_menu        mgmt

        :param interface: a string with the number(index) of interface

        :return: a string with the status of transmission mode ("Full-Duplex/Half-Duplex")
                -1 the interface was not found
        """

        list_items = self.get_icon_ports_items()
        if list_items:
            pass
        else:
            kwargs['fail_msg'] = "List was not found"
            self.common_validation.fault(**kwargs)
            return -1
        for el in list_items:
            if interface == el.text.lower():
                self.utils.print_debug("Interface found: ", el.text)
                button = self.get_port_click(el)
                if button:
                    self.utils.print_info("Right click on interface")
                    self.auto_actions.click(button)
                    interface_transmission_mode = self.get_d360_interface_transmission_mode()
                    return interface_transmission_mode.text
                else:
                    self.utils.print_info("Interface not found")
            else:
                pass
        kwargs['fail_msg'] = "Interface not found"
        self.common_validation.failed(**kwargs)
        return -1

    def transmission_mode_overview_table(self, port_name, **kwargs):
        """
        This keyword checks the status of transmission mode for a port in Overview status
        :param port_name: a string with the specific port
        -Keyword Usage:
                transmission_mode_overview_table    1/1
        :return: a string with the status of transmission mode ("Full-Duplex/Half-Duplex")
                -1 if the status port was not found
        """
        port_row = None
        rows_items = self.get_d360_monitor_items_rows()
        if rows_items:
            for row in rows_items:
                interface_name = self.get_d360_monitor_interface_name(row)
                if interface_name:
                    self.utils.print_debug("Found interface name for port: ", interface_name.text)
                else:
                    kwargs['fail_msg'] = "Interface name for port is not displayed. Check the tab "
                    self.common_validation.fault(**kwargs)
                    return -1
                if port_name == interface_name.text.lower():
                    port_row = row
                    self.utils.print_info("Found port: ", interface_name.text)
                    self.utils.print_info("Found row for port: ", port_row.text)
                    break
                else:
                    pass
        else:
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.fault(**kwargs)
            return -1
        if port_row:
            transmission_mode_row = self.get_d360_monitor_transmission_mode(port_row)
        else:
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.fault(**kwargs)
            return -1
        if transmission_mode_row:
            return transmission_mode_row.text
        else:
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_d360_view_100_rows_on_page(self, **kwargs):
        """
        This keyword press view 100 rows into d360 page
        :return: 1 if button was selected; else -1
        """
        if self.get_d360_view_100_rows_on_page():
            self.utils.print_info("Select view 100 rows ")
            self.auto_actions.click_reference(self.get_d360_view_100_rows_on_page)
            self.auto_actions.scroll_up()
            kwargs['pass_msg'] = "Button was selected"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("view 100 rows button was not found ")

        kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
        self.common_validation.failed(**kwargs)
        return -1

    def check_two_lists(self, port_state, port_duplex_cli, **kwargs):
        """
        This keyword find out if two lists have at least one element different by '' at the same index into list
        :param port_state:
        :param port_duplex_cli:
        :return: 1 if two lists have at least one element different by '' at the same index into list ; else -1
        """
        cnt = 0
        for el in port_state:
            if not '' == el and not '' == port_duplex_cli[cnt]:
                kwargs['pass_msg'] = "At leas one port match"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                pass
            cnt = cnt + 1

        kwargs['fail_msg'] = "There is no match"
        self.common_validation.failed(**kwargs)
        return -1

    def exit_d360_Page(self, **kwargs):
        """
        This keyword close the d360 page
        :return: 1 all time
        """

        if self.dev360.get_device360_device_configuration_exit_button():
            self.utils.print_info("Click on exit button")
            self.auto_actions.click_reference(self.dev360.get_device360_device_configuration_exit_button)
        else:
            kwargs['fail_msg'] = "The exit button was not found"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Closed the d360 page"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_transmission_mode_overview(self, port_name, **kwargs):
        """
        This keyword checks the status of transmission mode for a port in Overview status
        :param port_name: a string with the specific port
        -Keyword Usage:
                device360_transmission_mode_overview    1/1
        :return: a string with the status of transmission mode ("Full-Duplex/Half-Duplex")
                -1 if the status port was not found
        """
        rows_items = self.get_d360_monitor_items_rows()
        if rows_items:
            port_row = self.device360_get_row_specified_port_name(rows_items, port_name)
            self.utils.print_info("Found row for port: ", port_row.text)
        else:
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.fault(**kwargs)
            return -1
        transmission_mode_row = self.get_d360_monitor_transmission_mode(port_row)
        if transmission_mode_row:
            return transmission_mode_row.text
        else:
            kwargs['fail_msg'] = "Transmission mode status not found"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_speed_overview(self, port_name, **kwargs):
        """
        This keyword checks the status of speed for a port in Overview status
        :param port_name: a string with the specific port
        -Keyword Usage:
                device360_speed_overview    1/1
        :return: a string with the status of speed
                -1 if the status port was not found
        """
        rows_items = self.get_d360_monitor_items_rows()
        self.utils.print_info(len(self.get_d360_monitor_items_rows()))
        if rows_items:
            port_row = self.device360_get_row_specified_port_name(rows_items, port_name)
            self.utils.print_info("Found row for port: ", port_row.text)
        else:
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.failed(**kwargs)
            return -1
        port_speed_row = self.get_d360_monitor_port_speed(port_row)
        if port_speed_row:
            self.utils.print_info("Port speed for port {} is {}".format(port_name, port_speed_row.text))
            return port_speed_row.text
        else:
            kwargs['fail_msg'] = "Port speed status not found"
            self.common_validation.failed(**kwargs)
            return -1

    def interface_transmission_mode(self, interface, **kwargs):
        """
        - This keyword checks the status of transmission mode for an interface by right click on interface in Device360
        - Keyword Usage:
        -  interface transmission mode        20
        -  interface transmission mode        mgmt

        :param interface: a string with the number(index) of interface
        :return: a string with the status of transmission mode ("Full-Duplex/Half-Duplex"), -1 the interface was not found
        """
        list_items = self.get_items()
        if list_items:
            pass
        else:
            self.utils.print_info("List was not found")
            kwargs['fail_msg'] = "List was not found"
            self.common_validation.fault(**kwargs)
            return -1
        for el in list_items:
            if interface == el.text.lower():
                self.utils.print_info("Interface found: ", el.text)
                buton = self.get_port_click(el)
                if buton:
                    self.utils.print_info("Click on interface")
                    self.auto_actions.right_click(buton)
                    interface_transmission_mode = self.get_d360_interface_transmission_mode()
                    return interface_transmission_mode.text
                else:
                    self.utils.print_info("Interface not found")
            else:
                pass
        kwargs['fail_msg'] = "Interface not found"
        self.common_validation.failed(**kwargs)
        return -1

    def interface_port_speed(self, port):
        """
        -This keyword checks the status of speed for an interface by right click on interface in Device360

        - Keyword Usage:
        -  interface_port_speed        20
        -  interface_port_speed        mgmt

        :param port: a string with the number(index) of interface
        :return: a string with the status of speed, -1 the interface was not found
        """
        list_items = self.get_items()
        self.utils.print_info(len(list_items))
        for el in list_items:
            if port == el.text:
                self.utils.print_info("Interface found: ", el.text)
                button = self.get_port_click(el)
                if button:
                    self.utils.print_info("Click on interface")
                    self.auto_actions.right_click(button)
                    interface_port_speed = self.get_d360_interface_port_speed()
                    self.utils.print_info("{}".format(interface_port_speed.text))
                    return 1
                else:
                    self.utils.print_info("Button not found")
            else:
                pass
        return 1

    def d360_check_if_vim_is_installed(self, **kwargs):
        """
        This function check if the Vim is installed
        :return: a string with VIM model or -1 if vim is not present
        """
        vim_model = self.get_d360_vim_model()
        if vim_model:
            kwargs['pass_msg'] = f"Vim is present: {vim_model.text}"
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "Vim is not present"
            self.common_validation.failed(**kwargs)
            return False

    def d360_return_vim_port_number(self, **kwargs):
        """
        This function return the first port of vim
        :return: the first port of vim ; else -1
        """
        vim_ports_list = self.get_d360_vim_ports()
        if vim_ports_list:
            self.utils.print_info("First port of vim is: ", vim_ports_list[0].text)
            return vim_ports_list[0].text
        else:
            self.utils.print_info("Vim is not present")

        kwargs['fail_msg'] = "Vim is not present"
        self.common_validation.failed(**kwargs)
        return -1

    def device360_left_click_on_port_icon(self, port):
        """
        - This keyword clicks on port icon in the Device360 view based on the specified port.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Click On Port Icon``
        :port: Specifies the port value
        :return: Displayed Port icon name in the Device360 view
        """
        device360_info = -1
        self.utils.print_info("Locating Device360 Port Icon")
        sleep(10)
        port_icon_list = self.dev360.get_device360_wireframe_port()
        self.utils.print_info("selecting ports to right click")
        # Commented on 1/18/23 because variable is unused
        # ret_val = self.auto_actions.click(port_icon_list[int(port) - 1])
        self.auto_actions.click(port_icon_list[int(port) - 1])
        self.utils.print_info("Clicking success")
        sleep(2)

        port_name_el = self.dev360.get_device360_port_leftclick_interface_name()
        port_mode_el = self.dev360.get_device360_port_leftclick_port_mode()
        port_access_vlan_el = self.dev360.get_device360_port_leftclick_access_vlan()
        port_tagged_vlan_el = self.dev360.get_device360_port_leftclick_tagged_vlan()
        port_status_el = self.dev360.get_device360_port_leftclick_port_status()

        device360_info = {}
        if port_name_el:
            device360_info["Interface_name"] = port_name_el.text
        else:
            self.utils.print_info("Could not determine value for Device Port name")
            device360_info["Interface_name"] = ""

        if port_mode_el:
            device360_info["port_mode"] = port_mode_el.text
        else:
            self.utils.print_info("Could not determine value for Device Port Mode")
            device360_info["port_mode"] = ""

        if port_access_vlan_el:
            device360_info["port_access_vlan"] = port_access_vlan_el.text
        else:
            self.utils.print_info("Could not determine value for Port Access Vlan")
            device360_info["port_access_vlan"] = ""

        if port_tagged_vlan_el:
            device360_info["port_tagged_vlan"] = port_tagged_vlan_el.text
        else:
            self.utils.print_info("Could not determine value for Port Tagged Vlan")
            device360_info["port_tagged_vlan"] = ""

        if port_status_el:
            device360_info["port_status"] = port_status_el.text
        else:
            self.utils.print_info("Could not determine value for Port Status")
            device360_info["port_status"] = ""

        return device360_info

    def device360_get_automation_port_info(self, port):
        self.utils.print_info("Locating Device360 Port Icon")
        sleep(10)
        port_icon_list = self.dev360.get_device360_automation_port()
        self.utils.print_info("selecting ports to right click")

        searched_port = "automation-port-" + port
        for port in port_icon_list:
            if port.get_attribute("data-automation-tag") == searched_port:
                self.auto_actions.click(port)
                self.utils.print_info("Clicking success")
                sleep(2)
                break

        port_name_el = self.dev360.get_device360_port_leftclick_interface_name()
        port_mode_el = self.dev360.get_device360_port_leftclick_port_mode()
        port_access_vlan_el = self.dev360.get_device360_port_leftclick_access_vlan()
        port_tagged_vlan_el = self.dev360.get_device360_port_leftclick_tagged_vlan()
        port_status_el = self.dev360.get_device360_port_leftclick_port_status()

        device360_info = {}
        if port_name_el:
            device360_info["Interface_name"] = port_name_el.text
        else:
            self.utils.print_info("Could not determine value for Device Port name")
            device360_info["Interface_name"] = ""

        if port_mode_el:
            device360_info["port_mode"] = port_mode_el.text
        else:
            self.utils.print_info("Could not determine value for Device Port Mode")
            device360_info["port_mode"] = ""

        if port_access_vlan_el:
            device360_info["port_access_vlan"] = port_access_vlan_el.text
        else:
            self.utils.print_info("Could not determine value for Port Access Vlan")
            device360_info["port_access_vlan"] = ""

        if port_tagged_vlan_el:
            device360_info["port_tagged_vlan"] = port_tagged_vlan_el.text
        else:
            self.utils.print_info("Could not determine value for Port Tagged Vlan")
            device360_info["port_tagged_vlan"] = ""

        if port_status_el:
            device360_info["port_status"] = port_status_el.text
        else:
            self.utils.print_info("Could not determine value for Port Status")
            device360_info["port_status"] = ""

        return device360_info

    def device360_device_configuration_auto_template(self, device_mac, name_stack_template, **kwargs):
        """
        This function will go to D360 and press create auto template and name the template
        :param device_mac: Mac of device
        :param name_stack_template: Policy template name
        :return: 1 if remain in the Create auto Template ; -1 else
        """
        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
            kwargs['fail_msg'] = "D360 page was not opened"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            self.utils.print_info("D360 page was opened ")

        if self.devices_web_elements.get_ap_configure_button():
            self.utils.print_info("Clicking on 'Configure' button  ")
            self.auto_actions.click_reference(self.devices_web_elements.get_ap_configure_button)
        else:
            kwargs['fail_msg'] = "'Configure' button was not found"
            self.common_validation.fault(**kwargs)
            return -1

        if self.dev360.get_device360_device_configuration_button():
            self.auto_actions.click_reference(self.dev360.get_device360_device_configuration_button)
            self.utils.print_info("Clicking on 'Device Configuration 'button")
        else:
            kwargs['fail_msg'] = "'Device Configuration' button was not found "
            self.common_validation.fault(**kwargs)
            return -1

        # Click on creating auto template on stacking
        if self.dev360.get_device360_create_auto_template_button():
            self.auto_actions.click_reference(self.dev360.get_device360_create_auto_template_button)
            self.utils.print_info("Clicking on 'Creating Auto template' button")
        else:
            kwargs['fail_msg'] = "'Creating Auto template' button was not found "
            self.common_validation.fault(**kwargs)
            return -1
        sleep(10)
        self.utils.print_info("Enter the switch Template Name: ", name_stack_template)
        self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                    name_stack_template)
        self.auto_actions.send_enter(self.sw_template_web_elements.get_sw_template_name_textfield())
        sleep(10)

        kwargs['pass_msg'] = "Successfully created auto template"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_configure_device_port_status(self, device_mac="", device_name="", port_number="", port_status="ON",
                                               **kwargs):
        """
        - This keyword will Enable/Disable Port Status in Device360 Page
        - Flow: Click Device -->Device 360 Window --> Configure --> Port Configuration--> Port State to OFF/ON
        - Keyword Usage:
        - ``Device360 Configure Device Port Status  device_mac=${MAC_ADDRESS}  port_number=${PORT_NUMBER}   port_status=${PORT_STATUS}``
        - ``Device360 Configure Device Port Status  device_NAME=${NAME}  port_number=${PORT_NUMBER}   port_status=${PORT_STATUS}``

         :param device_mac: Device Mac Address
         :param device_name: Device Name
         :param port_number: Port Number of the Switch
        :param  port_status:  Port Status either ON/OFF
        :return: 1 if port Status changed Successfully or already in expected port status, else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        sleep(2)

        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            port_row = self.device360_get_port_row(port_number)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)

                if port_status.upper() == "ON":
                    port_disabled = self.get_device360_configure_port_row_state_disabled(port_row)
                    if port_disabled:
                        self.auto_actions.click(port_disabled)
                        self.screen.save_screen_shot()
                    else:
                        self.utils.print_info(f"Port {port_number} Already Enabled")
                        self.utils.print_info("Close Dialogue Window")
                        self.auto_actions.click_reference(self.get_close_dialog)
                        kwargs['pass_msg'] = f"Port {port_number} Already Enabled"
                        self.common_validation.passed(**kwargs)
                        return 1

                if port_status.upper() == "OFF":
                    port_enabled = self.get_device360_configure_port_row_state_enabled(port_row)
                    if port_enabled:
                        self.auto_actions.click(port_enabled)
                        self.screen.save_screen_shot()
                    else:
                        self.utils.print_info(f"Port {port_number} Already Disabled")
                        self.utils.print_info("Close Dialogue Window")
                        self.auto_actions.click_reference(self.get_close_dialog)
                        kwargs['pass_msg'] = f"Port {port_number} Already Disabled"
                        self.common_validation.passed(**kwargs)
                        return 1

                save_btn = self.get_device360_configure_port_save_button()
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)

                    tool_tip_text = tool_tip.tool_tip_text
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        kwargs['pass_msg'] = "Interface settings were updated successfully."
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"{tool_tip_text}"
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                self.utils.print_info("Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Port Row Not Found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page "
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_port_access_vlan(self, device_mac="", device_name="", port_number="", access_vlan_id="",
                                             port_type="Access Port", **kwargs):
        """
        - This keyword will Configure Device switch Port Access Vlan in Device360 Page.
        - Flow: Click Device -->Device 360 Window --> Configure --> Port Configuration--> interface --> Port Usage and Vlan
        - Keyword Usage:
        - ``Device360 Configure Port Access Vlan  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}``
        - ``Device360 Configure Port Access Vlan  device_name=${DEVICE_NAME}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}``

         :param device_mac: Device Mac Address
         :param device_name: Device Name
         :param port_number: Port Number of the Switch
         :param access_vlan_id: Access Vlan Number for switch port
        :param  port_type:  Access Port
        :return: 1 if Port Usage Access and Vlan Successfully configured else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        sleep(2)

        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            port_row = self.device360_get_port_row(port_number)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)
                self.utils.print_info("click Port Usage drop down")
                self.auto_actions.click(self.get_device360_configure_port_usage_drop_down_button(port_row))
                sleep(2)

                self.utils.print_info("Selecting Port Usage")
                self.auto_actions.select_drop_down_options(
                    self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                sleep(2)

                self.utils.print_info("Entering Search String...")
                self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                            Keys.CONTROL + "a")
                self.utils.print_info("Deleting the selected values in port..")
                self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                            Keys.BACK_SPACE)
                self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                            access_vlan_id)
                self.screen.save_screen_shot()
                sleep(2)

                save_btn = self.get_device360_configure_port_save_button()
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)

                    tool_tip_text = tool_tip.tool_tip_text
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        kwargs['pass_msg'] = "Interface settings were updated successfully."
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"{tool_tip_text}"
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                self.utils.print_info("Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Port Row Not Found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_port_trunk_vlan(self, device_mac="", device_name="", port_number="", trunk_native_vlan="",
                                            trunk_vlan_id="", port_type="Trunk Port", **kwargs):
        """
        - This keyword will Configure Device switch Port Trunk Vlan in Device360 Page.
        - Flow: Click Device -->Device 360 Window --> Configure --> Port Configuration--> interface --> Port Usage and Vlan
        - Keyword Usage:
        - ``Device360 Configure Port Trunk Vlan  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}``
        - ``Device360 Configure Port Trunk Vlan  device_name=${NAME}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}``

         :param device_mac: Device Mac Address
         :param device_name: Device Name
         :param port_number: Port Number of the Switch
         :param trunk_native_vlan: Trunk Native Vlan Number for switch port
         :param trunk_vlan_id: Trunk Vlan Number for switch port
        :param  port_type:  Trunk Port
        :return: 1 if Port Usage Trunk and Vlan Successfully configured else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        sleep(2)

        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            port_row = self.device360_get_port_row(port_number)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)
                self.utils.print_info("click Port Usage drop down")
                self.auto_actions.click(self.get_device360_configure_port_usage_drop_down_button(port_row))
                sleep(2)

                self.utils.print_info("Selecting Port Usage")
                self.auto_actions.select_drop_down_options(
                    self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                sleep(2)

                self.utils.print_info("Entering Trunk Native Vlan TextField...")
                self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                                            Keys.CONTROL + "a")
                sleep(2)
                self.utils.print_info("Deleting the selected values in port..")
                self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                                            Keys.BACK_SPACE)
                sleep(2)
                self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                                            trunk_native_vlan)
                self.screen.save_screen_shot()
                sleep(4)

                self.utils.print_info("Entering Trunk Allowed Vlan IDs TextField...")
                sleep(2)
                element = self.get_device360_configure_port_trunk_vlan_textfield(port_row)
                self.utils.print_info("Deleting the selected values in Vlan ID textfield..")
                self.auto_actions.send_keys(element, Keys.CONTROL + "a")
                self.auto_actions.send_keys(element, Keys.BACK_SPACE)
                element.send_keys(trunk_vlan_id)
                self.screen.save_screen_shot()
                sleep(2)

                self.select_configure_tab()
                sleep(5)
                save_btn = self.get_device360_configure_port_save_button()
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)

                    tool_tip_text = tool_tip.tool_tip_text
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        kwargs['pass_msg'] = "Interface settings were updated successfully."
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"{tool_tip_text}"
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                self.utils.print_info("Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Port Row Not Found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_port_transmission_mode_and_speed(self, device_mac="", device_name="", port_number="",
                                                             transmission_mode="", speed="", **kwargs):
        """
        - This keyword will Configure Device switch Port transmission_mode and speed in Device360 Page.
        - Flow: Click Device -->Device 360 Window --> Configure --> Port Configuration-->
                Port settings --> Interface --> Transmission Mode and Speed
        - Keyword Usage:
        - `` device360 configure port transmission mode and speed  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}
         transmission_mode=${MODE}  speed=${SPEED}``
        - `` device360 configure port transmission mode and speed  device_name=${DEVICE_NAME}  port_number=${PORT_NUMBER}
         transmission_mode=${MODE}  speed=${SPEED}``

         :param device_mac: Device Mac Address
         :param device_name: Device Name
         :param port_number: Port Number of the Switch
         :param transmission_mode: switch port Transmission Mode
        :param  speed:  switch port Speed
        :return: 1 if Port Transmission Mode and speed Successfully configured else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        sleep(2)

        self.utils.print_info("Click Port Settings Tab")
        self.auto_actions.click_reference(self.get_device360_port_configuration_port_settings_tab)
        sleep(2)

        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            port_row = self.device360_get_port_row(port_number)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)
                self.utils.print_info("clicking Transmission Mode drop down Button")
                self.auto_actions.click(self.get_device360_port_settings_transmission_mode_drop_down_button(port_row))
                sleep(2)

                self.utils.print_info(f"Selecting Transmission Mode Option : {transmission_mode}")
                self.auto_actions.select_drop_down_options(
                    self.get_device360_port_settings_transmission_mode_drop_down_options(port_row), transmission_mode)
                sleep(2)

                self.utils.print_info("clicking Speed drop down Button")
                self.auto_actions.click(self.get_device360_port_settings_speed_drop_down_button(port_row))
                sleep(2)

                self.utils.print_info(f"Selecting Speed Option : {speed}")
                self.auto_actions.select_drop_down_options(
                    self.get_device360_port_settings_speed_drop_down_options(port_row), speed)
                sleep(2)

                save_btn = self.get_device360_configure_port_save_button()
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)

                    tool_tip_text = tool_tip.tool_tip_text
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        kwargs['pass_msg'] = "Interface settings were updated successfully."
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"{tool_tip_text}"
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                self.utils.print_info("Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Port Row Not Found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page "
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_device_port_poe_status_and_profile(self, device_mac="", device_name="", port_number="",
                                                               poe_profile="", poe_status="ON", **kwargs):
        """
        - This keyword will Enable/Disable Port POE Status and POE Profile in Device360 Page
        - Flow: Click Device -->Device 360 Window --> Configure --> Port Configuration--> PSE--> POE Status and Profile
        - Keyword Usage:
        - ``Device360 Configure Device Port POE Status And Profile  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}   poe_profile=${POE_PROFILE}    poe_status=${POE_STATUS}``
        - ``Device360 Configure Device Port POE Status And Profile  device_NAME=${DEVICE_NAME}  port_number=${PORT_NUMBER}   poe_profile=${POE_PROFILE}    poe_status=${POE_STATUS}``

         :param device_mac: Device Mac Address
         :param device_name: Device Name
         :param port_number: Port Number of the Switch
        :param  poe_profile:  POE Profile Name for Switch Port
        :param  poe_status:  POE Status(ON/OFF) for Switch Port
        :return: 1 if port POE Status and Profile changed Successfully else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        sleep(2)

        self.utils.print_info("Click PSE Tab")
        self.auto_actions.click_reference(self.get_device360_port_configuration_pse_tab)
        sleep(2)

        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            port_row = self.device360_get_port_row(port_number)
            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)
                if poe_profile:
                    self.utils.print_info("clicking POE Profile Select Button")
                    self.auto_actions.click(self.get_device360_port_configuration_pse_profile_select_button(port_row))
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info(f"Selecting POE Profile Option : {poe_profile}")
                    self.auto_actions.select_drop_down_options(
                        self.get_device360_port_configuration_pse_profile_select_options(), poe_profile)
                    self.screen.save_screen_shot()
                    sleep(2)

                if poe_status.upper() == "ON":
                    port_disabled = self.get_device360_configure_port_pse_poe_state_disabled(port_row)
                    if port_disabled:
                        self.auto_actions.click(port_disabled)
                        self.screen.save_screen_shot()
                    else:
                        self.utils.print_info(f"POE on Port {port_number} Already Enabled")
                        self.screen.save_screen_shot()

                if poe_status.upper() == "OFF":
                    port_enabled = self.get_device360_configure_port_pse_poe_state_enabled(port_row)
                    if port_enabled:
                        self.auto_actions.click(port_enabled)
                        self.screen.save_screen_shot()
                    else:
                        self.utils.print_info(f"POE on Port {port_number} Already Disabled")
                        self.screen.save_screen_shot()

                save_btn = self.get_device360_configure_port_save_button()
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)

                    tool_tip_text = tool_tip.tool_tip_text
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        kwargs['pass_msg'] = "Interface settings were updated successfully."
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        kwargs['fail_msg'] = f"{tool_tip_text}"
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                self.utils.print_info("Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Port Row Not Found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_get_voss_wireframe_cpu_utilization(self, device_mac="", device_name="", **kwargs):
        """
        - This keyword will get Wireframe CPU Utilization for VOSS Device in Device360 Page
        - Flow: Click Device -->Device 360 Window -->CPU Usage ICON
        - Keyword Usage:
        - ``Device360 Get VOSS Wireframe CPU Utilization  device_mac=${DEVICE_MAC}``
        - ``Device360 Get VOSS Wireframe CPU Utilization  device_name=${DEVICE_NAME}``

        :param device_mac:  Device Mac Address
        :param device_name:  Device Name
        :return: For success return CPU Usage Percentage Value else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(10)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(10)

        cpu_el = self.get_device360_wireframe_cpu_utilization_piechart()
        mem_el = self.dev360.get_topbar_memory()
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
        if cpu_el:
            self.auto_actions.move_to_element(cpu_el)
            sleep(10)
            self.auto_actions.move_to_element(cpu_el)
            self.screen.save_screen_shot()
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                cpu_utilization_tooltip = tt_content.text
                self.utils.print_debug(f"Tooltip content for CPU Utilization is : {cpu_utilization_tooltip}")
                cpu_utilization = cpu_utilization_tooltip.split(":")
                cpu_utilization_percentage = cpu_utilization[1].strip()
                self.utils.print_info(f"WireFrame CPU Utilization Percentage is : {cpu_utilization_percentage}")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                self.screen.save_screen_shot()
                return cpu_utilization[1].strip()
            else:
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Tooltip content Not Found for WireFrame CPU Utilization"
                self.common_validation.fault(**kwargs)
                return -1

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        kwargs['fail_msg'] = "One or more elements are missing"
        self.common_validation.fault(**kwargs)
        return -1

    def device360_get_voss_wireframe_memory_utilization(self, device_mac="", device_name="", **kwargs):
        """
        - This keyword will get Wireframe Memory Utilization for VOSS Device in Device360 Page
        - Flow: Click Device -->Device 360 Window -->Memory Usage ICON
        - Keyword Usage:
        - ``Device360 Get VOSS Wireframe Memory Utilization  device_mac=${DEVICE_MAC}``
        - ``Device360 Get VOSS Wireframe Memory Utilization  device_name=${DEVICE_NAME}``

        :param device_mac:  Device Mac Address
        :param device_name:  Device Name
        :return: For success return Memory Usage Percentage Value else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(10)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(10)

        cpu_el = self.get_device360_wireframe_cpu_utilization_piechart()
        mem_el = self.dev360.get_topbar_memory()
        if cpu_el:
            self.auto_actions.move_to_element(cpu_el)
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
            sleep(10)
            self.auto_actions.move_to_element(mem_el)
            self.screen.save_screen_shot()
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                memory_usage_tooltip = tt_content.text
                self.utils.print_debug(f"Tooltip content for Memory Usage is : {memory_usage_tooltip}")
                memory_usage = memory_usage_tooltip.split(":")
                memory_usage_percentage = memory_usage[1].strip()
                self.utils.print_info(f"WireFrame Memory Usage Percentage is : {memory_usage_percentage}")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                self.screen.save_screen_shot()
                return memory_usage[1].strip()
            else:
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['fail_msg'] = "Tooltip content Not Found for WireFrame Memory Utilization "
                self.common_validation.failed(**kwargs)
                return -1

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        kwargs['fail_msg'] = "One or more elements are missing"
        self.common_validation.fault(**kwargs)
        return -1

    def test_device_cli(self, command, device_serial=None, device_mac=None, max_time=180, interval_time=20, delay=30,
                        **kwargs):
        """
        This function is used for testing WEB CLI from extauto.xiq. A command or a list of commands can be send from XIQ to exos
        device

        test device cli  ${SW2_SERIAL}  ping 127.0.0.1,show iq,show vlan
        test device cli  ${SW2_SERIAL}  ping 127.0.0.1

        :param device_serial: Serial for exos device
        :param command: a CLI command or a list of commands i.g.
        :param max_time: The max period time of waiting to appear the output of command
        :param interval_time: Time interval between two consecutive output checks
        :param delay: Delay after send the command
        :return: output of command ; else -1
        """
        self.utils.print_info("Starting web Cli for command: ", command)
        command_list = command.split(",")
        # rows = self.dev360.get_device_rows()
        # self.utils.print_info("Printing all Device Rows: ",rows)
        flag_device_selected = False
        if device_mac:
            self.utils.print_info("Deleting device: ", device_mac)
            search_result = self.dev.search_device(device_mac=device_mac, ignore_failure=True)

            if search_result != -1:
                if self.dev.select_device(device_mac=device_mac, ignore_failure=True) == 1:
                    sleep(2)
                    self.utils.print_info("Selected the device with MAC ", device_mac)
                    flag_device_selected = True

        elif device_serial:
            self.utils.print_info("Finding device with serial ", device_mac)
            search_result = self.dev.search_device(device_serial=device_serial, ignore_failure=True)

            if search_result != -1:
                if self.dev.select_device(device_serial=device_serial, ignore_failure=True) == 1:
                    sleep(2)
                    self.utils.print_info("Selected the device with serial ", device_serial)
                    flag_device_selected = True

        else:
            self.screen.save_screen_shot()
            self.utils.print_info("Rows not found")

        if not flag_device_selected:
            self.screen.save_screen_shot()
            self.utils.print_info("Device not found")
        else:
            self.utils.print_debug("Device was found")
        sleep(3)

        actions = self.dev360.get_actions_button()
        if actions:
            self.utils.print_info("Clicking on Actions button")
            self.auto_actions.click(actions)
        else:
            kwargs['fail_msg'] = "Actions button not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(3)

        advanced = self.dev360.get_advanced_button()
        for el in advanced:
            if 'Advanced' == el.text:
                if el:
                    self.utils.print_info("Hovering on Advanced")
                    self.auto_actions.move_to_element(el)
                else:
                    kwargs['fail_msg'] = "Advanced button not found"
                    self.common_validation.fault(**kwargs)
                    return -1
                break
            else:
                pass
        sleep(3)

        cli = self.dev360.get_cli_button()
        if cli:
            self.utils.print_info("Clicking on Device CLI")
            self.auto_actions.click(cli)
        else:
            kwargs['fail_msg'] = "Device CLI button not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(5)

        output_before = ''
        if len(command_list) > 1:
            for el in command_list:
                search = self.dev360.get_cli_command_line()
                if search:
                    self.utils.print_info("Send command:", el)
                    self.auto_actions.send_keys(search, el)
                    sleep(2)
                    self.auto_actions.click_reference(self.dev360.get_cli_apply)
                    sleep(delay)
                else:
                    kwargs['fail_msg'] = "'Send command' field not found"
                    self.common_validation.fault(**kwargs)
                    return -1
                cnt = 0
                while cnt < int(max_time):
                    result = self.dev360.get_result_area()
                    if result:
                        if result.text != '':
                            output_after = result.text
                            if output_before != output_after:
                                output_before = output_after
                                self.utils.print_info("The output after command {} is : {}".format(el, output_before))
                                break
                    else:
                        self.utils.print_info("The command gave no output. Trying again...")
                    sleep(interval_time)
                    cnt = cnt + interval_time
                    self.utils.print_info("Waited {} sec".format(cnt))
            self.utils.print_info("The output for the all command is: ", output_before)
            self.screen.save_screen_shot()
            sleep(2)
            x_button = self.dev360.get_cli_close_button()
            if x_button:
                self.utils.print_info("close button")
                self.auto_actions.click(x_button)
            else:
                self.utils.print_info("close button not found")
            self.screen.save_screen_shot()
            if output_before == '':
                kwargs['fail_msg'] = "Can not get the output of the command"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                return output_before
        else:
            search = self.dev360.get_cli_command_line()
            if search:
                self.utils.print_info("Send command:", command)
                self.auto_actions.send_keys(search, command)
                sleep(2)
                self.auto_actions.click_reference(self.dev360.get_cli_apply)
                sleep(delay)
            else:
                kwargs['fail_msg'] = "Web CLI input field not found"
                self.common_validation.fault(**kwargs)
                return -1
            cnt = 0
            while cnt < int(max_time):
                result = self.dev360.get_result_area()
                if result:
                    output = result.text
                    if output != '':
                        self.utils.print_info("The output for the command is: ", output)
                        self.screen.save_screen_shot()
                        sleep(2)
                        x_button = self.dev360.get_cli_close_button()
                        if x_button:
                            self.utils.print_info("close button was found ")
                            self.auto_actions.click(x_button)
                        else:
                            kwargs['fail_msg'] = "close button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                        return output
                    else:
                        pass
                else:
                    self.utils.print_info("The command gave no output. Trying again...")
                sleep(interval_time)
                cnt = cnt + interval_time
                self.utils.print_info("Waited {} sec".format(cnt))
        x_button = self.dev360.get_cli_close_button()
        if x_button:
            self.utils.print_info("close button was found ")
            self.auto_actions.click(x_button)
        else:
            self.utils.print_info("close button not found")

        kwargs['fail_msg'] = "close button not found"
        self.common_validation.fault(**kwargs)
        return -1

    def get_supplemental_cli(self, name_s_cli, cli_commands="", **kwargs):
        """
        This keyword will add or edit a supplemental cli profile with cli commands in D360
        - Keyword Usage
        - ``Get supplemental cli       ${NAME_CLI}     ${CLI_COMMANDS}``
        :param name_s_cli: Name of the supplemental cli profile
        :param cli_commands: list of CLI commands separated by comma
        :return: 1 if supplemental cli profile save successfully else -1
        """
        self.auto_actions.click_reference(self.get_device360_configure_button)
        self.auto_actions.click_reference(self.get_device360_device_configuration_button)
        self.auto_actions.click_reference(self.get_device360_select_supplemental_cli)
        sleep(3)
        list_items = self.get_device360_supplemental_cli_list()
        found_profile = False
        if list_items:
            for profile in list_items:
                if name_s_cli == profile.text:
                    self.utils.print_info("{} found in S-CLI list".format(profile.text))
                    self.utils.print_info("Selecting '{}' profile in S-CLI list".format(profile.text))
                    self.auto_actions.click(profile)
                    if name_s_cli == "No Supplemental CLI":
                        self.utils.print_info("Saving Configuration")
                        self.auto_actions.click_reference(self.get_device360_device_configuration_save_button)
                        sleep(3)
                        found_profile = True
                        self.utils.print_info("Exit device configuration")
                        if self.get_device360_device_configuration_exit_button():
                            self.auto_actions.click_reference(self.get_device360_device_configuration_exit_button)
                            kwargs['pass_msg'] = "cli profile saved successfully"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['fail_msg'] = "Exit D360 button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("Edit profile")
                        self.auto_actions.click_reference(self.get_device360_supplemental_cli_edit_profile)
                        profile_commands_cli = self.get_device_360_supplemental_cli_profile_commands()
                        cli_command_list = cli_commands.split(",")
                        new_line_cli_commands = "\n".join(cli_command_list)
                        sleep(3)
                        self.auto_actions.send_keys(profile_commands_cli, new_line_cli_commands)
                        sleep(3)
                        self.utils.print_info("Saving Profile")
                        self.auto_actions.click_reference(self.get_device360_supplemental_cli_save_profile)
                        sleep(3)
                        self.utils.print_info("Saving Configuration")
                        self.auto_actions.click_reference(self.get_device360_device_configuration_save_button)
                        sleep(3)
                        found_profile = True
                        self.utils.print_info("Exit device configuration")
                        if self.get_device360_device_configuration_exit_button():
                            self.auto_actions.click_reference(self.get_device360_device_configuration_exit_button)
                            kwargs['pass_msg'] = "cli profile saved successfully"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['fail_msg'] = "Exit D360 button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
            if found_profile == False:
                self.utils.print_info("'{}' profile was not found".format(name_s_cli))
                self.utils.print_info("Creating one")
                self.auto_actions.click_reference(self.get_device_360_supplemental_cli_new_profile)

                input_element, _ = self.utils.wait_till(
                    func=self.get_device_360_supplemental_cli_profile_name,
                     delay=5, exp_func_resp=True, silent_failure=True
                )

                if not input_element:
                    kwargs["fail_msg"] = "Failed to get the input element"
                    self.common_validation.fault(**kwargs)
                    return -1

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.send_keys(input_element, name_s_cli),
                    exp_func_resp=True, silent_failure=True, delay=5
                )

                if res != 1:
                    kwargs["fail_msg"] = "Failed to sent the keys to the input element"
                    self.common_validation.fault(**kwargs)
                    return -1

                sleep(3)
                profile_commands_cli = self.get_device_360_supplemental_cli_profile_commands()
                cli_command_list = cli_commands.split(",")
                new_line_cli_commands = "\n".join(cli_command_list)
                sleep(3)
                self.auto_actions.send_keys(profile_commands_cli, new_line_cli_commands)
                sleep(3)
                self.utils.print_info("Saving Profile")
                self.auto_actions.click_reference(self.get_device360_supplemental_cli_save_profile)
                sleep(3)
                self.utils.print_info("Saving Configuration")
                self.auto_actions.click_reference(self.get_device360_device_configuration_save_button)
                sleep(3)
                self.utils.print_info("Exit device configuration")
                if self.get_device360_device_configuration_exit_button():
                    self.auto_actions.click_reference(self.get_device360_device_configuration_exit_button)
                    kwargs['pass_msg'] = "cli profile saved successfully"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.utils.print_info("Exit D360 button not found")
                sleep(3)
        else:
            kwargs['fail_msg'] = "List was not found"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "cli profile saved successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_power_details(self, device_mac="", device_name="", **kwargs):
        """
        - This keyword will get Power Supply Details in Device 360 from thunderbolt icon
        - Flow: Click Device -->Device 360 Window -->Thunderbolt ICON
        - Keyword Usage:
        - ``Device360 Power Details      device_mac=${DEVICE_MAC}``
        - ``Device360 Power Details      device_name=${DEVICE_NAME}``
        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :return: list with power supply details
        """
        def _power_detail():
            power_el = self.dev360.get_device360_thunderbold_icon()
            if power_el:
                self.utils.print_info("Power Details")
                self.auto_actions.click_and_hold_element(power_el)
                self.auto_actions.move_to_element(power_el)
                self.screen.save_screen_shot()
            else:
                self.utils.print_info("Power details not found")
                self.screen.save_screen_shot()
                return False

            self.utils.wait_till(self.dev360.get_device360_power_details, timeout=5, is_logging_enabled=True, delay=1)
            power_details = self.dev360.get_device360_power_details()
            if power_details:
                self.utils.print_info("Power details from XIQ are : ", power_details.text)
                self.utils.print_info("Close Dialogue Window")
                self.screen.save_screen_shot()
                details = power_details.text
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.common_validation.passed(**kwargs)
                return details
            else:
                self.utils.print_info("Power details not found")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                kwargs['fail_msg'] = "Power details not found"
                self.common_validation.fault(**kwargs)
                return False

        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.wait_till(self.dev360.get_device360_thunderbold_icon, timeout=20, is_logging_enabled=True, delay=1)
        res = self.utils.wait_till(_power_detail, timeout=20, is_logging_enabled=True, delay=1)[0]
        self.common_validation.passed(**kwargs)

        return str(res)

    def unlock_device360_port_config(self, raise_error_if_button_not_found=False, **kwargs):
        """
        Method that unlocks the port configuration menu in Device360.
        
        kwargs:
            :raise_error_if_button_not_found: specifies if an error should be raised if the button is not found
                                              it is disabled by default so the keyword is backwards compatible   
        """
        unlock_button, _ = self.utils.wait_till(
            func=self.get_device360_unlock_port_config_button,
            exp_func_resp=True,
            silent_failure=True, 
            delay=3
        )
        
        if not unlock_button:
            if raise_error_if_button_not_found:
                kwargs["fail_msg"] = "Failed to get the device360_unlock_port_config_button element"
                self.common_validation.failed(**kwargs)
                return -1
   
        if unlock_button:
            
            if not unlock_button.is_displayed():
                kwargs["pass_msg"] = "The device360 unlock button is already pressed"
                self.common_validation.passed(**kwargs)
                return 1

            if self.auto_actions.click_reference(lambda: unlock_button) != 1:
                kwargs["fail_msg"] = "Failed to click the device360_unlock_port_config_button element"
                self.common_validation.failed(**kwargs)
                return -1
            
            confirmation_button, _ = self.utils.wait_till(
                func=self.get_device360_unlock_port_config_confirmation_button,
                exp_func_resp=True,
                silent_failure=True, 
                delay=3
            )
        
            if not confirmation_button:
                kwargs["fail_msg"] = "Failed to get the device360_unlock_port_config_confirmation_button element"
                self.common_validation.failed(**kwargs)
                return -1

            if self.auto_actions.click_reference(lambda: confirmation_button) != 1:
                kwargs["fail_msg"] = "Failed to click the device360_unlock_port_config_confirmation_button element"
                self.common_validation.failed(**kwargs)
                return -1

            kwargs["pass_msg"] = "Successfully clicked device360 unlock button"
            self.common_validation.passed(**kwargs)
            return 1
        
    def device360_configure_poe_threshold_value(self, threshold_value, device_mac="", device_name="", **kwargs):
        """
        - This keyword will configure the POE threshold value in Device 360
        - Flow: Click Device --> Device 360 Window --> Port Configuration --> PSE --> PSE SETTINGS FOR DEVICE
        - Keyword Usage:
        - ``Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}   device_mac=${DEVICE_MAC}``
        - ``Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}   device_name=${DEVICE_NAME}``
        :param threshold_value: value for threshold between 1 and 99
        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :return: 1 if value was configured successfully , else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
        sleep(5)
        self.select_configure_tab()
        self.select_port_configuration_view()
        sleep(2)

        self.unlock_device360_port_config()
        
        sleep(5)
        self.utils.print_info("Click PSE Tab")
        self.auto_actions.click_reference(self.get_device360_port_configuration_pse_tab)
        sleep(2)
        pse_settings_for_device_button = self.get_device360_pse_settings_for_device_button()
        if pse_settings_for_device_button:
            self.utils.print_info("Click on PSE settings for device")
            self.auto_actions.click(pse_settings_for_device_button)
        else:
            kwargs['fail_msg'] = "PSE settings for device button not found"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
            
        edit_threshold_poe = self.get_device360_edit_threshold_poe()
        self.utils.print_info("Editing threshold value")
        self.auto_actions.send_keys(edit_threshold_poe, Keys.CONTROL + "a" + Keys.BACK_SPACE)
        sleep(2)
        threshold_value_int = int(threshold_value)
        if 1 <= threshold_value_int <= 99:
            self.utils.print_info("Sending threshold {} % value".format(threshold_value))
            self.auto_actions.send_keys(edit_threshold_poe, threshold_value)
            self.screen.save_screen_shot()
            sleep(5)
        else:
            kwargs['fail_msg'] = "Value needs to be between 1 and 99."
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        save_threshold_poe = self.get_device360_save_threshold_poe_value()
        if save_threshold_poe:
            self.utils.print_info("Saving threshold {} % ".format(threshold_value))
            self.auto_actions.click(save_threshold_poe)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Save button not found"
            self.common_validation.fault(**kwargs)
            return -1
        save_btn = self.get_device360_configure_port_save_button()
        if save_btn:
            self.utils.print_info("Clicking 'Save Port Configuration' button'")
            self.auto_actions.click(save_btn)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Could not click Save button"
            self.common_validation.fault(**kwargs)
            return -1
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        kwargs['pass_msg'] = "POE threshold value was configured successfully "
        self.common_validation.passed(**kwargs)
        return 1

    def device360_check_wired_client(self, device_serial=None, device_mac=None, client_mac=None, sleep_time=30,
                                     iteration=15, **kwargs):
        """
        - This keyword is used to check the client exist in device360 page based on passed client mac address
        - Flow: Manage --> Devices --> check on the Clients which is present in Device grid row based on Client MAC
        - Keyword Usage:

        :param device_serial: Serial Number of the Device
        :param device_mac: Mac address of the Device
        :param client_mac: Client MAC address
        :param sleep_time: The time period between each iteration
        :param iteration: The number of iteration
        :return: -1 if there are any failure or client details in dict format
        Client details: client mac,ipv4,ipv6,port speed,negotiated speed,vlan, port mode,

        """
        client_found = -1

        for eachiteration in range(0, iteration):
            if device_mac:
                self.utils.print_info("Using device MAC: ", device_mac)
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

            if device_serial:
                self.utils.print_info("Using device name: ", device_serial)
                self.navigator.navigate_to_device360_page_with_host_name(device_serial)

            self.device360_navigate_to_monitor_clients()
            sleep(4)
            self.utils.print_info("Searching Device Entry with Search String : ", client_mac)
            self.auto_actions.send_keys(self.deviceConfig.get_unique_clients_search_field(), client_mac)
            self.screen.save_screen_shot()
            sleep(5)
            table = self.dev360.get_device_active_clients_grid()
            rows = self.dev360.get_device_active_clients_grid_rows(table)
            self.screen.save_screen_shot()
            sleep(5)
            if rows:
                for row in rows:
                    self.utils.print_info("Getting the clients rows: ", row.text)
                    get_client_mac = None
                    try:
                        get_client_mac = self.get_device360_hyperlink_client().text
                    except Exception:
                        print("Problem while getting client mac")
                    if client_mac in row.text and "CONNECTED" in row.text:
                        self.utils.print_info("Client found")
                        self.utils.print_info("Retrieve the device's unique client information")
                        client_found = 1

                    elif get_client_mac:
                        if get_client_mac.lower() == client_mac.lower():
                            self.utils.print_info("Client found ", get_client_mac)
                            self.utils.print_info("Retrieve the device's unique client information")
                            client_found = 1
                    else:
                        self.close_device360_window()
                if client_found == 1:
                    break
            else:
                self.utils.print_info("Client not found yet! Retrying after 30 seconds")
                self.close_device360_window()
                sleep(sleep_time)

        if client_found == 1:
            client_info = dict()

            try:
                client_info["connection_type"] = self.deviceConfig.get_wired_client_connection_type().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Connection type not found")
                client_info["connection_type"] = None

            try:
                client_info["ostype"] = self.deviceConfig.get_wired_client_os_type().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Os type not found")
                client_info["ostype"] = None

            try:
                client_info["connectstatus"] = self.deviceConfig.get_wired_client_connection_status().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Connect status not found")
                client_info["connectstatus"] = None

            try:
                client_info["hostname"] = self.deviceConfig.get_wired_client_hostname().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Host Name not found")
                client_info["hostname"] = None

            try:
                client_info["clientmac"] = self.deviceConfig.get_wired_client_mac().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Client Mac not found")
                client_info["clientmac"] = None

            try:
                client_info["ipv4"] = self.deviceConfig.get_wired_client_IPv4().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> IPv4 Address not found")
                client_info["ipv4"] = None

            try:
                client_info["ipv6"] = self.deviceConfig.get_wired_client_IPv6().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> IPv6 not found")
                client_info["ipv6"] = None

            try:
                client_info["username"] = self.deviceConfig.get_wired_client_user_name().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Username not found")
                client_info["username"] = None

            try:
                client_info["vlan"] = self.deviceConfig.get_wired_client_vlan().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> vlan not found")
                client_info["vlan"] = None

            try:
                client_info["Connected_via"] = self.deviceConfig.get_wired_client_connected_via().text
            except Exception:
                self.utils.print_info("In Device360 -> clients table -> Connected via not found")
                client_info["Connected_via"] = None

            print("The complete client info -> ", client_info)
            self.close_device360_window()

            return client_info
        else:
            kwargs['fail_msg'] = "Client does not exists"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_click_clients(self, search_string, device_mac="", device_serial="", sleeptime=30, iteration=30,
                                **kwargs):
        """
        This keyword is to check whether the clients can be clickable
        :param search_string: The mac address of the client
        :param device_mac: Device MAC address for device selection
        :param device_serial: Device serial number for device selection
        :param sleeptime: The time period of sleep between each iteration
        :param iteration: the number of iteration
        :return: -1 if can't click client else return 1
        """
        count = 0
        for each in range(0, iteration):
            self.navigator.navigate_to_devices()
            count += 1
            self.utils.print_info("Checking the client for ")
            try:
                if device_mac:
                    self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
                    device_row = self.dev.get_device_row(device_mac=device_mac)
                    if device_row:
                        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                            kwargs['fail_msg'] = f"Device not found in the device row grid with mac: {device_mac}"
                            self.common_validation.fault(**kwargs)
                            return -1
                        sleep(8)

                if device_serial:
                    self.utils.print_info("Checking Search Result with Device Name : ", device_serial)
                    device_row = self.dev.get_device_row(device_serial=device_serial)
                    if device_row:
                        if self.navigator.navigate_to_device360_page_with_host_name(device_serial) == -1:
                            kwargs['fail_msg'] = f"Device not found in the device row grid with device name:{device_serial}"
                            self.common_validation.fault(**kwargs)
                            return -1
                        sleep(8)
                sleep(5)

            except Exception:
                kwargs['fail_msg'] = "Not able to navigate to the page"
                self.common_validation.fault(**kwargs)
                return -1
            sleep(5)

            self.utils.print_info("Click on Clients")
            sleep(3)
            self.device360_navigate_to_monitor_clients()

            self.utils.print_info("Searching Device Entry with Search String : ", search_string)
            self.auto_actions.send_keys(self.deviceConfig.get_unique_clients_search_field(), search_string)
            self.screen.save_screen_shot()
            sleep(5)
            # remove this try once AIQ-1529
            clickable = -1
            try:
                clickable = self.auto_actions.click_reference(self.dev360.get_device360_click_particular_client)
                if clickable == 1:
                    print("Able to click the client and see the popup...")
                    sleep(5)
                    break
            except Exception:
                print("There was an error during click of Client")

            if clickable != 1:
                print("The link is not clickable, so waiting for the client Mac address to become clickable")
                self.utils.print_info("Close D360 Dialogue Window")
                self.close_device360_window()
                self.dev.refresh_devices_page()

        kwargs['pass_msg'] = "Client is clickable"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_read_wired_clients_popup(self):
        """
        This keyword read the Wired client Popup
        This keyword assumes that we should have clicked the wired client pop-up
        Manage -> Devices -> Device 360 -> Clients -> Clickable client (clicked)
        :return: client details in dict format if found else it will return client details with None
        Client details: client mac,ipv4,ipv6,port speed,negotiated speed,vlan, port mode,
        """
        print(" we should have landed in C360 page")

        client_info = dict()

        try:
            print(self.deviceConfig.get_wired_client_popup_mac())
            client_info["client_mac"] = self.deviceConfig.get_wired_client_popup_mac().text

        except Exception:
            self.utils.print_info("In Client Popup, Client Mac not found")
            client_info["client_mac"] = None

        try:
            client_info["ipv4"] = self.deviceConfig.get_wired_client_popup_IPv4().text
        except Exception:
            self.utils.print_info("In Client Popup, IPv4 Address not found")
            client_info["ipv4"] = None

        try:
            client_info["ipv6"] = self.deviceConfig.get_wired_client_IPv6().text
        except Exception:
            self.utils.print_info("In Client Popup, IPv6 not found")
            client_info["ipv6"] = None

        try:
            client_info["port_speed"] = self.deviceConfig.get_wired_client_popup_portSpeed().text
        except Exception:
            self.utils.print_info("In Client Popup, Port speed not found")
            client_info["port_speed"] = None

        try:
            client_info["negotiated_speed"] = self.deviceConfig.get_wired_client_popup_negotiatedspeed().text
        except Exception:
            self.utils.print_info("In Client Popup, Negotiated speed not found")
            client_info["negotiated_speed"] = None

        try:
            client_info["vlan"] = self.deviceConfig.get_wired_client_popup_vlan().text
        except Exception:
            self.utils.print_info("In Client Popup, VLAN Not found")
            client_info["vlan"] = None
        try:
            client_info["portMode"] = self.deviceConfig.get_wired_client_popup_portMode().text
        except Exception:
            self.utils.print_info("In Client Popup, portMode not found")
            client_info["portMode"] = None

        self.utils.print_info("The complete client info -> ", client_info)
        return client_info

    def close_client360_window(self, **kwargs):
        """
        - This keyword closes the Device360 dialog window.  It assumes the Device360 Window is open - if the close
          button cannot be found, a message is printed.
        - Flow: Client 360 Window --> Click "X" to close Device360 Window
        - Keyword Usage:
        - ``Close Client360 Window``
        :return: 1 if the Client 360 window was closed, else -1
        """
        close_btn = self.dev360.get_client360_close_dialog()
        if close_btn:
            self.utils.print_info("Closing client360 Dialog Window.")
            self.auto_actions.click_reference(self.dev360.get_client360_close_dialog)
            kwargs['pass_msg'] = "Client 360 window was closed"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Could not obtain Client360 close button - make sure Client360 window is open")
            kwargs['fail_msg'] = "Could not obtain Client360 close button - make sure " \
                                 "Client360 window is open "
            self.common_validation.failed(**kwargs)
            return -1

    def device360_decide_clientpage_or_device360_page(self):
        """
        This keyword is to decide whether we have landed at client page or Device360 page
        :return: 1 if Device 360 page ,2 if Client 360 page else -1
        """
        connection_status = None
        client_status = None
        try:
            connection_status = self.dev360.get_system_info_device_model().text
        except Exception:
            self.utils.print_info(
                "There is a problem while fetching connection status in D360 page, which means we are not at intended page")
        try:
            client_status = self.deviceConfig.get_wired_client_popup_mac().text
        except Exception:
            self.utils.print_info(
                "There is a problem while fetching mac of client, which indirectly means we are not landed at C360 page")
        if client_status:
            print("The current page is client 360 page....")
            return 2
        elif connection_status:
            print("The current page is Device 360 page")
            return 1
        return -1

    def device360_set_network_policy(self, network_policy="default", **kwargs):
        """
        - This keyword sets a custom network policy on the Device Configuration page.
        - It is assumed that the Device360 window is open.
        - Flow : Device 360 Page -> Configure -> Device Configuration
        - Keyword Usage
        - ``device360_set_network_policy  network_policy=PPSK_POL``
        :return: 1 if the selection was made, -1 if not
        """
        self.utils.print_info(f"select '{network_policy}' from drop down")
        self.auto_actions.click_reference(self.get_device360_configure_device_network_policy)
        device_network_policy_drop_down_items = self.get_device360_configure_device_network_policy_items()

        if device_network_policy_drop_down_items:
            if self.auto_actions.select_drop_down_options(device_network_policy_drop_down_items, network_policy):
                self.utils.print_info(f"Selected network policy '{network_policy}' from drop down")

        element = self.get_device360_configure_device_network_policy()
        if element.text not in network_policy:
            kwargs['fail_msg'] = f"Not able to select '{network_policy}' from drop down"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "The selection was made"
        self.common_validation.passed(**kwargs)
        return 1

    def select_dhcp_ip_address_view(self, **kwargs):
        """
        - This keyword clicks the DHCP & IP Address link on the Configure tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Configure tab.
        - Flow: Device 360 Window --> Configure tab --> Click "DHCP & IP Address" link
        - Keyword Usage:
        - ``select_dhcp_ip_address_view``
        :return: 1 if the select_dhcp_ip_address_view was selected, else -1
        """
        dhcp_ip_link = self.get_device360_configure_dhcp_ip_address_link()
        if dhcp_ip_link:
            self.utils.print_info("Clicking the dhcp_ip_link on the Device360 Configure tab")
            self.auto_actions.click(dhcp_ip_link)
        else:
            kwargs['fail_msg'] = "Could not find the dhcp_ip_link - make sure Device360 window is open and on " \
                                 "Configure tab "
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "DHCP & IP Address link on the Configure tab in the Device360 dialog window was selected"
        self.common_validation.passed(**kwargs)
        return 1

    def search_for_vlan_subnetworks_type_in_row_table(self, *searched_values, **kwargs):
        """
        - This keyword searches any multiple values in the subnetworks row table
          The values must match to a row in table
          It assumes the Device360 Window is open and on the Configure tab.
        - Flow: Device 360 Window --> Configure tab --> Click "DHCP & IP Address" link
        - Keyword Usage:
        - ``search_for_vlan_subnetworks_type_in_row_table   192.168.167.0/25  MGMT  10``
        :param  *searched_values: list of searched values
        :return: 1 if all values are found in table
        """
        sleep(5)
        subnet_header = self.get_device360_configure_subnetworks_header()
        cells = self.get_device360_configure_subnetworks_tol_cells()

        if not cells:
            self.utils.print_info(" Table is empty ")
            kwargs['fail_msg'] = "Table is empty"
            self.common_validation.failed(**kwargs)
            return -1

        row_text = []
        cnt = 0
        found = False

        self.utils.print_info("Search for the values " + str(searched_values))
        for cell in cells:
            row_text.append(cell.text)
            cnt = cnt + 1
            if cnt == len(subnet_header):
                for value in searched_values:
                    if value in str(row_text):
                        found = True
                    else:
                        found = False
                        self.utils.print_info(str(row_text))
                        break
                if found:
                    self.utils.print_info("Able to locate the values in this row table " + str(row_text))
                    return 1
                row_text = []
                cnt = 0

        if not found:
            kwargs['fail_msg'] = "Not able to find the searched value in table"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_confirm_column_picker_column_selected(self, option, *columns, select_page="", device_mac="",
                                                        device_name="", **kwargs):
        """
        - This keyword confirms the list of columns are all selected in the column picker
        - Keyword Usage:
        - `Confirm Column Picker Column Selected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}`

        :param columns: list of device columns that should be selected
        :return: returns 1 if all columns are selected in the column picker; else, -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)

        sleep(5)
        if select_page == "Overview":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.select_monitor_overview()
        elif select_page == "Clients":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.select_monitor_clients()
        elif select_page == "Events":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.device360_select_events_view()
        elif select_page == "Alarms":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.device360_select_alarms_view()
        else:
            kwargs['fail_msg'] = f"No '{select_page}' page"
            self.common_validation.fault(**kwargs)
            return -1

        ret_val = 1
        self.utils.print_info("Clicking on Column Picker")
        sleep(5)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.auto_actions.click_reference(self.get_device360_column_picker_icon)
        sleep(2)
        if option.lower() == "check":
            self.utils.print_info("Column list to check for selected items: ", columns)
            for filter_ in columns:
                filter_row, row_num = self.dev._get_column_picker_filter_exact(filter_)
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
                                self.utils.print_info(f"Selecting Column Picker Filter '{filter_}'")
                                self.auto_actions.click(filter_row)
                            break
                else:
                    self.utils.print_info("Unable to obtain status of the column ", filter_)
                    ret_val = -1
        elif option.lower() == "uncheck":
            self.utils.print_info("Column list to uncheck for selected items: ", columns)
            for filter_ in columns:
                filter_row, row_num = self.dev._get_column_picker_filter_exact(filter_)
                if filter_row != "":
                    row_inputs = self.devices_web_elements.get_column_picker_row_input()
                    row_input_count = 0
                    for row_inp in row_inputs:
                        row_input_count += 1
                        if row_input_count == row_num:
                            ans = row_inp.get_attribute("checked")
                            if ans == "true":
                                self.utils.print_info(f"Column Picker Filter '{filter_}' is selected")
                                self.utils.print_info(f"Unselecting Column Picker Filter '{filter_}'")
                                self.auto_actions.click(filter_row)
                            else:
                                self.utils.print_info(f"Column Picker Filter '{filter_}' is not selected")
                            break
                else:
                    self.utils.print_info("Unable to obtain status of the column ", filter_)
                    ret_val = -1
        else:
            self.utils.print_info(f"No option available '{option}'")
            ret_val = -1
        sleep(2)
        self.utils.print_info("Closing Column Picker")
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.auto_actions.click_reference(self.get_device360_column_picker_icon)
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)

        if ret_val == -1:
            kwargs['fail_msg'] = f"Unable to obtain status of the column {filter_}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "All columns are selected in column picker"
            self.common_validation.passed(**kwargs)
        return ret_val

    def device360_check_column_picker(self, option, *columns, select_page="", device_mac="", device_name="", **kwargs):
        """
        This keyword confirms the list of the column picker values that was previously checked or unchecked in the
        column from a specific page
        :param option: check/uncheck columns picker values from each page
        :param columns: list of columns from each page that should be selected
        :param select_page: the page can be Overview/Clients/Alarms/Events
        :param device_mac: mac of the device
        :param device_name: name of the device
        :return: 1 if you can select the page and return the status of the column from the specific page; else -1
        """

        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(10)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(10)
        if select_page == "Overview":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.select_monitor_overview()
        elif select_page == "Clients":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.select_monitor_clients()
        elif select_page == "Events":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.device360_select_events_view()
        elif select_page == "Alarms":
            self.utils.print_info(f"Selecting '{select_page}' page")
            self.device360_select_alarms_view()
        else:
            kwargs['fail_msg'] = f"No '{select_page}' page"
            self.common_validation.fault(**kwargs)
            return -1
        ret_val = 1
        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.auto_actions.click_reference(self.get_device360_column_picker_icon)
        if option.lower() == "unchecked":
            self.utils.print_info(f"Checking '{columns}' are not selected")
            sleep(2)
            for filter_ in columns:
                filter_row, row_num = self.dev._get_column_picker_filter_exact(filter_)
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
                                sleep(2)
                else:
                    self.utils.print_info("Unable to obtain status of the column ", filter_)
                    ret_val = -1
        elif option.lower() == "checked":
            self.utils.print_info(f"Checking '{columns}' are selected")
            sleep(2)
            for filter_ in columns:
                filter_row, row_num = self.dev._get_column_picker_filter_exact(filter_)
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
                else:
                    self.utils.print_info("Unable to obtain status of the column ", filter_)
                    ret_val = -1
        else:
            self.utils.print_info(f"No option available '{option}'")
            ret_val = -1
        sleep(2)
        self.utils.print_info("Closing Column Picker")
        self.auto_actions.click_reference(self.get_device360_column_picker_icon)
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)

        if ret_val == -1:
            kwargs['fail_msg'] = f"Unable to obtain status of the column {filter_}"
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Successfully selected the page and return the status of the column from the " \
                                 "specific page "
            self.common_validation.passed(**kwargs)
        return ret_val

    def create_new_port_type(self, template_values, port, d360=False, verify_summary=True, **kwargs):
        """
        This function is used to create a new port type from d360 or template page by using new format

        :param template_values: A dictionary with below structure:

        Each element from dictionary template_values has the following format:
                'setting name': [configured_value, check_summary_value]

        To change the value of a setting, use the following syntax:
                template_voss_auto_sense_on['setting name'][0] = 'configured_value'
        To not configure an element from dictionary:
                template_voss_auto_sense_on['setting name'][0] = None

        To check the value of a setting into summary page, use the following sintax:
                template_voss_auto_sense_on['setting name'][1] = 'check_summary_value'
        To not verify an element from dictionary into summary page :
                template_voss_auto_sense_on['setting name'][1] = None

        To press next buttom use into dictionary an element like this : 'page2 accessVlanPage':["next_page", None],

        template_values=                {'name': ["port type name", 'port type name'],
                                        'description': ["add_description", "add_description"],
                                        'status':['click', 'off'],          #['click'/None, 'on'/'off'/None]
                                        'auto-sense':['click',None],       #['click'/None, None]
                                        'port usage':['trunk port', 'trunk'],
                                                #['trunk port'/'access port'/None, 'trunk'/'access'/'auto_sense'/None]

                                        #'page2 accessVlanPage':["next_page", None],       # used for access ports
                                        #'vlan':['40', '40'],                       # used for access ports

                                        'page2 trunkVlanPage': ["next_page", None],
                                        'native vlan': ['50', '50'],     # used for trunk ports
                                        'allowed vlans': ['60', '60'],   # used for trunk ports ['all'/None, 'all'/None]

                                        'page3 transmissionSettingsPage': ["next_page", None],
                                        'transmission type': ['auto','auto'],
                                            #['auto'/'Half-Duplex'/'Full-Duplex', 'auto'/'Half_Duplex'/'Full_Duplex'/None]
                                        'transmission speed':['auto','auto'],
                                            #['auto'/'10 Mbps'/'100 Mbps'/None, 'auto'/'10 Mbps'/'100 Mbps'/None]
                                        'cdp receive':[None, 'off'],        # ['click'/'None', 'on'/'off'/None]
                                        'lldp transmit':['click', 'off'],   # ['click'/'None', 'on'/'off'/None]
                                        'lldp receive':[None, 'off'],       # ['click'/'None', 'on'/'off'/None]

                                        'page4 stpPage': ["next_page", None],
                                        'stp enable':['click', 'enabled'],      #['click'/None, 'on'/'off'/None]
                                        'edge port': ['click', 'enabled'],      #['click'/None, 'on'/'off'/None]
                                        'bpdu protection':[None, 'disabled'],   #['click'/None, 'on'/'off'/None]
                                        'priority':['32', '32'],
                                                #['0'/'16'/'32'/'48'.../'192'/None, '0'/'16'/'32'/'48'.../'192'/None]
                                        'path cost':['50', '50'],   #['1 - 200000000'/None, '1 - 200000000'/None]

                                        'page5 stormControlSettingsPage': ["next_page", None],
                                        'broadcast':[None, 'disabled'],         #['click'/None, 'enabled'/'disabled'/None]
                                        'unknown unicast':[None, 'disabled'],   #[None, 'disabled'/None]
                                        'multicast':[None, 'disabled'],         #['click'/None, 'enabled'/'disabled'/None]
                                        'rate limit type':[None,'pps'],         #[None, 'pps'/None]
                                        'rate limit value': ['65535', '65535'], #['0-65535'/None, '0-65535'/None]

                                        #for VOSS
                                        'page6 pseSettingsPage': ["next_page", None],
                                        'PSE profile':[None,None],
                                                ## To select an already existing pse profile:
                                                # [{'pse_profile_name': 'default-pse-vsp'}/'None' , 'default-pse-vsp'/'None'],

                                                ## To create a new profile
                                                # [{'pse_profile_name': 'PSE_123',
                                                    'pse_profile_power_mode': '802.3at',
                                                    'pse_profile_power_limit': '20000',
                                                    'pse_profile_priority': 'high',
                                                    'pse_profile_description': 'Testing PSE'
                                                   }, 'PSE_123'/None],
                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page7 summaryPage': ["next_page", None]

                                        #==========================================
                                        #Only for exos
                                        'page6 ELRPSettingsPage': ["next_page", None],
                                        'elrp status': ['click', 'enabled'],      #['click'/None, 'on'/'off'/None]

                                        'page7 pseSettingsPage': ["next_page", None],
                                        'PSE profile':[None,None],
                                                ## To select an already existing pse profile:
                                                # [{'pse_profile_name': 'default-pse-vsp'}/'None' , 'default-pse-vsp'/'None'],

                                                ## To create a new profile
                                                # [{'pse_profile_name': 'PSE_123',
                                                    'pse_profile_power_mode': '802.3at',
                                                    'pse_profile_power_limit': '20000',
                                                    'pse_profile_priority': 'high',
                                                    'pse_profile_description': 'Testing PSE'
                                                   }, 'PSE_123'/None],

                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page8 summaryPage': ["next_page", None]
                                    }

        :param port: the port where new port type will be created
        :param d360: False if new port type will be created into policy template, True if new port type will be created
        into d360 page
        :param verify_summary: True if configured values will be verify on summary page. False if verification on summary
        page will be skipped
        :return: 1 if new port type was successfully created and summary page displays correct values  ; else -1
        """

        if template_values["name"][0] == None:
            self.utils.print_info("name can not be empty")
            kwargs['fail_msg'] = "name can not be empty"
            self.common_validation.fault(**kwargs)
            return -1

        if not d360:
            rows = self.get_policy_configure_port_rows()
            if not rows:
                self.utils.print_info("Could not obtain list of port rows")
                return -1
            else:
                for row in rows:
                    if port in row.text:
                        d360_create_port_type = self.get_d360_create_port_type(row)
                        if d360_create_port_type:
                            self.utils.print_info(" The button d360_create_port_type from policy  was found")
                            self.auto_actions.click(d360_create_port_type)
                            sleep(2)
                            break
                        else:
                            kwargs['fail_msg'] = "The button d360_create_port_type from policy was not found"
                            self.common_validation.fault(**kwargs)
                            return -1

        else:
            port_conf_content = self.get_device360_port_configuration_content()
            if port_conf_content:
                port_row = self.device360_get_port_row(port)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)

                    d360_create_port_type = self.get_d360_create_port_type(port_row)
                    if d360_create_port_type:
                        self.utils.print_info(" The button d360_create_port_type  was found")
                        self.auto_actions.click(d360_create_port_type)
                        sleep(2)
                    else:
                        kwargs['fail_msg'] = "The button d360_create_port_type from policy " \
                                             "was not found "
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "Port was not found"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Could not get port"
                self.common_validation.fault(**kwargs)
                return -1
        cnt = 0
        for key in template_values.keys():
            if not template_values[key][0] == None:
                conf_element = self.configure_element_port_type(key, template_values[key][0])
                if conf_element == 1:
                    self.utils.print_info("The element {} was configured ".format(key))
                else:
                    self.utils.print_info("The element {} was not configured ".format(key))
                    kwargs['fail_msg'] = "The element was not configured"
                    self.common_validation.failed(**kwargs)
                    return -1
            else:
                pass
            cnt = cnt + 1
        if verify_summary:
            return self.port_type_verify_summary(template_values)
        else:
            def _check_that_port_type_is_closed():
                if not self.get_close_port_type_box():
                    self.utils.print_info("Port type profile dialog has been closed")
                    return True
                else:
                    self.utils.print_info("Port type profile dialog box hasn't closed yet... Retrying...")
                    return False

            sleep(5)
            close_port_type_box = self.get_save_and_close_port_type_box()
            sleep(5)
            if close_port_type_box:
                self.utils.print_info(" The button close_port_type_box from policy  was found")
                self.auto_actions.click(close_port_type_box)
                self.utils.wait_till(_check_that_port_type_is_closed, is_logging_enabled=True, timeout=120, delay=5,
                                     silent_failure=True, msg="Checking that create new port type profile has been"
                                                              "dialog box has been closed...")
                sleep(2)
            else:
                self.utils.print_info(" The button close_port_type_box from policy was not found")
            return 1

    def edit_port_type(self, template_values, port, verify_summary=True, close_page=True, **kwargs):
        """
        This Keyword edit a port type and verify the summary page .

        :param template_values:
        A dictionary with below structure:

        Each element from dictionary template_values has the following format:
                'setting name': [configured_value, check_summary_value]

        To change the value of a setting, use the following syntax:
                template_voss_auto_sense_on['setting name'][0] = 'configured_value'
        To not configure an element from dictionary:
                template_voss_auto_sense_on['setting name'][0] = None

        To check the value of a setting into summary page, use the following sintax:
                template_voss_auto_sense_on['setting name'][1] = 'check_summary_value'
        To not verify an element from dictionary into summary page :
                template_voss_auto_sense_on['setting name'][1] = None

        To press next buttom use into dictionary an element like this : 'page2 accessVlanPage':["next_page", None],

        template_values=                {'name': ["port type name", 'port type name'],
                                        'description': ["add_description", "add_description"],
                                        'status':['click', 'off'],          #['click'/None, 'on'/'off'/None]
                                        'auto-sense':['click',None],       #['click'/None, None]
                                        'port usage':['trunk port', 'trunk'],
                                                #['trunk port'/'access port'/None, 'trunk'/'access'/'auto_sense'/None]

                                        #'page2 accessVlanPage':["next_page", None],       # used for access ports
                                        #'vlan':['40', '40'],                       # used for access ports

                                        'page2 trunkVlanPage': ["next_page", None],
                                        'native vlan': ['50', '50'],     # used for trunk ports
                                        'allowed vlans': ['60', '60'],   # used for trunk ports ['all'/None, 'all'/None]

                                        'page3 transmissionSettingsPage': ["next_page", None],
                                        'transmission type': ['auto','auto'],
                                            #['auto'/'Half-Duplex'/'Full-Duplex', 'auto'/'Half_Duplex'/'Full_Duplex'/None]
                                        'transmission speed':['auto','auto'],
                                            #['auto'/'10 Mbps'/'100 Mbps'/None, 'auto'/'10 Mbps'/'100 Mbps'/None]
                                        'cdp receive':[None, 'off'],        # ['click'/'None', 'on'/'off'/None]
                                        'lldp transmit':['click', 'off'],   # ['click'/'None', 'on'/'off'/None]
                                        'lldp receive':[None, 'off'],       # ['click'/'None', 'on'/'off'/None]

                                        'page4 stpPage': ["next_page", None],
                                        'stp enable':['click', 'enabled'],      #['click'/None, 'on'/'off'/None]
                                        'edge port': ['click', 'enabled'],      #['click'/None, 'on'/'off'/None]
                                        'bpdu protection':[None, 'disabled'],   #['click'/None, 'on'/'off'/None]
                                        'priority':['32', '32'],
                                                #['0'/'16'/'32'/'48'.../'192'/None, '0'/'16'/'32'/'48'.../'192'/None]
                                        'path cost':['50', '50'],   #['1 - 200000000'/None, '1 - 200000000'/None]

                                        'page5 stormControlSettingsPage': ["next_page", None],
                                        'broadcast':[None, 'disabled'],         #['click'/None, 'enabled'/'disabled'/None]
                                        'unknown unicast':[None, 'disabled'],   #[None, 'disabled'/None]
                                        'multicast':[None, 'disabled'],         #['click'/None, 'enabled'/'disabled'/None]
                                        'rate limit type':[None,'pps'],         #[None, 'pps'/None]
                                        'rate limit value': ['65535', '65535'], #['0-65535'/None, '0-65535'/None]

                                        #for VOSS
                                        'page6 pseSettingsPage': ["next_page", None],
                                        'PSE profile':[None,None],
                                                ## To edit and existing PSE profile, add: 'pse_profile_edit_flag': True
                                                # [{'pse_profile_name': 'PSE_123'
                                                #   'pse_profile_power_mode': '802.3bt',
                                                #   'pse_profile_power_limit': '30000',
                                                #   'pse_profile_priority': 'low',
                                                #   'pse_profile_description': 'Testing PSE EDIT',
                                                #   'pse_profile_edit_flag': True
                                                #  }, 'PSE_123'/None],
                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page7 summaryPage': ["next_page", None]

                                        #==========================================
                                        #Only for EXOS
                                        'page6 ELRPSettingsPage': ["next_page", None],
                                        'elrp status': ['click', 'enabled'],      #['click'/None, 'on'/'off'/None]

                                        'page7 pseSettingsPage': ["next_page", None],
                                        'PSE profile':[None,None],
                                                ## To edit and existing PSE profile, add: 'pse_profile_edit_flag': True
                                                # [{'pse_profile_name': 'PSE_123'
                                                #   'pse_profile_power_mode': '802.3bt',
                                                #   'pse_profile_power_limit': '30000',
                                                #   'pse_profile_priority': 'low',
                                                #   'pse_profile_description': 'Testing PSE EDIT',
                                                #   'pse_profile_edit_flag': True
                                                #  }, 'PSE_123'/None],
                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page8 summaryPage': ["next_page", None]
                                    }
        :param port: the port where new port type will be created
        :param verify_summary: True if configured values will be verify on summary page. False if verification on summary
        page will be skipped
        :return: 1 if new port type was successfully edited and summary page displays correct values  ; else -1
        """
        self.utils.print_info("Waiting for the policy rows to load...")
        self.utils.wait_till(self.get_policy_configure_port_rows, delay=5)
        rows = self.get_policy_configure_port_rows()
        if not rows:
            kwargs['fail_msg'] = "Could not obtain list of port rows"
            self.common_validation.fault(**kwargs)
            return -1
        else:
            for row in rows:
                if port in row.text:

                    def _wait_for_edit_button_to_load():
                        if self.get_policy_edit_port_type(row):
                            self.utils.print_info("Edit port type profile button has been found")
                            return True
                        else:
                            self.utils.print_info("Edit port type profile hasn't been found yet... Retrying...")
                            return False

                    self.utils.wait_till(_wait_for_edit_button_to_load, timeout=40, delay=3, is_logging_enabled=True,
                                         silent_failure=True, msg="Waiting for edit port type profile button to show..")
                    policy_edit_port_type = self.get_policy_edit_port_type(row)
                    if policy_edit_port_type:
                        self.utils.print_info(" The button policy_edit_port_type from policy was found")
                        self.auto_actions.click(policy_edit_port_type)
                        sleep(2)
                        break
                    else:
                        kwargs['fail_msg'] = "The button policy_edit_port_type from policy was not found"
                        self.common_validation.fault(**kwargs)
                        return -1
        cnt = 0
        for key in template_values.keys():
            if not template_values[key][0] == None or 'usagePage' in key:
                self.utils.print_info(key)
                if "page" in key:
                    conf_element = self.configure_element_port_type(key, "None")
                    self.utils.print_info("return", conf_element)
                    if conf_element == 1:
                        self.utils.print_info("The element {} was configured ".format(key))
                    else:
                        self.utils.print_info("The element {} was not configured ".format(key))
                        kwargs['fail_msg'] = "The element was not configured"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    conf_element = self.configure_element_port_type(key, template_values[key][0])
                    if conf_element == 1:
                        self.utils.print_info("The element {} was configured ".format(key))
                    else:
                        self.utils.print_info("The element {} was not configured ".format(key))
                        kwargs['fail_msg'] = "The element was not configured"
                        self.common_validation.failed(**kwargs)
                        return -1
            else:
                pass
            cnt = cnt + 1
        if verify_summary:
            return self.port_type_verify_summary(template_values)
        else:
            def _check_that_port_type_is_closed():
                if not self.get_close_port_type_box():
                    self.utils.print_info("Port type profile dialog box has been closed")
                    return True
                else:
                    self.utils.print_info("Port type profile dialog box hasn't closed yet... Retrying...")
                    return False
            if close_page:
                close_port_type_box = self.get_close_port_type_box()
                if close_port_type_box:
                    self.utils.print_info(" The button close_port_type_box from policy  was found")
                    self.auto_actions.click(close_port_type_box)
                    self.utils.wait_till(_check_that_port_type_is_closed, is_logging_enabled=True, timeout=120, delay=5,
                                         silent_failure=True, msg="EDIT - Checking that create new port type profile has been"
                                                                  "dialog box has been closed...")
                else:
                    self.utils.print_info(" The button close_port_type_box from policy was not found")
                    return -1
            kwargs['pass_msg'] = "edit_port_type() -> All elements were configured"
            self.common_validation.passed(**kwargs)
            return 1

    def port_type_verify_summary(self, template_values, **kwargs):
        """
        This keyword verify the summary after configure new port type.
        See edit_port_type and create_new_port_type
        :param template_values: a dictionary (See edit_port_type and create_new_port_type )
        :return: 1 if informations from summary page are correct ; else -1
        """

        cnt = 0
        for key in template_values.keys():
            cnt = cnt + 1
            if not template_values[key][1] == None:
                sleep(5)
                conf_element = self.get_select_element_port_type_summary(key.lower())
                print("For ", key, "we have ", conf_element)
                if conf_element.text.lower() == template_values[key][1].lower():
                    self.utils.print_info(f"The element is correct into summary. Key: {key}  Value: "
                                          f"{conf_element.text.lower()}")
                else:
                    self.utils.print_info("The element is not correct into summary. Current value in summary:" +
                                          conf_element.text + " Wanted value: " + template_values[key][1])
                    cancel_button_port_type = self.get_cancel_button_port_type()
                    self.utils.print_info("Canceling the port type profile")
                    self.auto_actions.click(cancel_button_port_type)
                    kwargs['fail_msg'] = "The element is not correct into summary."
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                pass

        def _check_that_port_type_is_closed():
            if not self.get_close_port_type_box():
                self.utils.print_info("Port type profile dialog box has been closed")
                return True
            else:
                self.utils.print_info("Port type profile dialog box hasn't closed yet... Retrying...")
                return False

        close_port_type_box = self.get_close_port_type_box()
        if close_port_type_box:
            self.utils.print_info(" The button close_port_type_box from policy  was found")
            self.auto_actions.click(close_port_type_box)
            self.utils.wait_till(_check_that_port_type_is_closed, is_logging_enabled=True, timeout=120, delay=5,
                                 silent_failure=True, msg="Checking that create new port type profile has been"
                                                          "dialog box has been closed...")
            sleep(2)
        else:
            self.utils.print_info(" The button close_port_type_box from policy was not found")
        return 1

    def configure_element_port_type(self, element, value):
        """
        This keyword select the Tabs and configure all field when create or edit a new port type
        See edit_port_type and create_new_port_type
        :param element: name of field
        :param value: value of field ; if contains the string "next_page" will move to next tab
        :return:
        """

        # tab
        sleep(2)
        if "next_page" in value:
            sleep(5)

            def _check_next_button():
                if self.get_select_element_port_type("next_button"):
                    self.utils.print_info("Found 'next' button")
                    return True
                else:
                    self.utils.print_info("Did not find next button. Retrying...")
                    self.screen.save_screen_shot()
                    return False
            self.utils.wait_till(_check_next_button, timeout=30, delay=1, silent_failure=True, is_logging_enabled=True,
                                 msg="Waiting for 'next' button to load...")

            get_next_button = self.get_select_element_port_type("next_button")
            if get_next_button:
                sleep(5)
                self.auto_actions.click(get_next_button)
                sleep(2)
                return 1
            else:
                self.utils.print_info("get_next_button not found ")

        elif "next_all_pages" in value:
            sleep(5)
            cnt = 0
            flag_save_is_displayed = False
            while not flag_save_is_displayed and cnt < 10:
                summaryPage = self.get_select_element_port_type("summaryPage")
                if summaryPage:
                    self.utils.print_info("bgd", summaryPage.get_attribute("class"))
                    if "active" in summaryPage.get_attribute("class"):
                        flag_save_is_displayed = True
                        break
                    else:
                        get_next_button = self.get_select_element_port_type("next_button")
                        if get_next_button:
                            sleep(2)
                            self.auto_actions.click(get_next_button)
                        else:
                            self.utils.print_info("get_next_button not found ")
                else:
                    self.utils.print_info("save_and_close_port_type_box not found ")
                cnt = cnt + 1
            if flag_save_is_displayed:
                return 1

        elif "usagePage" in element:
            sleep(5)

            def _check_usage_page():
                if self.get_select_element_port_type("usagePage"):
                    self.utils.print_info("Found 'usagePage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'usagePage' button. Retrying...")
                    return False
            self.utils.wait_till(_check_usage_page, timeout=30, delay=1, silent_failure=True, is_logging_enabled=True,
                                 msg="Waiting for 'usagePage' button to load...")

            get_tab_usagePage = self.get_select_element_port_type("usagePage")
            if get_tab_usagePage:
                sleep(5)
                self.auto_actions.click(get_tab_usagePage)
                return 1

        elif "trunkVlanPage" in element or "accessVlanPage" in element or 'phoneVlanPage' in element:
            sleep(5)

            def _check_vlan_page():
                if self.get_select_element_port_type("tab_vlan"):
                    self.utils.print_info("Found 'tab_vlan' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'tab_vlan' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False
            self.utils.wait_till(_check_vlan_page, timeout=30, delay=1, silent_failure=True, is_logging_enabled=True,
                                 msg="Waiting for 'vlanPage' to load...")

            get_tab_vlan = self.get_select_element_port_type("tab_vlan")
            if get_tab_vlan:
                sleep(5)
                self.auto_actions.click(get_tab_vlan)
                return 1

        elif "transmissionSettingsPage" in element:
            sleep(5)

            def _check_transmission_settings_page():
                if self.get_select_element_port_type("transmissionSettingsPage"):
                    self.utils.print_info("Found 'transmissionSettingsPage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'transmissionSettingsPage' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False
            self.utils.wait_till(_check_transmission_settings_page, timeout=30, delay=1, silent_failure=True,
                                 is_logging_enabled=True, msg="Waiting for 'transmissionSettingsPage' to load...")

            get_tab_transmission = self.get_select_element_port_type("transmissionSettingsPage")
            if get_tab_transmission:
                sleep(5)
                self.auto_actions.click(get_tab_transmission)
                return 1

        elif "stpPage" in element:
            sleep(5)

            def _check_stp_page():
                if self.get_select_element_port_type("stpPage"):
                    self.utils.print_info("Found 'stpPage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'stpPage' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False
            self.utils.wait_till(_check_stp_page, timeout=30, delay=1, silent_failure=True, is_logging_enabled=True,
                                 msg="Waiting for 'stpPage' to load...")

            get_tab_stp = self.get_select_element_port_type("stpPage")
            if get_tab_stp:
                sleep(5)
                self.auto_actions.click(get_tab_stp)
                return 1

        elif "stormControlSettingsPage" in element:
            sleep(5)

            def _check_stormControlSettingsPage():
                if self.get_select_element_port_type("stormControlSettingsPage"):
                    self.utils.print_info("Found 'stormControlSettingsPage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'stormControlSettingsPage' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False
            self.utils.wait_till(_check_stormControlSettingsPage, timeout=30, delay=1, silent_failure=True,
                                 is_logging_enabled=True, msg="Waiting for 'stormControlSettingsPage' to load...")

            get_storm_control = self.get_select_element_port_type("stormControlSettingsPage")
            if get_storm_control:
                sleep(5)
                self.auto_actions.click(get_storm_control)
                return 1

        elif "MACLOCKINGSettingsPage" in element:
            get_mac_locking = self.get_select_element_port_type("MACLOCKINGSettingsPage")
            if get_mac_locking:
                self.auto_actions.click(get_mac_locking)
                return 1

        elif "ELRPSettingsPage" in element:
            sleep(5)

            def _check_stormControlSettingsPage():
                if self.get_select_element_port_type("ELRPSettingsPage"):
                    self.utils.print_info("Found 'ELRPSettingsPage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'ELRPSettingsPage' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False

            self.utils.wait_till(_check_stormControlSettingsPage, timeout=30, delay=1, silent_failure=True,
                                 is_logging_enabled=True, msg="Waiting for 'ELRPSettingsPage' to load...")

            get_elrp = self.get_select_element_port_type("ELRPSettingsPage")
            if get_elrp:
                sleep(5)
                self.auto_actions.click(get_elrp)
                return 1

        elif "pseSettingsPage" in element:
            sleep(5)

            def _check_pse_settings_page():
                if self.get_select_element_port_type("pseSettingsPage"):
                    self.utils.print_info("Found 'pseSettingsPage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'pseSettingsPage' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False

            self.utils.wait_till(_check_pse_settings_page, timeout=30, delay=1, silent_failure=True,
                                 is_logging_enabled=True, msg="Waiting for 'pseSettingsPage' to load...")

            get_tab_pse_settings = self.get_select_element_port_type("pseSettingsPage")
            if get_tab_pse_settings:
                sleep(5)
                self.auto_actions.click(get_tab_pse_settings)
                return 1

        elif "summaryPage" in element:
            sleep(5)

            def _check_pse_settings_page():
                if self.get_select_element_port_type("summaryPage"):
                    self.utils.print_info("Found 'summaryPage' button")
                    return True
                else:
                    self.utils.print_info("Did not find 'summaryPage' button. Retrying...")
                    self.screen.save_screen_shot()
                    return False

            self.utils.wait_till(_check_pse_settings_page, timeout=30, delay=1, silent_failure=True,
                                 is_logging_enabled=True, msg="Waiting for 'summaryPage' to load...")

            get_tab_summary = self.get_select_element_port_type("summaryPage")
            if get_tab_summary:
                sleep(5)
                self.auto_actions.click(get_tab_summary)
                return 1
        # page Port Name
        elif element == "name":
            sleep(5)
            get_name_el = self.get_select_element_port_type(element)
            if get_name_el:
                self.auto_actions.send_keys(get_name_el, value)
                return 1
        elif element == "description":
            sleep(5)
            get_description_el = self.get_select_element_port_type(element)
            if get_description_el:
                self.auto_actions.send_keys(get_description_el, value)
                return 1
        elif element == "status":
            sleep(5)
            get_status_el = self.get_select_element_port_type(element)
            if get_status_el:
                self.auto_actions.click(get_status_el)
                return 1
        elif element == "auto-sense":
            sleep(5)
            get_auto_sense_el = self.get_select_element_port_type(element)
            if get_auto_sense_el:
                self.auto_actions.click(get_auto_sense_el)
                return 1
        elif element == "port usage" and value == "access port":
            sleep(5)
            get_access_el = self.get_select_element_port_type(element, value)
            if get_access_el:
                sleep(2)
                self.auto_actions.click(get_access_el)
                return 1
        elif element == "port usage" and value == "trunk port":
            sleep(5)
            get_trunk_el = self.get_select_element_port_type(element, value)
            self.utils.print_info("trunk element", get_trunk_el)
            if get_trunk_el:
                sleep(2)
                self.auto_actions.click(get_trunk_el)
                return 1
        elif element == "port usage" and value == "phone port":
            get_phone_el = self.get_select_element_port_type(element,value)
            self.utils.print_info("phone element",get_phone_el)
            if get_phone_el:
                self.auto_actions.click(get_phone_el)
                return 1
        # page Vlan
        elif element == "vlan":
            sleep(5)
            get_select_button = self.get_select_element_port_type("select_button")
            sleep(5)
            if get_select_button:
                self.auto_actions.click(get_select_button)
                sleep(2)
                get_dropdown_items = self.get_select_element_port_type("dropdown_items")
                sleep(5)
                if self.auto_actions.select_drop_down_options(get_dropdown_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
                else:
                    sleep(5)
                    get_add_vlan = self.get_select_element_port_type("add_vlan")
                    sleep(5)
                    if get_add_vlan:
                        self.auto_actions.click(get_add_vlan)
                        sleep(5)
                        get_name_vlan = self.get_select_element_port_type("name_vlan")
                        sleep(5)
                        if get_name_vlan:
                            sleep(5)
                            self.auto_actions.send_keys(get_name_vlan, value)
                            sleep(2)
                        else:
                            self.utils.print_info("get_id_vlan not found ")
                        sleep(5)
                        get_id_vlan = self.get_select_element_port_type("id_vlan")
                        if get_id_vlan:
                            self.auto_actions.send_keys(get_id_vlan, value)
                            sleep(2)
                        else:
                            self.utils.print_info("get_id_vlan not found ")
                        sleep(5)
                        get_save_vlan = self.get_select_element_port_type("save_vlan")
                        if get_save_vlan:
                            self.auto_actions.click(get_save_vlan)
                            return 1
                        else:
                            self.utils.print_info("get_id_vlan not found ")
                    else:
                        self.utils.print_info("get_add_vlan not found ")
            else:
                self.utils.print_info("get_select_button not found ")
            self.utils.print_info(" Error when configure vlan  ")
            return -1

        elif element == "native vlan":
            sleep(5)
            get_select_button = self.get_select_element_port_type("native_vlan_select_button")
            if get_select_button:
                self.auto_actions.click(get_select_button)
                sleep(2)
                get_dropdown_items = self.get_select_element_port_type("native_vlan_dropdown_items")
                if self.auto_actions.select_drop_down_options(get_dropdown_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
                else:
                    sleep(5)
                    get_add_vlan = self.get_select_element_port_type("native_vlan_add_vlan")
                    if get_add_vlan:
                        self.auto_actions.click(get_add_vlan)
                        sleep(5)
                        get_name_vlan = self.get_select_element_port_type("native_vlan_name_vlan")
                        if get_name_vlan:
                            self.auto_actions.send_keys(get_name_vlan, value)
                            sleep(2)
                        else:
                            self.utils.print_info("native vlan get_id_vlan not found ")
                        sleep(5)
                        get_id_vlan = self.get_select_element_port_type("native_vlan_id_vlan")
                        if get_id_vlan:
                            self.auto_actions.send_keys(get_id_vlan, value)
                            sleep(2)
                        else:
                            self.utils.print_info("native vlan get_id_vlan not found ")
                        sleep(5)
                        get_save_vlan = self.get_select_element_port_type("save_vlan")
                        if get_save_vlan:
                            self.auto_actions.click(get_save_vlan)
                            return 1
                        else:
                            self.utils.print_info("get_save_vlan not found ")
                    else:
                        self.utils.print_info("native vlan get_add_vlan not found ")
            else:
                self.utils.print_info("native vlan get_select_button not found ")
            self.utils.print_info(" Error when configure native vlan ")
            return -1

        elif element == "voice vlan":
            def _save_vlan_disappear():
                return not bool(self.get_select_element_port_type("save_vlan"))

            def _voice_vlan_appear():
                return bool(self.get_select_element_port_type("voice_vlan_name_vlan"))

            def _voice_vlan_dropdown():
                return bool(self.get_select_element_port_type("voice_vlan_dropdown_items"))


            get_select_button = self.get_select_element_port_type("voice_vlan_select_button")
            if get_select_button:
                self.auto_actions.click(get_select_button)

                self.utils.wait_till(_voice_vlan_dropdown,is_logging_enabled=True)
                get_dropdown_items = self.get_select_element_port_type("voice_vlan_dropdown_items")
                if self.auto_actions.select_drop_down_options(get_dropdown_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
                else:
                    get_add_vlan = self.get_select_element_port_type("voice_vlan_add_vlan")
                    if get_add_vlan:
                        self.auto_actions.click(get_add_vlan)

                        self.utils.wait_till(_voice_vlan_appear,is_logging_enabled=True)

                        get_name_vlan = self.get_select_element_port_type("voice_vlan_name_vlan")
                        if get_name_vlan:
                            self.auto_actions.send_keys(get_name_vlan,value)
                        else:
                            self.utils.print_info("voice vlan get_id_vlan not found ")
                        get_id_vlan = self.get_select_element_port_type("voice_vlan_id_vlan")
                        if get_id_vlan:
                            self.auto_actions.send_keys(get_id_vlan,value)
                        else:
                            self.utils.print_info("voice vlan get_id_vlan not found ")
                        get_save_vlan = self.get_select_element_port_type("save_vlan")
                        if get_save_vlan:
                            self.auto_actions.click(get_save_vlan)

                            self.utils.wait_till(_save_vlan_disappear, is_logging_enabled=True)
                            return 1
                        else:
                            self.utils.print_info("get_save_vlan not found ")
                    else:
                        self.utils.print_info("voice vlan get_add_vlan not found ")
            else:
                self.utils.print_info("voice vlan get_select_button not found ")
            self.utils.print_info(" Error when configure voice vlan ")
            return -1
        elif element == "data vlan":

            def _data_vlan_dropdown():
                return bool(self.get_select_element_port_type("data_vlan_dropdown_items"))

            def _data_vlan_appear():
                return bool(self.get_select_element_port_type("data_vlan_name_vlan"))

            def _save_vlan_disappear():
                return not bool(self.get_select_element_port_type("save_vlan"))

            get_select_button = self.get_select_element_port_type("data_vlan_select_button")
            if get_select_button:
                self.auto_actions.click(get_select_button)

                self.utils.wait_till(_data_vlan_dropdown, is_logging_enabled=True)

                get_dropdown_items = self.get_select_element_port_type("data_vlan_dropdown_items")
                if self.auto_actions.select_drop_down_options(get_dropdown_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
                else:
                    get_add_vlan = self.get_select_element_port_type("data_vlan_add_vlan")
                    if get_add_vlan:
                        self.auto_actions.click(get_add_vlan)

                        self.utils.wait_till(_data_vlan_appear,is_logging_enabled=True)
                        get_name_vlan = self.get_select_element_port_type("data_vlan_name_vlan")
                        if get_name_vlan:
                            self.auto_actions.send_keys(get_name_vlan,value)
                        else:
                            self.utils.print_info("data vlan get_id_vlan not found ")
                        get_id_vlan = self.get_select_element_port_type("data_vlan_id_vlan")
                        if get_id_vlan:
                            self.auto_actions.send_keys(get_id_vlan,value)
                        else:
                            self.utils.print_info("data vlan get_id_vlan not found ")
                        get_save_vlan = self.get_select_element_port_type("save_vlan")
                        if get_save_vlan:
                            self.auto_actions.click(get_save_vlan)
                            self.utils.wait_till(_save_vlan_disappear, is_logging_enabled=True)
                            return 1
                        else:
                            self.utils.print_info("get_save_vlan not found ")
                    else:
                        self.utils.print_info("data vlan get_add_vlan not found ")
            else:
                self.utils.print_info("data vlan get_select_button not found ")
            self.utils.print_info(" Error when configure data vlan ")
            return -1

        elif element in ["lldp_voice_vlan_options", "cdp_voice_vlan_options"]:
            get_options_el = self.get_select_element_port_type(element)
            if get_options_el:
                self.auto_actions.click(get_options_el)
                return 1

        elif element == "enable_lldp_advertisment_of_dot1_vlan":
            get_options_el = self.get_select_element_port_type(element)
            if get_options_el:
                self.auto_actions.click(get_options_el)
                return 1

        elif element == "enable_lldp_advertisment_of_med_voice_vlan":
            get_options_el = self.get_select_element_port_type(element)
            if get_options_el:
                self.auto_actions.click(get_options_el)
                return 1

        elif element == "lldp_advertisment_of_med_voice_vlan_dscp_value":
            get_value_el = self.get_select_element_port_type(element)
            if get_value_el:
                self.auto_actions.send_keys(get_value_el, value)
                return 1

        elif element == "enable_lldp_advertisment_of_med_voice_signaling_vlan":
            get_options_el = self.get_select_element_port_type(element)
            if get_options_el:
                self.auto_actions.click(get_options_el)
                return 1

        elif element == "lldp_advertisment_of_med_voice_signaling_vlan_dscp_value":
            get_value_el = self.get_select_element_port_type(element)
            if get_value_el:
                self.auto_actions.send_keys(get_value_el, value)
                return 1

        elif element == "enable_cdp_advertisment_of_voice_vlan":
            get_options_el = self.get_select_element_port_type(element)
            if get_options_el:
                self.auto_actions.click(get_options_el)
                return 1

        elif element == "enable_cdp_advertisment_of_power_available":
            get_options_el = self.get_select_element_port_type(element)
            if get_options_el:
                self.auto_actions.click(get_options_el)
                return 1

        elif element == "allowed vlans":
            sleep(5)
            get_allowed_vlans = self.get_select_element_port_type(element)
            if get_allowed_vlans:
                self.auto_actions.send_keys(get_allowed_vlans, value)
                return 1
        # Page Transmission
        elif element == "transmission type":
            sleep(5)
            get_transmission_type = self.get_select_element_port_type(element)
            if get_transmission_type:
                sleep(2)
                self.auto_actions.click(get_transmission_type)
                sleep(2)
                get_dropdown_items = self.get_select_element_port_type("transmission_type_dropdown_items")
                if self.auto_actions.select_drop_down_options(get_dropdown_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
        elif element == "transmission speed":
            sleep(5)
            get_transmission_speed = self.get_select_element_port_type(element)
            if get_transmission_speed:
                sleep(2)
                self.auto_actions.click(get_transmission_speed)
                sleep(2)
                get_dropdown_items = self.get_select_element_port_type("transmission_speed_dropdown_items")
                if self.auto_actions.select_drop_down_options(get_dropdown_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
                else:
                    self.utils.print_info(" Error get_dropdown_items ")
            else:
                self.utils.print_info(" Error get_transmission_speed ")
        elif element == "cdp receive":
            sleep(5)
            get_lldp_receive = self.get_select_element_port_type(element)
            if get_lldp_receive:
                sleep(2)
                self.auto_actions.click(get_lldp_receive)
                return 1
        elif element == "lldp transmit":
            sleep(5)
            get_lldp_transmit = self.get_select_element_port_type(element)
            if get_lldp_transmit:
                sleep(2)
                self.auto_actions.click(get_lldp_transmit)
                return 1
        elif element == "lldp receive":
            sleep(5)
            get_lldp_receive = self.get_select_element_port_type(element)
            if get_lldp_receive:
                sleep(2)
                self.auto_actions.click(get_lldp_receive)
                return 1
        # page STP
        elif element == "stp enable":
            sleep(5)
            get_stp_el = self.get_select_element_port_type(element, value)
            if get_stp_el:
                sleep(2)
                self.auto_actions.click(get_stp_el)
                return 1
        elif element == "edge port":
            sleep(5)
            get_edge_el = self.get_select_element_port_type(element, value)
            if get_edge_el:
                sleep(2)
                self.auto_actions.click(get_edge_el)
                return 1
        elif element == "bpdu protection":
            sleep(5)
            get_bpdu_protection = self.get_select_element_port_type(element)
            if get_bpdu_protection:
                sleep(2)
                self.auto_actions.click(get_bpdu_protection)
                sleep(5)
                get_bpdu_protection_items = self.get_select_element_port_type("bpdu_protection_items")
                if self.auto_actions.select_drop_down_options(get_bpdu_protection_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
        elif element == "priority":
            sleep(5)
            get_priority = self.get_select_element_port_type(element)
            if get_priority:
                sleep(2)
                self.auto_actions.click(get_priority)
                sleep(5)
                get_priority_items = self.get_select_element_port_type("priority_items")
                if self.auto_actions.select_drop_down_options(get_priority_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
        elif element == "path cost":
            sleep(5)
            get_cost_el = self.get_select_element_port_type(element)
            if get_cost_el:
                sleep(2)
                self.auto_actions.send_keys(get_cost_el, value)
                return 1
        # page Storm Control
        elif element == "broadcast":
            sleep(5)
            get_broadcast_el = self.get_select_element_port_type(element, value)
            if get_broadcast_el:
                sleep(2)
                self.auto_actions.click(get_broadcast_el)
                return 1
        elif element == "unknown unicast":
            sleep(5)
            get_unknown_el = self.get_select_element_port_type(element, value)
            if get_unknown_el:
                sleep(2)
                self.auto_actions.click(get_unknown_el)
                return 1
        elif element == "multicast":
            sleep(5)
            get_multicast_el = self.get_select_element_port_type(element, value)
            if get_multicast_el:
                sleep(2)
                self.auto_actions.click(get_multicast_el)
                return 1
        elif element == "rate limit type":
            return 1
        elif element == "rate limit value":
            sleep(5)
            get_rate_limit_val_el = self.get_select_element_port_type(element)
            if get_rate_limit_val_el:
                sleep(2)
                self.auto_actions.send_keys(get_rate_limit_val_el, value)
                return 1

        # page MAC LOCKING
        elif element == "mac locking":
            get_maclocking = self.get_select_element_port_type(element, value)
            if get_maclocking:
                sleep(3)
                self.auto_actions.click(get_maclocking)
                return 1

        elif element == "max first arrival":
            get_max_first_arrival_el = self.get_select_element_port_type(element)
            if get_max_first_arrival_el:
                self.auto_actions.send_keys(get_max_first_arrival_el, value)
                return 1

        elif element == "disable port":
            get_maclocking_disable_port = self.get_select_element_port_type(element, value)
            if get_maclocking_disable_port:
                self.auto_actions.click(get_maclocking_disable_port)
                return 1

        elif element == "link down clear":
            get_maclocking_link_down_clear = self.get_select_element_port_type(element, value)
            if get_maclocking_link_down_clear:
                self.auto_actions.click(get_maclocking_link_down_clear)
                return 1

        elif element == "link down retain":
            get_maclocking_link_down_retain = self.get_select_element_port_type(element, value)
            if get_maclocking_link_down_retain:
                self.auto_actions.click(get_maclocking_link_down_retain)
                return 1

        elif element == "remove aged MACs":
            get_maclocking_remove_aged_MACs = self.get_select_element_port_type(element, value)
            if get_maclocking_remove_aged_MACs:
                self.auto_actions.click(get_maclocking_remove_aged_MACs)
                return 1

        #page ELRP (ONLY FOR EXOS)

        elif element == "elrp status":
            sleep(5)
            get_elrp_status = self.get_select_element_port_type(element, value)
            if get_elrp_status:
                sleep(2)
                self.auto_actions.click(get_elrp_status)
                return 1

        # page PSE
        elif element.lower() == "pse profile":
            self.utils.print_info("Pse Profile is :", value)
            sleep(5)

            try:
                edit_flag = value['pse_profile_edit_flag']
            except KeyError:
                print("'pse_profile_edit_flag' key not found in pse dictionary.")
                edit_flag = False

            get_pse_profile = self.get_select_element_port_type(element)
            if get_pse_profile:
                self.utils.print_info("Click - > Open dropbox")
                self.auto_actions.click(get_pse_profile)
                more_button_times_found = 0
                while self.get_select_element_port_type('pse_more_button'):
                    more_button_times_found += 1
                    self.utils.print_info(f"'More' button present {more_button_times_found} times in PSE dropdown. "
                                          "Scrolling down...")
                    try:
                        def _check_stale_element_exception_more_button():
                            try:
                                self.auto_actions.move_to_element(self.get_select_element_port_type('pse_more_button'))
                                self.utils.print_info("move to element ",more_button_times_found)
                                self.screen.save_screen_shot()
                                return True
                            except StaleElementReferenceException as e:
                                self.utils.print_info("Scrolling to 'More' button failed. Stale element exception "
                                                      f"error detected {e} ; Retrying...")
                                return False

                        self.utils.wait_till(_check_stale_element_exception_more_button, is_logging_enabled=True,
                                             msg="Waiting for StaleElementException to dissapear...")
                        self.utils.print_info("Clicking 'More' button...")
                        self.auto_actions.click(self.get_select_element_port_type('pse_more_button'))
                        self.screen.save_screen_shot()
                    except ElementNotInteractableException as e:
                        self.utils.print_info(f"Element not interactable error: {e} ; Element is inactive! "
                                              "Breaking loop. \n\nNOTE: If 'More' button is visible and active, but "
                                              "still getting: ElementNotInteractable error ; "
                                              "check that the CSS_SELECTOR is correct.")
                        break

                sleep(2)
                get_pse_profile_items = self.get_select_element_port_type("pse_profile_items")
                pse_profile_name = value['pse_profile_name']

                if self.auto_actions.select_drop_down_options(get_pse_profile_items, pse_profile_name):
                    self.utils.print_info(" Selected into dropdown value : ", pse_profile_name)

                    if edit_flag:
                        self.utils.print_info(f"Editing PSE profile {value['pse_profile_name']}")
                        get_pse_profile_edit_button = self.get_select_element_port_type("pse_profile_edit")
                        if get_pse_profile_edit_button:
                            self.utils.print_info("Found pse profile edit button!")
                            self.auto_actions.click(get_pse_profile_edit_button)
                        else:
                            self.utils.print_info("get_pse_profile_edit_button not found ")
                            return -1
                        if not self.fill_in_pse_profile_fields(value) == 1:
                            return -1
                    return 1

                elif edit_flag:
                    self.utils.print_info(f"Edit flag is: {edit_flag}")
                    self.utils.print_info(f"PSE profile: {value['pse_profile_name']} not found in the dropdown items. "
                                          "Cannot edit non-exisiting PSE profile. Make sure 'More' button is clicked."
                                          "Closing dialog box...")
                    close_dialog_box = self.get_close_port_type_dialog_box()
                    if close_dialog_box:
                        self.utils.print_info("Found 'close dialog' button. Clicking...")
                        self.auto_actions.click(close_dialog_box)
                    else:
                        self.utils.print_info("Cannot find 'close dialog' button...")
                    return -1

                else:
                    self.utils.print_info(
                        f"PSE profile: {value['pse_profile_name']} not found in the dropdown items. "
                        "Closing dropdown...")

                    self.auto_actions.click(get_pse_profile)
                    get_pse_profile_add = self.get_select_element_port_type("pse_profile_add")
                    if get_pse_profile_add:
                        self.auto_actions.click(get_pse_profile_add)
                        if not self.fill_in_pse_profile_fields(value) == 1:
                            return -1
                    else:
                        self.utils.print_info("get_pse_profile_add not found ")
                    return 1
            else:
                self.utils.print_info("get_pse_profile not found ")
        elif element.lower() == "poe status":
            sleep(10)
            get_poe_status = self.get_select_element_port_type('poe status')
            print('Found POE_Status button: ', get_poe_status)
            sleep(5)
            if get_poe_status:
                sleep(5)
                self.auto_actions.click(get_poe_status)
                return 1
            else:
                print("Could not find POE Status!")

        self.utils.print_info(" Error when configure : ", element)
        return -1

    def d360_save_port_configuration(self, **kwargs):

        get_save_button = self.get_device360_configure_port_save_button()
        if get_save_button:
            self.auto_actions.click(get_save_button)
            self.utils.print_info("Saved port configuration ")
            kwargs['pass_msg'] = "Port Configuration Saved"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Save button not found on the page!"
            self.common_validation.failed(**kwargs)
            return -1

    def d360_save_port_configuration_all_switches(self):
        self.utils.print_info("Clicking 'Save Port Configuration' button'")
        self.auto_actions.click_reference(self.get_device360_device_configuration_save_button)

    def d360_cancel_port_configuration(self):
        self.utils.print_info("Exit the port configuration ")
        self.auto_actions.click_reference(self.get_device_d360_cancel_port_configuration)

    def d360_cancel_port_configuration_all_switches(self):
        self.utils.print_info("Exit the port configuration ")
        self.auto_actions.click_reference(self.get_d360_cancel_port_configuration)

    def device360_configure_ports_trunk_vlan(self, port_numbers="", trunk_native_vlan="", trunk_vlan_id="",
                                             port_type="Trunk Port", **kwargs):
        """
        - This keyword will configure multiple ports to Port Type: Trunk and assign a vlan value
        - Assume that already in device360 window
        - Flow: Configure --> Port Configuration--> interface --> Ports Usage and Vlan Range

        :param device_name: Device Name
        :param port_numbers: Port Number of the Switch
        :param trunk_native_vlan: Trunk Native Vlan Number for switch port
        :param trunk_vlan_id: The vlan values [Can be any value EX: single , range ]
        :param  port_type:  Trunk Port
        :return: 1 if Ports Usage Trunk and Vlan range Successfully configured else -1
        """

        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            for port_number in port_numbers.split(','):

                def _wait_for_port_row():
                    if self.device360_get_port_row(port_number):
                        return True
                    else:
                        return False

                self.utils.wait_till(_wait_for_port_row)

                port_row = self.device360_get_port_row(port_number)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)
                    self.utils.print_info("Click Port Usage drop down")
                    drop_down_button = self.get_device360_configure_port_usage_drop_down_button(port_row)
                    self.auto_actions.click(drop_down_button)
                    if self.get_device360_configure_port_usage_drop_down_options_presence(port_row):
                        pass
                    else:
                        self.auto_actions.click(drop_down_button)
                    self.utils.print_info("Selecting Port Usage")
                    self.auto_actions.select_drop_down_options(
                        self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                    self.utils.print_info("Entering Trunk Native Vlan TextField...")
                    self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                                                Keys.CONTROL + "a")
                    self.utils.print_info("Deleting the selected values in port..")
                    self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                                                Keys.BACK_SPACE)
                    self.utils.print_info("Entering Trunk Native Vlan in TextField...")
                    self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                                                trunk_native_vlan)
                    self.utils.print_info("Entering Trunk Allowed Vlan IDs TextField...")
                    self.utils.print_info("Deleting the selected values in port trunk textfield..")
                    self.auto_actions.send_keys(self.get_device360_configure_port_trunk_vlan_textfield(port_row),
                                                Keys.CONTROL + "a")
                    self.auto_actions.send_keys(self.get_device360_configure_port_trunk_vlan_textfield(port_row),
                                                Keys.BACK_SPACE)
                    self.auto_actions.send_keys(self.get_device360_configure_port_trunk_vlan_textfield(port_row),
                                                trunk_vlan_id)
                else:
                    self.utils.print_info("Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    kwargs['fail_msg'] = "Port Row Not Found"
                    self.common_validation.failed(**kwargs)
            self.select_configure_tab()
            save_btn = self.get_device360_configure_port_save_button()
            if save_btn:
                self.utils.print_info("Clicking 'Save Port Configuration' button'")
                self.auto_actions.click(save_btn)
                self.screen.save_screen_shot()
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['pass_msg'] = "Switch Port Configuration Saved"
                self.common_validation.passed(**kwargs)
                return 1
                # Needs to be debugged. Tooltip won't capture 'Switch Port Configuration Saved' message in D360

                # def check_for_confirmation():
                #     #tool_tip_text = tool_tip.tool_tip_text
                #     tool_tip_text = self.dialogue_web_elements.get_tooltip_text()
                #
                #     self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                #     if tool_tip_text:
                #         return 'Switch Port Configuration Saved' in tool_tip_text
                #     else:
                #         return False
                #
                # confirmation_message = self.utils.wait_till(check_for_confirmation, is_logging_enabled=True)[0]
                # self.utils.print_info("Close Dialogue Window")
                # self.auto_actions.click_reference(self.get_close_dialog)
                # if confirmation_message:
                #     kwargs['pass_msg'] = "Found confirmation message. Port Configuration Saved"
                #     self.common_validation.passed(**kwargs)
                #     return 1
                # else:
                #     kwargs['fail_msg'] = "Confirmation message not found."
                #     self.screen.save_screen_shot()
                #     self.common_validation.failed(**kwargs)
                #     return -1
        else:
            self.utils.print_info("Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_configure_ports_trunk_stack(self, port_numbers="", trunk_native_vlan="", trunk_vlan_id="", slot="",
                                              port_type="Trunk Port", **kwargs):
        """
        - This keyword will configure multiple ports to Port Type: Trunk and assign a vlan value for a slot
        - Flow: Device 360 Window --> Configure --> Port Configuration--> interface --> Ports Usage and Vlan Range
        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :param port_number: Port Number of the Switch
        :param trunk_native_vlan: Trunk Native Vlan Number for switch port
        :param trunk_vlan_id: The vlan values [Can be any value EX: single , range ]
        :param port_type:  Trunk Port
        :param slot: The current slot of the stack
        :return: 1 if Ports Usage Trunk and Vlan range Successfully configured else -1
        """
        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            for port_number in port_numbers.split(','):
                port_row = self.device360_get_port_row(str(slot) + ':' + port_number)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)
                    self.utils.print_info("Click Port Usage drop down")
                    drop_down_button = self.get_device360_configure_port_usage_drop_down_button(port_row)
                    self.auto_actions.click(drop_down_button)
                    if self.get_device360_configure_port_usage_drop_down_options_presence(port_row):
                        pass
                    else:
                        self.auto_actions.click(drop_down_button)

                    self.auto_actions.select_drop_down_options(
                        self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                    self.utils.print_info("Entering Trunk Native Vlan TextField...")
                    self.auto_actions.send_keys(
                        self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                        Keys.CONTROL + "a")
                    self.utils.print_info("Deleting the selected values in port..")
                    self.auto_actions.send_keys(
                        self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                        Keys.BACK_SPACE)
                    self.utils.print_info(f"Inserting native vlan value: {trunk_native_vlan} ...")
                    self.auto_actions.send_keys(
                        self.get_device360_configure_port_trunk_native_vlan_textfield(port_row),
                        trunk_native_vlan)
                    self.utils.print_info("Selecting the actual allowed vlans values...")
                    self.auto_actions.send_keys(
                        self.get_device360_configure_port_trunk_vlan_textfield(port_row),
                        Keys.CONTROL + "a")
                    self.utils.print_info("Deleting the actual allowed vlans values...")
                    self.auto_actions.send_keys(
                        self.get_device360_configure_port_trunk_vlan_textfield(port_row),
                        Keys.BACK_SPACE)
                    self.utils.print_info("Entering allowed vlans values in allowed vlans textfield...")
                    element = self.get_device360_configure_port_trunk_vlan_textfield(port_row)
                    element.send_keys(trunk_vlan_id)
                else:
                    self.utils.print_info("Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    kwargs['fail_msg'] = "Port Row was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
            self.select_configure_tab()
            save_btn = self.get_device360_configure_port_save_button()
            if save_btn:
                self.utils.print_info("Clicking 'Save Port Configuration' button'")
                self.auto_actions.click(save_btn)
                self.screen.save_screen_shot()
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['pass_msg'] = "Stack Port Configuration Saved"
                self.common_validation.passed(**kwargs)
                return 1
                # Needs to be debugged. Tooltip won't capture 'Switch Port Configuration Saved' message in D360
                # def check_for_confirmation():
                #     tool_tip_text = tool_tip.tool_tip_text
                #     self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                #     if tool_tip_text:
                #         return 'Stack Port Configuration Saved' in tool_tip_text
                #
                # confirmation_message = self.utils.wait_till(check_for_confirmation, is_logging_enabled=True)[0]
                # if confirmation_message:
                #     kwargs['pass_msg'] = "Found confirmation message. Port Configuration Saved."
                #     self.common_validation.passed(**kwargs)
                #     return 1
                # else:
                #     kwargs['fail_msg'] = "Confirmation message not found."
                #     self.screen.save_screen_shot()
                #     self.common_validation.failed(**kwargs)
                #     return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_ports_access_vlan(self, device_mac="", device_name="", port_numbers="", access_vlan_id="",
                                              port_type="Access Port", **kwargs):
        """
        - This keyword will configure multiple ports to the port type "Access Port"
        - Flow: Click Device -->Device 360 Window --> Configure --> Port Configuration--> interface -->
                Ports Usage and Vlan

        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :param port_numbers: Port Numbers of the Switch [written as: "1,2,3..."]
        :param access_vlan_id: Access Vlan Number for switch port
        :param  port_type:  Access Port
        :return: 1 if Ports Usage Access and Vlan Successfully configured else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)

        self.utils.print_info("Click Port Configuration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            for port_number in port_numbers.split(','):

                def _wait_for_port_row():
                    if self.device360_get_port_row(port_number):
                        return True
                    else:
                        return False

                self.utils.wait_till(_wait_for_port_row)

                port_row = self.device360_get_port_row(port_number)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)
                    self.utils.print_info("click Port Usage drop down")
                    drop_down_button = self.get_device360_configure_port_usage_drop_down_button(port_row)
                    self.auto_actions.click(drop_down_button)
                    if self.get_device360_configure_port_usage_drop_down_options_presence(port_row):
                        pass
                    else:
                        self.auto_actions.click(drop_down_button)

                    self.utils.print_info("Selecting Port Usage")
                    self.auto_actions.select_drop_down_options(
                        self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                    self.utils.print_info("Entering Search String...")
                    self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                                Keys.CONTROL + "a")
                    self.utils.print_info("Deleting the selected values in port..")
                    self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                                Keys.BACK_SPACE)
                    self.utils.print_info("Inserting the access vlan id..")
                    self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                                access_vlan_id)
                    self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    kwargs['fail_msg'] = "Port Row was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
            self.select_configure_tab()
            save_btn = self.get_device360_configure_port_save_button()
            if save_btn:
                self.utils.print_info("Clicking 'Save Port Configuration' button'")
                self.auto_actions.click(save_btn)
                self.screen.save_screen_shot()
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['pass_msg'] = "Switch Port Configuration Saved"
                self.common_validation.passed(**kwargs)
                return 1
                # Needs to be debugged. Tooltip won't capture 'Switch Port Configuration Saved' message in D360
                # def check_for_confirmation():
                #     tool_tip_text = tool_tip.tool_tip_text
                #     self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                #     if tool_tip_text:
                #         return 'Switch Port Configuration Saved' in tool_tip_text
                #     else:
                #         return False
                #
                # confirmation_message = self.utils.wait_till(check_for_confirmation, is_logging_enabled=True)[0]
                # if confirmation_message:
                #     kwargs['pass_msg'] = "Found confirmation message. Port Configuration Saved"
                #     self.common_validation.passed(**kwargs)
                #     return 1
                # else:
                #     kwargs['fail_msg'] = "Confirmation message not found."
                #     self.screen.save_screen_shot()
                #     self.common_validation.failed(**kwargs)
                #     return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_ports_access_vlan_stack(self, port_numbers="", access_vlan_id="1", slot="",
                                                    port_type="Access Port", **kwargs):
        """
        - This keyword will configure multiple ports to the port type "Access Port"
        - Assume that already in Device 360 Window
        - Flow: Configure --> Port Configuration--> interface --> Ports Usage and Vlan

        :param port_numbers: Port Numbers of the Switch [written as: "1,2,3..."]
        :param access_vlan_id: Access Vlan Number for switch port
        :param slot: The slot of the stack
        :param port_type:  Access Port
        :return: 1 if Ports Usage Access and Vlan Successfully configured else -1
        """
        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device360_configure_button)
        self.utils.print_info("Click Port Configuration Button")
        self.auto_actions.click_reference(self.get_device360_configure_port_configuration_button)
        port_conf_content = self.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            for port_number in port_numbers.split(','):
                port_row = self.device360_get_port_row(str(slot) + ':' + port_number)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)
                    self.utils.print_info("Click Port Usage drop down")
                    drop_down_button = self.get_device360_configure_port_usage_drop_down_button(port_row)
                    self.auto_actions.click(drop_down_button)
                    if self.get_device360_configure_port_usage_drop_down_options_presence(port_row):
                        pass
                    else:
                        self.auto_actions.click(drop_down_button)
                    self.auto_actions.select_drop_down_options(
                        self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                    self.utils.print_info("Entering Search String...")
                    self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                                Keys.CONTROL + "a")
                    self.utils.print_info("Deleting the selected values in port..")
                    self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                                Keys.BACK_SPACE)
                    self.utils.print_info("Inserting the access vlan id..")
                    self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row),
                                                access_vlan_id)
                    self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click_reference(self.get_close_dialog)
                    kwargs['fail_msg'] = "Port Row was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
            self.select_configure_tab()
            save_btn = self.get_device360_configure_port_save_button()
            if save_btn:
                self.utils.print_info("Clicking 'Save Port Configuration' button'")
                self.auto_actions.click(save_btn)
                self.screen.save_screen_shot()
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click_reference(self.get_close_dialog)
                kwargs['pass_msg'] = "Stack Port Configuration Saved"
                self.common_validation.passed(**kwargs)
                return 1
                # Needs to be debugged. Tooltip won't capture 'Switch Port Configuration Saved' message in D360
                # def check_for_confirmation():
                #     tool_tip_text = tool_tip.tool_tip_text
                #     self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                #     if tool_tip_text:
                #         return 'Stack Port Configuration Saved' in tool_tip_text
                #     else:
                #         return False
                #
                # confirmation_message = self.utils.wait_till(check_for_confirmation, is_logging_enabled=True)[0]
                # if confirmation_message:
                #     kwargs['pass_msg'] = "Found confirmation message. Port Configuration Saved."
                #     self.common_validation.passed(**kwargs)
                #     return 1
                # else:
                #     kwargs['fail_msg'] = "Confirmation message not found."
                #     self.screen.save_screen_shot()
                #     self.common_validation.failed(**kwargs)
                #     return -1
        else:
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.common_validation.fault(**kwargs)
            return -1

    def select_stack_unit(self, slot, **kwargs):
        """
        This keyword will select a slot from a stack in Device360
        :param slot: The slot which will be selected
        :return: 1 if the slot was selected; else -1
        """

        def _check_dropdown():
            if self.dev360.get_device360_port_configuration_stack_units_dropdown():
                return True
            else:
                return False

        self.utils.wait_till(_check_dropdown)
        self.auto_actions.click_reference(self.dev360.get_device360_port_configuration_stack_units_dropdown)

        self.utils.print_info("Gather the list of the devices in the stack")
        slot_found = False

        slots_in_stack = self.dev360.get_device360_port_configuration_stack_units_rows()
        if slots_in_stack:
            for stack_item in slots_in_stack:
                if "Unit " + str(slot) in stack_item.text:
                    self.utils.print_info(f"Slot {str(slot)} found in the stack, selecting the slot")
                    self.auto_actions.click(stack_item)
                    slot_found = True
                    kwargs['pass_msg'] = f"Selected the slot {str(slot)} successfully"
                    self.common_validation.passed(**kwargs)
                    return 1
            if not slot_found:
                kwargs['fail_msg'] = f"Unable to locate slot {str(slot)}"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to gather the list of the slots for the stack"
            self.common_validation.fault(**kwargs)
            return -1

    def device360_configure_poe_threshold_value_stack(self, threshold_value, slot, device_mac="", device_name="",
                                                      **kwargs):
        """
        - This keyword will configure the POE threshold value in Device 360
        - Flow: Click Device --> Device 360 Window --> Port Configuration --> PSE --> PSE SETTINGS FOR DEVICE
        - Keyword Usage:
        - ``Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}  slot=${SLOT} device_mac=${DEVICE_MAC}``
        - ``Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}  slot=${SLOT}  device_name=${DEVICE_NAME}``
        :param threshold_value: value for threshold between 1 and 99
        :param slot: The slot which supported POE
        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :return: 1 if value was configured successfully , else -1
        """
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
        self.select_configure_tab()
        self.select_port_configuration_view()
        self.select_stack_unit(slot=slot)
        sleep(2)
        
        self.unlock_device360_port_config()
        sleep(2)
        
        self.utils.print_info("Click PSE Tab")
        self.auto_actions.click_reference(self.get_device360_port_config_pse_tab_slot_stack)
        sleep(2)
        pse_settings_for_device_button = self.get_device360_pse_settings_for_device_button_stack()
        if pse_settings_for_device_button:
            self.utils.print_info("Click on PSE settings for device")
            self.auto_actions.click(pse_settings_for_device_button)
        else:
            kwargs['fail_msg'] = "PSE settings for device button not found "
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        edit_threshold_poe = self.get_device360_edit_threshold_poe_stack()
        self.utils.print_info("Editing threshold value")
        self.auto_actions.send_keys(edit_threshold_poe, Keys.CONTROL + "a" + Keys.BACK_SPACE)
        threshold_value_int = int(threshold_value)
        if 1 <= threshold_value_int <= 99:
            self.utils.print_info("Sending threshold {} % value".format(threshold_value))
            self.auto_actions.send_keys(edit_threshold_poe, threshold_value)
            self.screen.save_screen_shot()
        else:
            kwargs['fail_msg'] = "Value needs to be between 1 and 99"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)
        save_threshold_poe = self.get_device360_save_threshold_poe_value_stack()
        if save_threshold_poe:
            self.utils.print_info("Saving threshold {} % ".format(threshold_value))
            self.auto_actions.click(save_threshold_poe)
        else:
            kwargs['fail_msg'] = "Save button not found"
            self.common_validation.fault(**kwargs)
            return -1
        self.select_configure_tab()
        sleep(2)
        save_btn = self.get_device360_configure_port_save_button_stack()
        if save_btn:
            self.utils.print_info("Clicking 'Save Port Configuration' button'")
            self.auto_actions.click(save_btn)
        else:
            kwargs['fail_msg'] = "Could not click Save button"
            self.common_validation.fault(**kwargs)
            return -1
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        kwargs['pass_msg'] = "The value was configured successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_power_details_stack(self, slot, device_mac="", device_name="", **kwargs):
        """
        - This keyword will get Power Supply Details in Device 360 from thunderbolt icon
        - Flow: Click Device -->Device 360 Window -->Thunderbolt ICON
        - Keyword Usage:
        - ``Device360 Power Details      device_mac=${DEVICE_MAC}``
        - ``Device360 Power Details      device_name=${DEVICE_NAME}``
        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :return: list with power supply details; else -1
        """
        rez = None
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
        slot_index = 1
        slot_found = False
        self.utils.wait_till(self.get_device360_stack_overview_slot_details_rows, timeout=120, is_logging_enabled=True,
                             delay=5)
        self.screen.save_screen_shot()
        slot_details_overview = self.get_device360_stack_overview_slot_details_rows()
        if slot_details_overview:
            power_elements = self.dev360.get_device360_thunderbold_icon_stack(slot_details_overview)
            for power_item in power_elements:
                if slot_index == int(slot):
                    self.utils.print_info("Slot " + str(slot) + " found in the stack, selecting the slot")
                    self.screen.save_screen_shot()
                    self.auto_actions.click_and_hold_element(power_item)
                    sleep(2)
                    self.auto_actions.move_to_element(power_item)
                    self.screen.save_screen_shot()
                    slot_found = True
                    break
                slot_index = slot_index + 1
            if not slot_found:
                kwargs['fail_msg'] = "Unable to locate the correct slot"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Power details not found"
            self.common_validation.failed(**kwargs)
            return -1
        sleep(2)
        power_details = self.dev360.get_device360_power_details()
        if power_details:
            self.utils.print_info(f"{power_details.text}")
            rez = power_details.text
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
        else:
            kwargs['fail_msg'] = "Power details not found"
            self.common_validation.failed(**kwargs)
            return -1
            
        kwargs['pass_msg'] = "Got Power Supply Details in Device 360 from thunderbolt icon"
        self.common_validation.passed(**kwargs)
        return rez

    def _is_device360_relaunch_digital_twin_button_visible(self, **kwargs):
        """
        - This keyword checks if the 'Relaunch Digital Twin' button is visible in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Is Device360 Relaunch Digital Twin Button Visible``
        :return: True if visible, False if not visible, else -1
        """
        relaunch_link = self.dev360.get_device360_digital_twin_relaunch_button()
        if relaunch_link:
            hidden = relaunch_link.get_attribute("class")
            self.utils.print_debug(f"'Relaunch Digital Twin' button Class value: {hidden}")
            if "fn-hidden" in hidden:
                kwargs['fail_msg'] = "The 'Relaunch Digital Twin' button is not displayed."
                self.common_validation.failed(expect_error=True)
                return False
            else:
                kwargs['pass_msg'] = "The 'Relaunch Digital Twin' button is displayed."
                self.common_validation.passed(**kwargs)
                return True
        else:
            self.utils.print_info("Could not find the 'Relaunch Digital Twin' button.")

        kwargs['fail_msg'] = "Could not find the 'Relaunch Digital Twin' button "
        self.common_validation.fault(**kwargs)
        return -1

    def verify_device360_relaunch_digital_twin_button_visible(self, **kwargs):
        """
        - This keyword verifies if the 'Relaunch Digital Twin' button is visible in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Verify Device360 Relaunch Digital Twin Button Visible``
        :return: True if visible, False if not visible, else -1
        """
        return self._is_device360_relaunch_digital_twin_button_visible(**kwargs)

    def verify_device360_relaunch_digital_twin_button_hidden(self, **kwargs):
        """
        - This keyword verifies if the 'Relaunch Digital Twin' button is hidden in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Verify Device360 Relaunch Digital Twin Button Hidden``
        :return: True if visible, False if not visible, else -1
        """
        return self._is_device360_relaunch_digital_twin_button_visible(**kwargs)

    def device360_relaunch_digital_twin_device(self, confirm="yes", **kwargs):
        """
        - This keyword clicks the 'Relaunch Digital Twin' button in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Device360 Relaunch Digital Twin Device   confirm="no"``
        :param confirm: Click Yes or No button within the confirmation panel
        :return: 1 if action was successful, else -1
        """
        relaunch_button = self.dev360.get_device360_digital_twin_relaunch_button()
        if relaunch_button:
            hidden = relaunch_button.get_attribute("class")
            self.utils.print_info(f"'Relaunch Digital Twin' button Class value: {hidden}")
            if "fn-hidden" in hidden:
                kwargs['fail_msg'] = "The 'Relaunch Digital Twin' button is not displayed"
                self.common_validation.fault(**kwargs)
                return -1
            else:
                self.utils.print_info("Clicking the 'Relaunch Digital Twin' button.")
                self.auto_actions.click(relaunch_button)
                if confirm.lower() == 'yes':
                    sleep(3)
                    self.screen.save_screen_shot()
                    self.auto_actions.click_reference(self.dialog_web_elements.get_confirm_yes_button)
                    self.utils.print_info("Confirming the relaunch.")
                    banner_text_error = self.devices_web_elements.get_ui_banner_error_message()
                    if banner_text_error:
                        self.utils.print_info(banner_text_error.text)
                        kwargs['fail_msg'] = f"{banner_text_error}"
                        self.common_validation.fault(**kwargs)
                        return -1

                    kwargs['pass_msg'] = "Clicked on the 'Relaunch Digital Twin' button."
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.auto_actions.click_reference(self.dialog_web_elements.get_confirm_cancel_button)
                    kwargs['pass_msg'] = "Clicked on the 'Relaunch Digital Twin' button."
                    self.common_validation.passed(**kwargs)
                    return 1
        else:
            self.utils.print_info("Could not find the 'Relaunch Digital Twin' button.")

        kwargs['fail_msg'] = "The 'Relaunch Digital Twin' button is not displayed"
        self.common_validation.fault(**kwargs)
        return -1

    def _is_device360_shutdown_digital_twin_button_visible(self, **kwargs):
        """
        - This keyword checks if the 'Shutdown Digital Twin' button is visible in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Is Device360 Shutdown Digital Twin Button Visible``
        :return: True if visible, False if not visible, else -1
        """
        shutdown_link = self.dev360.get_device360_digital_twin_shutdown_button()
        if shutdown_link:
            hidden = shutdown_link.get_attribute("class")
            self.utils.print_debug(f"'Shutdown Digital Twin' button Class value: {hidden}")
            if "fn-hidden" in hidden:
                kwargs['fail_msg'] = "The 'Shutdown Digital Twin' button is not displayed."
                self.common_validation.failed(expect_error=True)
                return False
            else:
                kwargs['pass_msg'] = "The 'Shutdown Digital Twin' button is displayed."
                self.common_validation.passed(**kwargs)
                return True
        else:
            self.utils.print_info("Could not find the 'Shutdown Digital Twin' button.")

        kwargs['fail_msg'] = "Could not find the 'Shutdown Digital Twin' button "
        self.common_validation.fault(**kwargs)
        return -1

    def verify_device360_shutdown_digital_twin_button_visible(self, **kwargs):
        """
        - This keyword verifies if the 'Relaunch Digital Twin' button is visible in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Verify Device360 Shutdown Digital Twin Button Visible``
        :return: True if visible, False if not visible, else -1
        """
        return self._is_device360_shutdown_digital_twin_button_visible(**kwargs)

    def verify_device360_shutdown_digital_twin_button_hidden(self, **kwargs):
        """
        - This keyword verifies if the 'Relaunch Digital Twin' button is hidden in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Verify Device360 Shutdown Digital Twin Button Hidden``
        :return: True if visible, False if not visible, else -1
        """
        return self._is_device360_shutdown_digital_twin_button_visible(**kwargs)

    def device360_shutdown_digital_twin_device(self, confirm="yes", **kwargs):
        """
        - This keyword clicks the 'Shutdown Digital Twin' button in the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Device360 Shutdown Digital Twin Device   confirm="no"``
        :param confirm: Click Yes or No button within the confirmation panel
        :return: 1 if action was successful, else -1
        """
        shutdown_button = self.dev360.get_device360_digital_twin_shutdown_button()
        if shutdown_button:
            hidden = shutdown_button.get_attribute("class")
            self.utils.print_info(f"'Shutdown Digital Twin' button Class value: {hidden}")
            if "fn-hidden" in hidden:
                self.utils.print_info("The 'Shutdown Digital Twin' button is not displayed.")
                kwargs['fail_msg'] = "The 'Shutdown Digital Twin' button " \
                                     "is not displayed "
                self.common_validation.failed(**kwargs)
                return -1
            else:
                self.utils.print_info("Clicking the 'Shutdown Digital Twin' button.")
                self.auto_actions.click(shutdown_button)
                if confirm.lower() == 'yes':
                    sleep(3)
                    self.screen.save_screen_shot()
                    self.auto_actions.click_reference(self.dialog_web_elements.get_confirm_yes_button)
                    self.utils.print_info("Confirming the shutdown.")
                    banner_text_error = self.devices_web_elements.get_ui_banner_error_message()
                    if banner_text_error:
                        self.utils.print_info(banner_text_error.text)
                        kwargs['fail_msg'] = f"{banner_text_error.text}"
                        self.common_validation.fault(**kwargs)
                        return -1
                    kwargs['pass_msg'] = "Clicked the 'Shutdown Digital Twin' button"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.auto_actions.click_reference(self.dialog_web_elements.get_confirm_cancel_button)
                    kwargs['pass_msg'] = "Clicked the 'Shutdown Digital Twin' button"
                    self.common_validation.passed(**kwargs)
                    return 1
        else:
            self.utils.print_info("Could not find the 'Shutdown Digital Twin' button.")

        kwargs['fail_msg'] = "Could not find the 'Shutdown Digital Twin' button"
        self.common_validation.fault(**kwargs)
        return -1

    def get_device360_digital_twin_device_status(self, **kwargs):
        """
        - This keyword obtains the Digital Twin status icon within the Device 360 view.
        - It is assumed that the Device 360 window is already opened for the Digital Twin.
        - Keyword Usage
        - ``Get Device360 Digital Twin Device Status``
        :return:
            'connected' if Device Status icon is 'Digital Twin' and status is 'connected'
            'disconnected' if Device Status icon is 'Digital Twin' and status is 'disconnected'
            'unknown' if Device Status icon is not 'Digital Twin' and status is 'unknown'
            'error' if Device Status icon is not 'Digital Twin'
        """
        status_icon = self.get_device360_digital_twin_status_icon().get_attribute("class")
        if status_icon:
            self.utils.print_info(f"Status Icon class value: {status_icon}")
            self.screen.save_screen_shot()
            if "dt-icon" in status_icon:
                #  vv 22R5 Device360 UI Issue, not seen in 22R6
                if "hive-status-true hive-status-false" in status_icon:
                    return 'disconnected'
                if "hive-status-false hive-status-true" in status_icon:
                    return 'connected'
                #  ^^ 22R5 Device360 UI issue, not seen in 22R6
                if "hive-status-true" in status_icon:
                    return 'connected'
                elif "hive-status-false" in status_icon:
                    return 'disconnected'
                else:
                    return 'unknown'
            else:
                self.utils.print_info("Unable to determine Device Status icon.")
                kwargs['fail_msg'] = "Unable to determine Device Status icon"
                self.common_validation.fault(**kwargs)
                return 'error'
        else:
            self.utils.print_info("Digital Twin Status icon could not be found.")

        kwargs['fail_msg'] = "Digital Twin Status icon could not be found"
        self.common_validation.fault(**kwargs)
        return 'error'

    def device360_wait_until_device_online(self, retry_duration=30, retry_count=20, **kwargs):
        """
        - This keyword waits till the device status updates to connected in the XIQ Device 360 view.
        - This keyword by default loops every 30 seconds for 20 times to check the device status.
        - It is assumed that the Device 360 window is already opened for the Device.
        - Keyword Usage:
        - ``Device360 Wait Until Device Online       retry_duration=10       retry_count=12``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device connected within time else -1
        """
        count = 1

        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Device Online Status Check - Loop: {count}")
                    sleep(retry_duration)
                    self.utils.print_info(f"Time elapsed for device status check: {retry_duration} seconds")
                    self.device360_refresh_page()

                    connected_text = self.get_sidebar_connected_state().text
                    self.utils.print_info(f"Connected_el: {connected_text}")

                    if connected_text:
                        if "Disconnected" in connected_text:
                            self.utils.print_info(
                                f"Device status is disconnected. Waiting for {retry_duration} seconds")
                        elif "Connected" in connected_text:
                            kwargs['pass_msg'] = "Device status is connected!"
                            self.common_validation.passed(**kwargs)
                            return 1
                    else:
                        self.utils.print_info("Could not obtain text string for the Connection Status field.")
                        return -1
                    count += 1
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        kwargs['fail_msg'] = "Device failed to come ONLINE. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def device360_wait_until_device_offline(self, retry_duration=30, retry_count=20, **kwargs):
        """
        - This keyword waits till the device status updates to disconnected in the XIQ Device 360 view.
        - This keyword by default loops every 30 seconds for 20 times to check the device status.
        - It is assumed that the Device 360 window is already opened for the Device.
        - Keyword Usage:
        - ``Device360 Wait Until Device Offline       retry_duration=10       retry_count=12``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device connected within time else -1
        """
        count = 1

        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Device Offline Status Check - Loop: {count}")
                    sleep(retry_duration)
                    self.utils.print_info(f"Time elapsed for device status check: {retry_duration} seconds")
                    self.device360_refresh_page()

                    connected_text = self.get_sidebar_connected_state().text
                    self.utils.print_info(f"Connected_el: {connected_text}")

                    if connected_text:
                        if "Connected" in connected_text:
                            self.utils.print_info(f"Device status is connected. Waiting for {retry_duration} seconds")
                        elif "Disconnected" in connected_text:
                            kwargs['pass_msg'] = "Device status is disconnected!"
                            self.common_validation.passed(**kwargs)
                            return 1
                    else:
                        self.utils.print_info("Could not obtain text string for the Connection Status field.")
                        return -1
                    count += 1
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        kwargs['fail_msg'] = "Device failed to go OFFLINE. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def create_port_type_with_stp_settings(self, switch_port, port_type_name, path_cost, description=None, status=None,
                                           port_usage="access", priority=None, bpdu_protection=None, stp_enabled=None,
                                           edge_port=None, device_360=False, save=True, **kwargs):
        """ This function creates a port type with custom STP settings at device or template level.

        The only mandatory arguments are switch_port, port_type_name and path_cost. All the other arguments are optional.

        The function will return a tuple that contains the status of the function and the summary of the newly created port type.

        args:
            :switch_port:        str  - the name of the port
            :port_type_name:     str  - the name of the port type
            :path_cost:          int  - the value of path cost

        kwargs:
            :description:        str  - the description|None for no action
            :status:             bool - True for enabled|False for disabled|None for no action
            :port_usage:         str  - "access"|"trunk"|None for no action
            :priority:           int  - 0, 16, 32, ...|None for no action
            :bpdu_protection:    str  - "Disabled"|"Guard"|None for no action
            :stp_enabled:        bool - True for enabled|False for disabled|None for no action
            :edge_port:          bool - True for enabled|False for disabled|None for no action
            :device_360:         bool - True for device level|False for template level
            :save:               bool - True for saving the port type at the end|False for not saving

        return: if the function succeeds it will return (1, {...})
                if the function fails it will return (-1, {})

        usage:

            status, summary = self.xiq.xflowsmanageDevice360.create_port_type_with_stp_settings(
                1, "testing_port_type_1", 1111, description="description", status=True,
                port_usage="access", priority=64, bpdu_protection="Disabled", stp_enabled=True, edge_port=True)
            >>> status
            1
            >>> summary
            {'STP': 'Enabled', 'Edge Port': 'Enabled', 'BPDU Protection': 'Disabled', 'Priority': '64', 'Path Cost': '1111'}
            >>>
        """
        if not device_360:
            rows = self.get_policy_configure_port_rows()
            if not rows:
                self.utils.print_info("Could not obtain list of port rows")
                kwargs['fail_msg'] = "Could not obtain list of port rows"
                self.common_validation.fault(**kwargs)
                return -1, {}
            else:
                for row in rows:
                    if re.search(f'{switch_port}\n', row.text):
                        d360_create_port_type = self.get_d360_create_port_type(row)

                        if d360_create_port_type:
                            self.utils.print_info("The button d360_create_port_type from policy was found")
                            self.auto_actions.click(d360_create_port_type)
                            sleep(10)
                            break
                        else:
                            kwargs['fail_msg'] = "The button d360_create_port_type from policy was not found "
                            self.common_validation.fault(**kwargs)
                            return -1, {}
                else:
                    kwargs['fail_msg'] = "The button d360_create_port_type from policy was not found "
                    self.common_validation.fault(**kwargs)
                    return -1, {}
        else:
            port_conf_content = self.get_device360_port_configuration_content()
            if port_conf_content:
                port_row = self.device360_get_port_row(switch_port)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)

                    d360_create_port_type = self.get_d360_create_port_type(port_row)
                    if d360_create_port_type:
                        self.utils.print_info("The button d360_create_port_type was found")
                        self.auto_actions.click(d360_create_port_type)
                        sleep(2)
                    else:
                        kwargs['fail_msg'] = "The button d360_create_port_type from policy was not found "
                        self.common_validation.fault(**kwargs)
                        return -1, {}
                else:
                    kwargs['fail_msg'] = "The button d360_create_port_type from policy was not found. Port wasn't found"
                    self.common_validation.failed(**kwargs)
                    return -1, {}
            else:
                kwargs['fail_msg'] = "Couldn't get the port"
                self.common_validation.failed(**kwargs)
                return -1, {}

        name_element = self.get_select_element_port_type("name")
        if not name_element:
            kwargs['fail_msg'] = "Port name element was not found"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if self.auto_actions.send_keys(name_element, port_type_name) == 1:
            self.utils.print_info("Successfully configured the name field")
            sleep(2)
        else:
            kwargs['fail_msg'] = "Failed to configure the name field"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if description is not None:
            description_element = self.get_select_element_port_type("description")
            if not description_element:
                kwargs['fail_msg'] = "Port description element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.send_keys(description_element, description) == 1:
                self.utils.print_info("Successfully configured the description field")
                sleep(2)
            else:
                kwargs['fail_msg'] = "Failed to configure the description field"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if status is not None:
            status_element = self.get_select_element_port_type("status")
            if not status_element:
                kwargs['fail_msg'] = "Port status element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not status_element.is_selected() and status) or (
                    status_element.is_selected() and not status):

                if self.auto_actions.click(status_element) == 1:
                    self.utils.print_info("Successfully clicked on the status element")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the status element"
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        auto_sense = self.dev360.get_select_element_port_type("auto-sense")
        if auto_sense:
            if auto_sense.is_selected():
                if self.auto_actions.click(auto_sense) == 1:
                    self.utils.print_info("Successfully disabled the auto sense on chosen port")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to disable the auto sense on chosen port "
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        port_element = self.dev360.get_select_element_port_type("port usage", f"{port_usage} port")
        if not port_element:
            kwargs['fail_msg'] = f"{port_usage} port type element was not found"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if self.auto_actions.click(port_element) == 1:
            self.utils.print_info("Successfully chose the port usage field")
            sleep(2)
        else:
            kwargs['fail_msg'] = "Failed to chose the port usage field"
            self.common_validation.fault(**kwargs)
            return -1, {}

        self.utils.print_info("Go to the STP settings page")
        for _ in range(5):
            if "active" in self.get_select_element_port_type("stpPage").get_attribute("class"):
                break
            get_next_button = self.get_select_element_port_type("next_button")
            if get_next_button:
                if get_next_button.is_enabled():
                    self.auto_actions.click(get_next_button)
                    sleep(2)
                else:
                    break
            else:
                kwargs['fail_msg'] = "get_next_button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if stp_enabled is not None:
            stp_enabled_element = self.get_select_element_port_type("stp enable")

            if not stp_enabled_element:
                kwargs['fail_msg'] = "STP Enabled element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not stp_enabled_element.is_selected() and stp_enabled) or (
                stp_enabled_element.is_selected() and not stp_enabled):

                if self.auto_actions.click(stp_enabled_element) == 1:
                    self.utils.print_info("Successfully clicked on the STP enabled element")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the STP Enabled element "
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        if edge_port is not None:
            edge_port_element = self.get_select_element_port_type("edge port")

            if not edge_port_element:
                kwargs['fail_msg'] = "Edge Port element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not edge_port_element.is_selected() and edge_port) or (
                edge_port_element.is_selected() and not edge_port):

                if self.auto_actions.click(edge_port_element) == 1:
                    self.utils.print_info("Successfully clicked on the Edge Port element")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the Edge Port element "
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        if bpdu_protection is not None:
            bpdu_protection_element = self.get_select_element_port_type("bpdu protection")

            if not bpdu_protection_element:
                kwargs['fail_msg'] = "BPDU Protection element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(bpdu_protection_element) == 1:
                self.utils.print_info("Successfully clicked on the BPDU Protection element")
                sleep(5)
            else:
                self.utils.print_info("Successfully clicked on the BPDU Protection element")
                return -1, {}

            get_bpdu_protection_items = self.get_select_element_port_type("bpdu_protection_items")

            if not get_bpdu_protection_items:
                kwargs['fail_msg'] = "BPDU Protection list elements not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.select_drop_down_options(get_bpdu_protection_items, bpdu_protection):
                self.utils.print_info("Selected into dropdown value : ", bpdu_protection)
            else:
                kwargs['fail_msg'] = "Failed to select from BPDU Protection dropdown"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if path_cost is not None:
            path_cost_element = self.get_select_element_port_type("path cost")

            if not path_cost_element:
                kwargs['fail_msg'] = "Path Cost element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.send_keys(path_cost_element, str(path_cost)) == 1:
                self.utils.print_info("Successfully configured the path cost field")
                sleep(2)
            else:
                kwargs['fail_msg'] = "Failed to configure the path cost field"
                self.common_validation.fault(**kwargs)
                return -1, {}

        if priority:
            priority_element = self.get_select_element_port_type("priority")

            if not priority_element:
                kwargs['fail_msg'] = "Priority element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(priority_element) == 1:
                self.utils.print_info("Successfully clicked on the priority element")
                sleep(5)
            else:
                kwargs['fail_msg'] = "Failed to click on the priority element"
                self.common_validation.fault(**kwargs)
                return -1, {}

            get_priority_items = self.get_select_element_port_type("priority_items")
            if not get_priority_items:
                kwargs['fail_msg'] = "Priority dropdown elements not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.select_drop_down_options(get_priority_items, str(priority)):
                self.utils.print_info("Selected into dropdown value : ", priority)
            else:
                kwargs['fail_msg'] = "Failed to select item from priority dropdown"
                self.common_validation.fault(**kwargs)
                return -1, {}

        self.utils.print_info("Go to the last page")
        for _ in range(5):
            if "active" in self.get_select_element_port_type("summaryPage").get_attribute("class"):
                break
            get_next_button = self.get_select_element_port_type("next_button")
            if get_next_button:
                if get_next_button.is_enabled():
                    self.auto_actions.click(get_next_button)
                    sleep(2)
                else:
                    break
            else:
                kwargs['fail_msg'] = "get_next_button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

        summary = {}

        for row_name, row_value in zip(
            ["STP", "Edge Port", "BPDU Protection", "Priority", "Path Cost"],
            ["stp", "edge port", "bpdu protection", "priority", "path cost"]
        ):
            try:
                summary[row_name] = self.dev360.get_select_element_port_type_summary(row_value).text
            except Exception:
                summary[row_name] = ""

        if save:
            save_button = self.dev360.get_close_port_type_box()

            if not save_button:
                self.utils.print_info("save button not found")
                kwargs['fail_msg'] = "save button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(save_button) == 1:
                self.utils.print_info("Successfully clicked on the Save element")
            else:
                kwargs['fail_msg'] = "Failed to click on the Save element"
                self.common_validation.fault(**kwargs)
                return -1, {}

        return 1, summary

    def edit_stp_settings_in_honeycomb_port_editor(self, switch_port, port_type_name, status=None, stp_enabled=None,
                                                   edge_port=None, bpdu_protection=None, priority=None,
                                                   path_cost=None, save=True, **kwargs):
        """ This function edits a port type with custom STP settings at template level.

        The only mandatory arguments are switch_port, port_type_name and path_cost. All the other arguments are optional.

        The function will return a tuple that contains the status of the function and the summary of the newly created port type.

        args:
            :switch_port:        str   -   the name of the port
            :port_type_name:     str   -   the name of the port type

        kwargs:
            :description:        str   -   the description
            :status:             bool  -   True for enabled|False for disabled|None for no action
            :port_usage:         str   -   "access"|"trunk"|None for no action
            :priority:           int   -   0, 16, 32, ...|None for no action
            :bpdu_protection:    str   -   "Disabled"|"Guard"|None for no action
            :stp_enabled:        bool  -   True for enabled|False for disabled|None for no action
            :edge_port:          bool  -   True for enabled|False for disabled|None for no action
            :device_360:         bool  -   True for device level|False for template level
            :path_cost:          int   -   the value of path cost|None for no action
            :save:               bool  -   True for saving the port type at the end|False for not saving|None for no action

        return: if the function succeeds it will return (1, {...})
                if the function fails it will return (-1, {})

        return: if the function succeeds it will return (1, {...})
                if the function fails it will return (-1, {})

        usage:
            status, summary = self.xiq.xflowsmanageDevice360.edit_stp_settings_in_honeycomb_port_editor(
                "1/1", "testing_port_10", path_cost=2222, bpdu_protection="Guard"
            )

            status, summary = self.xiq.xflowsmanageDevice360.edit_stp_settings_in_honeycomb_port_editor(
                "1/1", "testing_port_10", bpdu_protection="Disabled"
            )

            status, summary = self.xiq.xflowsmanageDevice360.edit_stp_settings_in_honeycomb_port_editor(
                "1/1", "testing_port_10", priority=80, edge_port=False, stp_enabled=False
            )

            status, summary = self.xiq.xflowsmanageDevice360.edit_stp_settings_in_honeycomb_port_editor(
                "1/1", "testing_port_10", status=False, edge_port=True, stp_enabled=True
            )

            status, summary = self.xiq.xflowsmanageDevice360.edit_stp_settings_in_honeycomb_port_editor(
                "1/1", "testing_port_10", status=True
            )

        """
        rows = self.get_policy_configure_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
            kwargs['fail_msg'] = "Could not obtain list of port rows"
            self.common_validation.fault(**kwargs)
            return -1, {}
        else:
            for row in rows:
                if re.search(rf'{switch_port}\n{port_type_name}\n', row.text):
                    policy_edit_port_type = self.get_policy_edit_port_type(row)
                    if policy_edit_port_type:
                        self.utils.print_info("The button policy_edit_port_type from policy was found")
                        self.auto_actions.click(policy_edit_port_type)
                        sleep(10)
                        break
                    else:
                        kwargs['fail_msg'] = "The button policy_edit_port_type from policy was not found "
                        self.common_validation.fault(**kwargs)
                        return -1, {}
            else:
                kwargs['fail_msg'] = "The button policy_edit_port_type from policy was not found "
                self.common_validation.fault(**kwargs)
                return -1, {}

        if status is not None:

            usage_tab = self.get_select_element_port_type("usagePage")
            if not usage_tab:
                kwargs['fail_msg'] = "Failed to click the usage tab"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(usage_tab) == 1:
                self.utils.print_info("Successfully clicked the usage tab")
                sleep(2)
            else:
                kwargs['fail_msg'] = "Failed to click the usage tab"
                self.common_validation.fault(**kwargs)
                return -1, {}

            status_element = self.get_select_element_port_type("status")
            if not status_element:
                kwargs['fail_msg'] = "Port status element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not status_element.is_selected() and status) or (
                    status_element.is_selected() and not status):

                if self.auto_actions.click(status_element) == 1:
                    self.utils.print_info("Successfully clicked on the status element")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the status element "
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        stp_tab = self.get_select_element_port_type("stpPage")
        if not stp_tab:
            kwargs['fail_msg'] = "Failed to click the stp tab"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if self.auto_actions.click(stp_tab) == 1:
            self.utils.print_info("Successfully clicked the stp tab")
            sleep(2)
        else:
            kwargs['fail_msg'] = "Failed to click the stp tab"
            self.common_validation.fault(**kwargs)
            return -1, {}

        if stp_enabled is not None:
            stp_enabled_element = self.get_select_element_port_type("stp enable")

            if not stp_enabled_element:
                kwargs['fail_msg'] = "STP Enabled element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not stp_enabled_element.is_selected() and stp_enabled) or (
                stp_enabled_element.is_selected() and not stp_enabled):

                if self.auto_actions.click(stp_enabled_element) == 1:
                    self.utils.print_info("Successfully clicked on the STP enabled element")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the STP Enabled element "
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        if edge_port is not None:
            edge_port_element = self.get_select_element_port_type("edge port")

            if not edge_port_element:
                kwargs['fail_msg'] = "Edge Port element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if (not edge_port_element.is_selected() and edge_port) or (
                edge_port_element.is_selected() and not edge_port):

                if self.auto_actions.click(edge_port_element) == 1:
                    self.utils.print_info("Successfully clicked on the Edge Port element")
                    sleep(2)
                else:
                    kwargs['fail_msg'] = "Failed to click on the Edge Port element "
                    self.common_validation.fault(**kwargs)
                    return -1, {}

        if bpdu_protection is not None:
            bpdu_protection_element = self.get_select_element_port_type("bpdu protection")

            if not bpdu_protection_element:
                kwargs['fail_msg'] = "BPDU Protection element was not found "
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(bpdu_protection_element) == 1:
                self.utils.print_info("Successfully clicked on the BPDU Protection element")
                sleep(5)
            else:
                self.utils.print_info("Successfully clicked on the BPDU Protection element")
                return -1, {}

            get_bpdu_protection_items = self.get_select_element_port_type("bpdu_protection_items")

            if not get_bpdu_protection_items:
                kwargs['fail_msg'] = "BPDU Protection list elements not found "
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.select_drop_down_options(get_bpdu_protection_items, bpdu_protection):
                self.utils.print_info("Selected into dropdown value : ", bpdu_protection)
            else:
                kwargs['fail_msg'] = "Failed to select from BPDU Protection dropdown "
                self.common_validation.fault(**kwargs)
                return -1, {}

        if path_cost is not None:
            path_cost_element = self.get_select_element_port_type("path cost")

            if not path_cost_element:
                kwargs['fail_msg'] = "Path Cost element was not found"
                self.common_validation.failed(**kwargs)
                return -1, {}

            if self.auto_actions.send_keys(path_cost_element, str(path_cost)) == 1:
                self.utils.print_info("Successfully configured the path cost field")
                sleep(2)
            else:
                kwargs['fail_msg'] = "Failed to configure the path cost field "
                self.common_validation.failed(**kwargs)
                return -1, {}

        if priority:
            priority_element = self.get_select_element_port_type("priority")

            if not priority_element:
                kwargs['fail_msg'] = "Priority element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(priority_element) == 1:
                self.utils.print_info("Successfully clicked on the priority element")
                sleep(5)
            else:
                kwargs['fail_msg'] = "Failed to click on the priority element "
                self.common_validation.fault(**kwargs)
                return -1, {}

            get_priority_items = self.get_select_element_port_type("priority_items")
            if not get_priority_items:
                kwargs['fail_msg'] = "Priority element was not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.select_drop_down_options(get_priority_items, str(priority)):
                self.utils.print_info("Selected into dropdown value : ", priority)
            else:
                kwargs['fail_msg'] = "Failed to select item from priority dropdown "
                self.common_validation.fault(**kwargs)
                return -1, {}

        summary_tab = self.get_select_element_port_type("summaryPage")
        if not summary_tab:
            kwargs['fail_msg'] = "Failed to get the summary tab element"
            self.common_validation.fault(**kwargs)
            return -1

        if self.auto_actions.click(summary_tab) == 1:
            self.utils.print_info("Successfully clicked on the summary tab")
            sleep(5)
        else:
            kwargs['fail_msg'] = "Failed to click on the summary tab"
            self.common_validation.fault(**kwargs)
            return -1, {}

        summary = {}

        for row_name, row_value in zip(
            ["STP", "Edge Port", "BPDU Protection", "Priority", "Path Cost"],
            ["stp", "edge port", "bpdu protection", "priority", "path cost"]
        ):
            try:
                summary[row_name] = self.dev360.get_select_element_port_type_summary(row_value).text
            except Exception:
                summary[row_name] = ""

        if save:
            save_button = self.dev360.get_close_port_type_box()

            if not save_button:
                kwargs['fail_msg'] = "save button not found"
                self.common_validation.fault(**kwargs)
                return -1, {}

            if self.auto_actions.click(save_button) == 1:
                self.utils.print_info("Successfully clicked on the Save element")
            else:
                kwargs['fail_msg'] = "Failed to click on the Save element "
                self.common_validation.fault(**kwargs)
                return -1, {}

        kwargs['pass_msg'] = "Successfully got the summary of the newly created port type"
        self.common_validation.passed(**kwargs)
        return 1, summary

    def get_all_ports_from_each_asic(self):
        """
            This method returns all the ASICS and their ports from the Device360 Overview port groups.

            returns: a list which contains lists of ports (List[List[str]])

        Output e.g.:
            SR:
            >>> self.get_all_ports_from_each_asic()
            [
                ['1/0/1', '1/0/2', '1/0/3', '1/0/4', '1/0/5', '1/0/6', '1/0/7', '1/0/8'],
                ['1/0/9', '1/0/10', '1/0/11', '1/0/12', '1/0/13', '1/0/14', '1/0/15', '1/0/16'],
                ['1/0/17', '1/0/18', '1/0/19','1/0/20', '1/0/21', '1/0/22', '1/0/23', '1/0/24']
            ]

            EXOS:
            >>> self.get_all_ports_from_each_asic()
            [
                ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24']
            ]
            VOSS:
            >>> self.get_all_ports_from_each_asic()
            [
                ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24']
            ]
        """
        port_asics = self.dev360.get_device360_asic_port_groups()
        ret = []
        for asic in port_asics:
            temp = []
            ports_of_asic = self.dev360.get_device360_ports_each_asic_port_group(asic)
            if ports_of_asic:
                for p in ports_of_asic:
                    data_automation_tag = p.get_attribute("data-automation-tag")
                    if data_automation_tag:
                        port = data_automation_tag.split("automation-port-")[1]
                        if port not in ["mgmt", "console"]:
                            temp.append(port)
                if temp:
                    ret.append(temp)
        return [asic for asic in ret if len(asic) == len(max(ret, key=len))]

    def get_one_port_from_each_asic(self, order):
        """
            This method returns the ports on specific position from all the available ASICs.

            args:
                :order: int value that specifies which port of the ASIC to get

            returns: a list of strings (List[str])

        Output e.g.:
            SR:
            >>> self.get_one_port_from_each_asic(order=1)
            ['1/0/1', '1/0/9', '1/0/17']
            >>> self.get_one_port_from_each_asic(order=5)
            ['1/0/5', '1/0/13', '1/0/21']
            >>> self.get_one_port_from_each_asic(order=8)
            ['1/0/8', '1/0/16', '1/0/24']
            >>> self.get_one_port_from_each_asic(order=20)
            ['1/0/8', '1/0/16', '1/0/24']


            EXOS:
            >>> self.get_one_port_from_each_asic(order=1)
            ['1', '13']
            >>> self.get_one_port_from_each_asic(order=5)
            ['5', '17']
            >>> self.get_one_port_from_each_asic(order=12)
            ['12', '24']
            >>> self.get_one_port_from_each_asic(order=20)
            ['12', '24']

            VOSS:
            >>> self.get_one_port_from_each_asic(order=1)
            ['1/1', '1/13']
            >>> self.get_one_port_from_each_asic(order=5)
            ['1/5', '1/17']
            >>> self.get_one_port_from_each_asic(order=12)
            ['1/12', '1/24']
            >>> self.get_one_port_from_each_asic(order=20)
            ['1/12', '1/24']
        """
        ret = []
        port_asics = self.get_all_ports_from_each_asic()
        for asic in port_asics:
            if asic:
                try:
                    ret.append(asic[order-1])
                except IndexError:
                    ret.append(asic[-1])
        return ret

    def get_all_ports_from_each_asic_stack(self, slot):
        """
            This method returns all the ASICS and their ports from the Device360 Overview port groups.

            returns: a list which contains lists of ports (List[List[str]])

        Output e.g.:
            SR:
            >>> self.get_all_ports_from_each_asic()
            [
                ['1/0/1', '1/0/2', '1/0/3', '1/0/4', '1/0/5', '1/0/6', '1/0/7', '1/0/8'],
                ['1/0/9', '1/0/10', '1/0/11', '1/0/12', '1/0/13', '1/0/14', '1/0/15', '1/0/16'],
                ['1/0/17', '1/0/18', '1/0/19','1/0/20', '1/0/21', '1/0/22', '1/0/23', '1/0/24']
                ['2/0/1', '2/0/2', '2/0/3', '2/0/4', '2/0/5', '2/0/6', '2/0/7', '2/0/8'],
                ['2/0/9', '2/0/10', '2/0/11', '2/0/12', '2/0/13', '2/0/14', '2/0/15', '2/0/16'],
                ['2/0/17', '2/0/18', '2/0/19','2/0/20', '2/0/21', '2/0/22', '2/0/23', '2/0/24']
            ]

            EXOS:
            >>> self.get_all_ports_from_each_asic()
            [
                ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24']
                ['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11', '2/12'],
                ['2/13', '2/14', '2/15', '2/16', 2/17', '2/18', '2/19', '2/20', '2/21', '2/22', '2/23', '2/24']
            ]
            VOSS:
            >>> self.get_all_ports_from_each_asic()
            [
                ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24']
                ['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11', '2/12'],
                ['2/13', '2/14', '2/15', '2/16', '2/17', '2/18', '2/19', '2/20', '2/21', '2/22', '2/23', '2/24']
            ]
        """
        port_asics = self.dev360.get_device360_asic_port_groups_stack()
        ret = []
        for asic in port_asics:
            temp = []
            ports_of_asic = self.dev360.get_device360_ports_each_asic_port_group_stack(asic, slot=slot)
            if ports_of_asic:
                for p in ports_of_asic:
                    data_automation_tag = p.get_attribute("data-automation-tag")
                    if data_automation_tag:
                        port = data_automation_tag.split("automation-port-")[1]
                        if port not in ["mgmt", "console"]:
                            temp.append(port)
                if temp:
                    ret.append(temp)
        return [asic for asic in ret if len(asic) == len(max(ret, key=len))]

    def get_one_port_from_each_asic_stack(self, order, slot):
        """
            This method returns the ports on specific position from all the available ASICs.

            args:
                :order: int value that specifies which port of the ASIC to get

            returns: a list of strings (List[str])

        Output e.g.:
            SR:
            >>> self.get_one_port_from_each_asic(order=1)
            ['1/0/1', '1/0/9', '1/0/17']
            ['2/0/1', '2/0/9', '2/0/17']
            >>> self.get_one_port_from_each_asic(order=5)
            ['1/0/5', '1/0/13', '1/0/21']
            ['2/0/5', '2/0/13', '2/0/21']
            >>> self.get_one_port_from_each_asic(order=8)
            ['1/0/8', '1/0/16', '1/0/24']
            ['2/0/8', '2/0/16', '2/0/24']
            >>> self.get_one_port_from_each_asic(order=20)
            ['1/0/8', '1/0/16', '1/0/24']
            ['2/0/8', '2/0/16', '2/0/24']


            EXOS:
            >>> self.get_one_port_from_each_asic(order=1)
            ['1:1', '1:13']
            ['2:1', '2:13']
            >>> self.get_one_port_from_each_asic(order=5)
            ['1:5', '1:17']
            ['2:5', '2:17']
            >>> self.get_one_port_from_each_asic(order=12)
            ['1:12', '1:24']
            ['2:12', '2:24']
            >>> self.get_one_port_from_each_asic(order=20)
            ['1:12', '1:24']
            ['1:12', '1:24']

            VOSS:
            >>> self.get_one_port_from_each_asic(order=1)
            ['1/1', '1/13']
            ['2/1', '2/13']
            >>> self.get_one_port_from_each_asic(order=5)
            ['1/5', '1/17']
            ['2/5', '2/17']
            >>> self.get_one_port_from_each_asic(order=12)
            ['1/12', '1/24']
            ['2/12', '2/24']
            >>> self.get_one_port_from_each_asic(order=20)
            ['1/12', '1/24']
            ['2/12', '2/24']
        """
        ret = []
        port_asics = self.get_all_ports_from_each_asic_stack(slot=slot)
        for asic in port_asics:
            if asic:
                try:
                    ret.append(asic[order - 1])
                except IndexError:
                    ret.append(asic[-1])
        return ret

    def port_info_bounce_port(self, port, **kwargs):
        """
        - This keyword will bounce a port in D360
        - Assume that already in D360
        - Flow: D360 -> Monitor -> Overview -> Click on a port with 'connected' status ->
        :param port: A port in connected/disconnected status ;
                     Usage Ex: voss(1/1) , exos(1), stack(1:1)
        :return: 1 if 'Bounce Port' button has been successfully pressed; -1 if otherwise
        """
        def _check_port_is_loaded():
            if self.get_device360_overview_port(port):
                self.utils.print_info(f"Port {port} has been loaded.")
                return True
            self.utils.print_info(f"Port {port} hasn't been loaded yet... Saving screenshot...")
            self.screen.save_screen_shot()
            return False
        self.utils.wait_till(_check_port_is_loaded, silent_failure=True, timeout=5, delay=3,
                             msg=f'Waiting for the port {port} to load...')

        port_search = self.get_device360_overview_port(port)
        if port_search:
            self.auto_actions.click(port_search)
        else:
            kwargs['fail_msg'] = f"Cannot find the port: {port}; Check that port exists in the overview page. "
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info(f"Searching for the 'Bounce Port' button for port {port}...")
        bounce_port_button = self.get_device360_overview_port_info_bounce_port()
        if bounce_port_button:
            self.utils.print_info(f"Found 'Bounce Port' button for port {port}. Clicking...")
            self.auto_actions.click(bounce_port_button)
            self.utils.print_info(f"'Bounce Port' clicked! for port {port}")

            def _check_successful_message():
                self.utils.print_info("Captured tool tip: ", tool_tip.tool_tip_text)
                if f'Bounce Port {port} successful' in tool_tip.tool_tip_text:
                    self.utils.print_info(f"Found Bounce Port for port {port} successful message: {tool_tip.tool_tip_text}")
                    return True

                for tool_tp in tool_tip.tool_tip_text:
                    if "Unable to bounce port: " in tool_tp:
                        self.utils.print_info("RequestError message found: ", tool_tp)
                        self.utils.print_info("Saving screenshot...")
                        self.screen.save_screen_shot()
                        self.device360_refresh_page()
                        port_search = self.get_device360_overview_port(port)
                        if port_search:
                            self.auto_actions.click(port_search)
                        else:
                            self.utils.print_info(
                                f"Cannot find the port: {port}; Check that port exists in the overview page.")
                            kwargs['fail_msg'] = f"Cannot find the port: {port}; " \
                                                 f"Check that port exists in the overview page. Saving screenshot..."
                            self.screen.save_screen_shot()
                            self.common_validation.failed(**kwargs)
                            return -1

                        self.utils.print_info(f"Searching for the 'Bounce Port' button for port {port} ...")
                        bounce_port_button = self.get_device360_overview_port_info_bounce_port()
                        if bounce_port_button:
                            self.utils.print_info(f"Found 'Bounce Port' button for port {port}. Clicking...")
                            self.auto_actions.click(bounce_port_button)
                            self.utils.print_info(f"'Bounce Port'{port} clicked!")
                        return False
                self.utils.print_info(f"Did not find Bounce port for port {port} successful message yet. Retrying...")
                return False
            message = self.utils.wait_till(_check_successful_message, timeout=300, delay=15, silent_failure=True,
                                           msg=f"Looking for Bounce Port for port {port} successful message...")
            if message[0]:
                kwargs['pass_msg'] = f"'Bounce Port {port}' clicked! Successful message found!"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"'Bounce Port' successful message for port {port} not found!\nGot " \
                                     f"this instead: {tool_tip.tool_tip_text} "
                self.common_validation.failed(**kwargs)
                return -1

    def port_info_bounce_poe(self, port, **kwargs):
        """
        - This keyword will bounce PoE on a port in D360
        - Assume that already in D360
        - Flow: D360 -> Monitor -> Overview -> Click on a port with 'connected' status ->
        :param port: A port in connected/disconnected status ;
                     Usage Ex: voss(1/1) , exos(1), stack(1:1)
        :return: 1 if 'Bounce PoE' button has been successfully pressed; -1 if otherwise
        """
        def _check_port_is_loaded():
            if self.get_device360_overview_port(port):
                self.utils.print_info(f"Port {port} has been loaded.")
                return True
            self.utils.print_info(f"Port {port} hasn't been loaded yet... Saving screenshot...")
            self.screen.save_screen_shot()
            return False
        self.utils.wait_till(_check_port_is_loaded, silent_failure=True, timeout=5, delay=3,
                             msg=f'Waiting for the port {port} to load...')

        port_search = self.get_device360_overview_port(port)
        if port_search:
            self.auto_actions.click(port_search)
        else:
            kwargs['fail_msg'] = f"Cannot find the port: {port}; Check that port exists in the overview page. "
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Searching for the 'Bounce PoE' button...")
        bounce_poe_button = self.get_device360_overview_port_info_bounce_poe()
        if bounce_poe_button:
            self.utils.print_info(f"Found 'Bounce PoE' button for port {port}. Clicking...")
            self.auto_actions.click(bounce_poe_button)
            self.utils.print_info(f"'Bounce PoE' clicked! for port {port}")

            def _check_successful_message():
                self.utils.print_info("Tool tip captured: ", tool_tip.tool_tip_text)
                if f'Bounce PoE Port {port} successful' in tool_tip.tool_tip_text:
                    self.utils.print_info(f"Found Bounce PoE successful message: {tool_tip.tool_tip_text}")
                    return True
                for tool_tp in tool_tip.tool_tip_text:
                    if 'Unable to bounce PoE port: ' in tool_tp:
                        self.utils.print_info("RequestError found. Retrying bouncing PoE...")
                        self.utils.print_info("Saving screenshot...")
                        self.screen.save_screen_shot()
                        port_search = self.get_device360_overview_port(port)
                        if port_search:
                            self.auto_actions.click(port_search)
                        else:
                            self.utils.print_info(
                                f"Cannot find the port: {port}; Check that port exists in the overview page.")
                            kwargs[
                                'fail_msg'] = f"Cannot find the port: {port}; " \
                                              f"Check that port exists in the overview page. Saving screenshot..."
                            self.screen.save_screen_shot()
                            self.common_validation.failed(**kwargs)
                            return -1

                        self.utils.print_info(f"Searching for the 'Bounce PoE' button for port {port}...")
                        bounce_poe_button = self.get_device360_overview_port_info_bounce_poe()
                        if bounce_poe_button:
                            self.utils.print_info(f"Found 'Bounce PoE' button for port {port}. Clicking...")
                            self.auto_actions.click(bounce_poe_button)
                            self.utils.print_info(f"'Bounce PoE' clicked! for port {port}")
                self.utils.print_info(f"Did not find Bounce PoE successful message for port {port} yet. Retrying...")
                print(tool_tip.tool_tip_text)
                return False
            message = self.utils.wait_till(_check_successful_message, timeout=300, delay=15, silent_failure=True,
                                           msg=f"Looking for Bounce PoE successful message for port {port}...")
            if message[0]:
                kwargs['pass_msg'] = f"'Bounce PoE' clicked  for port {port} ! Successful message found!"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"'Bounce PoE' successful message not found for port {port} !\nGot this " \
                                     f"instead: {tool_tip.tool_tip_text} "
                self.common_validation.failed(**kwargs)
                return -1

    def get_event_from_device360(self, dut, event, close_360_window=True, **kwargs):
        """
        This function is used to search for an event given as parameter in Events view from Device360 window
        :param dut: the instance of the device
        :param event: the event that is being looking for
        :param close_360_window: True - if Device360 to be close; False - if not
        :return: 1 - if the event was found successfully ; -1 - if not
        """
        if self.navigator.navigate_to_devices() != 1:
            self.utils.print_info("Failed to navigate to Devices tab")
            kwargs['fail_msg'] = "Failed to navigate to Devices tab"
            self.common_validation.failed(**kwargs)
            return -1
        if self.deviceCommon.go_to_device360_window(device_mac=dut.mac) != 1:
            self.utils.print_info("Failed to go to Device360 window")
            kwargs['fail_msg'] = "Failed to go to Device360 window"
            self.common_validation.failed(**kwargs)
            return -1
        if self.device360_select_events_view() != 1:
            self.utils.print_info("Failed to select Events view")
            kwargs['fail_msg'] = "Failed to select Events view"
            self.common_validation.failed(**kwargs)
            return -1
        sleep(3)

        count = self.device360_search_event_and_confirm_event_description_contains(event, **kwargs)

        if close_360_window:
            self.close_device360_window()
        return count

    def check_port_cdp_lldp(self, port_type_name, cdp_transmit_receive_should_be_editable=None,
                            cdp_transmit_receive_should_be_enabled=None, lldp_transmit_should_be_editable=None,
                            lldp_transmit_should_be_enabled=None, lldp_receive_should_be_editable=None,
                            lldp_receive_should_be_enabled=None):
        """
        AIQ-1739
        Keyword: In port type editor, in transmission settings - check CDP/LLDP options are enabled /disabled/editable
                https://jira.extremenetworks.com/browse/AIQ-1739
        This function verifies that the 'Enable CDP Transmit/Receive', 'Enable LLDP Transmit', 'Enabled LLDP Receive'
         checkboxes are selected/not selected/editable/not editable.
        It will also verify the status of the 'LLDP Voice VLAN Options', 'CDP Voice VLAN Options' options
         of the VLAN page.
        For the configurable voice port type fields that are a bool type value:
            If kwarg == True then the function will verify the port type editor field that corresponds to the kwarg
                is enabled/editable
            If kwarg == False then the function will verify the port type editor field that corresponds to the kwarg
                is not enabled/editable
            If kwarg == None then the function will not verify the port type field that corresponds to the kwarg
        The method should be called from 'Configure -> Network Policies -> Network Policy -> Device Template -> Port Configuration'.
        args:
            :port_type_name:                              <str>
        kwargs:
            :cdp_transmit_receive_should_be_editable:     <bool|None>
            :cdp_transmit_receive_should_be_enabled:      <bool|None>
            :lldp_transmit_should_be_editable:            <bool|None>
            :lldp_transmit_should_be_enabled:             <bool|None>
            :lldp_receive_should_be_editable:             <bool|None>
            :lldp_receive_should_be_enabled:              <bool|None>
        returns: 1 if the selected verifications are successful else -1
        usage:
          self.xiq.xflowsmanageDevice360.check_port_cdp_lldp(
                port_type_name="testing_port", cdp_transmit_receive_should_be_editable=True,
                lldp_receive_should_be_enabled=False)
        # the check_port_cdp_lldp method will verify:
        #   - the 'Enable CDP Transmit/Receive' checkbox is editable
        #   - the 'Enable LLDP Transmit' checkbox is not selected
        """
        if not any(
                [
                    cdp_transmit_receive_should_be_editable is not None,
                    cdp_transmit_receive_should_be_enabled is not None,
                    lldp_transmit_should_be_editable is not None,
                    lldp_transmit_should_be_enabled is not None,
                    lldp_receive_should_be_editable is not None,
                    lldp_receive_should_be_enabled is not None
                ]
        ):
            self.utils.print_info("At least a checkbox should be verified (at least a kwarg should be True/False)")
            return -1

        rows = self.get_policy_configure_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
            return -1
        else:
            for row in rows:
                if re.search(rf'\d+\n{port_type_name}\n', row.text):
                    policy_edit_port_type = self.get_policy_edit_port_type(row)
                    if policy_edit_port_type:
                        self.utils.print_info("The button policy_edit_port_type from policy  was found")
                        self.auto_actions.click(policy_edit_port_type)
                        def _check_port_editor_window_present():
                            return bool(self.get_select_element_port_type("tab_vlan"))

                        self.utils.wait_till(_check_port_editor_window_present, timeout=10, delay=1,
                                                       msg="Waiting for edit port type window to appear",
                                                       is_logging_enabled=True)
                        break
                    else:
                        self.utils.print_info("The button policy_edit_port_type from policy  was not found")
                        self.screen.save_screen_shot()
                        return -1

        lldp_voice_vlan_options_checkbox_name = "LLDP Voice VLAN Options"
        cdp_voice_vlan_options_checkbox_name = "CDP Voice VLAN Options"

        en_cdp_transmit_receive_checkbox_name = "Enable CDP Transmit/Receive"
        en_lldp_transmit_checkbox_name = "Enable LLDP Transmit"
        en_lldp_receive_checkbox_name = "Enabled LLDP Receive"

        vlan_tab = self.get_select_element_port_type("tab_vlan")
        if not vlan_tab:
            self.utils.print_info("Failed to get the vlan page")
            return -1
        self.auto_actions.click(vlan_tab)

        def _wait_for_vlan_tab_appear():
            return bool(self.get_select_element_port_type("vlan_tab_confirmation")) \
                   and bool(self.get_select_element_port_type("lldp_voice_vlan_options"))

        self.utils.wait_till(_wait_for_vlan_tab_appear, timeout=4, delay=1,
                             msg="Waiting for vlan window to appear",
                             is_logging_enabled=True)

        lldp_voice_options = self.get_select_element_port_type("lldp_voice_vlan_options")
        if not lldp_voice_options:
            self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' option not found")
            return -1

        lldp_options_enabled = lldp_voice_options.is_selected()
        self.utils.print_info(
            f"'{lldp_voice_vlan_options_checkbox_name}': {'enabled' if lldp_options_enabled else 'not enabled'}")

        cdp_voice_options = self.get_select_element_port_type("cdp_voice_vlan_options")
        if not cdp_voice_options:
            self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' option not found")
            return -1

        cdp_options_enabled = cdp_voice_options.is_selected()
        self.utils.print_info(
            f"'{cdp_voice_vlan_options_checkbox_name}': {'enabled' if cdp_options_enabled else 'not enabled'}")

        transmission_tab = self.get_select_element_port_type("transmissionSettingsPage")
        if not transmission_tab:
            self.utils.print_info("Failed to get transmission settings page")
            return -1
        self.auto_actions.click(transmission_tab)
        def _wait_for_transmission_tab_appear():
            return bool(self.get_select_element_port_type("transmission_tab_confirmation")) \
                   and bool(self.get_select_element_port_type("cdp receive"))

        self.utils.wait_till(_wait_for_transmission_tab_appear, timeout=4, delay=1,
                             msg="Waiting for transmission tab window to appear",
                             is_logging_enabled=True)

        if (cdp_transmit_receive_should_be_editable is not None) or (
                cdp_transmit_receive_should_be_enabled is not None):
            cdp_transmit_receive = self.get_select_element_port_type("cdp receive")
            if not cdp_transmit_receive:
                self.utils.print_info(f"Failed to get '{en_cdp_transmit_receive_checkbox_name}' checkbox")
                return -1

        if cdp_transmit_receive_should_be_editable is not None:
            # first check the transmission settings page
            cdp_transmit_receive_is_editable = cdp_transmit_receive.is_enabled()

            if cdp_transmit_receive_is_editable == cdp_transmit_receive_should_be_editable:
                self.utils.print_info(
                    f"Successfully found '{en_cdp_transmit_receive_checkbox_name}' checkbox in the expected state: "
                    f"'{'editabled' if cdp_transmit_receive_is_editable else 'not editable'}'")
            else:
                self.utils.print_info(
                    f"Failed to find '{en_cdp_transmit_receive_checkbox_name}' in the expected state. Found"
                    f" '{'editabled' if cdp_transmit_receive_is_editable else 'not editable'}' but expected "
                    f"'{'editabled' if cdp_transmit_receive_should_be_editable else 'not editable'}'")
                return -1

            # now check the vlan page

            # CDP voice vlan options = OFF (VLAN PAGE) => enable CDP transmit/receive = not editable (TRANSMISSION SETTINGS page)
            # LLDP voice vlan options = OFF (VLAN PAGE) => enable LLDP transmit = not editable (TRANSMISSION SETTINGS page)
            # LLDP voice vlan options = OFF (VLAN PAGE) => enable LLDP receive = not editable (TRANSMISSION SETTINGS page)

            # CDP voice vlan options = ON (VLAN PAGE) => enable CDP transmit/receive = editable (TRANSMISSION SETTINGS page)
            # LLDP voice vlan options = ON (VLAN PAGE) => enable LLDP transmit = editable (TRANSMISSION SETTINGS page)
            # LLDP voice vlan options = ON (VLAN PAGE) => enable LLDP receive = editable (TRANSMISSION SETTINGS page)

            if cdp_transmit_receive_is_editable != cdp_options_enabled:
                self.utils.print_info(
                    f"Successfully found 'cdp_transmit_receive_is_enable'='{cdp_transmit_receive_is_editable}' "
                    f"when cdp_options_enable='{cdp_options_enabled}' in the vlan page"
                )
            else:
                self.utils.print_info(
                    f"Failed! Found 'cdp_transmit_receive_is_enable'='{cdp_transmit_receive_is_editable}'"
                    f" when 'cdp_options_enable'='{cdp_options_enabled}' in the vlan page"
                )
                return -1

        if cdp_transmit_receive_should_be_enabled is not None:
            cdp_transmit_receive_is_enabled = cdp_transmit_receive.is_selected()

            if cdp_transmit_receive_is_enabled == cdp_transmit_receive_should_be_enabled:
                self.utils.print_info(f"Successfully found that '{en_cdp_transmit_receive_checkbox_name}' checkbox is "
                                      f"'{'enabled' if cdp_transmit_receive_should_be_enabled else 'disabled'}'")
            else:
                self.utils.print_info(f"Expected to find the '{en_cdp_transmit_receive_checkbox_name}' checkbox as "
                                      f"'{'enabled' if cdp_transmit_receive_should_be_enabled else 'disabled'}' "
                                      f"but found '{'enabled' if cdp_transmit_receive_is_enabled else 'disabled'}'")
                return -1

        if (lldp_transmit_should_be_editable is not None) or (lldp_transmit_should_be_enabled is not None):
            lldp_transmit = self.get_select_element_port_type("lldp transmit")
            if not lldp_transmit:
                self.utils.print_info(f"Failed to get '{en_lldp_transmit_checkbox_name}' checkbox")
                return -1

        if lldp_transmit_should_be_editable is not None:
            lldp_transmit_is_editable = lldp_transmit.is_enabled()

            if lldp_transmit_is_editable == lldp_transmit_should_be_editable:
                self.utils.print_info(
                    f"Successfully found '{en_lldp_transmit_checkbox_name}' checkbox in the expected state: "
                    f"'{'editable' if lldp_transmit_is_editable else 'not editable'}'")
            else:
                self.utils.print_info(
                    f"Failed to find '{en_lldp_transmit_checkbox_name}' checkbox in the expected state. Found "
                    f"'{'editable' if lldp_transmit_is_editable else 'not editable'}' but expected "
                    f"'{'editable' if lldp_transmit_should_be_editable else 'not editable'}'")
                return -1

            if lldp_transmit_is_editable != lldp_options_enabled:
                self.utils.print_info(
                    f"Successfully found 'lldp_transmit_is_editable'='{lldp_transmit_is_editable}'"
                    f"when 'cdp_options_enable'='{lldp_options_enabled}'"
                )
            else:
                self.utils.print_info(
                    f"Failed! Found 'lldp_transmit_is_editable'='{lldp_transmit_is_editable}'"
                    f" when 'cdp_options_enable'='{lldp_options_enabled}'"
                )
                return -1

        if lldp_transmit_should_be_enabled is not None:
            lldp_transmit_is_enabled = lldp_transmit.is_selected()

            if lldp_transmit_is_enabled == lldp_transmit_should_be_enabled:
                self.utils.print_info(f"Successfully found that '{en_lldp_transmit_checkbox_name}' checkbox is "
                                      f"'{'enabled' if lldp_transmit_should_be_enabled else 'disabled'}'")
            else:
                self.utils.print_info(f"Expected to find the '{en_lldp_transmit_checkbox_name}' checkbox as "
                                      f"'{'enabled' if lldp_transmit_should_be_enabled else 'disabled'}' but found "
                                      f"'{'enabled' if lldp_transmit_is_enabled else 'disabled'}'")
                return -1

        if (lldp_receive_should_be_editable is not None) or (lldp_receive_should_be_enabled is not None):
            lldp_receive = self.get_select_element_port_type("lldp transmit")
            if not lldp_receive:
                self.utils.print_info(f"Failed to get '{en_lldp_receive_checkbox_name}' checkbox")
                return -1

        if lldp_receive_should_be_editable is not None:
            lldp_receive_is_editable = lldp_receive.is_enabled()

            if lldp_receive_is_editable == lldp_receive_should_be_editable:
                self.utils.print_info(
                    f"Successfully found '{en_lldp_receive_checkbox_name}' checkbox in the expected state:"
                    f" '{'editable' if lldp_receive_is_editable else 'not editable'}'")
            else:
                self.utils.print_info(
                    f"Failed to find '{en_lldp_receive_checkbox_name}' checkbox in the expected state. Found "
                    f"'{'editable' if lldp_receive_is_editable else 'not editable'}' but expected "
                    f"'{'editable' if lldp_receive_should_be_editable else 'not editable'}'")
                return -1

            if lldp_receive_is_editable != lldp_options_enabled:
                self.utils.print_info(
                    f"Successfully found 'lldp_receive_is_enable'='{lldp_receive_is_editable}'"
                    f"when 'lldp_options_enable'='{lldp_options_enabled}'"
                )
            else:
                self.utils.print_info(
                    f"Failed! Found 'lldp_receive_is_enable'={lldp_receive_is_editable}"
                    f" when 'lldp_options_enable'='{lldp_options_enabled}'"
                )
                return -1

        if lldp_receive_should_be_enabled is not None:
            lldp_receive_is_enabled = lldp_receive.is_selected()

            if lldp_receive_is_enabled == lldp_receive_should_be_enabled:
                self.utils.print_info(f"Successfully found that '{en_lldp_receive_checkbox_name}' checkbox is "
                                      f"'{'enabled' if lldp_receive_should_be_enabled else 'disabled'}'")
            else:
                self.utils.print_info(f"Expected to find the '{en_lldp_receive_checkbox_name}' checkbox as "
                                      f"'{'enabled' if lldp_receive_should_be_enabled else 'disabled'}' but found "
                                      f"'{'enabled' if lldp_receive_is_enabled else 'disabled'}'")
                return -1

        summary_page = self.get_select_element_port_type("summaryPage")
        if not summary_page:
            self.utils.print_info("Failed to get summary page")
            return -1
        self.auto_actions.click(summary_page)
        # self.utils.wait_till(3)
        def _wait_for_summary_tab_appear():
            return bool(self.get_select_element_port_type("summary_tab_confirmation")) \
                   and bool(self.dev360.get_close_port_type_box())

        self.utils.wait_till(_wait_for_summary_tab_appear, timeout=4, delay=1,
                             msg="Waiting for summary tab window to appear",
                             is_logging_enabled=True)

        close_button = self.dev360.get_close_port_type_box()
        if not close_button:
            self.utils.print_info("save button not found")
            return -1
        self.auto_actions.click(close_button)
        return 1

    def create_voice_port(self, port, port_type_name="test_port", description="description_of_test_port", status=True,
                          voice_vlan="1", data_vlan="2", lldp_voice_options_flag=True, cdp_voice_options_flag=True,
                          dot1_vlan_id_flag=True, lldp_advertisment_of_med_voice_vlan_flag=True,
                          lldp_voice_vlan_dscp=1, lldp_advertisment_of_med_signaling_vlan_flag=True,
                          lldp_voice_signaling_dscp=2, cdp_advertisment_of_voice_vlan_flag=True,
                          cdp_advertisment_of_power_available_flag=True, device_360=False):
        """
        AIQ-1736
        Keyword: Create port type - phone with a data port in template level
                https://jira.extremenetworks.com/browse/AIQ-1736
        Method used to configure a new voice port type.
        For the configurable voice port type fields that are a bool type value:
            If kwarg == True then the function will enable the port type editor field that
                corresponds to the given kwarg (if not already enabled).
            If kwarg == False then the function will disable the port type editor field that
                corresponds to the given kwarg (if not already disabled).
        If the device_360 keyword is False then the method should be called from 'Configure -> Network Policies -> Network Policy -> Device Template -> Port Configuration'.
        If the device_360 keyword is True then the method should be called from 'Manage -> Devices -> Device -> Configure -> Port Configuration'.
        args:
            :port:                                           <str>
        kwargs:
            :port_type_name:                                 <str>
            :description:                                    <str>
            :status:                                         <bool
            :voice_vlan: the voice vlan                      <str>
            :data_vlan: the data vlan                        <str>
            :lldp_voice_options_flag:                        <bool>
            :cdp_voice_options_flag:                         <bool>
            :dot1_vlan_id_flag:                              <bool>
            :lldp_advertisment_of_med_voice_vlan_flag:       <bool>
            :lldp_voice_vlan_dscp:                           <int>
            :lldp_advertisment_of_med_signaling_vlan_flag:   <bool>
            :lldp_voice_signaling_dscp:                      <int>
            :cdp_advertisment_of_voice_vlan_flag:            <bool>
            :cdp_advertisment_of_power_available_flag:       <bool>
            :device_360:                                     <bool>
        returns: 1 if the configuration is successful else -1
        usage:
            self.xiq.xflowsmanageDevice360.create_voice_port(
                port="2", port_type_name="testing")
            # creates a port type with every phone port type option turned on
            self.xiq.xflowsmanageDevice360.create_voice_port(
                port="2", port_type_name="testing", lldp_voice_options_flag=False, cdp_voice_options_flag=False)
            # creates a port type with 'LLDP Voice VLAN Options' and 'CDP Voice VLAN Options' disabled
        """
        if not device_360:
            rows = self.get_policy_configure_port_rows()
            if not rows:
                self.utils.print_info("Could not obtain list of port rows")
                return -1
            else:
                for row in rows:
                    if re.search(f'{port}\n', row.text):
                        d360_create_port_type = self.get_d360_create_port_type(row)
                        if d360_create_port_type:
                            self.utils.print_info(" The button d360_create_port_type from policy  was found")
                            self.auto_actions.click(d360_create_port_type)
                            def _check_port_editor_window_present():
                                return bool(self.get_select_element_port_type("tab_vlan"))

                            self.utils.wait_till(_check_port_editor_window_present, timeout=10, delay=1,
                                                 msg="Waiting for new port type window to appear",
                                                 is_logging_enabled=True)
                            break
                        else:
                            self.utils.print_info(" The button d360_create_port_type from policy  was not found")
                            self.screen.save_screen_shot()
                            return -1
        else:
            port_conf_content = self.get_device360_port_configuration_content()
            if port_conf_content:
                port_row = self.device360_get_port_row(port)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)

                    d360_create_port_type = self.get_d360_create_port_type(port_row)
                    if d360_create_port_type:
                        self.utils.print_info(" The button d360_create_port_type  was found")
                        self.auto_actions.click(d360_create_port_type)

                        def _check_port_editor_window_present():
                            return bool(self.get_select_element_port_type("tab_vlan"))

                        self.utils.wait_till(_check_port_editor_window_present, timeout=3, delay=1,
                                             msg="Waiting for new port type window to appear",
                                             is_logging_enabled=True)
                    else:
                        self.utils.print_info(" The button d360_create_port_type  was not found")
                        self.screen.save_screen_shot()
                        return -1
                else:
                    self.utils.print_info("Port was not found ")
                    return -1
            else:
                return -1

        name_element = self.get_select_element_port_type("name")
        if not name_element:
            self.utils.print_info("Port name was not found ")
            return -1
        self.auto_actions.send_keys(name_element, port_type_name)

        description_element = self.get_select_element_port_type("description")
        if not description_element:
            self.utils.print_info("Port description was not found ")
            return -1
        self.auto_actions.send_keys(description_element, description)

        status_element = self.get_select_element_port_type("status")
        if not status_element:
            self.utils.print_info("Port status was not found ")
            return -1

        if (not status_element.is_selected() and status) or (
                status_element.is_selected() and not status):
            self.auto_actions.click(status_element)
            self.utils.wait_till(delay=1,timeout=2,msg= "waiting for port status element")

        phone_port_element = self.get_select_element_port_type("port usage", "phone port")
        if not phone_port_element:
            self.utils.print_info("phone port type was not found ")
            return -1
        self.auto_actions.click(phone_port_element)
        self.utils.wait_till(delay=1,timeout=2)

        get_next_button = self.get_select_element_port_type("next_button")
        if get_next_button:
            self.utils.print_info("go to the vlan configuration page")
            self.auto_actions.click(get_next_button)
            def _wait_for_vlan_tab_appear():
                return bool(self.get_select_element_port_type("vlan_tab_confirmation")) \
                       and bool(self.get_select_element_port_type("lldp_voice_vlan_options"))

            self.utils.wait_till(_wait_for_vlan_tab_appear, timeout=4, delay=1,
                                 msg="Waiting for vlan window to appear",
                                 is_logging_enabled=True)
        else:
            self.utils.print_info("get_next_button not found ")
            return -1

        get_select_button = self.get_select_element_port_type("voice_vlan_select_button")
        if get_select_button:
            self.auto_actions.click(get_select_button)

            self.utils.wait_till(delay=2, timeout=4)
            get_dropdown_items = self.get_select_element_port_type("voice_vlan_dropdown_items")

            if self.auto_actions.select_drop_down_options(get_dropdown_items, voice_vlan):
                self.utils.print_info(" Selected into dropdown voice_vlan : ", voice_vlan)
                self.utils.wait_till(delay=1,timeout=2,msg="Dropdown voice vlan selection")
            else:
                get_add_vlan = self.get_select_element_port_type("voice_vlan_add_vlan")
                if get_add_vlan:
                    self.auto_actions.click(get_add_vlan)

                    def _voice_vlan_appear():
                        return bool(self.get_select_element_port_type("voice_vlan_name_vlan"))

                    self.utils.wait_till(_voice_vlan_appear,
                                         is_logging_enabled=True,
                                         msg= "Voice vlan appear on clicking")

                    get_name_vlan = self.get_select_element_port_type("voice_vlan_name_vlan")
                    if get_name_vlan:
                        self.auto_actions.send_keys(get_name_vlan, voice_vlan)
                    else:
                        self.utils.print_info("voice vlan get_id_vlan not found ")
                        return -1
                    get_id_vlan = self.get_select_element_port_type("voice_vlan_id_vlan")
                    if get_id_vlan:
                        self.auto_actions.send_keys(get_id_vlan, voice_vlan)
                    else:
                        self.utils.print_info("voice vlan get_id_vlan not found ")
                        return -1
                    get_save_vlan = self.get_select_element_port_type("save_vlan")
                    if get_save_vlan:
                        self.auto_actions.click(get_save_vlan)

                        def _save_vlan_disappear():
                            return not bool(self.get_select_element_port_type("save_vlan"))

                        self.utils.wait_till(_save_vlan_disappear, is_logging_enabled=True)
                    else:
                        self.utils.print_info("get_save_vlan not found ")
                        return -1
                else:
                    self.utils.print_info("voice vlan get_add_vlan not found ")
                    return -1
        else:
            self.utils.print_info("voice vlan get_select_button not found ")
            return -1

        get_select_button = self.get_select_element_port_type("data_vlan_select_button")
        if get_select_button:
            self.auto_actions.click(get_select_button)
            self.utils.wait_till(delay=2, timeout=4)

            get_dropdown_items = self.get_select_element_port_type("data_vlan_dropdown_items")
            if self.auto_actions.select_drop_down_options(get_dropdown_items, data_vlan):
                self.utils.print_info(" Selected into dropdown value : ", data_vlan)
                self.utils.wait_till(delay=1,timeout=2,msg="Dropdown data vlan selection")

            else:
                get_add_vlan = self.get_select_element_port_type("data_vlan_add_vlan")
                if get_add_vlan:
                    self.auto_actions.click(get_add_vlan)
                    def _data_vlan_appear():
                        return bool(self.get_select_element_port_type("data_vlan_name_vlan"))

                    self.utils.wait_till(_data_vlan_appear, is_logging_enabled=True)

                    get_name_vlan = self.get_select_element_port_type("data_vlan_name_vlan")
                    if get_name_vlan:
                        self.auto_actions.send_keys(get_name_vlan, data_vlan)
                    else:
                        self.utils.print_info("data vlan get_id_vlan not found ")
                        return -1
                    get_id_vlan = self.get_select_element_port_type("data_vlan_id_vlan")
                    if get_id_vlan:
                        self.auto_actions.send_keys(get_id_vlan, data_vlan)
                    else:
                        self.utils.print_info("data vlan get_id_vlan not found ")
                        return -1
                    get_save_vlan = self.get_select_element_port_type("save_vlan")
                    if get_save_vlan:
                        self.auto_actions.click(get_save_vlan)

                        def _save_vlan_disappear():
                            return not bool(self.get_select_element_port_type("save_vlan"))
                        self.utils.wait_till(_save_vlan_disappear, is_logging_enabled=True)

                    else:
                        self.utils.print_info("get_save_vlan not found ")
                        return -1
                else:
                    self.utils.print_info("data vlan get_add_vlan not found ")
                    return -1
        else:
            self.utils.print_info("data vlan get_select_button not found ")
            return -1

        lldp_voice_vlan_options_checkbox_name = "LLDP Voice VLAN Options"
        cdp_voice_vlan_options_checkbox_name = "CDP Voice VLAN Options"

        en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name = "Enable LLDP advertisement of 802.1 VLAN ID and port protocol of Voice VLAN"
        en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name = "Enable LLDP advertisement of med Voice VLAN DSCP Value"
        en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name = "Enable LLDP advertisement of med Voice Signaling VLAN DSCP Value"
        en_cdp_adv_of_voice_vlan_checkbox_name = "Enable CDP advertisement of Voice VLAN"
        en_cdp_adv_of_power_available_checkbox_name = "Enable CDP advertisement of power available"

        lldp_voice_options = self.get_select_element_port_type("lldp_voice_vlan_options")
        if not lldp_voice_options:
            self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox not found")
            return -1
        previous_state_1 = lldp_voice_options.is_selected()
        if (not lldp_voice_options.is_selected() and lldp_voice_options_flag) or (
                lldp_voice_options.is_selected() and not lldp_voice_options_flag):
            self.auto_actions.click(lldp_voice_options)
            def _lldp_voice_option():
                return not (bool(lldp_voice_options.is_selected()) and previous_state_1)

            self.utils.wait_till(_lldp_voice_option, is_logging_enabled=True)

        cdp_voice_options = self.get_select_element_port_type("cdp_voice_vlan_options")
        if not cdp_voice_options:
            self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' checkbox not found")
            return -1

        previous_state_2 = cdp_voice_options.is_selected()

        if (not cdp_voice_options.is_selected() and cdp_voice_options_flag) or (
                cdp_voice_options.is_selected() and not cdp_voice_options_flag):
            self.auto_actions.click(cdp_voice_options)
            def _cdp_voice_option():
                return not (bool(cdp_voice_options.is_selected()) and previous_state_2)

            self.utils.wait_till(_cdp_voice_option, is_logging_enabled=True)

        if lldp_voice_options_flag:

            lldp_advertisment_of_med_voice_vlan = self.get_select_element_port_type(
                "enable_lldp_advertisment_of_med_voice_vlan")

            if not lldp_advertisment_of_med_voice_vlan:
                self.utils.print_info(
                    f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' checkbox option not found")
                return -1
            previous_state_3 = lldp_advertisment_of_med_voice_vlan.is_selected()

            if (not lldp_advertisment_of_med_voice_vlan.is_selected() and lldp_advertisment_of_med_voice_vlan_flag) or \
                    (
                            lldp_advertisment_of_med_voice_vlan.is_selected() and not lldp_advertisment_of_med_voice_vlan_flag):
                self.auto_actions.click(lldp_advertisment_of_med_voice_vlan)
                def _lldp_med_voice_option():
                    return not (bool(lldp_advertisment_of_med_voice_vlan.is_selected()) and previous_state_3)

                self.utils.wait_till(_lldp_med_voice_option, is_logging_enabled=True)

            if lldp_advertisment_of_med_voice_vlan.is_selected():

                lldp_advertisment_of_med_voice_vlan_dscp_value_element = self.get_select_element_port_type(
                    "lldp_advertisment_of_med_voice_vlan_dscp_value")
                if not lldp_advertisment_of_med_voice_vlan_dscp_value_element:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' input dscp value not found")
                    return -1
                else:
                    self.auto_actions.send_keys(lldp_advertisment_of_med_voice_vlan_dscp_value_element,
                                                lldp_voice_vlan_dscp)

            lldp_advertisment_of_med_signaling_vlan = self.get_select_element_port_type(
                "enable_lldp_advertisment_of_med_voice_signaling_vlan")
            previous_state_4 = lldp_advertisment_of_med_signaling_vlan.is_selected()

            if not lldp_advertisment_of_med_signaling_vlan:
                self.utils.print_info(
                    f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' checkbox not found")
                return -1

            if (
                    not lldp_advertisment_of_med_signaling_vlan.is_selected() and lldp_advertisment_of_med_signaling_vlan_flag) \
                    or (lldp_advertisment_of_med_signaling_vlan.is_selected()
                        and not lldp_advertisment_of_med_signaling_vlan_flag):
                self.auto_actions.click(lldp_advertisment_of_med_signaling_vlan)
                def _lldp_med_signalling_vlan():
                    return not (bool(lldp_advertisment_of_med_signaling_vlan.is_selected()) and previous_state_4)

                self.utils.wait_till(_lldp_med_signalling_vlan, is_logging_enabled=True)

            if lldp_advertisment_of_med_signaling_vlan.is_selected():
                lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element = self.get_select_element_port_type(
                    "lldp_advertisment_of_med_voice_signaling_vlan_dscp_value")
                if not lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' input dscp value not found")
                    return -1
                else:
                    self.auto_actions.send_keys(lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element,
                                                lldp_voice_signaling_dscp)
            dot1_vlan_id_element = self.get_select_element_port_type("enable_lldp_advertisment_of_dot1_vlan")
            previous_state_5 = dot1_vlan_id_element.is_selected()

            if not dot1_vlan_id_element:
                self.utils.print_info(
                    f"{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name} option not found")
                return -1

            if (not dot1_vlan_id_element.is_selected() and dot1_vlan_id_flag) or (
                    dot1_vlan_id_element.is_selected() and not dot1_vlan_id_flag):
                self.auto_actions.click(dot1_vlan_id_element)
                def _dot1_vlan_id_element_():
                    return not (bool(dot1_vlan_id_element.is_selected()) and previous_state_5)

                self.utils.wait_till(_dot1_vlan_id_element_, is_logging_enabled=True)

        else:
            self.utils.print_info(f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}',"
                              "'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' and"
                              "'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}'"
                              "checkboxes cant be updated because '{lldp_voice_vlan_options_checkbox_name}' checkbox is disabled")

        if cdp_voice_options_flag:
            cdp_advertisment_of_power_available = self.get_select_element_port_type(
                "enable_cdp_advertisment_of_power_available")
            previous_state_6 = cdp_advertisment_of_power_available.is_selected()

            if not cdp_advertisment_of_power_available:
                self.utils.print_info(f"'{en_cdp_adv_of_power_available_checkbox_name}' checkbox not found")
                if cdp_voice_options_flag:
                    return -1

            if (not cdp_advertisment_of_power_available.is_selected() and cdp_advertisment_of_power_available_flag) or \
                    (cdp_advertisment_of_power_available.is_selected() and not cdp_advertisment_of_power_available_flag):
                self.auto_actions.click(cdp_advertisment_of_power_available)
                def _cdp_power_available_vlan():
                    return (not bool(cdp_advertisment_of_power_available.is_selected())) and previous_state_6

                self.utils.wait_till(_cdp_power_available_vlan, is_logging_enabled=True)

            cdp_advertisment_of_voice_vlan = self.get_select_element_port_type("enable_cdp_advertisment_of_voice_vlan")
            previous_state_7 = cdp_advertisment_of_voice_vlan.is_selected()

            if not cdp_advertisment_of_voice_vlan:
                self.utils.print_info(f"'{en_cdp_adv_of_voice_vlan_checkbox_name}' checkbox not found")
                return -1

            if (not cdp_advertisment_of_voice_vlan.is_selected() and cdp_advertisment_of_voice_vlan_flag) or \
                    (cdp_advertisment_of_voice_vlan.is_selected() and not cdp_advertisment_of_voice_vlan_flag):
                self.auto_actions.click(cdp_advertisment_of_voice_vlan)
                def _cdp_voice_vlan():
                    return not (bool(cdp_advertisment_of_voice_vlan.is_selected()) and previous_state_7)

                self.utils.wait_till(_cdp_voice_vlan, is_logging_enabled=True)
        else:
            self.utils.print_info(
                f"'{en_cdp_adv_of_power_available_checkbox_name}' and '{en_cdp_adv_of_voice_vlan_checkbox_name}' checkboxes cant"
                f"be updated because '{cdp_voice_vlan_options_checkbox_name}' checkbox is disabled'")

        self.utils.print_info("Go to the last page and save the port type")
        for _ in range(10):
            get_next_button = self.get_select_element_port_type("next_button")
            if get_next_button:
                if get_next_button.is_enabled():
                    self.auto_actions.click(get_next_button)
                    self.utils.wait_till(delay=1,timeout=2)
                else:
                    break
            else:
                self.utils.print_info("get_next_button not found")
                return -1

        save_button = self.dev360.get_close_port_type_box()
        if not save_button:
            self.utils.print_info("save button not found")
            return -1
        self.auto_actions.click(save_button)
        return 1

    def edit_voice_port_type(self, port_type_name, **kwargs):
        """
        AIQ-1849
        Keyword: Edit port type - phone with a data port in template level
                https://jira.extremenetworks.com/browse/AIQ-1849
        Method used to enable or disable configurable fields of a voice port type.
        If kwarg == True then the function will enable the port type editor field that
            corresponds to the given kwarg (if not already enabled).
        If kwarg == False then the function will disable the port type editor field that
            corresponds to the given kwarg (if not already disabled).
        If kwarg == None then the function will not change the port type editor field that
            corrsponds to the given kwarg.
        The method should be called from 'Configure -> Network Policies -> Network Policy -> Device Template -> Port Configuration'.
        args:
            :port_type_name:                                  <str>
        kwargs:
            :voice_vlan:                                      <str>
            :data_vlan:                                       <str>
            :lldp_voice_options_flag:                         <bool|None>
            :cdp_voice_options_flag:                          <bool|None>
            :dot1_vlan_id_flag:                               <bool|None>
            :lldp_advertisment_of_med_voice_vlan_flag:        <bool|None>
            :lldp_advertisment_of_med_signaling_vlan_flag:    <bool|None>
            :cdp_advertisment_of_voice_vlan_flag:             <bool|None>
            :cdp_advertisment_of_power_available_flag:        <bool|None>
            :enable_cdp_transmit_receive_flag:                <bool|None>
            :enable_lldp_transmit_flag:                       <bool|None>
            :enable_lldp_receive_flag:                        <bool|None>
            :lldp_voice_vlan_dscp:                            <int>
            :lldp_voice_signaling_dscp:                       <int>
        returns: 1 if the functions call is successfull else -1
        usage:
            self.xiq.xflowsmanageDevice360.edit_voice_port_type(
                port_type_name="test", enable_lldp_receive_flag=True, cdp_voice_options_flag=True)
            # enables 'Enable LLDP Receive', enables 'Enable CDP Voice VLAN Options'
            self.xiq.xflowsmanageDevice360.edit_voice_port_type(
                port_type_name="test", voice_vlan="31")
            # updates Voice VLAN to "31"
            self.xiq.xflowsmanageDevice360.edit_voice_port_type(
                port_type_name="test", lldp_voice_vlan_dscp=12, lldp_voice_signaling_dscp=14)
            # updates dscp values
        """
        if not kwargs:
            self.utils.print_info("At least a field should be updated")
            return -1

        rows = self.get_policy_configure_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
            return -1
        else:
            for row in rows:
                if re.search(rf'\d+\n{port_type_name}\n', row.text):
                    policy_edit_port_type = self.get_policy_edit_port_type(row)
                    if policy_edit_port_type:
                        self.utils.print_info("The button policy_edit_port_type from policy  was found")
                        self.auto_actions.click(policy_edit_port_type)
                        def _check_port_editor_window_present():
                            return bool(self.get_select_element_port_type("tab_vlan"))

                        self.utils.wait_till(_check_port_editor_window_present, timeout=10, delay=1,
                                             msg="Waiting for existing port type window to appear",
                                             is_logging_enabled=True)
                        break
                    else:
                        self.utils.print_info("The button policy_edit_port_type from policy  was not found")
                        self.screen.save_screen_shot()
                        return -1

        vlan_tab_flags = [
            "voice_vlan", "data_vlan", "lldp_voice_options_flag", "cdp_voice_options_flag", "dot1_vlan_id_flag",
            "lldp_advertisment_of_med_voice_vlan_flag", "lldp_advertisment_of_med_signaling_vlan_flag",
            "cdp_advertisment_of_voice_vlan_flag", "cdp_advertisment_of_power_available_flag", "lldp_voice_vlan_dscp",
            "lldp_voice_signaling_dscp"
        ]

        lldp_voice_vlan_options_checkbox_name = "LLDP Voice VLAN Options"
        cdp_voice_vlan_options_checkbox_name = "CDP Voice VLAN Options"

        en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name = "Enable LLDP advertisement of 802.1 VLAN ID and port protocol of Voice VLAN"
        en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name = "Enable LLDP advertisement of med Voice VLAN DSCP Value"
        en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name = "Enable LLDP advertisement of med Voice Signaling VLAN DSCP Value"
        en_cdp_adv_of_voice_vlan_checkbox_name = "Enable CDP advertisement of Voice VLAN"
        en_cdp_adv_of_power_available_checkbox_name = "Enable CDP advertisement of power available"
        en_cdp_transmit_receive_checkbox_name = "Enable CDP Transmit/Receive"
        en_lldp_transmit_checkbox_name = "Enable LLDP Transmit"
        en_lldp_receive_checkbox_name = "Enabled LLDP Receive"

        if any(k in vlan_tab_flags for k in kwargs):

            vlan_tab = self.get_select_element_port_type("tab_vlan")
            if not vlan_tab:
                self.utils.print_info("Failed to get the vlan page")
                return -1
            self.auto_actions.click(vlan_tab)
            def _check_vlan_editor_window_present():
                return bool(self.get_select_element_port_type("vlan_tab_confirmation"))

            self.utils.wait_till(_check_vlan_editor_window_present, timeout=3, delay=1,
                                 msg="Waiting for vlan port type window to appear",
                                 is_logging_enabled=True)
            voice_vlan = kwargs.get("voice_vlan")

            if isinstance(voice_vlan, (str, int)):
                get_select_button = self.get_select_element_port_type("voice_vlan_select_button")
                if get_select_button:
                    self.auto_actions.click(get_select_button)
                    self.utils.wait_till(delay=2,timeout=4)

                    get_dropdown_items = self.get_select_element_port_type("voice_vlan_dropdown_items")

                    if self.auto_actions.select_drop_down_options(get_dropdown_items, str(voice_vlan)):
                        self.utils.print_info(" Selected into dropdown voice_vlan : ", str(voice_vlan))
                    else:
                        get_add_vlan = self.get_select_element_port_type("voice_vlan_add_vlan")
                        if get_add_vlan:
                            self.auto_actions.click(get_add_vlan)
                            def _voice_vlan_appear():
                                return bool(self.get_select_element_port_type("voice_vlan_name_vlan"))

                            self.utils.wait_till(_voice_vlan_appear, is_logging_enabled=True)
                            get_name_vlan = self.get_select_element_port_type("voice_vlan_name_vlan")
                            if get_name_vlan:
                                self.auto_actions.send_keys(get_name_vlan, str(voice_vlan))
                            else:
                                self.utils.print_info("voice vlan get_id_vlan not found ")
                                return -1
                            get_id_vlan = self.get_select_element_port_type("voice_vlan_id_vlan")
                            if get_id_vlan:
                                self.auto_actions.send_keys(get_id_vlan, str(voice_vlan))
                            else:
                                self.utils.print_info("voice vlan get_id_vlan not found ")
                                return -1
                            get_save_vlan = self.get_select_element_port_type("save_vlan")
                            if get_save_vlan:
                                self.auto_actions.click(get_save_vlan)
                            else:
                                self.utils.print_info("get_save_vlan not found ")
                                return -1
                        else:
                            self.utils.print_info("voice vlan get_add_vlan not found ")
                            return -1
                else:
                    self.utils.print_info("voice vlan get_select_button not found ")
                    return -1
            else:
                self.utils.print_info("voice vlan won't be updated")

            data_vlan = kwargs.get("data_vlan")

            if isinstance(data_vlan, (str, int)):
                get_select_button = self.get_select_element_port_type("data_vlan_select_button")
                if get_select_button:
                    self.auto_actions.click(get_select_button)

                    self.utils.wait_till(delay=2, timeout=4)
                    get_dropdown_items = self.get_select_element_port_type("data_vlan_dropdown_items")
                    if self.auto_actions.select_drop_down_options(get_dropdown_items, str(data_vlan)):
                        self.utils.print_info(" Selected into dropdown value : ", str(data_vlan))
                    else:
                        get_add_vlan = self.get_select_element_port_type("data_vlan_add_vlan")
                        if get_add_vlan:
                            self.auto_actions.click(get_add_vlan)
                            def _data_vlan_appear():
                                return bool(self.get_select_element_port_type("data_vlan_name_vlan"))

                            self.utils.wait_till(_data_vlan_appear, is_logging_enabled=True)
                            get_name_vlan = self.get_select_element_port_type("data_vlan_name_vlan")
                            if get_name_vlan:
                                self.auto_actions.send_keys(get_name_vlan, str(data_vlan))
                            else:
                                self.utils.print_info("data vlan get_id_vlan not found ")
                                return -1
                            get_id_vlan = self.get_select_element_port_type("data_vlan_id_vlan")
                            if get_id_vlan:
                                self.auto_actions.send_keys(get_id_vlan, data_vlan)
                            else:
                                self.utils.print_info("data vlan get_id_vlan not found ")
                                return -1
                            get_save_vlan = self.get_select_element_port_type("save_vlan")
                            if get_save_vlan:
                                self.auto_actions.click(get_save_vlan)

                                def _save_vlan_disappear():
                                    return not bool(self.get_select_element_port_type("save_vlan"))

                                self.utils.wait_till(_save_vlan_disappear, is_logging_enabled=True)
                            else:
                                self.utils.print_info("get_save_vlan not found ")
                                return -1
                        else:
                            self.utils.print_info("data vlan get_add_vlan not found ")
                            return -1
                else:
                    self.utils.print_info("data vlan get_select_button not found ")
                    return -1
            else:
                self.utils.print_info("data vlan won't be updated")

            lldp_voice_options_flag = kwargs.get("lldp_voice_options_flag")

            if lldp_voice_options_flag is not None:
                lldp_voice_options = self.get_select_element_port_type("lldp_voice_vlan_options")
                if not lldp_voice_options:
                    self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox not found")
                    return -1
                previous_state_1 = lldp_voice_options.is_selected()
                self.utils.print_info(previous_state_1)
                if (not lldp_voice_options.is_selected() and lldp_voice_options_flag) or (
                        lldp_voice_options.is_selected() and not lldp_voice_options_flag):
                    self.auto_actions.click(lldp_voice_options)
                    def _lldp_voice_option():
                        return  not ((bool(lldp_voice_options.is_selected())) and previous_state_1)

                    self.utils.wait_till(_lldp_voice_option, is_logging_enabled=True,
                                         msg="lldp voice options toggled",delay =2, timeout=6)

            else:
                self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox won't be updated")

            cdp_voice_options_flag = kwargs.get("cdp_voice_options_flag")

            if cdp_voice_options_flag is not None:
                cdp_voice_options = self.get_select_element_port_type("cdp_voice_vlan_options")
                if not cdp_voice_options:
                    self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' checkbox not found")
                    return -1

                if (not cdp_voice_options.is_selected() and cdp_voice_options_flag) or (
                        cdp_voice_options.is_selected() and not cdp_voice_options_flag):
                    self.auto_actions.click(cdp_voice_options)
                    self.utils.wait_till(delay=2,timeout=6,msg="waiting for CDP options to get toggled")

            else:
                self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' checkbox won't be updated")

            lldp_voice_options = self.get_select_element_port_type("lldp_voice_vlan_options")
            if not lldp_voice_options:
                self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox not found")
                return -1

            lldp_voice_options_enabled = lldp_voice_options.is_selected()
            self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox is "
                                  f"{'enabled' if lldp_voice_options_enabled else 'disabled'}")

            dot1_vlan_id_flag = kwargs.get("dot1_vlan_id_flag")

            if isinstance(dot1_vlan_id_flag, bool):
                if not lldp_voice_options_enabled:
                    if not dot1_vlan_id_flag:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}' is already disabled")
                    else:
                        self.utils.print_info(
                            f"'{lldp_voice_vlan_options_checkbox_name}' checkbox is not enabled so we cannot update "
                            f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}'")
                        return -1
                else:
                    dot1_vlan_id_element = self.get_select_element_port_type("enable_lldp_advertisment_of_dot1_vlan")
                    previous_state_5 = dot1_vlan_id_element.is_selected()

                    if not dot1_vlan_id_element:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}' checkbox not found")
                        return -1

                    if (not dot1_vlan_id_element.is_selected() and dot1_vlan_id_flag) or (
                            dot1_vlan_id_element.is_selected() and not dot1_vlan_id_flag):
                        self.auto_actions.click(dot1_vlan_id_element)
                        def _dot1_vlan_id_element_():
                            return not (bool(dot1_vlan_id_element.is_selected()) and previous_state_5)

                        self.utils.wait_till(_dot1_vlan_id_element_, is_logging_enabled=True)
            else:
                self.utils.print_info(
                    f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}' checkbox won't be updated")

            lldp_advertisment_of_med_voice_vlan_flag = kwargs.get("lldp_advertisment_of_med_voice_vlan_flag")
            lldp_voice_vlan_dscp = kwargs.get("lldp_voice_vlan_dscp")

            if isinstance(lldp_advertisment_of_med_voice_vlan_flag, bool):
                if not lldp_voice_options_enabled:
                    if not lldp_advertisment_of_med_voice_vlan_flag:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' is already disabled")
                    else:
                        self.utils.print_info(
                            f"'{lldp_voice_vlan_options_checkbox_name}' checkbox is not enabled so "
                            f"we cannot update '{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}'")
                        return -1
                else:
                    lldp_advertisment_of_med_voice_vlan = self.get_select_element_port_type(
                        "enable_lldp_advertisment_of_med_voice_vlan")

                    if not lldp_advertisment_of_med_voice_vlan:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' checkbox not found")
                        return -1

                    if (
                            not lldp_advertisment_of_med_voice_vlan.is_selected() and lldp_advertisment_of_med_voice_vlan_flag) or \
                            (
                                    lldp_advertisment_of_med_voice_vlan.is_selected() and not lldp_advertisment_of_med_voice_vlan_flag):
                        self.auto_actions.click(lldp_advertisment_of_med_voice_vlan)
                        self.utils.wait_till(delay=2, timeout=6, msg="waiting for lldp advertisement options to get toggled")

                    if lldp_advertisment_of_med_voice_vlan.is_selected():
                        lldp_advertisment_of_med_voice_vlan_dscp_value_element = self.get_select_element_port_type(
                            "lldp_advertisment_of_med_voice_vlan_dscp_value")
                        if not lldp_advertisment_of_med_voice_vlan_dscp_value_element:
                            self.utils.print_info(
                                f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' checkbox not found")
                            return -1
                        else:
                            self.auto_actions.send_keys(lldp_advertisment_of_med_voice_vlan_dscp_value_element, 2)
            else:
                self.utils.print_info(f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' won't be updated")

            if isinstance(lldp_voice_vlan_dscp, (str, int)):

                lldp_advertisment_of_med_voice_vlan = self.get_select_element_port_type(
                    "enable_lldp_advertisment_of_med_voice_vlan")

                if not lldp_advertisment_of_med_voice_vlan:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' checkbox not found")
                    return -1

                if lldp_advertisment_of_med_voice_vlan.is_selected():
                    lldp_advertisment_of_med_voice_vlan_dscp_value_element = self.get_select_element_port_type(
                        "lldp_advertisment_of_med_voice_vlan_dscp_value")
                    if not lldp_advertisment_of_med_voice_vlan_dscp_value_element:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' checkbox not found")
                        return -1
                    else:
                        self.auto_actions.send_keys(lldp_advertisment_of_med_voice_vlan_dscp_value_element,
                                                    lldp_voice_vlan_dscp)
                else:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' is not enabled "
                        "so the dscp value cant be set")
                    return -1
            else:
                self.utils.print_info(
                    f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' dscp value won't be updated")

            lldp_advertisment_of_med_signaling_vlan_flag = kwargs.get("lldp_advertisment_of_med_signaling_vlan_flag")
            lldp_voice_signaling_dscp = kwargs.get("lldp_voice_signaling_dscp")

            if isinstance(lldp_advertisment_of_med_signaling_vlan_flag, bool):

                if not lldp_voice_options_enabled:
                    if not lldp_advertisment_of_med_signaling_vlan_flag:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' is already disabled")
                    else:
                        self.utils.print_info(
                            f"'{lldp_voice_vlan_options_checkbox_name}' checkbox is not enabled so we cannot "
                            f"update '{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' checkbox")
                        return -1
                else:
                    lldp_advertisment_of_med_signaling_vlan = self.get_select_element_port_type(
                        "enable_lldp_advertisment_of_med_voice_signaling_vlan")

                    if not lldp_advertisment_of_med_signaling_vlan:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' option not found")
                        return -1

                    if (
                            not lldp_advertisment_of_med_signaling_vlan.is_selected() and lldp_advertisment_of_med_signaling_vlan_flag) \
                            or (lldp_advertisment_of_med_signaling_vlan.is_selected()
                                and not lldp_advertisment_of_med_signaling_vlan_flag):
                        self.auto_actions.click(lldp_advertisment_of_med_signaling_vlan)
                        self.utils.wait_till(delay=2, timeout=6, msg="waiting for lldp advertisement medvoice  to get toggled")

                    if lldp_advertisment_of_med_signaling_vlan.is_selected():
                        lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element = self.get_select_element_port_type(
                            "lldp_advertisment_of_med_voice_signaling_vlan_dscp_value")
                        if not lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element:
                            self.utils.print_info(
                                f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' checkbox not found")
                            return -1
                        else:
                            self.auto_actions.send_keys(
                                lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element, 1)

            else:
                self.utils.print_info(
                    f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' won't be updated")

            if isinstance(lldp_voice_signaling_dscp, (str, int)):

                lldp_advertisment_of_med_signaling_vlan = self.get_select_element_port_type(
                    "enable_lldp_advertisment_of_med_voice_signaling_vlan")

                if not lldp_advertisment_of_med_signaling_vlan:
                    self.utils.print_info("enable_lldp_advertisment_of_med_voice_signaling_vlan option not found")
                    return -1

                if lldp_advertisment_of_med_signaling_vlan.is_selected():
                    lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element = self.get_select_element_port_type(
                        "lldp_advertisment_of_med_voice_signaling_vlan_dscp_value")
                    if not lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' option not found")
                        return -1
                    else:
                        self.auto_actions.send_keys(lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element,
                                                    lldp_voice_signaling_dscp)
                else:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' dscp value can't be set "
                        "because the checkbox is not selected")
                    return -1
            else:
                self.utils.print_info(
                    f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' dscp value won't be updated")

            cdp_voice_options = self.get_select_element_port_type("cdp_voice_vlan_options")
            if not cdp_voice_options:
                self.utils.print_info("cdp_voice_options option not found")
                return -1

            cdp_voice_options_enabled = cdp_voice_options.is_selected()
            self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' is "
                                  f"{'enabled' if cdp_voice_options_enabled else 'not enabled'}")

            cdp_advertisment_of_voice_vlan_flag = kwargs.get("cdp_advertisment_of_voice_vlan_flag")
            cdp_advertisment_of_power_available_flag = kwargs.get("cdp_advertisment_of_power_available_flag")

            if isinstance(cdp_advertisment_of_power_available_flag, bool):
                if not cdp_voice_options_enabled:
                    self.utils.print_info(
                        f"'{en_cdp_adv_of_power_available_checkbox_name}' can't be updated because "
                        f"'{cdp_voice_vlan_options_checkbox_name}' is not enabled")
                    return -1

                cdp_advertisment_of_power_available = self.get_select_element_port_type(
                    "enable_cdp_advertisment_of_power_available")
                if not cdp_advertisment_of_power_available:
                    self.utils.print_info("'{en_cdp_adv_of_power_available_checkbox_name}' checkbox not found")
                    return -1
                previous_state_6 = cdp_advertisment_of_power_available.is_selected()

                if (
                        not cdp_advertisment_of_power_available.is_selected() and cdp_advertisment_of_power_available_flag) or \
                        (
                                cdp_advertisment_of_power_available.is_selected() and not cdp_advertisment_of_power_available_flag):
                    self.auto_actions.click(cdp_advertisment_of_power_available)
                    def _cdp_power_available_vlan():
                        return not (bool(cdp_advertisment_of_power_available.is_selected()) and previous_state_6)

                    self.utils.wait_till(_cdp_power_available_vlan, is_logging_enabled=True)
            else:
                self.utils.print_info(f"'{en_cdp_adv_of_power_available_checkbox_name}' won't be updated")

            if isinstance(cdp_advertisment_of_voice_vlan_flag, bool):
                if not cdp_voice_options_enabled:
                    self.utils.print_info(
                        f"'{en_cdp_adv_of_voice_vlan_checkbox_name}' can't be updated because"
                        f" '{cdp_voice_vlan_options_checkbox_name}' is not enabled")
                    return -1

                cdp_advertisment_of_voice_vlan = self.get_select_element_port_type(
                    "enable_cdp_advertisment_of_voice_vlan")
                previous_state_7 = cdp_advertisment_of_voice_vlan.is_selected()

                if not cdp_advertisment_of_voice_vlan:
                    self.utils.print_info(f"{en_cdp_adv_of_voice_vlan_checkbox_name} checkbox not found")
                    return -1

                if (not cdp_advertisment_of_voice_vlan.is_selected() and cdp_advertisment_of_voice_vlan_flag) or \
                        (cdp_advertisment_of_voice_vlan.is_selected() and not cdp_advertisment_of_voice_vlan_flag):
                    self.auto_actions.click(cdp_advertisment_of_voice_vlan)
                    def _cdp_voice_vlan():
                        return not (bool(cdp_advertisment_of_voice_vlan.is_selected()) and previous_state_7)

                    self.utils.wait_till(_cdp_voice_vlan, is_logging_enabled=True)
            else:
                self.utils.print_info(f"'{en_cdp_adv_of_voice_vlan_checkbox_name}' won't be updated")
        else:
            self.utils.print_info("No change needed in the VLAN tab of the port type editor")

        transmission_tab_flags = [
            "enable_cdp_transmit_receive_flag", "enable_lldp_transmit_flag", "enable_lldp_receive_flag"
        ]

        if any(k in transmission_tab_flags for k in kwargs):
            transmission_tab = self.get_select_element_port_type("transmissionSettingsPage")
            if not transmission_tab:
                self.utils.print_info("Failed to get transmission settings page")
                return -1
            self.auto_actions.click(transmission_tab)
            self.utils.wait_till(delay=2, timeout=6, msg="waiting for transmission tab")

            enable_cdp_transmit_receive_flag = kwargs.get("enable_cdp_transmit_receive_flag")
            enable_lldp_transmit_flag = kwargs.get("enable_lldp_transmit_flag")
            enable_lldp_receive_flag = kwargs.get("enable_lldp_receive_flag")

            if isinstance(enable_cdp_transmit_receive_flag, bool):

                cdp_transmit_receive = self.get_select_element_port_type("cdp receive")
                if not cdp_transmit_receive:
                    self.utils.print_info(f"Failed to get '{en_cdp_transmit_receive_checkbox_name}' checkbox")
                    return -1

                if not cdp_transmit_receive.is_enabled():
                    if cdp_transmit_receive.is_selected() == enable_cdp_transmit_receive_flag:
                        self.utils.print_info(
                            f"'{en_cdp_transmit_receive_checkbox_name}' is already '{'enabled' if enable_cdp_transmit_receive_flag else 'disabled'}' "
                            "so no need to be updated (the checkbox is not editable)")
                    else:
                        self.utils.print_info(
                            f"'{en_cdp_transmit_receive_checkbox_name}' is not clickable so it won't be updated")
                        return -1
                else:
                    if (not cdp_transmit_receive.is_selected() and enable_cdp_transmit_receive_flag) or \
                            (cdp_transmit_receive and not enable_cdp_transmit_receive_flag):
                        self.auto_actions.click(cdp_transmit_receive)
                        self.utils.wait_till(delay=2,timeout=6,msg= "cdp transmit receive")
            else:
                self.utils.print_info(f"'{en_cdp_transmit_receive_checkbox_name}' won't be updated")

            if isinstance(enable_lldp_transmit_flag, bool):

                lldp_transmit = self.get_select_element_port_type("lldp transmit")
                if not lldp_transmit:
                    self.utils.print_info(f"Failed to get '{en_lldp_transmit_checkbox_name}' checkbox")
                    return -1

                if not lldp_transmit.is_enabled():
                    if lldp_transmit.is_selected() == enable_lldp_transmit_flag:
                        self.utils.print_info(
                            f"'{en_lldp_transmit_checkbox_name}' is already '{'enabled' if enable_lldp_transmit_flag else 'disabled'}' "
                            "so no need to be updated (the checkbox is not editable)")
                    else:
                        self.utils.print_info(
                            f"'{en_lldp_transmit_checkbox_name}' checkbox is not clickable so it won't be updated")
                        return -1
                else:
                    if (not lldp_transmit.is_selected() and enable_lldp_transmit_flag) or \
                            (lldp_transmit and not enable_lldp_transmit_flag):
                        self.auto_actions.click(lldp_transmit)
                        self.utils.wait_till(timeout=2,delay=2)
            else:
                self.utils.print_info(f"'{en_lldp_transmit_checkbox_name}' won't be updated")

            if isinstance(enable_lldp_receive_flag, bool):
                lldp_receive = self.get_select_element_port_type("lldp receive")
                if not lldp_receive:
                    self.utils.print_info(f"Failed to get {en_lldp_receive_checkbox_name} checkbox")
                    return -1

                if not lldp_receive.is_enabled():
                    if lldp_receive.is_selected() == enable_lldp_receive_flag:
                        self.utils.print_info(
                            f"'{en_lldp_receive_checkbox_name}' is already '{'enabled' if enable_lldp_receive_flag else 'disabled'}' "
                            "so no need to be updated (the checkbox is not editable)")
                    else:
                        self.utils.print_info(
                            f"'{en_lldp_receive_checkbox_name}' checkbox is not clickable so it won't be updated")
                        return -1
                else:
                    if (not lldp_receive.is_selected() and enable_lldp_receive_flag) or \
                            (lldp_receive and not enable_lldp_receive_flag):
                        self.auto_actions.click(lldp_receive)
                        self.utils.wait_till(timeout=2,delay=1)
            else:
                self.utils.print_info(f"'{en_lldp_receive_checkbox_name}' won't be updated")
        else:
            self.utils.print_info("No change needed in the Transmission Settings tab of the port type editor")

        summary_page = self.get_select_element_port_type("summaryPage")
        if not summary_page:
            self.utils.print_info("Failed to get summary page")
            return -1
        self.auto_actions.click(summary_page)
        def _wait_for_summary_tab_appear():
            return bool(self.get_select_element_port_type("summary_tab_confirmation")) \
                   and bool(self.dev360.get_close_port_type_box())

        self.utils.wait_till(_wait_for_summary_tab_appear, timeout=4, delay=1,
                             msg="Waiting for summary tab window to appear",
                             is_logging_enabled=True)
        close_button = self.dev360.get_close_port_type_box()
        if not close_button:
            self.utils.print_info("save button not found")
            return -1
        self.auto_actions.click(close_button)
        return 1

    def get_voice_port_summary(self, port_type_name):
        """
        Method used to get the summary of the voice port type related fields of the honeycomb summary tab at template level.
        args:
            :port_type_name:        <str>
        The method should be called from 'Configure -> Network Policies -> Network Policy -> Device Template -> Port Configuration'.
        returns: empty dict if the function fails or a dict which contains all the voice port type fields from the summary tab if the function does not fail.
        usage:
            >>> data = self.xiq.xflowsmanageDevice360.get_voice_port_summary("port_type_tcxm_19696")
            ...
            >>> print(json.dumps(data, indent=4))
            {
                "LLDP Advertisements": "ON",
                "802.1 VLAN and port protocol": "ON",
                "Med Voice VLAN DSCP Value": "OFF",
                "Med Voice Signaling DSCP Value": "2",
                "CDP Advertisement": "ON",
                "CDP Voice VLAN": "ON",
                "CDP Power Available": "OFF"
            }
        """
        rows = self.get_policy_configure_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
            return {}
        else:
            for row in rows:
                if re.search(rf'\d+\n{port_type_name}\n', row.text):
                    policy_edit_port_type = self.get_policy_edit_port_type(row)
                    if policy_edit_port_type:
                        self.utils.print_info("The button policy_edit_port_type from policy  was found")
                        self.auto_actions.click(policy_edit_port_type)

                        def _check_port_editor_window_present():
                            return bool(self.get_select_element_port_type("tab_vlan"))

                        self.utils.wait_till(_check_port_editor_window_present, timeout=10, delay=1,
                                             msg="Waiting for existing port type window to appear",
                                             is_logging_enabled=True)
                        break
                    else:
                        self.utils.print_info("The button policy_edit_port_type from policy  was not found")
                        self.screen.save_screen_shot()
                        return {}

        summary_page = self.get_select_element_port_type("summaryPage")
        if not summary_page:
            self.utils.print_info("Failed to get summary page")
            return {}
        self.auto_actions.click(summary_page)
        self.utils.wait_till(delay=2, timeout=4, msg = "waiting at summary page..")
        ret = {}
        for row_name, row_value in zip(
                [
                    "LLDP Advertisements",
                    "802.1 VLAN and port protocol",
                    "Med Voice VLAN DSCP Value",
                    "Med Voice Signaling DSCP Value",
                    "CDP Advertisement",
                    "CDP Voice VLAN",
                    "CDP Power Available",
                    "Voice VLAN",
                    "Data VLAN"
                ],
                [
                    "port_type_voice_lldp_advertisment_summary",
                    "802_1_vlan_and_port_protocol_summary",
                    "med_voice_vlan_dscp_value_summary",
                    "med_voice_signaling_dscp_value_summary",
                    "cdp_advertisment_summary",
                    "cdp_voice_vlan_summary",
                    "cdp_power_available_summary",
                    "voice_vlan_summary",
                    "data_vlan_summary"
                ]
        ):
            ret[row_name] = self.get_select_element_port_type_summary(row_value).text

        close_button = self.dev360.get_close_port_type_box()
        if not close_button:
            self.utils.print_info("save button not found")
            return {}
        self.auto_actions.click(close_button)

        return ret

    def device360_voip_get_port_row(self, port_name):
        """
        - Get the port row object matching the specified port_name from Device360 --> Configure --> Port Configuration
        :param port_name: name of the port to return the row for
        :return: row element if row exists else return None
        """
        ret_val = None
        self.utils.print_info("Getting the Port rows from the Device360 Port Configuration page")
        rows = self.get_device360_voip_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
        else:
            for row in rows:
                self.utils.print_info("rowtext =>", row.text)
                if port_name in row.text:
                    ret_val = row
                    self.utils.print_info("rowtext =>", row.text)
                    break
        return ret_val

    def edit_voip_in_d360(self,port, **kwargs):
        #Navigating to Voice tab
        """
        This method is to edit the VOIP in d360
        :param port: name of the port to return
       The method should be called from 'Configure -> D360 -> Port configuration -> VOIP tab'.
        args:
            :port:                                            <str>
        kwargs:
            :lldp_voice_options_flag:                         <bool|None>
            :cdp_voice_options_flag:                          <bool|None>
            :dot1_vlan_id_flag:                               <bool|None>
            :lldp_advertisment_of_med_voice_vlan_flag:        <bool|None>
            :lldp_advertisment_of_med_signaling_vlan_flag:    <bool|None>
            :cdp_advertisment_of_voice_vlan_flag:             <bool|None>
            :cdp_advertisment_of_power_available_flag:        <bool|None>
            :enable_cdp_transmit_receive_flag:                <bool|None>
            :enable_lldp_transmit_flag:                       <bool|None>
            :enable_lldp_receive_flag:                        <bool|None>
            :lldp_voice_vlan_dscp:                            <int>
            :lldp_voice_signaling_dscp:                       <int>
        returns: 1 if the functions call is successfull else -1
        usage:
            self.xiq.xflowsmanageDevice360.edit_voip_in_d360(
                enable_lldp_receive_flag=True, cdp_voice_options_flag=True)
            # enables 'Enable LLDP Receive', enables 'Enable CDP Voice VLAN Options'
            self.xiq.xflowsmanageDevice360.edit_voip_in_d360( lldp_voice_vlan_dscp=12, lldp_voice_signaling_dscp=14)
            # updates dscp values
        :return:
        """
        voip_tab = self.dev360.get_device360_voip_tab()
        if voip_tab:
            self.auto_actions.click(voip_tab)
        else:
            return -1

        self.utils.wait_till(delay=2,timeout=4)
        port_voice_tab_content = self.dev360.get_device360_voip_tab_data()
        if port_voice_tab_content:
            port_row = self.device360_voip_get_port_row(port)
            if port_row:
                self.utils.print_info("Found port row")
                self.utils.print_info(port_row)
            else:
                return -1
            vlan_tab_flags = [
                "voice_vlan", "data_vlan", "lldp_voice_options_flag", "cdp_voice_options_flag", "dot1_vlan_id_flag",
                "lldp_advertisment_of_med_voice_vlan_flag", "lldp_advertisment_of_med_signaling_vlan_flag",
                "cdp_advertisment_of_voice_vlan_flag", "cdp_advertisment_of_power_available_flag",
                "lldp_voice_vlan_dscp",
                "lldp_voice_signaling_dscp"
            ]

            lldp_voice_vlan_options_checkbox_name = "LLDP Voice VLAN Options"
            cdp_voice_vlan_options_checkbox_name = "CDP Voice VLAN Options"

            en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name = "Enable LLDP advertisement of 802.1 VLAN ID and port protocol of Voice VLAN"
            en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name = "Enable LLDP advertisement of med Voice VLAN DSCP Value"
            en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name = "Enable LLDP advertisement of med Voice Signaling VLAN DSCP Value"
            en_cdp_adv_of_voice_vlan_checkbox_name = "Enable CDP advertisement of Voice VLAN"
            en_cdp_adv_of_power_available_checkbox_name = "Enable CDP advertisement of power available"

            lldp_voice_options_flag = kwargs.get("lldp_voice_options_flag")
            if any(k in vlan_tab_flags for k in kwargs):

                if lldp_voice_options_flag is not None:

                    lldp_voice_options = self.dev360.get_device360_vlan_lldp_capabilities(port_row)
                    if not lldp_voice_options:
                        self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox not found")
                        return -1
                    previous_state_1 = lldp_voice_options.is_selected()

                    if (not lldp_voice_options.is_selected() and lldp_voice_options_flag) or (
                            lldp_voice_options.is_selected() and not lldp_voice_options_flag):
                        self.auto_actions.click(lldp_voice_options)
                        self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' updated as true")
                        def _lldp_voice_option():
                            return not ((bool(lldp_voice_options.is_selected())) and previous_state_1)

                        self.utils.wait_till(_lldp_voice_option, is_logging_enabled=True,
                                             msg="lldp voice options toggled", delay=2, timeout=6)
                else:
                    self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox won't be updated")
                cdp_voice_options_flag = kwargs.get("cdp_voice_options_flag")
                cdp_voice_options = self.dev360.get_d360_port_voice_vlan_cdp_capabilities(port_row)

                if cdp_voice_options_flag is not None:
                    cdp_voice_options = self.dev360.get_d360_port_voice_vlan_cdp_capabilities(port_row)
                    self.utils.print_info(cdp_voice_options,cdp_voice_options.is_selected())
                    if not cdp_voice_options:
                        self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' checkbox not found")
                        return -1

                    if (not cdp_voice_options.is_selected() and cdp_voice_options_flag) or (
                            cdp_voice_options.is_selected() and not cdp_voice_options_flag):
                        self.auto_actions.click(cdp_voice_options)
                        self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' checkbox is updated")
                        self.utils.wait_till(delay=2,timeout=6,msg="waiting for CDP options to get toggled")

                    self.utils.print_info("Not doing anything==")
                else:
                    self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' checkbox won't be updated")

                lldp_voice_options = self.dev360.get_device360_vlan_lldp_capabilities(port_row)
                if not lldp_voice_options:
                    self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox not found")
                    return -1

                lldp_voice_options_enabled = lldp_voice_options.is_selected()
                self.utils.print_info(f"'{lldp_voice_vlan_options_checkbox_name}' checkbox is "
                                      f"{'enabled' if lldp_voice_options_enabled else 'disabled'}")
                dot1_vlan_id_flag = kwargs.get("dot1_vlan_id_flag")

                if isinstance(dot1_vlan_id_flag, bool):
                    if not lldp_voice_options_enabled:
                        if not dot1_vlan_id_flag:
                            self.utils.print_info(
                                f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}' is already disabled")
                        else:
                            self.utils.print_info(
                                f"'{lldp_voice_vlan_options_checkbox_name}' checkbox is not enabled so we cannot update "
                                f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}'")
                            return -1
                    else:
                        dot1_vlan_id_element = self.dev360.get_device360_802_1_voice_vlan(port_row)
                        previous_state_5 = dot1_vlan_id_element.is_selected()

                        if not dot1_vlan_id_element:
                            self.utils.print_info(
                                f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}' checkbox not found")
                            return -1

                        if (not dot1_vlan_id_element.is_selected() and dot1_vlan_id_flag) or (
                                dot1_vlan_id_element.is_selected() and not dot1_vlan_id_flag):
                            self.auto_actions.click(dot1_vlan_id_element)
                            def _dot1_vlan_id_element_():
                                return not (bool(dot1_vlan_id_element.is_selected()) and previous_state_5)

                            self.utils.wait_till(_dot1_vlan_id_element_, is_logging_enabled=True)

                else:
                        self.utils.print_info(
                        f"'{en_lldp_adv_of_802_port_protocol_of_voice_vlan_checkbox_name}' checkbox won't be updated")
                lldp_voice_vlan_dscp = kwargs.get("lldp_voice_vlan_dscp")

                if isinstance(lldp_voice_vlan_dscp, (str, int)):

                    lldp_advertisment_of_med_voice_vlan_dscp_value_element = self.dev360.get_d360_port_voice_vlan_med_dscp(port_row)
                    if not lldp_advertisment_of_med_voice_vlan_dscp_value_element:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' checkbox not found")
                        return -1
                    else:
                        self.auto_actions.send_keys(lldp_advertisment_of_med_voice_vlan_dscp_value_element,
                                                    lldp_voice_vlan_dscp)

                else:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_vlan_dscp_value_checkbox_name}' dscp value won't be updated")

                lldp_voice_signaling_dscp = kwargs.get("lldp_voice_signaling_dscp")

                if isinstance(lldp_voice_signaling_dscp, (str, int)):

                    lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element = self.dev360.get_d360_port_voice_vlan_med_sig_dscp(port_row)

                    if not lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element:
                        self.utils.print_info(
                            f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' option not found")
                        return -1
                    else:
                        self.auto_actions.send_keys(lldp_advertisment_of_med_voice_signaling_vlan_dscp_value_element,
                                                    lldp_voice_signaling_dscp)
                else:
                    self.utils.print_info(
                        f"'{en_lldp_adv_of_med_voice_signaling_vlan_dscp_value_checkbox_name}' dscp value can't be set "
                        "because the checkbox is not selected")

                cdp_voice_options_enabled = cdp_voice_options.is_selected()
                self.utils.print_info(f"'{cdp_voice_vlan_options_checkbox_name}' is "
                                      f"{'enabled' if cdp_voice_options_enabled else 'not enabled'}")
                cdp_advertisment_of_voice_vlan_flag = kwargs.get("cdp_advertisment_of_voice_vlan_flag")
                cdp_advertisment_of_power_available_flag = kwargs.get("cdp_advertisment_of_power_available_flag")

                if cdp_advertisment_of_power_available_flag is not None:

                    if not cdp_voice_options_enabled:
                        self.utils.print_info(
                            f"'{en_cdp_adv_of_power_available_checkbox_name}' can't be updated because "
                            f"'{cdp_voice_vlan_options_checkbox_name}' is not enabled")
                        return -1

                    cdp_advertisment_of_power_available = self.dev360.get_d360_advert_power_available(port_row)
                    if not cdp_advertisment_of_power_available:
                        self.utils.print_info("'{en_cdp_adv_of_power_available_checkbox_name}' checkbox not found")
                        return -1
                    previous_state_6 = cdp_advertisment_of_power_available.is_selected()

                    if ( not cdp_advertisment_of_power_available.is_selected() and cdp_advertisment_of_power_available_flag) or \
                            ( cdp_advertisment_of_power_available.is_selected() and not cdp_advertisment_of_power_available_flag):
                        self.auto_actions.click(cdp_advertisment_of_power_available)
                        def _cdp_power_available_vlan():
                            return not (bool(cdp_advertisment_of_power_available.is_selected()) and previous_state_6)

                        self.utils.wait_till(_cdp_power_available_vlan, is_logging_enabled=True)
                else:
                    self.utils.print_info(f"'{en_cdp_adv_of_power_available_checkbox_name}' won't be updated")

                if cdp_advertisment_of_voice_vlan_flag is not None:

                    if not cdp_voice_options_enabled:
                        self.utils.print_info(
                            f"'{en_cdp_adv_of_voice_vlan_checkbox_name}' can't be updated because"
                            f" '{cdp_voice_vlan_options_checkbox_name}' is not enabled")
                        return -1

                    cdp_advertisment_of_voice_vlan = self.dev360.get_d360_cdp_voice_vlan(port_row)
                    previous_state_7 = cdp_advertisment_of_voice_vlan.is_selected()

                    if not cdp_advertisment_of_voice_vlan:
                        self.utils.print_info(f"{en_cdp_adv_of_voice_vlan_checkbox_name} checkbox not found")
                        return -1

                    if (not cdp_advertisment_of_voice_vlan.is_selected() and cdp_advertisment_of_voice_vlan_flag) or \
                            (cdp_advertisment_of_voice_vlan.is_selected() and not cdp_advertisment_of_voice_vlan_flag):
                        self.auto_actions.click(cdp_advertisment_of_voice_vlan)
                        def _cdp_voice_vlan():
                            return not (bool(cdp_advertisment_of_voice_vlan.is_selected()) and previous_state_7)

                        self.utils.wait_till(_cdp_voice_vlan, is_logging_enabled=True)
                else:
                    self.utils.print_info(f"'{en_cdp_adv_of_voice_vlan_checkbox_name}' won't be updated")
            else:
                self.utils.print_info("No change needed in the VLAN tab of the port type editor")

    def d360_assign_port_type(self, port_type, port_numbers, **kwargs):
        port_conf_content = self.dev360.get_device360_port_configuration_content()
        if port_conf_content and port_conf_content.is_displayed():
            for port_number in port_numbers.split(','):
                port_row = self.device360_get_port_row(port_number)
                if port_row:
                    self.utils.print_debug("Found row for port: ", port_row.text)
                    self.utils.print_info("click Port Usage drop down")
                    self.utils.wait_till(delay=1, timeout=2)
                    drop_down_button = self.dev360.get_device360_configure_port_usage_drop_down_button(port_row)
                    self.auto_actions.click(drop_down_button)
                    self.utils.wait_till(delay=1, timeout=2)
                    if self.dev360.get_device360_configure_port_usage_drop_down_options_presence(port_row):
                        options = self.dev360.get_d360_port_type_options(port_row)
                        self.utils.wait_till(delay=1, timeout=2)
                        self.utils.print_info("drop down options", options)
                        self.auto_actions.select_drop_down_options(options, port_type)

                        kwargs['pass_msg'] = "Successfully selected port"
                        self.common_validation.passed(**kwargs)
                        return 1

                    else:
                        self.utils.print_info("Port usage drop down didnot present,")
                        kwargs['fail_msg'] = "Port usage drop down is not present"
                        self.common_validation.failed(**kwargs)
                        return -1

    def add_new_pse_profile_from_port_type_page_button(self, **kwargs):
        '''
        This keyword click on new pse profile button from pse tab from port type page
        :return: 1 if button has been found; else -1
        '''

        get_pse_profile_add = self.get_select_element_port_type("pse_profile_add")
        if get_pse_profile_add:
            self.utils.print_info("pse_profile_add has been found ")
            self.auto_actions.click(get_pse_profile_add)
        else:
            self.utils.print_info("pse_profile_add not found ")
            kwargs['fail_msg'] = "pse_profile_add not found"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully clicked on new pse profile button from pse tab from port type page"
        self.common_validation.passed(**kwargs)
        return 1

    def create_new_pse_profile_from_port_type_page(self, value, **kwargs):
        '''
        This keyword create new pse profile from port type page

        :param value:
        'value': {'pse_profile_name': pse_profile_name,
                 'pse_profile_power_mode': pse_profile_power_mode,
                 'pse_profile_power_limit': pse_profile_power_limit,
                 'pse_profile_priority': pse_profile_priority,
                 'pse_profile_description': pse_profile_description
                 }
        :return: 1 if profile has been created ; else -1
        '''

        if not self.add_new_pse_profile_from_port_type_page_button() == 1:
            kwargs['fail_msg'] = "Could not create pse profile"
            self.common_validation.failed(**kwargs)
            return -1
        if not self.fill_in_pse_profile_fields(value) == 1:
            kwargs['pass_msg'] = "pse profile has been created"
            self.common_validation.passed(**kwargs)
            return -1
        return 1

    def fill_in_pse_profile_fields(self, value, **kwargs):
        '''
        This keyword fill in all fields when pse profile is created and save the profile

        :param value:
        'value': {'pse_profile_name': pse_profile_name,
                 'pse_profile_power_mode': pse_profile_power_mode,
                 'pse_profile_power_limit': pse_profile_power_limit,
                 'pse_profile_priority': pse_profile_priority,
                 'pse_profile_description': pse_profile_description
                 }
        :return: 1 if successfully ; else -1
        '''

        get_pse_profile_name = self.get_select_element_port_type("pse_profile_name")
        if get_pse_profile_name:
            self.auto_actions.send_keys(get_pse_profile_name, value['pse_profile_name'])
            self.auto_actions.click(get_pse_profile_name)
        else:
            self.utils.print_info("get_pse_profile_name not found ")
            kwargs['fail_msg'] = "get_pse_profile_name not found"
            self.common_validation.failed(**kwargs)
            return -1

        get_pse_profile_power_mode_dropdown = self.get_select_element_port_type(
            'pse_profile_power_mode_dropdown')
        if get_pse_profile_power_mode_dropdown:
            self.screen.save_screen_shot()
            self.auto_actions.click(get_pse_profile_power_mode_dropdown)
            self.screen.save_screen_shot()
            get_pse_profile_power_mode_items = self.get_select_element_port_type(
                "pse_profile_power_mode_items")
            self.screen.save_screen_shot()
            if self.auto_actions.select_drop_down_options(get_pse_profile_power_mode_items,
                                                          value['pse_profile_power_mode']):
                self.utils.print_info(" Selected into dropdown value : ",
                                      value['pse_profile_power_mode'])
            else:
                kwargs['fail_msg'] = "Can not select into drop down"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Can not click on drop down"
            self.common_validation.fault(**kwargs)
            return -1

        get_pse_profile_power_limit = self.get_select_element_port_type("pse_profile_power_limit")
        if get_pse_profile_power_limit:
            self.auto_actions.send_keys(get_pse_profile_power_limit, value['pse_profile_power_limit'])
        else:
            kwargs['fail_msg'] = "Power Limit textbox not found!"
            self.common_validation.fault(**kwargs)
            return -1

        get_pse_profile_priority_dropdown = self.get_select_element_port_type("pse_profile_priority")
        if get_pse_profile_priority_dropdown:
            self.auto_actions.click(get_pse_profile_priority_dropdown)
            get_pse_profile_priority_items = self.get_select_element_port_type(
                "pse_profile_priority_items")
            if get_pse_profile_priority_items:
                if self.auto_actions.select_drop_down_options(get_pse_profile_priority_items,
                                                              value['pse_profile_priority']):
                    self.utils.print_info(" Selected into dropdown value : ", value['pse_profile_priority'])
                else:
                    kwargs['fail_msg'] = "fill_in_pse_profile_fields() -> Cannot select into dropdown"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Cannot select into dropdown"
                self.common_validation.fault(**kwargs)
                return -1

        else:
            kwargs['fail_msg'] = "Cannot select element port type"
            self.common_validation.fault(**kwargs)
            return -1

        get_pse_profile_description = self.get_select_element_port_type("pse_profile_description")
        if get_pse_profile_description:
            self.auto_actions.send_keys(get_pse_profile_description, value['pse_profile_description'])
        else:
            kwargs['fail_msg'] = "get_pse_profile_description not found"
            self.common_validation.failed(**kwargs)
            return -1

        def _check_save_pse_profile_closure():
            if not self.get_select_element_port_type("pse_profile_save"):
                self.utils.print_info("PSE profile save button not present anymore.")
                return True
            else:
                self.utils.print_info("PSE profile save button is still present. Retrying to save...")
                get_pse_profile_save = self.get_select_element_port_type("pse_profile_save")
                if get_pse_profile_save:
                    self.auto_actions.click(get_pse_profile_save)
                else:
                    self.utils.print_info("get_pse_profile_save not found")
                return False

        get_pse_profile_save = self.get_select_element_port_type("pse_profile_save")
        if get_pse_profile_save:
            self.auto_actions.click(get_pse_profile_save)
            # Check if error is displayed after save
            get_pse_profile_save_error = self.get_select_element_port_type("pse_profile_save_error")
            if get_pse_profile_save_error:

                self.utils.print_info("Below error is displayed after save profile:" , get_pse_profile_save_error)
                kwargs['fail_msg'] = "fill_in_pse_profile_fields() -> get_pse_profile_save not found"
                self.common_validation.failed(**kwargs)
                return -1
            self.utils.wait_till(_check_save_pse_profile_closure, is_logging_enabled=True, timeout=60,
                                 delay=5, silent_failure=False, msg="Waiting for port type profile to "
                                                                   "save...")
            self.screen.save_screen_shot()
            kwargs['pass_msg'] = "Profile saved"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "get_pse_profile_save not found"
            self.common_validation.failed(**kwargs)
            return -1

    def device360_edit_select_or_add_new_pse_profile(self, mode, port_number, poe_profile=None, **kwargs):
        '''
        This keyword edit,select or add new pse profile from port configuration page

        :param mode: Specify the modes : edit, select or add
        :param port_number: port
        :param poe_profile: pse profile name
        :return: 1 if successfully ; else -1
        '''
        port_rows = self.get_device360_configure_port_pse_rows()
        if port_rows:
            for port_row in port_rows:
                get_interface = self.get_device360_port_configuration_pse_profile_port_interface(port_row)
                if port_number in get_interface.text:
                    self.utils.print_info("Found row for port: ", port_row.text)
                    if mode == 'select':
                        if poe_profile:
                            self.utils.print_info("clicking POE Profile Select Button")
                            select_button = self.get_device360_port_configuration_pse_profile_select_button(port_row)
                            if select_button:
                                self.auto_actions.click(select_button)
                                self.screen.save_screen_shot()
                            else:
                                self.utils.print_info("select_button not found")
                                kwargs['fail_msg'] = "select_button " \
                                                     "not found "
                                self.common_validation.fault(**kwargs)
                                return -1
                            self.utils.print_info(f"Selecting POE Profile Option : {poe_profile}")
                            items = self.get_device360_port_configuration_pse_profile_select_options()
                            if items:
                                self.auto_actions.move_to_element(items[-1])
                                self.screen.save_screen_shot()

                            if self.auto_actions.select_drop_down_options(
                                    items, poe_profile):
                                self.utils.print_info("Pse profile has been selected")
                                self.screen.save_screen_shot()
                                kwargs['pass_msg'] = "Pse profile has been selected"
                                self.common_validation.passed(**kwargs)
                                return 1
                    elif mode == 'add':
                        self.utils.print_info("clicking POE Profile ADD Button")
                        add_button = self.get_device360_port_configuration_pse_profile_add_button(port_row)
                        if add_button:
                            self.auto_actions.click(add_button)
                            kwargs['pass_msg'] = "POE Profile is added"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['fail_msg'] = "add_button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                    elif mode == 'edit':
                        if poe_profile:
                            self.utils.print_info("clicking POE Profile Select Button")
                            select_button = self.get_device360_port_configuration_pse_profile_select_button(port_row)
                            if select_button:
                                self.auto_actions.click(select_button)
                                self.screen.save_screen_shot()
                            else:
                                kwargs['fail_msg'] = "select_button not found"
                                self.common_validation.fault(**kwargs)
                                return -1
                            self.utils.print_info(f"Selecting POE Profile Option : {poe_profile}")
                            if self.auto_actions.select_drop_down_options(self.get_device360_port_configuration_pse_profile_select_options(), poe_profile):
                                self.utils.print_info("Pse profile has been selected")
                                self.screen.save_screen_shot()
                        sleep(5)
                        self.utils.print_info("clicking POE Profile EDIT Button")
                        edit_button = self.get_device360_port_configuration_pse_profile_edit_button(port_row)
                        if edit_button:
                            self.auto_actions.click(edit_button)
                            kwargs['pass_msg'] = "clicked POE Profile EDIT Button"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['fail_msg'] = "edit_button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "The selected mode is not valid"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    pass
        else:
            self.utils.print_info("Can not get rows")

        kwargs['fail_msg'] = "Can not get rows"
        self.common_validation.fault(**kwargs)
        return -1

    def port_type_nav_to_summary_page_and_save(self, **kwargs):
        '''
        This keyword navigate to summary page into port type page and save it .
        :return: 1 if successfully ; else -1
        '''

        summary_tab = self.get_select_element_port_type("summaryPage")
        if summary_tab:
            self.auto_actions.click(summary_tab)
            save_port_type_box = self.get_common_save_button()
            if save_port_type_box:
                self.utils.print_info(" The button close_port_type_box from policy was found")
                self.auto_actions.click(save_port_type_box)
                kwargs['pass_msg'] = "Port type was saved"
                self.common_validation.passed(**kwargs)
                return True
            else:
                self.utils.print_info("save button not found")
                kwargs['fail_msg'] = "port_type_nav_to_summary_page_and_save() -> save button not found"
                self.common_validation.failed(**kwargs)
                return False

        else:
            self.utils.print_info("Summary tab not found")
            kwargs['fail_msg'] = "Summary tab not found"
            self.common_validation.failed(**kwargs)
            return False

    def banner_message_after_save_config(self):
        '''
            This keyword return the message displayed after a config is saved.
            It can be use after save a template, policy or device360 page
        :return: messages which are displayed ; None if no message is displayed
        '''

        message = self.sw_template_web_elements.get_sw_template_error_message()
        if message:
            return message
        else:
            self.screen.save_screen_shot()
            return None

    def device360_navigate_to_pse_tab(self, **kwargs):
        '''
        This keyword navigate to pse tab from device360 page
        :return: 1 if successfully ; else -1
        '''

        port_conf_btn = self.get_device360_configure_port_configuration_button()
        if port_conf_btn:
            self.utils.print_info("Click PortConfiguration Button")
            self.auto_actions.click(port_conf_btn)
        else:
            self.utils.print_info("PortConfiguration Button was not found ")
            kwargs['fail_msg'] = "PortConfiguration Button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        self.utils.wait_till(self.get_device360_port_configuration_pse_tab, timeout=20, delay=1, is_logging_enabled=True )
        pse_tab_button = self.get_device360_port_configuration_pse_tab()
        if pse_tab_button:
            self.utils.print_info("Click PSE Tab")
            self.auto_actions.click(pse_tab_button)
        else:
            self.utils.print_info("PSE Tab was not found ")
            kwargs['fail_msg'] = "PSE Tab was not found"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully navigated to pse tab from device360 page"
        self.common_validation.passed(**kwargs)
        return 1

    def common_cancel_button(self, **kwargs):
        '''
        This keyword push the cancel button. It can be use in all pages where cancel button is displayed
        :return: 1 if succesfully ; else -1
        '''
        cancel_button = self.get_common_cancel_button()
        if cancel_button:
            self.utils.print_info("Click cancel button")
            self.auto_actions.click(cancel_button)
            kwargs['pass_msg'] = "Clicked cancel button"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("cancel button not found")
            kwargs['fail_msg'] = "cancel button not found"
            self.common_validation.failed(**kwargs)
            return -1

    def poe_pse_profiles_elements(self, element):
        '''
        This keyword returns the web elements returned by get_select_element_port_type function from Device360WebElements.py
        :param element: Specify the element. See get_select_element_port_type function
        :return: web element if it has been found; None if element was not found
        '''
        return self.get_select_element_port_type(element)

    def multi_edit_d360_port_config(self):
        '''
        This keyword push the multi edit button.
        :return: 1 if succesfully ; else -1
        '''
        self.utils.print_info("Click multi edit button")
        self.auto_actions.click_reference(self.get_d360_monitor_port_details_edit)

    def fill_port_details_multi_edit_fields(self, port_state=None, port_usage=None, description=None, **kwargs):
        '''
        This keyword fill in all fields when port settings are configured for multiple ports from multi edit tab
        :args:
                 'port_state': ON/OFF - mandatory,
                 'port_usage': port_usage_mode - mandatory,
                 'description': description - mandatory
            kwargs:
                 'vlan_access_port': vlan_value - used for Access Port,
                 'native_vlan_trunk_port': vlan_native - used for Trunk Port,
                 'allowed_vlan_trunk_port' : vlan_allowed - used for Trunk Port,
                 'voice_vlan_phone_port' : voice_vlan - used for Phone with a Data Port,
                 'data_vlan_phone_port' : Data_vlan - used for Phone with a Data Port,

        Keyword Usage:
            - depending on the port_usage value, kwargs args can be used as following:
                case1: for port_usage: Access Port the following args are needed:
                    - port_state, vlan_access_port, description;
                case2: for port_usage: Trunk Port the following args are needed:
                    - port_state, native_vlan_trunk_port, allowed_vlan_trunk_port, description;
                case3: for port_usage: Phone Port the following args are needed:
                    - port_state, voice_vlan_phone_port, data_vlan_phone_port, description;
        e.g. xiq_library_at_class_level.xflowsmanageDevice360.fill_port_details_multi_edit_fields
        (port_usage='Access Port',vlan_access_port=500,port_state='OFF',description='Description for multiple ports')
        '''

        vlan_access_port = kwargs.get("vlan_access_port")
        self.utils.print_info(vlan_access_port)

        native_vlan_trunk_port = kwargs.get("native_vlan_trunk_port")
        self.utils.print_info(native_vlan_trunk_port)

        allowed_vlan_trunk_port = kwargs.get("allowed_vlan_trunk_port")
        self.utils.print_info(allowed_vlan_trunk_port)

        voice_vlan_phone_port = kwargs.get("voice_vlan_phone_port")
        self.utils.print_info(voice_vlan_phone_port)

        data_vlan_phone_port = kwargs.get("data_vlan_phone_port")
        self.utils.print_info(data_vlan_phone_port)

        if port_state is not None:

            """
             - This keyword will select Port State in Multi Edit (D360-Port Configuration)
                and after that will put the port to OFF;
            """
            self.utils.print_info("Click on Port State checkbox")
            self.auto_actions.click_reference(self.get_multi_edit_checkbox_status)

            self.utils.print_info("Clicking Port State toggle to Off")
            self.auto_actions.click_reference(self.get_multi_edit_status_toggle)

        if port_usage is not None:
            """
             - This keyword will select Port Usage in Multi Edit (D360-Port Configuration)
            """
            checkbox = self.get_multi_edit_checkbox_port_type()
            if checkbox:
                if checkbox.is_selected():
                    kwargs['pass_msg'] = "The Port Usage is checked!"
                    self.common_validation.passed(**kwargs)
                else:
                    self.utils.print_info("Click on Port Usage checkbox")
                    self.auto_actions.click_reference(self.get_multi_edit_checkbox_port_type)
                    kwargs['pass_msg'] = "The Port Usage was checked successfully"
                    self.common_validation.passed(**kwargs)
            else:
                kwargs['fail_msg'] = "Unable to click the element"
                self.common_validation.failed(**kwargs)

            get_port_usage_mode_dropdown = self.get_multi_edit_port_type_dropdown()

            if get_port_usage_mode_dropdown:
                self.auto_actions.click_reference(self.get_multi_edit_port_type_dropdown)
                get_port_usage_items = self.get_multi_edit_port_type_drop_down_list()
                if self.auto_actions.select_drop_down_options(get_port_usage_items,
                                                              port_usage):
                    self.utils.print_info(" Selected into dropdown value : ",port_usage)

                    if port_usage == 'Access Port':
                        if vlan_access_port is not None:
                            """
                             - This keyword will select Vlan in Multi Edit when Port usage is Access Port
                             (D360 - Port Configuration) and after that will complete the field with one value
                            """
                            self.utils.print_info("Click on VLAN checkbox when Port Usage is Access Port")
                            self.auto_actions.click_reference(self.get_multi_edit_checkbox_vlan)

                            get_multi_edit_vlan = self.get_multi_edit_vlan_input()
                            if get_multi_edit_vlan:
                                self.auto_actions.send_keys(get_multi_edit_vlan, Keys.CONTROL + "a")
                                self.utils.print_info("Deleting the selected")
                                self.auto_actions.send_keys(get_multi_edit_vlan, Keys.BACK_SPACE)
                                self.utils.print_info("Configuring new vlan values")
                                self.auto_actions.send_keys(get_multi_edit_vlan, vlan_access_port)
                            else:
                                self.utils.print_info("get_multi_edit_vlan cannot be completed ")
                                return -1

                    elif port_usage == 'Trunk Port':
                        if (native_vlan_trunk_port is not None) or (allowed_vlan_trunk_port is not None):
                            """
                             - This keyword will select Vlan settings in Multi Edit when Port usage is Trunk Port
                             (D360 - Port Configuration) and after that will complete the fields with values
                            """
                            self.utils.print_info("Click on Native VLAN checkbox when Port Usage is Trunk Port")
                            self.auto_actions.click_reference(self.get_d360_multi_edit_checkbox_native_vlan)

                            self.utils.print_info("Click on Allowed VLAN checkbox when Port Usage is Trunk Port")
                            self.auto_actions.click_reference(self.get_d360_multi_edit_checkbox_allowed_vlan)

                        if native_vlan_trunk_port is not None:

                            get_multi_edit_native_vlan = self.get_d360_multi_edit_native_vlan_input()
                            if get_multi_edit_native_vlan:
                                self.auto_actions.send_keys(get_multi_edit_native_vlan, Keys.CONTROL + "a")
                                self.utils.print_info("Deleting the selected")
                                self.auto_actions.send_keys(get_multi_edit_native_vlan, Keys.BACK_SPACE)
                                self.utils.print_info("Configuring new native vlan values")
                                self.auto_actions.send_keys(get_multi_edit_native_vlan, native_vlan_trunk_port)
                            else:
                                self.utils.print_info("get_multi_edit_native_vlan cannot be completed ")
                                return -1

                        if allowed_vlan_trunk_port is not None:

                            get_multi_edit_allowed_vlan = self.get_d360_multi_edit_allowed_vlan_input()
                            if get_multi_edit_allowed_vlan:
                                self.auto_actions.send_keys(get_multi_edit_allowed_vlan, Keys.CONTROL + "a")
                                self.utils.print_info("Deleting the selected")
                                self.auto_actions.send_keys(get_multi_edit_allowed_vlan, Keys.BACK_SPACE)
                                self.utils.print_info("Configuring new allowed vlan values")
                                self.auto_actions.send_keys(get_multi_edit_allowed_vlan, allowed_vlan_trunk_port)
                            else:
                                self.utils.print_info("get_multi_edit_allowed_vlan cannot be completed ")
                                return -1

                    elif port_usage == 'Auto-sense Port':
                        checkbox_vlan = self.get_multi_edit_checkbox_vlan()
                        if checkbox_vlan:
                            if checkbox_vlan.is_enabled():
                                self.utils.print_info("Click on checkbox")
                                self.auto_actions.click_reference(self.get_multi_edit_checkbox_vlan)
                            else:
                                self.utils.print_info("The vlan is disabled")
                        else:
                            self.utils.print_info("Unable to click the element")

                    else:
                        if (voice_vlan_phone_port is not None) or (data_vlan_phone_port is not None):
                            """
                             - This keyword will select Vlan settings in Multi Edit when Port usage is Phone Port
                             (D360 - Port Configuration) and after that will complete the fields with values.
                            """
                            self.utils.print_info("Click on Voice VLAN checkbox when Port Usage is Phone Port")
                            self.auto_actions.click_reference(self.get_d360_multi_edit_checkbox_voice_vlan)
                            self.utils.print_info("Click on Data VLAN checkbox when Port Usage is Phone Port")
                            self.auto_actions.click_reference(self.get_d360_multi_edit_checkbox_data_vlan)

                        if voice_vlan_phone_port is not None:

                            get_multi_edit_voice_vlan = self.get_d360_multi_edit_voice_vlan_input()
                            if get_multi_edit_voice_vlan:
                                self.auto_actions.send_keys(get_multi_edit_voice_vlan, Keys.CONTROL + "a")
                                self.utils.print_info("Deleting the selected")
                                self.auto_actions.send_keys(get_multi_edit_voice_vlan, Keys.BACK_SPACE)
                                self.utils.print_info("Configuring new native vlan values")
                                self.auto_actions.send_keys(get_multi_edit_voice_vlan, voice_vlan_phone_port)
                            else:
                                self.utils.print_info("get_multi_edit_voice_vlan cannot be completed ")
                                return -1

                        if data_vlan_phone_port is not None:

                            get_multi_edit_data_vlan = self.get_d360_multi_edit_data_vlan_input()
                            if get_multi_edit_data_vlan:
                                self.auto_actions.send_keys(get_multi_edit_data_vlan, Keys.CONTROL + "a")
                                self.utils.print_info("Deleting the selected")
                                self.auto_actions.send_keys(get_multi_edit_data_vlan, Keys.BACK_SPACE)
                                self.utils.print_info("Configuring new allowed vlan values")
                                self.auto_actions.send_keys(get_multi_edit_data_vlan, data_vlan_phone_port)
                            else:
                                self.utils.print_info("get_multi_edit_data_vlan cannot be completed ")
                                return -1
                else:
                    self.utils.print_info("Can not select into drop down")
                    return -1
            else:
                self.utils.print_info("Can not click on drop down")
                return -1

        if description is not None:
            """
             - This keyword will select Description in Multi Edit (D360-Port Configuration)
             and after that will complete the field;
            """
            self.utils.print_info("Click on Description checkbox")
            self.auto_actions.click_reference(self.get_multi_edit_checkbox_port_description)

            get_multi_edit_description = self.get_multi_edit_port_description_input()
            if get_multi_edit_description:
                self.auto_actions.send_keys(get_multi_edit_description, description)
            else:
                self.utils.print_info("get_multi_edit_description cannot be completed ")
                return -1

    def check_fileds_from_multi_edit_tab(self, **kwargs):
        '''
        This function select Port Usage, Port State and Description from Multi Edit tab.
        - used to configure the default settings by selecting the fields listed above.
        :return: pass message if successfully
        :return: fail message if error
        '''
        self.utils.print_info("Click on Port Type checkbox")
        self.auto_actions.click_reference(self.get_multi_edit_checkbox_port_type)
        self.utils.print_info("Click on Port State checkbox")
        self.auto_actions.click_reference(self.get_multi_edit_checkbox_status)
        self.utils.print_info("Click on Description checkbox")
        self.auto_actions.click_reference(self.get_multi_edit_checkbox_port_description)

    def d360_save_multi_edit_button(self):
        '''
        This method click the save button from Multi Edit tab.
        - used to save the configuration made in the multi-edit tab;
        '''
        self.utils.print_info("Clicking 'Save' button from Multi Edit")
        self.auto_actions.click_reference(self.get_d360_save_multi_edit)

    def d360_cancel_multi_edit_button(self):
        '''
        This method click the cancel button from Multi Edit.
        - used to exit the multi-edit tab without saving the configuration;
        '''
        self.utils.print_info("Click Cancel button from Multi Edit")
        self.auto_actions.click_reference(self.get_d360_cancel_multi_edit)

    def select_max_pagination_size(self, **kwargs):
        """
         - This keyword will navigate to the max pagination size Monitoring Overview Ports Table, using the page number button
         - Flow: Click max page number
         It Assumes That Already Navigated to Device360 Page
        """
        sleep(2)
        pagination_size = max(self.dev360.get_device360_ports_table_pagination_sizes(),
                            key=lambda x: int(x.text))
        pagination_size.location_once_scrolled_into_view
        self.auto_actions.click(pagination_size)
        print(f"Selected the max pagination size: {pagination_size.text}")
        sleep(5)
        kwargs['pass_msg'] = f"Selected the max pagination size: {pagination_size.text}"
        self.common_validation.passed(**kwargs)

    def select_pagination_size(self, int_size, **kwargs):
        """
         - This keyword will navigate to the specific pagination size Monitoring Overview Ports Table, using the page number button
         - Flow: Click specific page number
         It Assumes That Already Navigated to Device360 Page
        """
        sleep(2)
        paginations = self.dev360.get_device360_ports_table_pagination_sizes()
        [pg_size] = [pg for pg in paginations if pg.text == int_size]
        self.auto_actions.click(pg_size)
        sleep(5)
        kwargs['pass_msg'] = "Selected the specific pagination size"
        self.common_validation.passed(**kwargs)
        return 1

    def device360_confirm_current_page_number(self, page_num_ref, **kwargs):
        """
         - This keyword will check if the page with page_num_ref number is currently displayed
         It Assumes That Already Navigated to Device360 Page (Monitoring->Overview)
         - Keyword Usage:
         - ``Device360 Monitor Overview Pagination Next Page By Number``
        :return: True if page number matches
        """
        current_page = int(
            self.dev360.get_device360_ports_table_current_pagin_number().text)
        if current_page == page_num_ref:
            kwargs['pass_msg'] = "Confirm current page number"
            self.common_validation.passed(**kwargs)
            return True
        kwargs['fail_msg'] = "'device360_confirm_current_page_number()' failed."
        self.common_validation.failed(**kwargs)

    def device360_switch_get_current_page_port_name_list(self, **kwargs):
        """
         - This keyword will get a list with all the port names from the current page (Monitoring->Overview)
         - Flow: Click next page number
         It Assumes That Already Navigated to Device360 Page (Monitoring->Overview)
         - Keyword Usage:
         - ``Device360 Monitor Overview Pagination Next Page By Number``
        :return: port_name_list if successfully extracted the port names
        """

        port_name_list = []
        rows = self.get_device360_port_table_rows()
        for row in rows:
            port_name_list.append(
                self.dev360.get_d360_switch_ports_table_interface_port_name_cell(row).text)
        if 'PORT NAME' in port_name_list:
            port_name_list.remove('PORT NAME')
        pattern_voss_three_nums = re.compile(r'\d+\/\d+\/\d+', re.M)
        filtered = [i for i in port_name_list if not pattern_voss_three_nums.match(i)]
        pattern_mgmt = re.compile(r'.*mgmt.*', re.M)
        filtered = [i for i in filtered if not pattern_mgmt.match(i)]
        kwargs['pass_msg'] = f"Port name list from current page: {filtered}"
        self.common_validation.passed(**kwargs)
        return filtered

    def device360_monitor_overview_pagination_next_page_by_number(self, **kwargs):
        """
         - This keyword will navigate to the next page of the Monitoring Overview Ports Table, using the
         page number button
         - Flow: Click next page number
         It Assumes That Already Navigated to Device360 Page
         - Keyword Usage:
         - ``Device360 Monitor Overview Pagination Next Page By Number``
        :return: 1 if successfully changed to next page
        :return: 2 if already on the last page
        """
        current_page = int(
            self.dev360.get_device360_ports_table_current_pagin_number().text)
        other_pages = self.dev360.get_device360_pagination_page_buttons()
        for page in other_pages:
            if int(page.text) == current_page + 1:
                self.utils.print_info(f"Going to page {str(current_page + 1)}")
                self.auto_actions.click(page)
                sleep(5)
                kwargs['pass_msg'] = "Successfully changed to next page"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['pass_msg'] = "Already on the last page"
        self.common_validation.passed(**kwargs)
        return 2

    def list_port_element(self, xiq, port_no, dut, **kwargs):
        """
         - This keyword will get port details info
         It Assumes That Already Navigated to Device360 Page
        """
        rows = xiq.xflowscommonDevices.devices_web_elements.get_port_details_info()
        if dut.cli_type.upper() == 'VOSS':
            matchers = ['Port Name', 'Type', 'LACP Status', 'Port Mode', 'Port Status',
                        'Transmission Mode', 'Access VLAN', 'Tagged VLAN(s)', 'LLDP Neighbor', 'Traffic Received',
                        'Traffic Sent', 'Port Errors', 'STP Port State', 'Port Speed']
        if dut.cli_type.upper() == 'EXOS':
            matchers = ['Port Name', 'Type', 'Link Aggregation', 'LAG Logical Port', 'Link Aggregation Status', 'Port Mode', 'Port Status',
                        'Transmission Mode', 'Access VLAN', 'Tagged VLAN(s)', 'LLDP Neighbor', 'Traffic Received',
                        'Traffic Sent', 'Port Errors', 'STP Port State', 'Port Speed']
        if rows:
            xiq.xflowscommonDevices.utils.print_info(f"Searching {len(rows)} rows")
            for row in rows:
                xiq.xflowscommonDevices.utils.print_info(f"Port {port_no} details: ",
                                                         xiq.xflowscommonDevices.format_row(row.text))
                for i in matchers:
                    test = any(i in string for string in xiq.xflowscommonDevices.format_row(row.text))
                    if test == False:
                        # return -1
                        kwargs['fail_msg'] = "'list_port_element()' failed."
                        self.common_validation.fault(**kwargs)
            kwargs['pass_msg'] = "Success"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'list_port_element()' failed."
            self.common_validation.failed(**kwargs)

    def enter_port_transmission_mode(self, port, transmission_mode, **kwargs):
        """
         - This keyword will enter port transimission mode
        Args:
            port
            transmission_mode: ex. "Half-Duplex"
        """
        sleep(10)
        configure_port_btn = self.dev360.get_d360_configure_port_settings_aggregation_tab_button()
        if not configure_port_btn:
            configure_port_btn = self.dev360.weh.get_element({"XPATH": '//div[@data-automation-tag="automation-port-configuration-port-settings"]'})
        # assert configure_port_btn, "Could not find element port configuration button"
        if not configure_port_btn:
            kwargs['fail_msg'] = "'enter_port_transmission_mode()' failed. Could not find element port configuration button"
            self.common_validation.fault(**kwargs)
        self.utils.print_info("Click Port Settings Tab")
        self.auto_actions.click(configure_port_btn)
        sleep(3)

        rows = self.dev360.get_device360_configure_port_settings_aggregation_rows()
        if not rows:
            rows = self.dev360.weh.get_elements({"XPATH": '//div[@class="port-details-entry line clearfix"]'})
        # assert rows, "Could not get the port settings aggregation rows"
        if not rows:
            kwargs['fail_msg'] = "'enter_port_transmission_mode()' failed. Could not get the port settings aggregation rows"
            self.common_validation.fault(**kwargs)

        for port_row in rows:
            if re.search(f"{port}\n", port_row.text):
                self.utils.print_debug("Found row for port: ", port_row.text)
                break
        else:
            assert False, f"Failed to find the row for port {port}"

        self.utils.print_info("clicking Transmission Mode drop down Button")
        drop_down_button = self.dev360.get_device360_port_settings_transmission_mode_drop_down_button(port_row)
        if self.auto_actions.click(drop_down_button) in [None, -1]:
            drop_down_button = self.dev360.weh.get_element({
                "XPATH": ".//div[@data-automation-tag='automation-automation-port-settings-port-transmission-type-chzn-container-ctn']"
            }, parent=port_row)
            # assert self.auto_actions.click(drop_down_button) == 1, "Failed to open transmission type drop down"
            if not self.auto_actions.click(drop_down_button) == 1:
                kwargs['fail_msg'] = "'enter_port_transmission_mode()' failed. Failed to open transmission type drop down."
                self.common_validation.fault(**kwargs)
        sleep(2)

        drop_down_options = self.dev360.get_device360_port_settings_transmission_mode_drop_down_options(port_row)
        if not drop_down_options:
            drop_down_options = self.dev360.weh.get_elements({
                "XPATH": './/li[contains(@data-automation-tag, "automation-automation-port-settings-port-transmission-type-chzn-option")]'
            })
        # assert drop_down_options
        if not drop_down_options:
            kwargs['fail_msg'] = "'enter_port_transmission_mode()' failed. Assert drop_down_option"
            self.common_validation.fault(**kwargs)
        drop_down_options = [opt for opt in drop_down_options if opt.text]
        self.utils.print_info(f"Selecting Transmission Mode Option : {transmission_mode}")
        self.auto_actions.select_drop_down_options(drop_down_options, transmission_mode)
        sleep(2)
        kwargs['pass_msg'] = "enter_port_transmission_mode() passed."
        self.common_validation.passed(**kwargs)

    def generate_vlan_id(self, rng=range(1024, 4096)):
        """
         - This keyword will generate vlan id
        :return: random vlan id
        """
        return str(random.choice(rng))

    def device360_display_traffic_received_from_xiq_and_return_traffic_list(self, dut, first_port, second_port, **kwargs):
        """
         - This keyword will display the received traffic from two ports connected to the Ixia traffic generator visible in XIQ and returns a list with them
        Args:
         dut: e.g. tb.dut1
         first_port: e.g. self.tb.dut1_tgen_port_a.ifname
         second_port: e.g. self.tb.dut1_tgen_port_b.ifname
        """

        paginations = self.dev360.get_device360_ports_table_pagination_sizes()
        assert paginations, "Failed to find the paginations for Device 360 tabular ports view"

        [pagination] = [pg for pg in paginations if pg.text == '10']
        sleep(5)
        self.auto_actions.click(pagination)
        sleep(3)

        if dut.cli_type.upper() == "VOSS":
            x = self.dev360.get_device360_ports_table()
            print("Displaying the traffic received value for the first 10 entries in the table")
            for i in x:
                traffic_received = i["TRAFFIC RECEIVED (RX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC RECEIVED: {traffic_received} for port: {port_name}")
            sleep(5)

            [pagination] = [pg for pg in paginations if pg.text == '100']
            sleep(5)
            self.auto_actions.click(pagination)
            sleep(3)

            x = self.dev360.get_device360_ports_table()

            traffic_list_xiq = []

            print(" Displaying the traffic received value for pagination 100")
            for i in x:
                traffic_received = i["TRAFFIC RECEIVED (RX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC RECEIVED: {traffic_received} for port: {port_name}")
                    traffic_list_xiq.append(traffic_received)
            sleep(5)
            kwargs['pass_msg'] = f"Traffic received values: {traffic_list_xiq}"
            self.common_validation.passed(**kwargs)
            return traffic_list_xiq
        elif dut.cli_type.upper() == "EXOS":
            x = self.dev360.get_device360_ports_table()

            print("x pentru exos 67 este: ", x)
            print("Displaying the traffic received value for the first 10 entries in the table")
            for i in x:
                traffic_received = i["TRAFFIC RECEIVED (RX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC RECEIVED: {traffic_received} for port: {port_name}")
            sleep(5)

            [pagination] = [pg for pg in paginations if pg.text == '100']
            sleep(5)
            self.auto_actions.click(pagination)
            sleep(3)

            x = self.dev360.get_device360_ports_table()

            traffic_list_xiq = []

            print(" Displaying the traffic received value for pagination 100")
            for i in x:
                traffic_received = i["TRAFFIC RECEIVED (RX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC RECEIVED: {traffic_received} for port: {port_name}")
                    traffic_list_xiq.append(traffic_received)
            sleep(5)
            kwargs['pass_msg'] = f"Traffic received values: {traffic_list_xiq}"
            self.common_validation.passed(**kwargs)
            return traffic_list_xiq

        kwargs['fail_msg'] = "'device360_display_traffic_received_from_xiq_and_return_traffic_list()' failed."
        self.common_validation.failed(**kwargs)

    def device360_display_traffic_transmitted_from_xiq_and_return_traffic_list(
        self, dut, first_port, second_port, **kwargs):
        """
         - This keyword will display the transmitted traffic from two ports connected to the Ixia traffic generator visible in XIQ and returns a list with them
        Args:
         dut: e.g. tb.dut1
         first_port: e.g. self.tb.dut1_tgen_port_a.ifname
         second_port: e.g. self.tb.dut1_tgen_port_b.ifname
        """

        paginations = self.dev360.get_device360_ports_table_pagination_sizes()
        assert paginations, "Failed to find the paginations for Device 360 tabular ports view"

        [pagination] = [pg for pg in paginations if pg.text == '10']
        sleep(5)
        self.auto_actions.click(pagination)
        sleep(3)

        if dut.cli_type.upper() == "VOSS":
            x = self.dev360.get_device360_ports_table()
            print("Displaying the traffic transmitted value for the first 10 entries in the table")
            for i in x:
                traffic_received = i["TRAFFIC TRANSMITTED (TX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC TRANSMITTED (TX): {traffic_received} for port: {port_name}")
            sleep(5)

            [pagination] = [pg for pg in paginations if pg.text == '100']
            sleep(5)
            self.auto_actions.click(pagination)
            sleep(3)

            x = self.dev360.get_device360_ports_table()

            traffic_list_xiq = []

            print(" Displaying the traffic transmitted value for pagination 100")
            for i in x:
                traffic_received = i["TRAFFIC TRANSMITTED (TX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"TRAFFIC TRANSMITTED (TX): {traffic_received} for port: {port_name}")
                    traffic_list_xiq.append(traffic_received)
            sleep(5)
            kwargs['pass_msg'] = f"Traffic transmitted values: {traffic_list_xiq}"
            self.common_validation.passed(**kwargs)
            return traffic_list_xiq

        elif dut.cli_type.upper() == "EXOS":
            x = self.dev360.get_device360_ports_table()

            print("Displaying the traffic transmitted value for the first 10 entries in the table")
            for i in x:
                traffic_received = i["TRAFFIC TRANSMITTED (TX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC TRANSMITTED (TX): {traffic_received} for port: {port_name}")
            sleep(5)

            [pagination] = [pg for pg in paginations if pg.text == '100']
            sleep(5)
            self.auto_actions.click(pagination)
            sleep(3)

            x = self.dev360.get_device360_ports_table()

            traffic_list_xiq = []

            print(" Displaying the traffic transmitted value for pagination 100")
            for i in x:
                traffic_received = i["TRAFFIC TRANSMITTED (TX)"]
                port_name = i["PORT NAME"]
                if port_name == first_port or port_name == second_port:
                    print(f"Found TRAFFIC TRANSMITTED (TX): {traffic_received} for port: {port_name}")
                    traffic_list_xiq.append(traffic_received)
            sleep(5)
            kwargs['pass_msg'] = f"Traffic transmitted values: {traffic_list_xiq}"
            self.common_validation.passed(**kwargs)
            return traffic_list_xiq

        kwargs['fail_msg'] = "'device360_display_traffic_transmitted_from_xiq_and_return_traffic_list()' failed."
        self.common_validation.failed(**kwargs)

    def check_power_values(self, ports_power_xiq, ports_power_cli, **kwargs):
        """
         - This keyword will check power values
        :return: results
        """
        results = []
        for port_xiq, port_cli in zip(ports_power_xiq, ports_power_cli):
            if port_xiq[0] == port_cli[0]:
                if port_xiq[1] == "N/A":
                    if port_xiq[1] == port_cli[1]:
                        results.append(["Port: " + port_xiq[0], "PASSED"])
                    else:
                        results.append(["Port: " + port_xiq[0], "FAILED"])
                else:
                    if float(port_xiq[1]) == (float(port_cli[1])*1000):
                        results.append(["Port: " + port_xiq[0], "PASSED"])
                    else:
                        results.append(["Port: " + port_xiq[0], "FAILED"])
            else:
                # return -1
                kwargs[
                    'fail_msg'] = "'check_power_values() failed."
                self.common_validation.failed(**kwargs)
        kwargs['pass_msg'] = f"{results}"
        self.common_validation.passed(**kwargs)
        return results

    def check_port_type(self, dut, **kwargs):
        """
         - This keyword will check port type
        :return:
        """

        if dut.cli_type.upper() == "VOSS":

            sleep(10)
            self.networkElementCliSend.send_cmd(dut.name, 'enable',
                                    max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show int gig l1-config | no-more',
                                            max_wait=10, interval=2)
            p = re.compile(r'(^\d+\/\d+)\s+(false|true)\s+(false|true)', re.M)
            match_port = re.findall(p, output[0].return_text)
            print(f"{match_port}")

            x = self.dev360.get_device360_ports_table()
            x.pop(0)
            cnt_values_port_type = 0
            j = 0

            for it in x:

                port_type = it["TYPE"]
                port_name = it["PORT NAME"]
                print(f"port name:{port_name} and port type:{port_type}")

                print("Verify that each entry has a value set for the 'port type' column('RJ45,'SFP+','SFP-DD')")
                if not port_type in ['RJ45', 'SFP', 'SFP+', "QSFP28", 'SFP-DD', "SFP28"]:
                    kwargs['fail_msg'] = "'check_port_type()' failed. Port type column has an entry with a value different from ('RJ45','SFP+','SFP-DD')."
                    self.common_validation.fault(**kwargs)

                cnt_values_port_type = cnt_values_port_type + 1

                if port_type == 'RJ45':

                    port_type_match_cli = 'true'
                    print("check if the port type 'RJ45' from XIQ is the same as the one from CLI")
                    if not (match_port[j][0] == port_name) and (match_port[j][2] == port_type_match_cli):
                        kwargs['fail_msg'] = "'check_port_type()' failed. Did not found the expected port type value for expected port name value."
                        self.common_validation.fault(**kwargs)

                    j = j + 1

                else:

                    print(f"{port_name},{port_type}")
                    if not port_type in ['RJ45', 'SFP', 'SFP+', "QSFP28", 'SFP-DD', "SFP28"]:
                        kwargs['fail_msg'] = "'check_port_type()' failed. Did not found the expected value. Port type column has an entry with a value different from ('SFP+','SFP-DD')"
                        self.common_validation.fault(**kwargs)

            print("Verify that the 'port type' column has no empty entry")
            if not len(x) == cnt_values_port_type:
                kwargs['fail_msg'] = "'check_port_type()' failed. Expecting to find a value for the 'port type' field of each table entry"
                self.common_validation.fault(**kwargs)

        elif dut.cli_type.upper() == "EXOS":

            sleep(10)
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                    max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports transceiver information',
                                            max_wait=10, interval=2)
            p = re.compile(r'(^\d+)\s+(DDMI\sis\snot\ssupported\son\sthis\sport)', re.M)
            match_port = re.findall(p, output[0].return_text)
            print(f"{match_port}")

            x = self.dev360.get_device360_ports_table()
            x.pop(0)
            cnt_values_port_type = 0
            j = 0

            for it in x:

                port_type = it["TYPE"]
                port_name = it["PORT NAME"]
                print(f"port name:{port_name} and port type:{port_type}")

                print("Verify that each entry has a value set for the 'port type' column('RJ45,'SFP+','SFP-DD')")
                if not port_type in ['RJ45', 'SFP', 'SFP+', "QSFP28", 'SFP-DD', "SFP28"]:
                    kwargs['fail_msg'] = "'check_port_type()' failed. Port type column has an entry with a value different from ('RJ45','SFP+','SFP-DD')"
                    self.common_validation.fault(**kwargs)

                cnt_values_port_type = cnt_values_port_type + 1

                if port_type == 'RJ45':
                    port_type_match_cli = 'DDMI is not supported on this port'
                    print("check if the port type 'RJ45' from XIQ is the same as the one from CLI")
                    if not (match_port[j][0] == port_name) and (match_port[j][1] == port_type_match_cli):
                        kwargs['fail_msg'] = "'check_port_type()' failed. Did not found the expected port type value RJ45 for expected port name"
                        self.common_validation.fault(**kwargs)
                    j = j + 1

                else:
                    print(f"{port_name},{port_type}")
                    if not port_type in ['RJ45', 'SFP', 'SFP+', "QSFP28", 'SFP-DD', "SFP28"]:
                        kwargs['fail_msg'] = "'check_port_type()' failed. Did not found the expected value. Port type column has an entry with a value different from ('SFP+','SFP-DD')"
                        self.common_validation.fault(**kwargs)

            print("Verify that the 'port type' column has no empty entry")
            if not len(x) == cnt_values_port_type:
                kwargs['fail_msg'] = "'check_port_type()' failed. Expecting to find a value for the 'port type' field of each table entry"
                self.common_validation.fault(**kwargs)

        kwargs['pass_msg'] = "'check_port_type()' passed."
        self.common_validation.passed(**kwargs)

    def go_to_last_page(self, **kwargs):
        """Method that goes to the last page of the honeycomb port type editor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """

        self.utils.print_info("Go to the last page and save the port type")
        for _ in range(10):

            get_next_button, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("next_button"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not get_next_button:
                kwargs["fail_msg"] = "Failed to get the next button"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the next button")

            if get_next_button.is_enabled():
                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click(get_next_button),
                    exp_func_resp=True,
                    delay=4,
                    silent_failure=True,
                )

                if res != 1:
                    kwargs["fail_msg"] = "Failed to click the next button"
                    self.common_validation.failed(**kwargs)
                    return -1

                self.utils.print_info("Successfully clicked the next page button")
            else:
                break

        kwargs["pass_msg"] = "Successfully went to the last page"
        self.common_validation.passed(**kwargs)
        return 1

    def go_to_next_editor_tab(self, **kwargs):
        """Method that goes to the next page of the honeycomb port editor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        get_next_button, _ = self.utils.wait_till(
            lambda: self.get_select_element_port_type("next_button"),
            exp_func_resp=True,
            delay=5,
            silent_failure=True)

        if not get_next_button:
            kwargs["fail_msg"] = "Failed to get the next button"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully got the next button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(get_next_button),
            exp_func_resp=True,
            delay=4,
            silent_failure=True)

        if res != 1:
            kwargs["fail_msg"] = "Failed to click the next button"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully clicked the next button"
        self.common_validation.passed(**kwargs)

        return 1

    ### Commented on 1/18/23 because this is a duplicate of a function below.
    ### The second function to be declared will be used. Thus, this function was commented
    #
    # def configure_port_name_usage_tab(self, port_type_name, description="test", status=True, port_type="access", **kwargs):
    #     """Method that configures the first page of the honeycomb port type editor.

    #     Args:
    #         port_type_name (str): the name of the port type
    #         description (str, optional): the description of the port type. Defaults to "test".
    #         status (bool, optional): the port status. Defaults to True.
    #         port_type (str, optional): the port type. Defaults to "access".

    #     Returns:
    #         int: 1 if the function call has succeeded else -1
    #     """
    #     name_element, _ = self.utils.wait_till(
    #         func=lambda: self.get_select_element_port_type("name"),
    #         exp_func_resp=True,
    #         silent_failure=True,
    #         delay=5)

    #     if not name_element:
    #         kwargs["fail_msg"] = "Failed to find port name element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully found port name element")

    #     res, _ = self.utils.wait_till(
    #         func=lambda: self.auto_actions.send_keys(name_element, port_type_name),
    #         exp_func_resp=True,
    #         delay=4
    #     )

    #     if res != 1:
    #         kwargs["fail_msg"] = "Failed to send keys to port name element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully sent keys to port name element")

    #     description_element, _ = self.utils.wait_till(
    #         func=lambda: self.get_select_element_port_type("description"),
    #         exp_func_resp=True,
    #         silent_failure=True,
    #         delay=5)

    #     if not description_element:
    #         kwargs["fail_msg"] = "Failed to find port description element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully found port description element")

    #     res, _ = self.utils.wait_till(
    #         func=lambda: self.auto_actions.send_keys(description_element, description),
    #         exp_func_resp=True,
    #         delay=4,
    #         silent_failure=True
    #     )

    #     if res != 1:
    #         kwargs["fail_msg"] = "Failed to send keys to port description element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully sent keys to port description element")

    #     status_element, _ = self.utils.wait_till(
    #         func=lambda: self.get_select_element_port_type("status"),
    #         exp_func_resp=True,
    #         silent_failure=True,
    #         delay=5
    #     )

    #     if not status_element:
    #         kwargs["fail_msg"] = "Failed to find port status element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully found port status element")

    #     if (not status_element.is_selected() and status) or (
    #         status_element.is_selected() and not status):
    #         res, _ = self.utils.wait_till(
    #             func=lambda: self.auto_actions.click(status_element),
    #             exp_func_resp=True,
    #             delay=4
    #         )

    #         if res != 1:
    #             kwargs["fail_msg"] = "Failed to click the status button"
    #             self.common_validation.failed(**kwargs)
    #             return -1

    #         self.utils.print_info("Successfully clicked the status button")

    #     auto_sense, _ = self.utils.wait_till(
    #         func=lambda: self.get_select_element_port_type("auto-sense"),
    #         exp_func_resp=True,
    #         silent_failure=True,
    #         delay=5
    #     )

    #     if auto_sense:
    #         if auto_sense.is_selected():
    #             res, _ = self.utils.wait_till(
    #                 func=lambda: self.auto_actions.click(auto_sense),
    #                 exp_func_resp=True,
    #                 delay=4
    #             )

    #             if res != 1:
    #                 kwargs["fail_msg"] = "Failed to click the auto sense button"
    #                 self.common_validation.failed(**kwargs)
    #                 return -1

    #             self.utils.print_info("Successfully clicked the auto sense button")

    #     port_element, _ = self.utils.wait_till(
    #         func=lambda: self.get_select_element_port_type("port usage", f"{port_type} port"),
    #         exp_func_resp=True,
    #         silent_failure=True,
    #         delay=5
    #     )

    #     if not port_element:
    #         kwargs["fail_msg"] = "Failed to get the port type element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully got the port type element")

    #     res, _ = self.utils.wait_till(
    #         func=lambda: self.auto_actions.click(port_element),
    #         exp_func_resp=True,
    #         delay=4,
    #         silent_failure=True
    #     )

    #     if res != 1:
    #         kwargs["fail_msg"] = "Failed to click the port type element"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     kwargs["pass_msg"] = "Successfully clicked the port type element"
    #     self.common_validation.passed(**kwargs)

    #     self.utils.wait_till(timeout=2)
    #     return 1

    def open_new_port_type_editor(self, port, device_360=False, **kwargs):
        """Method that opens the honeycomb port type editor for given port.

        Args:
            port (str): the name of the port
            device_360 (bool, optional): True if the browser is in the device 360 window. Defaults to False.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.wait_till(timeout=10)

        if not device_360:
            rows, _ = self.utils.wait_till(
                func=self.get_policy_configure_port_rows,
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not rows:
                kwargs["fail_msg"] = "Failed to get the rows"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the rows")

            for row in rows:
                if re.search(f'{port}\n', row.text):
                    d360_create_port_type, _ = self.utils.wait_till(
                        func=lambda: self.get_d360_create_port_type(row),
                        exp_func_resp=True,
                        silent_failure=True,
                        delay=5
                    )

                    if not d360_create_port_type:
                        kwargs["fail_msg"] = "Failed to get the d360_create_port_type button"
                        self.common_validation.failed(**kwargs)
                        return -1

                    self.utils.print_info("Successfully got the d360_create_port_type button")

                    res, _ = self.utils.wait_till(
                        func=lambda: self.auto_actions.click(d360_create_port_type),
                        exp_func_resp=True,
                        silent_failure=True,
                        delay=4
                    )

                    if res != 1:
                        kwargs["fail_msg"] = "Failed to click the d360_create_port_type button"
                        self.common_validation.failed(**kwargs)
                        return -1

                    self.utils.print_info("Successfully clicked the d360_create_port_type button")
                    self.utils.wait_till(timeout=10)
                    break
        else:

            port_conf_content, _ = self.utils.wait_till(
                func=self.get_device360_port_configuration_content,
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not port_conf_content:
                kwargs["fail_msg"] = "Failed to get the port_conf_content element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the port_conf_content element")

            port_row, _ = self.utils.wait_till(
                func=lambda: self.device360_get_port_row(port),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )
            if not re.search(f"{port}\n", port_row.text):
                port_row, _ = self.utils.wait_till(
                    func=lambda: self.device360_get_port_row(f"{port}\n"),
                    exp_func_resp=True,
                    silent_failure=True
                )
                if not re.search(f"{port}\n", port_row.text):
                    self.utils.print_info("Port was not found")
                    port_row = None

            if port_row:
                self.utils.print_debug("Found row for port: ", port_row.text)

                d360_create_port_type, _ = self.utils.wait_till(
                    func=lambda: self.get_d360_create_port_type(port_row),
                    silent_failure=True,
                    exp_func_resp=True,
                    delay=5
                )

                if not d360_create_port_type:
                    kwargs["fail_msg"] = "Failed to get the d360_create_port_type button"
                    self.common_validation.failed(**kwargs)
                    return -1

                self.utils.print_info("Successfully got the d360_create_port_type button")

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click(d360_create_port_type),
                    exp_func_resp=True,
                    delay=4
                )

                if res != 1:
                    kwargs["fail_msg"] = "Failed to click the d360_create_port_type button"
                    self.common_validation.failed(**kwargs)
                    return -1

                kwargs["pass_msg"] = "Successfully clicked the d360_create_port_type button"
                self.common_validation.passed(**kwargs)
                self.utils.wait_till(timeout=10)
        return 1

    def save_port_type_config(self, **kwargs):
        """Method that press the save button in the honeycomb port type edtitor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        save_button, _ = self.utils.wait_till(
            func=self.get_close_port_type_box,
            exp_func_resp=True,
            silent_failure=True,
            delay=5
        )

        if not save_button:
            kwargs["fail_msg"] = "Failed to get the save button"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully got the save button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(save_button),
            exp_func_resp=True,
            silent_failure=True,
            delay=4
        )

        if res != 1:
            kwargs["fail_msg"] = "Failed to click the save button"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully clicked the save button"
        self.common_validation.passed(**kwargs)

        self.utils.wait_till(timeout=10)
        return 1

    ### Commented on 1/18/23 because this is a duplicate of a function below.
    ### The second function to be declared will be used. Thus, this function was commented
    #
    # def close_port_type_config(self, **kwargs):
    #     """Method that press the close button in the honeycomb port type edtitor.

    #     Returns:
    #         int: 1 if the function call has succeeded else -1
    #     """
    #     close_button, _ = self.utils.wait_till(
    #         func=self.get_cancel_port_type_box,
    #         exp_func_resp=True,
    #         delay=5,
    #         silent_failure=True
    #     )

    #     if not close_button:
    #         kwargs["fail_msg"] = "Failed to get the close button"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     self.utils.print_info("Successfully got the close button")

    #     res, _ = self.utils.wait_till(
    #         func=lambda: self.auto_actions.click(close_button),
    #         exp_func_resp=True,
    #         delay=4,
    #         silent_failure=True
    #     )

    #     if res != 1:
    #         kwargs["fail_msg"] = "Failed to click the next button"
    #         self.common_validation.failed(**kwargs)
    #         return -1

    #     kwargs["pass_msg"] = "Successfully clicked the next button"
    #     self.common_validation.passed(**kwargs)

    #     self.utils.wait_till(timeout=10)
    #     return 1

    def click_on_stp_tab(self, **kwargs):
        """Method that click the STP configure port stb tab button in the device 360 window.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        stp_tab_button, _ = self.utils.wait_till(
            func=self.get_d360_configure_port_stp_tab_button,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not stp_tab_button:
            kwargs["fail_msg"] = "Failed to get the stp tab button"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully got the stp tab button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(stp_tab_button),
            exp_func_resp=True,
            silent_failure=True,
            delay=4
        )

        if res != 1:
            kwargs["fail_msg"] = "Failed to click the stp tab button"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully clicked the stp tab button"
        self.common_validation.passed(**kwargs)
        return 1

    def get_stp_port_configuration_rows(self, **kwargs):
        """Method that returns the STP port configuration rows in the device 360 window.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        rows, _ = self.utils.wait_till(
            func=self.get_device360_configure_stp_rows,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not rows:
            kwargs["fail_msg"] = "Failed to get rows"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the rows"
        self.common_validation.passed(**kwargs)
        return rows

    def get_stp_port_configuration_row(self, port, **kwargs):
        """Method that returns a specific STP port configuration row from the device 360 window.
        """
        rows = self.get_stp_port_configuration_rows()
        for row in rows:
            if re.search(f"^{port}\n", row.text):
                self.utils.print_info(f"Successfully found the row port for port='{port}'")
                return row
        else:
            kwargs["fail_msg"] = f"Failed to find the row port for port='{port}'"
            self.common_validation.failed(**kwargs)
            return -1

    def get_path_cost_value_from_stp_port_configuration_row(self, port, **kwargs):
        """Method that returns the path cost value of a specific port from device 360.

        Args:
            port (str): the port of the switch

        Returns:
            int: the path cost value
        """
        row = self.get_stp_port_configuration_row(port=port)

        cost_element, _ = self.utils.wait_till(
            func=lambda: self.get_device360_port_configuration_path_cost_stp(row),
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not cost_element:
            kwargs["fail_msg"] = "Failed to get the path " \
                                 "cost element "
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the path cost element"
        self.common_validation.passed(**kwargs)

        return cost_element.get_attribute("value")

    def get_stp_settings_summary(self):
        """Method that returns the STP settings from the honeycomb summary tab.

        Returns:
            dict: the summary
        """
        self.utils.wait_till(timeout=5)
        summary = {}

        for row_name, row_value in zip(
            ["STP", "Edge Port", "BPDU Protection", "Priority", "Path Cost"],
            ["stp", "edge port", "bpdu protection", "priority", "path cost"]
        ):
            try:
                summary[row_name]  = self.dev360.get_select_element_port_type_summary(row_value).text
            except Exception:
                summary[row_name] = ""
        return summary

    def verify_stp_settings_in_honeycomb_summary(self, stp_settings_summary, stp_enabled=None, edge_port=None,
                                                 bpdu_protection=None, priority=None, path_cost=None, **kwargs):
        """Method that verifies the STP settings of the summary tab in the honeycomb port type editor.

        Args:
            stp_settings_summary (dict): the summary returned by the get_stp_settings_summary method
            stp_enabled (bool, optional): True or False Defaults to None.
            edge_port (bool, optional): True or False. Defaults to None.
            bpdu_protection (int, optional): The pbdu protection value. Defaults to None.
            priority (int, optional): the priority value. Defaults to None.
            path_cost (int, optional): the path cost value. Defaults to None.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        if stp_enabled is not None:

            stp_enabled = "Enabled" if stp_enabled is True else "Disabled"

            if stp_enabled != stp_settings_summary["STP"]:
                kwargs["fail_msg"] = f'Expected STP Enabled to be "{stp_enabled}" but found "{stp_settings_summary["STP"]}"'
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info(f'Successfully found STP Enabled as "{stp_enabled}"')

        if edge_port is not None:

            edge_port = "Enabled" if edge_port is True else "Disabled"

            if edge_port != stp_settings_summary["Edge Port"]:
                kwargs["fail_msg"] = f'Expected Edge Port to be "{edge_port}" but found "{stp_settings_summary["Edge Port"]}"'
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info(f"Successfully found Edge Port as {edge_port}")

        if bpdu_protection is not None:

            if bpdu_protection != stp_settings_summary["BPDU Protection"]:
                kwargs["fail_msg"] = f'Expected BPDU Protection to be "{bpdu_protection}" ' \
                                    f'but found "{stp_settings_summary["BPDU Protection"]}"'
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info(f"Successfully found BPDU Protection as {bpdu_protection}")

        if priority is not None:

            if int(priority) != int(stp_settings_summary["Priority"]):
                kwargs["fail_msg"] = f'Expected Priority to be "{priority}" but found "{stp_settings_summary["Priority"]}"'
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info(f"Successfully found Priority as {priority}")

        if path_cost is not None:

            if int(path_cost) != int(stp_settings_summary["Path Cost"]):
                kwargs["fail_msg"] = f'Expected Path Cost enabled to be "{path_cost}" but found "{stp_settings_summary["Path Cost"]}"'
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info(f"Successfully found path cost as {path_cost}")

        kwargs["pass_msg"] = "Successfully verified the given stp settings"
        self.common_validation.passed(**kwargs)
        return 1

    def go_to_stp_settings_tab_in_honeycomb(self, **kwargs):
        """Method that goes to the STP settings tab in the honeycomb port editor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.print_info("Go to the STP settings page")

        for _ in range(5):

            stp_page, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("stpPage"),
                silent_failure=True,
                exp_func_resp=True,
                delay=5
            )

            if not stp_page:
                kwargs["fail_msg"] = "Failed to get the stp page element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the stp page element")

            if "active" in stp_page.get_attribute("class"):
                break

            get_next_button, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("next_button"),
                silent_failure=True,
                exp_func_resp=True,
                delay=5
            )

            if not get_next_button:
                kwargs["fail_msg"] = "Failed to get the next button"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the next button")

            if get_next_button.is_enabled():

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click(get_next_button),
                    exp_func_resp=True,
                    silent_failure=True,
                    delay=4
                )

                if res != 1:
                    kwargs["fail_msg"] = "Failed to click the next button"
                    self.common_validation.failed(**kwargs)
                    return -1

                self.utils.print_info("Successfully clicked the next button")
                self.utils.wait_till(timeout=2)

            else:
                break

        kwargs["pass_msg"] = "Successfully went to the stp settings tab in the hoenycomb port type editor"
        self.common_validation.passed(**kwargs)
        return 1

    def get_one_port_from_each_asic_flow(self, dut, order, slot=None):
        """Method that returns one port from each asic in the device360 window.

        Args:
            dut (dict): the dut
            order (int): the order in asic of the port
            slot (int, optional): the slot of the stack if the device is a stack. Defaults to None.

        Returns:
            list: a list with the selected ports
        """
        self.utils.wait_till(timeout=5)
        self.dev._goto_devices()

        try:
            self.utils.wait_till(timeout=5)
            self.deviceCommon.go_to_device360_window(device_mac=dut.mac)
            self.utils.wait_till(timeout=5)

            if slot:
                return self.get_one_port_from_each_asic_stack(order=order, slot=slot)

            return self.get_one_port_from_each_asic(order=order)

        finally:
            self.utils.wait_till(timeout=5)
            self.close_device360_window()

    def verify_port_type_editor_still_in_stp_tab(self, **kwargs):
        """Method that verifies if the browser is still in the STP tab of the honeycomb port editor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        stp_page, _ = self.utils.wait_till(
            func=lambda: self.get_select_element_port_type("stpPage"),
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not stp_page:
            kwargs["fail_msg"] = "Failed to get the stp page element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully got the stp page element")

        if "active" not in stp_page.get_attribute("class"):
            kwargs["fail_msg"] = "Currently not in the STP tab"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Currently in the STP tab"
        self.common_validation.passed(**kwargs)

        return 1

    def set_path_cost_in_honeycomb(self, path_cost, **kwargs):
        """Method that sets the path cost in the honeycomb port type editor.

        Args:
            path_cost (int): the path cost value

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        path_cost_element, _ = self.utils.wait_till(
            func=lambda: self.get_select_element_port_type("path cost"),
            exp_func_resp=True,
            silent_failure=True,
            delay=5
        )

        if not path_cost_element:
            kwargs["fail_msg"] = "Failed to get the path cost element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully got the path cost element")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.send_keys(path_cost_element, str(path_cost)),
            exp_func_resp=True,
            delay=4,
            silent_failure=True
        )

        if res != 1:
            kwargs["fail_msg"] = "Failed to send keys to the path cost element"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully sent keys to the path cost element"
        self.common_validation.passed(**kwargs)
        self.utils.wait_till(timeout=5)

        return 1

    def verify_path_cost_field_is_editable(self, **kwargs):
        """Method that verifies if the path cost field in editable in the honeycomb port type editor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        path_cost_element, _ = self.utils.wait_till(
            func=lambda: self.get_select_element_port_type("path cost"),
            exp_func_resp=True,
            silent_failure=True,
            delay=5
        )

        if not path_cost_element:
            kwargs["fail_msg"] = "Failed to get the path cost element"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Successfully got the path cost element")

        if path_cost_element.is_enabled() is True:
            kwargs["pass_msg"] = "Successfully verified that the path cost field is editable"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs["fail_msg"] = "The path cost element is not editable"
        self.common_validation.failed(**kwargs)
        return -1

    def configure_stp_settings_tab_in_honeycomb(self, stp_enabled=None, edge_port=None, bpdu_protection=None,
                                                path_cost=None, priority=None, **kwargs):
        """Method that configures the STP settings tab in the honeycomb port type editor.

        Args:
            stp_enabled (bool, optional): the STP status. Defaults to None.
            edge_port (bool, optional): the edge port status. Defaults to None.
            bpdu_protection (int, optional): the bpdu protection value. Defaults to None.
            path_cost (int, optional): the path cost value. Defaults to None.
            priority (int, optional): the priority value. Defaults to None.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        if stp_enabled is not None:
            stp_enabled_element, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("stp enable"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not stp_enabled_element:
                kwargs["fail_msg"] = "Failed to get the stp_enabled"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the stp_enabled")

            if (not stp_enabled_element.is_selected() and stp_enabled) or (
                stp_enabled_element.is_selected() and not stp_enabled):

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click(stp_enabled_element),
                    exp_func_resp=True,
                    silent_failure=True,
                    delay=4
                )

                if res != 1:
                    kwargs["fail_msg"] = "Failed to click the " \
                                         "stp_enabled button "
                    self.common_validation.fault(**kwargs)
                    return -1

                self.utils.print_info("Successfully clicked the stp_enabled button")

        if edge_port is not None:
            edge_port_element, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("edge port"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not edge_port_element:
                kwargs["fail_msg"] = "Failed to get the " \
                                     "edge_port_element button "
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the edge_port_element button")

            if (not edge_port_element.is_selected() and edge_port) or (
                edge_port_element.is_selected() and not edge_port):

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click(edge_port_element),
                    exp_func_resp=True,
                    silent_failure=True,
                    delay=4
                )

                if res != 1:
                    kwargs["fail_msg"] = "Failed to click the " \
                                         "edge_port_element button "
                    self.common_validation.fault(**kwargs)
                    return -1

                self.utils.print_info("Successfully clicked the edge_port_element button")

        if bpdu_protection is not None:
            bpdu_protection_element, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("bpdu protection"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not bpdu_protection_element:
                kwargs["fail_msg"] = "Failed to get the " \
                                     "bpdu_protection_element button "
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the bpdu_protection_element button")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(bpdu_protection_element),
                exp_func_resp=True,
                silent_failure=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click the " \
                                     "bpdu_protection_element button "
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully clicked the bpdu_protection_element button")

            get_bpdu_protection_items, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("bpdu_protection_items"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not get_bpdu_protection_items:
                kwargs["fail_msg"] = "Failed to get " \
                                     "get_bpdu_protection_items "
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got get_bpdu_protection_items")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.select_drop_down_options(
                get_bpdu_protection_items, bpdu_protection),
                exp_func_resp=True,
                silent_failure=True,
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to select from dropdown"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully selected from dropdown")

        if path_cost is not None:

            path_cost_element, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("path cost"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not path_cost_element:
                kwargs["fail_msg"] = "Failed to get the path_cost_element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the path_cost_element")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.send_keys(path_cost_element, str(path_cost)),
                exp_func_resp=True,
                silent_failure=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to send keys to the path_cost_element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully sent keys to the path_cost_element")

        if priority:
            priority_element, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("priority"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not priority_element:
                kwargs["fail_msg"] = "Failed to get the priority_element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the priority_element")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(priority_element),
                exp_func_resp=True,
                silent_failure=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click the priority_element"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully clicked the priority_element")

            get_priority_items, _ = self.utils.wait_till(
                func=lambda: self.get_select_element_port_type("priority_items"),
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

            if not get_priority_items:
                kwargs["fail_msg"] = "Failed to get the priority_items"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully got the priority_items")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.select_drop_down_options(get_priority_items, str(priority)),
                exp_func_resp=True,
                silent_failure=True
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to select from dropdown"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully selected from dropdown")

        kwargs["pass_msg"] = "Successfully configured the stp settings"
        self.common_validation.passed(**kwargs)
        return 1

    def get_vlan_settings_summary(self):
        """Method that returns the vlan settings from the summary tab of the honeycomb port type editor.

        Returns:
            dict: the vlan settings
        """
        self.utils.wait_till(timeout=5)
        summary = {}

        for row_name, row_value in zip(
            ["Port Usage", "Native VLAN", "Allowed VLANs", "VLAN"],
            ["port usage", "native vlan","allowed vlans", "vlan"]
        ):
            try:
                summary[row_name] = self.get_select_element_port_type_summary(row_value).text
            except Exception:
                summary[row_name] = ""
        return summary

    # There is a duplicate of this function above that was commented out on 1/18/23
    def configure_port_name_usage_tab(self, port_type_name, description="test",
                                      status=True, port_type="access", **kwargs):
        """Method that configures the first tab of the honeycomb port type editor.

        Args:
            port_type_name (str): the name of the port type
            description (str, optional): the description of the port type. Defaults to "test".
            status (bool, optional): the status of the port. Defaults to True.
            port_type (str, optional): the type of port. Defaults to "access".

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        name_element = self.get_select_element_port_type("name")

        if not name_element:
            kwargs["fail_msg"] = "Failed to find the port name element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully found the port name element")

        if self.auto_actions.send_keys(name_element, port_type_name) != 1:
            kwargs["fail_msg"] = "Failed to send keys to the port name element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully sent keys to the port name element")
        self.utils.wait_till(timeout=2)

        description_element = self.get_select_element_port_type("description")

        if not description_element:
            kwargs["fail_msg"] = "Failed to get the description element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the description element")

        if self.auto_actions.send_keys(description_element, description) != 1:
            kwargs["fail_msg"] = "Failed to send keys to the description element"
            self.common_validation.fault(**kwargs)

        self.utils.wait_till(timeout=2)
        self.utils.print_info("Successfully sent keys to the description element")

        status_element = self.get_select_element_port_type("status")

        if not status_element:
            kwargs["fail_msg"] = "Failed to get the status element"
            self.common_validation.fault(**kwargs)

        self.utils.wait_till(timeout=2)
        self.utils.print_info("Successfully got the status element")

        if (not status_element.is_selected() and status) or (
            status_element.is_selected() and not status):

            if self.auto_actions.click(status_element) != 1:
                kwargs["fail_msg"] = "Failed to click the status element"
                self.common_validation.fault(**kwargs)

            self.utils.wait_till(timeout=2)
            self.utils.print_info("Successfully clicked the status element")

        auto_sense = self.get_select_element_port_type("auto-sense")
        if auto_sense:
            # disable autosense if found in initial tab
            if auto_sense.is_selected():

                if self.auto_actions.click(auto_sense) != 1:
                    kwargs["fail_msg"] = "Failed to click the autosense button"
                    self.common_validation.fault(**kwargs)

                self.utils.print_info("Successfully clicked the autosense button")
                self.utils.wait_till(timeout=2)

        port_element = self.get_select_element_port_type("port usage", f"{port_type} port")

        if not port_element:
            kwargs["fail_msg"] = "Failed to get the port usage element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the port usage element")

        if self.auto_actions.click(port_element) != 1:
            kwargs["fail_msg"] = "Failed to click the port usage element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully clicked the port usage element")

        kwargs["pass_msg"] = "Successfully configured the initial tab of the honeycomb port type editor"
        self.common_validation.passed(**kwargs)
        self.utils.wait_till(timeout=2)
        return 1

    def set_vlan_id(self, vlan_id, **kwargs):
        """Method that sets the vlan id in the vlan tab of honeycomb port type editor.
        If the vlan is not found in the dropdown then it will be created.

        Args:
            vlan_id (int): the vlan

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        get_select_button = self.get_select_element_port_type("select_button")

        if not get_select_button:
            kwargs["fail_msg"] = "Failed to get the select_button element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the select_button element")

        if self.auto_actions.click_reference(lambda: get_select_button) != 1:
            kwargs["fail_msg"] = "Failed to click the select_button element"
            self.common_validation.fault(**kwargs)

        self.utils.wait_till(timeout=2)

        get_dropdown_items = self.get_select_element_port_type("dropdown_items")

        if not get_dropdown_items:
            kwargs["fail_msg"] = "Failed to get the dropdown_items elements"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the dropdown_items elements")

        if self.auto_actions.select_drop_down_options(get_dropdown_items, str(vlan_id)) == 1:
            kwargs["pass_msg"] = f"Selected into dropdown value: {vlan_id}"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("vlan {vlan_id} is not found so it will be created")

        get_add_vlan = self.get_select_element_port_type("add_vlan")

        if not get_add_vlan:
            kwargs["fail_msg"] = "Failed to get the add_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the add_vlan element")

        if self.auto_actions.click_reference(lambda: get_add_vlan) != 1:
            kwargs["fail_msg"] = "Failed to click the get_add_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully clicked the add_vlan element")
        self.utils.wait_till(timeout=2)

        get_name_vlan = self.get_select_element_port_type("name_vlan")

        if not get_name_vlan:
            kwargs["fail_msg"] = "Failed to get the name_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the name_vlan element")

        if self.auto_actions.send_keys(get_name_vlan, str(vlan_id)) != 1:
            kwargs["fail_msg"] = "Failed to send keys to name_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully sent keys to the name_vlan element")
        self.utils.wait_till(timeout=2)

        get_id_vlan = self.dev360.get_select_element_port_type("id_vlan")

        if not get_id_vlan:
            kwargs["fail_msg"] = "Failed to get the id_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the id_vlan element")

        if self.auto_actions.send_keys(get_id_vlan, str(vlan_id)) != 1:
            kwargs["fail_msg"] = "Failed to send keys to the id_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully sent keys to the id_vlan element")
        self.utils.wait_till(timeout=2)

        get_save_vlan = self.get_select_element_port_type("save_vlan")

        if not get_save_vlan:
            kwargs["fail_msg"] = "Failed to get the save_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the save_vlan element")

        if self.auto_actions.click_reference(lambda: get_save_vlan) != 1:
            kwargs["fail_msg"] = "Failed to click the save_vlan element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully clicked the save_vlan element")

        kwargs["pass_msg"] = "Successfully configured the vlan"
        self.common_validation.passed(**kwargs)
        return 1

    def set_native_vlan_id(self, native_vlan_id, **kwargs):
        """Method that sets the native vlan id in the vlan tab of honeycomb port type editor.
        If the vlan is not found in the dropdown then it will be created.

        Args:
            native_vlan_id (int): the vlan

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        get_select_button = self.get_select_element_port_type("native_vlan_select_button")

        if not get_select_button:
            kwargs["fail_msg"] = "Failed to get the select_button"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the select_button element")

        if self.auto_actions.click_reference(lambda: get_select_button) != 1:
            kwargs["fail_msg"] = "Failed to click the select_button element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully clicked the select_button element")
        self.utils.wait_till(timeout=2)

        get_dropdown_items = self.get_select_element_port_type("native_vlan_dropdown_items")

        if not get_dropdown_items:
            kwargs["fail_msg"] = "Failed to get the get_dropdown_items elements"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the get_dropdown_items elements")

        if self.auto_actions.select_drop_down_options(get_dropdown_items, str(native_vlan_id)) == 1:
            kwargs["pass_msg"] = f"Selected into dropdown value: {native_vlan_id}"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("vlan {native_vlan_id} is not found so it will be created")

        get_add_vlan = self.get_select_element_port_type("native_vlan_add_vlan")

        if not get_add_vlan:
            kwargs["fail_msg"] = "Failed to get the native_vlan_add_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the native_vlan_add_vlan element")

        if self.auto_actions.click_reference(lambda: get_add_vlan) != 1:
            kwargs["fail_msg"] = "Failed to click the native_vlan_add_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully clicked the native_vlan_add_vlan element")
        self.utils.wait_till(timeout=2)

        get_name_vlan = self.get_select_element_port_type("native_vlan_name_vlan")

        if not get_name_vlan:
            kwargs["fail_msg"] = "Failed to get the native_vlan_name_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully found the native_vlan_name_vlan element")

        if self.auto_actions.send_keys(get_name_vlan, str(native_vlan_id)) != 1:
            kwargs["fail_msg"] = "Failed to send keys to name_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully clicked the native_vlan_name_vlan element")

        get_id_vlan = self.get_select_element_port_type("native_vlan_id_vlan")

        if not get_id_vlan:
            kwargs["fail_msg"] = "Failed to get the native_vlan_id_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully found the native_vlan_id_vlan element")

        if self.auto_actions.send_keys(get_id_vlan, str(native_vlan_id)) != 1:
            kwargs["fail_msg"] = "Failed to send keys to the native_vlan_id_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully sent keys to the native_vlan_id_vlan element")
        self.utils.wait_till(timeout=2)

        get_save_vlan = self.get_select_element_port_type("save_vlan")

        if not get_save_vlan:
            kwargs["fail_msg"] = "Failed to get the save_vlan element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the save_vlan element")

        if self.auto_actions.click_reference(lambda: get_save_vlan) != 1:
            kwargs["fail_msg"] = "Failed to click the save_vlan element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully clicked the save_vlan element")

        kwargs["pass_msg"] = "Successfully configured the native vlan"
        self.common_validation.passed(**kwargs)
        return 1

    def create_port_type_with_custom_vlan_values(self, port, port_type_name, port_type="access", vlan_id=None,
                                                 native_vlan_id=None, allowed_vlans=None, device_360=False, **kwargs):
        """Method that creates a new port type with custom values for the vlan tab of the port type editor.
        All the other fields remain with the default values.

        Args:
            port (str): the name of the port
            port_type_name (str): the name of the port type
            port_type (str, optional): type of port - acces/trunk. Defaults to "access".
            vlan_id (str, optional): the vlan id. Defaults to None.
            native_vlan_id (str, optional): the native vlan id. Defaults to None.
            allowed_vlans (str, optional): the allowed vlans. Defaults to None.
            device_360 (bool, optional): True if the configuration is at device level. Defaults to False.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        try:
            self.utils.wait_till(timeout=4)

            self.open_new_port_type_editor(port=port, device_360=device_360)

            self.configure_port_name_usage_tab(port_type_name=port_type_name, port_type=port_type)

            self.go_to_next_editor_tab()

            if vlan_id:
                self.utils.wait_till(timeout=2)
                self.set_vlan_id(vlan_id=vlan_id)
                self.utils.wait_till(timeout=2)

            if native_vlan_id:
                self.utils.wait_till(timeout=2)
                self.set_native_vlan_id(native_vlan_id=native_vlan_id)
                self.utils.wait_till(timeout=2)

            if allowed_vlans:
                self.utils.wait_till(timeout=2)
                self.set_allowed_vlans(allowed_vlans_value=allowed_vlans)
                self.utils.wait_till(timeout=2)

            kwargs["pass_msg"] = "Successfully created the new port type"
            self.common_validation.passed(**kwargs)
            return 1

        except Exception:
            kwargs["fail_msg"] = "Failed to create the new port type"
            self.common_validation.failed(**kwargs)
            return -1

        finally:
            self.go_to_last_page()
            self.save_port_type_config()

    def set_allowed_vlans(self, allowed_vlans_value, **kwargs):
        """Method that sets the allowed vlans field in vlan tab of the honeycomb port type editor.

        Args:
            allowed_vlans_value (str): the allowed vlans value

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        allowed_vlans = self.get_select_element_port_type("allowed vlans")

        if not allowed_vlans:
            kwargs["fail_msg"] = "Failed to get allowed vlans element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the allowed vlans element")

        if self.auto_actions.send_keys(allowed_vlans, allowed_vlans_value) != 1:
            kwargs["fail_msg"] = "Failed to send keys to the allowed vlans element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully sent keys to the allowed vlans element")

        kwargs["pass_msg"] = "Successfully configured the allowed vlans field"
        self.common_validation.passed(**kwargs)
        return 1

    def go_to_device_360_port_config(self, dut, slot=None, unlock_button_flag=True, **kwargs):
        """Method that goes to the port configuration tab of the device 360 window.

        Args:
            dut (dict): the dut, e.g. tb.dut1
            slot (str): the slot/unit of the stack

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.wait_till(timeout=2)
        self.dev._goto_devices()
        self.utils.wait_till(timeout=2)

        self.utils.wait_till(timeout=2)
        self.deviceCommon.go_to_device360_window(device_mac=dut.mac)
        self.utils.wait_till(timeout=2)

        config_button = self.get_device360_configure_button()

        if not config_button:
            kwargs["fail_msg"] = "Failed to get the config_button element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the config_button element")

        if not config_button.is_selected():

            if self.auto_actions.click_reference(lambda: config_button) != 1:
                kwargs["fail_msg"] = "Failed to click the config_button element"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully clicked the config_button element")
            self.utils.wait_till(timeout=5)

        port_config_button = self.get_device360_configure_port_configuration_button()

        if not port_config_button:
            kwargs["fail_msg"] = "Failed to get the port_config_button element"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the port_config_button element")

        if self.auto_actions.click_reference(lambda: port_config_button) != 1:
            kwargs["fail_msg"] = "Failed to click the port_config_button element"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully clicked the port_config_button element")

        if slot:
            self.select_stack_unit(slot)

        kwargs["pass_msg"] = "Successfully went to the port configuration tab of the device 360 window"
        self.common_validation.passed(**kwargs)
        self.utils.wait_till(timeout=20)
        
        if unlock_button_flag:
            unlock_button, _ = self.utils.wait_till(
                func=self.get_device360_unlock_port_config_button,
                exp_func_resp=True,
                silent_failure=True, 
                delay=3
            )
            
            if unlock_button and unlock_button.is_displayed():
                if self.auto_actions.click_reference(lambda: unlock_button) != 1:
                    kwargs["fail_msg"] = "Failed to click the device360_unlock_port_config_button element"
                    self.common_validation.failed(**kwargs)
                    return -1
                
                confirmation_button, _ = self.utils.wait_till(
                    func=self.get_device360_unlock_port_config_confirmation_button,
                    exp_func_resp=True,
                    silent_failure=True, 
                    delay=3
                )
            
                if not confirmation_button:
                    kwargs["fail_msg"] = "Failed to get the device360_unlock_port_config_confirmation_button element"
                    self.common_validation.failed(**kwargs)
                    return -1

                if self.auto_actions.click_reference(lambda: confirmation_button) != 1:
                    kwargs["fail_msg"] = "Failed to click the device360_unlock_port_config_confirmation_button element"
                    self.common_validation.failed(**kwargs)
                    return -1
            
        return 1

    def verify_none_vlan_id_appears_in_device_view(self, dut, port, **kwargs):
        """Method that verifies if 'None' appear as access vlan in the device 360 window after the vlan is
        set as 'none' in the honeycomb port type editor for given port.

        Args:
            dut (dict): the dut, e.g. tb.dut1
            port (str): the port of the dut

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        try:

            self.dev.refresh_devices_page()
            self.utils.wait_till(timeout=10)

            self.navigator.navigate_to_device360_page_with_mac(dut.mac)
            self.utils.wait_till(timeout=8)

            self.auto_actions.click_reference(self.get_d360_switch_port_view_all_pages_button)
            self.utils.wait_till(timeout=4)

            # before extracting the ports from tabular view, perform a scroll down to load all elements,
            # otherwise only the first 26 elements are loaded
            self.auto_actions.scroll_down_table(self.d360_switch_ports_table_last_row_of_table)
            rows = self.get_d360_switch_ports_table_grid_rows()[1:]

            if not rows:
                kwargs["fail_msg"] = "Failed to get the port" \
                                     " rows from device 360"
                self.common_validation.fault(**kwargs)

            [port_row] = [r for r in rows if re.search(rf"^{port}\s+", r.text) and 'Stacking' not in r.text]

            if not any([port in port_row.text, 'None' in port_row.text]):
                kwargs["fail_msg"] = "Failed to find 'None' set as" \
                                     f" access vlan to the given port '{port}'"
                self.common_validation.failed(**kwargs)
                return -1

            kwargs["pass_msg"] = f"Successfully found 'None' set as access vlan to the given port '{port}'"
            self.common_validation.passed(**kwargs)
            return 1

        finally:
            self.exit_d360_Page()

    def save_device_360_port_config(self, **kwargs):
        """ Method that saves the device 360 port config window.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.wait_till(timeout=5)

        save_btn = self.get_device360_configure_port_save_button()
        if not save_btn:
            kwargs["fail_msg"] = "Failed to get the save button"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the save button")

        if self.auto_actions.click_reference(self.get_device360_configure_port_save_button) != 1:
            kwargs["fail_msg"] = "Failed to click the save button"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully clicked the save button")

        kwargs["pass_msg"] = "Successfully saved the device 360 port config"
        self.common_validation.passed(**kwargs)
        self.utils.wait_till(timeout=10)
        return 1

    def get_vlan_data_from_device_360_tabular_view(self, dut, port, **kwargs):
        """Method that returns from device 360 the port_mode, port_access_vlan and port_tagged_vlan fields of a given port.

        Args:
            dut (dict): the dut, e.g. tb.dut1
            port (str): the port of the dut

        Returns:
            dict|int: a dict if the function call has succeeded else -1
        """
        try:

            self.dev.refresh_devices_page()
            self.utils.wait_till(timeout=10)

            self.navigator.navigate_to_device360_page_with_mac(dut.mac)
            self.utils.wait_till(timeout=8)

            self.auto_actions.click_reference(self.get_d360_switch_port_view_all_pages_button)
            self.utils.wait_till(timeout=4)

            # before extracting the ports from tabular view, perform a scroll down to load all elements,
            # otherwise only the first 26 elements are loaded
            self.auto_actions.scroll_down_table(self.d360_switch_ports_table_last_row_of_table)

            rows = self.get_d360_switch_ports_table_grid_rows()[1:]
            assert rows, "Failed to get the port rows from device 360"

            [port_row] = [r for r in rows if re.search(rf"^{port}\s+", r.text) and 'Stacking' not in r.text]

            data = {
                "port_mode": self.get_device360_switch_port_table_port_mode(port_row).text,
                "port_access_vlan": self.get_device360_switch_port_table_access_vlan(port_row).text,
                "port_tagged_vlan": self.get_device360_switch_port_table_tagged_vlans(port_row).text
            }

            kwargs["pass_msg"] = "Successfully got the port info from the device 360"
            self.common_validation.passed(**kwargs)
            return data

        except Exception as e:

            kwargs["fail_msg"] = "Failed to get the port info from " \
                                 f"the device 360 \n Exception found: {repr(e)}"
            self.common_validation.failed(**kwargs)
            return -1

        finally:
            self.exit_d360_Page()

    def get_vlan_data_from_device_360_tabular_for_all_ports(self, dut, **kwargs):
        """Method that returns from device 360 the port_mode, port_access_vlan and port_tagged_vlan fields for all the ports of a dut.

        Args:
            dut (dict): the dut, e.g. tb.dut1

        Returns:
            dict|int: a dict if the function call has succeeded else -1
        """
        try:

            self.dev.refresh_devices_page()
            self.utils.wait_till(timeout=10)

            self.navigator.navigate_to_device360_page_with_mac(dut.mac)
            self.utils.wait_till(timeout=8)

            self.auto_actions.click_reference(self.get_d360_switch_port_view_all_pages_button)
            self.utils.wait_till(timeout=4)

            rows = self.get_d360_switch_ports_table_grid_rows()[1:]
            assert rows, "Failed to get the port rows from device 360"

            ports = [row.text.split(" ")[0] for row in rows]

            ret = {}

            for port in ports:

                [port_row] = [r for r in rows if re.search(rf"^{port}\s+", r.text) and 'Stacking' not in r.text]

                ret[port] = {
                    "port_mode": self.get_device360_switch_port_table_port_mode(port_row).text,
                    "port_access_vlan": self.get_device360_switch_port_table_access_vlan(port_row).text,
                    "port_tagged_vlan": self.get_device360_switch_port_table_tagged_vlans(port_row).text
                }

            kwargs["pass_msg"] = "Successfully got the port info from device 360"
            self.common_validation.passed(**kwargs)
            return ret

        except Exception:
            kwargs["fail_msg"] = "Failed to get the port" \
                                 " info from the device 360"
            self.common_validation.failed(**kwargs)
            return -1

        finally:
            self.exit_d360_Page()

    def enter_port_type_and_vlan_id(self, port, port_type=None, access_vlan_id=None, native_vlan=None,
                                    allowed_vlans=None, device_os="EXOS", **kwargs):
        """Method that configures the vlan and port type in the device 360 port configuration window.

        Args:
            port (str): the port
            port_type (str, optional): the port type. Defaults to None.
            access_vlan_id (str, optional):the access vlan id. Defaults to None.
            native_vlan (str, optional): the native vlan id. Defaults to None.
            allowed_vlans (str, optional): the allowed vlans. Defaults to None.
            device_os (str, optional): the cli_type field of dut. Defaults to "EXOS".

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.wait_till(timeout=8)
        port_row = self.device360_get_port_row(port)

        if not port_row:
            kwargs["fail_msg"] = "Failed to get the port_row element"
            self.common_validation.fault(**kwargs)

        self.utils.print_debug("Found row for port: ", port_row.text)

        if port_type:

            drop_down = self.get_device360_configure_port_usage_drop_down_button(port_row)

            if not drop_down:
                kwargs["fail_msg"] = "Failed to get the drop_down button"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully got the drop_down button")

            if self.auto_actions.click_reference(lambda: drop_down) != 1:
                kwargs["fail_msg"] = "Failed to click the drop_down button"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully clicked the drop_down button")
            self.utils.wait_till(timeout=2)

            self.utils.print_info("Selecting Port Usage")
            dropdown_options = self.get_device360_configure_port_usage_drop_down_options(port_row)

            if not dropdown_options:
                kwargs["fail_msg"] = "Failed to get the dropdown_options elements"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully got the dropdown_options elements")

            if self.auto_actions.select_drop_down_options(dropdown_options, port_type) != 1:
                kwargs["fail_msg"] = "Failed to select options from the" \
                                     " dropdown_options elements"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully selected options from the dropdown_options elements")
            self.utils.wait_till(timeout=2)

        if access_vlan_id:
            # 3/22/2023, WD1R2, 23.3.0.20-WI23R3IN-SNAPSHOT
            # I commented this because now these XPATHs are identical for both EXOS/VOSS
            # note: this commented code block can be deleted later; also the defs and web elements
            # if device_os == "EXOS":
            #     input_field_access_vlan_id = self.get_device360_configure_port_access_vlan_textfield(port_row)
            # else:
            #     input_field_access_vlan_id = self.get_device360_configure_port_access_vlan_textfield_VOSS(port_row)
                
            input_field_access_vlan_id = self.get_device360_configure_port_access_vlan_textfield(port_row)

            if not input_field_access_vlan_id:
                kwargs["fail_msg"] = "Failed to get the input_field_access_vlan_id" \
                                     " element"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully got the input_field_access_vlan_id element")

            if self.auto_actions.send_keys(input_field_access_vlan_id, Keys.BACK_SPACE * 10 + access_vlan_id + Keys.ENTER) != 1:
                kwargs["fail_msg"] = "Failed to sent keys to " \
                                     "the input_field_access_vlan_id element"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully sent keys to the input_field_access_vlan_id element")
            self.utils.wait_till(timeout=2)

        if native_vlan:

            # 3/22/2023, WD1R2, 23.3.0.20-WI23R3IN-SNAPSHOT
            # I commented this because now these XPATHs are identical for both EXOS/VOSS
            # note: this commented code block can be deleted later; also the defs and web elements
            # if device_os == "EXOS":
            #     input_field_trunk_native = self.get_device360_configure_port_trunk_native_vlan_textfield(port_row)
            # else:
            #     input_field_trunk_native = self.get_device360_configure_port_trunk_native_vlan_textfield_VOSS(port_row)
                
            input_field_trunk_native = self.get_device360_configure_port_trunk_native_vlan_textfield(port_row)

            if not input_field_trunk_native:
                kwargs["fail_msg"] = "Failed to get the input_field_trunk_native element"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully got the input_field_trunk_native element")

            if self.auto_actions.send_keys(input_field_trunk_native, Keys.BACK_SPACE * 10 + native_vlan + Keys.ENTER) != 1:
                kwargs["fail_msg"] = "Failed to send keys to the" \
                                     " input_field_trunk_native element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully sent keys to the input_field_trunk_native element")
            self.utils.wait_till(timeout=2)

        if allowed_vlans:

            # 3/22/2023, WD1R2, 23.3.0.20-WI23R3IN-SNAPSHOT
            # I commented this because now these XPATHs are identical for both EXOS/VOSS
            # note: this commented code block can be deleted later; also the defs and web elements
            # if device_os == "EXOS":
            #     input_field_allowed_vlans = self.get_device360_configure_port_trunk_vlan_textfield(port_row)
            # else:
            #     input_field_allowed_vlans = self.get_device360_configure_port_trunk_vlan_textfield_VOSS(port_row)
                
            input_field_allowed_vlans = self.get_device360_configure_port_trunk_vlan_textfield(port_row)

            if not input_field_allowed_vlans:
                kwargs["fail_msg"] = "Failed to get the input_field_allowed_vlans element"
                self.common_validation.fault(**kwargs)

            self.utils.print_info("Successfully got the input_field_allowed_vlans element")

            if self.auto_actions.send_keys(input_field_allowed_vlans, Keys.BACK_SPACE * 10 + allowed_vlans + Keys.ENTER) != 1:
                kwargs["fail_msg"] = "Failed to send keys to the " \
                                     "input_field_allowed_vlans element"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("Successfully sent keys to the input_field_allowed_vlans element")

        kwargs["pass_msg"] = f"Successfully configured the vlan fields of the port '{port}'"
        self.common_validation.passed(**kwargs)
        self.utils.wait_till(timeout=8)
        return 1

    # There is a duplicate of this function above that was commented out on 1/18/23
    def close_port_type_config(self, **kwargs):
        """Method that closes the honeycomb port type editor.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        close_button = self.get_device_d360_cancel_port_configuration()

        if not close_button:
            kwargs["fail_msg"] = "Failed to get the close button"
            self.common_validation.fault(**kwargs)

        self.utils.print_info("Successfully got the close button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(close_button),
            exp_func_resp=True,
            delay=3
        )

        if res != 1:
            kwargs["fail_msg"] = "Failed to click the close button"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Successfully clicked the close button")

        kwargs["pass_msg"] = "Successfully closed the honeycomb port type editor"
        self.common_validation.passed(**kwargs)
        self.utils.wait_till(timeout=10)
        return 1

    def get_connected_ports(self, dut, **kwargs):
        """
        This keyword will get connected ports from D360 table.
        It Assumes That Already Navigated to Device360 Page
        Returns: connected_ports
        """
        sleep(8)
        self.navigator.navigate_to_device360_page_with_mac(dut.mac)
        sleep(8)

        self.auto_actions.click(self.dev360.get_d360_switch_port_view_all_pages_button())
        sleep(4)

        rows = self.dev360.get_d360_switch_ports_table_grid_rows()[1:]
        connected_ports = []

        for row in rows:
            try:
                port_name = row.text.split(" ")[0]
                if (not "Disconnected" in row.text) and port_name != "mgmt":
                    connected_ports.append(port_name)
            except Exception:
                pass
        self.exit_d360_Page()
        kwargs["pass_msg"] = "Successfully closed the honeycomb port type editor"
        self.common_validation.passed(**kwargs)
        return connected_ports


    def verify_port_names(self, **kwargs):
        """
        Verifies that the port details of slot 1 are displayed by default in D360 table.
        It Assumes That Already Navigated to Device360 Page
        """
        first_order_rows = [r.text for r in self.get_device360_port_table_rows()]
        first_port_names = [r.split(" ")[0] for r in first_order_rows]
        print(f"Found these port names in the table: {first_port_names}")
        for port_name in first_port_names:
            print(f"Port name: {port_name}")
            if not re.match(r"1:(\d+|mgmt)", port_name):
                kwargs["fail_msg"] = "At least one port displayed is not from Slot 1"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs["pass_msg"] = "All ports displayed by default are from Slot 1"
        self.common_validation.passed(**kwargs)

    def check_device360_LLDP_neighbors_with_hyperlink(self, isl_ports_dut, hyperlinks=False, **kwargs):
        """
        Check Device360 LLDP neighbors with hyperlink in D360 table.
        Args:
            isl_ports_dut: create_list_of_netelem_isl_ports("netelem1")
            hyperlinks: True -> to return the LLDP neighbors hyperlinks from D360 table
        """
        header_row = self.dev360.get_device360_ports_description_table_row()
        ths = self.dev360.weh.get_elements(
            self.dev360.device360_ports_table_th_columns, parent=header_row)

        table_rows = self.get_device360_port_table_rows()

        is_hyperlink = 0
        hyperlinks_dut = []
        for row in table_rows:
            tds = self.dev360.weh.get_elements(
                self.dev360.device360_ports_table_td_gridcell, parent=row)
            for th, td in zip(ths, tds):
                if th.text.strip() == "PORT NAME":
                    port_found = 0
                    for port in isl_ports_dut:
                        print(td.text.strip())
                        print(port)
                        if td.text.strip() == port:
                            port_found = 1
                            print(f"Port found: {td.text.strip()}")
                            break
                elif th.text.strip() == "LLDP NEIGHBOR":
                    if port_found == 1:
                        print(self.dev360.get_cell_href(td))
                        if self.dev360.get_cell_href(td) != None:
                            if hyperlinks:
                                hyperlink_dut = self.dev360.get_cell_href(td)
                                hyperlinks_dut.append(hyperlink_dut)
                            is_hyperlink = is_hyperlink + 1
                            print(f"LLDP column displays the sysname, {td.text.strip()} with hyperlink for port {port}")
                        else:
                            print(
                                f"LLDP column displays the sysname, {td.text.strip()} without hyperlink for port {port}")
                    break

        # assert is_hyperlink == len(
        #     isl_ports_dut), "LLDP column displays the sysname without hyperlink for at least one port"
        if not is_hyperlink == len(isl_ports_dut):
            kwargs["fail_msg"] = "'check_device360_LLDP_neighbors_with_hyperlink()' failed. LLDP column displays the sysname without hyperlink for at least one port"
            self.common_validation.failed(**kwargs)

        kwargs["pass_msg"] = "Successfully checked Device360 LLDP neighbors with hyperlink."
        self.common_validation.passed(**kwargs)
        if hyperlinks:
            kwargs["pass_msg"] = f"Hyperlinks: {hyperlinks_dut}"
            self.common_validation.passed(**kwargs)
            return hyperlinks_dut

    def check_device360_LLDP_neighbors_without_hyperlink(self, isl_ports, **kwargs):
        """
        Check Device360 LLDP neighbors without hyperlink in D360 table.
        Args:
            isl_ports_dut: create_list_of_netelem_isl_ports("netelem1")
        """
        header_row = self.dev360.get_device360_ports_description_table_row()
        ths = self.dev360.weh.get_elements(
            self.dev360.device360_ports_table_th_columns, parent=header_row)

        table_rows = self.get_device360_port_table_rows()

        no_hyperlink = 0
        for row in table_rows:
            tds = self.dev360.weh.get_elements(
                self.dev360.device360_ports_table_td_gridcell, parent=row)
            for th, td in zip(ths, tds):
                if th.text.strip() == "PORT NAME":
                    port_found = 0
                    for port in isl_ports:
                        if td.text.strip() == port:
                            port_found = 1
                            print(f"Port found: {td.text.strip()}")
                            break
                elif th.text.strip() == "LLDP NEIGHBOR":
                    if port_found == 1:
                        if self.dev360.get_cell_href(td) != None:
                            print(
                                f"LLDP column displays the sysname, {td.text.strip()} with hyperlink for port {port}")
                        else:
                            if td.text.strip() != "":
                                no_hyperlink = no_hyperlink + 1
                            print(
                                f"LLDP column displays the sysname, {td.text.strip()} without hyperlink for port {port}")
                    break

        # assert no_hyperlink == len(
        #     isl_ports), "LLDP column displays the sysname with hyperlink/sysname missing for at least one port"
        if not no_hyperlink == len(isl_ports):
            kwargs["fail_msg"] = "'check_device360_LLDP_neighbors_without_hyperlink()' failed. LLDP column displays the sysname with hyperlink/sysname missing for at least one port"
            self.common_validation.failed(**kwargs)
        kwargs["pass_msg"] = "Successfully checked Device360 LLDP neighbors without hyperlink."
        self.common_validation.passed(**kwargs)

    def verify_lacp_status_for_port_device_in_360_table(self, logger, dut, port, check_value, **kwargs):
        """
        Check Device360 LACP status for port device in D360 table.
        Args:
            port: dut1.isl.port_a.ifname
            check_value: 'true'/'false'
        """
        self.select_max_pagination_size()

        logger.info("Select LACP Status column if is not selected in column picker")
        checkbox_button = self.dev360.get_device360_columns_toggle_button()
        checkbox_button.location_once_scrolled_into_view

        self.auto_actions.click(checkbox_button)

        sleep(2)
        all_checkboxes = self.dev360.get_device360_all_checkboxes()
        default_disabled = [k for k, v in all_checkboxes.items() if v["is_selected"] is False]

        if dut.cli_type.upper() == 'VOSS':
            for checkbox_name, stats in all_checkboxes.items():
                if checkbox_name.upper() == "LACP STATUS" and checkbox_name in default_disabled \
                        and stats["is_selected"] is False:
                    self.auto_actions.click(stats["element"])
                    break
        elif dut.cli_type.upper() == 'EXOS':
            for checkbox_name, stats in all_checkboxes.items():
                if checkbox_name.upper() == "LINK AGGREGATION" and checkbox_name in default_disabled \
                        and stats["is_selected"] is False:
                    self.auto_actions.click(stats["element"])
                    break

        ports_table = self.dev360.get_device360_ports_table()
        [port_row] = [row for row in ports_table if row["PORT NAME"] == port]

        if dut.cli_type.upper() == 'VOSS':
            lacp_status = port_row["LACP STATUS"]
            logger.info(f"LACP status = {lacp_status}")
        if dut.cli_type.upper() == 'EXOS':
            lacp_status = port_row["LINK AGGREGATION"]
            logger.info(f"LACP status = {lacp_status}")

        if not lacp_status == check_value:
            kwargs["failed_msg"] = f"verify_lacp_status_for_port_device_in_360_table() failed. Default LACP Status for port: {port} is not {check_value}"
            self.common_validation.fault(**kwargs)

        logger.info("Select LACP Status column if is not selected in column picker")
        checkbox_button = self.dev360.get_device360_columns_toggle_button()
        if checkbox_button:
            checkbox_button.location_once_scrolled_into_view

            self.auto_actions.click(checkbox_button)
            sleep(2)

            all_checkboxes = self.dev360.get_device360_all_checkboxes()
            if dut.cli_type.upper() == 'VOSS':
                for checkbox_name, stats in all_checkboxes.items():
                    if checkbox_name.upper() == "LACP STATUS" and stats["is_selected"] is True:
                        self.auto_actions.click(stats["element"])
                        break
            elif dut.cli_type.upper() == 'EXOS':
                for checkbox_name, stats in all_checkboxes.items():
                    if checkbox_name.upper() == "LINK AGGREGATION" and stats["is_selected"] is True:
                        self.auto_actions.click(stats["element"])
                        break
        self.select_pagination_size("10")
        self.close_device360_window()
        kwargs["pass_msg"] = "Successfully verified lacp status for port device in D360 table"
        self.common_validation.passed(**kwargs)

    def check_lld_neighbour_field_with_value_and_with_hyperlink(self, ports_isl, real_ports, logger, **kwargs):
        """
        Check LLDP neighbor field with value and with hyperlink.
        Args:
            ports_isl: ex. create_list_of_netelem_isl_ports("netelem1")
            real_ports: device_360_web_elements.get_ports_from_device360_up()
        """
        lldp_neighbour = {}
        success = 1
        for port in ports_isl:
            logger.info("PORT =  {}".format(port))
            self.auto_actions.click(real_ports[port - 1])
            elem = Device360WebElements().get_ports_from_device360_up_lldp_neighbour()
            if not elem:
                elem = Device360WebElements().weh.get_element(
                    {"XPATH": '//div[contains(@class, "port-info port-lldp-neighbor")]'})
            lldp_neighbour[port] = elem
            logger.info("lldp_neighbour =  {}".format(lldp_neighbour[port].text))
            lldp_hyper_link = Device360WebElements().get_cell_href(lldp_neighbour[port])
            logger.info("lldp_neighbour href =  {}".format(lldp_hyper_link is not None))
            str1 = lldp_neighbour[port].text
            splits = str1.split()
            for split in splits:
                logger.info("SPLIT = {}".format(split))
            if (lldp_neighbour[port].text is not None and lldp_neighbour[port].text != "" and len(
                    splits) > 2) and lldp_hyper_link is not None:
                success = 1
            else:
                success = 0
                break
            sleep(5)
        kwargs["pass_msg"] = f"Successfully checked LLDP neighbor field with value and with hyperlink: {success}"
        self.common_validation.passed(**kwargs)
        return success

    def navigate_to_unit_options_from_xiq_diagnostics_page(self, unit, unit_role, **kwargs):
        """
        - This keyword navigates to unit options from Device360 - Diagnostics Page
        - It is assumed that the Device360 window is open in Monitor-Diagnostics
        - Keyword Usage:
            stacking_info_cli = cli.get_stacking_details_cli(dut)
            res = self.xiq.xflowsmanageDevice360.navigate_to_unit_options_from_xiq_diagnostics_page(stacking_info_cli[0][0][1],
                                                                          stacking_info_cli[0][0][2].upper())

        :param unit: the unit you wish to search for
        :param unit_role: the stack role that the unit has
        """

        ok = 1
        if self.auto_actions.click_reference(
                self.dev360.get_device360_monitor_diagnostics_stack_drop_down_unit) != 1:
            ok = 0
        else:
            print("Clicked on Drop down")
        if ok != 1:
            kwargs[
                'fail_msg'] = "navigate_to_unit_options_from_xiq_diagnostics_page() failed; Unable to click on drop down"
            self.common_validation.failed(**kwargs)

            return -1

        ok = 1
        if self.auto_actions.click_reference(
                lambda: self.dev360.get_device360_monitor_diagnostics_stack_drop_down_unit_options(unit, unit_role)) != 1:
            ok = 0
        else:
            print("Unit was selected")
        if ok != 1:
            kwargs['fail_msg'] = "navigate_to_unit_options_from_xiq_diagnostics_page() failed; Unable to select unit"
            self.common_validation.failed(**kwargs)

            return -1

        kwargs['pass_msg'] = "Successfully navigated from unit options to diagnostics page"
        self.common_validation.passed(**kwargs)

        return 1

    def check_all_the_individual_devices_in_the_stack_monitor_diagnostics(self, dut, stacking_info_cli, **kwargs):
        """
        - This keyword checks the dropdown in Device360 Monitor Diagnostics.
        - It is assumed that the Device360 window is open in Monitor-Diagnostics

        :param dut: the dut object
        :apram stacking_info_cli: the cli info of the stack to check against
        """

        print(f"Print a list with mac add, number of slot and role for each stack unit: {stacking_info_cli}")

        mac_add_list_cli = []
        for i in range(0, len(stacking_info_cli[0])):
            unit_i_mac_address = stacking_info_cli[0][i][0]
            unit_i_mac_address_mapped = unit_i_mac_address.replace(':', '')
            unit_i_mac_address_final_mapped = unit_i_mac_address_mapped.upper()
            mac_add_list_cli.append(unit_i_mac_address_final_mapped)
        print(f"Print mac add units: {mac_add_list_cli}")

        print("Navigate to through units and make mac add check")
        for i in range(1, len(stacking_info_cli[0])):
            if stacking_info_cli[0][i][2].upper() == 'STANDBY':
                self.utils.wait_till(
                    lambda: self.navigate_to_unit_options_from_xiq_diagnostics_page(
                        stacking_info_cli[0][i][1], 'MEMBER'),
                    delay=8, exp_func_resp=True)
            else:
                res = self.navigate_to_unit_options_from_xiq_diagnostics_page(
                    stacking_info_cli[0][i][1], stacking_info_cli[0][i][2].upper())
                if res == -1:
                    kwargs[
                        'fail_msg'] = "check_all_the_individual_devices_in_the_stack_monitor_diagnostics() failed; Unable to navigate to unit options"
                    self.common_validation.failed(**kwargs)

                    return -1
            self.utils.wait_till(delay=5)
            mac_address_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_mac_address_stack_active_unit(
                mac_add_list_cli[i])
            if not mac_address_xiq:
                kwargs[
                    'fail_msg'] = f"check_all_the_individual_devices_in_the_stack_monitor_diagnostics() failed;\
                                  Backup/Standby MAC address from the header side is displayed wrong according to the CLI({mac_add_list_cli[i]})"
                self.common_validation.failed(**kwargs)

                return -1

        print("Navigate to master unit and make mac add check")
        res = self.navigate_to_unit_options_from_xiq_diagnostics_page(stacking_info_cli[0][0][1],
                                                                                     stacking_info_cli[0][0][2].upper())
        if res == -1:
            kwargs[
                'fail_msg'] = "check_all_the_individual_devices_in_the_stack_monitor_diagnostics() failed; Unable to navigate to unit options"
            self.common_validation.failed(**kwargs)

            return -1

        self.utils.wait_till(delay=5)
        mac_address_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_mac_address_stack_active_unit(
            mac_add_list_cli[0])
        if not mac_address_xiq:
            kwargs[
                'fail_msg'] = f"check_all_the_individual_devices_in_the_stack_monitor_diagnostics() failed; \
                              Master MAC address from the header side is displayed wrong according to the CLI({mac_add_list_cli[0]})"
            self.common_validation.failed(**kwargs)

            return -1

        kwargs['pass_msg'] = "check_all_the_individual_devices_in_the_stack_monitor_diagnostics() passed"
        self.common_validation.passed(**kwargs)

        return 1

    def navigate_to_unit_1_n_and_hover_over_top_bar_information_stack(self, dut, stacking_info_cli, **kwargs):
        """
        - This keyword gets information from the top bar of the Device360 view.
        - It is assumed that the Device360 window is open in Diagnostics Page.

        :param dut: the dut object
        :apram stacking_info_cli: the cli info of the stack to check against
        :return: dictionary of information obtained from the top bar of the Device360 view
        """
        print("Verify the first seven icons from the top bar for each unit")
        for i in range(1, len(stacking_info_cli[0])):
            if stacking_info_cli[0][i][2].upper() == 'STANDBY':
                self.utils.wait_till(
                    lambda: self.navigate_to_unit_options_from_xiq_diagnostics_page(
                        stacking_info_cli[0][i][1], 'MEMBER'),
                    delay=8, exp_func_resp=True)
            else:
                self.navigate_to_unit_options_from_xiq_diagnostics_page(
                    stacking_info_cli[0][i][1], stacking_info_cli[0][i][2].upper())
            self.utils.wait_till(delay=5)
            self.device360_get_top_bar_information_stack()

        kwargs['pass_msg'] = "navigate_to_unit_1_n_and_hover_over_top_bar_information_stack() passed"
        self.common_validation.passed(**kwargs)

    def match_info_stack_cli_with_xiq(self, dut, stack_info, slot=1, **kwargs):
        """
        - This keyword Verifies if the device information(ip, mac address, software version, model, serial, make, iqagent version) from the header side is displayed correctly according to the cli
        It is assumed that the Device360 window is open in Diagnostics Page and the dropdown is showing the wanted unit. Default is MASTER.
        If the results

        :param dut: the dut object
        :param stack_info: the cli info of the stack to check against
        :param slot: The slot numer of the unit
        """
        slot = int(slot)

        if not stack_info:
            kwargs['fail_msg'] = "match_info_stack_cli_with_xiq() failed; Unable to get info from dut"
            self.common_validation.failed(**kwargs)

            return -1

        print(f"List of info from CLI: {stack_info}")
        ip_address_cli = stack_info[0][0]
        print(f"Ip Add from CLI: {ip_address_cli}")
        ip_address_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_ip_address_stack_active_unit(
            ip_address_cli)
        if not ip_address_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; Ip address from the header side is displayed wrong according to the CLI ({ip_address_cli})"
            self.common_validation.failed(**kwargs)

            return -1

        mac_address_cli = stack_info[1][slot - 1]
        print(f"MAC Add from CLI: {mac_address_cli}")
        mac_address_cli_mapped = mac_address_cli.replace(':', '')
        mac_address_cli_final_mapped = mac_address_cli_mapped.upper()
        print(f"MAC Add from CLI mapped to match XIQ: {mac_address_cli_final_mapped}")
        mac_address_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_mac_address_stack_active_unit(
            mac_address_cli_final_mapped)

        if not mac_address_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; MAC address from the header side is displayed wrong according to the CLI({mac_address_cli})"
            self.common_validation.failed(**kwargs)

            return -1

        soft_version_cli = stack_info[2][slot - 1]
        print(f"Soft version from CLI: {soft_version_cli}")
        soft_version_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_soft_version_stack_active_unit(
            soft_version_cli)
        if not soft_version_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; Soft Version from the header side is displayed wrong according to the CLI({soft_version_cli})"
            self.common_validation.failed(**kwargs)

            return -1

        model_cli = stack_info[3][slot - 1]
        print(f"Dut Model from CLI: {model_cli}")
        if "EXOS" in model_cli:
            model_cli = model_cli.replace("-EXOS", "")
        if stack_info[5][0] == "ExtremeXOS":
            stack_info[5][0] = "Switch Engine"
        if stack_info[5][0] == "Extreme Networks Switch Engine":
            stack_info[5][0] = "Switch Engine"
        # model_cli_mapped = 'Switch Engine ' + model_cli
        model_cli_mapped = stack_info[5][0] + ' ' + model_cli
        print(f"Dut Model from CLI mapped to match XIQ: {model_cli_mapped}")
        model_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_model_stack_active_unit(
            model_cli_mapped)
        if not model_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; Model from the header side is displayed wrong according to the CLI({model_cli})"
            self.common_validation.failed(**kwargs)

            return -1

        serial_number_cli = stack_info[4][slot - 1]
        print(f"Serial number from CLI: {serial_number_cli}")
        serial_number_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_serial_number_stack_active_unit(
            serial_number_cli)
        if not serial_number_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; Serial number from the header side is displayed wrong according to the CLI({serial_number_cli})"
            self.common_validation.failed(**kwargs)

            return -1

        # make_cli = "Switch Engine"
        if stack_info[5][0] == "ExtremeXOS":
            stack_info[5][0] = "Switch Engine"
        else:
            make_cli = stack_info[5][0]
        print(f"Make from CLI: {make_cli}")
        make_xiq = self.dev360.get_device360_monitor_diagnostics_health_item_make_stack_active_unit(
            make_cli)
        if not make_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; Make from the header side is displayed wrong according to the CLI({make_cli}"
            self.common_validation.failed(**kwargs)

            return -1

        iqagent_version_cli = stack_info[6][0]
        print(f"Iqagent version from CLI: {iqagent_version_cli}")
        self.dev360.get_device360_monitor_diagnostics_health_item_iqagent_version_stack_active_unit(
            iqagent_version_cli)
        if not make_xiq:
            kwargs[
                'fail_msg'] = f"match_info_stack_cli_with_xiq() failed; Iqagent Version from the header side is displayed wrong according to the CLI({iqagent_version_cli})"
            self.common_validation.failed(**kwargs)

            return -1

        kwargs['pass_msg'] = "get_info_from_stack() passed"
        self.common_validation.passed(**kwargs)

        return 1

    def device360_get_top_bar_information_stack(self, **kwargs):
        """
        - This keyword gets information from the top bar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
         - ``Device360 Get Top Bar Information``
        :return: dictionary of information obtained from the top bar of the Device360 view
        """

        print("Getting Device360 Top Bar Information")
        device360_info = dict()

        cpu_el = self.dev360.get_topbar_cpu()
        mem_el = self.dev360.get_topbar_memory()
        mac_el = self.dev360.get_topbar_mac_usage_diagnostics()
        uptime_el = self.dev360.get_topbar_uptime_diagnostics()
        temp_el = self.dev360.get_topbar_temperature_diagnostics()
        power_el = self.dev360.get_topbar_power_diagnostics()
        fan_el = self.dev360.get_topbar_fan_diagnostics()

        # Workaround - first element moved to isn't being recognized, so move to Memory element first
        if mem_el:
            self.auto_actions.move_to_element(mem_el)

        if cpu_el:
            self.auto_actions.move_to_element(cpu_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                print(f"Tooltip content for CPU Usage is {tt_text}")
                cpu_values = tt_text.split(":")
                if len(cpu_values) == 2 and cpu_values[0] == "CPU Usage":
                    cpu_value = cpu_values[1].strip()
                    device360_info["cpu_usage"] = cpu_value
                else:
                    print("Unable to parse value for CPU Usage")
                    device360_info["cpu_usage"] = ""
            else:
                print("Could not determine value for CPU Usage")
                device360_info["cpu_usage"] = ""
        else:
            print("Could not find CPU Usage element")
            device360_info["cpu_usage"] = ""

        if mem_el:
            self.auto_actions.move_to_element(mem_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                print(f"Tooltip content for Memory is {tt_text}")
                mem_values = tt_text.split(":")
                if len(mem_values) == 2 and mem_values[0] == "Memory":
                    mem_value = mem_values[1].strip()
                    device360_info["memory_usage"] = mem_value
                else:
                    print("Unable to parse value for Memory Usage")
                    device360_info["memory_usage"] = ""
            else:
                print("Could not determine value for Memory Usage")
                device360_info["memory_usage"] = ""
        else:
            print("Could not find Memory Usage element")
            device360_info["memory_usage"] = ""

        if mac_el:
            self.auto_actions.move_to_element(mac_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                print(f"Tooltip content for MAC Table Utilization is {tt_text}")
                mac_values = tt_text.split(":")
                if len(mac_values) == 2 and mac_values[0] == "MAC Table Utilization":
                    mac_value = mac_values[1].strip()
                    device360_info["mac_usage"] = mac_value
                else:
                    print("Unable to parse value for MAC Table Utilization")
                    device360_info["mac_usage"] = ""
            else:
                print("Could not determine value for MAC Table Utilization")
                device360_info["mac_usage"] = ""
        else:
            print("Could not find MAC Table Utilization element")
            device360_info["mac_usage"] = ""

        if uptime_el:
            self.auto_actions.move_to_element(uptime_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                # This field is currently in the format "Uptime: Last seen: <date>, <time>" so we want to strip
                # off the label ("Uptime: Last seen:"), and remove the comma from the date and time portion.
                # NOTE: This may change when APC-45218 is addressed.
                print(f"Tooltip content for Uptime is {tt_text}")
                tt_text = re.sub('Uptime: Last seen: ', '', tt_text)
                print(f"Stripped tooltip content for Uptime is {tt_text}")
                uptime_values = tt_text.split(",")
                if len(uptime_values) == 2:
                    uptime_date = uptime_values[0].strip()
                    uptime_time = uptime_values[1].strip()
                    device360_info["uptime"] = uptime_date + " " + uptime_time
                else:
                    print("Unable to parse value for Uptime")
                    device360_info["uptime"] = ""
            else:
                print("Could not determine value for Uptime")
                device360_info["uptime"] = ""
        else:
            print("Could not find Uptime element")
            device360_info["uptime"] = ""

        if temp_el:
            self.auto_actions.move_to_element(temp_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                print(f"Tooltip content for temperature is {tt_text}")
                temp_values = tt_text.split(":")
                if len(temp_values) == 2 and temp_values[0] == "Temperature":
                    temp_value = temp_values[1].strip()
                    device360_info["temp"] = temp_value
                else:
                    print("Unable to parse value for temperature")
                    device360_info["temp"] = ""
            else:
                print("Could not determine value for temperature")
                device360_info["temp"] = ""
        else:
            print("Could not find MAC Table Utilization element")
            device360_info["temp"] = ""

        if power_el:
            self.auto_actions.move_to_element(power_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                power_el_text = tt_content.text
                power_supply_text_2 = power_el_text.split('\n')
                power_supply_list = []
                total_power_available = 0
                total_power_consumed = 0
                threshold_power = 0
                for status in power_supply_text_2:
                    if "Total Power Available" in status:
                        total_power_available = re.sub('[^0-9]+', '', status)
                    elif "Total Power Consumed" in status:
                        total_power_consumed = re.sub('[^0-9]+', '', status)
                    elif "Threshold" in status:
                        threshold_power = re.sub('[^0-9]+', '', status)
                    else:
                        if "Power " in status and "Status" not in status:
                            status = re.sub('Power [0-9]: ', '', status)
                            power_supply_list.append(status)
                print(f"Power supply grepped list in D360 is {power_supply_list}")
                device360_info["power_supply"] = power_supply_list
                device360_info["total_power_available"] = total_power_available
                device360_info["total_power_consumed"] = total_power_consumed
                device360_info["threshold_power"] = threshold_power
            else:
                print("Could not parse the values for Power")
                device360_info["power_supply"] = ""
                device360_info["total_power_available"] = ""
                device360_info["total_power_consumed"] = ""
                device360_info["threshold_power"] = ""
        else:
            print("Could not determine values for Power")
            device360_info["power_supply"] = ""
            device360_info["total_power_available"] = ""
            device360_info["total_power_consumed"] = ""
            device360_info["threshold_power"] = ""

        if fan_el:
            self.auto_actions.move_to_element(fan_el)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                fan_status_text = tt_content.text
                fan_status_text_2 = fan_status_text.split('\n')
                print(f"Fan status output list is {fan_status_text}")
                fan_status_list = []
                for status in fan_status_text_2:
                    if "Operating" in status:
                        status1 = re.sub('Tray [0-9] Fan [0-9]: ', '', status)
                        fan_status_list.append(status1)
                    else:
                        if "failed" in status:
                            fan_status_list.append("Unit has failed")
                print(f"Fan status grepped list is {fan_status_list}")
                device360_info["fan_status"] = fan_status_list
            else:
                print("Could not parse the value for Fan")
                device360_info["fan_status"] = ""
        else:
            print("Could not determine value for Fan status")
            device360_info["fan_status"] = ""

        kwargs['pass_msg'] = "device360_get_top_bar_information_stack() passed"
        self.common_validation.passed(**kwargs)

        return device360_info

    def select_ports_d360_port_config(self, isl_ports_dut, **kwargs):
        """
         - This keyword will select multiple ports in (D360-Port Configuration)
        :return: pass message if successfully
        :return: fail message if error
        """

        if self.auto_actions.click_reference(
            lambda: self.dev360.get_d360_monitor_port_details_checkbox_interface(isl_ports_dut)):
            kwargs['pass_msg'] = f"The port {isl_ports_dut} was selected successfully!"
            self.common_validation.passed(**kwargs)
        else:
            kwargs['fail_msg'] = f"The port {isl_ports_dut} cannot be selected."
            self.common_validation.failed(**kwargs)

    def multi_edit_add_port_usage(self):
        '''
        This keyword click on add button for multi edit port usage. This function will open the Create Port Type tab.
        :return: pass message if successfully
        :return: fail message if error
        '''
        self.utils.print_info("Click add port usage from Multi Edit tab to open Create Port Type")
        self.auto_actions.click_reference(self.dev360.get_add_port_type_port_usage_multi_edit)

    def close_multi_edit_vlan_error_message(self):
        """
         - This keyword will close the vlan error message in Multi Edit (D360-Port Configuration).
         - The error message is generated when the VLAN field is empty or contains an invalid value.
        :return: pass message if successfully
        :return: fail message if error
        """
        self.utils.print_info("Close the multi edit vlan error message")
        self.auto_actions.click_reference(self.dev360.get_vlan_error_message_close_multi_edit)

    def check_delta_config_local(self, device_mac, commands_into_delta, **kwargs):
        """
         - This function will check if the commands are present into Delta view tab.
        :return: pass message if successfully
        :return: fail message if error
        """
        if not self.navigator.navigate_to_devices() == 1:
            kwargs['fail_msg'] = "Can't navigate to device page!"
            self.common_validation.failed(**kwargs)
        delta_configs = self.deviceConfig.get_device_config_audit_delta(device_mac)
        if delta_configs:
            for el in commands_into_delta:
                commands_into_delta = False
                if el in delta_configs:
                    commands_into_delta = True
                    print("Command was found into delta :", el)
                    kwargs['pass_msg'] = f"Command was found into Delta: {el}"
                    self.common_validation.passed(**kwargs)
                if not commands_into_delta:
                    print("Command was not found into delta :", el)
                    kwargs['fail_msg'] = f"Command not found into Delta: {el}"
                    self.common_validation.failed(**kwargs)

    def multi_edit_port_count_message(self):
        '''
        This keyword verify if the ports are succesfully selected. Will also verify if the row with selected ports is
        present in Multi Edit tab.
        :return: pass message if successfully
        :return: fail message if error
        '''

        d360_port_count = self.dev360.get_d360_multi_edit_port_count()
        if d360_port_count:
            self.utils.print_info(f"The ports selected are displayed in multi edit tab: {d360_port_count[0].text}")
            return d360_port_count[0].text
        else:
            self.utils.print_info(f"The ports selected are not displayed in multi edit tab: {d360_port_count[0].text}")

    def succesful_message_multi_edit(self):
        """
         - This keyword will verify the success message for Multi Edit configuration.
         It is a different success message depending on the platform it is running on.
        :return: pass message if the success message is generated  and the same as the one in the function
        :return: fail message if error (the message is not generated)
        """

        success_message = self.dev360.get_d360_save_port_configuration_message_multi_edit()
        max_wait = 120
        count = 0
        while (success_message == None) and count < max_wait:
            count += 10
            success_message = self.dev360.get_d360_save_port_configuration_message_multi_edit()
        if success_message:
            self.utils.print_info (f"The configuration was saved successfully: {success_message.text}")
            return success_message.text
        else:
            self.utils.print_info (f"Unable to display the success message: {success_message.text}")


    def succesful_message_multi_edit_exos(self):
        """
         - This keyword will verify the success message for Multi Edit configuration for Switch Engine devices.
        :return: pass message if the success message is generated  and the same as the one in the function
        :return: fail message if error (the message is not generated)
        """
        start_time = int(time.time())
        max_wait = 180
        success_message = self.dev360.get_d360_save_port_configuration_message_exos()
        while not success_message.is_displayed():
            if (int(time.time()) - start_time) < max_wait:
                success_message = self.dev360.get_d360_save_port_configuration_message_exos()
                self.utils.wait_till(delay=2)
            else:
                self.utils.print_info(f"Unable to display the success message: {success_message.text}")
        if success_message:
            self.utils.print_info (f"The configuration was saved successfully: {success_message.text}")
            return success_message.text
        else:
            self.utils.print_info (f"Unable to display the success message: {success_message.text}")


    def succesful_message_multi_edit_voss(self):
        """
         - This keyword will verify the success message for Multi Edit configuration for Fabric Engine devices.
        :return: pass message if the success message is generated  and the same as the one in the function
        :return: fail message if error (the message is not generated)
        """
        start_time = int(time.time())
        max_wait = 180
        success_message = self.dev360.get_d360_save_port_configuration_message_voss()
        while not success_message.is_displayed():
            if (int(time.time()) - start_time) < max_wait:
                success_message = self.dev360.get_d360_save_port_configuration_message_voss()
                self.utils.wait_till(delay=2)
            else:
                self.utils.print_info(f"Unable to display the success message: {success_message.text}")
        if success_message:
            self.utils.print_info (f"The configuration was saved successfully: {success_message.text}")
            return success_message.text
        else:
            self.utils.print_info (f"Unable to display the success message: {success_message.text}")

    def device360_get_stack_ports_by_type(self, port_type, **kwargs):
        """
            Keyword used to get all the ports of type vim or sfp from stack device
            port_type: vim or sfp
            :return: On success: list of all ports ex: [1:59, 1:60,..], on Failure False
        """
        ret_ports = []
        if port_type == "vim":
            ports = self.get_device360_stack_slot_vim_ports()
        elif port_type == "sfp":
            ports = self.get_device360_stack_slot_sfp_ports()
        else:
            kwargs['fail_msg'] = f"'device360_get_stack_ports_by_type()' failed. port_type {port_type} not suported "
            self.common_validation.failed(**kwargs)
            return False
        if not ports:
            kwargs['fail_msg'] = "'device360_get_stack_ports_by_type()' failed. No ports available"
            self.common_validation.failed(**kwargs)
            return False
        for port in ports:
            tag = port.get_attribute("data-automation-tag")
            ret_ports.append(tag.split('-')[2])
        if len(ret_ports) == 0:
            kwargs['fail_msg'] = "'device360_get_stack_ports_by_type()' failed. XPATH have no automation tag"
            self.common_validation.failed(**kwargs)
            return False
        kwargs['pass_msg'] = f"Ports for type {port_type} are: {ret_ports}"
        self.common_validation.passed(**kwargs)
        return ret_ports

    def device360_change_slot_view(self, unit, **kwargs):
        """
           This keyword is used to switch between slot port config pages
           It Assumes That Already Navigated to Device360->Port Configuration->Port Settings & Aggregation

           :param unit: string with slot number
           :return: True if successful or False on failure
           """
        # Get slots dropdown
        slots_dropdown = self.get_device360_port_config_stack_slots_dropdown()
        if slots_dropdown:
            self.utils.print_info("Clicking on slots dropdown")
            self.auto_actions.click(slots_dropdown)
            sleep(5)
        else:
            kwargs['fail_msg'] = "'device360_change_slot_view()' failed. Slots dropdown not found"
            self.common_validation.failed(**kwargs)
            return False

        # Get next slot
        next_slot = self.get_device360_slot_from_dropdown(unit=unit)
        if next_slot:
            self.utils.print_info("Clicking on next slot")
            self.auto_actions.click(next_slot)
            sleep(5)
        else:
            kwargs['fail_msg'] = "'device360_change_slot_view()' failed.Next slot not found in dropdown list"
            self.common_validation.failed(**kwargs)
            return False
        kwargs['pass_msg'] = f"Stack slot changed to slot {unit}"
        self.common_validation.passed(**kwargs)
        return True

    def device360_aggregate_ports(self, ports, click_lacp=True, device='', **kwargs):
        """
           This keyword is used to aggregate ports from same/different stack slots
           It Assumes That Already Navigated to Device360->Port Configuration->Port Settings & Aggregation

           :param click_lacp:  boolean value if needed to click the lacp toggle
           :param ports: port list
           :return: True if successful, False if failed, 1 if couldn't aggregate from other slot
           """
        click_checkbox_or_button = None
        if device == "stack":
            if not self.device360_change_slot_view(ports[0].split(":")[0]):
                kwargs['fail_msg'] = "Failed to change stack slot."
                self.common_validation.failed(**kwargs)
                return False
            click_checkbox_or_button = self.get_device360_port_settings_and_aggregation_interface_exos_standalone(ports[0].split(":")[1])
        elif device == "standalone":
            click_checkbox_or_button = self.get_device360_port_settings_and_aggregation_interface_exos_standalone(
                ports[0])
        else:
            kwargs['fail_msg'] = "Please give a device type!"
            self.common_validation.fault(**kwargs)
            return False
        if click_checkbox_or_button:
            self.utils.print_info("Clicking on port checkbox")
            self.auto_actions.click(click_checkbox_or_button)
        else:
            kwargs['fail_msg'] = "Checkbox not found"
            self.common_validation.failed(**kwargs)
            return False

        # Aggregate
        aggregate_btn = self.get_device360_configure_port_aggregate_button()
        if aggregate_btn:
            self.utils.print_info("Clicking 'Aggregate Selected Ports' button")
            self.auto_actions.click(aggregate_btn)
            sleep(5)
        else:
            kwargs['fail_msg'] = "'Aggregate Selected Ports' button not found"
            self.common_validation.failed(**kwargs)
            return False

        # Get cancel button reference
        cancel_button = self.get_device360_lag_cancel_button()
        if not cancel_button:
            kwargs['fail_msg'] = "Could not find cancel button"
            self.common_validation.failed(**kwargs)
            return False

        # Add other ports to aggregation
        for i in range(1, len(ports)):
            if device == "stack":
                if ports[i - 1].split(":")[0] != ports[i].split(":")[0]:
                    # Switching to other slot
                    other_slot = self.get_device360_aggregate_choose_slot(ports[i].split(":")[0])
                    if other_slot:
                        self.utils.print_info("Changing to other slot")
                        self.auto_actions.click(other_slot)
                    else:
                        kwargs['fail_msg'] = "Failed to change to other slot"
                        self.common_validation.failed(**kwargs)
                        self.auto_actions.click(cancel_button)
                        return False
            # Choose the next port
            available_port = self.get_device360_aggregate_available_port(ports[i])
            if available_port:
                self.utils.print_info("Choosing next available port")
                self.auto_actions.click(available_port)
            else:
                self.utils.print_info("Ports are not available in this slot. Skipping..")

            # Add next port
            add_port_to_lacp = self.get_device360_aggregate_add_button()
            if add_port_to_lacp:
                self.utils.print_info("Clicking on add port")
                self.auto_actions.click(add_port_to_lacp)
            else:
                kwargs['fail_msg'] = "Add port not found"
                self.common_validation.failed(**kwargs)
                self.auto_actions.click(cancel_button)
                return False

        # Toggle lacp on window
        if click_lacp:
            lacp_switch = self.get_device360_lacp_toggle()
            if lacp_switch:
                self.utils.print_info("Clicking LACP toggle")
                self.auto_actions.click(lacp_switch)
            else:
                kwargs['fail_msg'] = "LACP toggle not found"
                self.common_validation.failed(**kwargs)
                self.auto_actions.click(cancel_button)
                return False

        # Save
        lag_save_button = self.get_device360_lag_save_button()
        if lag_save_button:
            self.utils.print_info("Clicking Save button")
            self.auto_actions.click(lag_save_button)
            sleep(10)
        else:
            kwargs['fail_msg'] = "Save button not found"
            self.common_validation.failed(**kwargs)
            self.auto_actions.click(cancel_button)
            return False

        # Save port Config
        self.utils.wait_till(func=self.get_device360_lag_popup_spinner, timeout=60, delay=1.5, exp_func_resp=False)
        self.utils.print_info("Clicking Save port config button")
        if self.auto_actions.click_reference(self.get_device360_save_port_config) == 1:
            self.utils.print_info("Successfully clicked on Save Port Config")
        else:
            kwargs['fail_msg'] = "Save port config button not found"
            self.common_validation.failed(**kwargs)
            return False

        # Check lacp formed in Device360
        if self.get_device360_lacp_label(port=ports[0]):
            kwargs['pass_msg'] = "LAG link is available."
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "LAG link is not available"
            self.common_validation.failed(**kwargs)
            return False

    def device360_check_aggregated_ports_number(self, reference_num, no_slots, **kwargs):
        """
           This keyword is used to check the number of aggregated ports matches the reference
           It Assumes That Already Navigated to Device360->Port Configuration->Port Settings & Aggregation

           :param no_slots: number of slots
           :param reference_num: reference integer
           :return: If match True, else False
           """
        i = 1
        no_of_ports = 0
        while self.device360_change_slot_view(str(i)):
            i = i + 1
            lag_rows = self.get_device360_configure_aggregated_port_settings_aggregation_rows()
            if lag_rows:
                no_of_ports = no_of_ports + len(lag_rows)
            if i == no_slots+1:
                break

        if no_of_ports == reference_num:
            kwargs['pass_msg'] = "Number of LAG link matches."
            self.common_validation.passed(**kwargs)
            return True
        else:
            kwargs['fail_msg'] = "LAG number does not match."
            self.common_validation.failed(**kwargs)
            return False

    def device360_add_remove_lag_ports(self, master_port, ports, action='add', device='', **kwargs):
        """
           This keyword is used to remove port aggregation
           It Assumes That Already Navigated to Device360->Port Configuration->Port Settings & Aggregation

           :param device: type of device stack or standalone
           :param ports: list of ports: ex: ["1:1", "2:1", "3:2"]
           :param master_port: master port of LAG
           :param action: add or remove ports from LAG
           :return: True if successful or False on failure
           """
        if device == "stack":
            if not self.device360_change_slot_view(master_port.split(":")[0]):
                kwargs['fail_msg'] = "Change slot failed."
                self.common_validation.failed(**kwargs)
                return False
        if action == 'remove':
            aggregated_ports = self.get_device360_lacp_label(port=master_port)
            if aggregated_ports:
                self.utils.print_info("Clicking on aggregated ports label")
                self.auto_actions.click(aggregated_ports)
            else:
                kwargs['fail_msg'] = "Failed to find aggregated port."
                self.common_validation.failed(**kwargs)
                return False

            # Get cancel button reference
            cancel_button = self.get_device360_lag_cancel_button()
            if not cancel_button:
                kwargs['fail_msg'] = "Could not find cancel button."
                self.common_validation.failed(**kwargs)
                return False

            selected_port = self.get_device360_aggregate_selected_port(ports[0])
            if selected_port:
                self.utils.print_info("Choosing next port")
                self.auto_actions.click(selected_port)
            else:
                tt_msg = self.dev360.get_tooltip_content().text
                kwargs['fail_msg'] = f"Failed due to error {tt_msg}"
                self.common_validation.failed(**kwargs)
                self.auto_actions.click(cancel_button)
                return False

            # Remove ports from aggregation
            for i in range(len(ports)):
                # Remove the next port
                remove_port_from_lacp = self.get_device360_aggregate_remove_button()
                if remove_port_from_lacp:
                    self.utils.print_info("Clicking on remove port")
                    self.auto_actions.click(remove_port_from_lacp)
                else:
                    tt_msg = self.dev360.get_tooltip_content().text
                    self.auto_actions.click(cancel_button)
                    kwargs['fail_msg'] = f"Failed due to error {tt_msg}."
                    self.common_validation.failed(**kwargs)
                    return False

            # Save
            lag_save_button = self.get_device360_lag_save_button()
            if lag_save_button:
                self.utils.print_info("Clicking Save button")
                self.auto_actions.click(lag_save_button)
            else:
                tt_msg = self.dev360.get_tooltip_content().text
                kwargs['fail_msg'] = f"Failed due to error {tt_msg}"
                self.common_validation.failed(**kwargs)
                self.auto_actions.click(cancel_button)
                return False

            # Save port Config
            self.utils.wait_till(func=self.get_device360_lag_popup_spinner, timeout=60, delay=1.5, exp_func_resp=False)
            self.utils.print_info("Clicking Save port config button")
            if self.auto_actions.click_reference(self.get_device360_save_port_config) == 1:
                self.utils.print_info("Successfully clicked on Save Port Config")
            else:
                kwargs['fail_msg'] = "Save port config button not found"
                self.common_validation.failed(**kwargs)
                return False

            # Check lacp not visible anymore in Device360
            if self.get_device360_lacp_label(port=ports[0]):
                self.utils.print_info(f"LAG {master_port} is still there after trying to delete it.")
                kwargs['fail_msg'] = "Remove LAG failed."
                self.common_validation.failed(**kwargs)
                return False
            kwargs['pass_msg'] = f"Ports {ports} were removed from LAG."
            self.common_validation.passed(**kwargs)
            return True
        elif action == 'add':
            aggregated_ports = self.get_device360_lacp_label(port=master_port)
            if aggregated_ports:
                self.utils.print_info("Clicking on aggregated ports label")
                self.auto_actions.click(aggregated_ports)
            else:
                kwargs['fail_msg'] = "Failed to find aggregated port."
                self.common_validation.failed(**kwargs)
                return False
            for port in ports:
                self.auto_actions.click(self.get_device360_aggregate_available_port(port=port))
                self.auto_actions.click(self.get_device360_aggregate_add_button())
            self.auto_actions.click(self.get_device360_lag_save_button())
            self.auto_actions.click(self.get_device360_save_port_config())
            kwargs['pass_msg'] = f"Ports {ports} were added to LAG."
            self.common_validation.passed(**kwargs)
            return 1

    def select_monitor_diagnostics_port_details(self, **kwargs):
        """
        - This keyword clicks the Port Details button on the Monitor ->Diagnostics tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details``
        :return: 1 if Monitor> Diagnostics> Port Details was selected, else -1
        """
        self.auto_actions.click_reference(self.get_device360_port_details_button)

    def select_diagnostics_port_details_table(self, **kwargs):
        """
        - This keyword clicks the Port Details table on the Monitor ->Diagnostics ->Port Details tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> click Port Details table
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(self.get_device360_monitor_diagnostics_port_details_table)

    def click_device360_diagnostics_select_all_button(self, unit, **kwargs):
        """
        - This keyword clicks the 'Select All Ports' button on the Port Diagnostics page in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics page.
        - Keyword Usage:
        - ``Device360 Port Diagnostics Select All Ports``
        :return: 1 if button was clicked, else -1
        """
        self.auto_actions.click_reference(lambda: self.get_device360_diagnostics_select_all_button(unit))

    def click_device360_diagnostics_deselect_all_button(self, unit, **kwargs):
        """
        - This keyword clicks the 'Select All Ports' button on the Port Diagnostics page in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics page.
        - Keyword Usage:
        - ``Device360 Port Diagnostics Select All Ports``
        :return: 1 if button was clicked, else -1
        """
        self.auto_actions.click_reference(lambda: self.get_device360_diagnostics_deselect_all_button(unit))

    def get_device360_diagnostics_all_port_table_rows(self):
        """
        - This keyword returnes the rows in the Port Details table.
        It assumes the Device360 Window is open and on the Monitor> Diagnostics page.
        """
        scroll_element = self.auto_actions.click_reference(self.get_device360_diagnostics_ports_table_scroll)
        if scroll_element:
            for _ in range(10):
                self.auto_actions.scroll_down()
        return self.get_device360_monitor_diagnostics_port_details_table_rows()

    def select_device360_diagnostics_actions_button(self, **kwargs):
        """
        - This keyword clicks the Port Details table on the Monitor ->Diagnostics ->Port Details tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> click Port Details table
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(self.get_device360_diagnostics_port_details_actions_button)

    def select_device360_diagnostics_bounce_port_button(self, **kwargs):
        """
        - This keyword clicks the Bounce Port button under Actions on  the Monitor ->Diagnostics ->Port Details tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> click Port Details table --> Click Actions --> Click Bounce Port
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(self.get_device360_diagnostics_actions_bounce_port_button)

    def select_device360_diagnostics_bounce_poe_button(self, **kwargs):
        """
        - This keyword clicks the Bounce Poe button under Actions on  the Monitor ->Diagnostics ->Port Details tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> click Port Details table --> Click Actions --> Click Bounce Poe
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(self.get_device360_diagnostics_actions_bounce_poe_button)

    def device360_diagnostics_click_on_port_icon(self, port_nr, **kwargs):
        """
        - This keyword clicks on port icon in the Device360 Diagnostics view based on the specified port.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Diagnostics Click On Port Icon``
        :port: Specifies the port value
        :return: Displayed Port icon name in the Device360 view
        """
        self.auto_actions.click_reference(lambda: self.get_device360_diagnostics_wireframe_port(port_nr))

    def select_device360_diagnostics_port_select_button(self, port_nr, **kwargs):
        """
        - This keyword selects ports in Port Details table on the Monitor ->Diagnostics ->Port Details tab in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> Select port
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(lambda: self.get_device360_diagnostics_port_table_select_checkbox(port_nr))

    def wait_for_device360_diagnostics_actions_message(self, max_wait = 60, **kwargs):
        """
        - This keyword waits for the success message generated when  Bounce Port, Bounce PoE or Clear Mac Locking
        actions are issued on a list of ports.
        - The list is updated as ports are enabled/bounced one by one so this function waits for the success message
        to be generated for all ports
        """
        start_time = int(time.time())
        message  = self.get_device360_diagnostics_bounce_port_message()

        while message is None:
            if (int(time.time()) - start_time) < max_wait:
                message = self.get_device360_diagnostics_bounce_port_message()
                self.utils.wait_till(delay=1)
            else:
                kwargs['fail_msg'] = "Message not displayed"
                return None
        temp_message = message
        while temp_message and (int(time.time()) - start_time) < max_wait:
            temp_message = self.get_device360_diagnostics_bounce_port_message()
            if temp_message is None:
                break
            else:
                message = temp_message
                self.utils.wait_till(delay=1)
        return message


    def select_device360_diagnostics_stack_unit(self, slot, **kwargs):
        """
        - This keyword clicks the stack unit in the unit dropdown list on  the Monitor ->Diagnostics page in the Device360 dialog window.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click  down arrow to select stack unit - > select unit
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        actions_btn1 = self.auto_actions.click_reference(self.get_device360_diagnostics_current_unit)
        if actions_btn1:
            kwargs['pass_msg'] = "Clicked current unit to display Stack dropdown list"
            self.auto_actions.click_reference(lambda: self.get_device360_diagnostics_dropdown_unit(slot))

    def select_device360_diagnostics_actions_clear_mac_locking(self, **kwargs):
        """
        - This keyword clicks the Port Details table on the Monitor ->Diagnostics ->Port Details ->Actions -> Enable Mac Locking button.
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> Select Port disabled by Mac Locking ->Click Enable MAC Locking button
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(self.get_device360_diagnostics_actions_clear_mac_locking)

    def click_device360_diagnostics_actions_refresh_button(self, **kwargs):
        """
        - This keyword clicks the Refresh button on the Monitor ->Diagnostics ->Port Details page
          It assumes the Device360 Window is open and on the Monitor->Diagnostics ->Port Details tab.
        - Flow: Device 360 Window --> Monitor tab --> Diagnostics --> click Port Details button --> click Refresh page button
        - Keyword Usage:
         - ``Select Monitor Diagnostics Port Details table``
        """
        self.auto_actions.click_reference(self.get_device360_diagnostics_port_details_refresh_button)
    def configure_vlan_range_d360(self, dut, port_numbers, vlan_range, **kwargs):
        """Method that configures given ports as trunk port with specific trunk vlan id.

        Currently this method supports only switches with cli_type - exos.

        Args:
            dut (dict): the dut, e.g. tb.dut1
            ports (str): the ports that will be configured - e.g. '1,3,5,10'
            vlan_range (str): trunk vlan id values - e.g.  '400-500'

        Returns:
            int: 1 if the function call has succeeded else -1

        """
        supported_devices = ["EXOS"]

        if dut.cli_type.upper() not in supported_devices:
            kwargs["fail_msg"] = f"Chosen device is not currently supported. Supported devices: {supported_devices}"
            self.common_validation.fault(**kwargs)
            return -1

        if dut.cli_type.upper() == "EXOS":
            if dut.platform.upper() == 'STACK':

                for slot in range(1, len(dut.serial.split(',')) + 1):
                    self.navigator.navigate_to_devices()
                    self.dev.refresh_devices_page()
                    self.navigator.navigate_to_device360_page_with_mac(dut.mac)
                    self.navigator.navigate_to_port_configuration_d360()
                    self.select_stack_unit(slot)
                    self.device360_configure_ports_trunk_stack(
                        port_numbers=port_numbers, trunk_native_vlan="1", trunk_vlan_id=vlan_range, slot=slot)
            else:

                self.navigator.navigate_to_devices()
                self.dev.refresh_devices_page()
                self.navigator.navigate_to_device360_page_with_mac(dut.mac)
                self.navigator.navigate_to_port_configuration_d360()
                self.device360_configure_ports_trunk_vlan(
                    port_numbers=port_numbers, trunk_native_vlan="1", trunk_vlan_id=vlan_range)

        self.dev.refresh_devices_page()

        kwargs["pass_msg"] = "Successfully configured the ports"
        self.common_validation.passed(**kwargs)
        return 1


    def get_supplemental_cli_vlan(self, mac, os, vlan_min, vlan_max, option="create", profile_scli="default_profile", **kwargs):
        """Method that generates the create/delete VLAN cli commands and use them in a given supplemental cli profile object.
        Currently this method supports only os EXOS/VOSS.

        Args:
            mac (dict): the mac of the device
            os (str): the os of the device
            vlan_min (int): lower bound of the vlan range
            vlan_max (int): upper bound of the vlan range
            option (str): "create"|"delete"
            profile_scli (str): the name of the scli profile
        Returns:
            int: 1 if the function call has succeeded else -1
        """
        vlan_list = []

        if option not in ["create", "delete"]:
            kwargs["fail_msg"] = "Wrong option! Choose 'create' or 'delete'."
            self.common_validation.failed(**kwargs)
            return -1

        if os.lower() not in ["exos", "voss"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.common_validation.fault(**kwargs)
            return -1

        self.navigator.navigate_to_device360_page_with_mac(device_mac=mac)

        if os.lower() == "voss":

            vlan_list.append("configure terminal")

            if option == "create":

                self.utils.print_info(f"Creating {vlan_min}-{vlan_max} vlans")
                for vlan in range(vlan_min, vlan_max + 1):
                    vlan_commands = f"vlan create {vlan} type port-mstprstp 0"
                    vlan_list.append(vlan_commands)
                i = 10
                for show in range(10):
                    show = "show running-config | no-more"
                    vlan_list.insert(i, show)
                    i += 10
                vlan_list_one_string = ",".join(vlan_list)
                self.get_supplemental_cli(profile_scli, vlan_list_one_string)

            elif option == "delete":

                self.utils.print_info(f"Deleting {vlan_min}-{vlan_max} vlans")
                for vlan in range(vlan_min, vlan_max + 1):
                    vlan_commands = f"vlan delete {vlan}"
                    vlan_list.append(vlan_commands)
                vlan_list_one_string = ",".join(vlan_list)
                self.get_supplemental_cli(profile_scli, vlan_list_one_string)

        elif os.lower() == "exos":

            if option.lower() == "create":

                self.utils.print_info(f"Creating {vlan_min}-{vlan_max} vlans")
                vlan_commands_1 = f"create vlan {vlan_min}-{int(vlan_max / 4)}"
                vlan_commands_2 = f"create vlan {int(vlan_max / 4 + 1)}-{int(vlan_max / 2)}"
                vlan_commands_3 = f"create vlan {int(vlan_max / 2 + 1)}-{vlan_max}"
                vlan_list.append(vlan_commands_1)
                vlan_list.append(vlan_commands_2)
                vlan_list.append(vlan_commands_3)
                vlan_list_one_string = ",".join(vlan_list)
                self.get_supplemental_cli(profile_scli, vlan_list_one_string)

            elif option.lower() == "delete":

                self.utils.print_info(f"Deleting {vlan_min}-{vlan_max} vlans")
                vlan_commands_1 = f"delete vlan {vlan_min}-{int(vlan_max / 4)}"
                vlan_commands_2 = f"delete vlan {int(vlan_max / 4 + 1)}-{int(vlan_max / 2)}"
                vlan_commands_3 = f"delete vlan {int(vlan_max / 2 + 1)}-{vlan_max}"
                vlan_list.append(vlan_commands_1)
                vlan_list.append(vlan_commands_2)
                vlan_list.append(vlan_commands_3)
                vlan_list_one_string = ",".join(vlan_list)
                self.get_supplemental_cli(profile_scli, vlan_list_one_string)

        kwargs["pass_msg"] = "Successfully created the supplemental cli profile with the generated commands."
        self.common_validation.passed(**kwargs)
        return 1

    def check_overview_row_table_by_port(self, port_name, **kwargs):
        """
        Keyword to return the value of the cell from D360 Overview status main page for a given port.
        :param kwargs = column name. Valid inputs are "LLDP NEIGHBOR","LINK AGGREGATION","PORT STATUS","TRANSMISSION MODE", "PORT MODE",
                        "ELRP ENABLED VLAN(S)","ACCESS VLAN","TAGGED VLAN(S)","MAC LOCKING","TRAFFIC RECEIEVED (RX)",
                        "TRAFFIC TRANSMITTED (TX)","POWER USED","PORT SPEED"
        :param port_name: a string with the specific port
        -Keyword Usage:
                check overview row table by port    "1/1" or "1" column_name="PORT STATUS"
        :return: A string with the value of intersection of port name cell with the head of the table name. Eg: take the
                 port status of port 5. It will return "Auto"
                -1 if the status port was not found
        """
        self.select_pagination_size("100")
        rows_items = self.get_d360_monitor_items_rows()
        self.utils.print_info(len(self.get_d360_monitor_items_rows()))
        if rows_items:
            port_row = self.device360_get_row_specified_port_name(rows_items, port_name)
            self.auto_actions.click(port_row)
            self.utils.print_info("Found row for port: ", port_row.text)
        else:
            self.utils.print_info("Port rows are not displayed. Check the tab")
            kwargs['fail_msg'] = "Port rows are not displayed. Check the tab"
            self.common_validation.failed(**kwargs)
            return -1
        column_to_check = kwargs.get("column_name", "")
        if column_to_check == "LLDP NEIGHBOR":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "LINK AGGREGATION":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "PORT STATUS":
            self.utils.print_info("Checking PORT STATUS")
            port_status = self.get_d360_port_status_overview(port_row)
            if port_status:
                self.utils.print_info(f"Port status for port {port_name} is {port_status.text}")
                return port_status.text
            else:
                self.utils.print_info("'PORT STATUS' not found")
                kwargs['fail_msg'] = "'PORT STATUS' not found"
                self.common_validation.failed(**kwargs)
                return -1
        elif column_to_check == "TRANSMISSION MODE":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "PORT MODE":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "ELRP ENABLED VLAN(S)":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "ACCESS VLAN":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "TAGGED VLAN(S)":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "MAC LOCKING":
            self.utils.print_info("Checking MAC LOCKING")
            mac_locking = self.get_d360_mac_locking_overview(port_row)
            if mac_locking:
                self.utils.print_info(f"MAC locking for port {port_name} is {mac_locking.text}")
                return mac_locking.text
            else:
                self.utils.print_info("'PORT STATUS' not found")
                kwargs['fail_msg'] = "'PORT STATUS' not found"
                self.common_validation.failed(**kwargs)
                return -1
        elif column_to_check == "TRAFFIC RECEIVED (RX)":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "TRAFFIC TRANSMITTED (TX)":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "POWER USED":
            self.utils.print_info("For future development if needed.")
        elif column_to_check == "PORT SPEED":
            port_speed_row = self.get_d360_monitor_port_speed(port_row)
            if port_speed_row:
                self.utils.print_info("Port speed for port {} is {}".format(port_name, port_speed_row.text))
                return port_speed_row.text
            else:
                self.utils.print_info("Port speed status not found")
                kwargs['fail_msg'] = "Port speed status not found"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['fail_msg'] = "No valid input. Please check again."
        self.common_validation.failed(**kwargs)
        return -1

    def navigate_to_port_config_options(self, option, **kwargs):
        """
        This function selects one of the option of the port configuration menu. It assumes D360 is already opened.
        :param option: Tab option name to navigate to. Valid options are: port-details, port-settings, stp, storm-control,
                                                                        mac-locking, voice, pse(only for VOSS), elrp
        :keyword usage navigate to port config options ${option}
        :return: 1 if the navigation is succesfully.
        """
        option_tab_after_click = None
        self.utils.print_info("Navigate to port configuration.")
        self.device360_navigate_to_port_configuration()
        page_loading = self.get_wait_for_port_config_to_load()
        while "fn-hidden" not in page_loading.get_attribute("class"):
            sleep(2)
            page_loading = self.get_wait_for_port_config_to_load()
        self.utils.print_info(f"Selecting {option} tab.")
        option_tab = self.get_d360_port_config_option_tab(option)
        if option_tab:
            self.auto_actions.click(option_tab)
            self.utils.print_info(f"Successfully clicked on {option}.")
            option_tab_after_click = self.get_d360_port_config_option_tab(option)
        else:
            kwargs['fail_msg'] = "'navigate_to_port_config_options' failed. No tab available or hidden"
            self.common_validation.failed(**kwargs)
        if "ui-tab-active" in option_tab_after_click.get_attribute("class"):
            kwargs['pass_msg'] = f"Successfully navigate to '{option}'."
            self.common_validation.passed(**kwargs)
            return 1

    def configure_mac_locking_from_port_config(self, port, mac_lock="", max_first_limit="", disable_port="",
                                               link_down="", remove_mac="", **kwargs):
        """
         - This keyword will change MAC locking state of a list of ports from Device level config
         It assumes that MAC locking is already globally enabled on a device template
         :param: mac_lock= OFF/ON, max_first_limit=1-600, disable_port=ON/OFF, link_down=clear macs/retain macs,
                remove_mac=ON/OFF
        :return: -1 if error
        """
        port_index = int(port)-1
        self.utils.print_info("Navigate to MAC locking tab option from 'Port Configuration' menu.")
        assert self.navigate_to_port_config_options('mac-locking') == 1, "Failed to navigate to MAC Locking tab."
        mac_locking_status = self.get_d360_monitor_mac_locking_on_off(port_index)
        if mac_lock and not mac_locking_status.is_selected() and mac_lock == "ON":
            self.auto_actions.click(mac_locking_status)
            self.utils.print_info(f"Successfully set MAC Locking 'Status' to {mac_lock} for port {port}")
        elif mac_lock and mac_locking_status.is_selected() and mac_lock == "OFF":
            self.auto_actions.click(mac_locking_status)
            self.utils.print_info(f"Successfully set MAC Locking 'Status' to {mac_lock} for port {port}")
        elif mac_lock and mac_locking_status.is_selected() and mac_lock == "ON":
            kwargs['fail_msg'] = f"MAC locking 'Status' for port '{port}' is already set to '{mac_lock}'.Verify it was disabled first!"
            self.common_validation.failed(**kwargs)
            return -1
        elif mac_lock and not mac_locking_status.is_selected() and mac_lock == "OFF":
            self.utils.print_info(f"MAC locking 'Status' for port '{port}' is set to default {mac_lock} state.")

        max_first_arrival_box = self.get_d360_monitor_mac_locking_max_first_arrival_limit(port_index)
        if max_first_limit and max_first_arrival_box and max_first_limit == "600":
            self.utils.print_info(f"'Max first arrival' for port '{port}' is set to default value of {max_first_limit}.")
        elif max_first_limit:
            self.auto_actions.send_keys(max_first_arrival_box, max_first_limit)
            self.auto_actions.send_enter(max_first_arrival_box)
            if "form-error" in max_first_arrival_box.get_attribute("class"):
                self.utils.print_info("Error! Maximum limit of 600 has been exceeded.")
                return self.get_mac_locking_exceed_limit_error().get_attribute("data-tooltip")
            else:
                self.utils.print_info(f"Successfully set 'Max arrival' to {max_first_limit} for port {port}.")

        disable_port_toggle = self.get_d360_mac_locking_disable_port(port_index)
        if disable_port_toggle and not disable_port_toggle.is_selected() and disable_port == "ON":
            self.auto_actions.click(disable_port_toggle)
            self.utils.print_info(f"Successfully set 'Disable Port' to {disable_port} for port {port}")
        elif disable_port_toggle and disable_port_toggle.is_selected() and disable_port == "OFF":
            self.auto_actions.click(disable_port_toggle)
            self.utils.print_info(f"Successfully set 'Disable Port' to {disable_port} for port {port}")
        elif disable_port_toggle and disable_port_toggle.is_selected() and disable_port == "ON":
            kwargs['fail_msg'] = f"'Disable Port' for port '{port}' is already set to '{disable_port}'.Verify it was disabled first!"
            self.common_validation.failed(**kwargs)
            return -1
        elif disable_port_toggle and not disable_port_toggle.is_selected() and disable_port == "OFF":
            self.utils.print_info(f"'Disable Port' for port '{port}' is set to default {disable_port} state.")

        link_down_action_dropdown = self.get_d360_mac_locking_link_down_action(port_index)
        if link_down:
            print(f"To be developed if needed {link_down_action_dropdown}")

        remove_mac_toggle = self.get_d360_mac_locking_remove_mac_toggle(port_index)
        if remove_mac and not remove_mac_toggle.is_selected() and remove_mac == "ON":
            self.auto_actions.click(remove_mac_toggle)
            self.utils.print_info(f"Successfully set MAC Locking 'Remove MAC' to {remove_mac} for port {port}")
        elif remove_mac and remove_mac_toggle.is_selected() and remove_mac == "OFF":
            self.auto_actions.click(remove_mac_toggle)
            self.utils.print_info(f"Successfully set MAC Locking 'Remove MAC' to {remove_mac} for port {port}")
        elif remove_mac and remove_mac_toggle.is_selected() and remove_mac == "ON":
            kwargs['fail_msg'] = f"MAC locking 'Remove MAC' for port '{port}' is already set to '{remove_mac}'.Verify it was disabled first!"
            self.common_validation.failed(**kwargs)
            return -1
        elif remove_mac and not remove_mac_toggle.is_selected() and remove_mac == "OFF":
            self.utils.print_info(f"MAC locking 'Remove MAC' for port '{port}' is set to default {remove_mac} state.")

        kwargs['pass_msg'] = "Successfully set up parameters for MAC locking in D360."
        self.common_validation.passed(**kwargs)
        return 1

    def navigate_wireless_interface(self):
        """
        - This keyword used to navigate to the wireless interface page in device360 page
        - Keyword Usage
         - ``Navigate Wireless Interface``

        """
        self.utils.print_info("Clicking on Wireless Interface")
        self.auto_actions.click(self.dev360.get_device360_wireless_interface_tab())
        return 1

    def navigateto_device360_withmac(self,device_mac=""):
        """
        - This keyword used to navigate to the wireless interface page in device360 page
        - Keyword Usage
         - ``Navigate To Device360 With MAC     ${DEVICE_MAC}``

        """
        self.utils.print_info("Navigate to device 360")
        self.navigator.navigate_to_device360_page_with_mac(device_mac)
        return 1


    def device360_get_total_wireless_clients(self):
        """
        - This keyword gets the total clients from wireless page in the Device360 view.
        - It is assumed that the Device360 window is open and on the Overview tab.
        - Keyword Usage
         - ``Device360 Get Total Wireless Clients``
        :return: total number of clients displayed in the wireless Device360 view
        """
        ret_val = ""

        self.utils.print_info("Getting Device360 Total Wireless Count")
        sleep(5)
        total_count = self.dev360.get_device360_total_wireless_clients()
        sleep(5)
        if total_count:
            ret_val = total_count.text
        else:
            self.utils.print_info("Unable to get the total clients count")

        return ret_val

    def device360_get_wireless_combinedscore(self):
        """
        - This keyword gets the total clients from wireless page in the Device360 view.
        - It is assumed that the Device360 window is open and on the Overview tab.
        - Keyword Usage
         - ``Device360 Get Wireless CombinedScore``
        :return: total number of clients displayed in the wireless Device360 view
        """
        ret_val = ""

        self.utils.print_info("Getting Device360 wireless combined score")
        self.auto_actions.click(self.get_device360_wireless_combinedscoretab())
        sleep(5)
        total_score = self.dev360.get_device360_wireless_combinedscore()
        sleep(5)
        if total_score:
            ret_val = total_score.text
        else:
            self.utils.print_info("Unable to get the wireless combined score")

        return ret_val

    def device360_get_wireless_wifi6gscore(self):
        """
        - This keyword gets the total clients from wireless page in the Device360 view.
        - It is assumed that the Device360 window is open and on the Overview tab.
        - Keyword Usage
         - ``Device360 Get Wireless Wifi6GScore``
        :return: total number of clients displayed in the wireless Device360 view
        """
        ret_val = ""
        self.utils.print_info("Getting Device360 wifi 6G score ")
        self.auto_actions.click(self.get_device360_wireless_wifi6gscoretab())
        sleep(5)
        total_score = self.dev360.get_device360_wireless_wifi6gscore()
        sleep(5)
        if total_score:
            ret_val = total_score.text
        else:
            self.utils.print_info("Unable to get the wifi 6G score")
        return ret_val

    def device360_get_wireless_wifi2widget_client(self):
        """
        - This keyword gets the total clients from wireless page in the Device360 view.
        - It is assumed that the Device360 window is open and on the Overview tab.
        - Keyword Usage
         - ``Device360 Get Wireless Wifi2Widget Client``
        :return: total number of clients displayed in the wireless Device360 view
        """
        ret_val = ""
        self.utils.print_info("Getting Device360 Total Wireless Count")
        sleep(5)
        total_count = self.dev360.get_device360_wireless_wifi2widgetclient()
        sleep(5)
        if total_count:
            ret_val = total_count.text
        else:
            self.utils.print_info("Unable to get the widget data")
        return ret_val

    def device360_get_sidebar_uniqueclient_count(self):
        """
        - This keyword gets the unique client side bar in the Device360 view.
        - It is assumed that the Device360 window is open
        - Keyword Usage
         - ``Device360 Get Sidebar UniqueClient Count``
        :return: Unique number of clients displayed in the leftpane
        """
        ret_val = ""

        self.utils.print_info("Getting Device360 unique client Count")
        sleep(5)
        total_count = self.dev360.get_leftpane_unique_clients()
        sleep(5)
        if total_count:
            ret_val = total_count.text
        else:
            self.utils.print_info("Unable to get the widget data")

        return ret_val


    def device360_get_total_clients_clientspage(self, device_serial=""):
        """
        - This keyword gets the total clients from clients page in the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
         - ``Device360 Get Total Clients ClientsPage   ${DEVICE_SERIAL} ``
        :return: total number of clients displayed in the clients Device360 view
        """
        ret_val = ""

        self.utils.print_info("Navigate to Mange-->Devices")
        self.navigator.navigate_to_device360_with_client(device_serial)
        sleep(5)
        self.utils.print_info("Getting Device360 Total clients Count in clients page")
        sleep(5)
        total_count = self.dev360.get_device360_total_clients_clientspage()

        if total_count:
            ret_val = total_count.text
        else:
            self.utils.print_info("Unable to get the total clients count")

        return ret_val

    def device360_get_connected_clients_count(self):
        """
        - This keyword obtains the count of connected clients from Device360 view.
        - Keyword Usage
         - ``Device360 Get Connected clients count``
        :return: value of the device title in the Device360 view
        """
        ret_clientcount = ""
        clients_count= self.dev360.get_connected_clients_count()
        if clients_count:
            self.utils.print_info("Connected clients count ")
            ret_clientcount = clients_count.text
        else:
            self.utils.print_info("Unable to find the clients count")
        return ret_clientcount

    def d360_get_info(self, device_mac, get_d360, **kwargs):
        """
        - This keyword obtains information from device360 page by demand from $(GET_D360) Dictionary
        - Flow: Manage --> Devices --> click on(device serial hyperlink).
        - Keyword Usage:
        - ``${D360_INFO}    D360 GET INFO    ${DEVICE_MAC}    ${GET_D360}``

        :param device_mac: MAC of the device
        :param get_d360: (Dict) Info. request to get from Device 360 page
        :return: (Dict) Device 360 information if successfully else -1
        """
        monitor        = get_d360.get('monitor'       , 'None')
        unique_clients = get_d360.get('unique_clients', 'None')

        try:
            self.deviceCommon.go_to_device360_window(device_mac, device_mac)
            if unique_clients != 'None':
                self.utils.wait_till(self.dev360.get_connected_clients_count, timeout=12, delay=3, is_logging_enabled=True)
                get_d360['unique_clients'] = self.dev360.get_leftpane_unique_clients().text
                self.utils.print_info("Unique Clients:", get_d360['unique_clients'])

            if monitor != 'None':
                get_d360['monitor'] = self._get_d360_monitor(monitor)


            self.utils.print_info("Click on close Diaglog Window(x)")
            self.auto_actions.click_reference(self.dev360.get_close_dialog)

            kwargs['pass_msg'] = "Successfully able to get D360 Information."
            self.common_validation.passed(**kwargs)
            return get_d360

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Information: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_d360_monitor(self, get_monitor, **kwargs):
        """
        - This keyword obtains Monitor info page.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor

        :param get_monitor: (Dict) Info. request to get from Device 360 Monitor page
        :return: (Dict) Device 360 information monitor if successfully else -1
        """
        overview            = get_monitor.get('overview'           , 'None')
        system_information  = get_monitor.get('system_information' , 'None')
        wireless_interfaces = get_monitor.get('wireless_interfaces', 'None')
        clients             = get_monitor.get('clients'            , 'None')

        try:
            if overview != 'None':
                get_monitor['overview'] = self._get_d360_monitor_overview(overview)

            if system_information != 'None':
                get_monitor['system_information'] = self._get_d360_monitor_system_information(system_information)

            if wireless_interfaces != 'None':
                get_monitor['wireless_interfaces'] = self._get_d360_monitor_wireless_interfaces(wireless_interfaces)

            if clients != 'None':
                get_monitor['clients'] = self._get_d360_monitor_clients(clients)

            kwargs['pass_msg'] = "Successfully able to get D360 Monitor."
            self.common_validation.passed(**kwargs)
            return get_monitor

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_d360_monitor_overview(self, get_overview, **kwargs):
        """
        - This keyword obtains Overview page.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor -> OverView

        :param get_overview: (Dict) Info. request to get from Device 360 Overview page
        :return: (Dict) Device 360 information monitor overview if successfully else -1
        """
        connected_clients = get_overview.get('connected_clients', 'None')

        try:
            if connected_clients != 'None':
                self.utils.wait_till(self.dev360.get_connected_clients_count, timeout=20, delay=4, is_logging_enabled=True)
                get_overview['connected_clients'] = self.dev360.get_connected_clients_count().text
                self.utils.print_info("Connected clients: ", get_overview['connected_clients'])

            kwargs['pass_msg'] = "Successfully able to get D360 Monitor Overview."
            self.common_validation.passed(**kwargs)
            return get_overview

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor Overview: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_d360_monitor_system_information(self, get_system_info, **kwargs):
        """
        - This keyword obtains System Information page.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor -> System Information

        :param get_system_info: (Dict) Info. request to get from Device 360 System Information page
        :return: (Dict) Device 360 information monitor System Information if successfully else -1
        """
        host_name            = get_system_info.get('host_name'           , 'None')
        network_policy       = get_system_info.get('network_policy'      , 'None')
        ssid                 = get_system_info.get('ssid'                , 'None')
        device_model         = get_system_info.get('device_model'        , 'None')
        function             = get_system_info.get('function'            , 'None')
        device_template      = get_system_info.get('device_template'     , 'None')
        configuration_type   = get_system_info.get('configuration_type'  , 'None')
        serial_number        = get_system_info.get('serial_number'       , 'None')
        iq_engine            = get_system_info.get('iq_engine'           , 'None')
        device_status        = get_system_info.get('device_status'       , 'None')
        mgt0_ipv4_address    = get_system_info.get('mgt0_ipv4_address'   , 'None')
        mgt0_ipv6_address    = get_system_info.get('mgt0_ipv6_address'   , 'None')
        ipv4_subnet_mask     = get_system_info.get('ipv4_subnet_mask'    , 'None')
        ipv6_subnet_mask     = get_system_info.get('ipv6_subnet_mask', 'None')
        ipv4_default_gateway = get_system_info.get('ipv4_default_gateway', 'None')
        ipv6_default_gateway = get_system_info.get('ipv6_default_gateway', 'None')
        mgt0_mac_address     = get_system_info.get('mgt0_mac_address'    , 'None')
        dns                  = get_system_info.get('dns'                 , 'None')
        ntp                  = get_system_info.get('ntp'                 , 'None')

        try:
            self.utils.print_info("Clicking on System Information")
            self.auto_actions.click_reference(self.dev360.get_system_info_button)
            self.utils.wait_till(self.dev360.get_system_info_iq_engine, timeout=15, delay=3, is_logging_enabled=True)
            self.screen.save_screen_shot()

            self.utils.print_info("Getting System Information.")
            if host_name != 'None':
                get_system_info['host_name'] = self.dev360.get_system_info_device_host_name().text
                self.utils.print_info('Host Name: ', get_system_info['host_name'])

            if network_policy != 'None':
                get_system_info['network_policy'] = self.dev360.get_system_info_network_policy().text
                self.utils.print_info('Network Policy: ', get_system_info['network_policy'])

            if ssid != 'None':
                get_system_info['ssid'] = self.dev360.get_system_info_device_ssids().text
                self.utils.print_info('SSID: ', get_system_info['ssid'])

            if device_model != 'None':
                get_system_info['device_model'] = self.dev360.get_system_info_device_model().text
                self.utils.print_info('Devie Model: ', get_system_info['device_model'])

            if function != 'None':
                get_system_info['function'] = self.dev360.get_system_info_device_function().text
                self.utils.print_info('Function: ', get_system_info['function'])

            if device_template != 'None':
                get_system_info['device_template'] = self.dev360.get_system_info_device_template().text
                self.utils.print_info('Device Template: ', get_system_info['device_template'])

            if configuration_type != 'None':
                get_system_info['configuration_type'] = self.dev360.get_system_info_conf_type().text
                self.utils.print_info('Configuration Type: ', get_system_info['configuration_type'])

            if serial_number!= 'None':
                get_system_info['serial_number'] = self.dev360.get_system_info_serial_num().text
                self.utils.print_info('Serial Number: ', get_system_info['serial_number'])

            if iq_engine != 'None':
                get_system_info['iq_engine'] = self.dev360.get_system_info_iq_engine().text
                self.utils.print_info('IQ Engine: ', get_system_info['iq_engine'])

            if device_status != 'None':
                get_system_info['device_status'] = self.dev360.get_system_info_dev_status().text
                self.utils.print_info('Device Status: ', get_system_info['device_status'])

            if mgt0_ipv4_address != 'None':
                get_system_info['mgt0_ipv4_address'] = self.dev360.get_system_info_mgt0_ipv4().text
                self.utils.print_info('Mgt0 IPv4 Address: ', get_system_info['mgt0_ipv4_address'])

            if mgt0_ipv6_address != 'None':
                get_system_info['mgt0_ipv6_address'] = self.dev360.get_system_info_mgt0_ipv6().text
                self.utils.print_info('Mgt0 IPv6 Address: ', get_system_info['mgt0_ipv6_address'])

            if ipv4_subnet_mask != 'None':
                get_system_info['ipv4_subnet_mask'] = self.dev360.get_system_info_ipv4_subnet().text
                self.utils.print_info('IPv4 Subnet Mask: ', get_system_info['ipv4_subnet_mask'])

            if ipv6_subnet_mask != 'None':
                get_system_info['ipv6_subnet_mask'] = self.dev360.get_system_info_ipv6_subnet().text
                self.utils.print_info('IPv6 Subnet Mask: ', get_system_info['ipv6_subnet_mask'])

            if ipv4_default_gateway!= 'None':
                get_system_info['ipv4_default_gateway'] = self.dev360.get_system_info_ipv4_default().text
                self.utils.print_info('IPv4 Default Gateway: ', get_system_info['ipv4_default_gateway'])

            if ipv6_default_gateway!= 'None':
                get_system_info['ipv6_default_gateway'] = self.dev360.get_system_info_ipv6_default().text
                self.utils.print_info('IPv6 Default Gateway: ', get_system_info['ipv6_default_gateway'])

            if mgt0_mac_address != 'None':
                get_system_info['mgt0_mac_address'] = self.dev360.get_system_info_mgt0_mac().text
                self.utils.print_info('Mgt0 Mac Address: ', get_system_info['mgt0_mac_address'])

            if dns != 'None':
                get_system_info['dns'] = self.dev360.get_system_info_dns().text
                self.utils.print_info('DNS: ', get_system_info['dns'])

            if ntp != 'None':
                get_system_info['ntp'] = self.dev360.get_system_info_ntp().text
                self.utils.print_info('NTP: ', get_system_info['ntp'])

            kwargs['pass_msg'] = "Successfully able to get D360 Monitor System Information."
            self.common_validation.passed(**kwargs)
            return get_system_info

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor System Information: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_d360_monitor_wireless_interfaces(self, get_wireless_interfaces, **kwargs):
        """
        - This keyword obtains Wireless Interfaces page.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor -> Wireless Interfaces

        :param get_wireless_interfaces: (Dict) Info. request to get from Device 360 Wireless Interfaces page
        :return: (Dict) Device 360 information monitor Wireless Interfaces if successfully else -1
        """
        total_clients        = get_wireless_interfaces.get('total_clients'       , 'None')
        wifi_health_2ghz     = get_wireless_interfaces.get('wifi_health_2.4ghz'  , 'None')
        wifi_health_5ghz     = get_wireless_interfaces.get('wifi_health_5ghz'    , 'None')
        wifi_health_6ghz     = get_wireless_interfaces.get('wifi_health_6ghz'    , 'None')
        wifi_health_combined = get_wireless_interfaces.get('wifi_health_combined', 'None')
        wifi2                = get_wireless_interfaces.get('wifi2'               , 'None')

        try:
            self.utils.print_info("Clicking on Wireless Interface")
            self.auto_actions.click_reference(self.dev360.get_device360_wireless_interface_tab)

            if total_clients != 'None':
                self.utils.wait_till(self.dev360.get_device360_total_wireless_clients, timeout=12, delay=3, is_logging_enabled=True)
                get_wireless_interfaces['total_clients'] = self.dev360.get_device360_total_wireless_clients().text
                self.utils.print_info("Total Clients: ", get_wireless_interfaces['total_clients'])

            if wifi_health_2ghz != 'None':
                get_wireless_interfaces['wifi_health_2.4ghz'] = self._get_d360_monitor_wireless_interfaces_wifi_health('2ghz', wifi_health_2ghz)

            if wifi_health_5ghz != 'None':
                get_wireless_interfaces['wifi_health_5ghz'] = self._get_d360_monitor_wireless_interfaces_wifi_health('5ghz', wifi_health_5ghz)

            if wifi_health_6ghz != 'None':
                get_wireless_interfaces['wifi_health_6ghz'] = self._get_d360_monitor_wireless_interfaces_wifi_health('6ghz', wifi_health_6ghz)

            if wifi_health_combined != 'None':
                get_wireless_interfaces['wifi_health_combined'] = self._get_d360_monitor_wireless_interfaces_wifi_health('combined',  wifi_health_combined)

            if wifi2 != 'None':
                get_wireless_interfaces['wifi2'] = self._get_get_d360_monitor_wireless_interfaces_wifix('wifi2', wifi2)

            kwargs['pass_msg'] = "Successfully able to get D360 Monitor Wireless Interfaces."
            self.common_validation.passed(**kwargs)
            return get_wireless_interfaces

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor Wireless Interfaces: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_d360_monitor_clients(self, get_clients, **kwargs):
        """
        - This keyword obtains Clients page.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor -> Clients

        :param get_clients: (Dict) Info. request to get from Device 360 Clients page
        :return: (Dict) Device 360 information monitor Clients if successfully else -1
        """
        total_clients          = get_clients.get('total_clients'         , 'None')
        client_mac             = get_clients.get('client_mac'            , 'None')
        current_connect_status = get_clients.get('current_connect_status', 'None')

        try:
            self.utils.print_info("Click on Clients tab")
            self.auto_actions.click_reference(self.deviceConfig.get_go_to_clients)

            if total_clients != 'None':
                self.utils.wait_till(self.dev360.get_device_active_clients_grid, timeout=12, delay=3, is_logging_enabled=True)
                get_clients['total_clients'] = self.dev360.get_device360_total_clients_clientspage().text
                self.utils.print_info("Total Clients within selected time range: ", get_clients['total_clients'])

            if client_mac != 'None':
                self.utils.wait_till(self.dev360.get_device_active_clients_grid, timeout=12, delay=3, is_logging_enabled=True)
                table = self.dev360.get_device_active_clients_grid()
                rows = self.dev360.get_device_active_clients_grid_rows(table)
                self.utils.print_info("Getting the total number of rows: ", len(rows))
                self.screen.save_screen_shot()
                for row in rows:
                    self.utils.print_info("Getting the clients rows: ", row.text)
                    if client_mac in row.text and "CONNECTED" in row.text:
                        if current_connect_status != 'None':
                            get_clients['current_connect_status'] = "CONNECTED"
                            self.utils.print_info("Client current connect status: ", get_clients['current_connect_status'])
                        break

            kwargs['pass_msg'] = "Successfully able to get D360 Monitor Clients."
            self.common_validation.passed(**kwargs)
            return get_clients

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor Clients: {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_get_d360_monitor_wireless_interfaces_wifix(self, wifix, get_wifix, **kwargs):
        """
        - This keyword obtains WIFIx frame.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor -> WIFIx(frame)

        :param get_clients: (Dict) Info. request to get from Device 360 wireless interfaces WIFIx frame
        :return: (Dict) Device 360 information monitor wireless interfaces WIFIx if successfully else -1
        """
        my_clients = get_wifix.get('my_clients', 'None')

        try:
            self.utils.wait_till(self.dev360.get_device360_wireless_wifi2widgetclient, timeout=12, delay=3, is_logging_enabled=True)
            if wifix == 'wifi2':
                if my_clients != 'None':
                    self.utils.print_info("Getting Device360 Total Wireless Count")
                    get_wifix['my_clients'] = self.dev360.get_device360_wireless_wifi2widgetclient().text

            kwargs['pass_msg'] = f"Successfully able to get D360 Monitor Wireless Interface WIFIx: {wifix}"
            self.common_validation.passed(**kwargs)
            return get_wifix

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor Interface WIFIx: {wifix} : {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def _get_d360_monitor_wireless_interfaces_wifi_health(self, band, get_wifi_health, **kwargs):
        """
        - This keyword obtains WIFI HEALTH frame.
        - Flow: Manage -->Devices --> click on(device serial hyperlink) -> Monitor -> Wireless Interfaces -> WIFI HEALTH(frame)

        :param get_clients: (Dict) Info. request to get from Device 360 wireless interfaces WIFI HEALTH page
        :return: (Dict) Device 360 information monitor wireless interfaces WIFI HEALTH if successfully else -1
        """
        overall_score = get_wifi_health.get('overall_score', 'None')

        try:
            if   band == '2ghz':
                self.utils.print_info("Click on 2.4 GHz tab")
                self.auto_actions.click_reference(self.get_device360_wireless_wifi2gscoretab)
            elif band == '5ghz':
                self.utils.print_info("Click on 5 GHz tab")
                self.auto_actions.click_reference(self.get_device360_wireless_wifi5gscoretab)
            elif band == '6ghz':
                self.utils.print_info("Click on 6 GHz tab")
                self.auto_actions.click_reference(self.get_device360_wireless_wifi6gscoretab)
            elif band == 'combined':
                self.utils.print_info("Click on combined tab")
                self.auto_actions.click_reference(self.get_device360_wireless_combinedscoretab)

            if overall_score != 'None':
                self.utils.wait_till(self.dev360.get_device360_wireless_combinedscore, timeout=15, delay=5, is_logging_enabled=True)
                get_wifi_health['overall_score'] = self.dev360.get_device360_wireless_combinedscore().text
                self.utils.print_info("Overall Score Value: ", get_wifi_health['overall_score'])

            kwargs['pass_msg'] = f"Successfully able to get D360 Monitor Wireless Interface WIFI HEALTH: {band}"
            self.common_validation.passed(**kwargs)
            return get_wifi_health

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to get D360 Monitor WIFI HEALTH: {band} : {e}"
            self.common_validation.failed(**kwargs)
            return -1
