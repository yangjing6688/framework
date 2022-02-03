class ExtremeGuestSplashTemplateWebElementsDefs:
    extreme_guest_system_template_tab = \
        {
            'XPATH': '//span[text()="System Templates"]',
            'wait_for': 5
        }

    extreme_guest_user_template_tab = \
        {
            'XPATH': '//span[text()="User Templates"]',
            'wait_for': 5
        }

    extreme_guest_clone_accept_connect_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Accept_and_Connect") and not(contains(@class, '
                     '"eguest-dataview-Accept_and_Connect_with_terms_and_agreement"))]//a',
            'wait_for': 5
        }

    extreme_guest_clone_accept_and_connect_with_terms_and_agreement_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Accept_and_Connect_with_terms_and_agreement")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_device_registration_with_social_wifi_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Device_Registration_with_Social_WiFi")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_email_access_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Email_Access")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_social_wifi_with_facebook_and_googleplus_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Social_WiFi_with_Facebook_and_GooglePlus")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_social_wifi_with_all_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Social_WiFi_with_all")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_sponsored_guest_access_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-Sponsored_Guest_Access")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_user_reg_with_social_forgot_passcode_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-User_Reg_With_Social_Forgot_Passcode")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_user_registration_with_social_wifi_icon = \
        {
            'XPATH': '//div[contains(@class, "eguest-dataview-User_Registration_with_Social_WiFi")]//a',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_name_textbox = \
        {
            'XPATH': '//input[contains(@name, "name")]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_landing_tab = \
        {
            'XPATH': '//span[text()="Landing"]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_welcome_tab = \
        {
            'XPATH': '//span[text()="Welcome"]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_dropdown_icon = \
        {
            'XPATH': '//span[text()="+"]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_dropdown_login_item = \
        {
            'XPATH': '//span[text()="Login"]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_dropdown_failure_item = \
        {
            'XPATH': '//span[text()="Failure"]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_widget_icon = \
        {
            'XPATH': '//span[contains(@class, "x-btn-text")]/span[contains(@class, "fa-widget")]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_save_icon = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-splash-edittemplate-save-btn")]//span[contains(@class, "x-btn-glyph")]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_preview_icon = \
        {
            'XPATH': '//[contains(@data-qtip, "Preview")]//span[contains(@class, "x-btn-glyph")]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_cancel_icon = \
        {
            'XPATH': '//a[contains(@data-qtip, "Cancel")]//span[contains(@class, "x-btn-glyph")]',
            'wait_for': 5
        }

    extreme_guest_clone_system_template_theme_field = \
        {
            'XPATH': '//div[contains(@style, "height: 705px")]//div[contains(@data-ref, "innerCt")]',
            'wait_for': 5
        }

    extreme_guest_user_accept_connect_template_apply_icon = \
        {
            'XPATH': '//b[text()="accept_connect_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_accept_connect_terms_template_apply_icon = \
        {
            'XPATH': '//b[text()="accept_connect_terms_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_dev_reg_social_template_apply_icon = \
        {
            'XPATH': '//b[text()="dev_reg_social_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_email_access_template_apply_icon = \
        {
            'XPATH': '//b[text()="email_access_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_social_wifi_fb_gle_template_apply_icon = \
        {
            'XPATH': '//b[text()="social_wifi_fb_gle_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_social_wifi_all_template_apply_icon = \
        {
            'XPATH': '//b[text()="social_wifi_all_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_sponsored_guest_template_apply_icon = \
        {
            'XPATH': '//b[text()="sponsored_guest_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_user_reg_social_forgot_pass_template_apply_icon = \
        {
            'XPATH': '//b[text()="user_reg_social_forgot_pass_template"]/parent::*/parent::div//a[contains(@class, '
                     '"apply")]',
            'wait_for': 5
        }

    extreme_guest_user_user_reg_social_wifi_template_apply_icon = \
        {
            'XPATH': '//b[text()="user_reg_social_wifi_template"]/parent::*/parent::div//a[contains(@class, "apply")]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_dropdown = \
        {
            'XPATH': '(//div[contains(@class, "x-form-arrow-trigger")])[3]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_dropdown_new = \
        {
            'XPATH': '(//span[text()= "Network:"])[2]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_dropdown_items = \
        {
            'XPATH': '(//div[contains(@class, "x-boundlist-list-ct")]//ul)[2]//li',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_dropdown_items_new = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_location_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="eguest-splash-applytemplate-location-tree"]//div[contains(@class, '
                     '"x-form-arrow-trigger")]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_location_dropdown_item = \
        {
            'XPATH': '//*[@data-automation-tag="eguest-splash-applytemplate-location-tree"]//div[contains(@class, '
                     '"x-form-arrow-trigger")]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_add_button = \
        {
            'XPATH': '//span[text()="Add"]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_delete_button = \
        {
            'XPATH': '//div[@data-qtip="Delete"]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_apply_button = \
        {
            'XPATH': '//span[text()="Apply"]',
            'wait_for': 5
        }

    extreme_guest_user_test_template_apply_network_apply_ok_button = \
        {
            'XPATH': '//span[text()="OK"]',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_root_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_root_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]/preceding-sibling::div[contains('
                     '@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_city_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_city_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_building_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_building_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_apply_user_template_locations_floor_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-4")]/ancestor::tr',
            'wait_for': 5
        }