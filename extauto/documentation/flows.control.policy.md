# extauto.xiqse.flows.control.policy package

## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicy module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicy.XIQSE_ControlPolicy()
Bases: `ControlPolicyWebElements`


#### xiqse_control_policy_dismiss_cached_window()
> 
> * This keyword dismisses the “Cached Policy Domain - Unsaved Changes” window, if present


> * Keyword Usage

> > 
> > * 

> > ```
> > ``
> > ```

> > XIQSE Control Policy Dismiss Cached Window

:param none
:return: 1 if action was successful, else -1


#### xiqse_control_policy_select_tab(tab_name)

#### xiqse_control_policy_select_tree_node(node_name)
> 
> * This keyword selects the specified tab in the main navigation panel


> * Keyword Usage

> > 
> > * `XIQSE Policy Tree Node Select    Roles`


* **Parameters**

    **node_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomain module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomain.XIQSE_ControlPolicyDomain()
Bases: `ControlPolicyDomainWebElements`


#### xiqse_select_assign_devices_to_domain_menu()
> 
> * This keyword selects the “Assign Device(s) to Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Assign Device(s) to Domain window.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select assign devices to domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_create_domain_menu()
> 
> * This keyword selects the “Create Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Create Domain window.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select save domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_delete_domain_menu()
> 
> * This keyword selects the “Delete Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Delete Domain window.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select save domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_enforce_domain_menu()
> 
> * This keyword selects the “Enforce Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and starts the Enforce Domain process.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select enforce domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_enforce_preview_menu()
> 
> * This keyword selects the “Enforce Preview” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Enforce Preview window


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select enforce preview menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_lock_domain_menu()
> 
> * This keyword selects the “Lock Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select lock domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_open_domain_menu()
> 
> * This keyword selects the “Open Domain” menu. This will activate the secondary dropdown menu with a list


> * of policy domains that have already been created.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select open domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_openmanage_domains()
> 
> * This keyword selects the “Open/Manage Domain(s)” and display its dropdown menu


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select openmanage domains


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_save_domain_menu()
> 
> * This keyword selects the “Save Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and starts the Save Domain action.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select save domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_select_verify_domain_menu()
> 
> * This keyword selects the “Verify Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and starts the Verify Domain action


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select verify domain menu


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainAssignDevice module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainAssignDevice.XIQSE_ControlPolicyDomainAssignDevice()
Bases: `ControlPolicyDomainAssignDeviceWebElements`


#### xiqse_control_policy_assign_device_to_domain(device_ip)
> 
> * This keyword adds a device to the current policy domain


> * It is assumed that:


> * the Assign Device(s) to Domain window is already open. This window can be launched from either the


> * Open/Manage Domains menu, or popup menu from the Devices tree view.


> * the device is already created on XIQ-SE,


> * the Devices tree displays the devices with IP addresses (not nickname nor sysName)


> * Keyword Usage


> * xiqse control policy assign device to domain    <device_ip>


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainCreate module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainCreate.XIQSE_ControlPolicyDomainCreate()
Bases: `ControlPolicyDomainCreateWebElements`


#### xiqse_control_policy_create_domain(domain_name)
> 
> * This keyword selects the “Create Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and create a new policy domain


> * NOTE:  If the domain exists, then it will get deleted and then re-created.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse control policy create domain      <domain_name>


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainDelete module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainDelete.XIQSE_ControlPolicyDomainDelete()
Bases: `ControlPolicyDomainDeleteWebElements`


#### xiqse_control_policy_delete_domain(domain_name)
> 
> * This keyword selects the “Delete Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and delete the specified policy domain


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse control policy delete domain      <domain_name>


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforce module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforce.XIQSE_ControlPolicyDomainEnforce()
Bases: `ControlPolicyDomainEnforceWebElements`


#### xiqse_control_policy_enforce_domain()
> 
> * This keyword performs Enforce Domain action.


> * It is assumed that:


> * the current view is Control>Policy,


> * the Enforce action is initiated by the user, from one of these places on Policy Mgr view:


> * 
>     * Open/Manage Domain(s) dropdown menu


> * 
>     * popup menu from a device


> * 
>     * dropdown menu from the lower-left corner


> * the device(s) is already added to the current policy domain,


> * NOTE: On every automation run, Enforce Preview window is always launched during the Enforce, even though

>     I uncheck the “Show on Enforce” checkbox in the Enforce Preview window before the automation starts.


> * Keyword Usage


> * xiqse control policy enforce domain


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforcePreview module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainEnforcePreview.XIQSE_ControlPolicyDomainEnforcePreview()
Bases: `ControlPolicyDomainEnforcePreviewWebElements`


#### click_enforce_button()

* Click the “Enforce” button.


* **Returns**

    1 if button is clicked, else -1



#### xiqse_control_policy_enforce_preview_show_on_enforce_setting()

* Check for the “Show on enforce” checkbox setting:


* checked = show Enforce Preview window during the Enforce Domain process


* not-checked = do NOT show the Enforce Preview window during the Enforce Domain process


* NOTE: it looks like the checkbox is always checked every time XIQ-SE client is launched by the automation.


* I tried to uncheck it, and it is still checked on the next launch.


* this checkbox setting is per user, and it looks like automation uses a new-user for every launch.


* **Returns**

    1 if checkbox is checked.  -1 if checkbox is not checked


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpen module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpen.XIQSE_ControlPolicyDomainOpen()
Bases: `ControlPolicyDomainOpenWebElements`


#### xiqse_control_policy_domain_exists(domain_name)
> 
> * This keyword checks if a domain exists in the Policy Manager database


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse control policy domain exists      <domain_name>


* **Returns**

    1 if domain exists, else -1



#### xiqse_control_policy_open_domain(domain_name)
> 
> * This keyword opens an existing domain, if exists


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse control policy open domain      <domain_name>


* **Returns**

    1 if domain is open successfully, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainOpenManageMenu.XIQSE_ControlPolicyDomainOpenManageMenu()
Bases: `ControlPolicyDomainOpenManageMenuWebElements`


#### xiqse_control_policy_select_assign_devices_to_domain_menu()
> 
> * This keyword selects the “Assign Device(s) to Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Assign Device(s) to Domain window.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select assign devices to domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_create_domain_menu()
> 
> * This keyword selects the “Create Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Create Domain window.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select save domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_delete_domain_menu()
> 
> * This keyword selects the “Delete Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Delete Domain window.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select save domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_enforce_domain_menu()
> 
> * This keyword selects the “Enforce Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and starts the Enforce Domain process.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select enforce domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_enforce_preview_menu()
> 
> * This keyword selects the “Enforce Preview” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and launches the Enforce Preview window


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select enforce preview menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_lock_domain_menu()
> 
> * This keyword selects the “Lock Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select lock domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_open_domain_menu()
> 
> * This keyword selects the “Open Domain” menu. This will activate the secondary dropdown menu with a list


> * of policy domains that have already been created.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select open domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_openmanage_domains()
> 
> * This keyword selects the “Open/Manage Domain(s)” and display its dropdown menu


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select openmanage domains


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_save_domain_menu()
> 
> * This keyword selects the “Save Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and starts the Save Domain action.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select save domain menu


* **Returns**

    1 if action was successful, else -1



#### xiqse_control_policy_select_verify_domain_menu()
> 
> * This keyword selects the “Verify Domain” menu option from the “Open/Manage Domain(s)” dropdown menu


> * and starts the Verify Domain action


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse select verify domain menu


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainSave.XIQSE_ControlPolicyDomainSave()
Bases: `ControlPolicyDomainSaveWebElements`


#### xiqse_control_policy_save_domain()
> 
> * This keyword saves the current domain by selecting “Save Domain” menu from “Open/Manage Domain(s)”

>     dropdown menu and goes through the save domain process.


> * It is assumed that the current view is Control>Policy.


> * Keyword Usage


> * xiqse control policy save domain


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainVerify module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyDomainVerify.XIQSE_ControlPolicyDomainVerify()
Bases: `ControlPolicyDomainVerifyWebElements`


#### xiqse_control_policy_verify_domain()
> 
> * This keyword performs Verify Domain action.


> * It is assumed that:


> * the current view is Control>Policy,


> * the Verify action is initiated by the user, from one of these places on Policy Mgr view:


> * 
>     * Open/Manage Domain(s) dropdown menu


> * 
>     * popup menu from a device


> * 
>     * dropdown menu from the lower-left corner


> * the device(s) is already added to the current policy domain,


> * Keyword Usage


> * xiqse control policy verify domain


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRole module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRole.XIQSE_ControlPolicyRole()
Bases: `ControlPolicyRoleDetailsWebElements`


#### xiqse_control_policy_create_role(name)

#### xiqse_control_policy_delete_role(name)
## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRule module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRule.XIQSE_ControlPolicyRule()
Bases: `ControlPolicyRuleDetailsWebElements`

## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleCreate module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleCreate.XIQSE_ControlPolicyRuleCreate()
Bases: `ControlPolicyRuleCreateWebElements`


#### xiqse_control_policy_create_rule(rule_name, service_name, service_type='local')

* This keyword creates a rule (local or global). Users need to specify which service the rule is in.


* IMPORTANT NOTE:


* I think accessing tree nodes (e.g. select, right-click, expand, etc) in Roles/Services/Rules trees are the same.


* Since I already have the methods created in Service files, I use them to access the rule nodes for now.


* These methods can be rolled up to the ControlPolicy level, if time allows.


* **Parameters**

    
    * **rule_name** – 


    * **service_name** – 


    * **service_type** – local or global



* **Returns**

    1 if success, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleDelete module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyRuleDelete.XIQSE_ControlPolicyRuleDelete()
Bases: `ControlPolicyRuleDeleteWebElements`


#### xiqse_control_policy_delete_rule(rule_name, service_name, service_type='local')

* This keyword deletes a rule (local or global). Users need to specify which service the rule is in.


* IMPORTANT NOTE:


* I think accessing tree nodes (e.g. select, right-click, expand, etc) in Roles/Services/Rules trees are the same.


* Since I already have the methods created in Service files, I use them to access the rule nodes for now.


* These methods can be rolled up to the ControlPolicy level, if time allows.


* **Parameters**

    
    * **rule_name** – 


    * **service_name** – 


    * **service_type** – local or global



* **Returns**

    1 if success, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyService module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyService.XIQSE_ControlPolicyService()
Bases: `ControlPolicyServiceDetailsWebElements`


#### collapse_service_tree_node(node_name)

#### expand_service_tree_node(node_name)

#### right_click_service_tree_node(node_name)
## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceCreate module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceCreate.XIQSE_ControlPolicyServiceCreate()
Bases: `ControlPolicyServiceCreateWebElements`


#### xiqse_control_policy_create_service(service_name, service_type='local')

* This keyword creates a service (local or global).


* **Parameters**

    
    * **service_name** – 


    * **service_type** – local or global



* **Returns**

    1 if success, else -1


## extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceDelete module


### _class_ extauto.xiqse.flows.control.policy.XIQSE_ControlPolicyServiceDelete.XIQSE_ControlPolicyServiceDelete()
Bases: `ControlPolicyServiceDeleteWebElements`


#### xiqse_control_policy_delete_service(service_name, service_type='local')

* This keyword deletes a service (local or global).


* **Parameters**

    
    * **service_name** – 


    * **service_type** – local or global



* **Returns**

    1 if success, else -1
