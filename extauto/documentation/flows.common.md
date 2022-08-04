# extauto.xiq.flows.common package

## Submodules

## extauto.xiq.flows.common.DeviceCommon module


### _class_ extauto.xiq.flows.common.DeviceCommon.DeviceCommon()
Bases: `DeviceCommonElements`


#### check_select_all_devices_checkbox_status(device_serials='')

* This keyword is used to click on select all check box and validate devices are selected


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Check Select All Devices Checkbox Status   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}`


* **Parameters**

    **device_serials** – device serial numbers with comma separated



* **Returns**

    1 if all Devices Selected Successfully else -1



#### edit_device(device_serial)

* This keyword is used to select the single device and click on the edit but in Manage –> Device page


* Assumes that navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Edit Device   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – 



* **Returns**

    1 if device selected in grid and able to click edit button else -1



#### edit_devices(device_serials='')

* This keyword is used to select the multiple device and click on the edit but in Manage –> Device page


* Assumes that navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Edit Device   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}`


* **Parameters**

    **device_serials** – device serial numbers with comma separated



* **Returns**

    1 if Multiple devices selected in grid and able to click edit button else -1



#### get_devices_per_page()

* This keyword is used to obtain the number of devices that are displayed per page.


* Keyword Usage:
- `Get Devices Per Page`


* **Returns**

    the current Devices Per Page value, else -1



#### get_select_device_checkbox_status(device_serial)

* This keyword is used to select the single device row in Manage –> Device page


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Select Device Row   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial number of the device



* **Returns**

    1 if device row selected, -1 if device row not found in grid



#### go_to_device360_window(device_mac='', device_host='')

* Assume that navigated to the Manage –> Device


* This keyword click on device MAC or device host name hyper link based on the passed args


* Keyword Usage:

> 
> * `Go To Device360 Window   ${DEVICE_MAC}`


> * `Go To Device360 Window   ${DEVICE_HOST}`


* **Parameters**

    
    * **device_mac** – device MAC


    * **device_host** – Device host name



* **Returns**

    1 if device 360 page Opened Successfully else -1



#### goto_device360_with_client(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and clicks on client hyperlink.


* Keyword Usage:

> 
> * `Goto Device360 With Client   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if navigated to client page from manage devices grid else -1



#### goto_device360_with_hostname(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and clicks on host name hyperlink.


* Keyword Usage:

> 
> * `Goto Device360 With Hostname   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if navigated to D360 page from manage devices grid else -1



#### goto_device360_with_mac(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and clicks on MAC hyperlink.


* Keyword Usage:

> 
> * `Goto Device360 With Mac   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if navigated to D360 page from manage devices grid else -1



#### is_client_link_available(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and checks if client hyperlink is available


* Keyword Usage:

> 
> * `Is Client Link Available   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if available else -1



#### is_hostname_link_available(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and checks if host name hyperlink is available


* Keyword Usage:

> 
> * `Is Hostname Link Available   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if available else -1



#### is_location_link_available(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and checks if location hyperlink is available


* Keyword Usage:

> 
> * `Is Location Link Available   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if available else -1



#### is_mac_link_available(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and checks if mac hyperlink is available


* Keyword Usage:

> 
> * `Is Mac Link Available   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if available else -1



#### is_policy_link_available(device_serial=None)

* Assume that navigated to the Manage –> Device


* This keyword searches for the row with passed device serial and checks if network policy hyperlink is available


* Keyword Usage:

> 
> * `Is Policy Link Available   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – device serial number



* **Returns**

    1 if available else -1



#### select_device_row(device_serial='', device_mac='', device_name='')

* This keyword is used to select the single device row in Manage –> Device page


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Select Device Row   device_serial=${DEVICE_SERIAL}`


> * `Select Device Row   device_mac=${DEVICE_MAC}`


> * `Select Device Row   device_name=${DEVICE_NAME}`


* **Parameters**

    
    * **device_serial** – serial number of the device


    * **device_mac** – MAC Address of the device


    * **device_name** – name of the device



* **Returns**

    1 if device row selected, -1 if device row not found in grid



#### select_device_rows(device_serials='', device_macs='', device_names='')

* This keyword is used to select the multiple device row in Manage –> Device page


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Select Device Rows   device_serials=${DEVICE1_SERIAL},${DEVICE2_SERIAL}`


> * `Select Device Rows   device_macs=${DEVICE1_MAC},${DEVICE2_MAC}`


> * `Select Device Rows   device_names=${DEVICE1_NAME},${DEVICE2_NAME}`


* **Parameters**

    
    * **device_serials** – comma separated list of device serial numbers


    * **device_macs** – comma separated list of device MAC addresses


    * **device_names** – comma separated list of device names



* **Returns**

    1 if devices rows selected Successfully else -1



#### update_devices_per_page(device_count=10)

* This keyword is used to select the number of devices that are displayed on the page.


* Keyword Usage:
- `Update Devices Per Page  ${DEVICE_COUNT}`


* **Parameters**

    **device_count** – the number of devices displayed per page - 10, 20, 50, or 100



* **Returns**

    None


## extauto.xiq.flows.common.GlobalSearch module


### _class_ extauto.xiq.flows.common.GlobalSearch.GlobalSearch()
Bases: `object`


#### application_details(search_result)

* This Keyword uses to get application details Based on Search Results string


* Keyword Usage

> 
> * `Application Details  ${SEARCH_RESULT_STRING}`


* **Parameters**

    **search_result** – Expected Application Information String displaying on Search Result



* **Returns**

    Application Name And Category



#### get_ap_details(search_result)

* Get AP details ie AP Host Name ,Mac Address,IP address and Serial Number


* Flow : Click Global search Box–> Search String


* Keyword Usage

> 
> * `Get AP Details      ${SEARCH_RESULT_STRING}`


* **Parameters**

    **search_result** – Expected AP Information String displaying on Search Result



* **Returns**

    Host Name, AP serial number, AP MAC, AP IP



#### get_ap_name()

* This Keyword Gets AP name and if no AP is present then it onboards the AP and gets its name.


* Keyword Usage

> 
> * `Get Ap Name`


* **Returns**

    Access Point Name



#### get_ap_row()

* This Keyword Gets AP name in Row Text


* Assumes that Already Navigated to Manage–> Devices Page


* Keyword Usage

> 
> * `Get AP Row`


* **Returns**

    ap device presented row information



#### get_client_details(search_result)

* Get client details ie Client Name ,Mac Address and Client IP address


* Flow : Click Global search Box–> Search String


* Keyword Usage

> 
> * `Get Client Details      ${SEARCH_RESULT_STRING}`


* **Parameters**

    **search_result** – Expected Client Information String displaying on Search Result



* **Returns**

    Client name, client MAC, client IP



#### get_sim_ap()

* This Keyword Gets AP name in Row Text


* Keyword Usage

> 
> * `Get Sim AP`


* **Returns**

    Access Point Name



#### global_search(search_value, category, expect_result='')

* This Keyword searches given search string info in global search


* Flow : Click Global search Box–> Search String


* Keyword Usage

> 
> * `Global Search   ${AP_MAC}   ${AP_CATEGORY}   ${AP_NAME}`


* **Parameters**

    
    * **search_value** – Info to be searched ie AP Mac Address


    * **category** – Category of the information


    * **expect_result** – Expected Result



* **Returns**

    returns matched value when found or else returns -1



#### net_policy_details(search_result)

* Get Network Policy details ie Network Policy Name and SSID


* Flow : Click Global search Box–> Search String


* Keyword Usage

> 
> * `Net Policy Details      ${SEARCH_RESULT_STRING}`


* **Parameters**

    **search_result** – Expected Network Policy Information String displaying on Search Result



* **Returns**

    Network Policy name and SSID



#### sim_ap_name()

* This Keyword Uses to get AP name and if no AP is present then it onboards the AP and gets its name.


* Keyword Usage

> 
> * `Sim AP Name`


* **Returns**

    Access Point Name



#### view_all_organizations()

* This Keyword uses to view all the organizations Details in the Account


* Flow : View Organization –> Select All Organization


* Keyword Usage

> 
> * `View All Organizations`


* **Returns**

    1 if Viewing All organization Details Successfully


## extauto.xiq.flows.common.Login module


### _class_ extauto.xiq.flows.common.Login.Login()
Bases: `object`


#### check_if_xiq_user_exists(customer_name)
This function check if the XIQ user exists into portal page
:param customer_name:   the name of the customer under which the account was created
:return: returns 1 if the account user doesn’t exist; else -1


#### click_advanced_onboard_popup()
> This keyword just clicks the advanced Onboard popup sliding window that appears during the first login or after reset VIQ.
> - Keyword Usage:


* \` click advanced popup\`

    
    * **return**

        None



#### close_window(win_index)

* Closes the specified window


* **Param**

    win_index - Index of the window to close



* **Returns**

    None



#### create_new_user_portal(customer_name, admin_first_name, admin_last_name, admin_password, sw_connection_host)
Creates a fresh new user in portal
:param customer_name: the name of the customer, written as an email
:param admin_first_name: first name of the admin
:param admin_last_name: last name of the admin
:param admin_email: admin email, the email that is used to log in into xiq cloud
:param admin_password: the password chosen to log in into xiq cloud
:param sw_connection_host: the url of the RDC
:return: returns 1 if the account was created succesfully or -1 if otherwise


#### delete_user_portal(customer_name, check_delete_devices=- 1)
This function deletes the account created in portal
:param customer_name:   the name of the customer under which the account was created
:return: returns 1 if the account was deleted or -1 if otherwise


#### enable_exos_status_on_xiq(url)

* for Exos switch to appear in UI we need to load the provided url


* Keyword Usage:

> 
> * `Enable Exos Status On Xiq   ${URL}`


* **Parameters**

    **url** – url to load for enabling exos on cloud UI



* **Returns**

    1 if loaded the url successfully



#### forgot_password(_email, url='default')

* Get the link to set the forget password


* Keyword Usage:

> 
> * `Forget Password   ${EMAIL}`


* **Parameters**

    
    * **_email** – Email Address


    * **url** – Forget Password URL



* **Returns**

    1 if reset password message displayed on Page else -1



#### get_base_url_of_current_page()

* This Keyword is used to get the url of current loaded page


* Keyword Usage:

> 
> * `Get Base URL Of Current Page`


* **Returns**

    current page url



#### get_current_page_url()

* This Keyword returns URL of current page


* Keyword Usage:

> 
> * `Get Current Page URL`


* **Returns**

    current page url



#### get_data_center_name()

* Get XIQ Data Center Name


* **Returns**

    data_center_name



#### get_page_title()

* Get the title of the page


* Keyword Usage:

> 
> * `Get Page Title`


* **Returns**

    page title



#### get_portal_url(sw_connection_host)

* **Parameters**

    **sw_connection_host** – the url of the RDC



* **Returns**

    the url of portal page ; else -1



#### get_viq_id()

* This method is used to get the build id or owner id


* Keyword Usage:

> 
> * `Get Viq Owner Id`


* **Returns**

    viq id



#### get_window_index()

* Get the index of the window handle for this session


* Keyword Usage:

> 
> * `Get Window Index`


* **Returns**

    index of window handle



#### get_xiq_version()
> 
> * Get XIQ Build version details


* **Returns**

    xiq_version



#### link_xiq_to_extreme_portal(sfdc_user_type, sfdc_email, sfdc_pwd, shared_cuid=None)

#### load_web_page(url='default')

* Loads web page with the passed URL


* Keyword Usage:

> 
> * `Load Web Page    ${URL}`


* **Parameters**

    **url** – Proper URL



* **Returns**

    creates global driver object & returns



#### log_out_portal()
This function logs out from portal
:return: returns 1 if logging out was succesfull or -1 if otherwise


#### login_for_first_time()

* This keyword used to login for the first time user based on option provided in test case


* If option is not specified, default option of “30-days trial” is selected.


* Getting started with license is not supported through Automation as it depends on Gemalto license.


* Assumes that user already in login option selection page


* Keyword Usage:

> 
> * `Login For First Time`


* **Returns**

    1



#### login_user(username, password, capture_version=False, login_option='30-day-trial', url='default', incognito_mode='False', co_pilot_status=False, entitlement_key=False, salesforce_username=False, salesforce_password=False, saleforce_shared_cuid=False, quick=False, check_warning_msg=False, \*\*kwargs)

* Login to Xiq account with username and password


* By default url will load from the topology file


* keyword Usage:

> 
> * `Login User   ${USERNAME}   ${PASSWORD}`


> * `Login User   ${USERNAME}   ${PASSWORD}    capture_version=True`


> * `Login User   ${USERNAME}   ${PASSWORD}    co_pilot_status=True`


* **Parameters**

    
    * **username** – login account username


    * **password** – login account password


    * **capture_version** – true if want capture the xiq build version


    * **login_option** – login option to get started with any of options: 30-day-trial, License, Legacy Entitlement, Pilot License & Connect


    * **incognito_mode** – Enable/Disable incognito_mode


    * **co_pilot_status** – Enable Co-Pilot Status in XIQ Login Page


    * **url** – url to load


    * **entitlement_key** – Entitlement Key


    * **salesforce_username** – Salesforce Username


    * **salesforce_password** – Salesforce Password


    * **saleforce_shared_cuid** – Salesforce Shared CUID


    * **quick** – Quick login without more sleep time while loading url


    * **check_warning_msg** – Flag to Enable to Warning Messages validation during XIQ Login



* **Returns**

    1 if login successful else -1



#### logo_check_on_login_screen()

* Get the login logo and save it as screenshot


* **Returns**

    login logo



#### logout_user()

* Logout the current user


* Keyword Usage:

> 
> * `Logout User`


* **Returns**

    1 if logout success



#### quit_browser(_driver=None)

* Closes all the browser windows and ends the WebDriver session gracefully.


* if the driver object is passed, quits and returns


* Keyword Usage:

> 
> * `Quit Browser`

:param _driver
:return: 1 if success


#### refresh_page(refresh_delay=10)
This keyword refreshes the current page
:param refresh_delay: delay needed to reload the page
:return: None


#### reset_password(new_pwd)

* Assumes that reset password url browser is opened


* Reset the user account password


* Keyword Usage:

> 
> * \`\` Reset Password  ${NEW_PASSWORD}\`\`


* **Parameters**

    **new_pwd** – 



* **Returns**

    1 if able to Reset the Password Successfully



#### reset_password_for_new_customer(password, url='default')

* Reset password for xiq account with passed reset password url link


* Keyword Usage:

> 
> * `Reset Password For New Account  ${RESET_PASSWORD}   ${RESET_URL_LINK}`


* **Parameters**

    
    * **password** – password to reset


    * **url** – reset password url link



* **Returns**

    1



#### select_login_option(login_option, entitlement_key, salesforce_username=False, salesforce_password=False, saleforce_shared_cuid=False)

#### select_welcome_page_option(login_option, ekey, sfdc_user_type, sfdc_email, sfdc_pwd, shared_cuid)
> 
> * This keyword selects login option on welcome page as indicated by login_option


* **Returns**

    None



#### set_password(new_pwd)

* Assumes that set password url is already opened


* Set new password for the account


* Keyword Usage:

> 
> * `Set Password   ${NEW_PASSWORD}`


* **Parameters**

    **new_pwd** – New Password string to set



* **Returns**

    1 if Able to Set the Password Successfully for the Account else None



#### skip_if_account_90_days()

* This keyword detects a license of 90 days and clicks on the option of 90 days


* Keyword Usage:

> 
> * `skip_if_account_90_days`


* **Returns**

    None



#### start_video_record(record_sta_ip, test_name=None)

* This Keyword will Start Video Record on mentioned machine IP Address .


* **Parameters**

    
    * **record_sta_ip** – Station IP address to Start the Video Recordings


    * **test_name** – Test Name for Video Recordings



* **Returns**

    None



#### stop_video_record(record_sta_ip)

* This Keyword will Stop Video Record on mentioned machine IP Address .


* **Parameters**

    **record_sta_ip** – Station IP address to Stop the Video Recordings



* **Returns**

    None



#### switch_to_window(win_index)

* Switches to the specified window


* **Param**

    win_index - Index of the window to switch to



* **Returns**

    None



#### verify_upgrade_option_for_connect_user()

* This keyword checks if upgrade button is displayed and clicking on upgrade button

navigates connect user to license management UI
:return: None


#### welcome_page_login(username, password, login_option, ekey=None, sfdc_user_type=None, sfdc_email=None, sfdc_pwd=None, shared_cuid=None, capture_version=False, code='default', url='default', incognito_mode='False')

* Login Xiq account with username and password


* By default url will load from the topology file


* keyword Usage:

> 
> * `Login User   ${USERNAME}   ${PASSWORD}`


> * `Login User   ${USERNAME}   ${PASSWORD}    capture_version=True`


> * $login_type} : trial, connect, extremecloudiq license, legacy license


* **Parameters**

    
    * **username** – login account username


    * **password** – login account password


    * **login_type** – trial, connect, extremecloudiq license, legacy license


    * **capture_version** – true if want capture the xiq build version


    * **code** – 


    * **url** – url to load



* **Returns**

    1 if login successful else -1



#### xiq_get_child_window_list(win_index)

* Obtain the Child Window Index List


* Keyword Usage:
- `XIQ Get Child Window List`


* **Param**

    win_index - Index of the window to close



* **Returns**

    Return List containing the Child Window Indexes



#### xiq_quit_browser(_driver=None)

* Closes all the browser windows and ends the WebDriver session gracefully.


* if the driver object is passed, quits and returns


* Keyword Usage:

> 
> * `XIQ Quit Browser`


* **Parameters**

    **_driver** – specific driver to use; if not specified, default driver will be used



* **Returns**

    None


## extauto.xiq.flows.common.MuCaptivePortal module


### _class_ extauto.xiq.flows.common.MuCaptivePortal.MuCaptivePortal()
Bases: `MuCPWebElement`


#### accept_user_acceptance_page()

* Accept User Acceptance page to get network access


* Keyword Usage:

> 
> * `Accept User Acceptance Page`


* **Returns**

    1 If successfully Accept User page Acceptance to get network access else -1



#### cancel_user_acceptance_policy()

* Cancel User page Acceptance Policy for getting network access


* Keyword Usage:

> 
> * `Cancel User Acceptance Policy`


* **Returns**

    1 if cancel user acceptance Policy for getting network access else None



#### check_cwp_social_login_term_and_condition_page_text()

* Check Captive Web Portal social login term and condition page


* Keyword Usage:

> 
> * `check cwp social login term and condition page`


* **Returns**

    1 if successfully get the term and condition page text else -1



#### check_internet_connectivity(mu_ip, url='https://www.extremenetworks.com/')

* By loading url check the internet connectivity


* By default url is [https://www.extremenetworks.com/](https://www.extremenetworks.com/)


* Keyword Usage:

> 
> * `Check Internet Connectivity   ${MU_IP}`


> * `Check Internet Connectivity   ${MU_IP}   url=${URL}`


* **Parameters**

    
    * **mu_ip** – mu ip to load the url


    * **url** – url to load on the browser



* **Returns**

    url page title



#### check_social_login_page_title()

* Get the social login cwp page title


* Keyword Usage:

> 
> * `Check Social Login Page Title`


* **Returns**

    1 if social login page loaded else None



#### check_successful_page_title()

* Once social login successful it will redirect the url given while registration.


* Check the page title of the loaded url


* Keyword Usage:

> 
> * `Check Successful Page Title`


* **Returns**

    1 if successfully loaded else -1



#### config_cloud_pin_email_id(email)

* Enter the email id to get the cloud pin


* cloud pin will get the the entered email ID


* Keyword Usage:

> 
> * `Config Cloud Pin Email Id   ${EMAIL}`


* **Parameters**

    **email** – Email address



* **Returns**

    
    * 1 if “Success! Check your email for your new PIN”


    * else error message




#### enter_cloud_pin(pin)

* Enter the cloud pin to authenticate user


* Keyword Usage:

> 
> * `Enter Cloud Pin  ${CLOUD_PIN}`


* **Parameters**

    **pin** – clodu pin got from email



* **Returns**

    1 if Entered Cloud Pin Successfully else None



#### get_ppsk_passcode_user_registration()

* When user register with open network cwp and returning to aerohive ppsk network


* Get the pass code from user self registration page


* Keyword Usage:

> 
> * `Get PPSK Passcode User Registration`


* **Returns**

    if success ppsk pass code else -1



#### guest_user_self_registration(\*\*guest_user)

* Register the Guest User to access the network


* Keyword Usage:

> 
> * `Guest USer Self Registration   &{GUEST_USER}`


> * &{GUEST_USER}   user_name=${USER_NAME}   email=${EMAIL}  ccode=${CCODE}  ph_num=${PHONE_NUMB}
> …             visitor_email=${VISITOR_EMAIL}


* **Parameters**

    **guest_user** – guest user registration dictionary



* **Returns**

    1 if registration success else -1



#### login_guest_user(user_name, password)

* Login the the guest Access network using username and password


* Keyword Usage:

> 
> * `Login Guest User  ${USER_NAME}   ${PASSWORD}`


* **Parameters**

    
    * **user_name** – username to login to network


    * **password** – password to login the network



* **Returns**

    1 if Login success else -1



#### social_login_user_acceptance_page()

* Accept the user acceptance button with social login types to get access to the network


* Keyword Usage:

> 
> * `Social Login User Acceptance Page`


* **Returns**

    1 if user acceptance button clicked else None



#### user_self_registration(\*\*user_info)

* User Self Registration on captive web portal


* Keyword Usage:

> 
> * `User Self Registration   &{USER_INFO}`


> * &{USER_INFO}    first_name=${FIRST_NAME}   last_name=${LAST_NAME}  email=${USERS_CRED_EMAIL}
> …             ccode=${CCODE}   ph_num=${PHONE_NUMBER}    visitor_email=${VISITOR_EMAIL}


* **Parameters**

    **user_info** – user registration parameters ie First and Last Name, Email,Mobile number,visitor Email address



* **Returns**

    1 If registration success else -1



#### validate_cwp_social_login_with_facebook(username, password)

* Register network via facebook login CWP


* Validate Captive Web Portal social login with facebook credentials


* Keyword Usage:

> 
> * `Validate CWP Social Login With Facebook  ${FACEBOOK_USERNAME}   ${FACEBOOK_PASSWORD}`


* **Returns**

    1 if successfully connected with internet with social login type facebook else -1



#### validate_cwp_social_login_with_google_account(username, password)

* Register network via google login CWP


* Validate Captive Web Portal social login with google credentials


* Keyword Usage:

> 
> * `Validate CWP Social Login With Facebook  ${GMAIL_USERNAME}   ${GMAIL_PASSWORD}`


* **Returns**

    1 if successfully connected with internet with social login type google else -1



#### validate_cwp_social_login_with_linkedin_account(username, password)

* Register network via Linkdin login CWP


* Validate Captive Web Portal social login with linkdin credentials


* Keyword Usage:

> 
> * `Validate CWP Social Login With Facebook  ${LINKDIN_USERNAME}   ${LINKDIN_PASSWORD}`


* **Returns**

    1 if successfully connected with internet with social login type Linkedin else -1


## extauto.xiq.flows.common.Navigator module


### _class_ extauto.xiq.flows.common.Navigator.Navigator()
Bases: `NavigatorWebElements`


#### navigate_a3_inventory()

* This Keyword Navigate to A3 –> Inventory


* Flow: A3—>Inventory


* Keyword Usage
- `Navigate A3 Inventory`


* **Returns**

    1 if Navigation Successful to Inventory tab on A3 Menu else None



#### navigate_a3_reporting()

* This Keyword Navigate to A3 –> Reporting


* Flow: A3—>Reporting


* Keyword Usage
- `Navigate A3 Reporting`


* **Returns**

    1 if Navigation Successful to Reporting tab on A3 Menu else None



#### navigate_configure_alert()
> 
> * This keyword Navigates to Alert On Configure Menu


> * Flow Configure–> Alert


> * Keyword Usage

> > 
> > * `Navigate Configure Alert`


* **Returns**

    1 if Navigation Successful to Alert On Configure Menu else return -1



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



#### navigate_configure_users()

* Navigate To CONFIGURE—>USERS


* Flow: CONFIGURE—>USERS


* Keyword Usage:

> 
> * `Navigate Configure Users`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_manage_application()

* Navigate to the MANAGE->Application


* Flow: Manage –> application


* Keyword Usage:

> 
> * `Navigate Manage Application`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_manage_events()

* Navigate to the MANAGE->EVENTS


* Flow: Manage –> Events


* Keyword Usage:

> 
> * `Navigate Manage Events`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_manage_security()

* This Keyword Navigate to Manage –> Security


* Flow: Manage—>Security


* Keyword Usage
- `Navigate Manage Security`


* **Returns**

    1 if Navigation Successful to Security tab on Monitor Menu else return -1



#### navigate_to_a3_menu()

* This Keyword Navigate to A3 menu


* Keyword Usage

> 
> * `Navigate To A3 Menu`


* **Returns**

    1 if Navigation Successful



#### navigate_to_aaa_server_settings()

* This Keyword Navigate to AAA server Settings on common objects


* Flow: Configure –> Common Object –> Authentication –> AAA Server Settings


* Keyword Usage

> 
> * `Navigate To AAA Server Settings`


* **Returns**

    1 if Navigation Successful



#### navigate_to_account_details_page()

* Navigate to the USER ACCOUNT-> Global settings > Account Details


* Flow: USER ACCOUNT-> Global settings > Account Details


* Keyword Usage:

> 
> * `Navigate To Account Details Page`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_to_account_mgmt()

* Navigate to the USER ACCOUNT-> Global settings > Account Management


* Flow: USER ACCOUNT-> Global settings > Account Management


* Keyword Usage:

> 
> * `Navigate To Account Mgmt`


* **Returns**

    1 If Navigated successfully else -1



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



#### navigate_to_accounts_organization_page()

* Navigate to the USER ACCOUNT-> Global settings > Account –> Organization


* Flow: USER ACCOUNT-> Global settings > Account –> Organization


* Keyword Usage:

> 
> * `Navigate To Accounts Organization Page`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_to_ad_servers()

* This Keyword Navigate to AD servers on common objects


* Flow: Configure –> Common Object –> Authentication –> Ad Servers


* Keyword Usage

> 
> * `Navigate To Ad Servers`


* **Returns**

    1 if Navigation Successful



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

    1 if Navigation Successful



#### navigate_to_alert_tab()
> 
> * This keyword Navigates to Alert


> * Keyword Usage

> > 
> > * `Navigate To Alert Tab`


* **Returns**

    1 if Navigation Successful to Alert On Configure Menu else return -1



#### navigate_to_api_token_mngment()

* This keyword is used to navigate the “API Token Management”


* Flows XIQ User Menu(Account Info) –> Global Settings –> API Token Management


* Keyword Usage:

> 
> * `Navigate To Api Token Mngment`


* **Returns**

    1 if Navigation Successful



#### navigate_to_applications_tab()
”
- This Keyword Navigate to Applications Page
- Flow: Manage –> Applications
- Keyword Usage:

> 
> * ‘Navigate to Applications page’


* **Returns**

    1 if Navigation Successful



#### navigate_to_audit_logs_menu()

* This keyword Navigate to the Audit Logs Slider Menu


* Flow: Authentication Logs


* Keyword Usage

> 
> * `Navigate To Authentication Logs Menu`


* **Returns**

    1 if Navigation Successful to Authentication Logs Slider Menu else return -1



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

    1 if Navigation Successful



#### navigate_to_basic_vlans_tab()

* This Keyword Navigate to Vlans Tabs On Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>BASIC–>VLAN’s


* Keyword Usage:

> 
> * `Navigate To Basic Vlans Tab`


* **Returns**

    1 if Navigation Successful



#### navigate_to_captive_web_portal()

* This keyword Navigate to the captive web portal tab on common objects


* FLow: Configure –> Common Object –> Authentication –> Captive Web Portal


* Keyword Usage

> 
> * `Navigate To Captive Web Portal`


* **Returns**

    1 if Navigation Successful



#### navigate_to_classification_rule()

* This keyword Navigates to ClassificationRule Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> Classification Rule


* Keyword Usage

> 
> * `Navigate To Policy Classification Rule Submenu`


* **Returns**

    1 if Navigation Successful



#### navigate_to_client360()

* This Keyword Navigate to Client360 on ML Insights Menu


* Flow: ML Insights –> Client 360


* Keyword Usage:

> 
> * `Navigate To Client360`


* **Returns**

    1 if Navigation Successful



#### navigate_to_client_mode_profiles()

* This Keyword Navigate to Client Mode Profile on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>Basic–>Client Mode Profiles


* Keyword Usage:

> 
> * `Navigate To Client Mode Profiles`


* **Returns**

    1 if Navigation Successful



#### navigate_to_client_monitor_and_diagnosis_tab()
”
- This Keyword Navigate to Client Monitor and Diagnosis Page
- Flow: Manage –> Client Monitor & Diagnosis
- Keyword Usage:

> 
> * ‘Navigate To Client Monitor And Diagnosis Tab’


* **Returns**

    1 if Navigation Successful



#### navigate_to_clients()

* This keyword Navigates to Clients On Manage Menu


* Flow: Manage –> Client 360


* Keyword Usage

> 
> * `Navigate To Clients`


* **Returns**

    1 if Navigation Successful to Clients Tab on Monitor else return -1



* **Returns**

    -2 if Navigation Not Successful to Monitor Tab



#### navigate_to_clients_tab()
> 
> * This keyword Navigates to Client 360 Tab on Manage Menu


> * Keyword Usage

> > 
> > * `Navigate To Clients Tab`


* **Returns**

    1 if Navigation Successful to Clients On Manage Menu else return -1



#### navigate_to_cloud_config_groups()

* This keyword Navigates to CCGs Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> Cloud Config Groups


* Keyword Usage

> 
> * `Navigate To Policy Cloud Config Group Submenu`


* **Returns**

    1 if Navigation Successful



#### navigate_to_common_object_authentication_tab()

* This keyword Navigate to the Authentication Tab on common objects


* Assumes that already navigated to the configure –> common object


* Flow: Authentication


* Keyword Usage

> 
> * `Navigate To Common Object Authentication Tab`


* **Returns**

    1 if Navigation Successful



#### navigate_to_common_object_basic_tab()

* This Keyword Navigate to Basic Tab On Common Objects


* Assumes that already navigated to the configure –> common object


* Flow: Basic


* Keyword Usage:

> 
> * `Navigate To Common Object Basic Tab`


* **Returns**

    1 if Navigation Successful



#### navigate_to_common_object_network_tab()

* This Keyword Navigate to Network Tab On Common Objects


* Assumes that already navigated to the configure –> common object


* Flow: Networks


* Keyword Usage:
- `Navigate To Common Object Network Tab`


* **Returns**

    1 if Navigation Successful



#### navigate_to_common_object_policy_tab()

* This Keyword Navigate to Policies option Menu on Common Objects


* Assumes that already navigated to the configure –> common object


* Keyword Usage:

> 
> * `Navigate To Common Object Policy Tab`


* **Returns**

    1 if Navigation Successful



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

    


#### navigate_to_common_objects_management_options()

* This Keyword Navigate to Management Options on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>NETWORK–>MANAGEMENT OPTIONS


* Keyword Usage:

> 
> * `Navigate To Common Objects Management Options`


* **Returns**

    1 if Navigation Successful



#### navigate_to_communications_page()

* This Keyword Navigate to communications menu in Global settings page


* Keyword Usage
- `Navigate To Communications Page`


* **Returns**

    1 if Navigation Successful to Communications



#### navigate_to_configure_guest_essentials_users()
> 
> * This keyword Navigates to Guest Essentials Users on Configure Menu


> * Flow Configure–> Guest Essentials Users


> * Keyword Usage

> > 
> > * `Navigate To Configure Guest Essentials Users`


* **Returns**

    1 if Navigation Successful to Guest Essentials Users Sub tab on Configure Tab else return -1



#### navigate_to_configure_ppsk_classification()

* This keyword Navigates to PPSK Classification On Configure Menu


* Flow: Configure –> Users –> User Management –> PPSK Classification


* Keyword Usage

> 
> * `Navigate To Configure User Management PPSK Classification Submenu`


* **Returns**

    1 if Navigation Successful



#### navigate_to_configure_private_client_group()

* This keyword Navigates to Private Client Group On Configure Menu


* Flow: Configure –> Users –> User Management –> Private Client Groups


* Keyword Usage

> 
> * `navigate_to_configure_private_client_group`


* **Returns**

    1 if Navigation Successful



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

    1 if Navigation Successful



#### navigate_to_configure_user_sub_tab()

* This keyword Navigates to Global Settings on User Account Menu which is already Navigated


* Keyword Usage

> 
> * `Navigate To Configure User Sub Tab`


* **Returns**

    1 if Navigation Successful to Global Settings on User Account Menu else return -1



#### navigate_to_configure_users_subtab_users()

* This keyword Navigates to PPSK Classification On Configure Menu


* Flow: Configure –> Users –> User Management –> Users


* Keyword Usage

> 
> * `Navigate To Configure User Management Users Submenu`


* **Returns**

    1 if Navigation Successful



#### navigate_to_copilot_anomaly_notification_icon()

* This Keyword navigates to Copilot Anomaly Notification Icon


* Keyword Usage:

> 
> * `Navigate To Copilot Anomaly Notification Icon`


* **Returns**

    1 if Navigation Successful



#### navigate_to_copilot_menu()

* This Keyword navigates to Copilot Menu


* Keyword Usage:

> 
> * `Navigate To Copilot Menu`


* **Returns**

    1 if Navigation Successful



#### navigate_to_credential_dist_groups()

* Navigate to Global settings > Credential Distribution Groups


* Flow: Global settings > Credential Distribution Groups


* Keyword Usage:

> 
> * `Navigate To Credential Dist Groups`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_to_dashboard_page()

* Navigate to dashboard page by clicking top left of UI


* Flow: Dashboard Menu


* Keyword Usage:

> 
> * `Navigate To Dashboard Page`


* **Returns**

    1 If Navigated successfully else -1



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

    1 if Navigation Successful else -1



#### navigate_to_device_client_information()

* This keyword is used to navigate to a single device client information tool window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Client Information`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_get_tech_data()

* This keyword is used to navigate to single/multiple device get tech data tool window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Get Tech Data`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_layer_neighbor_info()

* This keyword is used to navigate to a single device l2 neighbor info tool window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Layer Neighbor Info`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_locate_device()

* This keyword is used to navigate to a single device locate device tool window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Locate Device`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_management_settings()

* This Keyword Navigate to Device Management Settings Page


* Flow: Global Settings –> Device Management Settings


* Keyword Usage:

> 
> * `navigate to device management settings page`


* **Returns**

    1 if Navigation Successful



#### navigate_to_device_packet_capture()

* This keyword is used to navigate to a single packet capture tool window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Packet Capture`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_ping()

* This keyword is used to navigate to a single device ping diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Ping`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_amrp_tunnel()

* This keyword is used to navigate to a single device show amrp tunnel diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Amrp Tunnel`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_arp_cache()

* This keyword is used to navigate to a single device show arp cache diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Arp Cache`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_cpu()

* This keyword is used to navigate to a single device show cpu diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Cpu`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_dnxp_cache()

* This keyword is used to navigate to a single device show dnxp cache diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Dnxp Cache`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_dnxp_neighbors()

* This keyword is used to navigate to a single device show dnxp neighbors diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Dnxp Neighbors`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_gre_tunnel()

* This keyword is used to navigate to a single device show gre tunnel diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Gre Tunnel`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_ike_event()

* This keyword is used to navigate to a single device show ike event diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Ike Event`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_ike_sa()

* This keyword is used to navigate to a single device show ike sa diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Ike Sa`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_ip_routes()

* This keyword is used to navigate to a single device show ip routes diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Ip Routes`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_ipsec_sa()

* This keyword is used to navigate to a single device show ipsec sa diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Ipsec Sa`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_ipsec_tunnel()

* This keyword is used to navigate to a single device show ipsec tunnel diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Ipsec Tunnel`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_log()

* This keyword is used to navigate to a single device show log diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Log`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_mac_routes()

* This keyword is used to navigate to a single device show mac routes diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Mac Routes`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_mac_table()

* This keyword is used to navigate to a single device show mac table diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Mac Table`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_memory()

* This keyword is used to navigate to a single device show memory diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Memory`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_pse()

* This keyword is used to navigate to a single device show pse diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Pse`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_roaming_cache()

* This keyword is used to navigate to a single device show roaming cache diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Roaming Cache`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_running_config()

* This keyword is used to navigate to a single device show running config diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Running Config`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_startup_config()

* This keyword is used to navigate to a single device show startup config diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Startup Config`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_version()

* This keyword is used to navigate to a single device show version diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Version`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_show_vpn_tunnel()

* This keyword is used to navigate to a single device show vpn tunnel diagnostic window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Show Vpn Tunnel`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_utilities(device_serial='')

