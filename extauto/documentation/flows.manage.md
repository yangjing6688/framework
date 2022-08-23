# extauto.xiq.flows.manage package

## Submodules

## extauto.xiq.flows.manage.AdvOnboard module


### _class_ extauto.xiq.flows.manage.AdvOnboard.AdvOnboard()
Bases: `AdvOnboardWebElements`


#### advance_onboard_access_point(device_detail=None, location=None, branch_id=None, nw_policy=None, internal_ssid=None, guest_ssid=None)

* This keyword is used to advance onboard the access point


* This keyword is used to onboard both simulated and real devices


* Flow:

> 
> * Navigate to Manage –> Devices –> Add(+) –>Advance Onboarding


* Keyword Usage:

> 
> * `Advance Onboard Access Point    device_detail=&{DEVICE_DETAIL1}   location=&{LOCATION01}    nw_policy=&{NW_POLICY01}   internal_ssid=&{INTERNAL_SSID1_CONFIG}  guest_ssid=&{GUEST_SSID1_CONFIG}`


* **Parameters**

    **device_detail** – device detail is the dictionary Ex:



* &{DEVICE_DETAIL1}    device_type=real         device_model=Extreme-Aerohive    device_sn=06301908310568


* &{DEVICE_DETAIL2}    device_type=simulated    device_model=AP550


* **Parameters**

    **location** – location is the dict parameter Ex:



* &{LOCATION01}    loc_node=auto_location_01   country_node=San Jose    building_node=building_01     floor_node=floor_01


* **Parameters**

    
    * **branch_id** – branch id argument not required for access point


    * **nw_policy** – network policy is the dict parameter Ex:



* &{NW_POLICY01}      policy_name=AUTO_ADVANCE_TEST    internal_nw_type=Enable     guest_acc_nw_type=Enable


* &{NW_POLICY01}      policy_name=AUTO_ADVANCE_TEST    internal_nw_type=Disable    guest_acc_nw_type=Enable


* &{NW_POLICY01}      policy_name=AUTO_ADVANCE_TEST    internal_nw_type=Enable     guest_acc_nw_type=Disable


* &{NW_POLICY03}      policy_name=OPEN_AUTO            existing_nw_policy=enable


* **Parameters**

    **internal_ssid** – internal ssid dict parameters Ex:



* &{INTERNAL_SSID1_CONFIG}   internal_ssid_name=AUTO_TEST    network_type=Secure    create_global_password=Enable    [global_passwd=Extreme@123](mailto:global_passwd=Extreme@123)


* **Parameters**

    **guest_ssid** – guest ssid dict parameters Ex:



* &{GUEST_SSID1_CONFIG}    guest_ssid_name=AUTO_GUEST        network_type=Unsecure   guest_access_without_login=Enable


* **Returns**

    


* 1 If successfully on boarded


* -1 failed in ADD DEVICES Step


* -2 Failed in ASSIGN LOCATION Step


* -3 Failed in ASSIGN BRANCH ID Step


* -4 Failed in CREATE NETWORK POLICY step

## extauto.xiq.flows.manage.AdvanceOnboarding module


### _class_ extauto.xiq.flows.manage.AdvanceOnboarding.AdvanceOnboarding()
Bases: `AdvanceOnboardingWebElements`


#### advance_onboard_device(device_serial, device_make='', dev_location='', device_type='Real', entry_type='Manual', csv_location='', create_location=False)
> 
> * This keyword is used to onboard Device using Advance Onboarding Method


> * Keyword Usage:

> > 
> > * `Onboard Device  ${DEVICE_SERIAL}   device_make=${DEVICE_MAKE_AEROHIVE}   dev_location=${LOCATION}`


* **Parameters**

    
    * **device_serial** – serial number of Device


    * **device_make** – Model of the Device ex:Extreme-aerohive,ExOS,VOSS,DELL


    * **dev_location** – Location details in Comma format


    * **device_type** – Real or Simulated Device type


    * **entry_type** – Either Manual or CSV Entry Type


    * **csv_location** – Absolute Path of Device onboarding CSV File Location on remote Machine


    * **create_location** – Create new location during onboarding



* **Returns**

    1 if Device Onboarded Sucessfully else -1


## extauto.xiq.flows.manage.Alarms module


### _class_ extauto.xiq.flows.manage.Alarms.Alarms()
Bases: `AlarmsWebElements`


#### clear_alarm(search_string)

* Flow: Manage–> Alarms


* Clear the generated alarms based on the search string


* Keyword Usage:

> 
> * `Clear Alarm   ${DEVICE_MAC}`


* **Parameters**

    **search_string** – str to search the alarm in grid ex: it may be severity, host name, Device mac, category



* **Returns**

    1 if alarm Cleared Successfully else -1



#### get_alarm_details(search_string)

* Flow: Manage–> Alarms


* Get Alarm details based on search string


* Keyword Usage:

> 
> * `Get Alarm Details   ${DEVICE_MAC}`


* **Parameters**

    **search_string** – str to search the alarm in grid ex: it may be severity, host name, Device mac, category



* **Returns**

    Alarm details in a dictionary



#### get_alarms_count_from_status_card(alarm_type='critical')

* Flow: Manage–> Alarms


* Get the alarms count from the status bar , based on alarms type


* Keyword Usage:

> 
> * `Get Alarms Count From Status Card    ${ALARM_TYPE}`


* **Parameters**

    **alarm_type** – it will be critical, minor, major



* **Returns**

    Total alarm Count


## extauto.xiq.flows.manage.Applications module


### _class_ extauto.xiq.flows.manage.Applications.Applications()
Bases: `object`


#### add_custom_applications(application_name, group_name)

* This keyword will create Custom Application under Manage > Applications.


* Flow: Manage –> Applications –> Manage Applications –> ADD CUSTOM


* Keyword Usage:

> 
> * `Add Custom Applications  ${APPLICATION_NAME}  ${GROUP_NAME}`


* **Parameters**

    
    * **application_name** – Custom application name


    * **group_name** – group name



* **Returns**

    1 if success and -1 if fails



#### delete_custom_applications(application_name_modified)

* This keyword will delete Custom Application under Manage > Applications.


* Flow: Manage –> Applications –> Manage Applications –> Search and select an application –> Delete application


* Keyword Usage:

> 
> * `Delete Custom Applications  ${APPLICATION_NAME_MODIFIED}`


* **Parameters**

    **application_name_modified** – Modified application name



* **Returns**

    1 if success and -1 if fails



#### edit_custom_applications(application_name, application_name_modified)

* This keyword will modify Custom Application under Manage > Applications.


* Flow: Manage –> Applications –> Manage Applications –> Search and select an application –> Edit application


* Keyword Usage:

> 
> * `Edit Custom Application  ${APPLICATION_NAME}  ${APPLICATION_NAME_MODIFIED}`


* **Parameters**

    
    * **application_name** – Custom application name


    * **application_name_modified** – Modified application name



* **Returns**

    1 if success and -1 if fails


## extauto.xiq.flows.manage.Client module


### _class_ extauto.xiq.flows.manage.Client.Client()
Bases: `object`


#### convert_mac_to_colon_Format(mac_address)

* This keyword will convert Mac address from ‘XXXXXXXXXXXX’ to ‘xx:xx:xx:xx:xx:xx’ format


* Keyword Usage:

> 
> * `convert mac to colon format  ${ANY_MAC}`


* **Parameters**

    **mac_address** – Mac Address to convert



* **Returns**

    Mac address in ‘xx:xx:xx:xx:xx:xx’ format



#### convert_to_client_mac(mac_address)

* This keyword will convert Mac address in ‘xxxxxxxx:xxxxxxx’ format


* Keyword Usage:

> 
> * `convert to client mac  ${CLIENT_MAC}`


* **Parameters**

    **mac_address** – Mac Address to convert



* **Returns**

    Mac address entry in ‘xxxxxxxx:xxxxxxx’ format



#### delete_client_historical(client_mac)

* Clear the client from GDC


* Flow: Manage–>Clients–>Historical


* Keyword Usage:

> 
> * `Delete Client Historical  ${CLIENT_MAC}`


* **Parameters**

    **client_mac** – Client Mac address



* **Returns**

    1 if cleared Client Mac entry else -1



#### delete_client_realtime(client_mac)

* Clear the client from GDC


* Flow: Manage–>Clients–>Historical


* Keyword Usage:

> 
> * `Delete Client RealTime  ${CLIENT_MAC}`


* **Parameters**

    **client_mac** – Client Mac address



* **Returns**

    1 if cleared Client Mac entry else -1



#### get_client_row(client_name='default', client_mac='default')

* Get the Client row from the grid row based on client_name or client_mac


* Keyword Usage:

> 
> * `Get Client Row  client_mac=${CLIENT_MAC}`


> * `Get Client Row  client_name=${CLIENT_NAME}`


* **Parameters**

    
    * **client_name** – Client Name


    * **client_mac** – Client Mac Address



* **Returns**

    Row information if Client information found on Grid else return None



#### get_client_status(client_name='default', client_mac='default')

* Get the Client Status from the grid row based on client_name or client_mac


* Keyword Usage:

> 
> * `Get Client Status  client_mac=${CLIENT_MAC}`


> * `Get Client Status  client_name=${CLIENT_NAME}`


* **Parameters**

    
    * **client_name** – Client Name


    * **client_mac** – Client Mac Address



* **Returns**

    1 if client entry shows green and connected else -1



#### get_real_time_client360_information(client_mac)

* Get the real time client details from the client grid


* Flow : Manage–> clients–> Client MAC hyper Link–>Client 360 Page


* Keyword Usage:

> 
> * `Get Real Time Client360 Information    ${CLIENT_MAC}`


* **Parameters**

    **client_mac** – client mac address



* **Returns**

    client 360 details dictionary if MAC entry found on clients grid else -1



#### get_real_time_client_details(search_string)

* Get the real time client details from the client grid


* Flow Manage –> Clients –> Real Time


* Keyword Usage:

> 
> * `Get Real Time Client Details    ${SEARCH_STRING}`


* **Parameters**

    **search_string** – client row search  ex: client mac, device name etc



* **Returns**

    client details dict



#### verify_client_status(client_name='default', client_mac='default', status='default')

* This keyword returns 1 if Client status expected matches the status passed as argument


* Keyword Usage:

> 
> * `Get Client Status  client_mac=${CLIENT_MAC}       status=green`


> * `Get Client Status  client_mac=${CLIENT_MAC}       status=red`


> * `Get Client Status  client_name=${CLIENT_NAME}     status=green`


> * `Get Client Status  client_name=${CLIENT_NAME}     status=red`


* **Parameters**

    
    * **client_name** – client serial number


    * **client_mac** – client mac MAC


    * **status** – green, red, or amber as of now - may change in future



* **Returns**

    1 if Client status matches else None


## extauto.xiq.flows.manage.ClientMonitor module


### _class_ extauto.xiq.flows.manage.ClientMonitor.ClientMonitor()
Bases: `ClientMonitorWebElements`


#### get_authentication_counts()

* Flow: Manage –> Client Monitor & Diagnosis –> Client Monitor


* get ths issue authentication counts from authentication status card


* Keyword Usage:

> 
> * `Get Authentication Counts`


* **Returns**

    client authentication issue count



#### get_client_issue_entries(search_string, issue_type='All', issue_state='All')

* Flow: Manage –> Tools –> Client Monitor


* Get the client issue entries from the client issue grid rows,


* Keyword Usage:

> 
> * `Get Client Issue Entries   ${CLIENT_MAC}`


* **Parameters**

    
    * **search_string** – sting to search the client issue rows, it may be detected time, client mac


    * **issue_type** – type of the issue i.e Authentication, Association, Networking


    * **issue_state** – state of the issue, i.e Active, All, Resolved, Escalated



* **Returns**

    client issue detail dict


## extauto.xiq.flows.manage.Device360 module


### _class_ extauto.xiq.flows.manage.Device360.Device360()
Bases: `Device360WebElements`


#### advance_channel_selection(device_serial=None)

* This keyword  gets advance channel selection details

-Flow: Manage –> Devices –> Select the device row based on the passed device serial –>Utilities –> Status –> Advanced Channel Selection
- Keyword Usage:

> 
> * 

> ```
> ``
> ```

> ${RESULT}=        Advance Channel Selection         ${DEVICE_SERIAL} \`\`


* **Parameters**

    **device_serial** – serial of the device



* **Returns**

    returns the output of the advance channel selection



#### check_client_in_device360(device_serial=None, client_mac=None)

* This keyword is used to check the client in device360 page based on passed client mac address

-Flow: Manage –> Devices –> click on the Clients hyperlink which is present in Device grid row based on device serial
- Keyword Usage:

> 
> * `${RESULT}=        Check Client In Device360          ${DEVICE_SERIAL}       ${CLIENT _MAC}`


* **Parameters**

    
    * **device_serial** – serial of the device


    * **client_mac** – MAC of the client



* **Returns**

    1 if successful else -1



#### check_devices_by_search_field(search_string, device_name='', device_mac='')

* This keyword is used to Search devices Using Search String passed on devices page Search Option.


* Flow : Manage –> Devices–> Enter Search String on Devices Search Field


* Select the device and give the System information details


* Keyword Usage:

> 
> * `Check Devices By Search Field  ${AP_NAME_PART_STRING1}   device_name=${AP1_NAME}`


* **Parameters**

    
    * **search_string** – Partial String of AP Name


    * **device_mac** – Device MAC Address


    * **device_name** – Device Host Name



* **Returns**

    dictionary of Device information



#### check_two_lists(port_state, port_duplex_cli)
This keyword find out if two lists have at least one element different by ‘’ at the same index into list
:param port_state:
:param port_duplex_cli:
:return: 1 if two lists have at least one element different by ‘’ at the same index into list ; else -1


#### check_up_or_down_ports(port_list, port_state='down')
This keyword check the list of ports and returns only ports with “OPERATE” status that are up/down
(if port_state = ‘down’ the function will return a list with ports that are ‘up’ and the other ports will be
deleted and will be replaced with ‘’)
(if port_state = ‘up’ the function will return a list with ports that are ‘down’ and the other ports will be
deleted and will be replaced with ‘’)
:param port_list: a list with status of ports (up/down)
-Keyword Usage

> check_up_or_down_ports    ${OPERATE STATE}


* **Parameters**

    **port_state** – specify the element which will be deleted from list



* **Returns**

    port_list - a list with the ports that are up/down
    -1 - no port is up/down



#### click_hyperlink_on_system_information(device_mac=None, device_name=None, Clickon=None)

* This keyword Clicks SSID or Device Template on system information from device360 page using DeviceMac or Name


* Flow : Manage–> Devices –> Monitor –> SystemInformation –> click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Click HyperLink on System Information  device_mac=${AP1_MAC} Clickon=Template`


> * `Click HyperLink on System Information  device_name=${AP1_NAME} Clickon=SSID`


* **Returns**

    Name of device Template or SSID after navigation by clicking on hyperlink or -1 in case of error



#### close_client360_window()

* This keyword closes the Device360 dialog window.  It assumes the Device360 Window is open - if the close
button cannot be found, a message is printed.


* Flow: Client 360 Window –> Click “X” to close Device360 Window


* Keyword Usage:

> 
> * `Close Client360 Window`

:param  None
:return: 1 if the Client 360 window was closed, else -1


#### close_device360_window()

* This keyword closes the Device360 dialog window.  It assumes the Device360 Window is open - if the close
button cannot be found, a message is printed.


* Flow: Device 360 Window –> Click “X” to close Device360 Window


* Keyword Usage:

> 
> * `Close Device360 Window`

:param  None
:return: 1 if the device 360 window was closed, else -1


#### compare_transmission_mode(port_index, port_state, port_duplex_cli)
This keyword compares the status for transmission mode between XIQ and CLI
:param port_index: a string of a port or a list of ports
:param port_state: a string or a list which contains the status UP/DOWN of ports. If an element of list is ‘’, it will be ignored
:param port_duplex_cli: the “OPERATE DUPLEX” status from CLI
-Keyword Usage:

> compare_transmision_mode     1/7  up  full
> compare_transmision_mode     2/4  up  full
> compare_transmision_mode     ${PORTS_INDEX}   ${OPERATE_STATE_UP}   ${OPERATE_DUPLEX}


* **Returns**

    1 if the status of transmission in XIQ and CLI are the same
    -1 if the status of transmission in XIQ and CLI are different



#### configure_element_port_type(element, value)
This keyword select the Tabs and configure all field when create or edit a new port type
See edit_port_type and create_new_port_type
:param element: name of field
:param value: value of field ; if contains the string “next_page” will move to next tab
:return:


#### confirm_device360_monitor_clients_chart_displayed()

* This keyword confirms the chart on the Monitor> Clients page in the Device360 dialog window is displayed.
It assumes the Device360 Window is open and on the Monitor> Clients tab.


* Keyword Usage:

> 
> * `Confirm Device360 Monitor Clients Chart Displayed`

:param  none
:return: 1 if the chart is displayed, else -1


#### confirm_device360_monitor_diagnostics_chart_displayed()

* This keyword confirms the chart on the Monitor> Diagnostics page in the Device360 dialog window is displayed.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Confirm Device360 Monitor Diagnostics Chart Displayed`

:param  none
:return: 1 if the chart is displayed, else -1


#### confirm_device360_monitor_overview_chart_displayed()

* This keyword confirms the chart on the Monitor> Overview page in the Device360 dialog window is displayed.
It assumes the Device360 Window is open and on the Monitor> Overview tab.


* Keyword Usage:

> 
> * `Confirm Device360 Monitor Overview Chart Displayed`

:param  none
:return: 1 if the chart is displayed, else -1


#### confirm_device360_port_diagnostics_all_ports_deselected()

* This keyword confirms all ports on the Monitor> Diagnostics page are deselected in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Confirm Device360 Port Diagnostics All Ports Deselected`

:param  none
:return: 1 if all ports are deselected, else -1


#### confirm_device360_port_diagnostics_all_ports_selected()

* This keyword confirms all ports on the Monitor> Diagnostics page are selected in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Confirm Device360 Port Diagnostics All Ports Selected`

:param  none
:return: 1 if all ports are selected, else -1


#### confirm_device360_port_diagnostics_port_deselected(port_num)

* This keyword confirms the specified port on the Monitor> Diagnostics page is deselected.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Confirm Device360 Port Diagnostics Port Deselected    3`

:param  port_num    specifies which port should be deselected
:return: 1 if the specified ports are selected, else -1


#### confirm_device360_port_diagnostics_port_selected(port_num)

* This keyword confirms the specified port on the Monitor> Diagnostics page is selected.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Confirm Device360 Port Diagnostics Port Selected    3`

:param  port_num    specifies which port should be selected
:return: 1 if the specified ports are selected, else -1


#### confirm_device360_time_range_selected(time_range)

* This keyword confirms the specified time range is selected in the Device360 dialog window.
It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.


* Keyword Usage:

> 
> * `Confirm Device360 Time Range Selected    Day`


> * `Confirm Device360 Time Range Selected    Week`


> * `Confirm Device360 Time Range Selected    Month`

:param  time_range  indicates which time range value to check for (e.g., Day, Week, Month)
:return: 1 if the specified time range is currently selected, else -1


#### create_new_port_type(template_values, port, d360=False, verify_summary=True)
This function is used to create a new port type from d360 or template page by using new format


* **Parameters**

    **template_values** – A dictionary with below structure:


Each element from dictionary template_values has the following format:

    ‘setting name’: [configured_value, check_summary_value]

To change the value of a setting, use the following syntax:

    template_voss_auto_sense_on[‘setting name’][0] = ‘configured_value’

To not configure an element from dictionary:

    template_voss_auto_sense_on[‘setting name’][0] = None

To check the value of a setting into summary page, use the following sintax:

    template_voss_auto_sense_on[‘setting name’][1] = ‘check_summary_value’

To not verify an element from dictionary into summary page :

    template_voss_auto_sense_on[‘setting name’][1] = None

To press next buttom use into dictionary an element like this : ‘page2 accessVlanPage’:[“next_page”, None],

template_values=                {‘name’: [“port type name”, ‘port type name’],

    > ‘description’: [“add_description”, “add_description”],
    > ‘status’:[‘click’, ‘off’],          #[‘click’/None, ‘on’/’off’/None]
    > ‘auto-sense’:[‘click’,None],       #[‘click’/None, None]
    > ‘port usage’:[‘trunk port’, ‘trunk’],

    > > #[‘trunk port’/’access port’/None, ‘trunk’/’access’/’auto_sense’/None]

    > #’page2 accessVlanPage’:[“next_page”, None],       # used for access ports
    > #’vlan’:[‘40’, ‘40’],                       # used for access ports

    > ‘page2 trunkVlanPage’: [“next_page”, None],
    > ‘native vlan’: [‘50’, ‘50’],     # used for trunk ports
    > ‘allowed vlans’: [‘60’, ‘60’],   # used for trunk ports [‘all’/None, ‘all’/None]

    > ‘page3 transmissionSettingsPage’: [“next_page”, None],
    > ‘transmission type’: [‘auto’,’auto’],

    > > #[‘auto’/’Half-Duplex’/’Full-Duplex’, ‘auto’/’Half_Duplex’/’Full_Duplex’/None]

    > ‘transmission speed’:[‘auto’,’auto’],

    >     #[‘auto’/’10 Mbps’/’100 Mbps’/None, ‘auto’/’10 Mbps’/’100 Mbps’/None]

    > ‘cdp receive’:[None, ‘off’],        # [‘click’/’None’, ‘on’/’off’/None]
    > ‘lldp transmit’:[‘click’, ‘off’],   # [‘click’/’None’, ‘on’/’off’/None]
    > ‘lldp receive’:[None, ‘off’],       # [‘click’/’None’, ‘on’/’off’/None]

    > ‘page4 stpPage’: [“next_page”, None],
    > ‘stp enable’:[‘click’, ‘enabled’],      #[‘click’/None, ‘on’/’off’/None]
    > ‘edge port’: [‘click’, ‘enabled’],      #[‘click’/None, ‘on’/’off’/None]
    > ‘bpdu protection’:[None, ‘disabled’],   #[‘click’/None, ‘on’/’off’/None]
    > ‘priority’:[‘32’, ‘32’],

    > > #[‘0’/’16’/’32’/’48’…/’192’/None, ‘0’/’16’/’32’/’48’…/’192’/None]

    > ‘path cost’:[‘50’, ‘50’],   #[‘1 - 200000000’/None, ‘1 - 200000000’/None]

    > ‘page5 stormControlSettingsPage’: [“next_page”, None],
    > ‘broadcast’:[None, ‘disabled’],         #[‘click’/None, ‘enabled’/’disabled’/None]
    > ‘unknown unicast’:[None, ‘disabled’],   #[None, ‘disabled’/None]
    > ‘multicast’:[None, ‘disabled’],         #[‘click’/None, ‘enabled’/’disabled’/None]
    > ‘rate limit type’:[None,’pps’],         #[None, ‘pps’/None]
    > ‘rate limit value’: [‘65535’, ‘65535’], #[‘0-65535’/None, ‘0-65535’/None]

    > #for VOSS
    > ‘page6 pseSettingsPage’: [“next_page”, None],
    > ‘PSE profile’:[None,None],

    > > #[‘default-pse-vsp’/’None’, ‘default-pse-vsp’/’None’]

    > ‘poe status’:[None,’on’],           #[‘click’/None, ‘on’/’off’/None]

    > ‘page7 summaryPage’: [“next_page”, None]

    > #==========================================
    > #Only for exos
    > ‘page6 ELRPSettingsPage’: [“next_page”, None],
    > ‘elrp status’: [‘click’, ‘enabled’],      #[‘click’/None, ‘on’/’off’/None]

    > ‘page7 pseSettingsPage’: [“next_page”, None],
    > ‘PSE profile’:[None,None],

    > > #[‘default-pse-vsp’/’None’, ‘default-pse-vsp’/’None’]

    > ‘poe status’:[None,’on’],           #[‘click’/None, ‘on’/’off’/None]

    > ‘page8 summaryPage’: [“next_page”, None]

    }


* **Parameters**

    
    * **port** – the port where new port type will be created


    * **d360** – False if new port type will be created into policy template, True if new port type will be created


into d360 page
:param verify_summary: True if configured values will be verify on summary page. False if verification on summary
page will be skipped
:return: 1 if new port type was successfully created and summary page displays correct values  ; else -1


#### d360Event_search(search_value)
This keyword inserts info into event search text box. No button for search is present, the search will be done
automatically after the text was inserted
:param search_value:
:return: 1 if the text was entered into search box and -1 if search text box was not found


#### d360_cancel_port_configuration()

#### d360_check_if_vim_is_installed()
This function check if the Vim is installed
:return: a string with VIM model or -1 if vim is not present


#### d360_return_vim_port_number()
This function return the first port of vim
:return: the first port of vim ; else -1


#### d360_save_port_configuration()

#### device360_check_column_picker(option, \*columns, select_page='', device_mac='', device_name='')
This keyword confirms the list of the column picker values that was previously checked or unchecked in the
column from a specific page
:param option: check/uncheck columns picker values from each page
:param columns: list of columns from each page that should be selected
:param select_page: the page can be Overview/Clients/Alarms/Events
:param device_mac: mac of the device
:param device_name: name of the device
:return: 1 if you can select the page and return the status of the column from the specific page; else -1


#### device360_check_events_is_in_order()

* This Keyword checks whether the events in D360 are on order


* **Return 1 - if the Events severity are in order**



* **Return -1 - if the Events severity are not in order**



#### device360_check_wired_client(device_serial=None, device_mac=None, client_mac=None, sleep_time=30, iteration=15)
> 
> * This keyword is used to check the client exist in device360 page based on passed client mac address

> -Flow: Manage –> Devices –> check on the Clients which is present in Device grid row based on Client MAC
> - Keyword Usage:


* **Parameters**

    
    * **device_serial** – Serial Number of the Device


    * **device_mac** – Mac address of the Device


    * **client_mac** – Client MAC address


    * **sleep_time** – The time period between each iteration


    * **iteration** – The number of iteration



* **Returns**

    -1 if there are any failure or client details in dict format


Client details: client mac,ipv4,ipv6,port speed,negotiated speed,vlan, port mode,


#### device360_click_clients(search_string, device_mac='', device_serial='', sleeptime=30, iteration=30)
This keyword is to check whether the clients can be clickable
:param search_string: The mac address of the client
:param device_mac: Device MAC address for device selection
:param device_serial: Device serial number for device selection
:param sleeptime: The time period of sleep between each iteration
:param iteration: the number of iteration
:return: -1 if can’t click client else return 1


#### device360_click_on_checkbox_or_button_port_configuration(select_column, port_name)
This keyword click on checkbox for the specific row and column into device360 Port Configuration window
select_column : - Port Details : ‘port state’

> 
> * Port Settings & Aggregation: ‘transmit’ , ‘receive’ , ‘cdp’ , ‘client reporting’


> * STP: ‘stp status’ , ‘edge port’


> * Storm Control: ‘broadcast’ , ‘unknown unicast’ , ‘multicast’

port_name: Number of port . e.g 1/1 ; 2:1
E.g. :
device360_revert_port_configuration          flow        1:3

return: 1 if successful revert; else -1


#### device360_click_open_site_engine_link()

* This keyword clicks on the OPEN SITE ENGINE link


* It is assumed that the Device360 window is open and the Overview panel is selected.


* Keyword Usage

> 
> * `Device360 Click Open Site Engine Link`


* **Returns**

    1 if action was successful (or the field is disabled), else -1



#### device360_configure_device_port_poe_status_and_profile(device_mac='', device_name='', port_number='', poe_profile='', poe_status='ON')

* This keyword will Enable/Disable Port POE Status and POE Profile in Device360 Page


* Flow: Click Device –>Device 360 Window –> Configure –> Port Configuration–> PSE–> POE Status and Profile


* Keyword Usage:

> 
> * `Device360 Configure Device Port POE Status And Profile  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}   poe_profile=${POE_PROFILE}    poe_status=${POE_STATUS}`


> * `Device360 Configure Device Port POE Status And Profile  device_NAME=${DEVICE_NAME}  port_number=${PORT_NUMBER}   poe_profile=${POE_PROFILE}    poe_status=${POE_STATUS}`


> * **param device_mac**

>     Device Mac Address



> * **param device_name**

>     Device Name



> * **param port_number**

>     Port Number of the Switch



* **Parameters**

    
    * **poe_profile** – POE Profile Name for Switch Port


    * **poe_status** – POE Status(ON/OFF) for Switch Port



* **Returns**

    1 if port POE Status and Profile changed Successfully else -1



#### device360_configure_device_port_status(device_mac='', device_name='', port_number='', port_status='ON')

* This keyword will Enable/Disable Port Status in Device360 Page


* Flow: Click Device –>Device 360 Window –> Configure –> Port Configuration–> Port State to OFF/ON


* Keyword Usage:

> 
> * `Device360 Configure Device Port Status  device_mac=${MAC_ADDRESS}  port_number=${PORT_NUMBER}   port_status=${PORT_STATUS}`


> * `Device360 Configure Device Port Status  device_NAME=${NAME}  port_number=${PORT_NUMBER}   port_status=${PORT_STATUS}`


> * **param device_mac**

>     Device Mac Address



> * **param device_name**

>     Device Name



> * **param port_number**

>     Port Number of the Switch



* **Parameters**

    **port_status** – Port Status either ON/OFF



* **Returns**

    1 if port Status changed Successfully or already in expected port status, else -1



#### device360_configure_device_vlan_for_port(vlan=1363)
This keyword is to configure vlan in D360
Manage –> Devices –> Device360 –> Port Configuration –> Vlan for port 1
It Assumes That Already Navigated to Device360 Page
:param vlan: vlan to configure on port 1
:return: returns 1 if successfully configured, else returns -1


#### device360_configure_poe_threshold_value(threshold_value, device_mac='', device_name='')
> 
> * This keyword will configure the POE threshold value in Device 360


> * Flow: Click Device –> Device 360 Window –> Port Configuration –> PSE –> PSE SETTINGS FOR DEVICE


> * Keyword Usage:


> * `Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}   device_mac=${DEVICE_MAC}`


> * `Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}   device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **threshold_value** – value for threshold between 1 and 99


    * **device_mac** – Device Mac Address


    * **device_name** – Device Name



* **Returns**

    1 if value was configured successfully , else -1



#### device360_configure_poe_threshold_value_stack(threshold_value, slot, device_mac='', device_name='')
> 
> * This keyword will configure the POE threshold value in Device 360


> * Flow: Click Device –> Device 360 Window –> Port Configuration –> PSE –> PSE SETTINGS FOR DEVICE


> * Keyword Usage:


> * `Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}  slot=${SLOT} device_mac=${DEVICE_MAC}`


> * `Device360 Configure POE Threshold value    threshold_value=${THRESHOLD_POE}  slot=${SLOT}  device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **threshold_value** – value for threshold between 1 and 99


    * **device_mac** – Device Mac Address


    * **device_name** – Device Name



* **Slot**

    The slot which supported POE



* **Returns**

    1 if value was configured successfully , else -1



#### device360_configure_port_access_vlan(device_mac='', device_name='', port_number='', access_vlan_id='', port_type='Access Port')

* This keyword will Configure Device switch Port Access Vlan in Device360 Page.


* Flow: Click Device –>Device 360 Window –> Configure –> Port Configuration–> interface –> Port Usage and Vlan


* Keyword Usage:

> 
> * `Device360 Configure Port Access Vlan  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}`


> * `Device360 Configure Port Access Vlan  device_name=${DEVICE_NAME}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}`


> * **param device_mac**

>     Device Mac Address



> * **param device_name**

>     Device Name



> * **param port_number**

>     Port Number of the Switch



> * **param access_vlan_id**

>     Access Vlan Number for switch port



* **Parameters**

    **port_type** – Access Port



* **Returns**

    1 if Port Usage Access and Vlan Successfully configured else -1



#### device360_configure_port_transmission_mode_and_speed(device_mac='', device_name='', port_number='', transmission_mode='', speed='')

* This keyword will Configure Device switch Port transmission_mode and speed in Device360 Page.


* Flow: Click Device –>Device 360 Window –> Configure –> Port Configuration–>

    Port settings –> Interface –> Transmission Mode and Speed


* Keyword Usage:

> 
> * \`\` device360 configure port transmission mode and speed  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}

> transmission_mode=${MODE}  speed=${SPEED}\`\`
> - \`\` device360 configure port transmission mode and speed  device_name=${DEVICE_NAME}  port_number=${PORT_NUMBER}
> transmission_mode=${MODE}  speed=${SPEED}\`\`


> * **param device_mac**

>     Device Mac Address



> * **param device_name**

>     Device Name



> * **param port_number**

>     Port Number of the Switch



> * **param transmission_mode**

>     switch port Transmission Mode



* **Parameters**

    **speed** – switch port Speed



* **Returns**

    1 if Port Transmission Mode and speed Successfully configured else -1



#### device360_configure_port_trunk_vlan(device_mac='', device_name='', port_number='', trunk_native_vlan='', trunk_vlan_id='', port_type='Trunk Port')

* This keyword will Configure Device switch Port Trunk Vlan in Device360 Page.


* Flow: Click Device –>Device 360 Window –> Configure –> Port Configuration–> interface –> Port Usage and Vlan


* Keyword Usage:

> 
> * `Device360 Configure Port Trunk Vlan  device_mac=${DEVICE_MAC}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}`


> * `Device360 Configure Port Trunk Vlan  device_name=${NAME}  port_number=${PORT_NUMBER}  access_vlan_id=${VLAN_ID}`


> * **param device_mac**

>     Device Mac Address



> * **param device_name**

>     Device Name



> * **param port_number**

>     Port Number of the Switch



> * **param trunk_native_vlan**

>     Trunk Native Vlan Number for switch port



> * **param trunk_vlan_id**

>     Trunk Vlan Number for switch port



* **Parameters**

    **port_type** – Trunk Port



* **Returns**

    1 if Port Usage Trunk and Vlan Successfully configured else -1



#### device360_configure_ports_access_vlan(device_mac='', device_name='', port_numbers='', access_vlan_id='', port_type='Access Port', \*\*kwargs)

* This keyword will configure multiple ports to the port type “Access Port”


* Flow: Click Device –>Device 360 Window –> Configure –> Port Configuration–> interface –>

    Ports Usage and Vlan


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name


    * **port_numbers** – Port Numbers of the Switch [written as: “1,2,3…”]


    * **access_vlan_id** – Access Vlan Number for switch port


    * **port_type** – Access Port



* **Returns**

    1 if Ports Usage Access and Vlan Successfully configured else -1



#### device360_configure_ports_access_vlan_stack(port_numbers='', access_vlan_id='1', slot='', port_type='Access Port', \*\*kwargs)

* This keyword will configure multiple ports to the port type “Access Port”


* Assume that already in Device 360 Window


* Flow: Configure –> Port Configuration–> interface –> Ports Usage and Vlan


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name


    * **port_numbers** – Port Numbers of the Switch [written as: “1,2,3…”]


    * **access_vlan_id** – Access Vlan Number for switch port


    * **port_type** – Access Port


    * **slot** – The slot of the stack



* **Returns**

    1 if Ports Usage Access and Vlan Successfully configured else -1



#### device360_configure_ports_trunk_stack(port_numbers='', trunk_native_vlan='', trunk_vlan_id='', slot='', port_type='Trunk Port', \*\*kwargs)

* This keyword will configure multiple ports to Port Type: Trunk and assign a vlan value for a slot


* Flow: Device 360 Window –> Configure –> Port Configuration–> interface –> Ports Usage and Vlan Range


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name


    * **port_number** – Port Number of the Switch


    * **trunk_native_vlan** – Trunk Native Vlan Number for switch port


    * **trunk_vlan_id** – The vlan values [Can be any value EX: single , range ]


    * **port_type** – Trunk Port


    * **slot** – The current slot of the stack



* **Returns**

    1 if Ports Usage Trunk and Vlan range Successfully configured else -1



#### device360_configure_ports_trunk_vlan(port_numbers='', trunk_native_vlan='', trunk_vlan_id='', port_type='Trunk Port', \*\*kwargs)

* This keyword will configure multiple ports to Port Type: Trunk and assign a vlan value


* Assume that already in device360 window


* Flow: Configure –> Port Configuration–> interface –> Ports Usage and Vlan Range


* **Parameters**

    
    * **device_name** – Device Name


    * **port_number** – Port Number of the Switch


    * **trunk_native_vlan** – Trunk Native Vlan Number for switch port


    * **trunk_vlan_id** – The vlan values [Can be any value EX: single , range ]


    * **port_type** – Trunk Port



* **Returns**

    1 if Ports Usage Trunk and Vlan range Successfully configured else -1



#### device360_confirm_alarm_category_exists(alarm_cat, after_time=None)

* This keyword confirms the specified alarm category is present in the view, after the specified time.
If no time is specified, it just confirms the alarm is present.
It assumes the Device360 Window is open and on the Monitor> Alarms tab.


* Keyword Usage:

> 
> * `Device360 Confirm Alarm CategoryExists  ${ALARM}  ${AFTER_TIME}`


> * `Device360 Confirm Alarm CategoryExists  ${ALARM}`


* **Parameters**

    
    * **alarm_cat** – Alarm category to look for


    * **after_time** – Indicates at which point in time to start searching for the existence of the alarm
    (if not specified, it just checks for the existence of the alarm in general)



* **Returns**

    1 if the alarm is present (since “after_time”, if specified), else -1



#### device360_confirm_column_picker_column_selected(option, \*columns, select_page='', device_mac='', device_name='')

* This keyword confirms the list of columns are all selected in the column picker


* Keyword Usage:

    
        * Confirm Column Picker Column Selected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}


* **Parameters**

    **columns** – list of device columns that should be selected



* **Returns**

    returns 1 if all columns are selected in the column picker; else, -1



#### device360_confirm_event_description_contains(event_str, after_time=None)

* This keyword confirms the specified event text is present in the description field of the event, after the
specified time. If no time is specified, it just confirms the event is present.
It assumes the Device360 Window is open and on the Monitor> Events tab.


* Keyword Usage:

> 
> * `Device360 Confirm Event Exists  ${EVENT}  ${AFTER_TIME}`


> * `Device360 Confirm Event Exists  ${EVENT}`


* **Parameters**

    
    * **event_str** – String to look for in the event description


    * **after_time** – Indicates at which point in time to start searching for the existence of the event
    (if not specified, it just checks for the existence of the event in general)



* **Returns**

    1 if the event is present (since “after_time”, if specified), else -1



#### device360_confirm_port_disabled(port_name)

* This keyword confirms the specified port is disabked/off.
It assumes the Device360 Window is open and navigated to the Configure> Port Configuration view.


* Flow: Device 360 Window –> Click “Configure” tab –> Click “Port Configuration” link –> Confirm specified port is disabled/off


* Keyword Usage:

> 
> * `Device360 Confirm Port Disabled  ${PORT_NAME}`


* **Parameters**

    **port_name** – name of the port to confirm the state of



* **Returns**

    1 if port is disabled, else -1



#### device360_confirm_port_enabled(port_name)

* This keyword confirms the specified port is enabled/on.
It assumes the Device360 Window is open and navigated to the Configure> Port Configuration view.


* Flow: Device 360 Window –> Click “Configure” tab –> Click “Port Configuration” link –> Confirm specified port is enabled/on


* Keyword Usage:

> 
> * `Device360 Confirm Port Enabled  ${PORT_NAME}`


* **Parameters**

    **port_name** – name of the port to confirm the state of



* **Returns**

    1 if port is enabled, else -1



#### device360_confirm_ssh_enabled(device_mac='', device_name='')

* This keyword confirms if SSH is enabled for the specified device


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname) -> check if SSH is enabled


* Keyword Usage

> 
> * `Device360 Confirm SSH Enabled  device_mac=${AP1_MAC}`


> * `Device360 Confirm SSH Enabled  device_name=${AP1_NAME}`


* **Returns**

    1 if SSH enabled, -1 if SSH is disabled



#### device360_d360_view_100_rows_on_page()
This keyword press view 100 rows into d360 page
:return: 1 if button was selected; else -1


#### device360_decide_clientpage_or_device360_page()
This keyword is to decide whether we have landed at client page or Device360 page
:return: 1 if Device 360 page ,2 if Client 360 page else -1


#### device360_device_configuration_auto_template(device_mac, name_stack_template)
This function will go to D360 and press create auto template and name the template
:param device_mac: Mac of device
:param name_stack_template: Policy template name
:return: 1 if remain in the Create auto Template ; -1 else


#### device360_device_configuration_click_cancel()

* This keyword clicks Cancel in the Configure> Device Configuration view in the Device360 dialog window.
It assumes the Device360 Window is open and on the Configure> Device Configuration page.


* Flow: Device 360 Window –> Configure tab –> Device Configuration page –> Click Cancel


* Keyword Usage:

> 
> * `Device360 Device Configuration Click Cancel`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_device_configuration_select_template(device_mac, sw_template_name)
This function select the template into d360 and start update process


* **Parameters**

    
    * **device_mac** – Mac of device


    * **sw_template_name** – Policy template



* **Returns**

    1 if update is completed ; -1 else



#### device360_disable_port(port_name)

* This keyword disables the specified port.
It assumes the Device360 Window is open and navigated to the Configure> Port Configuration view.


* Flow: Device 360 Window –> Click “Configure” tab –> Click “Port Configuration” link –> Toggle Port State to Off


* Keyword Usage:

> 
> * `Device360 Disable Port  ${PORT_NAME}`


* **Parameters**

    **port_name** – name of the port to disable



* **Returns**

    1 if port was disabled, 2 if port was already disabled, else -1



#### device360_disable_ssh_connectivity(device_mac='', device_name='')

* This keyword disables SSH Connectivity for the specified device


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname) -> Click Disable SSH button


* Keyword Usage

> 
> * `Device360 Disable SSH CLI Connectivity  device_mac=${AP1_MAC}`


> * `Device360 Disable SSH CLI Connectivity  device_name=${AP1_NAME}`


* **Returns**

    SSH String



#### device360_disable_ssh_web_connectivity(device_mac='', device_name='', run_time=5)

* This keyword disables SSH WEB Connectivity


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Device360 Disable SSH Web Connectivity  device_mac=${AP1_MAC}`


> * `Device360 Disable SSH Web Connectivity  device_name=${AP1_NAME}`


* **Returns**

    1 if passed else -1



#### device360_enable_ssh_cli_connectivity(device_mac='', device_name='', run_time=5)

* This keyword enables SSH CLI Connectivity


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Get Device360 Enable SSH CLI Connectivity  device_mac=${AP1_MAC}    run_time=5`


> * `Get Device360 Enable SSH CLI Connectivity  device_name=${AP1_NAME}  run_time=10`


* **Returns**

    SSH String



#### device360_enable_ssh_web_connectivity(device_mac='', device_name='', run_time=5)

* This keyword enables SSH CLI Connectivity


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Device360 Enable SSH Web Connectivity  device_mac=${AP1_MAC}    run_time=5`


> * `Device360 Enable SSH Web Connectivity  device_name=${AP1_NAME}  run_time=10`


* **Returns**

    SSH String



#### device360_get_device_title()

* This keyword obtains the value of the device title in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Device Title`


* **Returns**

    value of the device title in the Device360 view



#### device360_get_port_icon_count()

* This keyword gets the number of port icons displayed in the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Port Icon Count`


* **Returns**

    number of port icons displayed in the Device360 view



#### device360_get_port_row(port_name)

* Get the port row object matching the specified port_name from Device360 –> Configure –> Port Configuration


* **Parameters**

    **port_name** – name of the port to return the row for



* **Returns**

    row element if row exists else return None



#### device360_get_row_specified_port_name(rows, port_name)

* Get the port row object matching the specified port_name


* **Parameters**

    **port_name** – name of the port to return the row for



* **Returns**

    row element if row exists else return None



#### device360_get_side_bar_active_since_information()

* This keyword gets the Active Since information from the left sidebar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Side Bar Active Since Information`


* **Returns**

    dictionary of “Active Since” information obtained from the left side bar of the Device360 view



#### device360_get_side_bar_cpu_usage()

* This keyword obtains the value of the CPU Usage from the left sidebar in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Side Bar CPU Usage`


* **Returns**

    value of the CPU Usage field from the left sidebar in the Device360 view



#### device360_get_side_bar_information()

* This keyword gets information from the left sidebar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Side Bar Information`


* **Returns**

    dictionary of information obtained from the left side bar of the Device360 view



#### device360_get_side_bar_memory_usage()

* This keyword obtains the value of the Memory Usage from the left sidebar in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Side Bar Memory Usage`


* **Returns**

    value of the Memory Usage field from the left sidebar in the Device360 view



#### device360_get_switch_system_information()

* This keyword gets the values from the system information page of the Device360 view for a switch.


* It is assumed that the Device360 window is open for a switch.


* Keyword Usage

> 
> * `Device360 Get Switch System Information`


* **Returns**

    dictionary of information obtained from the System Information page of the Device360 view



#### device360_get_top_bar_cpu_usage()

* This keyword obtains the value of the CPU Usage from the top bar in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Top Bar CPU Usage`


* **Returns**

    value of the CPU Usage field from the top bar in the Device360 view



#### device360_get_top_bar_information()

* This keyword gets information from the top bar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Top Bar Information`


* **Returns**

    dictionary of information obtained from the top bar of the Device360 view



#### device360_get_top_bar_last_update_time()

* This keyword gets information from the left sidebar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Top Bar Last Update Time`


* **Returns**

    last update time if successful, otherwise None



#### device360_get_top_bar_memory_usage()

* This keyword obtains the value of the Memory Usage from the top bar in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Top Bar Memory Usage`


* **Returns**

    value of the Memory Usage field from the top bar in the Device360 view



#### device360_get_top_bar_temperature()

* This keyword obtains the value of the Temperature field from the top bar in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Top Bar Temperature`


* **Returns**

    value of the Temperature field from the top bar in the Device360 view



#### device360_get_total_active_alarms_count()

* This keyword gets the total active alarms displayed in the Active Alarms panel of the Device360 view.


* It is assumed that the Device360 window is open and on the Overview tab.


* Keyword Usage

> 
> * `Device360 Get Total Active Alarms Count`


* **Returns**

    total number of active alarms displayed in the Device360 view



#### device360_get_voss_wireframe_cpu_utilization(device_mac='', device_name='')

* This keyword will get Wireframe CPU Utilization for VOSS Device in Device360 Page


* Flow: Click Device –>Device 360 Window –>CPU Usage ICON


* Keyword Usage:

> 
> * `Device360 Get VOSS Wireframe CPU Utilization  device_mac=${DEVICE_MAC}`


> * `Device360 Get VOSS Wireframe CPU Utilization  device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name



* **Returns**

    For success return CPU Usage Percentage Value else -1



#### device360_get_voss_wireframe_memory_utilization(device_mac='', device_name='')

* This keyword will get Wireframe Memory Utilization for VOSS Device in Device360 Page


* Flow: Click Device –>Device 360 Window –>Memory Usage ICON


* Keyword Usage:

> 
> * `Device360 Get VOSS Wireframe Memory Utilization  device_mac=${DEVICE_MAC}`


> * `Device360 Get VOSS Wireframe Memory Utilization  device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name



* **Returns**

    For success return Memory Usage Percentage Value else -1



#### device360_is_port_details_table_displayed()

* This keyword determines if the port details table is displayed in the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Is Port Details Table Displayed`


* **Returns**

    1 if port table is displayed, else 0



#### device360_is_ssh_disabled(device_mac='', device_name='')

* This keyword verifies if SSH Web Connectivity is disabled


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Device360 Is SSH Disabled  device_mac=${AP1_MAC}`


> * `Device360 Is SSH Disabled  device_name=${AP1_NAME}`


* **Parameters**

    
    * **device_mac** – device MAC address


    * **device_name** – device name



* **Returns**

    1 if is disabled, else -1



#### device360_is_ssh_enabled(device_mac='', device_name='')

* This keyword verifies if SSH Web Connectivity is enabled


* Flow : Manage–>Devices–>click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Device360 Is SSH Enabled  device_mac=${AP1_MAC}`


> * `Device360 Is SSH Enabled  device_name=${AP1_NAME}`


* **Parameters**

    
    * **device_mac** – device MAC address


    * **device_name** – device name



* **Returns**

    1 if is enabled, else -1



#### device360_left_click_on_port_icon(port)

* This keyword clicks on port icon in the Device360 view based on the specified port.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Click On Port Icon`


* **Port**

    Specifies the port value



* **Returns**

    Displayed Port icon name in the Device360 view



#### device360_navigate_to_device_configuration()

* This keyword navigates to the Configure> Device Configuration view in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Configure” tab –> Click “Device Configuration” link


* Keyword Usage:

> 
> * `Device360 Navigate to Device Configuration`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_navigate_to_monitor_clients()

* This keyword navigates to the Monitor> Clients view in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Monitor” tab –> Click “Clients” button


* Keyword Usage:

> 
> * `Device360 Navigate to Monitor Clients`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_navigate_to_monitor_diagnostics()

* This keyword navigates to the Monitor> Diagnostics view in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Monitor” tab –> Click “Diagnostics” button


* Keyword Usage:

> 
> * `Device360 Navigate to Monitor Diagnostics`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_navigate_to_monitor_overview()

* This keyword navigates to the Monitor> Overview view in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Monitor” tab –> Click “Overview” button


* Keyword Usage:

> 
> * `Device360 Navigate to Monitor Overview`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_navigate_to_port_configuration()

* This keyword navigates to the Configure> Port Configuration view in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Configure” tab –> Click “Port Configuration” link


* Keyword Usage:

> 
> * `Device360 Navigate to Port Configuration`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_navigate_to_switch_system_information()

* This keyword navigates to the System Information view in the Device360 dialog window.
It assumes the Device360 Window is open for a switch.


* Flow: Device 360 Window –> Click “System Information” button


* Keyword Usage:

> 
> * `Device360 Navigate to Switch System Information`

:param  None
:return: 1 if navigation was successful, else -1


#### device360_port_configuration_click_save_button()

* This keyword clicks on the SAVE PORT CONFIGURATION button


* It is assumed that the Device360 window is open in Configure in Port Configuration section.


* Keyword Usage

> 
> * `Device360 Port Configuration Click Save Button`


* **Returns**

    Click on SAVE PORT CONFIGURATION



#### device360_port_diagnostics_deselect_all_ports()

* This keyword clicks the ‘Deselect All Ports’ button on the Port Diagnostics page in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor> Diagnostics page.


* Keyword Usage:

> 
> * `Device360 Port Diagnostics Deselect All Ports`

:param  None
:return: 1 if button was clicked, else -1


#### device360_port_diagnostics_deselect_port(port_num)

* This keyword deselects the specified port on the Monitor> Diagnostics page.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Device360 Port Diagnostics Deselect Port    3`

:param  port_num    specifies which port to deselect
:return: none


#### device360_port_diagnostics_select_all_ports()

* This keyword clicks the ‘Select All Ports’ button on the Port Diagnostics page in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor> Diagnostics page.


* Keyword Usage:

> 
> * `Device360 Port Diagnostics Select All Ports`

:param  None
:return: 1 if button was clicked, else -1


#### device360_port_diagnostics_select_port(port_num)

* This keyword selects the specified port on the Monitor> Diagnostics page.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Device360 Port Diagnostics Select Port    3`

:param  port_num    specifies which port to select
:return: none


#### device360_power_details(device_mac='', device_name='')
> 
> * This keyword will get Power Supply Details in Device 360 from thunderbolt icon


> * Flow: Click Device –>Device 360 Window –>Thunderbolt ICON


> * Keyword Usage:


> * `Device360 Power Details      device_mac=${DEVICE_MAC}`


> * `Device360 Power Details      device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name



* **Returns**

    list with power supply details



#### device360_power_details_stack(slot, device_mac='', device_name='')
> 
> * This keyword will get Power Supply Details in Device 360 from thunderbolt icon


> * Flow: Click Device –>Device 360 Window –>Thunderbolt ICON


> * Keyword Usage:


> * `Device360 Power Details      device_mac=${DEVICE_MAC}`


> * `Device360 Power Details      device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Name



* **Returns**

    list with power supply details; else -1



#### device360_read_wired_clients_popup()
This keyword read the Wired client Popup
This keyword assumes that we should have clicked the wired client pop-up
Manage -> Devices -> Device 360 -> Clients -> Clickable client (clicked)
:return: client details in dict format if found else it will return client details with None
Client details: client mac,ipv4,ipv6,port speed,negotiated speed,vlan, port mode,


#### device360_refresh_page()

* Refreshes the Device 360 window by clicking the refresh page button.


* **Returns**

    1 if page was refreshed, -1 if not



#### device360_revert_port_configuration(select_column, port_name)
This keyword press the revert button for the specific row and column into device360 Port Configuration window
select_column : - Port Details : ‘port state’ , ‘port usage’ , ‘vlan’ , ‘description’

> 
> * Port Settings & Aggregation: ‘transmission’ , ‘speed’ , ‘flow’ , ‘transmit’ , ‘receive’ , ‘cdp’ , ‘client reporting’


> * STP: ‘stp status’ , ‘edge port’ , ‘bpdu protection’ , ‘priority’ , ‘path cost’


> * Storm Control: ‘broadcast’ , ‘unknown unicast’ , ‘multicast’ , ‘value’

port_name: Number of port . e.g 1/1 ; 2:1
E.g. :
device360_revert_port_configuration          flow        1:3

return: 1 if successful revert; else -1


#### device360_save_device_configuration()

* This keyword clicks the Save Device Configuration button on the Device Configuration page.


* It is assumed that the Device360 window is open and on the Device Configuration page.


* Flow : Device 360 Page -> Configure -> Device Configuration -> Save Device Configuration


* Keyword Usage

> 
> * `Device360 Save Device Configuration`


* **Returns**

    1 if the button was clicked, -1 if not



#### device360_search_event_and_confirm_event_description_contains(event_str, after_time=None)

* This keyword search event and then confirms that specified event text is present in the description field of the event, after the
specified time. If no time is specified, it just confirms the event is present.
It assumes the Device360 Window is open and on the Monitor> Events tab.
After search is done it confirms that the log is present only on first page of event list. If more logs are matching it returns the number of them


* Keyword Usage:

> 
> * `Device360 Search Event And Confirm Event Description Contains  ${EVENT}  ${AFTER_TIME}`


> * `Device360 Search Event And Confirm Event Description Contains  ${EVENT}`


* **Parameters**

    
    * **event_str** – String to look for in the event description


    * **after_time** – Indicates at which point in time to start searching for the existence of the event
    (if not specified, it just checks for the existence of the event in general)



* **Returns**

    1 if only one log (row in table) is found; If more logs (rows) are found it will be return the number of them; else -1



#### device360_select_alarms_view()

* This keyword clicks the Alarms link on the Monitor tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor tab.


* Flow: Device 360 Window –> Monitor tab –> Click “Alarms” link


* Keyword Usage:

> 
> * `Device360 Select Alarms View`

:param  None
:return: 1 if the Alarms view was selected, else -1


#### device360_select_day_time_range()

* This keyword selects the ‘Day’ time range in the Device360 dialog window.
It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range`

:param  None
:return: 1 if selection was successful, else -1


#### device360_select_day_time_range_eight_hours()

* This keyword selects the ‘8 Hours’ Day time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Day” time range.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range Eight Hours`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_day_time_range_four_hours()

* This keyword selects the ‘4 Hours’ Day time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Day” time range.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range Four Hours`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_day_time_range_hours_button(hours_value)

* This keyword selects the specified Day time range hours button in the Device360 dialog window.
It assumes the Device360 Window is open and a Day time range is selected.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range Hours Button    1`


> * `Device360 Select Day Time Range Hours Button    2`


> * `Device360 Select Day Time Range Hours Button    4`


> * `Device360 Select Day Time Range Hours Button    8`


> * `Device360 Select Day Time Range Hours Button    24`

:param  hours_value  string indicating which hours value to select (e.g., 1, 2, 4, 8, 24)
:return: 1 if the specified button was clicked, else -1


#### device360_select_day_time_range_one_hour()

* This keyword selects the ‘1 Hour’ Day time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Day” time range.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range One Hour`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_day_time_range_twenty_four_hours()

* This keyword selects the ‘24 Hours’ Day time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Day” time range.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range Twenty Four Hours`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_day_time_range_two_hours()

* This keyword selects the ‘2 Hours’ Day time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Day” time range.


* Keyword Usage:

> 
> * `Device360 Select Day Time Range Two Hours`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_events_view()

* This keyword clicks the Events link on the Monitor tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor tab.


* Flow: Device 360 Window –> Monitor tab –> Click “Events” link


* Keyword Usage:

> 
> * `Device360 Select Events View`

:param  None
:return: 1 if the Events view was selected, else -1


#### device360_select_month_time_range()

* This keyword selects the ‘Month’ time range in the Device360 dialog window.
It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.


* Keyword Usage:

> 
> * `Device360 Select Month Time Range`

:param  None
:return: 1 if selection was successful, else -1


#### device360_select_month_time_range_days_button(days_value)

* This keyword selects the specified Month time range days button in the Device360 dialog window.
It assumes the Device360 Window is open and a Month time range is selected.


* Keyword Usage:

> 
> * `Device360 Select Month Time Range Days Button    7`


> * `Device360 Select Month Time Range Days Button    14`


> * `Device360 Select Month Time Range Days Button    30`


> * `Device360 Select Month Time Range Days Button    90`

:param  days_value  string indicating which days value to select (e.g., 7, 14, 30, 90)
:return: 1 if the specified button was clicked, else -1


#### device360_select_month_time_range_fourteen_days()

* This keyword selects the ‘14 Days’ time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Month” time range.


* Keyword Usage:

> 
> * `Device360 Select Month Time Range Fourteen Days`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_month_time_range_ninety_days()

* This keyword selects the ‘90 Days’ time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Month” time range.


* Keyword Usage:

> 
> * `Device360 Select Month Time Range Ninety Days`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_month_time_range_seven_days()

* This keyword selects the ‘7 Days’ Month time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Month” time range.


* Keyword Usage:

> 
> * `Device360 Select Month Time Range Seven Days`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_month_time_range_thirty_days()

* This keyword selects the ‘30 Days’ time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Month” time range.


* Keyword Usage:

> 
> * `Device360 Select Month Time Range Thirty Days`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_time_range(time_range)

* This keyword selects the specified time range in the Device360 dialog window.
It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.


* Keyword Usage:

> 
> * `Device360 Select Time Range    Day`


> * `Device360 Select Time Range    Week`


> * `Device360 Select Time Range    Month`

:param  time_range  indicates which time range value to select (e.g., Day, Week, Month)
:return: 1 if the specified time range was selected, else -1


#### device360_select_week_time_range()

* This keyword selects the ‘Week’ time range in the Device360 dialog window.
It assumes the Device360 Window is open and on a tab with the Time Range drop down selector.


* Keyword Usage:

> 
> * `Device360 Select Week Time Range`

:param  None
:return: 1 if selection was successful, else -1


#### device360_select_week_time_range_days_button(days_value)

* This keyword selects the specified Week time range days button in the Device360 dialog window.
It assumes the Device360 Window is open and a Week time range is selected.


* Keyword Usage:

> 
> * `Device360 Select Week Time Range Days Button    1`


> * `Device360 Select Week Time Range Days Button    2`


> * `Device360 Select Week Time Range Days Button    7`

:param  days_value  string indicating which days value to select (e.g., 1, 2, 7)
:return: 1 if the specified button was clicked, else -1


#### device360_select_week_time_range_one_day()

* This keyword selects the ‘1 Day’ Week time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Week” time range.


* Keyword Usage:

> 
> * `Device360 Select Week Time Range One Day`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_week_time_range_seven_days()

* This keyword selects the ‘7 Days’ Week time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Week” time range.


* Keyword Usage:

> 
> * `Device360 Select Week Time Range Seven Days`

:param  None
:return: 1 if button was clicked, else -1


#### device360_select_week_time_range_two_days()

* This keyword selects the ‘2 Days’ Week time range in the Device360 dialog window.
It assumes the Device360 Window is open and on the “Week” time range.


* Keyword Usage:

> 
> * `Device360 Select Week Time Range Two Days`

:param  None
:return: 1 if button was clicked, else -1


#### device360_set_device_function(value='AP')

* This keyword sets the Device Function value on the Device Configuration page.


* It is assumed that the Device360 window is open.


* Flow : Device 360 Page -> Configure -> Device Configuration


* Keyword Usage

> 
> * `Device360 Set Device Function  AP`


> * `Device360 Set Device Function  ApAsRouter`


* **Returns**

    1 if the selection was made, -1 if not



#### device360_set_network_policy(network_policy='default')

* This keyword sets a custom network policy on the Device Configuration page.


* It is assumed that the Device360 window is open.


* Flow : Device 360 Page -> Configure -> Device Configuration


* Keyword Usage

> 
> * `device360_set_network_policy  network_policy=PPSK_POL`


* **Returns**

    1 if the selection was made, -1 if not



#### device360_speed_overview(port_name)
This keyword checks the status of speed for a port in Overview status
:param port_name: a string with the specific port
-Keyword Usage:

> device360_speed_overview    1/1


* **Returns**

    a string with the status of speed
    -1 if the status port was not found



#### device360_stack_devcfg_fetch_snmp_location()

* This keyword gets the value of snmp location from device configuration page of D360


* Keyword Usage

> 
> * `Device360 Device Config Snmp Location`


* **Returns**

    assigned snmp location



#### device360_standalone_devcfg_fetch_snmp_location()

* This keyword gets the value of snmp location from device configuration page of D360


* Keyword Usage

> 
> * `Device360 Device Config Snmp Location`


* **Returns**

    assigned snmp location



#### device360_transmission_mode_overview(port_name)
This keyword checks the status of transmission mode for a port in Overview status
:param port_name: a string with the specific port
-Keyword Usage:

> device360_transmission_mode_overview    1/1


* **Returns**

    a string with the status of transmission mode (“Full-Duplex/Half-Duplex”)
    -1 if the status port was not found



#### edit_port_type(template_values, port, verify_summary=True)
This Keyword edit a port type and verify the summary page .


* **Parameters**

    **template_values** – 


A dictionary with below structure:

Each element from dictionary template_values has the following format:

    ‘setting name’: [configured_value, check_summary_value]

To change the value of a setting, use the following syntax:

    template_voss_auto_sense_on[‘setting name’][0] = ‘configured_value’

To not configure an element from dictionary:

    template_voss_auto_sense_on[‘setting name’][0] = None

To check the value of a setting into summary page, use the following sintax:

    template_voss_auto_sense_on[‘setting name’][1] = ‘check_summary_value’

To not verify an element from dictionary into summary page :

    template_voss_auto_sense_on[‘setting name’][1] = None

To press next buttom use into dictionary an element like this : ‘page2 accessVlanPage’:[“next_page”, None],

template_values=                {‘name’: [“port type name”, ‘port type name’],

    > ‘description’: [“add_description”, “add_description”],
    > ‘status’:[‘click’, ‘off’],          #[‘click’/None, ‘on’/’off’/None]
    > ‘auto-sense’:[‘click’,None],       #[‘click’/None, None]
    > ‘port usage’:[‘trunk port’, ‘trunk’],

    > > #[‘trunk port’/’access port’/None, ‘trunk’/’access’/’auto_sense’/None]

    > #’page2 accessVlanPage’:[“next_page”, None],       # used for access ports
    > #’vlan’:[‘40’, ‘40’],                       # used for access ports

    > ‘page2 trunkVlanPage’: [“next_page”, None],
    > ‘native vlan’: [‘50’, ‘50’],     # used for trunk ports
    > ‘allowed vlans’: [‘60’, ‘60’],   # used for trunk ports [‘all’/None, ‘all’/None]

    > ‘page3 transmissionSettingsPage’: [“next_page”, None],
    > ‘transmission type’: [‘auto’,’auto’],

    > > #[‘auto’/’Half-Duplex’/’Full-Duplex’, ‘auto’/’Half_Duplex’/’Full_Duplex’/None]

    > ‘transmission speed’:[‘auto’,’auto’],

    >     #[‘auto’/’10 Mbps’/’100 Mbps’/None, ‘auto’/’10 Mbps’/’100 Mbps’/None]

    > ‘cdp receive’:[None, ‘off’],        # [‘click’/’None’, ‘on’/’off’/None]
    > ‘lldp transmit’:[‘click’, ‘off’],   # [‘click’/’None’, ‘on’/’off’/None]
    > ‘lldp receive’:[None, ‘off’],       # [‘click’/’None’, ‘on’/’off’/None]

    > ‘page4 stpPage’: [“next_page”, None],
    > ‘stp enable’:[‘click’, ‘enabled’],      #[‘click’/None, ‘on’/’off’/None]
    > ‘edge port’: [‘click’, ‘enabled’],      #[‘click’/None, ‘on’/’off’/None]
    > ‘bpdu protection’:[None, ‘disabled’],   #[‘click’/None, ‘on’/’off’/None]
    > ‘priority’:[‘32’, ‘32’],

    > > #[‘0’/’16’/’32’/’48’…/’192’/None, ‘0’/’16’/’32’/’48’…/’192’/None]

    > ‘path cost’:[‘50’, ‘50’],   #[‘1 - 200000000’/None, ‘1 - 200000000’/None]

    > ‘page5 stormControlSettingsPage’: [“next_page”, None],
    > ‘broadcast’:[None, ‘disabled’],         #[‘click’/None, ‘enabled’/’disabled’/None]
    > ‘unknown unicast’:[None, ‘disabled’],   #[None, ‘disabled’/None]
    > ‘multicast’:[None, ‘disabled’],         #[‘click’/None, ‘enabled’/’disabled’/None]
    > ‘rate limit type’:[None,’pps’],         #[None, ‘pps’/None]
    > ‘rate limit value’: [‘65535’, ‘65535’], #[‘0-65535’/None, ‘0-65535’/None]

    > #for VOSS
    > ‘page6 pseSettingsPage’: [“next_page”, None],
    > ‘PSE profile’:[None,None],

    > > #[‘default-pse-vsp’/’None’, ‘default-pse-vsp’/’None’]

    > ‘poe status’:[None,’on’],           #[‘click’/None, ‘on’/’off’/None]

    > ‘page7 summaryPage’: [“next_page”, None]

    > #==========================================
    > #Only for EXOS
    > ‘page6 ELRPSettingsPage’: [“next_page”, None],
    > ‘elrp status’: [‘click’, ‘enabled’],      #[‘click’/None, ‘on’/’off’/None]

    > ‘page7 pseSettingsPage’: [“next_page”, None],
    > ‘PSE profile’:[None,None],

    > > #[‘default-pse-vsp’/’None’, ‘default-pse-vsp’/’None’]

    > ‘poe status’:[None,’on’],           #[‘click’/None, ‘on’/’off’/None]

    > ‘page8 summaryPage’: [“next_page”, None]

    }


* **Parameters**

    
    * **port** – the port where new port type will be created


    * **verify_summary** – True if configured values will be verify on summary page. False if verification on summary


page will be skipped
:return: 1 if new port type was successfully edited and summary page displays correct values  ; else -1


#### exit_d360_Page()
This keyword close the d360 page
:return: 1 all time


#### get_device360_overview_information(device_mac='', device_name='')

* This keyword gets information from device360 page eg Model, Serial Number, etc


* Flow : Manage–>Devices–>click on XMC hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Get Device360 Overview Information   device_mac=${MAC}`


> * `Get Device360 Overview Information   device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **device_mac** – MAC Address of the device to access the D360 view for


    * **device_name** – Host Name of the device to access the D360 view for



* **Returns**

    dictionary of information from the Overview tab of the Device360 view



#### get_device_system_information(device_mac=None, device_name=None)

* This keyword gets Device system information from device360 page using Device Mac and Name


* Flow : Manage–> Devices –>click on hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Get Device System Information  device_mac=${AP1_MAC}`


> * `Get Device System Information  device_name=${AP1_NAME}`


* **Returns**

    dictionary of system information



#### get_exos_information()

* This keyword gets EXOS Switch information from device360 page


* It Assumes That Already Navigated to Device360 Page


* Flow : Device 360 Page


* Keyword Usage

> 
> * `Get ExOS Information`


* **Returns**

    dictionary of ExOS Switch information



#### get_exos_switch_360_information(device_mac='', device_name='')

* This keyword gets EXOS Switch information from device360 page ie Model,Serial Number etc


* Flow : Manage–>Devices–>click on SWitch hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Get ExOS Switch 360 Information   device_name=${SW1_NAME}`


> * `Get ExOS Switch 360 Information   device_mac=${SW1_MAC}`


* **Parameters**

    
    * **device_mac** – ExOS SWitch MAC Address


    * **device_name** – ExOS SWitch Name



* **Returns**

    dictionary of ExOS Switch information



#### get_hostname_name_from_device_360(device_mac=None, device_name=None)

* This keyword gets hostname from device360 page by clicking on hyperlink(MAC/hostname)

-Flow: Manage –>Devices –> click on device MAC or Host name hyperlink.
- Keyword Usage:

> 
> * `${HOST_NAME}=                Get Hostname Name From Device 360           ${DEVICE_MAC}`


* **Parameters**

    
    * **device_mac** – MAC of the device


    * **device_name** – Host name of the device



* **Returns**

    host name



#### get_overview_information()

* This keyword gets information from the Monitor> Overview page of the Device360 view


* It is assumed that the Device360 window is open and on the Monitor> Overview page


* Flow : Device 360 Page -> Monitor -> Overview


* Keyword Usage

> 
> * `Get Overview Information`


* **Returns**

    dictionary of information obtained from the Monitor> Overview page of the Device360 view



#### get_status_interface(device_serial=None, interface_name=None)

* This keyword  gets status interface

-Flow: Manage –> Devices –> Select the device row based on the passed device serial –> Utilities –> Status –> Interface –> select interface and get the output
- Keyword Usage:

> 
> * `${RESULT}=        Get Status Interface         ${DEVICE_SERIAL}       ${INTERFACE}`


* **Parameters**

    
    * **device_serial** – serial of the device


    * **interface_name** – name of the interface



* **Returns**

    returns the output of the interface



#### get_status_interface_list(device_serial=None)

* This keyword  gets interfaces list

-Flow: Manage –> Devices –> Select the device row based on the passed device serial –> Utilities –> Status –> Interface –> interface menu
- Keyword Usage:

> 
> * `${RESULT}=        Get Status Interface         ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial of the device



* **Returns**

    returns the list of interface names



#### get_supplemental_cli(name_s_cli, cli_commands='')
This keyword will add or edit a supplemental cli profile with cli commands in D360
- Keyword Usage

> 
> * `Get supplemental cli       ${NAME_CLI}     ${CLI_COMMANDS}`


* **Parameters**

    
    * **name_s_cli** – Name of the supplemental cli profile


    * **cli_commands** – list of CLI commands separated by comma



* **Returns**

    1 if supplemental cli profile save successfully else -1



#### get_switch_device360_port_table_information(device_mac='', device_name='', port_number='')

* This keyword gets EXOS/VOSS Switch Port table information from device360 page


* Flow : Manage –> Devices–> Select Device–>Device 360 Page


* Keyword Usage

> 
> * 

> ```
> ``
> ```

> Get Switch Device360 Port Table Information  device_mac={DEVICE_MAC}  port_number={PORT_NUMBER} \`\`


> * 

> ```
> ``
> ```

> Get Switch Device360 Port Table Information  device_name={DEVICE_NAME}  port_number={PORT_NUMBER} \`\`


> * **param device_mac**

>     Device Mac Address



> * **param device_name**

>     Device Name



> * **param port_number**

>     Port Number of the Switch



* **Returns**

    Dictionary of Port Table Information if port found else -1



#### get_system_info()

* This keyword gets system information from device360 page


* Keyword Usage

> 
> * `Get System Info`


* **Returns**

    dictionary of system information



#### get_voss_device360_device_configuration_information(device_mac='', device_name='')

* This keyword gets VOSS Switch information from device360 page ie Model,Serial Number etc


* Flow : Manage–>Devices–>click on VOSS Switch hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Get VOSS Switch 360 Information   device_mac=${SW1_MAC}`


> * `Get VOSS Switch 360 Information   device_name=${SW1_NAME}`


* **Parameters**

    
    * **device_mac** – VOSS Switch MAC Address


    * **device_name** – VOSS SWitch Name



* **Returns**

    dictionary of VOSS Switch information



#### get_voss_device360_overview_information(device_mac='', device_name='')

* This keyword gets VOSS Switch information from device360 page ie Model,Serial Number etc


* Flow : Manage–>Devices–>click on VOSS Switch hyperlink(MAC/hostname)


* Keyword Usage

> 
> * `Get VOSS Switch 360 Information   device_mac=${SW1_MAC}`


> * `Get VOSS Switch 360 Information   device_name=${SW1_NAME}`


* **Parameters**

    
    * **device_mac** – VOSS Switch MAC Address


    * **device_name** – VOSS SWitch Name



* **Returns**

    dictionary of VOSS Switch information



#### get_voss_device_configuration_information()

* This keyword gets VOSS Switch information from the Configure> Device Configuration page of the Device360 view


* It is assumed that the Device360 window is open and on the Configure> Device Configuration page


* Flow : Device 360 Page -> Configure -> Device Configuration


* Keyword Usage

> 
> * `Get VOSS Device Configuration Information`


* **Returns**

    dictionary of VOSS Switch information obtained from the Configure> Device Configuration page of the Device360 view



#### get_voss_overview_information()

* This keyword gets VOSS Switch information from the Monitor> Overview page of the Device360 view


* It is assumed that the Device360 window is open and on the Monitor> Overview page


* Flow : Device 360 Page -> Monitor -> Overview


* Keyword Usage

> 
> * `Get VOSS Overview Information`


* **Returns**

    dictionary of VOSS Switch information obtained from the Monitor> Overview page of the Device360 view



#### interface_port_speed(port)
This keyword checks the status of speed for an interface by right click on interface in Device360
:param port: a string with the number(index) of interface
-Keyword Usage:

> 
> * interface_port_speed        20


> * interface_port_speed        mgmt


* **Returns**

    a string with the status of speed
    -1 the interface was not found



#### interface_transmission_mode(interface)
This keyword checks the status of transmission mode for an interface by right click on interface in Device360
:param interface: a string with the number(index) of interface
-Keyword Usage:

> 
> * interface transmission mode        20


> * interface transmission mode        mgmt


* **Returns**

    a string with the status of transmission mode (“Full-Duplex/Half-Duplex”)
    -1 the interface was not found



#### port_type_verify_summary(template_values)
This keyword verify the summary after configure new port type.
See edit_port_type and create_new_port_type
:param template_values: a dictionary (See edit_port_type and create_new_port_type )
:return: 1 if informations from summary page are correct ; else -1


#### return_stack_units_number(units_serials)

#### search_for_vlan_subnetworks_type_in_row_table(\*searched_values)

* This keyword searches any multiple values in the subnetworks row table
The values must match to a row in table
It assumes the Device360 Window is open and on the Configure tab.


* Flow: Device 360 Window –> Configure tab –> Click “DHCP & IP Address” link


* Keyword Usage:

> 
> * `search_for_vlan_subnetworks_type_in_row_table   192.168.167.0/25  MGMT  10`


* **Parameters**

    **\*searched_values** – list of searched values




* **Returns**

    1 if all values are found in table



#### select_configure_tab()

* This keyword clicks the Configure tab in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Configure” tab


* Keyword Usage:

> 
> * `Select Configure Tab`

:param  None
:return: 1 if the Configure tab was clicked, else -1


#### select_device_configuration_view()

* This keyword clicks the Device Configuration link on the Configure tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Configure tab.


* Flow: Device 360 Window –> Configure tab –> Click “Device Configuration” link


* Keyword Usage:

> 
> * `Select Device Configuration View`

:param  None
:return: 1 if the Device Configuration view was selected, else -1


#### select_dhcp_ip_address_view()

* This keyword clicks the DHCP & IP Address link on the Configure tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Configure tab.


* Flow: Device 360 Window –> Configure tab –> Click “DHCP & IP Address” link


* Keyword Usage:

> 
> * `select_dhcp_ip_address_view`

:param  None
:return: 1 if the select_dhcp_ip_address_view was selected, else -1


#### select_monitor_clients()

* This keyword clicks the Clients button on the Monitor tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor tab.


* Flow: Device 360 Window –> Monitor tab –> Click “Clients” button


* Keyword Usage:

> 
> * `Select Monitor Clients`

:param  None
:return: 1 if Monitor> Clients was selected, else -1


#### select_monitor_diagnostics()

* This keyword clicks the Diagnostics button on the Monitor tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor tab.


* Flow: Device 360 Window –> Monitor tab –> Click “Diagnostics” button


* Keyword Usage:

> 
> * `Select Monitor Diagnostics`

:param  None
:return: 1 if Monitor> Diagnostics was selected, else -1


#### select_monitor_overview()

* This keyword clicks the Overview button on the Monitor tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Monitor tab.


* Flow: Device 360 Window –> Monitor tab –> Click “Overview” button


* Keyword Usage:

> 
> * `Select Monitor Overview`

:param  None
:return: 1 if Monitor> Overview was selected, else -1


#### select_monitor_tab()

* This keyword clicks the Monitor tab in the Device360 dialog window.
It assumes the Device360 Window is open.


* Flow: Device 360 Window –> Click “Monitor” tab


* Keyword Usage:

> 
> * `Select Monitor Tab`

:param  None
:return: 1 if the Monitor tab was clicked, else -1


#### select_port_configuration_view()

* This keyword clicks the Port Configuration link on the Configure tab in the Device360 dialog window.
It assumes the Device360 Window is open and on the Configure tab.


* Flow: Device 360 Window –> Configure tab –> Click “Port Configuration” link


* Keyword Usage:

> 
> * `Select Port Configuration View`

:param  None
:return: 1 if the Port Configuration view was selected, else -1


#### select_stack_unit(slot, \*\*kwargs)
This keyword will select a slot from a stack in Device360
:param slot: The slot which will be selected
:return: 1 if the slot was selected; else -1


#### select_switch_system_information()

* This keyword clicks the System Information button in the Monitoring view of the Device360 dialog window.
This view applies to a switch, and is different from an AP which would have a Monitor and Configure tab.
It assumes the Device360 Window is open and on the Monitoring view for a switch.


* Flow: Device 360 Window –> Click “System Information” button


* Keyword Usage:

> 
> * `Select Switch System Information`

:param  None
:return: 1 if System Information was selected, else -1


#### test_device_cli(command, device_serial=None, device_mac=None, max_time=180, interval_time=20, delay=30)
This function is used for testing WEB CLI from extauto.xiq. A command or a list of commands can be send from XIQ to exos
device

test device cli  ${SW2_SERIAL}  ping 127.0.0.1,show iq,show vlan
test device cli  ${SW2_SERIAL}  ping 127.0.0.1


* **Parameters**

    
    * **device_serial** – Serial for exos device


    * **command** – a CLI command or a list of commands i.g.


    * **max_time** – The max period time of waiting to appear the output of command


    * **interval_time** – Time interval between two consecutive output checks


    * **delay** – Delay after send the command



* **Returns**

    output of command ; else -1



#### transmission_mode_overview_table(port_name)
This keyword checks the status of transmission mode for a port in Overview status
:param port_name: a string with the specific port
-Keyword Usage:

> transmission_mode_overview_table    1/1


* **Returns**

    a string with the status of transmsission mode (“Full-Duplex/Half-Duplex”)
    -1 if the status port was not found



#### transmission_mode_right_click_menu(interface)
This keyword checks the status of transmission mode for an interface by click on interface in Device360
:param port: a string with the number(index) of interface
-Keyword Usage:

> 
> * transmission_mode_right_click_menu        20


> * transmission_mode_right_click_menu        mgmt


* **Returns**

    a string with the status of transmission mode (“Full-Duplex/Half-Duplex”)
    -1 the interface was not found



#### wifi_status_summary(device_serial=None)

* This keyword  gets wifi status summary

-Flow: Manage –> Devices –>Select the device row based on the passed device serial –> Click on Utilities –> Status –> Wifi Status Summary –> station
- Keyword Usage:

> 
> * 

> ```
> ``
> ```

> ${RESULT}=        Wifi Status Summary         ${DEVICE_SERIAL}  \`\`


* **Parameters**

    **device_serial** – serial of the device



* **Returns**

    returns the output of the wifi status summary


## extauto.xiq.flows.manage.Device360Stack module


### _class_ extauto.xiq.flows.manage.Device360Stack.Device360Stack()
Bases: `Device360WebElements`


#### device360_get_stack_side_bar_information()

* This keyword gets information from the left sidebar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Stack Side Bar Information`


* **Returns**

    dictionary of information obtained from the left side bar of the Device360 view



#### device360_get_stack_slot_overview_information(slot_number)

* This keyword gets information from the top bar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Stack Slot Overview Information   1`


* **Returns**

    dictionary of information obtained from the top bar of the Device360 view



#### device360_get_stack_slot_top_bar_last_update_time(slot_number)

* This keyword gets information from the left sidebar of the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Get Stack Slot Top Bar Last Update Time     1`


* **Returns**

    last update time if successful, otherwise None



#### device360_get_stack_slot_top_bar_temperature(slot_number)

