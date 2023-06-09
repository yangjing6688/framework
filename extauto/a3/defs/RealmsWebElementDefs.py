class RealmsWebElementDefs:

    realm_ui = \
        {
                'XPATH': '//*[@data-automation-tag="Realms"]',
                'wait_for': 5
        }

    realm_button = \
        {
                'XPATH': '//*[@href="#/configuration/realms/1/new"]',
                'wait_for': 5
        }

    realm_input = \
        {
                'XPATH': '//*[@data-automation-tag="automation-id"]',
                'wait_for': 5
        }

    realm_ntlm_auth = \
        {
                'XPATH': '//*[@data-automation-tag="NTLMAuth"]',
                'wait_for': 5
        }

    realm_list = \
        {
                'XPATH': '//*[@data-automation-tag="automation-domain"]',
                'wait_for': 5
        }

    realm_select_option = \
        {
                'XPATH': '//span[text()="ad154"]',
                'wait_for': 5
        }

    radiusd_button = \
        {
                'XPATH': "//button[text()=' radiusd-auth ']",
                'wait_for': 5
        }

    radiusd_options = \
        {
                'XPATH': "//ul[@class='dropdown-menu show']//li/a",
                'wait_for': 5
        }
    realm_select = \
        {
                'XPATH': '//*[@data-automation-tag="automation-id"]',
                'wait_for': 5
        }

    create_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    close_button = \
        {
            'XPATH': '//button[@title = "Close [ESC]"]',
            'wait_for': 2
        }