* This Keyword navigates to  device utilities


* Navigate to Manage –> Device


* Select the device row based on the passed device serial


* Click on Utilities –> Status –> Wifi Status Summary


* Keyword Usage:

> 
> * `Navigate To Wifi Status Summary   ${DEVICE_SERIAL}`


* **Parameters**

    **device_serial** – serial number of the device



* **Returns**

    1 if Navigation Successful



#### navigate_to_device_utilities_diagnostics()

* This keyword is used to navigate to utilities diagnostics menu


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Utilities Diagnostics`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_utilities_status()

* This keyword is used to navigate to utilities status menu


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Utilities Status`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_utilities_tools()

* This keyword is used to navigate to utilities tools menu


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Utilities Tools`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_device_vlan_probe()

* This keyword is used to navigate to single/multiple device vlan probe tool window


* Assumes that already navigated to the Manage –> Device page


* Keyword Usage:

> 
> * `Navigate To Device Vlan Probe`


* **Returns**

    1 if Navigation Successful else -1



#### navigate_to_devices()
> 
> * This keyword Navigates to Devices on Manage Menu


> * Flow Manage–> Devices


> * Keyword Usage

> > 
> > * `Navigate To Devices`


* **Returns**

    1 if Navigation Successful to Devices Sub tab on Monitor Tab else return -1



#### navigate_to_essentials_menu()

* This Keyword Navigate to Essentials Menu


* Keyword Usage
- `Navigate To Essentials Menu`


* **Returns**

    1 if Navigation Successful to Essentials Menu



#### navigate_to_external_radius_server()

* This Keyword Navigate to External Radius Server on common objects


* Flow: Configure –> Common Object –> Authentication –> External Radius Server


* Keyword Usage

> 
> * `Navigate To External Radius Server`


* **Returns**

    1 if Navigation Successful



#### navigate_to_extreme_airdefence()

* This Keyword Navigate to Extreme AirDefence Menu


* Flow: Extreme AirDefence


* Keyword Usage
- `Navigate To Extreme AirDefence`


* **Returns**

    1 if Navigation Successful to Extreme AirDefence Menu



#### navigate_to_extreme_guest_menu()

* This Keyword Navigate to Extreme guest Page


* Keyword Usage
- `Navigate To Extreme Guest Menu`


* **Returns**

    1 if Navigation Successful to Extreme Guest Menu



#### navigate_to_extreme_iot_clients_page()

* This Keyword Navigate to Clients Page on Extreme IOT Essentials Page


* Keyword Usage
- `Navigate To Extreme IOT Clients Page`


* **Returns**

    1 if Navigation Successful to Clients Menu on Extreme IOT Essentials Menu



#### navigate_to_extreme_iot_dashboard_page()

* This Keyword Navigate to Dashboard Page on Extreme IOT Essentials Page


* Keyword Usage
- `Navigate To Extreme IOT Dashboard Page`


* **Returns**

    1 if Navigation Successful to Dashboard Menu on Extreme IOT Essentials Menu



#### navigate_to_extreme_iot_devices_page()

* This Keyword Navigate to Devices Page on Extreme IOT Essentials Page


* Keyword Usage
- `Navigate To Extreme IOT Devices Page`


* **Returns**

    1 if Navigation Successful to Devices Menu on Extreme IOT Essentials Menu



#### navigate_to_extreme_iot_menu()

* This Keyword Navigate to Extreme IOT Essentials Page


* Keyword Usage
- `Navigate To Extreme IOT Menu`


* **Returns**

    1 if Navigation Successful to Extreme IOT Essentials Menu



#### navigate_to_extreme_iot_policy_groups_page()

* This Keyword Navigate to policy groups Page on Extreme IOT Essentials Page


* Keyword Usage
- `Navigate To Extreme IOT Policy Groups Page`


* **Returns**

    1 if Navigation Successful to policy groups Menu on Extreme IOT Essentials Menu



#### navigate_to_extreme_iot_user_profiles_page()

* This Keyword Navigate to user profiles Page on Extreme IOT Essentials Page


* Keyword Usage
- `Navigate To Extreme IOT User Profiles Page`


* **Returns**

    1 if Navigation Successful to user profiles Menu on Extreme IOT Essentials Menu



#### navigate_to_extreme_location_access_points_menu()

* This Keyword Navigate to Access Points Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Access Points Menu`


