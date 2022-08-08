class RolesWebElementDefs:
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
            'XPATH': '//*[@data-automation-tag="automation-filter,0,type"]',
            'wait_for': 5
        }

    add_filter_act2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-filter,0,match"]//input',
            'wait_for': 5
        }

    add_source = \
        {
            'XPATH': '//*[@data-automation-tag="Add Source"]',
            'wait_for': 5
        }

    save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }