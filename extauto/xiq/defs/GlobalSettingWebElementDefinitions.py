class GlobalSettingWebElementDefinitions:
    authentication_logs_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 5
        }

    authentication_logs_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 2
        }

    authentication_logs_auth_status_cell = \
        {
            'CSS_SELECTOR': '.auth-logs-reply',
            'wait_for': 2
        }

    global_settings_account_enable_hiq_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableHhm"]',
            'wait_for': 3
        }

    opt_out_copilot_beta_status_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="disableCopilotBeta"]',
            'wait_for': 3
        }

    global_settings_account_organizations_slider = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-orgManagement"]',
            'wait_for': 3
        }

    global_settings_account_organizations_add_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'wait_for': 5
        }

    global_settings_account_organization_name_inputfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="organizationNameNode"]',
            'wait_for': 3
        }

    global_settings_organization_name_colour_scroll_button = \
        {
            'CSS_SELECTOR': '.placeholder',
            'wait_for': 3
        }

    global_settings_organization_scroll_all_items = \
        {
            'CSS_SELECTOR': '.customDropdownList',
            'wait_for': 5
        }

    global_settings_organization_scroll_get_colour = \
        {
            'CSS_SELECTOR': '.colorName',
            'wait_for': 5
        }

    global_settings_account_organization_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="submitButtonNode"]',
            'wait_for': 3
        }


    global_settings_create_account_organization_scroll_button = \
        {
            'XPATH': '//span[contains(text(),"All Organizations")]',
            'wait_for': 3
        }

    global_settings_create_account_organization_scroll_all_items = \
        {
            'CSS_SELECTOR': '.chzn-results',
            'wait_for': 5
        }

    global_settings_create_account_organization_scroll_get_name = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    global_settings_create_account_organization_section = \
        {
            'XPATH': '//*[@data-dojo-attach-point="organizationSection"]',
            'wait_for': 3
        }

    organization_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            
        }

    organization_grid_rows_cell = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            
        }

    global_settings_account_enable_hiq_confirm_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableHhmBtn"]',
            'wait_for': 3
        }

    authentication_logs_view_all_pages = \
        {
            'XPATH': '//a[contains(text(),"100")]',
            'wait_for': 3
        }

    authentication_logs_search_text_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="filterText"]',
            'wait_for': 3
        }

    device_management_settings_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-deviceMng"]',
            'wait_for': 3
        }

    device_management_settings_password = \
        {
            'XPATH': '//*[@data-dojo-attach-point="defaultPassword"]',
            'wait_for': 3
        }

    device_management_settings_password_confirm = \
        {
            'XPATH': '//*[@data-dojo-attach-point="confirmDefaultPassword"]',
            'wait_for': 3
        }

    device_management_settings_show_password_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="showHideDefPassCheck"]',
            'wait_for': 3
        }

    device_management_settings_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveDefaultPassword"]',
            'wait_for': 3
        }

    authentication_logs_unknown_error_close_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="xEl"]',
            'wait_for': 3
        }

    account_select_language_drop_down = \
        {
            'XPATH': '//div[contains(@class, "select-language")]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 3
        }

    account_select_language_drop_down_options = \
        {
            'XPATH': '//div[contains(@class, "select-language")]//div[@data-automation-tag="automation-chzn-container-ctn"]//ul/li',
            'wait_for': 3
        }

    account_language_apply_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="btnApplyLanguage"]',
            'wait_for': 3
        }

    account_icon = \
        {
            'XPATH': "//*[@data-dojo-attach-point='headerUserIcon']",
            'wait_for': 5
        }

    global_settings = \
        {
            'XPATH': "//*[@data-dojo-attach-point='accountEl']",
            'wait_for': 5
        }

    SSH_availability = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-sshAvailability']",
            'wait_for': 5
        }

    enable_ssh = \
        {
            'XPATH': "//*[@data-dojo-attach-point='globalEnableSSH']",
            'wait_for': 5
        }

    api_access_token_rows = \
        {
            'XPATH': '//div[@class="xapi-token-mgmt container"]//table[@class="dojoxGridRowTable"]',
            'wait_for': 5
        }

    api_access_token_row_cells = \
        {
            'CSS_SELECTOR': '.dojoxGridCell',
            'wait_for': 2
        }

    api_access_tokens_select_check_box = \
        {
            'XPATH': '//div[@class="xapi-token-mgmt container"]//table[@class="dojoxGridRowTable"]'
                     '//div[contains(@class, "dojoxGridRowSelector")]',
            'wait_for': 5,
            'index': 0
        }

    api_access_tokens_delete_button = \
        {
            'XPATH': '//ul[@class="grid-action-menu-list"]//li[@data-dojo-attach-point="removeToken"]',
            'wait_for': 5,
        }

    api_access_tokens_delete_cnfm_button = \
        {
            'XPATH': '//p[@class="cfm-btns"]//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5,
        }

    account_time_zone_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag = "automation-account-details-timezone"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 3
        }

    account_time_zone_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag = "automation-account-details-timezone"]//div[@data-automation-tag="chzn-container-ctn"]//ul/li',
            'wait_for': 3
        }

    account_time_zone_apply_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="btnApplyTimeZone"]',
            'wait_for': 3
        }

    viq_backup_now_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="backupNow"]',
            'wait_for': 3
        }

    viq_last_backup_time_textfield = \
        {
            'XPATH': '//span[@data-dojo-attach-point="displayLastBackup"]',
            'wait_for': 3
        }

    viq_delete_data_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="deleteData"]',
            'wait_for': 3
        }

    viq_backup_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 3
        }

    reset_viq_confirm_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 3
        }

    viq_export_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="exportVhm"]',
            'wait_for': 3
        }

    viq_export_now_button = \
        {
            'XPATH': '//*[@class="export-button-antdButton-mainComponent ant-btn ant-btn-info"]',
            'wait_for': 3
        }

    viq_export_yes_button = \
        {
            'XPATH': '//*[@class="ant-btn ant-btn-primary ant-btn-lg"]',
            'wait_for': 3
        }

    viq_export_ok_button = \
        {
            'XPATH': '//*[@class="return-antdButton-loadResponseComponent ant-btn ant-btn-default"]',
            'wait_for': 3
        }

    export_status_textfield_success = \
        {
            'XPATH': '//div[@id="lastExportSuccess"]//div[@class="last-export-success-title-div-mainComponent"]',
            'wait_for': 3
        }

    export_status_textfield_fail = \
        {
            'XPATH': '//div[@id="lastExportFailed"]//div[@class="last-export-title-div-mainComponent"]',
            'wait_for': 3
        }

    account_industry_drop_down = \
        {
            'XPATH': '//div[contains(@data-automation-tag,"chzn-container-ctn")]',
            'wait_for': 3,
            'index': 2
        }

    account_industry_drop_down_options = \
        {
            'XPATH': '//div[contains(@data-dojo-attach-point,"industryCtn")]//div[contains(@data-dojo-attach-point,"templContainer")]//div[contains(@data-automation-tag,"chzn-container-ctn")]//ul//li',
            'wait_for': 3
        }

    account_industry_apply_button = \
        {
            'XPATH': '//button[contains(@data-dojo-attach-point,"btnApplyIndustry")]',
            'wait_for': 3
        }

    audit_logs_view_all_pages = \
        {
            'XPATH': '//a[contains(text(),"100")]',
            'wait_for': 3,
            'index': 1
        }

    viq_supplemental_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableSupplementalCli"]',
            'wait_for': 3
        }

    ssh_availability_option_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableSSHAvailability"]',
            'wait_for': 3
        }

    device_management_settings_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableExosVoss"]',
            'wait_for': 3
        }

    device_management_settings_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveDefaultPassword"]',
            'wait_for': 3
        }

    enable_copilot_feature_option_status = \
        {
            'XPATH': '//*[@data-automation-tag="viq-copilot-feature-toggle"]',
            'wait_for': 3
        }
