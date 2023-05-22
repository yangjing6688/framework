class NavigatorWebElementDefinitions:
    configure_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-configure"]'
        }

    configure_nav_img = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-configure"]//img',
            'wait_for': 2
        }

    subtab_head_img_nav = \
        {
            'CSS_SELECTOR': '.subTab-head.img-nav',
            'wait_for': 5
        }

    configure_network_policy_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-policy"]',
        }

    manage_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-manage"]',
            'wait_for': 2
        }

    manage_nav_img = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-manage"]//img',
            'wait_for': 2
        }

    ml_insight_tab = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-n360"]',
            'wait_for': 2
        }

    ml_insight_tab_img = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-n360"]//img',
            'wait_for': 2
        }

    manage_devices_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-manage"]',
            'wait_for': 2
        }

    manage_device_menu_item_href = \
        {
            'TAG_NAME': 'a'
        }

    manage_clients_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-nav-clients']",
            'wait_for': 5
        }

    manage_clients_menu_item_href = \
        {
            'TAG_NAME': 'a'
        }

    manage_devices_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-nav-devices']",
            'wait_for': 5
        }

    manage_devices_menu_item_href = \
        {
            'TAG_NAME': 'a'
        }

    configure_users_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-configure-users"]',
            'wait_for': 5
        }

    user_management_dropdown_toggle = \
        {
            'XPATH': '//div//span[@data-dojo-attach-point="dropdownToggle"]'
        }

    configure_users_user_management_side_menu = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-label-User-Management"]'
        }

    deutcshe_configure_users_user_management_side_menu = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-label-Benutzerverwaltung"]',
            'wait_for': 5
        }

    configure_user_group_side_nav_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-usergroups']",
            'wait_for': 5
        }

    deutcshe_configure_user_group_side_nav_item = \
        {
            'XPATH': '//a[contains(text(), "Benutzergruppen")]',
            'wait_for': 5,
            'index': 0
        }

    configure_common_objects_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-header-nav-common']",
            'wait_for': 5
        }

    user_account_nav = \
        {
            'XPATH': '//div[@data-dojo-attach-point="accountInfo"]',
            'wait_for': 5
        }

    global_settings = \
        {
            'XPATH': '//*[@data-automation-tag="automation-account-menu-account-link"]',
            'wait_for': 2
        }

    account_mgmt = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-accountMng"]',
            'wait_for': 2
        }

    license_mgmt = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-licenseMng']",
            'wait_for': 5
        }

    manage_tools_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-header-nav-issue']",
            'wait_for': 5
        }

    global_settings_account_organizations_slider = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-orgManagement"]',
            'wait_for': 3
        }

    global_settings_account_details = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-accountDtl"]',
            'wait_for': 2
        }

    global_settings_webhooks = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-manageWebhooks"]',
            'wait_for': 2
        }

    dashboard = \
        {
            'XPATH': "//*[@data-dojo-attach-point='appLogo']",
            'wait_for': 5
        }

    dashboard_conn_status = \
        {
            'XPATH': "//*[@data-dojo-attach-point='connStatusText']",
            'wait_for': 5
        }

    credential_dist_group = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-credentialDistributionGroups']",
            'wait_for': 5
        }

    manage_tools_menu_item_href = \
        {
            'TAG_NAME': 'a'
        }

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

    create_report = \
        {
            'CSS_SELECTOR': '.dashboard-report-btn',
            'wait_for': 5
        }

    global_settings_authentication_logs_slider = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-authLogs"]',
            'wait_for': 3
        }

    global_settings_accounting_logs_slider = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-acctLogs"]',
            'wait_for': 3
        }
   
    manage_tool_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-issue"]/a',
            
        }

    tool_utility_nav = \
        {
            'XPATH': '//td[@data-automation-tag="automation-tools-controller-troubleshoot-utilities-link"]/ul/li/a',
            
        }

    global_header_nav = \
        {
            'XPATH': '//div[@data-dojo-attach-point="headerUserIcon"]',
            
        }

    global_header_communication_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-account-menu-communications-link"]',
            
        }

    manage_reports_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-reports"]/a',
            
        }

    manage_alarms_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-alerts"]//a',
            
        }

    manage_security_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-security"]//a',
            
        }

    policy_toggle = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Policy"]',
            
        }

    policy_toggle_right_arrow = \
        {
            'CSS_SELECTOR': 'ui-chevron-big.dropdown-chevron.right.active.pilot-active-bot',
            
        }

    auto_provisioning_option = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-autoProvision"]',
            
        }

    device_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-devices"]',
            
        }

    devices_page = \
        {
            'CSS_SELECTOR': '.device-list-area',
            'wait_for': 5
        }

    common_objects_ssids = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ssidManage"]',
            
        }

    manage_clients_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-clients"]',
            
        }

    common_object_authentication_tab = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-label-Authentication"]',
            'wait_for': 5
        }

    common_object_authentication_captive_portal = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-cwp"]',
            'wait_for': 3
        }

    common_object_authentication_aaa_server_settings = \
        {
            'XPATH': '//div//a[@data-automation-tag="automation-sider-list-aaaServerSettings"]',
            'wait_for': 3
        }

    common_object_authentication_ad_servers = \
        {
            'XPATH': '//div//a[@data-automation-tag="automation-sider-list-ADServers"]',
            'wait_for': 3
        }

    common_object_authentication_external_radius_server = \
        {
            'XPATH': '//div//a[@data-automation-tag="automation-sider-list-extServers"]',
            'wait_for': 3
        }

    common_object_authentication_extreme_networks_a3 = \
        {
            'XPATH': '//div//a[@data-automation-tag="aautomation-sider-list-ahA3Servers"]',
            'wait_for': 3
        }

    common_object_authentication_servers = \
        {
            'XPATH': '//div//a[@data-automation-tag="automation-sider-list-ahA3Servers"]',
            'wait_for': 3
        }

    common_object_authentication_ldap_servers = \
        {
            'XPATH': '//div//a[@data-automation-tag="automation-sider-list-LDAPServers"]',
            'wait_for': 3
        }

    common_object_security_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Security"]',
            'wait_for': 5
        }

    common_object_security_wips_policies = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-wipsPolicies"]',
            'wait_for': 5
        }

    common_object_policy_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Policy"]',
            'wait_for': 5
        }

    common_object_policy_ap_template = \
        {
            'XPATH': '//div[@data-automation-tag="automation-sider-list-ApTemplate"]',
            'wait_for': 5
        }

    common_object_policy_port_types = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-PortTypes"]',
            'wait_for': 5
        }

    common_object_network_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Network"]',
            'wait_for': 5
        }

    common_object_network_sub_network_space = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-subnetworkSpace"]',
            'wait_for': 5
        }

    common_object_basic_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Basic"]',
            'wait_for': 5
        }

    common_object_basic_client_mode_profiles = \
        {
            'XPATH': '//a[@data-automation-tag="automation-sider-list-clientModeProfile"]',
            'wait_for': 5
        }

    common_object_basic_vlans = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-VLANs"]',
            'wait_for': 5
        }

    common_object_basic_supplemental_cli = \
        {
            'XPATH': '//div[@data-automation-tag="automation-sider-list-supplementalCLIObjects"]',
            'wait_for': 5
        }

    ml_insight_client360 = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-clientsoverview"]',
            'wait_for': 5
        }

    ml_insight_network360plan = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-plan"]'
        }

    ml_insight_network360monitor = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-tracker"]',
            'wait_for': 5
        }

    ml_insight_networkScorecard = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-scorecard"]',
            'wait_for': 5
        }

    ml_insight_retail = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-retail"]',
            'wait_for': 5
        }

    device_actions_advanced = \
        {
            'XPATH': '//*[contains(@class, "ui-menu-item")]//a[contains(text(), "Advanced")]'
                     '//span[contains(@class, "ui-icon ui-icon-next")]',
            'wait_for': 5
        }

    device_actions_advanced_cli_access = \
        {
            'XPATH': "//a[@data-automation-tag='automation-manage-device-actions-ap-cli-access']",
            'wait_for': 5
        }

    device_actions_advanced_cli_router_access = \
        {
            'XPATH': "//*[@data-automation-tag='automation-manage-device-actions-router-cli-access']//a",
            'wait_for': 5
        }

    list_view = \
        {
            'XPATH': "//*[@data-automation-tag='automation-config-list']",
            
        }

    card_view = \
        {
            'XPATH': "//*[@data-automation-tag='automation-config-card']",
            'wait_for': 30
        }

    network_policy_page_size = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 3
        }

    device_actions_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-actions-button"]',
            
        }

    device_utilities_status = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-status"]',
            'wait_for': 5
        }

    utilities_status_interface = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-status-interface"]',
            'wait_for': 5
        }

    utilities_status_adv_channel_sel = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-status-advanced-channel-selection-protocol"]',
            'wait_for': 5
        }

    device_utilities = \
        {
            'XPATH': '//*[contains(@class, "btn btn-secondary-text") and contains(text(), "Utilities")]',
            'wait_for': 5
        }

    utilities_status_wifi_status_summary = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-status-wifi-status-summary"]',
            'wait_for': 5
        }

    common_objects_switch_templates = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-switchTemplate"]',
            
        }

    api_token_mgmt_tab = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-xapiTokenMng"]',
            
        }

    a3_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-a3"]',
            'wait_for': 2
        }

    a3_nav_img = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-a3"]//img',
            'wait_for': 2
        }

    a3_inventory_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-a3-inventory"]',
            'wait_for': 2
        }

    a3_reporting_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-a3-reporting"]',
            'wait_for': 2
        }

    manage_events_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-events"]',
            'wait_for': 5
        }

    manage_alerts_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-alerts"]',
            'wait_for': 5
        }

    air_defence_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-airdefense-essentials"]',
            'wait_for': 2
        }

    onboard_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ah-drawer-trigger"]',
            'wait_for': 2
        }

    common_objects_policy = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Policy"]',
            'wait_for': 5
        }

    common_objects_policy_user_profile = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-userProfile"]',
            'wait_for': 5
        }

    extreme_IOT_essentials = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-iot-essentials"]',
            'wait_for': 5
        }

    extreme_guest = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-guest-essentials"]',
            'wait_for': 5
        }

    essentials_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-essentials"]',
            'wait_for': 5
        }

    essentials_menu_img = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-essentials"]//img',
            'wait_for': 5
        }

    extreme_location = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-location-essentials"]',
            'wait_for': 5
        }

    subscribe_button = \
        {
            'XPATH': '//span[contains(text(), "Subscribe")]',
            'wait_for': 5
        }

    extreme_IOT_dashboard = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-iot-essentials-dashboard"]',
            'wait_for': 5
        }

    extreme_IOT_devices = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-iot-essentials-devices"]',
            'wait_for': 5
        }

    extreme_IOT_clients = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-iot-essentials-clients"]',
            'wait_for': 5
        }

    extreme_IOT_user_profiles = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-iot-essentials-userProfile"]',
            'wait_for': 5
        }

    extreme_IOT_policy_groups = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-iot-essentials-groups"]',
            'wait_for': 5
        }

    communications_notification_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-notifications"]',
            
        }

    extreme_IOT_subscribe_button = \
        {
            'XPATH': '//div[@class="defender-subscribe"]//span[@data-dojo-attach-point="containerNode"]',
            'wait_for': 5
        }

    extreme_guest_subscribe_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="preSubscribeCtn"]//*[@data-dojo-attach-point="containerNode"]',
            'wait_for': 5
        }

    extreme_location_subscribe_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="preSubscribeCtn"]//span[@data-dojo-attach-point="containerNode"]',
            'wait_for': 5
        }

    extreme_guest_monitor_tab = \
        {
            'ID': 'ext-element-8',
            'wait_for': 5
        }

    extreme_guest_configure_tab = \
        {
            'ID': 'ext-element-17',
            'wait_for': 5
        }

    extreme_guest_analyze_tab = \
        {
            'ID': 'ext-element-22',
            'wait_for': 5
        }

    extreme_guest_configure_settings_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 3
        }

    eguest_configure_authorization_policy_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 4
        }

    eguest_configure_access_groups_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 5
        }

    eguest_configure_deployment_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 6
        }

    eguest_configure_location_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 7
        }

    eguest_configure_network_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 8
        }

    eguest_configure_devices_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 9
        }

    eguest_configure_notification_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 10
        }

    eguest_configure_notification_policy_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 11
        }

    eguest_configure_onboarding_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 12
        }

    eguest_configure_onboarding_policy_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 13
        }

    eguest_configure_onboarding_rules_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 14
        }

    eguest_configure_splash_templates_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 15
        }

    eguest_configure_users_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 16
        }

    eguest_configure_clients_menu = \
        {
            'CSS_SELECTOR': '.x-tree-node-text',
            'wait_for': 3,
            'index': 17
        }

    extreme_location_dashboard_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.dashboardIconCls',
            'wait_for': 3
        }

    extreme_location_sites_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.siteMenuIconCls',
            'wait_for': 3
        }

    extreme_location_category_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.zoneIconCls',
            'wait_for': 3
        }

    extreme_location_access_points_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.apIconCls',
            'wait_for': 3
        }

    extreme_location_beacons_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.bleIconCls',
            'wait_for': 3
        }

    extreme_location_asset_management_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.assetIconCls',
            'wait_for': 3
        }

    extreme_location_asset_management_assets_menu = \
        {
            'XPATH': '//*[@class="x-grid-item x-grid-item-selected"]',
            'wait_for': 5
        }

    extreme_location_asset_management_alarms_menu = \
        {
            'XPATH': '//div[@id="AssetManagementNavigation-1544-body"]//span[@class="x-tree-node-text "]',
            'wait_for': 5,
            'index': 1
        }

    extreme_location_devices_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.wirelessDevicesIconCls',
            'wait_for': 3
        }

    extreme_location_devices_wireless_devices_menu = \
        {
            'XPATH': '//*[contains(@id, "DevicesNavigation")]//div[@class="x-grid-cell-inner x-grid-cell-inner-treecolumn"]',
            'index': 1,
            'wait_for': 5
        }

    extreme_location_devices_bss_devices_menu = \
        {
            'XPATH': '//*[contains(@id, "DevicesNavigation")]//div[@class="x-grid-cell-inner x-grid-cell-inner-treecolumn"]',
            'index': 2,
            'wait_for': 5
        }

    extreme_location_settings_menu = \
        {
            'CSS_SELECTOR': '.x-treelist-item-tool.settingIconCls',
            'wait_for': 3
        }

    extreme_location_settings_device_classification_menu = \
        {
            'XPATH': '//span[contains(text(),"Device Classification")]',
            'wait_for': 5
        }

    extreme_location_settings_threshold_menu = \
        {
            'XPATH': '//div[@id="SettingsNavigation-1730-body"]//span[@class="x-tree-node-text "]',
            'wait_for': 5,
            'index': 1
        }

    extreme_location_settings_third_party_config_menu = \
        {
            'CSS_SELECTOR': '.x-grid-cell-treecolumn',
            'index': 2,
            'wait_for': 5
        }

    extreme_location_settings_alarms_menu = \
        {
            'XPATH': '//div[@id="SettingsNavigation-1730-body"]//span[@class="x-tree-node-text "]',
            'wait_for': 5,
            'index': 3
        }

    common_objects_ccgs = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-CloudConfigGroups"]',
            
        }

    common_objects_classification = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ClassificationRules"]',
            
        }

    configure_ppsk_classification_side_nav_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-ppskgroup']",
            'wait_for': 5
        }

    viq_management_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-backupRestore"]',
            'wait_for': 3
        }

    manage_applications_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-apps"]',
            'wait_for': 5
        }

    common_objects_radio_profile = \
        {
            'XPATH': '//div[@data-automation-tag="automation-sider-list-RadioProfiles"]',
            
        }
    
    subtab_common_object = \
        {
            'CSS_SELECTOR': '.subSubTab-option.Policy',
            'wait_for': 3
        }

    subtab_common_object_basic = \
        {
            'CSS_SELECTOR': '.subSubTab-option.Basic',
            'wait_for': 3
        }

    global_settings_audit_logs_slider = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-auditLogs"]',
            'wait_for': 3
        }

    copilot_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-copilotdash"]',
            'index': 0,
            'wait_for': 5
        }

    copilot_tab_img = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-copilotdash"]//img',
            'index': 0,
            'wait_for': 5
        }

    copilot_anomaly_notification_icon = \
        {
            'XPATH': '//div[@data-dojo-attach-point="headerAnomalyIcon"]',
            'wait_for': 5
        }

    configure_users_subtab_users_side_nav_item = \
        {
            'XPATH': '//a[@data-automation-tag="automation-sider-list-users"]',
            'wait_for': 5
        }

    common_object_policy_imago_tag_profile = \
        {
            'XPATH': '//*[@data-automation-tag="automation-slider-list-imagoTagProfiles"]',
            'wait_for': 5
        }

    common_object_security_ip_firewall_policies = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ipFirewallPolicies"]',
            'wait_for': 5
        }

    common_object_policy_user_profiles = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-userProfile"]',
            'wait_for': 5
        }
    
    navigate_to_device_management_settings_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-deviceMng"]',
            'wait_for': 5
        }

    common_object_network_management_options = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ManagementOptions"]',
            'wait_for': 5
        }

    utilities_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-button"]',
            'wait_for': 2
        }

    tools_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools"]',
            'wait_for': 2
        }

    tools_client_information_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools-client-information"]',
            'wait_for': 2
        }

    tools_get_tech_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools-get-tech-data"]',
            'wait_for': 2
        }

    tools_locate_device_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools-locate-device"]',
            'wait_for': 2
        }

    tools_layer_neighbor_info_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools-layer-neighbor-info"]',
            'wait_for': 2
        }

    tools_packet_capture_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools-packet-capture"]',
            'wait_for': 2
        }

    tools_vlan_probe_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-tools-vlan-probe"]',
            'wait_for': 2
        }

    diagnostics_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics"]',
            'wait_for': 2
        }

    diagnostics_show_ping_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ping"]',
            'wait_for': 2
        }

    diagnostics_show_log_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-log"]',
            'wait_for': 2
        }

    diagnostics_show_mac_table_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-mac-table"]',
            'wait_for': 2
        }

    diagnostics_show_version_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-version"]',
            'wait_for': 2
        }

    diagnostics_show_running_config_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-running-config"]',
            'wait_for': 2
        }

    diagnostics_show_startup_config_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-startup-config"]',
            'wait_for': 2
        }

    diagnostics_show_ip_routes_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ip-routes"]',
            'wait_for': 2
        }

    diagnostics_show_mac_routes_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-mac-routes"]',
            'wait_for': 2
        }

    diagnostics_show_arp_cache_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-arp-cache"]',
            'wait_for': 2
        }

    diagnostics_show_roaming_cache_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-roaming-cache"]',
            'wait_for': 2
        }

    diagnostics_show_dnxp_neighbors_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-dnxp-neighbors"]',
            'wait_for': 2
        }

    diagnostics_show_dnxp_cache_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-dnxp-cache"]',
            'wait_for': 2
        }

    diagnostics_show_amrp_tunnel_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-amrp-tunnel"]',
            'wait_for': 2
        }

    diagnostics_show_gre_tunnel_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-gre-tunnel"]',
            'wait_for': 2
        }

    diagnostics_show_ike_event_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ike-event"]',
            'wait_for': 2
        }

    diagnostics_show_ike_sa_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ike-sa"]',
            'wait_for': 2
        }

    diagnostics_show_ipsec_sa_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ipsec-sa"]',
            'wait_for': 2
        }

    diagnostics_show_ipsec_tunnel_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ipsec-tunnel"]',
            'wait_for': 2
        }

    diagnostics_show_vpn_tunnel_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-vpn-tunnel"]',
            'wait_for': 2
        }

    diagnostics_show_cpu_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-cpu"]',
            'wait_for': 2
        }

    diagnostics_show_memory_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-memory"]',
            'wait_for': 2
        }

    diagnostics_show_pse_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-pse"]',
            'wait_for': 2
        }

    locked_users_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-lockedusers"]',
            'wait_for': 5
        }

    unbind_device_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-unbinddevice"]'
        }

    client_monitor_diagnosis_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-clientmonitor-Diagnosis"]',
            'wait_for': 5
        }

    configure_alert_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-alert"]',
            'wait_for': 2
        }

    applications_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-apps"]',
            'wait_for': 5
        }

    main_side_nav_tabs = \
        {
            'XPATH': '//div[@data-dojo-attach-point="headerMenu"]//div',
            'wait_for': 5
        }

    side_nav_panel_1_menu_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="panel1"]/div[@class="panel-container"]//div[contains(@class, "subTab-option")]',
            'wait_for': 5
        }

    side_nav_panel_2_menu_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="panel2"]/div[@class="panel-container"]//div[contains(@class, "subTab-option")]',
            'wait_for': 5
        }

    manage_summary_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-summary"]',
            'wait_for': 5
        }

    manage_users_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-manage-clients"]',
            'wait_for': 5
        }

    configure_guest_essentials_users_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-configure-guest-essentials-users"]',
            'wait_for': 5
        }

    spectrum_intelligence_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-spectrum-intelligence"]',
            'wait_for': 5
        }

    reset_device_to_default_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-reset-device-to-default"]',
            'wait_for': 5
        }

    vpn_management_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-vpnMgmt"]',
            'wait_for': 5
        }

    vpn_services_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-vpnServices"]',
            'wait_for': 5
        }

    clients_hyperlink = \
        {
            'XPATH': '//*[@data-automation-tag="automation-dashboard-health-cards-client-header-count"]',
            'wait_for': 5
        }

    nw_policy_port_types_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="100"]',
            'wait_for': 3
        }

    table_load_spinner = \
        {
            'DESC': 'Manage > Devices "load" mask',
            # The spinner does not have its own automation-tag and there is more than one "grid-mark" on the
            # page.  So we'll get the nearest container that has an automation tag then find the element within
            # that container that has the 'grid-mark' CSS style.
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]//div[@class="grid-mark"]',
            'wait_for': 5
        }

    configure_button_d360 = \
        {
            'XPATH': '//li[@data-automation-tag="device-entity-configure"]'
        }

    port_configuration_d360 = \
        {
            'XPATH': '//li[@data-automation-tag="device-entity-nav-menu-port-configuration"]'
        }

    port_rows_d360 = \
        {
            'CSS_SELECTOR': '.port-details-entry'
        }

    page_size = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 5
        }
        
    no_100_devices_per_page = \
        {
        "XPATH": '//a[@data-size="100"]'
        }

    unknown_tooltip_error = {
        'XPATH': '//*[contains(@class,"ui-tipbox-error")]'
    }

    unknown_error_tooltip_close_icon = {
        'XPATH': '//*[contains(@class,"ui-tipbox-close")]'
    }

    grid_loading_wheel = \
        {
            'XPATH': '//div[@class="grid-mark"]',
            'wait_for': 5
        }

    grid_spinner = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spinner"]',
            'wait_for': 5
        }

    tools_page = \
        {
            'CSS_SELECTOR': '.tools-controller',
            'wait_for': 5
        }

    grid_loading_mark = \
        {
            'XPATH': '//div[@data-dojo-attach-point="loadingMark"]',
            'wait_for': 5
        }
