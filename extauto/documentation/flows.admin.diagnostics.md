# extauto.xiqse.flows.admin.diagnostics package

## extauto.xiqse.flows.admin.diagnostics.XIQSE_AdminDiagnostics module


### _class_ extauto.xiqse.flows.admin.diagnostics.XIQSE_AdminDiagnostics.XIQSE_AdminDiagnostics()
Bases: `AdminDiagnosticsWebElements`


#### xiqse_auto_onboard_xiqse(email_value, pwd_value)

* Clicks the Auto Onboard XIQ-SE button, enters the email and password credentials, clicks Submit, and confirms


* the onboard action.


* **Parameters**

    
    * **email_value** – Value to enter into the Email field


    * **pwd_value** – Value to enter into the Password field



* **Returns**

    1 if successful, else -1



#### xiqse_confirm_onboard_status(device_ip, device_type, expected_value)

* Searches for row matching device’s IP Address and Type and confirms the Onboard Status value is expected.


* Assumes the XIQ Device Message Details view is open and the Onboard Status column is shown.


* **Parameters**

    
    * **device_ip** – Device IP Address to search for


    * **device_type** – Device Type to search for


    * **expected_value** – expected value of the onboard status



* **Returns**

    returns 1 if onboard status matches the expected value, else -1



#### xiqse_confirm_server_log_contents_contains_string(value)
> 
> * This keyword checks for the specified string in the contents of the Server Log view.


> * Assumes already navigated to the Administration> Diagnostics> Server> Server Log view.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Server Log Contents Contains String  ${STRING_TO_FIND}`


* **Parameters**

    **value** – string to look for in the server log



* **Returns**

    1 if action was successful, else -1



#### xiqse_expand_server_tree_node()
> 
> * This keyword expands the Server tree node in the panel on the left if not already expanded.


> * Keyword Usage

> > 
> > * `XIQSE Expand Server Tree Node`


* **Returns**

    1 if action was successful, else -1



#### xiqse_expand_system_tree_node()
> 
> * This keyword expands the System tree node in the panel on the left if not already expanded.


> * Keyword Usage

> > 
> > * `XIQSE Expand System Tree Node`


* **Returns**

    1 if action was successful, else -1



#### xiqse_get_xiq_device_message_details_row(device_ip, device_type=None)

* This keyword returns the row for the device matching the IP address and optional type


* **Parameters**

    
    * **device_ip** – IP address of the device to obtain the row for


    * **device_type** – Device Type of the device to obtain the row for - optional



* **Returns**

    returns the row object if found, else None



#### xiqse_get_xiq_device_message_details_row_count()

* Returns the number of rows displayed in the XIQ Device Message Details table, as reported by


* the “Displaying # of rows” label.


* Assumes the XIQ Device Message Details view is open.


* **Returns**

    number of rows in the table



#### xiqse_onboard_xiqse_if_not_onboarded(xiqse_ip, email_value, pwd_value)

* Onboards XIQSE if it is not yet onboarded:


* Checks if XIQSE is present in the table and, if it is not, it sends the request to onboard.


* If XIQSE is present in the table with onboard status of UNKNOWN, it sends the request to onboard.


* **Parameters**

    
    * **xiqse_ip** – IP of XIQSE to check for


    * **email_value** – Value to enter into the Email field


    * **pwd_value** – Value to enter into the Password field



* **Returns**

    1 if successful, else -1



#### xiqse_select_server_log_tree_node()
> 
> * This keyword selects the Server Log tree node in the panel on the left.


> * If the parent “Server” node is not expanded, it will expand it first.


> * Keyword Usage

> > 
> > * `XIQSE Select Server Log Tree Node`


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_xiq_device_message_details_tree_node()
> 
> * This keyword selects the XIQ Device Message Details tree node in the panel on the left.


> * If the parent “System” node is not expanded, it will expand it first.


> * Keyword Usage

> > 
> > * `XIQSE Select XIQ Device Message Details Tree Node`


* **Returns**

    1 if action was successful, else -1



#### xiqse_server_log_clear()
> 
> * This keyword clicks the Clear button in the Server Log view.


> * Assumes already navigated to the Administration> Diagnostics> Server> Server Log view.


> * Keyword Usage

> > 
> > * `XIQSE Server Log Clear`


* **Returns**

    1 if action was successful, else -1



#### xiqse_server_log_refresh()
> 
> * This keyword clicks the Refresh button in the Server Log view.


> * Assumes already navigated to the Administration> Diagnostics> Server> Server Log view.


> * Keyword Usage

> > 
> > * `XIQSE Server Log Refresh`


* **Returns**

    1 if action was successful, else -1



#### xiqse_set_level_advanced()
> 
> * This keyword sets the Level dropdown to Advanced.


> * Keyword Usage

> > 
> > * `XIQSE Set Level Advanced`


* **Returns**

    1 if action was successful, else -1



#### xiqse_wait_until_device_has_expected_onboard_status(device_ip, device_type, expected_value, retry_duration=30, retry_count=10)

* This keyword is used to wait for the device to have the expected Onboard Status in the Device Message Details.


* The column checked is “Onboarded Status”.


* This keyword by default loops 10 times every 30 seconds to check if the status is at the expected value.


* It is assumed the Administration> Diagnostics tab is already selected and on the System> ExtremeCloud IQ Device


* Message Details view.


* Keyword Usage:

> 
> * `XIQSE Wait Until Device Has Expected Onboard Status   1.1.1.1  X460-G2-48t-10G4  DEVICE_ALREADY_ONBOARDED`


> * `XIQSE Wait Until Device Has Expected Onboard Status   2.2.2.2  XIQ_SE  SUCCESS  retry_duration=10  retry_count=12`


* **Parameters**

    
    * **device_ip** – device IP to check the Onboard Status of


    * **device_type** – Device Type of the device to obtain the information for


    * **expected_value** – expected value for the Onboard Status to wait for


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device has expected onboard status within specified time; else -1



#### xiqse_xiq_device_message_details_auto_onboard_xiqse(email_value, pwd_value)

* Clicks the Auto Onboard XIQ-SE button.


* Assumes the XIQ Device Message Details view is open.


* **Parameters**

    
    * **email_value** – Value to enter into the Email field


    * **pwd_value** – Value to enter into the Password field



* **Returns**

    1 if successful, else -1



#### xiqse_xiq_device_message_details_clear_filter()

* Clears the filter on the XIQ Device Message Details table.


* Assumes the XIQ Device Message Details view is open and the search box is open.


* **Returns**

    1 if action is successful, else -1



#### xiqse_xiq_device_message_details_filter_table(value)

* Filters the XIQ Device Message Details table by the specified value.


* Assumes the XIQ Device Message Details view is open.


* **Parameters**

    **value** – string to enter in the search field



* **Returns**

    1 if action is successful, else -1



#### xiqse_xiq_device_message_details_get_last_update_time(device_ip, device_type)

* Gets the value in the Last Update Time column for the specified device in the XIQ Device Message Details table.


* Assumes the XIQ Device Message Details view is open.


* **Parameters**

    
    * **device_ip** – IP Address of the device to obtain the information for


    * **device_type** – Device Type of the device to obtain the information for



* **Returns**

    Value of the ‘Last Update Time’ column if action is successful, else -1



#### xiqse_xiq_device_message_details_get_metric_from_device(device_ip, device_type, metric)

* Gets the specified metric value sent to XIQ for the specified device by using the Show XIQ Messages button


* in the XIQ Device Message Details table.


* Assumes the XIQ Device Message Details view is open.


* **Parameters**

    
    * **device_ip** – IP Address of the device to obtain the information for


    * **device_type** – Device Type of the device to obtain the information for


    * **metric** – Value of the metric to obtain the information for



* **Returns**

    metric value if action is successful, else -1



#### xiqse_xiq_device_message_details_get_onboard_status(device_ip, device_type)

* Gets the value in the Onboard Status column for the specified device in the XIQ Device Message Details table.


* Assumes the XIQ Device Message Details view is open.


* **Parameters**

    
    * **device_ip** – IP Address of the device to obtain the information for


    * **device_type** – Device Type of the device to obtain the information for



* **Returns**

    Value of the ‘Onboard Status’ column if action is successful, else -1



#### xiqse_xiq_device_message_details_hide_columns(\*columns)

* This keyword hides the specified list of columns if they are currently shown.


* Assumes already navigated to the Administration> Diagnostics> System> XIQ Device Message Details view.


* Keyword Usage:

> 
> * `XIQSE XIQ Device Message Details Hide Columns        Onboard Status  Onboard`


* **Parameters**

    **columns** – list of columns to hide



* **Returns**

    returns 1 if successful. else -1



#### xiqse_xiq_device_message_details_refresh_table()

* Refreshes the table on the XIQ Device Message Details page.


* Assumes the XIQ Device Message Details view is open.


* **Returns**

    returns 1 if action is successful, else -1



#### xiqse_xiq_device_message_details_show_columns(\*columns)

* This keyword shows the specified list of columns if they are currently hidden.


* Assumes already navigated to the Administration> Diagnostics> System> XIQ Device Message Details view.


* Keyword Usage:

> 
> * `XIQSE XIQ Device Message Details Show Columns        Onboard Status  Onboard`


* **Parameters**

    **columns** – list of columns to show



* **Returns**

    returns 1 if successful. else -1
