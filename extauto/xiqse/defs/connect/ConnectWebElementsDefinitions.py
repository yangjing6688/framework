

class ConnectWebElementsDefinitions:

    configuration_tab = \
        {
            'DESC': 'Connect> Configuration Tab',
            'XPATH': '//span[text()="Configuration" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    diagnostics_tab = \
        {
            'DESC': 'Connect> Diagnostics Tab',
            'XPATH': '//span[text()="Diagnostics" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    services_api_tab = \
        {
            'DESC': 'Connect> Services API Tab',
            'XPATH': '//span[text()="Services API" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }
