class DeviceWebElementDefs:
    device_ui = \
        {
            'XPATH': '//*[@data-automation-tag="Devices"]',
            'wait_for': 5
        }

    new_dev_btn = \
        {
            'XPATH': '//button[normalize-space()="New Device"]',
            'wait_for': 5
        }

    new_dev_options = \
        {
            'XPATH': '//ul[@class="dropdown-menu show"]//li[2]/a',
            'wait_for': 5
        }

    options = \
        {
            'XPATH': '//*[@class="btn dropdown-toggle btn-outline-primary"]',
            'wait_for': 5
        }

    toggle_option = \
        {
            'XPATH': '//*[@class="base-input-range-label col-form-label text-nowrap mr-2"]',
            'wait_for': 5
        }

    device_ip = \
        {
            'XPATH': '//*[@data-automation-tag="automation-id"]',
            'wait_for': 5
        }

    device_description = \
        {
            'XPATH': '//*[@data-automation-tag="automation-description"]',
            'wait_for': 5
        }

    device_type = \
        {
            'XPATH': '//*[@data-automation-tag="automation-type"]//input',
            'wait_for': 5
        }

    device_mode = \
        {
            'XPATH': '//*[@data-automation-tag="automation-mode"]//input',
            'wait_for': 5
        }

    device_de_auth_method = \
        {
            'XPATH': '//*[@data-automation-tag="automation-deauthMethod"]//input',
            'wait_for': 5
        }

    device_roles = \
        {
            'XPATH': '//*[@data-automation-tag="Roles" and @role="tab"]',
            'wait_for': 5
        }

    guest_vlan = \
        {
            'XPATH': '//*[@data-automation-tag="automation-guestVlan"]',
            'wait_for': 5
        }

    emp_vlan = \
        {
            'XPATH': '//*[@data-automation-tag="automation-roleEVlan"]',
            'wait_for': 5
        }

    radius_tab = \
        {
            'XPATH': '//*[@data-automation-tag="RADIUS"]',
            'wait_for': 5
        }

    radius_SC = \
        {
            'XPATH': '//*[@data-automation-tag="automation-radiusSecret"]',
            'wait_for': 5
        }

    save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }