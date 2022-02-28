

class AdminOptionsWebElementsDefinitions:

    save_options_button = \
        {
            'DESC': 'Save Options Button',
            'XPATH': '//span[text()="Save"]/../../..',
            'wait_for': 10
        }

    save_warning_dialog = \
        {
            'DESC': 'Save Options Warning Dialog',
            'XPATH': '//div[contains(@class, "x-message-box")]//div[contains(text(), "Save Warn")]',
            'wait_for': 10
        }

    save_warning_yes_button = \
        {
            'DESC': 'Save Options Warning Confirm Yes Button',
            'XPATH': '//span[text()="Yes"]/../../..',
            'wait_for': 10
        }

    restore_default_options_button = \
        {
            'DESC': 'Restore Defaults Button',
            'XPATH': '//span[text()="Restore Defaults"]/../../..',
            'wait_for': 10
        }

    reset_options_button = \
        {
            'DESC': 'Reset Options Button',
            'XPATH': '//span[text()="Reset"]/../../..',
            'wait_for': 10
        }

    site_engine_general_option = \
        {
            'DESC': 'Site Engine - General Option',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Site Engine - General"]',
            'wait_for': 10
        }

    device_tree_name_format_dropdown_trigger = \
        {
            'DESC': 'Device Tree Name Format dropdown trigger',
            'XPATH': '//input[@name="deviceDisplayFormat"]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            'wait_for': 10
        }

    device_tree_name_format_dropdown = \
        {
            'DESC': 'Device Tree Name Format dropdown',
            'XPATH': '//input[@name="deviceDisplayFormat"]',
            'wait_for': 10
        }

    xiq_connection_option = \
        {
            'DESC': 'XIQ Connection Option',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[contains(text(), "IQ Connection")]',
            'wait_for': 10
        }

    xiq_connection_enable_sharing_checkbox = \
        {
            'DESC': 'XIQ Connection: Enable Sharing Checkbox',
            'XPATH': '//input[@name="xiqConnectionEnabled"]',
            'wait_for': 10
        }

    xiqse_serial_number_label = \
        {
            'DESC': 'XIQ-SE Serial Number Label',
            'XPATH': '//label[contains(@class, "x-component-default") and contains(text(), "Site Engine serial number:")]',
            'wait_for': 10
        }

    web_server_option = \
        {
            'DESC': 'Web Server Option',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Web Server"]',
            'wait_for': 10
        }

    web_server_session_timeout_value = \
        {
            'DESC': 'HTTP Session Timeout Value',
            'XPATH': '//input[@name="httpSessionTimeoutOpt"]',
            'wait_for': 10
        }

    web_server_session_timeout_units_dropdown = \
        {
            'DESC': 'HTTP Session Timeout Units dropdown',
            'XPATH': '//div[contains(@class, "timeIntervalUnitsField")]//input',
            'wait_for': 10
        }

    inventory_manager_option = \
        {
            'DESC': 'Inventory Manager',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Inventory Manager"]',
            'wait_for': 10
        }

    scp_login_information_anonymous_checkbox = \
        {
            'DESC': 'SCP Login Information Anonymous Checkbox',
            'XPATH': '//input[@name="invsrvroScpUseAnonymous"]',
            'wait_for': 10
        }

    scp_login_information_username = \
        {
            'DESC': 'SCP Login Information Username field',
            'XPATH': '//input[@name="invsrvroScpUsername"]',
            'wait_for': 10
        }

    scp_login_information_password = \
        {
            'DESC': 'SCP Login Information Password field',
            'XPATH': '//input[@name="invsrvroScpPassword"]',
            'wait_for': 10
        }

    sftp_login_information_anonymous_checkbox = \
        {
            'DESC': 'SFTP Login Information Anonymous Checkbox',
            'XPATH': '//input[@name="invsrvroSftpUseAnonymous"]',
            'wait_for': 10
        }

    sftp_login_information_username = \
        {
            'DESC': 'SFTP Login Information Username field',
            'XPATH': '//input[@name="invsrvroSftpUsername"]',
            'wait_for': 10
        }

    sftp_login_information_password = \
        {
            'DESC': 'SFTP Login Information Password field',
            'XPATH': '//input[@name="invsrvroSftpPassword"]',
            'wait_for': 10
        }

    status_polling_option = \
        {
            'DESC': 'Status Polling',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Status Polling"]',
            'wait_for': 10
        }

    status_polling_group_2_interval_value = \
        {
            'DESC': 'Status Polling Group 2 Interval Value',
            'XPATH': '//input[@name="spoGroup2Interval"]',
            'wait_for': 10
        }

