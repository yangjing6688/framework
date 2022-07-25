# extauto.xiq.flows.globalsettings package

## Submodules

## extauto.xiq.flows.globalsettings.AccountManagement module


### _class_ extauto.xiq.flows.globalsettings.AccountManagement.AccountManagement()
Bases: `AccntMgmtWebElements`


#### check_config_error()

* Check for Errors while Saving Configurations on XIQ


* Keyword Usage

> 
> * `Check Config Error`


* **Returns**

    1 if no error message after saving the config else returns -2



#### check_for_dashboard_page()

* Check for Dashboard Page


* Keyword Usage

> 
> * `Check For Dashboard Page`


* **Returns**

    1 if no issues in opening page else returns -2



#### check_packet_capture_option()

* Navigates to Packet Capture option Page


* Flow : Manage > Tools–>Packet Capture

> 
> * Keyword Usage

> > 
> > * `Check Packet Capture Option`


* **Returns**

    1 if no issues in opening Tools –> Packet Capture page else returns -2



#### create_credential_distribution_groups(group_name, admin_account, member_of, restriction_count, registration_operation, user_group_name)

* **Parameters**

    
    * **group_name** – group name


    * **admin_account** – admin account


    * **member_of** – member of


    * **restriction_count** – credential_restriction\`count


    * **registration_operation** – registration_operation


    * **user_group_name** – user_group_name



* **Returns**

    1 if success. -1 if fails



* **Returns**

    -2 if error: User must be a member of a group.



* **Returns**

    -3 if error: Select at least one user group.



* **Returns**

    -4 if error: That group already exists.



* **Returns**

    -5 if error: The Member Group cannot be saved because the name << >> already exists.



#### create_role_based_account(\*\*accnt_config)

* Creates an account based on the arguments from rbac_config.robot


* &{OPERATOR_ROLE}, &{MONITOR_ROLE}, &{HELPDESK_ROLE}, &{Guest_Management_Role}, &{Observer_Role}


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * `Create Role Based Account  &{ACCOUNT_CONFIGS}`


* **Parameters**

    **accnt_config** – (dict) include email, name, timeout, role, organization, location



* **Returns**

    1 if there is no error



#### delete_guest_management_account(email_addr)

* Search the specified guest account in accounts grid


* if exist delete the account


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * `Delete Management Account  ${ACCOUNT_EMAIL}`


* **Parameters**

    **email_addr** – email address to search the account



* **Returns**

    1 if Account found on grid and got deleted successfully else None



#### delete_guest_management_accounts()

* Search the guest accounts in accounts grid


* if exist delete the account


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * 

> ```
> ``
> ```

> Delete Management Account \`\`


* **Returns**

    1 if Account found on grid and got deleted successfully else None



#### delete_management_account(email_addr)

* Search the management account in accounts grid


* if exist delete the account


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * `Delete Management Account  ${ACCOUNT_EMAIL}`


* **Parameters**

    **email_addr** – email address to search the account



* **Returns**

    1 if Account found on grid and got deleted successfully else None



#### get_packet_capture_button()

#### open_account_mgmt_page()
> 
> * Navigates to Account Management Page


> * Flow : User account image–>Global Settings–> Account Management


> * Keyword Usage

> > 
> > * `Open Account Mgmt Page`


* **Returns**

    1 if no issues in opening Account Management page else returns -2



#### open_dashboard_page()

* Navigates to Dashboard Page


* Keyword Usage

> 
> * `Open Dashboard Page`


* **Returns**

    1 if no issues in opening Dashboard page else returns -2



#### open_guest_mgmt_page()

* Navigates to Guest Management Page


* Flow : Global settings > Credential Distribution Groups


* Keyword Usage
- `Open Guest Mgmt Page`


* **Returns**

    1 if no issues in opening Guest Management page else returns -2



#### open_license_mgmt_page()

* Navigates to License Management Page


* Flow : User account image–>Global Settings–> ADMINISTRATION–>License Management


* Keyword Usage
- `Open License Mgmt Page`


* **Returns**

    1 if no issues in opening License Management page else returns -2



#### open_tools_page()

* Navigates to Tools Page on Monitor Menu Option


* Flow : Manage–>Tools


* Keyword Usage
- `Open Tools Page`


* **Returns**

    1 if no issues in opening Tools page else returns -2



#### search_guest_account(email_addr)

* Search the management account in accounts grid


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * `Search Management Account  ${ACCOUNT_EMAIL}`


* **Parameters**

    **email_addr** – Email Address Of the Account



* **Returns**

    row if Exists else None



#### search_guest_accounts()

* Search the guest management accounts in accounts grid


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * 

> ```
> ``
> ```

> Search Management Account \`\`


* **Returns**

    row if Exists else None



#### search_management_account(email_addr)

* Search the management account in accounts grid


* Flow : User account image–>Global Settings–> Account Management


* Keyword Usage

> 
> * `Search Management Account  ${ACCOUNT_EMAIL}`


* **Parameters**

    **email_addr** – Email Address Of the Account



* **Returns**

    row if Exists else None


## extauto.xiq.flows.globalsettings.Communications module


### _class_ extauto.xiq.flows.globalsettings.Communications.Communications()
Bases: `CommunicationsWebElements`


#### validate_communications_page()

* This Keyword Navigate to communications menu in Global settings page


* Keyword Usage
- `Validate Communications Page`


* **Returns**

    1 if Validation is Successful to Communications Page



#### validate_new_in_extremecloud_page()

* This Keyword Navigate to New in ExtremeCLoud IQ


* Keyword Usage
- `Navigate To New In Extremecloud Page`


* **Returns**

    1 if Navigation Successful to New in XIQ



#### validate_notifications_page()

* This Keyword Navigate to notifications page from communications page


* Keyword Usage
- `Navigate To Notifications Page`


* **Returns**

    1 if Navigation is Successful to notification page



#### validate_preview_page()

* This Keyword Navigate to preview page in communications


* Keyword Usage
- `Navigate To preview Page`


* **Returns**

    1 if Navigation Successful to Preview Page


## extauto.xiq.flows.globalsettings.CredDistrGrup module


### _class_ extauto.xiq.flows.globalsettings.CredDistrGrup.CredDistrGrup()
Bases: `CredDistrGrupWebElemnts`


#### create_cred_distribution_group(\*\*group_config)

* Flow: Global Settings –> Credential Distribution Groups


* Create Credential distribution Groups


* There are two admin account type need to include the cred distribution groups


* 
    1. Guest Management Role User. 2.Active directory User


* Keyword Usage:

> 
> * `Create Cred Distribution Groups  &{CRED_DISTR_GROUPS_CONFIG}`


> * For Creation of &{CRED_DISTR_GROUPS_CONFIG}  refer emails_reports_config.robot file


* **Parameters**

    **group_config** – (dict) configuration parameters



* **Returns**

    1 if group created
    -1 Configure at least one guest management user



#### delete_cred_distr_group(group_name)

* Flow: Global Settings –> Credential Distribution Groups


* Search the credentials distribution group


* If exists delete the group


* Keyword Usage:

> 
> * `Delete Cred Distr Group   ${GROUP_NAME}`


* **Parameters**

    **group_name** – group name



* **Returns**

    1 if deleted


## extauto.xiq.flows.globalsettings.Dashboard module


### _class_ extauto.xiq.flows.globalsettings.Dashboard.Dashboard()
Bases: `object`


#### dashboard_cards_connection_status_offline_count()

* This keyword will get total Connection status offline count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Connection Status offline Count`


* **Returns**

    if success return Connection Status Online Count else -1



#### dashboard_cards_connection_status_online_count()

* This keyword will get total Connection status online count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Connection Status Online Count`


* **Returns**

    if success return Connection Status Online Count else -1



#### dashboard_cards_total_application_count()

* This keyword will get total aps count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Application Count`


* **Returns**

    if success return total aps Count else -1



#### dashboard_cards_total_clients_count()

* This keyword will get total clients count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Clients Count`


* **Returns**

    if success return total clients Count else -1



#### dashboard_cards_total_critical_alarm_count()

* This keyword will get total critical alarm count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Critical Alarm Count`


* **Returns**

    if success return total critical alarm count else -1



#### dashboard_cards_total_major_alarm_count()

* This keyword will get total Major alarm count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Major Alarm Count`


* **Returns**

    if success return total Major alarm count else -1



#### dashboard_cards_total_minor_alarm_count()

* This keyword will get total Minor alarm count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Minor Alarm Count`


* **Returns**

    if success return total Minor alarm count else -1



#### dashboard_cards_total_rogue_aps_count()

* This keyword will get total Rogue Aps Count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Rogue Aps Count`


* **Returns**

    if success return Rogue Aps Count else -1



#### dashboard_cards_total_rogue_clients_count()

* This keyword will get total Rogue Aps Count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Rogue clients Count`


* **Returns**

    if success return Rogue clients Count else -1



#### dashboard_cards_total_users_count()

* This keyword will get total Users count in dashboard health card


* Keyword Usage

> 
> * `Dashboard Cards Total Users Count`


* **Returns**

    if success return total Users Count else -1



#### dashboard_stats_total_application_usage()

* This keyword will get total Application usage in Dashboard Page


* Keyword Usage

> 
> * `Dashboard Stats Total Application Usage`


* **Returns**

    if success return total Application usage Count else -1


## extauto.xiq.flows.globalsettings.GlobalSetting module


### _class_ extauto.xiq.flows.globalsettings.GlobalSetting.GlobalSetting()
Bases: `GlobalSettingWebElements`


#### backup_viq_data()

* This Keyword will Backup the current VIQ Data


* Flow : User account icon–>Global Settings–> VIQ Management —> Backup Now


* Keyword Usage:

> 
> * \`\` Backup VIQ Data \`\`


* **Returns**

    1 after successfully Backup the VIQ data else -1



#### change_device_password(password)

* Change the Device Password String on Global Settings–>Device Management Page.


* Flow : User account image–>Global Settings–> Device Management Settings


* Keyword Usage:

> 
> * `Change Device password   ${LANGUAGE}`


* **Parameters**

    **password** – Password String



* **Returns**

    1 if XIQ Account Language Changed Successfully else -1



#### change_exos_device_management_settings(option, platform)

* This Keyword will Enable/Disable device management settings for EXOS switches.


* Flow : User account image–>Global Settings–> Device Management Settings


* Keyword Usage

> 
> * `Change exos device management settings     ${OPTION}   {DUT_PLATFORM}`


* **Parameters**

    
    * **option** – Choose an option for Device management settings for EXOS switches:”enable””disable”


    * **platform** – Choose the platform:  EXOS/VOSS



* **Returns**

    1 If device management settings for EXOS switches is Successful



#### change_xiq_account_language(language)

* Change the language of the account


* Flow : User account image–>Global Settings–> Account Details–> Select Language–>Apply


* Keyword Usage:

> 
> * `Change Xiq Account Language   ${LANGUAGE}`


* **Parameters**

    **language** – Language Name ie English



* **Returns**

    1 if XIQ Account Language Changed Successfully else -1



#### change_xiq_account_time_zone(time_zone='(GMT) UTC')

* Change the time zone of the account


* Flow : User account image–>Global Settings–> Account Details–> Select Time Zone–>Apply


* Keyword Usage:

> 
> * `Change XIQ Account Time Zone   ${TIMEZONE}`


* **Parameters**

    **time_zone** – Time zone to select e.g., UTC, EST5EDT, etc



* **Returns**

    1 if XIQ Account Time Zone was changed successfully, else -1



#### check_audit_log(date_start, description, rows_number='20')
This function checks if a log is present into audit log


* **Parameters**

    
    * **date_start** – Starting date for search


    * **description** – Expected log description


    * **rows_number** – number of logs displayed into table



* **Returns**

    1 if the log was found ; else -1



#### create_organization(organization_name, colour_name)

* This Keyword Uses To Create Organization


* Flow : User account image–>Global Settings–> Organization


* Keyword Usage

> 
> * `Create Organization   ${ORGANIZATION_NAME}  ${ORGANIZATION_COLOUR}`


* **Parameters**

    
    * **organization_name** – Name of the Organization


    * **colour_name** – Organization Colour



* **Returns**

    1 If Organization Created Successfully else None



#### delete_api_access_tokens()

* This keyword is used to delete the all generated access tokens


* Flow: Global Settings –> API Token Management –> Select all rows –> Delete


* Keyword Usage:

> 
> * `Delete Api Access Tokens\``


* **Returns**

    None



#### disable_ssh_availability()

* Disabling SSH availability in Global Settings Page


* Flow : User account icon–>Global Settings–> VIQ Management


