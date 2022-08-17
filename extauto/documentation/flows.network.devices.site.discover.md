# extauto.xiqse.flows.network.devices.site.discover package

## Submodules

## extauto.xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscover module


### _class_ extauto.xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscover.XIQSE_NetworkDevicesSiteDiscover()
Bases: `NetworkDevicesSiteDiscoverWebElements`


#### xiqse_discover_addresses_add_address_range(start_address, end_address)
> 
> * This keyword adds the specified address range on the Network> Devices> Site> Discover Tab.


> * It is assumed the view is currently navigated to the Discover tab.


> * Keyword Usage

> > 
> > * 

> > ```
> > ``
> > ```

> > XIQSE Discover Add Address Range   1.2.3.1    1.2.3.255\`


* **Parameters**

    
    * **start_address** – value to enter for the starting IP address range


    * **end_address** – value to enter for the ending IP address range



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_add_seed_address(seed_address)
> 
> * This keyword adds the specified seed address on the Network> Devices> Site> Discover Tab.


> * It is assumed the view is currently navigated to the Discover tab.


> * Keyword Usage

> > 
> > * 

> > ```
> > ``
> > ```

> > XIQSE Discover Addresses Add Seed Address   1.2.3.4\`


* **Parameters**

    **seed_address** – seed address to enter



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_add_subnet(subnet_mask)
> 
> * This keyword adds the specified subnet address on the Network> Devices> Site> Discover Tab.


> * It is assumed the view is currently navigated to the Discover tab.


> * Keyword Usage

> > 
> > * 

> > ```
> > ``
> > ```

> > XIQSE Discover Addresses Add Subnet   1.2.3.4/24\`


* **Parameters**

    **subnet_mask** – subnet/mask value to enter



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_delete_address_range(start_address, end_address)
> 
> * This keyword selects the specified address range in the Addresses panel and clicks the Delete toolbar button.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Addresses Delete Address Range    1.2.3.4    1.2.3.5`


* **Parameters**

    
    * **start_address** – value of the starting IP address range to delete


    * **end_address** – value of the ending IP address range to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_delete_seed_address(seed_address)
> 
> * This keyword selects the specified seed address in the Addresses panel and clicks the Delete toolbar button.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Addresses Delete Seed Address    1.2.3.4`


* **Parameters**

    **seed_address** – value of the seed address to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_delete_subnet(subnet_mask)
> 
> * This keyword selects the specified subnet/mask in the Addresses panel and clicks the Delete toolbar button.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Addresses Delete Seed Address    1.2.3.4`


* **Parameters**

    **subnet_mask** – value of the subnet/mask to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_select_address_range(start_address, end_address)
> 
> * This keyword selects the specified address range in the Addresses panel.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Addresses Select Address Range    1.2.3.4    1.2.3.5`


* **Parameters**

    
    * **start_address** – value of the starting IP address range to select


    * **end_address** – value of the ending IP address range to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_select_seed_address(seed_address)
> 
> * This keyword selects the specified seed address in the Addresses panel.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Addresses Select Seed Address    1.2.3.4`


* **Parameters**

    **seed_address** – value of the seed address to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_addresses_select_subnet(subnet_mask)
> 
> * This keyword selects the specified subnet address in the Addresses panel.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Addresses Select Subnet    1.2.3.1/24`


* **Parameters**

    **subnet_mask** – value of the subnet/mask to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_clear_all_profile_selections()

* This keyword clears the selected state of the Accept and Reject columns for all profiles in the Profiles panel.


* It is assumed the Site> Discover tab is visible.


* Keyword Usage

> 
> * `XIQSE Discover Clear All Profile Selections`


#### xiqse_discover_click_add_address_button()
> 
> * This keyword clicks the Add button in the Addresses panel on the Network> Devices> Site> Discover Tab


> * It is assumed the view is already navigated to the Discover tab.


> * Keyword Usage

> > 
> > * `XIQSE Discover Click Add Address Button`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_delete_selected_address()
> 
> * This keyword deletes the currently-selected address in the Addresses panel.


> * It is assumed the Site> Discover tab is visible and the address entry to delete is selected.


> * Keyword Usage

> > 
> > * `XIQSE Discover Delete Selected Address`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_set_accept_profile(profile_name, accept_val='true')
> 
> * This keyword sets the selected state of the Accept column for the specified profile in the Profiles panel.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Set Accept Profile  public_v1_Profile  true`


