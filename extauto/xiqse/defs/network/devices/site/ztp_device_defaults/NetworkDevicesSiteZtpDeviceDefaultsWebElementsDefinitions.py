
class NetworkDevicesSiteZtpDeviceDefaultsWebElementsDefinitions:
    # Items Contained Within Dropdown List
    dropdown_element_list = \
        {
            'DESC': 'Dropdown lists that use list. (li)',
            'XPATH': '//div[contains(@id, "${item}") and contains(@id, "-picker-listWrap")]/ul/li',
            
        }

    dropdown_element_division = \
        {
            'DESC': 'Dropdown lists that use division. (div) Example, Management Interface',
            'XPATH': '//div[contains(@id, "${item}") and contains(@id, "-picker-listWrap")]/ul/div',
            
        }

    # Basic Management section
    use_discovered_drop_down = \
        {
            'DESC': 'Use Discovered field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpUseDiscoveredMode"]',
            
        }

    subnet_address_field = \
        {
            'DESC': 'Subnet Address field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpSubnetAddress"]',
            
        }

    starting_ip_address_field = \
        {
            'DESC': 'Starting IP Address field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpStartingIp"]',
            
        }

    ending_ip_address_field = \
        {
            'DESC': 'Ending IP Address field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpEndingIp"]',
            
        }

    gateway_address_field = \
        {
            'DESC': 'Gateway Address field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="gateway"]',
            
        }

    management_interface_drop_down = \
        {
            'DESC': 'Management Interface field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="mgmtInterface"]',
            
        }

    cli_recovery_mode_only_checkbox = \
        {
            'DESC': 'CLI Recovery Mode Only checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpCLIRecoveryModeOnly"]',
            
        }

    domain_name_field = \
        {
            'DESC': 'Domain Name field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpDomainName"]',
            
        }

    dns_server_field = \
        {
            'DESC': 'DNS Server field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="dnsServer"]',
            
        }

    dns_server_two_field = \
        {
            'DESC': 'DNS Server 2 field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="dnsServer2"]',
            
        }

    dns_server_three_field = \
        {
            'DESC': 'DNS Server 3 field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="dnsServer3"]',
            
        }

    dns_search_suffix_field = \
        {
            'DESC': 'DNS Search Suffix field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpDnsSearchSuffix"]',
            
        }

    ntp_server_field = \
        {
            'DESC': 'NTP Server field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ntpServer"]',
            
        }

    ntp_server_two_field = \
        {
            'DESC': 'NTP Server 2 field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ntpServer2"]',
            
        }

    system_contact_field = \
        {
            'DESC': 'System Contact field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="siteSystemContact"]',
            
        }

    system_location_field = \
        {
            'DESC': 'System Location field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="siteSystemLocation"]',
            
        }

    admin_profile_drop_down = \
        {
            'DESC': 'Admin Profile field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpProfile"]',
            
        }

    poll_group_drop_down = \
        {
            'DESC': 'Poll Group field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPollGroup"]',
            
        }

    poll_type_drop_down = \
        {
            'DESC': 'Poll Type field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpMonitorType"]',
            
        }

    site_precedence_drop_down = \
        {
            'DESC': 'Site Precedence field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="sitePrecedence"]',
            
        }

    # Configuration/Upgrade section
    # 2021-06-17: need to add combobox fields to configure date/time/offset
    configuration_updates_drop_down = \
        {
            'DESC': 'Configuration Updates field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledConfigureType"]',
            
        }

    configuration_updates_date_drop_down = \
        {
            'DESC': 'Configuration Updates > Update Date field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledConfigureDate"]',
            
        }

    configuration_updates_time_drop_down = \
        {
            'DESC': 'Configuration Updates > Update Time field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledConfigureTime"]',
            
        }

    configuration_updates_offset_drop_down = \
        {
            'DESC': 'Configuration Updates > Update UTC Offset field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledConfigureUtcOffset"]',
            
        }

    firmware_upgrades_drop_down = \
        {
            'DESC': 'Firmware Upgrades field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledDownloadType"]',
            
        }

    firmware_upgrades_date_drop_down = \
        {
            'DESC': 'Firmware Upgrades > Upgrade Date field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledDownloadDate"]',
            
        }

    firmware_upgrades_time_drop_down = \
        {
            'DESC': 'Firmware Upgrades > Upgrade Time field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledDownloadTime"]',
            
        }

    firmware_upgrades_offset_drop_down = \
        {
            'DESC': 'Firmware Upgrades > Upgrade UTC Offset field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpScheduledDownloadUtcOffset"]',
            
        }

    # Device Protocols section
    device_protocols_telnet_checkbox = \
        {
            'DESC': 'Telnet checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPlusTelnetEnabled"]',
            
        }

    device_protocols_ssh_checkbox = \
        {
            'DESC': 'SSH checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPlusSshEnabled"]',
            
        }

    device_protocols_http_checkbox = \
        {
            'DESC': 'HTTP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPlusHttpEnabled"]',
            
        }

    device_protocols_https_checkbox = \
        {
            'DESC': 'HTTPS checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPlusHttpsEnabled"]',
            
        }

    device_protocols_ftp_checkbox = \
        {
            'DESC': 'FTP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPlusFtpEnabled"]',
            
        }

    device_protocols_snmp_checkbox = \
        {
            'DESC': 'SNMP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="ztpPlusSnmpEnabled"]',
            
        }

    device_protocols_lacp_checkbox = \
        {
            'DESC': 'LACP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="lacp"]',
            
        }

    device_protocols_lldp_checkbox = \
        {
            'DESC': 'LLDP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="lldp"]',
            
        }

    device_protocols_mvrp_checkbox = \
        {
            'DESC': 'MVRP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="mvrp"]',
            
        }

    device_protocols_mstp_checkbox = \
        {
            'DESC': 'MSTP checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="spanningTree"]',
            
        }

    device_protocols_poe_checkbox = \
        {
            'DESC': 'POE checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="poe"]',
            
        }

    device_protocols_vxlan_checkbox = \
        {
            'DESC': 'VXLAN checkbox field within the Site > ZTP+ Device Defaults view',
            'XPATH': '//input[@name="vxlan"]',
            
        }

    # Global IP to Site Mapping section
    global_ip_to_site_mapping_grid = \
        {
            'DEC': 'Global IP to Site Mapping table within the Site > ZTP+ Device Defaults view',
            'XPATH': '//div[contains(@id,"SiteGlobalIpRangeGrid") and @role="grid"]',
            
        }
