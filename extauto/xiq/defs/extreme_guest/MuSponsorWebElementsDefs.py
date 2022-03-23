class MuSponsorWebElementsDefs:
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
            'XPATH': '//a[contains(@class,"submit")]',
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