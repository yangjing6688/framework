# extauto.common

## extauto.common.Ap module


### _class_ extauto.common.Ap.Ap()
Bases: `object`


#### access_ap_root_prompt(ap_spawn, ap_mac)

* This keyword will Get Wing AP Root Prompt


* Keyword Usage:

> 
> * `Access AP Root Prompt    ${AP_SPAWN}   ${AP_MAC}`


* **Parameters**

    
    * **ap_spawn** – AP Spawn to Open Console


    * **ap_mac** – AP Mac Address



* **Returns**

    1 if Wing AP root Prompt Access Successful



#### get_ap_last_root_password(ap_spawn)

* This keyword will Get Wing AP Last used Root Password


* Keyword Usage:

> 
> * `Get AP Last Root Password    ${AP_SPAWN}`


* **Parameters**

    **ap_spawn** – AP Spawn to Open Console



* **Returns**

    Last used Password of Wing AP else -1



#### load_cloud_certificate_on_ap(spawn, mac)

* Load Cloud Certificate on Access Point


* Keyword Usage:

> 
> * `Load Cloud Certificate On AP    ${AP_SPAWN}   ${MAC_ADDRESS}`


* **Parameters**

    
    * **spawn** – AP Spawn to Open Console


    * **mac** – Wing AP Mac Address



* **Returns**

    None



#### send_command_to_ap_root(ap_spawn, ap_mac, command)

* This keyword will uses to send CLI Command to Win g AP


* Keyword Usage:

> 
> * `Send Command To AP Root    ${AP_SPAWN}   ${AP_MAC}   ${CLI_COMMAND}`


* **Parameters**

    
    * **ap_spawn** – AP Spawn to Open Console


    * **ap_mac** – AP Mac Address


    * **command** – Wing AP CLI Command



* **Returns**

    Wing AP CLI command Output


## extauto.common.AutoActions module


### _class_ extauto.common.AutoActions.AutoActions()
Bases: `object`


#### center_element(element)

* **Parameters**

    **element** – 



* **Returns**

    


#### click(element)

* This Keyword Uses to Click the Mentioned Web Element


* If the Element is not visible into view it Scroll element into view and Scroll down into page to click Element


* **Parameters**

    **element** – Web Element to Click on Web Page



* **Returns**

    None



#### click_and_hold_element(source_el, offset_value=40)

* Click and hold the element


* **Parameters**

    
    * **source_el** – source element


    * **offset_value** – offset value


:return:if Element Click and Hold successful else -1


#### click_image(position)

#### disable_check_box(element)

* Disable the check box


* **Parameters**

    **element** – check box locator element



* **Returns**

    None



#### disable_radio_button(element)

* This Keyword Uses to Disable Radio Button.


* **Parameters**

    **element** – Radio Button locator element



* **Returns**

    None



#### double_click(source_el)

* Double click the element


* **Parameters**

    **source_el** – source element



* **Returns**

    1 if action was successful, else -1



#### drag_and_drop_element(source_el, target_el)

* Drag and drop the element from Source Element to Target Element


* **Parameters**

    
    * **source_el** – source element


    * **target_el** – target element


:return:1 if Element Drag and Drag successful else -1


#### enable_check_box(element)

* Enable the check box


* **Parameters**

    **element** – check box locator element


:return:None


#### enable_radio_button(element)

* This Keyword Uses to Enable Radio Button.


* **Parameters**

    **element** – Radio Button locator element



* **Returns**

    None



#### move_to_element(element)

* This Keyword Uses to Move the Mentioned Web Element using Mouse Actions


* **Parameters**

    **element** – Web Element to Move the Mouse Cursor on Web Page



* **Returns**

    None



#### right_click(source_el)

* Right click (context click) the element


* **Parameters**

    **source_el** – source element



* **Returns**

    1 if action was successful, else -1



#### scroll_by()

* This Keyword Uses to Scroll the page by 250 pixels y-coordinate


* **Returns**

    None



#### scroll_by_horizontal(element)

* This Keyword Uses to Scroll the page ro end in x-coordinate


* **Returns**

    None



#### scroll_down()

* This Keyword Uses to Scroll Down the page.


* **Returns**

    None



#### scroll_up()

* This Keyword Uses to Scroll Up the page.


* **Returns**

    None



#### select_drop_down_options(options, item)

* Select the item from the drop down options


* loop over the options and compare the text with item to be selected.


* if item text present in options select that item element


* **Parameters**

    
    * **options** – list of options


    * **item** – element to be select based on item string



* **Returns**

    True if selected else None



#### select_drop_down_options_partial_match(options, item)

* Select the item from the drop down options using a partial match - if the item is a sub string of


* one of the options, the first found will be selected.


* loop over the options and compare the text with item to be selected.


* if item text present in options select that item element


* **Parameters**

    
    * **options** – list of options


    * **item** – element to be select based on item string using partial match



* **Returns**

    True if selected else None



#### select_options(element, item, by='value')
Select the available options from drop down
:param element:
:param by:
:param item:
:return:


#### select_radio_button(element)

* select the radio button


* **Parameters**

    **element** – radio button element


:return:None


#### select_table_range(start_row, end_row)

* Selects a range in the table by clicking the first row, holding Shift, and clicking the last row.


* **Parameters**

    
    * **start_row** – first row to select in the range


    * **end_row** – last row to select in the range



* **Returns**

    1 if action was successful, else -1



#### send_enter(element)

* This Keyword Uses to press enter Key on Web Page from mentioned Web Element


* **Parameters**

    **element** – Web Element To enter Send Key



* **Returns**

    None



#### send_keys(element, value)

* This Keyword Uses to Send Clear the Text Area and Input the Mentioned Value on Text Field Web Element.


* **Parameters**

    
    * **element** – Web Element To enter Text Field


    * **value** – Element Text Field Value



* **Returns**

    None



#### send_page_down(element)

* This Keyword Uses to press Page down Key on Web Page from mentioned Web Element


* **Parameters**

    **element** – Web Element To enter Page Down Key



* **Returns**

    None



#### shift_click(source_el)

* Holds Shift while performing the click.  This is useful for multi-selecting items in a table.


* **Parameters**

    **source_el** – element to click with the Shift modifier



* **Returns**

    1 if action was successful, else -1


## extauto.common.Cli module


### _class_ extauto.common.Cli.Cli()
Bases: `object`


#### capwap_ap_on_off(ip, usr, passwd, mode)

* This Keyword will enable/disable capwap mode


* Keyword Usage:

> 
> * `Capwap AP On Off`


* **Parameters**

    
    * **ip** – IP Address of AP


    * **usr** – user name


    * **passwd** – Password


    * **mode** – Either on/off



* **Returns**

    None



#### clear_ssh_host_key()

* This keyword will clear the SSH key


* Keyword Usage:

> 
> * `clear ssh host key`


* **Returns**

    None



#### close_netmiko_spawn(spawn)

* Closing netmiko spawn object


* Keyword Usage:

> 
> * `Close Netmiko Spawn   ${SPAWN}`


* **Parameters**

    **spawn** – netmiko spawn



* **Returns**

    returns -1 if there is any exception



#### close_paramiko_spawn(spawn)

* Closes paramiko spawn object


* Keyword Usage:

> 
> * `Close Paramiko Spawn   ${SPAWN}`


* **Parameters**

    **spawn** – paramiko spawn



* **Returns**

    returns -1 if there is any exception



#### close_pxssh_spawn(\*\*kwargs)

#### close_spawn(spawn, \*\*kwargs)

* Closes a device spawn


* Keyword Usage:

> 
> * `Close Spawn`


* **Parameters**

    **spawn** – device spawn



* **Returns**

    1 if device spawn closed successfully else -1



#### configure_device_to_connect_to_cloud(cli_type, ip, port, username, password, server_name, vr='VR-Default', retry_count=10)

* This Keyword will configure necessary configuration in the Device to Connect to Cloud


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Configure Device To Connect To Cloud   ${DEVICE_MAKE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}

>     ${PLATFORM}  ${SERVER_NAME}\`\`


* **Parameters**

    
    * **cli_type** – Device Cli Type


    * **ip** – Console IP Address of the Device


    * **port** – Console Port


    * **username** – username to access console


    * **password** – Password to access console


    * **server_name** – Cloud Server Name to connect the device


:param vr : VR configuration Option for EXOS device. options: VR-Default and VR-Mgmt
:param retry_count: Retry count to check device connection status with capwap server
:return: 1 id device successfully connected with capwap server else -1


#### disconnect_device_from_cloud(cli_type, ip, port, username, password, retry_count=10)

* This Keyword Disconnect Device From Cloud


* Keyword Usage:

> 
> * `disconnect device from cloud  ${CLI_TYPE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}`


* **Parameters**

    
    * **cli_type** – The cli type


    * **ip** – Console IP Address of the Device


    * **port** – Console Port


    * **username** – username to access console


    * **password** – Password to access console


    * **retry_count** – Retry count to check device connection status with Cloud server



* **Returns**

    1 id device successfully disconnected with cloud server else -1



#### downgrade_iqagent_exos(ip, port, username, password, cli_type, url_image)

#### downgrade_iqagent_voss(ip, port, username, password, cli_type)

#### exec_shell_command(exec_shell_command)

* Executes a shell command


* Keyword Usage:

> 
> * `Exec Shell Command  ${SHELL_COMMAND}`


* **Parameters**

    **exec_shell_command** – Any shell command



* **Returns**

    output of the command



#### get_ap_version(spawn=None)

* This method returns the AP HiveOs version


* Keyword Usage:

> 
> * `Get AP Version`


* **Parameters**

    **spawn** – spawn to AP



* **Returns**

    returns the version if success else -1



#### get_mac_hostname(ip, userid, passwd)

* This keyword will get the Host Name of Mac book


* Keyword Usage:

> 
> * `Get MAC Hostname  ${IP}  ${USERNAME}  {PASSWORD}`


* **Parameters**

    
    * **ip** – IP Address of MAC book


    * **userid** – username of MAC book


    * **passwd** – Password of MAC book



* **Returns**

    Host Name of mac book



#### get_thput_value(ip, cli_spawn, server_spawn)

* Get the throughput value from and to air


* Keyword Usage:
- `Get Thput Value   ${IP}    ${CLI_SPAWN}   ${SERVER_SPAWN}`


* **Parameters**

    
    * **ip** – IP address


    * **cli_spawn** – CLI Spawn


    * **server_spawn** – Server Spawn



* **Returns**

    server command output



#### httping_from(_spawn, destination, count=3, timeout=5)

* This method pings from the spawn to the destination.


* default count is 3


* Keyword Usage:

> 
> * `Httping From   ${SPAWN}  ${DESTINATION_IP}`


> * `Httping From   ${SPAWN}  ${DESTINATION_IP}   count=10`


> * `Httping From   ${SPAWN}  ${DESTINATION_IP}   count=10   timeout=10`


* **Parameters**

    
    * **_spawn** – spawn of DUT/host from where ping should start


    * **destination** – IP or host name


    * **count** – Number of ping requests. Default is 3


    * **timeout** – Timeout for the HTTP ping. Default is 5 seconds



* **Returns**

    returns 1 if 0 packet loss else -1



#### mac_wifi_connection(ip, usr, passwd, ssid, ssid_pass='badpassword20\*rd', wifi_port='en1', mode='pass', ntimes=1)

* This Keyword will establish WiFi Connection in MAC PC/Laptop


* Keyword Usage:

> 
> * `mac_wifi_connection  ${IP}  ${USERNAME}  {PASSWORD}  ${SSID}`


> * `mac_wifi_connection  ${IP}  ${USERNAME}  {PASSWORD}  ${SSID}  ssid_pass=${SSID_PASSWORD}`


* **Parameters**

    
    * **ip** – IP Address of MAC book


    * **usr** – username of MAC book


    * **passwd** – Password of MAC book


    * **ssid** – WiFI SSID


    * **ssid_pass** – ssid Password


    * **wifi_port** – WiFi interface


    * **mode** – WiFi Mode


    * **ntimes** – No.of times to try to establish the WiFi Connections



* **Returns**

    None



#### open_paramiko_ssh_spawn(host, username, password, port=22)

* Creating ssh spawn object


* Keyword Usage:

> 
> * `Open Paramiko SSH Spawn   ${HOST}  ${USERNAME}  ${PASSWORD}`


* **Parameters**

    
    * **host** – IP or host name of DUT


    * **username** – username to access Spawn


    * **password** – password to access Spawn



* **Returns**

    returns spawn else -1



#### open_pxssh_spawn(\*\*kwargs)

#### open_spawn(ip, port, username, password, cli_type, connection_method='ssh')

* This Keyword used to access device/host Prompt Using IP Address,port number, username,password and cli_type

# Device type:

    
    * VOSS


    * EXOS


    * WING-AP


    * AH-FASTPATH


    * AH-AP


    * AH-XR

# Endsystem:

    
    * MU-WINDOWS


    * MU-MAC


    * MU-LINUX


    * A3


* Keyword Usage:

> 
> * `Open Spawn     ${IP}   ${PORT}  ${USERNAME}  ${PASSWORD}   ${cli_type}`


* **Parameters**

    
    * **ip** – Device IP address


    * **port** – port number for spawn access


    * **username** – User Name for spawn access


    * **password** – Password for spawn access


    * **cli_type** – Device Cli Type


    * **connection_method** – The connection type, will default to ssh. (ssh, telnet, console)



* **Returns**

    Device Prompt



#### ping_from(destination, count=3)

* This method pings from the script host to the destination.


* default count is 3


* Keyword Usage:

> 
> * `Ping From     ${DESTINATION_IP}`


> * `Ping From     ${DESTINATION_IP}  count=10`


* **Parameters**

    
    * **destination** – IP or host name


    * **count** – Number of ping requests. Default is 3



* **Returns**

    returns 1 if 0 packet loss else -1



#### ping_from_spawn(_spawn, destination, count=3)

* This method pings from the spawn to the destination.


* default count is 3


* Keyword Usage:

> 
> * `Ping From Spawn   ${SPAWN}  ${DESTINATION_IP}`


> * `Ping From Spawn   ${SPAWN}  ${DESTINATION_IP}   count=10`


* **Parameters**

    
    * **_spawn** – spawn of DUT/host from where ping should start


    * **destination** – IP or host name


    * **count** – Number of ping requests. Default is 3



* **Returns**

    returns 1 if 0 packet loss else -1



#### send(spawn, line, expect_match='default', time_out='default', platform='default', \*\*kwargs)

* This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor


* Default timeout is 90 seconds


* Keyword Usage:

> 
> * `Send   ${SPAWN}        ${COMMAND}`


* **Parameters**

    
    * **spawn** – Device Spawn to execute command


    * **line** – CLI command to be execute


    * **expect_match** – Expected Prompt Match


    * **time_out** – Timeout value


    * **platform** – Device/Host Platform (Not needed anymore)


Optional Arguments (kwargs):
:param wait_for_prompt: If set to True, keyword will move on without waiting for the device prompt to return. This is often used in cli commands that have follow-up questions or outputs that do not contain the prompt. Default is False.
:param check_initial_prompt: If set to False, keyword will not check for prompt before issuing a command to agent. Default is True.
:param expect_error: This will cause a keyword to fail unless an error is seen in the commands output. This is disabled by default.
:param wait_for and interval: This function executes a wait for validation. It checks the result of the passed parse function every (The time in seconds between each status check of the keyword function) until it matches the expected result or <max_wait> seconds have passed.
:param max_wait: The amount of time in seconds the keyword should wait before it is considered a failure.
:param ignore_error: This adds errors to the devices error checker to ignore for the given keyword.
:param ignore_cli_feedback: If set to True CLI feedback is ignored. This is set to False by default. This will ignore any errors that may be returned from running this keyword. This could be used to make sure the device is in a clean state before a test will begin. In some cases the keyword would execute with and without errors but the user doesn’t want to report on the errors that may be returned.
:param prompt:  This accepts a prompt constant (which can be found in NetworkElementConstants).

> It tells the device which prompt it should sent the command from.


* **Parameters**

    
    * **prompt_args** – This accepts either a string or list of strings which should contain
    any arguments required by the prompt handler to change prompt.


    * **confirmation_phrases** – This accepts either a string or list of strings which contain any
    outputs that require a response.


    * **confirmation_args** – This accepts a string or list of strings to send in response to the
    received confirmation phrase.



* **Returns**

    CLI Command Output



#### send_commands(spawn, commands_list)

* Sends multiple commands separated by a “,”


* Keyword Usage:

> 
> * `Send Commands   ${SPAWN}  ${COMMAND_LIST}`


* **Parameters**

    
    * **spawn** – spawn of DUT/host


    * **commands_list** – list of DUT/Lunux commands separated by comma



* **Returns**

    output of the command



#### send_paramiko_cmd(spawn, cmd, timeout=10)

* Execute the commands on ssh spawn


* Keyword Usage:

> 
> * `Send Paramiko Cmd   ${SPAWN}  ${COMMAND}`


> * `Send Paramiko Cmd   ${SPAWN}  ${COMMAND}  timeout=${TIMEOUT_VALUE}`


* **Parameters**

    
    * **spawn** – Paramiko spawn


    * **cmd** – command to send


    * **timeout** – command timeout



* **Returns**

    -1 in case of error else output of command



#### send_pxssh(\*\*kwargs)

#### wait_for_cli_output(spawn, cmd, expected_output, retry_duration=30, retry_count=10)

* This Keyword will Helps to Wait till getting expected output based on retry duration


* Retry duration by default 30 seconds


* Retry Count by default 10


* Keyword Usage:

> 
> * `Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}`


> * `Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60`


> * `Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60  ${COUNT}=15`


* **Parameters**

    
    * **spawn** – Device Spawn


    * **cmd** – Command to Execute


    * **expected_output** – Expected CLI Output


    * **retry_duration** – Retry Duration in seconds


    * **retry_count** – Retry Count



* **Returns**

    1 if Getting the expected output else -1


## extauto.common.CloudDriver module


### _class_ extauto.common.CloudDriver.CloudDriver()
Bases: `object`


#### close_browser()

#### close_window(win_index=0)

* This keyword will close Windows handles based on windows index value


* By default it will close windows handles index 0


* Keyword Usage:
- `Close Window`
- `Close Window  win_index=${INDEX_VALUE}`


* **Parameters**

    **win_index** – windows index value


:return:None


#### get_child_window_list(win_index=0)

* This keyword will obtain the Windows handles for any child windows that are open.


* The order of the list is reversed to handle the conditional test within ‘Switch To Window’


* The parent window is not included in the returned list.


* Keyword Usage:
- `Get Child Window List`


* **Param**

    win_index - XIQ Window Index value



* **Returns**

    List of Child Window Indexes (list order reversed)



#### load_browser(url='default', program='default', incognito_mode='False')

* This keyword will Load the default Test URL on Browser Mentioned in the topology file and environment file


* Otherwise It Loads the Mentioned URL


* By default it will not open the URL in Incognito Window


* Keyword Usge:

    
        * `Load Browser  url=${URL}`


        * `Load Browser  url=${URL}   program=${PROGRAM}   incognito_mode=${INCOGNITO_MODE}`


* **Parameters**

    
    * **url** – URL to Load on Browser


    * **program** – cloud url by default othewise adsp,xiqse etc


    * **incognito_mode** – Incognito Mode flag to open the browser



* **Returns**

    Cloud Driver



#### open_window(url='default', program='default')

* This keyword will Load the default Test URL mentioned in topology file on new windows handles

> 
> * Keyword Usage:


>         * `Open Window  url=${URL}`


>         * `Open Window  url=${URL}   program=${PROGRAM}`


* **Parameters**

    
    * **url** – URL to Load on Browser


    * **program** – cloud url by default othewise adsp,xiqse etc



* **Returns**

    Windows Index



#### refresh_page()

#### start_browser(url='default', program='default', incognito_mode='False')

#### switch_to_window(win_index=0)

* This keyword will switch to Windows handles based on windows index value


* By default it will switch to windows handles index 0


* Keyword Usage:
- `Switch To Window`
- `Switch To Window  win_index=${INDEX_VALUE}`


* **Parameters**

    **win_index** – windows index value


:return:None

## extauto.common.CoPilotUtils module


### _class_ extauto.common.CoPilotUtils.CoPilotUtils()
Bases: `Cli`


#### connect_to_xiq_cloud_console(local_host_ip, local_host_username, local_host_pwd, js_ip, js_username, js_pwd, rdc_console_name, rdc_console_username, ahqa_key)
This keyword connects to XIQ Cloud Console


* **Parameters**

    
    * **local_host_ip** – local host IP


    * **local_host_username** – local host Username


    * **local_host_pwd** – local host Password


    * **js_ip** – Jump Station IP address


    * **js_username** – Jump Station Username


    * **js_pwd** – Jump Station Password


    * **rdc_console_name** – RDC Console Name Ex: g7r1-console.qa.xcloudiq.com, g7r3-console.qa.xcloudiq.com


    * **rdc_console_username** – 


    * **ahqa_key** – QA keys relative path



* **Returns**

    


#### disconnect_from_xiq_cloud_console()
This keyword sends a command to XIQ cloud console
:return: 1 if success, -1 if fails


#### send_command_to_xiq_cloud_console(command, timeout=10)
This keyword sends a command to XIQ cloud console
:param command: command to send to XIQ cloud console
:param timeout: timout for the command
:return: returns command output

## extauto.common.CommonValidation module


### _class_ extauto.common.CommonValidation.CommonValidation()
Bases: `object`


#### get_kwarg(kwargs, key, default='')

#### get_kwarg_bool(kwargs, key, def_val)
Returns a normalized boolean from the kwarg.


#### string_to_boolean(boolean_string, default=True)
Converts boolean strings to a python boolean.
Example “True” and “true” would be converted to True.
The default option is used to set the boolean value when the passed string
does not contain “True”, “true”, “False”, or “false”.


#### validate(value, expectedValue, \*\*kwargs)
Description: Validate the input values for framework

kwargs:

    IRV = Internal Result verification flag, will be set to true by default
    fail_msg = The message to print on failure
    pass_msg = The message to print on success
    ignore_cli_feedback = which ignores any errors or output from the keyword
    expect_error = verifies that an error was returned by the keyword


### _exception_ extauto.common.CommonValidation.FailureException()
Bases: `AssertionError`


#### ROBOT_CONTINUE_ON_FAILURE(_ = Tru_ )
## extauto.common.ConfigFileHelper module


### _class_ extauto.common.ConfigFileHelper.ConfigFileHelper()
Bases: `object`


#### build_dict_of_elems(\*\*kwargs)

#### checkConfigRefresh()

#### get_device_names_from_variables(var_prefix)
Returns a list of all devices with the same var_prefix.


#### get_device_number(search_name)
Returns the DeviceNumber for the devicetypeDeviceNumber[‘name’]
Ex:
For netelem2 the device number is “2”


#### loadRdcAio()

#### loadTestBed()

#### set_ap1_default()
Returns old style of AP1_UPPER variables for first AP or allows
substituting any AP# in the yaml file, based on model number if the variable
AP_MODEL or AP is passed in on the command line

## extauto.common.GmailHandler module


### _class_ extauto.common.GmailHandler.GmailHandler()
Bases: `object`


#### get_cloud_cwp_no_pin_event_report(mail_id, password, mail_trash='True')

* Get the CWP No pin Event report


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Cloud Cwp No Pin Event Report  ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    event report from and to time



#### get_cloud_cwp_pin_event_report(mail_id, password, mail_trash='True')

* Get the CWP pin Event report csv and table data


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Cloud Cwp Pin Event Report   ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to get event reports


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    event report table data and csv data



#### get_cloud_pin_for_wi_fi_network(mail_id, password, mail_trash='True')

* Get WI-Fi Network access cloud PIN


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Cloud Pin For Wi Fi Network    ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    cloud pin



#### get_email_reports_url_link(mail_id, password, mail_trash='True')

* Get the url link of email reports sent by XIQ


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Email Reports Url Link    ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – mail id to get the url link


    * **password** – mail id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    url link



#### get_email_subj(mail_id, password)

* Get email subject line


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Email Subj   ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id


    * **password** – email id password



* **Returns**

    email subj line



#### get_login_credential(mail_id, password, mail_trash='True')

* Get User Credential sent to email


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Login Credential  ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    access_key, login id



#### get_login_credential_from_attachments(mail_id, password, mail_trash='True')

* Get bulk user credentials from attachments


* It will read the latest two emails


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Login Credentials From Attachments  ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    credentials dict



#### get_password_reset_link(mail_id, password, mail_trash='True')

* Get the url link to set the new user password


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Password Reset Link  ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    reset url link



#### get_password_setup_link(mail_id, password, msg, mail_trash='True')

* Get the url link to set the new user password


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Password Setup Link  ${MAIL_ID}  ${PASSWORD}    ${MSG}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **msg** – subject line of email id to search from gmail


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    reset url link



#### get_sender_email_id(mail_id, password, subj_line, mail_trash='True')

* Get the sender email id based on the subj line


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Sender Email Id  ${MAIL_ID}  ${PASSWORD}  ${SUBJ_LINE}`


* **Parameters**

    
    * **mail_id** – id of the email


    * **password** – password of the email


    * **subj_line** – subject string to get the email


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    sender email id



#### get_sponsor_action_login_credential(mail_id, password, emailto, passcode_length)

* Get the user credential from email


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Sponsor Action Login Credential  ${EMAIL_ID}   ${PASSWORD} ${EMAIL_TO}  ${SPONSOR_ACTION}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **emailto** – email is sent to ‘sponsor’ or ‘user’


    * **passcode_length** – passcode length length=4 for OTP and 8 for Passcode



* **Returns**

    passcode



#### get_sponsor_action_url(mail_id, password, sponsor_action)

* Get the sponsor action url link


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Sponsor Action Url  ${EMAIL_ID}   ${PASSWORD}  ${SPONSOR_ACTION}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **sponsor_action** – ‘permit’ or ‘deny’ action by sponsor


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    url link



#### get_url_to_set_password_for_new_user(mail_id, password, mail_trash='True')

* Get the url link to set the new user password


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get Url To Set Password For New User  ${MAIL_ID}  ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    url link



#### get_user_approval_url(mail_id, password, mail_trash='True')

* Get the user approve url link


* It will read the latest two emails


* Keyword Usage:

> 
> * `Get User Approval Url  ${EMAIL_ID}   ${PASSWORD}`


* **Parameters**

    
    * **mail_id** – email id to open


    * **password** – email id password


    * **mail_trash** – trash the mail if mail trash is true



* **Returns**

    url link


## extauto.common.Iapi module

## extauto.common.IdentifiAP module


### _class_ extauto.common.IdentifiAP.IdentifiAP()
Bases: `object`


#### factory_rest_identifi_ap(ip, port)

* Does factory reset of Indentifi AP


* Keyword Usage:

> 
> * `Factory Rest Identifi AP    ${ip}   ${port}`


* **Parameters**

    
    * **ip** – IP address of AP console


    * **port** – AP console port



* **Returns**

    1 if successful


## extauto.common.ImageAnalysis module


### _class_ extauto.common.ImageAnalysis.ImageAnalysis()
Bases: `object`


#### find_image(input_image, test_type)

* Finds the input image in UI


* Keyword Usage:

> 
> * `Find Image    ${input_image}    ${test_type}`


* **Parameters**

    
    * **input_image** – .png image to find


    * **test_type** – test_type of image



* **Returns**

    None


## extauto.common.ImageHandler module


### _class_ extauto.common.ImageHandler.ImageHandler()
Bases: `object`


#### click_image(target_icon)

* Clicks on input image


#### get_position(target_icon)

* Gets the position of image

## extauto.common.Internal_api module


### _class_ extauto.common.Internal_api.Internal_api()
Bases: `object`


#### generate_access_token(username, password, path='login')

* This Keyword is used to get the access token


* **Parameters**

    
    * **username** – username


    * **password** – password


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### get_json_val(json_data, json_key, key_type='default')

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **key_type** – optional index of the array



* **Returns**

    value



#### get_json_value(json_data, json_key, key_type='default')

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **index** – optional index of the array



* **Returns**

    value



#### get_json_value_as_string(json_data)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data from the API call to get the device ids


    * **device_mac** – mac of the device to match the dict


    * **key_str** – key string to get the value



* **Returns**

    key_str value



#### get_json_values(json_data, json_key)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **index** – optional index of the array



* **Returns**

    value



#### rest_api_get(path, base_url='', access_token='default', csrf_token='')

* This Keyword is used to get the access token


* **Parameters**

    
    * **access_token** – access token


    * **csrf_token** – csrf-token


    * **path** – API Endpoint path


    * **base_url** – Base URL if not using the default



* **Returns**

    returns access_token



#### rest_api_post(path, post_data, access_token='default', return_output='default', result_code='default', role='default')
## extauto.common.JsonUtils module


### _class_ extauto.common.JsonUtils.JsonUtils()
Bases: `object`


#### get_json_val(json_data, json_key, key_type='default')

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **key_type** – optional index of the array



* **Returns**

    value



#### get_json_value(json_data, json_key, key_type='default')

* This Keyword gets the key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **index** – optional index of the array



* **Returns**

    value



#### get_json_value_as_string(json_data)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data from the API call to get the device ids


    * **device_mac** – mac of the device to match the dict


    * **key_str** – key string to get the value



* **Returns**

    key_str value



#### get_json_values(json_data, json_key)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **index** – optional index of the array



* **Returns**

    value


## extauto.common.LoadBrowser module


### _class_ extauto.common.LoadBrowser.LoadBrowser()
Bases: `object`


#### load_browser(url, remote_host=None)

#### quite_approve_browser()
## extauto.common.Logging module


### _class_ extauto.common.Logging.Logging()
Bases: `object`


#### get_logger()

#### log(message)

#### set_log_level()
## extauto.common.Mu module


### _class_ extauto.common.Mu.Mu()
Bases: `object`


#### associate_mu(mu_spawn, interface, ssid_name, ip_address='default', retries=3)

* **Parameters**

    
    * **mu_spawn** – 


    * **interface** – 


    * **ssid_name** – 


    * **ip_address** – 


    * **retries** – 



* **Returns**

    


#### associate_mu_to_ethport(mu_spawn, wlan_port, eth_port, ip_address='default', retries=3)

* **Parameters**

    
    * **mu_spawn** – 


    * **interface** – 


    * **ssid_name** – 


    * **ip_address** – 


    * **retries** – 



* **Returns**

    


#### connect_mu1_to_psk_network(ssid, psk, ip_address='default')

#### connect_mu1_to_wep_network(ssid, key_type, key, key_index, ip_address='default')

#### connect_mu5_to_open_network(ssid, ip_address='default')

* This keyword used to connect MU5 to open network


* Keyword Usage:

> 
> * `Connect MU5 To Open Network    ${SSID_NAME}`


* **Parameters**

    **ssid** – ssid name



* **Returns**

    cli ping from spawn.



#### get_mu_test_ip(mu_spawn, interface)

#### get_testip_mu1(wlan_port, eth_port, ip_address='default', retries=3)

* **Parameters**

    
    * **mu_spawn** – 


    * **interface** – 


    * **ssid_name** – 


    * **ip_address** – 


    * **retries** – 



* **Returns**

    


#### mu_interface_down(mu_spawn, interface)

* This keyword used to bring down MU interface


* Keyword Usage:

> 
> * `MU Interface Down      ${MU5_SPAWN}      ${MU5_INTERFACE}`


* **Parameters**

    
    * **mu_spawn** – MU5 spawn


    * **interface** – MU5 interface



* **Returns**

    


#### mu_reboot(mu_ip, mu_port, mu_username, mu_password, mu_platform)

#### reload_mu(spawn)

