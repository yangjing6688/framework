

class NetworkDevicesDevicesBackupConfigurationWebElementsDefinitions:

    yes_button = \
        {
            'DESC': 'Yes button in the Backup Configuration confirmation dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    no_button = \
        {
            'DESC': 'No button in the Backup Configuration confirmation dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }

    ok_button = \
        {
            'DESC': 'OK button in the Backup Configuration dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[text()="OK"]',
            'wait_for': 10
        }
