class WirelessNetworksDefinitions:

    wireless_nw_tab_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tab-wireless-networks"]',
            'wait_for': 10
        }

    wireless_nw_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            
        }

    wireless_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    wireless_nw_tab_page = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wirelessConnectivityContainer"]',
            'wait_for': 5
        }

    wireless_nw_add_button = \
        {
         'XPATH': '//div[@data-automation-tag="automation-wireless-networks-grid"]//span[@data-tip="Add"]',
         'wait_for': 5
         }

    guest_access_nw_menu_item = \
        {
         'XPATH': '//div[@data-automation-tag="automation-wireless-networks-grid"]'
                  '//li/a[contains(text(), "Guest Access Network (simplified)")]',
         'wait_for': 2
         }

    all_other_nw_menu_item = \
        {
            'XPATH': '//li[@type="createadvancedssid"]/a[contains(text(), "All Other Networks (standard)")]',
            'wait_for': 5
        }

    wireless_ssid_name_input_field = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ssid-details-ssid-name"]',
            'wait_for': 5
        }

    wireless_broadcast_ssid_name_input_field = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ssid-details-ssid-broadcast-name"]',
            'wait_for': 1
        }

    wireless_ssid_auth_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidTab"]//a[contains(text(), "SSID AUTHENTICATION")]',
            'wait_for': 1
        }
    wireless_select_enterprise_ssid_auth = \
        {
            'CLASS_NAME': 'ui-select-card-title',
            'wait_for': 1
        }

    wireless_select_ppsk_ssid_auth = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ssid-auth-ppsk"]',
            'wait_for': 1
        }

    wireless_select_personal_ssid_auth = \
        {
            'CLASS_NAME': 'ui-select-card-title',
            'index': 1,
            'wait_for': 1
        }

    wireless_select_enhanced_ssid_auth = \
        {
            'CLASS_NAME': 'ui-select-card-title',
            'index': 4,
            'wait_for': 1
        }

    transition_mode_for_2ghz_and_5ghz = \
        {
            'XPATH': '//input[@data-automation-tag="ssid-details-access-security-owe-transition-mode"]',
            'wait_for': 5
        }

    wireless_select_open_ssid_auth = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ssid-auth-open-access"]',
            'wait_for': 1
        }

    wireless_wifi0_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bandng"]',
            'wait_for': 1
        }

    wireless_wifi1_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bandna"]',
            'wait_for': 1
        }

    key_management_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ssid-details-access-security-key-mgmt-chzn-arrow-down"]',
            'wait_for': 5,
            'index': 0
        }

    key_management_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-keymanagement")]//li',
            'wait_for': 5
        }

    encryption_method_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ssid-details-access-security-encr-method-chzn-arrow-down"]',
            'wait_for': 5,
        }

    encryption_key_method_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-encryptionmethod")]//li',
            'wait_for': 5
        }

    auth_with_extiq_auth_service_slider_button = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="enableIdm"]',
            'wait_for': 5
        }

    wireless_network_save_button = \
        {
            'XPATH': '//button[@data-automation-tag="ssid-details-save-button"]',
            'wait_for': 5,
        }

    open_template_cloud_cwp_radio_button = \
        {
            'NAME': 'cwpCategory',
            'wait_for': 1
        }

    policy_enable_captive_web_portal_button = \
        {
            'NAME': 'enableCwp',
            'wait_for': 1
        }

    max_num_of_clients_per_ppsk_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableMaxClientsPerPpsk"]',
            'wait_for': 5
        }

    max_num_of_clients_per_ppsk_input_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="maxClientsPerPpsk"]',
            'wait_for': 5
        }

    ppsk_classification_use_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enablePpskGroup"]',
            'wait_for': 5
        }

    pcg_use_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enablePCG"]',
            'wait_for': 5
        }

    ap_based_radio_button = \
        {
            'XPATH': '//*[@id="apBasedPCG"]',
            'wait_for': 5
        }

    key_based_radio_button = \
        {
            'XPATH': '//*[@data-automation-tag="ssid-details-access-security-key-based-pcg"]',
            'wait_for': 5
        }

    personal_wpa2_key_type_drop_down_section = \
        {
            'XPATH': '//*[@data-dojo-attach-point="keyType"]',
            'wait_for': 1
        }

    personal_wpa2_key_type_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ssid-details-access-security-key-type-chzn-arrow-down"]',
            'wait_for': 5
        }

    personal_wpa2_key_value_input_field_section = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wpa2KeyValueArea"]',
            'wait_for': 5
        }

    personal_wpa2_key_value_input_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wpa2KeyValueArea"]//input[@data-validid="keyVal.norEl"]',
            'wait_for': 5
        }

    personal_wpa2_key_type_options = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-ssid-details-access-security-key-type-chzn-results-ctn"]'
                     '//li',
            'wait_for': 5
        }

    sae_group_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ssid-details-access-security-sae-group-chzn-arrow-down"]',
            'wait_for': 5,
        }

    sae_group_options = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ssid-details-access-security-sae-group-chzn-results-ctn"]//li',
            'wait_for': 5,
        }

    transition_mode_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saeTransitionMode"]',
            'wait_for': 1
        }

    personal_wpa3_key_value_input_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wpa3KeyValueArea"]//input[@data-dojo-attach-point="norEl"]',
            'wait_for': 5
        }

    anti_logging_threshold = \
        {
            'XPATH': '//*[@data-dojo-attach-point="antiLoggingThreshold"]',
            'wait_for': 5
        }

    wireless_ssid_list = \
        {
            'CSS_SELECTOR': '.wireless-ssid-container .dgrid-row',
            'wait_for': 15
        }

    wireless_chkbox = \
        {
            'CSS_SELECTOR': '.wireless-ssid-container .dgrid-row .dgrid-selector',
            'wait_for': 5
        }

    wireless_delete_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-wireless-ssids-remove-btn"]',
            'wait_for': 5
        }

    wireless_re_use_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-wireless-ssids-reusable-btn"]',
            'wait_for': 5
        }

    wireless_re_use_delete_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-reusable-grid"]//span[@data-tip="Delete"]',
            'wait_for': 5,
        }

    wireless_re_use_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5,
        }

    confirm_dialog_yes_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 5
        }

    wireless_nw_select_button = \
        {
         'XPATH': '//div[@data-automation-tag="automation-wireless-networks-grid"]//span[@data-tip="Select"]',
         'wait_for': 5
         }

    wireless_nw_select_ssid_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-reusable-grid"]//table[@class="dojoxGridRowTable"]',
            'wait_for': 5
        }

    wireless_select_ssid_row_check_box = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'wait_for': 5
        }

    wireless_ssid_select_option_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 5
        }

    wireless_ssid_select_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    wireless_wifi2_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bandx"]',
            'wait_for': 1
        }

    wireless_wifi2_checkbox_dialog_yes_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="msgWrap"]//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 1
        }
