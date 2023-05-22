# Author        : Madhavi Shrotri
# Date          : May 27 2020
# Description   : Basic Login Test Cases
# Edited by     :
#
# Topology      :
# Host ----- Cloud


*** Variables ***
${WEB_DRIVER_LOC}           local
${TENANT_USERNAME}          admin@cust001.com
${TENANT_PASSWORD}          aerohive
${TEST_URL}                 https://10.16.118.155
${BASE_URL}                 https://10.16.118.155
${BROWSER}                  chrome
${GETPATH}                  acct-webapp/oauth/cookietoken

*** Settings ***
Library     common/Screen.py
#Library     xiq/flows/common/Login.py
Library     keywords/gui/login/KeywordsLogin.py
Library     xiq/flows/manage/Devices.py
Library     common/Internal_api.py
Library     common/Utils.py
Library     common/TestFlow.py

#*** Keywords ***
## generate the key once per suite
#Pre Condition
#    [Documentation]   Get internal API access token
#    ${ACCESS_TOKEN}, ${CSRF_TOKEN} =        generate_access_token    ${TENANT_USERNAME}      ${TENANT_PASSWORD}      acct-webapp/oauth/cookietoken
#    set global variable     ${ACCESS_TOKEN}
#    Log                     ${ACCESS_TOKEN}

*** Test Cases ***
Verify Getting Access Token and device list

    [Documentation]   Get internal API access token
    ${ACCESS_TOKEN_LIST} =        generate_access_token    ${TENANT_USERNAME}      ${TENANT_PASSWORD}      ${GETPATH}
#    set global variable     ${ACCESS_TOKEN}
    Log                     ${ACCESS_TOKEN_LIST}
    ${output}=              rest api get             /acct-webapp/services/acct/selectvhm           access_token=${ACCESS_TOKEN_LIST[0]}
    Log                     ${output}
#    ${ownerId}=             get json value          ${output}           "ownerId"
#    Log                     ${ownerId}
    ${output2}=             rest api get             /hm-webapp/services/inventory/devices/all?ownerId=102  access_token=${ACCESS_TOKEN_LIST[0]}    csrf_token=${ACCESS_TOKEN_LIST[1]}
    Log                     ${output2}
#Verify Getting Access Token
#    [Documentation]         Check the functionality of getting access token
#    [Tags]                  sanity              login
#    ${result1}=             Login User          ${TENANT_USERNAME}     ${TENANT_PASSWORD}
#    Save Screen shot
#    ${result2}=             Logout User
#
#    Should Be Equal As Strings      '${result1}'     '1'
#    Should Be Equal As Strings      '${result2}'     '1'
#
#    [Teardown]
#    Logout User
#    Quit Browser

