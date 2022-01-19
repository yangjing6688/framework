

class AdminDiagnosticsWebElementsDefinitions:

    level_dropdown = \
        {
            'DESC': '"Level:" Dropdown',
            'XPATH': '//div[contains(@id, "rptAdminNavigationTree")]//span[contains(text(), "Level:")]',
            'wait_for': 10
        }

    level_advanced_choice = \
        {
            'DESC': '"Advanced" Choice from the "Level:" Dropdown"',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Advanced"]',
            'wait_for': 10
        }

    level_basic_choice = \
        {
            'DESC': '"Basic" Choice from the "Level:" Dropdown"',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Basic"]',
            'wait_for': 10
        }

    level_diagnostic_choice = \
        {
            'DESC': '"Diagnostic" Choice from the "Level:" Dropdown"',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Diagnostic"]',
            'wait_for': 10
        }

    server_tree_node = \
        {
            'DESC': 'Server Tree Node',
            'XPATH': '//span[text()="Server"]',
            'wait_for': 10
        }

    server_tree_node_expanded = \
        {
            'DESC': 'Server Tree Node Expanded',
            'XPATH': '//span[text()="Server"]/../div[contains(@class, "parent-expanded")]',
            'wait_for': 10
        }

    server_tree_node_collapsed = \
        {
            'DESC': 'Server Tree Node Collapsed',
            'XPATH': '//span[text()="Server"]/../div[not(contains(@class, "parent-expanded"))]',
            'wait_for': 10
        }

    server_log_tree_node = \
        {
            'DESC': 'Server Log Tree Node',
            'XPATH': '//span[text()="Server Log"]',
            'wait_for': 10
        }

    system_tree_node = \
        {
            'DESC': 'System Tree Node',
            'XPATH': '//span[text()="System"]',
            'wait_for': 10
        }

    system_tree_node_expanded = \
        {
            'DESC': 'System Tree Node Expanded',
            'XPATH': '//span[text()="System"]/../div[contains(@class, "parent-expanded")]',
            'wait_for': 10
        }

    system_tree_node_collapsed = \
        {
            'DESC': 'System Tree Node Collapsed',
            'XPATH': '//span[text()="System"]/../div[not(contains(@class, "parent-expanded"))]',
            'wait_for': 10
        }

    server_log_panel_title = \
        {
            'DESC': 'Server Log Panel Title',
            'XPATH': '//div[contains(@class, "x-title-text") and contains(text(), "Server Log")]',
            'wait_for': 10
        }

    server_log_clear_button = \
        {
            'DESC': 'Server Log Clear Button',
            'XPATH': '//a[contains(@class, "x-btn-default-toolbar-small")]//span[text()="Clear"]',
            'wait_for': 10
        }

    server_log_refresh_button = \
        {
            'DESC': 'Server Log Refresh Button',
            'XPATH': '//a[contains(@class, "x-btn-default-toolbar-small")]//span[text()="Refresh"]',
            'wait_for': 10
        }

    server_log_contents = \
        {
            'DESC': 'Server Log Contents',
            'XPATH': '//div[@class="stringDisplayPanel"]',
            'wait_for': 10
        }

    xiq_device_message_details_tree_node = \
        {
            'DESC': 'XIQ Device Message Details Tree Node',
            'XPATH': '//span[contains(text(), "Device Message Details")]',
            'wait_for': 10
        }

    xiq_device_message_details_ip_address_column_header = \
        {
            'DESC': 'XIQ Device Message Details IP Address Column Header',
            'XPATH': '//span[@class="x-column-header-text-inner" and text()="IP Address"]',
            'wait_for': 10
        }

    xiq_device_message_details_title = \
        {
            'DESC': 'XIQ Device Message Details Panel Title',
            'XPATH': '//div[contains(@class, "x-title-text") and contains(text(), "Device Message Details")]',
            'wait_for': 10
        }

    xiq_device_message_details_table_rows = \
        {
            'DESC': 'XIQ Device Message Details Table Rows',
            'XPATH': '//div[contains(@id, "beanGrid")]//div[@class="x-grid-item-container"]/table//tr',
            'wait_for': 10
        }

    xiq_device_message_details_last_update_time_col = \
        {
            'DESC': 'Last Update Time column header in the XIQ Device Message Details Table',
            'XPATH': '//span[contains(@id, "gridcolumn") and text()="Last Update Time"]',
            'wait_for': 10
        }

    xiq_device_message_details_onboard_status_col = \
        {
            'DESC': 'Onboard Status column header in the XIQ Device Message Details Table',
            'XPATH': '//span[contains(@id, "gridcolumn") and text()="Onboard Status"]',
            'wait_for': 10
        }

    xiq_device_message_details_refresh_button = \
        {
            'DESC': 'Refresh Button for the XIQ Device Message Details Table',
            'XPATH': '//div[contains(@id, "beanGrid")]//a[@data-qtip="Refresh"]',
            'wait_for': 10
        }

    xiq_device_message_details_displaying_rows_label = \
        {
            'DESC': 'Refresh Button for the XIQ Device Message Details Table',
            'XPATH': '//div[contains(@id, "beanGrid")]//label[contains(text(), "Displaying")]',
            'wait_for': 10
        }

    xiq_device_message_details_search_button = \
        {
            'DESC': 'Search Button  to open the search panel for the XIQ Device Message Details Table',
            'XPATH': '//div[contains(@id, "beanGrid")]//a[@data-qtip="Open Search Box"]',
            'wait_for': 10
        }

    xiq_device_message_details_search_text_field = \
        {
            'DESC': 'Search Text Field for the XIQ Device Message Details Table',
            'XPATH': '//div[contains(@id, "beanGrid")]//input',
            'wait_for': 10
        }

    xiq_device_message_details_perform_search_button = \
        {
            'DESC': 'Search Button in the search box to perform the search',
            'XPATH': '//div[contains(@id, "beanGrid")]//div[contains(@id, "trigger-search")]',
            'wait_for': 10
        }

    xiq_device_message_details_search_clear_button = \
        {
            'DESC': 'Clear Search Button for the XIQ Device Message Details Table',
            'XPATH': '//div[contains(@id, "beanGrid")]//div[contains(@id, "trigger-clear")]',
            'wait_for': 10
        }

    xiq_device_message_details_show_xiq_messages_button = \
        {
            'DESC': 'Show XIQ Messages button for the XIQ Device Message Details Table',
            'XPATH': '//span[contains(text(), "Show") and contains(text(), "Messages")]',
            'wait_for': 10
        }

    show_xiq_messages_dialog_title = \
        {
            'DESC': 'Title for the Show XIQ Messages dialog',
            'XPATH': '//div[contains(@class, "x-title-text") and contains(text(), "Messages for Device:")]',
            'wait_for': 10
        }

    show_xiq_messages_dialog_content = \
        {
            'DESC': 'Content for the Show XIQ Messages dialog',
            'XPATH': '//textarea[not(contains(@id, "messagebox"))]',
            'wait_for': 10
        }

    show_xiq_messages_dialog_close_button = \
        {
            'DESC': 'Close button for the Show XIQ Messages dialog',
            'XPATH': '//span[text()="Close"]',
            'wait_for': 10
        }

    xiq_device_message_details_auto_onboard_xiqse_button = \
        {
            'DESC': 'Auto Onboard XIQ-SE button in the XIQ Device Message Details view',
            'XPATH': '//span[contains(text(), "Auto onboard XIQ-SE") or contains(text(), "Auto Onboard ExtremeCloud IQ - Site Engine")]',
            'wait_for': 10
        }

    auto_onboard_xiqse_dialog_title = \
        {
            'DESC': 'Title for the Auto Onboard XIQ-SE to XIQ dialog',
            'XPATH': '//div[contains(@class, "x-title-text") and '
                      '(contains(text(), "Auto onboard XIQ-SE to XIQ") or contains(text(), "Auto Onboard ExtremeCloud IQ - Site Engine"))]',
            'wait_for': 10
        }

    auto_onboard_xiqse_dialog_email_field = \
        {
            'DESC': 'Email field for the Auto Onboard XIQ-SE to XIQ dialog',
            'XPATH': '//label//span[text()="Email:"]/ancestor::div//input[@name="email"]',
            'wait_for': 10
        }

    auto_onboard_xiqse_dialog_password_field = \
        {
            'DESC': 'Password field for the Auto Onboard XIQ-SE to XIQ dialog',
            'XPATH': '//label//span[text()="Password:"]/ancestor::div//input[@name="password"]',
            'wait_for': 10
        }

    auto_onboard_xiqse_dialog_submit_button = \
        {
            'DESC': 'Submit button for the Auto Onboard XIQ-SE to XIQ dialog',
            'XPATH': '//span[text()="Submit"]',
            'wait_for': 10
        }

    auto_onboard_xiqse_dialog_confirm_ok = \
        {
            'DESC': 'OK button for the Auto Onboard XIQ-SE to XIQ confirmation dialog',
            'XPATH': '//div[@role="alertdialog"]//span[text()="OK"]',
            'wait_for': 10
        }

    auto_onboard_xiqse_dialog_confirm_cancel = \
        {
            'DESC': 'Cancel button for the Auto Onboard XIQ-SE to XIQ confirmation dialog',
            'XPATH': '//div[@role="alertdialog"]//span[text()="Cancel"]',
            'wait_for': 10
        }

    xiq_device_message_details_column = \
        {
            'DESC': 'Column value for the specified column ID and row in the XIQ Device Message Details table',
            'CSS_SELECTOR': 'td[data-columnid="${element_id}"]',
            'wait_for': 10
        }