* Keyword Usage

> 
> * `Disable SSH Availability`


* **Returns**

    1 after successfully disabling SSH



#### enable_account_hiq()

* Enable MSP Feature in the Account


* Flow : User account image–>Global Settings–> Account Details–> Enable HIQ Button


* Keyword Usage

> 
> * `Enable Account HIQ`


* **Returns**

    1 If HIQ Enabled Successfully in the Account else -1



#### enable_ssh_availability()

* Enabling SSH availability in Global Settings Page


* Flow : User account icon–>Global Settings–> VIQ Management


* Keyword Usage

> 
> * `Enable SSH Availability`


* **Returns**

    1 after successfully enabling SSH



#### export_viq()

* This Keyword will Export the current VIQ Data


* Flow : User account icon–>Global Settings–> VIQ Management —> Export VIQ


* Keyword Usage:

> 
> * \`\` Export VIQ \`\`


* **Returns**

    1 after successfully exporting the VIQ data else -1



#### get_accounting_logs_details(search_string, search_filter=None)

* Filter the logs based on the Filter arguments Allowed Filters are: Client or user name


* Get accounts detailed logs from the row


* Flow : User account image–>Global Settings–> Accounting Logs


* Keyword Usage:

> 
> * `Get Accounting Logs Details   ${SEARCH_STRING}   ${SEARCH_FILTER}`


* **Parameters**

    
    * **search_filter** – String to filter the accounting log rows


    * **search_string** – String to search the row



* **Returns**

    Accounting Logs dict



#### get_accounting_logs_row(search_string)

* Get the Accounting Logs from Global Settings Page


* Flow : User account image–>Global Settings–> Accounting Logs


* Keyword Usage

> 
> * `Get Accounting Logs Row   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell
    example search_string be like user_name, auth_type,client etc



* **Returns**

    row element if row exists else return None



#### get_api_access_token_details(search_string)

* This key word is used to get the token details i.e access token, refresh token, expiry time


* Flow:


* Global Settings –> API Token Management


* Keyword Usage:

> 
> * `Get API Access Token Details  ${SEARCH_STRING}`


* **Parameters**

    **search_string** – Search string is the access token generated from the curl command



* **Returns**

    access token row detail dict



#### get_audit_logs_details(category, search_string)

* Get the audit log rows based on category and search_string provided


* Flow : User account image–>Global Settings–> Audit Logs


* Keyword Usage

> 
> * `Get Audit Logs Details   ${CATEGORY}    ${SEARCH_STRING}`


* **Parameters**

    
    * **category** – Category field(Eg: ADMIN, MONITORING)


    * **search_string** – Search string(Eg: Delete, Reset, Reboot)



* **Returns**

    1 if search string found in logs else -1



#### get_audit_logs_row(category, search_string)

* Get the Audit log row with provided search arguments


* Assumes that Already in Audit logs page


* Keyword Usage

> 
> * `Get Audit Logs Row    ${CATEGORY}       ${SEARCH_STRING}`


* Example of Keyword Usage

> 
> * `Get Audit Logs Row    MONITORING      Reset device ${AP1_NAME}`


* **Parameters**

    
    * **category** – Category of Audit log, eg: ADMIN,CONFIG,MONITORING


    * **search_string** – it should be anything which is searched on the row cell
    eg: Reset device ${AP1_NAME}, Added device, Deleted



* **Returns**

    row element if row exists else return -1



#### get_authentication_logs_auth_method(search_string)

* Get the Authentication method Field on authentication Logs grid


* Flow : User account image–>Global Settings–> Authentication Logs


* Keyword Usage

> 
> * `Get Authentication Logs Auth Method   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – Row Search String i.e client mac or user name



* **Returns**

    Authentication Logs Authentication Method Field Text



#### get_authentication_logs_client_detail(search_string)

* Get the Client Details on authentication Logs grid


* Keyword Usage

> 
> * `Get Authentication Logs Client Detail   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – Row Search String i.e client mac or user name



* **Returns**

    Authentication Logs callingStationId Field Text



#### get_authentication_logs_date(search_string)

* Get the date Field on authentication Logs grid


* Flow : User account image–>Global Settings–> Authentication Logs


* Keyword Usage