* This keyword obtains the value of the Temperature field from the top bar in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Stack Slot Top Bar Temperature   1`


* **Returns**

    value of the Temperature field from the top bar in the Device360 view



#### device360_get_title_stack_info()

* This keyword obtains the value of the Stack Members in device title in the Device360 view.


* Keyword Usage

> 
> * `Device360 Get Title Stack Info`


* **Returns**

    value of Stack Members in the device title in the Device360 view



#### device360_stack_get_port_icon_count()

* This keyword gets the number of port icons displayed for Stack in the Device360 view.


* It is assumed that the Device360 window is open.


* Keyword Usage

> 
> * `Device360 Stack Get Port Icon Count`


* **Returns**

    number of port icons displayed in the Device360 view



#### device360_stack_overview_select_port(port_num)

* This keyword selects the specified port on the Monitor> Diagnostics page.
It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.


* Keyword Usage:

> 
> * `Device360 Stack Overview Select Port    3`

:param  port_num    specifies which port to select
:return: none


#### get_stack_port_information_on_device(spawn, port_num)

* This keyword gets information from the the Device through cli.


* It is assumed that the Device spawn is open.


* Keyword Usage

> 
> * `Get Stack Port Information on Device  ${SW_SPAWN}    1:4`


* **Returns**

    dictionary of information obtained from the Device



#### get_stack_port_table_information(port_num)

* This keyword gets Stack port table information from device360 page


* It Assumes That Already Navigated to Device360 Page and Port is selected


* Flow : Device 360 Page


* Keyword Usage

> 
> * `Get Stack Port Table Information`


* **Returns**

    dictionary of Stack Switch information



#### get_stack_system_information(slot_number)

* This keyword gets Stack Switch information from device360 page


* It Assumes That Already Navigated to Device360 Page


* Flow : Device 360 Page


* Keyword Usage

> 
> * `Get Stack System Information   1`


* **Returns**

    dictionary of Stack Switch information



#### get_switch_stack_device360_port_table_information(device_mac='', device_name='', port_number='')

* This keyword gets EXOS/VOSS Switch stack Port table information from device360 page


* Flow : Manage –> Devices–> Select Device stack–>Device stack 360 Page


* Keyword Usage

> 
> * 

> ```
> ``
> ```

> Get Switch Stack Device360 Port Table Information  device_mac={DEVICE_MAC}  port_number={PORT_NUMBER} \`\`


> * 

> ```
> ``
> ```

> Get Switch Stack Device360 Port Table Information  device_name={DEVICE_NAME}  port_number={PORT_NUMBER} \`\`


> * **param device_mac**

>     Device Stack Mac Address



> * **param device_name**

>     Device Stack Name



> * **param port_number**

>     Port Number of the Switch Stack



* **Returns**

    Dictionary of Port Table Information if port found else -1


## extauto.xiq.flows.manage.DeviceCliAccess module


### _class_ extauto.xiq.flows.manage.DeviceCliAccess.DeviceCliAccess()
Bases: `DeviceCliAccessElements`


#### ap_operating_channel(cli_op)
> 
> * Verifing the Ap Operating channel


> * Keyword Usage:

>     =>  ${channel}=     Ap Operating Channel     ${cli_output}

Note

    > =>  ${cli_output}=              Send            ${SPAWN}    sho interface | in Wifi1.1


    * **param cli_op**

        get the channel information from send command



    * **return**

        will return the current operating channel if AP is UP,
        else return -1



#### check_cli_output_of_previous_ap_in_current_ap_cli_output(device_host_names='', cmd='show hw-info')

* This keyword is used to validate the CFD-4322


* To check The CLI Access output for the previous AP is displayed for the current AP if the Apply button is clicked too quickly


* Keyword Usage:

> 
> * Check Clo Output Of Previous Ap In Current Ap Cli Output   device_serials=${AP1_SERIAL},${AP2_SERIAL}\`\`


* **Parameters**

    
    * **device_host_names** – comma separated host names of the devices to select device rows


    * **cmd** – cmd to execute



* **Returns**

    returns 1 if successful



#### send_cmd_on_device_advanced_cli(device_serial='', cmd='show version')

* This keyword is used to execute the command on device advanced cli window


* It will Return the executed command output in str format


* Flow:

> 
> * Navigate to Manage –> Device –> Select Device –> Actions –> Advanced –> CLi Access


* Keyword Usage:

> 
> * `Send Cmd On Device Advanced Cli   ${DEVICE1_SERIAL}   cmd=${CMD}`


* **Parameters**

    
    * **device_serial** – device serial number


    * **cmd** – cmd to execute on the device advanced cli



* **Returns**

    


* if command is valid return the str format of the command output


* if command is invalid return -1


#### verify_command(ui_output='default', cli_output='default', cmd='default')

* This keyword  verifies whether UI output and CLI output match.


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> ${RESULT}=        Verify UI Command         ${UI_OUTPUT}      ${CLI_OUTPUT}       ${CMD}  \`\`


* **Parameters**

    
    * **ui_output** – output of command in UI


    * **cli_output** – output of command in cli


    * **cmd** – command that is executed



* **Returns**

    returns 1 if successful


## extauto.xiq.flows.manage.DeviceConfig module


### _class_ extauto.xiq.flows.manage.DeviceConfig.DeviceConfig()
Bases: `DeviceConfigElements`


#### change_device_host_name(new_host_name, device_mac='', device_name='')

* This keyword will Change the Host Name of the Device


* Flow : Click AP MAC or Name Link –> Configure–>Device Configuration–> Host Name


* Keyword Usage:

> 
> * `Change Device Host Name    ${HOST_NAME}    $device_mac=${AP1_MAC}`

> > 
> > * `Change Device Host Name    ${HOST_NAME}   $device_name=${AP1_NAME}`


* **Parameters**

    
    * **new_host_name** – Device Host Name to change


    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name



* **Returns**

    1 in case of success else -1



#### change_multiple_devices_wireless_interface_radio_status(device_serials='', interface_name='', status='')

* This Keyword will Change Status(ON/OFF) of Wireless Interface for Multiple Devices


* Flow:MANAGE–>Devices–>Select Multiple devices–>Edit–>Interface settings–>wireless interfaces–>Radio Status


* Keyword Usage:

> 
> * `Change Multiple Devices Wireless Interface Radio Status  device_serials=${AP1_SERIAL},${AP2_SERIAL}  interface_name=${INTERFACE_NAME}  status=${STATUS_ON}`


* **Parameters**

    
    * **device_serials** – Devices Serial Numbers Seperated by Comma


    * **interface_name** – Wireless Interface Name


    * **status** – WiFi interface radio status ie ON or OFF



* **Returns**

    1 if WiFi radio Status Updated successfully



#### change_single_device_wireless_interface_radio_status(device_serial=None, interface_name=None, status=None)

* This Keyword will Change Status(ON/OFF) of Wireless Interface of a single device


* Flow:MANAGE–>Devices–>Select Multiple devices–>Edit–>Interface settings–>wireless interfaces–>Radio Status


* Keyword Usage:

    
        * `Change Single Device Wireless Interface Radio Status  device_serial=${AP1_SERIAL}  interface_name=${INTERFACE_NAME}  status=${STATUS_ON}`

    > 
    > * **param device_serial**

    >     Device Serial Number



    > * **param interface_name**

    >     Wireless Interface Name



    > * **param status**

    >     WiFi interface radio status ie ON or OFF



    > * **return**

    >     1 if WiFi radio Status Updated successfully



#### change_transmission_power_to_multiple_devices(device_serials='', interface_name='', transmission_mode='', power_value='')

* This Keyword will Change the Transmission of Wireless Interface


* Go To MANAGE–>Devices–>Select All devices–>Edit–>Interface settings–>wireless interfaces


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Change Transmission Power To Multiple Devices  device_serials=${AP1_SERIAL},${AP2_SERIAL}

>     interface_name=${INTERFACE_NAME}  transmission_mode=${MANUAL}  power_value=${VALUE}\`\`


* **Parameters**

    
    * **device_serials** – Device Serial Numbers seperated by comma


    * **interface_name** – Wireless Interface Name


    * **transmission_mode** – Transmission Mode ie Manual or Auto


    * **power_value** – name of the network to deploy



* **Returns**

    1 if Transmission Power Updated successfully



#### check_config_audit_delta_match(serial='')

* This keyword is used to select the check device configuration in Delta in Manage –> Device page


* Assumes that navigated to the Manage –> Device page


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Check Config Audit Delta Match     serials=${DEVICE1_SERIAL} \`\`


* **Parameters**

    **serial** – device serial number



* **Returns**

    1 in case of success else -1



#### check_device_configured_template(device_mac='', device_name='')

* This keyword will get device template configured it on Device


* Flow : Click AP MAC Link –> Configure–>Interface Settings—>Device Template


* Keyword Usage:

> 
> * `Check Device Configured Template  device_mac=${AP1_MAC}`


> * `Check Device Configured Template  device_name=${AP1_NAME}`


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name to change



* **Returns**

    Device Template Name



#### check_device_template_on_device_configuration_page(device_mac='', device_name='')

* This keyword will get device template configured on Device


* Flow : Click AP MAC Link –> Configure–>Device Configuration —>Device Template


* Keyword Usage:

> 
> * `Check Device Template on Device Configuration Page  device_mac=${AP1_MAC}`


> * `Check Device Template on Device Configuration Page  device_name=${AP1_NAME}`


* **Parameters**

    
    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name to change



* **Returns**

    Device Template Name



#### check_interface_channel_width_and_channels(channels, mode='included', channel_width='default', interface='wifi2')

* The Keyword validates any valid channel on the wireless page either excluded, included, disable, enabled mode


* Keyword Usage:

-`check_channel_width_and_channels  [7 12 4 5]  mode=included  channel_width=80`

> 
> * **param channels**

>     list of valid channels


> :param mode    : excluded, included, enabled, or disabled mode
> :param channel_width:  channel width either 80, 20, 30, 40, 160 HMz
> :param interface: either wirless wifi0, wifi1, or wifi2 page
> :return: 1  or -1


#### check_wifi_radio_status(wifi_interface_name, device_mac='', device_name='')

* This keyword will check WiFi interface Radio status of the Device


* Flow : Click AP MAC Link –> Configure–>Wireless Interfaces–> WIFI interface–>Status


* Keyword Usage:

> 
> * `Check WiFi Radio Status    ${WIFI_INTERFACE_WIFI0}   device_mac=${AP1_MAC}`


> * `Check WiFi Radio Status    ${WIFI_INTERFACE_WIFI0}   device_name=${AP1_NAME}`


* **Parameters**

    
    * **wifi_interface_name** – WiFi Interface Name ie WiFi0/WiFi1


    * **device_mac** – Device Mac Address


    * **new_host_name** – Device Host Name to change



* **Returns**

    ON If Radio Status is ON else OFF



#### close_D360_configuration_page()

* This keyword will close D360 configuration page.


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    close_D360_configuration_page’’


#### configure_custom_radio_profile(profile_name='default', interface='wifi2')

* The keyword selects a custom radio profile from the radio profile drop down list either on page wifi2, wifi1, wifi0
flow: Managed - device - configuration - interface setting - wireless - either (wifi1, wifi2, wifi0)


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    configure_custom_radio_profile   radio_profile_name=${profile_name}   interface=wifi2’   ‘’


* **Parameters**

    
    * **profile_name** – profile name from the radio profile drop down list


    * **interface** – either wireless wifi0, wifi1, or wifi2 page



* return 1


#### configure_supplemental_cli_for_device(suppl_cli_name='', suppl_cli_cmds='', device_mac='', device_name='')

* This keyword will Configure Supplemental Cli on Device


* Flow : Click AP MAC or Name Link –> Configure–>Device Configuration–> Device Template


* Keyword Usage:

> 
> * `Configure Supplemental Cli for Device    ${CLI_NAME}    $device_mac=${AP1_MAC}`


> * `Configure Supplemental Cli for Device    ${CLI_NAME}    ${CLI_CMDS}     $device_name=${AP1_NAME}`


* **Parameters**

    
    * **suppl_cli_name** – Supplemental Cli Name


    * **suppl_cli_cmds** – Supplemental Cli commands


    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name



* **Returns**

    1 in case of success else -1



#### configure_wifi2_transmission_power(transmission_mode='', power_value='default')

* 
    * This keyword will Configure the WiFi2 interface power status of AP4000 or AP4000U


* Flow : Click AP MAC Link –> Configure–>Wireless Interfaces–> WiFi2 interface –> Transmission Power


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Configure WiFi2 Transmission Power   ‘Auto’ \`\`


> * 

> ```
> ``
> ```

> Configure WiFi2 Transmission Power   ‘Manual’    ${POWER_VALUE}=’13’ \`\`

:param transmission_mode : Transmission Mode ie ‘Manual’ or ‘Auto’
:param power_value: Enter power between 1dbm and 20dbm (Numerical value only)
:return: 1


#### delete_common_object_supplemental_cli(suppl_cli_name)

* This keyword will Deletes Supplemental Cli under Common objects -> Basic


* Flow : Click AP MAC or Name Link –> Common objects -> Basic -> Supplemental Cli


* Keyword Usage:

> 
> * `Delete Common Object Supplemental Cli    ${CLI_NAME}`


* **Parameters**

    **suppl_cli_name** – Supplemental Cli Name



* **Returns**

    1 in case of success else -1



#### device360_event_select_severity(severity)

* This keyword is used to select the severity in D360 Event configuration


* Assumes that navigated to the Manage –> Device page –> Events page


* Depends on the severity value, it will select in dropdown


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Device360 Event Select Severity     severity=${SEVERITY} \`\`


* Severity values should be in the category - “Critical, Info, Show All, Minor, Major, Clear”


* **Parameters**

    **severity** – “Critical, Info, Show All, Minor, Major, Clear”



* **Returns**

    1 in case of success else -1



#### device_override_change_wifi2_interface_status(device_serial='', interface_status='')

* This Keyword will Enable/Disable the WIFI2 interface status at device override configuration.


* Flow: Manage–>Devices–>select Device with serial number->Edit–>configuration–>interface settings

    –>Wireless settings–> WiFi2


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Device Override Change WiFi2 Interface Status  device_serial=${DEVICE_SERIAL}   interface_status=${STATUS} \`\`


* **Parameters**

    
    * **device_serial** – Device serial Number


    * **interface_status** – Interface status Enable/Disable



* **Returns**

    1 if interface status enable/disable Successfully else -1



#### device_override_create_imago_tag_profile(device_serial='', profile_name='', server='', channel='', fcc_mode=True, server_port='default')

* This Keyword will Crete ImagoTag Profile at device override configuration.


* Flow: Manage–>Devices–>select Device with serial number->Edit–>configuration–>interface settings

    –>Wired Settings –> Imagotag


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Device Override Create Imago Tag Profile  device_serial=${DEVICE_SERIAL}  profile_name=${PROFILE}

> server=${SERVER}  channel=${CHANNEL}\`\`


> * 

> ```
> ``
> ```

> Device Override Create Imago Tag Profile  device_serial=${DEVICE_SERIAL}  profile_name=${PROFILE}

> server=${SERVER}  channel=${CHANNEL}  server_port=${PORT}\`\`


* **Parameters**

    
    * **device_serial** – Device serial Number


    * **profile_name** – Imago Tag Profile name


    * **channel** – Channel Number


    * **server** – Server detail


    * **fcc_mode** – By default fcc_mode is enabled.To Disable mention this flag as False


    * **server_port** – Server Port Details



* **Returns**

    1 if ImagTag Profile Created Successfully else -1



#### disable_radio_status(mode, interface='wifi2')

* This keyword will enable the radio status button on the page

    manage - device - configuration - interface - wiffi2


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    enable_radio_status  ON     interface=wifi2      ‘’


* **Parameters**

    
    * **mode** – ON or OFF


    * **interface** – either inface wifi0, wifi1, wifi2



#### enabe_override_channel_exclusion_setting_in_radio_profile(interface='default')

* Enable the override the channel exclusion setting in radio profile

    :param  interface : either wireless wifi0, wifi1, wifi2 page
    :return: 1 or -1


#### enable_radio_status(mode, interface='wifi2')

* This keyword will disable the radio status button on the page

    manage - device - configuration - interface - wiffi2


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    enable_radio_status  ON     interface=wifi2      ‘’


* **Parameters**

    
    * **mode** – ON or OFF


    * **interface** – either inface wifi0, wifi1, wifi2



#### get_device_config_audit_delta(device_mac, \*\*kwargs)

* This keyword will get the delta cli configuration


* Assumes That Already in Devices Page


* **Parameters**

    **device_mac** – The serial of the device string



* **Returns**

    Returns a list of strings with the commands present in delta cli



#### get_device_configuration_interface_WiFi0_details()

* This keyword fetches all values on the device configuration interface WiFi0 page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> interface settings –> WiFi0


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    get_device_configuration_interface_WiFi2_details  ‘’


#### get_device_configuration_interface_WiFi1_details()

* This keyword fetches all values on the device configuration interface WiFi2 page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> interface settings –> WiFi2


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    get_device_configuration_interface_WiFi2_details  ‘’


#### get_device_configuration_interface_WiFi2_details()

* This keyword fetches all values on the device configuration interface WiFi2 page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> interface settings –> WiFi2


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    get_device_configuration_interface_WiFi2_details  ‘’


#### get_override_psk_ssid_settings(device_mac, interface)

* This keyword works only with device updated with psk network


* Get the override psk ssid settings from device360 configure interface wireless settings page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> interface settings –> Wireless Interfaces


* Get the ”     Override SSID Broadcast Name”, “Override PSK Password”, “Reassign CWP”


* After reading ssid settings variable close the device360 window


* Keyword Usage:

> 
> * `Get Override PSK SSID Settings   ${DEVICE_MAC}    WiFi0`


* **Parameters**

    
    * **device_mac** – device MAC to go to device 360 page


    * **interface** – interface name to get the override parameters, WiFi0, WiFi1, WiFi2



* **Returns**

    override broadcast name, psk password



#### get_unique_client_details(device_mac, search_string)

* Stores the Unique Client Page device row’s keys and values in a dictionary based on the passed search string.


* Supported search_strings are Column headers like Hostname, MAC Address and IP Address


* Keyword Usage:


* `Get Unique Client Details    ${AP_MAC}     search_string=1418C347F9B4`


* **Parameters**

    
    * **search_string** – Enter Client Hostname, Client MAC Address or IP Address (Client MAC Ex: 1418C347F9B4)


    * **device_mac** – Device MAC Ex: F09CE9F89600



* **Returns**

    Dictionary including these keys -> TYPE, OS TYPE, CURRENT CONNECT STATUS, HEALTH STATUS,


HOST NAME, CLIENT MAC, IPv4, IPv6, User Name, VLAN, Connected Via, RSSI, SNR


#### get_unique_clients_number(device_mac='')

* Get the number of Unique Clients on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Unique Client Number   ap_mac=${AP_MAC}`


* **Parameters**

    **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Number of unique clients as shown on device 360 page.



#### make_interface_channels_included_excluded(channels, mode='default', interface='wifi2')

* The keyword excludes or includes the channels

    Managed - device - configuration - interface setting - wireless - wifi2


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    make_interface_channels_included_excluded  [7  23   35]  mode=included  interface=wifi1     ‘’

:param  channels  : list of valid channels
:param  mode      : excluded or included
:param  interface : either wireless wifi2, wifi1, or wifi0 page

:return  1 or -1


#### navigate_to_device_config_device_config_dhcp(device_mac, dhcp='ENABLE')

* This keyword will retrieve the all settings in the device configuration interface WiFi2 page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> Device Configuration –>dhcp


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> navigate_to_device_config_device   ${DEVICE_MAC}   Enable’’


* **Parameters**

    
    * **device_mac** – device MAC to go to device 360 page


    * **dhcp** – Enable/Disable



* **Returns**

    1 or -1



#### navigate_to_device_config_interface_wireless(device_mac, interface='wifi2')

* This keyword will retrieve the all settings in the device configuration interface WiFi2 page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> interface settings –> wireless –> WiFi2


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> navigate_to_device_config_interface_wireless_wifi2   ${DEVICE_MAC}  ‘’


* **Parameters**

    
    * **device_mac** – device MAC to go to device 360 page


    * **interface** – interface name to get the override parameters, WiFi0, WiFi1, WiFi2



* **Returns**

    1 or -1



#### override_client_mode_in_device_config(device_mac='', interface='', \*\*client_mode_profile)

* This keyword is used to modify or override the client mode settings in wireless interface settings page


* override wireless interface settings includes client mode options of radio usage


* Flow: Manage –> Devices –> Select single device –>  Select interface setting tab –> Wireless Interfaces


* Keyword Usage:

> 
> * `Override PSK SSID Settings     device_mac=${DEVICE}   interface=WiFi0   &{client_mode_profile}`


> * `Override PSK SSID Settings     device_mac=${DEVICE}   interface=WiFi1   &{client_mode_profile}`


* **Parameters**

    
    * **device_mac** – device mac


    * **interface** – device interface i.e WiFi0/WiFi1


    * **client_mode_profile** – override config dict



* **Returns**

    1 if interface setting updated success else -1



#### override_config_device_template(template_name, device_mac='', device_name='')

* This keyword will Change the Template Name of the Device


* Flow : Click AP MAC or Name Link –> Configure–>Device Configuration–> Device Template


* Keyword Usage:

> 
> * `Override Devices Config Device Template    ${TEMPLATE_NAME}    $device_mac=${AP1_MAC}`


> * `Override Devices Config Device Template    ${TEMPLATE_NAME}   $device_name=${AP1_NAME}`


* **Parameters**

    
    * **template_name** – Device Template to Change


    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name



* **Returns**

    1 in case of success else -1



#### override_config_exos_device_template(template_name, device_mac='', device_name='')

* This keyword will Change the Template Name of the Device


* Flow : Click SW MAC or Name Link –> Configure–>Device Configuration–> Device Template


* Keyword Usage:

> 
> * `Override Devices Config Device Template    ${TEMPLATE_NAME}    $device_mac=${SW_MAC}`


> * `Override Devices Config Device Template    ${TEMPLATE_NAME}   $device_name=${SW_NAME}`


* **Parameters**

    
    * **template_name** – Device Template to Change


    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name



* **Returns**

    1 in case of success else -1



#### override_devices_config_wireless_channel(device_serials='', interface='WiFi0', override_channel='6')

* This keyword is used to override the wireless channel


* This keyword is used with multiple devices


* Flow:

> 
> * Navigate to the Manage –> Devices


> * Select the devices with passed serial numbers


> * click on Edit button  –> Interface settings –> Wireless Interfaces


> * Select the Interface (WiFi0/WiFi1) –> click radio status ON –> change channel


* Keyword Usage:

> 
> * `Override Devices Config Wireless Channel   device_serials=${AP1_SERIAL},${AP2_SERIAL}    interface='WiFi0', override_channel='6'`


* **Parameters**

    
    * **device_serials** – comma separated device serial numbers


    * **interface** – device interface i.e WiFi0/WiFi1


    * **override_channel** – override channel



* **Returns**

    returns 1 if successful



#### override_devices_config_wireless_radio_profile(device_serials='', interface='WiFi0', override_radio_prof='radio_ng_ng0')

* This keyword is used to override the radio profile


* This keyword is used with multiple devices


* Flow:

> 
> * Navigate to the Manage –> Devices


> * Select the devices with passed serial numbers


> * click on Edit button  –> Interface settings –> Wireless Interfaces


> * Select the Interface (WiFi0/WiFi1) –> click radio status ON –> change the radio profile from drop down


* Keyword Usage:

> 
> * `Override Devices Config Wireless Radio Profile   device_serials=${AP1_SERIAL},${AP2_SERIAL}    interface='WiFi0', override_radio_prof='radio_ng_ng0'`


* **Parameters**

    
    * **device_serials** – comma separated device serial numbers


    * **interface** – device interface i.e WiFi0/WiFi1


    * **override_radio_prof** – override wireless interface radio channel



* **Returns**

    


#### override_psk_ssid_settings(device_serials='', \*\*override_args)

* This keyword is used to modify or override the psk ssid settings in wireless interface settings page


* override wireless interface settings includes SSID Broadcast name, PSK password, reassigning the cwp


* Flow: Manage –> Devices –> Select the multiple device –> click on edit button –> Select the interface setting tab


* This keyword will work only with psk network policy applied to multiple devices devices


* Keyword Usage:

> 
> * `Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    &{OVERRIDE_ARGS}`


> * `Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    interface=WiFi0    override_ssid_broadcast_name=${NEW_SSID_NAME}`


> * `Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    interface=WiFi0    override_psk_password=${NEW_PSK_PASSWORD}`


> * `Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    interface=WiFi0    reassign_cwp=${NEW_CWP_NAME}`


* **Parameters**

    
    * **override_args** – override psk config dict


    * **device_serials** – device serial number to select



* **Returns**

    1 if interface setting updated success else -1



#### override_single_device_config_wireless_radio_profile(device_serial='', interface='WiFi0', override_radio_prof='radio_ng_ng0')
> 
> * Override the WiFi0 interface radio profile


* **Parameters**

    
    * **device_serial** – Device Serial Number


    * **interface** – Wifi Interface


    * **override_radio_prof** – Radio Profile



* **Returns**

    1 if able to configure Radio profile



#### override_wifi2_channel(channel_input='default')

* 
    * This keyword will Configure the WiFi2 interface power status of AP4000 or AP4000U


* Flow : Click AP MAC Link –> Configure–>Wireless Interfaces–> WiFi2 interface –> Channel Dropdown


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Override wifi2 channel   ${CHANNEL_INPUT}=’Auto’ \`\`


> * 

> ```
> ``
> ```

> Override wifi2 channel   ${CHANNEL_INPUT}=’7’ \`\`


* **Parameters**

    **channel_input** – Input AP channel (‘Auto’ for default configuration)



* **Returns**

    1



#### select_configure_supplemental_cli_for_device(suppl_cli_name='', device_mac='', device_name='')

* This keyword will Configure Supplemental Cli on Device


* Flow : Click AP MAC or Name Link –> Configure–>Device Configuration–> Device Template


* Keyword Usage:

> 
> * `Select Configure Supplemental Cli for Device    ${CLI_NAME}    $device_mac=${AP1_MAC}`


> * `Select Configure Supplemental Cli for Device    ${CLI_NAME}    ${CLI_CMDS}     $device_name=${AP1_NAME}`


* **Parameters**

    
    * **suppl_cli_name** – Supplemental Cli Name


    * **device_mac** – Device Mac Address


    * **device_name** – Device Host Name



* **Returns**

    1 in case of success else -1



#### select_supplemental_cli_row(suppl_cli_name)
select the supplemental cli
:param suppl_cli_name:
:return:


#### verify_page_details(dic1=None, dic2=None)

* This keyword will validate key value pair on any page.


* Keyword Usage:

    
        * ‘’ &{wifi2_interface_detail}=   get_device_configuration_interface_WiFi2_details ‘’


        * ‘’ &{fields_to_check}=   Create Dictionary   radio_profile=radio_ng_11ax-6g    client_access=OFF   channel_width=80MHz ‘’


        * \`\` verify_page_details  ${wifi2_interface_detail}     ${fields_to_check}      ‘’


    * **param  dic1**

        a dictionary lists of key pair of page detail



    * **param  dic2**

        list of key and values of that page


    :return 1 else -1

## extauto.xiq.flows.manage.Devices module


### _class_ extauto.xiq.flows.manage.Devices.Devices()
Bases: `object`


#### actions_change_os(device_serial, os, max_time=300, time_interval=10)
This function chenge the os on switch by using ACTIONS->CHANGE OS button . Return 1 when “Rebooting” status is displayed
:param device_serial: SN of device
:param os: exos or voss
:param max_time:  maximum time waited for “Rebooting” status
:param time_interval: check interval
:return: 1 when “Rebooting” status is displayed; else -1


#### actions_menu_disabled()

* This keyword checks if the ACTIONS menu is disabled in the Manage > Devices table.


* It is assumed that the Manage > Device window is open.


* Keyword Usage

> 
> * `Actions Menu Disabled`


* **Returns**

    1 if the field is disabled, else -1



#### actions_xiqse_maximum_site_engine_message()

* This keyword checks if the ‘Maximum 5 Site Engine > Device View’ message banner is displayed.


* The message banner will be closed, if displayed.


* Keyword Usage

> 
> * `Actions XIQSE Maximum Site Engine Message`


* **Returns**

    1 if the menu option is displayed, else -1



#### actions_xiqse_open_site_engine()

* This keyword clicks on the ACTIONS > OPEN SITE ENGINE link


* It is assumed that the Manage > Device window is open and an XIQ-SE managed device is selected.


* Keyword Usage

> 
> * `Actions XIQSE Open Site Engine`


* **Returns**

    1 if action was successful (or the field is disabled), else -1



#### activate_device_license(device_serial, license_type, username=None, password=None, shared_cuid=None, warning_msg=None, skip_warning_check=False)
This function activate premier or macsec license on a device


* **Parameters**

    
    * **device_serial** – Serial of device


    * **license_type** – premier or macsec



* **Returns**

    1 if license was activated ; else -1



#### assign_and_update_network_policy_to_exos(policy_name=None, serial=None, update_method='PolicyAndConfig')

* By default this keyword do delta config push


* Go To MANAGE–>Devices–>Select EXOS SW row  to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* select Switch –>Update device


* Keyword Usage:

> 
> * `Assign and Update Network Policy To EXOS   policy_name=${POLICY_NAME}    serial=${SW1_SERIAL}`


> * `Assign and Update Network Policy To EXOS   policy_name=${POLICY_NAME}    serial=${SW1_SERIAL}  update_method=Complete`


* **Parameters**

    
    * **policy_name** – name of the network to deploy


    * **serial** – serial number of the switch to select


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if policy is updated else -1



#### assign_network_policy_to_all_devices(policy_name)

* This keyword will assign the network policy to the all devices


* flow:

    – If Not in devices page, go to it
    – Select all devices
    – Actions
    – Assign Network Policy
    – Select the network policy from drop down window
    – Assign


* Keyword Usage:

> 
> * `Assign Network Policy To All Devices    ${policy_name}`


* **Parameters**

    **policy_name** – policy name to be applied



* **Returns**

    Success 1 else -1



#### assign_network_policy_to_switch(policy_name, serial)

* This keyword does a config push for a switch


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Assign Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}`


* **Parameters**

    
    * **policy_name** – name of the network policy to deploy


    * **serial** – serial number of the switch to select



* **Returns**

    1 if policy is assigned, else -1



#### assign_network_policy_to_switch_mac(policy_name, mac)

* This keyword does a config push for a switch


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Assign Policy To Switch  policy_name=${POLICY_NAME}  mac=${SWITCH_MAC}`


* **Parameters**

    
    * **policy_name** – name of the network policy to deploy


    * **mac** – mac number of the switch to select



* **Returns**

    1 if policy is assigned, else -1



#### change_country(ap_serial, country)

* Sets the country code of a AP to selected one.


* In case of SKU incompatibility, following is an example error we get


* The region code AH-13ad80 is set for “world”, and cannot be changed on an FCC coded device.


* Keyword Usage:

> 
> * `Change Country    ${AP1_SERIAL}    ${COUNTRY}`


* **Parameters**

    
    * **ap_serial** – AP Serial Number


    * **country** – Country Code



* **Returns**

    1 in case of success else -1



#### change_device_onboarding_date(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, days, serial_number, owner_id, sw_connection_host)
This function change the onboarding date with specific number of days behind
To use this function you need to have access to RDC database


* **Parameters**

    
    * **ip_dest_ssh** – ip of ‘Jump station’


    * **user_dest_ssh** – extreme account user


    * **pass_dest_ssh** – extreme account password


    * **days** – The number of days passed from onboarding date


    * **serial_number** – Serial number of device


    * **owner_id** – Owner Id for XIQ account


    * **rdc** – RDC name : e.g w1r1 , g2r1



* **Returns**

    1 if onboarding date has been changed ; else -1



#### change_device_onboarding_date_for_each_stack_member(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, days, serial_number, owner_id, sw_connection_host)
This function change the onboarding date with specific number of days behind
To use this function you need to have access to RDC database


* **Parameters**

    
    * **ip_dest_ssh** – ip of ‘Jump station’


    * **user_dest_ssh** – extreme account user


    * **pass_dest_ssh** – extreme account password


    * **days** – The number of days passed from onboarding date


    * **serial_number** – Serial number of device


    * **owner_id** – Owner Id for XIQ account


    * **rdc** – RDC name : e.g w1r1 , g2r1



* **Returns**

    1 if onboarding date has been changed ; else -1



#### change_manage_device_status(manage_type='MANAGE', device_serial=None, device_mac=None, device_name=None)
This Keyword changes the management status of the device.
- Keyword Usage:

> 
> * `Change Manage Device Status    MANAGE      device_serial=${DEVICE_SERIAL}`


> * `Change Manage Device Status    UNMANAGE    device_mac=${DEVICE_MAC}`


> * `Change Manage Device Status    MANAGE    device_mac=${DEVICE_NAME}`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_mac** – device MAC address


    * **manage_type** – Manage/Unmanage device



* **Returns**

    1 if the management status was changed



#### check_device_license_action(device_serial)

* Assumes that already navigated to Manage –> Devices


* This method checks if License action is available for a device matching the serial(s)


* Keyword Usage:

> 
> * `Check Device License Action ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    int



#### check_device_reboot_action(device_serial)

* Assumes that already navigated to Manage –> Devices


* This method checks if License action is available for a device matching the serial(s)


* Keyword Usage:

