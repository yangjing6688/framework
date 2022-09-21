

class AdminOptionsWebElementsDefinitions:

    alarm_event_option = \
        {
            'DESC': 'Alarm/Event Logs and Tables',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Alarm/Event Logs and Tables"]',

        }

    event_search_scope_client_checkbox = \
        {
            'DESC': 'Event Search Scope - Client Checkbox',
            'XPATH': '//input[@name="aeloClientField"]',

        }

    event_search_scope_event_checkbox = \
        {
            'DESC': 'Event Search Scope - Event Checkbox',
            'XPATH': '//input[@name="aeloEventField"]',

        }

    event_search_scope_source_host_name_checkbox = \
        {
            'DESC': 'Event Search Scope - Source Host NAme Checkbox',
            'XPATH': '//input[@name="aeloSourceHostNameField"]',

        }
    save_options_button = \
        {
            'DESC': 'Save Options Button',
            'XPATH': '//span[text()="Save"]/../../..',
            
        }

    save_warning_dialog = \
        {
            'DESC': 'Save Options Warning Dialog',
            'XPATH': '//div[contains(@class, "x-message-box")]//div[contains(text(), "Save Warn")]',
            
        }

    save_warning_yes_button = \
        {
            'DESC': 'Save Options Warning Confirm Yes Button',
            'XPATH': '//span[text()="Yes"]/../../..',
            
        }

    restore_default_options_button = \
        {
            'DESC': 'Restore Defaults Button',
            'XPATH': '//span[text()="Restore Defaults"]/../../..',
            
        }

    reset_options_button = \
        {
            'DESC': 'Reset Options Button',
            'XPATH': '//span[text()="Reset"]/../../..',
            
        }

    site_engine_general_option = \
        {
            'DESC': 'Site Engine - General Option',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Site Engine - General"]',
            
        }

    device_tree_name_format_dropdown_trigger = \
        {
            'DESC': 'Device Tree Name Format dropdown trigger',
            'XPATH': '//input[@name="deviceDisplayFormat"]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

    device_tree_name_format_dropdown = \
        {
            'DESC': 'Device Tree Name Format dropdown',
            'XPATH': '//input[@name="deviceDisplayFormat"]',
            
        }

    xiq_connection_option = \
        {
            'DESC': 'XIQ Connection Option',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[contains(text(), "IQ Connection")]',
            
        }

    xiq_connection_enable_sharing_checkbox = \
        {
            'DESC': 'XIQ Connection: Enable Sharing Checkbox',
            'XPATH': '//input[@name="xiqConnectionEnabled"]',
            
        }

    xiqse_serial_number_label = \
        {
            'DESC': 'XIQ-SE Serial Number Label',
            'XPATH': '//label[contains(@class, "x-component-default") and contains(text(), "Site Engine serial number:")]',
            
        }

    web_server_option = \
        {
            'DESC': 'Web Server Option',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Web Server"]',
            
        }

    web_server_session_timeout_value = \
        {
            'DESC': 'HTTP Session Timeout Value',
            'XPATH': '//input[@name="httpSessionTimeoutOpt"]',
            
        }

    web_server_session_timeout_units_dropdown = \
        {
            'DESC': 'HTTP Session Timeout Units dropdown',
            'XPATH': '//div[contains(@class, "timeIntervalUnitsField")]//input',
            
        }

    inventory_manager_option = \
        {
            'DESC': 'Inventory Manager',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Inventory Manager"]',
            
        }

    scp_login_information_anonymous_checkbox = \
        {
            'DESC': 'SCP Login Information Anonymous Checkbox',
            'XPATH': '//input[@name="invsrvroScpUseAnonymous"]',
            
        }

    scp_login_information_username = \
        {
            'DESC': 'SCP Login Information Username field',
            'XPATH': '//input[@name="invsrvroScpUsername"]',
            
        }

    scp_login_information_password = \
        {
            'DESC': 'SCP Login Information Password field',
            'XPATH': '//input[@name="invsrvroScpPassword"]',
            
        }

    sftp_login_information_anonymous_checkbox = \
        {
            'DESC': 'SFTP Login Information Anonymous Checkbox',
            'XPATH': '//input[@name="invsrvroSftpUseAnonymous"]',
            
        }

    sftp_login_information_username = \
        {
            'DESC': 'SFTP Login Information Username field',
            'XPATH': '//input[@name="invsrvroSftpUsername"]',
            
        }

    sftp_login_information_password = \
        {
            'DESC': 'SFTP Login Information Password field',
            'XPATH': '//input[@name="invsrvroSftpPassword"]',
            
        }

    status_polling_option = \
        {
            'DESC': 'Status Polling',
            'XPATH': '//td[contains(@class, "x-grid-cell-treecolumn")]//span[text()="Status Polling"]',
            
        }

    status_polling_group_2_interval_value = \
        {
            'DESC': 'Status Polling Group 2 Interval Value',
            'XPATH': '//input[@name="spoGroup2Interval"]',
            
        }

