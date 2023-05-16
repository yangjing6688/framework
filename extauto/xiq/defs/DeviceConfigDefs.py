class DeviceConfigDefs:
    interface_settings_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-interfaceSettings"]',
            'wait_for': 5
        }

    interface_settings_tab_single_device = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-nav-menu-interface-settings"]',
            'wait_for': 5
        }

    wireless_interface_toggle = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wirelessToggle"]',
            'wait_for': 5
        }

    wifi0_interface_tab = \
        {
            'XPATH': '//div[contains(@class, "ui-tab ui-tab-updated") ]//a[contains(text(), "WiFi0")]',
            'wait_for': 5
        }

    wifi1_interface_tab = \
        {
            'XPATH': '//div[contains(@class, "ui-tab ui-tab-updated") ]//a[contains(text(), "WiFi1")]',
            'wait_for': 5
        }

    wifi2_interface_tab = \
        {
            'XPATH': '//div[contains(@class, "ui-tab ui-tab-updated") ]//a[contains(text(), "WiFi2")]',
            'wait_for': 5
        }

    override_client_mode_wifi0_checked = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage2GHzClientMode"]',
            'wait_for': 5
        }

    override_client_mode_wifi1_checked = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage5GHzClientMode"]',
            'wait_for': 5
        }

    override_client_access_wifi0_checked = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage2GHzClientAccess"]',
            'wait_for': 5
        }

    override_client_access_wifi1_checked = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage5GHzClientAccess"]',
            'wait_for': 5
        }

    override_add_client_mode_wifi0_profile = \
        {
            'XPATH': '//span[@data-dojo-attach-point="addClientModeProfileLink2GHz"]',
            'wait_for': 5
        }

    override_add_client_mode_wifi1_profile = \
        {
            'XPATH': '//span[@data-dojo-attach-point="addClientModeProfileLink5GHz"]',
            'wait_for': 5
        }

    override_wifi0_1_client_mode_profile_name = \
        {
            'XPATH': '//div[@data-dojo-attach-point="nameArea"]//input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_checkbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableLocalWeb"]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_add = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ssidListWrap"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_ssid_textbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ssid"]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_password_textbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="password"]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_auth_dropdown = \
        {
            'DESC': 'Auth Method click to dropdown',
            'XPATH': '//input[@data-dojo-attach-point="ssid"]//following::div[@data-automation-tag="automation-chzn-arrow-down"][1]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_auth_dropdown_option = \
        {
            'DESC': 'Auth Method Pre-Shared key/Open',
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-securitytype"]/li',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_key_type_dropdown = \
        {
            'DESC': 'Key Type click to dropdown',
            'XPATH': '//input[@data-dojo-attach-point="ssid"]//following::div[@data-automation-tag="automation-chzn-arrow-down"][2]',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_key_type_dropdown_option = \
        {
            'DESC': 'Key Type ASCII/HEX',
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-keytype"]/li',
            'wait_for': 5
        }

    override_wifi0_1_cm_local_web_page_add_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="addToSsid"]',
            'wait_for': 5
        }

    override_wifi0_1_client_mode_profile_dhcp_server_scope = \
        {
            'XPATH': '//input[@data-dojo-attach-point="dhcpServerScope"]',
            'wait_for': 5
        }

    override_wifi0_1_client_mode_profile_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    override_wifi0_ssid_broadcast_ssid_field = \
        {
            'XPATH': '//tbody[@data-dojo-attach-point="wifi0_SsidAreaContents"]//input[@name="SsidBroadcastName"]',
            'wait_for': 5
        }

    override_wifi0_psk_password = \
        {
            'XPATH': '//tbody[@data-dojo-attach-point="wifi0_SsidAreaContents"]//input[@name="SsidPsk"]',
            'wait_for': 5
        }

    interface_settings_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="interfaceSettingsContainer"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    configuration_tab = \
        {
            'XPATH': '//li[@data-dojo-attach-point="configureViewSelect"]/a',
            'wait_for': 5
        }

    device_360_page = \
        {
            'CSS_SELECTOR': '.device-entity.modal-360',
            'wait_for': 5
        }

    device_configuration_tab = \
        {
            'XPATH': '//li[@data-dojo-attach-point="deviceConfigurationTab"]',
            'wait_for': 5
        }

    device_configuration_node = \
        {
            'CSS_SELECTOR': '.device-config-node',
            'wait_for': 5
        }

    device_configuration_dhcp_checkbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="dhcpAddressOnly"]',
            'wait_for': 5
        }

    close_device360_dialog_window = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    wireless_interface_wifi0_channel_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="chzn-container-ctn"]//a[@class="chzn-single"]',
            'index': 5,
            'wait_for': 5
        }

    wireless_interface_wifi0_channel_options = \
        {
            'XPATH':  '//*[@data-automation-tag="automation-interface-settings-wifi0-channel-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    wireless_interface_wifi1_channel_drop_down = \
        {
            'XPATH': '//a[contains(@class, "qa-chzn-results-channel5ghz")]',
            'wait_for': 5
        }

    wireless_interface_wifi1_channel_options = \
        {
            'XPATH': '//*[@data-automation-tag="automation-interface-settings-wifi1-channel-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    wireless_interface_wifi2_channel_options = \
        {
            'XPATH': '//div[@class="grid_10 column"]//*[@data-automation-tag="automation-interface-settings-wifi1-radio-profile-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    wireless_wifi0_radio_profile_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="chzn-container-ctn"]//a[@class="chzn-single"]',
            'index': 2,
            'wait_for': 5
        }

    wireless_wifi0_radio_profile_options = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-wirelessporttype2ghz,wirelessporttype5dualghz"]//li',
            'wait_for': 5
        }

    wireless_wifi1_radio_profile_drop_down = \
        {
            'XPATH': '//a[contains(@class, "qa-chzn-results-wirelessporttype5ghz")]',
            'wait_for': 5
        }

    wireless_wifi2_radio_profile_options = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-wirelessporttype5ghz"]//li',
            'wait_for': 5
        }

    manage_devices_select_all_devices_checkbox = \
        {
            'XPATH': '//*[@class="dgrid-resize-header-container"]//input[@type="checkbox"]',
            'index': 0,
            'wait_for': 5
        }

    manage_devices_edit_interface_settings_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-interfaceSettings"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_link = \
        {
            'CSS_SELECTOR': '.header-toggle-caret',
            'index': 0,
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi0_tab = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wirelessContent"]//a[contains(text(), "WiFi0")]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi1_tab = \
        {
            'CSS_SELECTOR': '.ui-tab.ui-tab-updated',
            'index': 1,
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi0_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableWifi0RadioStatus"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi0_on_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifi0RadioStatus-on"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi0_off_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifi0RadioStatus-off"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi1_on_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifi1RadioStatus-on"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_wifi1_off_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifi1RadioStatus-off"]',
            'wait_for': 5
        }

    wireless_interface_wifi0_transmission_mode_auto = \
        {
            'XPATH': '//*[@data-dojo-attach-point="powerType2GHz-auto"]',
            'wait_for': 5
        }

    wireless_interface_wifi0_transmission_mode_manual = \
        {
            'XPATH': '//*[@data-dojo-attach-point="powerType2GHz-manual"]',
            'wait_for': 5
        }

    wireless_interface_wifi1_transmission_mode_auto = \
        {
            'XPATH': '//*[@data-dojo-attach-point="powerType5GHz-auto"]',
            'wait_for': 5
        }

    wireless_interface_wifi1_transmission_mode_manual = \
        {
            'XPATH': '//*[@data-dojo-attach-point="powerType5GHz-manual"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    wifi1_transmission_power_slider_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPower5GBar_20"]'
                     '//div[@data-dojo-attach-event="press:_onHandleClick"]',
            'wait_for': 5
        }

    wifi0_transmission_power_slider_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPower2GBar_20"]'
                     '//div[@data-dojo-attach-event="press:_onHandleClick"]',
            'wait_for': 5
        }

    wifi1_transmission_power_value_text = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPowerArea5g"]'
                     '//div[@data-dojo-attach-point="sliderBarContainer"]//div[@class="tip-default toolTip-up"]',
            'wait_for': 5
        }

    wifi0_transmission_power_value_text = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPowerArea2g"]'
                     '//div[@data-dojo-attach-point="sliderBarContainer"]//div[@class="tip-default toolTip-up"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="interfaceSettingsContainer"]//a[@class="btn btn-cancel"]',
            'wait_for': 5
        }

    device_override_configure_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureViewSelect"]//a',
            'wait_for': 5
        }

    device_override_monitor_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="monitorViewSelectText"]//a',
            'wait_for': 5
        }

    device_override_configure_device_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureNav"]//li[@data-id="deviceconfiguration"]',
            'wait_for': 5
        }

    device_override_configure_exos_device_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureNav"]//li[@data-id="deviceconfiguration"]',
            'wait_for': 5
        }

    device_override_configure_host_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hostName"]',
            'wait_for': 5
        }

    device_override_save_device_configuration = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceconfiguration"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device_override_exos_save_device_configuration = \
        {
            'XPATH': '//button[contains(.//text(),"Save Configuration")]',
            'wait_for': 5
        }

    device_override_configure_interface_settings_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureNav"]//li[@data-dojo-attach-point="interfaceSettingsTab"]',
            'wait_for': 5
        }

    device_override_configure_interface_settings_wifi0_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidTab"]//a[contains(text(),"WiFi0")]',
            'wait_for': 5
        }

    device_override_configure_interface_settings_wifi1_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidTab"]//a[contains(text(),"WiFi1")]',
            'wait_for': 5
        }

    device_override_configure_interface_settings_wifi0_radio_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidTab"]//input[@data-dojo-attach-point="enableWifi0RadioStatus"]',
            'wait_for': 5
        }

    device_override_configure_interface_settings_wifi1_radio_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidTab"]//input[@data-dojo-attach-point="enableWifi1RadioStatus"]',
            'wait_for': 5
        }

    device_override_configure_wireless_interface_link = \
        {
            'CSS_SELECTOR': '.header-toggle-caret',
            'index': 0,
            'wait_for': 5
        }

    device_edit_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-device-list-bulkEdit-btn"]',
            'wait_for': 5
        }

    close_dialog = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeDialog']",
            'wait_for': 5
        }

    device_edit_wifi0_operating_mode_area= \
        {
            'XPATH': '//div[@data-dojo-attach-point="dualGHzArea"]',
            'wait_for': 5,
            'index': 0
        }

    device_edit_wifi0_operating_mode_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="dualGHzArea"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5,
            'index': 0
        }

    device_edit_wifi0_operating_mode_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="dualGHzArea"]'
                     '//ul[contains(@class, "qa-chzn-results-dualghz")]//li',
            'wait_for': 5
        }

    device_edit_template_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="chzn-drop-ctn"]'
                     '//ul[contains(@class, "chzn-results qa-chzn-results-devicetemplate")]//li',
            'wait_for': 5
        }

    device_edit_template_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceTemplateArea"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    device_edit_template_text = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceTemplate"]',
            'wait_for': 5
        }

    devices_edit_config_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureViewSelect"]/a',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_close_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    # Defs for Supplemental cli

    device_supplemental_cli_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cliSupplementArea"]'
                     '//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    device_select_supplemental_cli_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]'
                     '//ul[contains(@class, "item-area")]//li',
            'wait_for': 5
        }

    device_config_supplemental_cli_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cliSupplementArea"]'
                     '//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    device_config_supplemental_cli_edit_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cliSupplementArea"]'
                     '//span[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 5
        }

    device_supplemental_cli_config_enter_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    device_supplemental_cli_enter_commands = \
        {
            'XPATH': '//textarea[@data-dojo-attach-point="cli"]',
            'wait_for': 5
        }

    device_supplemental_cli_save_button = \
        {
            'XPATH': '//div[@componentpath="CLISupplementObject"]'
                     '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device_supplemental_cli_config_cancel_button = \
        {
            'XPATH': '//div[@componentpath="CLISupplementObject"]'
                     '//button[contains(.//text(),"Cancel")]',
            'wait_for': 5
        }

    device_open_config_audit_view = \
        {
            'XPATH': '//div[contains(@class, "dgrid-selected ui-state-active")]'
                     '//span[@title="Configuration Audit"]',
            'wait_for': 5
        }

    device_config_audit_audit_view = \
        {
            'XPATH': '//div[@componentpath="AHDialog"]'
                     '//a[contains(text(), "Audit")]',
            'wait_for': 5
        }

    device_config_audit_delta_view = \
        {
            'XPATH': '//div[@componentpath="AHDialog"]'
                     '//a[contains(text(), "Delta")]',
            'wait_for': 5
        }

    device_config_audit_complete_view = \
        {
            'XPATH': '//a[contains(text(), "Complete")]',
            'wait_for': 5
        }

    device_config_audit_audit_view_content = \
        {
            'XPATH': '//div[@data-dojo-attach-point="auditCtn"]',
            'wait_for': 5
        }

    device_config_audit_delta_view_content = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deltaCtn"]',
            'wait_for': 5
        }

    device_config_audit_complete_view_content = \
        {
            'XPATH': '//div[@data-dojo-attach-point="fullCtn"]',
            'wait_for': 5
        }

    device_config_audit_view_close_button = \
        {
            'XPATH': '//button[contains(.//text(),"Close")]',
            'wait_for': 5
        }

    common_obj_basic_supplemental_cli_tab = \
        {
            'XPATH': '//a[@type="Supplemental CLI Objects"]',
            'wait_for': 5
        }

    select_supplemental_cli_object_rows = \
        {
            'CSS_SELECTOR': '.dojoxGridRow',
            'wait_for': 5
        }

    select_supplemental_cli_checkbox = \
        {
            'CSS_SELECTOR': '.dijitCheckBox',
            'wait_for': 5
        }

    supplemental_cli_delete_button = \
        {
            'XPATH': '//*[@data-tip="Delete"]',
            'wait_for': 5
        }

    supplemental_cli_delete_confirm_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    device_events_select_severity = \
        {
            'XPATH': '//table[@data-dojo-attach-point="_buttonNode,tableNode,focusNode,_popupStateNode"]',
            'wait_for': 5
        }

    severity_dropdown_options = \
        {
            'XPATH': '(//*[contains(@class,"dijit dijitReset dijitMenuTable")])[1]//tr/td[@data-dojo-attach-point="containerNode,textDirNode"]',
            'wait_for': 5
        }

    device_config_wireless_interfaces_wifi2_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wirelessContent"]//*[contains(text(),"WiFi2")]',
            'wait_for': 5
        }

    device_config_wireless_interfaces_wifi2_status_radio_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableWifi2RadioStatus"]',
            'wait_for': 5
        }

    device_config_wireless_interfaces_wifi2_primary_server_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="airDefensePrimaryServerIP"]',
            'wait_for': 5
        }

    device_config_wireless_interfaces_wifi2_primary_server_port_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="airDefensePrimaryPort"]',
            'wait_for': 5
        }

    device_config_wireless_interfaces_wifi2_secondary_server_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="airDefenseSecondaryServerIP"]',
            'wait_for': 5
        }

    device_config_wireless_interfaces_wifi2_secondary_server_port_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="airDefenseSecondarPort"]',
            'wait_for': 5
        }

    manage_device_edit_wireless_interface_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="interfaceSettingsContainer"]'
                     '//button[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 5
        }

    manage_device_edit_wireless_interface_save_button = \
        {
            'XPATH': '//*[@class="entity-interface-settings"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    manage_device_interface_settings_save_button_disabled = \
        {
            'XPATH': '//*[@data-dojo-attach-point="interfaceSettingsContainer"]//button[@disabled]',
            'wait_for': 5
        }

    wifi2_transmission_power_textfield_input = \
        {
            'XPATH': '//*[@data-automation-tag="interface-settings-wifi2-transmission-power-slider-20-tip-default"]/input',
            'wait_for': 5
        }

    wifi2_transmission_power_textfield = \
        {
            'XPATH': '//*[@data-automation-tag="interface-settings-wifi2-transmission-power-slider-20-tip-default"]/span',
            'wait_for': 5
        }

    wireless_interface_wifi2_transmission_mode_auto = \
        {
            'XPATH': '//*[@data-automation-tag="interface-settings-wifi2-power-type-auto"]',
            'wait_for': 5
        }

    wireless_interface_wifi2_transmission_mode_manual = \
        {
            'XPATH': '//*[@data-automation-tag="interface-settings-wifi2-power-type-manual"]',
            'wait_for': 5
        }

    wireless_wifi2_channel_list = \
        {
            'XPATH': '//li[@data-automation-tag="automation-interface-settings-wifi1-radio-profile-chzn-option-',
            'wait_for': 5
        }

    wifi2_Radio_Profile_confirmation_button_yes = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    interface_settings_update_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deployNowBtn"]',
            'wait_for': 5
        }

    interface_settings_perform_update_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadBtn"]',
            'wait_for': 5
        }


    wifi2_transmission_power_value_text = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPowerArea6g"]//div[@data-dojo-attach-point="sliderBarContainer"]//div[@class="tip-default toolTip-up"]',
            'wait_for': 5
        }

    wifi2_transmission_power_slider_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPower6GBar_20"]//div[@data-dojo-attach-event="press:_onHandleClick"]',
            'wait_for': 5
        }

    total_unique_clients = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientsNum"]//span[1]',
            'wait_for': 5
        }

    go_to_clients = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-nav-menu-connected-clients"]',
            'wait_for': 5
        }

    total_client_count = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-client-counts"]//div[@data-dojo-attach-point="totalClientCount"]',
            'wait_for': 5
        }

    poor_client_count = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-client-counts"]//div[@data-dojo-attach-point="poorClientCount"]',
            'wait_for': 5
        }

    unique_clients_search_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="searchTerm"]',
            'wait_for': 5
        }

    client_connection_type = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-connectionType w70"]',
            'wait_for': 5
        }

    client_os_type = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-osType w80 fn-ellipsis"]',
            'wait_for': 5
        }

    client_connection_status = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-connectionStatus w200"]',
            'wait_for': 5
        }

    client_health_status = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-clientHealthStatus w100"]',
            'wait_for': 5
        }

    client_hostname = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-hostName w100 fn-ellipsis"]',
            'wait_for': 5
        }

    client_mac = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-clientMac w110 fn-ellipsis"]',
            'wait_for': 5
        }

    client_IPv4 = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-ipAddress w100"]',
            'wait_for': 5
        }

    client_IPv6 = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-ipv6Address w255"]',
            'wait_for': 5
        }

    client_user_name = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-userName w75 fn-ellipsis"]',
            'wait_for': 5
        }

    client_vlan = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-vlan w100"]',
            'wait_for': 5
        }

    client_connected_via = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-ssid w100"]',
            'wait_for': 5
        }

    client_rssi = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-rssi w100 fn-ellipsis"]',
            'wait_for': 5
        }

    client_snr = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-cell-0-snr w100 fn-ellipsis"]',
            'wait_for': 5
        }

    wireless_wifi_device_model = \
        {
            'XPATH': '//span[@data-automation-tag="interface-settings-device-model"]',
            'wait_for': 5
        }

    wireless_wifi_device_template = \
        {
            'XPATH': '//span[@data-automation-tag="interface-settings-device-template"]',
            'wait_for': 5
        }

    wireless_wifi_radio_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableWifi2RadioStatus"]',
            'wait_for': 5
        }

    wireless_wifi2_radio_mode = \
        {
            'XPATH': '//label[@data-dojo-attach-point="radioMode6GHz"]',
            'wait_for': 5
        }

    wireless_wifi1_radio_mode = \
        {
            'XPATH': '//label[@data-dojo-attach-point="radioMode5GHz"]',
            'wait_for': 5
        }

    wireless_wifi0_radio_mode = \
        {
            'XPATH': '//label[@data-dojo-attach-point="radioMode2GHz,radioMode5DualGHz"]',
            'wait_for': 5
        }

    wireless_wifi2_default_radio_profile_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfileChange6"]/div/a/span',
            'wait_for': 5
        }

    wireless_wifi1_default_radio_profile_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfileChange5"]/div/a/span',
            'wait_for': 5
        }

    wireless_wifi0_default_radio_operating_mode_drop_down = \
        {
            'XPATH': '//*[@data-automation-tag="automation-interface-settings-operating-mode-chzn-container-ctn"]',
            'wait_for': 5
        }

    wireless_wifi0_default_radio_profile_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfileChange24"]',
            'wait_for': 5
        }

    wireless_wifi2_radio_usage_client_access_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi2-radio-usage-client-access"]',
            'wait_for': 5
        }

    wireless_wifi1_radio_usage_client_access_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi1-radio-usage-client-access"]',
            'wait_for': 5
        }

    wireless_wifi0_radio_usage_client_access_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi0-radio-usage-client-access"]',
            'wait_for': 5
        }

    wireless_wifi2_radio_usage_blackhaul_mesh_link_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi2-radio-usage-mesh-link"]',
            'wait_for': 5
        }

    wireless_wifi1_radio_usage_blackhaul_mesh_link_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi1-radio-usage-mesh-link"]',
            'wait_for': 5
        }

    wireless_wifi0_radio_usage_blackhaul_mesh_link_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi0-radio-usage-mesh-link"]',
            'wait_for': 5
        }

    wireless_wifi0_radio_usage_sensor_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi0-radio-usage-sensor"]',
            'wait_for': 5
        }

    wireless_wifi1_radio_usage_sensor_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi1-radio-usage-sensor"]',
            'wait_for': 5
        }

    wireless_wifi2_radio_usage_sensor_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi2-radio-usage-sensor"]',
            'wait_for': 5
        }

    wireless_wifi2_channel_dropdown = \
        {
            'XPATH': '//div[@class="grid_10 column"]/div[@data-automation-tag="automation-interface-settings-wifi1-radio-profile-chzn-container-ctn"]/a/span',
            'wait_for': 5
        }

    wireless_wifi1_channel_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="automation-interface-settings-wifi1-channel-chzn-container-ctn"]',
            'wait_for': 5
        }

    wireless_wifi0_channel_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="automation-interface-settings-wifi0-channel-chzn-container-ctn"]/a/span',
            'wait_for': 5
        }

    wireless_wifi2_channel_width_text = \
        {
            'XPATH': '//span[@data-dojo-attach-point="channelWidthLabel6g"]',
            'wait_for': 5
        }

    wireless_wifi1_channel_width_text = \
        {
            'XPATH': '//span[@data-dojo-attach-point="channelWidthLabel5g"]',
            'wait_for': 5
        }

    wireless_wifi0_channel_width_text = \
        {
            'XPATH': '//span[@data-dojo-attach-point="channelWidthLabel2g"]',
            'wait_for': 5
        }

    device_override_configure_interface_settings_wifi2_radio_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidTab"]//input[@data-dojo-attach-point="enableWifi2RadioStatus"]',
            'wait_for': 5
        }

    manage_devices_edit_wireless_interface_save_button2 = \
        {
            'XPATH': '//button[contains(text(),"Save Interface Settings")]',
            'wait_for': 5
        }

    wireless_wifi2_override_channel_exclusion_setting_radio_profile_label = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi2-exclude-channels"]/div/label/span',
            'wait_for': 5
        }

    wireless_wifi1_override_channel_exclusion_setting_radio_profile_label = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi1-exclude-channels"]/div/label/span',
            'wait_for': 5
        }

    wireless_wifi0_override_channel_exclusion_setting_radio_profile_label = \
        {
            'XPATH': '//div[@data-dojo-attach-point="excludeChannels2Area,excludeChannels5DualArea"]/div/label',
            'wait_for': 5
        }

    wireless_wifi0_override_channel_exclusion_setting_radio_profile_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="interface-settings-wifi0-exclude-channels"]',
            'wait_for': 5
        }

    # wireless_wifi0_override_channel_exclusion_setting_radio_profile_checkbox = \
    #     {
    #         'XPATH': '//div[@data-dojo-attach-point="excludeChannels2Area,excludeChannels5DualArea"]/div/label/input',
    #         'wait_for': 5
    #     }

    wireless_wifi1_override_channel_exclusion_setting_radio_profile_checkbox = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi1-exclude-channels"]/div/label/input',
            'wait_for': 5
        }

    wireless_wifi2_override_channel_exclusion_setting_radio_profile_checkbox = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi2-exclude-channels"]/div/label/input',
            'wait_for': 5
        }

    wireless_wifi2_icon = \
        {
            'XPATH': '//div[@class="ui-tipbox-ctn"]/div/div[@class="ui-tipbox-icon"]',
            'wait_for': 5
        }

    wireless_wifi2_radio_profile_list = \
        {
            'XPATH': '//li[@data-automation-tag="automation-interface-settings-wifi1-radio-profile-chzn-option-',
            'wait_for': 5
        }

    wireless_wifi1_radio_profile_list = \
        {
            'XPATH': '//li[@data-automation-tag="automation-interface-settings-wifi1-radio-profile-chzn-option-',
            'wait_for': 5
        }

    wireless_wifi0_radio_profile_list = \
        {
            'XPATH': '//li[@data-automation-tag="automation-interface-settings-wifi0-radio-profile-chzn-option-',
            'wait_for': 5
        }

    dialog_box_selected_radio_profile_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    dialog_box_selected_radio_profile_no_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="noBtn"]',
            'wait_for': 5
        }

    interface_settings_wifi2_80MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi2-channel-picker-header-80mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi2_40MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi2-channel-picker-header-40mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi2_160MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi2-channel-picker-header-160mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi2_20MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi2-channel-picker-header-20mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi1_80MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi1-channel-picker-header-80mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi1_40MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi1-channel-picker-header-40mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi1_160MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi1-channel-picker-header-160mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi1_20MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi1-channel-picker-header-20mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi0_80MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi0-channel-picker-header-80mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi0_40MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi0-channel-picker-header-40mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi0_160MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi0-channel-picker-header-160mhz"]',
            'wait_for': 5
        }

    interface_settings_wifi0_20MHz_channel = \
        {
            'XPATH': '//div[@data-automation-prefix="interface-settings-wifi0-channel-picker-header-20mhz"]',
            'wait_for': 5
        }

    devices_override_channel_exclusion_setting_wifi2 = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi2-channel-picker-channel-',
            'wait_for': 5
        }

    devices_override_channel_exclusion_setting_wifi1 = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi1-channel-picker-channel-',
            'wait_for': 5
        }

    devices_override_channel_exclusion_setting_wifi0 = \
        {
            'XPATH': '//div[@data-automation-tag="interface-settings-wifi0-channel-picker-channel-',
            'wait_for': 5
        }

    wired_interface_toggle = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wiredToggle"]',
            'wait_for': 5
        }

    imago_tag_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableImagotag"]',
            'wait_for': 5
        }

    imago_tag_add_profile_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imagotagAdd"]',
            'wait_for': 5
        }
    wired_client_connection_type = \
        {
            'XPATH': '//td',
            'wait_for': 5
        }

    wired_client_os_type = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-0 field-connectionType w70"]',
            'wait_for': 5
        }

    wired_client_connection_status = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-1 field-osType w80 fn-ellipsis"]',
            'wait_for': 5
        }

    wired_client_hostname = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-4 field-hostName w100 fn-ellipsis"]',
            'wait_for': 5
        }

    wired_client_mac = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-3 field-clientMac w110 fn-ellipsis"]',
            'wait_for': 5
        }

    wired_client_IPv4 = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-6 field-ipAddress w100"]',
            'wait_for': 5
        }

    wired_client_IPv6 = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-7 field-ipv6Address w300"]',
            'wait_for': 5
        }

    wired_client_user_name = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-8 field-userName w75 fn-ellipsis"]',
            'wait_for': 5
        }

    wired_client_vlan = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-9 field-vlan w100"]',
            'wait_for': 5
        }

    wired_client_connected_via = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-5 field-port w110 fn-ellipsis"]',
            'wait_for': 5
        }
    wired_client_popup_mac = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMac"]',
            'wait_for': 5
        }
    wired_client_popup_ipv4 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="switchIp"]',
            'wait_for': 5
        }
    wired_client_popup_portSpeed = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portSpeed"]',
            'wait_for': 5
        }
    wired_client_popup_negotiatedspeed = \
        {
            'XPATH': '//*[@data-dojo-attach-point="negotiatedSpeed"]',
            'wait_for': 5
        }
    wired_client_popup_portMode = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portMode"]',
            'wait_for': 5
        }
    wired_client_popup_vlan = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlan"]',
            'wait_for': 5
        }
    wired_client_popup_portNumber = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portNumber"]',
            'wait_for': 5
        }
    wired_client_popup_confirmation = \
        {
            'XPATH': '//*[@data-dojo-attach-point=""]',
            'wait_for': 5
        }

    close_D360_popup = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    config_audit_delta_view_button = \
        {
            'XPATH': '//span[@title="Configuration Audit"]',
            'wait_for': 5
        }

    devices_config_audit_view_button = \
        {
            'XPATH': '//span[@title="Configuration Audit"]',
            'wait_for': 5
        }

    devices_config_audit_mismatch = \
        {
            'CSS_SELECTOR': '.ui-icon-sprite-mismatch',
            'index': 0,
            'wait_for': 5
        }

    devices_config_audit_match = \
        {
            'CSS_SELECTOR': '.ui-icon-sprite-match',
            'index': 0,
            'wait_for': 5
        }

    devices_page_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]//td/..',
            'wait_for': 10
        }

    devices_device_config_device_function_set_ap = \
        {
            'XPATH': '//a[@href="javascript:void(0)"] //span[contains(text(),"AP")]',
            'wait_for': 5
        }

    devices_device_config_device_function_set_router = \
        {
            'XPATH': '//a[@href="javascript:void(0)"] //span[contains(text(), "ApAsRouter")]',
            'wait_for': 5
        }

    devices_device_config_device_function = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-devicefunction .active-result',
            'wait_for': 5
        }

    devices_device_config_page_save_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-deviceconfiguration-save-btn"]',
            'wait_for': 5
        }

    config_audit_content = \
        {
            'XPATH': "//div[@data-dojo-attach-point='auditCtn']"
        }

    config_audit_delta_view_button_yellow = \
        {
            'CSS_SELECTOR': '.ui-icon-sprite-mismatch'
        }

    stack_edit_template_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="stackTemplateArea"]//div['
                     '@data-automation-tag="automation-chzn-container-ctn"]/a',
            'wait_for': 5
        }

    device_edit_template_drop_down_options_stack = \
        {
            'XPATH': '//div[@data-automation-tag="automation-chzn-drop-ctn"]//ul[contains(@class, "chzn-results '
                     'qa-chzn-results-stacktemplatelist")]//li',
        }

    devices_config_wired_eth0 = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enabled"]',
            'index': 0,
            'wait_for': 5
        }

    devices_config_wired_eth1 = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enabled"]',
            'index': 1,
            'wait_for': 5
        }

    devices_config_wired_eth0_lldp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lldpRec"]',
            'index': 0,
            'wait_for': 5
        }

    devices_config_wired_eth1_lldp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lldpRec"]',
            'index': 1,
            'wait_for': 5
        }

    devices_config_wired_eth0_cdp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cdpReceive"]',
            'index': 0,
            'wait_for': 5
        }

    devices_config_wired_eth1_cdp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cdpReceive"]',
            'index': 1,
            'wait_for': 5
        }