> 
> * `Check Device License Action ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    int



#### check_device_reboot_message(device_serial, config_update_option, reboot_message)

* check device reboot status


* keyword Usage:

> 
> * `Check Device Reboot Message   ${DEVICE_SERIAL}   ${CFG_UPDATE_OPT}   ${REBOOT_MSG}`


* **Parameters**

    
    * **device_serial** – device serial number


    * **config_update_option** – Config update option Delta/Full Config update


    * **reboot_message** – Reboot Status Message “Rebooting”



* **Returns**

    True If reboot status Message found on device updating Status else False



#### check_device_update_status_by_using_mac(device_mac)

* This keyword is used to check the status of the device update


* It will poll the “update status” every 30 seconds


* Assuming that config push will take a maximum of five minutes


* If Device Update Failed will return -1


* **Parameters**

    **device_mac** – device MAC to check the config push status



* **Returns**

    1 if config push success else -1



#### check_device_update_status_rollback_reboot(device_serial=None, device_mac=None, duration_retry=300)

* This keyword is used to check the status of the device update in XIQ


* It will poll the “update status” every 30 seconds


* Assuming that config push will take a maximum of five minutes


* **Parameters**

    **device_serial** – device serial number to check the config push status



* **Returns**

    1 if config push success else -1



#### check_double_verification_display_rollback(policy_name, option, device_serial=None, device_mac=None)
-This Keyword will check the double verification is displayed for the Reboot/Rollback option in Update Device Configuration
- Keyword Usage:

> 
> * `Check pop up message reboot revert   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}`


* **Parameters**

    
    * **policy_name** – Assign a policy for device


    * **option** – Enable/Disable reboot/rollback option in Update Devices


    * **device_serial** – serial number(s) of the device(s)


    * **device_mac** – device MAC address



* **Returns**

    1 if the double verification is displayed else -1



#### check_license_status(device_sn, max_time=180, time_interval=10)

* This keyword is used to check the status of the device license


* It will poll the “license status” at every time_interval seconds


* **Parameters**

    
    * **device_sn** – Device serial


    * **max_time** – Maximum duration of check


    * **time_interval** – Time interval between two consecutive checks



* **Returns**

    returns the status displayed into device license field (NONE; PREMIER; MACSEC; FOURPORT10G;EIGHTPORT10G) +


error message if it is present ;else -1


#### check_license_update_frequency(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, sw_connection_host)
This function checks the update frequency for license job


* **Parameters**

    
    * **ip_dest_ssh** – ip of ‘Jump station’


    * **user_dest_ssh** – extreme account user


    * **pass_dest_ssh** – extreme account password


    * **sw_connection_host** – RDC DNS



* **Returns**

    1 if update time is less or equal than 10 minutes ; else -1



#### check_long_sn_or_legacy_sn_mapping(device_serial, ip_dest_ssh, user_dest_ssh, pass_dest_ssh, sw_connection_host)
This function checks if the SN for 5520 has short or long format . If the function has short format the sn will be
searched into extr_legacy_sn_mapping table
:param ip_dest_ssh: ip of ‘Jump Station’
:param user_dest_ssh: SFDC username account
:param pass_dest_ssh: SFDC password account
:param sw_connection_host: The RDC DNS
:return: 1 if SN has long format or if it is into db ; else -1


#### check_message_unlink_button(expected_message)
This function checks if the message is correct when try to unlink
:param expected_message: Expected message
:return: 1 if expected message was found ; else -1


#### check_negative_combinations()

#### check_pilot_license_consumption(expected_available, expected_activated, license_type='PRD-XIQ-PIL-S-C', max_time=660, interval_check_time=60)
This function checks if the available and activated licenses are displayed as expected into License Management page
:param expected_available: Number of expected available licenses
:param expected_activated: Number of expected activated license
:param license_type: type of license
:param max_time: Maximum duration of check
:param interval_check_time: time interval between two consecutive checks
:return:


#### check_pop_up_message_reboot_revert(policy_name, option, device_serial=None, device_mac=None)
-This Keyword will check the Reboot/Rollback option in Update Device Configuration has a pop-up message
- Keyword Usage:

> 
> * `Check pop up message reboot revert   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}`


* **Parameters**

    
    * **policy_name** – Assign a policy for device


    * **option** – Enable/Disable reboot/rollback option in Update Devices


    * **device_serial** – serial number(s) of the device(s)


    * **device_mac** – device MAC address



* **Returns**

    1 if the pop-up message has been found else -1



#### check_serial_list(serial)
This function checks if a device or more need a Pilot License in next 15 days. The list from banner is cheked


* **Parameters**

    **serial** – a serial or more



* **Returns**

    1 if the SN or SNs are into serial list from banner ; else -1



#### check_status_rebooting_cli(spawn, device_serial=None, device_mac=None)
This keyword gets status about the rebooting information from CLI .First will check the update status from the XIQ if IQagent loses connectivity during configuration in 10 minutes.
- Keyword Usage:
- `Check status rebooting cli   ${SPAWN}       ${DEVICE_SERIAL}      ${DEVICE_MAC}`
:param spawn: device spawn
:param device_serial: serial number(s) of the device(s)
:param device_mac:  device MAC address
:return: 1 if gets information about rebooting from CLI else -1


#### check_tooltip_message_presence(tooltip_message)

* This Keyword will validate whether given Tooltip Message Displayed on Manage–> Devices Page


* Keyword Usage:

> 
> * `check tooltip message presence  ${TOOLTIP_MESSAGE}`


* **Parameters**

    **tooltip_message** – Tooltip message to check on devices page



* **Returns**

    1 if tooltip message appears, else -1



#### check_unlink_button()
This function checks if the unlink button is present


* **Returns**

    1 if unlink button is present ; else -1



#### check_unmanage_message_on_device()
This Keyword verifies if the unmanage message was shown.
:return: 1 if the unmanaged message was shown


#### check_update_time_on_rdc(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, sw_connection_host)
This function returns the update time interval for RDC


* **Parameters**

    
    * **ip_dest_ssh** – ip of ‘bastion station’


    * **user_dest_ssh** – extreme account user


    * **pass_dest_ssh** – extreme account password


    * **sw_connection_host** – The RDC DNS



* **Returns**

    interval time and interval unit ; else -1



#### check_upgrade_account_button()
This function presses the upgrade account button


* **Returns**

    1 if account button was pressed  ; else -1



#### check_voss_image_version(output_image_version, os_version, operator='less')
Check is os_version is equel, less or greater than on version from cli
:param spawn:
:param os_version: 8.6.0.0
:param operator: equal, less or greater than on version from cli
:return: True or False if os_version is equel, less or greater than on version from cli ; else -1


#### clear_search_field()

* Clears the search field is necessary


#### clear_search_on_devices_table()

* Clears the search field on the Manage> Devices page, if it is populated.


* Keyword Usage:

> 
> * `Clear Search On Devices Table`

:return  1 if action was successful, else -1


#### close_last_refreshed_tooltip()

* Closes the “Last Refreshed at:” tooltip by moving the mouse to the element, if it is displayed.


#### column_picker_select(\*columns)

* This keyword checks the device column picker if it is not checked


* Keyword Usage:

> 
> * `Column Picker Select        Zone   Branch ID   Host Name   Network Policy`

> -`Column Picker Select        Stack Unit`


* **Parameters**

    **columns** – list of device columns that can be checked



* **Returns**

    returns 1 if successful



#### column_picker_unselect(\*columns)

* This keyword unchecks the device column picker if it is checked


* Keyword Usage:

> 
> * `Column Picker Unselect      Branch ID  Host Name   Cloud Config Groups`

> -`Column Picker Unselect       Network Policy`


* **Parameters**

    **columns** – list of device columns that can be unchecked



* **Returns**

    returns 1 if successful



#### confirm_all_devices_deselected()

* This keyword confirms all devices in the table are deselected


* Keyword Usage:

    
        * Confirm All Devices Unselected


* **Returns**

    returns 1 if no devices are selected; else, -1



#### confirm_all_devices_selected()

* This keyword confirms all devices in the table are selected


* Keyword Usage:

    
        * Confirm All Devices Selected


* **Returns**

    returns 1 if all devices are selected; else, -1



#### confirm_column_picker_column_selected(\*columns)

* This keyword confirms the list of columns are all selected in the column picker


* Keyword Usage:

    
        * Confirm Column Picker Column Selected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}


* **Parameters**

    **columns** – list of device columns that should be selected



* **Returns**

    returns 1 if all columns are selected in the column picker; else, -1



#### confirm_column_picker_column_unselected(\*columns)

* This keyword confirms the list of columns are all unselected in the column picker


* Keyword Usage:

    
        * Confirm Column Picker Column Unselected  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}


* **Parameters**

    **columns** – list of device columns that should be selected - passed in as multiple arguments



* **Returns**

    returns 1 if all columns are selected in the column picker; else, -1



#### confirm_column_picker_contains_column(\*columns)

* This keyword confirms the list of columns are all present in the column picker


* Keyword Usage:

    
        * Confirm Column Picker Contains Column  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}


* **Parameters**

    **columns** – list of device columns that should be present in the column picker list



* **Returns**

    returns 1 if all columns are present in the column picker; else, -1



#### confirm_column_picker_does_not_contain_column(\*columns)

* This keyword confirms the list of columns are NOT present in the column picker


* Keyword Usage:

    
        * Confirm Column Picker Does Not Contain Column  ${COLUMN_1}  ${COLUMN_2}  ${COLUMN_3}


* **Parameters**

    **columns** – list of device columns that should not be present in the column picker list



* **Returns**

    returns 1 if none of the columns are present in the column picker; else, -1



#### confirm_device_disconnected(device_serial='default', device_name='default', device_mac='default')

* This keyword confirms the device is disconnected


* Keyword Usage:

> 
> * `Confirm Device Disconnected   device_serial=${DEVICE_SERIAL}`


> * `Confirm Device Disconnected   device_name=${DEVICE_NAme}`


> * `Confirm Device Disconnected   device_mac=${DEVICE_MAC}`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device host name


    * **device_mac** – device MAC address



* **Returns**

    1 if device is currently disconnected, else -1



#### confirm_devices_deselected(\*device_list)

* This keyword confirms the list of devices are all deselected in the table


* Keyword Usage:

    
        * Confirm Devices Deselected  ${SERIAL_1}  ${SERIAL_2}  ${SERIAL_3}


* **Parameters**

    **device_list** – list of device serial numbers to check the selection state of



* **Returns**

    returns 1 if all specified devices are deselected; else, -1



#### confirm_devices_selected(\*device_list)

* This keyword confirms the list of devices are all selected in the table


* Keyword Usage:

    
        * Confirm Devices Selected  ${SERIAL_1}  ${SERIAL_2}  ${SERIAL_3}


* **Parameters**

    **device_list** – list of device serial numbers to check the selection state of



* **Returns**

    returns 1 if all specified devices are selected; else, -1



#### confirm_no_duplicate_rows(search_string)

* Searches for device rows containing the search_string and confirms only one row exists with the value.


* This is useful for confirming only one device with a specified MAC Address exists in the table, but


* should not be used for search strings where multiple rows could contain the same value (e.g., a certain


* name value, or a serial number which is also used in another row, like CLOUD CONFIG GROUPS in XIQ-SE).


* **Parameters**

    **search_string** – String to look for in each row



* **Returns**

    return 1 if none or only one row with the search string is found (no duplicates);
    -1 if more than one row contains the search string



#### confirm_xiqse_managed_device_not_onboarded_by_xiq(device_serial, device_make, location)

* This keyword attempts to onboard a device which is currently managed by XIQ-SE and confirms the appropriate


* error is displayed.


* Keyword Usage:

> 
> * `Confirm XIQSE Managed Device Not Onboarded By XIQ    ${SERIAL}  ${MAKE}  ${LOCATION"`


* **Parameters**

    
    * **device_serial** – serial number of Device


    * **device_make** – Model of the Device (e.g., aerohive, voss, exos, etc.)


    * **location** – Location of the Device (e.g., San Jose, building_01, floor_02)



* **Returns**

    1 if expected error message appears, else -1



#### create_stack_auto_template(device_mac='default', name_stack_template='default')

* This Keyword will create EXOS Stack Auto Template after assigned a policy to the stack


* Keyword Usage

> 
> * `Get Template Status   device_mac=${DEVICE_MAC}`


> * `Name Stack Template   ${Stack_TEMPLATE_NAME}`


* **Parameters**

    
    * **device_mac** – device MAC address


    * **name_stack_template** – Name of the stack_template



* **Returns**

    1 If successfully Switch Stack template



#### delete_all_aps()
This function is deprecated. This Keyword will Delete All the Devices in the Manage–> Devices Grid
:return: 1 if Devices Deleted Successfully else -1


#### delete_all_devices()

* This Keyword will Delete All the Devices in the Manage–> Devices Grid


* Keyword Usage:

> 
> * `Delete All devices`


* **Returns**

    1 if Devices Deleted Successfully else -1



#### delete_ap(ap_serial=None, ap_name=None, ap_mac=None)

* Assumes that already navigated to manage –> Devices Page


* Deletes AP matching either one of serial, name, MAC


* Keyword Usage:

> 
> * `Delete AP   ap_serial=${AP_SERIAL}`


> * `Delete AP   ap_name=${AP_NAME}`


> * `Delete AP   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – ap serial number


    * **ap_name** – host name of the AP


    * **ap_mac** – ap Mac address



* **Returns**

    1 if deleted else -1



#### delete_aps(ap_serials=None, ap_names=None, ap_macs=None)

* Assumes that already navigated to Manage –> Devices


* Delete the multiple AP one by one


* Keyword Usage:

> 
> * `Delete APs   ap_serials=${AP1_SERIAL},${AP2_SERIAL}`


> * `Delete APs   ap_serials=${AP1_SERIAL}`


* **Parameters**

    
    * **ap_serials** – AP serial number


    * **ap_names** – Host name of the AP


    * **ap_macs** – MAC of the AP



* **Returns**

    1 if deleted else -1



#### delete_device(device_serial=None, device_name=None, device_mac=None, \*\*kwargs)

* Deletes Device matching either any of either one of serial, name, MAC


* Keyword Usage:

> 
> * `Delete Device    device_serial=${DEVICE_SERIAL}`


* **Parameters**

    
    * **device_serial** – device serial number


    * **device_name** – name of the device


    * **device_mac** – mac address of the device



* **Returns**

    1 if device deleted successfully or is already deleted/does not exist, else -1



#### delete_devices(\*device_list)

* Deletes the list of devices denoted by serial numbers


* Keyword Usage:

> 
> * `Delete Devices    ${DEVICE_SERIAL1}  ${DEVICE_SERIAL2}  ${DEVICE_SERIAL3}`


* **Parameters**

    **device_list** – list of device serial numbers to delete



* **Returns**

    1 if devices deleted successfully or are already deleted/do not exist, else -1



#### delete_simulated_ap(ap_model)

* Deletes Simulated AP from the device grid based on ap model


* Keyword Usage:

> 
> * `Delete Simulated Aps    ${AP_MODEL}`


* **Parameters**

    **ap_model** – model of the AP



* **Returns**

    1 if deleted successfully else -1



#### deselect_all_devices()

* This keyword deselects all devices in the table by clicking the Select All check box column header to deselect
it if it is already selected, or clicking the Select All check button twice (once to select all, once to deselect
all) if it is not already selected.


* Keyword Usage:

    
        * Deselect All Devices

:param None
:return: returns 1 if the action was successful; else, -1


#### device_reboot(device_serial)

* This keyword is used to reboot the device from Actions –> Reboot


* Flow:

> 
> * Navigate to Manage –> Devices


> * Select the device row based on the passed device serial number


> * Click on ACTIONS –> Reboot


* Keyword Usage:

> 
> * `Device Reboot   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number to reboot



* **Returns**

    1



#### device_update_progress(device_serial='default', retry_duration=30, retry_count=900)

* This keyword is used to check the status of the device update and also shows device update progress status such as 19%…etc


* It will poll the “update status” every retry_duration seconds


* Assuming that config push will take a maximum of fiften minutes


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the device status and device update prograss for a device based on passed device serial


* Keyword Usage:

> 
> * Device Update Progress       ${DEVICE_SERIAL}   retry_duration=30       retry_count=800\`


* **Parameters**

    
    * **device_serial** – device serial number to check the config push status


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    device update status if config push success else -1



#### edit_ap_description(ap_desc, ap_serial=None, ap_name=None, ap_mac=None)

* Edits AP matching either any of either one of serial, name, MAC


* Keyword Usage:

> 
> * `Edit Ap Description   ${AP_DESC}   ap_serial=${AP_SERIAL}`


* **Parameters**

    
    * **ap_desc** – AP’s Description


    * **ap_serial** – AP Serial


    * **ap_name** – AP Name


    * **ap_mac** – AP MAC



* **Returns**

    1 if success else -1



#### format_row(row)

#### get_ap_assigned_location(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Location Assigned to the AP


* Keyword Usage:

> 
> * `Get Ap Assigned Location   ap_serial=${AP_SERIAL}`


> * `Get Ap Assigned Location   ap_name=${AP_NAME}`


> * `Get Ap Assigned Location   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Location applied to the AP



#### get_ap_country(ap_serial)

* This method gets the country name from country cell from Devices page.


* Keyword Usage:

> 
> * `Get Ap Country   ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – serial number of AP



* **Returns**

    country name



#### get_ap_country_cli(cli_output)

* This keyword gets country code of AP from CLI output


* Keyword Usage:

> 
> * `Get Ap Country Cli    ${CLI_OUTPUT}`


* **Parameters**

    **cli_output** – output of show boot-param command



* **Returns**

    returns country code



#### get_ap_flag(ap_serial)

* This method gets the country cell element from Devices page and saves the screenshot of it.


* Keyword Usage:

> 
> * `Get AP Flag    ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – ap serial number



* **Returns**

    1 if flag saved else -1



#### get_ap_hostname(ap_serial)

* This method gets AP hostname based on AP serial


* Keyword Usage:

> 
> * `Get Ap Hostname   ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – serial number of AP



* **Returns**

    success AP hostname else -1



#### get_ap_management_ip_address(ap_serial=None, ap_name=None, ap_mac=None)

* Get Management IP Assigned to the AP


* Keyword Usage:

> 
> * `Get Ap Management IP Address   ap_serial=${AP_SERIAL}`


> * `Get Ap Management IP Address   ap_name=${AP_NAME}`


> * `Get Ap Management IP Address   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    AP Management IP Address



#### get_ap_network_policy(ap_serial=None, ap_name=None, ap_mac=None)

* Get the network policy deployed to the AP


* Keyword Usage:

> 
> * `Get Ap Network Policy   ap_serial=${AP_SERIAL}`


> * `Get Ap Network Policy   ap_name=${AP_NAME}`


> * `Get Ap Network Policy   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    network policy name applied to the AP



#### get_ap_public_ip_address(ap_serial=None, ap_name=None, ap_mac=None)

* Get AP Public IP address using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap Public IP Address   ap_serial=${AP_SERIAL}`


> * `Get Ap Public IP Address   ap_name=${AP_NAME}`


> * `Get Ap Public IP Address   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Ap Public IP Address



#### get_ap_row(ap_serial='default', ap_name='default', ap_mac='default')

* Get the AP row object from the Devices grid


* Keyword Usage:

> 
> * `Get AP Row  ap_serial=${AP_SERIAL}`


> * `Get AP Row  ap_name=${AP_NAME}`


> * `Get AP Row  ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – AP Serial


    * **ap_name** – AP Name


    * **ap_mac** – AP MAC



* **Returns**

    returns the row object



#### get_ap_row_with_search_option(ap_serial='default', ap_name='default', ap_mac='default')

* Get the AP row object from the Devices grid


* Keyword Usage:

> 
> * `Get AP Row With Search Option  ap_serial=${AP_SERIAL}`


> * `Get AP Row With Search Option  ap_name=${AP_NAME}`


> * `Get AP Row With Search Option  ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – AP Serial


    * **ap_name** – AP Name


    * **ap_mac** – AP MAC



* **Returns**

    returns the row object



#### get_ap_row_without_search_option(ap_serial='default', ap_name='default', ap_mac='default')

* Get the AP row object from the Devices grid


* Keyword Usage:

> 
> * `Get AP Row Without Search Option  ap_serial=${AP_SERIAL}`


> * `Get AP Row Without Search Option  ap_name=${AP_NAME}`


> * `Get AP Row Without Search Option  ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – AP Serial


    * **ap_name** – AP Name


    * **ap_mac** – AP MAC



* **Returns**

    returns the row object



#### get_ap_status(ap_serial='default', ap_name='default', ap_mac='default')

* This keyword returns the AP’s status by searching AP using serial, name or mac address


* Keyword Usage:

> 
> * `Get Ap Status    ap_serial=${AP_SERIAL}`


> * `Get Ap Status    ap_name=${AP_NAME}`


> * `Get Ap Status    ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – AP Serial


    * **ap_name** – AP Name ie AP Host name in GUI ex: AH-2aa840


    * **ap_mac** – AP MAC



* **Returns**

    ‘green’ if the AP is online else return -1



#### get_ap_wifi0_channel(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi0 Channel applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI0 Channel   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI0 Channel   ap_name=${AP_NAME}`


> * `Get Ap WIFI0 Channel   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Channel value of wifi0 interface



#### get_ap_wifi0_power(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi0 power applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI0 Power   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI0 Power   ap_name=${AP_NAME}`


> * `Get Ap WIFI0 Power   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Transmission power value of wifi0 interface



#### get_ap_wifi0_radio_profile(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi0 Radio Profile applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI0 Radio Profile   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI0 Radio Profile   ap_name=${AP_NAME}`


> * `Get Ap WIFI0 Radio Profile   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Radio Profile value of wifi0 interface



#### get_ap_wifi0and1_configured_ssids(ap_name)

* This keyword will get wifi0 and wifi1 ssids from interface settings page behind Configure tab in AP device level


* flow:

    – Go to configure tab in AP device level based on AP hostname
    – Click Configure tab
    – Click Interface Settings
    – Get wifi0 ssids and wifi1 ssids
    – Put them to a ssid dictionary, as example {‘wifi0’:[‘ssid1’,’ssid2’], ‘wifi1’:[‘ssid1’,’ssid2’]}
    – return the ssid dictionary


* Keyword Usage:

> 
> * `Get Ap Wifi0and1 Configured Ssids    ${ap_name}`


* **Parameters**

    **ap_name** – AP hostname



* **Returns**

    Success ssid dictionary whatever it is null



#### get_ap_wifi1_channel(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi1 Channel applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI1 Channel   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI1 Channel   ap_name=${AP_NAME}`


> * `Get Ap WIFI1 Channel   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Channel value of wifi0 interface



#### get_ap_wifi1_power(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi1 power applied on AP using AP’s serial number,Name or Mac address.


* Flow : Manage —> Devices


* Keyword Usage:

> 
> * `Get Ap WIFI1 Power   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI1 Power   ap_name=${AP_NAME}`


> * `Get Ap WIFI1 Power   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Transmission power value of wifi1 interface



#### get_ap_wifi1_radio_profile(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi1 Radio Profile applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI1 Radio Profile   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI1 Radio Profile   ap_name=${AP_NAME}`


> * `Get Ap WIFI1 Radio Profile   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Radio Profile value of wifi1 interface



#### get_ap_wifi2_channel(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi2 Channel applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI2 Channel   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI2 Channel   ap_name=${AP_NAME}`


> * `Get Ap WIFI2 Channel   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Channel value of wifi2 interface



#### get_ap_wifi2_power(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi2 power applied on AP using AP’s serial number,Name or Mac address.


* Flow : Manage —> Devices


* Keyword Usage:

> 
> * `Get Ap WIFI2 Power   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI2 Power   ap_name=${AP_NAME}`


> * `Get Ap WIFI2 Power   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Transmission power value of wifi2 interface



#### get_ap_wifi2_radio_profile(ap_serial=None, ap_name=None, ap_mac=None)

* Get the Wifi2 Radio Profile applied on AP using AP’s serial number,Name or Mac address.


* Keyword Usage:

> 
> * `Get Ap WIFI2 Radio Profile   ap_serial=${AP_SERIAL}`


> * `Get Ap WIFI2 Radio Profile   ap_name=${AP_NAME}`


> * `Get Ap WIFI2 Radio Profile   ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – Serial number of AP Ex:11301810220048


    * **ap_name** – Ap name Ex: AP1130


    * **ap_mac** – Ap mac Ex: F09CE9F89600



* **Returns**

    Radio Profile value of wifi2 interface



#### get_audit_log()
This function returns the date for the last log from audit
:return: the date of last log ; else -1


#### get_banner_messages(expected_message)
This function compares a message from banner with expected_message


* **Parameters**

    **expected_message** – 



* **Returns**

    1 if expected message was found in banner ; else -1



#### get_check_update_failed_after_reboot(device_serial=None, device_mac=None)
This keyword gets information of the update failed status in XIQ for a device after reboot/rollback configuration
- Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Get check update failed after reboot   ${DEVICE_SERIAL} \`\`


> * 

> ```
> ``
> ```

> Get check update failed after reboot   ${DEVICE_MAC} \`\`


* **Parameters**

    
    * **device_serial** – Gets the information of the update failed status based on serial number


    * **device_mac** – Gets the information of the update failed status based on address MAC



* **Returns**

    1 if the information was found else -1



#### get_column_header_tooltip(column_name)
This keyword verifies whether the Devices grid’s Network Policy column shows it is sortable or not in a tooltip
:return 1 if we get a tool-tip message eX: “Network Policy - This column is not sortable” else it returns -1


#### get_cuid_and_viq_id(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, owner_id, sw_connection_host)
This functions returns VHM ID an CUID ID.
:param ip_dest_ssh: ip/dns destination of bastion host
:param user_dest_ssh: user for bastion host account
:param pass_dest_ssh: password for bastion host account
:param owner_id: Owner id
:param sw_connection_host: RDC environment
:return: CUID and VIQ_IQ; else return None


#### get_deselected_device_count()

* Gets the number of deselected devices from the Devices grid


* Keyword Usage:

> 
> * `Get Deselected Device Count`


* **Returns**

    returns the number of deselected rows



#### get_device_configuration_audit_status(device_serial)

* This keyword is used to get the device configuration audit status


* Flow:

> 
> * Navigate to Manage –> Devices  –> Get the configuration audit status under status column of the device row


* Keyword Usage:

> 
> * `Get Device Configuration Audit Status    ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number to check the device configuration audit status



* **Returns**

    


* audit match : if configuration audit matched


* audit mismatch : if configuration audit mismatch


* -1 if device not found in the device grid


#### get_device_connected_status(device_serial)

* This keyword is used to check the device connected status on XIQ.


* After Configuring the CAPWAP client server in device cli, check the device connected status


* This keyword loop over every 30 seconds to check the device connected status


* This will wait maximum ${XIQ_DEVICE_CONNECT_WAIT} defined in waits.robot to check the device connected status


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the device status for a device based on passed device serial


* Keyword Usage:

> 
> * `Get Device Connected Status   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number to check the device connected status



* **Returns**

    1 if device connected within ${XIQ_DEVICE_CONNECT_WAIT} time else -1



#### get_device_count()

* Gets the device count from the Devices grid


* Keyword Usage:

> 
> * `Get Device Count`


* **Returns**

    returns the number of devices in the table



#### get_device_details(search_string, label_str)

* Gets the device row label value based on the passed label_str


* Supported label_str are Column headers like IQ ENGINE, POLICY, NTP STATE, MGT IP ADDRESS


* If the Column is not visible also it will get the value for particular  column header


* Keyword Usage:

> 
> * `${POLICY}        Get Device Details    ${AP1_MAC}     POLICY`


> * `${UPDATED}       Get Device Details    ${AP1_MAC}     UPDATED`


> * `${MGT_IP_ADDR}   Get Device Details    ${AP1_MAC}     MGT IP ADDRESS`


> * `${MAC}           Get Device Details    ${AP1_MAC}     MAC`


* **Parameters**

    
    * **search_string** – string to uniquely identify the row in device grid


    * **label_str** – supported labels are Column headers ex: LOCATION, IQ ENGINE, POLICY, NTP STATE, MGT IP ADDRESS

        MAC, CLIENTS

    UPTIME, MODEL, SERIAL, UPDATED, MGT VLAN,




* **Returns**

    column header value



#### get_device_events_list(device_model)

#### get_device_row(device_serial='default', device_name='default', device_mac='default')

* This keyword returns the row of matched device


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device Name


    * **device_mac** – device MAC



* **Returns**

    returns the row object



#### get_device_row_values(search_string, col_list)

* Gets a dictionary of device row values based on the passed column label list


* The column list should be a comma-separated list of column headers, like HOST NAME,MGT IP ADDRESS,MAC


* Keyword Usage:

> 
> * `@{DEVICE_VALUES}=  Get Device Row Values   ${DEVICE_SERIAL}  HOST NAME,MGT IP ADDRESS,MAKE,MODEL`


* **Parameters**

    
    * **search_string** – string to uniquely identify the row in the device grid


    * **col_list** – comma-separated list of column headers (e.g., LOCATION,MAC,MGT IP ADDRESS)



* **Returns**

    dictionary containing the values for each of the specified columns



#### get_device_serial_numbers(device_type)

* gets all existing devices serials with the same device_type


* Keyword Usage:

> 
> * `Get Device Serial Numbers   ${DEVICE_TYPE}`


* **Parameters**

    **device_type** – type of device to onboard



* **Returns**

    serial number(s) with same device type



#### get_device_stack_status(device_mac='default', device_serial='default', duration_retry=300)

* This keyword returns the device’s connection status, audit log status


* Keyword Usage:

> 
> * `Get Device Status   device_serial=${DEVICE_SERIAL}`


> * `Get Device Status   device_name=${DEVICE_NAme}`


> * `Get Device Status   device_mac=${DEVICE_MAC}`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device host name


    * **device_mac** – device MAC address


:param duration_retry : duration of retry in seconds


* **Returns**

    


* ‘blue’ if device connected and config audit match and stack toggle icon is blue


* ‘red’ stack toggle icon is red


* ‘config audit mismatch’ if device connected and config audit mismatch


* ‘disconnected’ if device disconnected and unable to connect after 10 minutes


* ‘unknown’ if device connection status is ‘Unknown’


#### get_device_status(device_serial='default', device_name='default', device_mac='default', \*\*kwargs)

* This keyword returns the device’s connection status, audit log status


* Keyword Usage:

> 
> * `Get Device Status   device_serial=${DEVICE_SERIAL}`


> * `Get Device Status   device_name=${DEVICE_NAme}`


> * `Get Device Status   device_mac=${DEVICE_MAC}`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device host name


    * **device_mac** – device MAC address



* **Returns**

    


* ‘green’ if device connected and config audit match


* ‘config audit mismatch’ if device connected and config audit mismatch


* ‘disconnected’ if device disconnected and unable to connect after 10 minutes


* ‘unknown’ if device connection status is ‘Unknown’


#### get_device_template_status(device_mac='default', duration_retry=50)

* This keyword returns the device’s connection status, audit log status


* Keyword Usage:

> 
> * `Get Template Status   device_mac=${DEVICE_MAC}`


* **Parameters**

    **device_mac** – device MAC address


:param duration_retry : duration of retry in seconds


* **Returns**

    


* 1 for ‘empty’ if device is a EXOS Stack and don’t have a policy


* 2 for ‘Device default-template’ if device is a standalone device


* 3 for ‘Assign/Create Template’ if device is a EXOS Stack and have a policy


#### get_device_updated_status(device_serial=None, device_name=None, device_mac=None)

* This keyword returns the device updated status by searching device row using serial, name or mac address


* Assumes that already navigated to the manage–>device page


* Keyword Usage:

> 
> * `Get Device Updated Status   device_serial=${DEVICE_SERIAL}`


> * `Get Device Updated Status   device_name=${DEVICE_NAME}`


> * `Get Device Updated Status   device_mac=${DEVICE_MAC}`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device Name


    * **device_mac** – device MAC



* **Returns**

    ‘updated Time’ if the device is updated correctly else return updating status message



#### get_exos_stack_status(device_mac='default')
> 
> * This keyword returns the EXOS Stack icon status is blue or red


> * ‘blue’ means all the stack members are in managed state


> * ‘red’ means one or more slot is not in managed state


> * ‘-1’ means the device is not a stack device


> * Keyword Usage:


> * `Get Exos Stack Status   device_mac=${DEVICE_MAC}`


* **Parameters**

    **device_mac** – device MAC address



* **Returns**

    


* ‘blue’ if all the stack members are in managed state else ‘red’


* ‘-1’ if the stack icon is not in the device row


#### get_manage_device_row(search_string)

* Get the device row object from the Manage –> Device page


* Based on the search string it will search the device row


* Search string should be device serial, device mac, device host name


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell
    example search_string be like device_name, Device Model, Mac Address or Serial number



* **Returns**

    row element if row exists else return None



#### get_os_change(device_serial=None, device_name=None, device_mac=None)

#### get_pilot_license_consumption(license_type='PRD-XIQ-PIL-S-C', max_time=120, interval_check_time=60)
This functions gets the available and activated licenses
:param license_type:
:param max_time:
:param interval_check_time:
:return: available and activated licenses


#### get_router_network_policy(router_serial=None, router_name=None, router_mac=None)

* Get router network policy applied to the router


* Keyword Usage:

> 
> * `Get Router Network Policy  router_serial=${ROUTER_SERIAL}`


> * `Get ROuter Network Policy  router_name=${ROUTER_NAME}`


> * `Get ROuter Network Policy  router_mac=${ROUTER_MAC}`


* **Parameters**

    
    * **router_serial** – router serial number


    * **router_name** – router host name


    * **router_mac** – router mac address



* **Returns**

    nw policy applied to the router



#### get_selected_device_count()

* Gets the number of selected devices from the Devices grid


* Keyword Usage:

> 
> * `Get Selected Device Count`


* **Returns**

    returns the number of selected rows



#### get_stack_status(device_mac='default')
> 
> * This keyword returns the Stack status


> * Keyword Usage:


> * `Get Stack Status   device_mac=${DEVICE_MAC}`


* **Parameters**

    **device_mac** – device MAC address



* **Returns**

    


* ‘enabled’ if stack is connected and enabled properly else ‘disabled’


#### get_total_device_count()

* Gets the total device count using the “Showing X of Y” label at the top of the view (since more devices


* may exist than are currently being displayed).


* Keyword Usage:

> 
> * `Get Total Device Count`


* **Returns**

    returns the total number of devices



#### get_update_devices_reboot_rollback(policy_name, option, device_serial=None, device_mac=None)
-This Keyword will Update Device Configuration with Reboot/Rollback option if the IQagent loses connectivity with XIQ during configuration
- Keyword Usage:

> 
> * `Get update devices reboot rollback   ${POLICY_NAME}   ${OPTION}  ${DEVICE_SERIAL}  ${DEVICE_MAC}`


* **Parameters**

    
    * **policy_name** – Assign a policy for device


    * **option** – Enable/Disable reboot/rollback option in Update Devices


    * **device_serial** – serial number(s) of the device(s)


    * **device_mac** – device MAC address



* **Returns**

    1 if update configuration is pushed on the device with Reboot/Rollback option



#### is_actions_button_visible()

* This Keyword checks if the actions button is visible


* Keyword Usage:

> 
> * `Is Actions Button Visible`


* **Returns**

    1 if visible, -1 if not



#### is_add_button_visible()

* This Keyword checks if the add button is visible


* Keyword Usage:

> 
> * `Is Add Button Visible`


* **Returns**

    1 if visible, -1 if not



#### is_bulk_edit_button_visible()

* This Keyword checks if the bulk edit button is visible


* Keyword Usage:

> 
> * `Is Bulk Edit Button Visible`


* **Returns**

    1 if visible, -1 if not



#### is_delete_button_visible()

* This Keyword checks if the delete button is visible


* Keyword Usage:

> 
> * `Is Delete Button Visible`


* **Returns**

    1 if visible, -1 if not



#### is_download_button_visible()

* This Keyword checks if the download button is visible


* Keyword Usage:

> 
> * `Is Download Button Visible`


* **Returns**

    1 if visible, -1 if not



#### is_update_device_button_visible()

* This Keyword checks if the device update button is visible


* Keyword Usage:

> 
> * `Is Update Device Button Visible`


* **Returns**

    1 if visible, -1 if not



#### is_utilities_button_visible()

* This Keyword checks if the utilities button is visible


* Keyword Usage:

> 
> * `Is Utilities Button Visible`


* **Returns**

    1 if visible, -1 if not



#### link_to_sfdc_from_license_management_page(username, password, shared_cuid=None)
This function links the XIQ account to SFDC and will move the account to Pilot mode from License Management page
:param username: SFDC username account
:param password: SFDC password account
:param shared_cuid: SFDC shared cuid
:return: 1 if account was linked ; else -1


#### link_to_sfdc_from_unmanage_box(username, password, shared_cuid=None)
This function links the XIQ account to SFDC by using the ‘ADD LICENSE’ button from unmanage dialog
:param username: SFDC username account
:param password: SFDC password account
:param shared_cuid: SFDC shared cuid
:return: 1 if account was linked ; else -1


#### location_dialog_select_location(dev_location='default')

* This keyword selects the specified location in the Select Location dialog


* Keyword Usage:

> 
> * `Location Dialog Select Location    San Jose, building_01, floor_02`


* **Parameters**

    **dev_location** – location where the device is to be assigned in the above format



#### login_to_extreme_portal(username, password, shared_cuid=None)
This function enters the credentials when SFDC page is displayed
:param username: SFDC username account
:param password: SFDC password account
:param shared_cuid: SFDC shared cuid
:return: 1 if the credentials were entered ; else -1


#### max_device_num_from_hm_vhm_account_table(ip_dest_ssh, user_dest_ssh, pass_dest_ssh, vhm_id, sw_connection_host)
This function returns the number of devices which can be onboarded
To use this function you need to have access to RDC database


* **Parameters**

    
    * **ip_dest_ssh** – ip of ‘Jump station’


    * **user_dest_ssh** – extreme account user


    * **pass_dest_ssh** – extreme account password


    * **vhm_id** – VHM Id for XIQ account


    * **rdc** – RDC name : e.g w1r1 , g2r1



* **Returns**

    number of devices which can be onboarded  ; else -1



#### move_to_free_pilot_from_trial_or_connect()
This function moves XIQ account into free pilot mode by using the link from banner
:return: 1 if account was moved ; else -1


#### move_to_pilot_mode_from_unmanage_box()
This function move the XIQ account from free pilot or trial mode into pilot mode by using the ‘ADD LICENSE’
button from unmanage dialog
:param username: SFDC username account
:param password: SFDC password account
:param shared_cuid: SFDC shared cuid
:return: 1 if account was moved into Pilot mode  ; else -1


#### navigate_to_device_configure(ap_name)

* Click on the AP Rows host name –> Configure


* **Parameters**

    **ap_name** – AP’s name



* **Returns**

    success 1 else -1



#### navigate_to_wireless_interface_details(ap_name)

* Assumes that already navigated to the Manage –> Devices


* Click on the AP Rows host name –> Wireless Interfaces


* **Parameters**

    **ap_name** – AP’s Serial Number



* **Returns**

    1



#### onboard_ap(ap_serial, device_make, location, device_os=False)

* This keyword on-boards an aerohive device [AP or Switch] using Quick on-boarding flow.


* Keyword Usage:

> 
> * `Onboard Ap   ${AP_SERIAL}   ${AP_TYPE}`


* **Parameters**

    
    * **ap_serial** – serial number of AP


    * **device_make** – Model of the AP i.e aerohive


    * **device_os** – verifies the Device OS automatically selected after entering device serial


    * **location** – location of the device Ex: San Jose, building_01, floor_02



* **Returns**

    1 if on boarded else -1



#### onboard_device(device_serial, device_make, device_mac=False, device_type='Real', entry_type='Manual', csv_file_name='', device_os=False, location=False, service_tag=False, \*\*kwargs)

* This keyword on boards an aerohive device [AP or Switch] , Exos Switch and Voss devices using Quick on boarding flow.


* Keyword Usage:

> 
> * `Onboard Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}`


> * `Onboard Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}  device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}`


* **Parameters**

    
    * **device_serial** – serial number of Device


    * **device_make** – Model of the Device ex:aerohive


    * **device_mac** – Device MAC


    * **device_type** – Real/Simulated


    * **entry_type** – Manual/CSV


    * **csv_file_name** – CSV File Name


    * **device_os** – verifies the Device OS automatically selected after entering device serial


    * **location** – device location



* **Returns**

    1 if onboarding success



* **Returns**

    -2 for error - Serial numbers entered are from different platform families. Please enter serial numbers that are part of the same platform family. Please remove serial number



* **Returns**

    -3 for error - Could not recognize 166A129943554583. Please onboard 166A129943554583 separately.



* **Returns**

    -4 for error - No more than 10 serial numbers could be entered at once.



* **Returns**

    -5 for error - When onboarding multiple devices, serial numbers must be separated by “, ” (Commas).



* **Returns**

    -6 for error - The number of MAC Addresses must match the number of Serial Numbers



* **Returns**

    -7 for error - Please enter a valid MAC Address



* **Returns**

    -8 for error - Unable to get pop-up menu item



#### onboard_exos_device(device_serial, device_make='exos', device_type='Real', entry_type='Manual', csv_file_name='', policy_name=None, loc_name=None)

* This keyword onboards an EXOS device using Quick on boarding flow.


* Keyword Usage:

> 
> * `Onboard EXOS Device  ${DEVICE_SERIAL}`


> * `Onboard EXOS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}`


> * `Onboard EXOS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    policy_name=${POLICY_NAME}    loc_name=${LOCATION_NAME}`


> * 

> ```
> ``
> ```

> Onboard EXOS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}


* **Parameters**

    
    * **device_serial** – serial number of Device


    * **device_make** – Model of the Device (e.g., exos, etc.)


    * **device_type** – Real/Simulated


    * **entry_type** – Manual/CSV


    * **csv_file_name** – Csv File name  from folder testsuites/xiq/functional/onboard_csv_files


    * **policy_name** – Name of the policy to assign to the device (if not specified, policy will not be assigned)


    * **loc_name** – Location to assign to the device (if not specified, location will not be assigned)



* **Returns**

    1



#### onboard_multiple_devices(serials, device_make)

* This Keyword will Onboard Multiple Devices with Serial Numbers and AP type


* Keyword Usage:

> 
> * Onboard Multiple Devices  ${SERIALS}  {AP_TYPE}\`


* **Parameters**

    
    * **serials** – Serial Numbers seperated by comma


    * **ap_type** – AP Type ie aerohive,wing



* **Returns**

    1 if on boarded else -1



#### onboard_multiple_exos_switches(device_serials, device_make='exos')

* This Keyword will Onboard Multiple Exos Devices with Serial Numbers


* Keyword Usage:

> 
> * Onboard Multiple Exos Devices  ${SERIAL1},${SERIAL2},${SERIALS3}  {DEVICE_MAKE}\`


> * Onboard Multiple Exos Devices  ${SERIAL1},${SERIAL2},${SERIALS3}\`


* **Parameters**

    
    * **device_serials** – Serial Numbers seperated by comma


    * **device_make** – Device Make Type ie EXOS



* **Returns**

    1 if Exos Devices on boarded Successfully else -1



#### onboard_simulated_device(device_model, count=1, location=None, policy=None)

* onboard multiple simulated devices of same type and returns their serial number(s)


* Keyword Usage:

> 
> * `Onboard Simulated Device  ${DEVICE_TYPE}   count=2`


> * For supported ${DEVICE_TYPE} look the device type drop down in quick add


* **Parameters**

    
    * **device_model** – device model to onboard


    * **count** – number of devices to onboard


    * **location** – device location


    * **policy** – network policy - optional parameter



* **Returns**

    returns the serial number(s) of newly onboarded devices



#### onboard_switch_device(device_serial, device_make, device_type='Real', entry_type='Manual', csv_location='', policy_name=None, loc_name=None)

* This keyword onboards a switch device (exos/voss) using Quick on boarding flow.


* Keyword Usage:

> 
> * `Onboard Switch Device  ${DEVICE_SERIAL}   EXOS`


> * `Onboard Switch Device  ${DEVICE_SERIAL}   VOSS`


> * `Onboard Switch Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    policy_name=${POLICY_NAME}    loc_name=${LOCATION_NAME}`


> * 

> ```
> ``
> ```

> Onboard Switch Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}


* **Parameters**

    
    * **device_serial** – serial number of Device


    * **device_make** – Model of the Device (e.g., exos, voss, etc.)


    * **device_type** – Real/Simulated


    * **entry_type** – Manual/CSV


    * **csv_location** – Absolute Path of Device onboarding CSV File Location on remote Machine


    * **policy_name** – Name of the policy to assign to the device (if not specified, policy will not be assigned)


    * **loc_name** – Location to assign to the device (if not specified, location will not be assigned)



* **Returns**

    1



#### onboard_voss_device(device_serial, device_type='Real', entry_type='Manual', csv_location='', policy_name=None, loc_name=None)

* This keyword onboards a VOSS device using Quick on boarding flow.


* Keyword Usage:

> 
> * `Onboard VOSS Device  ${DEVICE_SERIAL}`


> * `Onboard VOSS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}`


> * `Onboard VOSS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    policy_name=${POLICY_NAME}    loc_name=${LOCATION_NAME}`


> * 

> ```
> ``
> ```

> Onboard VOSS Device  ${DEVICE_SERIAL}   ${DEVICE_MAKE}    device_type=Real   entry_type=CSV  csv_location=${DEVICE_CSV_PATH}


* **Parameters**

    
    * **device_serial** – serial number of Device


    * **device_make** – Model of the Device (e.g., voss, etc.)


    * **device_type** – Real/Simulated


    * **entry_type** – Manual/CSV


    * **csv_location** – Absolute Path of Device onboarding CSV File Location on remote Machine


    * **policy_name** – Name of the policy to assign to the device (if not specified, policy will not be assigned)


    * **loc_name** – Location to assign to the device (if not specified, location will not be assigned)



* **Returns**

    1



#### onboard_wing_ap(device_serial, device_mac, device_make, location=False)

* This keyword on-boards an WiNG device [AP or Switch] using Quick on-boarding flow.


* Keyword Usage:

> 
> * `Onboard Ap   ${AP_SERIAL}   ${AP_MAC}`


* **Parameters**

    
    * **device_serial** – serial number of AP


    * **device_make** – Model of the AP i.e WiNG


    * **device_mac** – Device MAC


    * **location** – Device location



* **Returns**

    1 if on boarded else -1



#### onboard_xiq_site_engine(xiqse_serial)

* This keyword on boards an XIQ Site Engine using the Quick Add Devices flow.


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Onboard XIQ Site Engine  ${XIQSE_SERIAL}


* **Parameters**

    **xiqse_serial** – serial number of the XIQ Site Engine



* **Returns**

    1



#### onboarding_stack_per_unit(serial_numbers_list, device_os, location)
This functions onboard serials one by one
:param serial_numbers_list: list of SNs
:param device_os: device os
:param location: location
:return: 1 if all SN was onboarded; else -1


#### perform_search_on_devices_table(the_value)

* Enters the search string value into the Search box on the Manage> Devices page.


* Note: currently, search is only supported for Serial Number, MAC Address, Host Name, or Ip Address.


* Keyword Usage:

> 
> * `Perform Search On Devices Table  ${SERIAL}`


> * `Perform Search On Devices Table  ${HOST_NAME}`


> * `Perform Search On Devices Table  ${MAC}`


> * `Perform Search On Devices Table  ${IP_ADDRESS}`


* **Parameters**

    **the_value** – value to enter in the search box above the Devices table (Serial, MAC Address, or Host Name)


:return  1 if action was successful, else -1


#### pilot_lic_inventory_from_unmanage_box(max_time=120, interval_time=20)
This function returns the number of license which should be consumed and the number of license available from
unmanage box. These are displayed into this format   e.g.  1/0
:param max_time: Maximum duration of check
:param interval_time: Time interval between two consecutive checks
:return: the number of license which should be consumed and the number of license available from
unmanage box. These are displayed into this format   e.g.  1/0  ; else -1


#### quick_onboarding_cloud_csv(device_make, csv_location, location=None, policy_name=None)
This keyword on boards your devices directly to cloud by using new onboarding flow
Can on boards an aerohive device [AP or Switch], Universal APs , Exos Switch, Exos Stack and Voss devices
using Quick onboarding flow.
- Keyword Usage:

> 
> * quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}


* **Parameters**

    
    * **device_sn** – serial number of Device; single SN or a list of SNs


    * **device_make** – Model of the Device e.g. :aerohive/universal_ap/voss/exos


    * **location** – The location, building and floor separated by comma ; e.g. Bucharest,address,Floor 1


    * **csv_location** – csv file path


e.g. ${DUT_CSV_FILE}             /automation/xiq/cw_automation/testsuites/xiq/topologies/${TESTBED}/MultipleVossDevices.csv
:param policy_name: The policy name
:return: 1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message

> will be returned ; else -1


#### quick_onboarding_cloud_manual(device_sn, device_make, location, policy_name=None)
This keyword on boards your devices directly to cloud by using new onboarding flow
Can on boards an aerohive device [AP or Switch], Universal APs , Exos Switch, Exos Stack and Voss devices
using Quick onboarding flow.
- Keyword Usage:

> 
> * quick_onboarding_cloud_manual          ${DUT_SERIAL}    voss      Bucharest,address,Floor 1


* **Parameters**

    
    * **device_sn** – serial number of Device; single SN or a list of SNs


    * **device_make** – Model of the Device e.g. :aerohive/universal_ap/voss/exos


    * **location** – The location, building and floor separated by comma ; e.g. Bucharest,address,Floor 1


    * **policy_name** – The policy name



* **Returns**

    1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message
    will be returned ; else -1



#### quick_onboarding_locally_csv(device_make, csv_location)
This keyword on boards your devices locally by using new onboarding flow
Can on boards an Wing device, Exos Switch, Exos Stack and Voss devices
using Quick onboarding flow.
- Keyword Usage:

> 
> * quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}


* **Parameters**

    
    * **device_make** – Model of the Device e.g. :aerohive/universal_ap/voss/exos


    * **csv_location** – csv file path


e.g. ${DUT_CSV_FILE}             /automation/xiq/cw_automation/testsuites/xiq/topologies/${TESTBED}/MultipleVossDevices.csv
:return: 1 if successfully onboarded; if any error occurs on banner the text of error message will be returned ;

> else -1


#### quick_onboarding_locally_manual(device_sn, device_make)
This keyword on boards your devices locally by using new onboarding flow
Can on boards an Universal APs, Exos Switch, Exos Stack and Voss devices
using Quick onboarding flow.
- Keyword Usage:

> 
> * quick_onboarding_cloud_csv          voss      ${DUT_LOCATION}   ${DUT_CSV_FILE}


* **Parameters**

    **device_make** – Model of the Device e.g. :aerohive/universal_ap/voss/exos



* **Returns**

    1 if successfully onboarded; if any error occurs on banner or when enter the SN the text of error message
    will be returned ; else -1



#### rbac_user_multiple_location_search_AP_serial(ap_serial)

* Searches for AP matching AP’s Serial Number based on


* Keyword Usage:

> 
> * `Search AP Serial  ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – AP’s Serial Number



* **Returns**

    return 1 if AP found else False



#### reboot_device(device_serial)

* Assumes that already navigated to Manage –> Devices


* This method reboots a device matching the serial(s)


* Keyword Usage:

> 
> * `Reboot Device  ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    None



#### reboot_device_while_update(device_serial)

* Assumes that already navigated to Manage –> Devices


* This method reboots a device matching the serial(s)


* Keyword Usage:

> 
> * `Reboot Device  ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    None



#### refresh_devices_page(\*\*kwargs)

* This Keyword will Refresh the Devices Page


* keyword Usage:

> 
> * `Refresh Devices Page`


* **Returns**

    1 if device page refreshed successfully else -1



#### revert_device_to_template(device_serial)

* Assumes already navigated to Manage –> Devices


* This method accesses the “Revert Device to Template” action for a device matching the specified serial


* Keyword Usage:

> 
> * `Revert Device to Template  ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial number of the device to perform the action on



* **Returns**

    1 if action succeeds, else -1



#### revoke_device_license(device_serial, license_type, username=None, password=None, shared_cuid=None, warning_msg=None, skip_warning_check=False)
This function revoke premier or macsec license on a device


* **Parameters**

    
    * **device_serial** – Serial of device


    * **license_type** – premier or macsec



* **Returns**

    1 if license was revoked ; else -1



#### search_ap(ap_serial=None, ap_name=None, ap_mac=None)

* Searches for the AP matching either one of serial, name or MAC


* Keyword Usage:

> 
> * `Search AP  ap_serial=${AP_SERIAL}`


> * `Search AP  ap_name=${AP_NAME}`


> * `Search AP  ap_mac=${AP_MAC}`


* **Parameters**

    
    * **ap_serial** – AP Serial


    * **ap_name** – AP Name


    * **ap_mac** – AP MAC



* **Returns**

    1 if ap present in the grid else False



#### search_ap_mac(ap_mac=None)

* Searches for AP matching AP’s MAC


* Keyword Usage

> 
> * `Search Ap Mac   ${AP_MAC}`


* **Parameters**

    **ap_mac** – AP’s MAC



* **Returns**

    return 1 if AP found else -1



#### search_ap_model(ap_model)

* Searches for AP matching AP’s Model


* Keyword Usage:

> 
> * `Search AP Model ${AP_MODEL}`


* **Parameters**

    **ap_model** – AP’s Name



* **Returns**

    return 1 if AP found else -1



#### search_ap_name(ap_name)

* Searches for AP matching AP’s Host NAME


* Keyword Usage:

> 
> * `Search AP Name  ${AP_NAME}`


* **Parameters**

    **ap_name** – AP’s Name



* **Returns**

    return 1 if AP found



#### search_ap_serial(ap_serial)

* Searches for AP matching AP’s Serial Number


* Keyword Usage:

> 
> * `Search AP Serial  ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – AP’s Serial Number



* **Returns**

    return 1 if AP found else False



#### search_device(device_serial=None, device_name=None, device_mac=None, \*\*kwargs)

* Searches for the device matching either one of serial, name or MAC


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device Name


    * **device_mac** – device MAC



* **Returns**

    1 if device found else -1



#### search_device_model(device_model)

* Searches for Device matching Device’s name in device grid


* Keyword Usage:

> 
> * `Search Device Model  ${DEVICE_MODEL}`


* **Parameters**

    **device_model** – Device’s Name



* **Returns**

    return 1 if Device found



#### search_exos_device(EXOS_VOSS_device)

#### select_all_devices()

* This keyword selects all devices in the table by clicking the Select All check box column header


* Keyword Usage:

    
        * Select All Devices

:param None
:return: returns 1 if the Select All checkbox was clicked; else, -1


#### select_ap(ap_serial=None, ap_name=None, ap_mac=None)

* Selects the AP row marching with AP’s Serial Number


* Keyword USage:

> 
> * `Select AP   ${AP_SERIAL}`


* **Parameters**

    
    * **ap_serial** – AP’s Serial Number


    * **ap_name** – host name of the AP


    * **ap_mac** – ap Mac address



* **Returns**

    return 1 if AP found and selected else -1



#### select_device(device_serial=None, device_name=None, device_mac=None)

* Selects the device matching device’s Serial Number,Device Mac address and device mane


* Keyword Usage:

> 
> * `Select Device      device_serial=${DEVICE_SERIAL}`


> * `Select Device      device_name=${DEVICE_NAME}`


> * `Select Device      device_mac=${DEVICE_MAC}`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device host name


    * **device_mac** – device MAC address



* **Returns**

    return 1 if device found else False



#### select_location_quick_onboarding(sel_loc)

* This keyword selects a location in the location dialog and clicks the “Select” button.
It is assumed the location dialog is already open.


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Select Location  ${LOCATION}


* **Parameters**

    **sel_loc** – location to select, in a comma-separated list format; e.g., San Jose, building_01, floor_02



* **Returns**

    1 if location is selected, else -1’



#### select_table_view_type(view_type='Default View')

* This keyword selects the view type for the Manage> Devices view.


* Keyword Usage:

    
        * Select Table View Type   ${VIEW_TYPE}


* **Parameters**

    **view_type** – view type to select (Default View, Wireless View, LAN View, WAN View)



* **Returns**

    returns 1 if the specified view type was selected; else, -1



#### select_version_and_upgrade_device_to_specific_version(device_serial, version)

* This method update device to specific version from the dropdown


* keyword Usage:

> 
> * Select Version And Upgrade Device To Specific Version    ${DEVICE_SERIAL}   version=${VERSION}


* **Parameters**

    
    * **device_serial** – serial number(s) of the device(s)


    * **version** – version to which device(s) should get upgraded. This string should be contains into image name . e.g : 5520.8.3.0.0



* **Returns**

    1 if success else -1



#### sort_device_grid_with_mgmt_ip_address(sort='ascending')

* This keyword is used to sort up or sort down the device grid with MGMT IP ADDRESS column


* This sorting apply the all device present in the device grid


* By default this keyword sort the device grid in ascending order


* Flow:

> 
> * Navigate to the Device page


> * Click on MGT IP ADDRESS Column to sort up or sort down based on the sorting parameter


* Keyword Usage:

> 
> * `Sort Device Grid With Mgmt Ip Address  ascending`


> * `Sort Device Grid With Mgmt Ip Address  descending`


* **Parameters**

    **sort** – sorting method i.e ascending, descending



* **Returns**

    


* sorted list values if sorting is matched with GUI sorted the grid values by logic sorted values

> 
> * 
>     * Here “logic sorted values” means taking the unsorted device grid values and applying the sort method over those values


* 
#### sort_device_grid_with_updated(sort='ascending')

* This keyword is used to sort ascending(up) or sort descending(down) the device grid with “UPDATED” column


* This sorting apply the all device present in the device grid


* By default this keyword sort the device grid in ascending order


* Flow:

> 
> * Navigate to the Device page


> * Click on “UPDATED” column to sort ascending or sort descending based on the sorting parameter


* Keyword Usage:

> 
> * `Sort Device Grid With Updated  ascending`


> * `Sort Device Grid With Updated  descending`


* **Parameters**

    **sort** – sorting method i.e ascending, descending



* **Returns**

    


* sorted list values if sorting is matched with GUI sorted grid values with logic sorted values

> 
> * Here “logic sorted values” means taking the unsorted device grid values and applying the sort method over those values


* 
#### teardown_check_and_revoke_license(device_sn)
This function revoke all device license
:param device_sn: Sn of device
:return: 1 if device license status in “None” ; else -1


#### unlink_sfdc_account()
This function presses the unlink button from License Management page
:return: 1 if the account was unlinked ; else -1


#### unmanage_device_when_license_expired(device_sn)
This function unmanage a device when unmanage box is displayed
:param device_sn: Sn of device
:return: 1 when device was unmanage ; else -1


#### update_device_auto_template(device_mac, name_stack_template)
This function will go to Device Update and press create auto template and name the template


* **Parameters**

    
    * **device_mac** – Mac of device


    * **name_stack_template** – Policy template name



* **Returns**

    1 if remain in the Create auto Template ; -1 else



#### update_device_delta_configuration(device_serial, update_method='Delta')

* This Keyword will Update Device Configuration based on device serial number


* Keyword Usage:

> 
> * `Update Device Delta Configuration  ${DEVICE_SERIAL}`


> * `Update Device Delta Configuration  ${DEVICE_SERIAL}  ${UPDATE_METHOD}=Complete`


* **Parameters**

    
    * **device_serial** – Device Serial Number


    * **update_method** – Delta/Complete



* **Returns**

    


#### update_device_policy_config_image(device_serial)

#### update_device_policy_config_reboot(device_serial)

#### update_device_policy_config_simple(device_serial)

#### update_device_policy_image(device_serial)

#### update_device_using_hostname(device_name)

* Update the network policy to the selected devices


* Based on the update method, update the devices


* Keyword Usage:


* 

```
``
```

