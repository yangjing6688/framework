# extauto.xiqse.flows.admin.users package

## extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsers module


### _class_ extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsers.XIQSE_AdminAuthorizedUsers()
Bases: `AdminAuthorizedUsersWebElements`


#### xiqse_delete_authorized_user(name, ignore_case=False)
> 
> * This keyword deletes an existing Authorized User in XIQ-SE.


> * It is assumed the view is already navigated to Administration > Users.


> * Keyword Usage

> > 
> > * `XIQSE Delete Authorized User  username  ignore_case=True`


* **Parameters**

    
    * **name** – name of the Authorized User to delete


    * **ignore_case** – ignore case (optional) and defaults to False



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_authorized_user(name, ignore_case=False)

* Searches for Authorized User matching the specified name.


* Assumes the Administration > Users tab is already selected.


* Keyword Usage

> 
> * `XIQSE Find Authorized User  username  ignore_case=True`


* **Parameters**

    
    * **name** – Name of the Authorized User to search for


    * **ignore_case** – ignore case (optional) and defaults to False



* **Returns**

    return 1 if the Authorized User is found, else -1



#### xiqse_navigate_and_delete_authorized_user(name, ignore_case=False)
> 
> * This keyword navigates to the Administration> Users tab and deletes an existing Authorized User in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Delete Authorized User  username  ignore_case=True`


* **Parameters**

    
    * **name** – name of the Authorized User to delete


    * **ignore_case** – ignore case (optional) and defaults to False



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_select_authorized_user(name, ignore_case=False)
> 
> * This keyword navigates to the Administration> Users tab and selects an existing Authorized User in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Select Authorized User  username  ignore_case=True`


* **Parameters**

    
    * **name** – name of the Authorized User to select


    * **ignore_case** – ignore case (optional) and defaults to False



* **Returns**

    1 if action was successful, else -1



#### xiqse_select_authorized_user(name, ignore_case=False)
> 
> * This keyword selects an existing Authorized User in XIQ-SE.


> * It is assumed the view is already navigated to Administration > Users.


> * Keyword Usage

> > 
> > * `XIQSE Select Authorized User  username  ignore_case=True`


* **Parameters**

    
    * **name** – name of the Authorized User to select


    * **ignore_case** – ignore case (optional) and defaults to False



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsersDeleteUser module


### _class_ extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsersDeleteUser.XIQSE_AdminAuthorizedUsersDeleteUser()
Bases: `AdminAuthorizedUsersDeleteUserWebElements`


#### xiqse_delete_authorized_user_confirm_delete()
> 
> * This keyword confirms the Authorized User deletion.


> * It is assumed the Confirm Delete dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Authorized User Confirm Delete`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_authorized_user_confirm_dialog_click_no()
> 
> * This keyword clicks the No button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the Authorized User is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Site Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_authorized_user_confirm_dialog_click_yes()
> 
> * This keyword clicks the Yes button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the Authorized User is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Authorized User Confirm Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1