> > * `XIQSE Discover Set Accept Profile  public_v2_Profile  false`


* **Parameters**

    
    * **profile_name** – name of the profile to mark


    * **accept_val** – indicates whether to select or deselect the Accept check box



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_set_reject_profile(profile_name, reject_val='true')
> 
> * This keyword checks the Reject column for the specified profile in the Profiles panel.


> * It is assumed the Site> Discover tab is visible.


> * Keyword Usage

> > 
> > * `XIQSE Discover Set Reject Profile  public_v1_Profile  true`


> > * `XIQSE Discover Set Reject Profile  public_v2_Profile  false`


* **Parameters**

    
    * **profile_name** – name of the profile to mark


    * **reject_val** – indicates whether to select or deselect the Reject check box



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscoverAddAddress module


### _class_ extauto.xiqse.flows.network.devices.site.discover.XIQSE_NetworkDevicesSiteDiscoverAddAddress.XIQSE_NetworkDevicesSiteDiscoverAddAddress()
Bases: `NetworkDevicesSiteDiscoverAddAddressWebElements`


#### xiqse_discover_add_address_dialog_click_cancel()
> 
> * This keyword clicks the Cancel button in the Add Address dialog.


> * It is assumed the Add Address dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_click_ok()
> 
> * This keyword clicks the OK button in the Add Address dialog.


> * It is assumed the Add Address dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Click OK`


* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_select_type(type)
> 
> * This keyword selects the Discover Type in the Add Address dialog.


> * It is assumed the Add Address dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Select Type    Address Range`


> > * `XIQSE Discover Add Address Dialog Select Type    Seed Address`


> > * `XIQSE Discover Add Address Dialog Select Type    Subnet`


* **Parameters**

    **type** – value to select in the Discover Type dropdown (Address Range, Seed Address, Subnet)



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_set_address_range(start_val, end_val)
> 
> * This keyword sets the Start Address and End Address values in the Add Address dialog.


> * It is assumed the dialog is already opened and on the Address Range discover type.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Set Address Range  ${START_IP}  ${END_IP}`


* **Parameters**

    
    * **start_val** – Start Address value to enter in the Add Address dialog


    * **end_val** – End Address value to enter in the Add Address dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_set_end_address(the_val)
> 
> * This keyword sets the End Address value in the Add Address dialog.


> * It is assumed the dialog is already opened and on the Address Range discover type.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Set End Address  ${END_IP}`


* **Parameters**

    **the_val** – End Address value to enter in the Add Address dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_set_seed_address(the_val)
> 
> * This keyword sets the Seed Address value in the Add Address dialog.


> * It is assumed the dialog is already opened and on the Seed Address discover type.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Set Seed Address  ${SEED_IP}`


* **Parameters**

    **the_val** – Seed Address value to enter in the Add Address dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_set_start_address(the_val)
> 
> * This keyword sets the Start Address value in the Add Address dialog.


> * It is assumed the dialog is already opened and on the Address Range discover type.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Set Start Address  ${START_IP}`


* **Parameters**

    **the_val** – Start Address value to enter in the Add Address dialog



* **Returns**

    1 if action was successful, else -1



#### xiqse_discover_add_address_dialog_set_subnet_mask(the_val)
> 
> * This keyword sets the Subnet/Mask value in the Add Address dialog.


> * It is assumed the dialog is already opened and on the Subnet discover type.


> * Keyword Usage

> > 
> > * `XIQSE Discover Add Address Dialog Set Subnet Mask  ${Subnet/Mask}`


* **Parameters**

    **the_val** – Subnet/Mask value to enter in the Add Address dialog



* **Returns**

    1 if action was successful, else -1


## Module contents
