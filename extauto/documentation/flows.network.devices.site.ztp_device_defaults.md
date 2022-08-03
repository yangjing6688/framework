# extauto.xiqse.flows.network.devices.site.ztp_device_defaults package

## Submodules

## extauto.xiqse.flows.network.devices.site.ztp_device_defaults.XIQSE_NetworkDevicesSiteZtpDeviceDefaults module


### _class_ extauto.xiqse.flows.network.devices.site.ztp_device_defaults.XIQSE_NetworkDevicesSiteZtpDeviceDefaults.XIQSE_NetworkDevicesSiteZtpDeviceDefaults()
Bases: `NetworkDevicesSiteZtpDeviceDefaultsWebElements`


#### xiqse_site_ztp_global_ip_to_site_mapping_state()
> 
> * This keyword obtains the state of the Global IP to Site Mapping table in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Note: This table is only read-write when the World site is selected.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Global Ip To Site Mapping State`


* **Returns**

    1 if the table is read-write, 2 if the table is read-only, else -1



#### xiqse_site_ztp_set_admin_profile(admin_profile)
> 
> * This keyword sets the Admin Profile value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Admin Profile  admin_profile`


* **Parameters**

    **admin_profile** – value to select for the Admin Profile field



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_cli_recovery_mode_only_checkbox(state='Disable')
> 
> * This keyword sets the Basic Management CLI Recovery Mode Only value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Note: This field will be enabled when the Poll Type is set to ZTP+.


> * 
> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Cli Recovery Mode Only Checkbox  Enable`


> > * `XIQSE Site Ztp Set Cli Recovery Mode Only Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Basic Management CLI Recovery Mode Only checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_device_protocols_ftp_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols FTP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Ftp Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Ftp Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols FTP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_http_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols HTTP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Http Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Http Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols HTTP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_https_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols HTTPS value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Https Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Https Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols HTTPS checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_lacp_checkbox(state='Disable')
> 
> * This keyword sets the Device Protocols LACP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Lacp Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Lacp Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols LACP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_lldp_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols LLDP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Lldp Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Lldp Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols LLDP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_mstp_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols MSTP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Mstp Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Mstp Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols MSTP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_mvrp_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols MVRP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Mvrp Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Mvrp Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols MVRP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_poe_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols POE value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Poe Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Poe Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols POE checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_snmp_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols SNMP value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Snmp Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Snmp Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols SNMP checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, 2 if the field is read-only, else -1



#### xiqse_site_ztp_set_device_protocols_ssh_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols SSH value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Ssh Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Ssh Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols SSH checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_telnet_checkbox(state='Enable')
> 
> * This keyword sets the Device Protocols Telnet value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Telnet Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Telnet Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols Telnet checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_device_protocols_vxlan_checkbox(state='Disable')
> 
> * This keyword sets the Device Protocols VXLAN value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Device Protocols Vxlan Checkbox  Enable`


> > * `XIQSE Site Ztp Set Device Protocols Vxlan Checkbox  Disable`


* **Parameters**

    **state** – value to set for the Device Protocols VXLAN checkbox (Enable || Disable)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_dns_search_suffix(dns_search_suffix)
> 
> * This keyword sets the DNS Search Suffix value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set DNS Search Suffix  dns_search_suffix`


* **Parameters**

    **dns_search_suffix** – value to set for the DNS Search Suffix



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_dns_server(dns_server)
> 
> * This keyword sets the DNS Server value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set DNS Server  dns_server`


* **Parameters**

    **dns_server** – value to set for the DNS Server



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_dns_server_three(dns_server)
> 
> * This keyword sets the DNS Server 3 value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set DNS Server Three  dns_server`


* **Parameters**

    **dns_server** – value to set for the DNS Server 3



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_dns_server_two(dns_server)
> 
> * This keyword sets the DNS Server 2 value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set DNS Server Two  dns_server`


* **Parameters**

    **dns_server** – value to set for the DNS Server 2



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_domain_name(domain_name)
> 
> * This keyword sets the Domain Name value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Domain Name  domain_name`


* **Parameters**

    **domain_name** – value to set for the Domain Name



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_ending_ip_address(ending_ip_address)
> 
> * This keyword sets the Ending IP Address value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Ending IP Address  ending_ip_address`


* **Parameters**

    **ending_ip_address** – value to set for the Ending IP Address



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_gateway_address(gateway_address)
> 
> * This keyword sets the Gateway Address value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Gateway Address  gateway_address`