Update Device Using Hostname    name=${SW_HOST}     ‘\`


* **Parameters**

    **update_method** – PolicyAndConfig - selects the “Update Network Policy and Configuration” check button



* **Returns**

    1 if update was performed, -1 if not



#### update_network_device_firmware(device_mac='default', version='default', forceDownloadImage='true', performUpgrade='true', saveDefault='false', updateTo='latest', updatefromD360Page='false', retry_duration=30, retry_count=1200)

* This method update device to latest version or to a specific version from the dropdown


* This method needs import datetime as dt


* Varibale and it’s possible values


* updateTo = {“latest”|”anything other than latest”}


* saveDefault = {true| false}


* performUpgrade = {true| false}                                                    # ‘false’ will be treated as ‘closing’ the update window


* forceDownloadImage = {true| false}


* version = {‘default’|’first’|’last’|’latest’|’noncurrent’|’specific version’}


* device_mac = {“mac adress of the device”}


* updatefromD360Page= {false|true}                                                  # Update page will be launched from D360 if it is true


* The retry_duration and retry_count will check for the firmware upgrade status as per these varibale values


* keyword Usage:


* Select Version And Upgrade Device To Latest Version    ${DEVICE_MAC}


* Select Version And Upgrade Device To Specific Version    ${DEVICE_MAC}   version=${VERSION}   updateTo=${“specific”}


* **Parameters**

    
    * **device_mac** – mac address of the device


    * **version** – version to which device should get upgraded. This string should contain into image name . e.g VOSS: “8.3.0.0”, EXOS “31.6.1.2”


    * **updateTo** – This will hold either “latest” or anything other than latest will be treated as a “specific version” except NULL



* **Returns**

    updateToVersion if success else -1



#### update_network_policy_to_all_devices(policy_name=None, update_method='Delta')

* By default this keyword do delta config push


* Flow: MANAGE–>Devices–>Select All Devices to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* Select All Devices–> Update device


* Keyword Usage:

> 
> * `Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}`


> * `Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}  update_method=Complete`


* **Parameters**

    
    * **policy_name** – name of the network to deploy


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if policy is updated else -1



#### update_network_policy_to_ap(policy_name=None, ap_serial=None, update_method='Delta')

* By default this keyword do delta config push


* Go To MANAGE–>Devices–>Select AP row  to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* select AP–>Update device


* Keyword Usage:

> 
> * `Update Network Policy To Ap   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}`


> * `Update Network Policy To Ap   policy_name=${POLICY_NAME}    ap_serial=${AP1_SERIAL}  update_method=Complete`


* **Parameters**

    
    * **policy_name** – name of the network to deploy


    * **ap_serial** – serial number of the ap to select


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if policy is updated else -1



#### update_network_policy_to_exos(serial=None, update_method='PolicyAndConfig')

* Update the network policy to the selected devices


* Based on the update method, update the devices


* Keyword Usage:


* `Update Network Policy To Exos      serial=${SW1_SERIAL}     update_method="PolicyAndConfig"`


* **Parameters**

    **update_method** – PolicyAndConfig - selects the “Update Network Policy and Configuration” check button



* **Returns**

    1 if update was performed, -1 if not



#### update_network_policy_to_multiple_ap(policy_name='', ap_serial='', update_method='Delta')

* This keyword is used to update/config push the network policy to the multiple AP’s


* By default this keyword do delta config push


* Procedure:

> 
> * Navigate to the Manage –> Device page


> * Select the multiple AP’s rows


> * Click on ACTIONS –> Assign Network Policy –> Select the network policy from drop down –> Assign


> * select the multiple AP’s


> * click on UPDATE DEVICES –> Update the delta or complete configuration update based on update method


* Keyword Usage:

> 
> * `Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serials=${AP1_SERIAL},${AP2_SERIALS}`


> * `Update Network Policy To All Devices   policy_name=${POLICY_NAME}    ap_serials=${AP1_SERIAL},${AP2_SERIALS}   update_method=Complete`


* **Parameters**

    
    * **policy_name** – name of the network to deploy


    * **ap_serial** – comma separated ap serial numbers


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if policy is updated else -1



#### update_network_policy_to_router(policy_name=None, router_serial=None, update_method='Delta')

* Go To MANAGE–>Devices–>Select Device row  to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* select AP–>Update device


* By default Delta config push will happen


* Keyword Usage:

> 
> * `Update Network Policy To Router   policy_name=${POLICY_NAME}`


> * `Update Network Policy To Router   router_serial=${ROUTER_SERIAL}`


* **Parameters**

    
    * **policy_name** – name of the network to deploy


    * **router_serial** – serial number of the ap to select


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if policy updated else -1



#### update_network_policy_to_stack(device_mac, policy_name, template_policy_name)

* Update the network policy to the selected stack devices


* Keyword Usage:


* 

```
``
```

Update Network Policy To Stack      device_mac  policy_name template_policy_name


* **Param**

    device_mac Device master MAC



* **Param**

    policy_name Name of policy



* **Param**

    template_policy_name Name of template



* **Returns**

    1 if update was performed, -1 if not



#### update_network_policy_to_switch(policy_name=None, serial=None, update_method='PolicyAndConfig')

* This keyword does a config push for a switch


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Actions–>Assign Network Policy –>Select the network policy to assign


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}`


> * `Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}  update_method=PolicyAndConfig`


> * `Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}  update_method=EngineAndImages`


> * `Update Network Policy To Switch  policy_name=${POLICY_NAME}  serial=${SWITCH_SERIAL}  update_method=Complete`


* **Parameters**

    
    * **policy_name** – name of the network policy to deploy


    * **serial** – serial number of the switch to select


    * **update_method** – PolicyAndConfig - selects just the “Update Network Policy and Configuration” check button
    EngineAndImages - selects just the “Upgrade IQ Engine and Extreme Network Switch Images” check button
    Complete        - selects both check buttons



* **Returns**

    1 if policy is updated else -1



#### update_override_configuration_to_device(device_serial='', update_method='Delta')

* This keyword uses to update configuration to the device using Device Serial Number


* Assume that Device already assigned Network Policy and Need to update Device Override Configuration.


* By default this keyword do delta config push


* Flow: MANAGE–>Devices–>Select a Device –>Update Devices


* Keyword Usage:

> 
> * `Update Override Configuration To Device   ap_serial=${AP1_SERIAL}`


> * `Update Override Configuration To Device   ap_serial=${AP1_SERIAL}  update_method=Delta`


> * `Update Override Configuration To Device   ap_serial=${AP1_SERIAL}  update_method=Complete`


* **Parameters**

    
    * **device_serial** – device serial number to update the override policy


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if Device Updated successfully else -1



#### update_override_configuration_to_multiple_devices(device_serials='', update_method='Delta')

* This keyword uses to update configuration with Multiple devices for Device override configuration.


* Assumes that Devices already assigned Network Policy and Need to update Device Override Configuration.


* By default this keyword do delta config push


* Flow: MANAGE–>Devices–>Select Multiple Devices –>Update Devices


* Keyword Usage:

> 
> * `Update Override Configuration To Multiple Devices   device_serials=${AP1_SERIAL},${AP2_SERIAL}`


> * `Update Override Configuration To Multiple Devices   device_serials=${AP1_SERIAL},${AP2_SERIAL}   update_method=Delta`


> * `Update Override Configuration To Multiple Devices   device_serials=${AP1_SERIAL},${AP2_SERIAL}   update_method=Complete`


* **Parameters**

    
    * **device_serials** – device serial  numbers


    * **update_method** – Perform Complete update or delta update



* **Returns**

    1 if Devices Updated successfully else -1



#### update_policy_and_configuration_stack(device_serial_mac_or_name=None)

* This keyword does a config push for a switch, selecting just the “Update Network Policy and Configuration”
check button in the Device Update dialog.


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Update Policy and Configuration  ${SWITCH_SERIAL}`


> * `Update Policy and Configuration  ${SWITCH_MAC}`


> * `Update Policy and Configuration  ${SWITCH_NAME}`


* **Parameters**

    **device_serial_mac_or_name** – device serial number, mac or name  of the switch to update



* **Returns**

    1 if config push success else -1



#### update_switch_complete(serial)

* This keyword does a config push for a switch, selecting both check buttons in the Device Update dialog.


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Update Switch Complete  ${SWITCH_SERIAL}`


* **Parameters**

    **serial** – serial number of the switch to update



* **Returns**

    1



#### update_switch_iq_engine_and_images(serial)

* This keyword does a config push for a switch, selecting just the “Upgrade IQ Engine and Extreme Network
Switch Images” check button in the Device Update dialog.


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Update Switch IQ Engine and Images  ${SWITCH_SERIAL}`


* **Parameters**

    **serial** – serial number of the switch to update



* **Returns**

    1



#### update_switch_policy_and_configuration(serial)

* This keyword does a config push for a switch, selecting just the “Update Network Policy and Configuration”
check button in the Device Update dialog.


* Go To Manage–>Devices–>Select switch row to apply the network policy


* Select Switch–>Update device


* Keyword Usage:

> 
> * `Update Switch Policy and Configuration  ${SWITCH_SERIAL}`


* **Parameters**

    **serial** – serial number of the switch to update



* **Returns**

    1



#### upgrade_device_to_latest_version(device_serial)

* This method update device(s) to latest version from the dropdown


* Keyword Usage:

> 
> * `Upgrade Device To Latest Version   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial number(s) of the device(s)



* **Returns**

    1 if success else -1



#### upgrade_device_to_specific_version(device_serial, version=None)

* This method update device(s) to specific version from the dropdown


* keyword Usage:

> 
> * `Upgrade Device To Specific Version    ${DEVICE_SERIAL}   version=${VERSION}`


* **Parameters**

    
    * **device_serial** – serial number(s) of the device(s)


    * **version** – version to which device(s) should get upgraded



* **Returns**

    1 if success



#### verify_device_status(device_serial='default', device_name='default', device_mac='default', status='default')

* This keyword returns 1 if device status expected matches the status passed as argument


* Keyword Usage:

> 
> * `Verify Device Status   device_serial=${DEVICE_SERIAL}    status=green`


> * `Verify Device Status   device_name=${DEVICE_NAME}    status=green`


> * `Verify Device Status   device_mac=${DEVICE_MAC}    status=green`


* **Parameters**

    
    * **device_serial** – device Serial


    * **device_name** – device Name


    * **device_mac** – device MAC


    * **status** – green, red, or amber as of now - may change in future



* **Returns**

    


#### verify_network_policy_column_is_not_sortable()
This keyword verifies whether the Devices grid’s Network Policy column shows it is sortable or not in a tooltip
:return 1 if we get a tool-tip message “Network Policy - This column is not sortable” else it returns -1


#### verify_stack_devices_managed(stack_mac, slot_serial_list)

* This keyword waits until the specified column for the specified device contains managed state.


* This keyword by default loops every 30 seconds for 10 times to check the column data


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the specified device column for data


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Verify Stack Devices Managed  ${STACK_MAC}  ${SLOT_SERIAL_LIST} \`\`


* **Parameters**

    
    * **stack_mac** – stack mac in use with which stack is onboarded


    * **slot_serial_list** – list of serial numbers of stack devices to check the devices managed status


    * **col** – column name to check for data



* **Returns**

    1 if column contains data within the specified time, else -1



#### wait_for_device_to_finish_update(device_serial=None, device_name=None, device_mac=None, retry_duration=10, retry_count=30, \*\*kwargs)

* This keyword waits for the device to finish updates


* This keyword by default loop over every 10 seconds for up to 5 minutes to check the device updated status


* Flow:

> 
> * check the device status for a device based on passed device serial/device mac/device_name


* Keyword Usage:

> 
> * `wait_for_device_to_finish_update       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12`


> * `wait_for_device_to_finish_update       ${DEVICE_MAC}           retry_duration=15       retry_count=5`


* **Parameters**

    
    * **device_serial** – device serial number to check the device update status


    * **device_mac** – device mac to check the device update status


    * **device_name** – device name to check the device update status


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device finished update, else -1



#### wait_until_all_devices_update_done(wait_time_in_min, \*\*kwargs)

* This Keyword checks if all devices are done with updating


* Keyword Usage:


* `wait_until_all_devices_update_done`

    
    * **param  wai_time_in_min**

        time to wait



    * **return**

        1 if done, -1 if not



#### wait_until_device_added(device_serial=None, device_name=None, device_mac=None, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show up in XIQ.


* This keyword by default loops 10 times every 30 seconds to check if the device exists


* Flow:

> 
> * Navigate to Manage –> Devices


> * search for the device based on specified device criteria


* Keyword Usage:

> 
> * `Wait Until Device Added    device_serial=${DEVICE_SERIAL}    retry_duration=15    retry_count=20`


> * `Wait Until Device Added    device_name=${DEVICE_NAME}        retry_duration=20    retry_count=15`


> * `Wait Until Device Added    device_mac=${DEVICE_MAC}          retry_duration=30    retry_count=10`


* **Parameters**

    
    * **device_serial** – device serial number to look for


    * **device_name** – device name to look for


    * **device_mac** – device MAC address to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### wait_until_device_data_present(device_serial, col, retry_duration=30, retry_count=10)

* This keyword waits until the specified column for the specified device contains data.


* This keyword by default loops every 30 seconds for 10 times to check the column data


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the specified device column for data


* Keyword Usage:

> 
> * `Wait Until Device Data Present  ${DEVICE_SERIAL}    MAC    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_serial** – device serial number to check the device connected status


    * **col** – column name to check for data


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if column contains data within the specified time, else -1



#### wait_until_device_managed(device_serial, col='MANAGED', retry_duration=30, retry_count=10)

* This keyword waits until the specified column for the specified device contains managed state.


* This keyword by default loops every 30 seconds for 10 times to check the column data


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the specified device column for data


* Keyword Usage:

> 
> * `Wait Until Device Data Present  ${DEVICE_SERIAL}    MAC    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_serial** – device serial number to check the device connected status


    * **col** – column name to check for data


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if column contains data within the specified time, else -1



#### wait_until_device_offline(device_serial=None, device_mac=None, retry_duration=30, retry_count=10)

* This keyword waits until the device status in XIQ is “Disconnected” or “Unknown”.


* After Configuring the CAPWAP client server in device cli, check the device connected status


* This keyword by default loop over every 30 seconds for 10 times to check the device connected status


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the device status for a device based on passed device serial


* Keyword Usage:

> 
> * `Wait Until Device Offline       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12`


> * `Wait Until Device Online       ${DEVICE_MAC}           retry_duration=15       retry_count=5`


* **Parameters**

    
    * **device_serial** – device serial number to check the device connected status


    * **device_mac** – device mac to check the device connected status


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device disconnected within time, else -1



#### wait_until_device_online(device_serial=None, device_mac=None, retry_duration=30, retry_count=10, \*\*kwargs)

* This keyword is used to check the device connected status on XIQ.


* After Configuring the CAPWAP client server in device cli, check the device connected status


* This keyword by default loop over every 30 seconds for 10 times to check the device connected status


* Flow:

> 
> * Navigate to Manage –> Devices


> * check the device status for a device based on passed device serial


* Keyword Usage:

> 
> * `Wait Until Device Online       ${DEVICE_SERIAL}        retry_duration=10       retry_count=12`


> * `Wait Until Device Online       ${DEVICE_MAC}           retry_duration=15       retry_count=5`


* **Parameters**

    
    * **device_serial** – device serial number to check the device connected status


    * **device_mac** – device mac to check the device connected status


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device connected within time else -1



#### wait_until_device_reboots(device_serial, retry_duration=30, retry_count=10)

* This Keyword will wait until device reboots based on device update status message


* Keyword Usage:

> 
> * \`\` Wait Until Device Reboots  ${DEVICE_SERIAL}\`\`


* **Parameters**

    
    * **device_serial** – Device Serial Number


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count


If the reboot message has a date value, the assumption the device hase finished rebooting
:return: 1 if Device wait till reboots else -1


#### wait_until_device_removed(device_serial=None, device_name=None, device_mac=None, retry_duration=10, retry_count=30)

* This keyword is used to wait for the device to be removed from extauto.xiq.


* This keyword by default loops 10 times every 30 seconds to check if the device exists


* Flow:

> 
> * Navigate to Manage –> Devices


> * search for the device based on specified device criteria


* Keyword Usage:

> 
> * `Wait Until Device Removed    device_serial=${DEVICE_SERIAL}    retry_duration=15    retry_count=20`


> * `Wait Until Device Removed    device_name=${DEVICE_NAME}        retry_duration=20    retry_count=15`


> * `Wait Until Device Removed    device_mac=${DEVICE_MAC}          retry_duration=30    retry_count=10`


* **Parameters**

    
    * **device_serial** – device serial number to look for


    * **device_name** – device name to look for


    * **device_mac** – device MAC address to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device removed within time; else -1



#### wait_until_device_update_done(device_serial=None, wait_time_in_min=15, IRV=None)

* This keyword checks if the expected device is done with updating


* Keyword Usage:

> 
> * `wait_until_device_update_done   device_serial=${AP_SERIAL}`


* **Parameters**

    
    * **device_serial** – Serial number of AP Ex:11301810220048


    * **wait_time_in_min** – time to wait in mins


    * **IRV** – True or False



* **Returns**

    1 if done, -1 if not



#### wait_until_devices_load_mask_cleared(retry_duration=30, retry_count=10)

* This keyword waits until the Manage > Devices ‘loading’ mask is cleared.


* This keyword by default loops every 30 seconds for 10 times to check for the ‘loading’ mask.


* Flow:

> 
> * Assumes that the ‘Manage –> Devices’ view is already visible.


> * check for the ‘loading’ mask


* Keyword Usage:

> 
> * `Wait Until Devices Load Mask Cleared   retry_duration=10    retry_count=5`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if the ‘loading’ mask is cleared within the specified time, else -1



#### xiq_upgrade_device_to_latest_version(device_serial, action='perform upgrade')

* This method update device(s) to latest version from the XIQ


* Keyword Usage:

> 
> * `XIQ Upgrade Device To Latest Version   ${DEVICE_SERIAL}`


> * xiq_upgrade_device_to_latest_version(device_serial, action = “perform upgrade”)


* **Parameters**

    **device_serial** – serial number(s) of the device(s)



* **Returns**

    Latest firmware version if success else -1



#### xiq_upgrade_device_to_specific_version(device_serial, version=None)

* This method update device(s) to specific version from the dropdown


* keyword Usage:

> 
> * `XIQ Upgrade Device To Specific Version    ${DEVICE_SERIAL}   version=${VERSION}`


* **Parameters**

    
    * **device_serial** – serial number(s) of the device(s)


    * **version** – version to which device(s) should get upgraded



* **Returns**

    1 if success


## extauto.xiq.flows.manage.DevicesActions module


### _class_ extauto.xiq.flows.manage.DevicesActions.DevicesActions()
Bases: `object`


#### clear_audit_mismatch_on_device(device_serial)

* Assumes that already navigated to Manage –> Devices


* This method Clear Audit Mismatch for the device matching the serial(s)


* Keyword Usage:

> 
> * `clear_audit_mismatch_on_device  ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    None



#### perform_device_factory_reset(\*device_list)

* This Keyword performs factory reset on AP


* Navigate to Manage –> Device


* Select the device row based on the passed device serial


* Click on Utilities –> Status –> Reset Device to Default


* Handles device reset pop up and validates reset dialogue box message.


* Keyword Usage:

> 
> * `Perform Device Factory Reset     ${AP1_SERIAL}   ${AP2_SERIAL}`


* **Parameters**

    **device_list** – serial numbers of the devices



* **Returns**

    1 if Reset is Successful else -1



#### reset_device_to_default(\*device_list)

* This Keyword performs factory reset on AP


* Navigate to Manage –> Device


* Select the device row based on the passed device serial


* Click Utilities –> Reset Device to Default


* Handles device reset pop up and validates reset dialogue box message.


* Keyword Usage:

> 
> * `Reset Device to Default     ${AP1_SERIAL}   ${AP2_SERIAL}`


* **Parameters**

    **device_list** – serial numbers of the devices



* **Returns**

    1 if Reset is Successful else -1



#### select_device_utilities(\*device_list)

* This Keyword selects device utilities


* Select the device row based on the passed device serial –> clicks on Utilities


* Keyword Usage:

> 
> * `Select Device Utilities   ${DEVICE_SERIAL}`


* **Parameters**

    **device_list** – Device list



* **Returns**

    1 if selecting Utilities is successful



#### validate_reset_dialogue_box_msg(diag_msg, \*device_list)

* This Keyword validates reset status of dialogue box message


* Validates whether the device is success or fail in performing reset


* Assumes already in dialogue box pop up page


* **Parameters**

    
    * **diag_msg** – dialogue box message


    * **device_list** – Device list



* **Returns**

    Returns failed list and success device list


## extauto.xiq.flows.manage.DevicesUtilities module


### _class_ extauto.xiq.flows.manage.DevicesUtilities.DevicesUtilities()
Bases: `DeviceUtilitiesWebElements`


#### accept_device_tool_get_tech_data()

* This keyword is used to accept the request to continue to get tech data


* Keyword Usage:

> 
> * `Accept Device Tool Get Tech Data`


* **Returns**

    1 if Get Tech Data window is displayed else -1



#### close_device_tool_cli()

* This keyword is used to close the device CLI tool window


* Keyword Usage:

> 
> * `Close Device Tool Cli`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_client_information()

* This keyword is used to close the client information tool window


* Keyword Usage:

> 
> * `Close Device Tool Client Information`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_get_tech_data()

* This keyword is used to close the get tech data tool window


* Keyword Usage:

> 
> * `Close Device Tool Get Tech Data`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_locate_device()

* This keyword is used to close locate device tool window


* Keyword Usage:

> 
> * `Close Device Tool Locate Device`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_neighbor_info()

* This keyword is used to close the device neighbor info tool window


* Keyword Usage:

> 
> * `Close Device Tool Neighbor Info`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_packet_capture()

* This keyword is used to close the device Packet Capture tool window


* Keyword Usage:

> 
> * `Close Device Tool Packet Capture`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_ping()

* This keyword is used to close the device ping tool window


* Keyword Usage:

> 
> * `Close Device Tool Ping`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_amrp_tunnel()

* This keyword is used to close the device show AMRP Tunnel tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Amrp Tunnel`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_arp_cache()

* This keyword is used to close the device show ARP Cache tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Arp Cache`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_cpu()

* This keyword is used to close the device show CPU tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Cpu`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_dnxp_cache()

* This keyword is used to close the device show DNXP Cache tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Dnxp Cache`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_dnxp_neighbors()

* This keyword is used to close the device show DNXP Neighbors tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Dnxp Neighbors`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_gre_tunnel()

* This keyword is used to close the device show GRE Tunnel tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Gre Tunnel`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_ike_event()

* This keyword is used to close the device show IKE Event tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Ike Event`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_ike_sa()

* This keyword is used to close the device show IKE SA tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Ike Sa`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_ip_routes()

* This keyword is used to close the device show IP Routes tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Ip Routes`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_ipsec_sa()

* This keyword is used to close the device show IPsec SA tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Ipsec Sa`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_ipsec_tunnel()

* This keyword is used to close the device show IPsec Tunnel tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Ipsec Tunnel`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_log()

* This keyword is used to close the device show log tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Log`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_mac_routes()

* This keyword is used to close the device show MAC Routes tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Mac Routes`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_mac_table()

* This keyword is used to close the device show MAC Table tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Mac Table`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_memory()

* This keyword is used to close the device show memory tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Memory`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_pse()

* This keyword is used to close the device show PSE tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Pse`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_roaming_cache()

* This keyword is used to close the device show Roaming Cache tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Roaming Cache`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_running_config()

* This keyword is used to close the device show Running Config tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Running Config`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_startup_config()

* This keyword is used to close the device show Startup Config tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Startup Config`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_version()

* This keyword is used to close the device show version tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Version`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_show_vpn_tunnel()

* This keyword is used to close the device show VPN Tunnel tool window


* Keyword Usage:

> 
> * `Close Device Tool Show Vpn Tunnel`


* **Returns**

    1 if is not displayed else -1



#### close_device_tool_vlan_probe()

* This keyword is used to close the device VLAN Probe tool window


* Keyword Usage:

> 
> * `Close Device Tool Vlan Probe`


* **Returns**

    1 if is not displayed else -1



#### close_select_stack_member()

* This keyword is used to close the select stack member window


* Keyword Usage:

> 
> * `Close Select Stack Member`


* **Returns**

    1 if is not displayed else -1



#### is_device_spectrum_intelligence_available()

* This keyword checks if the spectrum intelligence option is available


* Keyword Usage:

> 
> * `Is Device Spectrum Intelligence Available`


* **Returns**

    1 if is displayed else -1



#### is_device_status_advanced_channel_selection_protocol_available()

* This keyword checks if the status advanced channel selection protocol option is available


* Keyword Usage:

> 
> * `Is Device Status Advanced Channel Selection Protocol Available`


* **Returns**

    1 if is displayed else -1



#### is_device_status_interface_available()

* This keyword checks if the status interface option is available


* Keyword Usage:

> 
> * `Is Device Status Interface Available`


* **Returns**

    1 if is displayed else -1



#### is_device_status_wifi_status_summary_available()

* This keyword checks if the status wifi status summary option is available


* Keyword Usage:

> 
> * `Is Device Status Wifi Status Summary Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_client_information_available()

* This keyword checks if the tool client information option is available


* Keyword Usage:

> 
> * `Is Device Tool Client Information Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_get_tech_data_available()

* This keyword checks if the tool get tech data option is available


* Keyword Usage:

> 
> * `Is Device Tool Get Tech Data Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_layer_neighbor_info_available()

* This keyword checks if the tool layer neighbor info option is available


* Keyword Usage:

> 
> * `Is Device Tool Layer Neighbor Info Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_locate_device_available()

* This keyword checks if the tool locate device option is available


* Keyword Usage:

> 
> * `Is Device Tool Locate Device Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_packet_capture_available()

* This keyword checks if the tool packet capture option is available


* Keyword Usage:

> 
> * `Is Device Tool Packet Capture Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_ping_available()

* This keyword checks if the diagnostic ping option is available


* Keyword Usage:

> 
> * `Is Device Tool Ping Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_amrp_tunnel_available()

* This keyword checks if the diagnostic show amrp tunnel option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Amrp Tunnel Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_arp_cache_available()

* This keyword checks if the diagnostic show arp cache option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Arp Cache Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_cpu_available()

* This keyword checks if the diagnostic show cpu option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Cpu Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_dnxp_cache_available()

* This keyword checks if the diagnostic show dnxp cache option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Dnxp Cache Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_dnxp_neighbors_available()

* This keyword checks if the diagnostic show dnxp neighbors option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Dnxp Neighbors Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_gre_tunnel_available()

* This keyword checks if the diagnostic show gre tunnel option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Gre Tunnel Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_ike_event_available()

* This keyword checks if the diagnostic show ike event option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Ike Event Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_ike_sa_available()

* This keyword checks if the diagnostic show ike sa option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Ike Sa Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_ip_routes_available()

* This keyword checks if the diagnostic show ip routes option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Ip Routes Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_ipsec_sa_available()

* This keyword checks if the diagnostic show ipsec sa option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Ipsec Sa Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_ipsec_tunnel_available()

* This keyword checks if the diagnostic show ipsec tunnel option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Ipsec Tunnel Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_log_available()

* This keyword checks if the diagnostic show log option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Log Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_mac_routes_available()

* This keyword checks if the diagnostic show mac routes option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Mac Routes Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_mac_table_available()

* This keyword checks if the diagnostic show mac table option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Mac Table Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_memory_available()

* This keyword checks if the diagnostic show memory option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Memory Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_pse_available()

* This keyword checks if the diagnostic show pse option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Pse Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_roaming_cache_available()

* This keyword checks if the diagnostic show roaming cache option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Roaming Cache Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_running_config_available()

* This keyword checks if the diagnostic show running config option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Running Config Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_startup_config_available()

* This keyword checks if the diagnostic show startup config option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Startup Config Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_show_version_available()

* This keyword checks if the diagnostic show version option is available


* Keyword Usage:

> 
> * `Is Device Tool Show Version Available`


* **Returns**

    1 if is displayed else -1



#### is_device_tool_vlan_probe_available()

* This keyword checks if the tool vlan probe option is available


* Keyword Usage:

> 
> * `Is Device Tool Vlan Probe Available`


* **Returns**

    1 if is displayed else -1



#### is_reset_device_to_default_available()

* This keyword checks if the reset device to default option is available


* Keyword Usage:

> 
> * `Is Reset Device To Default Available`


* **Returns**

    1 if is displayed else -1



#### reject_device_tool_get_tech_data()

* This keyword is used to reject the request to continue to get tech data


* Keyword Usage:

> 
> * `Reject Device Tool Get Tech Data`


* **Returns**

    1 if is not displayed else -1



#### verify_confirm_message_dialog_is_open()

* This keyword is used to verify the confirm message window is open


* Keyword Usage:

> 
> * `Verify Confirm Message Dialog Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_cli_is_open()

* This keyword is used to verify the device CLI tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Cli Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_client_information_is_open()

* This keyword is used to verify the device client information tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Client Information Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_get_tech_data_is_open()

* This keyword is used to verify the device get tech data tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Get Tech Data Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_loading_is_open()

* This keyword is used to verify the device utilities loading window is open


* Keyword Usage:

> 
> * `Verify Device Tool Loading Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_locate_device_is_open()

* This keyword is used to verify the device locate device tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Locate Device Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_neighbor_info_is_open()

* This keyword is used to verify the device neighbor info tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Neighbor Info Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_packet_capture_is_open()

* This keyword is used to verify the device Packet Capture tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Packet Capture Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_ping_is_open()

* This keyword is used to verify the device ping tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Ping Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_amrp_tunnel_is_open()

* This keyword is used to verify the device show AMRP Tunnel tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Amrp Tunnel Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_arp_cache_is_open()

* This keyword is used to verify the device show ARP Cache tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Arp Cache Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_cpu_is_open()

* This keyword is used to verify the device show CPU tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Cpu Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_dnxp_cache_is_open()

* This keyword is used to verify the device show DNXP Cache tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Dnxp Cache Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_dnxp_neighbors_is_open()

* This keyword is used to verify the device show DNXP Neighbors tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Dnxp Neighbors Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_gre_tunnel_is_open()

* This keyword is used to verify the device show GRE Tunnel tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Gre Tunnel Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_ike_event_is_open()

* This keyword is used to verify the device show IKE Event tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Ike Event Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_ike_sa_is_open()

* This keyword is used to verify the device show IKE SA tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Ike Sa Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_ip_routes_is_open()

* This keyword is used to verify the device show IP Routes tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Ip Routes Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_ipsec_sa_is_open()

* This keyword is used to verify the device show IPsec SA tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Ipsec Sa Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_ipsec_tunnel_is_open()

* This keyword is used to verify the device show IPsec Tunnel tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Ipsec Tunnel Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_log_is_open()

* This keyword is used to verify the device show log tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Log Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_mac_routes_is_open()

* This keyword is used to verify the device show MAC Routes tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Mac Routes Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_mac_table_is_open()

* This keyword is used to verify the device show MAC Table tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Mac Table Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_memory_is_open()

* This keyword is used to verify the device show memory tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Memory Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_pse_is_open()

* This keyword is used to verify the device show PSE tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Pse Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_roaming_cache_is_open()

* This keyword is used to verify the device show Roaming Cache tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Roaming Cache Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_running_config_is_open()

* This keyword is used to verify the device show Running Config tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Running Config Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_startup_config_is_open()

* This keyword is used to verify the device show Startup Config tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Startup Config Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_version_is_open()

* This keyword is used to verify the device show version tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Version Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_show_vpn_tunnel_is_open()

* This keyword is used to verify the device show VPN Tunnel tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Show Vpn Tunnel Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_device_tool_vlan_probe_is_open()

* This keyword is used to verify the device VLAN Probe tool window is open


* Keyword Usage:

> 
> * `Verify Device Tool Vlan Probe Is Open`


* **Returns**

    1 if is displayed else -1



#### verify_select_stack_member_is_open()

* This keyword is used to verify the select stack member window is open


* Keyword Usage:

> 
> * `Verify Select Stack Member Is Open`


* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_cli_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device cli tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Cli Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_client_information_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device client information tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Client Information Is Open    retry_duration=5    retry_count=20`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_get_tech_data_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device get tech data tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Get Tech Data Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_locate_device_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device locate device tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Locate Device Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_neighbor_info_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device neighbor info tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Neighbor Info Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_packet_capture_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device packet capture tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Packet Capture Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_ping_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device ping tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Ping Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_show_roaming_cache_is_open()