* **Parameters**

    **spawn** – 



* **Returns**

    


#### start_wpa_supplicant(mu_spawn, _interface, encryption_type, key_type='ascii', ip_address='default')

* **Parameters**

    
    * **mu_spawn** – 


    * **_interface** – 


    * **encryption_type** – 


    * **key_type** – 


    * **ip_address** – 



* **Returns**

    

## extauto.common.Rest module


### _class_ extauto.common.Rest.Rest()
Bases: `object`


#### curl_command(_url)

#### generate_access_token(auth_code, client_secret, client_id, redirect_uri)

* This Keyword is used to get the access token


* **Parameters**

    
    * **auth_code** – 


    * **client_secret** – client secret key


    * **client_id** – client id


    * **redirect_uri** – redirect url



* **Returns**

    return json result



#### generate_auth_code(gdc_url, client_id, username, password)

#### get_data_from_api_resp(json_data, device_mac, key_str)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data from the API call to get the device ids


    * **device_mac** – mac of the device to match the dict


    * **key_str** – key string to get the value



* **Returns**

    key_str value



#### get_json_value(json_data, json_key)

#### get_json_value_recursive(json_data, json_key)

#### get_location_id_from_api_resp(json_data)

* This Keyword is used to get the  location id from api response json raw data


* **Parameters**

    **json_data** – raw json data from the API call to get the device ids



* **Returns**

    location id



#### get_presence_of_client_from_api_response(json_data, client_mac, key_str)

* This method is used to get the client information from the raw json data


* Client Mac is required to match the particular clients dict in the json resopnse


* Keyword Usage:

> 
> * `Get Presence Of Client From Api Response  ${JSON_DATA}   ${CLIENT_MAC}   clientMacAddress`


> * `Get Presence Of Client From Api Response  ${JSON_DATA}   ${CLIENT_MAC}   associated`


> * `Get Presence Of Client From Api Response  ${JSON_DATA}   ${CLIENT_MAC}   engaged`


* **Parameters**

    
    * **json_data** – 


    * **client_mac** – 


    * **key_str** – 



* **Returns**

    key corresponding value



#### get_value_from_gen_access_token_resp(json_data, owner_id, key)

* This method is used to get the key value from generated access token response


* **Parameters**

    
    * **json_data** – raw json data


    * **owner_id** – owner id to get the data



* **Returns**

    


#### xapi_get_method(url_path, client_secret, client_id, access_token)

* This keyword is used to request the REST AIP GET Call


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> XAPI Get Method  ${URL_PATH}   ${CLIENT_SECRET}   ${CLIENT_ID}   ${ACCESS_TOKEN}


* **Parameters**

    
    * **url_path** – Complete url path


    * **client_secret** – client secret


    * **client_id** – client id


    * **access_token** – access token



* **Returns**

    json response


## extauto.common.SNMPTraps module


### _class_ extauto.common.SNMPTraps.SNMPTraps()
Bases: `object`


#### start_snmp_traps(spawn)

#### start_snmp_traps_with_custom_port(spawn)

#### validate_snmp_trap_messages(spawn, trap_string)
## extauto.common.Screen module


### _class_ extauto.common.Screen.Screen()
Bases: `object`


#### add_screen_shot_to_allure(file_name, driver)

#### save_element_screen_shot(element)

#### save_element_screen_shot64()

#### save_screen_shot(_driver=None)

#### take_screen_shot(_driver=None)
## extauto.common.ScreenDiff module


### _class_ extauto.common.ScreenDiff.ScreenDiff()
Bases: `object`


#### compare_images(input_image1, input_image2, threshold='default')

* **Parameters**

    
    * **input_image** – 


    * **threshold** – 



* **Returns**

    


#### compare_screens(input_image, scale=False, threshold='default')

* **Parameters**

    
    * **input_image** – Input image to compare


    * **threshold** – Threshold limit for comparison


    * **scale** – scales the images



* **Returns**

    appends the images and diff in robot result log file


## extauto.common.Syslog module


### _class_ extauto.common.Syslog.Syslog()
Bases: `object`


#### start_syslog(password)
Starting syslog on script host


#### stop_syslog(password)
stop syslog on script host

## extauto.common.TestFlow module


### _class_ extauto.common.TestFlow.TestFlow()
Bases: `object`


#### Run_Again_If_Keyword_Fails(cmd, \*pars)

* Executes the failed command n times.


* Keyword Usage:

> 
> * `Run Again If Keyword Fails     ${CMD}       ${PARAMETERS}`


* **Parameters**

    
    * **cmd** – Command to be executed


    * **pars** – Parameters to be passed for command



* **Returns**

    Command execution status



#### depends_on(\*search_test_dependency)

* Current test execution depends on status of test[s] passed as arguments.


* If test case in the list fails, the current test case will be skipped else continues.


* Keyword Usage Example:

> 
> * `Depends On     test1       test2`


* **Parameters**

    **search_test_dependency** – list of test cases that current test depends upon



* **Returns**

    list of failed test cases



#### search_failed_test_case_dependency(prev_test_status, list_failed_test, prev_testname, \*search_test_dependency)

* It takes list of dependent tests and previous test execution status as arguments.


* If test fails, failed_list gets appended with test case name.


* Keyword Usage:

> 
> * 

> ```
> ``
> ```

