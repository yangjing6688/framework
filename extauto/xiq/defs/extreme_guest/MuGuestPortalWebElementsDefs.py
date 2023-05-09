class MuGuestPortalWebElementsDefs:
    social_wifi_all_facebook_icon = \
        {
            'XPATH': '//a[@data-connect="facebook"]',
        }

    social_wifi_all_facebook_username_field = \
        {
            'NAME': 'email',
        }

    social_wifi_all_facebook_password_field = \
        {
            'NAME': 'pass',
        }

    social_wifi_all_facebook_login_button = \
        {
            'NAME': 'login',
        }

    social_wifi_all_facebook_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
        }

    social_wifi_all_login_success_page = \
        {
            'XPATH': '//font[text()="Welcome, enjoy your free internet!"]',
        }

    social_wifi_max_count_error = \
        {
            'XPATH': '//div[text()="Max count(1) of devices supported per user exceeded. Please contact administrator."]',
        }

    social_wifi_all_google_icon = \
        {
            'XPATH': '//a[@data-connect="google"]',
        }

    social_wifi_all_linkedin_icon = \
        {
            'XPATH': '//a[@data-connect="linkedin"]',
        }

    social_wifi_all_linkedin_username_field = \
        {
            'NAME': 'session_key',
        }

    social_wifi_all_linkedin_password_field = \
        {
            'NAME': 'session_password',
        }

    social_wifi_all_linkedin_signin_button = \
        {
            'CSS_SELECTOR': '.btn__primary--large',
        }

    social_wifi_all_linkedin_allow_button = \
        {
            'NAME': 'action',
        }

    social_wifi_all_linkedin_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
        }

    social_wifi_all_google_username_field = \
        {
            'NAME': 'identifier',
        }

    social_wifi_all_google_next_button = \
        {
            'XPATH': '//span[text()="Next"]',
        }

    social_wifi_all_google_username_next_button = \
        {
            'ID': 'identifierNext',
        }

    social_wifi_all_google_password_next_button = \
        {
            'ID': 'passwordNext',
        }

    social_wifi_all_google_password_field = \
        {
            'NAME': 'password',
        }

    social_wifi_all_google_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
        }

    user_registration_social_wifi_username_field = \
        {
            'XPATH': '//input[@name="f_user"]',
        }

    user_registration_social_wifi_passcode_field = \
        {
            'XPATH': '//input[@name="f_pass"]',
        }

    user_registration_social_wifi_signin_button = \
        {
            'XPATH': '//a[text()="Sign In"]',
        }

    user_registration_social_wifi_login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
        }

    default_template_page_company_logo = \
        {
            'XPATH': '//img[contains(@src, "media")]',
        }

    default_template_page_acceptandconnect_button = \
        {
            'XPATH': '//a[text()=" ACCEPT & CONNECT "]',
        }

    sponsor_guest_access_username_field = \
        {
            'XPATH': '//input[@name="f_user"]',
        }

    sponsor_guest_access_password_field = \
        {
            'XPATH': '//input[@name="f_pass"]',
        }

    sponsor_guest_access_signin_btn = \
        {
            'XPATH': '//form[@class="loginForm"]//a[contains(@class,"submit")]',
        }

    sponsor_guest_access_clear_btn = \
        {
            'XPATH': '//a[@type="reset"]',
        }

    sponsor_guest_access_registernow_btn = \
        {
            'XPATH': '//a[contains(@class,"regButton")]',
        }

    sponsor_guest_access_register_employee_btn = \
        {
            'XPATH': '//a[contains(@class,"sponsor-emp")]',
        }

    sponsor_guest_access_register_vendor_btn = \
        {
            'XPATH': '//a[contains(@class,"sponsor-vnd")]',
        }

    sponsor_guest_access_register_guest_btn = \
        {
            'XPATH': '//a[contains(@class,"sponsor-gst")]',
        }

    sponsor_guest_access_register_guest_name = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_name"]',
        }

    sponsor_guest_access_register_guest_email = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_email"]',
        }

    sponsor_guest_access_register_guest_mobile = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_mobile"]',
        }

    sponsor_guest_access_register_guest_emailpreferred = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_emailcheck"]',
        }

    sponsor_guest_access_register_guest_mobilepreferred = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_mobilecheck"]',
        }

    sponsor_guest_access_register_guest_sponsor_name = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_sponsor_name"]',
        }

    sponsor_guest_access_register_guest_sponsor_mobile = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_sponsor_mobile"]',
        }

    sponsor_guest_access_register_guest_sponsor_email = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_sponsor_email"]',
        }

    sponsor_guest_access_register_guest_purpose = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_purpose"]',
        }

    sponsor_guest_access_register_guest_disclaimer = \
        {
            'XPATH': '//div[@id="guest-registration"]//input[@name="f_disclaimer"]',
        }

    sponsor_guest_access_register_guest_register = \
        {
            'XPATH': '//div[@id="guest-registration"]//a[contains(@class,"submit")]',
        }

    sponsor_guest_access_register_guest_clear = \
        {
            'XPATH': '//div[@id="guest-registration"]//a[@type="reset"]',
        }

    sponsor_guest_access_register_guest_sponsorlogin = \
        {
            'XPATH': '//div[@id="guest-registration"]//a[contains(@class,"sponsorLogin")]',
        }

    sponsor_guest_access_register_guest_registration_status = \
        {
            'XPATH': '//div[@id="guest-registration"]//div[@class="formError form-group"]',
        }

    sponsor_guest_access_register_employee_registration_status = \
        {
            'XPATH': '//div[@id="employee-registration"]//div[@class="formError form-group"]',
        }

    sponsor_guest_access_register_vendor_registration_status = \
        {
            'XPATH': '//div[@id="vendor-registration"]//div[@class="formError form-group"]',
        }

    sponsor_guest_access_login_error_button = \
        {
            'XPATH': '//button[text()="Send anyway"]',
        }

    sponsor_guest_access_login_success_page = \
        {
            'XPATH': '//font[text()="Welcome, enjoy your free internet!"]',
        }
    
    social_wifi_access_denied_error= \
        {
            'XPATH': '//*[text()="Access has been denied!"]',
        }
    
    username_field = \
        {
            'XPATH': '//input[@name="f_user"]',
        }

    password_field = \
        {
            'XPATH': '//input[@name="f_pass"]',
        }

    signin_btn = \
        {
            'XPATH': '//form[@class="loginForm"]//a[contains(@class,"submit")]',
        }

    register_btn = \
        {
            'XPATH': '//a[contains(@class,"submit")]',
        }

    login_btn = \
        {
            'XPATH': '//a[contains(@class,"logButton")]',
        }

    clear_btn = \
        {
            'XPATH': '//a[@type="reset"]',
        }

    registernow_btn = \
        {
            'XPATH': '//a[contains(@class,"regButton")]',
        }

    login_error_page = \
        {
            'XPATH': '//button[text()="Send anyway"]',
        }

    login_success_page = \
        {
            'XPATH': '//font[text()="Welcome, enjoy your free internet!"]',
        }

    name_field = \
        {
            'XPATH': '//input[@name="f_name"]',
        }

    email_field = \
        {
            'XPATH': '//input[@name="f_email"]',
        }

    mobile_field = \
        {
            'XPATH': '//input[@name="f_mobile"]',
        }

    emailpreferred_check = \
        {
            'XPATH': '//input[@name="f_emailcheck"]',
        }

    mobilepreferred_check = \
        {
            'XPATH': '//input[@name="f_mobilecheck"]',
        }

    registration_status = \
        {
            'XPATH': '//div[@class="formError form-group"]',
        }

    disclaimer_check = \
        {
            'XPATH': '//input[@name="f_disclaimer"]',
        }
