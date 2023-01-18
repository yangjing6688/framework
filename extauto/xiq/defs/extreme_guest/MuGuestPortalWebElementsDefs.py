class MuGuestPortalWebElementsDefs:
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

    social_wifi_max_count_error = \
        {
            'XPATH': '//div[text()="Max count(1) of devices supported per user exceeded. Please contact administrator."]',
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

    default_template_page_acceptandconnect_button = \
        {
            'XPATH': '//a[text()=" ACCEPT & CONNECT "]',
            'wait_for': 5
        }

    sponsor_guest_access_username_field = \
        {
            'XPATH': '//input[@name="f_user"]',
            'wait_for': 1
        }

    sponsor_guest_access_password_field = \
        {
            'XPATH': '//input[@name="f_pass"]',
            'wait_for': 1
        }

    sponsor_guest_access_signin_btn = \
        {
            'XPATH': '//form[@class="loginForm"]//a[contains(@class,"submit")]',
            'wait_for': 1
        }

    sponsor_guest_access_clear_btn = \
        {
            'XPATH': '//a[@type="reset"]',
            'wait_for': 1
        }

    sponsor_guest_access_registernow_btn = \
        {
            'XPATH': '//a[contains(@class,"regButton")]',
            'wait_for': 1
        }

    sponsor_guest_access_register_employee_btn = \
        {
            'XPATH': '//a[contains(@class,"sponsor-emp")]',
            'wait_for': 1
        }

    sponsor_guest_access_register_vendor_btn = \
        {
            'XPATH': '//a[contains(@class,"sponsor-vnd")]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_btn = \
        {
            'XPATH': '//a[contains(@class,"sponsor-gst")]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_name = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_name"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_email = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_email"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_mobile = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_mobile"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_emailpreferred = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_emailcheck"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_mobilepreferred = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_mobilecheck"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_sponsor_name = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_sponsor_name"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_sponsor_mobile = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_sponsor_mobile"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_sponsor_email = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_sponsor_email"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_purpose = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_purpose"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_disclaimer = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_disclaimer"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_register = \
        {
            'XPATH': '//div[@id="guest-registration"]//a[contains(@class,"submit")]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_clear = \
        {
            'XPATH': '//div[@id="guest-registration"]//a[@type="reset"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_sponsorlogin = \
        {
            'XPATH': '//div[@id="guest-registration"]//a[contains(@class,"sponsorLogin")]',
            'wait_for': 1
        }

    sponsor_guest_access_register_guest_registration_status = \
        {
            'XPATH': '//div[@id="guest-registration"]//div[@class="formError form-group"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_employee_registration_status = \
        {
            'XPATH': '//div[@id="employee-registration"]//div[@class="formError form-group"]',
            'wait_for': 1
        }

    sponsor_guest_access_register_vendor_registration_status = \
        {
            'XPATH': '//div[@id="vendor-registration"]//div[@class="formError form-group"]',
            'wait_for': 1
        }

    sponsor_guest_access_login_error_button = \
        {
            'XPATH': '//button[text()="Send anyway"]',
            'wait_for': 1
        }

    sponsor_guest_access_login_success_page = \
        {
            'XPATH': '//font[text()="Welcome, enjoy your free internet!"]',
            'wait_for': 1
        }
    
    social_wifi_access_denied_error= \
        {
            'XPATH': '//*[text()="Access has been denied!"]',
            'wait_for': 1
        }
    
    username_field = \
        {
            'XPATH': '//input[@name="f_user"]',
            'wait_for': 1
        }

    password_field = \
        {
            'XPATH': '//input[@name="f_pass"]',
            'wait_for': 1
        }

    signin_btn = \
        {
            'XPATH': '//form[@class="loginForm"]//a[contains(@class,"submit")]',
            'wait_for': 1
        }

    register_btn = \
        {
            'XPATH': '//a[contains(@class,"submit")]',
            'wait_for': 1
        }

    login_btn = \
        {
            'XPATH': '//a[contains(@class,"logButton")]',
            'wait_for': 1
        }

    clear_btn = \
        {
            'XPATH': '//a[@type="reset"]',
            'wait_for': 1
        }

    registernow_btn = \
        {
            'XPATH': '//a[contains(@class,"regButton")]',
            'wait_for': 1
        }

    login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
            'wait_for': 5
        }

    login_success_page = \
        {
            'XPATH': '//font[text()="Welcome, enjoy your free internet!"]',
            'wait_for': 1
        }

    name_field = \
        {
            'XPATH': '//input[@name="f_name"]',
            'wait_for': 1
        }

    email_field = \
        {
            'XPATH': '//input[@name="f_email"]',
            'wait_for': 1
        }

    mobile_field = \
        {
            'XPATH': '//input[@name="f_mobile"]',
            'wait_for': 1
        }

    emailpreferred_check = \
        {
            'XPATH': '//input[@name="f_emailcheck"]',
            'wait_for': 1
        }

    mobilepreferred_check = \
        {
            'XPATH': '//input[@name="f_mobilecheck"]',
            'wait_for': 1
        }

    registration_status = \
        {
            'XPATH': '//div[@class="formError form-group"]',
            'wait_for': 1
        }

    disclaimer_check = \
        {
            'XPATH': '//input[@name="f_disclaimer"]',
            'wait_for': 1
        }
