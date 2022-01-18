class RSWebElementsDefinitions:
    default_radius_server_group_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="defaultRadiusGroupArea"]//span[@data-dojo-attach-point="defBtn"]',
            'wait_for': 5
        }

    default_radius_server_group_dialog = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }

    default_radius_server_group_dialog_rsg_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-reusable-grid"]//table[@class="dojoxGridRowTable"]',
            'wait_for': 5
        }

    default_radius_server_group_dialog_cancel_button = \
        {
            'XPATH': '//div[@class="dijitDialogPaneContent"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    default_radius_server_group_dialog_rsg_row_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'wait_for': 5
        }

    default_radius_server_group_dialog_select_button = \
        {
            'XPATH': '//div//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 5
        }

    default_radius_server_group_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addRadiusGroup"]',
            'wait_for': 1
        }

    config_radius_server_dialog_window = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }

    radius_server_group_name_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 1
        }

    external_radius_server = \
        {
            'XPATH': '//*[@data-dojo-attach-point="extSelLabel"]',
            'wait_for': 1
        }

    radius_server_list = \
        {
            'CSS_SELECTOR': '.radius-list.line.mt5',
            'wait_for': 1
        }

    radius_server_list_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row-table',
            'wait_for': 1
        }

    radius_server_list_row_select_checkbox = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'index': 0,
            'wait_for': 1
        }

    radius_server_save_radius_button = \
        {
            'CSS_SELECTOR': '.btn.btn-primary-2',
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 1
        }

    radius_server_list_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="addServer"]',
            'wait_for': 5
        }

    new_external_radius_server_name_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 1
        }

    new_external_radius_server_ip_host_select_drop_down = \
        {
            'CSS_SELECTOR': '.ui-ip-mark.ui-ip-inactive',
            'wait_for': 1
        }

    popup_elment = \
        {
            'CSS_SELECTOR': '.dijitPopup.Popup',
            'wait_for': 1
        }

    new_external_radius_server_ip_list_items = \
        {
            'CSS_SELECTOR': '.ui-ip-list-item',
            'wait_for': 1
        }

    new_external_radius_server_ip_list_item = \
        {
            'CSS_SELECTOR': '.J-ip-item',
            'wait_for': 1
        }

    new_external_radius_server_ip_host_add_button = \
        {
            'XPATH': '//div[@class="external-radius-server"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 1
        }

    new_external_radius_server_ip_host_select_items = \
        {
            'CSS_SELECTOR': '.ui-ip-types-item.J-ip-type',
            'wait_for': 1
        }

    new_external_radius_server_host_name_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5,
            'index': 1
        }

    new_external_radius_server_ip_address_field= \
        {
            'XPATH': '//input[@class="ip-object-field ip-value"]',
            'wait_for': 5,
        }

    new_external_radius_server_save_ip_button = \
        {
            'XPATH': '//button[contains(@data-dojo-attach-point, "saveBtn") and contains(text(), "Save IP Object")]',
            'wait_for': 5
        }

    external_radius_server_shared_secret_field = \
        {
            'XPATH': '//input[@data-validid="sharedSecret.norEl"]',
            'wait_for': 1
        }

    external_radius_server_save_button = \
        {
            'CSS_SELECTOR': ".btn.btn-primary-2",
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 1
        }

    extreme_networks_radius_server = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahSelLabel"]',
            'wait_for': 1
        }

    extreme_networks_radius_server_db_scroll_button = \
        {
            'XPATH': '//span[contains(text(),"Active Directory")]',
            'wait_for': 3
        }

    extreme_networks_radius_server_db_scroll_all_items = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-basetype',
            'wait_for': 5
        }

    extreme_networks_radius_server_db_item = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    extreme_networks_radius_server_list = \
        {
            'CSS_SELECTOR': '.radius-list.mt10',
            'wait_for': 1
        }

    extreme_networks_radius_server_list_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row-table',
            'wait_for': 1
        }

    extreme_networks_radius_server_list_row_select_checkbox = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'index': 0,
            'wait_for': 1
        }

    user_db_active_directory_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="base-ad"]',
            'wait_for': 1,
        }

    user_db_local_database_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="base-local"]',
            'wait_for': 1,
        }

    user_db_ldap_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="base-ldap"]',
            'wait_for': 1,
        }

    get_extreme_networks_radius_server_aaa_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="base-ldap"]',
            'wait_for': 1,
        }

    new_extreme_networks_radius_server_field_parent = \
        {
            'CSS_SELECTOR': '.radius-client-name-ctn.mb30',
            'wait_for': 1,
        }

    new_extreme_networks_radius_server_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameEl"]',
            'index': 1,
            'wait_for': 1
        }

    extreme_networks_radius_server_approved_clients_tab = \
        {
            'XPATH': '//a[contains(text()," APPROVED RADIUS CLIENTS")]',
            'wait_for': 3
        }

    extreme_networks_radius_server_ip_host_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipSave"]',
            'wait_for': 1
        }

    extreme_networks_radius_server_add_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'index': 8,
            'wait_for': 1
        }

    extreme_networks_radius_server_select_button = \
        {
            'CSS_SELECTOR': '.ui-ip-mark',
            'index': 1,
            'wait_for': 1
        }

    extreme_networks_radius_server_shared_secret_field = \
        {
            'XPATH': '//*[@id="ah/util/form/ObscureInput_12"]/div/div[2]/div[1]/input',
            'wait_for': 1
        }

    extreme_networks_radius_server_shared_secret_field1 = \
        {
            'XPATH': '//*[@id="ah/util/form/ObscureInput_13"]/div/div[2]/div[1]/input',
            'wait_for': 1
        }

    extreme_networks_device_as_radius_server_list = \
        {
            'CSS_SELECTOR': '.mt20',
            'wait_for': 1
        }

    extreme_networks_device_as_radius_server_rows = \
        {
            'CSS_SELECTOR': '.dojoxGridRowTable',
            'wait_for': 1
        }

    extreme_networks_device_as_radius_server_list_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="radiusServerCtn"]//div[@data-dojo-attach-point="addServer1"]',
            'wait_for': 1
        }

    extreme_networks_device_as_radius_server_row_select_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'index': 0,
            'wait_for': 1
        }

    extreme_networks_device_as_radius_server_shared_secret_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="norEl"]',
            'wait_for': 1
        }

    extreme_networks_radius_server_select_db_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="localCtn"]//span[@data-tip="Select"]',
            'wait_for': 5
        }

    user_group_select_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-select',
            'wait_for': 1,
        }

    user_group_dialog_window = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }
    user_group_select_dialog_local_db_tab = \
        {
            'CSS_SELECTOR': '.ui-tab',
            'wait_for': 1
        }

    user_group_select_dialog_usergroup_rows = \
        {
            'CLASS_NAME': 'dojoxGridRowTable',
            'wait_for': 1
        }

    user_group_dialog_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-cancel',
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 1
        }

    usergroup_dialog_usergroup_row_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector.dijitReset.dijitReset.dijitCheckBox',
            'wait_for': 1
        }

    usergroup_dialog_select_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="linkButton"]',
            'CSS_SELECTOR': '.btn.btn-small.btn-primary.fn-right',
            'wait_for': 1
        }

    radius_server_group_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-reusable-grid"]//span[@data-tip="Delete"]',
            'CSS_SELECTOR': '.table-action-icons.table-remove',
            'wait_for': 1
        }

    radius_server_group_delete_confirm_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 1
        }