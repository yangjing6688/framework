class MuCPWebElementDefinitions:
    user_acceptance_page_accept_button = \
        {
            'CSS_SELECTOR': '.btn.acceptButton',
            'wait_for': 1
        }
    user_acceptance_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.cancelButton',
            'wait_for': 1
        }

    self_registration_user_first_name = \
        {
            'NAME': 'firstname',
            'wait_for': 1
        }

    self_registration_user_last_name = \
        {
            'NAME': 'lastname',
            'wait_for': 1
        }

    self_registration_user_email_id = \
        {
            'NAME': 'email',
            'wait_for': 1
        }

    self_registration_user_country_code_drop_down = \
        {
            'ID': 'ccode',
            'wait_for': 1
        }

    self_registration_user_phone_number = \
        {
            'NAME': 'phoneNumber',
            'wait_for': 1
        }

    self_registration_user_visiting_person_email = \
        {
            'NAME': 'visiting',
            'wait_for': 1
        }

    self_registration_user_registration_button = \
        {
            'CSS_SELECTOR': '.btn.button',
            'wait_for': 1
        }

    self_user_registration_status = \
        {
            'CSS_SELECTOR': '.ui-tipbox-title.tips',
            'wait_for': 1
        }

    user_registration_reply_msg = \
        {
            'XPATH': '//div[@id="replymsg"]',
            'wait_for': 2
        }

    user_registration_field_err = \
        {
            'XPATH': '//div[@class="field error"]',
            'wait_for': 2
        }

    ppsk_passcode = \
        {
            'ID': 'ppsk_pwd',
            'wait_for': 1
        }

    social_login_accept_condition_checkbox = \
        {
            'XPATH': '//*[@id="accept-tou"]',
            'wait_for': 2
        }

    social_login_accept_condition_checkbox1 = \
        {
            'ID': 'accept-tou',
            'wait_for': 2
        }

    social_login_with_facebook_button = \
        {
            'CSS_SELECTOR': '.signin-button-facebook',
            'wait_for': 2
        }

    social_login_with_facebook_username_field = \
        {
            'NAME': 'email',
            'wait_for': 2
        }

    social_login_with_facebook_password_field = \
        {
            'NAME': 'pass',
            'wait_for': 2
        }

    social_login_with_facebook_login_button = \
        {
            'NAME': 'login',
            'wait_for': 2
        }

    social_login_with_google_button = \
        {
            'CSS_SELECTOR': '.signin-button-google',
            'wait_for': 2
        }

    social_login_with_google_username_field = \
        {
            'NAME': 'identifier',
            'wait_for': 2
        }

    social_login_with_google_next_button = \
        {
            'ID': '//*[contains(text(),"Next")]',
            'wait_for': 2
        }

    social_login_with_google_username_next_button = \
        {
            'ID': 'identifierNext',
            'wait_for': 2
        }

    social_login_with_google_password_next_button = \
        {
            'ID': 'passwordNext',
            'wait_for': 2
        }


    social_login_with_google_password_field = \
        {
            'NAME': 'password',
            'wait_for': 2
        }

    social_login_with_linkedin_button = \
        {
            'CSS_SELECTOR': '.signin-button-linkedin',
            'wait_for': 1
        }

    social_login_with_linkedin_username_field = \
        {
            'NAME': 'session_key',
            'wait_for': 2
        }

    social_login_with_linkedin_password_field = \
        {
            'NAME': 'session_password',
            'wait_for': 2
        }

    social_login_signin_linkedin_button = \
        {
            'CSS_SELECTOR': '.btn__primary--large',
            'wait_for': 3
        }

    social_login_allow_linkedin_button = \
        {
            'NAME': 'action',
            'wait_for': 1
        }

    guest_access_user_name = \
        {
            'NAME': 'username',
            'wait_for': 1
        }

    guest_access_user_passwd = \
        {
            'NAME': 'password',
            'wait_for': 1
        }

    guest_access_login_button = \
        {
            'CSS_SELECTOR': '.btn.button',
            'wait_for': 1,
            'index': 0
        }

    guest_access_registration_button = \
        {
            'CSS_SELECTOR': '.btn.button',
            'wait_for': 1,
            'index': 1
        }

    registration_error_reason = \
        {
            'ID': 'reason',
            'wait_for': 2
        }

    email_id_to_get_pin = \
        {
            'ID': 'emailAddress',
            'wait_for': 2
        }

    accept_terms_cond_check_box = \
        {
            'ID': 'accept-tou',
            'wait_for': 2
        }

    submit_button = \
        {
            'CSS_SELECTOR': '.btn.btn-primary.btn-lg',
            'wait_for': 1,
        }

    pin_email_sent_success_text_area = \
        {
            'ID': 'email-sent',
            'wait_for': 2
        }

    pin_field = \
        {
            'ID': 'pin',
            'wait_for': 2
        }

    pin_not_valid_text_area = \
        {
            'ID': 'pin-not-valid',
            'wait_for': 2
        }

    cloud_pin_success_page = \
        {
            'CSS_SELECTOR': '.success.message',
            'wait_for': 1,
        }

    cwp_success_page = \
        {
            'CSS_SELECTOR': '.message-area',
            'wait_for': 1,
        }

    social_login_terms_and_condition_link = \
        {
            'XPATH': '//*[@id="termsLink"]',
            'wait_for': 2
        }

    social_login_terms_and_condition_page_text = \
        {
            'CSS_SELECTOR': '.modal-content',
            'wait_for': 2
        }

    social_login_terms_and_condition_close_button = \
        {
            'CSS_SELECTOR': '.btn.btn-secondary',
            'wait_for': 2
        }