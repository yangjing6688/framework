class DeviceTemplateWebElementDefinitions:
    device_template_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='switchSettings']",
            'wait_for': 5
        }

    device_template_ap_template_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='showAP']",
            'wait_for': 5
        }

    device_template_switch_template_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='showSwitch']",
            'wait_for': 5
        }

    device_template_ap_template_add_button = \
        {
            'CSS_SELECTOR': '.table-action-buttons.table-action-icons.table-drop-add',
            'index': 15,
            'wait_for': 1
        }

    device_template_ap_template_scroll_all_platform_items = \
        {
            'CSS_SELECTOR': '.ui-menu-list',
            'index': 15,
            'wait_for': 5
        }

    device_template_ap_template_name_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='tplName']",
            'wait_for': 5
        }

    device_template_ap_template_wifi0_tab = \
        {
            'CSS_SELECTOR': '.ui-tab',
            'index': 2,
            'wait_for': 5
        }

    device_template_ap_template_wifi1_tab = \
        {
            'CSS_SELECTOR': '.ui-tab',
            'index': 5,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi0_client_mode_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'wait_for': 5
        }

    ap_template_radio_usage_wifi0_client_access_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 1,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi0_backhaul_mesh_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 2,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi0_sensor_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 3,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi1_client_mode_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 4,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi1_client_access_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 5,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi1_backhaul_mesh_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 6,
            'wait_for': 5
        }

    ap_template_radio_usage_wifi1_sensor_checkbox = \
        {
            'CSS_SELECTOR': '.radioUsage',
            'index': 7,
            'wait_for': 5
        }

    device_ap_template_items = {'CSS_SELECTOR': '.ui-menu-item', 'wait_for': 5}

    device_template_grid_rows = {'CSS_SELECTOR': '.dgrid-row', 'wait_for': 5}

    device_ap_template_cell = {'CSS_SELECTOR': '.J-tmplName', 'wait_for': 5}

    device_ap_template_add_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-wireless-device-templates-menu-button"]',
            'wait_for': 5
        }

    device_ap_template_drop_box = \
        {
            'XPATH': '//*[@id="ah/util/layout/Menu_6"]/ul',
            'wait_for': 5
        }

    ap_template_name = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/APTemplate_0"]/div[2]/div[1]/div[2]/div[2]/input',
            'wait_for': 2
        }

    ap_template_save_button = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/APTemplate_0"]/div[2]/fixed-bar/button[2]',
            'wait_for': 2
        }

    device_template_page_next_button = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/ConfigWizard_0"]/fixed-bar/button[2]',
            'wait_for': 2
        }

    router_settings_page_next_button = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/ConfigWizard_0"]/fixed-bar/button[2]',
            'wait_for': 2
        }

    addition_setting_page_next_button = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/ConfigWizard_0"]/fixed-bar/button[2]',
            'wait_for': 2
        }

    ap_template_ap230_scroll_button = \
        {
            'XPATH': '//a[contains(text(),"WiFi1")]',
            'wait_for': 3
        }

    wireless_interface_wifi0_radio_profiles = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-wirelessporttype2ghz,wirelessporttype5dualghz"]//li',
            'wait_for': 5
        }

    wireless_interface_wifi1_radio_profiles = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-wirelessporttype5ghz"]//li',
            'wait_for': 5
        }

    device_template_ap_template_wifi2_tab = \
        {
            'XPATH': '//div[@class="clearfix ui-tab-updated-parent"]//a[contains(text(),"WiFi2")]',
            'wait_for': 5
        }

    wifi2_primary_server_ip_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='airDefensePrimaryServerIP']",
            'wait_for': 5
        }

    wifi2_primary_server_port_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='airDefensePrimaryPort']",
            'wait_for': 5
        }

    wifi2_radio_status_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableWifi2RadioStatus']",
            'wait_for': 5
        }

    wifi0_sdr_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableSdrProfile']",
            'wait_for': 5
        }

    wifi2_primary_server_ip_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='airDefensePrimaryServerIP']",
            'wait_for': 5
        }

    wifi2_primary_server_port_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='airDefensePrimaryPort']",
            'wait_for': 5
        }

    wifi2_radio_status_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableWifi2RadioStatus']",
            'wait_for': 5
        }

    wifi0_sdr_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableSdrProfile']",
            'wait_for': 5
        }

    ap_template_next_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="nextBtn"]',
            'wait_for': 3
        }

    device_template_grid_checkbox = {'CSS_SELECTOR': '.dgrid-column-0', 'wait_for': 5}

    delete_ap_template_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="apTemplateCtn"]//span[@data-tip="Delete"]',
            'wait_for': 3
        }

    select_rule_in_templates_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="listArea"]//div[@data-dojo-attach-point="gridBottomLeft"]'
                     '//a[@data-size="100"]',
            'wait_for': 3
        }

    wifi0_radio_profile_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfile2g"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    wifi1_radio_profile_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfile5g"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    ap_template_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="accesspointListArea"]//span[@data-tip="Select"]',
            'wait_for': 5
        }

    select_ap_templates_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="500"]',
            'wait_for': 3
        }

    select_ap_template_from_list = \
        {
            'XPATH': '//table[@class="dojoxGridRowTable"]',
            'wait_for': 15
        }

    click_selected_ap_template = \
        {
            'CSS_SELECTOR': '.dojoxGridCell ',
            'wait_for': 10
        }

    ap_template_dialog_select_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 3
        }

    ap_template_select_rule_button = \
        {
            'CSS_SELECTOR': '.J-select-rule',
            'wait_for': 5
        }

    ap_template_rule_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="listArea"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    ap_template_rule_link_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="linkButton"]',
            'wait_for': 5
        }

    select_ap_templates_rules_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="100"]',
            'wait_for': 3
        }

    device_template_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCtn"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }
