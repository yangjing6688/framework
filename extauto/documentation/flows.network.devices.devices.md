# extauto.xiqse.flows.network.devices.devices package

## Submodules

## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevices module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevices.XIQSE_NetworkDevicesDevices()
Bases: `NetworkDevicesDevicesWebElements`


#### xiqse_add_device(ip_addr, profile='public_v1_Profile', nickname='', status_only='False', add_actions='True')
> 
> * This keyword adds a device using the Add Device toolbar button on the Network> Devices> Devices tab.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Add Device  ${IP}  ${PROFILE}  ${NICKNAME}  True`


> > * `XIQSE Add Device  ${IP}  ${PROFILE}  ${NICKNAME}`


> > * `XIQSE Add Device  ${IP}  ${PROFILE}`


> > * `XIQSE Add Device  ${IP}  ${PROFILE}  status_only=True`


> > * `XIQSE Add Device  ${IP}`


> > * `XIQSE Add Device  ${IP}  nickname=TestDevice`


> > * `XIQSE Add Device  ${IP}  status_only=True`


> > * `XIQSE Add Device  ${IP}  add_actions=False`


* **Parameters**

    
    * **ip_addr** – IP address of the device to add - required


    * **profile** – profile to use for the device


    * **nickname** – nickname to use for the device


    * **status_only** – indicates if the device should be created with Poll Status Only selected (True/False)


    * **add_actions** – indicates if the Run Site’s Add Actions option should be enabled (True/False)



* **Returns**

    1 if action was successful, else -1



#### xiqse_close_add_device_dialog()
> 
> * This keyword closes the Add Device dialog if it is open.


> * Keyword Usage

> > 
> > * `XIQSE Close Add Device Dialog`


* **Returns**

    1 if action was successful, else -1



#### xiqse_configure_device_annotations(device_ip, nickname=None, asset_tag=None, ud1=None, ud2=None, ud3=None, ud4=None, note=None)
> 
> * This keyword configures the device with the specified Device Annotation values.  It does not save the changes.


> * Keyword Usage:

> > 
> > * 

> > ```
> > ``
> > ```

> > XIQSE Configure Device Annotations   1.2.3.4  nickname=MY_NICKNAME  ud2=MY DATA 2  note=MY NOTE

2nd LINE\`\`

> 
> * **param device_ip**

>     IP address of the device to configure



> * **param nickname**

>     Value to enter into the Nickname field



> * **param asset_tag**

>     Value to enter into the Asset Tag field



> * **param ud1**

>     Value to enter into the User Data 1 field



> * **param ud2**

>     Value to enter into the User Data 2 field



> * **param ud3**

>     Value to enter into the User Data 3 field



> * **param ud4**

>     Value to enter into the User Data 4 field



> * **param note**

>     Value to enter into the Note field



> * **return**

>     1 if action is successful, else -1



#### xiqse_configure_device_annotations_and_save(device_ip, nickname=None, asset_tag=None, ud1=None, ud2=None, ud3=None, ud4=None, note=None)
> 
> * This keyword configures the device with the specified Device Annotation values and saves the changes.


> * The Configure Device dialog is opened, the Device Annotation tab is selected and populated with the specified


> * values, and the Save button is clicked.


> * Keyword Usage:

> > 
> > * 

> > ```
> > ``
> > ```

> > XIQSE Configure Device Annotations and Save   1.2.3.4  nickname=MY_NICKNAME  ud2=MY DATA 2  note=MY NOTE

2nd LINE\`\`

> 
> * **param device_ip**

>     IP address of the device to configure



> * **param nickname**

>     Value to enter into the Nickname field



> * **param asset_tag**

>     Value to enter into the Asset Tag field



> * **param ud1**

>     Value to enter into the User Data 1 field



> * **param ud2**

>     Value to enter into the User Data 2 field



> * **param ud3**

>     Value to enter into the User Data 3 field



> * **param ud4**

>     Value to enter into the User Data 4 field



> * **param note**

>     Value to enter into the Note field



> * **return**

>     1 if action is successful, else -1



#### xiqse_configure_device_device_tab(device_ip, system_name=None, contact=None, location=None, profile=None, serial=None, remove_from_service=None, use_default_url=None, webview_url=None, site=None, poll_group=None, poll_type=None, timeout=None, retries=None, topo=None, mode=None, interval=None)

* This keyword configures the device with the specified Device tab values.  It does not save the changes.


* Keyword Usage:

> 
> * `XIQSE Configure Device Device Tab   1.2.3.4  system_name=MY_SYSTEMNAME  profile=EXTR_v2_Profile  timeout=10`


* **Parameters**

    
    * **device_ip** – IP address of the device to configure


    * **system_name** – Value to enter into the System Name field


    * **contact** – Value to enter into the Contact field


    * **location** – Value to enter into the Location field


    * **profile** – Value to enter into the Administration Profile field


    * **serial** – Value to enter into the Replacement Serial Number field


    * **remove_from_service** – Specifies whether to enable/disable the Remove From Service checkbox (true/false)


    * **use_default_url** – Specifies whether to enable/disable the Use Default WebView URL checkbox (true/false)


    * **webview_url** – Value to enter into the WebView URL field


    * **site** – Value to enter into the Default Site field


    * **poll_group** – Value to enter into the Poll Group field


    * **poll_type** – Value to enter into the Poll Type field


    * **timeout** – Value to enter into the SNMP Timeout field


    * **retries** – Value to enter into the SNMP Retries field


    * **topo** – Value to enter into the Topology Layer field


    * **mode** – Value to enter into the Collection Mode field


    * **interval** – Value to enter into the Collection Interval field



* **Returns**

    1 if action is successful, else -1



#### xiqse_configure_device_device_tab_and_save(device_ip, system_name=None, contact=None, location=None, profile=None, serial=None, remove_from_service=None, use_default_url=None, webview_url=None, site=None, poll_group=None, poll_type=None, timeout=None, retries=None, topo=None, mode=None, interval=None)

* This keyword configures the device with the specified Device tab values and saves the changes.


* The Configure Device dialog is opened, the Device tab is selected and populated with the specified


* values, and the Save button is clicked.


* Keyword Usage:

> 
> * `XIQSE Configure Device Device Tab and Save   1.2.3.4  system_name=MY_SYSTEMNAME  profile=EXTR_v2_Profile  timeout=10`


* **Parameters**

    
    * **device_ip** – IP address of the device to configure


    * **system_name** – Value to enter into the System Name field


    * **contact** – Value to enter into the Contact field


    * **location** – Value to enter into the Location field


    * **profile** – Value to enter into the Administration Profile field


    * **serial** – Value to enter into the Replacement Serial Number field


    * **remove_from_service** – Specifies whether to enable/disable the Remove From Service checkbox (true/false)


    * **use_default_url** – Specifies whether to enable/disable the Use Default WebView URL checkbox (true/false)


    * **webview_url** – Value to enter into the WebView URL field


    * **site** – Value to enter into the Default Site field


    * **poll_group** – Value to enter into the Poll Group field


    * **poll_type** – Value to enter into the Poll Type field


    * **timeout** – Value to enter into the SNMP Timeout field


    * **retries** – Value to enter into the SNMP Retries field


    * **topo** – Value to enter into the Topology Layer field


    * **mode** – Value to enter into the Collection Mode field


    * **interval** – Value to enter into the Collection Interval field



* **Returns**

    1 if action is successful, else -1



#### xiqse_confirm_device_profile(device_ip, profile_name, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device profile to be at the expected value in the Devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device profile matches the value.


* It is assumed the Network> Devices> Devices tab is already selected and the Admin Profile column is displayed.


* Keyword Usage:

> 
> * `XIQSE Confirm Device Profile    ${DEVICE_IP}  ${PROFILE_NAME}  retry_duration=10  retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to look for


    * **profile_name** – expected value of the profile


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### xiqse_confirm_table_empty()

