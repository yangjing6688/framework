import re
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.xiq.flows.manage.Location import *
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator
from selenium.webdriver.common.keys import Keys
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.Device360WebElements import Device360WebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
from extauto.xiq.flows.manage.DeviceConfig import DeviceConfig
from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.manage.Tools import Tools


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
        self.devices_web_elements = DevicesWebElements()
        self.wireless_web_elements = WirelessWebElements()
        self.device_template_web_elements = DeviceTemplateWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.common_validation = CommonValidation()
        self.tools = Tools()

    def get_system_info(self):
        """
        - This keyword gets system information from device360 page
        - Keyword Usage
         - ``Get System Info``

        :return: dictionary of system information
        """
        try:
            self.utils.print_info("Clicking on System Information")
            self.auto_actions.click(self.dev360.get_system_info_button())
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
            self.auto_actions.click(self.dev360.get_close_dialog())
            return sys_info
        except Exception as e:
            self.utils.print_info("Unable to get device360 details")
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
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sys_info = self.get_system_info()
                return sys_info
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sys_info = self.get_system_info()
                return sys_info

    def check_client_in_device360(self, device_serial=None, client_mac=None):
        """
           - This keyword is used to check the client in device360 page based on passed client mac address
           -Flow: Manage --> Devices --> click on the Clients hyperlink which is present in Device grid row based on device serial
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
#        totalrows = rows.len()
        self.utils.print_info("Getting the total number of rows: ", rows.len())
        self.screen.save_screen_shot()
        for row in rows:
            self.utils.print_info("Getting the clients rows: ", row.text)
            if client_mac in row.text and "CONNECTED" in row.text:
                self.utils.print_info("Client found")
                self.auto_actions.click(self.dev360.get_close_dialog())
                return 1
        self.utils.print_info("Client not found")
        self.auto_actions.click(self.dev360.get_close_dialog())
        return -1

    def get_status_interface_list(self, device_serial=None):
        """
           - This keyword  gets interfaces list
           -Flow: Manage --> Devices --> Select the device row based on the passed device serial --> Utilities --> Status --> Interface --> interface menu
           - Keyword Usage:
            - ``${RESULT}=        Get Status Interface         ${DEVICE_SERIAL}``

           :param device_serial: serial of the device
           :return: returns the list of interface names
           """
        if device_serial:
            self.navigator.navigate_to_status_interface(device_serial)
            sleep(5)
            self.auto_actions.click(self.dev360.get_utilities_status_interface_name_dropdown())
            sleep(2)
            options = self.dev360.get_utilities_status_interface_name_dropdown_opt()
            list_options = []
            for opt in options:
                if "All" not in opt.text:
                    list_options.append(opt.text)
            self.utils.print_info("Interfaces List: ", list_options)
            self.auto_actions.click(self.dev360.get_close_dialog())
            return list_options

    def get_status_interface(self, device_serial=None, interface_name=None):
        """
           - This keyword  gets status interface
           -Flow: Manage --> Devices --> Select the device row based on the passed device serial --> Utilities --> Status --> Interface --> select interface and get the output
           - Keyword Usage:
            - ``${RESULT}=        Get Status Interface         ${DEVICE_SERIAL}       ${INTERFACE}``

           :param device_serial: serial of the device
           :param interface_name: name of the interface
           :return: returns the output of the interface
           """
        if device_serial and interface_name:
            self.navigator.navigate_to_status_interface(device_serial)
            sleep(5)
            self.auto_actions.click(self.dev360.get_utilities_status_interface_name_dropdown())
            sleep(2)
            options = self.dev360.get_utilities_status_interface_name_dropdown_opt()
            for opt in options:
                if interface_name in opt.text:
                    self.auto_actions.click(opt)
                    sleep(5)
                    break

            content = self.dev360.get_utilities_status_interface_contents().text
            self.screen.save_screen_shot()
            self.auto_actions.click(self.dev360.get_close_dialog())
            return content
        else:
            self.utils.print_info("Device serial and interface name are not provided")
            return -1

    def device360_configure_device_vlan_for_port(self, vlan=1363):
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
        self.utils.print_info("Configuring new vlan values %s in port 1"%(vlan))
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
            self.auto_actions.click(self.get_close_dialog())
            ret_val = 1
        else:
            self.utils.print_info("couldn't close the dialogue box")
            ret_val = -1
        sleep(2)

        return  ret_val

    def device360_enable_ssh_cli_connectivity(self, device_mac='', device_name='', run_time=5, time_interval=30, retry_time=150, **kwargs):
        """
        - This keyword enables SSH CLI Connectivity
        - Flow : Manage-->Devices-->click on hyperlink(MAC/hostname)
        - Keyword Usage
         - ``Get Device360 Enable SSH CLI Connectivity  device_mac=${AP1_MAC}    run_time=5``
         - ``Get Device360 Enable SSH CLI Connectivity  device_name=${AP1_NAME}  run_time=10``

        :return: SSH String
        """
        if device_mac:
            self.utils.print_info("Using device MAC: ", device_mac.upper())
            self.navigator.navigate_to_device360_page_with_mac(device_mac.upper())

        if device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click(self.get_device360_configure_button())

        self.utils.print_info("Clicking Device 360 SSH CLI tab")
        self.auto_actions.click(self.get_device360_configure_ssh_cli_tab())
        sleep(3)

        self.utils.print_info("Clicking Device 360 SSH CLI Run Time: ", run_time)
        if run_time == 5:
            self.auto_actions.click(self.get_device360_configure_ssh_cli_5min_radio())

        elif run_time == 30:
            self.auto_actions.click(self.get_device360_configure_ssh_cli_30min_radio())

        elif run_time == 60:
            self.auto_actions.click(self.get_device360_configure_ssh_cli_60min_radio())

        elif run_time == 120:
            self.auto_actions.click(self.get_device360_configure_ssh_cli_120min_radio())

        elif run_time == 240:
            self.auto_actions.click(self.get_device360_configure_ssh_cli_240min_radio())
        else:
            kwargs['fail_msg'] = f"Unsupported run_time: {run_time} supported numbers are: 5, 30, 60, 120, 240"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1

        sleep(5)
        self.utils.print_info("Clicking Device 360 SSH CLI Enable SSH button...")
        self.auto_actions.click(self.get_device360_configure_ssh_cli_enable_button())
        self.screen.save_screen_shot()

        retry_count = 0
        while retry_count <= retry_time:
            self.utils.print_info(f"Checking SSH IP and Port Details after: {retry_count} seconds")
            ip = self.get_device360_configure_ssh_cli_ip()
            port = self.get_device360_configure_ssh_cli_port()
            self.screen.save_screen_shot()

            if ip and port:
                ip_port_info = dict()
                ip_port_info["ip"] = ip
                ip_port_info["port"] = port

                self.utils.print_info(f"****************** IP/Port Information ************************")
                for key, value in ip_port_info.items():
                    self.utils.print_info(f"{key}:{value}")
                kwargs['pass_msg'] = f"Got the SSH and port information: {ip}:{port}"
                self.common_validation.validate(1, 1, **kwargs)
                return ip_port_info
            else:
                self.utils.print_info(f"****************** IP/Port Information is not available after {retry_count} seconds ************************")
                sleep(time_interval)
                retry_count += 30
        kwargs['fail_msg'] = f"Failed to get the SSH and port information"
        self.common_validation.validate(-1, 1, **kwargs)
        return -1

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

        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click(self.get_device360_configure_button())
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH WEB tab")
        self.auto_actions.click(self.get_device360_configure_ssh_web_tab())
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH WEB Run Time: ", run_time)

        sleep(5)

        if run_time == 5:
            self.auto_actions.click(self.get_device360_configure_ssh_web_5min_radio())

        if run_time == 30:
            self.auto_actions.click(self.get_device360_configure_ssh_web_30min_radio())

        if run_time == 60:
            self.auto_actions.click(self.get_device360_configure_ssh_web_60min_radio())

        if run_time == 120:
            self.auto_actions.click(self.get_device360_configure_ssh_web_120min_radio())

        if run_time == 240:
            self.auto_actions.click(self.get_device360_configure_ssh_web_240min_radio())

        self.screen.save_screen_shot()

        sleep(5)
        self.utils.print_info("Clicking Device 360 SSH WEB Enable SSH button...")
        self.auto_actions.click(self.get_device360_configure_ssh_web_enable_button())

        sleep(60)

        url = self.get_device360_configure_ssh_web_url()

        self.utils.print_info("Device 360 SSH WEB URL: ", url)

        return url

    def device360_is_ssh_enabled(self, device_mac='', device_name=''):
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
        self.auto_actions.click(self.get_device360_configure_button())
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH tab")
        self.auto_actions.click(self.get_device360_configure_ssh_cli_tab())
        self.screen.save_screen_shot()

        self.utils.print_info("Check if enabled based on first radio button")
        if self.get_device360_configure_ssh_cli_5min_radio().is_enabled():
            return 1

        return -1

    def device360_is_ssh_disabled(self, device_mac='', device_name=''):
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
        self.auto_actions.click(self.get_device360_configure_button())
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Device 360 SSH tab")
        self.auto_actions.click(self.get_device360_configure_ssh_cli_tab())
        self.screen.save_screen_shot()

        self.utils.print_info("Check if disabled based on first radio button")
        if self.get_device360_configure_ssh_cli_5min_radio().is_enabled():
            return -1

        return 1

    def get_switch_information(self):
        """
        - This keyword gets Switch information from device360 page
        - It Assumes That Already Navigated to Device360 Page
        - Flow : Device 360 Page
        - Keyword Usage
         - ``Get ExOS Information``

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

        self.utils.print_info(f"******************ExOS Device360 Information************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        self.utils.print_info("Closing device360 Dialogue Window.")
        self.auto_actions.click(self.dev360.get_close_dialog())
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
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)
                self.screen.save_screen_shot()
                exos_info = self.get_switch_information()
                return exos_info

        if device_name:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)
                self.screen.save_screen_shot()
                exos_info = self.get_switch_information()
                return exos_info

    def advance_channel_selection(self, device_serial=None):
        """
            - This keyword  gets advance channel selection details
            -Flow: Manage --> Devices --> Select the device row based on the passed device serial -->Utilities --> Status --> Advanced Channel Selection
            - Keyword Usage:
             - ``${RESULT}=        Advance Channel Selection         ${DEVICE_SERIAL} ``

            :param device_serial: serial of the device
            :return: returns the output of the advance channel selection
            """
        if device_serial:
            self.navigator.navigate_to_advance_channel_selection(device_serial)
            content = self.dev360.get_utilities_status_adv_channel_sel_contents().text
            self.screen.save_screen_shot()
            self.auto_actions.click(self.dev360.get_close_dialog())
            return content
        else:
            self.utils.print_info("Device serial is not provided")
            return -1

    def wifi_status_summary(self, device_serial=None):
        """
            - This keyword  gets wifi status summary
            -Flow: Manage --> Devices -->Select the device row based on the passed device serial --> Click on Utilities --> Status --> Wifi Status Summary --> station
            - Keyword Usage:
             - ``${RESULT}=        Wifi Status Summary         ${DEVICE_SERIAL}  ``

            :param device_serial: serial of the device
            :return: returns the output of the wifi status summary
            """
        if device_serial:
            self.navigator.navigate_to_wifi_status_summary(device_serial)
            sleep(5)
            self.utils.print_info("Clicking on Station..")
            self.auto_actions.click(self.dev360.get_utilities_status_wifi_summary_station_btn())
            sleep(2)

            self.screen.save_screen_shot()
            self.utils.print_info("Getting the contents..")
            content = self.dev360.get_utilities_status_wifi_summary_station_content().text
            self.utils.print_info("Content: ", content)
            self.utils.print_info("Clicking on close dialog")
            self.auto_actions.click(self.dev360.get_close_dialog())
            return content
        else:
            self.utils.print_info("Device serial is not provided.")
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

        self.utils.print_info(f"******************VOSS Device360 Overview Information************************")
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
        device360_info["snmp_location"] = self.dev360.get_device360_configure_device_snmp_location().get_attribute('value')
        device360_info["network_policy"] = self.dev360.get_device360_configure_device_network_policy().text
        device360_info["device_template"] = self.dev360.get_device360_configure_device_device_template().text

        self.utils.print_info(f"******************VOSS Device360 Device Configuration Information************************")
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
            self.utils.print_info("Unable to get VOSS overview information - please specify a device MAC or device name")

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

                self.auto_actions.click(self.get_device360_configure_button())
                sleep(8)

                self.utils.print_info("Clicking Device Configuration on the Device360 Configure tab")
                self.auto_actions.click(self.get_device360_device_configuration_button())
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

                self.auto_actions.click(self.get_device360_configure_button())
                sleep(8)

                self.utils.print_info("Clicking Device Configuration on the Device360 Configure tab")
                self.auto_actions.click(self.get_device360_device_configuration_button())
                sleep(3)
                voss_info = self.get_voss_device_configuration_information()
                self.device360_device_configuration_click_cancel()
                self.close_device360_window()

        else:
            self.utils.print_info(
                "Unable to get VOSS device configuration information - please specify a device MAC or device name")

        return voss_info

    def select_configure_tab(self):
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
            return 1
        else:
            self.utils.print_info("Could not find Configure tab - make sure Device360 window is open")
            self.screen.save_screen_shot()
            return -1

    def select_device_configuration_view(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Device Configuration link - make sure Device360 window is open and on Configure tab")
            self.screen.save_screen_shot()
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

    def device360_device_configuration_click_cancel(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Cancel button - make sure Device360 window is open to the Device Configuration view")
            self.screen.save_screen_shot()
            return -1

    def close_device360_window(self):
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
            self.auto_actions.click(self.dev360.get_close_dialog())
            return 1
        else:
            self.utils.print_info("Could not obtain Device360 close button - make sure Device360 window is open")
            self.screen.save_screen_shot()
            return -1

    def device360_disable_ssh_connectivity(self, device_mac='', device_name=''):
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

        if device_name:
            self.utils.print_info("Using device name: ", device_name)
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Clicking Device 360 Configure button")
        self.auto_actions.click(self.get_device360_configure_button())

        self.utils.print_info("Clicking Device 360 SSH CLI tab")
        self.auto_actions.click(self.get_device360_configure_ssh_cli_tab())
        sleep(3)

        self.utils.print_info("Clicking Device 360 SSH Disable SSH button...")
        disable_ssh_btn = self.get_device360_configure_ssh_disable_button()
        if disable_ssh_btn:
            self.auto_actions.click(disable_ssh_btn)
        else:
            self.utils.print_info("Disable SSH button not present - SSH may already be disabled")

        return 1

    def device360_disable_ssh_web_connectivity(self, device_mac='', device_name=''):
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
            self.auto_actions.click(self.get_device360_configure_ssh_web_disable_button())
            sleep(5)
            self.screen.save_screen_shot()

            if self.get_device360_configure_ssh_web_url():
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
            self.auto_actions.click(self.get_device360_configure_button())

            self.utils.print_info("Clicking Device 360 SSH WEB tab")
            self.auto_actions.click(self.get_device360_configure_ssh_web_tab())

            sleep(5)

            self.utils.print_info("Clicking Device 360 SSH CLI Disable SSH button...")
            self.auto_actions.click(self.get_device360_configure_ssh_web_disable_button())

            if self.get_device360_configure_ssh_web_url():
                return -1
            return 1

    def device360_confirm_ssh_enabled(self, device_mac='', device_name=''):
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
        self.auto_actions.click(self.get_device360_configure_button())

        self.utils.print_info("Clicking Device 360 SSH CLI tab")
        self.auto_actions.click(self.get_device360_configure_ssh_cli_tab())
        sleep(3)

        disable_ssh_btn = self.get_device360_configure_ssh_disable_button()
        if disable_ssh_btn is None or disable_ssh_btn.get_attribute('visible') is False:
            self.utils.print_info("Disable button is not present - SSH is not enabled")
            ret_val = -1
        else:
            self.utils.print_info("Disable button is present - SSH is enabled")
            ret_val = 1

        return ret_val

    def device360_select_events_view(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Events link - make sure Device360 window is open and on Monitor tab")
            return -1

    def device360_select_alarms_view(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Alarms link - make sure Device360 window is open and on Monitor tab")
            return -1

    def device360_confirm_event_description_contains(self, event_str, after_time=None):
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
                                self.utils.print_debug("Found a match for '" + event_str + ''" after "'' + after_time + "'")
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

        return ret_val

    def device360_confirm_alarm_category_exists(self, alarm_cat, after_time=None):
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
                                self.utils.print_debug("Found a match for '" + alarm_cat + ''" after "'' + after_time + "'")
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
        return ret_val

    def select_port_configuration_view(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Port Configuration link - make sure Device360 window is open and on Configure tab")
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

    def device360_confirm_port_enabled(self, port_name):
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

        return ret_val

    def device360_confirm_port_disabled(self, port_name):
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

    def device360_get_port_row(self, port_name):
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
        return ret_val

    def device360_refresh_page(self):
        """
        - Refreshes the Device 360 window by clicking the refresh page button.

        :return: 1 if page was refreshed, -1 if not
        """
        ret_val = -1
        refresh_btn = self.get_device360_refresh_page_button()
        if refresh_btn:
            self.utils.print_info("Clicking Refresh Page button")
            self.auto_actions.click(refresh_btn)
            sleep(5)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Refresh Page button")

        return ret_val

    def select_monitor_tab(self):
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
            return 1
        else:
            self.utils.print_info("Could not find Monitor tab - make sure Device360 window is open")
            return -1

    def select_monitor_overview(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Overview button - make sure Device360 window is open and on Monitor tab")
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

    def select_switch_system_information(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find System Information button - make sure Device360 window is open for a switch")
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

    def select_monitor_clients(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Clients button - make sure Device360 window is open and on Monitor tab")
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

    def select_monitor_diagnostics(self):
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
            return 1
        else:
            self.utils.print_info(
                "Could not find Diagnostics button - make sure Device360 window is open and on Monitor tab")
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

    def confirm_device360_monitor_overview_chart_displayed(self):
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
                self.utils.print_info("Monitor> Overview chart is displayed")
                return 1
            else:
                self.utils.print_info("Monitor> Overview chart is not displayed")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("Could not find chart for Monitor> Overview page")
            self.screen.save_screen_shot()
            return -1

    def confirm_device360_monitor_clients_chart_displayed(self):
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
                self.utils.print_info("Monitor> Clients chart is displayed")
                return 1
            else:
                self.utils.print_info("Monitor> Clients chart is not displayed")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("Could not find chart for Monitor> Clients page")
            self.screen.save_screen_shot()
            return -1

    def confirm_device360_monitor_diagnostics_chart_displayed(self):
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
                self.utils.print_info("Monitor> Diagnostics chart is displayed")
                return 1
            else:
                self.utils.print_info("Monitor> Diagnostics chart is not displayed")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("Could not find chart for Monitor> Diagnostics page")
            self.screen.save_screen_shot()
            return -1

    def device360_select_time_range(self, time_range):
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

        return ret_val

    def confirm_device360_time_range_selected(self, time_range):
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
                self.utils.print_info(f"Current time range selection is '{time_range_sel}'")
                return 1
            else:
                self.utils.print_info(f"Current time range selection is '{time_range_sel}', not the expected '{time_range}'")
                return -1
        else:
            self.utils.print_info("Could not determine current time range selection")
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

    def device360_select_day_time_range_hours_button(self, hours_value):
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

    def device360_select_week_time_range_days_button(self, days_value):
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

    def device360_select_month_time_range_days_button(self, days_value):
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

    def device360_port_diagnostics_select_all_ports(self):
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

        return ret_val

    def device360_port_diagnostics_deselect_all_ports(self):
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

    def confirm_device360_port_diagnostics_all_ports_selected(self):
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
            return 1
        else:
            self.utils.print_info(f"{port_count} ports are not selected")
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                self.utils.print_info(f"-- deselected port: data jack index '{data_jack_index}'")
            return -1

    def confirm_device360_port_diagnostics_all_ports_deselected(self):
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
            return 1
        else:
            self.utils.print_info(f"{port_count} ports are selected")
            for port in port_list:
                data_jack_index = port.get_attribute("data-jack-index")
                self.utils.print_info(f"-- selected port: data jack index '{data_jack_index}'")
            return -1

    def confirm_device360_port_diagnostics_port_selected(self, port_num):
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
            self.utils.print_info(f"Port {port_num} is not selected")
            self.screen.save_screen_shot()

        return ret_val

    def confirm_device360_port_diagnostics_port_deselected(self, port_num):
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
            self.utils.print_info(f"Port {port_num} is not deselected")
            self.screen.save_screen_shot()

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

        self.utils.print_info(f"****************** Device360 Overview Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        return device360_info

    def device360_set_device_function(self, value="AP"):
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
                self.utils.print_info("Could not find Device Function selector")
                ret_val = -1
        else:
            self.utils.print_info("Unable to navigate to the Device Configuration view")
            ret_val = -1

        return ret_val

    def device360_save_device_configuration(self):
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

        self.utils.print_info(f"****************** Device360 Left Side Bar Information ************************")
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

        self.utils.print_info(f"****************** Device360 Left Side Bar Active Since Information ************************")
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
        power_el = self.dev360.get_topbar_power()
        fan_el = self.dev360.get_topbar_fan()
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

        self.utils.print_info(f"****************** Device360 Top Bar Information ************************")
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

    def device360_check_events_is_in_order(self):
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
                        return -1
        self.utils.print_debug("The severity are in order")
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

        self.utils.print_info(f"****************** Device360 Switch System Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}: {value}")

        return device360_info

    def click_hyperlink_on_system_information(self, device_mac=None, device_name=None, Clickon=None):
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
        self.auto_actions.click(self.dev360.get_system_info_button())
        sleep(2)

        try:
            if Clickon == "Template":
                self.auto_actions.click(self.dev360.
                                        get_hyper_link_system_information(self.dev360.get_system_info_device_template()))
                sleep(5)
                text = self.device_template_web_elements.get_ap_template_text().get_attribute("value")
                return text

            elif Clickon == "SSID":
                self.auto_actions.click(self.dev360.
                                        get_hyper_link_system_information(self.get_system_info_device_ssids()))
                sleep(2)
                text = self.wireless_web_elements.get_wireless_ssid_field().get_attribute("value")
                return text

        except Exception as e:
            self.utils.print_info("Unable to Click HyperLink on System Information")
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
        # self.auto_actions.click(self.get_device360_configure_device_snmp_location())

        return snmp_locn

    def device360_device_configuration_select_template(self, device_mac, sw_template_name):
        """
        This function select the template into d360 and start update process

        :param device_mac: Mac of device
        :param sw_template_name: Policy template
        :return: 1 if update is completed ; -1 else
        """

        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
            self.utils.print_info("D360 page was not opened ")
            return -1
        else:
            self.utils.print_info("D360 page was opened ")

        if self.devices_web_elements.get_ap_configure_button():
            self.utils.print_info("Clicking on 'Configure' button  ")
            self.auto_actions.click(self.devices_web_elements.get_ap_configure_button())
        else:
            self.utils.print_info("'Configure' button was not found ")
            return -1

        if self.dev360.get_device360_device_configuration_button():
            self.auto_actions.click(self.dev360.get_device360_device_configuration_button())
            self.utils.print_info("Clicking on 'Device Configuration 'button")
        else:
            self.utils.print_info("'Device Configuration 'button was not found ")
            return -1

        # Select from dropdown
        if sw_template_name is not None:
            click_dropdown = self.dev360.get_device360_device_configuration_stack_template_button()
            if click_dropdown:
                self.utils.print_info(f" Click on dropdown ")
                self.auto_actions.click(click_dropdown)
                sleep(3)
            else:
                self.utils.print_info(f" Not able to find dropdown  ")
            dropdown_items = self.dev360.get_device360_device_configuration_stack_template_items()
            if dropdown_items:
                self.utils.print_info(f" The templates from dropdown are: ")
                for elem in dropdown_items:
                    self.utils.print_info(elem.text)
                for el in dropdown_items:
                    if sw_template_name in el.text:
                        self.utils.print_info(f" Select {el.text} from dropdown")
                        self.auto_actions.select_drop_down_options(dropdown_items, el.text)
                        sleep(3)
                    else:
                        self.utils.print_info(f" The template name was not found in dropdown")
            else:
                self.utils.print_info(f" Not able to find dropdown items ")
        else:
            self.utils.print_info(f" The sw_template_name is None  ")

        # Press Save button
        self.screen.save_screen_shot()
        sleep(5)
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        if self.dev360.get_device360_device_configuration_save_button():
            self.utils.print_info("Click on save button")
            self.auto_actions.click(self.dev360.get_device360_device_configuration_save_button())
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
            self.auto_actions.click(self.dev360.get_device360_device_configuration_update_button())

        else:
            self.utils.print_info("The update button was not found")

        if self.devices_web_elements.get_devices_perform_update_button_d360():
            self.utils.print_info("Click on update performe button")
            self.auto_actions.click(self.devices_web_elements.get_devices_perform_update_button_d360())

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
            self.auto_actions.click(self.dev360.get_device360_device_configuration_exit_button())
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

    def device360_search_event_and_confirm_event_description_contains(self, event_str, after_time=None):
        """
        - This keyword search event and then confirms that specified event text is present in the description field of the event, after the
          specified time. If no time is specified, it just confirms the event is present.
          It assumes the Device360 Window is open and on the Monitor> Events tab.
          After search is done it confirms that the log is present only on first page of event list. If more logs are matching it returns the number of them
        - Keyword Usage:
         - ``Device360 Search Event And Confirm Event Description Contains  ${EVENT}  ${AFTER_TIME}``
         - ``Device360 Search Event And Confirm Event Description Contains  ${EVENT}``
        :param  event_str:      String to look for in the event description
        :param  after_time:     Indicates at which point in time to start searching for the existence of the event
                                (if not specified, it just checks for the existence of the event in general)
        :return: 1 if only one log (row in table) is found; If more logs (rows) are found it will be return the number of them; else -1
        """
        i = 0
        cont_rows_match = 0
        self.d360Event_search(event_str)
        events_table = self.dev360.get_device360_events_grid()
        if events_table:
            event_rows = self.dev360.get_device360_events_grid_rows(events_table)
            if event_rows:
                for row in event_rows:
                    self.utils.print_info(str(i))
                    i += 1
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
                    return -1
                else:
                    self.utils.print_info("Found a match for '" + event_str + "' on " + str(cont_rows_match) + " rows")
                    return cont_rows_match
            else:
                self.utils.print_info("Events table does not contain any rows")
        else:
            self.utils.print_info(
                "Could not find Events table - make sure Device360 window is open to the Monitor> Alarms view")
        return -1

    def d360Event_search(self, search_value):
        """
        This keyword inserts info into event search text box. No button for search is present, the search will be done
        automatically after the text was inserted
        :param search_value:
        :return: 1 if the text was entered into search box and -1 if search text box was not found
        """
        search_box = self.dev360.get_d360Event_search_textbox()
        if search_box:
            self.utils.print_info("Entering info to search : ", search_value)
            self.auto_actions.send_keys(self.dev360.get_d360Event_search_textbox(), search_value)
            sleep(10)
            return 1
        else:
            self.utils.print_info("Unable to find search text box")
            return -1

    def device360_revert_port_configuration(self, select_column, port_name):
        """
        This keyword press the revert button for the specific row and column into device360 Port Configuration window
        select_column : - Port Details : 'port state' , 'port usage' , 'vlan' , 'description'
                        - Port Settings & Aggregation: 'transmission' , 'speed' , 'flow' , 'transmit' , 'receive' , 'cdp' , 'client reporting'
                        - STP: 'stp status' , 'edge port' , 'bpdu protection' , 'priority' , 'path cost'
                        - Storm Control: 'broadcast' , 'unknown unicast' , 'multicast' , 'value'
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
                return -1
        # Port Settings & Aggregation
        if select_column in ['transmission', 'speed', 'flow', 'transmit', 'receive', 'cdp', 'client reporting']:
            button_settings = self.dev360.get_d360_configure_port_settings_aggregation_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Port Settings & Aggregation' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_port_settings_aggregation_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
                return -1
        # STP
        if select_column in ['stp status', 'edge port', 'bpdu protection', 'priority', 'path cost']:
            button_settings = self.get_d360_configure_port_stp_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'STP' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_stp_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
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
                return -1
        if rows:
            port_row = self.device360_get_row_specified_port_name(rows, port_name)
        else:
            self.utils.print_info("Port rows are not displayed. Check the tab")
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
                    self.screen.save_screen_shot()
                    sleep(10)
                    return 1
                else:
                    self.utils.print_info("Could not click Revert button")
                    self.screen.save_screen_shot()
                # Click the 'Save Port Configuration' button
                save_btn = self.get_device360_configure_port_save_button()
                self.utils.print_info("rularea a trecut pe aici ")  # sters
                if save_btn:
                    self.utils.print_info("Clicking 'Save Port Configuration' button'")
                    self.auto_actions.click(save_btn)
                    return 1
            else:
                self.utils.print_info("The override revert button was not found  ")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Could not find the port row for port ", port_name)
            self.screen.save_screen_shot()
        return -1

    def device360_get_row_specified_port_name(self, rows, port_name):
        """
        - Get the port row object matching the specified port_name

        :param port_name: name of the port to return the row for
        :return: row element if row exists else return None
        """
        ret_val = None
        self.utils.print_info("Getting the Port rows from the Device360 Settings and Aggregation page")
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
        else:
            for row in rows:
                if port_name in row.text:
                    ret_val = row
                    break
        return ret_val

    def device360_click_on_checkbox_or_button_port_configuration(self, select_column, port_name):
        """
        This keyword click on checkbox for the specific row and column into device360 Port Configuration window
        select_column : - Port Details : 'port state'
                        - Port Settings & Aggregation: 'transmit' , 'receive' , 'cdp' , 'client reporting'
                        - STP: 'stp status' , 'edge port'
                        - Storm Control: 'broadcast' , 'unknown unicast' , 'multicast'
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
                self.utils.print_info("Cannot click on tab button")
                return -1
        # Port Settings & Aggregation
        if select_column in ['transmit', 'receive', 'cdp', 'client reporting']:
            button_settings = self.dev360.get_d360_configure_port_settings_aggregation_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Port Settings & Aggregation' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_port_settings_aggregation_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
                return -1
        # STP
        if select_column in ['stp status', 'edge port']:
            button_settings = self.get_d360_configure_port_stp_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'STP' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_stp_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
                return -1
        # Storm Control
        if select_column in ['broadcast', 'unknown unicast', 'multicast']:
            button_settings = self.get_d360_configure_port_storm_control_tab_button()
            if button_settings:
                self.utils.print_info("Clicking 'Storm Control' button")
                self.auto_actions.click(button_settings)
                rows = self.get_device360_configure_storm_control_rows()
            else:
                self.utils.print_info("Cannot click on tab button")
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
            self.screen.save_screen_shot()
        return -1

    def device360_port_configuration_click_save_button(self):
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
        return ret_val

    def device360_click_open_site_engine_link(self):
        """
        - This keyword clicks on the OPEN SITE ENGINE link
        - It is assumed that the Device360 window is open and the Overview panel is selected.
        - Keyword Usage
         - ``Device360 Click Open Site Engine Link``
        :return: 1 if action was successful (or the field is disabled), else -1
        """
        ret_val = -1

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
        else:
            self.utils.print_info("Could not find the 'Open Site Engine' link.")

        return ret_val

    def get_switch_device360_port_table_information(self, device_mac="", device_name="", port_number=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        if view_log := self.get_d360_switch_port_view_all_pages_button():
            if view_log.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click(self.get_d360_switch_port_view_all_pages_button())
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
                    switch_device360_info["lldp_neighbor"] = self.dev360.get_device360_switch_port_table_lacp_neighbor(row).text
                    switch_device360_info["lacp_status"] = self.dev360.get_device360_switch_port_table_lacp_status(row).text
                    switch_device360_info["port_status"] = self.dev360.get_device360_switch_port_table_port_status(row).text
                    switch_device360_info["trasmission_mode"] = self.dev360.get_device360_switch_port_table_transmission_mode(row).text
                    switch_device360_info["port_mode"] = self.dev360.get_device360_switch_port_table_port_mode(row).text
                    switch_device360_info["access_vlan"] = self.dev360.get_device360_switch_port_table_access_vlan(row).text
                    if self.dev360.get_device360_switch_port_table_tagged_vlans(row):
                        switch_device360_info["tagged_vlans"] = self.dev360.get_device360_switch_port_table_tagged_vlans(row).text
                    switch_device360_info["traffic_received"] = self.dev360.get_device360_switch_port_table_traffic_received(row).text
                    switch_device360_info["traffic_transmitted"] = self.dev360.get_device360_switch_port_table_traffic_transmitted(row).text
                    switch_device360_info["power_used"] = self.dev360.get_device360_switch_port_table_power_used(row).text
                    switch_device360_info["port_speed"] = self.dev360.get_device360_switch_port_table_port_speed(row).text

                    self.utils.print_info(f"****************** Switch Port Table Information ************************")
                    for key, value in switch_device360_info.items():
                        self.utils.print_info(f"{key}:{value}")

                    self.screen.save_screen_shot()
                    self.auto_actions.click(self.dev360.get_close_dialog())
                    self.screen.save_screen_shot()
                    return switch_device360_info
        except Exception as e:
            self.utils.print_info("Unable to get Port Table Information")
            self.screen.save_screen_shot()
            self.auto_actions.click(self.dev360.get_close_dialog())
            self.screen.save_screen_shot()
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

    def compare_transmission_mode(self, port_index, port_state, port_duplex_cli):
        """
        This keyword compares the status for transmission mode between XIQ and CLI
        :param port_index: a string of a port or a list of ports
        :param port_state: a string or a list which contains the status UP/DOWN of ports. If an element of list is '', it will be ignored
        :param port_duplex_cli: the "OPERATE DUPLEX" status from CLI
        -Keyword Usage:
            compare_transmision_mode     1/7  up  full
            compare_transmision_mode     2/4  up  full
            compare_transmision_mode     ${PORTS_INDEX}   ${OPERATE_STATE_UP}   ${OPERATE_DUPLEX}
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
                        self.utils.print_info("Port {} is {} interface number on XIQ".format(port_index[cnt], first[2:]))
                        result_from_menu = self.transmission_mode_right_click_menu(first[2:])
                        if result_from_menu != -1:
                            self.utils.print_info("Interface transmission mode result from right click menu : {}".format(result_from_menu))
                        else:
                            self.utils.print_info("result was not found in right click menu")
                            sleep(5)
                        result_from_table = self.transmission_mode_overview_table(first)
                        if result_from_table != -1:
                            self.utils.print_info("Interface transmission mode result from table for port {} is  {}".format(first, result_from_table))
                        else:
                            self.utils.print_info("Result was not found in table ")
                        result_CLI = port_duplex_cli[cnt]
                        self.utils.print_info("Operate Duplex CLI: {}".format(result_CLI))
                        if result_from_menu == result_from_table and result_CLI.upper() in result_from_menu.upper():
                            self.utils.print_info("All transmission status are the same for port ", first)
                        else:
                            self.utils.print_info("Transmission status are not the same for port ", first)
                            return -1
                        sleep(5)
                    else:
                        if self.transmission_mode_right_click_menu(first) != -1:
                            result_from_menu = self.transmission_mode_right_click_menu(first)
                            self.utils.print_info("Interface transmission mode result from right click menu for port {} is  : {}".format(first, result_from_menu))
                        else:
                            self.utils.print_info("result was not found in right click menu ")
                            sleep(5)
                            if self.transmission_mode_overview_table(first) != -1:
                                result_from_table = self.transmission_mode_overview_table(first)
                                self.utils.print_info("Interface transmission mode result from table: {}".format(result_from_table))
                            else:
                                self.utils.print_info("result was not found in table ")
                            result_CLI = port_duplex_cli[cnt]
                            self.utils.print_info("Operate Duplex CLI: {}".format(result_CLI))
                            if result_from_menu == result_from_table and result_CLI.upper() in result_from_menu.upper():
                                self.utils.print_info("All transmission status are the same for port ", first)
                            else:
                                self.utils.print_info("Transmission status are not the same for port ", first)
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
                        self.utils.print_info("Interface transmission mode result from right click menu for port {} is  : {}".format(port_index, result_from_menu))
                    else:
                        self.utils.print_info("result was not found in right click menu for port {}".format(port_index))
                    sleep(5)
                    result_from_table = self.transmission_mode_overview_table(port_index)
                    if result_from_table != -1:
                        self.utils.print_info("Interface transmission mode result from table for port {} is  {}".format(port_index, result_from_table))
                    else:
                        self.utils.print_info("result was not found in right click menu for port {}".format(port_index))
                    result_CLI = port_duplex_cli
                    self.utils.print_info("Operate Duplex CLI: {}".format(result_CLI))
                    if result_from_menu == result_from_table and result_CLI.upper() in result_from_menu.upper():
                        self.utils.print_info("All transmission status are the same for port ", port_index)
                    else:
                        self.utils.print_info("Transmission status are not the same for port ", port_index)
                        return -1
                    sleep(5)
                else:
                    result_from_menu = self.transmission_mode_right_click_menu(port_index)
                    if result_from_menu != -1:
                        self.utils.print_info("Interface transmission mode result from right click menu for port {} is  : {}".format(port_index, result_from_menu))
                    else:
                        self.utils.print_info("Result was not found in right click menu for port {}".format(port_index))
                    sleep(5)
                    result_from_table = self.transmission_mode_overview_table(port_index)
                    if result_from_table != -1:
                        self.utils.print_info("Interface transmission mode result from table for port {} is  {}".format(port_index, result_from_table))
                    else:
                        self.utils.print_info("result was not found in right click menu for port {}".format(port_index))
                        self.utils.print_info("Operate Duplex CLI: {}".format(port_duplex_cli))
                    if result_from_menu == result_from_table and port_duplex_cli.upper() in result_from_menu.upper():
                        self.utils.print_info("All transmission status are the same for port ", port_index)
                    else:
                        self.utils.print_info("Transmission status are not the same for port ", port_index)
                        return -1
                    sleep(5)
        else:
            return -1
        return 1

    def transmission_mode_right_click_menu(self, interface):
        """
        This keyword checks the status of transmission mode for an interface by click on interface in Device360
        :param interface: a string with the number(index) of interface
        -Keyword Usage:
            -  transmission_mode_right_click_menu        20
            -  transmission_mode_right_click_menu        mgmt
        :return: a string with the status of transmission mode ("Full-Duplex/Half-Duplex")
                -1 the interface was not found
        """

        list_items = self.get_icon_ports_items()
        if list_items:
            pass
        else:
            self.utils.print_info("List was not found")
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
        return -1

    def transmission_mode_overview_table(self, port_name):
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
                    self.utils.print_debug("Interface name for port is not displayed. Check the tab")
                    return -1
                if port_name == interface_name.text.lower():
                    port_row = row
                    self.utils.print_info("Found port: ", interface_name.text)
                    self.utils.print_info("Found row for port: ", port_row.text)
                    break
                else:
                    pass
        else:
            self.utils.print_info("Port rows are not displayed. Check the tab")
            return -1
        if port_row:
            transmission_mode_row = self.get_d360_monitor_transmission_mode(port_row)
        else:
            self.utils.print_info("Port name was not found ")
            return -1
        if transmission_mode_row:
            return transmission_mode_row.text
        else:
            self.utils.print_info("Transmission mode status not found")
            return -1

    def device360_d360_view_100_rows_on_page(self):
        """
        This keyword press view 100 rows into d360 page
        :return: 1 if button was selected; else -1
        """
        if self.get_d360_view_100_rows_on_page():
            self.utils.print_info("Select view 100 rows ")
            self.auto_actions.click(self.get_d360_view_100_rows_on_page())
            self.auto_actions.scroll_up()
            return 1
        else:
            self.utils.print_info("view 100 rows button was not found ")
        return -1

    def check_two_lists(self, port_state, port_duplex_cli):
        """
        This keyword find out if two lists have at least one element different by '' at the same index into list
        :param port_state:
        :param port_duplex_cli:
        :return: 1 if two lists have at least one element different by '' at the same index into list ; else -1
        """
        cnt = 0
        for el in port_state:
            if not '' == el and not '' == port_duplex_cli[cnt]:
                self.utils.print_info("At leas one port match ")
                return 1
            else:
                pass
            cnt = cnt + 1
        return -1

    def exit_d360_Page(self):
        """
        This keyword close the d360 page
        :return: 1 all time
        """

        if self.dev360.get_device360_device_configuration_exit_button():
            self.utils.print_info("Click on exit button")
            self.auto_actions.click(self.dev360.get_device360_device_configuration_exit_button())
        else:
            self.utils.print_info("The exit button was not found")
        return 1

    def device360_transmission_mode_overview(self, port_name):
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
            self.utils.print_info("Port rows are not displayed. Check the tab")
            return -1
        transmission_mode_row = self.get_d360_monitor_transmission_mode(port_row)
        if transmission_mode_row:
            return transmission_mode_row.text
        else:
            self.utils.print_info("Transmission mode status not found")
            return -1

    def device360_speed_overview(self, port_name):
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
            self.utils.print_info("Port rows are not displayed. Check the tab")
            return -1
        port_speed_row = self.get_d360_monitor_port_speed(port_row)
        if port_speed_row:
            self.utils.print_info("Port speed for port {} is {}".format(port_name, port_speed_row.text))
            return port_speed_row.text
        else:
            self.utils.print_info("Port speed status not found")
            return -1

    def interface_transmission_mode(self, interface):
        """
        This keyword checks the status of transmission mode for an interface by right click on interface in Device360
        :param interface: a string with the number(index) of interface
        -Keyword Usage:
            -  interface transmission mode        20
            -  interface transmission mode        mgmt
        :return: a string with the status of transmission mode ("Full-Duplex/Half-Duplex")
                -1 the interface was not found
        """
        list_items = self.get_items()
        if list_items:
            pass
        else:
            self.utils.print_info("List was not found")
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
        return -1

    def interface_port_speed(self, port):
        """
        This keyword checks the status of speed for an interface by right click on interface in Device360
        :param port: a string with the number(index) of interface
        -Keyword Usage:
            -  interface_port_speed        20
            -  interface_port_speed        mgmt
        :return: a string with the status of speed
                -1 the interface was not found
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

    def d360_check_if_vim_is_installed(self):
        """
        This function check if the Vim is installed
        :return: a string with VIM model or -1 if vim is not present
        """
        vim_model = self.get_d360_vim_model()
        if vim_model:
            self.utils.print_info("Vim is present:", vim_model.text)
            return True
        else:
            self.utils.print_info("Vim is not present")
            return False

    def d360_return_vim_port_number(self):
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
        ret_val = self.auto_actions.click(port_icon_list[int(port) - 1])
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

    def device360_device_configuration_auto_template(self, device_mac, name_stack_template):
        """
        This function will go to D360 and press create auto template and name the template
        :param device_mac: Mac of device
        :param name_stack_template: Policy template name
        :return: 1 if remain in the Create auto Template ; -1 else
        """
        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
            self.utils.print_info("D360 page was not opened ")
            return -1
        else:
            self.utils.print_info("D360 page was opened ")

        if self.devices_web_elements.get_ap_configure_button():
            self.utils.print_info("Clicking on 'Configure' button  ")
            self.auto_actions.click(self.devices_web_elements.get_ap_configure_button())
        else:
            self.utils.print_info("'Configure' button was not found ")
            return -1

        if self.dev360.get_device360_device_configuration_button():
            self.auto_actions.click(self.dev360.get_device360_device_configuration_button())
            self.utils.print_info("Clicking on 'Device Configuration 'button")
        else:
            self.utils.print_info("'Device Configuration 'button was not found ")
            return -1

        # Click on creating auto template on stacking
        if self.dev360.get_device360_create_auto_template_button():
            self.auto_actions.click(self.dev360.get_device360_create_auto_template_button())
            self.utils.print_info("Clicking on 'Creating Auto template' button")
        else:
            self.utils.print_info("'Creating Auto template 'button was not found")
            return -1
        sleep(10)
        self.utils.print_info("Enter the switch Template Name: ", name_stack_template)
        self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                    name_stack_template)
        self.auto_actions.send_enter(self.sw_template_web_elements.get_sw_template_name_textfield())
        sleep(10)

        return 1

    def device360_configure_device_port_status(self, device_mac="", device_name="", port_number="", port_status="ON"):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
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
                        self.auto_actions.click(self.get_close_dialog())
                        self.screen.save_screen_shot()
                        return 1

                if port_status.upper() == "OFF":
                    port_enabled = self.get_device360_configure_port_row_state_enabled(port_row)
                    if port_enabled:
                        self.auto_actions.click(port_enabled)
                        self.screen.save_screen_shot()
                    else:
                        self.utils.print_info(f"Port {port_number} Already Disabled")
                        self.utils.print_info("Close Dialogue Window")
                        self.auto_actions.click(self.get_close_dialog())
                        self.screen.save_screen_shot()
                        return 1

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
                        return 1
                    else:
                        return -1
            else:
                self.utils.print_info(f"Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            self.screen.save_screen_shot()
            return -1

    def device360_configure_port_access_vlan(self, device_mac="", device_name="", port_number="", access_vlan_id="",
                                             port_type="Access Port"):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
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
                self.auto_actions.select_drop_down_options(self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                sleep(2)

                self.utils.print_info("Entering Search String...")
                self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row), Keys.CONTROL + "a")
                self.utils.print_info("Deleting the selected values in port..")
                self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row), Keys.BACK_SPACE)
                self.auto_actions.send_keys(self.get_device360_configure_port_access_vlan_textfield(port_row), access_vlan_id)
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
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        return 1
                    else:
                        return -1
            else:
                self.utils.print_info(f"Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            self.screen.save_screen_shot()
            return -1

    def device360_configure_port_trunk_vlan(self, device_mac="", device_name="", port_number="", trunk_native_vlan="",
                                            trunk_vlan_id="", port_type="Trunk Port"):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
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
                self.auto_actions.select_drop_down_options(self.get_device360_configure_port_usage_drop_down_options(port_row), port_type)
                sleep(2)

                self.utils.print_info("Entering Trunk Native Vlan TextField...")
                self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row), Keys.CONTROL + "a")
                sleep(2)
                self.utils.print_info("Deleting the selected values in port..")
                self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row), Keys.BACK_SPACE)
                sleep(2)
                self.auto_actions.send_keys(self.get_device360_configure_port_trunk_native_vlan_textfield(port_row), trunk_native_vlan)
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
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        return 1
                    else:
                        return -1
            else:
                self.utils.print_info(f"Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            self.screen.save_screen_shot()
            return -1

    def device360_configure_port_transmission_mode_and_speed(self, device_mac="", device_name="", port_number="",
                                                            transmission_mode="", speed=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
        sleep(2)

        self.utils.print_info("Click Port Settings Tab")
        self.auto_actions.click(self.get_device360_port_configuration_port_settings_tab())
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
                self.auto_actions.select_drop_down_options(self.get_device360_port_settings_transmission_mode_drop_down_options(port_row), transmission_mode)
                sleep(2)

                self.utils.print_info("clicking Speed drop down Button")
                self.auto_actions.click(self.get_device360_port_settings_speed_drop_down_button(port_row))
                sleep(2)

                self.utils.print_info(f"Selecting Speed Option : {speed}")
                self.auto_actions.select_drop_down_options(self.get_device360_port_settings_speed_drop_down_options(port_row), speed)
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
                        return 1
                    else:
                        return -1
            else:
                self.utils.print_info(f"Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            self.screen.save_screen_shot()
            return -1

    def device360_configure_device_port_poe_status_and_profile(self, device_mac="", device_name="", port_number="", poe_profile="", poe_status="ON"):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())
        sleep(4)

        self.utils.print_info("Click PortConfiguration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
        sleep(2)

        self.utils.print_info("Click PSE Tab")
        self.auto_actions.click(self.get_device360_port_configuration_pse_tab())
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
                    self.auto_actions.select_drop_down_options(self.get_device360_port_configuration_pse_profile_select_options(), poe_profile)
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
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
                    sleep(2)

                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    if "Interface settings were updated successfully." in tool_tip_text:
                        return 1
                    else:
                        return -1
            else:
                self.utils.print_info(f"Port Row Not Found")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            self.screen.save_screen_shot()
            return -1

    def device360_get_voss_wireframe_cpu_utilization(self, device_mac="", device_name=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(10)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
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
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return cpu_utilization[1].strip()
            else:
                self.utils.print_info(f"Tooltip content Not Found for WireFrame CPU Utilization")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        self.screen.save_screen_shot()
        return -1

    def device360_get_voss_wireframe_memory_utilization(self, device_mac="", device_name=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(10)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
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
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return memory_usage[1].strip()
            else:
                self.utils.print_info(f"Tooltip content Not Found for WireFrame Memory Utilization")
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
                self.screen.save_screen_shot()
                return -1

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        self.screen.save_screen_shot()
        return -1

    def test_device_cli(self, command, device_serial=None, device_mac=None, max_time=180, interval_time=20, delay=30):
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
            search_result = self.dev.search_device(device_mac=device_mac)

            if search_result != -1:
                if self.dev.select_device(device_mac=device_mac):
                    sleep(2)
                    self.utils.print_info("Selected the device with MAC ", device_mac)
                    flag_device_selected = True

        elif device_serial:
            self.utils.print_info("Finding device with serial ", device_mac)
            search_result = self.dev.search_device(device_serial=device_serial)

            if search_result != -1:
                if self.dev.select_device(device_serial=device_serial):
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
            self.utils.print_info("Actions button not found")
            self.screen.save_screen_shot()
            return -1
        sleep(3)

        advanced = self.dev360.get_advanced_button()
        for el in advanced:
            if 'Advanced' == el.text:
                if el:
                    self.utils.print_info("Hovering on Advanced")
                    self.auto_actions.move_to_element(el)
                else:
                    self.utils.print_info("Advanced button not found")
                    self.screen.save_screen_shot()
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
            self.utils.print_info("Device CLI button not found")
            self.screen.save_screen_shot()
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
                    self.auto_actions.click(self.dev360.get_cli_apply())
                    sleep(delay)
                else:
                    self.utils.print_info("'Send command' field not found")
                    self.screen.save_screen_shot()
                    return -1
                cnt = 0
                while cnt < int(max_time):
                    result = self.dev360.get_result_area()
                    if result:
                        if result.text != '':
                            output_after = result.text
                            if output_before != output_after:
                                output_before = output_after
                                self.utils.print_info("The output after command {} is : ".format(el, output_before))
                                break
                            else:
                                pass
                        else:
                            pass
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
                return -1
            else:
                return output_before
        else:
            search = self.dev360.get_cli_command_line()
            if search:
                self.utils.print_info("Send command:", command)
                self.auto_actions.send_keys(search, command)
                sleep(2)
                self.auto_actions.click(self.dev360.get_cli_apply())
                sleep(delay)
            else:
                self.utils.print_info("Web CLI input field not found")
                self.screen.save_screen_shot()
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
                            self.utils.print_info("close button not found")
                            self.screen.save_screen_shot()
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
        self.screen.save_screen_shot()
        
        return -1

    def get_supplemental_cli(self, name_s_cli, cli_commands=""):
        """
        This keyword will add or edit a supplemental cli profile with cli commands in D360
        - Keyword Usage
         - ``Get supplemental cli       ${NAME_CLI}     ${CLI_COMMANDS}``
        :param name_s_cli: Name of the supplemental cli profile
        :param cli_commands: list of CLI commands separated by comma
        :return: 1 if supplemental cli profile save successfully else -1
        """
        self.auto_actions.click(self.get_device360_configure_button())
        self.auto_actions.click(self.get_device360_device_configuration_button())
        self.auto_actions.click(self.get_device360_select_supplemental_cli())
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
                        self.auto_actions.click(self.get_device360_device_configuration_save_button())
                        sleep(3)
                        found_profile = True
                        self.utils.print_info("Exit device configuration")
                        if self.get_device360_device_configuration_exit_button():
                            self.auto_actions.click(self.get_device360_device_configuration_exit_button())
                            return 1
                        else:
                            self.utils.print_info("Exit D360 button not found")
                            return -1
                    else:
                        self.utils.print_info("Edit profile")
                        self.auto_actions.click(self.get_device360_supplemental_cli_edit_profile())
                        profile_commands_cli = self.get_device_360_supplemental_cli_profile_commands()
                        cli_command_list = cli_commands.split(",")
                        new_line_cli_commands = "\n".join(cli_command_list)
                        sleep(3)
                        self.auto_actions.send_keys(profile_commands_cli, new_line_cli_commands)
                        sleep(3)
                        self.utils.print_info("Saving Profile")
                        self.auto_actions.click(self.get_device360_supplemental_cli_save_profile())
                        sleep(3)
                        self.utils.print_info("Saving Configuration")
                        self.auto_actions.click(self.get_device360_device_configuration_save_button())
                        sleep(3)
                        found_profile = True
                        self.utils.print_info("Exit device configuration")
                        if self.get_device360_device_configuration_exit_button():
                            self.auto_actions.click(self.get_device360_device_configuration_exit_button())
                            return 1
                        else:
                            self.utils.print_info("Exit D360 button not found")
                            return -1
            if found_profile == False:
                self.utils.print_info("'{}' profile was not found".format(name_s_cli))
                self.utils.print_info("Creating one")
                self.auto_actions.click(self.get_device_360_supplemental_cli_new_profile())
                self.auto_actions.send_keys(self.get_device_360_supplemental_cli_profile_name(), name_s_cli)
                sleep(3)
                profile_commands_cli = self.get_device_360_supplemental_cli_profile_commands()
                cli_command_list = cli_commands.split(",")
                new_line_cli_commands = "\n".join(cli_command_list)
                sleep(3)
                self.auto_actions.send_keys(profile_commands_cli, new_line_cli_commands)
                sleep(3)
                self.utils.print_info("Saving Profile")
                self.auto_actions.click(self.get_device360_supplemental_cli_save_profile())
                sleep(3)
                self.utils.print_info("Saving Configuration")
                self.auto_actions.click(self.get_device360_device_configuration_save_button())
                sleep(3)
                self.utils.print_info("Exit device configuration")
                if self.get_device360_device_configuration_exit_button():
                    self.auto_actions.click(self.get_device360_device_configuration_exit_button())
                    return 1
                else:
                    self.utils.print_info("Exit D360 button not found")
                sleep(3)
        else:
            self.utils.print_info("List was not found")
            return -1
        return 1

    def device360_power_details(self, device_mac="", device_name=""):
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
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)
        sleep(5)

        power_el = self.dev360.get_device360_thunderbold_icon()
        if power_el:
            self.utils.print_info("Power Details")
            self.auto_actions.click_and_hold_element(power_el)
            self.auto_actions.move_to_element(power_el)
        else:
            self.utils.print_info("Power details not found")
        sleep(5)
        power_details = self.dev360.get_device360_power_details().text
        self.utils.print_info(f"", power_details)
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        return power_details

    def device360_configure_poe_threshold_value(self, threshold_value, device_mac="", device_name=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
        sleep(5)
        self.select_configure_tab()
        self.select_port_configuration_view()
        sleep(2)
        self.utils.print_info("Click PSE Tab")
        self.auto_actions.click(self.get_device360_port_configuration_pse_tab())
        sleep(2)
        pse_settings_for_device_button = self.get_device360_pse_settings_for_device_button()
        if pse_settings_for_device_button:
            self.utils.print_info("Click on PSE settings for device")
            self.auto_actions.click(pse_settings_for_device_button)
        else:
            self.utils.print_info("PSE settings for device button not found")
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
            self.utils.print_info("Value needs to be between 1 and 99.")
            return -1
        sleep(2)
        save_threshold_poe = self.get_device360_save_threshold_poe_value()
        if save_threshold_poe:
            self.utils.print_info("Saving threshold {} % ".format(threshold_value))
            self.auto_actions.click(save_threshold_poe)
            sleep(2)
        else:
            self.utils.print_info("Save button not found")
            return -1
        save_btn = self.get_device360_configure_port_save_button()
        if save_btn:
            self.utils.print_info("Clicking 'Save Port Configuration' button'")
            self.auto_actions.click(save_btn)
            sleep(2)
        else:
            self.utils.print_info("Could not click Save button")
            return -1
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        return 1

    def device360_check_wired_client(self, device_serial=None, device_mac=None, client_mac=None, sleep_time=30, iteration=15):
        """
           - This keyword is used to check the client exist in device360 page based on passed client mac address
           -Flow: Manage --> Devices --> check on the Clients which is present in Device grid row based on Client MAC
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
                    except:
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
            except:
                self.utils.print_info("In Device360 -> clients table -> Connection type not found")
                client_info["connection_type"] = None

            try:
                client_info["ostype"] = self.deviceConfig.get_wired_client_os_type().text
            except:
                self.utils.print_info("In Device360 -> clients table -> Os type not found")
                client_info["ostype"] = None

            try:
                client_info["connectstatus"] = self.deviceConfig.get_wired_client_connection_status().text
            except:
                self.utils.print_info("In Device360 -> clients table -> Connect status not found")
                client_info["connectstatus"] = None

            try:
                client_info["hostname"] = self.deviceConfig.get_wired_client_hostname().text
            except:
                self.utils.print_info("In Device360 -> clients table -> Host Name not found")
                client_info["hostname"] = None

            try:
                client_info["clientmac"] = self.deviceConfig.get_wired_client_mac().text
            except:
                self.utils.print_info("In Device360 -> clients table -> Client Mac not found")
                client_info["clientmac"] = None

            try:
                client_info["ipv4"] = self.deviceConfig.get_wired_client_IPv4().text
            except:
                self.utils.print_info("In Device360 -> clients table -> IPv4 Address not found")
                client_info["ipv4"] = None

            try:
                client_info["ipv6"] = self.deviceConfig.get_wired_client_IPv6().text
            except:
                self.utils.print_info("In Device360 -> clients table -> IPv6 not found")
                client_info["ipv6"] = None

            try:
                client_info["username"] = self.deviceConfig.get_wired_client_user_name().text
            except:
                self.utils.print_info("In Device360 -> clients table -> Username not found")
                client_info["username"] = None

            try:
                client_info["vlan"] = self.deviceConfig.get_wired_client_vlan().text
            except:
                self.utils.print_info("In Device360 -> clients table -> vlan not found")
                client_info["vlan"] = None

            try:
                client_info["Connected_via"] = self.deviceConfig.get_wired_client_connected_via().text
            except:
                self.utils.print_info("In Device360 -> clients table -> Connected via not found")
                client_info["Connected_via"] = None

            print("The complete client info -> ", client_info)
            self.close_device360_window()

            return client_info
        else:
            return -1

    def device360_click_clients(self, search_string, device_mac="", device_serial="", sleeptime=30, iteration=30):
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
                    device_row = self.dev.get_device_row(device_mac)
                    if device_row:
                        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                            self.utils.print_info(f"Device not found in the device row grid with mac:{device_mac}")
                            return -1
                        sleep(8)

                if device_serial:
                    self.utils.print_info("Checking Search Result with Device Name : ", device_serial)
                    device_row = self.dev.get_device_row(device_serial)
                    if device_row:
                        if self.navigator.navigate_to_device360_page_with_host_name(device_serial) == -1:
                            self.utils.print_info(f"Device not found in the device row grid with device name :{device_serial}")
                            return -1
                        sleep(8)
                sleep(5)

            except:
                self.utils.print_info("Not able to navigate to the page")
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
                clickable = self.auto_actions.click(self.dev360.get_device360_click_particular_client())
                if clickable == 1:
                    print("Able to click the client and see the popup...")
                    sleep(5)
                    break
            except:
                print("There was an error during click of Client")

            if clickable != 1:
                print("The link is not clickable, so waiting for the client Mac address to become clickable")
                self.utils.print_info("Close D360 Dialogue Window")
                self.close_device360_window()
                self.dev.refresh_devices_page()
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

        except:
            self.utils.print_info("In Client Popup, Client Mac not found")
            client_info["client_mac"] = None

        try:
            client_info["ipv4"] = self.deviceConfig.get_wired_client_popup_IPv4().text
        except:
            self.utils.print_info("In Client Popup, IPv4 Address not found")
            client_info["ipv4"] = None

        try:
            client_info["ipv6"] = self.deviceConfig.get_wired_client_IPv6().text
        except:
            self.utils.print_info("In Client Popup, IPv6 not found")
            client_info["ipv6"] = None

        try:
            client_info["port_speed"] = self.deviceConfig.get_wired_client_popup_portSpeed().text
        except:
            self.utils.print_info("In Client Popup, Port speed not found")
            client_info["port_speed"] = None

        try:
            client_info["negotiated_speed"] = self.deviceConfig.get_wired_client_popup_negotiatedspeed().text
        except:
            self.utils.print_info("In Client Popup, Negotiated speed not found")
            client_info["negotiated_speed"] = None

        try:
            client_info["vlan"] = self.deviceConfig.get_wired_client_popup_vlan().text
        except:
            self.utils.print_info("In Client Popup, VLAN Not found")
            client_info["vlan"] = None
        try:
            client_info["portMode"] = self.deviceConfig.get_wired_client_popup_portMode().text
        except:
            self.utils.print_info("In Client Popup, portMode not found")
            client_info["portMode"] = None

        self.utils.print_info("The complete client info -> ", client_info)
        return client_info

    def close_client360_window(self):
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
            self.auto_actions.click(self.dev360.get_client360_close_dialog())
            return 1
        else:
            self.screen.save_screen_shot()
            self.utils.print_info("Could not obtain Client360 close button - make sure Client360 window is open")
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
        except:
            self.utils.print_info("There is a problem while fetching connection status in D360 page, which means we are not at intended page")
        try:
            client_status = self.deviceConfig.get_wired_client_popup_mac().text
        except:
            self.utils.print_info("There is a problem while fetching mac of client, which indirectly means we are not landed at C360 page")
        if client_status:
            print("The current page is client 360 page....")
            return 2
        elif connection_status:
            print("The current page is Device 360 page")
            return 1
        return -1

    def device360_set_network_policy(self, network_policy="default"):
        """
        - This keyword sets a custom network policy on the Device Configuration page.
        - It is assumed that the Device360 window is open.
        - Flow : Device 360 Page -> Configure -> Device Configuration
        - Keyword Usage
         - ``device360_set_network_policy  network_policy=PPSK_POL``
        :return: 1 if the selection was made, -1 if not
        """
        self.utils.print_info(f"select '{network_policy}' from drop down")
        self.auto_actions.click(self.get_device360_configure_device_network_policy())
        device_network_policy_drop_down_items = self.get_device360_configure_device_network_policy_items()

        if device_network_policy_drop_down_items:
            if self.auto_actions.select_drop_down_options(device_network_policy_drop_down_items, network_policy):
                self.utils.print_info(f"Selected network policy '{network_policy}' from drop down")

        element = self.get_device360_configure_device_network_policy()
        if element.text not in network_policy:
            self.utils.print_info(f"Not able to select '{network_policy}' from drop down")
            return -1

        return 1

    def select_dhcp_ip_address_view(self):
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
            self.utils.print_info(
                "Could not find the dhcp_ip_link - make sure Device360 window is open and on Configure tab")
            return -1

        return 1

    def search_for_vlan_subnetworks_type_in_row_table(self, *searched_values):
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
            self.utils.print_info(" Not able to find the searched value in table ")
            return -1

    def device360_confirm_column_picker_column_selected(self, option, *columns, select_page="", device_mac="",
                                                        device_name=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
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
            self.utils.print_info(f"No '{select_page}' page ")
            return -1

        ret_val = 1
        self.utils.print_info("Clicking on Column Picker")
        sleep(5)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.auto_actions.click(self.get_device360_column_picker_icon())
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
        self.auto_actions.click(self.get_device360_column_picker_icon())
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        return ret_val

    def device360_check_column_picker(self, option, *columns, select_page="", device_mac="", device_name=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(10)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
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
            self.utils.print_info(f"No '{select_page}' page ")
            return -1
        ret_val = 1
        self.utils.print_info("Clicking on Column Picker")
        sleep(10)
        # Handle the case where a tooltip / popup is covering the column picker icon
        self.auto_actions.click(self.get_device360_column_picker_icon())
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
        self.auto_actions.click(self.get_device360_column_picker_icon())
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        return ret_val

    def create_new_port_type(self, template_values, port, d360=False, verify_summary=True):
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
                                                #['default-pse-vsp'/'None', 'default-pse-vsp'/'None']
                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page7 summaryPage': ["next_page", None]

                                        #==========================================
                                        #Only for exos
                                        'page6 ELRPSettingsPage': ["next_page", None],
                                        'elrp status': ['click', 'enabled'],      #['click'/None, 'on'/'off'/None]

                                        'page7 pseSettingsPage': ["next_page", None],
                                        'PSE profile':[None,None],
                                                #['default-pse-vsp'/'None', 'default-pse-vsp'/'None']
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
            self.utils.print_info("name can not be empty" )
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
                        sleep(2)
                    else:
                        self.utils.print_info(" The button d360_create_port_type  was not found")
                        self.screen.save_screen_shot()
                        return -1
                else:
                    self.utils.print_info("Port was not found ")
                    return -1
            else:
                return -1
        cnt = 0
        for key in template_values.keys():
            if not template_values[key][0] == None:
                conf_element = self.configure_element_port_type(key, template_values[key][0])
                if conf_element == 1:
                    self.utils.print_info("The element {} was configured ".format(key))
                else:
                    self.utils.print_info("The element {} was not configured ".format(key))
                    return -1
            else:
                pass
            cnt = cnt + 1
        if verify_summary:
            return self.port_type_verify_summary(template_values)
        else:
            sleep(5)
            close_port_type_box = self.get_close_port_type_box()
            sleep(5)

            if close_port_type_box:
                self.utils.print_info(" The button close_port_type_box from policy  was found")
                self.auto_actions.click(close_port_type_box)
                sleep(2)
            else:
                self.utils.print_info(" The button close_port_type_box from policy was not found")
            return 1

    def edit_port_type(self, template_values, port, verify_summary=True):
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
                                                #['default-pse-vsp'/'None', 'default-pse-vsp'/'None']
                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page7 summaryPage': ["next_page", None]

                                        #==========================================
                                        #Only for EXOS
                                        'page6 ELRPSettingsPage': ["next_page", None],
                                        'elrp status': ['click', 'enabled'],      #['click'/None, 'on'/'off'/None]

                                        'page7 pseSettingsPage': ["next_page", None],
                                        'PSE profile':[None,None],
                                                #['default-pse-vsp'/'None', 'default-pse-vsp'/'None']
                                        'poe status':[None,'on'],           #['click'/None, 'on'/'off'/None]

                                        'page8 summaryPage': ["next_page", None]
                                    }
        :param port: the port where new port type will be created
        :param verify_summary: True if configured values will be verify on summary page. False if verification on summary
        page will be skipped
        :return: 1 if new port type was successfully edited and summary page displays correct values  ; else -1
        """

        rows = self.get_policy_configure_port_rows()
        if not rows:
            self.utils.print_info("Could not obtain list of port rows")
            return -1
        else:
            for row in rows:
                if port in row.text:
                    policy_edit_port_type = self.get_policy_edit_port_type(row)
                    if policy_edit_port_type:
                        self.utils.print_info(" The button policy_edit_port_type from policy  was found")
                        self.auto_actions.click(policy_edit_port_type)
                        sleep(2)
                        break
                    else:
                        self.utils.print_info(" The button policy_edit_port_type from policy  was not found")
                        self.screen.save_screen_shot()
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
                        return -1
                else:
                    conf_element = self.configure_element_port_type(key, template_values[key][0])
                    if conf_element == 1:
                        self.utils.print_info("The element {} was configured ".format(key))
                    else:
                        self.utils.print_info("The element {} was not configured ".format(key))
                        return -1
            else:
                pass
            cnt = cnt + 1
        if verify_summary:
            return self.port_type_verify_summary(template_values)
        else:
            close_port_type_box = self.get_close_port_type_box()
            if close_port_type_box:
                self.utils.print_info(" The button close_port_type_box from policy  was found")
                self.auto_actions.click(close_port_type_box)
                sleep(2)
            else:
                self.utils.print_info(" The button close_port_type_box from policy was not found")
            return 1

    def port_type_verify_summary(self, template_values):
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
                conf_element = self.get_select_element_port_type_summary(key)
                print("For ", key, "we have ", conf_element)
                if conf_element.text.lower() == template_values[key][1].lower():
                    self.utils.print_info(f"The element is correct into summary. Key: {key}  Value: "
                                          f"{conf_element.text.lower()}")
                else:
                    self.utils.print_info("The element is not correct into summary. Current value in summary:" +
                                          conf_element.text + " Wanted value: " + template_values[key][1])
                    return -1
            else:
                pass
        close_port_type_box = self.get_close_port_type_box()
        if close_port_type_box:
            self.utils.print_info(" The button close_port_type_box from policy  was found")
            self.auto_actions.click(close_port_type_box)
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
            get_next_button = self.get_select_element_port_type("next_button")
            if get_next_button:
                sleep(5)
                self.auto_actions.click(get_next_button)
                sleep(2)
                return 1
            else:
                self.utils.print_info("get_next_button not found ")

        elif "usagePage" in element:
            sleep(5)
            get_tab_usagePage = self.get_select_element_port_type("usagePage")
            if get_tab_usagePage:
                sleep(5)
                self.auto_actions.click(get_tab_usagePage)
                return 1

        elif "trunkVlanPage" in element or "accessVlanPage" in element:
            sleep(5)
            get_tab_vlan = self.get_select_element_port_type("tab_vlan")
            if get_tab_vlan:
                sleep(5)
                self.auto_actions.click(get_tab_vlan)
                return 1

        elif "transmissionSettingsPage" in element:
            sleep(5)
            get_tab_transmission = self.get_select_element_port_type("transmissionSettingsPage")
            if get_tab_transmission:
                sleep(5)
                self.auto_actions.click(get_tab_transmission)
                return 1

        elif "stpPage" in element:
            sleep(5)
            get_tab_stp = self.get_select_element_port_type("stpPage")
            if get_tab_stp:
                sleep(5)
                self.auto_actions.click(get_tab_stp)
                return 1

        elif "stormControlSettingsPage" in element:
            sleep(5)
            get_storm_control = self.get_select_element_port_type("stormControlSettingsPage")
            if get_storm_control:
                sleep(5)
                self.auto_actions.click(get_storm_control)
                return 1

        elif "ELRPSettingsPage" in element:
            sleep(5)
            get_elrp = self.get_select_element_port_type("ELRPSettingsPage")
            if get_elrp:
                sleep(5)
                self.auto_actions.click(get_elrp)
                return 1

        elif "pseSettingsPage" in element:
            sleep(5)
            get_tab_pse_settings = self.get_select_element_port_type("pseSettingsPage")
            if get_tab_pse_settings:
                sleep(5)
                self.auto_actions.click(get_tab_pse_settings)
                return 1

        elif "summaryPage" in element:
            sleep(5)
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

        # page ELRP (ONLY FOR EXOS)
        elif element == "elrp status":
            sleep(5)
            get_elrp_status = self.get_select_element_port_type(element, value)
            if get_elrp_status:
                sleep(2)
                self.auto_actions.click(get_elrp_status)
                return 1

        # page PSE
        elif element.lower() == "pse profile":
            sleep(5)
            get_pse_profile = self.get_select_element_port_type(element)
            if get_pse_profile:
                self.auto_actions.click(get_pse_profile)
                sleep(2)
                get_pse_profile_items = self.get_select_element_port_type("pse_profile_items")
                if self.auto_actions.select_drop_down_options(get_pse_profile_items, value):
                    self.utils.print_info(" Selected into dropdown value : ", value)
                    return 1
                else:
                    sleep(5)
                    get_pse_profile_add = self.get_select_element_port_type("pse_profile_add")
                    if get_pse_profile_add:
                        self.auto_actions.click(get_pse_profile_add)
                        sleep(2)
                        get_pse_profile_name = self.get_select_element_port_type("pse_profile_name")
                        if get_pse_profile_name:
                            self.auto_actions.send_keys(get_pse_profile_name, value)
                            sleep(2)
                        else:
                            self.utils.print_info("get_pse_profile_name not found ")
                        sleep(5)
                        get_pse_profile_power_mode = self.get_select_element_port_type(element)
                        if get_pse_profile_power_mode:
                            self.auto_actions.click(get_pse_profile_power_mode)
                            sleep(2)
                            get_pse_profile_power_mode_items = self.get_select_element_port_type("pse_profile_power_mode_items")
                            if self.auto_actions.select_drop_down_options(get_pse_profile_power_mode_items, value):
                                self.utils.print_info(" Selected into dropdown value : ", value)
                        sleep(2)
                        get_pse_profile_priority = self.get_select_element_port_type(element)
                        if get_pse_profile_priority:
                            self.auto_actions.click(get_pse_profile_priority)
                            sleep(2)
                            get_pse_profile_priority_items = self.get_select_element_port_type("pse_profile_priority_items")
                            if self.auto_actions.select_drop_down_options(get_pse_profile_priority_items, value):
                                self.utils.print_info(" Selected into dropdown value : ", value)
                        sleep(2)
                        get_pse_profile_description = self.get_select_element_port_type("pse_profile_description")
                        if get_pse_profile_description:
                            self.auto_actions.send_keys(get_pse_profile_description, value)
                            sleep(2)
                        else:
                            self.utils.print_info("get_pse_profile_description not found ")
                        sleep(5)
                        get_pse_profile_save = self.get_select_element_port_type("pse_profile_save")
                        if get_pse_profile_save:
                            self.auto_actions.click(get_pse_profile_save)
                            return 1
                        else:
                            self.utils.print_info("get_pse_profile_save not found ")
                    else:
                        self.utils.print_info("get_pse_profile_add not found ")
            else:
                self.utils.print_info("get_pse_profile not found ")
        elif element.lower() == "poe status":
            sleep(5)
            get_poe_status = self.get_select_element_port_type(element, value)
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

    def d360_save_port_configuration(self):

        get_save_button = self.get_device_d360_save_port_configuration()
        if get_save_button:
            self.auto_actions.click(get_save_button)
            self.utils.print_info("save the port configuration ")
            return 1
        else:
            return -1

    def d360_cancel_port_configuration(self):

        get_save_button = self.get_device_d360_cancel_port_configuration()
        if get_save_button:
            self.auto_actions.click(get_save_button)
            self.utils.print_info("Exit the port configuration ")
            return 1
        else:
            return -1

    def device360_configure_ports_trunk_vlan(self, port_numbers="", trunk_native_vlan="", trunk_vlan_id="",
                                                   port_type="Trunk Port", **kwargs):
        """
        - This keyword will configure multiple ports to Port Type: Trunk and assign a vlan value
        - Assume that already in device360 window
        - Flow: Configure --> Port Configuration--> interface --> Ports Usage and Vlan Range

        :param device_name: Device Name
        :param port_number: Port Number of the Switch
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
                    self.utils.print_info(f"Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
                    kwargs['fail_msg'] = "Port Row Not Found"
                    self.screen.save_screen_shot()
                    self.common_validation.failed(**kwargs)
            self.select_configure_tab()
            save_btn = self.get_device360_configure_port_save_button()
            if save_btn:
                self.utils.print_info("Clicking 'Save Port Configuration' button'")
                self.auto_actions.click(save_btn)
                self.screen.save_screen_shot()
                self.utils.print_info("Close Dialogue Window")
                self.auto_actions.click(self.get_close_dialog())
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
                # self.auto_actions.click(self.get_close_dialog())
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
            self.auto_actions.click(self.get_close_dialog())
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def device360_configure_ports_trunk_stack(self, port_numbers="", trunk_native_vlan="", trunk_vlan_id="", slot = "",
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
                    self.utils.print_info(f"Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
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
                self.auto_actions.click(self.get_close_dialog())
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
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())

        self.utils.print_info("Click Port Configuration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
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
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
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
                self.auto_actions.click(self.get_close_dialog())
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
            self.utils.print_info("Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def device360_configure_ports_access_vlan_stack(self, port_numbers="", access_vlan_id="1", slot="",
                                                    port_type="Access Port", **kwargs):
        """
        - This keyword will configure multiple ports to the port type "Access Port"
        - Assume that already in Device 360 Window
        - Flow: Configure --> Port Configuration--> interface --> Ports Usage and Vlan

        :param device_mac: Device Mac Address
        :param device_name: Device Name
        :param port_numbers: Port Numbers of the Switch [written as: "1,2,3..."]
        :param access_vlan_id: Access Vlan Number for switch port
        :param port_type:  Access Port
        :param slot: The slot of the stack
        :return: 1 if Ports Usage Access and Vlan Successfully configured else -1
        """
        self.utils.print_info("Click Configure Button")
        if not self.get_device360_configure_button().is_selected():
            self.auto_actions.click(self.get_device360_configure_button())
        self.utils.print_info("Click Port Configuration Button")
        self.auto_actions.click(self.get_device360_configure_port_configuration_button())
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
                    self.utils.print_info(f"Port Row Not Found")
                    self.utils.print_info("Close Dialogue Window")
                    self.auto_actions.click(self.get_close_dialog())
                    self.screen.save_screen_shot()
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
                self.auto_actions.click(self.get_close_dialog())
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
            self.utils.print_info(f"Port Configuration Page Content not available in the Page")
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            kwargs['fail_msg'] = "Port Configuration Page Content not available in the Page"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
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
        self.auto_actions.click(self.dev360.get_device360_port_configuration_stack_units_dropdown())

        self.utils.print_info("Gather the list of the devices in the stack")
        slot_index = 1
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
                self.utils.print_info(f"Unable to locate slot {str(slot)}")
                kwargs['fail_msg'] = f"Unable to locate slot {str(slot)}"
                self.screen.save_screen_shot()
                self.common_validation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("Unable to gather the list of the slots for the stack")
            kwargs['fail_msg'] = "Unable to gather the list of the slots for the stack"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def device360_configure_poe_threshold_value_stack(self, threshold_value, slot, device_mac="", device_name=""):
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
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
        self.select_configure_tab()
        self.select_port_configuration_view()
        self.select_stack_unit(slot=slot)
        sleep(2)
        self.utils.print_info("Click PSE Tab")
        self.auto_actions.click(self.get_device360_port_config_pse_tab_slot_stack())
        sleep(2)
        pse_settings_for_device_button = self.get_device360_pse_settings_for_device_button_stack()
        if pse_settings_for_device_button:
            self.utils.print_info("Click on PSE settings for device")
            self.auto_actions.click(pse_settings_for_device_button)
        else:
            self.utils.print_info("PSE settings for device button not found")
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
            self.utils.print_info("Value needs to be between 1 and 99.")
            return -1
        sleep(2)
        save_threshold_poe = self.get_device360_save_threshold_poe_value_stack()
        if save_threshold_poe:
            self.utils.print_info("Saving threshold {} % ".format(threshold_value))
            self.auto_actions.click(save_threshold_poe)
        else:
            self.utils.print_info("Save button not found")
            return -1
        self.select_configure_tab()
        sleep(2)
        save_btn = self.get_device360_configure_port_save_button_stack()
        if save_btn:
            self.utils.print_info("Clicking 'Save Port Configuration' button'")
            self.auto_actions.click(save_btn)
        else:
            self.utils.print_info("Could not click Save button")
            return -1
        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click(self.get_close_dialog())
        return 1

    def device360_power_details_stack(self, slot, device_mac="", device_name=""):
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
        self.navigator.navigate_to_devices()
        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
        slot_index = 1
        slot_found = False
        slot_details_overview = self.get_device360_stack_overview_slot_details_rows()
        if slot_details_overview:
            power_elements = self.dev360.get_device360_thunderbold_icon_stack(slot_details_overview)
            for power_item in power_elements:
                if slot_index == int(slot):
                    self.utils.print_info("Slot " + str(slot) + " found in the stack, selecting the slot")
                    self.auto_actions.click_and_hold_element(power_item)
                    sleep(2)
                    self.auto_actions.move_to_element(power_item)
                    sleep(2)
                    slot_found = True
                    break
                slot_index = slot_index + 1
            if not slot_found:
                self.utils.print_info("Unable to locate the correct slot")
                return -1
        else:
            self.utils.print_info("Power details not found")
            return -1
        sleep(2)
        power_details = self.dev360.get_device360_power_details().text
        if power_details:
            self.utils.print_info(f"", power_details)
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click(self.get_close_dialog())
            return power_details
        else:
            self.utils.print_info("Power details not found")
            return -1

# Wifi6E Clients - Pranav

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
        #self.utils.print_info("Navigate to Mange-->Devices")
        #self.navigator.navigate_to_device360_with_client(device_serial)
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
        #self.utils.print_info("Navigate to Mange-->Devices")
        #self.navigator.navigate_to_device360_with_client(device_serial)

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
#        total_count = self.dev360.get_device360_total_wireless_clients()
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

# =============================================