> Search Failed Test Case Dependency      ${test_status}    ${failed_list}   ${prev_testname}   ${tests} \`\`


* **Parameters**

    
    * **search_test_dependency** – list of dependent test cases that current test depends upon


    * **prev_test_status** – previous test case execution status


    * **list_failed_test** – list of failed tests


    * **prev_testname** – previous test case name



* **Returns**

    list of failed test cases


## extauto.common.Tshark module


### _class_ extauto.common.Tshark.Tshark()
Bases: `object`


#### tshark_capture(spawn, wlan_int, ch_num, bssid, count=1000)

* **Parameters**

    
    * **spawn** – 


    * **wlan_int** – 
    * **param ch_num**



    * **param bssid**




    * **count** – 



* **Returns**

    

## extauto.common.Utils module


### _class_ extauto.common.Utils.Utils()
Bases: `object`


#### check_match(target_string, match)

* Check the match string in the target string


* Keyword Usage:

> 
> * `Check Match  ${TARGET_STRING}   ${MATHC}`


* **Parameters**

    
    * **target_string** – target string


    * **match** – search string in the target string



* **Returns**

    1 if match string in target string else -1



#### compare_date_time_strings(str1, str2)

#### convert_MAC_to_lower(mac)

#### convert_MAC_to_upper(mac)

#### convert_mac_to_random_case(mac)

#### convert_ms_to_time(milliseconds)

#### convert_string_to_date(str, pattern='(\\\\d+)')
This function covets a string into a date
:param str: The date as string
:param pattern: A Regex which match the date
:return:


#### convert_time_to_24_hours_format(_time)

* This method expects time format as HH:MM AM or HH:MM PM


* Converts it in to 24 Hour time format


* **Parameters**

    **_time** – 



* **Returns**

    


#### convert_time_to_milliseconds(time_str)

* This keyword converts given time to milliseconds.


* Keyword Usage:


* \`\` Convert Time To Milliseconds 12:03:47\`\`


* In above case it returns value as 43427000


* **Parameters**

    **time_str** – time should be of format : %H:%M:%S



* **Returns**

    time in milliseconds



#### count_down_in_minutes(t)

* Countdown in minutes


* **Parameters**

    **t** – time to count down



* **Returns**

    None



#### date_time_addition(date_time=None, days=None, hours=None, minutes=None, seconds=None)

* This keyword is used to add days/hours/minutes/seconds to the date-time  which is passed as argument.


* Keyword Usage:

> 
> * \`\` Date Time Addition  date_time=2020-10-20 12:03:47    days=5     hours=13    minutes=4      seconds=2\`\`


* **Parameters**

    
    * **date_time** – date and time should be of format : %Y-%m-%d %H:%M:%S


    * **days** – Number of days to be added.


    * **hours** – Number of hours to be added.


    * **minutes** – Number of minutes to be added.


    * **seconds** – Number of seconds to be added.



* **Returns**

    returns the modified date and time of format : %Y-%m-%d %H:%M:%S



#### decode_to_ascii(_str)

* decode given string to ascci


* Keyword Usage:

> 
> * `Decode To Ascii   ${STR}`


* **Parameters**

    **_str** – str to decode to ascci



* **Returns**

    decoded string



#### expand_port_range(port_range)
Take a port_range string of form ‘1-3,5,10,12-15’ and return list of individual ports
as shown here [1,2,3,5,10,12,13,14,15]
:param port_range:
:return:


#### get_config_value(conf_str)

* Get the config value of a variable


* Keyword Usage:

> 
> * `Get Config Value   VARIABLE`


* **Parameters**

    **conf_str** – Variable name



* **Returns**

    value of the variable



#### get_current_date()
Get current date with %Y-%m-%d format
:return: date


#### get_current_date_time(time_format='%Y-%m-%d %H:%M')

* Get current date with %Y-%m-%d %H:%M format


* **Parameters**

    **time_format** – default time format



* **Returns**

    current date with %Y-%m-%d %H:%M format



#### get_current_time()

* Get the Current Time


* Keyword Usage:

> 
> * `Get Current Time`


* **Returns**

    current time



#### get_current_time_in_milliseconds()

* This keyword is used to get the current time in milliseconds.


* Keyword Usage:


* \`\` Get Current Time In Milliseconds\`\`


* **Returns**

    time in milliseconds



#### get_current_time_in_sec()

* Get the Current Time in Sec


* Keyword Usage:


* `Get Current Time In Sec`


* **Returns**

    current time in sec



#### get_device_date(output, separator='/')

* Gets the device date from the CLI output of a DUT


* Keyword Usage:

> 
> * `Get Device Date       ${CLI_OUTPUT}`


* **Parameters**

    
    * **output** – 


    * **separator** – can be / or -



* **Returns**

    returns a date in mm/dd/yyyy or mm-dd-yyyy format



#### get_device_time(output)

* Gets the device time from the CLI output of a DUT


* Keyword Usage:

> 
> * `Get Device Time        ${CLI_OUTPUT}`


* **Returns**

    device time in hh:mm format



#### get_first_half_of_mac(mac)

* This keyword returns the first half of a MAC


* **Parameters**

    **mac** – MAC



* **Returns**

    returns first half of MAC



#### get_first_half_of_network_policy(network_policy)

* This keyword returns the first half of a Network Policy


* **Parameters**

    **network_policy** – network_policy



* **Returns**

    returns first half of MAC



#### get_half_of(_time)

* This method accepts time in minutes divides by 2 and returns the value


* **Parameters**

    **_time** – in minutes



* **Returns**

    


#### get_last_6_digts_of_MAC(mac)

#### get_min(\*args)

* used to find min(v1,v2,…)


#### get_previous_time_delta(t1, hour=None, minutes=None, time_format='%Y-%m-%d %H:%M')

* Get last specified time delta


* Example:

> 
> * if  t1=’2020-05-19 03:57’  last_24_hour_time=’’2020-05-18 03:57’’


* **Parameters**

    
    * **t1** – present time


    * **hour** – time in hour to get the previous time


    * **minutes** – time in Minutes to get the previous time


    * **time_format** – specify the time format



* **Returns**

    time delta



#### get_random_integer(length=10, lower_limit=9999, upper_limit=999999999)

* Get the random integer in specified upper and lower limit


* Keyword Usage:

> 
> * `Get Random Integer`


* **Parameters**

    
    * **length** – len of integer


    * **lower_limit** – lower limit to generate the integer


    * **upper_limit** – upper limit to generate the integer



* **Returns**

    generated random integer



#### get_random_ip()

* Generate the random ip address


* Keyword Usage:

> 
> * `Get Random Ip`


* **Returns**

    generated random ip address



#### get_random_mac(delimiter='default')

* Get the random mac


* By default it will generate mac in the format aa:bb:11:22:33:44


* Keyword Usage:

> 
> * `Get Random Mac`


> * `Get Random Mac   delimiter=:`


* **Parameters**

    **delimiter** – specify the delimiter ex  “-”, “:”



* **Returns**

    generated mac



#### get_random_string(length='default')

* Get the random string of specified length, default length is 10 characters


* Keyword Usage:

> 
> * `Get Random String`


> * `Get Random String   length=5`


* **Parameters**

    **length** – length of the character to generate



* **Returns**

    generated random string



#### get_regexp_matches(string, pattern, \*groups)
Returns a list of all non-overlapping matches in the given string.

`string` is the string to find matches from and `pattern` is the
regular expression. See BuiltIn.Should Match Regexp for more
information about Python regular expression syntax in general and how
to use it in Robot Framework test data in particular.

If no groups are used, the returned list contains full matches. If one
group is used, the list contains only contents of that group. If
multiple groups are used, the list contains tuples that contain
individual group contents. All groups can be given as indexes (starting
from 1) and named groups also as names.

Examples:
| ${no match} =    | Get Regexp Matches | the string | xxx     |
| ${matches} =     | Get Regexp Matches | the string | t..     |
| ${one group} =   | Get Regexp Matches | the string | t(..)   | 1 |
| ${named group} = | Get Regexp Matches | the string | t(?P<name>..) | name |
| ${two groups} =  | Get Regexp Matches | the string | t(.)(.) | 1 | 2 |
=>
| ${no match} = []
| ${matches} = [‘the’, ‘tri’]
| ${one group} = [‘he’, ‘ri’]
| ${named group} = [‘he’, ‘ri’]
| ${two groups} = [(‘h’, ‘e’), (‘r’, ‘i’)]


#### get_second_half_of_MAC(mac)

#### get_second_half_of_network_policy(net)

#### get_time_difference_in_milliseconds(time1, time2)

* This keyword is used to get the time difference in milliseconds.


* Keyword Usage:


* \`\` Get Time Difference In Milliseconds  1622696034870  24:03:47\`\`


* **Parameters**

    
    * **time1** – Timestamp in milliseconds


    * **time2** – Time in format : %H:%M:%S and should be greater than 24 hours



* **Returns**

    time in milliseconds



#### get_utc_hour_time_delta(utc_time, hour=24)

* Get the utc time after the specified time delta in hour


* Example:

> 
> * if utc time is:         utc_time        = 2020-04-24 03:12:04.905116


> * utc time after delta    utc_after_10min = 2020-04-25 03:12:04.905116


* **Parameters**

    
    * **utc_time** – 


    * **hour** – 



* **Returns**

    Time %Y-%m-%d %H:%M format



#### get_utc_iso_time_format()

* This keyword is used to get the time in ISO Format


* **Returns**

    ISO time now



#### get_utc_minute_time_delta(utc_time, minutes=10)

* Get the utc time after the specified time delta in minutes


* Example:

> 
> * if utc time :           utc_time        = 2020-04-24 03:12:04.905116


> * utc time after delta    utc_after_10min = 2020-04-24 03:23:09.519271


* **Parameters**

    
    * **utc_time** – 


    * **minutes** – 



* **Returns**

    Time %Y-%m-%d %H:%M format



#### get_utc_time(time_format=None)

* Get the utc time with specified time format, by default %Y-%m-%d %H:%M.%s


* **Parameters**

    **time_format** – specify the time format



* **Returns**

    utc time



#### get_utc_time_difference(t1, t2)

* Get the time difference between t2 and t1


* Keyword Usage:

> 
> * `Get Utc Time Difference   ${TIME1}  ${TIME2}`


* **Parameters**

    
    * **t1** – datetime.datetime object


    * **t2** – datetime.datetime object



* **Returns**

    time difference of t2 and t1 in minutes



#### grep(output_buffer, search_str)

* greps the second variable in the first string


* Keyword Usage:

> 
> * `Grep   ${OUTPUT}     Version`


* **Parameters**

    
    * **output_buffer** – Buffer in which we grep for search_str


    * **search_str** – search string which will be looked inside output_buffer for a match



* **Returns**

    returns 1 if finds a match else 0



#### has_number(input_string)

* check the input string has the digit on it


* Keyword Usage:

> 
> * `Has Number  ${INPUT_STRING}`


* **Parameters**

    **input_string** – 



* **Returns**

    True if digit in input string else False



#### include_image(file_name)

* includes the image in robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### log_to_report(file_name)

* logs a video file in robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### look_and_feel(first, second, third)

* embeds 3 png files in to robot framework output log.html file side by side


* Keyword Usage:

> 
> * `Look and Feel   Screen1.png     Screen2.png    Screen3.png`


* **Parameters**

    
    * **first** – screenshot or image 1


    * **second** – screenshot or image 2


    * **third** – screenshot or image 3



* **Returns**

    returns none



#### partial_ip(ip)

#### print_debug(\*words)

* prints the given list of words in to console and robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### print_error(\*words)

* prints the given list of words in to console and robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### print_info(\*words)

* prints the given list of words in to console and robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### print_log(\*words)

* prints the given list of words in to console and robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### print_warning(\*words)

* prints the given list of words in to console and robot framework log.html file


* Note this is not a keyword to use inside the robot framework script. only used in libs


#### round_time(upgrade_time)

* This method expects time format as 24 Hours


* Converts it in to AM or PM


* This is specific to XIQ UI behavior


* **Parameters**

    **upgrade_time** – 



* **Returns**

    


#### special_char_check(_str)

* check the special character in the given string


* Keyword Usage:

> 
> * `Special CHar Check   ${STR}`


* **Parameters**

    **_str** – str to check the special character



* **Returns**

    0 if special character exists else 1



#### split_string_into_3_parts(info)

* This keyword splits a string in to 3 equal parts


* **Parameters**

    **info** – input string



* **Returns**

    returns 3 strings by dividing the input string



#### switch_to_default(driver)
-This keyword Will Switch to default frame


#### switch_to_iframe(driver)
-This keyword Will Switch to iframe


#### switch_to_iframe_n(driver, iframe_num)

#### switch_to_iframe_with_attr(driver, attr)

#### wait_till(func=None, fail_func=None, timeout=20, delay=0.2, exp_func_resp=True, is_logging_enabled=False, silent_failure=False, custom_response=[], msg=None)
wait till method returns the func() response and raise Timeout Exception if timedout

    :param func              : callable function without arguments
    :param fail_func         : callable function, to be run after every unsuccessful attempt of func
    :param timeout           : float/int type , max number of seconds to wait before timed out
    :param delay             : float/int, delay in seconds between each retry
    :param exp_func_resp     : bool,by default wait_till expects True from the callback function func
    :pram is_logging_enabled : bool, prints the time remaining and result of the func function, default disabled
    :pram silent_failure     : bool, if true nothing will be returned and Timeout exceptions will not be raised.
    :pram custom_response    : list, should contain list of str values to match against the func() response. e.g [“Green”, “connected”, “MANAGED”]
    :param msg               : str, message that has to printed when this wait_till function is called.
    :return: raise timeout exception incase max timed out else resturns the calback function’s response

usages:

    self.utils.wait_till()
    self.utils.wait_till(_check_device_rows)
    self.utils.wait_till(_check_device_rows, timeout=5, delay=0.25)
    self.utils.wait_till(_check_device_rows, _click_eligible, is_logging_enabled=True, silent_failure=False)
    out, et = self.tools.wait_till(_check_device_rows, exp_func_resp=False, silent_failure=False, custom_response=[“Green”, “Managed”])

Note:

    
    1. custom_response has higher priority than the exp_func_resp


    2. Timeout might not the break point, callback func and fail_func might take sometime


    3. If no arguments passed then it will act like a sleep(timeout) and returns None.


    4. Calback func() response and the Execution Time are returned as tuple.

        e.g
        out,et = wait_till(_check_device_rows, _click_eligible, is_logging_enabled=True, silent_failure=False))
        out = func() response
        et  = Execution time (HH:MM:SS)

## extauto.common.WebElementHandler module


### _class_ extauto.common.WebElementHandler.WebElementHandler()
Bases: `object`


#### check_for_page_is_loading(driver)

#### get_a_href(element)

#### get_displayed_element(elements)
From the list of elements get the displayed element on web page
:param elements: (list)  list of elements
:return: (obj) displayed element


#### get_element(key_val, parent='default')
get the web element based on the locators provided in key_val dictionary
:param key_val: (dict) containing the locator:value ex: ‘CSS_SELECTOR’: ‘.btn.btn-primary-2.btn-dim’
:param parent: (str)
:return:(obj) web elements obj


#### get_elements(key_val, parent='default')
Get the web elements
:param key_val: (dict) containing the locator:value ex: ‘CSS_SELECTOR’: ‘.btn.btn-primary-2.btn-dim’
:param parent: (str) driver object
:return:(obj) web elements obj


#### get_template_element(key_val_template, parent='default', \*\*kwargs)
Get element based on key, value pairs defined in key_val_template dictionary.
Replaces kwarg names enclosed in ${} with kwarg values in each string
value defined in the key_val_template dictionary.
For example,

> Suppose the following key value dictionary definition
> template_example =                 {

> > > ‘DESC’: ‘This finds a panel with title=”${title}”’,
> > > ‘XPATH’: ‘//div[contains(@id, “panel-title”) and text()=”${title}”]’,

> > }

> self.weh.get_template_element(template_example, title=”Devices”)
> self.weh.get_template_element(template_example, title=”Policy”)


* **Parameters**

    
    * **key_val_template** – (dict) containing the locator:value ex: ‘CSS_SELECTOR’: ‘.btn.btn-primary-2.btn-dim’


    * **parent** – (str)


    * **kwargs** – (dict) containing key value pairs to replace in key_val_template string values



#### get_template_elements(key_val_template, parent='default', \*\*kwargs)
Get elements based on key, value pairs defined in key_val_template dictionary.
Replaces kwarg names enclosed in ${} with kwarg values in each string
value defined in the key_val_template dictionary.
For example,

> Suppose the following key value dictionary definition:
> list_dropdown_items =             {

> > ‘DESC’: ‘Drop down items for a list type dropdown (li)’,
> > ‘XPATH’: ‘//div[contains(@id, “${element_id}”) and contains(@id, “-picker-listWrap”)]/ul/li’,

> }
> You would then get the elements by passing in the element ID:
> self.weh.get_template_elements(list_dropdown_items, element_id=”combo-id”)


* **Parameters**

    
    * **key_val_template** – (dict) containing the locator:value ex: ‘CSS_SELECTOR’: ‘.btn.btn-primary-2.btn-dim’


    * **parent** – (str)


    * **kwargs** – (dict) containing key value pairs to replace in key_val_template string values


## extauto.common.WindowsMU module


### _class_ extauto.common.WindowsMU.WindowsMU()
Bases: `object`


#### connect_window_mu_to_wifi(spawn, ssid, user_name=None, password=None, profile=None, default_spawn='ssh')

* This keyword is used to connect a window platform MU to a wifi


* Keyword Usage:

> 
> * `Connect Window MU To Wifi     ${spawn}      ${ssid}`


* **Parameters**

    
    * **spawn** – spawn, ssh by default


    * **ssid** – SSID name


:param user_name:string | wifi user name
:param password:string | wifi user password
:return: Command execution status
@todo: connect wifi with username/password or profile


#### disconnect_windown_mu_wifi(spawn, default_spawn='ssh')
This keyword Disconnects a window platform MU from wifi
- Keyword Usage:

> 
> * `Disconnect Windown MU Wifi  ${spawn}`


* **Parameters**

    **spawn** – spawn by default ssh



* **Returns**

    1 if success


## extauto.common.WingAP module


### _class_ extauto.common.WingAP.WingAP()
Bases: `object`


#### associate_ap(ap_spawn, retries=2)

* **Parameters**

    
    * **ap_spawn** – 


    * **retries** – 



* **Returns**

    


#### factory_rest_wing_ap(ip, port)

* This Keyword is used to reset wing ap to factory defaults


* **Parameters**

    
    * **ip** – Wing AP IP


    * **port** – Console port of AP



* **Returns**

    returns 1 if success



#### reload_wing_ap(spawn)

* This Keyword is used to reload wing ap


* **Parameters**

    **spawn** – Wing AP SPAWN



* **Returns**

    returns 1 if success


## extauto.common.XAPIRequests module


### _class_ extauto.common.XAPIRequests.RestRequest()
Bases: `object`


#### generate_access_token(username, password, path='login')

* This Keyword is used to get the access token


* **Parameters**

    
    * **username** – username


    * **password** – password


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### rest_api_get(path, access_token='default')

* This Keyword is used to get the access token


* **Parameters**

    
    * **access_token** – access token


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### rest_api_post(path, post_data, access_token='default', return_output='default', result_code='default', role='default')

* This Keyword is used for REST API post


* **Parameters**

    
    * **path** – URL Path


    * **post_data** – data to post


    * **access_token** – access token



* **Returns**

    returns output


## extauto.common.XAPISwitch module


### _class_ extauto.common.XAPISwitch.XAPISwitch()
Bases: `object`


#### ExtractResponseCode(response, deviceIDList)

* **Parameters**

    
    * **response** – The URL response recieved


    * **deviceIDList** – The device ID



* **Returns**

    The response code for the CLI response



#### buildCLICommandSet()
Initiates the CLICommand dictionary with the list of commands for all the supported modules
:return:None


#### extract_by_device_mac(deviceList, deviceMac)

* **Parameters**

    
    * **deviceList** – List of devices


    * **deviceMac** – Mac Address to be searched for



* **Returns**

    Device ID of the device



#### extract_by_device_serial(deviceList, deviceSerial)

* **Parameters**

    
    * **deviceList** – List of devices


    * **deviceSerial** – Serial # to be searched for



* **Returns**

    Device ID of the device



#### extract_by_device_type(deviceList, device_type='EXOS', device_model='5520', stack_mac='null')

* The keyword is used to extract a device ID of the specified type from the List


* **Parameters**

    
    * **deviceList** – 
        * List of all devices



    * **device_type** – 
        * Type of device needed

    EXOS - 5520 , 5420 EXOS devices
    VOSS - 5520 , 5420 VOSS devices
    Stack - 5520 , 5420 in homogeneous stacks ( only EXOS)



:param device_model : - Model of the universal hardware to be searched for
:return:   - ID of the requested device


#### sendCLI_device_endpoint(deviceID, CLIList)

* **Parameters**

    
    * **deviceID** – The list of Devices for which the Request is to be sent


    * **CLIList** – List of CLI commands to be sent



* **Returns**

    1 for SUCCESS -1 for FAILURE



#### sendCLI_module_device_endpoint(deviceID, Module, NOS)

* **Parameters**

    
    * **deviceID** – ID of device that the CLI is to be sent to


    * **Module** – THe module for which the CLIs are to be sent


    * **NOS** – EXOS/VOSS



* **Returns**

    1 for SUCCESS -1 for FAILURE



#### sendCLI_module_multiple_devices(deviceIDList, Module, NOS)

* **Parameters**

    
    * **deviceIDList** – List of devices that the CLI is to be sent to


    * **Module** – THe module for which the CLIs are to be sent


    * **NOS** – EXOS/VOSS



* **Returns**

    1 for SUCCESS -1 for FAILURE



#### sendCLI_multiple_devices(URLpath, deviceIDList, CLIList)
:param URLpath  :   The endpoint for the XAPI Request
:param deviceIDList:  The list of Devices for which the Request is to be sent
:param CLIList: List of CLI commands to be sent
:return: 1 for SUCCESS -1 for FAILURE

## extauto.common.Xapi module


### _class_ extauto.common.Xapi.Xapi()
Bases: `object`


#### find_nth_occurrence_index(source, search, position)

#### generate_access_token(username, password, path='login')

* This Keyword is used to get the access token


* **Parameters**

    
    * **username** – username


    * **password** – password


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### get_http_response_code(curl_command_std_err_message)

#### get_index_connected_status_from_list_json(json_data, index)

* This Keyword is used to get the specific connected status of the device for the specified index of list json


* **Parameters**

    
    * **json_data** – the list of json data


    * **index** – the index of list



* **Returns**

    returns id



#### get_index_device_admin_state_from_list_json(json_data, index)

* This Keyword is used to get the specific device admin state for the specified index of list json


* **Parameters**

    
    * **json_data** – the list of json data


    * **index** – the index of list



* **Returns**

    returns id



#### get_index_id_from_list_json(json_data, index)

* This Keyword is used to get the specific id for the specified index of list json


* **Parameters**

    
    * **json_data** – the list of json data


    * **index** – the index of list



* **Returns**

    returns id



#### get_index_nw_policy_name_from_list_json(json_data, index)

* This Keyword is used to get the specific network policy name for the specified index of list json


* **Parameters**

    
    * **json_data** – the list of json data


    * **index** – the index of list



* **Returns**

    returns id



#### get_json_val(json_data, json_key, key_type='default')

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **key_type** – optional index of the array



* **Returns**

    value



#### get_json_value(json_data, json_key, key_type='default')

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key


    * **key_type** – index or



* **Returns**

    value



#### get_json_value_as_string(json_data)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    **json_data** – raw json data from the API call to get the device ids



* **Returns**

    key_str value



#### get_json_value_from_list_json(required_key, json_data, key_val)

#### get_json_values(json_data, json_key)

* This Keyword is used to get the  key_str value from the api response json raw data


* **Parameters**

    
    * **json_data** – raw json data


    * **json_key** – json key



* **Returns**

    returns value



#### get_json_values_for(required_key, json_data, key_val)

#### get_random_id_from_list_json(json_data)

#### rest_api_delete(path, delete_data='default', access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_delete_v1(path, delete_data='default', access_token='default', return_output='default', role='default')

#### rest_api_delete_v2(path, delete_data, access_token='default', return_output='default', role='default')

#### rest_api_get(path, access_token='default')

* This Keyword is used to get the access token


* **Parameters**

    
    * **access_token** – access token


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### rest_api_get_v1(path, access_token='default')

* This Keyword is used to get the access token


* **Parameters**

    
    * **access_token** – access token


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### rest_api_get_v2(path, access_token='default')

* This Keyword is used to get the access token


* **Parameters**

    
    * **access_token** – access token


    * **path** – API Endpoint path



* **Returns**

    returns access_token



#### rest_api_patch(path, patch_data='default', access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_post(path, post_data='default', access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_post_v1(path, post_data, access_token='default', return_output='default', role='default')

#### rest_api_post_v2(path, post_data, access_token='default', return_output='default', role='default')

#### rest_api_post_v3(path, post_data='default', access_token='default', return_output='default', result_code='default', role='default')

* This Keyword is used to post the API request evaluating the httpCode


#### rest_api_post_with_file(path, file_path, access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_post_with_no_file(path, access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_put(path, put_data='default', access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_put_v1(path, put_data='default', access_token='default', return_output='default', result_code='default', role='default')

#### rest_api_put_v3(path, put_data='default', access_token='default', return_output='default', result_code='default', role='default')

* This Keyword is used to run the update API request evaluating the httpCode


### extauto.common.Xapi.extract_connected_status_from_json(json_values)

### extauto.common.Xapi.extract_device_admin_state_from_json(json_values)

### extauto.common.Xapi.extract_id_from_json(json_values)

### extauto.common.Xapi.extract_nw_policy_name_from_json(json_values)
## extauto.common.switchAPI module


### _class_ extauto.common.switchAPI.Switchapi(baseurl='/rest/restconf/data/', timeout=30, username='admin', password='')
Bases: `object`


#### switch_restconf(nos: str, dutip: str, resourceurl: str, method: str, data: <module 'json' from '/usr/lib/python3.8/json/__init__.py'> = '')
A bridge between EXOS and VOSS Rest conf
:param nos: exos or voss
:param dutip: IP of DUT
:param resourceurl: Resource URL to perform Rest operation
:param method: POST/GET/PATCH/DELETE supported
:param data: For POST and PATCH - data in json format
:return:

## Module contents
