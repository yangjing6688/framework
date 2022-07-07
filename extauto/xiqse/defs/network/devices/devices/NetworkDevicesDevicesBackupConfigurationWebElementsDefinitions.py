

class NetworkDevicesDevicesBackupConfigurationWebElementsDefinitions:

    yes_button = \
        {
            'DESC': 'Yes button in the Backup Configuration confirmation dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[text()="Yes"]/ancestor::a',
            
        }

    no_button = \
        {
            'DESC': 'No button in the Backup Configuration confirmation dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[text()="No"]/ancestor::a',
            
        }

    ok_button = \
        {
            'DESC': 'OK button in the Backup Configuration dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[text()="OK"]',
            
        }
