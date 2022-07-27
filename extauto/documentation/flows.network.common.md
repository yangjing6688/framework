# extauto.xiqse.flows.network.common package

## Subpackages


* [extauto.xiqse.flows.network.common.configure_device package](flows.network.common.configure_device.md)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceActions module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceactions-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceAnnotations module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceannotations-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceClipAddresses module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceclipaddresses-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceDevice module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredevicedevice-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceImportSiteConfig module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceimportsiteconfig-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceLags module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredevicelags-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDevicePorts module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceports-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceServices module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceservices-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceTopology module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredevicetopology-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceVendorProfile module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredevicevendorprofile-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceVlan module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredevicevlan-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceVrf module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredevicevrf-module)


    * [extauto.xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceZtpPlus module](flows.network.common.configure_device.md#extauto-xiqse-flows-network-common-configure-device-xiqse-networkcommonconfiguredeviceztpplus-module)


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
