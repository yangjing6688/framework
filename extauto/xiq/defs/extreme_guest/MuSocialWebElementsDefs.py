class MuSocialWebElementsDefs:
    social_wifi_all_facebook_icon = \
        {
            'XPATH': '//a[@data-connect="facebook"]',
            'wait_for': 5
        }

    social_wifi_all_facebook_username_field = \
        {
            'NAME': 'email',
            'wait_for': 2
        }

    social_wifi_all_facebook_password_field = \
        {
            'NAME': 'pass',
            'wait_for': 2
        }

    social_wifi_all_facebook_login_button = \
        {
            'NAME': 'login',
            'wait_for': 2
        }

    social_wifi_all_facebook_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
            'wait_for': 5
        }

    social_wifi_all_login_success_page = \
        {
            'XPATH': '//font[text()="Welcome, enjoy your free internet!"]',
            'wait_for': 5
        }

    social_wifi_all_google_icon = \
        {
            'XPATH': '//a[@data-connect="google"]',
            'wait_for': 5
        }

    social_wifi_all_linkedin_icon = \
        {
            'XPATH': '//a[@data-connect="linkedin"]',
            'wait_for': 5
        }

    social_wifi_all_linkedin_username_field = \
        {
            'NAME': 'session_key',
            'wait_for': 2
        }

    social_wifi_all_linkedin_password_field = \
        {
            'NAME': 'session_password',
            'wait_for': 2
        }

    social_wifi_all_linkedin_signin_button = \
        {
            'CSS_SELECTOR': '.btn__primary--large',
            'wait_for': 3
        }

    social_wifi_all_linkedin_allow_button = \
        {
            'NAME': 'action',
            'wait_for': 1
        }

    social_wifi_all_linkedin_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
            'wait_for': 5
        }

    social_wifi_all_google_username_field = \
        {
            'NAME': 'identifier',
            'wait_for': 2
        }

    social_wifi_all_google_next_button = \
        {
            'XPATH': '//span[text()="Next"]',
            'wait_for': 2
        }

    social_wifi_all_google_username_next_button = \
        {
            'ID': 'identifierNext',
            'wait_for': 2
        }

    social_wifi_all_google_password_next_button = \
        {
            'ID': 'passwordNext',
            'wait_for': 2
        }

    social_wifi_all_google_password_field = \
        {
            'NAME': 'password',
            'wait_for': 2
        }

    social_wifi_all_google_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
            'wait_for': 5
        }

    user_registration_social_wifi_username_field = \
        {
            'XPATH': '//input[@name="f_user"]',
            'wait_for': 5
        }

    user_registration_social_wifi_passcode_field = \
        {
            'XPATH': '//input[@name="f_pass"]',
            'wait_for': 5
        }

    user_registration_social_wifi_signin_button = \
        {
            'XPATH': '//a[text()="Sign In"]',
            'wait_for': 5
        }

    user_registration_social_wifi_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
            'wait_for': 5
        }

    default_template_page_company_logo = \
        {
            'XPATH': '//img[contains(@src, "media")]',
            'wait_for': 5
        }
