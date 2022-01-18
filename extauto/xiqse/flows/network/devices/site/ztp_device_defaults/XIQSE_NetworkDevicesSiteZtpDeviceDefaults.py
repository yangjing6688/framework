# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.site.ztp_device_defaults.NetworkDevicesSiteZtpDeviceDefaultsWebElements import NetworkDevicesSiteZtpDeviceDefaultsWebElements
from xiqse.flows.common.XIQSE_CommonField import XIQSE_CommonField


class XIQSE_NetworkDevicesSiteZtpDeviceDefaults(NetworkDevicesSiteZtpDeviceDefaultsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.com_field = XIQSE_CommonField()

    def xiqse_site_ztp_set_use_discovered(self, use_discovered):
        """
         - This keyword sets the Use Discovered value in the Site > ZTP+ Device Defaults tab
         - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
         - Keyword Usage
          - ``XIQSE Site Ztp Set Use Discovered  Disabled``
          - ``XIQSE Site Ztp Set Use Discovered  IP``
          - ``XIQSE Site Ztp Set Use Discovered  IP and Management Interface``
          - ``XIQSE Site Ztp Set Use Discovered  Management Interface``
        :param use_discovered: value to select for the Use Discovered field
         (Disabled, IP, IP and Management Interface, Management Interface)
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Use Discovered value: {use_discovered}")
        the_field = self.get_use_discovered_drop_down()
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
            self.utils.print_info(f"Could not find the Use Discovered field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_subnet_address(self, subnet_address):
        """
          - This keyword sets the Subnet Address value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set Subnet Address  Subnet_Address``
         :param subnet_address: value to set for the Subnet Address
         :return: 1 if action was successful, else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided Subnet Address value: {subnet_address}")
        subnet_address_field = self.get_subnet_address_field()
        if subnet_address_field:
            self.auto_actions.send_keys(subnet_address_field, subnet_address)
        else:
            self.utils.print_info(f"Could not find the Subnet Address field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_starting_ip_address(self, starting_ip_address):
        """
          - This keyword sets the Starting IP Address value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set Starting IP Address  starting_ip_address``
         :param starting_ip_address: value to set for the Starting IP Address
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided Starting IP Address value: {starting_ip_address}")
        starting_ip_address_field = self.get_starting_ip_address_field()
        if starting_ip_address_field:
            disabled = self.com_field.xiqse_is_field_disabled(starting_ip_address_field)
            if disabled:
                self.utils.print_info(f"The Starting IP Address field is disabled.")
            else:
                self.auto_actions.send_keys(starting_ip_address_field, starting_ip_address)
        else:
            self.utils.print_info(f"Could not find the Staring IP Address field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_ending_ip_address(self, ending_ip_address):
        """
          - This keyword sets the Ending IP Address value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set Ending IP Address  ending_ip_address``
         :param ending_ip_address: value to set for the Ending IP Address
         :return: 1 if action was successful (or the field is disabled), else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided Starting IP Address value: {ending_ip_address}")
        ending_ip_address_field = self.get_ending_ip_address_field()
        if ending_ip_address_field:
            disabled = self.com_field.xiqse_is_field_disabled(ending_ip_address_field)
            if disabled:
                self.utils.print_info(f"The Ending IP Address field is disabled.")
            else:
                self.auto_actions.send_keys(ending_ip_address_field, ending_ip_address)
        else:
            self.utils.print_info(f"Could not find the Ending IP Address field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_gateway_address(self, gateway_address):
        """
          - This keyword sets the Gateway Address value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set Gateway Address  gateway_address``
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
        else:
            self.utils.print_info(f"Could not find the Gateway Address field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_management_interface(self, management_interface):
        """
         - This keyword sets the Management Interface value in the Site > ZTP+ Device Defaults tab.
         - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
         - Keyword Usage
          - ``XIQSE Site Ztp Set Management Interface  Out-Of-Band``
          - ``XIQSE Site Ztp Set Management Interface  Default``
          - ``XIQSE Site Ztp Set Management Interface  <VlAN-NAME>``
        :param management_interface: value to select for the Use Discovered field
               (Out-Of-Band || Default || VlAN-NAME)
        :return: 1 if action was successful (or the field is disabled), else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Management Interface value: {management_interface}")
        the_field = self.get_management_interface_drop_down()
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
                        self.utils.print_info(f"Unable to select {management_interface} in the Management Interface dropdown")
                        self.screen.save_screen_shot()

                        # Click the dropdown again to close it
                        self.auto_actions.click(the_field)
                else:
                    self.utils.print_info(f"Unable to find the Management Interface option {management_interface}")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Management Interface field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_cli_recovery_mode_only_checkbox(self, state="Disable"):
        """
             - This keyword sets the Basic Management CLI Recovery Mode Only value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Note: This field will be enabled when the Poll Type is set to ZTP+.
             -
             - Keyword Usage
              - ``XIQSE Site Ztp Set Cli Recovery Mode Only Checkbox  Enable``
              - ``XIQSE Site Ztp Set Cli Recovery Mode Only Checkbox  Disable``
            :param state: value to set for the Basic Management CLI Recovery Mode Only checkbox (Enable || Disable)
            :return: 1 if action was successful (or the field is disabled), else -1
            """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Basic Management 'CLI Recovery Mode Only' value: {state}")
        checkbox = self.get_cli_recovery_mode_only_checkbox()
        if checkbox:
            disabled = self.com_field.xiqse_is_field_disabled(checkbox)
            if disabled:
                self.utils.print_info(f"The CLI Recovery Mode Only field is disabled.")
                ret_val = 1
            if state == "Enable":
                self.utils.print_info("Enabling the Basic Management 'CLI Recovery Mode Only' checkbox")
                self.auto_actions.enable_check_box(checkbox)
                ret_val = 1
            elif state == "Disable":
                self.utils.print_info("Disabling the Basic Management 'CLI Recovery Mode Only' checkbox")
                self.auto_actions.disable_check_box(checkbox)
                ret_val = 1
            else:
                self.utils.print_info(f"Invalid value provided for the Basic Management 'CLI Recovery Mode Only' checkbox.")
        else:
            self.utils.print_info(f"Could not find the Basic Management 'CLI Recovery Mode Only' checkbox in ZTP+ Device Defaults")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_domain_name(self, domain_name):
        """
          - This keyword sets the Domain Name value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set Domain Name  domain_name``
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
        else:
            self.utils.print_info(f"Could not find the Domain Name field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_dns_server(self, dns_server):
        """
          - This keyword sets the DNS Server value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set DNS Server  dns_server``
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
        else:
            self.utils.print_info(f"Could not find the DNS Server field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_dns_server_two(self, dns_server):
        """
          - This keyword sets the DNS Server 2 value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set DNS Server Two  dns_server``
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
        else:
            self.utils.print_info(f"Could not find the DNS Server 2 field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_dns_server_three(self, dns_server):
        """
          - This keyword sets the DNS Server 3 value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set DNS Server Three  dns_server``
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
        else:
            self.utils.print_info(f"Could not find the DNS Server 3 field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_dns_search_suffix(self, dns_search_suffix):
        """
          - This keyword sets the DNS Search Suffix value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set DNS Search Suffix  dns_search_suffix``
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
        else:
            self.utils.print_info(f"Could not find the DNS Search Suffix field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_ntp_server(self, ntp_server):
        """
          - This keyword sets the NTP Server value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set NTP Server  ntp_server``
         :param ntp_server: value to set for the NTP Server
         :return: 1 if action was successful, else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided NTP Server value: {ntp_server}")
        ntp_server_field = self.get_ntp_server_field()
        if ntp_server_field:
            self.auto_actions.send_keys(ntp_server_field, ntp_server)
        else:
            self.utils.print_info(f"Could not find the NTP Server field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_ntp_server_two(self, ntp_server):
        """
          - This keyword sets the NTP Server 2 value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set NTP Server 2  ntp_server``
         :param ntp_server: value to set for the NTP Server 2
         :return: 1 if action was successful, else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided NTP Server 2 value: {ntp_server}")
        ntp_server_two_field = self.get_ntp_server_two_field()
        if ntp_server_two_field:
            self.auto_actions.send_keys(ntp_server_two_field, ntp_server)
        else:
            self.utils.print_info(f"Could not find the NTP Server 2 field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_system_contact(self, system_contact):
        """
          - This keyword sets the System Contact value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set System Contact  system_contact``
         :param system_contact: value to set for the System Contact
         :return: 1 if action was successful, else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided System Contact value: {system_contact}")
        system_contact_field = self.get_system_contact_field()
        if system_contact_field:
            self.auto_actions.send_keys(system_contact_field, system_contact)
        else:
            self.utils.print_info(f"Could not find the System Contact field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_system_location(self, system_location):
        """
          - This keyword sets the System Location value in the Site > ZTP+ Device Defaults tab.
          - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
          - Keyword Usage
           - ``XIQSE Site Ztp Set System Location  system_location``
         :param system_location: value to set for the System Location
         :return: 1 if action was successful, else -1
         """
        ret_val = 1

        self.utils.print_debug(f"This is the provided System Location value: {system_location}")
        system_location_field = self.get_system_location_field()
        if system_location_field:
            self.auto_actions.send_keys(system_location_field, system_location)
        else:
            self.utils.print_info(f"Could not find the System Location field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_site_ztp_set_admin_profile(self, admin_profile):
        """
         - This keyword sets the Admin Profile value in the Site > ZTP+ Device Defaults tab.
         - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
         - Keyword Usage
          - ``XIQSE Site Ztp Set Admin Profile  admin_profile``
        :param admin_profile: value to select for the Admin Profile field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Admin Profile value: {admin_profile}")
        the_field = self.get_admin_profile_drop_down()
        if the_field:
            self.utils.print_info(f"Clicking the Admin Profile drop down to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Admin Profile items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, admin_profile):
                    self.utils.print_info(f"Selected {admin_profile} in the Admin Profile dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {admin_profile} in the Admin Profile dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info(f"Unable to find the Admin Profile option {admin_profile}")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Admin Profile field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_poll_group(self, poll_group):
        """
         - This keyword sets the Poll Group value in the Site > ZTP+ Device Defaults tab.
         - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
         - Keyword Usage
          - ``XIQSE Site Ztp Set Poll Group  More Frequent``
          - ``XIQSE Site Ztp Set Poll Group  Default``
          - ``XIQSE Site Ztp Set Poll Group  Less Frequent``
        :param poll_group: value to select for the Poll Group field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Poll Group value: {poll_group}")
        the_field = self.get_poll_group_drop_down()
        if the_field:
            self.utils.print_info(f"Clicking the Poll Group drop down to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Poll Group items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, poll_group):
                    self.utils.print_info(f"Selected {poll_group} in the Poll Group dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(
                        f"Unable to select {poll_group} in the Poll Group dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info(f"Unable to find the Poll Group option {poll_group}")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Poll Group field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_poll_type(self, poll_type):
        """
         - This keyword sets the Poll Type value in the Site > ZTP+ Device Defaults tab.
         - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
         - Keyword Usage
          - ``XIQSE Site Ztp Set Poll Type  Not Polled``
          - ``XIQSE Site Ztp Set Poll Type  Ping``
          - ``XIQSE Site Ztp Set Poll Type  SNMP``
          - ``XIQSE Site Ztp Set Poll Type  Maintenance``
          - ``XIQSE Site Ztp Set Poll Type  ZTP+``
        :param poll_type: value to select for the Poll Type field
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Poll Type value: {poll_type}")
        the_field = self.get_poll_type_drop_down()
        if the_field:
            self.utils.print_info(f"Clicking the Poll Type drop down to expand the choices")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Poll Type items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, poll_type):
                    self.utils.print_info(f"Selected {poll_type} in the Poll Type dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Unable to select {poll_type} in the Poll Type dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info(f"Unable to find the Poll Type option {poll_type}")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Poll Type field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_site_precedence(self, site_precedence):
        """
         - This keyword sets the Site Assignment Precedence value in the Site > ZTP+ Device Defaults tab.
         - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
         - Note: This field is only enabled when the World site is selected.
         - Keyword Usage
          - ``XIQSE Site Ztp Set Site Precedence  IP Range, LLDP``
          - ``XIQSE Site Ztp Set Site Precedence  LLDP, IP Range``
          - ``XIQSE Site Ztp Set Site Precedence  LLDP Only``
          - ``XIQSE Site Ztp Set Site Precedence  IP Range Only``
          - ``XIQSE Site Ztp Set Site Precedence  None``
        :param site_precedence: value to select for the Site Assignment Precedent field
        :return: 1 if action was successful (or the field is disabled), else -1
        """
        ret_val = -1

        self.utils.print_debug(f"This is the provided Site Assignment Precedent value: {site_precedence}")
        the_field = self.get_site_precedence_drop_down()
        if the_field:
            disabled = self.com_field.xiqse_is_field_disabled(the_field)
            if disabled:
                self.utils.print_info(f"The Site Assignment Precedent field is disabled.")
                ret_val = 1
            else:
                self.utils.print_info(f"Clicking the Site Assignment Precedent drop down to expand the choices")
                self.auto_actions.click(the_field)

                # Obtain the dropdown items
                the_id = self.view_el.get_dropdown_id(the_field)
                self.utils.print_debug(f"Got dropdown ID {the_id}")
                the_items = self.view_el.get_list_dropdown_items(the_id)
                if the_items:
                    self.utils.print_debug(f"Site Assignment Precedent items count is {len(the_items)}")
                    if self.auto_actions.select_drop_down_options(the_items, site_precedence):
                        self.utils.print_info(f"Selected {site_precedence} in the Site Assignment Precedent dropdown")
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Unable to select {site_precedence} in the Site Assignment Precedent dropdown")
                        self.screen.save_screen_shot()

                        # Click the dropdown again to close it
                        self.auto_actions.click(the_field)
                else:
                    self.utils.print_info(f"Unable to find the Site Assignment Precedent option {site_precedence}")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
        else:
            self.utils.print_info(f"Could not find the Site Assignment Precedent field in ZTP+ Device Defaults")
            self.screen.save_screen_shot()

        return ret_val

    # Configuration/Upgrade section
    # 2021-07-01 - Need to add keywords

    # Device Protocols section
    def xiqse_site_ztp_set_device_protocols_telnet_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols Telnet value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Telnet Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Telnet Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'Telnet' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'Telnet' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'Telnet' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_ssh_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols SSH value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Ssh Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Ssh Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'SSH' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'SSH' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'SSH' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_http_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols HTTP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Http Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Http Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'HTTP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'HTTP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'HTTP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_https_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols HTTPS value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Https Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Https Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'HTTPS' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'HTTPS' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'HTTPS' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_ftp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols FTP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Ftp Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Ftp Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'FTP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'FTP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'FTP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_snmp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols SNMP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Snmp Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Snmp Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'SNMP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'SNMP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'SNMP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_lacp_checkbox(self, state="Disable"):
        """
             - This keyword sets the Device Protocols LACP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Lacp Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Lacp Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'LACP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'LACP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'LACP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_lldp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols LLDP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Lldp Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Lldp Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'LLDP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'LLDP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'LLDP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_mvrp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols MVRP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Mvrp Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Mvrp Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'MVRP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'MVRP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'MVRP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_mstp_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols MSTP value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Mstp Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Mstp Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'MSTP' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'MSTP' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'MSTP' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_poe_checkbox(self, state="Enable"):
        """
             - This keyword sets the Device Protocols POE value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Poe Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Poe Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'POE' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'POE' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'POE' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_site_ztp_set_device_protocols_vxlan_checkbox(self, state="Disable"):
        """
             - This keyword sets the Device Protocols VXLAN value in the Site > ZTP+ Device Defaults tab.
             - It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.
             - Keyword Usage
              - ``XIQSE Site Ztp Set Device Protocols Vxlan Checkbox  Enable``
              - ``XIQSE Site Ztp Set Device Protocols Vxlan Checkbox  Disable``
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
            elif state == "Disable":
                self.utils.print_info("Disabling Device Protocols 'VXLAN' checkbox")
                self.auto_actions.disable_check_box(checkbox)
            else:
                self.utils.print_info(f"Invalid value provided for the Device Protocols 'VXLAN' checkbox.")
                ret_val = -1
        else:
            self.utils.print_info(f"Could not find the Device Protocols 'VXLAN' checkbox in ZTP+ Device Defaults")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