* This keyword confirms there are no devices in the Devices table.

> 
> * Keyword Usage

> > 
> > * `XIQSE Confirm Table Empty`


* **Returns**

    returns 1 if table is empty, else -1



#### xiqse_delete_all_devices()

* This keyword deletes all items in the Devices table.


* Note this needs to be done in batches as not all rows are visible at once.


* **Returns**

    returns 1 if action was successful, else -1



#### xiqse_delete_device(device_ip)
> 
> * This keyword deletes the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Delete Device    ${DEVICE_IP}`


> > * `XIQSE Delete Device    ${DEVICE_IP}    false`


* **Parameters**

    **device_ip** – IP address of the device to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_selected_devices()
> 
> * This keyword deletes the currently-selected devices.


> * It is assumed the user is already on the Network> Devices> Devices tab and the devices to delete are selected.


> * Keyword Usage

> > 
> > * `XIQSE Delete Selected Devices`


* **Returns**

    1 if action was successful, else -1



#### xiqse_device_restore_configuration(device_ip, the_value)
> 
> * This keyword selects Restore Configuration and the configuration to restore for the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Device Select Restore Configuration  1.2.3.4  the_value`


* **Parameters**

    
    * **device_ip** – IP address of the device to select restore config on


    * **the_value** – Selects the configuration file



* **Returns**

    1 if action was successful, else -1



#### xiqse_device_select_backup_configuration(device_ip)
> 
> * This keyword selects Backup Configuration for the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Device Select Backup Configuration  1.2.3.4`


* **Parameters**

    **device_ip** – IP address of the device to select backup config on



* **Returns**

    1 if action was successful, else -1



#### xiqse_device_select_restore_configuration(device_ip)
> 
> * This keyword selects Restore Configuration for the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Device Select Restore Configuration  1.2.3.4`


