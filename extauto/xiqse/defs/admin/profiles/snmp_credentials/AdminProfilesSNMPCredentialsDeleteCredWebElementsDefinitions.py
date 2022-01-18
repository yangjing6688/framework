

class AdminProfilesSNMPCredentialsDeleteCredWebElementsDefinitions:

    confirm_delete_snmp_credential_dialog = \
        {
            'DESC': 'Confirmation dialog for Delete SNMP Credential action',
            'XPATH': '//div[contains(@class, "x-title") and text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            'wait_for': 10
        }

    delete_snmp_credential_confirm_dialog_yes_button = \
        {
            'DESC': 'Yes button for the Confirm Delete SNMP Credential dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="Yes"]',
            'wait_for': 10
        }

    delete_snmp_credential_confirm_dialog_no_button = \
        {
            'DESC': 'No button for the Confirm Delete SNMP Credential dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="No"]',
            'wait_for': 10
        }
