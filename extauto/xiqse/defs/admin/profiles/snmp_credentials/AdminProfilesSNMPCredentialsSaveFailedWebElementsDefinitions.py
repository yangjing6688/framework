

class AdminProfilesSNMPCredentialsSaveFailedWebElementsDefinitions:

    add_snmp_credential_save_failed_dialog = \
        {
            'DESC': 'Save Failed dialog for Add SNMP Credential',
            'XPATH': '//div[text()="Save Failed"]/ancestor::div[contains(@class, "x-message-box")]',
            
        }

    add_snmp_credential_save_failed_dialog_message = \
        {
            'DESC': 'Save Failed dialog message for Add SNMP Credential',
            'XPATH': '//div[text()="Save Failed"]/ancestor::div[contains(@class, "x-message-box")]//div[contains(@id, "-msg")]',
            
        }

    add_snmp_credential_save_failed_dialog_ok_button = \
        {
            'DESC': 'OK button for the Save Failed dialog',
            'XPATH': '//div[text()="Save Failed"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="OK"]',
            
        }
