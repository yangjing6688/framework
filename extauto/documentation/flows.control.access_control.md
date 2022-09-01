# extauto.xiqse.flows.control.access_control package

## extauto.xiqse.flows.control.access_control.XIQSE_AccessControlAddRemove module


### _class_ extauto.xiqse.flows.control.access_control.XIQSE_AccessControlAddRemove.XIQSE_AccessControlAddRemove()
Bases: `ControlAccessControlAddRemoveWebElements`


#### xiqse_add_nac_appliance(ip_addr)
> 
> * This keyword adds NAC appliance via Control> Access Control Tab


> * Keyword Usage

> > 
> > * XIQSE ADD NAC APPLIANCE     {nac_appliance_ip1}


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_nac_appliance(nacip)
> 
> * This keyword deletes NAC appliance via Control> Access Control Tab


> * This keyword assumes that you already selected the All Engines in the tree


> * Select a row for NAC appliance and then hit Delete.


> * Keyword Usage

> > 
> > * XIQSE Delete NAC APPLIANCE     {nac_appliance_ip1}


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.access_control.XIQSE_AccessControlCommon module


### _class_ extauto.xiqse.flows.control.access_control.XIQSE_AccessControlCommon.XIQSE_AccessControlCommon()
Bases: `ControlAccessControlCommonWebElements`


#### xiqse_control_click_button(buttonname)
This is a general keyword in NAC to click on a button within Dialog.
This is using data-ref=”btnInnerEl” with Button Name
- Keyword Usage

> XIQSE CONTROL CLICK BUTTON  Close


* **Returns**

    XXX if action was successful, else -1



#### xiqse_control_select_tab_inpanel(tabpanel)
This is a general keyword in Access Control to click on a tab within panel.
- Keyword Usage

> XIQSE CONTROL SELECT TAB INPANEL  Switches
> XIQSE CONTROL SELECT TAB INPANEL  End-Systems
> XIQSE CONTROL SELECT TAB INPANEL  Details


* **Returns**

    XXX if action was successful, else -1


## extauto.xiqse.flows.control.access_control.XIQSE_AccessControlEnforce module


### _class_ extauto.xiqse.flows.control.access_control.XIQSE_AccessControlEnforce.XIQSE_AccessControlEnforce()
Bases: `ControlAccessControlEnforceWebElements`


#### xiqse_expand_control_enforce_dropdown()
This is a keyword to expand the dropdown menu in Control Access Control page
- Keyword Usage

> XIQSE EXPAND CONTROL ENFORCE DROPDOWN


* **Returns**

    XXX if action was successful, else -1



#### xiqse_select_control_enforce_dropdown_menu(combomenu)
This is a keyword to select the dropdown menu in Control Access Control page
- Keyword Usage

> XIQSE EXPAND CONTROL ENFORCE DROPDOWN   All…


* **Returns**

    XXX if action was successful, else -1


## extauto.xiqse.flows.control.access_control.XIQSE_AccessControlPanel module


### _class_ extauto.xiqse.flows.control.access_control.XIQSE_AccessControlPanel.XIQSE_AccessControlPanel()
Bases: `ControlAccessControlPanelWebElements`


#### is_xiqse_nac_license_valid()

#### is_xiqse_nac_unlicensed()

#### xiqse_get_nac_status()
> 
> * This keyword gets NAC status via Control> Access Control Tab


> * First you will need to select the NAC appliance in the tree node.


> * This keyword returns a status in text format (i.e. OK, Not Reachable and etc)


> * Keyword Usage

> > 
> > * XIQSE GET NAC STATUS


* **Returns**

    nac status text if action was successful, else None



#### xiqse_get_nac_status_in_panel()
> 
> * This keyword gets NAC status via Control> Access Control Tab


> * First you will need to select the NAC appliance in the tree node


> * If NAC status shows ‘OK’, the keyword is successful and return 1.


> * Keyword Usage

> > 
> > * XIQSE GET NAC STATUS IN PANEL


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.access_control.XIQSE_AccessControlTree module


### _class_ extauto.xiqse.flows.control.access_control.XIQSE_AccessControlTree.XIQSE_AccessControlTree()
Bases: `ControlAccessControlTreeWebElements`


#### xiqse_control_select_engines_tree_node(treenode)
> 
> * This keyword selects the specified tree node on the Control> Access Control Tab


> * Keyword Usage

> > 
> > * `XIQSE Control Select Engines Tree Node   ${TREENODE}`


* **Returns**

    1 if action was successful, else -1
