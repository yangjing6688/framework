# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#


class NetworkCommonConfigureDeviceZtpPlusWebElementsDefinitions:

    # ZTP+ Device Settings Tab Fields
    # Basic Management section
    serial_number_field = \
        {
            'DESC': 'Serial Number field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="serialNumber"]',
            'wait_for': 10
        }

    use_discovered_dropdown = \
        {
            'DESC': 'Use Discovered field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpUseDiscoveredMode"]',
            'wait_for': 10
        }

    ip_address_subnet_field = \
        {
            'DESC': 'IP Address / Subnet field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ipAddress"]',
            'wait_for': 10
        }
    gateway_address_field = \
        {
            'DESC': 'Gateway Address field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="gateway"]',
            'wait_for': 10
        }

    management_interface_dropdown = \
        {
            'DESC': 'Management Interface field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="mgmtInterface"]',
            'wait_for': 10
        }

    cli_recovery_mode_only_checkbox = \
        {
            'DESC': 'CLI Recovery Mode Only checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpCLIRecoveryModeOnly"]',
            'wait_for': 10
        }

    domain_name_field = \
        {
            'DESC': 'Domain Name field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpDomainName"]',
            'wait_for': 10
        }

    dns_server_field = \
        {
            'DESC': 'DNS Server field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="dnsServer"]',
            'wait_for': 10
        }

    dns_server_two_field = \
        {
            'DESC': 'DNS Server 2 field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="dnsServer2"]',
            'wait_for': 10
        }

    dns_server_three_field = \
        {
            'DESC': 'DNS Server 3 field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="dnsServer3"]',
            'wait_for': 10
        }

    dns_search_suffix_field = \
        {
            'DESC': 'DNS Search Suffix field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpDnsSearchSuffix"]',
            'wait_for': 10
        }

    ntp_server_field = \
        {
            'DESC': 'NTP Server field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ntpServer"]',
            'wait_for': 10
        }

    ntp_server_two_field = \
        {
            'DESC': 'NTP Server 2 field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ntpServer2"]',
            'wait_for': 10
        }

    # Configuration/Upgrade section
    # 2021-07-01: need to add combobox fields to configure date/time/offset
    configuration_updates_dropdown = \
        {
            'DESC': 'Configuration Updates field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledConfigureType"]',
            'wait_for': 10
        }

    configuration_updates_date_dropdown = \
        {
            'DESC': 'Configuration Updates > Update Date field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledConfigureDate"]',
            'wait_for': 10
        }

    configuration_updates_time_dropdown = \
        {
            'DESC': 'Configuration Updates > Update Time field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledConfigureTime"]',
            'wait_for': 10
        }

    configuration_updates_offset_dropdown = \
        {
            'DESC': 'Configuration Updates > Update UTC Offset field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledConfigureUtcOffset"]',
            'wait_for': 10
        }

    firmware_upgrades_dropdown = \
        {
            'DESC': 'Firmware Upgrades field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledDownloadType"]',
            'wait_for': 10
        }

    firmware_upgrades_date_dropdown = \
        {
            'DESC': 'Firmware Upgrades > Upgrade Date field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledDownloadDate"]',
            'wait_for': 10
        }

    firmware_upgrades_time_dropdown = \
        {
            'DESC': 'Firmware Upgrades > Upgrade Time field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledDownloadTime"]',
            'wait_for': 10
        }

    firmware_upgrades_offset_dropdown = \
        {
            'DESC': 'Firmware Upgrades > Upgrade UTC Offset field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpScheduledDownloadUtcOffset"]',
            'wait_for': 10
        }

    # Device Protocols section
    device_protocols_telnet_checkbox = \
        {
            'DESC': 'Telnet checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpPlusTelnetEnabled"]',
            'wait_for': 10
        }

    device_protocols_ssh_checkbox = \
        {
            'DESC': 'SSH checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpPlusSshEnabled"]',
            'wait_for': 10
        }

    device_protocols_http_checkbox = \
        {
            'DESC': 'HTTP checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpPlusHttpEnabled"]',
            'wait_for': 10
        }

    device_protocols_https_checkbox = \
        {
            'DESC': 'HTTPS checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpPlusHttpsEnabled"]',
            'wait_for': 10
        }

    device_protocols_ftp_checkbox = \
        {
            'DESC': 'FTP checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpPlusFtpEnabled"]',
            'wait_for': 10
        }

    device_protocols_snmp_checkbox = \
        {
            'DESC': 'SNMP checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="ztpPlusSnmpEnabled"]',
            'wait_for': 10
        }

    device_protocols_lacp_checkbox = \
        {
            'DESC': 'LACP checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="lacp"]',
            'wait_for': 10
        }

    device_protocols_lldp_checkbox = \
        {
            'DESC': 'LLDP checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="lldp"]',
            'wait_for': 10
        }

    device_protocols_mvrp_checkbox = \
        {
            'DESC': 'MVRP checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="mvrp"]',
            'wait_for': 10
        }

    device_protocols_mstp_checkbox = \
        {
            'DESC': 'MSTP checkbox ffield on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="spanningTree"]',
            'wait_for': 10
        }

    device_protocols_poe_checkbox = \
        {
            'DESC': 'POE checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="poe"]',
            'wait_for': 10
        }

    device_protocols_vxlan_checkbox = \
        {
            'DESC': 'VXLAN checkbox field on the ZTP+ Device Settings tab of the Configure Device dialog',
            'XPATH': '//input[@name="vxlan"]',
            'wait_for': 10
        }
