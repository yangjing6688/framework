class NavigatorWebElementDefinitions:
    configure_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-configure"]',
            'wait_for': 2
            }

    configure_network_policy_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-policy"]',
            'wait_for': 2
        }

    manage_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-manage"]',
            'wait_for': 2
        }

    ml_insight_tab = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-n360"]',
            'wait_for': 2
        }

    manage_devices_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-manage"]',
            'wait_for': 2
        }

    manage_device_menu_item_href = \
        {
            'TAG_NAME' : 'a'
        }

    manage_clients_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-nav-clients']",
            'wait_for': 5
        }

    manage_clients_menu_item_href = \
        {
            'TAG_NAME' : 'a'
        }

    manage_devices_menu_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-nav-devices']",
            'wait_for': 5
        }

    manage_devices_menu_item_href = \
        {
            'TAG_NAME' : 'a'
        }

    configure_users_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-configure-users"]',
            'wait_for': 5
        }

    user_management_dropdown_toggle = \
        {
            'XPATH': '//div//span[@data-dojo-attach-point="dropdownToggle"]',
            'wait_for': 5
        }

    configure_users_user_management_side_menu = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-label-User-Management"]',
            'wait_for': 5
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

    dashboard  = \
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
            'TAG_NAME' : 'a'
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
            'wait_for': 10
        }

    tool_utility_nav = \
        {
            'XPATH': '//td[@data-automation-tag="automation-tools-controller-troubleshoot-utilities-link"]/ul/li/a',
            'wait_for': 10
        }

    global_header_nav = \
        {
            'XPATH': '//div[@data-dojo-attach-point="headerUserIcon"]',
            'wait_for': 10
        }

    global_header_communication_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-account-menu-communications-link"]',
            'wait_for': 10
        }

    manage_reports_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-reports"]/a',
            'wait_for': 10
        }

    manage_alarms_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-alarms"]//a',
            'wait_for': 10
        }

    manage_security_nav = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-security"]//a',
            'wait_for': 10
        }

    policy_toggle = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-label-Policy"]',
            'wait_for': 10
        }

    policy_toggle_right_arrow = \
        {
            'CSS_SELECTOR': 'ui-chevron-big.dropdown-chevron.right.active.pilot-active-bot',
            'wait_for': 10
        }

    auto_provisioning_option = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-autoProvision"]',
            'wait_for': 10
        }

    device_nav = \
        {
            #'XPATH': '//*[@data-automation-tag="automation-header-nav-devices"]//a',
            'XPATH': ' //*[@data-automation-tag="automation-header-nav-devices"]',
            'wait_for': 10
        }

    common_objects_ssids = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ssidManage"]',
            'wait_for': 10
        }

    manage_clients_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-clients"]',
            'wait_for': 10
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
            'XPATH': '//div//a[@data-automation-tag=automation-sider-list-ADServers]',
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
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ApTemplate"]',
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

    common_object_basic_vlans = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-VLANs"]',
            'wait_for': 5
        }

    ml_insight_client360 = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-clientsoverview"]',
            'wait_for': 5
        }

    ml_insight_network360plan = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-plan"]',
            'wait_for': 5
        }

    ml_insight_network360monitor = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-nav-tracker"]',
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
            'XPATH': "//*[@data-automation-tag='automation-manage-device-actions-ap-cli-access']//a",
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
            'wait_for': 10
        }

    card_view = \
        {
            'XPATH': "//*[@data-automation-tag='automation-config-card']",
            'wait_for': 10
        }

    network_policy_page_size = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 3
        }

    device_actions_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-actions-actions_normal-btn"]',
            'wait_for': 10
        }

    device_utilities_status = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Status")]',
            'wait_for': 5
        }

    utilities_status_interface = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Interface")]',
            'wait_for': 5
        }

    utilities_status_adv_channel_sel = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Advanced Channel Selection Protocol")]',
            'wait_for': 5
        }

    device_utilities = \
        {
            'XPATH': '//*[contains(@class, "btn btn-secondary-text") and contains(text(), "Utilities")]',
            'wait_for': 5
        }

    utilities_status_wifi_status_summary = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Wi-Fi Status Summary")]',
            'wait_for': 5
        }

    common_objects_switch_templates = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-switchTemplate"]',
            'wait_for': 10
        }

    api_token_mgmt_tab = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-xapiTokenMng"]',
            'wait_for': 10
        }

    a3_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-a3"]',
            'wait_for': 2
        }

    a3_inventory_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-a3-inventory"]',
            'wait_for': 2
        }

    manage_events_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-events"]',
            'wait_for': 5
        }

    air_defence_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-airdefense"]',
            'wait_for': 2
        }

    onboard_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-onboard"]',
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
            'XPATH': '//*[@data-automation-tag="automation-header-defender"]',
            'wait_for': 5
        }

    extreme_guest = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-guestEssentials"]',
            'wait_for': 5
        }

    extreme_location = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-locationEssentials"]',
            'wait_for': 5
        }

    subscribe_button = \
        {
            'XPATH': '//span[contains(text(), "Subscribe")]',
            'wait_for': 5
        }

    extreme_IOT_dashboard = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-defender-dashboard"]',
            'wait_for': 5
        }

    extreme_IOT_devices = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-defender-devices"]',
            'wait_for': 5
        }

    extreme_IOT_clients = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-defender-clients"]',
            'wait_for': 5
        }

    extreme_IOT_user_profiles = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-defender-userProfile"]',
            'wait_for': 5
        }

    extreme_IOT_policy_groups = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-defender-groups"]',
            'wait_for': 5
        }

    communications_notification_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-notifications"]',
            'wait_for': 10
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
            'wait_for': 10
        }

    common_objects_classification = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ClassificationRules"]',
            'wait_for': 10
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
            'XPATH': '//*[@id="hcApp/navigation/sideNav/SideNavView_0"]/div[3]/div[1]/div[2]/div[9]/a',
            'wait_for': 10
        }
    
    subtab_common_object = \
        {
            'CSS_SELECTOR': '.subSubTab-option.Policy',
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
    