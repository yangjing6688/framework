#Unit Test: AIQ-2965
#Execution Command: robot -v ENV:environment.local.chrome.yaml -v TOPO:topo.test.g2r1.mkrishnamoorthy.yaml .\Tests\Robot\Functional\XIQ\Common\ESPAlerts\TestCases\KeywordsWebhook.robot

*** Settings ***

Variables   Environments/${TOPO}
Variables   Environments/${ENV}
Variables   ../Resources/Webhook.yaml

Library     keywords/gui/login/KeywordsLogin.py
Library     keywords/gui/webhook/KeywordsWebhook.py
library 	extauto/xiq/flows/common/Navigator.py

Force Tags            testbed_1_none
Suite Setup		Login User 		${TENANT_USERNAME}	${TENANT_PASSWORD}
Suite Teardown	Close Session         

*** Test Cases ***

Verify user is able to add/edit/delete a webhook
    [Documentation]         Create webhook
	
    Navigate To Webhooks Page
	
    ${result}=  Create Webhook  ${webhook1}
    Should Be Equal As Integers  ${result}  1
	
	${result}=  Edit Webhook  ${webhook1}  ${webhook2}
    Should Be Equal As Integers  ${result}  1
	
	Delete Webhook  ${webhook2}
	
*** Keywords ***

Close Session
	Logout User
	Quit Browser
	
