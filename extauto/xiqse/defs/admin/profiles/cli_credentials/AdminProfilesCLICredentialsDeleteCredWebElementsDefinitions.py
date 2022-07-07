

class AdminProfilesCLICredentialsDeleteCredWebElementsDefinitions:

    confirm_delete_cli_credential_dialog = \
        {
            'DESC': 'Confirmation dialog for Delete CLI Credential action',
            'XPATH': '//div[contains(@class, "x-title") and text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            
        }

    delete_cli_credential_confirm_dialog_yes_button = \
        {
            'DESC': 'Yes button for the Confirm Delete CLI Credential dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="Yes"]',
            
        }

    delete_cli_credential_confirm_dialog_no_button = \
        {
            'DESC': 'No button for the Confirm Delete CLI Credential dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="No"]',
            
        }
