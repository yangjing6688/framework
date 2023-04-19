class IAMWebElementsDefinitions:
    login_page_sso_button = \
        {
            'XPATH': '//span[@class="login-others-icon login-others-sso"]',
            'wait_for': 3,
        }

    saml_login_page_username_text = \
        {
            'XPATH': '//input[@id="loginName"]',
            'wait_for': 3,
        }

    saml_login_page_continue_button = \
        {
            'XPATH': '//button[@type="submit"]',
            'wait_for': 3,
        }

    saml_login_page_selecting_your_organization_title = \
        {
            'XPATH': '//h1[@class="iam-layout-main-title"]',
            'wait_for': 3,
        }

    saml_login_page_idp_server_item = \
        {
            'XPATH': '//div[@class="idp-server-item"]//a[contains(text(),',
            'wait_for': 3,
        }

    adfs_page_username_text = \
        {
            'XPATH': '//input[@id="userNameInput"]',
            'wait_for': 3,
        }

    adfs_page_password_text = \
        {
            'XPATH': '//input[@id="passwordInput"]',
            'wait_for': 3,
        }

    adfs_page_password_button = \
        {
            'XPATH': '//span[@id="submitButton"]',
            'wait_for': 3,
        }

    xiq_page_account_username_title = \
        {
            'XPATH': '//div[contains(text(),',
            'wait_for': 3,
        }

    xiq_page_account_orgname_title = \
        {
            'XPATH': '//div[contains(text(),',
            'wait_for': 3,
        }

    user_account_nav = \
        {
            'CSS_SELECTOR': '.ah-header-account-info-username',
            'XPATH': '//*[@data-dojo-attach-point="accountInfoUsername"]',
            'wait_for': 15
        }

    logout_user_menu_item = {'CSS_SELECTOR': '.user-list.user-list-acct', 'wait_for': 5}

    menu_item = {'TAG_NAME': 'li', 'wait_for': 5}