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
