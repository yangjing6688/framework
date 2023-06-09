

class NetworkCommonConfigureDeviceImportSiteConfigWebElementsDefinitions:

    import_site_config_dialog = \
        {
            'DESC': 'Import Site Configuration dialog seen when changing Default Site in Configure Device dialog',
            'XPATH': '//div[text()="Import Site Configuration"]/ancestor::div[contains(@class, "x-message-box")]',
            
        }

    yes_button = \
        {
            'DESC': 'Yes button in the Import Site Configuration dialog',
            'XPATH': '//div[text()="Import Site Configuration"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="Yes"]/ancestor::a',
            
        }

    no_button = \
        {
            'DESC': 'No button in the Import Site Configuration dialog',
            'XPATH': '//div[text()="Import Site Configuration"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="No"]/ancestor::a',
            
        }
