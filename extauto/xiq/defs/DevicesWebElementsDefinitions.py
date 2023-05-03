

class DevicesWebElementsDefinitions:
    devices_page_grid_ids = \
        {
            'ID': 'dgrid_1',
            
         }

    devices_page_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]/tr/td/..',
            
         }

    devices_page_grid_rows_next = \
        {
            'XPATH': '//*[@data-dojo-attach-point="next-item1"]',
            # 'XPATH': "//*[@data-page='1']",
            'index': 1,
            'wait_for': 2,
        }

    devices_page_numbers = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pagesWrap"]',
            'index': 1,
            'wait_for': 2
        }

    devices_page_number_one = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pagesWrap"]//a[@data-page="0"]',
            'wait_for': 5
        }

    devices_page_grid_ap_name_cells = \
        {
            'CSS_SELECTOR': '.field-hostname',
            
        }

    devices_page_grid_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'index': 0,
            
         }

    devices_ap_status_cell = \
        {
            'ID': 'field-isConnected',
            'wait_for': 5
         }

    device_status_cell = \
        {
            # Moving this to .hive-status away from .hive-status-true because
            # it is causing test failures.  This webelement is pulled from
            # get_status_cell() which needs to get the status of the cell whether
            # it's green or not.
            'CSS_SELECTOR': '.hive-status',
            'wait_for': 15
        }

    device_config_audit = \
        {
            'CSS_SELECTOR': '.J-view',
            'wait_for': 15
        }

    device_stack_status = \
        {
            'CSS_SELECTOR': '.ui-icon-stack',
            'wait_for': 1
         }

    device_stack_status_warning = \
        {
            'CSS_SELECTOR': '.ui-icon-stack-warning',
            'wait_for': 1
         }

    device_conn_status_after_ten_min = \
        {
            'CSS_SELECTOR': '.ui-icon-dc-ten-mins',
            'wait_for': 5
        }

    devices_ap_name = \
        {
            'CLASS_NAME': 'field-hostname',
            'wait_for': 1
        }

    device_entry_exos_csv_upload_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickImportCtn"]'
                     '//div[@data-dojo-attach-point="exosImportFileUploader"]//input[@name="file"]',
            'wait_for': 5,
            'index': 0
        }

    devices_add_menu = \
        {
            'CSS_SELECTOR': '.ui-menu-list',
            'wait_for': 1
        }

    devices_quick_add_menu_item = \
        {
            'CSS_SELECTOR': '.ui-menu-item',
            'wait_for': 1
        }

    devices_quick_add_devices_menu_item = \
        {
            'XPATH': '//a[@data-automation-tag="automation-device-list-menu-quick-add-devices"]',
            'wait_for': 3
        }

    deploy_devices_to_cloud_menu_item = \
        {
            'XPATH': '//div[@data-automation-tag="automation-device-list-menu-quick-add-devices-cloud-onboard"]',
            'wait_for': 3
        }

    deploy_devices_locally_menu_item = \
        {
            'XPATH': '//div[@data-automation-tag="automation-device-list-menu-quick-add-devices-local-onboard"]',
            'wait_for': 1
        }

    devices_serial_text_area = \
        {
            'XPATH': "//*[@data-automation-tag='automation-quick-add-onboard-serial-number-textbox']",
            'wait_for': 1
        }

    location_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-quick-add-onboard-select-location-button']",
            'wait_for': 1
        }

    device_os_radio = \
        {
            'XPATH': "//*[@data-dojo-attach-point='cloudIqEngineLine']",
            'wait_for': 1
        }

    devices_quick_add_device_os_radio = \
        {
            'DESC': "Quick Add Devices, Device OS section",
            'XPATH': "//div[@data-dojo-attach-point='deviceOsSection']",
            'wait_for': 10
        }

    devices_quick_add_device_make_field = \
        {
            'DESC': "Quick Add Devices, Device Make field",
            'XPATH': "//div[@data-dojo-attach-point='deviceOsSection']",
            'wait_for': 10
        }

    location_select_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnSelect']",
            'wait_for': 1
         }

    devices_add_devices_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-add-button"]',
            'wait_for': 5
         }

    devices_drawer_open = \
        {
            'CSS_SELECTOR': '.ah-drawer-ctn.is-open',
            'wait_for': 2
        }

    devices_drawer_trigger = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ah-drawer-trigger"]',
            'wait_for': 2
        }

    devices_add_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-device-list-menu-button"]',
            'wait_for': 2
        }

    device_delete_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-device-list-speRemove-btn"]',
            'wait_for': 2
        }

    device_download_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-device-list-download-btn"]',
            'wait_for': 2
        }

    device_bulk_edit_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-device-list-bulkEdit-btn"]',
            'wait_for': 2
        }

    device_action_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-actions-button"]',
            'wait_for': 2
        }

    device_os_change_error_message = \
        {
            'XPATH': '//*[@data-dojo-attach-point="textEl"]',
            'index': 0,
            'wait_for': 5
        }

    device_update_error_message = \
        {
            'XPATH': '//*[@class="ui-tipbox ui-tipbox-error"]//*[@data-dojo-attach-point="textEl"]|//*[@class="ui-tipbox ui-tipbox-error"]//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }


    device_select_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'wait_for': 2
        }

    device_delete_confirm_ok_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='yesBtn']",
            'wait_for': 5
        }

    devices_exos_serial_text_area = \
        {
            'CSS_SELECTOR': '.serial-numbers.exos',
            'wait_for': 1
         }

    devices_type_select_exos_platform = \
        {
            'XPATH': '//*[@id="ah/util/form/dgrid/TaskGrid_2"]/div[1]/div[5]/div[1]/div[1]/div[2]/ul/li[3]/a',
            'wait_for': 1
         }

    devices_type_select_voss_platform = \
        {
            'XPATH': '//*[@id="ah/util/form/dgrid/TaskGrid_2"]/div[1]/div[5]/div[1]/div[1]/div[2]/ul/li[4]/a',
            'wait_for': 1
        }

    device_edit_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-edit',
            'wait_for': 5
        }

    device_details_wireless_interfaces = \
        {
            'XPATH': '//*[@id="ah/comp/entities/DeviceEntity_0"]/div[3]/div[1]/div[4]/ul[1]/li[5]',
            'wait_for': 5
        }

    device_details_wireless_interfaces_surrounding_aps_grid = \
        {
            'XPATH': '//*[@id="ah/util/form/dgrid/LocalPageGrid_0"]',
            'wait_for': 5
        }

    device_row_celss = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    device_details_refresh_button = \
        {
            'XPATH':    '/html/body/div[8]/div[1]/div/div[1]/div[4]/div[2]',
            
        }

    update_config_delta_radio_button = \
        {
            "XPATH": "//input[@data-automation-tag='override-checkbox']"
        }

    update_devices_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-manage-update-config"]',
            'wait_for': 8
            
        }

    update_devices_full_radio_button = \
        {
            'CLASS_NAME': 'J-up',
            'index': 2,
            'wait_for': 1
        }

    devices_perform_update_button = \
        {
            'XPATH': '//div/a[@data-dojo-attach-point="uploadBtn"]',
         }

    devices_config_update_message = \
        {
            'CLASS_NAME': 'progress-message',
            'wait_for': 2
         }

    refresh_devices_page = \
        {
            'CSS_SELECTOR': '.ui-icon.ui-fresh-icon',
            'wait_for': 5
        }

    device_adv_onboard_serial_text_area = \
        {
            'XPATH': "//*[@data-automation-tag='automation-welcome-onboard-ap-serial']",
            'wait_for': 5
        }

    device_adv_onboard_next_button = \
        {
            'CSS_SELECTOR': '.WelcomeWizardButtonNext',
            'wait_for': 5
        }

    device_adv_onboard_finish_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='finishButton']",
            'CSS_SELECTOR': '.WelcomeWizardButton.WelcomeWizardButtonFinish',
            'wait_for': 5
        }

    device_type_dropdown = \
        {
            'XPATH': '//*[@class="chzn-single"]//span[contains(text(), "Real")]',
            'wait_for': 5
        }

    device_type_dropdown2 = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]//span[contains(text(), "Real")]',
            'wait_for': 5
        }

    quick_onboard_simulated = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-sim-device-radio-button"]',
            'wait_for': 5
        }

    device_filter_button = \
        {
            'CSS_SELECTOR': '.filter-toggle',
            'wait_for': 5
        }

    device_filter_select_all_checkbox = \
        {
            'CSS_SELECTOR': '.devicetypesall-filter',
            'wait_for': 5
        }

    simulated_device_dropdown_options = \
        {
            'XPATH': '//*[@data-automation-tag="-dropdown"]',
            'wait_for': 5
        }

    simulated_devices_grid_rows = \
        {
            'TITLE': 'Simulated Device',
            
         }

    simulated_device_icon = \
        {
            'CSS_SELECTOR': '.sim-icon',
            'wait_for': 5
        }

    # This Xpath has been changed to a more specific path in order to solve an intermitent issue
    manage_device_actions_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-actions-button"]',
            'wait_for': 5
        }

    manage_device_actions_change_management_status = \
        {
            'XPATH': '//li[6]//a[@data-automation-tag="automation-manage-device-actions-changemanagementstatus"]',
            'wait_for': 5
        }

    manage_device_actions_change_management_status_manage = \
        {
            'XPATH': '//li[6]//a[@data-automation-tag="automation-manage-device-actions-switch-manage-device"]',
            'wait_for': 5
        }

    manage_device_actions_change_management_status_unmanage = \
        {
            'XPATH': '//li[6]//a[@data-automation-tag="automation-manage-device-actions-switch-unmanage-device"]',
            'wait_for': 5
        }

    manage_device_actions_change_management_status_yes_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-no-button"]/following-sibling::button[1]',
            'wait_for': 5
        }

    manage_device_actions_change_management_status_no_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="noBtn"]',
            'wait_for': 5
        }

    manage_device_actions_change_management_status_close_dialog = \
        {
            'XPATH': '//span[@class="device-utilities-icons device-utilities-close"]',
            'wait_for': 5
        }

    manage_device_utilities_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-button"]',
            'wait_for': 2
        }

    manage_device_utilities_wan_access = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-utilities-device-wan-access"]',
            'wait_for': 2
        }

    actions_assign_network_policy = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "automation-manage-device-actions") and contains(@data-automation-tag, "-assign-policy")]',
            'wait_for': 5
        }

    actions_assign_network_policy_drop_down = \
        {
            'CSS_SELECTOR': '.dijitDownArrowButton.select-policy .dijitButtonContents .honeycomb-ui-form-selectLabel',
            'wait_for': 5
        }

    actions_assign_network_policy_drop_down2 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-assign-policy-select"]//tbody',
            'wait_for': 5
        }

    actions_assign_network_policy_drop_down_router = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-router-assign-policy"]',
            'wait_for': 5,
        }

    action_assign_network_policy_dialog = \
        {
            "CSS_SELECTOR": '.ui-dialog-content',
            'wait_for': 5
        }
    action_assign_network_policy_dialog_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    actions_network_policy_drop_down_items = \
        {
            'XPATH': '//*[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display: none"))] //table[@data-automation-tag="automation-assign-policy-select-dropdown"] //td[@data-dojo-attach-point="containerNode,textDirNode"]',
            'wait_for': 5
        }

    nw_policy_drop = \
        {
            'CSS_SELECTOR': '.assign-policy .select-policy .honeycomb-ui-form-selectLabel',
            'wait_for': 5,
        }

    actions_network_policy_assign_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 5,
        }

    actions_network_policy_assign_cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    country_code_cell = \
        {
            'CSS_SELECTOR': '.field-countryCode',
            'wait_for': 5
        }

    actions_country_code_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-manage-device-actions-ap-assign-country-code']",
            'wait_for': 5
        }

    actions_country_code_dropdown = \
        {
            'XPATH': '//*[contains(@class, "device-actions-dialog")]//*[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    actions_country_code_dropdown_option = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    actions_country_code_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="assignLocation"]',
            'wait_for': 5
        }

    actions_country_code_error_message = \
        {
            'CSS_SELECTOR': ".ui-tipbox-title",
            'wait_for': 5
        }

    actions_country_code_confirm_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    actions_country_code_dialog = \
        {
            'CSS_SELECTOR': ".device-actions-dialog",
            'wait_for': 5
        }

    actions_country_code_close_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    device_actions_reboot_button = \
        {
            # The identifier differs depending on which type of device is selected (ap, switch, etc.),
            # so need to get all partial matches and select the displayed element
            'XPATH': '//a[contains(@data-automation-tag, "automation-manage-device-actions-") and contains(@data-automation-tag,"-reboot")]',
            'wait_for': 5
        }

    device_actions_reboot_confirm_bttn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    device_level_configure_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureViewSelect"]',
            'wait_for': 2
        }

    device_level_configure_interface_settings = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-nav-menu-interface-settings"]',
            'wait_for': 10
        }
    device_level_configure_interface_settings_wireless_toggle = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wirelessToggle"] //*[@class="header-toggle-caret"]',
            'wait_for': 3
        }

    device_level_configure_interface_settings_wifi0_ssid = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifi0_SsidArea"] //*[@name="SsidBroadcastName"]',
            'wait_for': 5
        }

    device_level_configure_interface_settings_wifi1_ssid = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifi1_SsidArea"] //*[@name="SsidBroadcastName"]',
            'wait_for': 5
        }

    device_level_page_refresh = \
        {
            'CSS_SELECTOR': '.entity-page-actions .ui-fresh-icon',
            'wait_for': 3
        }

    device_level_page_close_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    ap_device_config_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceConfigurationTab"]',
            'wait_for': 5
        }

    ap_description_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    save_device_config = \
        {
            'XPATH': '//*[@data-automation-tag="automation-device-entity-configuration-save-btn"]',
            'wait_for': 5
        }

    assign_policy_close_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeButtonNode"]',
            'wait_for': 5
        }

    adv_onboard_simulated_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-onboard-simulated"]',
            'wait_for': 5
        }

    simulated_device_dropdown = \
        {
            'DESC': 'Quick Add Devices (cloud) > Simulated > Device Model field',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-step-device-model-dropdown"]'
        }

    simulated_device_dropdown_table = \
        {
            'CSS_SELECTOR': '.honeycomb-ui-form-selectMenu',
            'wait_for': 5
        }

    simulated_device_dropdown_table_rows = \
        {
            'CSS_SELECTOR': '.dijitMenuItem',
            'wait_for': 5
        }

    simulated_device_dropdown_items = \
        {
            'DESC': 'Quick Add Devices (cloud) > Simulated > Device Model field items',
            'XPATH': '//*[@data-automation-tag="-dropdown"]//tr[contains(@class, "dijitMenuItem")]'
        }

    simulation_device_count_input_field = \
        {
            'DESC': 'Quick Add Devices (cloud) > Simulated > Device Model Count field',
            'XPATH': '//*[@data-dojo-attach-point="deviceModelSection"]'
                     '//*[@data-dojo-attach-point="numOfDevices"]',
            'wait_for': 5
        }

    add_another_device = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addAnotherDevice"]//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    adv_simulated_device_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 1,
            'index': 4
        }

    actions_assign_network_policy_to_router = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-router-assign-policy"]',
            'index': 1,
            'wait_for': 5
        }

    devices_ap_updated_status_cell = \
        {
            # 'CSS_SELECTOR': '.field-updatedOn',
            'CSS_SELECTOR': '.ui-state-default .dgrid-row-table .field-updatedOn',
            'wait_for': 1
         }

    column_picker_icon = \
        {
            'CSS_SELECTOR': '.ui-icon.dgrid-hider-toggle.show',
            'wait_for': 5,
        }

    column_picker_row = \
        {
            'XPATH': '//*[@class="dgrid-hider-menu-row"]//label',
            'wait_for': 5
        }

    column_picker_row_input = \
        {
            'XPATH': '//*[@class="dgrid-hider-menu-row"]//input',
            'wait_for': 5
        }

    country_code_column_header = \
        {
            'CSS_SELECTOR': '.field-countryCode',
            'index': 0,
            'wait_for': 5
        }

    network_policy_column_header = \
        {
            'CSS_SELECTOR': '.field-networkPolicyName',
            'index': 0,
            'wait_for': 5
        }

    manage_device_search_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceSearchInput"]',
            'wait_for': 5
        }

    manage_devices_select_all_devices_checkbox = \
        {
            'XPATH': '//*[@class="dgrid-resize-header-container"]//input[@type="checkbox"]',
            'index': 0,
            'wait_for': 5
        }

    device_grid_column7 = \
        {
            'XPATH': '//th[contains(@class, "dgrid-cell")]',
            'index': 7,
            'wait_for': 5
        }

    wing_devices_mac_text_area = \
        {
            # 'XPATH': '//*[@data-dojo-attach-point="quickSerialWiNGMac"]',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-mac-address-textbox"]',
            'wait_for': 1,
        }

    wing_devices_serial_text_area = \
        {
            'XPATH': '//*[@data-dojo-attach-point="quickSerialWiNG"]',
            'wait_for': 1,
        }

    devices_quick_add_device_make_controllers = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-option-Controllers"]',
            'wait_for': 1,
        }

    devices_quick_add_device_make_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-container-ctn" and @class="chzn-container chzn-container-single"]//span[contains(text(), "Extreme")]',
            'wait_for': 1
        }

    update_policy_and_config = \
        {
            'XPATH': '//input[@name="updateNP"]/..',
            'wait_for': 1
        }

    upgrade_engine_and_images = \
        {
            'XPATH': '//input[@name="updateHiveOS"]/..',
            'wait_for': 1
        }

    reboot_and_revert_warning_dialog = \
        {
            'XPATH': '//div[contains(@id, "ActionsAndUpdateDialog")]//h3[contains(text(), "The reboot and revert option is currently selected")]',
            'wait_for': 1
        }

    reboot_and_revert_warning_dialog_yes_button = \
        {
            'XPATH': '//div[contains(@id, "ActionsAndUpdateDialog")]//button[@data-automation-tag="automation-notification-yes-btn"]',
            'wait_for': 1
        }

    device_update_close_button = \
        {
            'CSS_SELECTOR': '.btn[data-dojo-attach-point="closeDialog"]',
            'XPATH': '//div/a[@data-dojo-attach-point="closeDialog"]',
            
         }

    actions_assign_network_policy_switch = \
        {
            'XPATH': "//*[@data-automation-tag='automation-manage-device-actions-switch-assign-policy']",
            'wait_for': 5
        }

    devices_quick_add_device_panel = \
        {
            'DESC': 'Manage > Devices > Quick Add Devices panel',
            'XPATH': '//div[@data-dojo-attach-point="quickAddCtn"]',
            'wait_for': 5
        }

    devices_quick_add_device_make_drop_down = \
        {
            'CSS_SELECTOR': 'div[class="select-ctn"][data-dojo-attach-point="quickMakeSelect"]',
            'wait_for': 1
         }

    devices_advanced_add_device_make_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importDeviceMakeCtn"]//span[contains(text(), "Extreme - Aerohive")]',
            'wait_for': 1
         }

    devices_quick_add_device_make_aerohive_choice = \
        {
            'CSS_SELECTOR': '.chzn-results li[data-automation-tag="chzn-option-Extreme_-_Aerohive"]',
            'wait_for': 5
        }

    devices_quick_add_device_make_exos_choice = \
        {
            'CSS_SELECTOR': '.chzn-results li[data-automation-tag="chzn-option-EXOS"]',
            'wait_for': 5
        }

    devices_quick_add_device_make_voss_choice = \
        {
            'CSS_SELECTOR': '.chzn-results li[data-automation-tag="chzn-option-VOSS"]',
            'wait_for': 5
        }

    devices_advanced_add_device_make_voss_choice = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importDeviceMakeCtn"]//li[contains(text(), "EXOS")]',
            'wait_for': 5
        }

    devices_voss_serial_text_area = \
        {
         'CSS_SELECTOR': '.serial-numbers.voss',
         'wait_for': 1
         }

    devices_quick_add_device_make_xmc_choice = \
        {
            'CSS_SELECTOR': '.chzn-results li[data-automation-tag="chzn-option-XMC"]',
            'wait_for': 5
        }

    devices_xiqse_serial_text_area = \
        {
         'CSS_SELECTOR': '.serial-numbers.xmc',
         'wait_for': 1
         }

    devices_quick_add_location_field = \
        {
            'CSS_SELECTOR': '.location-input',
            'wait_for': 5
         }

    # This Xpath has been changed to a more specific path in order to solve an interminte
    devices_quick_add_policy_drop_down = \
        {
            'XPATH': '//table[@data-automation-tag="automation-quick-add-onboard-policy-select"]//tbody//tr//td[2]',
            'CSS_SELECTOR': 'div[class="policy-list-el"][data-dojo-attach-point="networkPolicyListCtn"]',
            'wait_for': 1
         }

    devices_quick_add_policy_drop_down_items = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-policy-select-dropdown"]'
                     '//tr[contains(@class, "dijitMenuItem")]',
            'wait_for': 5
        }

    devices_quick_add_block_show = \
        {
            'CSS_SELECTOR': '.show-quick-add',
            'wait_for': 1
        }

    devices_add_devices_cancel_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-cancel-button"]',
            'wait_for': 5
         }

    device360_cells_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 5
        }

    device_type_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickAddCtn"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5,
            'index': 0
        }

    device_type_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickAddCtn"]'
                     '//ul[contains(@class, "qa-chzn-results-quickdeviceselect")]//li',
            'wait_for': 5
        }

    device_make_drop_down = \
        {
            # 'XPATH': '//div[@data-dojo-attach-point="quickMakeSelect"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            # 'index': 0
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-make-select"]',
            'wait_for': 5
        }

    device_make_drop_down_options = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-make-select-dropdown"]  //td[@data-dojo-attach-point="containerNode,textDirNode"]',
            'wait_for': 5
        }

    device_entry_type_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickEntrySelect"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5,
            'index': 0
        }

    device_entry_type_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickEntrySelect"]'
                     '//ul[contains(@class, "qa-chzn-results-quickaddentrytype")]//li',
            'wait_for': 5
        }

    device_entry_csv_upload_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickImportCtn"]'
                     '//div[@data-dojo-attach-point="importFileUploader"]//input[@name="file"]',
            'wait_for': 5,
            'index': 0
        }

    device_entry_voss_csv_upload_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickImportCtn"]'
                     '//div[@data-dojo-attach-point="vossImportFileUploader"]//input[@name="file"]',
            'wait_for': 5,
            'index': 0
        }

    device_entry_exos_csv_upload_button_advanced_onboard = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importCtn"]//div[@data-dojo-attach-point="importFileUploader"]'
                     '//input[@name="file"]',
            'wait_for': 5,
            'index': 0
        }

    devices_table_view_type_drop_down = \
        {
            'CSS_SELECTOR': 'div[class="grid-extras"] [data-automation-tag="automation-chzn-container-ctn"]',
            'XPATH': '//div[@class="grid-extras"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 1
         }

    devices_table_view_type_drop_down_items = \
        {
            'CSS_SELECTOR': '.grid-extras .chzn-drop ul li',
            'XPATH': '//div[@class="grid-extras"]//div[@class="chzn-drop"]/ul/li',
            'wait_for': 1
         }

    devices_switch_assign_policy = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-switch-assign-policy"]',
            'index': 1,
            'wait_for': 5
        }

    devices_switch_assign_policy_dropdown = \
        {
            'XPATH': '//*[@class="ui-dialog-content has-policy"]//div[@data-dojo-attach-point="networkPolicyListCtn"]//span',
            'wait_for': 5
        }

    devices_switch_assign_policy_list = \
        {
            'XPATH': '//*[@class="ui-dialog-content has-policy"]//ul[@class="chzn-results qa-chzn-results-networkpolicylist"]//li',
            'wait_for': 5
        }

    devices_switch_assign_policy_assign_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 5
        }

    devices_switch_update_nw_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="updateNP"]',
            'wait_for': 5
        }

    devices_switch_update_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadBtn"]',
            'wait_for': 5
        }

    device_row_selection_checkbox_selected = \
        {
            'CSS_SELECTOR': 'input[aria-checked="true"]',
            'wait_for': 15
        }

    device_row_selection_checkbox_deselected = \
        {
            'CSS_SELECTOR': 'input[not(aria-checked="true")]',
            'wait_for': 15
        }

    manage_devices_select_all_devices_checkbox_selected = \
        {
            'XPATH': '//*[@class="dgrid-resize-header-container"]//input[@type="checkbox" and @aria-checked="true"]',
            'index': 0,
            'wait_for': 5
        }

    manage_devices_select_all_devices_checkbox_deselected = \
        {
            'XPATH': '//*[@class="dgrid-resize-header-container"]//input[@type="checkbox" and not(@aria-checked="true")]',
            'index': 0,
            'wait_for': 5
        }

    devices_page_grid_rows_all = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]/tr/td[contains(@class, "dgrid-selector")]/../..',
            
         }

    devices_page_grid_rows_selected = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]/tr/td[contains(@class, "dgrid-selector")]/input[@aria-checked="true"]/../..',
            
         }

    devices_page_grid_rows_deselected = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]/tr/td[contains(@class, "dgrid-selector")]/input[not(@aria-checked="true")]/../..',
            
         }

    last_refreshed_tooltip = \
        {
            'XPATH': '//div[@class="ui-tooltip-content"]/span[@data-dojo-attach-point="refreshTime"]',
            
         }

    total_count_label = \
        {
            'XPATH': '//span[@data-dojo-attach-point="gridTotalResults"]',
            
         }

    devices_display_count_per_page_selection_button = \
        {
            'XPATH': '//a[contains(text(),"20")]',
            'wait_for': 3
        }

    devices_pagination_next_button = \
        {
            'XPATH': '//li[@data-dojo-attach-point="pageNext"]//a[@class="J-page-next ui-page-item-next"]',
            'wait_for': 3
        }

    devices_display_count_per_page_buttons = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottom"]//div[@data-dojo-attach-point="gridBottomLeft"]',
            
            'index': 1
         }

    devices_pagination_buttons = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottom"]//div[@data-dojo-attach-point="gridBottomRight"]',
            'wait_for': 3,
            'index': 1
        }

    manage_device_search_clear_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="clearSearchField"]',
            'wait_for': 5
        }

    devices_page_stack_slot_rows = \
        {
            'XPATH': '//div[@class="expando"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }
    devices_stack_update_policy_dropdown_btn = \
        {
            'XPATH': '//div[@data-dojo-attach-point="stackTemplateChooser"]//*[@class="chzn-single"]',
            
        }

    devices_stack_update_policy_dropdown_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="stackTemplateChooser"]//div[@data-automation-tag="automation-chzn-drop-ctn"]//ul//li',
            
        }

    device_stack_toggle = \
        {
            'CSS_SELECTOR': '.stack-toggle',
            'wait_for': 5
        }

    devices_close_button_update = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    devices_perform_update_button_d360 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadBtn"]',
            
        }

    actions_open_site_engine_menu_option = \
        {
            'XPATH': '//a[@type="openSiteEngine"]',
            
        }

    device_make_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-make-select"]',
            'wait_for': 2
        }

    device_type_real_radio_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-real-device-radio-button"]',
            'wait_for': 2
        }

    entry_type_manual_radio_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-manual-type-radio-button"]',
            'wait_for': 2
        }

    entry_type_csv_radio_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-import-type-radio-button"]',
            'wait_for': 2
        }
    device_make_dropdownoption = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-make-select"]',
            'wait_for': 2
        }

    device_service_tag_textbox = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-service-tag-textbox"]',
            'wait_for': 5
        }

    devices_add_devices_menu = \
        {
            'CSS_SELECTOR': '.ui-menu-list',
            'wait_for': 1
         }

    devices_serial_text_area_error = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hcTextareaError"]',
            'wait_for': 5
        }

    devices_mac_text_area_error = \
        {
            "CSS_SELECTOR": ".quick-serial-numbers.invalid.honeycomb-ui-form-textarea",
            'wait_for': 5
        }

    mac_error = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5
        }

    add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="actionLeft"]/div',
            'wait_for': 3
        }

    quick_add_devices = \
        {
            'XPATH': '//*[@class="ui-menu-list"]'
                     '//*[@data-automation-tag="automation-device-list-menu-quick-add-devices"]',
            'wait_for': 3
        }

    deploy_to_cloud = \
        {
            'XPATH': '//a[@type="cloudQuickAdd"]',
            'wait_for': 3
        }

    insert_sn = \
        {
            'CSS_SELECTOR': '.honeycomb-ui-form-textarea-input',
            'wait_for': 3
        }

    devices_add_location_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hcSelectButton"]',
            'wait_for': 5
        }

    devices_select_location = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSelect"]',
            'wait_for': 5
        }

    devices_cancel_location_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-select-location-cancel"]',
            'wait_for': 5
        }

    devices_no_location_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createPlanLink"]',
            'wait_for': 5
        }

    add_devices_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-add-button"]',
            'wait_for': 5
        }

    device_make_list = \
        {
            'XPATH': '//*[@data-dojo-attach-point="containerNode,textDirNode"]',
            'wait_for': 5
        }

    device_make_voss = \
        {
            'XPATH': '//*[@data-dojo-attach-point="containerNode,textDirNode"]//span[contains(text(), "VOSS")]',
            'wait_for': 5
        }

    device_make_exos = \
        {
            'XPATH': '//*[@data-dojo-attach-point="containerNode,textDirNode"]//span[contains(text(), "EXOS")]',
            'wait_for': 5
        }
    device_make_aerohive = \
        {
            'XPATH': '//*[@data-dojo-attach-point="containerNode,textDirNode"]//span[contains(text(), "Extreme - Aerohive")]',
            'wait_for': 5
        }

    quick_onboard_failure_panel = \
        {
            'DESC': 'The Quick Onboard Failure panel.',
            'XPATH': '//div[@data-dojo-attach-point="failureCtn"]//ul',
            'wait_for': 5
        }

    quick_onboard_failure_reason = \
        {
            'DESC': 'Failure Reason displayed within the Quick Onboard Failure panel.',
            'XPATH': '//div[@data-dojo-attach-point="failureCtn"]//span[not(@class)]',
            'wait_for': 5
        }

    quick_onboard_failure_ok_button = \
        {
            'DESC': 'OK button within the Quick Onboard Failure panel',
            'XPATH': '//div[contains(@class,"quick-onboard-dialog")]//button[@data-dojo-attach-point="okBtn"]',
            'wait_for': 5
        }

    device_auto_detection_voss = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vossLine"]',
            'wait_for': 5
        }

    device_auto_detection_exos = \
        {
            'XPATH': '//*[@data-dojo-attach-point="exosLine"]',
            'wait_for': 5
        }

    deploy_locally = \
        {
            'XPATH': '//a[@type="localQuickAdd"]',
            'wait_for': 3
        }

    sn_error_message = \
        {
            'XPATH': '//div[@data-dojo-attach-point="serialNumberSection"]//*[@data-dojo-attach-point="hcTextareaError"]',
            'wait_for': 3
        }

    policy_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="policySection"]//div[@class="label-content"]',
            'wait_for': 3
        }

    policy_drop_down_items = \
        {
            'XPATH': '//td[@data-dojo-attach-point="containerNode,textDirNode"]',
            'wait_for': 3
        }

    device_auto_detection_cloudIqEngineRadio = \
        {
            'XPATH': '//li[@data-dojo-attach-point="cloudIqEngineLine"]',
            'wait_for': 5
        }

    select_csv = \
        {
            'XPATH': '//div[@data-dojo-attach-point="entryTypeSection"]//span[contains(text(), "CSV Import")]',
            'wait_for': 5
        }

    device_csv_upload_button = \
        {
            'XPATH': '//div[@class="honeycomb-ui-form-upload-input"]//div[@data-dojo-attach-point="importFileUploader"]//input[@type="file"]',
            'wait_for': 5
        }

    device_auto_detection_wingRadio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="containerNode,textDirNode"]//span[contains(text(), "EXOS")]',
            'wait_for': 5
        }

    device_stack_template = \
        {
            'CSS_SELECTOR': '.field-deviceTemplateName',
            'wait_for': 5
        }

    device_stack_template_click = \
        {
            'CSS_SELECTOR': '.J-template',
            'wait_for': 5
        }

    create_template_click = \
        {
            'XPATH': '//*[contains(text(), "currently")]',
            'wait_for': 5
        }

    create_auto_template_update_device_click = \
        {
            'XPATH': '//*[@class="img-add"]',
            'wait_for': 5
        }

    device_os_voss_radio = \
        {
            'DESC': 'Quick Add Devices, "Fabric Engine" Device OS',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-voss-radio-button"]',
            'wait_for': 10
        }

    device_os_exos_radio = \
        {
            'DESC': 'Quick Add Devices, "Switch Engine" Device OS',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-exos-radio-button"]',
            'wait_for': 10
        }

    device_os_cloudiq_engine_radio = \
        {
            'DESC': 'Quick Add Devices, "Cloud IQ Engine" Device OS',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-cloudiq-engine-radio-button"]',
            'wait_for': 10
        }

    device_os_wing_radio = \
        {
            'DESC': 'Quick Add Devices, "WING" Device OS',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-wing-radio-button"]',
            'wait_for': 10
        }

    device_np_header = \
        {
            'CSS_SELECTOR': ".field-networkPolicyName",
            'wait_for': 5
        }

    ui_tool_tip_inner = \
        {
            'CSS_SELECTOR': ".ui-tooltip-inner",
            'wait_for': 5
        }

    devices_page_horizontal_end = \
        {
            'XPATH': "//*[@data-automation-tag='device-list-grid-header-mgtVlan']",
            'wait_for': 1
        }

    devices_grid_column_headers = \
        {
            'XPATH': '//*[@role="columnheader"]',
            'wait_for': 5
        }

    assign_policy_device_selected = \
        {
            'XPATH': '//div[contains(@class,"dgrid-selected ui-state-active")]//*[@title="Assign Policy"]',
            'wait_for': 5
        }

    devices_switch_update_network_policy = \
        {
            'CSS_SELECTOR': 'input[class="J-up"][data-dojo-attach-point="updateNP"]',
            'wait_for': 5
        }

    devices_switch_update_reboot_rollback = \
        {
            'XPATH': "//li[@data-dojo-attach-point='revertWrap']//label[@class='checkbox']//input[@type='checkbox']",
            'wait_for': 5
        }

    devices_update_yes_btn = \
        {
            'XPATH': '//*[@class="ui-tipbox-con"]//*[@data-automation-tag="automation-notification-yes-btn"]',
            'wait_for': 5

        }

    update_status_failed_selected_device = \
        {
            'XPATH': '//div[contains(@class,"dgrid-selected ui-state-active")]//*[@class="form-error"]',
            'wait_for': 5
        }

    status_update_failed_after_reboot = \
        {
            'XPATH': '//div[contains(@class,"dgrid-selected ui-state-active")]//td[contains(@class,"field-updatedOn")]/div/span',
            'wait_for': 5
        }

    check_pop_message = \
        {
            'XPATH': '//*[@data-dojo-attach-point="revertWrap"]//*[@data-dojo-attach-point="deltaDes"]',
            'wait_for': 5
        }

    check_double_verification_display_rollback = \
        {
            'XPATH': '//*[@data-dojo-attach-point="msgWrap"]//*[@data-dojo-attach-point="msgContainer"]',
            'wait_for': 5
        }

    devices_update_no_btn = \
        {
            'XPATH': '//*[@class="ui-tipbox-con"]//*[@data-automation-tag="automation-notification-no-btn"]',
            'wait_for': 5
        }

    all_messages_banner = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wrapEl"]',
            'wait_for': 5
        }

    upgrade_to_free_pilot_link = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wrapEl"]//a[@class="free-year-upgrade"]',
            'wait_for': 5
        }

    yes_button_upgrade_to_free_pilot = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    check_portal_page = \
        {
            'XPATH': '//div[@class="form-container"]//div[@class="form-row"]',
            'wait_for': 5
        }

    field_license_stat = \
        {
            'CSS_SELECTOR': '.field-licenseState',
            'wait_for': 3,
        }

    license_form_error = \
        {
            'CSS_SELECTOR': '.form-error',
            'wait_for': 3,
        }

    check_unmanage_box = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="unmanageMsg"]',
            'wait_for': 5
        }

    pilot_lic_inventory = \
        {
            'XPATH': '//li[@data-dojo-attach-point="deviceInventory"]//div',
            'wait_for': 5
        }

    sn_button = \
        {
            'XPATH': '//a[@class = "u100SerialNumbersBanner"]',
            'wait_for': 5
        }

    sn_xiq_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]/ul/li',
            'wait_for': 5
        }

    sn_close = \
        {
            'XPATH': '//div[contains(@class,"hmOverride")]//span[@data-dojo-attach-point="closeButtonNode"]',
            'wait_for': 3,
        }

    link_my_account = \
        {
            'XPATH': '//button[@data-dojo-attach-point="portalBtn"]',
            'wait_for': 5
        }

    link_my_account_agree = \
        {
            'XPATH': '//input[@data-dojo-attach-point="iAgree"]',
            'wait_for': 5
        }

    link_my_account_continue = \
        {
            'XPATH': '//button[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 5
        }

    add_a_license = \
        {
            'XPATH': '//span[@data-dojo-attach-point="renewLicense"]',
            'wait_for': 5
        }

    upgrade_account_to_pilot = \
        {
            'XPATH': '//button[@data-dojo-attach-point="upgradeBtn"]',
            'wait_for': 5
        }

    sfdc_username = \
        {
            'XPATH': "//*[@type='text']",
            'wait_for': 5
        }

    sfdc_password = \
        {
            'XPATH': "//*[@type='password']",
            'wait_for': 5
        }

    sfdc_submit = \
        {
            'XPATH': "//*[@type='submit']",
            'wait_for': 5
        }

    sfdc_submit_check_error = \
        {
            'XPATH': '//div[@class="messageText"]',
            'wait_for': 5
        }

    sfdc_unlink = \
        {
            'XPATH': '//button[@data-dojo-attach-point="portalUnlinkBtn"]',
            'wait_for': 5
        }

    submit_shared_cuid = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 3,
        }

    yes_button_unlink = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    subscription_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="licenseCtn"]//div[@data-dojo-attach-point="gridContent"]//div[@class="dgrid-scroller"]//table[@class="dgrid-row-table"]/tr',
            'wait_for': 5
        }

    subscription_available = \
        {
            'CSS_SELECTOR': '.field-available',
            
        }

    subscription_activated = \
        {
            'CSS_SELECTOR': '.field-activated',
            
        }

    message_unlink_button = \
        {
            'XPATH': '//div[contains(@class,"ui-tooltip-text")]//span[@data-dojo-attach-point="contentEl"]',
            'wait_for': 5
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

    ui_banner_error_message = \
        {
            'DESC': 'XIQ UI Banner containing an error message.',
            'XPATH':  '//*[contains(@class, "ui-tipbox ui-tipbox-error") and contains(@data-dojo-attach-point, "wrapEl")]',
            'wait_for': 3
        }

    ui_banner_error_close_button = \
        {
            'DESC': 'XIQ UI Error Banner close button',
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-error"]//i[@class="ui-tipbox-close"]'
        }

    ui_banner_warning_message = \
        {
            'DESC': 'XIQ UI Banner containing a warning message.',
            'XPATH':  '//*[contains(@class, "ui-tipbox ui-tipbox-warning") and contains(@data-dojo-attach-point, "wrapEl")]',
            'wait_for': 3
        }

    ui_banner_warning_close_button = \
        {
            'DESC': 'XIQ UI Warning Banner close button',
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-warning"]//i[@class="ui-tipbox-close"]'
        }

    ui_banner_notice_message = \
        {
            'DESC': 'XIQ UI Banner containing a notice message.',
            'XPATH':  '//*[contains(@class, "ui-tipbox ui-tipbox-notice") and contains(@data-dojo-attach-point, "wrapEl")]',
            'wait_for': 3
        }

    ui_banner_notice_close_button = \
        {
            'DESC': 'XIQ UI Notice Banner close button',
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-notice"]//i[@class="ui-tipbox-close"]'
        }

    license_button = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-licenseMng"]',
            'wait_for': 5
        }

    user_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="accountInfoUsername"]',
            'wait_for': 5
        }

    global_settings = \
        {
            'XPATH': '//li[@data-automation-tag="automation-account-menu-account-link"]',
            'wait_for': 5
        }

    audit_button = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-auditLogs"]',
            'wait_for': 5
        }

    audit_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContainer"]//div[contains(@class, " dgrid-row")]',
            'wait_for': 5
        }

    audit_time_stamp = \
        {
            'CSS_SELECTOR': '.field-timeStamp',
            'wait_for': 5
        }

    field_description = \
        {
            'CSS_SELECTOR': '.field-description',
            'wait_for': 5
        }

    sort_time_stamp = \
        {
            'XPATH': '//th[contains(@class,"field-timeStamp")]//div[contains(@class,"dgrid-resize-header-container")]',
            'wait_for': 5
        }

    field_description_more_button = \
        {
            'CSS_SELECTOR': '.more',
            'wait_for': 5
        }

    more_row_description = \
        {
            'XPATH': '//div[@data-dojo-attach-point="msgContainer"]',
            'wait_for': 5
        }

    more_row_description_close = \
        {
            'XPATH': '//button[@data-automation-tag="automation-notification-no-btn"]',
            'wait_for': 5
        }

    number_of_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContainer"]//div[@class="ui-grid-bottom-left fn-left"]/a',
            'wait_for': 5
        }

    manage_devices_progress_status = \
        {
            'DESC': 'Manage > Devices "devices progress status',
            'XPATH': '//div[contains(@id,"updatedOn")]//div[@class="progress-message"]',
            'wait_for': 10
        }
    
    device_page_size_100 = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottom"]/div/a[@data-size="100"]',
            'wait_for': 3
        }
    
    upgrade_IQ_engine_and_extreme_network_switch_images_checkbox = \
        {
            'XPATH': '//*[@data-automation-tag="automation-config-download-options-update-hive-os"]',
            'wait_for': 5
        }
  
    license_mgmt = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-licenseMng"]',
            'wait_for': 5
        }

    license_unmanage_box = \
        {
            'XPATH': '//span[@data-dojo-attach-point="unmanage"]',
            'wait_for': 5
        }

    update_reboot_revert_checkbox = \
        {
            'XPATH': "//li[@data-dojo-attach-point='revertWrap']//label[@class='checkbox']//input[@type='checkbox']",
        }

    update_image_checkbox = \
        {
            'XPATH': "//div[@class='first column']//label[@class='checkbox']//input[@type='checkbox']",
        }

    update_config_checkbox = \
        {
            'CSS_SELECTOR': ".J-up",
        }

    get_events = \
        {
            'XPATH': "//td/div",
        }

    device_actions_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-button"]',
            'wait_for': 2
        }

    license_action_button = \
        {
            'CSS_SELECTOR': '.dijitMenuItem',
            'wait_for': 5
        }

    port_details_info = \
        {
            'XPATH': '//div[@class="port-info-view"]/div',
            'wait_for': 5
        }

    digital_twin_container_feature = \
        {
            'DESC': 'Quick Add Devices > Directly to the Cloud > Device Type > Digital Twin container',
            'XPATH': '//li[@data-dojo-attach-point="digitalTwinContainer"]'
        }
    device_type_digital_twin_radio_button = \
        {
            'DESC': 'Quick Add Devices > Directly to the Cloud > Device Type > Digital Twin radio button',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-digital-twin-device-radio-button"]'
        }

    digital_twin_os_persona_dropdown = \
        {
            'DESC': 'Quick Add Devices - Digital Twin > OS Persona dropdown menu',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-dt-os-persona-select"]'
        }

    digital_twin_os_persona_dropdown_items = \
        {
            'DESC': 'Quick Add Devices - Digital Twin > OS Persona dropdown menu items',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-dt-os-persona-select-dropdown"]'
                     '//tr[contains(@class, "dijitMenuItem")]'
        }

    digital_twin_device_model_dropdown = \
        {
            'DESC': 'Quick Add Devices - Digital Twin > Device Model dropdown menu',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-dt-model-select"]'
        }

    digital_twin_device_model_dropdown_items = \
        {
            'DESC': 'Quick Add Devices - Digital Twin > Device Model dropdown menu items',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-dt-model-select-dropdown"]'
                     '//tr[contains(@class, "dijitMenuItem")]'
        }

    digital_twin_os_version_dropdown = \
        {
            'DESC': 'Quick Add Devices - Digital Twin > OS Version dropdown menu',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-dt-os-version-select"]'
        }

    digital_twin_os_version_dropdown_items = \
        {
            'DESC': 'Quick Add Devices - Digital Twin > OS Version dropdown menu items',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-dt-os-version-select-dropdown"]'
                     '//tr[contains(@class, "dijitMenuItem")]'
        }

    one_hundred_rows_per_page_button = \
        {
            'XPATH': '//a[@data-size="100"]'
        }
   
    device_model = \
        {
            'CSS_SELECTOR': '.field-productType'
        }

    global_settings_management_dialog = \
        {
            'XPATH': '//*[@data-dojo-attach-point="msgWrap"]',
        }

    global_settings_management_dialog_yes_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
        }

    device_actions_change_os = \
        {
            # The identifier differs depending on which type of device is selected (ap, switch, etc.),
            # so need to get all partial matches and select the displayed element
            'XPATH': '//a[contains(@data-automation-tag, "automation-manage-device-actions-") and contains(@data-automation-tag,"-os-")]',
            'wait_for': 2
        }
        
    utilities_path = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-utilities-button"]',
            'wait_for': 5
        }

    restart_pse_path = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-utilities-restart-pse"]',
            'wait_for': 5
        }

    pse_yes_path = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 5
        }

    loading_bar_path = \
        {
            'XPATH': '//img[@class="widget-loading-image"]',
            'wait_for': 5
        }

    closing_window_path = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    pse_reset_status = \
        {
            'XPATH': '//div[contains(text(),"PSE reset has been completed.")]',
            'wait_for': 5
        }
