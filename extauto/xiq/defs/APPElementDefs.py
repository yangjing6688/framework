class APPElementDefs:

    auto_provisioning_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-autoProvision']",
            'wait_for': 5
        }

    auto_provisioning_add_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    auto_provisioning_delete_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    auto_provisioning_edit_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//span[contains(@data-tip, "Edit")]',
            'wait_for': 5
        }

    auto_provisioning_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    auto_provisioning_desc = \
        {
            'XPATH': '//*[@data-dojo-attach-point="desc"]',
            'wait_for': 5
        }

    auto_provisioning_serial = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableSerial"]',
            'wait_for': 5
        }

    auto_provisioning_serial_assign_devices_list = \
        {
            'XPATH': '//*[@id="ah/util/layout/list/duplex/__List_0"]',
            'wait_for': 5
        }

    auto_provisioning_serial_assign_devices_select_all = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rAll"]',
            'wait_for': 5
        }

    auto_provisioning_serial_assign_devices_deselect_all = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lAll"]',
            'wait_for': 5
        }

    auto_provisioning_serial_assign_devices_select_few = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rSelect"]',
            'wait_for': 5
        }

    auto_provisioning_serial_assign_devices_deselect_few = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lSelect"]',
            'wait_for': 5
        }

    auto_provisioning_serial_assign_devices_manual_enter = \
        {
            'XPATH': '//*[@data-dojo-attach-point="txtSNNode"]',
            'wait_for': 5
        }

    auto_provisioning_IP = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableIP"]',
            'wait_for': 5
        }

    auto_provisioning_ip_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 5
        }

    auto_provisioning_ip_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    auto_provisioning_device_function_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceProp"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]/a',
            'index': 0,
            'wait_for': 5
        }

    auto_provisioning_device_function_list = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-drop-ctn"]'
                     '//*[@class="chzn-results qa-chzn-results-devicefunc,sync-func"]//li',
            'wait_for': 5
        }

    auto_provisioning_device_model_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceProp"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]/a',
            'index': 1,
            'wait_for': 5
        }

    auto_provisioning_device_model_dropdown_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ApType,ctn-Ap"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    auto_provisioning_device_model_dropdown_switch_SR22_23 = \
        {
            'XPATH': '//div[@data-dojo-attach-point="SwitchType,ctn-Switch"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    auto_provisioning_device_model_dropdown_switch_SR20_21 = \
        {
            'XPATH': '//div[@data-dojo-attach-point="SwitchType,ctn-Switch"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    auto_provisioning_device_model_dropdown_switch_dell = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-container-ctn"]'
                     '//span[contains(text(), "All Dell Switches")]',
            'wait_for': 5
        }

    auto_provisioning_network_policy_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-autoprovision-policy-select"]',
            'wait_for': 5
        }

    auto_provisioning_network_policy_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-autoprovision-policy-select"]//li',
            'wait_for': 5
        }

    auto_provisioning_country_code_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-container-ctn"]//span[contains(text(), "--")]',
            'wait_for': 5
        }

    auto_provisioning_country_code_list = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-country-code-select"]'
                     '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    auto_provisioning_assign_location_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-assign-location-btn"]',
            'wait_for': 5
        }

    auto_provisioning_assign_location_search_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="keyword"]',
            'wait_for': 5
        }

    auto_provisioning_assign_location_select_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSelect"]',
            'wait_for': 5
        }

    auto_provisioning_assign_location_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancel"]',
            'wait_for': 5
        }

    auto_provisioning_loation_ip_subnet_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="actionLeft"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    auto_provisioning_loation_ip_subnet_delete_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="actionLeft"]//span[data-tip="Delete"]',
            'wait_for': 5
        }

    auto_provisioning_enable_Upload_Auth = \
        {
            'XPATH': '//*[data-dojo-attach-point="enableUploadAuth"]',
            'wait_for': 5
        }

    auto_provisioning_Upload_Auth_golden_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadGoldenOption"]',
            'wait_for': 5
        }

    auto_provisioning_Upload_Auth_latest_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadLatestOption"]',
            'wait_for': 5
        }

    auto_provisioning_enable_Upload_Auto = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableUploadAuto"]',
            'wait_for': 5
        }

    auto_provisioning_enable_Reboot = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableReboot"]',
            'wait_for': 5
        }

    auto_provisioning_enable_device_credential = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-enable-credentials"]',
            'wait_for': 5
        }

    auto_provisioning_device_credential_root_admin_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rootAdminName"]',
            'wait_for': 5
        }

    auto_provisioning_device_credential_root_admin_password = \
        {
            'XPATH': '//*[@data-validid="rootAdminPassword.norEl"]',
            'wait_for': 5
        }

    auto_provisioning_device_credential_readonly_admin_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="readOnlyAdminName"]',
            'wait_for': 5
        }

    auto_provisioning_device_credential_readonly_admin_password = \
        {
            'XPATH': '//*[@data-validid="readOnlyAdminPassword.norEl"]',
            'wait_for': 5
        }

    auto_provisioning_enable_capwap = \
        {
            'XPATH': '//*[@data-automation-tag="automation-common-object-autoprovision-enable-capwap"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_primary_server_input = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_2"]//input[@data-dojo-attach-point="ipEl"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_primary_server_add = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_2"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_ip_addr = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="ipTypeList"]//li[@data-type="ip-address-profile"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_hostname = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="ipTypeList"]//li[@data-type="host-name-profile"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_ip_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_ip_IPaddr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_hostname_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_add_hostname_hostname = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hostName"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_primary_server_edit = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_2"]//span[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_backup_server_input = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipEl"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_backup_server_add = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_backup_server_edit = \
        {
            'XPATH': '//div[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 5
        }

    auto_provisioning_capwap_shared_key_passphrase = \
        {
            'XPATH': '//div[@class="grid_9 last column last column"]//input[@data-dojo-attach-point="norEl"]',
            'wait_for': 5
        }

    auto_provisioning_save_button = \
        {
            'XPATH': '//div[@class="auto-provision"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    auto_provisioning_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    auto_provision_grid = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-autoprovision-provision-list"]',
            'wait_for': 5
        }

    auto_provision_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 5
        }

    auto_provisioning_grid_header = \
        {
            'XPATH': '//table[@class="dgrid-row-table" and @id="dgrid_3-header"]',
            'wait_for': 5
        }

    auto_provision_enable = \
        {
            'NAME': 'services-field-1',
            'wait_for': 5
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
            'wait_for': 5
        }

    auto_provisioning_alert_yes = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    auto_provisioning_select_all_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'wait_for': 5
        }
