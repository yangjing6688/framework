class ActiveDirectoryWebElementsDefs:

    domain_button = \
        {
            'XPATH': '//*[@href="#/configuration/domains/new"]',
            'wait_for': 2
        }

    ad_domain = \
        {
            'XPATH': '//*[@href="#/configuration/domains"]',
            'wait_for': 2
        }

    identifier_input = \
        {
            'XPATH': '//*[@data-automation-tag="automation-id"]',
            'wait_for': 2
        }

    workgroup_input = \
        {
            'XPATH': '//*[@data-automation-tag="automation-workgroup"]',
            'wait_for': 2
        }

    dns_name_input = \
        {
            'XPATH': '//*[@data-automation-tag="automation-dns_name"]',
            'wait_for': 2
        }

    ad_server_input = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ad_server"]',
            'wait_for': 2
        }

    dns_server_input = \
        {
            'XPATH': '//*[@data-automation-tag="automation-dns_servers"]',
            'wait_for': 2
        }

    save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    create_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    join_ad = \
        {
            'XPATH': '//button[normalize-space()="Join"]',
            'wait_for': 2
        }

    join_ad_domain_username = \
        {
            'XPATH': '//*[@data-automation-tag="automation-username"]',
            'wait_for': 2
        }

    join_ad_domain_password = \
        {
            'XPATH': '//*[@data-automation-tag="automation-password"]',
            'wait_for': 2
        }

    join_domain_button = \
        {
            'XPATH': '//button[normalize-space()="Join Domain"]',
            'wait_for': 2
        }

    domain_close = \
        {
            'XPATH': "//button[text()='Close']",
            'wait_for': 5
        }

