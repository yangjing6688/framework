

class AnalyticsConfigurationEnforceAllEnginesWebElementsDefinitions:

    enforce_all_engines_yes_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Enforce All Engines Dialog> Yes Button',
            'XPATH': '//span[text()="Yes"]/ancestor::a',
            
        }

    enforce_all_engines_no_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Enforce All Engines Dialog> No Button',
            'XPATH': '//span[text()="No"]/ancestor::a',
            
        }

    enforce_engines_error_dialog = \
        {
            'DESC': 'Enforce Engines Error dialog',
            'XPATH': '//div[contains(@aria-hidden, "false")]//div[contains(text(), "Enforce Engines Error")]',
            
        }

    enforce_engines_error_dialog_ok_button = \
        {
            'DESC': 'OK button within Enforce Engines Error dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[contains(text(), "OK")]',
            
        }


