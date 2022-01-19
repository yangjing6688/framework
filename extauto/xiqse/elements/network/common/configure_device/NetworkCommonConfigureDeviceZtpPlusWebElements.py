# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.WebElementHandler import *
from xiqse.defs.network.common.configure_device.NetworkCommonConfigureDeviceZtpPlusWebElementsDefinitions import *


class NetworkCommonConfigureDeviceZtpPlusWebElements(NetworkCommonConfigureDeviceZtpPlusWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # ZTP+ Device Settings Tab Fields
    # Basic Management section
    def get_serial_number_field(self):
        """
        :return: Serial Number field element
        """
        return self.weh.get_element(self.serial_number_field)

    def get_use_discovered_dropdown(self):
        """
        :return: Use Discovered field element
        """
        return self.weh.get_element(self.use_discovered_dropdown)

    def get_ip_address_subnet_field(self):
        """
        :return: IP Address / Subnet field element
        """
        return self.weh.get_element(self.ip_address_subnet_field)

    def get_gateway_address_field(self):
        """
        :return: Gateway Address field element
        """
        return self.weh.get_element(self.gateway_address_field)

    def get_management_interface_dropdown(self):
        """
        :return: Management Interface field element
        """
        return self.weh.get_element(self.management_interface_dropdown)

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

    # Configuration/Upgrade section
    # 2021-07-01: need to add combobox fields to configure date/time/offset
    def get_configuration_updates_dropdown(self):
        """
        :return: Configuration Updates field element
        """
        return self.weh.get_element(self.configuration_updates_dropdown)

    def get_configuration_updates_date_dropdown(self):
        """
        :return: Configuration Updates > Update Date field element
        """
        return self.weh.get_element(self.configuration_updates_date_dropdown)

    def get_configuration_updates_time_dropdown(self):
        """
        :return: Configuration Updates > Update Time field element
        """
        return self.weh.get_element(self.configuration_updates_time_dropdown)

    def get_configuration_updates_offset_dropdown(self):
        """
        :return: Configuration Updates > Update UTC Offset field element
        """
        return self.weh.get_element(self.configuration_updates_offset_dropdown)

    def get_firmware_upgrades_dropdown(self):
        """
        :return: Firmware Upgrades field element
        """
        return self.weh.get_element(self.firmware_upgrades_dropdown)

    def get_firmware_upgrades_date_dropdown(self):
        """
        :return: Firmware Upgrades > Update Date field element
        """
        return self.weh.get_element(self.firmware_upgrades_date_dropdown)

    def get_firmware_upgrades_time_dropdown(self):
        """
        :return: Firmware Upgrades > Update Time field element
        """
        return self.weh.get_element(self.firmware_upgrades_time_dropdown)

    def get_firmware_upgrades_offset_dropdown(self):
        """
        :return: Firmware Upgrades > Update UTC Offset field element
        """
        return self.weh.get_element(self.firmware_upgrades_offset_dropdown)

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
