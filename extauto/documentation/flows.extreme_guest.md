# extauto.xiq.flows.extreme_guest package

## Submodules

## extauto.xiq.flows.extreme_guest.AnalyzeClients module


### _class_ extauto.xiq.flows.extreme_guest.AnalyzeClients.AnalyzeClients()
Bases: `object`


#### check_if_the_client_exists(mac, location)
-This keyword Will Check if the mac address is present in the Extreme Guest Analyze Clients Page
- Keyword Usage:

> ‘’Check If The Client Exists        ${AP_MAC}        ${LOCATION_TREE}’’


* **Returns**

    1 if success



#### go_to_analyze_clients_page()
-This keyword Will Navigate to Extreme Guest Analyze Clients Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Analyze–> Clients
- Keyword Usage:

> ‘’Go to Analyze Clients Page’’


* **Returns**

    1 if success


## extauto.xiq.flows.extreme_guest.AnalyzeUsers module

## extauto.xiq.flows.extreme_guest.Dashboard module


### _class_ extauto.xiq.flows.extreme_guest.Dashboard.Dashboard()
Bases: `object`


#### check_dashboard_page_widgets()
-This keyword Will check if the newly created dashboard is displaying all the widgets
- Flow: dashboard–> automation_db1
- Keyword Usage:

> ‘’check dashboard page widgets’’


* **Returns**

    1 if navigation success



#### create_new_extreme_guest_dashboard(dashboard_name='automation_db1')
-This keyword Will Create a new dashboard with theme 15 and 9 widgets
- Flow: dashboard–> create new
- Keyword Usage:

> ‘’create new extreme guest dashboard’’


* **Returns**

    1 if navigation success



#### go_to_extreme_guest_dashboard_page()
-This keyword Will Navigate to Extreme Guest Dashboard Page
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window– Monitor–> dashboard
- Keyword Usage:

> ‘’Go To Extreme Guest Dashboard Page’’


* **Returns**

    1 if navigation success


## extauto.xiq.flows.extreme_guest.ExtremeGuest module


### _class_ extauto.xiq.flows.extreme_guest.ExtremeGuest.ExtremeGuest()
Bases: `object`


#### apply_selected_open_ssid(search_string)
-This keyword Will select and apply an open SSID
- Flow: Flow: Extreme Guest–> Subscribe–> Page
- Keyword Usage:

> ‘’apply selected open ssid’’


* **Parameters**

    **search_string** – Open SSID name to be selected



* **Returns**

    1 if success



#### check_created_ssid_table(ssid_name=None)
-This keyword Will check for an open SSID name
- Flow: Flow: Extreme Guest–> Subscribe–> Page
- Keyword Usage:

> ‘’check_created_ssid_table’’


* **Parameters**

    **ssid_name** – Open SSID name to be searched



* **Returns**

    1 if success



#### check_guest_subscription()
-This keyword Will Navigate to Extreme Guest Subscription Page
- Flow: Extreme Guest–> Subscribe–> Page
- Keyword Usage:

> ‘’Check Guest Subscription’’


* **Returns**

    1 if guest is not subscribed



#### check_help_information()
-This keyword Will check if help information is available to create open SSID
- Flow: Extreme Guest–> Subscribe–> Page
- Keyword Usage:

> ‘’check help information’’


* **Returns**

    1 if success



#### go_back_to_xiq()
-This keyword Will Navigate back to XIQ Window
- Keyword Usage:

> ‘’Go Back To Xiq’’


* **Returns**

    1 if success



#### go_to_analyze_manage_reports_page()
-This keyword Will Navigate to Extreme Guest Analyze Reports Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Users
- Keyword Usage:

> ‘’Go To Analyze Manage Reports Page’’


* **Returns**

    1 if success



#### go_to_analyze_page()
-This keyword Will Navigate to Extreme Guest Configure Menu Window
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure
- Keyword Usage:

> ‘’Go To Analyze Page’’


* **Returns**

    1 if success



#### go_to_configure_page()
-This keyword Will Navigate to Extreme Guest Configure Menu Window
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure
- Keyword Usage:

> ‘’Go To Configure Page’’


* **Returns**

    1 if success



#### go_to_configure_users_page()
-This keyword Will Navigate to Extreme Guest Configure Users Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Users
- Keyword Usage:

> ‘’Go To Configure Users Page’’


* **Returns**

    1 if success



#### go_to_extreme_guest_landing_page()
-This keyword Will Navigate to Extreme Guest Window
- Flow: XIQ–> Extreme Guest
- Keyword Usage:

> ‘’Go To Extreme Guest Page’’


* **Returns**

    1 if navigation success



#### go_to_extreme_guest_monitor_dashboard_page()
-This keyword Will Navigate to Extreme Guest Menu Window
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window– Monitor–> dashboard
- Keyword Usage:

> ‘’Go To Extreme Guest Monitor Dashboard Page’’


* **Returns**

    1 if navigation success



#### go_to_extreme_guest_monitor_page()
-This keyword Will Navigate to Extreme Guest Menu Window
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window– Monitor
- Keyword Usage:

> ‘’Go To Extreme Guest Monitor Page’’


* **Returns**

    1 if navigation success



#### go_to_extreme_guest_page()
-This keyword Will Navigate to Extreme Guest Menu Window
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’Go To Extreme Guest Page’’


* **Returns**

    1 if navigation success



#### go_to_extreme_guest_subscribe_page()
-This keyword Will Navigate to Extreme Guest Subscription Page
- Flow: Extreme Guest–> Subscribe–> Page
- Keyword Usage:

> ‘’Go To Extreme Guest subscribe Page’’


* **Returns**

    1 if navigation success



#### send_wg_cmd_to_ap(ssid_name, \*cli_objs)

* This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor


* Keyword Usage:

> 
> * `Send Command To AP1     ${COMMAND}`


* **Parameters**

    
    * **ssid_name** – 


    * **cli_objs** – CLI command to be execute on AP1



* **Returns**

    CLI Command Output


## extauto.xiq.flows.extreme_guest.ExtremeGuestUsers module


### _class_ extauto.xiq.flows.extreme_guest.ExtremeGuestUsers.ExtremeGuestUsers()
Bases: `object`


#### create_bulk_vouchers(number_of_vouchers, access_group='', location_name='', print_users=False)

* This Keyword will create Bulk Vouchers in Eguest users Page


* Flow : Eguest Essentials –> More Insights –> Settings –> Users –> Add user–> Create Bulk users Vouchers


* Keyword Usage:

> 
> * `Create Bulk Vouchers  ${NO_OF_VOUCHERS}    access_group=${ACCESS_GROUP}    location_name=${LOCATION_TREE}`


* **Parameters**

    
    * **print_users** – 


    * **number_of_vouchers** – No. Of Vouchers Value


    * **access_group** – Access Group


    * **location_name** – Location tree in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1



* **Returns**

    1 if Users Bulk Vouchers Created Successfully



#### create_bulk_vouchers_client_login(number_of_vouchers, access_group='', location_name='')

* **Parameters**

    
    * **number_of_vouchers** – 


    * **access_group** – 


    * **location_name** – 



* **Returns**

    


#### create_guest_management_role_bulk_vouchers(number_of_vouchers, access_group='', location_name='', print_users=False)

* This Keyword will create Bulk Vouchers in Guest Mangement Users Page


* Flow : Guest Management Users –> Add user–> Create Bulk users Vouchers


* Keyword Usage:

> 
> * `Create Guest Management Role Bulk Vouchers  ${NO_OF_VOUCHERS}    access_group=${ACCESS_GROUP}    location_name=${LOCATION_TREE}`


* **Parameters**

    
    * **print_users** – 


    * **number_of_vouchers** – No. Of Vouchers Value


    * **access_group** – Access Group


    * **location_name** – Location tree in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1



* **Returns**

    1 if Users Bulk Vouchers Created Successfully



#### delete_user(search_string)

* **Parameters**

    **search_string** – 



* **Returns**

    


#### get_extreme_guest_users_count()
Getting the row count in Extreme Guest Users Page
- Keyword Usage:

> 
> * `Get Extreme Guest Users Count`


* **Parameters**

    **search_string** – 



* **Returns**

    User Count



#### get_username_from_vouchers(credentials)

* Get first username from the list of credentials


* Keyword Usage:

> 
> * `Get Username from vouchers   ${CREDENTIALS}`


#### select_location_for_create_bulk_vouchers_page(sel_loc)

* This keyword selects a location in the Eguest Users –> Create Bulk users Vouchers Page


* It is assumed that location is already created


* Flow : Eguest Essentials –> More Insights –> Settings –> Users –> Add user–> Create Bulk users Vouchers


* Keyword Usage:

> 
> * `Select Location For Create Bulk Vouchers Page ${LOCATION}`


* **Parameters**

    **sel_loc** – location to select, in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1



* **Returns**

    1 if location is selected, else -1’


## extauto.xiq.flows.extreme_guest.Landing module


### _class_ extauto.xiq.flows.extreme_guest.Landing.Landing()
Bases: `object`


#### check_all_landing_page_widgets()
-This keyword Will Navigate to Extreme Guest Page and check all widgets
- Flow: XIQ–> Extreme Guest
- Keyword Usage:

> ‘’check all landing page widgets’’


* **Returns**

    1 if all widgets are displayed



* **Returns**

    


#### check_map_location_widget()
-This keyword Will Navigate to Extreme Guest Page and check map widget marker
- Flow: XIQ–> Extreme Guest
- Keyword Usage:

> ‘’Check Map Location Widget’’


* **Returns**

    1 if widget is displayed


## extauto.xiq.flows.extreme_guest.MuGuestPortal module


### _class_ extauto.xiq.flows.extreme_guest.MuGuestPortal.MuGuestPortal()
Bases: `MuGuestPortalWebElements`


#### check_approval_success_text(driver)

* Check the Approval Success Text


* Keyword Usage:

> 
> * `Check Approval Success Text`


* **Returns**

    success text



#### check_if_sponsor_mobile_is_displayed()

* Check if the sponsor mobile field is present in Sponsor Form


* Keyword Usage:

> 
> * `Check If Sponsor Mobile Is Displayed`


* **Returns**

    1 if sponsor field is not present else -1



#### register_device_for_guest_access(visitor_name, visitor_email)

* Register Device via Device registration CWP


* Register Device with Captive Web Portal Device Registration Form


* Keyword Usage:

> 
> * `Register Device for Guest Access  ${VISITOR_NAME}   ${VISITOR_EMAIL}`


* **Parameters**

    
    * **visitor_name** – Visitor Name


    * **visitor_email** – Visitor Email



* **Returns**

    1 if successfully registered else -1



#### register_device_with_email_for_guest_access(visitor_email)

* Register Device with email to receive offers


* Register Device with Captive Web Portal Email Access Form


* Keyword Usage:

> 
> * `Register Device with Email for Guest Access  ${VISITOR_EMAIL}`


* **Parameters**

    **email** – Visitor Email



* **Returns**

    1 if successfully registered else -1



#### register_sponsored_guest_user(visitor_name, visitor_email, visitor_mobile, sponsor_name, sponsor_email, access_purpose)

* Register network via Sponsor Action CWP


* Register User with Captive Web Portal Sponsor Form


* Keyword Usage:

> 
> * `Register Sponsor Guest User  ${VISITOR_NAME}   ${VISITOR_EMAIL} ${VISITOR_MOBILE}  ${SPONSOR_NAME}     ${SPONSOR_EMAIL}     ${ACCESS_PURPOSE}`


* **Parameters**

    
    * **visitor_name** – Visitor Name


    * **visitor_email** – Visitor Email


    * **visitor_mobile** – Visitor Mobile


    * **sponsor_name** – Sponsor Name


    * **sponsor_email** – Sponsor Email


    * **access_purpose** – Access Purpose



* **Returns**

    1 if successfully registered else -1



#### validate_eguest_default_template_with_no_mapping()

* Register network via google login CWP


* Validate Captive Web Portal social login with facebook credentials


* Keyword Usage:

> 
> * `validate eguest default template with no mapping`


* **Returns**

    1 if successfully connected with internet with social login type facebook else -1



#### validate_eguest_social_login_with_facebook(username, password)

* Register network via facebook login CWP


* Validate Captive Web Portal social login with facebook credentials


* Keyword Usage:

> 
> * `Validate EGuest Social Login With Facebook  ${FACEBOOK_USERNAME}   ${FACEBOOK_PASSWORD}`


* **Parameters**

    
    * **username** – Facebook Username


    * **password** – Facebook Password



* **Returns**

    1 if successfully connected with internet with social login type facebook else -1



#### validate_eguest_social_login_with_google(username, password)

* Register network via google login CWP


* Validate Captive Web Portal social login with facebook credentials


* Keyword Usage:

> 
> * `Validate EGuest Social Login With Google  ${GOOGLE_USERNAME}   ${GOOGLE_PASSWORD}`


* **Parameters**

    
    * **username** – Google username


    * **password** – Google password



* **Returns**

    1 if successfully connected with internet with social login type facebook else -1



#### validate_eguest_social_login_with_linkedin(username, password)

* Register network via Linkedin login CWP


* Validate Captive Web Portal social login with Linkedin credentials


* Keyword Usage:

> 
> * `Validate EGuest Social Login With Linkedin  ${Linkedin_USERNAME}   ${Linkedin_PASSWORD}`


* **Parameters**

    
    * **username** – Linkedin Username


    * **password** – Linkedin Password



* **Returns**

    1 if successfully connected with internet with social login type Linkedin else -1



#### validate_eguest_user_login_with_voucher_credentials(credentials)

* Register network via google login CWP


* Validate Captive Web Portal social login with facebook credentials


* Keyword Usage:

> 
> * `validate eguest user login with voucher credentials   ${CREDENTIALS}`


* **Parameters**

    **credentials** – Voucher credential dictionary



* **Returns**

    1 if successfully connected with internet with social login type facebook else -1



#### validate_sponsored_guest_access(email, password, onboarding_action, login_email='null')

* Validate the Sponsor Action on the Guest Access


* Validate User with Captive Web Portal Sponsor Form Login


* Keyword Usage:

> 
> * `Validate Sponsored Guest Access  ${USER_EMAL}   ${USER_PASSWORD} ${ONBOARDING_ACTION}  ${LOGIN_EMAIL}`


* **Parameters**

    
    * **email** – email to retrieve passcode


    * **password** – email password


    * **onboarding_action** – onboarding action to determine sponsor or user and passcode length


    * **login_email** – Sponsor Name



* **Returns**

    1 if successfully registered else -1


## extauto.xiq.flows.extreme_guest.Notification module


### _class_ extauto.xiq.flows.extreme_guest.Notification.Notification()
Bases: `object`


#### add_notification_policy(policy_name, policy_description, policy_type='user', sms='False', sponsor_number='', email='True')
-This keyword Will Navigate to Extreme Guest Notification Policy Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Notification > Policy
- Keyword Usage:

> ‘’Add Notification Policy   ${POLICY_NAME0}  ${POLICY_NAME0}     ${POLICY_TYPE0}     ${POLICY_SMS0}  ${POLICY_SPONSOR_NUMBER0}   ${POLICY_EMAIL0}’’


* **Parameters**

    
    * **policy_name** – Name of the Notification Policy


    * **policy_description** – Notification Policy Description


:param policy_type:Notification Policy Type - ‘user’ or ‘sponsor’
:param sms: Enable SMS for Notification Policy
:param sponsor_number: Sponsor Phone Numbers for the Sponsor Notification Polcy
:param email: Enable Email for Notification Policy
:return: 1 if success


#### check_if_notification_policy_exists(policy_name)
-This keyword Will Check if the Notification Policy Exists
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Notification > Policy
- Keyword Usage:

> ‘’Check If Notification Policy Exists   ${POLICY_NAME}’’


* **Parameters**

    **policy_name** – 



* **Returns**

    


#### delete_notification_policy(policy_name)
-This keyword Will Check if the Notification Policy Exists
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Notification > Policy
- Keyword Usage:

> ‘’Delete Notification Policy   ${POLICY_NAME}’’


* **Parameters**

    **policy_name** – 



* **Returns**

    


#### edit_notification_policy(policy_name, policy_description='null', policy_type='null', sms='null', sponsor_number='null', email='null')
-This keyword Will Navigate to Extreme Guest Notification Policy Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Notification > Policy
- Keyword Usage:

> ‘’Edit Notification Policy   ${POLICY_NAME0}  ${POLICY_NAME0}     ${POLICY_TYPE0}     ${POLICY_SMS0}  ${POLICY_SPONSOR_NUMBER0}   ${POLICY_EMAIL0}’’


* **Parameters**

    
    * **policy_name** – Name of the Notification Policy


    * **policy_description** – Notification Policy Description


:param policy_type:Notification Policy Type - ‘user’ or ‘sponsor’
:param sms: Enable SMS for Notification Policy
:param sponsor_number: Sponsor Phone Numbers for the Sponsor Notification Polcy
:param email: Enable Email for Notification Policy
:return: 1 if success


#### format_notification_policy_row(row)

#### get_notification_policy(policy_name)
-This keyword Will Check if the Notification Policy Exists
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Notification > Policy
- Keyword Usage:

> ‘’Get Notification Policy   ${POLICY_NAME}’’


* **Parameters**

    **policy_name** – 



* **Returns**

    


#### go_to_configure_notification_policy_tab()
-This keyword Will Navigate to Extreme Guest Notification Policy Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Notification > Policy
- Keyword Usage:

> ‘’Go To Configure Notification Policy Tab’’


* **Returns**

    1 if success


## extauto.xiq.flows.extreme_guest.Onboarding module


### _class_ extauto.xiq.flows.extreme_guest.Onboarding.Onboarding()
Bases: `object`


#### add_onboarding_policy(policy_name=None, group_name=None, condition_type='Any', condition_value='Any', action_type='Register Client', user_notifpolicy='UserNotificationPolicy', sponsor_notifpolicy='SPApprovalNotificationPolicy')

* This keyword will navigate to onboarding policy page and add policy


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Onboarding > Policy

    > Add Policy


* Keyword Usage:

    ‘’Add Onboarding Policy ${POLICY_NAME} ${GROUP_NAME} ${CONDITION_TYPE} ${CONDITION_VALUE}  ${ACTION_TYPE}   ${USER_NOTIFICATION_POLICY}   ${SPONSOR_NOTIFICATION_POLICY}’’


* **Parameters**

    
    * **group_name** – name of the group to be added


    * **action_type** – action to be performed


    * **condition_type** – matching conditions


    * **policy_name** – Name of the onboarding policy to be created


    * **condition_value** – matching condition value


    * **user_notifpoliy** – user notification policy


    * **sponsor_notifpolicy** – sponsor notification policy



* **Returns**

    1 if success



#### add_onboarding_rule(rule_name=None, policy_name=None, network_name='All Networks', location_name=None)

* This keyword will navigate to onboarding rules page and add rule


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Onboarding > Rules

    > Add rules


* Keyword Usage:

    ‘’Add Onboarding Rule ${RULE_NAME} ${POLICY_NAME} ${NETWORK_NAME} ${LOCATION_NAME}’’


* **Parameters**

    
    * **rule_name** – Name of the rule to be created


    * **location_name** – Name of location to be selected, in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1


    * **network_name** – Name of network to be added


    * **policy_name** – Name of the onboarding policy to be assigned



* **Returns**

    1 if success



#### go_to_configure_onboarding_policy_tab()
-This keyword Will Navigate to Extreme Guest Onboarding Policy Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Onboarding > Policy
- Keyword Usage:

> ‘’Go To Configure Onboarding Policy Tab’’


* **Returns**

    1 if success



#### go_to_configure_onboarding_rules_tab()
-This keyword Will Navigate to Extreme Guest Onboarding Rules Page
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Onboarding > Rules
- Keyword Usage:

> ‘’Go To Configure Onboarding Rules Tab’’


* **Returns**

    1 if success



#### select_location_for_add_onboarding_rule_page(sel_loc)

* This keyword selects a location in the Eguest Add on boarding Rule Page


* It is assumed that location is already created


* Flow : Eguest Essentials –> More Insights –> Settings –> Onboarding –> Rules –> Add Rule –> Location


* Keyword Usage:

> 
> * `Select Location For Add Onboarding Rule Page ${LOCATION}`


* **Parameters**

    **sel_loc** – location to select, in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1



* **Returns**

    1 if location is selected, else -1’


## extauto.xiq.flows.extreme_guest.Reports module


### _class_ extauto.xiq.flows.extreme_guest.Reports.Reports()
Bases: `object`


#### create_extreme_guest_report(report_name, report_type, report_format, save_type='save', scope=None, period=None, dashboard_name=None)

* **Parameters**

    
    * **report_name** – 


    * **report_type** – 


    * **report_format** – 


    * **save_type** – 


    * **scope** – 


    * **period** – 


    * **dashboard_name** – 



* **Returns**

    


#### delete_extreme_guest_generated_report(report_name)

* **Parameters**

    **report_name** – 



* **Returns**

    


#### delete_extreme_guest_manage_report(report_name)

* **Parameters**

    **report_name** – 



* **Returns**

    


#### edit_extreme_guest_report(report_name, updated_name, report_type=None, report_format=None, save_type='save', scope=None, period=None, dashboard_name=None)

* **Parameters**

    
    * **updated_name** – 


    * **scope** – 


    * **report_name** – 


    * **report_type** – 


    * **period** – 


    * **dashboard_name** – 


    * **report_format** – 


    * **save_type** – 



* **Returns**

    


#### go_to_generated_reports_tab()

* **Returns**

    


#### go_to_manage_reports_tab()

* **Returns**

    


#### select_scope_for_add_manage_report_page(scope)

* This keyword selects a location in the Eguest Users –> Create Bulk users Vouchers Page


* It is assumed that location is already created


* Flow : Eguest Essentials –> More Insights –> Settings –> Users –> Add user–> Create Bulk users Vouchers


* Keyword Usage:

> 
> * `Select Location For Create Bulk Vouchers Page ${LOCATION}`


* **Parameters**

    **scope** – location to select, in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1



* **Returns**

    1 if location is selected, else -1’


## extauto.xiq.flows.extreme_guest.SplashTemplate module


### _class_ extauto.xiq.flows.extreme_guest.SplashTemplate.SplashTemplate()
Bases: `object`


#### apply_network_to_user_template(network_name=None, template_name=None, location=None)

* This keyword will Apply the Network and Location To User Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Apply Network To User Template    ${NETWORK_NAME} ${TEMPLATE_NAME}’’


* **Parameters**

    
    * **template_name** – Name of the user template to be selected


    * **network_name** – Name of the network to be selected


:param location : Location Tree in comma format  e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
:return: 1 if success


#### clone_accept_connect_template(template_name=None)

* This keyword will clone the accept and connect template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Accept Connect Template             ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_accept_connect_terms_template(template_name=None)

* This keyword will clone the Accept Connect with Terms Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Accept Connect Terms Template       ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_device_registration_with_social_wifi_template(template_name=None)

* This keyword will clone the Device Registration With Social Wifi Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Device Registration With Social Wifi Template       ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_email_access_template(template_name=None)

* This keyword will clone the Email Access Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Email Access Template       ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_social_wifi_with_all_template(template_name=None)

* This keyword will clone the Social Wifi With All Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Social Wifi With All Template       ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_social_wifi_with_facebook_and_googleplus_template(template_name=None)

* This keyword will clone the Social Wifi With Facebook And Googleplus Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Social Wifi With Facebook And Googleplus Template   ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_sponsored_guest_access_template(template_name=None)

* This keyword will clone the Sponsored Guest Access Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone Sponsored Guest Access Template             ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_user_reg_with_social_forgot_passcode_template(template_name=None)

* This keyword will clone the User Reg With Social Forgot Passcode Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone User Reg With Social Forgot Passcode Template       ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### clone_user_registration_with_social_wifi_template(template_name=None)

* This keyword will clone the User Registration With Social Wifi Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Clone User Registration With Social Wifi Template ${TEMPLATE_NAME}’’


* **Parameters**

    **template_name** – Name of the user template to be created



* **Returns**

    1 if success



#### go_to_configure_splash_system_template_tab()
-This keyword Will Navigate to Extreme Guest System Splash Template
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

> Splash Template–> System Template


* Keyword Usage:

    ‘’Go To Configure Splash System Template Tab’’


* **Returns**

    1 if success



#### go_to_configure_splash_template_tab()
-This keyword Will Navigate to Extreme Guest Splash Template
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–> Splash Template
- Keyword Usage:

> ‘’Go To Configure Splash Template Tab’’


* **Returns**

    1 if success



#### go_to_configure_splash_user_template_tab()
-This keyword Will Navigate to Extreme Guest User Splash Template
- Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

> Splash Template–> User Template


* Keyword Usage:

    ‘’Go To Configure Splash User Template Tab’’


* **Returns**

    1 if success



#### remove_network_from_user_template(template_name=None)

* This keyword will Apply the Network and Location To User Template


* Flow: Extreme Guest–> More Insights–> Extreme Guest Menu Window–> Configure–>

    Splash Template–> System Template–> Clone


* Keyword Usage:

    ‘’Remove Network From User Template ${TEMPLATE_NAME}’’


* **Parameters**

    
    * **template_name** – Name of the user template to be selected


    * **network_name** – Name of the network to be selected


:param location : Location Tree in comma format  e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
:return: 1 if success


#### select_location_for_apply_user_template_page(sel_loc)

* This keyword selects a location in apply user template page


* It is assumed that location is already created


* Flow : Eguest Essentials –> More Insights –> Settings –>Splash Templates –>user Templates–>apply –> Location


* Keyword Usage:

> 
> * `Select Location For Apply User Template Page ${LOCATION}`


* **Parameters**

    **sel_loc** – location to select, in a comma-separated list format;
    e.g., Extreme Networks,Bangalore,Ecospace,Floor 1



* **Returns**

    1 if location is selected, else -1’


## extauto.xiq.flows.extreme_guest.Summary module


### _class_ extauto.xiq.flows.extreme_guest.Summary.Summary()
Bases: `object`


#### check_all_summary_page_widgets()
-This keyword Will Navigate to Extreme Guest Summary and check all widgets
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check all summary page widgets’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_conversion_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check conversion widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page conversion widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_facebook_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check facebook widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page facebook widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_gender_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check gender widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page gender widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_google_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check google widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page google widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_linkedin_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page linkedin widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_new_user_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check new user widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page new user widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_online_clients_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page total clients widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_online_users_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page online users widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_total_clients_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page total clients widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_total_users_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check linkedin widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page total users widget data’’


* **Returns**

    1 if all widgets are displayed



#### check_summary_page_visitor_widget_data()
-This keyword Will Navigate to Extreme Guest Summary and check visitor widget data
- Flow: Extreme Guest–> More Insights–>Extreme Guest Menu Window
- Keyword Usage:

> ‘’check summary page visitor widget data’’


* **Returns**

    1 if all widgets are displayed


## Module contents
