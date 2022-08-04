# extauto.xiqse.flows.network.devices.site.vrf_vlan package

## Submodules

## extauto.xiqse.flows.network.devices.site.vrf_vlan.XIQSE_NetworkDevicesSiteVrfVlan module


### _class_ extauto.xiqse.flows.network.devices.site.vrf_vlan.XIQSE_NetworkDevicesSiteVrfVlan.XIQSE_NetworkDevicesSiteVrfVlan()
Bases: `NetworkDevicesSiteVrfVlanWebElements`


#### xiqse_site_cancel_vlan()
> 
> * This keyword clicks Cancel in the VLAN row editor.


> * It is assumed the VLAN row editor is open.


> * Keyword Usage

> > 
> > * `XIQSE Site Cancel VLAN`


* **Returns**

    1 if action was successful, else -1



#### xiqse_site_create_vlan(name, vid='2')
> 
> * This keyword creates a new VLAN in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Site Create VLAN  test_vlan_1`


> > * 

> > ```
> > ``
> > ```

> > XIQSE Site Create VLAN  test_vlan_1  2 \`\`


* **Parameters**

    
    * **name** – value to enter in the VLAN Name field


    * **id** – value to select for the VLAN VID field



* **Returns**

    1 if action was successful, else -1


## Module contents
