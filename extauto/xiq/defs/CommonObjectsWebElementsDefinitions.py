class CommonObjectsWebElementsDefinitions:
    common_object_policy_slider_button = \
        {
            'CLASS_NAME': 'qa-sider-title-policy',
            'wait_for': 5
        }

    common_object_policy_manage_ssid = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ssidManage"]',
            'wait_for': 5
        }

    authentication_external_radius_server_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-extServers"]',
            'wait_for': 5
        }

    basic_slider_button = \
        {
            'CSS_SELECTOR': '.ui-nav-sider-title.qa-sider-title-basic',
            'wait_for': 5
        }

    ip_object_host_name_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ipObjectManage"]',
            'wait_for': 5
        }

    common_object_authentication_slider_button = \
        {
            'CLASS_NAME': 'qa-sider-title-authentication',
            'wait_for': 5
        }

    common_object_authentication_captive_portal = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-cwp"]',
            'wait_for': 3
        }

    common_object_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 10
        }

    common_object_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 2
        }

    common_object_edit_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-edit',
            'wait_for': 2
        }

    common_object_delete_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-remove',
            'wait_for': 2
        }

    common_object_confirm_delete_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 2
        }

    cwp_self_reg_employee_approval_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="approval"]',
            'wait_for': 3
        }

    cwp_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    page_size_element = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 2
        }

    next_page_element = \
        {
            'CSS_SELECTOR': '.J-page-next.ui-page-item-next',
            'wait_for': 2
        }

    common_object_authentication_aaa_server_settings = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-aaaServerSettings"]',
            'wait_for': 3
        }

    common_object_policy_manage_port_types = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-PortTypes"]',
            'wait_for': 5
        }

    common_object_policy_port_types_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="100"]',
            'wait_for': 3
        }

    common_object_network_subnetwork_space_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-subnetworkSpace"]',
            'wait_for': 5
        }

    common_object_network_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-titleNetwork"]',
            'wait_for': 5
        }

    common_object_basic_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-titleBasic"]',
            'wait_for': 5
        }

    common_object_basic_vlan_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-VLANs"]',
            'wait_for': 5
        }

    common_object_security_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-titleSecurity"]',
            'wait_for': 5
        }

    common_object_security_wips_policies_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-wipsPolicies"]',
            'wait_for': 5
        }

    common_object_policy_ap_template_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ApTemplate"]',
            'wait_for': 5
        }

    common_object_policy_ap_templates_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="100"]',
            'wait_for': 3
        }

    common_object_policy_add_ssid_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-ssidmanage-ssid-grid"]'
                     '//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    common_object_policy_clone_ssid_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-ssidmanage-ssid-grid"]'
                     '//span[@class="table-action-icons table-clone"]',
            'wait_for': 5
        }

    common_object_policy_clone_ssid_saveas_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="name"]',
            'wait_for': 3
        }

    common_object_policy_ssid_clone_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    common_object_radio_profile_add_button = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/CommonObject_1"]'
                     '//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    common_object_radio_profile_name = \
        {
            'XPATH': '//*[@id="name"]',
            'wait_for': 3
        }

    common_object_radio_profile_mode = \
        {
            'XPATH': '//*[@id="ah_util_Chosen_10_chzn"]',
            'wait_for': 3
        }

    common_object_radio_profile_select_mode = \
        {
            'XPATH': '//div[@data-automation-tag="chzn-drop-ctn"]'
                     '//ul[@data-automation-tag="chzn-results-ctn"]//li',
            'wait_for': 3
        }
    common_object_add_ap_template_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="accesspointListArea"]//span[@data-tip="Add"]',
            'wait_for': 3
        }

    common_object_matched_ap_model_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="accesspointListArea"]//li[contains(@class,"ui-menu-item")]',
            'wait_for': 3
        }

    common_object_add_ap_template_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="tplName"]',
            'wait_for': 3
        }

    common_object_ap_template_wifi_tab = \
        {
            'CSS_SELECTOR': '.ui-tab',
            'wait_for': 5
        }

    common_object_wifi0_radio_status_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableWifi0RadioStatus"]',
            'wait_for': 3
        }

    common_object_wifi1_radio_status_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableWifi1RadioStatus"]',
            'wait_for': 3
        }

    common_object_wifi2_radio_status_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableWifi2RadioStatus"]',
            'wait_for': 3
        }

    common_object_wifi0_radio_profile_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfile2g"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 3
        }

    common_object_wifi1_radio_profile_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="radioProfile5g"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 3
        }

    common_object_wifi0_radio_profile_dropdown = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-wirelessporttype2ghz,wirelessporttype5dualghz"]//li',
            'wait_for': 3
        }

    common_object_wifi1_radio_profile_dropdown = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-wirelessporttype5ghz"]//li',
            'wait_for': 3
        }

    common_object_wifi0_client_mode = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage2GHzClientMode"]',
            'wait_for': 3
        }

    common_object_wifi0_add_client_mode_profile = \
        {
            'XPATH': '//span[@data-dojo-attach-point="addClientModeProfileLink2GHz"]',
            'wait_for': 3
        }

    common_object_wifi1_add_client_mode_profile = \
        {
            'XPATH': '//span[@data-dojo-attach-point="addClientModeProfileLink5GHz"]',
            'wait_for': 3
        }

    common_object_wifi0_1_client_mode_profile_name = \
        {
            'XPATH': '//div[@data-dojo-attach-point="nameArea"]//input[@data-dojo-attach-point="name"]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_checkbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableLocalWeb"]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_add = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ssidListWrap"]//span[@data-tip="Add"]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_ssid_textbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ssid"]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_password_textbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="password"]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_auth_dropdown = \
        {
            'DESC': 'Auth Method click to dropdown',
            'XPATH': '//input[@data-dojo-attach-point="ssid"]//following::div[@data-automation-tag="automation-chzn-arrow-down"][1]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_auth_dropdown_option = \
        {
            'DESC': 'Auth Method Pre-Shared key/Open',
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-securitytype"]/li',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_key_type_dropdown = \
        {
            'DESC': 'Key Type click to dropdown',
            'XPATH': '//input[@data-dojo-attach-point="ssid"]//following::div[@data-automation-tag="automation-chzn-arrow-down"][2]',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_key_type_dropdown_option = \
        {
            'DESC': 'Key Type ASCII/HEX',
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-keytype"]/li',
            'wait_for': 3
        }

    common_object_wifi0_1_cm_local_web_page_add_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="addToSsid"]',
            'wait_for': 3
        }

    common_object_wifi0_1_client_mode_profile_dhcp_server_scope = \
        {
            'XPATH': '//input[@data-dojo-attach-point="dhcpServerScope"]',
            'wait_for': 3
        }

    common_object_wifi0_1_client_mode_profile_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 3
        }

    common_object_wifi0_client_access = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage2GHzClientAccess"]',
            'wait_for': 3
        }

    common_object_wifi0_mesh_link = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage2GHzMeshLink"]',
            'wait_for': 3
        }

    common_object_wifi0_sensor = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage2GHzSensor"]',
            'wait_for': 3
        }

    common_object_wifi1_client_mode = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage5GHzClientMode"]',
            'wait_for': 3
        }

    common_object_wifi1_client_access = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage5GHzClientAccess"]',
            'wait_for': 3
        }

    common_object_wifi1_mesh_link = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage5GHzMeshLink"]',
            'wait_for': 3
        }

    common_object_wifi1_sensor = \
        {
            'XPATH': '//input[@data-dojo-attach-point="radioUsage5GHzSensor"]',
            'wait_for': 3
        }

    common_object_ap_template_enable_sdr = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableSdrProfile"]',
            'wait_for': 3
        }

    common_object_ap_template_sdr_dropdown_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="sdrProfileContainer"]'
                     '//div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 3
        }

    common_object_ap_template_sdr_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="sdrProfileExtraFields"]'
                     '//ul[@data-automation-tag="chzn-results-ctn"]//li',
            'wait_for': 3
        }

    common_object_radio_profile_exclude_channels = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/RadioProfile_0"]/div[8]/div[3]/div[4]/div[1]/div[1]/div/input',
            'wait_for': 3
        }

    common_object_radio_profile_enable_dfs = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/RadioProfile_0"]/div[8]/div[4]/div[1]/div[1]/div/input',
            'wait_for': 3
        }

    common_object_radio_bg_scan = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/RadioProfile_0"]/div[8]/div[2]/div[2]/div[1]/div[1]/div/input',
            'wait_for': 3
        }

    common_object_radio_profile_save = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/RadioProfile_0"]/div[8]/div[12]/div/button[2]',
            'wait_for': 3
        }

    common_object_radio_exclude_ch_u_1 = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/ChannelSelect_0"]/div[2]/div/label/input',
            'wait_for': 3
        }

    common_object_radio_exclude_ch_u_2 = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/ChannelSelect_0"]/div[4]/div/label/input',
            'wait_for': 3
        }

    common_object_radio_exclude_ch_u_2e = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/ChannelSelect_0"]/div[6]/div/label/input',
            'wait_for': 3
        }

    common_object_radio_exclude_ch_u_3 = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/deviceTemplate/ChannelSelect_0"]/div[8]/div/label/input',
            'wait_for': 3
        }

    common_object_ap_template_disable_ssid = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableSdrProfile"]',
            'wait_for': 3
        }

    common_object_ap_template_lldp_eth0 = \
        {
            'XPATH': '//div[@id="ah/comp/configuration/deviceTemplate/APWiredInterfacesEntry_0"]'
                     '//input[@data-dojo-attach-point="lldpRec"]',
            'wait_for': 3
        }

    common_object_ap_template_lldp_eth1 = \
        {
            'XPATH': '//div[@id="ah/comp/configuration/deviceTemplate/APWiredInterfacesEntry_1"]'
                     '//input[@data-dojo-attach-point="lldpRec"]',
            'wait_for': 3
        }

    common_object_ap_template_cdp_eth0 = \
        {
            'XPATH': '//div[@id="ah/comp/configuration/deviceTemplate/APWiredInterfacesEntry_0"]'
                     '//input[@data-dojo-attach-point="cdpReceive"]',
            'wait_for': 3
        }

    common_object_ap_template_cdp_eth1 = \
        {
            'XPATH': '//div[@id="ah/comp/configuration/deviceTemplate/APWiredInterfacesEntry_1"]'
                     '//input[@data-dojo-attach-point="cdpReceive"]',
            'wait_for': 3
        }

    common_object_ap_template_eth0_status = \
        {
            'XPATH': '//div[@id="ah/comp/configuration/deviceTemplate/APWiredInterfacesEntry_0"]'
                     '//input[@data-dojo-attach-point="enabled"]',
            'wait_for': 3
        }

    common_object_ap_template_eth1_status = \
        {
            'XPATH': '//div[@id="ah/comp/configuration/deviceTemplate/APWiredInterfacesEntry_1"]'
                     '//input[@data-dojo-attach-point="enabled"]',
            'wait_for': 3
        }

    common_object_wifi2_primary_server_ip = \
        {
            'XPATH': '//input[@data-dojo-attach-point="airDefensePrimaryServerIP"]',
            'wait_for': 3
        }

    common_object_wifi2_primary_server_port = \
        {
            'XPATH': '//input[@data-dojo-attach-point="airDefensePrimaryPort"]',
            'wait_for': 3
        }

    common_object_ap_template_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCtn"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    common_object_radio_profile_select_pagination_max = \
        {
            'XPATH': '//*[@id="ah/comp/configuration/CommonObject_1"]'
                     '//*[@id="ah/util/form/Dgrid_0"]/div[4]/div[1]/a[4]',
            'wait_for': 3
        }

    common_object_imago_tag_profile_add_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-common-object-imagotagprofiles-imagoTag-ctn"]'
                     '//span[@class="table-action-icons table-add"]',
            'wait_for': 3
        }

    common_object_imago_tag_profile_name_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="imagoTagName"]',
            'wait_for': 3
        }

    common_object_imago_tag_profile_description_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imagoTagDesc"]',
            'wait_for': 3
        }

    common_object_imago_tag_profile_server_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imagoTagServer"]',
            'wait_for': 3
        }

    common_object_imago_tag_profile_channel_drop_down_button = \
        {
            'XPATH': '//*[@data-automation-tag="imago-tag-radio-mode-combo-chzn-container-ctn"]',
            'wait_for': 5
        }

    common_object_imago_tag_profile_channel_drop_down_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-imagotagchannelcombo")]//li[@class="active-result"]',
            'wait_for': 5
        }

    common_object_imago_tag_profile_fcc_mode_checkbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="imagoTagFccMode"]',
            'wait_for': 5
        }

    common_object_imago_tag_profile_advanced_settings_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imagoTagAdvToggle"]',
            'wait_for': 5
        }

    common_object_imago_tag_profile_advanced_settings_server_port = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imagoTagServerPort"]',
            'wait_for': 5
        }

    common_object_imago_tag_profile_save_button = \
        {
            'XPATH': '//*[@data-automation-tag="imago-tag-save-btn"]',
            'wait_for': 5
        }

    common_object_imago_tag_profile_save_tooltip_text = \
        {
            'XPATH': '//*[@class="ui-tipbox-con"]',
            'index': 2,
            'wait_for': 5
        }

    imago_tag_profile_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]',
            'wait_for': 10
         }

    imago_tag_profile_select_checkbox = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'wait_for':    2
        }

    imago_tag_profile_edit_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-edit',
            'wait_for': 5
        }

    common_object_ip_firewall_policy_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="additionalSettingsContentArea"]'
                     '//span[@class="table-action-icons table-add"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_name_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_description_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_add_rule_button = \
        {
            'XPATH': '//div[@componentpath="IPFirewallProfile"]//span[@class="table-action-icons table-add"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_add_rule_select_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceIp"]//*[@class="hmng-icon-select"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_add_rule_application_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="taber"]//*[contains(@class, "ui-tab ui-tab-updated")]',
            'index': 1,
            'wait_for': 3
        }

    common_object_ip_firewall_policy_add_rule_select_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceIp"]//*[@class="hmng-icon-select"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_add_rule_select_application_checkbox = \
        {
            'XPATH': '//*[@data-text=f"{app}"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_add_rule_select_application_rows = \
        {
            'XPATH': '//li[@class="filter-app-list-item"]',
            'wait_for': 10
         }

    firewall_policy_add_rule_select_application_check_box = \
        {
            'CSS_SELECTOR': '.checkbox',
            'wait_for':    2
        }

    common_object_ip_firewall_policy_select_application_save_button = \
        {
            'XPATH': '//div[@componentpath="IpFirewallRuleService"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_rule_action_dropdown_button = \
        {
            'XPATH': '//div[@componentpath="IPFirewallRule"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_rule_action_dropdown_options = \
        {
            'XPATH': '//div[@componentpath="IPFirewallRule"]'
                     '//ul[@data-automation-tag="automation-chzn-container-ctn"]//li',
            'wait_for': 3
        }

    common_object_ip_firewall_policy_save_button = \
        {
            'XPATH': '//div[@componentpath="IPFirewallRule"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    common_object_policy_user_profile_name_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="profileName"]',
            'wait_for': 3
        }

    common_object_policy_user_profiles_security_tab = \
        {
            'XPATH': '//div[@data-dojo-attach-point="userprofileTabs"]//*[contains(@class, "ui-tab ui-tab-updated")]',
            'wait_for': 3
        }

    common_object_user_profile_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="additionalSettingsContentArea"]'
                     '//span[@class="table-action-icons table-add"]',
            'wait_for': 3
        }

    common_object_user_profile_firewall_rules_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="firewallSwitch"]',
            'wait_for': 3
        }

    common_object_user_profile_select_ip_firewall_policy_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="firewallListContainer"]'
                     '//span[@class="table-action-icons table-select"]',
            'wait_for': 3
        }

    firewall_policy_select_dialog = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }

    firewall_policy_select_dialog_rows = \
        {
            'CLASS_NAME': 'dojoxGridRowTable',
            'wait_for': 1
        }

    firewall_policy_select_dialog_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-cancel',
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 1
        }

    firewall_policy_select_dialog_row_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector.dijitReset.dijitReset.dijitCheckBox',
            'wait_for': 1
        }

    firewall_policy_select_dialog_select_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 1
        }

    user_profile_save_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-user-profile-save-btn"]',
            'wait_for': 1
        }
