class WipsWebElementDefinitions:
    network_policy_additional_settings_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='additionalSettingsPage']",
            'wait_for': 2
        }

    network_policy_additional_settings_wips_menu_option = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-WIPS']",
            'wait_for': 2
        }

    network_policy_additional_settings_security_option = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-titleSECURITY']",
            'wait_for': 2
        }

    network_policy_additional_settings_enable_wips_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-wips']",
            'wait_for': 2
        }

    network_policy_additional_settings_wips_name_field = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-name']",
            'wait_for': 2
        }

    network_policy_additional_settings_wips_description_field = \
        {
            'XPATH': "//*[@data-dojo-attach-point='description']",
            'wait_for': 2
        }

    wips_rogue_ap_detection_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-enable-ap-detection']",
            'wait_for': 2
        }

    determine_wips_enable_same_network_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-enable-same-network']",
            'wait_for': 2
        }


    wips_rogue_ap_mac_oui_detection_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-enable-mac-oui-detect']",
            'wait_for': 2
        }

    wips_rogue_ap_mac_oui_detection_add_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'index': 5,
            'wait_for': 2
        }

    wips_rogue_ap_mac_oui_detection_delete_button = \
        {
            'XPATH': '//*[@id="ah/util/form/Grid_12"]/div[1]/div[2]/span[2]',
            'wait_for': 2
        }

    wips_select_mac_ouis_of_wireless_add_sign = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'index': 2,
            'wait_for': 2
        }

    wips_mac_oui_add_sign = \
        {
            'CSS_SELECTOR': '.ui-ip-sta.ui-ip-save',
            'wait_for': 2
        }

    wips_mac_oui_delete_symbol_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-remove',
            'index': 4,
            'wait_for': 5
        }

    wips_mac_oui_name_textfield = \
        {
            'CSS_SELECTOR': '.w200',
            'wait_for': 2
        }

    wips_mac_oui_textfield = \
        {
            'XPATH': "//*[@data-automation-tag='macOui']",
            'wait_for': 2
        }

    wips_mac_oui_save_button = \
        {
            'XPATH': "//*[@data-automation-tag='saveBtn']",
            'wait_for': 2
        }

    wips_mac_oui_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-cancel',
            'index': 3,
            'wait_for': 2
        }

    wips_add_mac_oui_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='addMacOuiButton']",
            'wait_for': 2
        }

    wips_enable_rogue_ssid_detection_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-enable-ssid-detect']",
            'wait_for': 2
        }

    wips_enable_rogue_ssid_detection_add_sign_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'index': 3,
            'wait_for': 2
        }

    wips_select_ssid_radio_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-ssid-type-ssid-profile']",
            'wait_for': 2
        }

    wips_enter_ssid_name_radio_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ssidEntryArea"]//input[@data-dojo-attach-point="ssidType-ssid"]',
            'wait_for': 2
        }

    wips_enter_ssid_name_text_field = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-ssid']",
            'wait_for': 2
        }

    wips_select_ssid_encryption_type_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableCheckSsidEncryptionType']",
            'wait_for': 2
        }

    wips_select_ssid_encryption_scroll_button = \
        {
            'XPATH': '//span[contains(text(),"Open - Unsecured")]',
            'wait_for': 3
        }

    wips_select_ssid_encryption_scroll_all_items = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-ssidencryptiontype',
            'wait_for': 5
        }

    wips_select_ssid_encryption_scroll_get_name = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    wips_select_ssid_encryption_add_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-add-ssid-button']",
            'wait_for': 2
        }

    wips_enable_rogue_ssid_detection_delete_button = \
        {
            'XPATH': '//*[@id="ah/util/form/Grid_13"]/div[1]/div[2]/span[2]',
            'wait_for': 2
        }

    wips_enable_adhoc_network_detection_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-enable-ad-hoc']",
            'wait_for': 2
        }

    wips_enable_rogue_client_reporting_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wips-enable-client-reporting']",
            'wait_for': 2
        }

    wips_mitigation_mode_manual_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mode-semiAuto']",
            'wait_for': 2
        }

    wips_mitigation_mode_automatic_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mode-Auto']",
            'wait_for': 2
        }

    wips_save_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-save-button']",
            'wait_for': 2
        }

    wips_select_mac_oui_scroll_button = \
        {
            'CSS_SELECTOR': '.ui-ip-mark.ui-ip-inactive',
            'wait_for': 5
        }

    wips_select_mac_oui_scroll_all_items = \
        {
            'CSS_SELECTOR': '.ui-ip-list-item',
            'wait_for': 5
        }

    wips_select_mac_oui_scroll_get_name = \
        {
            'CSS_SELECTOR': '.J-ip-item',
            'wait_for': 5
        }

    wips_mac_oui_select_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector.dijitReset.dijitInline.dijitCheckBox',
            'wait_for':    2
        }

    wips_mac_oui_grid_rows = \
        {
            'CLASS_NAME': 'dojoxGridRow',
            'wait_for': 10
         }

    wips_mac_oui_select_all_checkbox_list = \
        {
            'ID': 'ah/util/AHGrid_23_rowSelector_-1',
            'wait_for': 2
        }

    network_policy_back_list_link = \
        {
            'XPATH': '//a[contains(text(),"Network Policies")]',
            'wait_for': 3
        }

    wips_common_object_policy_name_textfield = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-name']",
            'wait_for': 2
        }

    wips_common_object_policy_description_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='description']",
            'wait_for': 2
        }

    wips_common_object_policy_rogue_ap_detection_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-ap-detection']",
            'wait_for': 2
        }

    wips_common_object_policy_enable_same_network_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-same-network']",
            'wait_for': 2
        }

    wips_common_object_policy_rogue_ap_mac_oui_detection_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-mac-oui-detect']",
            'wait_for': 2
        }

    wips_common_object_policy_enable_rogue_ssid_detection_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-ssid-detect']",
            'wait_for': 2
        }

    wips_common_object_policy_enable_adhoc_network_detection_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-ad-hoc']",
            'wait_for': 2
        }

    wips_common_object_policy_enable_rogue_client_reporting_checkbox = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-client-reporting']",
            'wait_for': 2
        }

    wips_common_object_mitigation_mode_manual_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mode-semiAuto']",
            'wait_for': 2
        }

    wips_common_object_mitigation_mode_automatic_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mode-Auto']",
            'wait_for': 2
        }

    wips_common_object_enable_rogue_ssid_detection_add_sign_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ssidEntryArea"]//span[@data-tip="Add"]',
            'wait_for': 2
        }

    wips_common_object_select_ssid_radio_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-ssid-type-ssid-profile']",
            'wait_for': 2
        }

    wips_common_object_enter_ssid_name_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ssidType-ssid']",
            'wait_for': 2
        }

    wips_common_object_enter_ssid_name_text_field = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-ssid']",
            'wait_for': 2
        }

    wips_common_object_select_ssid_encryption_type_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableCheckSsidEncryptionType']",
            'wait_for': 2
        }

    wips_common_object_select_ssid_encryption_scroll_button = \
        {
            'XPATH': '//span[contains(text(),"OPEN")]',
            'wait_for': 3
        }

    wips_common_object_select_ssid_encryption_scroll_all_items = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-ssidencryptiontype',
            'wait_for': 5
        }

    wips_common_object_select_ssid_encryption_scroll_get_name = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    wips_common_object_select_ssid_encryption_add_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-add-ssid-button']",
            'wait_for': 2
        }

    wips_common_object_enable_rogue_ssid_detection_delete_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ssidEntryArea"]//span[@data-tip="Delete"]',
            'wait_for': 2
        }
    wips_common_object_save_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-save-button']",
            'wait_for': 2
        }

    wips_common_object_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wipsCtn"]//span[@data-tip="Add"]',
            'wait_for': 2
        }

    wips_common_object_enter_ssid_name_text_field = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-ssid']",
            'wait_for': 2
        }

    network_policy_reuse_wips_settings_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-reuse-wips-settings']",
            'wait_for': 2
        }

    network_policy_reuse_wips_policy_dialog = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }

    network_policy_reuse_wips_policy_dialog_rsg_rows = \
        {
            'CLASS_NAME': 'dojoxGridRowTable',
            'wait_for': 1
        }

    network_policy_reuse_wips_policy_dialog_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-cancel',
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 1
        }

    network_policy_reuse_wips_policy_dialog_rsg_row_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector.dijitReset.dijitReset.dijitCheckBox',
            'wait_for': 1
        }

    network_policy_reuse_wips_policy_dialog_select_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 1
        }

    enable_wips_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-wips']",
            'wait_for': 2
        }

    rogue_ap_logs_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 10
        }

    rogue_ap_logs_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 2
        }

    rogue_ap_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-rogue-aps-ap-opt']",
            'wait_for': 2
        }

    rogue_checkbox = \
        {
            'CSS_SELECTOR': '.rogue-filter',
            'wait_for': 2
        }

    rogue_client_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='rClient']",
            'wait_for': 2
        }

    rogue_client_logs_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 10
        }

    rogue_client_logs_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 2
        }

    wips_common_object_policy_wireless_threat_detection_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-common-object-wips-enable-wireless-threat-detect']",
            'wait_for': 2
        }

    network_policy_wips_policy_dialog_rsg_rows = \
        {
            'CLASS_NAME': 'dgrid-cell.dgrid-column-1.field-name',
            'wait_for': 1
        }

    wips_enable_OnPrem_Airdefense_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableAirDefenseConfiguration']",
            'wait_for': 2
        }

    wips_primary_server_ip_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='primaryServer']",
            'wait_for': 2
        }

    wips_primary_server_port_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='airDefensePort1']",
            'wait_for': 2
        }

    wips_secondary_server_ip_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='secondaryServer']",
            'wait_for': 2
        }

    wips_secondary_server_port_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='airDefensePort2']",
            'wait_for': 2
        }