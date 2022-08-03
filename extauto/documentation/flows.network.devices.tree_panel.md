# extauto.xiqse.flows.network.devices.tree_panel package

## Submodules

## extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanel module


### _class_ extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanel.XIQSE_NetworkDevicesTreePanel()
Bases: `NetworkDevicesTreePanelWebElements`


#### xiqse_devices_create_site(site)
> 
> * This keyword creates the specified site on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Create Site   ${SITE}`


* **Parameters**

    **site** – name of site to create



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_delete_site(site)
> 
> * This keyword deletes the specified site from the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Delete Site   ${SITE}`


* **Parameters**

    **site** – name of site to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_device_tree_context(the_value)
> 
> * This keyword selects the device tree context in the left tree panel on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Device Tree Context   by Contact`


> > * `XIQSE Devices Select Device Tree Context   by Device Type`


> > * `XIQSE Devices Select Device Tree Context   by IP`


> > * `XIQSE Devices Select Device Tree Context   by Location`


> > * `XIQSE Devices Select Device Tree Context   Extended Bridges`


> > * `XIQSE Devices Select Device Tree Context   Sites`


> > * `XIQSE Devices Select Device Tree Context   User Device Groups`


> > * `XIQSE Devices Select Device Tree Context   Wireless Controllers`


* **Parameters**

    **the_value** – tree context to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_devices_select_site_tree_node(site)
> 
> * This keyword selects the specified site tree node on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Site Tree Node   ${SITE}`


* **Parameters**

    **site** – name of site tree node to select



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelCreateSite module


### _class_ extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelCreateSite.XIQSE_NetworkDevicesTreePanelCreateSite()
Bases: `NetworkDevicesTreePanelCreateSiteWebElements`


#### xiqse_create_site_dialog_click_cancel()
> 
> * This keyword clicks the Cancel button in the Create Site dialog.


> * It is assumed the Create Site dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Create Site Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_create_site_dialog_click_ok()
> 
> * This keyword clicks the OK button in the Create Site dialog.


> * It is assumed the Create Site dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Create Site Click OK`


* **Returns**

    1 if action was successful, else -1



#### xiqse_create_site_dialog_set_name(the_value)
> 
> * This keyword sets the Name value in the Create Site dialog.


> * It is assumed the dialog is already opened.


> * Keyword Usage

> > 
> > * `XIQSE Create Site Set Name  MySite`


* **Parameters**

    **the_value** – Name value to enter in the Create Site dialog



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelDeleteSite module


### _class_ extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelDeleteSite.XIQSE_NetworkDevicesTreePanelDeleteSite()
Bases: `NetworkDevicesTreePanelDeleteSiteWebElements`


#### xiqse_delete_site_confirm_delete()
> 
> * This keyword confirms the site deletion.


> * It is assumed the Delete Site confirmation dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Site Confirm Delete`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_site_confirm_dialog_click_no()
> 
> * This keyword clicks the No button in the Delete Site confirmation dialog.


> * It is assumed the Delete Site confirmation dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Site Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_site_confirm_dialog_click_yes()
> 
> * This keyword clicks the Yes button in the Delete Site confirmation dialog.


> * It is assumed the Delete Site confirmation dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Site Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelDeviceType module


### _class_ extauto.xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelDeviceType.XIQSE_NetworkDevicesTreePanelDeviceType()
Bases: `NetworkDevicesTreePanelDeviceTypeWebElements`


#### xiqse_select_device_type_node(device_type)
> 
> * This keyword selects the specified device type node on the Network> Devices Tab


> * Keyword Usage

> > 
> > * `XIQSE Devices Select Device Type Node   ${DEVICE_TYPE}`


* **Parameters**

    **device_type** – name of device type node to select



* **Returns**

    1 if action was successful, else -1


## Module contents
