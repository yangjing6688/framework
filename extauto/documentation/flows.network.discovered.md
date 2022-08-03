# extauto.xiqse.flows.network.discovered package

## Submodules

## extauto.xiqse.flows.network.discovered.XIQSE_NetworkDiscovered module


### _class_ extauto.xiqse.flows.network.discovered.XIQSE_NetworkDiscovered.XIQSE_NetworkDiscovered()
Bases: `NetworkDiscoveredWebElements`


#### xiqse_discovered_add_columns(column_name, \*columns)
> 
> * This keyword selects the Columns menu option for the provided column name and enables the provided columns


> * Keyword Usage

> > 
> > * `XIQSE Discovered Add Columns  Status  Connector`


* **Parameters**

    
    * **column_name** – column name to access


    * **columns** – List of columns to display



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_add_device(ip)
> 
> * This keyword adds the device by selecting the row matching the specified IP address, clicking Add Devices on
> the toolbar, then clicking Add in the Add Device dialog.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Add Device    ${DEVICE_IP}`


* **Parameters**

    **ip** – IP Address of the device to add



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_add_devices(ip_list)
> 
> * This keyword adds the list of devices by selecting the specified IP addresses, clicking ‘Add Devices’ on the


> * toolbar, then clicking ‘Add’ in the Add Device dialog.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Add Devices    ${DEVICE_IP1}.${DEVICE_IP2},${DEVICE_IP3}`


* **Parameters**

    **ip_list** – comma-separated list of IP Addresses to add



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_clear_all_devices()
> 
> * This keyword clears all devices from the Discovered table.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Clear All Devices`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_clear_row_by_ip(ip)
> 
> * This keyword clears the row matching the specified IP address.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Clear Row By IP    ${DEVICE_IP}`


* **Parameters**

    **ip** – IP Address of the row to clear



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_configure_devices_toolbar()
> 
> * This keyword clicks the Configure Devices… button on the Discovered table toolbar.


> * It is assumed the Network> Discovered tab is already selected.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Configure Devices Toolbar`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_confirm_table_empty()
> 
> * This keyword confirms the table is empty.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Confirm Table Empty`


* **Returns**

    1 if table is empty, else -1



#### xiqse_discovered_confirm_table_not_empty()
> 
> * This keyword confirms the table is not empty.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Confirm Table Not Empty`


* **Returns**

    1 if table is not empty, else -1



#### xiqse_discovered_confirm_table_row_count(value)
> 
> * This keyword confirms the table contains the expected number of rows.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Confirm Table Row Count    5`


* **Parameters**

    **value** – expected number of rows to check for



* **Returns**

    1 if table contains the expected number of rows, else -1



#### xiqse_discovered_do_not_show_in_groups()
> 
> * This keyword deselects the “Show in Groups” checkbox on the column menu on the Network> Discovered tab.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Do Not Show In Groups`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_find_row_with_ip(ip)

* Searches for row matching the specified IP Address


* **Parameters**

    **ip** – IP Address to search for



* **Returns**

    return 1 if row with specified IP address is found, else -1



#### xiqse_discovered_find_row_with_serial_number(serial_number)

* Searches for row matching the specified Serial Number


* Keyword Usage

> 
> * `XIQSE Discovered Find Row With Serial Number  ${SERIAL_NUMBER}`


* **Parameters**

    **serial_number** – Serial Number to search for



* **Returns**

    return 1 if row with specified IP address is found, else -1



#### xiqse_discovered_get_device_column_value(serial_number, col_name)

* This keyword is used to get the desired column value for the specified device in the discovered table.


* It is assumed the Network> Devices> Discovered tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Discovered Get Device Column Value    ${SERIAL_NUMBER}    Profile`


> * `XIQSE Discovered Get Device Column Value    ${SERIAL_NUMBER}    Status`


* **Parameters**

    
    * **serial_number** – device Serial Number to get the value for


    * **col_name** – name of the column to get the value of



* **Returns**

    column value for the specified device;  empty string (“”) if value cannot be determined



#### xiqse_discovered_get_row_by_ip(ip)

* This keyword returns the row containing the specified IP address


* **Parameters**

    **ip** – IP address of the device to obtain the row for



* **Returns**

    returns the row object if found, else None



#### xiqse_discovered_get_row_by_serial_number(serial_number)

* This keyword returns the row containing the specified Serial Number


* Keyword Usage

> 
> * `XIQSE Discovered Get Row By Serial Number  ${SERIAL_NUMBER}`


* **Parameters**

    **serial_number** – Serial Number of the device to obtain the row for



* **Returns**

    returns the row object if found, else None



#### xiqse_discovered_open_configure_devices_by_serial_number(serial_number)
> 
> * This keyword opens the ‘Configure Devices…’ view for the specified Serial Number.


> * The device row is selected and then the ‘Configure Devices…’ button on the toolbar is clicked.


> * It is assumed the Network> Discovered tab is already selected.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Open Configure Devices By Serial Number  ${SERIAL_NUMBER}`


* **Parameters**

    **serial_number** – Serial Number of the Device



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_open_configure_devices_menu_by_serial_number(serial_number)
> 
> * This keyword opens the ‘Configure Devices…’ view for the specified Serial Number.


> * The device row is selected and then the ‘Configure Devices…’ menu option is clicked.


> * This assumes that the OneView > Network > Discovered view is selected.


> * Keyword Usage

> > 
> > * ‘’XIQSE Discovered Open Configure Devices Menu Serial Number  ${SERIAL_NUMBER}\`\`


* **Parameters**

    **serial_number** – Serial Number for the Device



* **Returns**

    return 1 if action was successful, else -1



#### xiqse_discovered_refresh_table()
> 
> * This keyword clicks the refresh icon under the table.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Refresh Table`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_select_row_by_ip(ip)
> 
> * This keyword selects the specified IP in the Network> Discovered table.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Select Row By IP    1.2.3.4`


* **Parameters**

    **ip** – IP address to select in the table



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_select_row_by_serial_number(serial_number)
> 
> * This keyword selects the row containing the specified Serial Number in the Network> Discovered table.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Select Row By Serial Number  ${SERIAL_NUMBER}`


* **Parameters**

    **serial_number** – Serial Number to select in the table



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_select_rows_by_ips(ip_list)
> 
> * This keyword selects the specified IPs in the Network> Discovered table.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Select Rows By IPs    1.1.1.1,2.2.2.2,3.3.3.3`


* **Parameters**

    **ip_list** – comma-separated list of IP addresses to select in the table



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_sort_ascending(column_name)
> 
> * This keyword selects the Sort Ascending menu option for the provided column name.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Sort Ascending  Status`


* **Parameters**

    **column_name** – column name to sort ascending



* **Returns**

    1 if action was successful, else -1



#### xiqse_discovered_sort_descending(column_name)
> 
> * This keyword selects the Sort Descending menu option for the provided column name.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Sort Descending  Status`


* **Parameters**

    **column_name** – column name to sort descending



* **Returns**

    1 if action was successful, else -1



#### xiqse_get_discovered_table_row_count()
> 
> * This keyword returns the number of rows in the Discovered table based on the “Displaying # rows” label.


> * Keyword Usage

> > 
> > * `XIQSE Get Discovered Table Row Count`


* **Returns**

    1 if table contains the expected number of rows, else -1



#### xiqse_wait_until_device_staged(device_ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the device to show up as having staged config in the discovered table.


* This keyword by default loops 10 times every 30 seconds to check if the device exists.


* It is assumed the Network> Discovered tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Staged    ${DEVICE_IP}    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### xiqse_wait_until_discovered_device_added(ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the Discovered table to contain the specified device.


* This keyword by default loops 10 times every 30 seconds to check if the device is present.


* It is assumed the Network> Discovered tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Discovered Device Added    1.2.3.4    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **ip** – ip address of the device to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### xiqse_wait_until_discovered_device_removed(ip, retry_duration=10, retry_count=30)

* This keyword is used to wait for the Discovered table to no longer contain the specified device.


* This keyword by default loops 10 times every 30 seconds to check if the device is present.


* It is assumed the Network> Discovered tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Discovered Device Removed    1.2.3.4    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **ip** – ip address of the device to look for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### xiqse_wait_until_discovered_table_contains_row_count(value, retry_duration=10, retry_count=30)

* This keyword is used to wait for the Discovered table to contain the expected number of rows.


* This keyword by default loops 10 times every 30 seconds to check if the table is empty.


* It is assumed the Network> Discovered tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Discovered Table Contains Row Count    5    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **value** – number of expected rows to wait for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1



#### xiqse_wait_until_discovered_table_empty(retry_duration=10, retry_count=30)

* This keyword is used to wait for the Discovered table to be empty.


* This keyword by default loops 10 times every 30 seconds to check if the table is empty.


* It is assumed the Network> Discovered tab is already selected.


* Keyword Usage:

> 
> * `XIQSE Wait Until Discovered Table Empty    retry_duration=30    retry_count=12`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device added within time; else -1


## extauto.xiqse.flows.network.discovered.XIQSE_NetworkDiscoveredAddDevices module


### _class_ extauto.xiqse.flows.network.discovered.XIQSE_NetworkDiscoveredAddDevices.XIQSE_NetworkDiscoveredAddDevices()
Bases: `NetworkDiscoveredAddDevicesWebElements`


#### xiqse_discovered_add_devices_dialog_click_add()
> 
> * This keyword clicks ‘Add’ in the Add Device dialog.


> * Keyword Usage

> > 
> > * `XIQSE Discovered Add Devices Dialog Click Add`


* **Returns**

    1 if action was successful, else -1


## Module contents