* **Parameters**

    **device_ip** – IP address of the device to select restore config on



* **Returns**

    1 if action was successful, else -1



#### xiqse_device_set_profile(device_ip, profile_name)
> 
> * This keyword sets the profile for the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Device Set Profile  1.2.3.4  new_profile`


* **Parameters**

    
    * **device_ip** – IP address of the device to set the profile on


    * **profile_name** – name of the profile to set on the device



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_clear_search()
> 
> * This keyword clicks the clear button in the search box in the Network> Devices view


> * Keyword Usage

> > 
> > * `XIQSE Events Clear Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_enter_search_text(value)
> 
> * This keyword enters text into the search field in the Network> Devices view


> * Keyword Usage

> > 
> > * `XIQSE Devices Enter Search Text    My Device To Find`


* **Parameters**

    **value** – string to enter in the search box



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_hide_columns(\*columns)

* This keyword hides the specified list of columns if they are currently shown.


* Assumes already navigated to the Network> Devices> Devices view.


* Keyword Usage:

> 
> * `XIQSE Devices Hide Columns        Admin Profile  Context`


* **Parameters**

    **columns** – list of columns to hide



* **Returns**

    returns 1 if successful. else -1



#### xiqse_devices_open_search()
> 
> * This keyword opens the search box in the Network> Devices view


> * Keyword Usage

> > 
> > * `XIQSE Devices Open Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_perform_search(value, retry_duration=10, retry_count=30)
> 
> * This keyword performs a search in the Network> Devices view


> * Keyword Usage

> > 
> > * `XIQSE Devices Perform Search   My Search String`


> > * `XIQSE Devices Perform Search   My Search String  retry_duration=5  retry_count=10`


* **Parameters**

    
    * **value** – string to search for


    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_refresh_table()
> 
> * This keyword clicks the refresh icon under the table.


> * Keyword Usage

> > 
> > * `XIQSE Devices Refresh Table`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_show_columns(\*columns)

* This keyword shows the specified list of columns if they are currently hidden.


* Assumes already navigated to the Network> Devices> Devices view.


* Keyword Usage:

> 
> * `XIQSE Devices Show Columns        Admin Profile  Context`


* **Parameters**

    **columns** – list of columns to show



* **Returns**

    returns 1 if successful. else -1



#### xiqse_devices_trigger_search()
> 
> * This keyword clicks the search button in the search box in the Network> Devices view to perform the search


> * Keyword Usage

> > 
> > * `XIQSE Devices Trigger Search`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_wait_for_search_to_complete(retry_duration=10, retry_count=30)
> 
> * This keyword waits for the search to complete in the Network> Devices view


> * Keyword Usage

> > 
> > * `XIQSE Devices Wait For Search To Complete`


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the search to be complete


    * **retry_count** – number of times to check for the search to be complete



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_device_with_ip(device_ip, take_screenshot=True)

* Searches for Device matching Device’s IP Address


* **Parameters**

    
    * **device_ip** – Device IP Address to search for


    * **take_screenshot** – Indicates whether the xiqse_get_device_row keyword should take a screenshot on failure
    this is used when calling from a “wait until” keyword which won’t necessarily want to take a screenshot
    on each failed loop



* **Returns**

    return 1 if Device with specified IP address is found, else -1



#### xiqse_get_device_asset_tag(device_ip)

* This keyword is used to get the Asset Tag value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Asset Tag    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    asset tag for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_base_mac(device_ip)

* This keyword is used to get the base MAC for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Base MAC    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the base MAC for



* **Returns**

    base MAC for the specified device;  -1 if base MAC cannot be determined



#### xiqse_get_device_column_value(device_ip, col_name)

* This keyword is used to get the desired column value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Column Value    ${DEVICE_IP}    Admin Profile`


> * `XIQSE Get Device Column Value    ${DEVICE_IP}    Site`


* **Parameters**

    
    * **device_ip** – device IP to get the value for


    * **col_name** – name of the column to get the value of



* **Returns**

    desired column value for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_license(device_ip)

* This keyword is used to get the device license for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device License    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to look for



* **Returns**

    device license for the specified device;  empty string (“”) if device license cannot be determined



#### xiqse_get_device_nickname(device_ip)

* This keyword is used to get the Nickname value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Nickname    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    nickname for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_notes(device_ip)

* This keyword is used to get the Notes value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Notes    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    notes for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_profile(device_ip)

* This keyword is used to get the profile for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Profile    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the admin profile for



* **Returns**

    admin profile for the specified device;  empty string (“”) if admin profile cannot be determined



#### xiqse_get_device_row(device_ip, take_screenshot=True)

* This keyword returns the row for the device matching the IP address


