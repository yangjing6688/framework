# extauto.xiqse.flows.admin.profiles.cli_credentials package

## extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentials module


### _class_ extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentials.XIQSE_AdminProfilesCLICredentials()
Bases: `AdminProfilesCLICredentialsWebElements`


#### xiqse_create_cli_credential(desc, user_name, type='Telnet', login_pwd=None, enable_pwd=None, config_pwd=None)
> 
> * This keyword creates a new CLI credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> CLI Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1`


> > * `XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  type="SSH"`


> > * `XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  login_pwd=abc123`


* **Parameters**

    
    * **desc** – value to enter in the Description field


    * **user_name** – value to enter in the User Name field


    * **type** – value to select for the Type field (Telnt, SSH)


    * **login_pwd** – value to enter in the Login Password field


    * **enable_pwd** – value to enter in the Enable Password field


    * **config_pwd** – value to enter in the Configuration Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_cli_credential(name)
> 
> * This keyword deletes an existing CLI credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> CLI Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Delete CLI Credential  test_cred_1`


* **Parameters**

    **name** – name of the CLI credential to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_cli_credential(name)

* Searches for CLI Credential matching the specified name.


* Assumes the Administration> Profiles> CLI Credentials tab is already selected.


* **Parameters**

    **name** – Name of the CLI credential to search for



* **Returns**

    return 1 if the CLI credential is found, else -1



#### xiqse_navigate_and_create_cli_credential(desc, user_name, type='Telnet', login_pwd=None, enable_pwd=None, config_pwd=None)
> 
> * This keyword navigates to the Administration> Profiles> CLI Credentials tab and


> * creates a new CLI credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1`


> > * `XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  type="SSH"`


> > * `XIQSE Navigate and Create CLI Credential  cli_cred_1  user_1  login_pwd=abc123`


* **Parameters**

    
    * **desc** – value to enter in the Description field


    * **user_name** – value to enter in the User Name field


    * **type** – value to select for the Type field (Telnt, SSH)


    * **login_pwd** – value to enter in the Login Password field


    * **enable_pwd** – value to enter in the Enable Password field


    * **config_pwd** – value to enter in the Configuration Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_delete_cli_credential(desc)
> 
> * This keyword navigates to the Administration> Profiles> CLI Credentials tab and


> * deletes an existing CLI credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Delete CLI Credential  cli_cred_1`


* **Parameters**

    **desc** – name (Description column) of the CLI credential to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_select_cli_credential(desc)
> 
> * This keyword navigates to the Administration> Profiles> CLI Credentials tab and


> * selects an existing CLI credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Select CLI Credential  cli_cred_1`


* **Parameters**

    **desc** – name (Description column) of the CLI credential to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_refresh_cli_credentials_table()

* Refreshes the CLI Credentials table.


* Assumes the Administration> Profiles> CLI Credentials tab is already selected.


* **Returns**

    return 1 if the action is successful, else -1



#### xiqse_select_cli_credential(name)
> 
> * This keyword selects an existing CLI credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> CLI Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Select CLI Credential  test_cred_1`


* **Parameters**

    **name** – name of the CLI credential to select



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsAddCred module


### _class_ extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsAddCred.XIQSE_AdminProfilesCLICredentialsAddCred()
Bases: `AdminProfilesCLICredentialsAddCredWebElements`


#### xiqse_add_cli_credential_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_click_save()
> 
> * This keyword clicks Save in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Click Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_select_ssh()
> 
> * This keyword selects SSH from the Type dropdown in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Select SSH`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_select_telnet()
> 
> * This keyword selects Telnet from the Type dropdown in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Select Telnet`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_select_type(the_value)
> 
> * This keyword selects the CLI Version value in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Select Type    Telnet`


> > * `XIQSE Add CLI Credential Dialog Select Type    SSH`


* **Parameters**

    **the_value** – value to select in the Type field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_set_configuration_password(the_value)
> 
> * This keyword enters the Configuration Password value in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Set Configuration Password    abc123`


* **Parameters**

    **the_value** – value to enter in the Configuration Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_set_description(the_value)
> 
> * This keyword enters the Description value in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Set Description    my_cli_cred`


* **Parameters**

    **the_value** – value to enter in the Description field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_set_enable_password(the_value)
> 
> * This keyword enters the Login Password value in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Set Enable Password    abc123`


* **Parameters**

    **the_value** – value to enter in the Enable Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_set_login_password(the_value)
> 
> * This keyword enters the Login Password value in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Set Login Password    abc123`


* **Parameters**

    **the_value** – value to enter in the Login Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_cli_credential_dialog_set_user_name(the_value)
> 
> * This keyword enters the User Name value in the Add CLI Credential dialog.


> * It is assumed the Add CLI Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add CLI Credential Dialog Set User Name    admin`


* **Parameters**

    **the_value** – value to enter in the User Name field



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsDeleteCred module


### _class_ extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsDeleteCred.XIQSE_AdminProfilesCLICredentialsDeleteCred()
Bases: `AdminProfilesCLICredentialsDeleteCredWebElements`


#### xiqse_delete_cli_credential_confirm_delete()
> 
> * This keyword confirms the CLI Credential deletion.


> * It is assumed the Confirm Delete dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete CLI Credential Confirm Delete`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_cli_credential_confirm_dialog_click_no()
> 
> * This keyword clicks the No button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the CLI Credential is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete CLI Credential Confirm Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_cli_credential_confirm_dialog_click_yes()
> 
> * This keyword clicks the Yes button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the CLI Credential is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete CLI Credential Confirm Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsSaveFailed module


### _class_ extauto.xiqse.flows.admin.profiles.cli_credentials.XIQSE_AdminProfilesCLICredentialsSaveFailed.XIQSE_AdminProfilesCLICredentialsSaveFailed()
Bases: `AdminProfilesCLICredentialsSaveFailedWebElements`


#### xiqse_save_failed_dialog_handle_failure()
> 
> * This keyword handles a failure saving a credential in the Add CLI Credential dialog.


> * Keyword Usage

> > 
> > * `XIQSE Save Failed Dialog Handle Failure`


* **Returns**

    1 if no failure occurred, 2 if the failure is due to the entry already existing, else -1
