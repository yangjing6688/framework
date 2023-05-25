
*** Variables ***
${TENANT_NAME}              Cloud_User_Password_Reset
${TENANT_EMAIL_ID}          cloud.passreset@gmail.com

*** Settings ***
Variables    Environments/${TOPO}
Variables    Environments/${ENV}
Variables    Environments/Config/waits.yaml

Library     keywords/gui/passwordreset/KeywordsPasswordReset.py
Library     keywords/gui/account_management/KeywordsAccountManagement.py
Library     keywords/gui/login/KeywordsLogin.py
Resource    Tests/Robot/Functional/XIQ/Wireless/Extreme_Guest/Resources/variables.robot
Resource    Tests/Robot/Functional/XIQ/Wireless/Extreme_Guest/Resources/extreme_guest_config.robot
Resource    Tests/Robot/Functional/XIQ/Wireless/Extreme_Guest/Resources/email_ids.robot

Suite Setup		Login User 		${TENANT_USERNAME}	${TENANT_PASSWORD}
Suite Teardown	Close Session

*** Test Cases ***

UnitTest-1: Deleting The Management Account

	[Documentation]         Create Management Account and Delete

	${ADD_ACCOUNT}=          Add Account         ${TENANT_NAME}          ${TENANT_EMAIL_ID}
    Should Be Equal as Integers     ${ADD_ACCOUNT}      1
	
	${DELETE_ACCOUNT}=         Delete Management Account       ${TENANT_EMAIL_ID}
     Should Be Equal as Integers     ${DELETE_ACCOUNT}      1


UnitTest-2: Guest Management Role - Adding and deleting multiple users

    [Documentation]         Create Guest Management Role And Delete

    ${CREATE_ACCOUNT}=              Create Role Based Account   ${GUEST_MANAGEMENT_ROLE}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${CREATE_ACCOUNT}=              Create Role Based Account   ${GUEST_MANAGEMENT_ROLE2}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${CREATE_ACCOUNT}=              Create Role Based Account   ${GUEST_MANAGEMENT_ROLE3}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${DELETE_ACCOUNT}=                   Delete Guest Management Accounts
    Should Be Equal As Strings      '${DELETE_ACCOUNT}'     '1'
	

UnitTest-3: Operator Role - Adding and deleting users

    [Documentation]         Create Operator Role And Delete

    ${CREATE_ACCOUNT}=              Create Role Based Account   ${OPERATOR}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'

	${DELETE_ACCOUNT}=         		Delete Management Account       ${USER_EMAIL}
    Should Be Equal as Integers     ${DELETE_ACCOUNT}		1
	
	
UnitTest-4: Monitor Role - Adding and deleting users

    [Documentation]         Create Guest Management Role And Delete

    ${CREATE_ACCOUNT}=              Create Role Based Account   ${GUEST_MANAGEMENT_MONITOR_ROLE}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${DELETE_ACCOUNT}=         		Delete Management Account       ${USER_EMAIL}
    Should Be Equal as Integers     ${DELETE_ACCOUNT}		1
	
UnitTest-5: Help Desk Role - Adding and deleting users

    [Documentation]         Create Help Desk Role And Delete

    ${CREATE_ACCOUNT}=              Create Role Based Account   ${HELP_DESK_ROLE}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${DELETE_ACCOUNT}=         		Delete Management Account       ${USER_EMAIL}
    Should Be Equal as Integers     ${DELETE_ACCOUNT}		1
	
UnitTest-6: Observer Role - Adding and deleting users

    [Documentation]         Create Observer Role And Delete

    ${CREATE_ACCOUNT}=              Create Role Based Account   ${OBSERVER_ROLE}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${DELETE_ACCOUNT}=         		Delete Management Account       ${USER_EMAIL}
    Should Be Equal as Integers     ${DELETE_ACCOUNT}		1
	
 
*** Keywords ***

Close Session
	Logout User
	Quit Browser