* **Parameters**

    
    * **device_ip** – IP address of the device to obtain the row for


    * **take_screenshot** – Indicates whether this keyword should take a screenshot on failure.
    This is used when calling from a “wait until” keyword which won’t necessarily want
    to take a screenshot on each failed loop



* **Returns**

    returns the row object



#### xiqse_get_device_row_values(device_ip, col_list)

* Gets a dictionary of device row values based on the passed column label list


* The column list should be a comma-separated list of column headers, like Site,Admin Profile,Family


* Keyword Usage:

> 
> * `@{DEVICE_VALUES}=  XIQSE Get Device Row Values   ${DEVICE_IP}  Site,Admin Profile,Family`


* **Parameters**

    
    * **device_ip** – IP address of the device to obtain the values for


    * **col_list** – comma-separated list of column headers to obtain the values of (e.g., Site,Admin Profile,Family)



* **Returns**

    dictionary containing the values for each of the specified columns



#### xiqse_get_device_serial_number(device_ip)

* This keyword is used to get the serial number for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device Serial Number    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the serial number for



* **Returns**

    serial number for the specified device;  -1 if serial number cannot be determined



#### xiqse_get_device_total_count(take_screenshot=True)

* This keyword returns the total number of items in the Devices table based on the Displaying label.


* **Parameters**

    **take_screenshot** – Indicates whether the keyword should take a screenshot on failure.
    This is used when calling from a “wait until” keyword which won’t necessarily want to take a screenshot
    on each failed loop.



* **Returns**

    returns the total number of items in the table



#### xiqse_get_device_user_data_1(device_ip)

* This keyword is used to get the User Data 1 value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device User Data 1    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    user data 1 for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_user_data_2(device_ip)

* This keyword is used to get the User Data 2 value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device User Data 2    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    user data 2 for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_user_data_3(device_ip)

* This keyword is used to get the User Data 3 value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device User Data 3    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    user data 3 for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_device_user_data_4(device_ip)

* This keyword is used to get the User Data 4 value for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Device User Data 4    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – device IP to get the value for



* **Returns**

    user data 4 for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_get_syslog_status(device_ip)

* This keyword is used to get the syslog status for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Syslog Status    ${DEVICE_IP}`


* **Parameters**

    
    * **device_ip** – device IP to look for


    * **syslog_status** – expected value of the trap status



* **Returns**

    syslog status for the specified device;  empty string (“”) if syslog status cannot be determined



#### xiqse_get_trap_status(device_ip)

* This keyword is used to get the trap status for the specified device in the devices table.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Get Trap Status    ${DEVICE_IP}`


* **Parameters**

    
    * **device_ip** – device IP to look for


    * **trap_status** – expected value of the trap status



* **Returns**

    trap status for the specified device;  empty string (“”) if trap status cannot be determined



#### xiqse_open_configure_device_dialog(device_ip)

* This keyword opens the Configure Device dialog by selecting “Configure…” from the device context menu.


* It assumes the Network> Devices> Devices view is loaded.


* Keyword Usage:

> 
> * `XIQSE Open Configure Device Dialog    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP of the device to open the Configure Device dialog for



* **Returns**

    1 if action is successful, else -1



#### xiqse_open_upgrade_firmware_dialog(device_ip)

* This keyword opens the Upgrade Firmware dialog by selecting “Upgrade Firmware…” from the device context menu.


* It assumes the Network> Devices> Devices view is loaded.


* Keyword Usage:

> 
> * `XIQSE Open Upgrade Firmware Dialog    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP of the device to open the Configure Device dialog for



* **Returns**

    1 if action is successful, else -1



#### xiqse_perform_restart_device(device_ip)
> 
> * This keyword restarts the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab


> * Keyword Usage

> > 
> > * `XIQSE Perform Restart Device    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP address of the device to restart



* **Returns**

    1 if action was successful, else -1



#### xiqse_register_syslog_receiver(device_ip)
> 
> * This keyword registers the syslog receiver for the currently-selected device.


> * It is assumed the user is already on the Network> Devices> Devices tab and the device to register is selected.


> * Keyword Usage

> > 
> > * `XIQSE Register Syslog Receiver  ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP address of the device to select register syslog receiver on



* **Returns**

    1 if action was successful, else -1



#### xiqse_register_trap_receiver(device_ip)
> 
> * This keyword registers the trap receiver for the currently-selected device.


> * It is assumed the user is already on the Network> Devices> Devices tab and the device to register is selected.


> * Keyword Usage

> > 
> > * `XIQSE Register Trap Receiver    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP address of the device to select register trap receiver on



* **Returns**

    1 if action was successful, else -1



#### xiqse_restart_device(device_ip)
> 
> * This keyword restarts the currently-selected device.


> * It is assumed the user is already on the Network> Devices> Devices tab and the device to register is selected.


> * Keyword Usage

> > 
> > * `XIQSE Restart Device    ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP address of the device to restart



* **Returns**

    1 if action was successful, else -1



