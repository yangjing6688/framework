# extauto.xiqse.flows.network.devices.site package

## Subpackages

## Submodules

## extauto.xiqse.flows.network.devices.site.XIQSE_NetworkDevicesSite module


### _class_ extauto.xiqse.flows.network.devices.site.XIQSE_NetworkDevicesSite.XIQSE_NetworkDevicesSite()
Bases: `NetworkDevicesSiteWebElements`


#### xiqse_site_cancel_changes()
> 
> * This keyword cancels the changes on the Site tab.


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Cancel Changes`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_click_cancel()
> 
> * This keyword clicks the Cancel button on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_click_discover()
> 
> * This keyword clicks the Discover button on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Click Discover`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_click_save()
> 
> * This keyword clicks the Save button on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Click Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_perform_ip_range_discovery(ip_start, ip_end, profile_names, auto_add='true', trap='false', syslog='false', archive='false')
> 
> * This keyword configures and performs an IP range discovery.


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Perform IP Range Discovery  1.1.1.1  1.1.1.5  public_v1_Profile  true  true  true  true`


> > * 

> > ```
> > ``
> > ```

> > XIQSE Site Perform IP Range Discovery  2.2.2.1  2.2.2.250  public_v1_Profile,public_v2_Profile’’


* **Parameters**

    
    * **ip_start** – IP starting value to use in the discovery


    * **ip_end** – IP ending value to use in the discovery


    * **profile_names** – comma-separated list of profile names to use in the discovery


    * **auto_add** – specifies value of Automatically Add Devices checkbox on the Actions tab  (true/false)


    * **trap** – specifies value of Add Trap Receiver checkbox on the Actions tab  (true/false)


    * **syslog** – specifies value of Add Syslog Receiver checkbox on the Actions tab  (true/false)


    * **archive** – specifies value of Add to Archive checkbox on the Actions tab  (true/false)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_perform_seed_discovery(seed_address, profile_names, auto_add='true', trap='false', syslog='false', archive='false')
> 
> * This keyword configures and performs a seed discovery.


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Perform Seed Discovery  1.1.1.1  public_v1_Profile  true  true  true  true`


> > * 

> > ```
> > ``
> > ```

> > XIQSE Site Perform Seed Discovery  2.2.2.1  public_v1_Profile,public_v2_Profile’’


* **Parameters**

    
    * **seed_address** – IP address to use in the discovery


    * **profile_names** – comma-separated list of profile names to use in the discovery


    * **auto_add** – specifies value of Automatically Add Devices checkbox on the Actions tab  (true/false)


    * **trap** – specifies value of Add Trap Receiver checkbox on the Actions tab  (true/false)


    * **syslog** – specifies value of Add Syslog Receiver checkbox on the Actions tab  (true/false)


    * **archive** – specifies value of Add to Archive checkbox on the Actions tab  (true/false)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_perform_subnet_discovery(subnet_values, profile_names, auto_add='true', trap='false', syslog='false', archive='false')
> 
> * This keyword configures and performs a subnet discovery.


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Perform Subnet Discovery  1.1.1.1/24  public_v1_Profile  true  true  true  true`


> > * `XIQSE Site Perform Subnet Discovery  1.1.1.1/24,2.2.2.1/24  public_v1_Profile,public_v2_Profile`


* **Parameters**

    
    * **subnet_values** – comma-separated list of subnet/mask values to use in the discovery


    * **profile_names** – comma-separated list of profile names to use in the discovery


    * **auto_add** – specifies value of Automatically Add Devices checkbox on the Actions tab  (true/false)


    * **trap** – specifies value of Add Trap Receiver checkbox on the Actions tab  (true/false)


    * **syslog** – specifies value of Add Syslog Receiver checkbox on the Actions tab  (true/false)


    * **archive** – specifies value of Add to Archive checkbox on the Actions tab  (true/false)



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_save_changes()
> 
> * This keyword saves the changes on the Site tab.


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Save Changes`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_actions_tab()
> 
> * This keyword selects the Actions tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Actions Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_analytics_tab()
> 
> * This keyword selects the Analytics tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Analytics Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_custom_variables_tab()
> 
> * This keyword selects the Custom Variables tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Custom Variables Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_discover_tab()
> 
> * This keyword selects the Discover tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Discover Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_endpoint_locations_tab()
> 
> * This keyword selects the Endpoint Locations tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Endpoint Locations Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_port_templates_tab()
> 
> * This keyword selects the Port Templates tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Port Templates Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_services_tab()
> 
> * This keyword selects the Services tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Services Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Network> Devices> Site page


> * Keyword Usage

> > 
> > * `XIQSE Site Select Tab    Discover`


> > * `XIQSE Site Select Tab    Actions`


> > * `XIQSE Site Select Tab    VRF/VLAN`


> > * `XIQSE Site Select Tab    Topologies`


> > * `XIQSE Site Select Tab    Services`


> > * `XIQSE Site Select Tab    Port Templates`


> > * `XIQSE Site Select Tab    ZTP+ Device Defaults`


> > * `XIQSE Site Select Tab    Endpoint Locations`


> > * `XIQSE Site Select Tab    Analytics`


> > * `XIQSE Site Select Tab    Custom Variables`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_topologies_tab()
> 
> * This keyword selects the Topologies tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select Topologies Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_vrf_vlan_tab()
> 
> * This keyword selects the VRF/VLAN tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select VRF/VLAN Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_select_ztp_device_defaults_tab()
> 
> * This keyword selects the ZTP+ Device Defaults tab on the Network> Devices> Site Tab


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Site Select ZTP Device Defaults Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_unsaved_changes_dialog(the_answer='No')
> 
> * This keyword clicks the Yes, No, or Cancel button in the ‘Site - Unsaved Changes’ dialog.


> * This panel is displayed when moving away from a site that has unsaved changes.


> * Keyword Usage

> > 
> > * `XIQSE Site Unsaved Changes Dialog    No`


* **Parameters**

    **the_answer** – Specifies how to answer the question in the dialog - Yes, No, or Cancel



* **Returns**

    1 if action was successful, 2 if dialog was not displayed, else -1



#### xiqse_site_unsaved_changes_dialog_click_cancel()
> 
> * This keyword clicks ‘Cancel’ in the ‘Site - Unsaved Changes’ dialog panel.


> * This panel is displayed when moving away from a site that has unsaved changes.


> * It is assumed the ‘Site - Unsaved Changes’ dialog panel is already open.


> * Keyword Usage

> > 
> > * `XIQSE Site Unsaved Changes Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_unsaved_changes_dialog_click_no()
> 
> * This keyword clicks ‘No’ in the ‘Site - Unsaved Changes’ dialog panel.


> * This panel is displayed when moving away from a site that has unsaved changes.


> * It is assumed the ‘Site - Unsaved Changes’ dialog panel is already open.


> * Keyword Usage

> > 
> > * `XIQSE Site Unsaved Changes Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_unsaved_changes_dialog_click_yes()
> 
> * This keyword clicks ‘Yes’ in the ‘Site - Unsaved Changes’ dialog panel.


> * This panel is displayed when moving away from a site that has unsaved changes.


> * It is assumed the ‘Site - Unsaved Changes’ dialog panel is already open.


> * Keyword Usage

> > 
> > * `XIQSE Site Unsaved Changes Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_wait_until_discovery_complete(retry_duration=30, retry_count=10)
> 
> * This keyword waits until the discovery has completed by checking the Discover Site entry in the


> * Operations panel for progress value of 100%.


> * It is assumed the view is already navigated to the Site tab.


> * Keyword Usage

> > 
> > * `XIQSE Wait Until Discovery Complete`


> > * `XIQSE Wait Until Discovery Complete    retry_duration=10  retry_count=60`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if action was successful, else -1


## Module contents
