

class AnalyticsConfigurationEnforceEngineWebElementsDefinitions:

    enforce_engine_yes_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Enforce Engine Dialog> Yes Button',
            'XPATH': '//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    enforce_engine_no_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Enforce Engine Dialog> No Button',
            'XPATH': '//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }

    enforce_engine_error_dialog = \
        {
            'DESC': 'Enforce Engine Error dialog',
            'XPATH': '//div[contains(@aria-hidden, "false")]//div[contains(text(), "Enforce Engine Error")]',
            'wait_for': 10
        }

    enforce_engine_error_dialog_ok_button = \
        {
            'DESC': 'OK button within Enforce Engine Error dialog',
            'XPATH': '// div[contains(@role, "alertdialog")]//span[contains(text(), "OK")]',
            'wait_for': 10
        }
