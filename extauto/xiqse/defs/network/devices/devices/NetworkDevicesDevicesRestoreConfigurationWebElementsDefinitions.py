

class NetworkDevicesDevicesRestoreConfigurationWebElementsDefinitions:

    restore_dropdown_trigger = \
        {
            'DESC': 'Restore dropdown trigger arrow in the Restore Configuration dialog',
            'XPATH': '//label//span[contains(text(), "Restore")]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

    restore_dropdown = \
        {
            'DESC': 'Restore dropdown field in the Restore Configuration dialog',
            'XPATH': '//label//span[contains(text(), "Restore")]/ancestor::div[contains(@id, "combo")]//input',
            
        }

    start_btn = \
        {
            'DESC': 'Start button in the Restore Configuration dialog',
            'XPATH': '//div[contains(@role, "toolbar")]//a[contains(@class, "x-btn-blue-small")]//span[text()="Start"]',
            
        }

    cancel_btn = \
        {
            'DESC': 'Cancel button in the Restore Configuration dialog',
            'XPATH': '//div[contains(@role, "toolbar")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]',
            
        }

    yes_btn = \
        {
            'DESC': 'Yes button in the Confirm Change dialog',
            'XPATH': '//div[contains(@role, "presentation")]//a[contains(@class, "x-btn-blue-small")]//span[text()="Yes"]',
            
        }

    no_btn = \
        {
            'DESC': 'No button in the Confirm Change dialog',
            'XPATH': '//div[contains(@role, "presentation")]//a[contains(@class, "x-btn-default-small")]//span[text()="No"]',
            
        }

    ok_btn = \
        {
            'DESC': 'OK button in the Confirm Change dialog',
            'XPATH': '//div[contains(@role, "presentation")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]',
            
        }