#### xiqse_select_all_visible_devices()

* This keyword selects all visible rows in the table.  Note this may differ from the actual total number of


* rows, as the table populates with data when the table is scrolled (for example, although there may be 250


* rows in the table, only 44 would be “visible” and obtainable by automation).


* **Returns**

    returns 1 if action was successful, else -1



#### xiqse_select_device(device_ip)
> 
> * This keyword selects the specified device.


> * It is assumed the user is already on the Network> Devices> Devices tab.


> * Keyword Usage

> > 
> > * `XIQSE Select Device`


* **Parameters**

    **device_ip** – IP address of the device tp select



* **Returns**

    1 if action was successful, else -1



#### xiqse_unregister_syslog_receiver(device_ip)
> 
> * This keyword unregisters the syslog receiver for the currently-selected device.


> * It is assumed the user is already on the Network> Devices> Devices tab and the device to unregister is selected.


> * Keyword Usage

> > 
> > * `XIQSE Unregister Syslog Receiver  ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP address of the device to select unregister syslog receiver on



* **Returns**

    1 if action was successful, else -1



#### xiqse_unregister_trap_receiver(device_ip)
> 
> * This keyword unregisters the trap receiver for the currently-selected device.


> * It is assumed the user is already on the Network> Devices> Devices tab and the device to unregister is selected.


> * Keyword Usage

> > 
> > * `XIQSE Unregister Trap Receiver  ${DEVICE_IP}`


* **Parameters**

    **device_ip** – IP address of the device to select unregister trap receiver on



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_until_device_add_operation_complete(retry_duration=30, retry_count=10)
> 
> * This keyword waits until the device add operation has completed by checking the Device Added entry in the


> * Operations panel for progress value of 100%.


> * It is assumed the view is already navigated to the Site tab.


> * NOTE: before performing the Device Add operation, the operations panel should be cleared, as the first match


> * of “Device Added” will be used to check the progress.


> * Keyword Usage

> > 
> > * `XIQSE Site Wait Until Device Add Operation Complete`


> > * `XIQSE Site Wait Until Device Add Operation Complete    retry_duration=10  retry_count=60`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_until_device_added(device_ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the device to show up in the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device exists.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Added    ${DEVICE_IP}    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### xiqse_wait_until_device_archived(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show as being archived in the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device is archived.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Archived    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the archive status of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device archived within specified time; else -1



#### xiqse_wait_until_device_has_base_mac(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to have a base MAC.  This is used for devices


* which don’t have a base MAC and which XIQSE determines the base MAC value for.


* This keyword by default loops 10 times every 30 seconds to check if the device has a base MAC.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Has Base MAC    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the base MAC of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device has a base MAC value within specified time; else -1



#### xiqse_wait_until_device_has_serial_number(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to have a serial number.  This is used for devices


* which don’t have a serial number and which XIQSE determines the serial number for.


* This keyword by default loops 10 times every 30 seconds to check if the device has a serial number.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Has Serial Number    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the serial number of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device has a serial number value within specified time; else -1



#### xiqse_wait_until_device_not_archived(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show as not being archived in the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device is archived or not.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Not Archived    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the archive status of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device not archived within specified time; else -1



#### xiqse_wait_until_device_onboarded_to_xiq(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show as being Onboarded to XIQ in the devices table.


* The column checked is “XIQ Onboarded”.


* This keyword by default loops 10 times every 30 seconds to check if the device is onboarded to xiq.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Onboarded to XIQ    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the XIQ Onboarded status of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device archived within specified time; else -1



#### xiqse_wait_until_device_removed(device_ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the device to be removed from the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device exists.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Removed    ${DEVICE_IP}    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device removed within time; else -1



#### xiqse_wait_until_device_stats_historical(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show it is collecting historical statistics.


* This keyword by default loops 10 times every 30 seconds to check if the device is collecting historical statistics.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Stats Historical    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the stats column on


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device stats within specified time; else -1



#### xiqse_wait_until_device_stats_not_collecting(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show it is not collecting device statistics.


* This keyword by default loops 10 times every 30 seconds to check if the device is not collecting device statistics.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Stats Not Collecting    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the stats column on


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device stats within specified time; else -1



#### xiqse_wait_until_device_stats_threshold_alarms(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show it is collecting threshold alarms.


* This keyword by default loops 10 times every 30 seconds to check if the device is collecting threshold alarms statistics.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Stats Threshold Alarms    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the stats column on


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device stats within specified time; else -1



#### xiqse_wait_until_device_status_down(device_ip, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device status to show as “Device Status Down” in the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device is down.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Status Down    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the status of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device status is down within specified time; else -1



#### xiqse_wait_until_device_status_up(device_ip, retry_duration=30, retry_count=20)

* This keyword is used to wait for the device status to show as “Device Status Up” in the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device is up.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Status Up    ${DEVICE_IP}    retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the status of


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device status is up within specified time; else -1



#### xiqse_wait_until_device_upgraded(device_ip, upgrade_version, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to show as being upgraded to the upgrade version in the devices table.


* This keyword by default loops 10 times every 30 seconds to check if the device is upgraded.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Upgraded    ${DEVICE_IP}    ${UPGRADE_VERSION}     retry_duration=10    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the archive status of


    * **upgrade_version** – expected firmware version value


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device upgraded within specified time; else -1



#### xiqse_wait_until_devices_present(device_count, exact='true', retry_duration=30, retry_count=10)

* This keyword is used to wait for the specified number of devices to be present in the devices table.


* If “exact” is passed as “false”, then it will wait until at least the specified number of devices are present


* (will still succeed if more devices are present than the specified amount); otherwise, this keyword will only


* succeed if the device count exactly matches what is expected.


* This keyword by default loops 10 times every 30 seconds.


* It is assumed the Network> Devices> Devices tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Devices Present    ${DEVICE_COUNT}    retry_duration=10    retry_count=12`


> * `XIQSE Wait Until Devices Present    ${DEVICE_COUNT}    exact=false    retry_duration=20    retry_count=5`


* **Parameters**

    
    * **device_count** – number of devices which should be present


    * **exact** – true (default) or false.


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesAddDevice module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesAddDevice.XIQSE_NetworkDevicesDevicesAddDevice()
Bases: `NetworkDevicesDevicesAddDeviceWebElements`


#### xiqse_add_device_dialog_click_close()
> 
> * This keyword clicks Close in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Click Close`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_device_dialog_click_ok()
> 
> * This keyword clicks OK in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Click OK`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_device_dialog_select_profile(the_value)
> 
> * This keyword sets the IP Address value in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Select Profile  public_v2_Profile`


* **Parameters**

    **the_value** – profile value to select in the Add Device dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_device_dialog_set_ip(the_value)
> 
> * This keyword sets the IP Address value in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Set IP  ${IP}`


* **Parameters**

    **the_value** – IP address value to enter in the Add Device dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_device_dialog_set_nickname(the_value)
> 
> * This keyword sets the Nickname value in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Set Nickname  ${device_nickname}`


* **Parameters**

    **the_value** – nickname value to enter in the Add Device dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_device_dialog_set_poll_status_only(the_value='true')
> 
> * This keyword sets the value of the Poll Status Only checkbox in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Set Poll Status Only`


> > * `XIQSE Add Device Dialog Set Poll Status Only  true`


> > * `XIQSE Add Device Dialog Set Poll Status Only  false`


* **Parameters**

    **the_value** – true/false to indicate if the checkbox should be selected or not



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_device_dialog_set_run_site_add_actions(the_value='true')
> 
> * This keyword sets the value of the Run Site’s Add Action checkbox in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * This feature is supported in XIQ Site Engine versions 21.11.x or later.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Set Run Site Add Actions`


> > * `XIQSE Add Device Dialog Set Run Site Add Actions  true`


> > * `XIQSE Add Device Dialog Set Run Site Add Actions  false`


* **Parameters**

    **the_value** – true/false to indicate if the checkbox should be selected or not



* **Returns**

    1 if action was successful or if the option is not supported, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesBackupConfiguration module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesBackupConfiguration.XIQSE_NetworkDevicesDevicesBackupConfiguration()
Bases: `NetworkDevicesDevicesBackupConfigurationWebElements`


#### xiqse_confirm_backup_configuration_click_no()
> 
> * This keyword clicks No in the Backup Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Backup Configuration Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_backup_configuration_click_ok()
> 
> * This keyword clicks OK in the Backup Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Backup Configuration Click OK`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_backup_configuration_click_yes()
> 
> * This keyword clicks Yes in the Backup Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Backup Configuration Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesDeleteDevice module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesDeleteDevice.XIQSE_NetworkDevicesDevicesDeleteDevice()
Bases: `NetworkDevicesDevicesDeleteDeviceWebElements`


#### xiqse_confirm_delete_device_click_no()
> 
> * This keyword clicks No in the Confirm Delete dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Delete Device Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_delete_device_click_yes()
> 
> * This keyword clicks Yes in the Confirm Delete dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Delete Device Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesFirmwareSelection module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesFirmwareSelection.XIQSE_NetworkDevicesDevicesFirmwareSelection()
Bases: `NetworkDevicesDevicesFirmwareSelectionWebElements`


#### xiqse_click_firmware_selection_cancel_button()
> 
> * Clicks the Cancel button on the Firmware Selection Dialog to discard choices


> * It assumes the Firmware Selection dialog is already open


> * Keyword Usage


>         * `XIQSE Click Firmware Selection Cancel Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_click_firmware_selection_ok_button()
> 
> * Clicks the OK button on the Firmware Selection Dialog to accept choices


> * It assumes the Firmware Selection dialog is already open


> * Keyword Usage


>         * `XIQSE Click Firmware Selection OK Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_click_refresh_images()

