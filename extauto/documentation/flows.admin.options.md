# extauto.xiqse.flows.admin.options package

## extauto.xiqse.flows.admin.options.XIQSE_AdminOptions module


### _class_ extauto.xiqse.flows.admin.options.XIQSE_AdminOptions.XIQSE_AdminOptions()
Bases: `AdminOptionsWebElements`


#### get_xiqse_serial_number()
> 
> * This keyword navigates to the XIQ Connection option on the Administration> Options tab and


> * returns the XIQ-SE serial number.


> * Keyword Usage

> > 
> > * `Get XIQSE Serial Number`


* **Returns**

    XIQ-SE serial number, if found;  else, -1



#### get_xiqse_serial_number_label_value()
> 
> * This keyword returns the XIQ-SE serial number, found on the XIQ Connection options page.


> * It is assumed the view is already navigated to the XIQ Connection option on the Administration> Options tab.


> * Keyword Usage

> > 
> > * `Get XIQSE Serial Number Label Value`


* **Returns**

    XIQ-SE serial number, if found;  else, empty string



#### xiqse_confirm_xiq_connection_enable_sharing_option(expected_value='true')
> 
> * This keyword confirms the expected value of the Enable Sharing field for the XIQ Connection option.


> * It is assumed the view is already navigated to the XIQ Connection option on the Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Confirm XIQ Connection Enable Sharing Option  true`
> > `XIQSE Confirm XIQ Connection Enable Sharing Option  false`


* **Parameters**

    **expected_value** – indicates whether the Enable Sharing option is expected to be selected (true) or not (false)



* **Returns**

    1 if value is at expected value, else -1



#### xiqse_disable_xiq_connection_sharing_and_save()
> 
> * This keyword deselects the XIQ Connection “Enable Sharing” option and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Disable XIQ Connection Sharing and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_enable_xiq_connection_sharing_and_save()
> 
> * This keyword selects the XIQ Connection “Enable Sharing” option and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Enable XIQ Connection Sharing and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_reset_options()
> 
> * This keyword clicks the Reset button on the Options page.
> If the button is disabled, the options are already at the last-saved values and this is a no-op.
> It is assumed the view is already navigated to the Administration> Options tab and to
> the specific option to be reset.


> * Keyword Usage

> > 
> > * `XIQSE Reset Options`


* **Returns**

    1 if options were restored to defaults (or button is disabled), else -1



#### xiqse_restore_default_inventory_manager_options_and_save()
> 
> * This keyword restores the default values of the Inventory Manager options and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Restore Default Inventory Manager Options and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_restore_default_options()
> 
> * This keyword clicks the Restore Defaults button on the Options page.
> If the button is disabled, the options are already at the defaults and this is a no-op.
> It is assumed the view is already navigated to the Administration> Options tab and to
> the specific option to be restored.


> * Keyword Usage

> > 
> > * `XIQSE Restore Default Options`


* **Returns**

    1 if options were restored to defaults (or button is disabled), else -1



#### xiqse_restore_default_options_and_save()
> 
> * This keyword clicks the Restore Defaults button on the Options page and then clicks Save.
> If the button is disabled, the options are already at the defaults and this is a no-op.
> It is assumed the view is already navigated to the Administration> Options tab and to
> the specific option to be restored.


> * Keyword Usage

> > 
> > * `XIQSE Restore Default Options and Save`


* **Returns**

    1 if options were restored to defaults (or button is disabled), else -1



#### xiqse_restore_default_site_engine_general_options_and_save()
> 
> * This keyword restores the default values of the Site Engine - General options and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Restore Default Site Engine General Options and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_restore_default_status_polling_options_and_save()
> 
> * This keyword restores the default values of the Status Polling options and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Restore Default Status Polling Options and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_restore_default_web_server_options_and_save()
> 
> * This keyword restores the default values of the Web Server options and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Restore Default Web Server Options and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_restore_default_xiq_connection_options_and_save()
> 
> * This keyword restores the default values of the XIQ Connection options and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Restore Default XIQ Connection Options and Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_save_options()
> 
> * This keyword clicks the Save button to save any unsaved options.
> If the button is disabled, there are no unsaved options and this is a no-op.
> It is assumed the view is already navigated to the Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Save Options`


