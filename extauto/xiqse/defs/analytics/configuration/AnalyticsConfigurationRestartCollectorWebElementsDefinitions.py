

class AnalyticsConfigurationRestartCollectorWebElementsDefinitions:

    restart_collector_yes_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Restart Collector Dialog> Yes Button',
            'XPATH': '//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    restart_collector_no_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Restart Collector Dialog> No Button',
            'XPATH': '//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }

    restart_collector_error_dialog = \
        {
            'DESC': 'Restart Collector Error dialog',
            'XPATH': '//div[contains(@aria-hidden, "false")]//div[contains(text(), "Restart Collector Error")]',
            'wait_for': 10
        }

    restart_collector_error_dialog_ok_button = \
        {
            'DESC': 'OK button within Restart Collector Error dialog',
            'XPATH': '//div[contains(@role, "alertdialog")]//span[contains(text(), "OK")]',
            'wait_for': 10
        }

