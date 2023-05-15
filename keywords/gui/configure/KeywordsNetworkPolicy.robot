*** Settings ***
Library    KeywordsNetworkPolicy.py
Library    xiq/flows/common/Login.py
Library    xiq/flows/configure/NetworkPolicy.py
Library    xiq/flows/configure/CommonObjects.py
Library    Collections
Variables    Environments/${TOPO}
Variables    Environments/${ENV}
Variables    TestBeds/${TESTBED}
Suite Setup     Test Suite Setup
Suite Teardown  Test Suite Cleanup

*** Variables ***
${Network_Policy_Prefix}=   Network_Policy_Auto
${Network_Policy_Name_A}=    ${Network_Policy_Prefix}_A

${SSID_Prefix}=     SSID_Auto
${ssid_1_name}=     ${SSID_Prefix}_1
&{ssid_profile}
&{cwp_profile_disable}      enable_cwp=DISABLE
&{auth_profile}=    auth_type=OPEN      cwp_profile=${cwp_profile_disable}
&{wireless_profile}=    ssid_name=${ssid_1_name}    ssid_profile=${ssid_profile}    auth_profile=${auth_profile}

&{SSID_Profile_WiFi_0}=  WIFI0=Enable   WIFI1=Enable	    WIFI2=Enable
&{SSID_Profile_WiFi_1}=  WIFI0=Enable   WIFI1=Enable	    WIFI2=Disable
&{SSID_Profile_WiFi_2}=  WIFI0=Enable   WIFI1=Enable
&{SSID_Profile_WiFi_3}=  WIFI0=Enable   WIFI1=Disable	WIFI2=Enable
&{SSID_Profile_WiFi_4}=  WIFI0=Enable   WIFI1=Disable	WIFI2=Disable
&{SSID_Profile_WiFi_5}=  WIFI0=Enable   WIFI1=Disable
&{SSID_Profile_WiFi_6}=  WIFI0=Disable   WIFI1=Enable	WIFI2=Enable
&{SSID_Profile_WiFi_7}=  WIFI0=Disable   WIFI1=Enable	WIFI2=Disable
&{SSID_Profile_WiFi_8}=  WIFI0=Disable   WIFI1=Enable
&{SSID_Profile_WiFi_9}=  WIFI0=Disable   WIFI1=Disable	WIFI2=Enable
&{SSID_Profile_WiFi_10}=  WIFI0=Disable   WIFI1=Disable	WIFI2=Disable
@{SSID_Profile_WiFis}=   &{SSID_Profile_WiFi_0}   &{SSID_Profile_WiFi_1}    &{SSID_Profile_WiFi_2}  &{SSID_Profile_WiFi_3}  &{SSID_Profile_WiFi_4}  &{SSID_Profile_WiFi_5}  &{SSID_Profile_WiFi_6}  &{SSID_Profile_WiFi_7}  &{SSID_Profile_WiFi_8}  &{SSID_Profile_WiFi_9}  &{SSID_Profile_WiFi_10}

*** Keywords ***
Test Suite Setup
    Login User          ${tenant_username}    ${tenant_password}

Test Suite Cleanup
    Logout User
    Quit Browser

Cleanup Network Policies and SSIDs
    [Arguments]    @{args}
    FOR    ${network_policy_name}   ${ssid_name}    IN ZIP    ${args}[0]    ${args}[1]
        Cleanup Network Policy and SSID     ${network_policy_name}   ${ssid_name}
    END

Cleanup Network Policy and SSID
    [Arguments]    ${network_policy_name}   ${ssid_name}
    Cleanup Network Policy      ${network_policy_name}
    Delete SSID     ${ssid_name}

Cleanup Network Policy
    [Arguments]    ${network_policy_name}

    ${STATUS}=  delete network policy    ${network_policy_name}
    should be equal as strings     '${STATUS}'        '1'

Cleanup Network Policies
    [Arguments]    @{network_policy_names}
    FOR    ${item}    IN    @{network_policy_names}
        ${STATUS}=  delete network policy    ${item}
        should be equal as strings     '${STATUS}'        '1'
    END

*** Test Cases ***
Test Create Network Policy
    [Documentation]  Test Objective: Create Network Policy

    @{ssid_list} =  Create List
    @{name_list} =  Create List

    FOR    ${index}    ${item}    IN ENUMERATE    @{SSID_Profile_WiFis}
        ${ssid_name}=   Set Variable    ${SSID_Prefix}_${index}
        &{ssid_profile}=    Create Dictionary    &{item}
        &{auth_profile}=    Create Dictionary

        ${Status}=    Evaluate    $item.get("WIFI2") == 'Enable'

        IF  ${Status}
            &{auth_profile}=    Create Dictionary   auth_type=ENHANCED
        ELSE
            &{auth_profile}=    Create Dictionary   auth_type=OPEN      cwp_profile=${cwp_profile_disable}
        END

        &{wireless_profile}=    Create Dictionary   ssid_name=${ssid_name}    ssid_profile=${ssid_profile}    auth_profile=${auth_profile}
        Append To List  ${ssid_list}    ${ssid_name}
        Append To List  ${name_list}    ${Network_Policy_Prefix}_${index}
        ${STATUS}=  KeywordsNetworkPolicy.Create Network Policy    ${Network_Policy_Prefix}_${index}     ${wireless_profile}     AH-AP
        should be equal as strings     '${STATUS}'        '1'
    END

    [Teardown]    Cleanup Network Policies and SSIDs    ${name_list}   ${ssid_list}
