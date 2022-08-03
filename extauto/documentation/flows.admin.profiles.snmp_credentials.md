# extauto.xiqse.flows.admin.profiles.snmp_credentials package

## extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentials module


### _class_ extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentials.XIQSE_AdminProfilesSNMPCredentials()
Bases: `AdminProfilesSNMPCredentialsWebElements`


#### xiqse_create_snmp_credential(name, version, comm_str)
> 
> * This keyword creates a new SNMPv1 or SNMPv2 credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.


> * Please use xiqse_create_snmpv3_credential to create an SNMPv3 credential


> * Keyword Usage

> > 
> > * `XIQSE Create SNMP Credential  test_cred_1  SNMPv1  public`


> > * `XIQSE Create SNMP Credential  test_cred_2  SNMPv2  private`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **version** – value to select for the SNMP Version field (SNMPv1, SNMPv2, SNMPv3)


    * **comm_str** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_create_snmpv1_credential(name, comm_str)
> 
> * This keyword creates a new SNMPv1 credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Create SNMP Credential  test_cred_1  public`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **comm_str** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_create_snmpv2_credential(name, comm_str)
> 
> * This keyword creates a new SNMPv2 credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Create SNMP Credential  test_cred_2  private`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **comm_str** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_create_snmpv3_credential(name, user_name, auth_type='None', auth_pwd=None, priv_type=None, priv_pwd=None)
> 
> * This keyword creates a new SNMPv3 credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.


> * Please use xiqse_create_snmp_credential to create an SNMPv1 or SNMPv2 credential


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create SNMPv3 Credential  test_cred_1  admin`


> > * `XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=MD5  auth_pwd=auth_pwd`


> > * `XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=SHA  auth_pwd=auth_pwd  priv_type=AES  priv_pwd=priv_pwd`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **user_name** – value to enter in the User Name field


    * **auth_type** – value to select for the Authentication Type field (None, MD5, SHA)


    * **auth_pwd** – value to enter in the Authentication Password field


    * **priv_type** – value to select for the Privacy Type field (None, AES, DES)


    * **priv_pwd** – value to enter in the Privacy Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_snmp_credential(name)
> 
> * This keyword deletes an existing SNMP credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Delete SNMP Credential  test_cred_1`


* **Parameters**

    **name** – name of the SNMP credential to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_snmp_credential(name)

* Searches for SNMP Credential matching the specified name.


* Assumes the Administration> Profiles> SNMP Credentials tab is already selected.


* **Parameters**

    **name** – Name of the SNMP credential to search for



* **Returns**

    return 1 if the SNMP credential is found, else -1



#### xiqse_navigate_and_create_snmp_credential(name, version, comm_str)
> 
> * This keyword navigates to the Administration> Profiles> SNMP Credentials tab and


> * creates a new SNMPv1 or SNMPv2 credential in XIQ-SE.


> * Please use xiqse_navigate_and_create_snmpv3_credential to create an SNMPv3 credential.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create SNMP Credential  test_cred_1  SNMPv1  public`


> > * `XIQSE Navigate and Create SNMP Credential  test_cred_2  SNMPv2  private`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **version** – value to select for the SNMP Version field (SNMPv1, SNMPv2)


    * **comm_str** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_create_snmpv1_credential(name, comm_str)
> 
> * This keyword navigates to the Administration> Profiles> SNMP Credentials tab and


> * creates a new SNMPv1 credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create SNMPv1 Credential  test_cred_1  public`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **comm_str** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_create_snmpv2_credential(name, comm_str)
> 
> * This keyword navigates to the Administration> Profiles> SNMP Credentials tab and


> * creates a new SNMPv2 credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create SNMP Credential  test_cred_2   private`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **comm_str** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_create_snmpv3_credential(name, user_name, auth_type='None', auth_pwd=None, priv_type=None, priv_pwd=None)
> 
> * This keyword navigates to the Administration> Profiles> SNMP Credentials tab and


> * creates a new SNMPv3 credential in XIQ-SE.


> * Please use xiqse_navigate_and_create_credential to create an SNMPv1 or SNMPv2 credential


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create SNMPv3 Credential  test_cred_1  admin`


> > * `XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=MD5  auth_pwd=auth_pwd`


> > * `XIQSE Navigate and Create SNMPv3 Credential  test_cred_2  my_user   auth_type=SHA  auth_pwd=auth_pwd  priv_type=AES  priv_pwd=priv_pwd`


* **Parameters**

    
    * **name** – value to enter in the Credential Name field


    * **user_name** – value to enter in the User Name field


    * **auth_type** – value to select for the Authentication Type field (None, MD5, SHA)


    * **auth_pwd** – value to enter in the Authentication Password field


    * **priv_type** – value to select for the Privacy Type field (None, AES, DES)


    * **priv_pwd** – value to enter in the Privacy Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_delete_snmp_credential(name)
> 
> * This keyword navigates to the Administration> Profiles> SNMP Credentials tab and


> * deletes an existing SNMP credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Delete SNMP Credential  test_cred_1`


* **Parameters**

    **name** – name of the SNMP credential to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_select_snmp_credential(name)
> 
> * This keyword navigates to the Administration> Profiles> SNMP Credentials tab and


> * selects an existing SNMP credential in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Select SNMP Credential  test_cred_1`


* **Parameters**

    **name** – name of the SNMP credential to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_refresh_snmp_credentials_table()

* Refreshes the SNMP Credentials table.


* Assumes the Administration> Profiles> SNMP Credentials tab is already selected.


* **Returns**

    return 1 if the action is successful, else -1



#### xiqse_select_snmp_credential(name)
> 
> * This keyword selects an existing SNMP credential in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles> SNMP Credentials.


> * Keyword Usage

> > 
> > * `XIQSE Select SNMP Credential  test_cred_1`


* **Parameters**

    **name** – name of the SNMP credential to select



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsAddCred module


### _class_ extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsAddCred.XIQSE_AdminProfilesSNMPCredentialsAddCred()
Bases: `AdminProfilesSNMPCredentialsAddCredWebElements`


#### xiqse_add_snmp_credential_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_click_save()
> 
> * This keyword clicks Save in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Click Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_select_authentication_type(the_value)
> 
> * This keyword selects the Authentication Type value in the Add SNMP Credential dialog for SNMPv3.


> * It is assumed the Add SNMP Credential dialog is open and the version is set to SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Select Authentication Type    None`


> > * `XIQSE Add SNMP Credential Dialog Select Authentication Type    MD5`


> > * `XIQSE Add SNMP Credential Dialog Select Authentication Type    SHA`


* **Parameters**

    **the_value** – value to select in the Authentication Type field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_select_privacy_type(the_value)
> 
> * This keyword selects the Privacy Type value in the Add SNMP Credential dialog for SNMPv3.


> * It is assumed the Add SNMP Credential dialog is open, the version is set to SNMPv3, and the


> * Authentication Type is something other than “None”.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Select Privacy Type    None`


> > * `XIQSE Add SNMP Credential Dialog Select Privacy Type    AES`


> > * `XIQSE Add SNMP Credential Dialog Select Privacy Type    DES`


* **Parameters**

    **the_value** – value to select in the Privacy Type field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_select_snmp_version(the_value)
> 
> * This keyword selects the SNMP Version value in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Select SNMP Version    SNMPv1`


> > * `XIQSE Add SNMP Credential Dialog Select SNMP Version    SNMPv2`


> > * `XIQSE Add SNMP Credential Dialog Select SNMP Version    SNMPv3`


* **Parameters**

    **the_value** – value to select in the SNMP Version field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_select_snmpv1()
> 
> * This keyword selects SNMP Version SNMPv1 in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Select SNMPv1`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_select_snmpv2()
> 
> * This keyword selects SNMP Version SNMPv2 in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Select SNMPv2`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_select_snmpv3()
> 
> * This keyword selects SNMP Version SNMPv3 in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Select SNMPv3`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_set_authentication_password(the_value)
> 
> * This keyword enters the Authentication Password value in the Add SNMP Credential dialog for SNMPv3.


> * It is assumed the Add SNMP Credential dialog is open, the version is set to SNMPv3, and the


> * Authentication Type is something other than “None”.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Set Authentication Password    ${PASSWORD}`


* **Parameters**

    **the_value** – value to enter in the Authentication Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_set_community_name(the_value)
> 
> * This keyword enters the Community Name value in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Set Community Name    public`


> > * `XIQSE Add SNMP Credential Dialog Set Community Name    private`


> > * `XIQSE Add SNMP Credential Dialog Set Community Name    ${MY_COMMUNITY}`


* **Parameters**

    **the_value** – value to enter in the Community Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_set_credential_name(the_value)
> 
> * This keyword enters the Credential Name value in the Add SNMP Credential dialog.


> * It is assumed the Add SNMP Credential dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Set Credential Name    my_snmp_cred`


* **Parameters**

    **the_value** – value to enter in the Credential Name field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_set_privacy_password(the_value)
> 
> * This keyword enters the Privacy Password value in the Add SNMP Credential dialog for SNMPv3.


> * It is assumed the Add SNMP Credential dialog is open, the version is set to SNMPv3, and the


> * Privacy Type is something other than “None”.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Set Authentication Password    ${PASSWORD}`


* **Parameters**

    **the_value** – value to enter in the Authentication Password field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_snmp_credential_dialog_set_user_name(the_value)
> 
> * This keyword enters the User Name value in the Add SNMP Credential dialog for SNMPv3.


> * It is assumed the Add SNMP Credential dialog is open and the version is set to SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add SNMP Credential Dialog Set User Name    admin`


* **Parameters**

    **the_value** – value to enter in the User Name field



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsDeleteCred module


### _class_ extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsDeleteCred.XIQSE_AdminProfilesSNMPCredentialsDeleteCred()
Bases: `AdminProfilesSNMPCredentialsDeleteCredWebElements`


#### xiqse_delete_snmp_credential_confirm_delete()
> 
> * This keyword confirms the SNMP Credential deletion.


> * It is assumed the Confirm Delete dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete SNMP Credential Confirm Delete`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_snmp_credential_confirm_dialog_click_no()
> 
> * This keyword clicks the No button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the SNMP Credential is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete SNMP Credential Confirm Dialog Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_snmp_credential_confirm_dialog_click_yes()
> 
> * This keyword clicks the Yes button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the SNMP Credential is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete SNMP Credential Confirm Dialog Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsSaveFailed module


### _class_ extauto.xiqse.flows.admin.profiles.snmp_credentials.XIQSE_AdminProfilesSNMPCredentialsSaveFailed.XIQSE_AdminProfilesSNMPCredentialsSaveFailed()
Bases: `AdminProfilesSNMPCredentialsSaveFailedWebElements`


#### xiqse_save_failed_dialog_handle_failure()
> 
> * This keyword handles a failure saving a credential in the Add SNMP Credential dialog.


> * Keyword Usage

> > 
> > * `XIQSE Save Failed Dialog Handle Failure`


* **Returns**

    1 if no failure occurred, 2 if the failure is due to the entry already existing, else -1
