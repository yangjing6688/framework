class ToolsWebElementsDefs:
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

    log_ui = \
        {
            'XPATH': '//*[@data-automation-tag="LOGS"]',
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

    start_button = \
        {
            'XPATH': '//*[@data-automation-tag="startButton"]',
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
