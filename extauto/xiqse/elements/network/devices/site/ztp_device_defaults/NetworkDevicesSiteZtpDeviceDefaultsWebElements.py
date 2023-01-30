from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.devices.site.ztp_device_defaults.NetworkDevicesSiteZtpDeviceDefaultsWebElementsDefinitions import NetworkDevicesSiteZtpDeviceDefaultsWebElementsDefinitions


class NetworkDevicesSiteZtpDeviceDefaultsWebElements(NetworkDevicesSiteZtpDeviceDefaultsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Basic Management section
    def get_use_discovered_drop_down(self):
        """
        :return: Use Discovered field element
        """
        return self.weh.get_element(self.use_discovered_drop_down)

    def get_subnet_address_field(self):
        """
        :return: Subnet Address field element
        """
        return self.weh.get_element(self.subnet_address_field)

    def get_starting_ip_address_field(self):
        """
        :return: Starting IP Address field element
        """
        return self.weh.get_element(self.starting_ip_address_field)

    def get_ending_ip_address_field(self):
        """
        :return: Ending IP Address field element
        """
        return self.weh.get_element(self.ending_ip_address_field)

    def get_gateway_address_field(self):
        """
        :return: Gateway Address field element
        """
        return self.weh.get_element(self.gateway_address_field)

    def get_management_interface_drop_down(self):
        """
        :return: Management Interface field element
        """
        return self.weh.get_element(self.management_interface_drop_down)

    def get_cli_recovery_mode_only_checkbox(self):
        """
        :return: CLI Recovery Mode Only field element
        """
        return self.weh.get_element(self.cli_recovery_mode_only_checkbox)

    def get_domain_name_field(self):
        """
        :return: Domain Name field element
        """
        return self.weh.get_element(self.domain_name_field)

    def get_dns_server_field(self):
        """
        :return: DNS Server field element
        """
        return self.weh.get_element(self.dns_server_field)

    def get_dns_server_two_field(self):
        """
        :return: DNS Server 2 field element
        """
        return self.weh.get_element(self.dns_server_two_field)

    def get_dns_server_three_field(self):
        """
        :return: DNS Server 3 field element
        """
        return self.weh.get_element(self.dns_server_three_field)

    def get_dns_search_suffix_field(self):
        """
        :return: DNS Search Suffix field element
        """
        return self.weh.get_element(self.dns_search_suffix_field)

    def get_ntp_server_field(self):
        """
        :return: NTP Server field element
        """
        return self.weh.get_element(self.ntp_server_field)

    def get_ntp_server_two_field(self):
        """
        :return: NTP Server 2 field element
        """
        return self.weh.get_element(self.ntp_server_two_field)

    def get_system_contact_field(self):
        """
        :return: System Contact field element
        """
        return self.weh.get_element(self.system_contact_field)

    def get_system_location_field(self):
        """
        :return: System Location field element
        """
        return self.weh.get_element(self.system_location_field)

    def get_admin_profile_drop_down(self):
        """
        :return: Admin Profile field element
        """
        return self.weh.get_element(self.admin_profile_drop_down)

    def get_poll_group_drop_down(self):
        """
        :return: Poll Group field element
        """
        return self.weh.get_element(self.poll_group_drop_down)

    def get_poll_type_drop_down(self):
        """
        :return: Poll Type field element
        """
        return self.weh.get_element(self.poll_type_drop_down)

    def get_site_precedence_drop_down(self):
        """
        :return: Site Assignment Precedence field element
        """
        return self.weh.get_element(self.site_precedence_drop_down)

    # Configuration/Upgrade section
    # 2021-06-17: need to add combobox fields to configure date/time/offset
    def get_configuration_updates_drop_down(self):
        """
        :return: Configuration Updates field element
        """
        return self.weh.get_element(self.configuration_updates_drop_down)

    def get_configuration_updates_date_drop_down(self):
        """
        :return: Configuration Updates > Update Date field element
        """
        return self.weh.get_element(self.configuration_updates_date_drop_down)

    def get_configuration_updates_time_drop_down(self):
        """
        :return: Configuration Updates > Update Time field element
        """
        return self.weh.get_element(self.configuration_updates_time_drop_down)

    def get_configuration_updates_offset_drop_down(self):
        """
        :return: Configuration Updates > Update UTC Offset field element
        """
        return self.weh.get_element(self.configuration_updates_offset_drop_down)

    def get_firmware_upgrades_drop_down(self):
        """
        :return: Firmware Upgrades field element
        """
        return self.weh.get_element(self.firmware_upgrades_drop_down)

    def get_firmware_upgrades_date_drop_down(self):
        """
        :return: Firmware Upgrades > Update Date field element
        """
        return self.weh.get_element(self.firmware_upgrades_date_drop_down)

    def get_firmware_upgrades_time_drop_down(self):
        """
        :return: Firmware Upgrades > Update Time field element
        """
        return self.weh.get_element(self.firmware_upgrades_time_drop_down)

    def get_firmware_upgrades_offset_drop_down(self):
        """
        :return: Firmware Upgrades > Update UTC Offset field element
        """
        return self.weh.get_element(self.firmware_upgrades_offset_drop_down)

    # Device Protocols section
    def get_device_protocols_telnet_checkbox(self):
        """
        :return: Telnet field element
        """
        return self.weh.get_element(self.device_protocols_telnet_checkbox)

    def get_device_protocols_ssh_checkbox(self):
        """
        :return: SSH field element
        """
        return self.weh.get_element(self.device_protocols_ssh_checkbox)

    def get_device_protocols_http_checkbox(self):
        """
        :return: HTTP field element
        """
        return self.weh.get_element(self.device_protocols_http_checkbox)

    def get_device_protocols_https_checkbox(self):
        """
        :return: HTTPS field element
        """
        return self.weh.get_element(self.device_protocols_https_checkbox)

    def get_device_protocols_ftp_checkbox(self):
        """
        :return: FTP field element
        """
        return self.weh.get_element(self.device_protocols_ftp_checkbox)

    def get_device_protocols_snmp_checkbox(self):
        """
        :return: SNMP field element
        """
        return self.weh.get_element(self.device_protocols_snmp_checkbox)

    def get_device_protocols_lacp_checkbox(self):
        """
        :return: LACP field element
        """
        return self.weh.get_element(self.device_protocols_lacp_checkbox)

    def get_device_protocols_lldp_checkbox(self):
        """
        :return: LLDP field element
        """
        return self.weh.get_element(self.device_protocols_lldp_checkbox)

    def get_device_protocols_mvrp_checkbox(self):
        """
        :return: MVRP field element
        """
        return self.weh.get_element(self.device_protocols_mvrp_checkbox)

    def get_device_protocols_mstp_checkbox(self):
        """
        :return: MSTP field element
        """
        return self.weh.get_element(self.device_protocols_mstp_checkbox)

    def get_device_protocols_poe_checkbox(self):
        """
        :return: POE field element
        """
        return self.weh.get_element(self.device_protocols_poe_checkbox)

    def get_device_protocols_vxlan_checkbox(self):
        """
        :return: VXLAN field element
        """
        return self.weh.get_element(self.device_protocols_vxlan_checkbox)

    # Global IP to Site Mapping section
    def get_global_ip_to_site_mapping_table(self):
        """
        :return: Global IP to Site Mapping grid
        """
        return self.weh.get_element(self.global_ip_to_site_mapping_grid)
