

class LoginWebElementsDefinitions:
    login_page_username_text_ids = \
        {
            'DESC': 'Login Page Username TextField',
            'XPATH': "//*[@data-automation-tag='automation-login-page-username-field']",
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
            'wait_for': 5
        }

    login_page_wrong_password_message = {'CSS_SELECTOR': '.wrong-password', 'wait_for': 3}

    logout_account_info = {'CSS_SELECTOR': '.ah-header-account-info', 'wait_for': 5}

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
        'CSS_SELECTOR': '.dijitDialogCloseIcon',
        'XPATH': '//*[@data-dojo-attach-point="closeButtonNode"]',
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
         'XPATH': '//div[@data-dojo-attach-point="drawerContent"]',
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

    close_about_extremecloudiq_dialogue = \
        {
            'XPATH': "//*[@data-dojo-attach-point='drawerTrigger']",
            'wait_for': 5
        }

    login_logo = \
        {
            'XPATH': '//*[@data-dojo-attach-point="dynamicImage"]',
            'wait_for': 5
        }

    welcome_page_option = \
        {
            'XPATH': '//div[@class="WelcomeEdition"]',
            'wait_for': 2
        }

    txt_30_days_trial = \
        {
            'XPATH': '//li[contains(.,"I want to continue with my 30-day trial of ExtremeCloud IQ.")]',
            'wait_for': 5
        }

    txt_extr_license = \
        {
            'XPATH': '//li[contains(.,"I have an ExtremeCloud IQ license")]',
            'wait_for': 5
        }

    txt_legacy_license = \
        {
            'XPATH': '//li[contains(.,"I have a legacy entitlement key.")]',
            'wait_for': 5
        }

    txt_extr_connect = \
        {
            'XPATH': '//li[contains(.,"I\'ll start with ExtremeCloud IQ Connect.")]',
            'wait_for': 5
        }

    trial_30day_login_option = \
        {
            'DESC': 'select trial option',
            'XPATH': '//input[@value="trial"]',
            'wait_for': 2
        }

    extr_cloudiq_license_login_option = \
        {
            'DESC': 'extr cloud iq login option',
            'XPATH': '//input[@value="upgrade"]',
            'wait_for': 2
        }

    legacy_license_login_option = \
        {
            'DESC': 'select legacy option',
            'XPATH': '//*[@data-dojo-attach-point="entitledRadio"]',
            'wait_for': 2
        }

    extr_connect_login_option = \
        {
            'DESC': 'select connect option',
            'XPATH': '//input[@value="express"]',
            'wait_for': 2
        }

    login_trail_30_days = \
        {
            'XPATH': "//*[@data-dojo-attach-point='trialRadio']",
            'wait_for': 5
        }

    login_license_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="upgradeKey"]',
            'wait_for': 5
        }

    login_entitlement_radio = \
        {
            'XPATH': "//*[@data-dojo-attach-point='entitledRadio']",
            'wait_for': 5
        }

    login_entitlement_key = \
        {
            'XPATH': "//*[@data-dojo-attach-point='entitlementKey']",
            'wait_for': 5
        }

    login_year_trail_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yearTrialRadio"]',
            'wait_for': 5
        }

    login_iq_connect = \
        {
            'XPATH': "//*[@data-dojo-attach-point='expressRadio']",
            'wait_for': 5
        }

    get_started_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="nextButton"]',
            'wait_for': 2
        }

    get_next_btn = \
        {
            #'XPATH': '//button[@data-dojo-attach-point="nextButton"]',
            'CSS_SELECTOR': '.WelcomeWizardButton.WelcomeWizardButtonNext.btn-visible',
            'wait_for': 2
        }

    get_finish_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 2
        }

    cloud_tos_popup_submit = \
        {
            'XPATH': '//input[@data-dojo-attach-point="submitButton"]',
            'wait_for': 2
        }

    cloud_tos_popup_agree = \
        {
            'XPATH': '//input[@data-dojo-attach-event="ondijitclick:_onClick" ]',
            'wait_for': 2
        }

    first_tos_header = \
        {
            'XPATH': '//h4[contains(.,"Cloud Terms of Service")]',
            'wait_for': '2'
        }

    second_tos_header = \
        {
            'XPATH': '//h4[contains(.,"Please read and accept the Data Privacy and Protection")]',
            'wait_for': 2
        }

    upgrade_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="upgradeButton"]',
            'wait_for': 2
        }

    upgrade_link = \
        {
            'XPATH': '//a[@data-dojo-attach-point="upgradeLink" and text()="Enter your entitlement key to upgrade now."]',
            'wait_for': 2
        }

    legacy_ek_input_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="entitlementKey"]',
            'wait_for': 2
        }

    legacy_ek_invalid_err = \
        {
            'XPATH': '//h3[@data-dojo-attach-point="textEl"]',
            'wait_for': 3
        }

    extr_license_tooltip = \
        {
            'XPATH': '//div[@class="ui-tipbox-con"][contains(.,"Thank you for purchasing")]',
            'wait_for': 2
        }

    legacy_ek_popup_hdr = \
    {
        'XPATH': '//h4[text()="If you have a Legacy Entitlement Key, enter below:"]',
        'wait_for': 2
    }

    legacy_ek_popup_no_btn = \
        {
            'XPATH': '//button[@class="btn btn-small btn-3"][text()="No"]',
            'wait_for': 2
        }

    legacy_ek_popup_submit_btn = \
        {
            'XPATH': '//button[@class="btn btn-small btn-primary"][text()="Submit"]',
            'wait_for': 2
        }

    sfdc_login_email = \
        {
            'XPATH': '//input[@id="j_id0:j_id20:email"][@type="text"]',
            'wait_for': 2
        }

    sfdc_login_pwd = \
        {
            'XPATH': '//input[@id="j_id0:j_id20:password"][@type="password"]',
            'wait_for': 2
        }

    sfdc_login_btn = \
        {
            'XPATH': '//input[@type="submit"][@value="Log In"]',
            'wait_for': 2
        }

    shared_cuid_hdr = \
        {
            'XPATH': '//h4[text()="Please enter Customer\'s Unique Identifier (CUID)"]',
            'wait_for': 2
        }

    shared_cuid_input = \
        {
            'XPATH': '//input[@class="entitlement-input req"][@type="text"]',
            'wait_for': 2
        }

    shared_cuid_submit_btn = \
        {
            'XPATH': '//button[@class="btn btn-small btn-primary"][@data-dojo-attach-point="saveBtn"]',
            'wait_for': 2
        }

    shared_cuid_cancel_btn = \
        {
            'XPATH': '//button[@class="btn btn-small btn-3"][@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 2
        }

    shared_cuid_error = \
        {
            'XPATH': '//h3[@data-dojo-attach-point="textEl"][text()="Invalid Customer Unique Identifier"]',
            'wait_for': 3
        }

    sfdc_login_error = \
        {
            'XPATH': '//div[@class="messageText"]',
            'wait_for': 2
        }

    terms_accept_terms_btn = \
        {
            'XPATH': "//*[@data-dojo-attach-point='focusNode']",
            'wait_for': 5
        }

    submit_terms_btn = \
        {
            'XPATH': "//*[@data-dojo-attach-point='submitButton']",
            'wait_for': 5
        }

    accept_data_privacy = \
        {
            'XPATH': "//*[@widgetid='data-privacy-accept']",
            'wait_for': 5
        }

    submit_data_privacy = \
        {
            'XPATH': "//*[@data-dojo-attach-point='submitButton']",
            'wait_for': 5
        }

    deploy_cloud_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='cloudButton']",
            'wait_for': 5
        }

    lets_get_started = \
        {
            'XPATH': "//*[@data-dojo-attach-point='getStarted']",
            'wait_for': 5
        }

    welcome_wizard_heading = \
        {
            'XPATH': "//*[@data-dojo-attach-point='headingNode']",
            'wait_for': 5
        }

    agree_checkbox = \
        {
            'CSS_SELECTOR': '.dijit.dijitReset.dijitInline.dijitCheckBox',
            'wait_for': 5
        }

    salesforce_username = \
        {
            'XPATH': "//*[@type='text']",
            'wait_for': 5
        }

    salesforce_password = \
        {
            'XPATH': "//*[@type='password']",
            'wait_for': 5
        }

    salesforce_submit = \
        {
            'XPATH': "//*[@type='submit']",
            'wait_for': 5
        }

    entitlement_key_error = \
        {
            'XPATH': '//*[@class="ui-tipbox-con"][contains(.,"This entitlement key has already been used by another system")]',
            'wait_for': 2
        }

    enter_shared_cuid = \
        {
            'XPATH': '//div[@class="entitlement-ctn"]//input[@data-dojo-attach-point="cuidKey"]',
            'wait_for': 3,
        }

    check_error_shared_cuid = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//div[@data-dojo-attach-point="wrapEl"]//*[@class="ui-tipbox-title"]',
            'wait_for': 3,
        }

    submit_shared_cuid = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 3,
        }

