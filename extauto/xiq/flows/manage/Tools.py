from time import sleep

import extauto.common.CloudDriver
from extauto.common.Cli import *
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.WebElementHandler import *

from extauto.xiq.elements.ToolsElements import ToolsElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.Device360WebElements import Device360WebElements

from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator


class Tools:
    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.tools_elements = ToolsElements()
        self.dialog_web_elements = DialogWebElements()
        self.dev360 = Device360WebElements()
        self.devices = Devices()
        self.screen = Screen()
        self.cli = Cli()
        self.builtin = BuiltIn()
        self.web = WebElementHandler()
        self.driver = extauto.common.CloudDriver.cloud_driver

    def get_neighbor_info(self, serial, mac):
        self.navigator.navigate_to_tools_page()
        sleep(5)

        self.utils.print_info("Clicking on Utilities button...")
        self.auto_actions.click(self.tools_elements.get_utilities_button())
        sleep(10)

        self.utils.print_info("Selecting Neighbor Info menu item")
        self.auto_actions.click(self.tools_elements.get_neighbor_info_menu_item())
        sleep(15)

        self.devices.refresh_devices_page()
        sleep(10)

        if self.devices.select_ap(ap_serial=serial):
            error = self.dialog_web_elements.get_tooltip_text()
            if error:
                self.utils.print_info("Error: ", error)
                if 'The requested operation cannot be performed because you selected at least one unmanaged device.' \
                        in error:
                    return -1
                elif 'The requested operation cannot be performed because you have selected at least one unmanaged/disconnected device.' \
                        in error:
                    return -1
                else:
                    return -2

            sleep(10)

            self.auto_actions.click(self.tools_elements.get_neighbor_info_button())
            sleep(10)
            rows = self.tools_elements.get_neighbor_page_body_grid_rows()
            sleep(10)
            for row in rows:
                if mac in row.text:
                    self.utils.print_info("Found AP MAC in row: ", row.text)

                self.utils.print_info("Closing the Dialog page")
                self.auto_actions.click(self.tools_elements.get_neighbor_info_close_button())
                return 1
        return -1

    def device_diagnostics_ping(self, serial):

        self.navigator.navigate_to_tools_page()
        sleep(5)

        self.utils.print_info("Clicking on Utilities button...")
        self.auto_actions.click(self.tools_elements.get_utilities_button())
        sleep(10)

        self.auto_actions.click(self.tools_elements.get_device_diagnostics_menu_item())

        self.devices.refresh_devices_page()
        sleep(10)

        if self.devices.search_ap(ap_serial=serial):
            if self.devices.select_ap(ap_serial=serial):
                error = self.dialog_web_elements.get_tooltip_text()
                if error:
                    self.utils.print_info("Error: ", error)
                    if 'The requested operation cannot be performed because you selected at least one unmanaged device.' \
                            in error:
                        return -1
                    elif 'The requested operation cannot be performed because you have selected at least one unmanaged/disconnected device.' \
                            in error:
                        return -1
                    else:
                        return -2
                sleep(10)

        self.utils.print_info("Clicking Diagnostics button")
        self.auto_actions.click(self.tools_elements.get_diagnostics_button())
        sleep(5)

        self.utils.print_info("Selecting Ping...")
        self.auto_actions.click(self.tools_elements.get_diagnostics_ping_menu_item())
        sleep(10)

        self.utils.print_info("Getting Ping Output...")
        output = self.tools_elements.get_diagnostics_ping_output().text
        sleep(2)

        self.utils.print_info("Getting Ping Output: ", output)
        sleep(2)

        self.utils.print_info("Closing the Dialog page")
        self.auto_actions.click(self.tools_elements.get_neighbor_info_close_button())

        if 'ping statistics' in output and '5 packets transmitted' in output:
            return 1

        return -1

    """
    def enable_ssh_availability(self):
        self.utils.print_info("Clicking on Account icon")
        sleep(5)

        self.auto_actions.click(self.tools_elements.get_account_icon())
        self.utils.print_info("Click on Global Settings")
        sleep(5)

        self.auto_actions.click(self.tools_elements.get_global_settings())
        self.utils.print_info("Clicking on SSH availability")
        sleep(2)

        self.auto_actions.click(self.tools_elements.get_ssh_availability())
        self.utils.print_info("Getting SSH Availability status")
        sleep(2)

        self.utils.print_info("printing ssh enable tag values : ")
        value = self.tools_elements.get_enable_ssh()
        self.utils.print_info(value)
        self.utils.print_info(value.get_attribute("type"))

        ans = value.get_attribute("checked")
        if ans == "true":
            self.utils.print_info("SSH enable box is already checked")
        else:
            self.utils.print_info("SSH is not enabled. Enabling...")
            self.auto_actions.click(self.tools_elements.get_enable_ssh())

        self.screen.save_screen_shot()
        return 1
    """

    def run_ssh_availability_on_ap(self, serial_num, time_lim):
        self.navigator.navigate_to_tools_page()
        sleep(5)
        self.auto_actions.scroll_up()
        sleep(5)
        self.utils.print_info("clicking on utilities button")
        self.auto_actions.click(self.tools_elements.get_utilities_button())

        self.utils.print_info("clicking on ssh availability")
        self.auto_actions.click(self.tools_elements.get_utilities_ssh_availability())
        sleep(5)


        if self.devices.select_ap(serial_num):
            self.utils.print_info("clicking on ssh RUN button")
            self.auto_actions.click(self.tools_elements.get_run_button())
            sleep(15)

            self.utils.print_info("clicking on 5 minutes radio")
            self.auto_actions.click(self.tools_elements.get_ssh_timeout_5_minutes_radio())
            sleep(10)

            self.utils.print_info("clicking on enable SSH button")
            self.auto_actions.click(self.tools_elements.get_enable_ssh_button())
            self.utils.print_info("sleep for 30seconds to enable SSH")
            sleep(45)

            if "SSH Active" in self.ui_tools_ssh_status_check():
                self.utils.print_info("getting ip and port number")
                ip_addr = self.tools_elements.get_ip_address().text
                port_num = self.tools_elements.get_port_num().text

                self.utils.print_info("IP is: ", ip_addr)
                self.utils.print_info("PORT number is: ", port_num)

                while ip_addr == "" and port_num == "":
                    ip_addr = self.tools_elements.get_ip_address().text
                    port_num = self.tools_elements.get_port_num().text
                sleep(5)

                self.utils.print_info(ip_addr)
                self.utils.print_info(port_num)

                return ip_addr, port_num
            else:
                self.utils.print_info("AP does not exists in the list")
                return -1

    def ui_ssh_status_check(self):
        self.utils.print_info("SSH status checking in UI")
        status = self.tools_elements.get_ssh_status().text
        self.utils.print_info("SSH Status on UI: ", status)
        self.utils.print_info(status)
        self.utils.print_info("Closing device360 Dialogue Window.")
        self.auto_actions.click(self.dev360.get_close_dialog())
        sleep(2)
        return status

    def ui_tools_ssh_status_check(self):
        self.utils.print_info("SSH status checking in UI")
        status = self.tools_elements.get_ssh_status().text
        self.utils.print_info("SSH Status on UI: ", status)
        self.utils.print_info(status)
        sleep(2)
        return status

    def lock_device(self, host, username, passwd, ssid, ssid_passwd="FFLJLSP09865"):
        # https://jira.aerohive.com/browse/APC-36061
        """
             Lock Device with 10 invalid logins
            :param host: mac station ip
            :param username: mac user login
            :param passwd: mac user password
            :param ssid:      global ssid in the network policy
            :param ssid_pass: password of ssid
            :return: return a hostname of mac station

        Usage:
            ${host}    lock device  ${MAC_STA_IP}  ${MAC_STA_USERID}  ${MAC_STA_PASS}  ${SSID}
        """
        self.utils.print_info("Lock Device")
        rc = self.cli.mac_wifi_connection(host, username, passwd, ssid, ssid_passwd, mode='fail', ntimes=11)
        return self.cli.get_mac_hostname(host, username, passwd)

    def verify_device_lock(self, host):
        # https://jira.aerohive.com/browse/APC-36061
        """ Prequis: AP should be onboared and mac station is availabe to connect to a WIFI
             Verification device is locked
            :param host: mac station ip
            :return:     return a hostname of mac station

        Usage:
            ${host}    verify_device_lock  host
        """
        self.utils.print_info("verify device lock utilities")
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.auto_actions.click(self.tools_elements.get_locked_device_element_link)

        # Feature is broken
        # self.wait_til_elements_avail(self.tool_utils.device_diag_list, 60)
        # assert  host in self.driver.page_source, "Not able to find the host"
        # ??
        # self.click_til_element_avail(self.tool_utils.get_locked_device_element_btn())
        # Unlock a device   feature is broken and not able to move forward

    def utility_device_info(self, mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name):
        """ Prequis: AP should be onboared
            Verification of the visiblity of the devices in the device list section of utilities
            :param mode     : online or offline
            :param ap_ip    : ap ip
            :param ap_usr   : ap login
            :param ap_pass  : ap password
            :param ap_sn    : ap serial number
            :param ap_name  : name of ap
            :return: None
        Usage:
            util_device_info  online  ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
            util_device_info  offline ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}}
        """

        # Navigate to the Device List
        self.utils.print_info("verify device info utilities")
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.auto_actions.click(self.tools_elements.get_device_list_element_link())
        # self.wait_til_elements_avail(self.tool_utils.device_diag_list, 60)
        self.enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)

        # Verify the AP info
        assert self.devices.search_ap_serial(ap_sn) == True, "Not able to find the ap serial " + ap_sn
        assert self.devices.select_ap(ap_sn) == 1, "Not able to select an ap " + ap_sn

        if mode == "online":
            self.click_til_element_avail(self.tools_elements.get_device_info_btn())
            actual_ap_name = self.tools_elements.get_device_info_device_name()
            assert actual_ap_name.text == ap_name, "AP does not exist " + str(ap_name)
            actual_status = self.tools_elements.get_device_connect_status()
            assert actual_status.text == "Connected", "Device is not connected"
            self.click_til_element_avail(self.tools_elements.get_device_close_dlg())
        else:
            btn_status = self.tools_elements.get_device_info_btn()
            assert btn_status.is_enabled() != True, "The device info button should be disabled"
            self.cli.capwap_ap_on_off(ap_ip, ap_usr, ap_pass, "on")

    def utility_device_client_info(self, mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_mac, ap_name):
        """ Prequis: AP should be onboared
            Verification of visibility of client information by selecting an AP
            :param mode     : online or offline
            :param ap_ip    : ap ip
            :param ap_usr   : ap login
            :param ap_pass  : ap password
            :param ap_sn    : ap serial number
            :param ap_name  : ap model
            :param ap_mac   : mac address
            :return         : None

        usage:  util_device_client_info  online   ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_MAC}  ${AP1_NAME}
                util_device_client_info  offline  ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_MAC}  ${AP1_NAME}

        """

        # Navigate to the Device Client Information
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.click_til_element_avail(self.tools_elements.get_device_client_info_link())
        self.wait_til_elements_avail(self.tools_elements.device_diag_list, 60)
        self.enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)

        assert self.devices.search_ap_serial(ap_sn) == True, "Not able to find the ap serial " + ap_sn
        assert self.devices.select_ap(ap_sn) == 1, "Not able to select an ap " + ap_sn

        # Verify the device info
        if mode == "online":
            self.click_til_element_avail(self.tools_elements.get_device_client_info_btn())
            assert ap_name in self.driver.page_source, "Not able to find the ap name"
            assert ap_mac in self.driver.page_source, "Not able to find the ap mac"
            self.auto_actions.click(self.tools_elements.get_device_client_close_btn())
        else:
            btn_status = self.tools_elements.get_device_client_info_btn()
            assert btn_status.is_enabled() != True, 'The Device Client Information button should be disabled'
            self.cli.capwap_ap_on_off(ap_ip, ap_usr, ap_pass, "on")

    def make_wifi_connection(self, host, username, passwd, ssid, ssid_passwd):
        """  Prequis: AP should be onboared and mac station is availabe to connect to a WIFI
             Make a wifi connection
            :param host: mac station ip
            :param username: mac user login
            :param passwd: mac user password
            :param ssid:      global ssid a network policy
            :param ssid_pass: password of ssid
            :param wifi_port: mac wifi port
            :param mode: pass : make a succesful wifi connection
                         fail : make a failed wifi connection
            :param ntimes     : number of times to authenticate in order to be in locked state
            :return: return a hostname of mac station
        usage:
            make wifi connection  ${MAC_STA_IP}  ${MAC_STA_USERID}  ${MAC_STA_PASS}  ${SSID}  ${SSID_PASSWD}
        """
        self.utils.print_info("Make a wifi connection")
        self.cli.mac_wifi_connection(host, username, passwd, ssid, ssid_passwd, mode='pass')
        return self.cli.get_mac_hostname(host, username, passwd)

    def verify_util_client_cnx(self, ssid, ap_name, client_mac, client_name="default", conn_type="WIRELESS"):
        """ Prequis: AP should be onboared and mac station for a WIFI
            Verification of the visibility of client information
            :param ssid     : ssid from a policy
            :param ap_name  : ap name
            :param client_mac  : mac addr of mac station
            :param client_name : name of mac station
            :param conn_type   : a conntection type - WIRELESS / WIRED
            :return: None
        usage:
            verify util client cnx    ${SSID}  ${AP1_NAME}  ${MAC_MAC_ADDR}
        """

        # Navigate to the Device Client Information
        sleep(30)  # Wait for 50 seconds for a client appearing after a wifi connections
        self.utils.print_info("verify_utility_client_cnx")
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.click_til_element_avail(self.tools_elements.get_client_info_link())

        self.wait_til_elements_avail(self.tools_elements.client_info_list, 60)
        assert self.get_value_in_tbl(self.tools_elements.client_info_list, client_mac) == 1, "client mac is not matched"
        assert self.get_value_in_tbl(self.tools_elements.client_info_list, ssid) == 1, "ssid is not matched"
        assert self.get_value_in_tbl(self.tools_elements.client_info_list, ap_name) == 1, "ap name is not matched"
        assert self.get_value_in_tbl(self.tools_elements.client_info_list, conn_type) == 1, "net_type is not matched"
        assert self.get_value_in_tbl(self.tools_elements.client_info_list,
                                     "CONNECTED") == 1, "connection type is not matched"

    def utility_device_diagnostic(self, mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name):
        """ Prequis: AP should be onboared
            Verification of the diagnostic functionalities of the device
            :param mode     : online or offline
            :param ap_ip    : ap ip
            :param ap_usr   : ap login
            :param ap_pass  : ap password
            :param ap_sn    : ap serial number
            :param ap_name  : ap name
            :return: None   :
        usage:
            utility device diagnostic  online   ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
            utility device diagnostic  offline  ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
        """

        # Navigate to the Device Diagnostic
        self.utils.print_info("utility_device_diagnostic")
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.click_til_element_avail(self.tools_elements.get_device_diag_link())
        self.wait_til_elements_avail(self.tools_elements.device_diag_list, 60)
        self.enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)

        # Verify if AP exists and selected
        assert self.devices.search_ap_serial(ap_sn) == True, "Not able to find the ap serial " + ap_sn
        assert self.devices.select_ap(ap_sn) == 1, "Not able to select an ap " + ap_sn

        if mode == "online":
            self.click_til_element_avail(self.tools_elements.get_device_diag_btn())
            self.click_til_element_avail(self.tools_elements.get_device_diag_ping_btn1())

            # Ping and verify
            self.wait_til_elements_avail(self.tools_elements.device_diag_ping_txt_area, 60)
            text_content = self.tools_elements.get_device_diag_ping_txt_area().text
            self.utils.print_info(" Dianostic content : " + text_content)
            assert "ping statistics" in text_content, "check1 fails"
            assert "packets transmitted" in text_content, "check2 fails"
            assert "packet loss" in text_content, "check3 fails"
            assert len(text_content) > 100, "check4 fails"
            self.click_til_element_avail(self.tools_elements.get_device_diag_ping_close_dlg())
        else:
            button_status = self.web.get_element(self.tools_elements.device_diag_btn)
            assert button_status.is_enabled() != 1, "Device dialog button should be disabled"
            self.cli.capwap_ap_on_off(ap_ip, ap_usr, ap_pass, "on")

    def utility_vlan_probe(self, mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name):
        """ Prequis: AP should be onboared
            Verification of visibility of client information by selecting an AP
            :param mode     : online or offline
            :param ap_ip    : ap ip
            :param ap_usr   : ap login
            :param ap_pass  : ap password
            :param ap_sn    : ap serial number
            :param ap_name  : ap name
            :return: None   :
        usage:
             utility_vlan_probe  online   ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
             utility_vlan_probe  offline  ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
        """

        # Navigate to the VLAN Probe
        self.utils.print_info("utility VLAN probe")
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.click_til_element_avail(self.tools_elements.get_vlan_probe_link())
        self.wait_til_elements_avail(self.tools_elements.client_info_list, 60)
        self.enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)

        assert self.devices.search_ap_serial(ap_sn) == True, "Not able to find the ap serial " + ap_sn
        assert self.devices.select_ap(ap_sn) == 1, "Not able to select an ap " + ap_sn

        # Verify a vlan
        if mode == "online":  # device must be onboarded
            self.click_til_element_avail(self.tools_elements.get_vlan_probe_btn())
            self.auto_actions.send_keys(self.tools_elements.get_vlan_probe_range_input(), "10")
            self.auto_actions.send_keys(self.tools_elements.get_vlan_probe_timeout_input(), "10")
            self.click_til_element_avail(self.tools_elements.get_vlan_probe_start_btn())  # start vlan
            self.wait_til_elements_avail(self.tools_elements.vlan_probe_start_btn, 180, False)  # wait until vlan completes
            assert "The VLAN Probe is complete!" in self.driver.page_source, "Can not start VLAN"
            self.click_til_element_avail(self.tools_elements.get_vlan_probe_close_diag())
        else:
            button_status = self.web.get_element(self.tools_elements.vlan_probe_btn)
            assert button_status.is_enabled() != 1, "VLAN button should be disabled"
            self.cli.capwap_ap_on_off(ap_ip, ap_usr, ap_pass, "on")

    def utility_get_tech_data(self, mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name):
        """ Prequis: AP should be onboared
            Verification of the downloading of the tech data of an AP
            :param mode     : online or offline
            :param ap_ip    : ap ip
            :param ap_usr   : ap login
            :param ap_pass  : ap password
            :param ap_sn    : ap serial number
            :param ap_name  : ap name
            :return: None   :
        usage:
            utility_get_tech_data  online   ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
            utility_get_tech_data  offline  ${AP1_IP}  ${AP1_USERNAME}  ${AP1_PASSWORD}  ${AP1_SERIAL}  ${AP1_NAME}
        """

        # Navigate to the VLAN Probe
        self.utils.print_info("utility get tech data")
        self.navigator.navigate_to_tools_page()
        self.navigator.navigate_tool_utility()
        self.click_til_element_avail(self.tools_elements.get_tech_data_link())
        self.wait_til_elements_avail(self.tools_elements.client_info_list)
        self.enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)

        assert self.devices.search_ap_serial(ap_sn) == True, "Not able to find the ap serial " + ap_sn
        assert self.devices.select_ap(ap_sn) == 1, "Not able to select an ap " + ap_sn

        # Verify a download
        if mode == "online":  # device must be onboarded
            self.click_til_element_avail(self.tools_elements.get_tech_data_btn())
            self.click_til_element_avail(self.tools_elements.get_tech_data_yes_btn())
            self.wait_til_elements_avail(self.tools_elements.tech_data_download_btn, 60)
            assert "Tech Data has been retrieved successfully" in self.driver.page_source, "Not able to retrieve data"
            self.click_til_element_avail(self.tools_elements.get_tech_data_download_btn())
            button_status = self.web.get_element(self.tools_elements.tech_data_download_btn)
            assert button_status == None, "Downloading does not happen"

        else:
            button_status = self.web.get_element(self.tools_elements.tech_data_btn)
            assert button_status.is_enabled() != 1, "tech data button should be disabled"
            self.enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)

    def get_value_in_tbl(self, grids, field):
        """

            Get value from table list
            :param grids    : list of rows in table
            :param field    : a column / cell
            :return         : true / false
        usage:
            get_value_in_tbl(grid1, column)
        """
        rows = self.web.get_elements(grids)
        for row in rows:
            if field == row.text:
                return 1
        self.utils.print_info("Not able to find the item in list" + field)
        return -1

    def wait_til_elements_avail(self, locator, seconds=60, elements=True):
        """ wait until elements or element is present. If it is a table, there is a least one row
            :param locator    : element's locator
            :param seconds    : number of seconds to wait
            :param true if element is a grid, false if element is not a grid
            :return:  true / false
        usage:
            self.wait_til_elements_avail(self.tool_utils.client_info_list, False)
        """
        self.utils.print_info("wait_until_appears")
        while seconds > 0:
            time.sleep(5)
            if elements:
                self.utils.print_info("get elements")
                rows = self.web.get_elements(locator)
                if len(rows) > 0:
                    return 1
            else:
                self.utils.print_info("get element")
                element = self.web.get_element(locator)
                if element.is_enabled() and element.is_displayed():
                    return 1
            seconds = seconds - 5
        sleep(5)
        return -1

    def wait_til_ap_change_status(self, ap_sn, ap_name, seconds, exp_status):
        """ Wait until a device is connected or disconnected
            :param ap_sn      : ap serial number
            :param ap_name    : ap name
            :param seconds    : number of seconds for waiting
            :param exp_status : expected either connected or disconnected
            :return:  true / false
        usage:
            self.wait_til_ap_change_status(ap_sn, ap_name, 180, "green")
        """
        while seconds > 0:
            time.sleep(5)
            cur_ap_status = self.devices.get_ap_status(ap_sn, ap_name)
            self.utils.print_info("Current Status : " + str(cur_ap_status) + ' and expected staus: ' + str(exp_status))
            if cur_ap_status == "green" and exp_status == "green":
                self.utils.print_info("AP is online")
                return 1
            elif cur_ap_status != "green" and exp_status == "red":
                return 1
            seconds = seconds - 5
        return -1

    def enable_disable_device(self, mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name):
        """
            Enable / disable a capwap device
            :param ap_sn      : ap serial number
            :param ap_name    : ap name
            :param seconds    : number of seconds for waiting
            :param exp_status : expected status either connected or disconnected
            :return:  true / false
        usage:
            self.wait_til_ap_change_status(ap_sn, ap_name, 180, "green")
        """
        if mode == "online":
            self.cli.capwap_ap_on_off(ap_ip, ap_usr, ap_pass, "on")
            self.wait_til_ap_change_status(ap_sn, ap_name, 180, "green")
        else:
            self.cli.capwap_ap_on_off(ap_ip, ap_usr, ap_pass, "off")
            self.wait_til_ap_change_status(ap_sn, ap_name, 180, "red")

    def click_til_element_avail(self, element, seconds=30):
        """ Click on a webelement until element is ready
            Enable an ap device  connected or disconnected
            :param element      : Web Element
            :param seconds      : a duration of waited time
            :return:  None
        usage:
            self.click_til_element_avail(self.tool_utils.get_tech_data_btn())
        """
        while seconds > 0:
            if element.is_enabled() and element.is_displayed():
                sleep(3)
                self.auto_actions.click(element)
                return 1
            seconds = seconds - 3
        self.builtin.fail("Not able to click " + element.text)