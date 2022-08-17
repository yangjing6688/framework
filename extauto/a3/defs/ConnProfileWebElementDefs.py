class ConnProfileWebElementDefs:
    conn_profile_menu = \
        {
            'XPATH': '//*[@data-automation-tag="StandardConnectionProfiles"]',
            'wait_for': 2
        }

    conn_profile_new = \
        {
            'XPATH': '//a[text()="New Connection Profile"]',
            'wait_for': 5
        }

    conn_profile_name = \
        {
            'XPATH': '//*[@data-automation-tag="automation-id"]',
            'wait_for': 2
        }

    add_filter = \
        {
            'XPATH': '//*[@data-automation-tag="Add Filter"]',
            'wait_for': 2
        }

    add_filter_act1 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-filter,0,type"]//input',
            'wait_for': 5
        }

    drop_opt_act1 = \
        {
            'XPATH': '//span[text()="Connection Type"]',
            'wait_for': 5
        }

    add_filter_act2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-filter,0,match"]//input',
            'wait_for': 5
        }

    drop_opt_act2 = \
        {
            'XPATH': '//span[text()="Wireless-802.11-EAP"]',
            'wait_for': 5
        }

    add_source = \
        {
            'XPATH': '//*[@data-automation-tag="Add Source"]',
            'wait_for': 5
        }

    select_source = \
        {
            'XPATH': '//span[text()="AS154"]',
            'wait_for': 5
        }

    save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }