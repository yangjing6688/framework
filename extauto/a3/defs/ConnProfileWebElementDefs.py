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

    conn_profile_desc = \
        {
            'XPATH': '//*[@data-automation-tag="automation-description"]',
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

    drop_opt_act3 = \
        {
            'XPATH': '//span[text()="Wireless-802.11-NoEAP"]',
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

    get_table = \
        {
            'XPATH': '//table',
            'wait_for': 5
        }

    radius_audit_log_ui = \
        {
                'XPATH': '//*[@data-automation-tag="RADIUSAuditLogs"]',
                'wait_for': 5
        }

    rad_entry_tab = \
        {
                'XPATH': '//a[contains(text(), "RADIUS")]',
                'wait_for': 5
        }

    rad_ent_info = \
        {
                'XPATH': '//*[contains(text(),"a3225\\a3test1")]',
                'wait_for': 5
        }

    rad_open_info = \
        {
                'XPATH': '//*[contains(text(),"548d5a693c55")]',
                'wait_for': 5
        }

    clients_search_ui = \
        {
                'XPATH': '//*[@data-automation-tag="Search"]',
                'wait_for': 5
        }

    client_info_tab = \
        {
                'XPATH': '//a[contains(text(),"Info")]',
                'wait_for': 5
        }

    client_ent_info = \
        {
                'XPATH': "//*[contains(text(),'realma3154\a3test1')]",
                'wait_for': 5
        }

    client_open_info = \
        {
                'XPATH': "//*[contains(text(),'548d5a693c55')]",
                'wait_for': 5
        }
