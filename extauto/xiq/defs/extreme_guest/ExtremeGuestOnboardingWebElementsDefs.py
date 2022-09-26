class ExtremeGuestOnboardingWebElementsDefs:
    extreme_guest_onboarding_policy_tab = \
        {
            'XPATH': '(//span[text()="Policy"])[2]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_policy = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-custom-component-add")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_refresh_policy = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-custom-component-refresh")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_delete_policy = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-custom-component-delete")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_name = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-policy-name")]//input',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_condition_dropdown = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-policy-criteria-condition")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_condition_dropdown_existing = \
        {
            'XPATH': '(//div[contains(@data-automation-tag, "eguest-onboarding-policy-criteria-condition")])[4]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_condition_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_condition_dropdown_value = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-policy-criteria-condition-value")]//input',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_action_dropdown = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-policy-criteria-action")]',
            'wait_for': 1
        }
    extreme_guest_onboarding_policy_add_action_dropdown_existing = \
        {
            'XPATH': '(//div[contains(@class, "x-form-text-wrap x-form-text-wrap-select-box")])[7]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_action_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_group_select_dropdown = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-policy-criteria-group-select")]',
            'wait_for': 1
        }
    extreme_guest_onboarding_policy_add_group_select_dropdown_existing = \
        {
            'XPATH': '(//div[contains(@class, "x-form-text-wrap x-form-text-wrap-select-box")])[8]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_group_select_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_usernotifpolicy_select_dropdown = \
        {
            'XPATH': '(//div[contains(@class, "x-form-trigger x-form-trigger-select-box x-form-arrow-trigger x-form-arrow-trigger-select-box")])[4]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_usernotifpolicy_select_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_spnotifpolicy_select_dropdown = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-policy-criteria-notify-sponsor")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_spnotifpolicy_select_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_save_button = \
        {
            'XPATH': '//span[text()="Save"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_cancel_button = \
        {
            'XPATH': '//span[text()="Cancel"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_add_save_ok_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-popup-message-OK")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_policy_close_button = \
        {
            'XPATH': '(//div[contains(@data-automation-tag, "eguest-popup-message-OK")])[2]',
            'wait_for': 2
        }

    extreme_guest_onboarding_rule_tab = \
        {
            'XPATH': '//span[text()="Rules"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_rule = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-rules-add-btn")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_name_add_rule_existing = \
        {
            'XPATH': '//span[text()="auto_eguest_onboarding_policy0"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_name_add_rule = \
        {
            'XPATH': '(//div[contains(@class, "x-tool-tool-el x-tool-img x-tool-plus")])[2]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_name = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-rules-form-name")]//input',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_policy_dropdown = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-rules-form-policy")]//div',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_policy_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_network_dropdown = \
        {
            'XPATH': '(//div[contains(@class, "x-form-arrow-trigger")])[3]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_network_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_location_dropdown = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-rules-form-location")]//div',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_location_dropdown_items = \
        {
            'XPATH': '//span[text()="Extreme Networks"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_save_button = \
        {
            'XPATH': '//span[text()="Save"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_cancel_button = \
        {
            'XPATH': '//span[text()="Cancel"]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_save_exists_button = \
        {
            'XPATH': '//div[contains(text(),"already exists")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_add_save_exists_button = \
        {
            'XPATH': '//div[contains(text(),"already exists")]',
            'wait_for': 5
        }

    extreme_guest_onboarding_rule_add_save_ok_button = \
        {
            'XPATH': '(//div[contains(@data-automation-tag, "eguest-popup-message-OK")])[1]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_refresh_rule = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-rules-refresh-btn")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_delete_rule = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-onboarding-rules-delete-btn")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_root_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]/ancestor::tr',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_city_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]/ancestor::tr',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_building_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]/ancestor::tr',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_floor_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-4")]/ancestor::tr',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_root_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_city_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 1
        }

    extreme_guest_onboarding_rule_locations_building_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 1
        }

    extreme_guest_users_add_create_bulk_vouchers_location_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-users-bulkvoucher-location-tree"]'
                     '//div[contains(@class, "x-form-arrow-trigger")]',
            'wait_for': 1
        }