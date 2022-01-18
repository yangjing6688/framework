

class CommonHelpWebElementsDefinitions:

    help_panel = \
        {
            'DESC': 'Help Panel',
            'XPATH': '//div[contains(@class, "x-panel-default") and contains(@id, "helpPanel")]',
            'wait_for': 10
        }

    help_panel_title = \
        {
            'DESC': 'Help Panel Title',
            'XPATH': '//div[contains(@id, "helpPanel") and contains(@class, "x-title-text") and text()="Help"]',
            'wait_for': 10
        }
