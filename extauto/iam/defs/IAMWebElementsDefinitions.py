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
            'XPATH': '(//button[@type="submit"])[1]',
            'wait_for': 3,
        }

    adfs_page_submit_button = \
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

    iam_idp_page_add_idp_button = \
        {
            'XPATH': '//mat-icon[contains(text(),"add")]',
            'wait_for': 5,
        }

    iam_idp_page_domain_text = \
        {
            'XPATH': '//input[@name="domain"]',
            'wait_for': 3,
        }

    iam_idp_page_description_text = \
        {
            'XPATH': '//textarea[@name="description"]',
            'wait_for': 3,
        }

    iam_idp_page_profile_continue_button = \
        {
            'XPATH': '(//span[contains(text(),"Continue")])[1]',
            'wait_for': 6,
        }

    iam_idp_page_connection_continue_button = \
        {
            'XPATH': '(//span[contains(text(),"Continue")])[2]',
            'wait_for': 3,
        }

    iam_idp_page_import_from_url_button = \
        {
            'XPATH': '//input[@value="url"]',
            'wait_for': 6,
        }

    iam_idp_page_idp_metadata_url_text = \
        {
            'XPATH': '//input[@name="url"]',
            'wait_for': 5,
        }

    iam_idp_page_import_button = \
        {
            'XPATH': '//span[contains(text(),"Import")]',
            'wait_for': 3,
        }

    iam_idp_page_email_text = \
        {
            #'CSS_SELECTOR': 'div.attr-list > form:nth-of-type(1) > div.attr-item > div.attr-item-saml',
            'XPATH': '(//input[@name="field"])[1]',
            'wait_for': 5
        }

    iam_idp_page_group_text = \
        {
            #'CSS_SELECTOR': 'div.attr-list > form:nth-of-type(2) > div.attr-item > div.attr-item-saml > mat-form-field',
            'XPATH': '(//input[@name="field"])[2]',
            'wait_for': 5
        }

    iam_idp_page_default_group_dropdown = \
        {
            'XPATH': '//div[@class="group-default-field"]',
            'wait_for': 3,
        }

    iam_idp_page_default_group_item = \
        {
            'XPATH': '//span[contains(text(),',
            'wait_for': 3,
        }

    iam_idp_page_entity_id = \
        {
            'XPATH': '//input[@name="entityId"]',
            'wait_for': 5,
        }

    iam_idp_page_sso_binding = \
        {
            'XPATH': '//input[@formcontrolname="ssoUrl"]',
            'wait_for': 3,
        }

    iam_idp_page_slo_binding = \
        {
            'XPATH': '//input[@formcontrolname="sloUrl"]',
            'wait_for': 3,
        }

    iam_idp_page_sloResponse_binding = \
        {
            'XPATH': '//input[@formcontrolname="sloResponseUrl"]',
            'wait_for': 3,
        }

    iam_idp_page_save_button = \
        {
            'XPATH': '//span[contains(text(),"Save")]',
            'wait_for': 5,
        }

    iam_page_list_idp = \
        {
            'XPATH': '//span[contains(text(),',
            'wait_for': 3,
        }

    iam_console_link = \
        {
            'XPATH': '//a[contains(text(),"Identity and Access Management")]',
            'wait_for': 3,
        }


