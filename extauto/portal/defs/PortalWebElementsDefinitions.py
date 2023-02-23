class PortalWebElementsDefinitions:
    login_portal_page_username_text = \
        {
            'XPATH': '//input[@name="username"]',
            'wait_for': 3,
        }

    login_portal_page_password_text = \
        {
            'XPATH': '//input[@name="password"]',
            'wait_for': 3,
        }

    login_portal_page_login_button = \
        {
            'XPATH': '//button[@type="submit"]',
            'wait_for': 3,
        }

    login_portal_check_error = \
        {
            'XPATH': '//span[@class="validation-error"]',
            'wait_for': 3,
        }

    add_button_portal = \
        {
            'XPATH': '//button[contains(text(),"Add")]',
            'wait_for': 3,
        }

    logout_menu_portal = \
        {
            'XPATH': '//div[@class="nav-item nav-item-split"]//a[contains(text(),"Logout")]',
            'wait_for': 3,
        }

    users_menu_portal = \
        {
            'XPATH': '//div[@class="nav-item"]//a[contains(text(),"Users")]',
            'wait_for': 3,
        }

    users_page_add_button = \
        {
            'XPATH': '//button[contains(text(),"Add")]',
            'wait_for': 3,
        }

    add_users_page_fullname_text = \
        {
            'XPATH': '//input[@id="displayName"]',
            'wait_for': 3,
        }

    add_users_page_email_text = \
        {
            'XPATH': '//input[@id="loginName"]',
            'wait_for': 3,
        }

    add_users_page_role_viq_text = \
        {
            'XPATH': '//span[contains(text(),"VIQ Administrator")]',
            'wait_for': 3,
        }

    add_users_page_role_msp_text = \
        {
            'XPATH': '//span[contains(text(),"MSP Administrator")]',
            'wait_for': 3,
        }

    add_users_page_submit_button = \
        {
            'XPATH': '//span[contains(text(),"Submit")]',
            'wait_for': 3,
        }

    users_page_name_filter_item = \
        {
            'XPATH': '//div[@colid="displayName"]//span[@class="ag-header-icon ag-header-cell-menu-button"]',
            'wait_for': 3,
        }

    users_page_name_filter_text = \
        {
            'XPATH': '//*[@id="filterText"]',
            'wait_for': 3,
        }

    users_page_filter_list = \
        {
           'XPATH': '//div[contains(text(),',
           'wait_for': 3,
        }

    add_users_page_datacenter_checkbox = \
        {
            'XPATH': '//*[@id="dc-cbx-0"]',
            'wait_for': 3,
        }

    add_users_page_datacenter_label = \
        {
            'XPATH': '//label[@for="dc-cbx-0"]',
            'wait_for': 3,
        }

    users_page_lastpage_button = \
        {
            'XPATH': '//button[@title="Last page"]',
            'wait_for': 3,
        }

    users_page_nextpage_button = \
        {
            'XPATH': '//button[@title="Next page"]',
            'wait_for': 3,
        }

    users_page_displayName_item = \
        {
            'XPATH': '//div[contains(text(),',
            'wait_for': 3,
        }

    delete_button_portal = \
        {
            'XPATH': '//button[contains(text(),"Delete")]',
            'wait_for': 3,
        }

    delete_confirm_yes_item = \
        {
            'XPATH': '//a[contains(text(),"Yes")]',
            'wait_for': 3,
        }

