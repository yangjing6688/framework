
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


UnitTest-2: Guest Management Role - Adding and deleting users

    [Documentation]         Create Guest Management Role And Delete

    ${CREATE_ACCOUNT}=              Create Role Based Account   ${GUEST_MANAGEMENT_ROLE}
    should be equal as strings      '${CREATE_ACCOUNT}'    '1'
	
	${DELETE_ACCOUNT}=                   Delete Guest Management Accounts
    Should Be Equal As Strings      '${DELETE_ACCOUNT}'     '1'

 
*** Keywords ***

Close Session
	Logout User
	Quit Browser
