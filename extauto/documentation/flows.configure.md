# xiq configure package

## Submodules

## extauto.xiq.flows.configure.AdditionalSettings module

## extauto.xiq.flows.configure.AutoProvisioning module


### _class_ extauto.xiq.flows.configure.AutoProvisioning.AutoProvisioning()
Bases: `object`


#### auto_provision_advanced_settings(\*\*advance_setting)

* This keyword creates auto provision advanced settings


* Keyword Usage:

> 
> * `Auto Provision Advanced Settings   &{APP_CONFIG_DICTIONARY}`


* **Param**

    upload_firmware,upload_configuration,reboot,Firmware_version



* **Returns**

    None



#### auto_provision_basic_settings(policy_name, country_code=None, \*\*auto_provision_profile)

* This keyword creates auto provision basic settings


* Keyword Usage:

> 
> * `Auto Provision Basic Settings    ${APP_POLICY_NAME}    ${AP_COUNTRY}    &{APP_CONFIG_DICTIONARY}`


* **Parameters**

    
    * **policy_name** – app policy name


    * **country_code** – country code


    * **auto_provision_profile** – policy_name, device_function, device_model, service_tags, ip sub networks,



* network_policy,country_code


* **Returns**

    1 if success else -1



#### auto_provision_capwap_configurations(\*\*capwap_configuration)

* This keyword creates auto provision CAPWAP configuration


* Keyword Usage:

> 
> * `Auto Provision capwap configurations &{CAPWAP_CONFIGURATION_DICTIONARY}`


* **Param**

    capwap_configuration: CAPWAP configuration values



* **Returns**

    None



#### auto_provision_device_credential(\*\*device_credential)

* This keyword adds auto provision device credentials if status is enabled on device_credential dictionary


* Keyword Usage:

> 
> * `Auto Provision Device Credential  &{DEVICE_CREDENTIAL_DICTIONARY}`


* **Param**

    device credentials dict : device_credential,root_admin_name,root_admin_password,read_only_admin_name,
    read_only_admin_password



* **Returns**

    None



#### auto_provision_enable_policy_row(policy_name)

* Enables a auto provision policy


* Keyword Usage:

> 
> * `Auto Provision Enable Policy Row   ${APP_POLICY_NAME}`


* **Param**

    auto provision policy name which is to be searched



* **Returns**

    None



#### choose_auto_provision_country_code(country_code)

* This keyword chooses auto provision country


* Keyword Usage

> 
> * `Choose Auto Provision Country Code   ${COUNTRY_CODE}`


* **Param**

    country_code : Country Code to Configure for Auto Provisioning Policy



* **Returns**

    1 if Country Code Successfully configured else -1



#### choose_auto_provision_device_function(device_function)

* This keyword chooses auto provision device function


* Keyword Usage

> 
> * `Choose Auto Provision Device Function   ${DEVICE_FUNCTION}`


* **Param**

    device_function : device function to be selected



* **Returns**

    1 if Device Function Selected Successfully else -1



#### choose_auto_provision_device_model(dev_model, device_function)

* This keyword chooses auto provision device model


* Keyword Usage

> 
> * `Choose Auto Provision Device Model   ${DEVICE_PLATFORM}   ${DEVICE_FUNCTION}`


* **Param**

    device model : Device Platform



* **Param**

    device function : Device Function Name ie AP,Switches


:return:None


#### choose_auto_provision_network_policy(network_policy)

* This keyword chooses auto provision network policy


* Keyword Usage

> 
> * `Choose Auto Provision Network Policy   ${NETWORK_POLICY_NAME}`


* **Param**

    network policy : Network Policy Name to be apply for autoprovision policy



* **Returns**

    None



#### delete_all_auto_provision_policies(\*\*kwargs)

* Delete all Auto Provisioning Policies


* Keyword Usage

> 
> * `Delete All Auto Provision Policies`


* **Returns**

    1 if successfully deleted All Auto Provisioning Policies else -1



#### delete_auto_provisioning_policy(policy_name)

* Delete a Auto Provisioning Policy


* Keyword Usage

> 
> * `Delete Auto Provisioning Policy   ${APP_NAME}`


* **Parameters**

    **policy_name** – Auto Provisioning policy Name



* **Returns**

    1 if successfully deleted Auto Provisioning Policy else -1



#### enter_auto_provision_policy_name(policy_name)

* This keyword uses to configure Auto Provisioning Policy Name


* Keyword Usage

> 
> * `Enter Auto Provision Policy Name   ${APP_NAME}`


* **Param**

    policy_name : Auto Provisioning Policy Name



* **Returns**

    None



#### get_auto_provision_policy_count()

* Returns the count of auto provision policies


* Keyword Usage

> 
> * `Get Auto Provision Policy Count`


* **Returns**

    number of auto provision policies



#### goto_auto_provisioning_policy()

* navigates to auto provisioning policy page


* Keyword Usage

> 
> * `Goto Auto Provisioning Policy`


* **Returns**

    1 if Navigate to Auto Provisioning Policy Successful else None



#### save_and_enable_auto_provision_policy(policy_name)

* This keyword saves and enables auto provision profile


* Keyword Usage:

> 
> * `Save and Enable Auto Provision Policy   ${APP_POLICY_NAME}`


* **Param**

    policy_name : auto provision policy name



* **Returns**

    None



#### search_auto_provisioning_policy(policy_name)

* Search a Auto Provisioning Policy


* Keyword Usage

> 
> * `Search Auto Provisioning Policy   ${APP_NAME}`


* **Parameters**

    **policy_name** – Auto Provision Policy



* **Returns**

    1 if Auto Provision Policy found On Grid else -1



#### verify_auto_provision_policy_update(serial, country_code='NA', \*\*auto_provision_policy)

* This keyword verifies if the device is updated with auto configuration policy


* Keyword Usage

> 
> * `verify auto provision_policy_update   ${NETWORK_POLICY_NAME}`


* **Param**

    serial : serial number of device



* **Param**

    auto_provision_policy: (Config Dict) device_function(AP or Switch), network_policy_name



* **Returns**

    1 Auto Provision Policy Update Successful else -1


## extauto.xiq.flows.configure.ClassificationRule module


### _class_ extauto.xiq.flows.configure.ClassificationRule.ClassificationRule()
Bases: `object`


#### add_classification_rule_to_ssid(policy_name, ssid_name, classification_rule)

* Flow: Configure –> NetworkPolicy –> Click Policy –> Wireless Networks -> assign classification rule to ssid


* Select Classification Rule for the mentioned SSiD


* Keyword Usage

`Add Classification Rule to SSID     ${Network_Policy}        ${SSiD_Name}        ${Classification_Rule}`


* **Parameters**

    
    * **policy_name** – Name of the Network Policy


    * **ssid_name** – Name of the SSiD


    * **classification_rule** – Classification Rule to be attached to SSiD



* **Returns**

    1 if success else -1



#### add_classification_rule_with_ccg(name, description, match_type_flag, ccg_policy)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Create Classification Rule with Cloud Config Group Policy


* Keyword Usage

`Add Classification Rule with CCG      ${RULE_NAME}        ${RULE_DESCRIPTION}    ${match_type}    ${CLOUD_CONFIG_GROUP_POLCIY}`


* **Parameters**

    
    * **name** – Name of the Classification Rule


    * **description** – Description of the Classification Rule


    * **match_type_flag** – YES = (default) match based on ‘Contains’ NOT = match based on “Does Not Contain”


    * **ccg_policy** – Cloud Config Group Policy Name



* **Returns**

    1 if created else -1



#### add_classification_rule_with_ip(name, description, option, \*\*ip_object_rule)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Create Classification Rule Based on AP’s IP , Subnet or Range


* Keyword Usage

`Add Classification Rule with IP      ${RULE_NAME}        ${RULE_DESCRIPTION}    ${Option}     &{IP_RULE_DETAILS}`


* **Parameters**

    
    * **name** – Name of the Classification Rule


    * **description** – Description of the Classification Rule


    * **option** – Option for the IP Rule, which can be IP, Subnet or Range


    * **ip_object_rule** – IP Rule Details



* **Returns**

    1 if created else -1



#### add_classification_rule_with_location(name, description, \*\*location)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Create Classification Rule Based on AP Location


* Keyword Usage

`Add Classification Rule with Location      ${RULE_NAME}        ${RULE_DESCRIPTION}        &{LOCATION_OF_AP}`


* **Parameters**

    
    * **name** – Name of the Classification Rule


    * **description** – Description of the Classification Rule


    * **location** – Location of the AP



* **Returns**

    1 if created else -1



#### check_classification_rule_to_ssid(policy_name, ssid_name, classification_rule)

* Flow: Configure –> NetworkPolicy –> Click Policy –> Wireless Networks -> Check classification rule to ssid


* This Method Verifies if the Correct Classification Rule is attached to the SSiD


* Keyword Usage

`Check Classification Rule to SSID     ${Network_Policy}        ${SSiD_Name}        ${Classification_Rule}`


* **Parameters**

    
    * **policy_name** – Name of the Network Policy


    * **ssid_name** – Name of the SSiD


    * **classification_rule** – Classification Rule to be attached to SSiD



* **Returns**

    1 if correct classification Rule attached else -1



#### delete_classification_rules(\*names)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Select Multiple Classification Rule and Click on Delete


* Keyword Usage

> 
> * `Delete Classification rules      ${Classification_Rule_NAME}`


* **Parameters**

    **names** – Name of the Classification Rule



* **Returns**

    1 if created else return -1



#### delete_single_classification_rule(name)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Select Single Classification Rule and Click on Delete


* Keyword Usage

> 
> * `Delete Single Classification rule      ${Classification_Rule_NAME}`


* **Parameters**

    **name** – Name of the Classification Rule



* **Returns**

    1 if created else return -1



#### remove_classification_rule_from_ssid(policy_name, ssid_name, classification_rule)

* Flow: Configure –> NetworkPolicy –> Click Policy –> Wireless Networks -> remove classification rule to ssid


* Remove Classification Rule for the mentioned SSiD


* Keyword Usage

`Remove Classification Rule From SSID     ${Network_Policy}        ${SSiD_Name}        ${Classification_Rule}`


* **Parameters**

    
    * **policy_name** – Name of the Network Policy


    * **ssid_name** – Name of the SSiD


    * **classification_rule** – Classification Rule to be attached to SSiD



* **Returns**

    1 if success else -1



#### search_classification_rule(name)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Search Single Classification Rule


* Keyword Usage

> 
> * `Search Classification rule      ${Classification_Rule_NAME}`


* **Parameters**

    **name** – Name of the Classification Rule



* **Returns**

    1 if found else return -1



#### select_classification_rule(name)

* Flow: Configure –> Common Objects –> Policy –> Classification Rule


* Select Single Classification Rule


* Keyword Usage

> 
> * `Select Classification rule      ${Classification_Rule_NAME}`


* **Parameters**

    **name** – Name of the Classification Rule



* **Returns**

    1 if able to select else return -1


## extauto.xiq.flows.configure.CloudConfigGroup module


### _class_ extauto.xiq.flows.configure.CloudConfigGroup.CloudConfigGroup()
Bases: `object`


#### add_cloud_config_group(policy, description, \*ap_serials)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group


* Create Cloud Config Group and include APs to the group


* Same Keyword can be used to add single or multiple APs to the CCG Group


* Keyword Usage

> 
> * `Add Cloud Config Group      ${CCG_NAME}        ${CCG_DESCRIPTION}        ${AP_SERIAL}`


* **Parameters**

    
    * **policy** – Name of the CCG Group


    * **description** – Description of the Group


:param ap_serials:[List] Single or multiple APs who are members of the Group
:return: 1 if created else -1, -2, -3 depending on the error received.


#### add_cloud_config_group_from_manage(policy, description, \*ap_serials)

* Flow: Manage –> Devices –> Select AP -> Actions -> Add to CLoud Config Group


* Create Cloud Config Group and include APs to the group


* Keyword Usage

> 
> * `Add Cloud Config Group From Manage     ${CCG_NAME}        ${CCG_DESCRIPTION}        ${AP_SERIAL}`


* **Parameters**

    
    * **policy** – Name of the CCG Group


    * **description** – Description of the Group


    * **ap_serials** – Serial number of the AP who is member of the Group



* **Returns**

    1 if created else -1



#### assign_cloud_config_group(policy_name=None, update_method='Delta', option='Continue', \*ap_serials)

* By default this keyword do delta config push


* Go To MANAGE–>Devices–>Select AP row  to apply the CCG policy


* Actions–>Add to Cloud Config group –>Select the CCG policy to assign


* select AP–>Continue


* Keyword Usage:

> 
> * `assign cloud config group       ${CCG_NAME}        ${Update_method}       ${Option}      ${AP_SERIAL}`


* **Parameters**

    
    * **policy_name** – name of the CCG Policy


    * **update_method** – Perform Complete update or delta update


    * **option** – Continue/Cancel assign CCG Policy to AP


    * **ap_serial** – serial number of the ap to select



* **Returns**

    1 if policy is updated else -1



#### create_bulk_cloud_config_group(policy_name, ap_serial, num)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group


* Create Cloud Config Group and include AP to the group


* This Keyword is used to create CCG in bulk.


* Keyword Usage

> 
> * `Create Bulk Cloud Config Group      ${CCG_NAME}        ${AP_SERIAL}        ${NUMBER_of_CCG_Policy}`


* **Parameters**

    **policy_name** – Name of the CCG Group


:param ap_serial:AP who are members of the Group
:param num: Number of the CCG Policy to be configured
:return: 1 if created else -1


#### delete_bulk_cloud_config_group(policy_name, num)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group


* Delete Cloud Config Group


* This Keyword is used to delete CCG in bulk.


* Keyword Usage

> 
> * `Delete Bulk Cloud Config Group      ${CCG_NAME}        ${AP_SERIAL}        ${NUMBER_of_CCG_Policy}`


* **Parameters**

    
    * **policy_name** – Name of the CCG Group


    * **num** – Number of the CCG Policy to be configured



* **Returns**

    1 if created else -1



#### delete_cloud_config_group(policy)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group


* Select Cloud Config Group and Click on Delete


* Keyword Usage

> 
> * `Delete Cloud Config Group      ${CCG_NAME}`


* **Parameters**

    **policy** – Name of the CCG Group



* **Returns**

    1 if created else return -1



#### delete_cloud_config_groups(\*policys)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group


* Select Cloud Config Group and Click on Delete


* Keyword Usage

> 
> * `Delete Cloud Config Groups      ${CCG_NAMES}`


* **Parameters**

    **policys** – Names of the CCG Group



* **Returns**

    1 if created else return -1



#### device_ccg_members(device_serial)
This keyword is used to get the list of CLoud Config Groups that the AP is member of
- Keyword Usage:

> 
> * `Device CCG Members     ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial_number of the AP



* **Returns**

    List of Cloud Config Groups that the AP is attached to



#### edit_cloud_config_group(policy, option='add', \*ap_serials)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group


* Select Cloud Config Group and Click on Edit


* Same Keyword can be used to add/remove single or multiple APs to the CCG Group


* Keyword Usage

> 
> * `Edit Cloud Config Group      ${CCG_NAME}        ${Option}        ${AP_SERIAL}`


* **Parameters**

    
    * **policy** – Name of the CCG Group


    * **option** – Whether to add new APs or remove AP from the CCG Group.


:param ap_serials:[List] Single or multiple APs who are members of the Group
:return: 1 if created else return -1


#### get_ccg_group_members(policy)
This keyword is used to get the list of  APs which are members of the CCG Policy
- Keyword Usage:

> 
> * `Get CCG Group Members   ${POLICY_NAME}`


* **Parameters**

    **policy** – CCG Policy



* **Returns**

    List of APs that are member of CCG Policy



#### search_ccg_group_from_common_object(policy)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group

This keyword Checks if the CCG Policy is available in CCG List
:param policy: CCG Policy name
:return: 1 if found else -1


#### select_ap_for_ccg(ap_serial)

* Selects the AP row marching with AP’s Serial Number


* Keyword USage:

> 
> * `Select AP For CCG   ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – AP’s Serial Number



* **Returns**

    return 1 if AP found and selected else -1



#### select_ap_for_ccg_manage_page(ap_serial)

* Selects the AP row marching with AP’s Serial Number


* Keyword USage:

> 
> * `Select AP For CCG Manage Page   ${AP_SERIAL}`


* **Parameters**

    **ap_serial** – AP’s Serial Number



* **Returns**

    return 1 if AP found and selected else -1



#### select_ccg_group_from_common_object(policy)

* Flow: Configure –> Common Objects –> Policy –> Cloud Config Group

This keyword Selects if the CCG Policy is available in CCG List
:param policy: CCG Policy name
:return: 1 if found else -1

## extauto.xiq.flows.configure.CommonObjects module


### _class_ extauto.xiq.flows.configure.CommonObjects.CommonObjects()
Bases: `object`


#### add_ap_template_from_common_object(ap_model, ap_template_name, \*\*wifi_interface_config)
”
- CONFIGURE–>COMMON OBJECTS–>Policy–>AP Templates
- Adding AP Template in Common Object
- Checking the AP template presence in the AP Templates Grid
- If it is not there add New AP Template
- Keyword Usage

> 
> * `Add AP Template From Common Object   ${AP_MODEL}   ${AP_TEMPLATE_NAME}     &{AP_TEMPLATE_CONFIG}`