* **Returns**

    1 if options were saved (or button is disabled/no changes to save), else -1



#### xiqse_select_inventory_manager_option()

* This keyword selects the Inventory Manager option in the Administration> Options tree.


* Keyword Usage


* `XIQSE Select Inventory Manager Option`


* **Returns**

    1 if selection was made, else -1



#### xiqse_select_site_engine_general_option()
> 
> * This keyword selects the Site Engine - General option in the Options tree.


> * Keyword Usage

> > 
> > * `XIQSE Select Site Engine General Option`


* **Returns**

    1 if selection was made, else -1



#### xiqse_select_status_polling_option()

* This keyword selects the Status Polling option in the Administration> Options tree.


* Keyword Usage


* `XIQSE Select Status Polling Option`


* **Returns**

    1 if selection was made, else -1



#### xiqse_select_web_server_option()
> 
> * This keyword selects the Web Server option in the Options tree.


> * Keyword Usage

> > 
> > * `XIQSE Select Web Server Option`


* **Returns**

    1 if selection was made, else -1



#### xiqse_select_xiq_connection_option()
> 
> * This keyword selects the XIQ Connection option in the Options tree.


> * Keyword Usage

> > 
> > * `XIQSE Select XIQ Connection Option`


* **Returns**

    1 if selection was made, else -1



#### xiqse_set_device_tree_name_format(value='IP Address')
> 
> * This keyword sets the Device Tree Name Format value for the Site Engine - General option.


> * It is assumed the view is already navigated to the Site Engine - General option on the


> * Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Set Device Tree Name Format Value    IP Address`


> > * `XIQSE Set Device Tree Name Format Value    Nickname`


> > * `XIQSE Set Device Tree Name Format Value    System Name`


* **Parameters**

    **value** – value to select in the Device Tree Name Format dropdown field



* **Returns**

    1 if value was set, else -1



#### xiqse_set_device_tree_name_format_and_save(value='IP Address')
> 
> * This keyword sets the value of the Site Engine - General’s Device Tree Name Format option


> * and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Set Device Tree Name Format and Save  IP Address`


> > * `XIQSE Set Device Tree Name Format and Save  Nickname`


> > * `XIQSE Set Device Tree Name Format and Save  System Name`


* **Parameters**

    **value** – value to select in the Device Tree Name Format dropdown field



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_scp_login_information_anonymous(value)

* This keyword sets the ‘Anonymous’ checkbox in the Inventory Manager> File Transfer> SCP Server Properties section


* It is assumed the view is already navigated to the Inventory Manager panel.


* Keyword Usage


* `XIQSE Set SCP Login Information Anonymous  true`


* `XIQSE Set SCP Login Information Anonymous  false`


* **Parameters**

    **value** – Indicates whether to enable or disable the checkbox; default is “true”



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_scp_login_information_password(the_val)

* This keyword enters the Password value in the Inventory Manager> File Transfer> SCP Server Properties section


* It is assumed the view is already navigated to the Inventory Manager panel.


* Keyword Usage


* `XIQSE Set SCP Login Information Password  ${password}`


* **Parameters**

    **the_val** – The password for the specified user



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_scp_login_information_username(the_val)

* This keyword enters the Username value in the Inventory Manager> File Transfer> SCP Server Properties section


* It is assumed the view is already navigated to the Inventory Manager panel.


* Keyword Usage


* `XIQSE Set SCP Login Information Username  ${username}`


* **Parameters**

    **the_val** – A valid XIQSE username



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_sftp_login_information_anonymous(value)

* This keyword sets the ‘Anonymous’ checkbox in the Inventory Manager> File Transfer> SFTP Server Properties section


* It is assumed the view is already navigated to the Inventory Manager panel.


* Keyword Usage


* `XIQSE Set SFTP Login Information Anonymous  true`


* `XIQSE Set SFTP Login Information Anonymous  false`


* **Parameters**

    **value** – Indicates whether to enable or disable the checkbox; default is “true”



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_sftp_login_information_password(the_val)

* This keyword enters the Password value in the Inventory Manager> File Transfer> SFTP Server Properties section


