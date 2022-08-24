class LoginWebElementsDefinitions:
    login_page_username_text_ids = \
        {
            'DESC': 'Login Page Username TextField',
            'XPATH': "//*[@data-automation-tag='username']",
            'wait_for': 5
         }

    login_page_password_text_ids = \
        {
            'DESC': 'Login Page Password',
            'XPATH': "//*[@data-automation-tag='password']",
            'wait_for': 5
         }

    login_page_login_button_ids = \
        {
            'DESC': 'Login Page Submit Button',
            'XPATH': "//*[@data-automation-tag='loginButton']",
            'wait_for': 10
        }

    login_page_wrong_password_message = {'CSS_SELECTOR': '.wrong-password', 'wait_for': 10}

    logout_account_info = {'CSS_SELECTOR': '.ah-header-account-info', 'wait_for': 10}

    logout_user_menu_item = {'CSS_SELECTOR': '.user-list.user-list-acct', 'wait_for': 5}

    dialog_box = {'CSS_SELECTOR': '.dijitDialog', 'wait_for': 5}

    dialog_box_close_button = {'CSS_SELECTOR': '.dijitReset.dijitStretch.dijitButtonContents', 'wait_for': 5}

    menu_item = {'TAG_NAME': 'li', 'wait_for': 5}

    welcome_page_done_button = {'CSS_SELECTOR': '.btn', 'wait_for': 5}

    header_text = {'CSS_SELECTOR': '.headerText', 'wait_for': 5}

    build_version_details = \
        {
            'DESC': 'XIQ Build Version Details',
            'XPATH': "//*[@data-automation-tag='automation-account-menu-build-version']",
            'wait_for': 5
        }

    user_account_nav = \
        {
            'CSS_SELECTOR': '.ah-header-account-info-username',
            'XPATH': '//*[@data-dojo-attach-point="accountInfoUsername"]',
            'wait_for': 5
        }

    cancel_about_extremecloudiq_dialogue = {
        'XPATH': '//*[@data-dojo-attach-point="closeButtonNode"]',
        'index': 2,
        'wait_for': 5
    }

    viq_id_field = \
        {
            'DESC': 'VIQ ID Element',
            'XPATH': '//span[@data-dojo-attach-point="ownerId"]',
            'wait_for': 5
        }

    txt_30_days_trial = \
        {'XPATH': '//div[contains(@id,"WelcomeEdition_1")]/ul/li[1]/span[2]',
         'wait_for': 5
         }

    option_30_days_trial = \
        {'XPATH': '//input[@id="ah/comp/common/WelcomeEdition_1_trial"]',
         'wait_for': 5
         }
    started_button = \
        {'XPATH': '//*[@id="ah/comp/common/WelcomeWizard_1"]/div[7]//button[2]',
         'wait_for': 5
         }

    drawer_trigger = \
        {'XPATH': '//div[@data-dojo-attach-point="drawerTrigger"]',
         'wait_for': 3
         }

    drawer_content = \
        {
         'XPATH': '//div[@data-dojo-attach-point="drawerContent"]//div[@class="welcome-banner-ctn"]',
         'wait_for': 3
         }

    wips_popup_dialog_close_button = \
        {
         'XPATH': '//span[@data-automation-tag="automation-certificate-expiration-close"]',
         'wait_for': 3
         }

    wips_popup_dialog_dont_show_again_checkbox = \
        {
         'XPATH': '//input[@data-automation-tag="automation-certificate-expiration-dont-show"]',
         'wait_for': 3
         }

    wips_dialog_message = \
        {
         'CSS_SELECTOR': '.warning-msg',
         'wait_for': 5
        }