* This keyword refreshes the uploaded firmware images by selecting “Refresh Images…” from the Firmware Selection dialog.


* It assumes the Firmware Selection dialog is already open.


* Keyword Usage:


* `XIQSE Click Refresh Images`


* **Returns**

    1 if action is successful, else -1



#### xiqse_select_firmware_image(firmware_image)
> 
> * This keyword selects the specified firmware for the device upgrade.


> * It is assumed the user is already on the Firmware Selection dialog.


> * Keyword Usage

> > 
> > * `XIQSE Select Firmware Image`


* **Parameters**

    **firmware_image** – Firmware Image from the table to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_for_refresh_images_to_complete(retry_duration=10, retry_count=30)

* This keyword waits for the “Refreshing Images” loading mask to complete before continuing


* Keyword Usage


* ‘’XIQSE Wait For Refresh Images to Complete’’


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the refresh to be complete


    * **retry_count** – Number of times for the check to be complete



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesInventorySettings module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesInventorySettings.XIQSE_NetworkDevicesDevicesInventorySettings()
Bases: `NetworkDevicesDevicesInventorySettingsWebElements`


#### xiqse_click_inventory_settings_cancel_button()
> 
> * Clicks the Cancel button for the Inventory Settings Dialog to close the dialog.


> * It assumes the Inventory Settings dialog is already open.


> * Keyword Usage


>         * `XIQSE Click Inventory Settings Cancel Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_click_inventory_settings_ok_button()
> 
> * Clicks the OK button on the Inventory Settings Dialog to accept choices


> * It assumes the Inventory Settings dialog is already open


> * Keyword Usage


>         * `XIQSE Click Inventory Settings OK Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_inventory_settings_dialog_select_configuration_download_mib(the_value)
> 
> * This keyword selects the Configuration Download MIB type in the Inventory Settings dialog.


> * It is assumed the Inventory Settings dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Configuration Download MIB Type    Disabled`


> > * `XIQSE Configuration Download MIB Type    Script\``


* **Parameters**

    **the_value** – value to select in the Configuration Download MIB dropdown (Disabled,Script)



* **Returns**

    1 if action was successful, else -1



#### xiqse_inventory_settings_dialog_select_device_family_definition_filename(the_value)
> 
> * This keyword selects the File Definition Family Name in the Inventory Settings dialog.


> * It is assumed the Inventory Settings dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Inventory Settings Dialog Select Device Family Definition Filename   Extreme Control Upgrade - SCP`


* **Parameters**

    **the_value** – value to select in the Device Family Definition Filename dropdown



* **Returns**

    1 if action was successful, else -1



#### xiqse_inventory_settings_dialog_select_file_transfer_mode(the_value)
> 
> * This keyword selects the File Transfer Mode in the Inventory Settings dialog.


> * It is assumed the Inventory Settings dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Inventory Settings Dialog Select File Transfer Mode    TFTP`


> > * `XIQSE Inventory Settings Dialog Select File Transfer Mode    SCP`


> > * `XIQSE Inventory Settings Dialog Select File Transfer Mode    FTP`


> > * `XIQSE Inventory Settings Dialog Select File Transfer Mode    SFTP`


* **Parameters**

    **the_value** – value to select in the File Transfer Mode dropdown (TFTP,SCP,FTP,SFTP)



* **Returns**

    1 if action was successful, else -1



#### xiqse_inventory_settings_dialog_select_firmware_download_mib(the_value)
> 
> * This keyword selects the Firmware Download MIB type in the Inventory Settings dialog.


> * It is assumed the Inventory Settings dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Firmware Download MIB Type    Disabled`


> > * `XIQSE Firmware Download MIB Type    Script\``


* **Parameters**

    **the_value** – value to select in the Firmware Download MIB dropdown (Disabled,Script)



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesRestartDevice module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesRestartDevice.XIQSE_NetworkDevicesDevicesRestartDevice()
Bases: `NetworkDevicesDevicesRestartDeviceWebElements`


#### xiqse_click_restart_devices_close_button()

* This keyword clicks the “Close” button on the Restart Device menu


* It assumes the Restart Device dialog is already open


* Keyword Usage:


* ‘XIQSE Click Restart Devices Close Button’


* **Returns**

    1 if action is successful, else -1



#### xiqse_click_start_restart_button()

* This keyword clicks the “Start” button on the Restart Device menu to begin restarting the device selected


* It assumes the Restart Device dialog is already open


* Keyword Usage:


* ‘XIQSE Click Start Restart Button’


* **Returns**

    1 if action is successful, else -1



#### xiqse_click_start_restart_yes_button()

* This Keyword clicks the “Yes” button to begin the switch restart


* Keyword usage:


* ‘XIQSE Click Start Restart Yes Button’


* **Returns**

    1 if action is successful, else -1



#### xiqse_wait_for_restart_operation_to_complete(seconds=900)

* This keyword waits for the “Restart Operation Complete” element to appear before continuing


* Keyword Usage


* ‘’XIQSE Wait For Restart Operation Complete’’


* **Parameters**

    
    * **retry_duration** – amount of time to wait in between each check for the refresh to be complete


    * **retry_count** – Number of times for the check to be complete



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesRestoreConfiguration module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesRestoreConfiguration.XIQSE_NetworkDevicesDevicesRestoreConfiguration()
Bases: `NetworkDevicesDevicesRestoreConfigurationWebElements`


#### xiqse_confirm_restore_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Restore Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Set Restore Configuration Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_restore_dialog_click_no()
> 
> * This keyword clicks No in the Restore Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Set Restore Configuration Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_restore_dialog_click_ok()
> 
> * This keyword clicks OK in the Restore Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Restore Configuration Click OK`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_restore_dialog_click_start()
> 
> * This keyword clicks Start in the Restore Configuration dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Set Restore Configuration Dialog Click  Yes`


* **Returns**

    1 if action was successful, else -1



#### xiqse_confirm_restore_dialog_click_yes()
> 
> * This keyword clicks Yes in the Confirm Change dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Set Restore Configuration Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1



#### xiqse_set_restore_dialog_select_configuration(the_value)

* This keyword selects the configuration value in the Restore Configuration dialog.


* It is assumed the dialog is already opened.


* Keyword Usage


* `XIQSE Set Restore Dialog Select Configuration  Site Engine Archive`


* **Parameters**

    **the_value** – configuration value to select in the Restore Configuration dialog



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesSetProfile module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesSetProfile.XIQSE_NetworkDevicesDevicesSetProfile()
Bases: `NetworkDevicesDevicesSetProfileWebElements`


#### xiqse_set_profile_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Set Device Profile dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Set Profile Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_set_profile_dialog_click_ok()
> 
> * This keyword clicks OK in the Set Device Profile dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Set Profile Dialog Click OK`


* **Returns**

    1 if action was successful, else -1



#### xiqse_set_profile_dialog_select_profile(the_value)
> 
> * This keyword sets the IP Address value in the Add Device dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Add Device Dialog Select Profile  public_v2_Profile`


* **Parameters**

    **the_value** – profile value to select in the Set Device Profile dialog



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesUpgradeFirmware module


### _class_ extauto.xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesUpgradeFirmware.XIQSE_NetworkDevicesDevicesUpgradeFirmware()
Bases: `NetworkDevicesDevicesUpgradeFirmwareWebElements`


#### xiqse_click_begin_downloading_firmware_no_button()
> 
> * Clicks the No button on the Begin Downloading Firmware Dialog to discard choices


> * It assumes the Begin Downloading Firmware dialog is already open


> * Keyword Usage


>         * `XIQSE Click Begin Downloading Firmware No Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_click_begin_downloading_firmware_yes_button()
> 
> * Clicks the Yes button on the Begin Downloading Firmware Dialog to discard choices


> * It assumes the Begin Downloading Firmware dialog is already open


> * Keyword Usage


>         * `XIQSE Click Begin Downloading Firmware Yes Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_click_upgrade_firmware_close_button()
> 
> * Clicks the Cancel button on the Upgrade Firmware Dialog to discard choices


> * It assumes the Upgrade Firmware dialog is already open


> * Keyword Usage


>         * `XIQSE Click Upgrade Firmware Close Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_click_upgrade_firmware_start_button()
> 
> * Clicks the Start button on the Upgrade Firmware Dialog to accept choices


> * It assumes the Firmware Selection dialog is already open


> * Keyword Usage


>         * `XIQSE Click Upgrade Firmware Start Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_open_assign_firmware_image()

* This keyword opens the Assign Firmware Image selector by selecting “Assign Firmware…” from the Upgrade Firmware dialog.


* It assumes the Upgrade Firmware dialog is already open.


* Keyword Usage:

> 
> * `XIQSE Open Assign Firmware Image`


* **Returns**

    1 if action is successful, else -1



#### xiqse_open_inventory_settings()

* This keyword opens the Inventory Settings dialog by selecting “Inventory Settings” from the Upgrade Firmware dialog.


* It assumes the Upgrade Firmware dialog is already open.


* Keyword Usage:

> 
> * `XIQSE Open Inventory Settings`


* **Returns**

    1 if action is successful, else -1



#### xiqse_wait_for_processed_no_failures_text(seconds=900)
> 
> * Institutes a loop waiting for “Processed 1 of 1 devices with 0 failures” text to appear in the Dialog


> * It assumes the dialog is already open


> * Keyword Usage


>         * `XIQSE Wait for Processed No Failures Text`


* **Returns**

    1 if action was successful, else -1


## Module contents
