# A3WebElementsflow module


### _class_ extauto.a3.flows.a3.A3WebElementsflow.A3WebElementsflow()
Bases: `A3WebElements`


#### add_device()

* This keyword will add the device in Device section


* Keyword Usage


* `Add Device`


* **Returns**

    1 if device is been added successfully else return -1



#### backup_file()
> 
> * This keyword will take the backup


> * Keyword Usage

> > 
> > * `Backup File`


* **Returns**

    1 if Backup created successfully else return -1



#### connection_profile_test(mac_add)
> 
> * This keyword select the connection profile test from tools menu and takes mac as input and give

>     profile in use


> * Keyword Usage

> > 
> > * `Connection Profile Test`


* **Returns**

    1 if profile test is successful else return -1



#### create_new_conn_profile()

* This keyword will create the connection profile


* Keyword Usage


* `Create New Conn Profile`


* **Returns**

    1 if connection profile is created successfully else return -1



#### select_clients_search(mac, client_status, owner)

* This keyword will validate the authentication with A3 in clients tab by selecting the client details


* Keyword Usage


* 

```
``
```

Select Clients Search mac owner \`\`


* **Parameters**

    
    * **mac** – it should be mac address of the client


    * **client_status** – it should be the client connection status ex: online/offline - on /unknown


    * **owner** – it should be the user name ex: ad or default



* **Returns**

    1 if Authentication is done successfully else -1



#### select_cloud_integration()
> 
> * This keyword select the Cloud Integration from the menu System Configuration ank link it to XIQ


> * Keyword Usage

> > 
> > * `Select cloud integration`


* **Returns**

    1 if Navigation Successful to Cloud Integration else return -1



#### select_logs(search_string)

* This keyword will select the log in Tools tab


* Keyword Usage


* `Select Logs   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be the name of the log file which is searched on the row cell



* **Returns**

    row element if row exists else return None



#### select_radius_audit_logs(mac, auth_status, user_name)

* This keyword will validate the authentication with A3 in Auditing tab by selecting the auditing details


* Keyword Usage


* `Select Radius Audit Logs mac auth_status client_status`


* **Parameters**

    
    * **mac** – it should be mac address of the client


    * **auth_status** – it should be authentication status of the client ex: Accept/Reject


    * **user_name** – it should be the user name ex: ad or mac id



* **Returns**

    1 if Authentication is done successfully else -1



#### select_ssh()
> 
> * This keyword selects SSH option in Tools Page


> * Keyword Usage

> > 
> > * `Selects SSH option in Tools Page`


* **Returns**

    1 if Navigation Successful to SSH Option else return -1



#### select_tech_data()
> 
> * This keyword selects Tech data in Tools Page


> * Keyword Usage

> > 
> > * `Select Tech Data`


* **Returns**

    1 if Tech data is selected & downloaded successfully else return -1



#### ssh_button()
> 
> * This keyword select the SSH checkbox and click it


> * Keyword Usage

> > 
> > * `Select SSH Checkbox`


* **Returns**

    1 if Navigation Successful to SSH checkbox else return -1



#### ssh_page_entries()

* This keyword will enter the values into SSH page tools


* Keyword Usage


* `SSH Page Entries`


* **Returns**

    1 if Navigation Successful to SSH inputs else return -1



#### switch_policies_access_control()
> 
> * This keyword switches to Policies & Access Control and expand the menu


> * Keyword Usage

> > 
> > * `Switch To Policies Access Control`


* **Returns**

    1 if Navigation Successful to Policies & Access Control else return -1



#### switch_system_configuration()
> 
> * This keyword switches to System Configuration Page


> * Keyword Usage

> > 
> > * `Switch To System Configuration Page`


* **Returns**

    1 if Navigation Successful to System Configuration else return -1



#### validate_backup_created(search_string)

* This keyword will validate the creation of the backup file


* Keyword Usage

> 
> * `Validate Backup Created   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be the file name of the backup which is searched on the row cell



* **Returns**

    row element if row exists else return None
