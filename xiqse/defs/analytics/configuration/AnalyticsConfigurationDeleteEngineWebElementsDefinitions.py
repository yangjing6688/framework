

class AnalyticsConfigurationDeleteEngineWebElementsDefinitions:

    delete_engine_yes_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Delete Engine Dialog> Yes Button',
            'XPATH': '//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    delete_engine_no_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Delete Engine Dialog> No Button',
            'XPATH': '//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }

