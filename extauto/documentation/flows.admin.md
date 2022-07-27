# flows.admin package


* [extauto.xiqse.flows.admin.backup_restore package](flows.admin.backup_restore.md)


    * [extauto.xiqse.flows.admin.backup_restore.XIQSE_Backup module](flows.admin.backup_restore.md#module-extauto.xiqse.flows.admin.backup_restore.XIQSE_Backup)


    * [extauto.xiqse.flows.admin.backup_restore.XIQSE_Restore module](flows.admin.backup_restore.md#module-extauto.xiqse.flows.admin.backup_restore.XIQSE_Restore)


* [extauto.xiqse.flows.admin.certificates package](flows.admin.certificates.md)


    * [Module contents](flows.admin.certificates.md#module-extauto.xiqse.flows.admin.certificates)


* [extauto.xiqse.flows.admin.client_api_access package](flows.admin.client_api_access.md)


    * [Module contents](flows.admin.client_api_access.md#module-extauto.xiqse.flows.admin.client_api_access)


* [extauto.xiqse.flows.admin.device_types package](flows.admin.device_types.md)


    * [extauto.xiqse.flows.admin.device_types.XIQSE_AdminDeviceTypes module](flows.admin.device_types.md#module-extauto.xiqse.flows.admin.device_types.XIQSE_AdminDeviceTypes)


* [extauto.xiqse.flows.admin.diagnostics package](flows.admin.diagnostics.md)


    * [extauto.xiqse.flows.admin.diagnostics.XIQSE_AdminDiagnostics module](flows.admin.diagnostics.md#module-extauto.xiqse.flows.admin.diagnostics.XIQSE_AdminDiagnostics)


* [extauto.xiqse.flows.admin.options package](flows.admin.options.md)


    * [extauto.xiqse.flows.admin.options.XIQSE_AdminOptions module](flows.admin.options.md#module-extauto.xiqse.flows.admin.options.XIQSE_AdminOptions)


* [extauto.xiqse.flows.admin.profiles package](flows.admin.profiles.md)


    * [Subpackages](flows.admin.profiles.md#subpackages)


    * [extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfiles module](flows.admin.profiles.md#module-extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfiles)


    * [extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesAddProfile module](flows.admin.profiles.md#module-extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesAddProfile)


    * [extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesDeleteProfile module](flows.admin.profiles.md#module-extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesDeleteProfile)


    * [extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesEditProfile module](flows.admin.profiles.md#module-extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesEditProfile)


    * [extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesSaveFailed module](flows.admin.profiles.md#module-extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesSaveFailed)


* [extauto.xiqse.flows.admin.server_info package](flows.admin.server_info.md)


    * [Module contents](flows.admin.server_info.md#module-extauto.xiqse.flows.admin.server_info)


* [extauto.xiqse.flows.admin.users package](flows.admin.users.md)


    * [extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsers module](flows.admin.users.md#module-extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsers)


    * [extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsersDeleteUser module](flows.admin.users.md#module-extauto.xiqse.flows.admin.users.XIQSE_AdminAuthorizedUsersDeleteUser)


## flows.admin.XIQSE_Administration module


### _class_ extauto.xiqse.flows.admin.XIQSE_Administration.XIQSE_Administration()
Bases: `AdministrationWebElements`


#### xiqse_admin_select_backup_restore_tab()
> 
> * This keyword selects the Backup/Restore tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Backup Restore Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_certificates_tab()
> 
> * This keyword selects the Certificates tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Certificates Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_client_api_access_tab()
> 
> * This keyword selects the Client API Access tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Client API Access Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_device_types_tab()
> 
> * This keyword selects the Device Types tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Device Types Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_diagnostics_tab()
> 
> * This keyword selects the Diagnostics tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Diagnostics Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_licenses_tab()
> 
> * This keyword selects the Licenses tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Licenses Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_options_tab()
> 
> * This keyword selects the Options tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Options Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_profiles_tab()
> 
> * This keyword selects the Profiles tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Profiles Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_server_information_tab()
> 
> * This keyword selects the Server Information tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Server Information Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Tab    Profiles`


> > * `XIQSE Administration Select Tab    Users`


> > * `XIQSE Administration Select Tab    Server Information`


> > * `XIQSE Administration Select Tab    Certificates`


> > * `XIQSE Administration Select Tab    Options`


> > * `XIQSE Administration Select Tab    Device Types`


> > * `XIQSE Administration Select Tab    Backup/Restore`


> > * `XIQSE Administration Select Tab    Diagnostics`


> > * `XIQSE Administration Select Tab    Client API Access`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_admin_select_users_tab()
> 
> * This keyword selects the Users tab of the Administration page


> * Keyword Usage

> > 
> > * `XIQSE Administration Select Users Tab`


* **Returns**

    1 if action was successful, else -1
