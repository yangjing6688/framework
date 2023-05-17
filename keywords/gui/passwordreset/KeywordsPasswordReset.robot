# Author        : Ramkumar
# Date          : April 9th 2020
# Description   : Password reset Test Cases
#
# Topology:
# ---------
#    ScriptHost
#      |
#      |
#     Cloud
#
# Pre-config:
# -----------
# This test case needs email id: cloud.passreset@gmail.com

# Execution Command:
# ------------------
# robot -v ENV:environment.seleniumhub.docker.chrome.yaml -v TOPO:topo.test.g2r1.yaml GlobalSettings_PasswordReset_XIQ-000.robot

*** Variables ***
${TENANT_NAME}              Cloud_User_Password_Reset
${TENANT_EMAIL_ID}          cloud.passreset@gmail.com
${TENANT_EMAIL_PWD}         jusnmdcwcdxrgmcg
${TENANT_NEW_PWD}           Extreme@123
${NEW_PASSWORD}             Extreme@324
${NEW_PASSWORD_02}          Extreme@12345

*** Settings ***
Library     extauto/common/GmailHandler.py
Library     extauto/common/TestFlow.py

Library     keywords/gui/login/KeywordsLogin.py
Library     keywords/gui/passwordreset/KeywordsPasswordReset.py
Library     extauto/xiq/flows/globalsettings/AccountManagement.py

Variables    Environments/${TOPO}
Variables    Environments/${ENV}
Variables    Environments/Config/waits.yaml

Force Tags  testbed_none

Suite Setup     Test Suite Setup
Suite Teardown    Test Suite Teardown

*** Keywords ***
Test Suite Setup
     Login User                 ${TENANT_USERNAME}          ${TENANT_PASSWORD}
     ${DELETE_ACCOUNT}=         Delete Management Account       ${TENANT_EMAIL_ID}

     [Teardown]   run keywords        Logout User
    ...                               Quit Browser

Test Suite Teardown
     Login User                 ${TENANT_USERNAME}          ${TENANT_PASSWORD}
     ${DELETE_ACCOUNT}=         Delete Management Account       ${TENANT_EMAIL_ID}

    [Teardown]   run keywords         Logout User
    ...                               Quit Browser

*** Test Cases ***
TCCS-8661 : Add a new Account and Setup New Password
    [Documentation]         Add a new Account and Setup New Password
    [Tags]                  regression    tccs-8661

    ${LOGIN_USER}=          Login User          ${TENANT_USERNAME}          ${TENANT_PASSWORD}
    Should Be Equal as Integers     ${LOGIN_USER}      1

    ${ADD_ACCOUNT}=          Add Account         ${TENANT_NAME}          ${TENANT_EMAIL_ID}
    Should Be Equal as Integers     ${ADD_ACCOUNT}      1

    ${LOGOUT_USER}=         logout user
    Should Be Equal as Integers     ${LOGOUT_USER}      1

    Sleep                   ${RECEIVE_MAIL}             Waiting for 30 seconds to get the password set link
    ${PWD_URL}=             Get Link            ${TENANT_EMAIL_ID}      ${TENANT_EMAIL_PWD}
    Should contain any      ${PWD_URL}    passwords     setupverify

    ${DRIVER}=              Load Web Page       url=${PWD_URL}
    ${SETUP_PASSWORD}=             Set Password        ${NEW_PASSWORD}
    Should Be Equal as Integers     ${SETUP_PASSWORD}      1    "Email might have ended up in Spam - please manually login & check"

    Quit Browser

    ${LOGIN_USER}=          Login User          ${TENANT_EMAIL_ID}          ${NEW_PASSWORD}     incognito_mode=True
    Should Be Equal as Integers     ${LOGIN_USER}      1

    ${LOGOUT_USER}=         Logout User
    Should Be Equal as Integers     ${LOGOUT_USER}      1

    [Teardown]   run keywords               Quit Browser


