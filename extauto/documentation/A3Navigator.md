# A3Navigator module


### _class_ extauto.a3.flows.a3.A3Navigator.Navigator()
Bases: `NavigatorWebElements`


#### navigate_a3_inventory()

* This Keyword Navigate to A3 –> Inventory


* Flow: A3—>Inventory


* Keyword Usage
- `Navigate A3 Inventory`


* **Returns**

    1 if Navigation Successful to Inventory tab on A3 Menu



#### navigate_configure_common_objects()

* This keyword Navigates to Common Objects On Configure Menu


* Flow: Configure –> Common Objects


* Keyword Usage

> 
> * `Navigate Configure Common Objects`


* **Returns**

    -1 if Navigation Not Successful to Configure Menu else return None



#### navigate_configure_network_policies()
> 
> * This keyword Navigates to Network Policies On Configure Menu


> * Flow Configure–> Network Policies


> * Keyword Usage

> > 
> > * `Navigate Configure Network Policies`


* **Returns**

    1 if Navigation Successful to Network Policies On Configure Menu else return -1



#### navigate_manage_security()

* This Keyword Navigate to Manage –> Security


* Flow: Manage—>Security


* Keyword Usage
- `Navigate To Manage Security`


* **Returns**

    1 if Navigation Successful to Security tab on Monitor Menu else return -1



#### navigate_to_aaa_server_settings()

* This Keyword Navigate to AAA server Settings on common objects


* Flow: Configure –> Common Object –> Authentication –> AAA Server Settings


* Keyword Usage

> 
> * `Navigate To AAA Server Settings`


* **Returns**

    None



#### navigate_to_accounting_logs()

* This keyword Navigate to the Accounting Logs Slider Menu


* Flow: User account –> Global Settings –> LOGS–> Accounting Logs


* Keyword Usage

> 
> * `Navigate To Accounting Logs Menu`


* **Returns**

    1 if Navigation Successful to Accounting Logs Slider else return -1



#### navigate_to_accounting_logs_menu()

* This keyword Navigate to the Accounting Logs Slider Menu


* Flow: Accounting Logs


* Keyword Usage

> 
> * `Navigate To Accounting Logs Menu`


* **Returns**

    1 if Navigation Successful to Accounting Logs Slider



#### navigate_to_ad_servers()

* This Keyword Navigate to AD servers on common objects


* Flow: Configure –> Common Object –> Authentication –> Ad Servers


* Keyword Usage

> 
> * `Navigate To Ad Servers`


* **Returns**

    None



#### navigate_to_advance_channel_selection(device_serial='')

* This Keyword navigates to device advanced channel selection window


* Navigate to Manage –> Device


* Select the device row based on the passed device serial


* Click on Utilities –> Status –> Advanced Channel Selection


* Keyword Usage:

> 
> * `Navigate To Advance Channel Selection   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial number of the device



* **Returns**

    1



#### navigate_to_api_token_mngment()

* This keyword is used to navigate the “API Token Management”


* Flows XIQ User Menu(Account Info) –> Global Settings –> API Token Management


* Keyword Usage:

> 
> * `Navigate To Api Token Mngment`


* **Returns**

    None



#### navigate_to_authentication_logs()

* This keyword Navigate to the Authentication Logs Slider Menu


* Flow: User account –> Global Settings –> LOGS–> Authentication Logs


* Keyword Usage

> 
> * `Navigate To Authentication Logs Menu`


* **Returns**

    1 if Navigation Successful to Authentication Logs Slider Menu else return -1



#### navigate_to_authentication_logs_menu()

* This keyword Navigate to the Authentication Logs Slider Menu


* Flow: Authentication Logs


* Keyword Usage

> 
> * `Navigate To Authentication Logs Menu`


* **Returns**

    1 if Navigation Successful to Authentication Logs Slider Menu else return -1



#### navigate_to_auto_provision()
> 
> * This keyword Navigates to Auto Provisioning on Common Objects


> * Flow Configure –> Common Objects –> Policy –> Auto Provisioning


> * Keyword Usage

> > 
> > * `Navigate To Auto Provision`


* **Returns**

    None



#### navigate_to_basic_vlans_tab()

* This Keyword Navigate to Vlans Tabs On Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>BASIC–>VLAN’s


* Keyword Usage:

> 
> * `Navigate To Basic Vlans Tab`


* **Returns**

    None



#### navigate_to_captive_web_portal()

* This keyword Navigate to the captive web portal tab on common objects


* FLow: Configure –> Common Object –> Authentication –> Captive Web Portal


* Keyword Usage

> 
> * `Navigate To Captive Web Portal`


* **Returns**

    None



#### navigate_to_client360()

* This Keyword Navigate to Client360 on ML Insights Menu


* Flow: ML Insights –> Client 360


* Keyword Usage:

> 
> * `Navigate To Client360`


* **Returns**

    None



#### navigate_to_clients()

* This keyword Navigates to Clients On Monitor Menu


* Flow: Monitor –> Clients


* Keyword Usage

> 
> * `Navigate To Clients`


* **Returns**

    1 if Navigation Successful to Clients Tab on Monitor else return -1



* **Returns**

    -2 if Navigation Not Successful to Monitor Tab



#### navigate_to_clients_tab()
> 
> * This keyword Navigates to Clients Tab on Manage Menu


> * Keyword Usage

> > 
> > * `Navigate To Clients Tab`


* **Returns**

    1 if Navigation Successful to Clients On Monitor Menu else return -1



#### navigate_to_common_object_authentication_tab()

* This keyword Navigate to the Authentication Tab on common objects


* Assumes that already navigated to the configure –> common object


* Flow: Authentication


* Keyword Usage

> 
> * `Navigate To Common Object Authentication Tab`


* **Returns**

    None



#### navigate_to_common_object_basic_tab()

* This Keyword Navigate to Basic Tab On Common Objects


* Assumes that already navigated to the configure –> common object


* Flow: Basic


* Keyword Usage:

> 
> * `Navigate To Common Object Basic Tab`


* **Returns**

    None



#### navigate_to_common_object_network_tab()

* This Keyword Navigate to Network Tab On Common Objects


* Assumes that already navigated to the configure –> common object


* Flow: Networks


* Keyword Usage:
- `Navigate To Common Object Network Tab`


* **Returns**

    None



#### navigate_to_common_object_policy_tab()

* This Keyword Navigate to Policies option Menu on Common Objects


* Assumes that already navigated to the configure –> common object


* Keyword Usage:

> 
> * `Navigate To Common Object Policy Tab`


* **Returns**

    None



#### navigate_to_common_object_security_tab()

* This Keyword Navigate to Security Tab on Common Objects


* Assumes that already navigated to the configure –> common object


* Flow: Security


* Keyword Usage

> 
> * `Navigate To Common Object Security Tab`


* **Returns**

    1 if Navigation Successful to Security tab on common Objects else return -1



* **Returns**

    


#### navigate_to_common_object_user_profile()

* **Returns**

    


#### navigate_to_configuration_tab()
> 
> * This keyword Navigates to Configuration Tab


> * Keyword Usage

> > 
> > * `Navigate To Configuration Tab`


* **Returns**

    1 if Navigation Successful to Configuration Tab else return -1



#### navigate_to_configure_tab()
> 
> * This keyword Navigates to configure tab


> * Keyword Usage

> > 
> > * `Navigate To Configure tab`


* **Returns**

    1 if Navigation Successful to configure tab else return -1



#### navigate_to_configure_user_groups()

* This keyword Navigates to User Groups On Configure Menu


* Flow: Configure –> Users –> User Management –> User Groups


* Keyword Usage

> 
> * `Navigate To Configure User Groups`


* **Returns**

    None



#### navigate_to_configure_user_sub_tab()

* This keyword Navigates to Global Settings on User Account Menu which is already Navigated


* Keyword Usage

> 
> * `Navigate To Configure User Sub Tab`


* **Returns**

    1 if Navigation Successful to Global Settings on User Account Menu else return -1



#### navigate_to_device360_page_with_host_name(device_host)

* This keyword is used to navigate to the device360 window


* FLow: Manage –> Device –> Click on either device host name hyper link


* Keyword Usage:

> 
> * `Navigate To Device360 With MAC   ${DEVICE_MAC}`


* **Parameters**

    **device_host** – device MAC number



* **Returns**

    1 if navigated else -1



#### navigate_to_device360_page_with_mac(device_mac)

* This keyword is used to navigate to the device360 window


* FLow: Manage –> Device –> Click on either device MAC hyper link


* Keyword Usage:

> 
> * `Navigate To Device360 With MAC   ${DEVICE_MAC}`


* **Parameters**

    **device_mac** – device MAC number



* **Returns**

    1 if navigated else -1



#### navigate_to_device360_with_client(device_serial='')

* This keyword is used to navigate to the device360 window


* FLow: Manage –> Device –> searches for the row with passed device serial and clicks on client hyperlink.


* Keyword Usage:

> 
> * `Navigate To Device360 With Client   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if navigated else -1



#### navigate_to_device_cli_access(device_serials='')

* This keyword is used to navigate to single/multiple device cli access window


* Flow:

> 
> * Navigate to Manage –> Device


> * Select the device/devices row based on the passed device serials


> * Click on Action –> Advanced –> CLI Access


* Keyword Usage:

> 
> * `Navigate To Device Cli Access    ${DEVICE1_SERIAL}`


> * `Navigate To Device Cli Access    device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}`


* **Parameters**

    **device_serials** – comma separated device serial numbers



* **Returns**

    


#### navigate_to_devices(\*\*kwargs)
> 
> * This keyword Navigates to Devices on Manage Menu


> * Flow Manage–> Devices


> * Keyword Usage

> > 
> > * `Navigate To Devices`


* **Returns**

    1 if Navigation Successful to Devices Sub tab on Monitor Tab else return -1



#### navigate_to_external_radius_server()

* This Keyword Navigate to External Radius Server on common objects


* Flow: Configure –> Common Object –> Authentication –> External Radius Server


* Keyword Usage

> 
> * `Navigate To External Radius Server`


* **Returns**

    None



#### navigate_to_extreme_airdefence()

* This Keyword Navigate to Extreme AirDefence Menu


* Flow: Extreme AirDefence


* Keyword Usage
- `Navigate To Extreme AirDefence`


* **Returns**

    1 if Navigation Successful to Extreme AirDefence Menu



#### navigate_to_extreme_networks_a3()

* This Keyword Navigate to Extreme Networks A3 on common objects


* Flow: Configure –> Common Object –> Authentication –> Extreme Networks A3


* Keyword Usage

> 
> * `Navigate To Extreme Networks A3`


* **Returns**

    None



#### navigate_to_global_settings_page()

* This keyword Navigates to Global Settings On User Account Menu


* Flow: User Account Menu –> Global Settings


* Keyword Usage

> 
> * `Navigate To Clients`


* **Returns**

    1 if Navigation Successful to Clients Tab on Monitor else return -1



* **Returns**

    -2 if Navigation Not Successful to Monitor Tab



#### navigate_to_ldap_servers()

* This Keyword Navigate to LDAP Servers on common objects


* Flow: Configure –> Common Object –> Authentication –> LDAP Servers


* Keyword Usage

> 
> * `Navigate To Ldap Servers`


* **Returns**

    None



#### navigate_to_manage_alarms()

* This Keyword Navigate to Alarms on manage Menu


* Flow: Manage –> Alarms


* Keyword Usage:

> 
> * \`\` Navigate To Manage Alarms\`\`


* **Returns**

    None



#### navigate_to_manage_reports()

* This Keyword Navigate to Reports on Manage Menu


* Flow: Manage –> Reports


* Keyword Usage:

> 
> * `Navigate To Manage Reports`


* **Returns**

    None



#### navigate_to_manage_tab()
> 
> * This keyword Navigates to Manage Tab


> * Keyword Usage

> > 
> > * `Navigate To Manage Tab`


* **Returns**

    1 if Navigation Successful to Monitor Tab else return -1



#### navigate_to_ml_insight_tab()
> 
> * This keyword Navigates to ML Insight tab


> * Keyword Usage

> > 
> > * `Navigate To ML Insight tab`


* **Returns**

    1 if Navigation Successful to ML Insight tab else return -1



#### navigate_to_multiple_device_configuration_page(device_serials='')

* Flow: Manage –> Device –> Select Multiple Device –> Click on Edit button


* This keyword is navigate to the devices configuration page


* Keyword Usage:

> 
> * Navigate To Multiple Device Configuration Page    device_serials=${DEVICE1_SER},${DEVICE2_SER}\`\`


* **Parameters**

    **device_serials** – device serial number with comma separated



* **Returns**

    1



#### navigate_to_network360monitor()

* This Keyword Navigate to network360monitor on ML Insights Menu


* Flow: ML Insights –> Network360Monitor


* Keyword Usage:

> 
> * `Navigate To Network360Monitor`


* **Returns**

    None



#### navigate_to_network360plan()

* This Keyword Navigate to network360plan on ML Insights Menu


* Flow: ML Insights –> Network360Plan


* Keyword Usage:

> 
> * `Navigate To Network360Plan`


* **Returns**

    None



#### navigate_to_network_policies_card_view_page()

* This Keyword navigate to the policies card view page


* Flow: Configure –> Network Policies –> Card View Tab


* Keyword Usage:

> 
> * `Navigate To Network Policies Card View Page`


* **Returns**

    1



#### navigate_to_network_policies_list_view_page()

* This keyword Navigate to policies list view page


* Flow: Configure –> Network Policies –> List View Tab


* Keyword Usage:

> 
> * `Navigate To Network Policies List View Page`


* **Returns**

    1



#### navigate_to_network_policies_tab()
> 
> * This keyword Navigates to Network Policies


> * Keyword Usage

> > 
> > * `Navigate To Network Policies Tab`


* **Returns**

    1 if Navigation Successful to Network Policies On Configure Menu else return -1



#### navigate_to_network_subnetwork_space()

* This Keyword Navigate to SubNetwork Space Tab On Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>NETWORK–>Subnetwork Space


* Keyword Usage:

> 
> * `Navigate To Network Subnetwork Space`


* **Returns**

    None



#### navigate_to_onboard_tab()
> 
> * This keyword Navigates to Onboard Tab


> * Keyword Usage

> > 
> > * `Navigate To onboard Tab`


* **Returns**

    1 if Navigation Successful to onboard Tab else return -1



#### navigate_to_policy_ap_template()

* This Keyword Navigate to AP Templates on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>AP Templates


* Keyword Usage:

> 
> * `Navigate To Policy Ap Template`


* **Returns**

    None



#### navigate_to_policy_port_types()

* This Keyword Navigate to Port Types On Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>POLICIES–>PORT TYPES


* Keyword Usage:

> 
> * `Navigate To Policy Port Types`


* **Returns**

    None



#### navigate_to_security_option()

* This Keyword Navigate to the Security option on Monitor Tab


* Flow: Security


* Keyword Usage

> 
> * `Navigate To Security Option`


* **Returns**

    1 if Navigation Successful to Security tab on Monitor Menu else return -1



#### navigate_to_security_wips_policies()

* This Keyword Navigate to WIPS Policies on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>SECURITY–>WIPS POLICIES


* Keyword Usage:

> 
> * `Navigate To Security Wips Policies`


* **Returns**

    None



#### navigate_to_servers()

* This Keyword Navigate to Servers on common objects


* Flow: Configure –> Common Object –> Authentication –> Servers


* Keyword Usage

> 
> * `Navigate To Servers`


* **Returns**

    None



#### navigate_to_ssids()

* This keyword Navigates to SSIDs Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> SSIDs


* Keyword Usage

> 
> * `Navigate To SSIDs`


* **Returns**

    None



#### navigate_to_status_interface(device_serial='')

* This Keyword navigates to device Status Interface window


* Navigate to Manage –> Device


* Select the device row based on the passed device serial


* Click on Utilities –> Status –> Interface


* Keyword Usage:

> 
> * `Navigate To Status Interface    ${DEVICE1_SERIAL}`


* **Parameters**

    **device_serial** – serial number of the device



* **Returns**

    


#### navigate_to_switch_templates()

* This keyword Navigates to Switch Templates Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> Switch Templates


* Keyword Usage

> 
> * `Navigate To Switch Templates`


* **Returns**

    None



#### navigate_to_tools_page()

* This keyword Navigates to Tools Page on Monitor Menu


* Flow MANAGE->Tools


* Keyword Usage

> 
> * `Navigate To Tools Page`


* **Returns**

    1 if Navigation Successful to Tools Sub tab on Monitor Tab else return -1



#### navigate_to_tools_sub_tab()
> 
> * This keyword Navigates to Tools Sub tab on Monitor Tab


> * Keyword Usage

> > 
> > * `Navigate To Tools Sub Tab`


* **Returns**

    1 if Navigation Successful to Tools Sub tab on Monitor Tab else return -1



#### navigate_to_tools_tab()
> 
> * This keyword Navigates to Tools Tab


> * Keyword Usage

> > 
> > * `Navigate To Tools Tab`


* **Returns**

    1 if Navigation Successful to Tools Tab else return -1



#### navigate_to_user_account()

* This keyword Navigates to User Account Menu


* Keyword Usage

> 
> * `Navigate To User Account`


* **Returns**

    1 if Navigation Successful to User Account Menu else return -1



#### navigate_to_wifi_status_summary(device_serial='')

* This Keyword navigates to  device Status Interface window


* Navigate to Manage –> Device


* Select the device row based on the passed device serial


* Click on Utilities –> Status –> Wifi Status Summary


* Keyword Usage:

> 
> * `Navigate To Wifi Status Summary   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial number of the device



* **Returns**

    1



#### select_active_directory_domains()
> 
> * This keyword select the Active Directory Domains from the menu Policies and Access Control


> * Keyword Usage

> > 
> > * `Select Active Directory Domains`


* **Returns**

    1 if Navigation Successful to Roles else return -1



#### select_cloud_integration()
> 
> * This keyword select the Cloud Integration from the menu System Configuration


> * Keyword Usage

> > 
> > * `Select cloud integration`


* **Returns**

    1 if Navigation Successful to Cloud Integration else return -1



#### select_roles()
> 
> * This keyword select the Roles from the menu Policies and Access Control


> * Keyword Usage

> > 
> > * `Select roles`


* **Returns**

    1 if Navigation Successful to Roles else return -1



#### select_ssh()
> 
> * This keyword selects SSH option in Tools Page


> * Keyword Usage

> > 
> > * `Selects SSH option in Tools Page`


* **Returns**

    1 if Navigation Successful to SSH Option else return -1



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


* `SSH Page Inputs`


* **Returns**

    1 if Navigation Successful to SSH inputs else return -1



#### switch_policies_access_control()
> 
> * This keyword switches to Policies & Access Control


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
