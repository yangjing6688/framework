# extauto.xiqse.flows.control package

## extauto.xiqse.flows.control.XIQSE_Control module


### _class_ extauto.xiqse.flows.control.XIQSE_Control.XIQSE_Control()
Bases: `ControlWebElements`


#### xiqse_control_select_access_control_tab()
> 
> * This keyword selects the Access Control tab of the Control page


> * Keyword Usage

> > 
> > * `XIQSE Control Select Access Control Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_select_dashboard_tab()
> 
> * This keyword selects the Dashboard tab of the Control page


> * Keyword Usage

> > 
> > * `XIQSE Control Select Dashboard Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_select_end_systems_tab()
> 
> * This keyword selects the End Systems tab of the Control page


> * Keyword Usage

> > 
> > * `XIQSE Control Select End systems Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_select_policy_tab()
> 
> * This keyword selects the Policy tab of the Control page


> * Keyword Usage

> > 
> > * `XIQSE Control Select Policy Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_select_reports_tab()
> 
> * This keyword selects the Reports tab of the Control page


> * Keyword Usage

> > 
> > * `XIQSE Control Select Reports Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Control page


> * Keyword Usage

> > 
> > * `XIQSE Control Select Tab    Dashboard`


> > * `XIQSE Control Select Tab    Policy`


> > * `XIQSE Control Select Tab    Access Control`


> > * `XIQSE Control Select Tab    End-Systems`


> > * `XIQSE Control Select Tab    Reports`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_control_select_title_header(title)
> 
> * This keyword selects the title header on the Control> Policy or Access Control tab.


> * You need to be in the correct page (i.e. Policy or Access Control) to use this keyword.


> * Keyword Usage

> > 
> > * `XIQSE Control Select Title Header   ${TITLE Header}`


> > * Examples:

> >     For Policy,

> >         XIQSE Control Select Title Header     Roles/Services
> >         XIQSE Control Select Title Header     Class of Service
> >         XIQSE Control Select Title Header     VLANs
> >         XIQSE Control Select Title Header     Network Resources
> >         XIQSE Control Select Title Header     Devices/Port Groups

> >     For Access Control

> >         XIQSE Control Select Title Header     Configuration
> >         XIQSE Control Select Title Header     Group Editor
> >         XIQSE Control Select Title Header     Engines


* **Returns**

    1 if action was successful, else -1
