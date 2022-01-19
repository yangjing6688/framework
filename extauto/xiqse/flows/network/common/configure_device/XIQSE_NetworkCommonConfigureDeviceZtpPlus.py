# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.common.configure_device.NetworkCommonConfigureDeviceZtpPlusWebElements import NetworkCommonConfigureDeviceZtpPlusWebElements
from xiqse.flows.common.XIQSE_CommonField import XIQSE_CommonField


class XIQSE_NetworkCommonConfigureDeviceZtpPlus(NetworkCommonConfigureDeviceZtpPlusWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.com_field = XIQSE_CommonField()

    # ZTP+ DEVICE SETTINGS TAB
    def xiqse_configure_device_dialog_ztp_verify_serial_number(self, serial_number):
        """
         - This keyword verifies the Serial Number value in the Configure Device dialog (ZTP+ Device Settings tab).
         - It assumes the dialog is already open.
         - Keyword Usage
          - ``XIQSE Configure Device Dialog Ztp Verify Serial Number  Serial Number``
        :param serial_number: value to test in the Serial Number field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1
        self.utils.print_info(f"This is the provided Serial Number value: {serial_number}")
        serial_number_field = self.get_serial_number_field()
        if serial_number_field:
            readonly = self.com_field.xiqse_is_field_readonly(serial_number_field)
            if readonly:
                self.utils.print_info(f"The Serial Number field is readonly.")
                serial_number_value = serial_number_field.get_attribute("value")
                if serial_number_value:
                    if serial_number_value.lower() == serial_number.lower():
                        self.utils.print_info(f"The Serial Number {serial_number} does match the current value {serial_number_value}.")
                        return ret_val
                    else:
                        self.utils.print_info(f"The Serial Number {serial_number} does not match the current value {serial_number_value}.")
                        ret_val = -1
                        return ret_val
                else:
                    self.utils.print_info(f"Could not obtain the Serial Number field value in ZTP+ Device Settings.")
                    ret_val = -1
            else:
                self.utils.print_info(f"The Serial Number field should be readonly.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the IP Address / Subnet field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_use_discovered(self, use_discovered):
        """
         - This keyword sets the Use Discovered value in the Configure Device dialog (ZTP+ Device Settings tab).
         - It assumes the dialog is already open.
         - Keyword Usage
          - ``XIQSE Configure Device Dialog Ztp Set Use Discovered  Disabled``
          - ``XIQSE Configure Device Dialog Ztp Set Use Discovered  IP``
          - ``XIQSE Configure Device Dialog Ztp Set Use Discovered  IP and Management Interface``
          - ``XIQSE Configure Device Dialog Ztp Set Use Discovered  Management Interface``
        :param use_discovered: value to select for the Use Discovered field
         (Disabled, IP, IP and Management Interface, Management Interface)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Use Discovered value: {use_discovered}")
        the_field = self.get_use_discovered_dropdown()
        if the_field:
            self.utils.print_info(f"Clicking the Use Discovered drop down to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Use Discovered items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, use_discovered):
                    self.utils.print_info(f"Selected {use_discovered} in the Use Discovered dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {use_discovered} in the Use Discovered dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info(f"Unable to find the Use Discovered option {use_discovered}")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Use Discovered field in ZTP+ Device Settings")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_ip_address_and_subnet(self, ip_address):
        """
          - This keyword sets the IP Address / Subnet value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - If only the IP Address is provided, then XIQ-SE defaults the Subnet value to /24
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set Starting IP Address  ip_address``
         :param ip_address: value to set for the IP Address/Subnet Mask
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided IP Address/Subnet value: {ip_address}")
        ip_address_field = self.get_ip_address_subnet_field()
        if ip_address_field:
            disabled = self.com_field.xiqse_is_field_disabled(ip_address_field)
            if disabled:
                self.utils.print_info(f"The IP Address / Subnet field is disabled.")
            else:
                self.auto_actions.send_keys(ip_address_field, ip_address)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the IP Address / Subnet field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_gateway_address(self, gateway_address):
        """
          - This keyword sets the Gateway Address value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set Gateway Address  gateway_address``
         :param gateway_address: value to set for the Gateway Address
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Gateway Address value: {gateway_address}")
        gateway_address_field = self.get_gateway_address_field()
        if gateway_address_field:
            disabled = self.com_field.xiqse_is_field_disabled(gateway_address_field)
            if disabled:
                self.utils.print_info(f"The Gateway Address field is disabled.")
            else:
                self.auto_actions.send_keys(gateway_address_field, gateway_address)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the Gateway Address field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_management_interface(self, management_interface):
        """
         - This keyword sets the Management Interface value in the Configure Device dialog (ZTP+ Device Settings tab).
         - It assumes the view is already open.
         - Keyword Usage
          - ``XIQSE Configure Device Dialog Ztp Set Management Interface  Out-Of-Band``
          - ``XIQSE Configure Device Dialog Ztp Set Management Interface  Default``
          - ``XIQSE Configure Device Dialog Ztp Set Management Interface  <VlAN-NAME>``
        :param management_interface: value to select for the Use Discovered field
               (Out-Of-Band || Default || VlAN-NAME)
        :return: 1 if action was successful (or the field is disabled), else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Management Interface value: {management_interface}")
        the_field = self.get_management_interface_dropdown()
        if the_field:
            disabled = self.com_field.xiqse_is_field_disabled(the_field)
            if disabled:
                self.utils.print_info(f"The Management Interface field is disabled.")
                ret_val = 1
            else:
                self.utils.print_info(f"Clicking the Management Interface drop down to expand the choices")
                self.auto_actions.click(the_field)

                # Obtain the dropdown items
                the_id = self.view_el.get_dropdown_id(the_field)
                self.utils.print_debug(f"Got dropdown ID {the_id}")
                the_items = self.view_el.get_div_dropdown_items(the_id)
                if the_items:
                    self.utils.print_debug(f"Management Interface items count is {len(the_items)}")
                    if self.auto_actions.select_drop_down_options(the_items, management_interface):
                        self.utils.print_info(f"Selected {management_interface} in the Management Interface dropdown")
                        ret_val = 1
                    else:
                        self.utils.print_info(
                            f"Unable to select {management_interface} in the Management Interface dropdown")
                        self.screen.save_screen_shot()

                        # Click the dropdown again to close it
                        self.auto_actions.click(the_field)
                else:
                    self.utils.print_info(f"Unable to find the Management Interface option {management_interface}")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Management Interface field in ZTP+ Device Settings")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_cli_recovery_mode_only_checkbox(self, state="Disable"):
        """
             - This keyword sets the Basic Management CLI Recovery Mode Only value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Cli Recovery Mode Only Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Cli Recovery Mode Only Checkbox  Disable``
            :param state: value to set for the Basic Management CLI Recovery Mode Only checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Basic Management 'CLI Recovery Mode Only' value: {state}")
        checkbox = self.get_cli_recovery_mode_only_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling the Basic Management 'CLI Recovery Mode Only' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling the Basic Management 'CLI Recovery Mode Only' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Basic Management 'CLI Recovery Mode Only' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Basic Management 'CLI Recovery Mode Only' checkbox field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_domain_name(self, domain_name):
        """
          - This keyword sets the Domain Name value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set Domain Name  domain_name``
         :param domain_name: value to set for the Domain Name
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Domain Name value: {domain_name}")
        domain_name_field = self.get_domain_name_field()
        if domain_name_field:
            disabled = self.com_field.xiqse_is_field_disabled(domain_name_field)
            if disabled:
                self.utils.print_info(f"The Domain Name field is disabled.")
            else:
                self.auto_actions.send_keys(domain_name_field, domain_name)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the Domain Name field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_dns_server(self, dns_server):
        """
          - This keyword sets the DNS Server value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set DNS Server  dns_server``
         :param dns_server: value to set for the DNS Server
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided DNS Server value: {dns_server}")
        dns_server_field = self.get_dns_server_field()
        if dns_server_field:
            disabled = self.com_field.xiqse_is_field_disabled(dns_server_field)
            if disabled:
                self.utils.print_info(f"The DNS Server field is disabled.")
            else:
                self.auto_actions.send_keys(dns_server_field, dns_server)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the DNS Server field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_dns_server_two(self, dns_server):
        """
          - This keyword sets the DNS Server 2 value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set DNS Server Two  dns_server``
         :param dns_server: value to set for the DNS Server 2
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided DNS Server 2 value: {dns_server}")
        dns_server_two_field = self.get_dns_server_two_field()
        if dns_server_two_field:
            disabled = self.com_field.xiqse_is_field_disabled(dns_server_two_field)
            if disabled:
                self.utils.print_info(f"The DNS Server 2 field is disabled.")
            else:
                self.auto_actions.send_keys(dns_server_two_field, dns_server)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the DNS Server 2 field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_dns_server_three(self, dns_server):
        """
          - This keyword sets the DNS Server 3 value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set DNS Server Three  dns_server``
         :param dns_server: value to set for the DNS Server 3
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided DNS Server 3 value: {dns_server}")
        dns_server_three_field = self.get_dns_server_three_field()
        if dns_server_three_field:
            disabled = self.com_field.xiqse_is_field_disabled(dns_server_three_field)
            if disabled:
                self.utils.print_info(f"The DNS Server 3 field is disabled.")
            else:
                self.auto_actions.send_keys(dns_server_three_field, dns_server)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the DNS Server 3 field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_dns_search_suffix(self, dns_search_suffix):
        """
          - This keyword sets the DNS Search Suffix value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set DNS Search Suffix  dns_search_suffix``
         :param dns_search_suffix: value to set for the DNS Search Suffix
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided DNS Search Suffix value: {dns_search_suffix}")
        dns_search_suffix_field = self.get_dns_search_suffix_field()
        if dns_search_suffix_field:
            disabled = self.com_field.xiqse_is_field_disabled(dns_search_suffix_field)
            if disabled:
                self.utils.print_info(f"The DNS Search Suffix field is disabled.")
            else:
                self.auto_actions.send_keys(dns_search_suffix_field, dns_search_suffix)
                sleep(2)
        else:
            self.utils.print_info(f"Could not find the DNS Search Suffix field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_ntp_server(self, ntp_server):
        """
          - This keyword sets the NTP Server value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set NTP Server  ntp_server``
         :param ntp_server: value to set for the NTP Server
         :return: 1 if action was successful, else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided NTP Server value: {ntp_server}")
        ntp_server_field = self.get_ntp_server_field()
        if ntp_server_field:
            self.auto_actions.send_keys(ntp_server_field, ntp_server)
            sleep(2)
        else:
            self.utils.print_info(f"Could not find the NTP Server field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_ntp_server_two(self, ntp_server):
        """
          - This keyword sets the NTP Server 2 value in the Configure Device dialog (ZTP+ Device Settings tab).
          - It assumes the view is already open.
          - Keyword Usage
           - ``XIQSE Configure Device Dialog Ztp Set NTP Server 2  ntp_server``
         :param ntp_server: value to set for the NTP Server 2
         :return: 1 if action was successful, else -1
         """
        ret_val = 1
        self.utils.print_debug(f"This is the provided NTP Server 2 value: {ntp_server}")
        ntp_server_two_field = self.get_ntp_server_two_field()
        if ntp_server_two_field:
            self.auto_actions.send_keys(ntp_server_two_field, ntp_server)
            sleep(2)
        else:
            self.utils.print_info(f"Could not find the NTP Server 2 field in ZTP+ Device Settings")
            ret_val = -1

        return ret_val

    # Configuration/Upgrades section
    # 2021-07-01 - Need to add keywords

    # Device Protocols section
    def xiqse_configure_device_dialog_ztp_set_device_protocols_telnet_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols Telnet value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Telnet Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Telnet Checkbox  Disable``
            :param state: value to set for the Device Protocols Telnet checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'Telnet' value: {state}")
        checkbox = self.get_device_protocols_telnet_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'Telnet' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'Telnet' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'Telnet' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'Telnet' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_ssh_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols SSH value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Ssh Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Ssh Checkbox  Disable``
            :param state: value to set for the Device Protocols SSH checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'SSH' value: {state}")
        checkbox = self.get_device_protocols_ssh_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'SSH' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'SSH' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'SSH' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'SSH' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_http_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols HTTP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Http Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Http Checkbox  Disable``
            :param state: value to set for the Device Protocols HTTP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'HTTP' value: {state}")
        checkbox = self.get_device_protocols_http_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'HTTP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'HTTP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'HTTP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'HTTP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_https_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols HTTPS value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Https Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Https Checkbox  Disable``
            :param state: value to set for the Device Protocols HTTPS checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'HTTPS' value: {state}")
        checkbox = self.get_device_protocols_https_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'HTTPS' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'HTTPS' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'HTTPS' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'HTTPS' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_ftp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols FTP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Ftp Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Ftp Checkbox  Disable``
            :param state: value to set for the Device Protocols FTP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'FTP' value: {state}")
        checkbox = self.get_device_protocols_ftp_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'FTP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'FTP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'FTP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'FTP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_snmp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols SNMP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Snmp Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Snmp Checkbox  Disable``
            :param state: value to set for the Device Protocols SNMP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'SNMP' value: {state}")
        checkbox = self.get_device_protocols_snmp_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'SNMP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'SNMP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'SNMP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'SNMP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_lacp_checkbox(self, state="Disable"):
        """
             - This keyword sets the Device Protocols LACP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Lacp checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Lacp checkbox  Disable``
            :param state: value to set for the Device Protocols LACP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'LACP' value: {state}")
        checkbox = self.get_device_protocols_lacp_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'LACP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'LACP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'LACP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'LACP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_lldp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols LLDP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Lldp Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Lldp Checkbox  Disable``
            :param state: value to set for the Device Protocols LLDP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'LLDP' value: {state}")
        checkbox = self.get_device_protocols_lldp_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'LLDP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'LLDP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'LLDP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'LLDP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_mvrp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols MVRP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Mvrp Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Mvrp Checkbox  Disable``
            :param state: value to set for the Device Protocols MVRP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'MVRP' value: {state}")
        checkbox = self.get_device_protocols_mvrp_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'MVRP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'MVRP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'MVRP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'MVRP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_mstp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols MSTP value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Mstp Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Mstp Checkbox  Disable``
            :param state: value to set for the Device Protocols MSTP checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'MSTP' value: {state}")
        checkbox = self.get_device_protocols_mstp_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'MSTP' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'MSTP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'MSTP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'MSTP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_poe_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols POE value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Poe Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Poe Checkbox  Disable``
            :param state: value to set for the Device Protocols POE checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'POE' value: {state}")
        checkbox = self.get_device_protocols_poe_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'POE' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'POE' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'POE' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'POE' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    def xiqse_configure_device_dialog_ztp_set_device_protocols_vxlan_checkbox(self, state="Disable"):
        """
             - This keyword sets the Device Protocols VXLAN value in the Configure Device dialog (ZTP+ Device Settings tab).
             - It assumes the view is already open.
             - Keyword Usage
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Vxlan Checkbox  Enable``
              - ``XIQSE Configure Device Dialog Ztp Set Device Protocols Vxlan Checkbox  Disable``
            :param state: value to set for the Device Protocols VXLAN checkbox (Enable || Disable)
            :return: 1 if action was successful, else -1
            """
        ret_val = 1
        self.utils.print_debug(f"This is the provided Device Protocols 'VXLAN' value: {state}")
        checkbox = self.get_device_protocols_vxlan_checkbox()
        if checkbox:
            if state == "Enable":
                self.utils.print_info("Enabling Device Protocols 'VXLAN' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                sleep(2)
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'VXLAN' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                sleep(2)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'VXLAN' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'VXLAN' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        return ret_val

    # COMMON FUNCTION TO TEST IF THE FIELD IS DISABLED
    def orig_xiqse_is_field_disabled(self, field_element):
        """
         - This keyword tests if the field is disabled.
         - It assumes the view is already open.
         - Keyword Usage
          - ``XIQSE is Field Disabled  field``
        :param field_element: field
        :return: True if disabled else None
        """
        if field_element:
            field_disabled = field_element.get_attribute("aria-disabled")
            self.utils.print_debug(f"Field Disabled Value: '{field_disabled}")
            if field_disabled == 'true':
                return True

    # COMMON FUNCTION TO TEST IF THE FIELD IS READ-ONLY
    def orig_xiqse_is_field_readonly(self, field_element):
        """
         - This keyword tests if the field is read only.
         - It assumes the view is already open.
         - Keyword Usage
          - ``XIQSE is Field Readonly  field``
        :param field_element: field
        :return: True if readonly else None
        """
        if field_element:
            field_readonly = field_element.get_attribute("aria-readonly")
            self.utils.print_debug(f"Field Read Only Value: '{field_readonly}")
            if field_readonly == 'true':
                return True
