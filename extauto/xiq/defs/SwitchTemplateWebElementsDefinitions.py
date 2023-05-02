class SwitchTemplateWebElementDefinitions:
    device_template_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='switchSettings']",
            'wait_for': 5
        }

    device_template_switch_template_tab = \
        {
            'XPATH': "//li[@data-automation-tag='policy-switching-templates']",
            'wait_for': 5
        }

    sw_template_add_button = \
        {
            'CSS_SELECTOR': '.table-filter-drop-add',
            'index': 0,
            'wait_for': 1
        }

    sw_template_name_textfield = \
        {
            'XPATH': "//input[@data-automation-tag='automation-switch-template-name']",
            'wait_for': 5
        }

    sw_template_save_btn = \
        {
            'XPATH': "//fixed-bar[@class='bottom']//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 5
        }

    device_sw_template_items = {'CSS_SELECTOR': '.ui-menu-item', 'wait_for': 5}

    sw_device_template_grid_rows = {'CSS_SELECTOR': '[data-dojo-attach-point="templateGridArea"] .dgrid-row', 'wait_for': 5}

    sw_template_enable_spanningtree = \
        {
            'XPATH': "//input[@data-automation-tag='automation-switch-template-stp-toggle']",
            'wait_for': 5
        }

    sw_template_enable_stp = \
        {
            'XPATH': "//input[@data-automation-tag='automation-switch-template-stp-mode']",
            'wait_for': 5
        }

    sw_template_enable_rstp = \
        {
            'XPATH': "//input[@data-automation-tag='automation-switch-template-rapid-stp']",
            'wait_for': 5
        }

    sw_template_enable_mstp = \
        {
            'XPATH': "//input[@data-automation-tag='automation-switch-template-multiple-stp']",
            'wait_for': 5
        }

    sw_template_device_configuration_tab = \
        {
            'CSS_SELECTOR': '.nav-configuration-device',
            'index': 0,
            'wait_for': 1
        }

    sw_template_port_configuration_tab = \
        {
            'CSS_SELECTOR': '.nav-configuration-ports',
            'index': 0,
            'wait_for': 1
        }

    sw_template_adv_settings_tab = \
        {
            'CSS_SELECTOR': '.nav-configuration-advanced',
            'index': 0,
            'wait_for': 1
        }

    sw_template_row_cells = \
        {
            'CSS_SELECTOR': '.J-tmplName',
            'wait_for': 5
        }

    sw_template_row_table_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 5
        }

    sw_template_select_button = \
        {
            'CSS_SELECTOR': '.table-select',
            'wait_for': 1
        }

    sw_template_selection_search_textfield = \
        {
            'CSS_SELECTOR': '.search-box',
            'wait_for': 1
        }

    sw_template_selection_search_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="searchButton"]',
            'wait_for': 1
        }

    sw_template_selection_grid = \
        {
            'XPATH': '//div[@data-dojo-attach-point="listArea"]//div[@class="dojoxGridContent"]',
            'wait_for': 5
        }

    sw_template_selection_grid_rows = \
        {
            'XPATH': '//tr',
            'wait_for': 5
        }

    sw_template_selection_row_checkbox = \
        {
            'XPATH': '//td/div[contains(@class, "dojoxGridRowSelector")]',
            'wait_for': 5
        }

    sw_template_selection_select_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="linkButton"]',
            'wait_for': 1
        }

    sw_template_selection_cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 1
        }

    sw_template_assign_button = \
        {
            'XPATH': '//button[text()="Assign"]',
            'wait_for': 5
        }

    sw_template_assign_choose_existing = \
        {
            'XPATH': '//a[@type="choosePortType"]',
            'wait_for': 5
        }

    sw_template_assign_create_new = \
        {
            'XPATH': '//a[@type="createPortType"]',
            'wait_for': 5
        }

    sw_template_assign_advanced_actions = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-advancedactions"]',
            'wait_for': 5
        }

    sw_template_assign_advanced_actions_aggr = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-aggregate"]',
            'wait_for': 5
        }

    sw_template_port_type_list_radio = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="portTypeList"]//label/input',
            'wait_for': 5
        }

    sw_template_port_type_list_label = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="portTypeList"]//label/span',
            'wait_for': 5
        }

    sw_template_port_type_list_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="assignCtn"]/div[2]/button[1]',
            'wait_for': 2
        }

    sw_template_port_type_list_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="assignCtn"]/div[2]/button[2]',
            'wait_for': 2
        }

    sw_template_select_all_ports_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="selectAllButton"]',
            'wait_for': 5
        }

    sw_template_deselect_all_ports_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="deselectAllButton"]',
            'wait_for': 5
        }

    sw_template_wireframe_net_ports = \
        {
            'XPATH': '//div[(contains(@class, "device-ports"))]/ul[(contains(@class, "net-ports"))]//li/ul/li/div[(contains(@class, "AH-ports-icons"))]',
            'wait_for': 5
        }

    sw_template_selected_ports = \
        {
            'XPATH': '//div[@class="device-ports"]/ul//li/ul/li/div[(contains(@class, "active"))]',
            'wait_for': 5
        }

    sw_template_edit_port_type = \
        {
            'XPATH': '//span[@data-dojo-attach-point="editPortTypeLink"]',
            'wait_for': 5
        }

    sw_template_port_usage = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-portusage"]/li[@class="active-result result-selected"]',
            'wait_for': 5
        }

    sw_template_port_desc = \
        {
            'XPATH': '//input[@data-dojo-attach-point="descriptionField"]',
            'wait_for': 5
        }

    sw_template_port_status = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enabledField"]',
            'wait_for': 5
        }

    sw_template_stack_add_button = \
        {
            'XPATH': "//div[@data-dojo-attach-point='switchesMenu']//div//button[text()='Add']",
            'wait_for': 5
        }

    sw_template_select_delete_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="listArea"]//div[@data-dojo-attach-point="actionLeft"]/span[@class="table-action-icons table-remove"]',
            'wait_for': 5
        }
    sw_template_sel_row_checkbox = \
        {

            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'wait_for': 5
        }

    sw_template_selection_close_button = \
        {
            'XPATH': '//div[@class="ui-dialog-bottom clearfix"]//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    sw_template_stack_delete_button = \
        {
            'CSS_SELECTOR': '.table-remove',
            'wait_for': 1
        }

    sw_template_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-selector',
            'wait_for': 5
        }

    port_details_all_rows = \
        {
            "CLASS_NAME": 'state-type-access-port',
            'wait_for': 5
        }

    port_details_row_label = \
        {
            "CSS_SELECTOR": '.portInterface',
            'wait_for': 5
        }

    port_details_row_add_button = \
        {
            "CSS_SELECTOR": '.table-action-icons',
            'index': 0,
            'wait_for': 5
        }

    port_type_text_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portTypeName"]',
            'wait_for': 3
        }

    port_details_vlan_ui_ip_button = \
        {
            'XPATH': '//div[contains(@class, "grid_7")]/div/div//*[@data-dojo-attach-point="ipMark"]',
            'index': 1,
            'wait_for': 5
        }

    port_details_vlan_pop_up_all_entries = \
        {
            "CSS_SELECTOR": '.J-ip-item',
            'wait_for': 5
        }

    port_details_vlan_input_obj = \
        {
            "XPATH": '//div[contains(@class, "grid_7")]/div/div/input',
            'index': 1,
            'wait_for': 5
        }

    port_details_add_vlan_button = \
        {
            'XPATH': '//div[contains(@class, "grid_7")]/div/div//*[@data-dojo-attach-point="ipSave"]',
            'index': 1,
            'wait_for': 5
        }

    port_details_vlan_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    port_details_vlan_id = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    port_details_vlan_cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 5
        }

    port_details_vlan_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    port_type_cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelButton"]',
            'index': 1,
            'wait_for': 5
        }

    port_new_type_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'index': 2,
            'wait_for': 5
        }

    switch_temp_cancel_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-switch-template-cancel-btn"]',
            'index': 3,
            'wait_for': 5
        }

    switch_temp_save_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-switch-template-save-btn"]',
            'wait_for': 5
        }

    complete_stack_list = \
        {
            'XPATH': '//*[@data-dojo-attach-point="templateElements"]',
            'wait_for': 5
        }

    complete_stack_all_rows = \
        {
            "CSS_SELECTOR": '.active-result',
            'wait_for': 5
        }

    aggr_ports_across_stack_button = \
        {
            'XPATH': '//button[@data-automation-tag="switch-template-aggregate-for-stack"]',
            'wait_for': 5
        }

    aggr_ports_standalone_button = \
        {
            'XPATH': '//*[@data-automation-tag="switch-template-aggregate-for-exos"]',
            'wait_for': 5
        }

    poe_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="poeStatus"]',
            'wait_for': 2
        }

    device_template_port_configuration = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portConfig"]',
            'wait_for': 2
        }

    select_all_ports_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="selectAllButton"]',
            'wait_for': 2
        }

    assign_all_ports_device_template = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template"]',
            'wait_for': 2
        }

    port_type_template = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-create-new"]',
            'wait_for': 2
        }

    port_type_name_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portTypeName"]',
            'wait_for': 2
        }

    save_button_port_type = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-types-new-save-btn"]',
            'wait_for': 2
        }

    save_button_template = \
        {
            'XPATH': '//fixed-bar[@class="bottom"]/button[@data-dojo-attach-point="saveButton"][text() = "Save"]',
            'wait_for': 2
        }

    pse_profile_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-types-new-pse-settings-add-btn"]',
            'wait_for': 2
        }

    pse_profile_name = \
        {
            'XPATH': '//*[@class="column last"]//*[@data-dojo-attach-point="nameEl"]',
            'wait_for': 2
        }

    pse_power_limit = \
        {
            'XPATH': '//*[@data-dojo-attach-point="powerLimit"]',
            'wait_for': 2
        }

    priority_options = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-bridge-dropdown-chzn-arrow-down"]'

        }

    low_value_option = \
        {
            'XPATH': '//*[@data-automation-tag="Low"]',
            'wait_for': 2
        }

    high_value_option = \
        {
            'XPATH': '//*[@data-automation-tag="High"]',
            'wait_for': 2
        }

    critical_value_option = \
        {
            'XPATH': '//*[@data-automation-tag="Critical"]',
            'wait_for': 2
        }

    priority_items_select_container = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-bridge-dropdown-chzn-results-ctn"]'
        }

    priority_items_select = \
        {
            'CSS_SELECTOR': '.active-result'
        }

    power_mode_items_select = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-powermode"]//li[contains(@class,"active-result")]',
            'wait_for': 2
        }

    power_mode_dropdown_button = \
        {
            'XPATH': '//div[@class="line clearfix"]//div[@class="column last"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 2
        }

    save_button_pse = \
        {
            'XPATH': '//div[@data-dojo-attach-point="btnArea"]//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 2
        }

    existing_port_type = \
        {
            'XPATH': '//a[@data-automation-tag="automation-switch-template-chooseexisting"]',
            'wait_for': 2
        }

    switch_template_port_types_list = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="portTypeList"]//li',
            'wait_for': 2
        }

    save_btn = \
        {
            'XPATH': '//button[@class="btn btn-dim fn-right"]',
            'wait_for': 2
        }

    edit_port_button_template = \
        {
            'XPATH': '//span[@data-automation-tag="automation-switch-template-switch-template-1-port-details-edit-port"]',
            'wait_for': 2
        }

    poe_verification_for_port_list = \
        {
            'XPATH': '//div[@class="column portEnabled"]',
            'wait_for': 2
        }

    sw_template_supplemental_cli_button = \
        {
            'XPATH': '//li[contains(text(), "Supplemental CLI")]',
            'wait_for': 1
        }

    sw_template_supplemental_cli_on_button = \
        {
            'XPATH': '//section[@data-dojo-attach-point="advSettingsCtn"]'
                     '//input[@data-dojo-attach-point="enabledControl"]',
            'wait_for': 1
        }

    sw_template_supplemental_cli_name_text = \
        {
            'XPATH': '//input[@data-dojo-attach-point="name"]',
            'wait_for': 1
        }

    sw_template_supplemental_cli_commands_text = \
        {
            'XPATH': '//textarea[@data-dojo-attach-point="cli"]',
            'wait_for': 1
        }

    sw_template_scli_save_btn = \
        {
            'XPATH': "//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 5
        }

    mgmt_checkbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="miSwitch"]',
            'wait_for': 2
        }

    mgmt_vlan_text_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="detail-mgtd-vlan"]//input[@data-dojo-attach-point="mgtVlan"]',
            'wait_for': 2
        }

    sw_template_assign_choose_existing_trunk_choice_second_dialog_box = \
        {
            'XPATH': '//div[@class="ui-dialog-content"]',
            'index': 1,
            'wait_for': 5
        }

    sw_template_check_box_row = \
        {
            'XPATH': '//tr//input[@type="checkbox"]',
            'index': 1,
            'wait_for': 5
        }

    sw_template_delete_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-switch-device-templates-speRemove-btn"]',
            'wait_for': 5
        }

    new_sw_template_add_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-switch-device-templates-menu-button"]',
            'wait_for': 5
        }
        
    sw_template_save_btn_bottom = \
        {
            'XPATH': "//*[@class='bottom']//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 5
        }

    lacp_toggle_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag,"lag-lacp-toggle")]',
            'wait_for': 2
        }

    lag_remove_port_button = \
        {
            'XPATH': '//*[@data-automation-tag="lag-remove-port-button"]',
            'wait_for': 2
        }

    lag_add_port_button = \
        {
            'XPATH': '//*[@data-automation-tag="lag-add-port-button"]',
            'wait_for': 2
        }

    select_ports_available = \
        {
            'XPATH': '//select[@data-dojo-attach-point="portsAvailable"]//option',
            'wait_for': 5
        }

    cancel_button = \
        {
            'XPATH': '//button[@data-automation-tag="lag-cancel-button"]',
            'wait_for': 5
        }

    save_port_type_button = \
        {
            'XPATH': '//fixed-bar[@class="bottom"]//button[@data-automation-tag="lag-save-button"]',
            'wait_for': 5
        }

    switch_temp_save_button_v2 = \
        {
            'XPATH': '//fixed-bar[@class="bottom"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5,
            'index': 1
        }

    lag_span = \
        {
            'CSS_SELECTOR': '.link-type-agg-prime .control-label.portInterface  [data-automation-tag="lag-edit-lag-${lag}"]',
            'wait_for': 10
        }

    available_port = \
        {
            'XPATH': '//option[@data-automation-tag="lag-available-port-${port}"]',
            'wait_for': 5
        }

    selected_port = \
        {
            'XPATH': '//option[@data-automation-tag="lag-selected-port-${port}"]',
            'wait_for': 5
        }

    port_settings_tab = \
        {
            'XPATH': '//label[@data-dojo-attach-point="configuration-ports-tab-settings"]',
            'wait_for': 5
        }

    available_slot = \
        {
            'XPATH': '//select[@data-automation-tag="lag-slots-available"]//option[@value="${slot}"]',
            'wait_for': 5
        }

    error_message = \
        {
            'XPATH': '//*[contains(@class, "ui-tipbox-error")]//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 1,
        }

    template_link = \
        {
            'XPATH': '//a[text()="${template}"]',
            'wait_for': 5
        }

    select_all_rows = \
        {
            'XPATH': '//div[@id="ah/util/AHGrid_1_rowSelector_-1"]',
            'wait_for': 5
        }

    confirm_message_yes_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 5
        }

    sw_template_adv_tab_textfield = \
        {
            'XPATH': '//input[@data-automation-tag="automation-switch-template-name"]',
            'wait_for': 2
        }

    sw_template_save_btn_adv_tab = \
        {
            'XPATH': '//*[@class = "bottom"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 2
        }

    sw_template_adv_settings_upgrade_device_text = \
        {
            'XPATH': '//*[contains(text(),"Upgrade device firmware upon device authentication")]/text()',
            'wait_for': 2
        }

    sw_template_adv_settings_upgrade_device_on_off_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableUploadAuthSwitchHac"]',
            'wait_for': 2
        }

    sw_template_adv_settings_upload_config_text = \
        {
            'XPATH': '//*[contains(text(),"Upload configuration automatically")]/text()',
            'wait_for': 2
        }

    sw_template_adv_settings_upload_configuration_on_off_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="configPushAuto"]',
            'wait_for': 2
        }

    sw_template_adv_settings_upgr_firm_latest_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="downloadFirmwareOption-latest"]',
            'wait_for': 2
        }

    sw_template_adv_settings_upgr_firm_specific_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="downloadFirmwareOption-specific"]',
            'wait_for': 2
        }

    sw_template_device_sett_forward_delay_drop_down = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-forward-dropdown-chzn-arrow-down"]',
            'wait_for': 2
        }

    sw_template_device_sett_forward_delay_drop_down_container = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-forward-dropdown-chzn-container-ctn"]',
            'wait_for': 2
        }

    sw_template_device_sett_forward_delay_drop_down_items = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-forward-dropdown-chzn-drop-ctn"]',
            'wait_for': 2
        }

    sw_template_device_sett_forward_delay_drop_down_items_container = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-forward-dropdown-chzn-results-ctn"]'
        }

    sw_template_device_sett_forward_delay_drop_down_items_all_items = \
        {
            'CSS_SELECTOR': '.active-result'
        }

    sw_template_device_sett_forward_delay_drop_down_item16 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-forward-dropdown-chzn-option-16"]',
            'wait_for': 2
        }

    sw_template_device_sett_forward_delay_drop_down_item15 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-forward-dropdown-chzn-option-15"]',
            'wait_for': 2
        }

    sw_template_adv_settings_download_specific_firmware_drop_down_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importImageArea"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    sw_template_adv_settings_download_specific_firmware_drop_down_items = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-deviceimagemetadata"]//li[contains(@class,"active-result")]',
            'wait_for': 2
        }

    sw_template_row_cells_hyperlink = \
        {
            'CSS_SELECTOR': '.J-tmplName',
            'wait_for': 10
        }

    sw_template_stp_tab = \
        {
            'XPATH': '//label[@data-dojo-attach-point="configuration-ports-tab-stp"]',
            'wait_for': 5
        }

    sw_template_port_details_tab = \
        {
            'XPATH': '//label[@data-dojo-attach-point="configuration-ports-tab-details"]',
            'wait_for': 5
        }

    sw_template_stp_port_rows = \
        {
            'XPATH': '//portentry-row[contains(@componentpath, "PortSTPEntry")]',
            'wait_for': 5
        }

    sw_template_path_cost_row = \
        {
            'XPATH': './/input[@data-dojo-attach-point="pathCostField"]',
            'wait_for': 5
        }

    template_slot = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-${slot}"]',
            'wait_for': 5
        }

    port_in_agg = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portsInAgg"]//option',
            'wait_for': 5
        }

    sw_template_hyperlink = \
        {
            'XPATH': "//a[@class='J-tmplName']",
            'wait_for': 5
        }

    sw_template_enable_mac_locking = \
        {
            'XPATH': "//section[@class='mac-locking state-configuration-device']//input[@data-automation-tag='template-maclock-enable']",
            'wait_for': 5
        }
    sw_template_enable_mac_locking_confirm_message_yes_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 5
        }

    sw_template_auto_cfg = \
        {
            'XPATH': '//input[@data-dojo-attach-point="configPushAuto"]',
            'wait_for': 5
        }

    sw_template_auto_revert_enabled = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableAutoRevert"]',
            'wait_for': 5
        }

    sw_template_auto_revert_msg = \
        {
            'XPATH': '//*[@data-automation-tag="automation-upload-config-auto-enable-revert"]',
            'wait_for': 5
        }

    sw_template_notification_yes_btn = \
        {
            'XPATH': '//*[@data-automation-tag="automation-notification-yes-btn"]',
            'wait_for': 5
        }

    sw_template_assign_existing_trunk_choice_second_dialog_box_save_button = \
        {
            'XPATH': '//div[@class="ui-dialog-bottom clearfix"]//button[@data-dojo-attach-point="saveButton"]'
        }

    pse_error_message = \
        {
            'XPATH': '//*[@data-dojo-attach-point="textEl"]',
            'index': 0,
        }

    sw_template_port_details_interface_all_rows = \
        {
            'CSS_SELECTOR': '.state-expanded.state-type-autoSense-port'
        }

    sw_template_port_details_row_interface_value = \
        {
            'CSS_SELECTOR': '.is-not-prime'
        }

    sw_template_port_details_row_combo = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-template-port-details-port-type']",
            'wait_for': 5
        }

    sw_template_port_details_combo_list = \
        {
            'XPATH': "//*[@data-dojo-attach-point='containerNode,textDirNode']",
            'wait_for': 5
        }

    sw_template_port_details_row_port_type_list = \
        {
            'CSS_SELECTOR': '.dijitReset.dijitMenuItem'
        }

    sw_template_port_details_port_type_editor_name = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-name']"
        }

    sw_template_port_details_port_type_editor_description = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-description']"
        }

    sw_template_port_details_port_type_editor_status = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-status']"
        }

    sw_template_port_details_port_type_editor_auto_sense_status = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-auto-sense-status']"
        }

    sw_template_port_details_port_type_editor_access = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-access']"
        }

    sw_template_port_details_port_type_editor_trunk = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-trunk']"
        }

    sw_template_port_details_port_type_editor_cancel = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-cancel']"
        }

    sw_template_port_details_port_type_editor_previous = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-prev']"
        }

    sw_template_port_details_port_type_editor_next = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-next']"
        }

    sw_template_port_details_port_type_editor_save = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-save']"
        }

    sw_template_port_details_port_type_editor_duplex_arrow = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-duplex-chzn-arrow-down']"
        }

    sw_template_port_details_port_type_editor_duplex_options_container = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-duplex-chzn-results-ctn']"
        }

    sw_template_port_details_port_type_editor_duplex_arrow_options = \
        {
            'CSS_SELECTOR': '.active-result'
        }

    sw_template_port_details_port_type_editor_speed_arrow = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-speed-chzn-arrow-down']"
        }

    sw_template_port_details_port_type_editor_speed_options_container = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-speed-chzn-results-ctn']"
        }

    sw_template_port_details_port_type_editor_speed_arrow_options = \
        {
            'CSS_SELECTOR': '.active-result'
        }

    sw_template_port_details_port_type_options = \
        {
            'CSS_SELECTOR': '.active-result'
        }

    sw_template_port_details_port_type_editor_client_reporting = \
        {
            'XPATH': '//*[@id="hcApp/deviceConfig/switchFeatures/porttypes/steps/PortTypesSettingsView_3"]/div[2]/div[2]/div[1]/span[2]/label/input'
        }

    sw_template_port_details_port_type_editor_cdp_receive = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-cdp']"
        }

    sw_template_port_details_port_type_editor_lldp_transmit = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-lldp-tx']"
        }

    sw_template_port_details_port_type_editor_lldp_receive = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-lldp-rx']"
        }

    sw_template_port_details_port_type_editor_sc_broadcast = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-sc-broadcast']"
        }

    sw_template_port_details_port_type_editor_sc_unicast = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-sc-unicast']"
        }

    sw_template_port_details_port_type_editor_sc_multicast = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-sc-multicast']"
        }

    sw_template_port_details_port_type_editor_sc_threshold = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-sc-threshold-chzn-arrow-down']"
        }

    sw_template_port_details_port_type_editor_sc_rate_limit_type = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-sc-rate-limit-type-chzn-arrow-down']"
        }

    sw_template_port_details_port_type_editor_sc_rate_limit_value = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-sc-rate-limit-value']"
        }

    sw_template_port_details_port_type_editor_port_name_and_usage_tab = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-step-info']"
        }

    sw_template_port_details_port_type_editor_transmission_tab = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-step-trans']"
        }

    sw_template_port_details_port_type_editor_storm_control_tab = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-step-storm-control']"
        }

    sw_template_port_details_port_type_editor_summary_tab = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-step-summary']"
        }

    sw_template_port_details_port_type_editor_vlan_tab = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-step-vlan']"
        }

    sw_template_port_details_port_type_editor_stp_tab = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-step-stp']"
        }

    device_switch_select_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-device-templates-reusable-btn']"
        }

    sw_template_table_rows = \
        {
            'CSS_SELECTOR': '.dojoxGridRow'
        }

    switch_template_device_configuration_igmp_settings = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-template-igmp-toggle']"
        }

    switch_template_device_configuration_igmp_immediate_leave = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-template-immediate-leave']"
        }

    switch_template_device_configuration_igmp_suppress_independent = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-template-suppress-independent']"
        }

    switch_template_device_configuration_mtu_1522 = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ethMtu-min']"
        }

    switch_template_device_configuration_mtu_1950 = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ethMtu-mid']"
        }

    switch_template_device_configuration_mtu_9600 = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ethMtu-max']"
        }

    switch_template_device_configuration_pse_enable = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-template-pse-toggle']"
        }

    switch_template_device_configuration_pse_budget = \
        {
            'XPATH': "//*[@data-automation-tag='automation-switch-template-pse-budget']"
        }

    sw_template_port_details_port_type_editor_spanning_tree_stp_enable = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-stp-enable']"
        }

    sw_template_port_details_port_type_editor_spanning_tree_edge_port_enable = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-stp-edge-port']"
        }

    sw_template_port_details_port_type_editor_spanning_tree_bdu_protection = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-stp-bpdu-prot-chzn-arrow-down']"
        }

    sw_template_port_details_port_type_editor_spanning_tree_priority = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-stp-priority-chzn-drop-ctn']"
        }

    sw_template_port_details_port_type_editor_spanning_tree_path_cost = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-stp-path-cost']"
        }

    sw_template_port_details_port_type_editor_vlan_native_vlan = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-native-vlan-input']"
        }

    sw_template_port_details_port_type_editor_vlan_add_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-port-type-editor-native-vlan-add-btn']"
        }

    sw_template_port_details_port_type_editor_vlan_allowed_vlans = \
        {
            'XPATH': "//*[@data-automation-tag='port-type-editor-allowed-vlans']"
        }

    sw_template_device_max_age_drop_down_items = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-age-dropdown-chzn-arrow-down"]',
            'wait_for': 2
        }

    sw_template_device_max_age_delay_items_container = \
        {
            'XPATH': '//*[@data-automation-tag="automation-switch-template-age-dropdown-chzn-results-ctn"]'
        }

    sw_template_device_max_age_drop_down_all_items = \
        {
            'CSS_SELECTOR': '.active-result'
        }

    device_template_no_of_ports = \
        {
            'CSS_SELECTOR': '.state-expanded.state-type-access-port',
            'wait_for': 10
        }

    device_template_override_policy = \
        {
            'XPATH': '//input[@data-automation-tag="switch-template-override-settings"]',
            'wait_for': 2
        }

    sw_template_enable_mac_locking_confirm_message = \
        {
            'CSS_SELECTOR': '.ui-cfmsg.confirm',
            'wait_for': 10
        }