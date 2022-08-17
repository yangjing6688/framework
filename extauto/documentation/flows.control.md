# extauto.xiqse.flows.control package

## Subpackages


* [extauto.xiqse.flows.control.access_control package](flows.control.access_control.md)


    * [extauto.xiqse.flows.control.access_control.XIQSE_AccessControlAddRemove module](flows.control.access_control.md#module-extauto.xiqse.flows.control.access_control.XIQSE_AccessControlAddRemove)


    * [extauto.xiqse.flows.control.access_control.XIQSE_AccessControlCommon module](flows.control.access_control.md#module-extauto.xiqse.flows.control.access_control.XIQSE_AccessControlCommon)


    * [extauto.xiqse.flows.control.access_control.XIQSE_AccessControlEnforce module](flows.control.access_control.md#module-extauto.xiqse.flows.control.access_control.XIQSE_AccessControlEnforce)


    * [extauto.xiqse.flows.control.access_control.XIQSE_AccessControlPanel module](flows.control.access_control.md#module-extauto.xiqse.flows.control.access_control.XIQSE_AccessControlPanel)


    * [extauto.xiqse.flows.control.access_control.XIQSE_AccessControlTree module](flows.control.access_control.md#module-extauto.xiqse.flows.control.access_control.XIQSE_AccessControlTree)


* [extauto.xiqse.flows.control.dashboard package](flows.control.dashboard.md)


    * [extauto.xiqse.flows.control.dashboard.XIQSE_ControlDashboard module](flows.control.dashboard.md#module-extauto.xiqse.flows.control.dashboard.XIQSE_ControlDashboard)


* [extauto.xiqse.flows.control.end_systems package](flows.control.end_systems.md)


* [extauto.xiqse.flows.control.policy package](flows.control.policy.md)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicy module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicy)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomain module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomain)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainAssignDevice module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainAssignDevice)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainCreate module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainCreate)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainDelete module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainDelete)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforce module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforce)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforcePreview module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforcePreview)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpen module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpen)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainVerify module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainVerify)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRole module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRole)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRule module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRule)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleCreate module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleCreate)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleDelete module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleDelete)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyService module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyService)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceCreate module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceCreate)


    * [extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceDelete module](flows.control.policy.md#module-extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceDelete)


* [extauto.xiqse.flows.control.reports package](flows.control.reports.md)


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
