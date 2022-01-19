

class WirelessThreatsWebElementsDefinitions:

    threats_tab = \
        {
            'DESC': 'Wireless> Threats> Threats Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Threats" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    threat_events_tab = \
        {
            'DESC': 'Wireless> Threats> Threat Events Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Threat Events" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    interference_tab = \
        {
            'DESC': 'Wireless> Threats> Interference Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Interference" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    interference_events_tab = \
        {
            'DESC': 'Wireless> Threats> Interference Events Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Interference Events" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }
