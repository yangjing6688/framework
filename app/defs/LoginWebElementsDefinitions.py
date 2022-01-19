

class LoginWebElementsDefinitions:
    login_page_username_text_ids = \
        {
            'DESC': 'Login Page Username TextField',
            'pradeep': "//*[@data-automation-tag='automation-login-page-username-field']",
            'wait_for': 20
         }

    login_page_password_text_ids = \
        {
            'DESC': 'Login Page Password',
            'XPATH': "//*[@data-automation-tag='automation-login-page-password-field']",
            'wait_for': 5
         }

    login_page_login_button_ids = \
        {
            'DESC': 'Login Page Submit Button',
            'XPATH': "//*[@data-automation-tag='automation-login-page-submit-btn']",
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
