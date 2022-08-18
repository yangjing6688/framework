class A3WebElementsDefs:
    auth_source_ui = \
        {
            'XPATH': '//*[@data-automation-tag="AuthenticationSources"]',
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

    add_rule_row1_act2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,actions,0,value"]',
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

    add_rule_row2_act2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-authentication_rules,0,actions,1,value"]',
            'wait_for': 5
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

    reset_button = \
        {
            'XPATH': '//*[@data-automation-tag="resetButton"]',
            'wait_for': 2
        }

    role_create_button = \
        {
            'XPATH': '//button[text()=" Create "]',
            'wait_for': 2
        }

    close_button = \
        {
            'XPATH': '//button[@title = "Close [ESC]"]',
            'wait_for': 2
        }

    conn_profile_menu = \
        {
            'XPATH': '//*[@data-automation-tag="StandardConnectionProfiles"]',
            'wait_for': 2
        }

    conn_profile_new = \
        {
            'XPATH': '//a[contains(@href,"#/configuration/connection_profiles/new")]',
            'wait_for': 2
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

    select_source = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sources,0"]//input',
            'wait_for': 5
        }

    device_ui = \
        {
            'XPATH': '//*[@data-automation-tag="Devices"]',
            'wait_for': 5
        }

    new_dev_btn = \
        {
            'XPATH': '//*[@class="btn dropdown-toggle btn-outline-primary"]',
            'wait_for': 5
        }

    dev_drop_down = \
        {
            'XPATH': '//ul[@class="dropdown-menu show"]/li',
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

    radiusd_service = \
        {
                'XPATH': "//button[text()=' radiusd-auth ']",
                'wait_for': 5
        }

    domain_close = \
        {
                 'XPATH': "//button[text()='Close']",
                 'wait_for': 5
        }

    conn_profile_test = \
        {
                'XPATH': '//*[@data-automation-tag="ConnectionProfileTest"]',
                'wait_for': 5
        }

    mac_input = \
        {
                'XPATH': '//*[@class="ivu-input-inner-container"]/input',
                'wait_for': 5
        }

    test_start = \
        {
                'XPATH': '//span[contains(text(), "START")]',
                'wait_for': 5
        }

    test_output = \
        {
                'XPATH': '//*[@class="a-tools-textarea"]//pre',
                'wait_for': 5
        }

    realm_ntlm_auth = \
        {
                'XPATH': '//*[@data-automation-tag="NTLMAuth"]',
                'wait_for': 5
        }

    select_duration = \
        {

            'XPATH': '//*[@data-automation-tag="automation-duration"]',
            'wait_for': 2
        }

    input_drop_down_options = \
        {
            'XPATH': '//ul[@class="ivu-select-dropdown-list"]/li',
            'wait_for': 5
        }

    ssh_password = \
        {
            'XPATH': '//input[@type="password" and @class="ivu-input ivu-input-default"]',
            'wait_for': 5
        }

    ssh_save_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 5
        }

    backup_save_config = \
        {
            'XPATH': '//button[normalize-space()="Save Current Configuration"]',
            'wait_for': 2
        }

    backup_menu = \
        {
            'XPATH': '//*[@data-automation-tag="Backup"]',
            'wait_for': 5
        }

    backup_description = \
        {
            'XPATH': '//*[@data-automation-tag="automation-description"]',
            'wait_for': 5
        }

    backup_save = \
        {
            'XPATH': '//*[@data-automation-tag="saveConfigButton"]',
            'wait_for': 5
        }

    backup_value = \
        {
            'XPATH': '//*[@id="blacklistTbl"]/div[2]/div[1]/div[5]',
            'wait_for': 5
        }

    log_ui = \
        {
            'XPATH': '//*[@data-automation-tag="LOGS"]',
            'wait_for': 5
        }

    auth_internal_source = \
        {
            'XPATH': "//*[@class = 'btn dropdown-toggle btn-outline-primary' and @aria-expanded='true']",
            'wait_for': 5
        }

    input_internal_source = \
        {
            'XPATH': '//ul[@class="dropdown-menu show"]//li/a',
            'wait_for': 5
        }

    policies_tab = \
        {
            'XPATH': '//span[contains(text(), "Policies and Access Control")]',
            'wait_for': 2
        }

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

    name_input = \
        {
            'XPATH': "//input[@class='base-form-group-input form-control is-invalid'][@type='text']",
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

    start_button = \
        {
            'XPATH': '//*[@data-automation-tag="startButton"]',
            'wait_for': 2
        }

    ad_domain = \
        {
            'XPATH': '//*[@href="#/configuration/domains"]',
            'wait_for': 2
        }

    domain_button = \
        {
            'XPATH': '//*[@href="#/configuration/domains/new"]',
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

    join_ad = \
        {
            'XPATH': '//button[normalize-space()="Join"]',
            'wait_for': 2
        }

    join_domain_button = \
        {
            'XPATH': '//button[normalize-space()="Join Domain"]',
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

    create_ad = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    system_config_tab = \
        {
            'XPATH': '//*[@id="pf-sidebar-links"]/ul/a[6]/span',
            'wait_for': 2
        }

    cloud_integration = \
        {
            'XPATH': '//*[@data-automation-tag="CloudIntegration"]',
            'wait_for': 2
        }

    cloud_host_input = \
        {
            'XPATH': '//input[@type="text" and @class="ivu-input ivu-input-default" and \
             @placeholder="https://extremecloudiq.com"]',
            'wait_for': 2
        }

    cloud_admin = \
        {
            'XPATH': '//input[@type="text" and @class="ivu-input ivu-input-default" and \
             @placeholder="admin@example.com"]',
            'wait_for': 2
        }

    cloud_password = \
        {
            'XPATH': '//input[@type="password" and @class="ivu-input ivu-input-default"]',
            'wait_for': 2
        }

    cloud_link_button = \
        {
            'XPATH': '//*[@data-automation-tag="linkButton"]',
            'wait_for': 5
        }

    cloud_unlink_button = \
        {
            'XPATH': '//*[@data-automation-tag="unlinkButton"]',
            'wait_for': 5
        }

    ssh_option_ui = \
        {
            'XPATH': '//*[@data-automation-tag="SSH"]',
            'wait_for': 2
        }

    tech_data_ui = \
        {
            'XPATH': '//*[@data-automation-tag="DOWNLOADTECHDATA"]',
            'wait_for': 2
        }

    lite_mode = \
        {
            'XPATH': '//*[@data-automation-tag="automation-litemode"]',
            'wait_for': 2
        }

    download_button = \
        {
            'XPATH': '//*[@data-automation-tag="downloadButton"]',
            'wait_for': 2
        }

    done_button = \
        {
            'XPATH': '//*[@data-automation-tag="doneButton"]',
            'wait_for': 2
        }

    ssh_enable = \
        {
            'XPATH': '/html/body/div/div[2]/div[2]/div[2]/div/div/div/form/div[3]/div/div/label',
            'wait_for': 2
        }

    ssh_selector = \
        {
            'XPATH': '//*[@data-automation-tag="automation-enable"]',
            'wait_for': 5
        }
