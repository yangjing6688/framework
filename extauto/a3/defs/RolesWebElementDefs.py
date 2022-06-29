class RolesWebElementDefs:
    roles = \
        {
            'XPATH': '//*[@href="#/configuration/roles"]',
            'wait_for': 2
        }

    role_button = \
        {
            'XPATH': '//*[@href="#/configuration/roles/new"]',
            'wait_for': 2
        }

    role_name = \
        {
            'XPATH': '//*[@data-automation-tag="automation-id"]',
            'wait_for': 5
        }

    name_desc = \
        {
            'XPATH': '//*[@data-automation-tag="automation-notes"]',
            'wait_for': 2
        }

    create_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    close_button = \
        {
            'XPATH': '//button[@title = "Close [ESC]"]',
            'wait_for': 2
        }

    save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }