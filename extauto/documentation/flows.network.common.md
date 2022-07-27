# extauto.xiqse.flows.network.common package

## extauto.xiqse.flows.network.common.XIQSE_NetworkCommonConfigureDevice module


### _class_ extauto.xiqse.flows.network.common.XIQSE_NetworkCommonConfigureDevice.XIQSE_NetworkCommonConfigureDevice()
Bases: `NetworkCommonConfigureDeviceWebElements`


#### xiqse_configure_device_dialog_click_cancel()

* This keyword clicks Cancel in the Configure Device dialog.


* It assumes the dialog is already open.


* Keyword Usage:

> 
> * `XIQSE Configure Device Dialog Click Cancel`


* **Returns**

    1 if action is successful, else -1



#### xiqse_configure_device_dialog_click_save()

* This keyword clicks Save in the Configure Device dialog.


* It assumes the dialog is already open.


* Keyword Usage:

> 
> * `XIQSE Configure Device Dialog Click Save`


* **Returns**

    1 if action is successful, else -1



#### xiqse_configure_device_dialog_select_tab(tab_name)

* This keyword selects the specified tab in the Configure Device dialog.


* It assumes the dialog is already open.


* Keyword Usage:

> 
> * `XIQSE Configure Device Dialog Select Tab    Device`


> * `XIQSE Configure Device Dialog Select Tab    Device Annotation`


> * `XIQSE Configure Device Dialog Select Tab    VLAN Definitions`


> * `XIQSE Configure Device Dialog Select Tab    Ports`


> * `XIQSE Configure Device Dialog Select Tab    ZTP+ Device Settings`


> * `XIQSE Configure Device Dialog Select Tab    Vendor Profile`


* **Parameters**

    **tab_name** – Name of the tab to select in the Configure Device dialog



* **Returns**

    1 if action is successful, else -1