* It is assumed the view is already navigated to the Inventory Manager panel.


* Keyword Usage


* `XIQSE Set SFTP Login Information Password  ${password}`


* **Parameters**

    **the_val** – The password for the specified user



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_sftp_login_information_username(the_val)

* This keyword enters the Username value in the Inventory Manager> File Transfer> SFTP Server Properties section


* It is assumed the view is already navigated to the Inventory Manager panel.


* Keyword Usage


* `XIQSE Set SFTP Login Information Username  ${username}`


* **Parameters**

    **the_val** – A valid XIQSE username



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_status_polling_group_2_interval_value(value='5')
> 
> * This keyword sets the value of the Status Polling Group 2 Interval option.


> * It is assumed the view is already navigated to the Status Polling option on the Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Set Status Polling Group 2 Interval Value  5`


> > * `XIQSE Set Status Polling Group 2 Interval Value  2`


* **Parameters**

    **value** – Value to enter in the Group 2 Interval option field



* **Returns**

    1 if value was set, else -1



#### xiqse_set_status_polling_group_2_interval_value_and_save(value='5')
> 
> * This keyword sets the value of the Status Polling Group 2 Interval option and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Set Status Polling Group 2 Interval Value and Save  5`


> > * `XIQSE Set Status Polling Group 2 Interval Value and Save  2`


* **Parameters**

    **value** – Value to enter in the Group 2 Interval option field



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_web_server_session_timeout_and_save(value='20', units='min(s)')
> 
> * This keyword sets the value of the Web Server Session Timeout option (value and units) and saves the changes


> * Keyword Usage

> > 
> > * `XIQSE Set Web Server Session Timeout and Save  20  min(s)`
> > `XIQSE Set Web Server Session Timeout and Save   8  hr(s)`
> > `XIQSE Set Web Server Session Timeout and Save   7  day(s)`


* **Parameters**

    
    * **value** – Value to enter in the HTTP Session Timeout option field


    * **units** – time units to select for the HTTP Session Timeout option (min(s), hr(s), day(s))



* **Returns**

    1 if action was successful, else -1



#### xiqse_set_web_server_session_timeout_units(units='min(s)')
> 
> * This keyword sets the Timeout units for the Web Server HTTP Session Timeout option.


> * It is assumed the view is already navigated to the Web Server option on the Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Set Web Server Session Timeout Units  min(s)`


> > * `XIQSE Set Web Server Session Timeout Units  hr(s)`


> > * `XIQSE Set Web Server Session Timeout Units  day(s)`


* **Parameters**

    **units** – time units to select for the HTTP Session Timeout option (min(s), hr(s), day(s))



* **Returns**

    1 if value was set, else -1



#### xiqse_set_web_server_session_timeout_value(value='20')
> 
> * This keyword sets the Timeout value for the Web Server HTTP Session Timeout option.


> * It is assumed the view is already navigated to the Web Server option on the Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Set Web Server Session Timeout Value  20`


> > * `XIQSE Set Web Server Session Timeout Value  7`


* **Parameters**

    **value** – Value to enter in the HTTP Session Timeout option field



* **Returns**

    1 if value was set, else -1



#### xiqse_set_xiq_connection_enable_sharing_option(value='true')
> 
> * This keyword sets the value of the Enable Sharing field for the XIQ Connection option.


> * It is assumed the view is already navigated to the XIQ Connection option on the Administration> Options tab.


> * Keyword Usage

> > 
> > * `XIQSE Set XIQ Connection Enable Sharing Option  true`
> > `XIQSE Set XIQ Connection Enable Sharing Option  false`


* **Parameters**

    **value** – indicates whether to select (true) or deselect (false) the Enable Sharing option



* **Returns**

    1 if value was set, else -1



#### xiqse_set_xiq_connection_option_and_save(enable='true')
> 
> * This keyword sets the value of the XIQ Connection option and saves the changes


> * Keyword Usage

>     `XIQSE Set XIQ Connection Option and Save  true`
>     `XIQSE Set XIQ Connection Option and Save  false`


* **Parameters**

    **enable** – indicates whether to select (true) or deselect (false) the Enable Sharing option



* **Returns**

    1 if action was successful, else -1
