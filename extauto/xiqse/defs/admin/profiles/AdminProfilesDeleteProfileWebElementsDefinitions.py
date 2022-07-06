

class AdminProfilesDeleteProfileWebElementsDefinitions:

    confirm_delete_profile_dialog = \
        {
            'DESC': 'Confirmation dialog for Delete Profile action',
            'XPATH': '//div[contains(@class, "x-title") and text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            
        }

    delete_profile_confirm_dialog_yes_button = \
        {
            'DESC': 'Yes button for the Confirm Delete SNMP Credential dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="Yes"]',
            
        }

    delete_profile_confirm_dialog_no_button = \
        {
            'DESC': 'No button for the Confirm Delete SNMP Credential dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="No"]',
            
        }
