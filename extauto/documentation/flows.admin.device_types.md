# extauto.xiqse.flows.admin.device_types package

## extauto.xiqse.flows.admin.device_types.XIQSE_AdminDeviceTypes module


### _class_ extauto.xiqse.flows.admin.device_types.XIQSE_AdminDeviceTypes.XIQSE_AdminDeviceTypes()
Bases: `AdminDeviceTypesWebElements`


#### xiqse_device_types_select_detection_and_profiling_tab()
> 
> * This keyword selects the Detection and Profiling tab on the Administration> Device Types page.


> * It is assumed the Administration> Device Types page is currently being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Device Types Select Detection and Profiling Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_device_types_select_mac_oui_vendors_tab()
> 
> * This keyword selects the MAC OUI Vendors tab on the Administration> Device Types page.


> * It is assumed the Administration> Device Types page is currently being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Device Types Select MAC OUI Vendors Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_device_types_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Administration> Device Types page


> * Keyword Usage

> > 
> > * `XIQSE Device Types Select Tab    Detection and Profiling`


> > * `XIQSE Device Types Select Tab    MAC OUI Vendors`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1