* **Parameters**

    
    * **ap_model** – Model of the AP like AP630, AP410C etc


    * **ap_template_name** – AP Template Name ie AP630-TEMPLATE,AP410C-TEMPLATE etc


    * **wifi_interface_config** – (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor etc



* **Returns**

    1 if AP Template Configured Successfully else -1



#### add_imago_tag_profile(profile_name, server='', channel='', fcc_mode=True, server_port='default')

* This keyword will create image Tag profile under Common Objects.


* Flow: Configure –> Common Objects –> Policy –>ImagoTag Profiles


* Keyword Usage:

> 
> * `Add Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL}`


> * `Add Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL} server_port=${PORT}`


> * `Add Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL}  fcc_mode=False`


* **Parameters**

    
    * **profile_name** – Imago Tag Profile name


    * **channel** – Channel Number


    * **server** – Server detail


    * **fcc_mode** – By default fcc_mode is enabled.To Disable mention this flag as False


    * **server_port** – Server Port Details



* **Returns**

    1 if Imago Tag Profile name Created successfully else -1



#### add_ip_object_hostname_with_ip_network(name, type, global_network, netmask, \*classify_network)

* Flow: Configure –> Common Objects –> Basic –> IP Objects / HostName –> Click + to add an ip object profile with Networks


* Create ip object profile with ip networks


* Keyword Usage:

    
        * `Add IP Object Hostname With IP Network    ${name}     ${type}     ${global_network}     ${netmask}    @{classify_network}`


* **Parameters**

    
    * **name** – The profile name


    * **type** – “Network”, or “Wildcard”


    * **global_network** – Unclassified Network, or unclassified Wildcard network


    * **netmask** – Netmask


    * **\*classify_network** – Classified network list, or classified wildcard network list




* **Returns**

    success return 1



#### add_ip_object_hostname_with_ip_or_hostname(name, type, global_item, \*classify_items)

* Flow: Configure –> Common Objects –> Basic –> IP Objects / HostName –> Click + to add an ip object profile with IP Address


* Create ip object profile with ip address


* Keyword Usage:

    
        * `Add IP Object Hostname With IP or Hostname     ${name}     ${type}     ${global_item}    @{classify_items}`


* **Parameters**

    
    * **name** – The profile name


    * **type** – “IP Address”, or “Host Name”, or “Wildcard Host Name”


    * **global_item** – Unclassified IP address, or unclassified Hostname, or unclassified wildcard hostname


    * **\*classify_items** – Classified IP address list, or classified Hostname list, or classified wildcard hostname list




* **Returns**

    success return 1 else return -1



#### add_ip_object_hostname_with_ip_range(name, global_range_start, ip_range_gap, \*classify_range_start)

* Flow: Configure –> Common Objects –> Basic –> IP Objects / HostName –> Click + to add an ip object profile with IP Range


* Create ip object profile with IP Range


* Keyword Usage:

    
        * `Add IP Object Hostname With IP Range    ${name}     ${global_range_start}       ${ip_range_gap}     @{classify_range_start}`


* **Parameters**

    
    * **name** – The profile name


    * **global_range_start** – The unclassified start IP address


    * **ip_range_gap** – 
        * The gap flag between start IP and end IP.


        * For example:


        * start IP is 192.168.1.1, the gap is 00, and the end IP is 192.168.1.100


        * end IP = string “192.168.1.1” + string “00” = string “192.168.1.100”



    * **classify_range_start** – Classified start IP list



* **Returns**

    success return 1



#### add_network_management_options(option_name='management_option_1', enable_legacy_http_redirect='True')

* Adds new network management option(s)

-Flow: Configure –> Common Objects –> Network –>Management Options

    
    * Keyword Usage:

    > 
    > * `Add Network Management Options`

:param option_name : name of the management option
:param enable_legacy_http_redirect: determines if enable legacy http redirect should be clicked or not
:return: 1


#### check_ap_template_in_common_object(ap_template_name)
”
- CONFIGURE–>COMMON OBJECTS–>Policy–>AP Templates
- Checking the AP template presence in the AP Templates Grid
- Keyword Usage

> 
> * `Check AP Template In Common Object   ${AP_TEMPLATE_NAME}`


* **Parameters**

    **ap_template_name** – AP Template Name ie AP630-TEMPLATE,AP410C-TEMPLATE etc



* **Returns**

    1 if AP Template Found else -1



#### clone_open_ssid_in_common_objects(ssid_name, clone_ssid_name)

* Flow: Configure –> Common Objects –> Policy –>SSIDs


* Clone Open SSID from the Existing ssid grid


* Keyword Usage:

> 
> * `Clone Open SSID In Common Objects  ${SSID_NAME}  ${CLONE_SSID_NAME}`


* **Parameters**

    
    * **ssid_name** – Copy of SSID to clone


    * **clone_ssid_name** – Clone SSID name



* **Returns**

    1 if Cloned Open SSID Successfully else -1



#### create_ip_firewall_policy_for_applications(policy_name, application='', source_ip='Any', destination_ip='Any', action='Permit')
> 
> * This Keyword will Create IP Firewall Policy for Application Access.


> * Flow: Configure –> Common Objects –> Security –>IP Firewall Policies –> Add


> * Keyword Usage:

> > 
> > * `Create IP Firewall Policy For Applications    ${POLICY_NAME}  application=${APP_NAME}  action=${ACTION}`


> > * 

> > ```
> > ``
> > ```

> > Create IP Firewall Policy For Applications    ${POLICY_NAME}  application=${APP_NAME1},${APP_NAME2}

> > action=${ACTION}\`\`


* **Parameters**

    
    * **policy_name** – IP Firewall Policy Name


    * **application** – Application Name or Application List


    * **source_ip** – Source IP with Default Option Any


    * **destination_ip** – Destination IP with Option Default Any


    * **action** – Firewall Policy Action Either Permit or Deny



* **Returns**

    1 if IP Firewall Policy Created Successfully else -1



#### create_open_ssid_in_common_objects(ssid_name)

* Flow: Configure –> Common Objects –> Policy –>SSIDs


* Create Open SSID from the ssid grid


* Keyword Usage:

> 
> * `Create Open SSID In Common Objects  ${SSID_NAME}`


* **Parameters**

    **ssid_name** – Name of the ssid_name



* **Returns**

    1 if Created Open SSID Successfully else -1



#### create_radio_profile(profile_name, radio_mode, dfs=False)

* Flow: Configure –> Common Objects –> Policy –>Radio Profile


* Create Radio profile from the radio grid


* Keyword Usage:

> 
> * `Create Radio Profile        ${RADIO_PROFILE_NAME}       ${RADIO_MODE}`


* **Parameters**

    **profile_name** – Name of the Radio profile


:param radio_mode : Select the radio mode (“ax (5GHz)” or “ax (2.4GHz)” or  “ac” or  “a/n”)
:param dfs : will select the DFS related option, when its “True”, disabled channel: u-1/u-2e/u-3

> else will create radio profile without DFS options


* **Returns**

    1 if Created Radio profile Successfully else -1



#### delete_aaa_server_profile(aaa_profile_name)

* Flow: CONFIGURE–>COMMON OBJECTS–>AUTHENTICATION–>AAA SERVER SETTINGS


* Delete AAA server profile from the grid

-Keyword Usage:

    
    * `Delete AAA Server Profile  ${AAA_PROFILE_NAME}`


* **Parameters**

    **aaa_profile_name** – Name of AAA Profile



* **Returns**

    1 if aaa profile deleted successfully else returns -1



#### delete_all_ap_templates()

* Flow: Configure –> Common Objects –> Policy –> AP Templates


* Delete All ap templates except default template from Template grid


* Keyword Usage:

> 
> * `Delete All AP Templates`


* **Returns**

    1 if deleted else -1



#### delete_all_captive_web_portals(exclude_list='')

* Flow: Configure –> Common Objects –> Authentication –> Captive Web Portal


* Delete captive web portals from the grid


* Keyword Usage:

> 
> * `Delete All Captive Web Portals   exclude_list=${cwp1},${cwp2}`


* **Parameters**

    **exclude_list** – list of cwps to exclude from delete



* **Returns**

    1 deleted
    -1 cannot be removed because it is used by another object



#### delete_all_client_mode_profiles()

* Flow: Configure –> Common Objects –> Basic –> Client Mode Profiles


* Delete all client mode profiles from Client Mode Profiles grid


* Keyword Usage:

> 
> * `Delete All Client Mode Profiles`


* **Returns**

    1 if deleted else -1



#### delete_all_ssids()

* Flow: Configure –> Common Objects –> Policy –>SSIDs


* Delete all SSIDs from the grid expect exclude_list SSIDs


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Delete All ssids   \`


* **Returns**

    1 if deleted else -1



#### delete_ap_template_profile(ap_template_name)

* –>COMMON OBJECTS–>AP Templates
- Delete ap_template_name in Common Object from the grid
- Keyword Usage:

> 
> * `Delete Ap Template Profile  ${AP_TEMPLATE_NAME}`


* **Parameters**

    **ap_template_name** – Name of AP Template



* **Returns**

    1 if ap template name deleted successfully else returns -1



#### delete_ap_templates(\*templates)

* Flow: Configure –> Common Objects –> Policy –> AP Templates


* Delete Templates from Template grid


* Keyword Usage:

> 
> * `Delete AP Templates  ${Template1}  ${Template2}  ${Template3}`


* **Parameters**

    **templates** – (list) list of template’s to delete



* **Returns**

    1 if deleted else -1



#### delete_captive_web_portal(cwp_name)

* Flow: Configure –> Common Objects –> Authentication –> Captive Web Portal


* Delete captive web portal from the grid


* Keyword Usage:

> 
> * `Delete Captive Web Portal  ${CWP_NAME}`


* **Parameters**

    **cwp_name** – Name of the Captive Web portal



* **Returns**

    1 deleted
    -1 cannot be removed because it is used by another object



#### delete_captive_web_portals(\*cwp_names)

* Flow: Configure –> Common Objects –> Authentication –> Captive Web Portal


* Delete captive web portals from the grid


* Keyword Usage:

> 
> * `Delete Captive Web Portals   ${CWP_NAME1}  ${CWP_NAME2}   ${CWP_NAME3}`


* **Parameters**

    **cwp_names** – Name of the Captive Web portal



* **Returns**

    1 deleted
    -1 cannot be removed because it is used by another object



#### delete_external_radius_server(radius_server)

* Flow: Configure –> Common Objects –> Authentication –> External radius server


* Delete external radius server from grid


* Keyword Usage:

> 
> * `Delete External Radius Server   ${RADIUS_SERVER_NAME}`


* **Parameters**

    **radius_server** – radius server name



* **Returns**

    1 if deleted
    -1 if can not be removed



#### delete_imago_tag_profile(profile_name)

* Flow: Configure –> Common Objects –> Policy –>Imago Tag Profile


* Delete specified Imago Tag Profile from the Imago Tag Profile grid


* Keyword Usage:

> 
> * `Delete Imago Tag Profile  ${PROFILE_NAME}`


* **Parameters**

    **profile_name** – Image Tag Profile Name



* **Returns**

    1 if deleted else -1



#### delete_ip_firewall_policy(ip_firewall_policy_name)

* Delete specified IP Firewall Policy Name from the Grid


* Keyword Usage:


* Flow: Flow: Configure –> Common Objects –> Security –>IP Firewall Policies

> 
> * `Delete Ip Firewall Policy  ${NAME}`


* **Parameters**

    **ip_firewall_policy_name** – IP Firewall Policy Name



* **Returns**

    1 if deleted else -1



#### delete_ip_object_hostname(object_name)

* Flow: Configure –> Common Objects –> Basic –> IP Objects / HostName


* Delete the ip object or hostname from Basic–>IP Objects/ Hostname


* Keyword Usage:

> 
> * `Delete IP Object Hostname  ${IP_OR_HOSTNAME}`


* **Parameters**

    **object_name** – Ip object or hostname



* **Returns**

    1 if deleted
    -1 if can not be removed



#### delete_management_options(management_options_name)

* Flow: Configure –> Common Objects –> Network –>Management Options–>Delete Management Option Name


* Delete specified Management Options Name from the Management Options Grid


* Keyword Usage:

> 
> * `Delete Management Options  ${NAME}`


* **Parameters**

    **management_options_name** – Management Options Name



* **Returns**

    1 if deleted else -1



#### delete_port_type_profile(port_type_name)

* Flow: CONFIGURE–>COMMON OBJECTS–>PORT TYPES


* Delete Port Type from the grid


* Keyword Usage:

> 
> * `Delete Port Type Profile  ${PORT_TYPE_NAME}`


* **Parameters**

    **port_type_name** – Name of Port Tye



* **Returns**

    1 if Port Type deleted successfully, else returns -1



#### delete_ssid(ssid_name)

* Flow: Configure –> Common Objects –> Policy –>SSIDs


* Delete SSID from the ssid grid


* Keyword Usage:

> 
> * `Delete SSID  ${SSID_NAME}`


* **Parameters**

    **ssid_name** – Name of the ssid_name



* **Returns**

    1 if deleted else -1



#### delete_ssids(\*ssids, \*\*kwargs)

* Flow: Configure –> Common Objects –> Policy –>SSIDs


* Delete ssid’s from ssid grid


* Keyword Usage:

> 
> * `Delete ssids  ${SSID1}  ${SSID2}  ${SSID3}`


* **Parameters**

    **ssids** – (list) list of ssid’s to delete



* **Returns**

    1 if deleted else -1



#### delete_sub_network_profile(sub_network_name)

* Flow: CONFIGURE–>COMMON OBJECTS–>NETWORK–>Subnetwork Space


* Delete Sub Network in Common Object from the grid


* Keyword Usage:

> 
> * `Delete Sub Network Profile   ${SUB_NETWORK_NAME}`


* **Parameters**

    **sub_network_name** – Name of SubNetwork Space



* **Returns**

    1 if SubNetwork Space deleted successfully else returns -1



#### delete_switch_template(template_name)

* Flow: Configure –> Common Objects –> Policy –>Switch Template


* Delete specified switch template from the Switch Templates grid


* Keyword Usage:

> 
> * `Delete Switch Template  ${TEMPLATE_NAME}`


* **Parameters**

    **template_name** – Name of the switch template



* **Returns**

    1 if deleted else -1



#### delete_user_profile(profile='user004')

* It deletes user profile

-Flow: Configure –> Common Objects –> User Profile

    
    * Keyword Usage:

    > 
    > * `Delete User Profile       profile=${PROFILE}`

:param profile : profile name
:return: 1


#### delete_vlan_profile(vlan_name)

* Flow: CONFIGURE–>COMMON OBJECTS–>BASIC–>VLAN’s


* Delete Vlans in Common Object from the grid


* Keyword Usage:

> 
> * `Delete Vlan Profile  ${VLAN_NAME}`


* **Parameters**

    **vlan_name** – Name of Vlan



* **Returns**

    1 if vlan name deleted successfully else returns -1



#### delete_wips_policy_profile(wips_policy_name)

* Flow: CONFIGURE–>COMMON OBJECTS–>SECURITY–>WIPS POLICIES


* Delete wips_policys in Common Object from the grid


* Keyword Usage:

> 
> * `Delete Wips Policy Profile   ${WIPS_POLICY_NAME}`


* **Parameters**

    **wips_policy_name** – Name of wips policy name



* **Returns**

    1 if wips policy name deleted successfully else returns -1



#### disable_cwp_employee_approval(cwp_name)

* Flow: Configure –> Common Objects –> Authentication –> Captive Web Portal


* Disable the employee approval in captive web portal configuration


* Keyword Usage:

> 
> * `Disable Cwp Employee Approval  ${CWP_NAME}`


* **Parameters**

    **cwp_name** – name of the captive web portal



* **Returns**

    


#### edit_captive_web_portal_social_login_configuration(\*\*cwp_template_config)

* Flow: Configure –> Common Objects –> Authentication –> Captive Web Portal


* Edit social login captive web portal from the grid


* Keyword Usage:

> 
> * `Edit Captive Web Portal Social Login Configuration   &{CWP_TEMPLATE_CONFIG}`


* **Parameters**

    **cwp_template_config** – social login cwp edit variables



* **Returns**

    1 edited



#### edit_imago_tag_profile(profile_name, server='', channel='', fcc_mode=True, server_port='')

* This keyword will Edit Existing image Tag profile under Common Objects.


* Flow: Configure –> Common Objects –> Policy –>Select ImagoTag Profile –> Edit


* Keyword Usage:

> 
> * `Edit Imago Tag profile  ${PROFILE_NAME}  server=${SERVER}`


> * `Edit Imago Tag profile  ${PROFILE_NAME}  channel=${CHANNEL}`


> * `Edit Imago Tag profile  ${PROFILE_NAME}  server_port=${SERVER_PORT}`


> * `Edit Imago Tag profile  ${PROFILE_NAME}  server=${SERVER} channel=${CHANNEL}  fcc_mode=False`


* **Parameters**

    
    * **profile_name** – Imago Tag Profile name


    * **channel** – Channel Number


    * **server** – Server detail


    * **fcc_mode** – By default fcc_mode is enabled.To Disable mention this flag as False


    * **server_port** – Server Port Details



* **Returns**

    1 if Imago Tag Profile Edited successfully else -1



#### ip_object_hostname_delete_object_profile(ip_object_profile_name)

* Delete IP Object profile


* Flow: Configure –> Common Objects –> Basic –> IP Objects / HostName –> Find the object profile –> Delete it


* Keyword Usage:

    
        * `IP Object Hostname Delete Object Profile    ${ip_object_profile_name}`


* **Parameters**

    **ip_object_profile_name** – IP Object profile name



* **Returns**

    Find and delete successfully return 1 else return -1



#### ip_object_hostname_list_all_objects_in_profile(ip_object_profile_name)

* Find all the items for existed IP Object profile, and return a list


* Flow: Configure –> Common Objects –> Basic –> IP Objects / HostName –> Find the object profile –> Edit it –> Click 100 items per page –> Get item row by row


* Keyword Usage:

    
        * `IP Object Hostname List All Objects In Profile    ${ip_object_profile_name}`


* **Parameters**

    **ip_object_profile_name** – IP Object profile name



* **Returns**

    success return a list else return -1



#### ip_object_hostname_update_object_profile(ip_object_profile_name, netmask=None, ip_range_gap=None, \*classified_items_list_1)

#### navigate_to_basic_ip_object_hostname()

* FLow: CONFIGURE–>COMMON OBJECTS–>BASIC–>IP Objects / HostNames


* Keyword Usage:

> 
> * `Navigate To Basic Ip Object Hostname\``


* **Returns**

    None



#### navigate_to_security_wips_policies()

* Flow: CONFIGURE–>COMMON OBJECTS–>SECURITY–>WIPS POLICIES


* Keyword Usage:

> 
> * `Navigate To Security Wips Policies`


* **Returns**

    None



#### radio_phy_mode_fiveghz(model)

* Flow: Configure –> Common Objects –> Policy –>Radio Profile


* Map the Radio phy mode based on the AP


* Keyword Usage:


* `${RADIO_MODE}      Radio Phy Mode Fiveghz      ${AP1_MODEL}`


* `${CREATE_RADIO_PROFILE}    Create Radio Profile    ${RADIO_PROFILE_NAME}   ${RADIO_MODE}   True`


* **Parameters**

    **model** – Name of the model being used our Test



* **Returns**

    Radio phy mode based on AP model (“ax (5GHz)” or  “ac” )



#### radio_phy_mode_twoghz(model)

* Flow: Configure –> Common Objects –> Policy –>Radio Profile


* Map the Radio phy mode based on the AP


* Keyword Usage:

> 
> * `${RADIO_MODE}      Radio Phy Mode Twoghz      ${AP1_MODEL}`


> * `${CREATE_RADIO_PROFILE}    Create Radio Profile    ${RADIO_PROFILE_NAME}   ${RADIO_MODE}`


* **Parameters**

    **model** – Name of the model being used our Test



* **Returns**

    Radio phy mode based on AP model (“ax (2.4GHz)” or “g/n”)



#### select_ip_firewall_policy_for_new_user_profile(user_profile_name='', firewall_policy_name='')

* This Keyword will Select Configured IP Firewall Policy Under New User Profile.


* Flow: Configure –> Common Objects –> Policy –> User Profiles

> 
> * Keyword Usage:

> > 
> > * 

> > ```
> > ``
> > ```

> > Select IP Firewall Policy For New User Profile   user_profile_name=${PROFILE_NAME}

> > firewall_policy_name=${FW_POLICY_NAME}\`\`


* **Parameters**

    
    * **user_profile_name** – User Profile Name


    * **firewall_policy_name** – Already Created Firewall Policy Name



* **Returns**

    1 if IP Firewall Policy Selected Successfully under New User File Created else -1


## extauto.xiq.flows.configure.DeviceTemplate module


### _class_ extauto.xiq.flows.configure.DeviceTemplate.DeviceTemplate()
Bases: `object`


#### add_ap_template(ap_model, ap_template_name, \*\*wifi_interface_config)

* Checking the AP template present in the AP Templates Grid


* If it is not there add New AP Template


* WiFi2 config was removed as per jira ticket EXTAUTO-113 and APC-44337.


* Keyword Usage

> 
> * `Add AP Template  ${AP_TEMPLATE_NAME}   &{AP_TEMPLATE_CONFIG}`


* **Parameters**

    
    * **ap_template_name** – AP Template Name ie prod_sanity_ap410ctemplate


    * **ap_model** – AP MODEL ie AP630,AP410C


    * **wifi_interface_config** – (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor



* **Returns**

    1 if AP Template Configured Successfully else -1



#### add_ap_template_model_type(ap_template_name, ap_model_type, \*\*wifi_interface_config)

* Checking the AP template present in the AP Templates Grid


* If it is not there add New AP Template


* Keyword Usage

> 
> * `Add AP Template  ${AP_TEMPLATE_NAME}   &{AP_TEMPLATE_CONFIG}`


* **Parameters**

    
    * **ap_template** – AP Template Name ie AP630,AP410C


    * **wifi_interface_config** – (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor



* **Returns**

    1 if AP Template Configured Successfully else -1



#### add_ap_template_to_network_policy(ap_template_name, policy_name)
”
- Selecting Network Policy to attach existing AP Template to the same
- Checking the AP template presence in the AP Templates Grid
- If not there, then select AP Template from the list
- Keyword Usage

> 
> * `Add AP Template To Network Policy   ${AP_TEMPLATE_NAME}       ${NETWORK_POLICY_NAME}`


* **Parameters**

    
    * **ap_template_name** – AP Template Name ie AP630,AP410C etc


    * **policy_name** – Name of the Network policy to attach the template



* **Returns**

    1 if AP Template Configured Successfully else -1



#### add_classification_rule_to_ap_template(ap_template_name, classification_rule)
“


* Checking the AP template presence in the AP Templates Grid


* Select Classification Rule button will only appear in case of second AP Template for same model


* Selecting the Classification Rule from the list


* Keyword Usage

> 
> * `Add Classification Rule to AP Template    ${AP_TEMPLATE_NAME}   ${CLASSIFICATION_RULE}`


* **Parameters**

    
    * **ap_template_name** – AP Template Name ie AP630-Template,AP410C-Template


    * **classification_rule** – Classification Rule to be added to AP Template



* **Returns**

    1 if Classification Rule added to AP Template Successfully else -1, -2, -3 depending on the scenario



#### check_ap_template(ap_template)

* Check the AP template in th AP template Grid


* Keyword Usage

> 
> * `Check AP Template  ${AP_TEMPLATE_NAME}`


* **Parameters**

    **ap_template** – Ap Template Name ie AP630,AP410C



* **Returns**

    True if AP Template Found on Grid else False



#### config_ap_template_wifi0(\*\*wifi0_profile)

* Configure the WIFI0 configuration on AP Template


* Keyword Usage

> 
> * `Config AP Template WiFi0  &{WIFI0_CONFIG}`


* **Parameters**

    **wifi0_profile** – (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor



* **Returns**

    1 if WiFi0 Profile Configured Successfully else None



#### config_ap_template_wifi1(\*\*wifi1_profile)

* Configure the WIFI1 configuration on AP Template


* Keyword Usage

> 
> * `Config AP Template WiFi1  &{WIFI1_CONFIG}`


* **Parameters**

    **wifi1_profile** – (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor



* **Returns**

    1 if WiFi1 Profile Configured Successfully else None



#### config_ap_template_wifi2(\*\*wifi2_profile)

* Configure the WIFI2 configuration on AP Template


* Keyword Usage

> 
> * `Config AP Template WiFi2  &{WIFI2_CONFIG}`


* **Parameters**

    **wifi2_profile** – (Config Dict) WiFi2 ADSP server Config ie primary server ip and port



* **Returns**

    1 if WiFi2 Profile Configured Successfully else None



#### edit_ap_net_policy_template_wifi2(policy_name)

* Selects the given network policy and edit, selects the AP Template and edit wifi2 and disable


* Keyword Usage

> 
> * `Edit AP Net Policy Template Wifi2   ${POLICY_NAME}`


* **Parameters**

    
    * **policy_name** – Network Policy Name


    * **ap_template** – Ap Template Name ie AP630,AP410C



* **Returns**

    1 if Editing is successful on AP Template or else -1



#### enable_supplemental_cli_in_ap_template(policy_name, ap_model, ap_template_name, suppl_cli_name, suppl_cli_cmds)

* This Keyword creates Supplemental CLI inside the AP Template


* Flow: Network Policies –> Device Template –> AP Template –> Advanced Settings –> Supplemental CLI


* Keyword Usage:

> 
> * `Enable Supplemental CLI in AP Template   ${POLICY_NAME}    ${AP_MODEL}    ${AP_TEMPLATE_NAME}   ${SUPPL_CLI_NAME}     ${SUPPL_CLI_CMDS}`


* **Parameters**

    
    * **policy_name** – Name of the Network policy


    * **ap_model** – AP Model


    * **ap_template_name** – Name of the AP Template


    * **suppl_cli_name** – Name of the Supplemental CLI name


    * **suppl_cli_cmds** – Supplemental CLI commands



* **Returns**

    1 if AP Template is saved successfully else -1



#### enable_supplemental_cli_in_switch_template(policy_name, switch_model, switch_template_name, suppl_cli_name, suppl_cli_cmds)

* This Keyword creates Supplemental CLI inside the Switch Template


* Flow: Network Policies –> Device Template –> Switch Template –> Advanced Settings –> Supplemental CLI


* Keyword Usage:

> 
> * `Enable Supplemental CLI in Switch Template   ${POLICY_NAME}    ${SWITCH_MODEL}    ${SWITCH_TEMPLATE_NAME}   ${SUPPL_CLI_NAME}     ${SUPPL_CLI_CMDS}`


* **Parameters**

    
    * **policy_name** – Name of the Network policy


    * **switch_model** – Switch Model


    * **switch_template_name** – Name of the Switch Template


    * **suppl_cli_name** – Name of the Supplemental CLI name


    * **suppl_cli_cmds** – Supplemental CLI commands



* **Returns**

    1 if AP Template is saved successfully else -1



#### remove_ap_template_from_network_policy(ap_template_name, policy_name)
”
- Selecting Network Policy to remove/detach AP Template
- Checking the AP template presence in the AP Templates Grid
- If it is not there return -1 else delete the template
- Keyword Usage

> 
> * `Remove AP Template From Network Policy   ${AP_TEMPLATE_NAME}       ${NETWORK_POLICY_NAME}`


* **Parameters**

    
    * **ap_template_name** – AP Template Name ie AP630,AP410C


    * **policy_name** – Name of the Network policy to remove the template



* **Returns**

    1 if AP Template Removed Successfully else -1


## extauto.xiq.flows.configure.EspAlert module


### _class_ extauto.xiq.flows.configure.EspAlert.EspAlert()
Bases: `EspAlertWebElements`


#### check_alert_detail(summary)

* Go to policy page and check alert detail exist


* Keyword Usage

> 
> * `Check Alert Detail  ${summary}`


* **Returns**

    returns 1 if successfully check alert detail exist else -1



#### create_alert_policy(policy_type, source_parent, source, trigger_type, when, threshold_operator='', threshold_input='')

* Go to policy page and check create alert policy works


* Keyword Usage

> 
> * `Create Alert Policy  ${policy_type}  ${source_parent}  ${source}  ${trigger_type}  ${when}  ${threshold_operator}  ${threshold_input}`


* **Returns**

    returns 1 if successfully create alert policy else -1



#### create_alert_policy_by_unconfigured_grid(policy_type, when, trigger_type, threshold_operator='', threshold_input='')

* Go to policy page and check create alert policy by unconfigure event/metric works


* Keyword Usage

> 
> * `Create Alert Policy By Unconfigured Grid  ${policy_type}  ${when}  ${trigger_type}  ${threshold_operator}  ${threshold_input}`


* **Returns**

    returns 1 if successfully create alert policy else -1



#### delete_alert_policy(when)

* Go to policy page and delete alert policy in configured grid


* Keyword Usage

> 
> * `Delete Alert Policy  ${when}`


* **Returns**

    returns 1 if successfully delete alert policy else -1



#### edit_alert_policy(when, severity, desc)

* Go to policy page and check edit alert policy works


* Keyword Usage

> 
> * `Edit Alert Policy  ${when}  ${severity}  ${desc}`


* **Returns**

    returns 1 if successfully edit alert policy else -1



#### enable_esp_alert(url)

* Keyword Usage:

> 
> * `Enable Esp Alert   ${URL}`


* **Parameters**

    **url** – url to load for enabling esp alert on cloud UI



* **Returns**

    1 if loaded the url successfully



#### find_desc_in_unconfigured_grid(desc)

* Go to policy page and find event/metric in unconfigured grid


* Keyword Usage

> 
> * `Find Desc In Unconfigured Grid  ${when}`


* **Returns**

    returns 1 if successfully matched else -1



#### find_when_in_configured_grid(when)

* Go to policy page and find alert policy in configured grid


* Keyword Usage

> 
> * `Find When In Configured Grid  ${when}`


* **Returns**

    returns 1 if successfully matched else -1



#### go_to_alert_policy()

#### go_to_policy_and_check_tab(configred_title, not_configured_title)

* Go to policy page and check configured policies and not configured policies tab


* Keyword Usage

> 
> * `Go To Policy And Check Tab  ${configred_title}  ${not_configured_title}`


* **Returns**

    returns 1 if successfully show configred policies and not configured policies tab else -1



#### search_in_unconfigure_grid(event_search_input, metric_search_input)

* Go to policy page and search in unconfigured grid


* Keyword Usage

> 
> * `Search In Unconfigure Grid  ${event_search_input}  ${metric_search_input}`


* **Returns**

    returns 1 if successfully search else -1



#### subscribe_alert_policy(when, name)

* Go to policy page and check subscribe alert policy works


* Keyword Usage

> 
> * `Subscribe Alert Policy  ${when}`


* **Returns**

    returns 1 if successfully subscribe alert policy else -1



#### toggle_alert_policy_status(when)

* Go to policy page and check disable alert policy works


* Keyword Usage

> 
> * `Toggle Alert Policy Status  ${when}`


* **Returns**

    returns 1 if successfully disable alert policy else -1


## extauto.xiq.flows.configure.ExpirationSettings module


### _class_ extauto.xiq.flows.configure.ExpirationSettings.ExpirationSettings()
Bases: `ExpSettingsWebElements`


#### config_expiration_settings(\*\*config)

* Config the account expiration settings based on the passed config dict


* For different combination of config parameters creation refer private_pre-shared_key_config.robot


* Assumes that user already navigated to User group edit page or called along with user group creation


* Keyword Usage

> 
> * `Config Expiration Settings   &{EXPIRATION_CONFIG}`


* **Parameters**

    **config** – configuration dict



* **Returns**

    1 if successfully configured


## extauto.xiq.flows.configure.ExpressNetworkPolicies module


### _class_ extauto.xiq.flows.configure.ExpressNetworkPolicies.ExpressNetworkPolicies()
Bases: `NPExpressPolicyWebElements`


#### create_express_network_policy_no_wireless(policy_name)

* Create  network express network policy (no wireless)


* Keyword Usage:

> 
> * `Create Express Network Policy No Wireless  ${POLICY_NAME}`


* **Parameters**

    **policy_name** – Policy Name



* **Returns**

    1



#### create_open_auth_express_network_policy(policy_name, ssid_name, cwp=None, \*\*kwargs)

* Create open network express network policy


* Checks the policy already exists, if it is not exist then create the network policy


* Keyword Usage:

> 
> * `Create Open Auth Express Network Policy  ${POLICY_NAME}   ${SSID_NAME}`


> * `Create Open Auth Express Network Policy  ${POLICY_NAME}   ${SSID_NAME}   ${CWP_NAME}`


* **Parameters**

    
    * **policy_name** – Policy Name


    * **ssid_name** – SSID name


    * **cwp** – Captive Portal name



* **Returns**

    1


## extauto.xiq.flows.configure.GuestAccessNetwork module


### _class_ extauto.xiq.flows.configure.GuestAccessNetwork.GuestAccessNetwork()
Bases: `GuestAccessNetworkWebElements`


#### create_guest_access_network(\*\*config)

* Create secure and unsecure guest networks


* Assuming navigated to Configure–>Network Policies–>Wireless Networks


* Keyword Usage:

> 
> * `Create Guest Access Network     &{CONFIG}`


> * For creation of &{CONFIG} refer guest_access_config.robot


* **Parameters**

    **config** – configuration parameter dict



* **Returns**

    1 if created else -1


## extauto.xiq.flows.configure.GuestPasswdSetting module


### _class_ extauto.xiq.flows.configure.GuestPasswdSetting.GuestPasswdSetting()
Bases: `GuestPasswdSettingElements`


#### config_password_settings(\*\*passwd_config)

* This keyword used with standalone and along with user group creation


* In stand alone mode assumes that  navigating to the user group


* For password_setting configuration variable refer the user_group_config robot file password setting section


* Configure the password settings


* keyword Usage:

> 
> * `Config Password Setting  &{PASSWORD_CONFIG}`


* **Parameters**

    **passwd_config** – 



* **Returns**

    1 if password config setting is success


## extauto.xiq.flows.configure.NetworkPolicy module


### _class_ extauto.xiq.flows.configure.NetworkPolicy.NetworkPolicy()
Bases: `object`


#### add_wireless_nw_to_network_policy(policy_name, \*\*wireless_profile)

* It will add the wireless network to existing network policy


* Flow: Navigate to Network policy–>Select List View–>Select Network Policy ROW–>
Edit–>Select wireless nw tab–>Add other wireless network


* Keyword Usage:

> 
> * `Add Wireless Nw To Network Policy    ${POLICY_NAME}    &{WIRELESS_NW_PROFILE}`


> * &{WIRELESS_NW_PROFILE} –> This is dictionary, include all key value pair to create wireless network


> * Fof Creating  &{WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot


* **Parameters**

    
    * **policy_name** – name of the network policy


    * **wireless_profile** – (dict) wireless network profile config parameters


:return:1 if success else -1


#### configure_access_security_pre_authentication_status(status, policy_name, ssid)

* configure Pre Authentication based on status for the wireless Network


* **Parameters**

    
    * **status** – (str) status is either enable or disable


    * **policy_name** – (str) Network Policy Name


    * **ssid** – (str) SSID name



* **Returns**

    1 if successfully changed the pre authentication status else -1



#### create_network_policy(policy, \*\*wireless_profile)

* Create the network policy from CONFIGURE–>NETWORK POLICIES


* This keyword will create the network policy and wireless network


* Wireless network includes open, ppsk, psk and enterprise network


* Keyword Usage:

> 
> * `Create Network Policy   ${POLICY_NAME}   &{WIRELESS_NW_PROFILE}`


> * &{WIRELESS_NW_PROFILE} –> This is dictionary, include all key value pair to create wireless network


> * Fof Creating  &{WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot


* **Parameters**

    
    * **policy** – Name of the network policy to create


    * **wireless_profile** – (dict) wireless network creation profile parameters



* **Returns**

    1 if network policy creation is success



#### create_owe_ssid(nw_policy, ssid, WiFi2)

* This keyword is ONLY used for OWE SSID testing purposes.


* Flow: Configure –> Network Policy –> select the Policy –>Wireless Setings –>Add SSID


* Keyword Usage:

> 
> * ‘’Create OWE SSID  ${POLICY_NAME}  ${SSID}   WiFi2=enable ‘’


> * ‘’Create OWE SSID  ${POLICY_NAME}  ${SSID}   WiFi2=disable ‘’


* **Parameters**

    
    * **nw_policy** – name of the policy


    * **SSID** – Enter SSID


:param WiFi2=enable : Enable WiFi2 checkbox
:param WiFi2=disable : Disable WiFi2 Checkbox
:return: 1 if OWE SSID is saved and configured successfully; else -1


#### create_ssid_to_policy(nw_policy, \*\*wireless_profile)

* This keyword will create extra new ssid and add to exist policy.


* Wireless network includes open, ppsk, psk, enhanced, and enterprise network


* Flow: Configure –> Network Policies –> select exist Policy –> select Wireless Networks tab –> Add(+) SSID


* Keyword Usage:

> 
> * ‘’Create SSID to Policy   ${SSID}   ${POLICY_NAME}   &{WIRELESS_NW_PROFILE}\`\`


> * &{WIRELESS_NW_PROFILE} –> This is dictionary, include all key value pair to create wireless network


> * Fof Creating  &{WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot


* **Parameters**

    
    * **nw_policy** – name of exist policy


    * **SSID** – extra new SSID to create


    * **wireless_profile** – (dict) wireless network creation profile parameters



* **Returns**

    1 if ssid creation and addition is success, otherwise -1



#### create_switching_routing_network_policy(policy_name)

* Create Switching and Routing network policy


* Checks the policy already exists, if it is not exist then create the network policy


* Routing and Switching checkbox selected and wireless checkbox unselected while creating policy for EXOS


* Keyword Usage:

> 
> * `Create Switching Routing Network Policy  ${POLICY_NAME}`


* **Parameters**

    **policy_name** – Policy Name



* **Returns**

    1 if network policy created successfully else returns -1.



#### delete_all_network_policies(exclude_list='')

* Delete all network policies from the grid expect exclude_list policies


* keyword Usage:
- `Delete All Network Policies  exclude_list=${POLICY1},${POLICY2)`


* **Parameters**

    **exclude_list** – list of policies to exclude from delete



* **Returns**

    1 if deleted successfully else -1



#### delete_all_ssid_in_policy(policy)
delete all ssids in the policy
:param: policy: name of the policy
:return 1 if deletion of ssids is success


#### delete_network_polices(\*policies, \*\*kwargs)

* Deleting the network policies based on the passed list of policies


* Keyword Usage:

> 
> * `Delete Network Policies   ${POLICY1}   ${POLICY2}`


* **Parameters**

    **policies** – list of network polices to delete



* **Returns**

    1 if deleted successfully else -1



#### delete_network_policy(policy)

* Delete Network Policy from network policy Grid


* Keyword Usage:

> 
> * `Delete Network Policy    ${POLICY_NAME}`


* **Parameters**

    **policy** – Name of the policy to delete



* **Returns**

    1 if deleted else -1



#### delete_network_policy_with_ssid(ssid_name)

* Deleting the network policy based on SSID name attached to it


* list all network policy from card view, get the ssid name of each policy , if any policy consists passed
ssid_name then delete that network policy


* Keyword Usage:


* `Delete Network Policy With SSID   ${SSID_NAME}`


* **Parameters**

    **ssid_name** – name of the ssid used to delete the network policy



* **Returns**

    


#### delete_radius_group(network_policy_name, radius_group_name)

* Delete Radius Server Group from wireless network


* For deleting radius server group, navigate to the network policy–> go to wireless network tab
–> add ssid –> select enterprise network –> click on radius server select button
–> select the radius server group and delete it


* Keyword Usage:

> 
> * `Delete Radius Group    ${POLICY_NAME}   ${RADIUS_SERVER_GROUP_NAME}`


* **Parameters**

    
    * **network_policy_name** – Network Policy Name


    * **radius_group_name** – Name of the radius group to delete



* **Returns**

    1 if deleted else -1



#### delete_single_ssid_in_policy(policy, ssid_name)
delete all ssids in the policy
:param: policy: name of the policy
:return 1 if deletion of ssids is success


#### deploy_network_policy(policy_name, devices, update_type='delta', next_reboot=False, _date=None, _time=None)

* Deploy the network policy to the particular device


* By default it will do delta config push


* If want to perform different type of config push, pass the appropriate parameter values


* If already in network policy then deploy the policy else navigate to network policy–> deploy policy tab


* Keyword Usage:

> 
> * `Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}`


> * `Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}  update_type=complete`


> * `Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}  next_reboot=True`


> * `Deploy Network Policy  ${POLICY_NAME}   ${DEVICE_MAC}  _date=${DATE}  _time=${TIME}`


* **Parameters**

    
    * **policy_name** – Name of the policy


    * **devices** – Device serial number


    * **update_type** – Config update type. By default it is complete


    * **next_reboot** – Next reboot option


    * **_date** – date when to update


    * **_time** – time when to update



* **Returns**

    


#### deploy_network_policy_at_specific_time(policy_name, devices, update_date, update_time)

* Config push network policy at specific time


* it will config push at specific date and at specific time


* if already in network policy then deploy the policy else navigate to network policy–> deploy policy tab


* Keyword Usage:

> 
> * `Deploy Network Policy At Specific Time   ${POLICY_NAME}  ${DEVICE_MAC}  ${UPDATE_DATE}  ${UPDATE_TIME}`


* **Parameters**

    
    * **policy_name** – Name of the policy


    * **devices** – Device serial number


    * **update_date** – date to update


    * **update_time** – update time



* **Returns**

    1 if success else -1



#### deploy_network_policy_with_complete_update(policy_name, devices)

* Config push network policy with complete update


* This will reboot the Device


* if already in network policy then deploy the policy else navigate to network policy–> deploy policy tab


* Keyword Usage:

> 
> * `Deploy Network Policy With Complete Update   ${POLICY_NAME}    ${DEVICE_MAC}`


* **Parameters**

    
    * **policy_name** – Name of the policy


    * **devices** – Device serial number



* **Returns**

    1 if success else -1



#### deploy_network_policy_with_delta_update(policy_name, devices)

* delta config push of network policy


* if already in network policy then deploy the policy else navigate to network policy–> deploy policy tab


* Keyword Usage:

> 
> * `Deploy Network Policy With Delta Update   ${POLICY_NAME}   ${DEVICE_MAC}`


* **Parameters**

    
    * **policy_name** – Name of the policy


    * **devices** – Device serial number



* **Returns**

    


#### deploy_network_policy_with_next_reboot(policy_name, devices)

* Config push network policy in next reboot


* this will do completed config push for the next reboot of device


* if already in network policy then deploy the policy else navigate to network policy–> deploy policy tab

> 
> * Keyword Usage:


> * `Deploy Network Policy With Next Reboot   ${POLICY_NAME}    ${DEVICE_MAC}`


* **Parameters**

    
    * **policy_name** – Name of the policy


    * **devices** – Device serial number



* **Returns**

    1 if success else -1



#### deploy_stack_network_policy(device_mac, policy_name, sw_template_name, firmwareUpdate=False)

* Deploy the network policy to the particular device


* By default it will do delta config push


* If want to perform different type of config push, pass the appropriate parameter values


* If already in network policy then deploy the policy else navigate to network policy–> deploy policy tab


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Deploy Network Policy     ${DEVICE_MAC}  ${POLICY_NAME} ${Switch_template}


* **Parameters**

    **policy_name** – Name of the policy


:param device_mac : The device mac
:param sw_template_name: Config update type. By default it is complete
:return: 1 if successfully updated ; else -1


#### disable_ibeacon_service_in_network_policy(nw_policy)

* This keyword is used to disable Ibeacon Service in Network Policy


* Flow: Configure –> Network Policy –> select the Policy –>Advance Settings–>IBeacon Services


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Disable IBeacon Service In Network Policy  ${POLICY_NAME}’’


* **Parameters**

    **nw_policy** – name of the policy for disabling the iBeacon



* **Returns**

    None



#### edit_network_policy_ssid(policy_name, ssid_name, new_ssid_name)

* Edit the SSID name of the wireless network in the network policy


* Flow: Navigate to the network policy – > click on network policy card view

    –> click on SSID –> Edit SSID


* Keyword Usage:

> 
> * `Edit Network Policy SSID   ${POLICY_NAME}   ${SSID_NAME}   ${NEW_SSID_NAME}`


* **Parameters**

    
    * **policy_name** – Name of the network policy


    * **ssid_name** – name of the ssid already exist on that network policy


    * **new_ssid_name** – new ssid name



* **Returns**

    1 if success



#### edit_network_policy_ssid_authentication(policy_name, ssid_name, new_auth_method)

* This keyword will Change SSID Authentication to Open in the network policy


* Flow: network policy – > click on network policy card view –> click on SSID –> Edit SSID Authentication


* Keyword Usage:

> 
> * `Edit Network Policy SSID Authentication   ${POLICY_NAME}   ${SSID_NAME}   ${NEW_AUTH_METHOD}`


* **Parameters**

    
    * **policy_name** – Name of the network policy


    * **ssid_name** – name of the ssid already exist on that network policy


    * **new_auth_method** – Open SSID authentication



* **Returns**

    1 if successfully changes SSID authentication to open



#### edit_network_policy_type(nw_policy, options_params)

* This keyword is used to select the type of policy option we are creating, i.e.., Routing, switching, wireless


* Flow: Configure –> Network Policy –> select the Policy –>enable/disable different policy type options above


* Keyword Usage:

> 
> * `Edit Network Policy Type  ${POLICY_NAME}   ${OPTION_PARAMS}`


* **Parameters**

    
    * **nw_policy** – name of the policy


    * **options_params** – wireless=enable,switches=disable,routing=enable



* **Returns**

    1 or -1



#### enable_QoS_Overview_DAS(nw_policy)

* This keyword is used to enable Marker Maps which Marks the outgoing or upstream traffic with the specified traffic priority markers.


* Flow: Configure –> Network Policy –> select the Policy –>Advance Settings–>QoS Options –> QoS Overview –> DAS


* Keyword Usage:

-

```
``
```

Enable QoS Overview DAS  ${POLICY_NAME} ‘’
:param nw_policy: name of the policy for enabling the Marker Maps
:return: 1 if successfully updated ; else -1


#### enable_classifier_maps(nw_policy, classifier_name)

* This keyword is used to enable Classifier Maps which Maps anonymous incoming traffic into the Extreme Networks classification system.


* Flow: Configure –> Network Policy –> select the Policy –>Advance Settings–>QoS Options –> Classifier Maps


* Keyword Usage:

-

```
``
```

Enable Classifier Maps   ${AP_NETWORK_POLICY}  ${classifier_name}’’
:param nw_policy: name of the policy for enabling the Marker Maps
:param classifier_name: Name and description for classier map settings
:return: 1 if successfully updated ; else -1


#### enable_ibeacon_service_in_network_policy(nw_policy, service_name, uuid, monitoring)

* This keyword is used to enable Ibeacon Service in Network Policy


* Flow: Configure –> Network Policy –> select the Policy –>Advance Settings–>IBeacon Services


* Keyword Usage:

> 
> * ‘’Enable IBeacon Service In Network Policy  ${POLICY_NAME}  ${service_name}  ${uuid} monitoring=enable ‘’


> * ‘’Enable IBeacon Service In Network Policy  ${POLICY_NAME}  ${service_name}  ${uuid} monitoring=disable ‘’


* **Parameters**

    
    * **nw_policy** – name of the policy


    * **service_name** – IBeacon Service Name


    * **uuid** – Enter UUID


:param monitoring=enable : Enable iBeacon Monitoring via checkbox if it was previously disabled
:param monitoring=disable : Disable iBeacon Monitoring via checkbox
:return: None


#### enable_marker_maps(nw_policy, \*\*MarkerMap_dict)

* This keyword is used to enable Marker Maps which Marks the outgoing or upstream traffic with the specified traffic priority markers.


* Flow: Configure –> Network Policy –> select the Policy –>Advance Settings–>QoS Options –> Marker Maps


* Keyword Usage:

-

```
``
```

Enable Marker Maps   ${AP_NETWORK_POLICY}  &{MarkerMap_dict}’’
:param nw_policy: name of the policy for enabling the Marker Maps
:param 

```
**
```

MarkerMap_dict: A dictionary that will contains all values required for Marker Maps Configuration
Marker Values for 802.1p : NC_8021P, CL_8021P, E_8021P, BF2_8021P
Marker Values for diffServ : NC_diffServ, Voice_diffServ, Video_diffServ, BG_diffServ
:return: 1 if successfully updated ; else -1


#### enable_mgmt_option_http_redirect(nw_policy, mgmt_option_name)

* This keyword is used to enable HTTP Redirect under enable Management Options.


* Flow: Configure –> Network Policy –> edit the Policy –> Additional Settings –> Management Options > Http Redirect


* Keyword Usage:

-

```
``
```

Enable Mgmt Option Http Redirect  ${POLICY_NAME}   ${MGMT_OPTION_NAME}’’
:param nw_policy: name of the policy
:param mgmt_option_name: name of the management option
:return: 1 if successfully updated ; else -1


#### enable_nw_presence_analytics(nw_policy)

* This keyword is used to enable the presence analytics


* Flow: Configure –> Network Policy –> select the Policy –> Enable Presence Analytics


* Keyword Usage:

> 
> * `Enable NW Presence Analytics  ${POLICY_NAME}`


* **Parameters**

    **nw_policy** – name of the policy



* **Returns**

    None



#### get_all_ssids_in_policy(policy, new_ssid=True, special_char=True)
return all ssids in each policy
:param: policies: list of policies
:param: new_ssid: Create a new ssid when the new_ssid is True
:param: special_char:  Create a new ssid with a special chars if the special_char is true
:return a dictionary contains policies and ssids


#### navigate_to_np_edit_tab(policy_name)

* Flow: Configure–>Network policy–>Select List View–>Select Network Policy ROW–> Edit


* **Parameters**

    **policy_name** – policy name



* **Returns**

    1 if success



#### navigate_wireless_ssid(policy_name, ssid)

* Flow: Configure –> Network Policies–> Select the policy–>Wireless tab–> Select SSID


* **Parameters**

    
    * **policy_name** – name of the network policy


    * **ssid** – ssid name



* **Returns**

    


#### select_network_policy_in_card_view(policy_name)

* Selects the existing network polices card view


* **Parameters**

    **policy_name** – name of the policy to search



* **Returns**

    1 if exists else -1



#### select_network_policy_management_option(nw_policy, mgmt_option_name)

* This keyword is used to select a Management Options under a Network Policy.


* Flow: Configure –> Network Policy –> edit the Policy –> Additional Settings –> Management Options


* Keyword Usage:

-

```
``
```

Select Network Policy Management Option  ${POLICY_NAME}   ${MGMT_OPTION_NAME}’’
:param nw_policy: name of the policy
:param mgmt_option_name: name of the management option
:return: 1 if successfully updated ; else -1


#### select_network_policy_row(policy)

* Select network policy row check box


* **Parameters**

    **policy** – Name of the policy row to select



* **Returns**

    1



#### select_ssid_in_policy(policy, ssid)

* Selects existing SSID in the policy


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Select SSID In Policy     ${POLICY}  ${SSID} \`\`


* **Parameters**

    **policy** – Name of the policy


:param ssid : SSID to select
:return: True if selection is success else False

## extauto.xiq.flows.configure.PasswdSettings module


### _class_ extauto.xiq.flows.configure.PasswdSettings.PasswdSettings()
Bases: `PasswdSettingsWebElements`


#### config_password_settings(\*\*passwd_config)

* Configure the user group password settings


* This keyword is called along with user group creation


* For standalone call, assumes that navigated to configure–>users–>user groups –> add user


* Keyword Usage:

> 
> * `Config Password Settings   &{PASSWORD_CONFIG}`


> * for &{PASSWORD_CONFIG} creation refer user_groups_config.robot “Password Settings” section


* **Parameters**

    **passwd_config** – password config parameters



* **Returns**

    1 if configured else None


## extauto.xiq.flows.configure.PpskClassification module


### _class_ extauto.xiq.flows.configure.PpskClassification.PpskClassification()
Bases: `object`


#### add_ppsk_classification_rule_to_user(network_name, user_name, classification_rule)

* Flow: Configure –> Users –> User Management –> PPSK Classification


* Select mentioned network from dropdown


* Add PPSK Classification Rule for the mentioned Network


* Keyword Usage

`Add PPSK Classification rule to User     ${Network_Policy}        ${PPSK_USER}        ${Classification_Rule}`


* **Parameters**

    
    * **network_name** – Name of the Network Policy


    * **user_name** – Name of the PPSK User created in the User Group


    * **classification_rule** – Classification Rule to be attached to User



* **Returns**

    1 if success else -1



#### delete_all_ppsk_classification_rule_user(network_name)

* Flow: Configure –> Users –> User Management –> PPSK Classification


* Select mentioned network from dropdown


* Delete all the PPSK classification users entries for the mentioned network


* Keyword Usage

> 
> * 

> ```
> ``
> ```

> Delete all PPSK Classification rule User     ${NETWORK_NAME} \`\`


* **Parameters**

    **network_name** – Name of the Network Policy



* **Returns**

    1 if success



#### edit_ppsk_classification_rule_to_user(network_name, user_name, classification_rule)

* Flow: Configure –> Users –> User Management –> PPSK Classification


* Select mentioned network from dropdown


* Edit the row Select new PPSK Classification Rule for the mentioned user


* Keyword Usage

`Edit Ppsk Classification rule to User  ${Network_Policy}  ${PPSK_USER}  ${Classification_Rule}`


* **Parameters**

    
    * **network_name** – Name of the Network Policy


    * **user_name** – Name of the PPSK User created in the User Group


    * **classification_rule** – Classification Rule to be attached to User



* **Returns**

    1 if success else -1



#### verify_ppsk_classification_rule_to_user(network_name, user_name, classification_rule)

* Flow: Configure –> Users –> User Management –> PPSK Classification


* Select mentioned network from dropdowm


* Select the row and verify PPSK Classification Rule for the mentioned user


* Keyword Usage

> 
> * `Verify Ppsk Classification rule to User     ${NETWORK_NAME}     ${PPSK_USER}      ${CLASSIFICATION_RULE}`


* **Parameters**

    
    * **network_name** – Name of the Network Policy


    * **user_name** – Name of the PPSK User created in the User Group


    * **classification_rule** – Classification Rule to be attached to User



* **Returns**

    1 if success else -1


## extauto.xiq.flows.configure.PrivateClientGroups module


### _class_ extauto.xiq.flows.configure.PrivateClientGroups.PrivateClientGroups()
Bases: `PrivateClientGroupsWebElements`


#### add_room_ap_based_group(room='default', user='default', user_position=1)
This keyword adds a romm in the ap based group
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `add_room_ap_based_group  room=abcdefefFFF  user=user22  user_position=0`

:param : room: room name
:param : user: exisiting user name
:param : user_position: which user in the dropdown list


* **Returns**

    1 or 0



#### add_user_key_based_group(user='default')
This keyword adds a existing user in the key based group
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `add_user_key_based_group    user=alex`

:param : user: exisiting key user name


* **Returns**

    1 or 0



#### delete_all_rooms_ap_based_group()
This keyword deletes all rooms in the ap based group table
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `delete_all_rooms_ap_based_group`


* **Returns**

    1 is for a successful deletion or -1 not a successful deletion



#### delete_all_user_keys_based_group()
This keyword deletes all user keys in the user key based group table
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `delete_all_user_keys_based_group`


* **Returns**

    1 is for a successful deletion or -1 not a successful deletion



#### delete_specific_room_ap_based_group(room)
This keyword deletes a specific room in the ap based group table
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `delete_specific_room_ap_based_group  room=room1`


* **Parameters**

    **room** – room name



* **Returns**

    1 or -1



#### delete_specific_user_key_based_group(user)
This keyword deletes a specific room in the user key base group table
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `delete_specific_user_key_based_group  user=alex`


* **Parameters**

    **user** – user name



* **Returns**

    1 or -1



#### enable_disable_ap_based_group(mode='default')
This keyword enables or disables the enable ap based group
- Flow: Configure –> Users –> User Management —>Private Client Group
- Keyword Usage:

> 
> * 

> ```
> ``
> ```

> ${rc}=   enable_disable_ap_based_groups   mode=enable \`\`


> * 

> ```
> ``
> ```

> ${rc}=   enable_disable_ap_based_groups   mode=disable  \`\`


* **Parameters**

    **mode** – enabling or disable=ing



* **Returns**

    1 or -1



#### enable_disable_key_based_group(mode='default')
This keyword enables or disables the key based group
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> ${rc}=   enable_disable_key_based_groups   mode=enable \`\`


> * 

> ```
> ``
> ```

> ${rc}=   enable_disable_key_based_groups   mode=disable  \`\`


* **Parameters**

    **mode** – enabling or disabling



* **Returns**

    1 or -1



#### get_based_grp_enabled_status(mode)
This keyword get a staus of the enable based groups button when the current status is on or off
- Flow: Configure –> Users –> User Management —>Private Client Group


* Keyword Usage:

> 
> * `get_based_grp_enabled_status  ap`


> * `get_based_grp_enabled_status  key`


> * **param  mode**

>     key for the key based group or ap for the ap based group



* **Returns**

    ON is active or OFF is not active



#### search_in_table(no_columns_per_row, cells, searched_value)

* This function searches a value in a table and return a selected row


* **Parameters**

    
    * **no_columns_per_row** – total columns


    * **cells** – total cells


    * **searched_value** – value to be searched



* **Returns**

    a selected check box of row  or -1



#### set_custom_network_policy(policy='default')
This keyword set a custom network policy on the private client group page
- Flow: Configure –> Users –> User Management —>Private Client Group
- Keyword Usage:

> 
> * `set_custom_network_policy  policy=ANC_ppsk`


* **Parameters**

    **policy** – an existing policy name



* **Returns**

    1 or -1



#### wait_until_element_available(element, seconds=60)

#### wait_until_elements_available(elements, seconds=60)
## extauto.xiq.flows.configure.RadioProfile module


### _class_ extauto.xiq.flows.configure.RadioProfile.RadioProfile()
Bases: `RadioProfileWebElements`


#### add_radio_profile(radio_profile_name)

* Flow: Configure –> Common Objects –> Policy –> Radio Profile


* This keyword is to Add a Radio profile from the radio grid


* Keyword Usage:

> 
> * `Add Radio Profile  ${RADIO_PROFILE_NAME}`


* **Parameters**

    **radio_profile_name** – Name of the Radio profile



* **Returns**

    1 if Radio profile named successfully else -1



#### cancel_radio_profile(cancel_radio_profile)

* This Keyword is to Cancel the Radio Profile


* Keyword Usage:

> -`Cancel Radio Profile ${RADIO_PROFILE_NAME}`


* **Parameters**

    **cancel_radio_profile** – Cancel the radio profile



* **Returns**

    1 if radio profile was cancelled else -1



#### choose_radio_profile_channel_width(channel_width=None)

* This keyword is to configure channel width in the radio profile


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    Choose Radio Profile Channel Width ${CHANNEL_WIDTH} \`\`

:param channel_width : Select any channel width(“20MHz” or “40MHz” or “80MHz”)
:return: 1 if channel_width is chosen Successfully else -1


#### choose_radio_profile_radio_mode(radio_mode=None)

* This keyword is to configure radio mode in the radio profile


* Keyword Usage:

> 
> * `Choose Radio Profile Radio Mode ${RADIO_MODE}`


* **Parameters**

    **radio_mode** – Select the radio mode (“b/g” or “g/n” or  “ax (2.4GHz)” or “a” or “a/n” or “ac” or
    “ax (5GHz)”)



* **Returns**

    1 if Chosen Radio Mode Successfully else -1



#### conf_transmission_power_auto(tx_power_auto)

* This Keyword is to Configure the Transmission Power as “Auto” in the Radio Profile


* Keyword Usage:

> `Conf Transmission Power Auto ${TX_POWER_AUTO}`


* **Parameters**

    **tx_power_auto** – Transmission Power Auto



* **Returns**

    1 if success else -1



#### conf_transmission_power_manual(tx_power_manual=None)

* This Keyword is to Configure the Transmission Power as “Manual” in the Radio Profile


* Keyword Usage:

> `Conf Transmission Power Auto ${TX_POWER_MANUAL}`


* **Parameters**

    **tx_power_manual** – 



* **Returns**

    1 if success else -1



#### config_radio_profile_bg_scan_interval(bg_scan_interval)

* This Keyword is to configure the Background Scan Interval and its parameters


* Keyword Usage:

> 
> * `Config Radio Profile BG Scan Interval ${BG_SCAN_INTERVAL}`


* **Parameters**

    **bg_scan_interval** – Enable/Disable Background Scan, Background Scan Interval



* **Returns**

    1 if success else -1



#### config_radio_profile_bg_scan_interval_unit(bg_scan_interval_unit=None)

* This Keyword is to configure the Background Scan Interval Unit


* Keyword Usage:

> 
> * `Config BG Scan Int Unit ${BG_SCAN_INT_UNIT}`


* **Parameters**

    **bg_scan_interval_unit** – Background Scan Interval Unit



* **Returns**

    1 if success else -1



#### config_radio_profile_max_no_of_clients(max_no_of_clients)

* This keyword is to configure max no of clients in the radio profile


* Keyword Usage:

> 
> * `Config Radio Profile Max No Of Clients ${MAX_CLIENTS}`


* **Parameters**

    **max_no_of_clients** – Configure maximum number of clients in the radio profile



* **Returns**

    1 if success else -1



#### config_radio_profile_max_transmit_power(max_transmit_power)

* This keyword is to configure the maximum transmit power in radio profile


* Keyword Usage:

> 
> * `Config Radio Profile Max Transmit Power ${MAX_TRANSMIT_POWER}`


* **Parameters**

    **max_transmit_power** – Configure maximum transmit power



* **Returns**

    1 if success else -1



#### config_radio_profile_radio_channel(channel_selection=None)

* This keyword is to configure channel in the radio profile


* Keyword Usage:

    
        * `Choose Radio Profile Channel ${CHANNEL}`


* **Parameters**

    **channel_selection** – Select any channel (“1-14” or “36-165”)



* **Returns**

    1 if channel is chosen Successfully else -1



#### config_radio_profile_skip_bg_scan_clients_pwr_save_mode(skip_bg_scan_pwr_save)

* This Keyword is to Skip the Background Scan when clients are in power save mode


* Keyword Usage:

> 
> * `Skip BG Scan When Clients are in Power Save Mode ${CLIENTS_PWR_SAVE_MODE}`

:param skip_bg_scan_pwr_save:Skip background scan when clients are in Power Save Mode
:return: 1 if success else -1


#### config_radio_profile_skip_bg_scan_nw_voice_priority(skip_bg_scan_nw_voice_priority)

* This Keyword is to Skip the Background Scan when clients has Network Voice Priority


* Keyword Usage:

> 
> * `Skip BG Scan When Clients has network voice priority ${CLIENTS_NW_VOICE_PRIORITY}`


* **Parameters**

    **skip_bg_scan_nw_voice_priority** – Skip background scan when clients has network voice priority



* **Returns**

    1 if success else -1



#### config_radio_profile_skip_bg_scan_when_clients_connected(skip_bg_scan_clients_connected)

* This Keyword is to Skip the Background Scan when clients are connected


* Keyword Usage:

> 
> * `Skip BG Scan When Clients Connected ${CLIENTS_CONNECTED}`


* **Parameters**

    **skip_bg_scan_clients_connected** – Skip background scan when clients are connected



* **Returns**

    1 if success else -1



#### config_radio_profile_tx_power_floor(tx_power_floor)

* This keyword is to configure the transmission power floor in radio profile


* Keyword Usage:

> 
> * `Config Radio Profile Tx Power Floor ${TX_PWR_FLOOR}`


* **Parameters**

    **tx_power_floor** – Configure transmission power floor



* **Returns**

    1 if success else -1



#### config_radio_profile_tx_power_max_drop(tx_power_max_drop)

* This keyword is to configure the transmission power max drop in radio profile


* Keyword Usage:

> 
> * `Config Transmission Power Max Drop ${TX_PWR_MAX_DROP}`


* **Parameters**

    **tx_power_max_drop** – Configure transmission power max drop in the radio profile



* **Returns**

    1 if success else -1



#### delete_radio_profile(profile_name='default')

* This keyword deletes a radio profile in radio profile table


* Keyword Usage:

> 
> * `delete_radio_profile   profile_name=abc_20MHz`


* **Parameters**

    **profile_name** – radio profile name



* **Returns**

    1



#### disable_dfs_button(disable_dfs_btn)

* This Keyword is to Disable the DFS button


* Keyword Usage:

> -`Disable DFS Btn ${DFS_BTN}`


* **Parameters**

    **disable_dfs_btn** – disable dfs button



* **Returns**

    1 if success else -1



#### disable_exclude_channels_btn(disable_exclude_channels_opt)

* This keyword is to Disable Exclude Channels option in the radio profile


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Disable Exclude Channels Button ${EXCLUDE_CHANNELS_BUTTON} \`\`


* **Parameters**

    **disable_exclude_channels_opt** – 



* **Returns**

    1 if exclude channels button is disabled successfully else -1



#### enable_DFS_selection()

* This keyword will enable DFS channel selection.


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    enable_DFS_selection’’


#### enable_dfs_button(enable_dfs_btn)

* This Keyword is to Enable the DFS button


* Keyword Usage:

> -`Enable DFS Btn ${DFS_BTN}`


* **Parameters**

    **enable_dfs_btn** – enable dfs button



* **Returns**

    1 if DFS button is enabled else -1



#### enable_exclude_channels_btn(exclude_channels_btn)

* This keyword is to Enable Exclude Channels option in the radio profile


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Enable Exclude Channels Button ${EXCLUDE_CHANNELS_BUTTON} \`\`

:param exclude_channels_btn : Enable Exclude Channels option
:return: 1 if channels are chosen for exclusion Successfully else -1


#### get_radio_profile_details()

* This keyword will retrieve the all fields in the device configuration interface WiFi2 page


* Flow: Manage –> Device –> Click on Device MAC hyperlink –> click on configure –> interface settings –> WiFi2


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    get_device_configuration_interface_WiFi2_details  ‘’


#### save_radio_profile(save_radio_profile)

* This Keyword is to Save the Radio Profile


* Keyword Usage:

> -`Save Radio Profile ${RADIO_PROFILE_NAME}`


* **Parameters**

    **save_radio_profile** – Save the Radio Profile



* **Returns**

    1 if radio profile was saved successfully else -1



#### select_radio_profile_excluded_channels(channels)

* This Keyword selects the valid channels to be exclusive

    
        * Keyword Usage:
    @channels   7 12 4 5

    -

    ```
    ``
    ```

    select_excluded_channels  $channels   \`\`


        * **param channels**

            list of valid channels



        * **return**

            1  else -1



#### verify_radio_profile_channel_width_and_channels(channels, mode='included', channel_width='default')

* This keyword validates the channels to be exclusive, inclusive, by default and not by default


* Keyword Usage:

    @channels    7 12 4 5

-`check_radio_profile_channel_width_and_channels  $channels  mode=included  channel_width=80`

    
    * **param channels**

        list of valid channels



    * **param mode**

        channel is either enabled, disabled, included, excluded channel



    * **param channel_width**

        channel width



    * **return**

        1  else - 1



#### verify_uni_group_channels(channels, group_channel, mode='excluded', radio_modes='5GHz', channel_width='20MHZ')

* This keyword verifies a excluded channels group of Uni for the 80 Mhz, 40 Mhz and 20 MHz


* Keyword Usage:

    
        * 

    ```
    ``
    ```

    verify_uni_group_exclusded_channels  [5,12,5,6]  group_channel=uni-1   mode=excluded  ‘’


* **Parameters**

    
    * **channels** – list of channels in Uni group


    * **group_channel** – either uni-1, uni-2, uni-3, uni-4, uni-5, uni-6, uni-7, uni-8


    * **mode** – excluded or included, disabled, enabled


    * **radio_modes** – either 5GHz or 6GHz


    * **channel_width** – either 20, 40, 80 MHz


## extauto.xiq.flows.configure.RadiusServer module


### _class_ extauto.xiq.flows.configure.RadiusServer.RadiusServer()
Bases: `RSWebElements`


#### config_external_radius_server(\*\*ext_server_config)

* This keyword is called in two ways, as standalone and as part of create network policy


* For standalone assumes that user navigated to the RADIUS server group add dialog window


* Create new external RADIUS server


* refer “Creating RADIUS Server group profile” section for ext_server_config dict in

captive_web_portal_config.robot
- Keyword Usage:

> 
> * `Config External RADIUS Server   &{EXT_SERVER_CONFIG}`


* **Parameters**

    **ext_server_config** – dict to create the external RADIUS server



* **Returns**

    1 if external RADIUS server group created else -1



#### config_extreme_networks_radius_server(\*\*extreme_networks_server_config)

* This keyword called two ways standalone way and as part of crete network policy keyword


* for standalone assumes that user navigated the RADIUS server group add window


* Assumes that navigated to RADIUS server add window


* Create new external RADIUS server


* refer “Creating RADIUS Server group profile” section for ext_server_config dict in

    enterprise_dot11x_config.robot


* Keyword Usage:

> 
> * `Config Extreme Network RADIUS Server   &{extreme_networks_server_config}`


* **Parameters**

    **extreme_networks_server_config** – dict to create the extreme radius server



* **Returns**

    1 if external RADIUS server group created else -1



#### config_radius_server(\*\*rs_group_config)

* Configuring the RADIUS server


* **Parameters**

    **rs_group_config** – 



* **Returns**

    1 if RADIUS server already exists else add the radius server group



#### delete_radius_server_group(rs_group_name)

* Select the RADIUS server group and delete it


* Keyword Usage:

> 
> * `Delete RADIUS Server Group   ${RS_GROUP_NAME}`


* **Parameters**

    **rs_group_name** – 



* **Returns**

    True if deleted else False


## extauto.xiq.flows.configure.RouterTemplate module


### _class_ extauto.xiq.flows.configure.RouterTemplate.RouterTemplate()
Bases: `RouterTemplateWebElements`


#### add_router_template(nw_policy, \*\*template_config_settings)

* Create New Router Template on Network Policy Router Settings If Not exists already


* Keyword Usage

> 
> * `Add Router Template     ${NW_POLICY_NAME}     &{ROUTER_TEMPLATE_CONFIG}`


* **Parameters**

    
    * **nw_policy** – Network Policy Name


    * **template_config_settings** – (Config Dict) router_model,template_name,interface_name,new_port_type_config,
    network_allocation_config,vlan_object_config,sub_network_config



* **Returns**

    1 if Router Template Configured Successfully



#### check_router_template(router_template)

* Check the router template in Router template Grid


* Keyword Usage

> 
> * `Check router Template  ${ROUTER_TEMPLATE_NAME}`


* **Parameters**

    **router_template** – Router Template Name ie XR200P,XR600P



* **Returns**

    True if Router Template Found on Grid else False



#### configure_advanced_subnetwork_section(\*\*advance_config)

* Configure Advanced Subnetwork Section on Router Template


* Keyword Usage

> 
> * `Configure Advanced Subnetwork Section  &{SUB_NETWORK_ADVANCED_SETTINGS}`


* **Parameters**

    **advance_config** – Config Dictionary Parameters of Subnetwork Advanced settings



* **Returns**

    return True if Config Successful



#### configure_basic_subnetwork_section(\*\*basic_config)

* Configure Basic Subnetwork section on Router Template


* Keyword Usage

> 
> * `Configure Basic Subnetwork Section   &{SUB_NETWORK_BASIC_SETTINGS}`


* **Parameters**

    **basic_config** – (Config Dictionary) include sub_network_name,sub_network_description,network_type,
    unique_subnetwork,local_ip_address_space,gateway_options



* **Returns**

    return True if Configuration Successful



#### configure_network_allocation_sub_network(\*\*network_allocation_sub_network_settings)

* Configure network allocation sub network on Router Template


* Keyword Usage

> 
> * `Configure Network Allocation Sub Network   &{SUB_NETWORK_SETTINGS}`


* **Parameters**

    **network_allocation_sub_network_settings** – (Config Dictionary) includes Basic and Advanced sub network
    Parameters



* **Returns**

    return True if Configuration Successful



#### configure_network_allocation_vlan(\*\*network_allocation_vlan_settings)

* Configure Network Allocation VLAN on Router Template


* Keyword Usage

> 
> * `Configure Network Allocation VLAN   &{VLAN_CONFIG_SETTINGS}`


* **Parameters**

    **network_allocation_vlan_settings** – (Config Dictionary) Vlan Name and Vlan ID



* **Returns**

    return True if Config Successful



#### configure_new_port_traffic_filter_management(\*\*port_type_settings)

* Configure New Port Traffic Filter Management ie SSH,Telnet,Ping,SNMP


* Keyword Usage

> 
> * `Configure New Port Traffic Filter Management   &{PORT_TYPE_SETTINGS}`


* **Parameters**

    **port_type_settings** – (Configuration Dictionary) To enable/Disable Status of SSH,Telnet,Ping,SNMP



* **Returns**

    return True if Configuration successful



#### configure_new_port_type(\*\*port_type_settings)

* Configure New Port type on Router Interface


* Keyword Usage

> 
> * `Configure New Port Type   &{PORT_TYPE_CONFIG}`


* **Parameters**

    **port_type_settings** – (Config Dict) port_type_name,description,port_status,port_usage_config,
    traffic_filter_settings



* **Returns**

    return 1 if Port type Configuration successful else -1



#### configure_port_type_config(\*\*port_usage_configuration)

* This keyword is used to do port type configuration


* Keyword Usage

> 
> * `Configure Port Type Config   &{PORT_USAGE_CONFIG}`


* **Parameters**

    **port_usage_configuration** – (Configuration Dictionary) Port Usage Configuration ie Access,Trunk,WAN



* **Returns**

    return 1 if Configuration successful else -1



#### delete_router_template(nw_policy, template_name)

* Delete Router Template Name Row from Network Policy–>Router settings–> Device Template


* Keyword Usage

> 
> * `Delete Router Template  ${NW_POLICY_NAME}  ${ROUTER_TEMPLATE_NAME}`

:param nw_policy : Network Policy Name
:param template_name: Router Template Name
:return:  True if router Template deleted successfully else returns False


#### navigate_to_router_settings_tab(nw_policy)

* To Navigate to Existing Network Policy’s Router Settings Tab


* Keyword Usage

> 
> * `Navigate To Router Settings Tab  ${NETWORK_POLICY_NAME}`


* **Parameters**

    **nw_policy** – Network Policy Name



* **Returns**

    True If Navigation successful else None



#### select_interface_to_add_new_port_type(interface_name)

* Selects the Router Interface To Configure New Port Type.


* Keyword Usage

> 
> * `Select Interface To Add New Port Type     ${INTERFACE_NAME}`


* **Parameters**

    **interface_name** – Router Interface Name ie ETH0,ETH1,ETH2



* **Returns**

    return 1 if Router Interface selected correctly else -1



#### select_router_template_row(template_name)

* Select Router Template Name Row from Network Policy–>Router settings–> Device Template


* Keyword Usage

> 
> * `Select Router Template Row   ${ROUTER_TEMPLATE_NAME}`


* **Parameters**

    **template_name** – Router Template Name



* **Returns**

    return True if Router Template Name found in the Row


## extauto.xiq.flows.configure.SwitchTemplate module


### _class_ extauto.xiq.flows.configure.SwitchTemplate.SwitchTemplate()
Bases: `object`


#### add_5520_sw_stack_template(model_units, nw_policy, sw_model, sw_template_name, save_template=True)

* Checks the given STACK switch template present already in the switch Templates Grid


* If it is not there add to the sw_template


* This function is working only for stack


* Keyword Usage

> 
> * \`\`  ${MODEL_UNITS} ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}\`\`


> * e.g. Add Sw Stack Template                           5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS
> …                             bgd2        EXOS-5520-Series-Stack          politicamea      True


* **Parameters**

    
    * **model_units** – a string will all units e.g 5520-24T,5520-24X,5520-48T


    * **nw_policy** – network policy


    * **sw_model** – Switch Model  ie EXOS-5520-Series-Stack


    * **sw_template_name** – Switch Template Name e.g mypolicy


    * **save_template** – True - will save the template ; False - will not save the template (More configures can be added after)



* **Returns**

    1 if Switch Template Configured Successfully else -1



#### add_5520_sw_template(nw_policy, sw_model, sw_template_name, save_template=True)

* Checks the given switch template present already in the switch Templates Grid


* If it is not there add to the sw_template


* This function is working only for stack


* Keyword Usage

> 
> * \`\`  ${MODEL_UNITS} ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}\`\`


> * e.g. Add Sw Stack Template                           5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS
> …                             bgd2        EXOS-5520-Series-Stack          politicamea      True


* **Parameters**

    
    * **model_units** – a string will all units e.g 5520-24T,5520-24X,5520-48T


    * **nw_policy** – network policy


    * **sw_model** – Switch Model  ie EXOS-5520-Series-Stack


    * **sw_template_name** – Switch Template Name e.g mypolicy


    * **save_template** – True - will save the template ; False - will not save the template (More configures can be added after)



* **Returns**

    1 if Switch Template Configured Successfully else -1



#### add_supplimental_cli_into_template(nw_policy, sw_template_name, s_cli_name, commands=None)
This function is used to add commands into S-CLI by using network policy and template
:param nw_policy: name of policy
:param sw_template_name: name of template
:param s_cli_name: name of s-cli profile
:param commands:  The commands which will be added into S-CLI. Multiple commands are supported
:return:


#### add_sw_template(nw_policy, sw_model, sw_template_name)

* Checks the given switch template present already in the switch Templates Grid


* If it is not there add to the sw_template


* Keyword Usage

> 
> * `Add SW Template  ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}`


* **Parameters**

    
    * **nw_policy** – network policy


    * **sw_model** – Switch Model ie SR2348P


    * **sw_template_name** – Switch Template Name ie template_SR2348P



* **Returns**

    1 if Switch Template Configured Successfully else -1



#### add_to_string(added_string, string)

#### assign_switch_template(nw_policy, sw_template_name)

* Checking the sw template present in the sw Templates Grid


* If it is not there add to the sw_template


* Keyword Usage

> 
> * `Assign SW Template  ${POLICY_NAME}  ${SW_TEMPLATE_NAME}`


* **Parameters**

    
    * **nw_policy** – Name of policy to assign the switch template to


    * **sw_template_name** – Name of the switch template to assign; e.g., SR_2348P-default-template



* **Returns**

    1 if switch template was assigned successfully, else -1



#### check_added_sw_stack_template_units(model_units, sw_template_name)

* Flow: First page from stack template


* This function is working only for stack. It checks if the names of units have correct format


* Keyword Usage

> 
> * e.g. check added sw stack template units      5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS     myTemplate


* **Parameters**

    
    * **model_units** – a string with all units e.g 5520-24T,5520-24X,5520-48T


    * **sw_template_name** – Switch Template Name; ie mypolicy



* **Returns**

    1 if all expected units are displayed in policy and the names match; else -1 ;
    ‘more’ - If more units are found into policy than into CLI;
    ‘less’ - If less units are found into policy than into CLI;



#### check_sw_template(sw_template)

* Check the Switch template in the Switch template Grid


* Assumes That Already in Network Policy Edit Page


* Keyword Usage

> 
> * `Check SW Template  ${SWITCH_TEMPLATE_NAME}`


* **Parameters**

    **sw_template** – Switch Template Name ie SR2024P,X440-G2-24p-10G4 etc



* **Returns**

    True if Switch Template Found on Grid else False



#### check_type_sw_stack_template_units(model_units)

* Flow: First page from stack template


* This function is working only for stack. It checks if the type of units are the same in XIQ and CLI


* Keyword Usage

> 
> * e.g. check added sw stack template units      5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS     myTemplate


* **Parameters**

    **model_units** – a string with all units e.g 5520-24T-EXOS,5520-24X-EXOS



* **Returns**

    1 if all expected units are displayed in policy and the names match; else -1 ;



#### config_vlan_in_template(port_string, vlan_number, port_type_name, stp_disable='false')

#### configure_oob_mgmt_int(nw_policy, sw_template_name, mgmtVlan='4092')

* Checks able to configure OOB Mgmt interface


* This function is working only if switch template already created


* Keyword Usage

> 
> * \`\`  ${NW_POLICY}  ${SW_TEMPLATE_NAME} ${MGMTVLAN}


> * e.g. configure_oob_mgmt_int bgd2 politicamea 4092


* **Parameters**

    
    * **nw_policy** – network policy


    * **sw_template_name** – Switch Template Name e.g mypolicy


    * **mgmtVlan** – 4092 -vlan range need to be (1-4093)



* **Returns**

    1 if Switch Template OOB mgmt interface Configured Successfully else -1



#### create_pse_profile(network_policy_name, device_template_name, device_model, port_type_name, pse_profile_name, power_limit, priority, power_mode)

* This Function creates a new PSE Profile from Network Policy Device Template


* Keyword Usage :     Create Pse Profile      ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}   ${PSE_PROFILE_NAME}          ${POWER_LIMIT}             ${PRIORITY}             ${POWER_MODE}

:param Network Policy Name -> Name of network policy
:param DEVICE_TEMPLATE_NAME -> Name of Device Template
:param DEVICE_MODEL     -> Device Model that should be found in the Template list
:param PORT_TYPE_NAME   -> String, for Device Port Type
:param PSE_PROFILE_NAME -> String, for PSE Profile Name
:param POWER_LIMIT     ->  Float Value
:param PRIORITY        -> Value chosen from the following options    low, high or critical     any other is not accepted by the function
:param POWER_MODE      -> Value chosen from the following options  802.3af or 802.3at or 802.3bt     any other is not accepted by the function
:return: 1 if the pse profile is created and saved else -1 ;


#### create_vlan_in_stacked_template(nw_policy, sw_template_name, slot, port, vlan, port_type_name, stp_disable='false')

* Create Vlan In Stacked Template


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Create Vlan In Stacked Template     ${nw_policy}  ${sw_template_name}  ${slot}  ${port}  ${vlan}

>     ${port_type_name}\`\`


* **Parameters**

    **nw_policy** – Name of the policy


:param sw_template_name : Name of the template
:param slot: Number of the slot
:param port: Number of the port
:param vlan : Number of the vlan
:param port_type_name : Name of the port type
:return: 1 if vlan creation was successful


#### create_vlan_in_template(policy_name, template_name, port, vlan, port_type_name, stp_disable='false')

* Create Vlan In Template


* Keyword Usage:

> 
> * `Create Vlan In Template     ${policy_name}  ${template_name}  ${port}  ${vlan_number}`


* **Parameters**

    **policy_name** – Name of the policy


:param template_name : Name of the template
:param port : Number of the port
:param vlan : Number of the vlan
:param port_type_name : Name of the port type
:return: 1 if vlan creation was successful


#### delete_stack_switch_template(nw_policy, sw_template_name)
> This function is used to delete a template from a policy


* **Parameters**

    
    * **nw_policy** – 


    * **sw_template_name** – 



* **Returns**

    1 if template was deleted or template doesn’t exist; else -1



#### delete_stack_units_device_template(nw_policy, sw_template_name)
This function deletes the unit’s template from a policy


* **Parameters**

    
    * **nw_policy** – Policy name


    * **sw_template_name** – template name



* **Returns**

    


#### delete_switch_template_from_policy(nw_policy, sw_template_name, \*\*kwargs)

* This keyword will delete the switch template from a newtwork policy


* Flow: Network Policies -> Edit nw_policy -> Device Templates -> Select Template -> Delete Template


* **Parameters**

    
    * **nw_policy** – The name of the network policy


    * **sw_template_name** – The name of the template



* **Returns**

    Returns 1 if template is succesfully deleted,
    Returns -1 if network policy not found



#### edit_port_type(port_list, port_type)

#### get_sw_template_row(sw_template)

* Get the switch template row element on Network Policy’s Switch Templates Grid


* Keyword Usage

> 
> * `Get SW Template Row  ${SW_TEMPLATE_NAME}`


* **Parameters**

    **sw_template** – name of the sw_template



* **Returns**

    Switch Template Cell present on row



#### go_to_port_configuration()

#### poe_status_button(network_policy_name, device_template_name, device_model, port_type_name, poe_status)

* This Function modifies, turns off or on the POE Status


* Keyword Usage : Poe Status Button           ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}

:param Network Policy Name -> Name of network policy
:param DEVICE_TEMPLATE_NAME -> Name of Device Template
:param DEVICE_MODEL     -> Device Model that should be found in the Template list
:param PORT_TYPE_NAME   -> String, for Device Port Type
:param POE_STATUS       -> String, could be “on”, “On”, “off” or “Off”
:return: 1 if poe status is turned off else -1 ;


#### poe_toggle_using_existing_port_type(network_policy_name, device_template_name, device_model, existing_port_type_option, poe_status)

* This Function modifies, turns off or on the POE Status on existing port type


* Keyword Usage : Poe Status Button           ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}

:param Network Policy Name -> Name of network policy
:param DEVICE_TEMPLATE_NAME -> Name of Device Template
:param DEVICE_MODEL     -> Device Model that should be found in the Template list
:param PORT_TYPE_NAME   -> String, for Device Port Type
:param POE_STATUS       -> String, could be “on”, “On”, “off” or “Off”
:return: 1 if poe status is turned off else -1 ;


#### save_stack_template()
Flow: First page from stack template
This function save the template after the configuration was made
return 1 if template was saved ; else -1


#### select_assign_choose_existing_port_type(port_type_name)

#### select_assign_create_new_port_type(port_type)

#### select_sw_template(nw_policy, sw_template)

* This Keyword will Select the Switch Template on Network Policy


* Keyword Usage

> 
> * `Select SW Template  ${NW_POLICY_NAME}  ${SW_TEMPLATE_NAME}`


* **Parameters**

    
    * **nw_policy** – Name of the Network Policy to select Switch Template


    * **sw_template** – Name of the sw_template



* **Returns**

    1 If successfully Selected Switch template



#### select_wireframe_net_ports(ports)

#### set_legacy_port_type_fields(port_type)

#### sw_template_stack_select_slot(slot, \*\*kwargs)

* Assume that already in Device Template Port Configuration


* **Parameters**

    **slot** – “The slot number that needs to be selected”



* **Returns**

    Returns 1 if slot found and clicked
    Returns -1 if otherwise



#### switch_template_save()

#### template_assign_ports_to_an_existing_port_type(ports, port_type_name, \*\*kwargs)

* This keyword will assign multiple ports in a template to an existing port type


* Assumes That Already in Device Template Port Configuration


* Flow: Select the ports -> Assign -> Choose Existing -> Select and existing Port Type -> Save


* **Parameters**

    
    * **policy_name** – The name of the network policy


    * **sw_template** – The name of the switch template


    * **ports** – The port interfaces [written as 1,2,4…]


    * **port_type_name** – The existing port type name



* **Returns**

    returns 1 if the ports have been assigned the existing port type
    returns -1 if otherwise



#### verify_sw_template_port_desc(port_list, description, default)

#### verify_sw_template_port_status(port_list, status, default)

#### verify_sw_template_port_type(port_list, port_type, default_port_type)

#### verify_sw_template_port_usage(port_list, port_type_name, default)
## extauto.xiq.flows.configure.UserGroups module


### _class_ extauto.xiq.flows.configure.UserGroups.UserGroups(\*\*kwargs)
Bases: `UserGroupsWebElements`


#### add_bulk_user_to_user_group(\*\*user_info)

* Add bulk users to User Groups


* Keyword Usage:

> 
> * `Add Bulk User To User Group    &{USER_INFO}`


> * For creating the &{USER_INFO} dict refer user_group_config.robot

:param user_info:(dict)  buk user config parameters
:return: True if created else False


#### add_multiple_user_to_user_group(password_db_loc, \*\*user_info)

* Add the multiple user to User Group


* multiple users options are different based on password_db_loc


* Keyword Usage:

> 
> * `Add Multiple User To User Group    ${PASSWORD_DB_LOC}    &{USER_INFO}`


> * For creating &{USER_INFO} refer user_group_config.robot


* **Parameters**

    
    * **user_info** – (dict)  Multiple user config parameters


    * **password_db_loc** – it will take either local or cloud



* **Returns**

    True if created else False



#### add_single_user_to_user_group(password_db_loc, \*\*user_info)

* Add the single user to User Groups


* single users options are different based on password_db_loc


* Keyword Usage:

> 
> * `Add Single User To User Group    ${PASSWORD_DB_LOC}    &{USER_INFO}`


> * For creating &{USER_INFO} refer user_group_config.robot


* **Parameters**

    
    * **user_info** – (dict)  Single user config parameters


    * **password_db_loc** – it will take either local or cloud



* **Returns**

    True if created else False



#### add_wireless_nw_user_group(group_name='Demo', user_group_profile=None)

* supports to create the user groups from wireless network page


* there are two ways to call this keyword


* standalone: Assumes that already navigated to the wireless network tab


* Keyword Usage:

> 
> * `Add Wireless Nw User Group   ${GROUP_NAME}   &{USER_GROUP_PROFILE}`


* **Parameters**

    
    * **group_name** – (str)  Name of the group to create


    * **user_group_profile** – (dict)  Config Parameters to create the user groups refer user_groups_config for
    different combination of user group profile



* **Returns**

    1 if success else -1



#### create_add_user_to_user_group(user_group, \*\*user_info)

* Add the single user to existing User Groups


* Keyword Usage:

> 
> * `Create Add User To User Group    ${user_group}    &{USER_INFO}`


> * For creating &{USER_INFO} refer user_group_config.robot


* **Parameters**

    
    * **user_info** – (dict)  Single user config parameters


    * **user_group** – Existing User Group name to which the user will be added



* **Returns**

    1 if created else -1



#### create_user_group(group_name='Demo', user_group_profile=None)

* Flow: Configure –> Users –> User Groups


* Create User Groups and add users to user Groups


* Keyword Usage

> 
> * `Create User Group   group_name=${GROUP_NAME}   user_group_profile=&{USER_GROUP_PROFILE}`


> * for supported combination of  &{USER_GROUP_PROFILE} creation refer  “user_group_config.robot”


* **Parameters**

    
    * **group_name** – Name of the user group


    * **user_group_profile** – (dict)  configuration parameter



* **Returns**

    1 if created else -1



#### delete_all_user_groups(\*\*kwargs)

* Delete all custom user groups


* Keyword Usage:


* `delete_all_user_groups    IRV=True`


* **Parameters**

    **IRV** – if False, the error will skip, otherwise, error will not skip



* **Returns**

    1 if deleted successfully else -1



#### delete_single_user(user)

* Delete single user from existing User Group


* Keyword Usage:

> 
> * `Delete single User    ${user}`


* **Parameters**

    **user** – username



* **Returns**

    1 if deleted else -1



#### delete_user_group(user_group_name)

* Flow Configure –> Users –> User Groups


* Delete the User Groups form User Groups grid


* Keyword Usage:

> 
> * `Delete User Group   ${USER_GROUP_NAME}`


* **Parameters**

    **user_group_name** – Name of the user group



* **Returns**

    1 if deleted successfully else -1



#### delete_user_groups(\*groups)

* Delete the multiple user groups form user groups grid


* Keyword Usage:

> 
> * `Delete User Groups    ${GROUP_NAME1}   ${GROUP_NAME2}`


* **Parameters**

    **groups** – groups names



* **Returns**

    1 if deleted successfully else -1



#### edit_single_user_password(user, password)

* Edit and change password of single user from existing User Group


* Keyword Usage:

> 
> * `Edit Single User Password   ${user}    ${password}`


* **Parameters**

    
    * **user** – username


    * **password** – password



* **Returns**

    1 if edited else -1



#### select_wireless_user_group(group_name, passwd_db_loc='None', passwd_type='None')
> 
> * Select the wireless user group from select window if it already created


> * Keyword Usage:


> * 

> ```
> ``
> ```

> Select Wireless User Group   group_name=${GROUP_NAME}   passwd_db_loc=&{PASSWD_DB_LOC}

>     passwd_type=${PASSWD_TYPE}’’


* **Parameters**

    
    * **group_name** – name of the user group


    * **passwd_db_loc** – password DB location


    * **passwd_type** – Password type



* **Returns**

    True if group select else False



#### select_wireless_user_profile(profile_name)
> 
> * Select the wireless user Profile from select window if it already created


> * Keyword Usage:


> * 

> ```
> ``
> ```

> Select Wireless User Group   profile_name=${PROFILE_NAME}’’


* **Parameters**

    **Profile_name** – name of the user group



* **Returns**

    True if User profile selected Successfully else False


## extauto.xiq.flows.configure.UserProfile module


### _class_ extauto.xiq.flows.configure.UserProfile.UserProfile()
Bases: `UserProfileWebElements`


#### add_user_profile(profile='user004', vlan_name='vlan004', vlan_id='004')

* It adds user profile and VLAN

-Flow: Configure –> Common Objects –> User Profile

    
    * Keyword Usage:

    > 
    > * `Add User Profile       profile=${PROFILE}    vlan_name=${VLAN_NAME}   vlan_id=${VLAN_ID}`

:param profile : profile name
:param vlan_name: VLAN name
:param vlan_id: VLAN id
:return: 1

## extauto.xiq.flows.configure.Users module

## extauto.xiq.flows.configure.Wips module


### _class_ extauto.xiq.flows.configure.Wips.Wips()
Bases: `WipsWebElements`


#### add_allowed_ssid_on_network_wips_policy(policy_name, ssid_name, auth_type)
> 
> * Configure Allowed SSID and Encryption Type on WIPS Policy


> * Flow  Network policy list—>Select Network Policy Edit—> Additional Settings—>Security–>WIPS–>

>     Enable Detect Rogue Based on SSID and Encryption Type


> * Keyword Usage

> > 
> > * `Add Allowed SSID On Network WIPS Policy  ${NW_POLICY_NAME}  ${SSID_NAME}  ${AUTH_TYPE}`


* **Parameters**

    
    * **policy_name** – Network Policy Name


    * **ssid_name** – SSID Name to Allow on WIPS Policy Configured


    * **auth_type** – Encryption Type ie OPEN Authentication


:return:1 if Allowed SSID configured On WIPS Policy else -1


#### configure_allowed_ssid_on_wips_policy(\*\*wips_ssid_config)
> 
> * Configure Allowed SSID and Encryption Type on WIPS Policy On Common Objects.


> * Flow  Common Objects–>WIPS–> Click Add Button on Enable Detect Rogue Based on SSID Name and Encryption Type


> * Keyword Usage

> > 
> > * `Configure Allowed Ssid On Wips Policy   &{WIPS_SSID_CONFIG}`

:param  wips_ssid_config : (dict) include allowed_ssid, authentication_type
:return: 1 if SSID and Encryption type added on WIPS Policy on Common Objects else -1


#### configure_reuse_wips_policy_on_network_policy(nw_policy, wips_policy_name)
> 
> * Select the Configured WIPS Policy on Network Policy


> * Flow  Configure–> Network policy Name Edit—> Router Settings –> Security–> WIPS–> Reuse WIPS Policy


> * Keyword Usage

> > 
> > * `Configure Reuse Wips Policy On Network Policy  ${NW_POLICY_NAME}  ${WIPS_POLICY_NAME}`


* **Parameters**

    
    * **nw_policy** – network policy name


    * **wips_policy_name** – wips policy name



* **Returns**

    return 1 if WIPS Policy Name selected and applied successfully on Network Policy else -1



#### configure_wips_options_on_network_policy(policy_name, \*\*wips_config_profile)
> 
> * Creates WIPS Policy On Network Policy based on the arguments from wireless_networks_config.robot


> * Flow  Network policy list—>Select Network Policy Edit—> Additional Settings—>Security–>WIPS


> * Keyword Usage

> > 
> > * `Configure WIPS Options On Network Policy  ${NW_POLICY_NAME}   &{WIPS_CONFIG_SETTINGS}`


* **Parameters**

    
    * **policy_name** – Network Policy Name


    * **wips_config_profile** – (dict) include status of rougue ap detection, detect rogue ap based on Mac and ssid.


:return:1 if WIPS Policy Options Configured on Network Policy else -1


#### configure_wips_policy_on_common_objects(wips_policy_name)
> 
> * Configure WIPS Policy On Common Objects.


> * Flow  Configure—>Common Objects—>Security–>WIPS Policies–> Add


> * Keyword Usage

> > 
> > * `Configure WIPS Policy On Common Objects   {WIPS_POLICY_NAME}`

:param  wips_policy_name : WIPS Policy Name
:return: 1 if WIPS POlicy Created on Common Objects else -1


#### create_wips_policy_adess_status_on_common_objects(wips_policy_name, status)
> 
> * Configure WIPS Policy On Common Objects.


> * Flow  Configure—>Common Objects—>Security–>WIPS Policies–> Add


> * Keyword Usage

> > 
> > * `Configure WIPS Policy On Common Objects   ${wips_policy_name} Enable/Disable`


* **Parameters**

    **wips_policy_name** – wips policy name



* **Returns**

    1 if WIPS POlicy Created on Common Objects else -1



#### disable_wips_on_network_policy(nw_policy)
> 
> * This Keyword will disable WIPS on Network Policy


> * Flow  Configure–> Network policy Name Edit—> Router Settings –> Security–> WIPS–> Disable WIPS


> * Keyword Usage

> > 
> > * `Disable Wips On Network Policy  ${NW_POLICY_NAME}`


* **Parameters**

    **nw_policy** – network policy name



* **Returns**

    return 1 if WIPS disabled successfully on Network Policy else -1



#### enable_wips_on_network_policy(policy_name, wips_name)

* Enable wips on Network Policy


* Flow  Network policy list—>Select Network Policy Edit—> Additional Settings—>Security–>WIPS


* Keyword Usage

> 
> * `Enable Wips On Network Policy  ${NETWORK_POLICY_NAME}   ${WIPS_POLICY_NAME}`


* **Parameters**

    
    * **policy_name** – Network Policy Name


    * **wips_name** – WIPS Policy Name



* **Returns**

    1 if WIPS Policy enabled Successfully on Network Policy else -1



#### get_rogue_ap_logs_row(search_string)
> 
> * Get the Rogue Aps Logs Row from Manage–>Security


> * Flow  Manage–> Security—> Rogue AP –> Row String


> * Keyword Usage

> > 
> > * `Get Rogue AP Logs Row    ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell



* **Returns**

    row element if row exists else return None



#### get_rogue_client_logs_row(search_string)
> 
> * Get the Rogue Clients Logs Row from Manage–>Security


> * Flow  Manage–> Security—> Rogue clients –> Row String


> * Keyword Usage

> > 
> > * `Get Rogue Client Logs Row    ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell



* **Returns**

    row element if row exists else return None



#### navigate_to_network_policy_edit_tab(policy_name)
> 
> * Navigates to Network Policies List and Edit the Specific Network Policy


> * Flow  Network policy list–>Select List View–>Select Network Policy ROW–> Edit


> * Keyword Usage

> > 
> > * `Navigate To Network Policy Edit Tab  ${NETWORK_POLICY_NAME}`


* **Parameters**

    **policy_name** – Network Policy Name


:return:1 if Navigates to Network Policy edit


#### navigate_to_network_policy_wips_tab(nw_policy)
> 
> * To Navigate to Existing Network Policy —>Router Settings –> Security–> WIPS


> * Flow  Configure–> Network policy list—>Select Network Policy Edit—> Router Settings –> Security–> WIPS


> * Keyword Usage

> > 
> > * `Navigate To Network Policy Wips Tab  ${NW_POLICY_NAME}`


* **Parameters**

    **nw_policy** – Network Policy Name


:return:1 if Navigated to Existing Network Policy Router Settings WIPS Tab else -1


#### select_allowed_mac_oui_on_network_wips_policy(policy_name, mac_oui_name)
> 
> * Select allowed MAC OUI on Network Wips Policy


> * Flow  Network policy list—>Select Network Policy Edit—> Additional Settings—>Security–>WIPS–>

>     Enable Detect Rogue Based on MAC OUI


> * Keyword Usage

> > 
> > * `Select Allowed Mac OUI On Network Wips Policy    ${NW_POLICY_NAME}   ${MAC_OUI}`


* **Parameters**

    
    * **policy_name** – Network Policy Name


    * **mac_oui_name** – MAC OUI Name to Allow on WIPS Policy


:return:1 if Allowed MAC OUI configured On WIPS Policy else -1


#### verify_rogue_ap(search_string)
> 
> * Filter the Rogue AP based on AP Name


> * Flow  Manage–> Security—> Rogue AP


> * Keyword Usage

> > 
> > * `Verify Rogue AP   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell



* **Returns**

    if search string appear Return Rogue AP entry details as dictionary with key and value pair else -1



#### verify_rogue_client(search_string)
> 
> * Filter the Rogue Client based on Client Name Search String


> * Flow  Manage–> Security—> Rogue Clients


> * Keyword Usage

> > 
> > * `Verify Rogue Client   ${SEARCH_STRING}`


* **Parameters**

    **search_string** – it should be anything which is searched on the row cell



* **Returns**

    if search string appear Return Rogue client entry details as dictionary with key and value pair else -1



#### wips_onprem_adsp_serverip_configuration_on_network_policy(nw_policy, wips_policy, status, \*\*onprem_adspip_config)

* Enable/Disable on prem Airdefense Configuration in Wips Of Network Policy


* Flow  Network policy list—>Select Network Policy Edit—> Additional Settings—>Security–>WIPS–>Airdefense Configuration


* Keyword Usage

> 
> * `Wips onprem adsp serverip configuration on Network Policy  ${NW_POLICY_NAME}  ${WIPS_POLICY_NAME}  enable  &{ON_PREM_ADSP_SERVER_IP_CONFIG}`


> ```
> ``
> ```

> Wips onprem adsp serverip configuration on Network policy  ${NW_POLICY_NAME}  ${WIPS_POLICY_NAME}  disable \`\`


* **Parameters**

    
    * **NW_POLICY** – Network Policy Name


    * **WIPS_POLICY** – WIPS Policy Name


    * **status** – Enable/ Disable


:param  ON_PREM_ADSP_SERVER_IP_CONFIG : (dict) include primary server IP and port, secondary server IP and port
:return: 1 if WIPS Policy saved Successfully on Network Policy else -1

## extauto.xiq.flows.configure.WirelessCaptiveWebPortal module


### _class_ extauto.xiq.flows.configure.WirelessCaptiveWebPortal.WirelessCaptiveWebPortal()
Bases: `WirelessCWPWebElements`


#### create_cloud_pin_cwp(\*\*cloud_pin_cwp_profile)

* This keyword is used to create cloud pin based cwp


* there are two ways to call this keyword


* 
    1. standalone, for this assumption is already navigated to the wireless network tab


* Keyword Usage:

> 
> * `Create Cloud Pin CWP   &{CLOUD_PIN_CWP_PROFILE}`


> * For &{CLOUD_PIN_CWP_PROFILE}  dict creation refer cloud_pin_config.robot


* 
    1. called by “create_open_network_captive_web_portal”


* **Parameters**

    **cloud_pin_cwp_profile** – (dict) configuration parameters to create cloud pin based cwp



* **Returns**

    1 if created or selected, else -1



#### create_cloud_social_login_cwp(\*\*social_cwp_profile)

* This keyword is used to create the cloud social login type CWP


* There are two ways to call this method


* 
    1. called by create_open_network_captive_web_portal


* 
    1. standalone call. for this pre-condition is already navigated to the wireless network tab


* Keyword Usage:

> 
> * `Create Cloud Social Login CWP  &{SOCIAL_LOGIN_CWP_PROFILE}`


> * For creation of different combination &{SOCIAL_LOGIN_CWP_PROFILE} dict refer social_login_config.robot


* **Parameters**

    **social_cwp_profile** – (dict) configuration profile



* **Returns**

    1 if created else -1



#### create_cloud_social_login_ege(\*\*social_cwp_profile)

* This keyword is used to create the guest social login type eguest


* There are two ways to call this method


* 
    1. called by create_open_network_captive_web_portal


* 
    1. standalone call. for this pre-condition is already navigated to the wireless network tab


* Keyword Usage:

> 
> * `Create Cloud Social Login EGE  &{SOCIAL_LOGIN_CWP_PROFILE}`


* **Parameters**

    **social_cwp_profile** – (dict) configuration profile



* **Returns**

    1 if created else -1



#### create_default_captive_web_portal(\*\*cwp_config)

* This keyword is used to create the default captive web portal with below combinations


* “User Auth on Captive Web Portal”, “Enable Self-Registration”, “Return Aerohive Private PSK”,
“Enable UPA”


* There are two way to call this keyword


* 
    1. called by create_open_network_captive_web_portal


* 
    1. standalone, Assumption is already navigated to the wireless network tab


* Keyword Usage:

> 
> * `Create Default Captive Web Portal  &{DEFAULT_CWP_CONFIG}`


* **Parameters**

    **cwp_config** – (dict) captive web portal config parameters



* **Returns**

    1 if config success else -1



#### create_enterprise_wireless_network_cwp(\*\*cwp_config)

* Create captive web portal for enterprise wireless network


* This is called as part of enterprise wireless network creation


* For standalone call assumes that already navigated to the wireless network page,
selected the enterprise auth type


* Keyword Usage:

> 
> * `Create Enterprise Wireless Network Cwp    &{CWP_CONFIG}`


* **Parameters**

    **cwp_config** – (dict) configuration



* **Returns**

    1 if created else -1



#### create_open_network_captive_web_portal(\*\*cwp_profile)

* If Authentication type is open, below are ways to create the CWP

> 
> * default captive web portal

> > 
> > * This consists of below 4 options

> > > 
> > > * User Auth on Captive Web Portal


> > > * Enable Self-Registration


> > > * Return Aerohive Private PSK


> > > * Enable UPA


> * cloud captive web portal

> > 
> > * It consists Social Login CWP, Cloud Pin CWP


* Based on passed cwp-profile dict create the cwp for open network


* Assumes that already navigated to the wireless network page


* Keyword Usage:

> 
> * `Create Open Network Captive Web Portal    &{CWP_PROFILE}`


> * For &{CWP_PROFILE} creation refer social_login_config.robot, cloud_pin_config.robot


* **Parameters**

    **cwp_profile** – (dict) configuration profile dictionary



* **Returns**

    1 if created else -1



#### create_ppsk_wireless_network_cwp(\*\*cwp_config)

* Create captive web portal for  PPSK wireless network


* This is called as part of PPSK wireless network creation


* For standalone call assumes that already navigated to the wireless network page, selected the PPSK auth type


* Keyword Usage:

> 
> * `Create PPSK Wireless Network CWP    &{CWP_CONFIG}`


* **Parameters**

    **cwp_config** – (dict) configuration



* **Returns**

    1 if created else -1



#### create_psk_wireless_network_cwp(\*\*cwp_config)

* Create captive web portal for  psk wireless network


* This is called as part of psk wireless network creation


* For standalone call assumes that already navigated to the wireless network page, selected the psk auth type


* Keyword Usage:

> 
> * `Create Psk Wireless Network CWP    &{CWP_CONFIG}`


* **Parameters**

    **cwp_config** – (dict) configuration



* **Returns**

    1 if created else -1



#### edit_cloud_pin_cwp(\*\*edit_config)

* Assuming that navigated up to cloud pin cwp dialog window


* It is used to edit the already existed CWP


* Keyword Usage:

> 
> * `\`Edit Cloud Pin CWP    ${EDIT_CONFIG}`


* **Parameters**

    **edit_config** – (dict) edit configuration parameters



* **Returns**

    1 if success else -1



#### _property_ perform_cwp_save()
Save the captive web portal and handle the error msgs in any field


* **Returns**

    1 if created else -1


## extauto.xiq.flows.configure.WirelessNetworks module


### _class_ extauto.xiq.flows.configure.WirelessNetworks.WirelessNetworks()
Bases: `object`


#### create_wireless_network(\*\*wireless_network_conf)

* Create Standard or Guest wireless network based on network type


* create open, PPSK, PSK, enterprise networks based authentication types


* Assumption is already navigated to the network policy tab


* Keyword Usage:

> 
> * `Create Wireless Network   &{WIRELESS_NETWORK_CONFIG}`


> * For creation of different config dict refer wireless_networks_config.robot, private_pre_shared_key_config.robot


> * guest_access_config.robot, wpa_personal_config.robot, social_login_config.robot, cloud_pin_config.robot


* **Parameters**

    **wireless_network_conf** – configuration parameter dictionary



* **Returns**

    1 if successfully created else -1



#### navigate_to_standard_enterprise_network()

* Navigate to Standard Enterprise Wireless Network after Network Policy Edit


* **Returns**

    True if success


## Module contents
