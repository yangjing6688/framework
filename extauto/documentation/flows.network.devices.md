# extauto.xiqse.flows.network.devices package

## Subpackages

## Submodules

## extauto.xiqse.flows.network.devices.XIQSE_NetworkDevices module


### _class_ extauto.xiqse.flows.network.devices.XIQSE_NetworkDevices.XIQSE_NetworkDevices()
Bases: `NetworkDevicesWebElements`


#### xiqse_devices_select_devices_tab()
> 
> * This keyword selects the Devices tab on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Devices Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_endpoint_locations_tab()
> 
> * This keyword selects the Endpoint Locations tab on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Endpoint Locations Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_flexreports_tab()
> 
> * This keyword selects the FlexReports tab on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select FlexReports Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_site_summary_tab()
> 
> * This keyword selects the Site Summary tab on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Site Summary Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_site_tab(site='World')
> 
> * This keyword selects the specified site tab on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Site Tab   ${SITE}`


* **Parameters**

    **site** – name of site tab to select (it changes name based on tree selection)



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_tab(tab_name, site='World')
> 
> * This keyword selects the specified tab of the Network> Devices page


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Tab    Devices`


> > * `XIQSE Devices Select Tab    Site Summary`


> > * `XIQSE Devices Select Tab    Endpoint Locations`


> > * `XIQSE Devices Select Tab    FlexReports`


* **Parameters**

    
    * **tab_name** – name of the sub tab to select


    * **site** – name of site tab to select, if tab to select is Site (it changes name based on tree selection)



* **Returns**

    1 if action was successful, else -1