* **Parameters**

    **gateway_address** – value to set for the Gateway Address



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_management_interface(management_interface='Default')
> 
> * This keyword sets the Management Interface value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Management Interface  Out-Of-Band`


> > * `XIQSE Site Ztp Set Management Interface  Default`


> > * `XIQSE Site Ztp Set Management Interface  <VlAN-NAME>`


* **Parameters**

    **management_interface** – value to select for the Management Interface field
    (Out-Of-Band || Default || VlAN-NAME)



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_ntp_server(ntp_server)
> 
> * This keyword sets the NTP Server value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set NTP Server  ntp_server`


* **Parameters**

    **ntp_server** – value to set for the NTP Server



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_ntp_server_two(ntp_server)
> 
> * This keyword sets the NTP Server 2 value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set NTP Server 2  ntp_server`


* **Parameters**

    **ntp_server** – value to set for the NTP Server 2



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_poll_group(poll_group)
> 
> * This keyword sets the Poll Group value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Poll Group  More Frequent`


> > * `XIQSE Site Ztp Set Poll Group  Default`


> > * `XIQSE Site Ztp Set Poll Group  Less Frequent`


* **Parameters**

    **poll_group** – value to select for the Poll Group field



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_poll_type(poll_type)
> 
> * This keyword sets the Poll Type value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Poll Type  Not Polled`


> > * `XIQSE Site Ztp Set Poll Type  Ping`


> > * `XIQSE Site Ztp Set Poll Type  SNMP`


> > * `XIQSE Site Ztp Set Poll Type  Maintenance`


> > * `XIQSE Site Ztp Set Poll Type  ZTP+`


* **Parameters**

    **poll_type** – value to select for the Poll Type field



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_site_precedence(site_precedence)
> 
> * This keyword sets the Site Assignment Precedence value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Note: This field is only enabled when the World site is selected.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Site Precedence  IP Range, LLDP`


> > * `XIQSE Site Ztp Set Site Precedence  LLDP, IP Range`


> > * `XIQSE Site Ztp Set Site Precedence  LLDP Only`


> > * `XIQSE Site Ztp Set Site Precedence  IP Range Only`


> > * `XIQSE Site Ztp Set Site Precedence  None`


* **Parameters**

    **site_precedence** – value to select for the Site Assignment Precedent field



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_starting_ip_address(starting_ip_address)
> 
> * This keyword sets the Starting IP Address value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Starting IP Address  starting_ip_address`


* **Parameters**

    **starting_ip_address** – value to set for the Starting IP Address



* **Returns**

    1 if action was successful, 2 if the field is disabled, else -1



#### xiqse_site_ztp_set_subnet_address(subnet_address)
> 
> * This keyword sets the Subnet Address value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Subnet Address  Subnet_Address`


* **Parameters**

    **subnet_address** – value to set for the Subnet Address



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_system_contact(system_contact)
> 
> * This keyword sets the System Contact value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set System Contact  system_contact`


* **Parameters**

    **system_contact** – value to set for the System Contact



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_system_location(system_location)
> 
> * This keyword sets the System Location value in the Site > ZTP+ Device Defaults tab.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set System Location  system_location`


* **Parameters**

    **system_location** – value to set for the System Location



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_set_use_discovered(use_discovered='Disabled')
> 
> * This keyword sets the Use Discovered value in the Site > ZTP+ Device Defaults tab


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Set Use Discovered  Disabled`


> > * `XIQSE Site Ztp Set Use Discovered  IP`


> > * `XIQSE Site Ztp Set Use Discovered  IP and Management Interface`


> > * `XIQSE Site Ztp Set Use Discovered  Management Interface`


* **Parameters**

    **use_discovered** – value to select for the Use Discovered field
    (Disabled, IP, IP and Management Interface, Management Interface)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_ztp_toggle_section(the_section='Basic Management')
> 
> * This keyword toggles (collapses or expands) the specified section in the Site > ZTP+ Device Defaults view.


> * It is assumed the view is already navigated to Network > Devices > Site > ZTP+ Device Defaults.


> * The Section name value is case-sensitive.


> * Keyword Usage

> > 
> > * `XIQSE Site Ztp Collapse Section   Basic Management`


> > * `XIQSE Site Ztp Collapse Section   Configuration/Upgrade`


> > * `XIQSE Site Ztp Collapse Section   Device Protocols`


> > * `XIQSE Site Ztp Collapse Section   Global IP to Site Mapping`


* **Parameters**

    **the_section** – the title of the section that should be toggled.



* **Returns**

    1 if action was successful, else -1


## Module contents