* This keyword is used to wait until the device show roaming cache tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Show Roaming Cache Is Open`


* **Returns**

    1 if is displayed else -1



#### wait_until_device_tool_vlan_probe_is_open(retry_duration=5, retry_count=20)

* This keyword is used to wait until the device VLAN Probe tool window is open


* Keyword Usage:

> 
> * `Wait Until Device Tool Vlan Probe Is Open    retry_duration=10    retry_count=30`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if is displayed else -1


## extauto.xiq.flows.manage.Events module


### _class_ extauto.xiq.flows.manage.Events.Events()
Bases: `object`


#### check_events_download()

* This keyword checks if download works on Events Page.

-Flow: Manage –> Events –> Checks for Download.
- Keyword Usage:

> 
> * `Check Events Download`


* **Returns**

    1 if success else -1



#### verify_events_grid_details(mac=None, events_details=None, nav=0)

* This keyword checks if Events page grid contains the list of strings(events_details) provided as argument and it also checks for MAC.

-Flow: Manage –> Events –> Checks for events details and MAC.
- Keyword Usage:

> 
> * `Verify Events Grid Details    mac=${MAC}       events_details=Client Connect Down,Connection Change    nav=1`


> * `Verify Events Grid Details    events_details=Client Connect Down,Connection Change`


* **Parameters**

    
    * **mac** – MAC of the device


    * **events_details** – details to be checked, it needs to be provided in the above format(comma separated format).


    * **nav** – Navigates to Events Page if nav=1



* **Returns**

    1 if success else -1



#### verify_events_pagination(events_details, nav=0)

* This keyword verfies pagination by checking the events details on page 2 of Events Page.

-Flow: Manage –> Events –> Checks for pagination.
- Keyword Usage:

> 
> * `Verify Events Pagination    events_details=Client Connect Down,Connection Change    nav=1`


> * `Verify Events Pagination    events_details=Client Connect Down,Connection Change`


* **Parameters**

    
    * **events_details** – details to be checked, it needs to be provided in the above format(comma separated format).


    * **nav** – Navigates to Events Page if nav=1



* **Returns**

    1 if success else -1


## extauto.xiq.flows.manage.FilterManageDevices module


### _class_ extauto.xiq.flows.manage.FilterManageDevices.FilterManageDevices()
Bases: `object`


#### action_change_managed_state(ap, state='managed')
change a managed state of ap
:param: ap: ap’s serial number
:param: state is either managed or unmanaged
:return True


#### check_available_devices(filter='default', real_device=False, ap_type=False)

#### clear_all_filters(navigator='device filter')
Clearing all applied and saved filters
:param navigator: navigator to a filtered page


#### close_filter_panel()
Closes the filter panel if it is open


#### expand_and_collapse_filters(element, filter_type='policy', collapse=False)
expand and collapse the filter links
:param element : link of filter
:param filter_type: page contains the filters
:param collapse: collapse the filter toggle when it is true


#### expand_default_filters()

#### filter_all_devices_by_software_version()
verification of the devices by software version
prequist: Require at least two or more onboard different hardware devices
usage of test case:

> Test1: Filter By Device Software Version

>     filter device by software version


#### filter_by_device_type(filter='default')
Verification of the filtering of the devices by the device type
prequist: Require at least one real device and one simulated device
Usage of test case:
Test1: Filter Device By Device Type

> filter by device type  real device
> filter by device type  simulated device


#### filter_client_by_device_function(filter)
Verification of the filtering of the clients based on the device function
prequist: AP and switch need to be onboarded and need one client to switch and one client connect to AP

> Usage of test case:

>     Test1: Filter Client By Device Function

>         client.filter client by device function  client ap
>         client.filter client by device function  client switch

Jira: APC - 3741


#### filter_client_by_os_type(filter)
Verification of the clients based on the os type
prequist: One or two clients should be connected via Wifi either Windows, Mac OS
Usage of test case:

> Test1: Filter Client By OS Type

>     filter client by os type


#### filter_client_by_ssid(filter)
Verification of the Clients based on the SSID
prequist: 1 Ap should be onboarded with wireless network
Usage of test case:

> Test1: Filter Client By Client SSID

>     filter client by ssid


#### filter_client_by_user_profiles(ssid_name, filter='default')
Verification of the filtering of the Clients based on the SSID
prequist: 1 Ap should be onboarded with wireless network
Usage of test case:

> Test1: Filter Client By User Profiles

>     filter client by user profiles  ${ssid_name}   client guess profile
>     filter client by user profiles  ${ssid_name}   client default profile


#### filter_device_both_unmanaged_and_managed_state()
Verification of the devices by the device mangement state
prequist: Require at least one or more onboard devices
Usage of test case:

> Test1: Filter By Device Management State

>     filter device by management state


#### filter_device_by_connection_state(ap_sn)
Verification of the devices by connection state
prequist: Require one device in connected state and one device in disconnected state


#### filter_device_by_function(filter)
Verification of the filtering of the devices by function
prequist: Require at least one AP and one Fasthpath / Hive OS switch
Ussage of test case:
Test1: Filter By Device Function

> filter device by function  ap model
> filter device by function  sw model


#### filter_device_by_network_policy()
Verification of the filtering of the devices by the network policy
prequist: Require at least two onboard APs with each policy
Usage of test case:
Test1:  Filter Device By Policy

> filter device by policy


#### filter_device_by_production_type()
Verification of the filtering of the device models
prequist: Require at least two or more APs with the different hardware models
Usage of test case:

Test1: Filter By Device Production Type

    filter device production type


#### filter_device_by_ssid()
Verification of the filtering of the devices by ssid
prequist: Require at least two onboard devices with with two different wireless networks
usage of test case:

> Test1: Filter Device By ssid

>     filter device by ssid

> Jira: APC-39526 - The SSID list in the SSID filter does not update accordingly


#### filter_device_by_user_profiles(filter='default')
Verification of the filtering of the devices by user profiles
prequist: Require at least one onboard devices with a network policy
usage of test case:

> Test1: Filter By Device user profile

>     filter device by user profiles  guest
>     filter device by user profiles  profile


#### filter_device_with_audit_match_and_mismatch()
Verification of the filtering of the devices by audit status
prequist: Require at least two or more onboard devices with a different policy
usage of test case :

> Test1: Filter By Device audit status

>     filter device by audit status


#### filter_hardware_model(model)

#### filter_policy(policy)

#### get_column_values_from_device_page(filter='default')
verify if the polices are assigned to all devices
:param  grid : a list of column values on the device page
:return list of column values


#### get_devices_with_network_policy(sns, policies)

#### get_elements_text(elements)

* **Param**

    list of elements


:return list of texts


#### open_filter_panel()
Opens the filter panel if it isn’t already open


#### parse_string(models)

#### save_filter()
create a filter and save the filter
:param: None
:return filter_name (name of filter)


#### select_filter_by(\*locators, filter_name='default', reset=False)
expand and collapse the filter links
:param locators : list of checkboxs
:param reset : clear the checkbox when it is true


#### set_cloud_config_groups_filter(filter='All', select='true')
Sets the cloud config groups filter to the specified value

    Usage of test case:

        Set Cloud Config Groups Filter  All  true
        Set Cloud Config Groups Filter  Model_AP_410C  true
        Set Cloud Config Groups Filter  All  false
        Set Cloud Config Groups Filter  Model_AP_410C  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### set_device_connection_state_filter(filter='All', select='true')
Sets the device connection state filter to the specified value

    Usage of test case:

        Set Device Connection State Filter  All  true
        Set Device Connection State Filter  Connected  true
        Set Device Connection State Filter  Disconnected  true
        Set Device Connection State Filter  Pre-Provisioned  true
        Set Device Connection State Filter  All  false
        Set Device Connection State Filter  Connected  false
        Set Device Connection State Filter  Disconnected  false
        Set Device Connection State Filter  Pre-Provisioned  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### set_device_function_filter(filter='All', select='true')
Sets the device function filter to the specified value

    Usage of test case:

        Set Device Function Filter  All  true
        Set Device Function Filter  Switch  true
        Set Device Function Filter  XIQSE  true
        Set Device Function Filter  All  false
        Set Device Function Filter  Switch  false
        Set Device Function Filter  XIQSE  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### set_device_management_state_filter(filter='All', select='true')
Sets the device management state filter to the specified value

    Usage of test case:

        Set Device Management State Filter  All  true
        Set Device Management State Filter  Managed  true
        Set Device Management State Filter  New  true
        Set Device Management State Filter  Setting Up  true
        Set Device Management State Filter  Unmanaged  true
        Set Device Management State Filter  All  false
        Set Device Management State Filter  Managed  false
        Set Device Management State Filter  New  false
        Set Device Management State Filter  Setting Up  false
        Set Device Management State Filter  Unmanaged  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### set_device_product_type_filter(filter='All', select='true')
Sets the device product type filter to the specified value

    Usage of test case:

        Set Device Product Type Filter  All  true
        Set Device Product Type Filter  X460_G2_48t_10_G4  true
        Set Device Product Type Filter  XIQ_SE  true
        Set Device Product Type Filter  All  false
        Set Device Product Type Filter  X460_G2_48t_10_G4  false
        Set Device Product Type Filter  XIQ_SE  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### set_device_software_version_filter(filter='All', select='true', exact_match='true')
Sets the device software version filter to the specified value

    Usage of test case:

        Set Device Software Version Filter  All  true
        Set Device Software Version Filter  21.4.10.6  true
        Set Device Software Version Filter  All  false
        Set Device Software Version Filter  30.7.11-patch1-23  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### set_device_type_filter(filter='All', select='true')
Sets the device type filter to the specified value

    Usage of test case:

        Set Device Type Filter  All  true
        Set Device Type Filter  Plan Devices  true
        Set Device Type Filter  Real Devices  true
        Set Device Type Filter  Simulated Devices  true
        Set Device Type Filter  All  false
        Set Device Type Filter  Plan Devices  false
        Set Device Type Filter  Real Devices  false
        Set Device Type Filter  Simulated Devices  false


* **Parameters**

    
    * **filter** – name of the filter to set


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### toggle_filter_check_box(element, select='true')
Toggles the filter check box to have the specified selection state


* **Parameters**

    
    * **element** – check box to toggle


    * **select** – indicates whether the filter check box should be selected (true) or deselected (false)



* **Returns**

    1 if filter was set, else -1



#### user_profile_filter_error(user_profile=None)

* Checks for error after selecting user profile which is not assigned to any device, ie, it should not throw error “can not get the required device list”


* **Parameters**

    **user_profile** – name of the user profile



* **Returns**

    1 if successful


## extauto.xiq.flows.manage.Location module


### _class_ extauto.xiq.flows.manage.Location.Location()
Bases: `object`


#### assign_location_using_hostname(device_host, dev_location=None)

* This keyword assigns location to device by clicking on Assign Location hyperlink in Devices page.

-Flow: Manage –> Devices –> based on hostname clicks on the Assign Location hyperlink present in Devices grid.
- Keyword Usage:

> 
> * `Assign Location With Hostname    ${SW_HOST}              San Jose, building_01, floor_02`


* **Parameters**

    
    * **device_serial** – switch host


    * **dev_location** – location where the device is to be assigned in the above format



* **Returns**

    1 if success else -1



#### assign_location_with_device_actions(device_serial=None, dev_location=None)

* This keyword assigns location to device by clicking on Actions button in Devices page.

-Flow: Manage –> Devices –> selects the device based on serial number –> Actions –> Assign Location
- Keyword Usage:

> 
> * `Assign Location With Device Actions    ${AP1_SERIAL}              San Jose, building_01, floor_02`


* **Parameters**

    
    * **device_serial** – device serial number


    * **dev_location** – location where the device is to be assigned in the above format



* **Returns**

    1 if success else -1



#### assign_location_with_device_actions_using_hostname(device_name='default', dev_location=None)

* This keyword assigns location to device by clicking on Actions button in Devices page.

-Flow: Manage –> Devices –> selects the device based on host name –> Actions –> Assign Location
- Keyword Usage:

> 
> * `Assign Location With Device Actions    ${SW_HOST}              San Jose, building_01, floor_02`


* **Parameters**

    
    * **device_serial** – device host name


    * **dev_location** – location where the device is to be assigned in the above format



* **Returns**

    1 if success else -1



#### assign_location_with_hyperlink(device_serial=None, dev_location=None)

* This keyword assigns location to device by clicking on Assign Location hyperlink in Devices page.

-Flow: Manage –> Devices –> based on device serial clicks on the Assign Location hyperlink present in Devices grid.
- Keyword Usage:

> 
> * `Assign Location With Hyperlink    ${AP1_SERIAL}              San Jose, building_01, floor_02`


* **Parameters**

    
    * **device_serial** – device serial number


    * **dev_location** – location where the device is to be assigned in the above format



* **Returns**

    1 if success else -1



#### create_first_organization(organization, street, city, country, width='50', height='50')
This keyword create new organization if this isn’t created
- Keyword Usage:

> create_first_organization                     Luxoft       Doftanei        Bucuresti     Romania


* **Parameters**

    
    * **organization** – name of organization


    * **street** – name of street


    * **city** – name of city


    * **country** – select the country



* **Returns**

    return 1 if the organization was created successfully, else -1



#### create_location_building_floor(location, building, floor, width='50', height='50')
-This function is to create location, building and floor in MLInsights >> N360plan
:param location:
:param building:
:param floor:
:return:


#### delete_location_building_floor(location, building, floor)
-This function is to delete location, building and floor in MLInsights >> N360plan
:param location:
:param building:
:param floor:
:return:


#### get_assigned_floor(device_serial)

* Pre-condition - this keyword assumes that location already assigned to device


* Clicks on device location link


* Returns the floor, which is highlighted from the location popup


* **Parameters**

    **device_serial** – Device Serial



* **Returns**

    floor highlighted if success else -1



#### get_device_location(device_serial='default')

* This keyword returns the location of a device


* location string format: auto_location_01 >> San Jose >> building_01 >> floor_01


* **Parameters**

    **device_serial** – client name



* **Returns**

    returns location string if success else -1



#### get_device_location_using_hostname(device_host='default')

* This keyword returns the location of a device


* location string format: auto_location_01 >> San Jose >> building_01 >> floor_01


* **Parameters**

    **device_serial** – client name



* **Returns**

    returns location string if success else -1



#### input_new_snmp_location(new_locn)

* This keyword is used to input new value to SNMP location in D360 >> device config


* location string format: auto_location_01 >> San Jose >> building_01 >> floor_01

:param loction name
:return: returns 1 if success else -1


#### select_location(sel_loc)

* This keyword selects a location in the location dialog and clicks the “Assign” button.
It is assumed the location dialog is already open.


* Keyword Usage:

> 
> * `Select Location  ${LOCATION}`


* **Parameters**

    **sel_loc** – location to select, in a comma-separated list format; e.g., San Jose, building_01, floor_02



* **Returns**

    1 if location is selected, else -1’


## extauto.xiq.flows.manage.Reports module


### _class_ extauto.xiq.flows.manage.Reports.Reports()
Bases: `ReportsWebElements`


#### get_default_network_summary_report(\*email_list)

* Flow: Manage –> Reports


* Default summary report will generate the reports with default options


* Keyword Usage:

> 
> * `Get Default Network Summary Report  @{EMAIL_LIST}`


* **Parameters**

    **email_list** – list of the emails to send the reports



* **Returns**

    1


## extauto.xiq.flows.manage.Switch module


### _class_ extauto.xiq.flows.manage.Switch.Switch()
Bases: `SwitchWebElements`


#### capture_xiq_switch_connection_host()

* This keyword Get Switch Connection Host


* Flow  Manage–> Devices


* Keyword Usage

> 
> * `Capture XIQ Switch Connection Host`


* **Parameters**

    
    * **sw_serial** – Switch Serial Number


    * **sw_name** – Switch Name


    * **sw_mac** – Switch MAC Address



* **Returns**

    row if the AP is present on devices grid else -1



#### delete_switch(sw_serial)

* This keyword Deletes Switch using serial number


* Flow  Manage–> Devices–> Select Switch Row using serial number–>Click Delete Button


* Keyword Usage

> 
> * `Delete Switch ${SWITCH_SERIAL}`


* **Parameters**

    **sw_serial** – Switch Serial Number



* **Returns**

    1 if the AP is online else return -1



#### get_switch_port_details(sw_serial, port_number)

* This keyword return Switch Port Details ie Status based on serial Number and Port Number of the Switch


* Flow  Manage–> Devices–> SWitch hyper Link –> Click Port Number


* Keyword Usage

> 
> * `Get Switch Port Details    ${SWITCH_SERIAL}  ${PORT_NUMBER}`


* **Parameters**

    
    * **sw_serial** – serial number of Switch


    * **port_number** – Port Number of the Switch



* **Returns**

    Port Details ie Port Status



#### get_switch_port_status(sw_serial, port_number)

* This keyword return Switch Port Status(Enabled/Disabled) based on serial Number and Port Number of the Switch


* Flow  Manage–> Devices–> SWitch hyper Link –> Click Port Number


* Keyword Usage

> 
> * `Get Switch Port Status   ${SWITCH_SERIAL}  ${PORT_NUMBER}`


* **Parameters**

    
    * **sw_serial** – serial number of Switch


    * **port_number** – Port Number of the Switch



* **Returns**

    Port Status ie Enabled/Disabled



#### get_switch_row(sw_serial='default', sw_name='default', sw_mac='default')

* This keyword Get presence of Switch row in devices grid using serial number,Switch Name and Mac address


* Flow  Manage–> Devices


* Keyword Usage

> 
> * `Get Switch Row sw_serial=${SWITCH_SERIAL}`


> * `Get Switch Row sw_name=${SWITCH_NAME}`


> * `Get Switch Row sw_mac=${SWITCH_MAC}`


* **Parameters**

    
    * **sw_serial** – Switch Serial Number


    * **sw_name** – Switch Name


    * **sw_mac** – Switch MAC Address



* **Returns**

    row if the AP is present on devices grid else -1



#### get_switch_status(serial='default', name='default', mac='default')

* This keyword Get the status of the Switch using serial number,Switch Name and Mac address


* Flow  Manage–> Devices


* Keyword Usage

> 
> * `Get Switch Status serial=${SWITCH_SERIAL}`


> * `Get Switch Status name=${SWITCH_NAME}`


> * `Get Switch Status mac=${SWITCH_MAC}`


* **Parameters**

    
    * **serial** – Switch Serial Number


    * **name** – Switch Name


    * **mac** – Switch MAC Address



* **Returns**

    Green if the AP is online



#### onboard_aerohive_switch(switch_serial, switch_type)

* This keyword onboards an Aerohive Switch using Quick onboarding flow.


* Flow  Manage–> Devices–> Add –> Quick Add Devices–> Select Aerohive Device Make –> Enter Serial Number

    –> Add Devices


* Keyword Usage

> 
> * `Onboard Aerohive Switch    ${SWITCH_SERIAL}  ${SWITCH_MAKE_TYPE}`


* **Parameters**

    
    * **switch_serial** – serial number of Switch


    * **switch_type** – Model of the Switch



* **Returns**

    1 if Aerohive Switch OnBoarding is Successful without Error Message



#### onboard_switch(switch_serial, switch_make='default', device_os='default', location=None, switch_type='Real', entry_type='Manual')

* This keyword onboards an Switch Device based on Switch Type(ie Exos) using Quick onboard flow.


* Flow  Manage–> Devices–> Add –> Quick Add Devices–> Select Device Make –> Serial Number–> Add Devices


* Keyword Usage

> 
> * `Onboard Switch    ${SWITCH_SERIAL}  ${SWITCH_MAKE_TYPE}`


* **Parameters**

    
    * **switch_serial** – serial number of Switch


    * **switch_make** – Switch Make


    * **device_os** – Switch OS


    * **location** – switch location


    * **switch_type** – Device Type ie Real or Simulated


    * **entry_type** – Device Entry Type ie Manual or CSV



* **Returns**

    1 if Switch OnBoarding is Successful without Error Message



#### search_switch(sw_serial=None, sw_name=None, sw_mac=None)

* This keyword returns Searches Switch using serial number,name or mac address


* Flow  Manage–> Devices–> Search Switch Row using Serial Number,Name or mac address


* Keyword Usage

> 
> * `Search Switch sw_serial=${SWITCH_SERIAL}`


> * `Search Switch sw_name=${SWITCH_NAME}`


> * `Search Switch sw_mac=${SWITCH_MAC}`


* **Parameters**

    
    * **sw_serial** – Switch Serial Number


    * **sw_name** – Switch Name


    * **sw_mac** – Switch MAC Address



* **Returns**

    ‘green’ if the AP is online else return -1



#### search_switch_mac(sw_mac)

* Searches for Switch matching Switch’s Mac Address


* Flow  Manage–> Devices–> Search Switch Row based on Mac Address


* Keyword Usage

> 
> * `Search Switch Mac   ${SWITCH_SERIAL}`


* **Parameters**

    **sw_mac** – Switch’s Mac Address



* **Returns**

    return 1 if Switch found on Devices Grid Row else -1



#### search_switch_name(sw_name)

* Searches for Switch matching Switch’s Name


* Flow  Manage–> Devices–> Search Switch Row based on Switch Name


* Keyword Usage

> 
> * `Search Switch Name   ${SWITCH_NAME}`


* **Parameters**

    **sw_name** – Switch’s Name



* **Returns**

    return 1 if Switch found on Devices Grid Row else -1



#### search_switch_serial(sw_serial)

* Searches for Switch matching Switch’s Serial Number


* Flow  Manage–> Devices–> Search Switch Row based on Serial Number


* Keyword Usage

> 
> * `Search Switch Serial   ${SWITCH_SERIAL}`


* **Parameters**

    **sw_serial** – Switch’s Serial Number



* **Returns**

    return 1 if Switch found on Devices Grid Row else -1



#### select_switch(sw_serial)

* This keyword Select Aerohive Switch based on Switch Serial Number From Devices Grid


* Flow  Manage–> Devices–> Select Aerohive SWitch


* Keyword Usage

> 
> * `Select Switch    ${SWITCH_SERIAL}`


* **Parameters**

    **sw_serial** – serial number of Switch



* **Returns**

    1 if Aerohive Switch selected Successfully else -1


## extauto.xiq.flows.manage.Tools module


### _class_ extauto.xiq.flows.manage.Tools.Tools()
Bases: `object`


#### click_til_element_avail(element, seconds=30)
Click on a webelement until element is ready

    Enable an ap device  connected or disconnected
    :param element      : Web Element
    :param seconds      : a duration of waited time
    :return:  None

usage:

    self.click_til_element_avail(self.tool_utils.get_tech_data_btn())


#### device_diagnostics_ping(serial, \*\*kwargs)

* Keywword requires that the device is already onboarded


* Used to get device diagnostics ping


* Keyword Usage:
- `Device Diagnostics Ping   ${SERIAL}`


* **Parameters**

    **SERIAL** – serial number of device



* **Returns**

    1 if successful else -1



#### enable_disable_device(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)
> Enable / disable a capwap device
> :param ap_sn      : ap serial number
> :param ap_name    : ap name
> :param seconds    : number of seconds for waiting
> :param exp_status : expected status either connected or disconnected
> :return:  true / false

usage:

    self.wait_til_ap_change_status(ap_sn, ap_name, 180, “green”)


#### get_l2_neighbor_info(serial, mac, \*\*kwargs)

* Keywword requires that the device is already onboarded


* Used to get l2 neighbor information


* Keyword Usage:

    
        * `Get l2 Neighbor Info   ${SERIAL}  ${MAC}`


* **Parameters**

    
    * **SERIAL** – serial number of device


    * **MAC** – mac address of device



* **Returns**

    1 if successful else -1



#### get_neighbor_info(serial, mac, \*\*kwargs)

* Keywword requires that the device is already onboarded


* Used to get neighbor information


* Keyword Usage:

    
        * `Get Neighbor Info   ${SERIAL}  ${MAC}`


* **Parameters**

    
    * **SERIAL** – serial number of device


    * **MAC** – mac address of device



* **Returns**

    1 if successful else -1



#### get_value_in_tbl(grids, field)
> Get value from table list
> :param grids    : list of rows in table
> :param field    : a column / cell
> :return         : true / false

usage:

    get_value_in_tbl(grid1, column)


#### installer_role_diagnostics_ping()

* This keyword is for testing Ping utility from Installer Role


* Flow: Installer Role -> Select a device ->  Utilities -> Diagnostics -> Ping

> 
> * Keyword Usage:

> > 
> > * ‘Installer Role Diagnostics Ping’


* **Returns**

    1 if operation is successful



#### lock_device(host, username, passwd, ssid, ssid_passwd='FFLJLSP09865')
> > Lock Device with 10 invalid logins


> * **param host**

>     mac station ip



> * **param username**

>     mac user login



> * **param passwd**

>     mac user password



> * **param ssid**

>     global ssid in the network policy



> * **param ssid_pass**

>     password of ssid



> * **return**

>     return a hostname of mac station


Usage:

    ${host}    lock device  ${MAC_STA_IP}  ${MAC_STA_USERID}  ${MAC_STA_PASS}  ${SSID}


#### make_wifi_connection(host, username, passwd, ssid, ssid_passwd)
Prequis: AP should be onboared and mac station is availabe to connect to a WIFI

    > Make a wifi connection


    * **param host**

        mac station ip



    * **param username**

        mac user login



    * **param passwd**

        mac user password



    * **param ssid**

        global ssid a network policy



    * **param ssid_pass**

        password of ssid



    * **param wifi_port**

        mac wifi port



    * **param mode**

        pass : make a succesful wifi connection
        fail : make a failed wifi connection


    :param ntimes     : number of times to authenticate in order to be in locked state
    :return: return a hostname of mac station

usage:

    make wifi connection  ${MAC_STA_IP}  ${MAC_STA_USERID}  ${MAC_STA_PASS}  ${SSID}  ${SSID_PASSWD}


#### run_ssh_availability_on_ap(serial_num, time_lim, \*\*kwargs)

* Used to run ssh availability on ap


* Keyword Usage:

    
        * `Run Ssh Availability On Ap   ${SERIAL}  ${TIME_LIM}`


* **Parameters**

    
    * **SERIAL** – serial number of device


    * **TIME_LIM** – time lim



* **Returns**

    1 if successful else -1



#### ui_ssh_status_check(\*\*kwargs)

* Used to ui ssh status check


* Keyword Usage:

    
        * `Ui Ssh Status Check`


* **Returns**

    status if successful else -1



#### ui_tools_ssh_status_check(\*\*kwargs)

* Used to ui tools ssh status check


* Keyword Usage:
- `Ui Tools Ssh Status Check`


* **Returns**

    status if successful else -1



#### utility_device_client_info(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_mac, ap_name)
Prequis: AP should be onboared

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


#### utility_device_diagnostic(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)
Prequis: AP should be onboared

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


#### utility_device_info(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)
Prequis: AP should be onboared

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


#### utility_get_tech_data(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)
Prequis: AP should be onboared

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


#### utility_vlan_probe(mode, ap_ip, ap_usr, ap_pass, ap_sn, ap_name)
Prequis: AP should be onboared

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


#### verify_device_lock(host)
Prequis: AP should be onboared and mac station is availabe to connect to a WIFI

    > Verification device is locked


    * **param host**

        mac station ip



    * **return**

        return a hostname of mac station


Usage:

    ${host}    verify_device_lock  host


#### verify_util_client_cnx(ssid, ap_name, client_mac, client_name='default', conn_type='WIRELESS')
Prequis: AP should be onboared and mac station for a WIFI

    Verification of the visibility of client information
    :param ssid     : ssid from a policy
    :param ap_name  : ap name
    :param client_mac  : mac addr of mac station
    :param client_name : name of mac station
    :param conn_type   : a conntection type - WIRELESS / WIRED
    :return: None

usage:

    verify util client cnx    ${SSID}  ${AP1_NAME}  ${MAC_MAC_ADDR}


#### wait_til_ap_change_status(ap_sn, ap_name, seconds, exp_status)
Wait until a device is connected or disconnected

    :param ap_sn      : ap serial number
    :param ap_name    : ap name
    :param seconds    : number of seconds for waiting
    :param exp_status : expected either connected or disconnected
    :return:  true / false

usage:

    self.wait_til_ap_change_status(ap_sn, ap_name, 180, “green”)


#### wait_til_elements_avail(locator, seconds=60, elements=True)
wait until elements or element is present. If it is a table, there is a least one row

    :param locator    : element’s locator
    :param seconds    : number of seconds to wait
    :param true if element is a grid, false if element is not a grid
    :return:  true / false

usage:

    self.wait_til_elements_avail(self.tool_utils.client_info_list, False)

## Module contents
