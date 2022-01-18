class NPExpressPolicySetupDefinitions:
    card_view = \
        {'XPATH': '//div//span[@data-automation-tag="automation-config-card"]',
         'wait_for': 5
         }

    list_view = {'CSS_SELECTOR': '.card-icons-list', 'wait_for': 5}

    new_account_express_policy_setup_button = \
        {'XPATH': '//button[@data-dojo-attach-point="noPolicyAddPackage"]',
         'wait_for': 5
         }

    network_policy_list = {'CSS_SELECTOR': '.card-item-title', 'wait_for': 5}

    network_policy_card_item = {'CSS_SELECTOR': '.card-item-static', 'wait_for': 5}

    express_policy_setup_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-config-cards-add-express']",
            'wait_for': 5
        }

    policy_name_text = {'CSS_SELECTOR': '.policy-name', 'wait_for': 5}

    network_toggle_checkbox = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="networkToggle"]',
            'wait_for': 5
         }

    auth_type_drop_down = \
        {
            'XPATH': '//div/select[@data-dojo-attach-point="ssidType"]/..//a',
            'wait_for': 5
        }

    auth_type_drop_down_options = \
        {
            'XPATH': '//div//ul[contains(@class, "qa-chzn-results-ssidtype")]//li',
            'wait_for': 2
        }

    auth_type_drop_down_auth_elements = {'CSS_SELECTOR': '.active-result', 'wait_for': 5}

    ssid_name_text_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="createContent"]//input[@data-dojo-attach-point="ssidName"]',
            'wait_for': 2
        }

    cwp_checkbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="cwpToggle"]',
            'wait_for': 2
        }

    cwp_name_text_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="createContent"]//input[@data-dojo-attach-point="cwpName"]',
            'wait_for': 2
        }

    express_policy_create_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="createBtn"]',
            'wait_for': 2
        }

    express_policy_create_dialog_done_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    express_policy_cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }
