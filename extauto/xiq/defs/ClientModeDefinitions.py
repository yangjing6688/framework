class ClientModeDefinitions:
    login_page_username_text = \
        {
            'DESC':  'Login Page Username TextField',
            'XPATH': '//input[@name="userName"]',
            'wait_for': 5
        }

    login_page_password_text = \
        {
            'DESC':  'Login Page Password',
            'XPATH': '//input[@name="password"] ',
            'wait_for': 5
        }

    login_page_login_button = \
        {
            'DESC':  'Login Page Submit Button',
            'XPATH': '//img[@src="/rs/extimages/button-login.png"]',
            'wait_for': 10
        }

    admin_page_client_mode_ssid_tab = \
        {
            'DESC': 'admin page -> Client Mode SSID tab',
            'XPATH': '//a[contains(text(), "Client Mode SSID")]',
            'wait_for': 5
        }

    other_ssids_button = \
        {
            'DESC': 'Other SSIDs button',
            'XPATH': '//input[@value="Other SSIDs"]',
            'wait_for': 5
        }

    ssid_textbox = \
        {
            'DESC': 'SSID textbox',
            'XPATH': '//input[@id="inputSSID"]',
            'wait_for': 5
        }

    security_type_dropbox = \
        {
            'DESC': 'Security Type Open Element dropbox',
            'XPATH': '//select[@id="SecurityType"]/option[text()="',
            'wait_for': 3
        }

    password_textbox = \
        {
            'DESC': 'Password textbox',
            'XPATH': '//input[@id="inputPWD"]',
            'wait_for': 5
        }

    connect_button = \
        {
            'DESC': 'Connect button',
            'XPATH': '//div[@id="popup_manual_ssid"]/descendant::input[@value="Connect"]',
            'wait_for': 5
        }

    cancel_button = \
        {
            'DESC': 'Cancel button',
            'XPATH': '//div[@id="popup_manual_ssid"]/descendant::input[@value="Cancel"]',
            'wait_for': 5
        }

    wifi_connection_status = \
        {
            'DESC': 'Wifi Connection Status',
            'XPATH': '//h1[text()="WiFi connection status"]/../h2',
            'wait_for': 20
        }

    check_wifi_connection_status = \
        {
            'DESC': 'Connect button',
            'XPATH': '//h1[text()="WiFi connection status"]/../h2',
            'wait_for': 5
        }

