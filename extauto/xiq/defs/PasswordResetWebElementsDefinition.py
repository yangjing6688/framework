class PasswordResetWebElementsDefinition:
    account_icon = \
        {
            'XPATH': "//*[@data-dojo-attach-point='headerUserIcon']",
            'wait_for': 5
        }
    global_settings = \
        {
            'XPATH': "//*[@data-dojo-attach-point='accountEl']",
            'wait_for': 5
        }
    account_management = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-accountMng']",
            'wait_for': 5
        }
    add_account = \
        {
            'XPATH': "//*[@data-automation-tag='automation-account-list-add-btn']",
            'wait_for': 5
        }
    email_textbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='emailAddressInput']",
            'wait_for': 5
        }
    name_textbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='adminNameInput']",
            'wait_for': 5
        }
    save_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 5
        }
    password_textbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="password" and @autocomplete="new-password"]',
            'wait_for': 5
        }
    confirm_password_textbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='confirmPassword']",
            'wait_for': 5
        }
    set_password_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='setupPasswordBtn']",
            'wait_for': 5
        }

    reset_password_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='resetpasswordBtn']",
            'wait_for': 5
        }

    user_table = \
        {
            'XPATH': "//*[@class='dgrid-row-table']",
            'wait_for': 5
        }

    delete_icon = \
        {
            'XPATH': '//*[@data-tip="Delete"]',
            'wait_for': 5
        }
    delete_alert = \
        {
            'XPATH': "//*[@data-dojo-attach-point='confirmButton']",
            'wait_for': 5
        }

    forgot_password_reset_it_here_link = \
        {
            'XPATH': "//*[@data-automation-tag='automation-login-page-reset-link']",
            
        }

    forgot_password_email_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='forgotEmail']",
            
        }

    forgot_password_reset_password_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='resetButton']",
            
        }

    forgot_password_result_label = \
        {
            'XPATH': "//*[@data-dojo-attach-point='resendMessaging']",
            
        }