> 
> * `Get Authentication Logs Date   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – Row Search String i.e client mac or user name



* **Returns**

    Authentication Logs AuthDate Field Text



#### get_authentication_logs_details(search_string, search_filter=None)

* Filter the logs based on the Filter arguments Allowed Filters are: Client or user name


* Gets all authentication details from the row


* Flow : User account image–>Global Settings–> Authentication Logs


* Keyword Usage

> 
> * `Get Authentication Logs Details   ${SEARCH_STRING}    ${SEARCH_FILTER`


* **Parameters**

    
    * **search_filter** – filter string


    * **search_string** – row search string i.e client mac or user name



* **Returns**

    authentication details dict



#### get_authentication_logs_row(search_string)

* Get the Authentication Logs from Global Settings Page


* Flow : User account image–>Global Settings–> Authentication Logs


* Keyword Usage

> 
> * `Get Authentication Logs Row   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell
    example search_string be like user_name, auth_type,client etc



* **Returns**

    row element if row exists else return None



#### get_authentication_logs_ssid(search_string)

* Get the ssid Field on authentication Logs grid


* Keyword Usage

> 
> * `Get Authentication Logs SSID   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – Row Search String i.e client mac or user name



* **Returns**

    Authentication Logs SSID Field Text



#### get_authentication_logs_username(search_string)

* Get the username Field on authentication Logs grid


* Flow : User account image–>Global Settings–> Authentication Logs


* Keyword Usage

> 
> * `Get Authentication Logs Username   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – Row Search String i.e client mac or user name



* **Returns**

    Authentication Logs User Name Field Text



#### get_opt_out_status_copilot_beta()

* Get Opt out of Copilot beta status


* Flow : User account image–>Global Settings–> Account Details–> Opt-out of Copilot BETA


* Keyword Usage

> 
> * `Get Opt Out Status Copilot BETA`


* **Returns**

    Current status(Enable/Disable) of opt-out Copilot BETA



#### get_supplemental_cli_option(option)

* This Keyword will Enable/Disable Supplemental CLI in Global Settings


* Flow : User account image–>Global Settings–> VIQ Management


* Keyword Usage

> 
> * `Get supplemental cli option     ${OPTION}`


* **Parameters**

    **option** – Choose an option for supplemental CLI “enable””disable”



* **Returns**

    1 If setting option Supplemental_cli is Successful



#### reset_viq_data()

* This Keyword will Delete the VIQ Data


* Flow : User account icon–>Global Settings–> VIQ Management —> Reset VIQ


* Keyword Usage:

> 
> * \`\` Reset VIQ \`\`


* **Returns**

    1 after successfully Resetting VIQ data else -1



#### search_organization_name(organization_name)

* Search the Organization Name From Global Settings Page


* Flow : User account image–>Global Settings–> Organization


* Keyword Usage

> 
> * `Search Organization Name   ${ORGANIZATION_NAME}`


* **Parameters**

    **organization_name** – Name of the Organization



* **Returns**

    1 If Organization found on Grid else -1



#### set_opt_out_copilot_beta(option)

* Enable/Disable Opt out of Copilot BETA


* Flow : User account image–>Global Settings–> Account Details–> Opt-out of copilot BETA


* Keyword Usage

> 
> * `Set Opt Out Copilot BETA     ${OPTION}`


* **Parameters**

    **option** – option to enable/disable Opt out of Copilot BETA



* **Returns**

    1 If setting opt_out of Copilot BETA is Successful



#### set_vertical(industry_type)

* This Keyword will set Industry type on xiq side


* Flow : User account icon–>Global Settings–> Account Details —> Industry


* Keyword Usage:

> 
> * \`\` Reset VIQ \`\`


* **Returns**

    1 after successfully Resetting VIQ data else -1


## extauto.xiq.flows.globalsettings.LicenseManagement module


### _class_ extauto.xiq.flows.globalsettings.LicenseManagement.LicenseManagement()
Bases: `LicenseManagementWebElements`


#### confirm_entitlements_table_contains_data()
> 
> * Checks if the Entitlements table contains data.


> * Assumes the License Management page is already being displayed.


> * Keyword Usage

> > 
> > * `Confirm Entitlements Table Contains Data`


* **Returns**

    1 if Entitlements Table is not empty, else -1



#### confirm_legacy_table_contains_data()
> 
> * Checks if the Legacy Entitlements table contains data.


> * Assumes the License Management page is already being displayed.


> * Keyword Usage

> > 
> > * `Confirm Legacy Table Contains Data`


* **Returns**

    1 if Legacy Entitlements Table is not empty, else -1



#### get_entitlement_activated_count_for_feature(feature='PRD-XIQ-PIL-S-C')

* Gets the entitlement “Activated” value for the specified feature.


* Keyword Usage:

> 
> * `${COUNT}=   Get Entitlement Activated Count For Feature`


> * `${COUNT}=   Get Entitlement Activated Count For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNT}=   Get Entitlement Activated Count For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNT}=   Get Entitlement Activated Count For Feature    PRD-XIQ-NAC-S`


* **Parameters**

    **feature** – feature to return the activated count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S



* **Returns**

    total number of activated licenses for the specified feature



#### get_entitlement_available_count_for_feature(feature='PRD-XIQ-PIL-S-C')

* Gets the entitlement “Available” value for the specified feature.


* Keyword Usage:

> 
> * `${COUNT}=   Get Entitlement Available Count For Feature`


> * `${COUNT}=   Get Entitlement Available Count For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNT}=   Get Entitlement Available Count For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNT}=   Get Entitlement Available Count For Feature    PRD-XIQ-NAC-S`


* **Parameters**

    **feature** – feature to return the available count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S



* **Returns**

    total number of available licenses allotted to the specified feature



#### get_entitlement_counts_for_feature(feature='PRD-XIQ-PIL-S-C')

* Returns counts of the specified feature from the Entitlements table as a dictionary


* Keyword Usage

> 
> * `${COUNTS}=   Get Entitlement Counts For Feature`


> * `${COUNTS}=   Get Entitlement Counts For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNTS}=   Get Entitlement Counts For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNTS}=   Get Entitlement Counts For Feature    PRD-XIQ-NAC-S`


* **Returns**

    Returns counts for the specified feature from the Entitlements table as a dictionary



#### get_entitlement_device_count_for_feature(feature='PRD-XIQ-PIL-S-C')

* Gets the entitlement “Devices” value for the specified feature.


* Keyword Usage:

> 
> * `${COUNT}=   Get Entitlement Device Count For Feature`


> * `${COUNT}=   Get Entitlement Device Count For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNT}=   Get Entitlement Device Count For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNT}=   Get Entitlement Device Count For Feature    PRD-XIQ-NAC-S`


* **Parameters**

    **feature** – feature to return the device count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S



* **Returns**

    total number of devices allotted to the specified feature



#### initiate_link_xiq_to_extr_portal_from_lic_mgt(sfdc_user_type=None, sfdc_email=None, sfdc_pwd=None, shared_cuid=None)
> 
> * links XIQ to extreme SFDC portal to get gemalto licenses


> * pass the below parameters as the keyword input:


> * sfdc user type (customer or parter)


> * sfdc customer/partner login email and password


> * shared cuid if parter login is used


* **Returns**

    1 linking is successful , else -1



#### is_entitlements_table_empty()
> 
> * Checks if the Entitlements table is empty.


> * Assumes the License Management page is already being displayed.


> * Keyword Usage

> > 
> > * `Is Entitlements Table Empty`


* **Returns**

    1 if Entitlements Table is empty (“No records found.” is displayed), else -1



#### is_legacy_table_empty()
> 
> * Checks if the Legacy Entitlements table is empty.


> * Assumes the License Management page is already being displayed.


> * Keyword Usage

> > 
> > * `Is Legacy Table Empty`


* **Returns**

    1 if Legacy Entitlements Table is empty (“No data” is displayed), else -1



#### navigate_and_get_entitlement_activated_count_for_feature(feature='PRD-XIQ-PIL-S-C')

* Gets the entitlement “Activated” count for the specified feature.


* Keyword Usage:

> 
> * `${COUNT}=   Navigate and Get Entitlement Activated Count For Feature`


> * `${COUNT}=   Navigate and Get Entitlement Activated Count For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNT}=   Navigate and Get Entitlement Activated Count For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNT}=   Navigate and Get Entitlement Activated Count For Feature    PRD-XIQ-NAC-S`


* **Parameters**

    **feature** – feature to return the activated count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S



* **Returns**

    total number of activations allotted to the specified feature



#### navigate_and_get_entitlement_available_count_for_feature(feature='PRD-XIQ-PIL-S-C')

* Gets the entitlement “Available” count for the specified feature.


* Keyword Usage:

> 
> * `${COUNT}=   Navigate and Get Entitlement Available Count For Feature`


> * `${COUNT}=   Navigate and Get Entitlement Available Count For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNT}=   Navigate and Get Entitlement Available Count For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNT}=   Navigate and Get Entitlement Available Count For Feature    PRD-XIQ-NAC-S`


* **Parameters**

    **feature** – feature to return the available count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S



* **Returns**

    total number of available licenses allotted to the specified feature



#### navigate_and_get_entitlement_counts_for_feature(feature='PRD-XIQ-PIL-S-C')

* Navigates to the License Management page and returns counts from the Entitlements table as a dictionary.


* Keyword Usage:

> 
> * `${COUNTS}=   Navigate and Get Entitlement Counts For Feature`


> * `${COUNTS}=   Navigate and Get Entitlement Counts For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNTS}=   Navigate and Get Entitlement Counts For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNTS}=   Navigate and Get Entitlement Counts For Feature    PRD-XIQ-NAC-S`


* **Returns**

    Returns counts from the Entitlements table as a dictionary



#### navigate_and_get_entitlement_device_count_for_feature(feature='PRD-XIQ-PIL-S-C')

* Gets the entitlement “Device Count” for the specified feature.


* Keyword Usage:

> 
> * `${COUNT}=   Navigate and Get Entitlement Device Count For Feature`


> * `${COUNT}=   Navigate and Get Entitlement Device Count For Feature    PRD-XIQ-PIL-S-C`


> * `${COUNT}=   Navigate and Get Entitlement Device Count For Feature    PRD-XIQ-NAV-S-C`


> * `${COUNT}=   Navigate and Get Entitlement Device Count For Feature    PRD-XIQ-NAC-S`


* **Parameters**

    **feature** – feature to return the device count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S



* **Returns**

    total number of devices allotted to the specified feature



#### open_license_management_page()
> 
> * Navigates to License Management Page


> * Flow : User account image–>Global Settings–> License Management


> * Keyword Usage

> > 
> > * `Open License Management Page`


* **Returns**

    1 if License Management page was opened, else -1



#### unlink_xiq_from_extr_portal()
> 
> * Unlink XIQ from extreme portal


* **Returns**

    1 if unlinked else -1



#### verify_contact_sales_btn_dispalyed()

* **Returns**

    contact sales button must be displayed



#### verify_ek_in_legacy_ek_table(ekey)
> 
> * Checks if legacy ek exists in the legacy ek table


> * pass the ek as input parameter to verify the ek to be checked


* **Returns**

    1 if ek exists , else -1



#### verify_xiq_linked_to_extr_portal()
verify XIQ is linked to extreme portal
:return:


#### verify_xiq_not_linked_to_extr_portal()
verify XIQ is not linked to extreme portal
:return:


#### wait_until_entitlement_activated_count_for_feature_matches(expected, feature='PRD-XIQ-PIL-S-C', retry_duration=30, retry_count=30)

* This keyword is used to wait until the activated count for the specified license entitlement matches the


* expected value.


* 
* Keyword Usage:

> 
> * `Wait Until Entitlement Activated Count For Feature Matches    1`


> * `Wait Until Entitlement Activated Count For Feature Matches    0  feature=PRD-XIQ-NAV-S-C`


> * `Wait Until Entitlement Activated Count For Feature Matches    3  retry_duration=10    retry_count=12`


> * `Wait Until Entitlement Activated Count For Feature Matches    2  feature=PRD-XIQ-PIL-S-C    retry_duration=60    retry_count=5`


> * `Wait Until Entitlement Activated Count For Feature Matches    1  feature=PRD-XIQ-NAV-S-C    retry_duration=30    retry_count=10`


> * `Wait Until Entitlement Activated Count For Feature Matches    1  feature=PRD-XIQ-NAC-S      retry_duration=15    retry_count=8`


* **Parameters**

    
    * **expected** – expected number of activated licenses for specified license entitlement feature


    * **feature** – type of license entitlement to check the activated count of (e.g., PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if activated count for feature matches within time, else -1



#### wait_until_entitlement_available_count_for_feature_matches(expected, feature='PRD-XIQ-PIL-S-C', retry_duration=30, retry_count=30)

* This keyword is used to wait until the available count for the specified license entitlement matches the


* expected value.


* 
* Keyword Usage:

> 
> * `Wait Until Entitlement Available Count For Feature Matches    1`


> * `Wait Until Entitlement Available Count For Feature Matches    0  feature=PRD-XIQ-NAV-S-C`


> * `Wait Until Entitlement Available Count For Feature Matches    3  retry_duration=10    retry_count=12`


> * `Wait Until Entitlement Available Count For Feature Matches    2  feature=PRD-XIQ-PIL-S-C    retry_duration=60    retry_count=5`


> * `Wait Until Entitlement Available Count For Feature Matches    1  feature=PRD-XIQ-NAV-S-C    retry_duration=30    retry_count=10`


> * `Wait Until Entitlement Available Count For Feature Matches    1  feature=PRD-XIQ-NAC-S      retry_duration=15    retry_count=8`


* **Parameters**

    
    * **expected** – expected number of available licenses for specified license entitlement feature


    * **feature** – type of license entitlement to check the available count of (e.g., PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if available count for feature matches within time, else -1



#### wait_until_entitlement_counts_for_feature_matches(feature, expected_available, expected_activated, expected_devices, retry_duration=30, retry_count=30)

* This keyword is used to wait until the entitlement counts (Available, Activated, Devices) for the specified


* feature match the expected value.


* 
* Keyword Usage:

> 
> * `Wait Until Entitlement Counts For Feature Matches    PRD-XIQ-PIL-S-C    9    1       1`


> * `Wait Until Entitlement Counts For Feature Matches    PRD-XIQ-NAV-S-C    2    0       0`


> * `Wait Until Entitlement Counts For Feature Matches    PRD-XIQ-NAC-S      0    1000    1000`


* **Parameters**

    
    * **feature** – type of license entitlement to check the counts of (PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)


    * **expected_available** – expected value for the “Available” column for the specified license entitlement feature


    * **expected_activated** – expected value for the “Activated” column for the specified license entitlement feature


    * **expected_devices** – expected value for the “Devices” column for the specified license entitlement feature


    * **retry_duration** – duration between each retry


    * **retry_count** – number of times to retry



* **Returns**

    1 if counts for feature matches within time, else -1



#### wait_until_entitlement_device_count_for_feature_matches(expected, feature='PRD-XIQ-PIL-S-C', retry_duration=30, retry_count=30)

* This keyword is used to wait until the device count for the specified license entitlement matches the


* expected value.


* 
* Keyword Usage:

> 
> * `Wait Until Entitlement Device Count For Feature Matches    1`


> * `Wait Until Entitlement Device Count For Feature Matches    0  feature=PRD-XIQ-NAV-S-C`


> * `Wait Until Entitlement Device Count For Feature Matches    3  retry_duration=10    retry_count=12`


> * `Wait Until Entitlement Device Count For Feature Matches    2  feature=PRD-XIQ-PIL-S-C    retry_duration=60    retry_count=5`


> * `Wait Until Entitlement Device Count For Feature Matches    1  feature=PRD-XIQ-NAV-S-C    retry_duration=30    retry_count=10`


> * `Wait Until Entitlement Device Count For Feature Matches    1  feature=PRD-XIQ-NAC-S      retry_duration=15    retry_count=8`


* **Parameters**

    
    * **expected** – expected number of devices for specified license entitlement feature


    * **feature** – type of license entitlement to check the device count of (e.g., PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)


    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if device count for feature matches within time, else -1



#### wait_until_entitlements_table_empty(retry_duration=30, retry_count=30)

* This keyword is used to wait until the Entitlements table is empty.


* 
* Keyword Usage:

> 
> * `Wait Until Entitlements Table Empty`


> * `Wait Until Entitlements Table Empty    retry_duration=10    retry_count=12`


> * `Wait Until Entitlements Table Empty    retry_duration=60`


> * `Wait Until Entitlements Table Empty    retry_count=10`


* **Parameters**

    
    * **retry_duration** – duration between each retry


    * **retry_count** – retry count



* **Returns**

    1 if Entitlements table is empty within time, else -1


## extauto.xiq.flows.globalsettings.PasswordReset module

## Module contents
