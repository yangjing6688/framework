class ExtremeGuestAnalyzeClientsWebElementsDefs:
    extreme_guest_analyze_clients_tab = \
        {
            'XPATH': '//span[text()="Clients"]',
            'wait_for': 5
        }

    extreme_guest_analyze_clients_total_clients = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-key-metrics-device-btn"]',
            'wait_for': 5
        }

    extreme_guest_analyze_clients_grid = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-analyzeclients-grid"]//td/..',
            'wait_for': 5
        }

    extreme_guest_analyze_clients_grid_location_column = \
        {
            'XPATH': '//span[contains(@class,"eguest-analyzeclients-locationcolumn-txt")]',
            'wait_for': 5
        }

    extreme_guest_analyze_clients_grid_macaddress_column = \
        {
            'XPATH': '//span[text()="${mac}"]',
            'wait_for': 5
        }