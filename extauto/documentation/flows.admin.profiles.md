# extauto.xiqse.flows.admin.profiles package

## Subpackages

## extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfiles module


### _class_ extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfiles.XIQSE_AdminProfiles()
Bases: `AdminProfilesWebElements`


#### xiqse_create_profile(name, version='SNMPv1', read=None, write=None, max=None, cli=None, read_sec=None, write_sec=None, max_sec=None)
> 
> * This keyword creates a new profile in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles.


> * Keyword Usage

> > 
> > * `XIQSE Create Profile  test_profile_1`


> > * `XIQSE Create Profile  test_profile_2  SNMPv2  public_v1  private_v1  private_v1  Default`


* **Parameters**

    
    * **name** – value to enter in the Profile Name field


    * **version** – value to select for the SNMP Version field (SNMPv1, SNMPv2, SNMPv3)


    * **read** – value to select for the Read field


    * **write** – value to select for the Write field


    * **max** – value to select for the Max Access field


    * **read_sec** – value to select for the Read Security field (for SNMPv3 version only)


    * **write_sec** – value to select for the Write Security field (for SNMPv3 version only)


    * **max_sec** – value to select for the Max Security field (for SNMPv3 version only)


    * **cli** – value to select for the CLI Credential field



* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_profile(name)
> 
> * This keyword deletes an existing profile in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles.


> * Keyword Usage

> > 
> > * `XIQSE Delete Profile  test_profile_1`


* **Parameters**

    **name** – name of the profile to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile(name, read=None, write=None, max=None, cli=None)
> 
> * This keyword edits the specified profile in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile  test_profile_1  cli=MY_CLI`


> > * `XIQSE Edit Profile  test_profile_2  read=public_v1  write=private_v1  max=private_v1  cli=Default`


* **Parameters**

    
    * **name** – name of the profile to edit


    * **read** – value to select for the Read field


    * **write** – value to select for the Write field


    * **max** – value to select for the Max Access field


    * **cli** – value to select for the CLI Credential field



* **Returns**

    1 if action was successful, else -1



#### xiqse_find_profile(name)

* Searches for Profile matching the specified name.


* Assumes the Administration> Profiles tab is already selected.


* **Parameters**

    **name** – Name of the Profile to search for



* **Returns**

    return 1 if the Profile is found, else -1



#### xiqse_navigate_and_create_profile(name, version='SNMPv1', read=None, write=None, max=None, cli=None)
> 
> * This keyword navigates to the Administration> Profiles tab and creates a new profile in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Create Profile  test_profile_1`


> > * `XIQSE Navigate and Create Profile  test_profile_2  SNMPv2  public_v1  private_v1  private_v1  Default`


* **Parameters**

    
    * **name** – value to enter in the Profile Name field


    * **version** – value to select for the SNMP Version field (SNMPv1, SNMPv2, SNMPv3)


    * **read** – value to select for the Read field


    * **write** – value to select for the Write field


    * **max** – value to select for the Max Access field


    * **cli** – value to select for the CLI Credential field



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_delete_profile(name)
> 
> * This keyword navigates to the Administration> Profiles tab and deletes an existing profile in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Delete Profile  test_profile_1`


* **Parameters**

    **name** – name of the profile to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_navigate_and_select_profile(name)
> 
> * This keyword navigates to the Administration> Profiles tab and selects an existing profile in XIQ-SE.


> * Keyword Usage

> > 
> > * `XIQSE Navigate and Select Profile  test_profile_1`


* **Parameters**

    **name** – name of the profile to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_profiles_select_cli_credentials_tab()
> 
> * This keyword selects the CLI Credentials tab on the Administration> Profiles page.


> * It is assumed the Administration> Profiles page is currently being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Profiles Select CLI Credentials Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_profiles_select_device_mapping_tab()
> 
> * This keyword selects the Device Mapping tab on the Administration> Profiles page.


> * It is assumed the Administration> Profiles page is currently being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Profiles Select Device Mapping Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_profiles_select_snmp_credentials_tab()
> 
> * This keyword selects the SNMP Credentials tab on the Administration> Profiles page.


> * It is assumed the Administration> Profiles page is currently being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Profiles Select SNMP Credentials Tab`


* **Returns**

    1 if action was successful, else -1



#### xiqse_profiles_select_tab(tab_name)
> 
> * This keyword selects the specified tab of the Administration> Profiles page


> * Keyword Usage

> > 
> > * `XIQSE Profiles Select Tab    SNMP Credentials`


> > * `XIQSE Profiles Select Tab    CLI Credentials`


> > * `XIQSE Profiles Select Tab    Device Mapping`


* **Parameters**

    **tab_name** – name of the sub tab to select



* **Returns**

    1 if action was successful, else -1



#### xiqse_refresh_profiles_table()

* Refreshes the Profiles table.


* Assumes the Administration> Profiles tab is already selected.


* **Returns**

    return 1 if the action is successful, else -1



#### xiqse_select_profile(name)
> 
> * This keyword selects an existing profile in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles.


> * Keyword Usage

> > 
> > * `XIQSE Select Profile  test_profile_1`


* **Parameters**

    **name** – name of the profile to select



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesAddProfile module


### _class_ extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesAddProfile.XIQSE_AdminProfilesAddProfile()
Bases: `AdminProfilesAddProfileWebElements`


#### xiqse_add_profile_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_click_save()
> 
> * This keyword clicks Save in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Click Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_cli(the_value)
> 
> * This keyword selects the CLI Credential value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select CLI    Default`


* **Parameters**

    **the_value** – value to select in the CLI Credential field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_max_access(the_value)
> 
> * This keyword selects the Max Access value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Max Access    public_v1`


* **Parameters**

    **the_value** – value to select in the Max Access field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_max_security(the_value)
> 
> * This keyword selects the Max Security value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open and the version is SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Max Security   NoAuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Max Security   AuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Max Security   AuthPriv`


* **Parameters**

    **the_value** – value to select in the Max Security field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_read(the_value)
> 
> * This keyword selects the Read value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Read    public_v1`


* **Parameters**

    **the_value** – value to select in the Read field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_read_security(the_value)
> 
> * This keyword selects the Read Security value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open and the version is SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Read Security   NoAuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Read Security   AuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Read Security   AuthPriv`


* **Parameters**

    **the_value** – value to select in the Read Securityfield



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_snmp_version(the_value)
> 
> * This keyword selects the SNMP Version value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select SNMP Version    SNMPv1`


> > * `XIQSE Add Profile Dialog Select SNMP Version    SNMPv2`


> > * `XIQSE Add Profile Dialog Select SNMP Version    SNMPv3`


* **Parameters**

    **the_value** – value to select in the SNMP Version field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_snmpv1()
> 
> * This keyword selects SNMP Version SNMPv1 in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select SNMPv1`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_snmpv2()
> 
> * This keyword selects SNMP Version SNMPv2 in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select SNMPv2`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_snmpv3()
> 
> * This keyword selects SNMP Version SNMPv3 in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select SNMPv3`


* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_write(the_value)
> 
> * This keyword selects the Write value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Write    public_v1`


* **Parameters**

    **the_value** – value to select in the Write field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_select_write_security(the_value)
> 
> * This keyword selects the Write Security value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open and the version is SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Write Security   NoAuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Write Security   AuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Write Security   AuthPriv`


* **Parameters**

    **the_value** – value to select in the Write Security field



* **Returns**

    1 if action was successful, else -1



#### xiqse_add_profile_dialog_set_profile_name(the_value)
> 
> * This keyword enters the Profile Name value in the Add Profile dialog.


> * It is assumed the Add Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Set Profile Name    my_profile`


* **Parameters**

    **the_value** – value to enter in the Profile Name field



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesDeleteProfile module


### _class_ extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesDeleteProfile.XIQSE_AdminProfilesDeleteProfile()
Bases: `AdminProfilesDeleteProfileWebElements`


#### xiqse_delete_profile(name)
> 
> * This keyword deletes an existing profile in XIQ-SE.


> * It is assumed the view is already navigated to Administration> Profiles.


> * Keyword Usage

> > 
> > * `XIQSE Delete Profile  test_profile_1`


* **Parameters**

    **name** – name of the profile to delete



* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_profile_confirm_delete()
> 
> * This keyword confirms the Profile deletion.


> * It is assumed the Confirm Delete dialog is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Profile Confirm Delete`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_profile_confirm_dialog_click_no()
> 
> * This keyword clicks the No button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the SNMP Credential is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Site Click No`


* **Returns**

    1 if action was successful, else -1



#### xiqse_delete_profile_confirm_dialog_click_yes()
> 
> * This keyword clicks the Yes button in the Confirm Delete dialog.


> * It is assumed the confirmation dialog for deleting the SNMP Credential is already open.


> * Keyword Usage

> > 
> > * `XIQSE Delete Site Click Yes`


* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesEditProfile module


### _class_ extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesEditProfile.XIQSE_AdminProfilesEditProfile()
Bases: `AdminProfilesAddProfileWebElements`


#### xiqse_edit_profile_dialog_click_cancel()
> 
> * This keyword clicks Cancel in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile Dialog Click Cancel`


* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_click_save()
> 
> * This keyword clicks Save in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile Dialog Click Save`


* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_cli(the_value)
> 
> * This keyword selects the CLI Credential value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile Dialog Select CLI    Default`


* **Parameters**

    **the_value** – value to select in the CLI Credential field



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_max_access(the_value)
> 
> * This keyword selects the Max Access value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile Dialog Select Max Access    public_v1`


* **Parameters**

    **the_value** – value to select in the Max Access field



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_max_security(the_value)
> 
> * This keyword selects the Max Security value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open and the version is SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Max Security   NoAuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Max Security   AuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Max Security   AuthPriv`


* **Parameters**

    **the_value** – value to select in the Max Security field



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_read(the_value)
> 
> * This keyword selects the Read value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile Dialog Select Read    public_v1`


* **Parameters**

    **the_value** – value to select in the Read field



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_read_security(the_value)
> 
> * This keyword selects the Read Security value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open and the version is SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Read Security   NoAuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Read Security   AuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Read Security   AuthPriv`


* **Parameters**

    **the_value** – value to select in the Read Securityfield



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_write(the_value)
> 
> * This keyword selects the Write value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open.


> * Keyword Usage

> > 
> > * `XIQSE Edit Profile Dialog Select Write    public_v1`


* **Parameters**

    **the_value** – value to select in the Write field



* **Returns**

    1 if action was successful, else -1



#### xiqse_edit_profile_dialog_select_write_security(the_value)
> 
> * This keyword selects the Write Security value in the Edit Profile dialog.


> * It is assumed the Edit Profile dialog is open and the version is SNMPv3.


> * Keyword Usage

> > 
> > * `XIQSE Add Profile Dialog Select Write Security   NoAuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Write Security   AuthNoPriv`


> > * `XIQSE Add Profile Dialog Select Write Security   AuthPriv`


* **Parameters**

    **the_value** – value to select in the Write Security field



* **Returns**

    1 if action was successful, else -1


## extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesSaveFailed module


### _class_ extauto.xiqse.flows.admin.profiles.XIQSE_AdminProfilesSaveFailed.XIQSE_AdminProfilesSaveFailed()
Bases: `AdminProfilesSaveFailedWebElements`


#### xiqse_save_failed_dialog_handle_failure()
> 
> * This keyword handles a failure saving a profile in the Add Profile dialog.


> * Keyword Usage

> > 
> > * `XIQSE Save Failed Dialog Handle Failure`


* **Returns**

    1 if no failure occurred, 2 if the failure is due to the entry already existing, else -1
