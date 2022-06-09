class SwitchTemplateWebElementDefinitions:
    device_template_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='switchSettings']",
            'wait_for': 5
        }

    device_template_switch_template_tab = \
        {
            'XPATH': "//*[@data-dojo-attach-point='showSwitch']",
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
            'XPATH': "//*[@data-dojo-attach-point='tplName']",
            'wait_for': 5
        }

    sw_template_save_btn = \
        {
            'XPATH': "//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 5
        }

    device_sw_template_items = {'CSS_SELECTOR': '.ui-menu-item', 'wait_for': 5}

    sw_device_template_grid_rows = {'CSS_SELECTOR': '.dgrid-row', 'wait_for': 5}

    sw_template_enable_spanningtree = \
        {
            'XPATH': "//*[@data-dojo-attach-point='stpSwitch']",
            'wait_for': 5
        }

    sw_template_enable_stp = \
        {
            'XPATH': "//*[@data-dojo-attach-point='stpMode-stp']",
            'wait_for': 5
        }

    sw_template_enable_rstp = \
        {
            'XPATH': "//*[@data-dojo-attach-point='stpMode-rstp']",
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
            'XPATH': '//div[@id="switchesMenu"]//div//button',
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
            'XPATH': '//button[@data-dojo-attach-point="cancelButton"]',
            'index': 3,
            'wait_for': 5
        }

    switch_temp_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'index': 4,
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
            'XPATH': '//*[@data-automation-tag="switch-template-aggregate-for-stack"]',
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
            'XPATH': '//*[@data-dojo-attach-point="selectAllButton"]',
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
            'XPATH': '//*[@class="bottom"]//*[@data-dojo-attach-point="saveButton"]',
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
            'XPATH': '//*[@class="line clearfix priority"]//*[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 2
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

    priority_items_select = \
        {
            'XPATH': '//div[@class="pse-profileobject-form ui-dialog-content"]//ul[@class="chzn-results qa-chzn-results-priority"]//li[contains(@class,"active-result")]',
            'wait_for': 2
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
            'XPATH': '//a[@data-automation-tag="automation-switch-template-choose-existing"]',
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
            'XPATH': '//input[@data-dojo-attach-point="enabledControl"]',
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

    lacp_toggle_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-lag-lacp-toggle"]',
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
            'XPATH': '//a[@data-automation-tag="lag-edit-lag-${lag}"]',
            'wait_for': 5
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
            'XPATH': '//*[@data-automation-tag="lag-slots-available"]//option[@value="${slot}"]',
            'wait_for': 5
        }

    error_message = \
        {
            'XPATH': '//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 1,
            'index': 2
        }

    template_link = \
        {
            'XPATH': '//a[text()="${template}"]',
            'wait_for': 5
        }