* **Returns**

    1 if Navigation Successful to Access Points Menu on Extreme Location



#### navigate_to_extreme_location_alarms_submenu()

* This Keyword Navigate to Alarms SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Alarms Submenu`


* **Returns**

    1 if Navigation Successful to Alarms SubMenu on Extreme Location



#### navigate_to_extreme_location_asset_management_menu()

* This Keyword Navigate to Beacons Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Asset Management Menu`


* **Returns**

    1 if Navigation Successful to Asset Management Menu on Extreme Location



#### navigate_to_extreme_location_assets_submenu()

* This Keyword Navigate to Assets SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Assets Submenu`


* **Returns**

    1 if Navigation Successful to Assets SubMenu on Extreme Location



#### navigate_to_extreme_location_beacons_menu()

* This Keyword Navigate to Beacons Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Beacons Menu`


* **Returns**

    1 if Navigation Successful to Beacons Menu on Extreme Location



#### navigate_to_extreme_location_bss_devices_submenu()

* This Keyword Navigate to BSS Devices SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location BSS Devices Submenu`


* **Returns**

    1 if Navigation Successful to BSS Devices SubMenu on Extreme Location



#### navigate_to_extreme_location_category_menu()

* This Keyword Navigate to Category Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Category Menu`


* **Returns**

    1 if Navigation Successful to Category Menu on Extreme Location



#### navigate_to_extreme_location_dashboard_menu()

* This Keyword Navigate to Dashboard Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Dashboard Menu`


* **Returns**

    1 if Navigation Successful to Dashboard Menu on Extreme Location



#### navigate_to_extreme_location_device_classification_submenu()

* This Keyword Navigate to Device Classification SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Device Classification Submenu`


* **Returns**

    1 if Navigation Successful to Device Classification SubMenu on Extreme Location



#### navigate_to_extreme_location_devices_menu()

* This Keyword Navigate to Devicess Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Devices Menu`


* **Returns**

    1 if Navigation Successful to Devices Menu on Extreme Location



#### navigate_to_extreme_location_menu()

* This Keyword Navigate to Extreme Location Page


* Keyword Usage
- `Navigate To Extreme Location Menu`


* **Returns**

    1 if Navigation Successful to Extreme Location Menu



#### navigate_to_extreme_location_settings_alarms_submenu()

* This Keyword Navigate to Settings Alarms SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Settings Alarms Submenu`


* **Returns**

    1 if Navigation Successful to Settings Alarms SubMenu on Extreme Location



#### navigate_to_extreme_location_settings_menu()

* This Keyword Navigate to Settings Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Settings Menu`


* **Returns**

    1 if Navigation Successful to Settings Menu on Extreme Location



#### navigate_to_extreme_location_sites_menu()

* This Keyword Navigate to Sites Menu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Sites Menu`


* **Returns**

    1 if Navigation Successful to Sites Menu on Extreme Location



#### navigate_to_extreme_location_third_party_config_submenu()

* This Keyword Navigate to Third Party Configuration SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Third Party Config Submenu`


* **Returns**

    1 if Navigation Successful to Third Party Config SubMenu on Extreme Location



#### navigate_to_extreme_location_threshold_submenu()

* This Keyword Navigate to Threshold SubMenu on Extreme Location


* Keyword Usage
- `Navigate To Extreme Location Threshold Submenu`


* **Returns**

    1 if Navigation Successful to Threshold SubMenu on Extreme Location



#### navigate_to_extreme_location_wireless_devices_submenu()

* This Keyword Navigate to Wireless Devices SubMenu on Extreme Location


* Keyword Usage

> 
> * `Navigate To Extreme Location Wireless Devices Submenu`


* **Returns**

    1 if Navigation Successful to Wireless Devices SubMenu on Extreme Location



#### navigate_to_extreme_networks_a3()

* This Keyword Navigate to Extreme Networks A3 on common objects


* Flow: Configure –> Common Object –> Authentication –> Extreme Networks A3


* Keyword Usage

> 
> * `Navigate To Extreme Networks A3`


* **Returns**

    1 if Navigation Successful



#### navigate_to_global_settings_page()

* This keyword Navigates to Global Settings On User Account Menu


* Flow: User Account Menu –> Global Settings


* Keyword Usage

> 
> * `Navigate To Global Settings Page`


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

    1 if Navigation Successful



#### navigate_to_license_management()
Navigate to the USER ACCOUNT-> Global Settings > License Management
:return:


#### navigate_to_license_mgmt()

* Navigate to the USER ACCOUNT-> Global settings > Account Management


* Flow: USER ACCOUNT-> Global settings > Account Management


* Keyword Usage:

> 
> * `Navigate To License Mgmt`


* **Returns**

    1 If Navigated successfully else -1



#### navigate_to_locked_users_tab()
”
- This Keyword Navigate to Locked Users Page
- Flow: Configure –> Users –> User Management –> Locked Users
- Keyword Usage:

> 
> * ‘Navigate to Locked Users page’


* **Returns**

    1 if Navigation Successful



#### navigate_to_manage_alarms()

* This Keyword Navigate to Alarms on manage Menu


* Flow: Manage –> Alarms


* Keyword Usage:

> 
> * \`\` Navigate To Manage Alarms\`\`


* **Returns**

    1 if Navigation Successful



#### navigate_to_manage_events()
> 
> * This keyword Navigates to Events on Manage Menu


> * Flow Manage–> Events


> * Keyword Usage

> > 
> > * `Navigate To Events`


* **Returns**

    1 if Navigation Successful to Devices Sub tab on Monitor Tab else return -1



#### navigate_to_manage_reports()

* This Keyword Navigate to Reports on Manage Menu


* Flow: Manage –> Reports


* Keyword Usage:

> 
> * `Navigate To Manage Reports`


* **Returns**

    1 if Navigation Successful



#### navigate_to_manage_summary()
> 
> * This keyword Navigates to Summary on Manage Menu


> * Flow Manage–> Summary


> * Keyword Usage

> > 
> > * `Navigate To Manage Summary`


* **Returns**

    1 if Navigation Successful to Summary Sub tab on Monitor Tab else return -1



#### navigate_to_manage_tab()
> 
> * This keyword Navigates to Manage Tab


> * Keyword Usage

> > 
> > * `Navigate To Manage Tab`


* **Returns**

    1 if Navigation Successful to Monitor Tab else return -1



#### navigate_to_manage_users()
> 
> * This keyword Navigates to Users on Manage Menu


> * Flow Manage–> Users


> * Keyword Usage

> > 
> > * `Navigate To Manage Users`


* **Returns**

    1 if Navigation Successful to Users Sub tab on Monitor Tab else return -1



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

    1 if Navigation Successful



#### navigate_to_network360monitor()

* This Keyword Navigate to network360monitor on ML Insights Menu


* Flow: ML Insights –> Network360Monitor


* Keyword Usage:

> 
> * `Navigate To Network360Monitor`


* **Returns**

    1 if Navigation Successful



#### navigate_to_network360plan()

* This Keyword Navigate to network360plan on Manage Menu


* Flow: Manage –> Network360Plan


* Keyword Usage:

> 
> * `Navigate To Network360Plan`


* **Returns**

    1 if Navigation Successful



#### navigate_to_network_policies_card_view_page()

* This Keyword navigate to the policies card view page


* Flow: Configure –> Network Policies –> Card View Tab


* Keyword Usage:

> 
> * `Navigate To Network Policies Card View Page`


* **Returns**

    1 in Navigated to network Policy Card View else None



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



#### navigate_to_network_scorecard()

* This Keyword Navigate to network scorecard on ML Insights Menu


* Flow: ML Insights –> Network Scorecard


* Keyword Usage:

> 
> * `Navigate To Network Scorecard`


* **Returns**

    1 if Navigation Successful



#### navigate_to_network_subnetwork_space()

* This Keyword Navigate to SubNetwork Space Tab On Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>NETWORK–>Subnetwork Space


* Keyword Usage:

> 
> * `Navigate To Network Subnetwork Space`


* **Returns**

    1 if Navigation Successful



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

    1 if Navigation Successful



#### navigate_to_policy_imago_tag_profiles()

* This Keyword Navigate to Imago Tag Profile on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>Imago Tag Profiles


* Keyword Usage:

> 
> * `Navigate To Policy Imago Tag Profiles`


* **Returns**

    1 if Navigation Successful



#### navigate_to_policy_port_types()

* This Keyword Navigate to Port Types On Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>POLICIES–>PORT TYPES


* Keyword Usage:

> 
> * `Navigate To Policy Port Types`


* **Returns**

    1 if Navigation Successful



#### navigate_to_policy_user_profiles()

* This Keyword Navigate to User Profiles on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>POLICY–>USER PROFILES


* Keyword Usage:

> 
> * `Navigate To Policy User Profiles`


* **Returns**

    1 if Navigation Successful



#### navigate_to_radio_profile()

* This keyword Navigates to SSIDs Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> Radio Profile


* Keyword Usage

> 
> * `Navigate To Radio Profile`


* **Returns**

    1 if Navigation Successful



#### navigate_to_retail_dashboard()

* This Keyword Navigate to retail dashboard on ML Insights Menu


* Flow: ML Insights –> Retail Dashboard


* Keyword Usage:

> 
> * `Navigate To Retail Dashboard`


* **Returns**

    1 if Navigation Successful



#### navigate_to_security_ip_firewall_policies()

* This Keyword Navigate to WIPS Policies on Common Objects


* Flow: CONFIGURE–>COMMON OBJECTS–>SECURITY–>IP Firewall POLICIES


* Keyword Usage:

> 
> * `Navigate To Security IP Firewall Policies`


* **Returns**

    1 if Navigation Successful



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

    1 if Navigation Successful



#### navigate_to_servers()

* This Keyword Navigate to Servers on common objects


* Flow: Configure –> Common Object –> Authentication –> Servers


* Keyword Usage

> 
> * `Navigate To Servers`


* **Returns**

    1 if Navigation Successful



#### navigate_to_ssids()

* This keyword Navigates to SSIDs Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> SSIDs


* Keyword Usage

> 
> * `Navigate To SSIDs`


* **Returns**

    1 if Navigation Successful



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

    1 if Navigation Successful



#### navigate_to_switch_templates()

* This keyword Navigates to Switch Templates Menu on Common Objects


* Flow Configure –> Common Objects –> Policy –> Switch Templates


* Keyword Usage

> 
> * `Navigate To Switch Templates`


* **Returns**

    1 if Navigation Successful



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



#### navigate_to_unbind_device_tab()
”
- This Keyword Navigate to Unbind Device Page
- Flow: Configure –> Users –> User Management –> Unbind Device
- Keyword Usage:

> 
> * ‘Navigate to Unbind Device page’


* **Returns**

    1 if Navigation Successful



#### navigate_to_user_account()

* This keyword Navigates to User Account Menu


* Keyword Usage

> 
> * `Navigate To User Account`


* **Returns**

    1 if Navigation Successful to User Account Menu else return -1



#### navigate_to_viq_management_page()

* This Keyword Navigate to VIQ Management Page


* Flow: Global Settings –> VIQ Management


* Keyword Usage:

> 
> * `Navigate To Viq Management Page`


* **Returns**

    1 if Navigation Successful



#### navigate_to_vpn_services_tab()
”
- This Keyword Navigate to VPN Services Page
- Flow: Manage –> VPN Services
- Keyword Usage:

> 
> * ‘Navigate to VPN Services Tab’


* **Returns**

    1 if Navigation Successful, else -1



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

    1 if Navigation Successful



#### navigate_tool_utility()

* Navigate to the Tools->Utilities link


* Flow: Tools->Utilities


* Keyword Usage:

> 
> * `Navigate Tool Utility`


* **Returns**

    1 If Navigated successfully else -1



#### point_client_hyperlink_to_client360()
”
- This Keyword point client hyperlink to Client 360 page in ML Insights
- Flow: Client Hyperlink –> ML Insights –> Client 360
- Keyword Usage:

> 
> * ‘Point Client Hyperlink To Client360’


* **Returns**

    1 if Navigation Successful, else -1



#### rbac_user_navigate_to_extreme_airdefence_helpdesk()

* This Keyword is used to check if Extreme Airdefence menu is available for RBAC helpdesk user


* Flow: Extreme AirDefence


* Keyword Usage
- 

```
``
```

Check for Extreme AirDefence menu \`\`


* **Returns**

    1 if Navigation is not Successful to Extreme AirDefence Menu


## extauto.xiq.flows.common.SideNavMenu module


### _class_ extauto.xiq.flows.common.SideNavMenu.SideNavMenu()
Bases: `NavigatorWebElements`


#### get_order_number_of_main_nav_tab(tab_tag)

* This Keyword gets the order number of the specified main nav tab


* Keyword Usage:

> 
> * `Get Order Number Of Main Nav Tab`


* **Parameters**

    **tab_tag** – automation tag for the nav tab



* **Returns**

    number if match else -1



#### get_order_number_of_side_nav_menu_item(menu_item_tag)

* This Keyword gets the order number of the specified side nav menu item


* Keyword Usage:

> 
> * `Get Order Number Of Side Nav Menu Item`


* **Parameters**

    **menu_item_tag** – automation tag for the side nav menu item



* **Returns**

    number if match else -1



#### get_order_number_of_side_nav_sub_menu_item(menu_item_tag)

* This Keyword gets the order number of the specified side nav sub menu item


* Keyword Usage:

> 
> * `Get Order Number Of Side Nav Sub Menu Item`


* **Parameters**

    **menu_item_tag** – automation tag for the side nav menu item



* **Returns**

    number if match else -1



#### has_main_nav_tab_the_expected_image(tab_tag, expected_class)

* This Keyword checks if the expected class of the specified main nav tab exists


* Keyword Usage:

> 
> * `Has Main Nav Tab The Expected Image`


* **Parameters**

    
    * **tab_tag** – automation tag for the nav tab


    * **expected_class** – expected class name



* **Returns**

    1 if exists, else -1



#### is_nav_menu_item_enabled(tag)

* This Keyword checks if the specified nav menu item is enabled


* Keyword Usage:

> 
> * `Is Nav Menu Item Enabled`


* **Parameters**

    **tag** – automation tag for the nav menu item



* **Returns**

    1 if visible, -1 if not



#### is_nav_menu_item_visible(tag)

* This Keyword checks if the specified nav menu item is visible


* Keyword Usage:

> 
> * `Is Nav Menu Item Visible`


* **Parameters**

    **tag** – automation tag for the nav menu item



* **Returns**

    1 if visible, -1 if not



#### is_the_expected_url(expected_url)

* This Keyword checks if the expected url of the specified main nav tab is loaded


* Keyword Usage:

> 
> * `Is The Expected Url`


* **Parameters**

    **expected_url** – expected url



* **Returns**

    1 if exists, else -1


## extauto.xiq.flows.common.SpecificSearch module


### _class_ extauto.xiq.flows.common.SpecificSearch.SpecificSearch()
Bases: `object`


#### ap_specific_search(info)

* searches information specific to AP in Devices page


* **Returns**

    1 if successfully Search information about specific AP else -1



#### application_specific_search(info)

* searches information specific to application in Application page


* **Returns**

    1 if successfully Search information about specific Application else -1



#### warning_search_close_window(info)

* searches information specific to warning page


* **Returns**

    1 if successfully Search information about specific Application else -1


## extauto.xiq.flows.common.ToolTipCapture module


### extauto.xiq.flows.common.ToolTipCapture.tool_tip_capture()
Capture tool tip in daemon process and append to global list


* **Returns**

    None


## extauto.xiq.flows.common.WiredLib module


### _class_ extauto.xiq.flows.common.WiredLib.WiredLib()
Bases: `object`


#### check_transmission_mode_exos(range_ports_start, range_ports_end, sw_spawn, state)

* **Parameters**

    
    * **range_ports_start** – First port of range


    * **range_ports_end** – End port of range


    * **sw_spawn** – spawn


    * **state** – Port state . If state = “” , that port will be ignored



* **Returns**

    1 if the status of transmission in XIQ and CLI are the same
    -1 if the status of transmission in XIQ and CLI are different



#### check_vlan_cli(vlan, device_make, sw_spawn)

* **Parameters**

    
    * **vlan** – 


    * **device_make** – 


    * **sw_spawn** – 



* **Returns**

    


#### configure_port_auto_cli(range_ports_start, range_ports_end, sw_spawn)
Thei function configured into CLI on EXOS devices the auto transmission mode


* **Parameters**

    
    * **range_ports_start** – First port of range


    * **range_ports_end** – End port of range


    * **sw_spawn** – spawn



* **Returns**

    1



#### configure_port_duplex_cli(range_ports_start, range_ports_end, sw_spawn, operate, speed=100)
Thei function configured into CLI on EXOS devices the duplex mode and speed


* **Parameters**

    
    * **range_ports_start** – First port of range


    * **range_ports_end** – End port of range


    * **sw_spawn** – spawn


    * **operate** – Operate mode


    * **speed** – Speed of port



* **Returns**

    

## extauto.xiq.flows.common.adsp module


### _class_ extauto.xiq.flows.common.adsp.Adsp()
Bases: `AdspWebElements`


#### get_adsp_alarm_details(search_string)

* Get Alarm details based on search string


* Flow: Manage–> Alarms


* Keyword Usage:

> 
> * `Get Alarm Details   ${DEVICE_MAC}`


> * `Get Alarm Details   ${DEVICE_NAME}`


> * `Get Alarm Details   ${ALARM_CATEGORY}`


* **Parameters**

    **search_string** – str to search the alarm in grid ex: it may be severity, host name, Device mac, category


:return:(dict) Alarm Details in dictionary Format


#### get_adsp_alarm_grid_row(search_string)

* Get the Adsp Alarm row from the grid row based on the search string


* Assumes that already navigated to the Manage–> Alarms page


* **Parameters**

    **search_string** – str to search the alarm in grid ex: it may be severity, host name, Device mac, category


:return:Alarm row information if row present with Search String

## Module contents
