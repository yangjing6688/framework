class APPElementDefs:

    auto_provisioning_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-autoProvision']",
        }

    auto_provisioning_add_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//span[@data-tip="Add"]',
        }

    auto_provisioning_delete_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//span[@data-tip="Delete"]',
        }

    auto_provisioning_edit_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//span[contains(@data-tip, "Edit")]',
        }

    auto_provisioning_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
        }

    auto_provisioning_desc = \
        {
            'XPATH': '//*[@data-dojo-attach-point="desc"]',
        }

    auto_provisioning_serial = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableSerial"]',
        }

    auto_provisioning_serial_assign_devices_list = \
        {
            'XPATH': '//*[@id="ah/util/layout/list/duplex/__List_0"]',
        }

    auto_provisioning_serial_assign_devices_select_all = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rAll"]',
        }

    auto_provisioning_serial_assign_devices_deselect_all = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lAll"]',
        }

    auto_provisioning_serial_assign_devices_select_few = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rSelect"]',
        }

    auto_provisioning_serial_assign_devices_deselect_few = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lSelect"]',
        }

    auto_provisioning_serial_assign_devices_manual_enter = \
        {
            'XPATH': '//*[@data-dojo-attach-point="txtSNNode"]',
        }

    auto_provisioning_IP = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableIP"]',
        }

    auto_provisioning_ip_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelBtn"]',
        }

    auto_provisioning_ip_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
        }

    auto_provisioning_device_function_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceProp"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]/a',
            'index': 0,
        }

    auto_provisioning_device_function_list = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-drop-ctn"]'
                     '//*[@class="chzn-results qa-chzn-results-devicefunc,sync-func"]//li',
        }

    auto_provisioning_device_model_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceProp"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]/a',
            'index': 1,
        }

    auto_provisioning_device_model_dropdown_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ApType,ctn-Ap"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
        }

    auto_provisioning_device_model_dropdown_list_SR22_23 = \
        {
            'XPATH': '//div[@data-dojo-attach-point="SwitchType,ctn-Switch"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
        }

    auto_provisioning_device_model_dropdown_switch_SR22_23 = \
        {
            # 'XPATH': '//div[@data-dojo-attach-point="SwitchType,ctn-Switch"]'
            #          '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'XPATH': '//span[contains(text(),"All Extreme Networks SR22xx / SR23xx Switches")]',
        }

    auto_provisioning_device_model_dropdown_switch_SR20_21 = \
        {
            'XPATH': '//div[@data-dojo-attach-point="SwitchType,ctn-Switch"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
        }

    auto_provisioning_device_model_dropdown_switch_dell = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-container-ctn"]'
                     '//span[contains(text(), "All Dell Switches")]',
        }

    auto_provisioning_network_policy_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-autoprovision-policy-select"]',
        }

    auto_provisioning_network_policy_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-autoprovision-policy-select"]//li',
        }

    auto_provisioning_country_code_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-container-ctn"]//span[contains(text(), "--")]',
        }

    auto_provisioning_country_code_list = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-country-code-select"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
        }

    auto_provisioning_assign_location_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-assign-location-btn"]',
        }

    auto_provisioning_assign_location_search_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="keyword"]',
        }

    auto_provisioning_assign_location_select_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSelect"]',
        }

    auto_provisioning_assign_location_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancel"]',
        }

    auto_provisioning_loation_ip_subnet_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="actionLeft"]//span[@data-tip="Add"]',
        }

    auto_provisioning_loation_ip_subnet_delete_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="actionLeft"]//span[data-tip="Delete"]',
        }

    auto_provisioning_enable_Upload_Auth = \
        {
            'XPATH': '//*[data-dojo-attach-point="enableUploadAuth"]',
        }

    auto_provisioning_Upload_Auth_golden_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadGoldenOption"]',
        }

    auto_provisioning_Upload_Auth_latest_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadLatestOption"]',
        }

    auto_provisioning_enable_Upload_Auto = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableUploadAuto"]',
        }

    auto_provisioning_enable_Reboot = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableReboot"]',
        }

    auto_provisioning_enable_device_credential = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-enable-credentials"]',
        }

    auto_provisioning_device_credential_root_admin_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rootAdminName"]',
        }

    auto_provisioning_device_credential_root_admin_password = \
        {
            'XPATH': '//*[@data-validid="rootAdminPassword.norEl"]',
        }

    auto_provisioning_device_credential_readonly_admin_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="readOnlyAdminName"]',
        }

    auto_provisioning_device_credential_readonly_admin_password = \
        {
            'XPATH': '//*[@data-validid="readOnlyAdminPassword.norEl"]',
        }

    auto_provisioning_enable_capwap = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-enable-capwap"]',
        }

    auto_provisioning_capwap_primary_server_input = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_2"]//input[@data-dojo-attach-point="ipEl"]',
        }

    auto_provisioning_capwap_primary_server_add = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_2"]//span[@data-dojo-attach-point="ipSave"]',
        }

    auto_provisioning_capwap_add_ip_addr = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="ipTypeList"]//li[@data-type="ip-address-profile"]',
        }

    auto_provisioning_capwap_add_hostname = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="ipTypeList"]//li[@data-type="host-name-profile"]',
        }

    auto_provisioning_capwap_add_ip_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameEl"]',
        }

    auto_provisioning_capwap_add_ip_IPaddr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
        }

    auto_provisioning_capwap_add_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelBtn"]',
        }

    auto_provisioning_capwap_add_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
        }

    auto_provisioning_capwap_add_hostname_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameEl"]',
        }

    auto_provisioning_capwap_add_hostname_hostname = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hostName"]',
        }

    auto_provisioning_capwap_primary_server_edit = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_2"]//span[@data-dojo-attach-point="ipEdit"]',
        }

    auto_provisioning_capwap_backup_server_input = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipEl"]',
        }

    auto_provisioning_capwap_backup_server_add = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipSave"]',
        }

    auto_provisioning_capwap_backup_server_edit = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipEdit"]',
        }

    auto_provisioning_capwap_shared_key_passphrase = \
        {
            'XPATH': '//div[@class="grid_9 last column last column"]//input[@data-dojo-attach-point="norEl"]',
        }

    auto_provisioning_save_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//*[@data-dojo-attach-point="saveButton"]',
        }

    auto_provisioning_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
        }

    auto_provision_grid = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-autoprovision-provision-list"]',
        }

    auto_provision_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
        }

    auto_provisioning_grid_header = \
        {
            'XPATH': '//table[@class="dgrid-row-table" and @id="dgrid_3-header"]',
        }

    auto_provision_enable = \
        {
            'NAME': 'services-field-1',
        }

    common_object_grid_row_cells = \
        {
            'XPATH': '//td[@role="gridcell"]',
            'wait_for': 2
        }

    auto_provisioning_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'index': 0,
        }

    auto_provisioning_alert_yes = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
        }

    auto_provisioning_select_all_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
        }
