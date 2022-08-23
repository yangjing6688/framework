class AuthSourcesWebElementDefs:
    auth_source_ui = \
        {
            'XPATH': '//*[@data-automation-tag="AuthenticationSources"]',
            'wait_for': 5,
        }

    auth_source_button = \
        {
            'XPATH': '//button[normalize-space()="New Internal Source"]',
            'wait_for': 5,
        }

    auth_source_options = \
        {
            'XPATH': '//ul[@class="dropdown-menu show"]//li/a',
            'wait_for': 5,
        }

    host_input = \
        {
            'XPATH': '//*[@data-automation-tag="automation-host"]//input',
            'wait_for': 5,
        }

    ad_name = \
        {
            'XPATH': '//*[@data-automation-tag="automation-id"]',
            'wait_for': 5,
        }

    ad_description = \
        {
            'XPATH': '//*[@data-automation-tag="automation-description"]',
            'wait_for': 5,
        }

    ad_host = \
        {
            'XPATH': '//*[@data-automation-tag="automation-host"]',
            'wait_for': 5,
        }

    ad_base_dn = \
        {
            'XPATH': '//*[@data-automation-tag="automation-basedn"]',
            'wait_for': 5,
        }

    ad_bind_dn = \
        {
            'XPATH': '//*[@data-automation-tag="automation-binddn"]',
            'wait_for': 5,
        }

    passwd = \
        {
            'XPATH': '//input[@type="password"]',
            'wait_for': 5,
        }

    test_pwd = \
        {
            'XPATH': '//button[normalize-space()="Test"]',
            'wait_for': 5,
        }

    ad_auth_add_rule = \
        {
            'XPATH': '//*[@data-automation-tag="Add Rule"]',
            'wait_for': 5,
        }

    auth_add_rule_unknown = \
        {
            'XPATH': '//*[@class="d-block text-secondary"]',
            'wait_for': 5,
        }

    add_rule_name = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,id"]',
            'wait_for': 5,
        }

    add_action = \
        {
            'XPATH': '//*[@data-automation-tag="Add Action"]',
            'wait_for': 5,
        }

    add_rule_row1_act1 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,actions,0,type"]//input',
            'wait_for': 5,
        }

    rule_row1_select_option = \
        {
                'XPATH': '//span[text()="Role"]',
                'wait_for': 5
        }

    add_rule_row1_act2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,actions,0,value"]//input',
            'wait_for': 5,
        }

    value_row1_select_option = \
        {
            'XPATH': '//span[text()="roleE"]',
            'wait_for': 5,
        }

    add_row = \
        {
            'XPATH': '//a[@title="Add Row"]',
            'wait_for': 5,
        }

    add_rule_row2_act1 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,type"]//input',
            'wait_for': 5,
        }

    rule_row2_select_option = \
        {
                'XPATH': '//span[text()="Access duration"]',
                'wait_for': 5
        }

    add_rule_row2_act2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,value"]//input',
            'wait_for': 5
        }

    value_row2_select_option = \
        {
            'XPATH': '//span[text()="5 days"]',
            'wait_for': 5,
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