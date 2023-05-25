
class NetworkPolicyWebElementDefinition:
    list_view = \
        {
            'XPATH': "//*[@data-automation-tag='automation-config-list']",
            'wait_for': 5
        }

    card_view = \
        {
            'XPATH': "//span[@data-automation-tag='automation-config-card']",
            'wait_for': 30
        }

    np_grid_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-network-policies-grid"]'
                     '//table[@class="dgrid-row-table"]//tr',
            
        }
    np_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    np_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-network-policies-grid"]//span[@data-tip="Delete"]',
            'wait_for': 2
         }

    np_delete_confirm_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 3
         }

    np_add_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-network-policies-grid"]//span[@data-tip="Add"]'
        }

    np_policy_crumb_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='backPolicyList']",
            'wait_for': 5
        }

    np_edit_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-network-policies-grid"]//span[@data-tip="Edit"]',
            'CSS_SELECTOR': '.table-action-icons.table-edit'
        }

    np_wireless_check_box = \
        {
            'XPATH': '//input[@data-automation-tag="automation-policy-wireless"]',
            'wait_for':    3
        }

    policy_name_text = \
        {
            'XPATH': "//*[@data-automation-tag='automation-policy-name']",
            'wait_for': 5
        }

    policy_save_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-policy-save']",
            'wait_for': 5
        }
    np_save_tool_tip = \
        {
            'XPATH': '//*[contains(@class, "ui-tipbox-success")]//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }

    policy_exit_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-tab-wireless-exit']",
            'wait_for': 5
        }

    network_policy_card_title = \
        {
            'CSS_SELECTOR': 'card-item-title',
            'wait_for': 5
        }

    network_policy_card_item_edit_icon = \
        {
            'CSS_SELECTOR': '.card-item-action-edit'
        }

    network_policy_wireless_networks_tab = \
        {
            'XPATH': "//*[@data-automation-tag='automation-tab-wireless-networks']",
            'wait_for': 5
        }

    network_policy_wireless_networks_grid = \
        {
            'XPATH': "//*[@data-automation-tag='automation-wireless-networks-grid']",
            'wait_for': 5
        }

    netwrok_policy_wireless_networks_grid_rows = \
        {
            'CSS_SELECTOR':'.dgrid-row',
            'wait_for': 5
        }

    netwrok_policy_wireless_networks_grid_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 5
        }

    netwrok_policy_wireless_networks_grid_ssid_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 2
        }

    network_policy_wireless_ssid_name_textfield = \
        {
            'XPATH': "//*[@data-automation-tag='automation-ssid-details-ssid-name']"
        }

    network_policy_wireless_networks_save_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 5
        }

    network_policy_card_item = {'CSS_SELECTOR': '.card-item-static'}

    deploy_policy_tab = \
        {
            'XPATH': "//*[@data-automation-tag='automation-tab-deploy-policy']",
            'wait_for': 5
        }

    eligible_device_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='showEligible']",
            'wait_for': 5
        }

    device_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 2
        }

    device_grid_row_table = {'CSS_SELECTOR': '.dgrid-row-table', 'wait_for': 5}

    device_select_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'wait_for':    2
        }

    deploy_policy_upload_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='upload']",
            'wait_for': 5
        }

    perform_update_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadBtn"]',
            'wait_for': 2
        }

    network_policy_cards = \
        {
            'XPATH': "//*[@data-automation-tag='automation-policy-card']",
            'wait_for': 5
        }

    network_policy_card_ssids = \
        {
            'CSS_SELECTOR': ".card-ssid-list",
            'wait_for': 1
        }

    network_policy_name_from_card_view = \
        {
            'XPATH': "//*[@data-automation-tag='automation-policy-card-title']",
            'wait_for': 5
        }

    np_title = \
        {
            'CSS_SELECTOR': ".title",
            'wait_for': 1
        }

    network_policy_page_size = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 3
        }

    back_to_network_policy_list= \
        {
            'CSS_SELECTOR': '.ui-crumb-item',
            'wait_for': 5
        }

    configure_to_network_policy_panel= \
        {
            'XPATH': "//*[@data-dojo-attach-point='panel1']",
            'wait_for': 5
        }

    enable_presence_analytics_btn = \
        {
            'XPATH': '//input[@data-dojo-attach-point="presenceSwitch"]',
            'wait_for': 5
        }

    network_policy_additional_settings_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="additionalSettingsPage"]',
            'wait_for': 2
        }

    additional_settings_ibeacon_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-beacon"]',
            'wait_for': 2
        }

    ibeacon_status_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableBeacon"]',
            'wait_for': 2
        }

    ibeacon_service_name_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceName"]',
            'wait_for': 2
        }

    ibeacon_description_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="desc"]',
            'wait_for': 2
        }

    ibeacon_uuid_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uuid"]',
            'wait_for': 2
        }

    ibeacon_monitoring_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="monitoringCheck"]',
            'wait_for': 2
        }

    ibeacon_services_save_button = \
        {
            'XPATH': '//*[@class="beacon-ctn"]//*[@data-dojo-attach-point="buttonEl"]'
                     '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 2
        }

    ibeacon_services_cancel_button = \
        {
            'XPATH': '//*[@class="beacon-ctn"]//*[@data-dojo-attach-point="buttonEl"]'
                     '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 2
        }

    policy_settings_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-titlePolicy Settings"]',
            'wait_for': 2
        }

    access_security_pre_authentication_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enablePreauth"]',
            'wait_for': 5
        }

    access_security_settings_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'index': 2,
            'wait_for': 5
        }

    ssid_authentication_additional_settings_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="additionalSettingsToggle"]//*[@class="header-toggle-caret"]',
            'wait_for': 5
        }

    advance_access_security_customize_button = \
        {
            'CSS_SELECTOR': '.btn.btn-2.J-option-widget',
            'index': 1,
            'wait_for': 5
        }

    np_ssid_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'index': 1,
            'wait_for': 5
        }

    np_switches_check_box = \
        {
            'XPATH': '//input[@data-automation-tag="automation-policy-switches"]',
            'wait_for': 3
        }
    np_routing_check_box = \
        {
            'XPATH': '//input[@data-automation-tag="automation-policy-routing"]',
            'wait_for': 3
        }

    devices_stack_update_policy_dropdown_btn = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single chzn-container-active"]',
            'wait_for': 5
        }

    devices_stack_update_policy_dropdown_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mainWizDiv"]//div[@data-automation-tag="chzn-drop-ctn"]',
            'wait_for': 5
        }

    perform_update_policy_button = \
        {
            'XPATH': '//div/a[@data-dojo-attach-point="uploadBtn"]',
            'wait_for': 2
        }

    perform_after_select_update_policy_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-config-download-options-update-btn"]',
            'wait_for': 2
        }

    yes_after_perform_update_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-notification-yes-btn"]',
            'wait_for': 2
        }

    additional_settings_classifiermaps = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ClassifierMaps"]',
            'wait_for': 5
        }

    classifiermaps_enable = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableClassifierMaps"]',
            'wait_for': 5
        }

    classifiermaps_name = \
        {
            'XPATH': '//div[@data-dojo-attach-point="settings"]//div/input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    classifiermaps_description = \
        {
            'XPATH': '//div[contains(@id,"ClassifierMaps")]//div/textarea',
            'wait_for': 5
        }

    classifiermaps_add_button = \
        {
            'XPATH': '//div[@id="ah/util/form/Grid_2"]''//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    classifiermaps_services_selectfromfollowing_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceIp"]',
            'wait_for': 5
        }

    classifiermaps_services_select_service_bgp = \
        {
            'XPATH': '//span[normalize-space()="BGP"]',
            'wait_for': 5
        }

    classifiermaps_services_initial_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="selectIp"]//div[@class="ui-dialog-bottom clearfix"]//button[@class="btn btn-primary fn-right"]',
            'wait_for': 5
        }

    classifiermaps_services_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createService"]//div[@class="ui-dialog-bottom clearfix"]//button[@class="btn btn-primary fn-right"]',
            'wait_for': 5
        }

    classifiermaps_macoui_link = \
        {
            'XPATH': '//a[normalize-space()="MAC OUIs"]',
            'wait_for': 5
        }

    classifiermaps_macoui_add = \
        {
            'XPATH': '//div[@id="ah/util/form/Grid_3"]//span[1]',
            'wait_for': 5
        }

    classifiermaps_macoui_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    classifiermaps_add_macoui_from_dropdown = \
        {
            'XPATH': '//li[normalize-space()="Aerohive-08EA44"]',
            'wait_for': 5
        }

    classifiermaps_macoui_save_button = \
        {
            'XPATH': '//div[@class="btn-area ui-dialog-bottom clearfix"]//button[2]',
            'wait_for': 5
        }

    classifiermaps_ssid_link = \
        {
            'XPATH': '//*[@id="ah/util/Tab_1"]/div[1]/div[3]/a[1]',
            'wait_for': 5
        }

    classifiermaps_add_ssid = \
        {
            'XPATH': '//*[@id="ah/util/form/Grid_4"]/div[1]/div[2]/span[1]',
            'wait_for': 5
        }

    classifiermaps_ssid_save_button = \
        {
            'XPATH': '//div[@class="btn-area ui-dialog-bottom clearfix"]//button[2]',
            'wait_for': 5
        }

    classifiermaps_802_link = \
        {
            'XPATH': '//div[@class="ui-tab ui-tab-updated clearfix ui-tab-active"]//a[1]',
            'wait_for': 5
        }

    classifiermaps_802enable = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enable8021p"]',
            'wait_for': 5
        }

    classifiermaps_diffservenable = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableServ"]',
            'wait_for': 5
        }

    classifiermaps_80211enable = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enable80211e"]',
            'wait_for': 5
        }

    Classifier_Maps_save_button = \
        {
            'XPATH': '//div[contains(@id,"ClassifierMaps")]//div/button[2]',
            'wait_for': 2
        }

    qos_options_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-titleQoS Options"]',
            'wait_for': 2
        }

    additional_settings_marker_maps = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-MarkerMaps"]',
            'wait_for': 2
        }

    marker_maps_status_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableMarkerMap"]',
            'wait_for': 2
        }

    marker_maps_name_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="settings"]//div/input[@data-dojo-attach-point="name"]',
            'wait_for': 3
        }

    marker_maps_description = \
        {
            'XPATH': '//div[contains(@id,"MarkerMaps")]//div/textarea',
            'wait_for': 3
        }

    marker_maps_8021P = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enablemarkers"]',
            'wait_for': 2
        }

    marker_maps_NetworkControl_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="markersOne"]',
            'wait_for': 2
        }

    marker_maps_ControlledLoad_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="markersFour"]',
            'wait_for': 2
        }

    marker_maps_Excellent_Effort_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="markersFive"]',
            'wait_for': 2
        }

    marker_maps_Best_Effort2_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="markersSeven"]',
            'wait_for': 2
        }

    marker_maps_Switch_to_diffServ = \
        {
            'XPATH': '//div[@class="ui-tab ui-tab-updated ui-tab-inactive clearfix"]/a',
            'wait_for': 2
        }

    marker_maps_diffServ = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enablediffServ"]',
            'wait_for': 2
        }

    marker_maps_NC_diffServ_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="diffServOne"]',
            'wait_for': 2
        }

    marker_maps_Voice_diffServ_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="diffServTwo"]',
            'wait_for': 2
        }

    marker_maps_Video_diffServ_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="diffServThree"]',
            'wait_for': 2
        }

    marker_maps_BG_diffServ_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="diffServEight"]',
            'wait_for': 2
        }

    marker_maps_services_save_button = \
        {
            'XPATH': '//div[contains(@id,"MarkerMaps")]//div/button[2]',
            'wait_for': 2
        }

    additional_settings_QoS_Overview = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-QoSOverview"]',
            'wait_for': 2
        }

    QoS_Dynamic_Airtime_Scheduling_Enable = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableDynamicAirTimeScheduling"]',
            'wait_for': 2
        }

    QoS_services_save_button = \
        {
            'XPATH': '//div[contains(@id,"QoSOverview")]//div/button[2]',
            'wait_for': 2
        }

    add_ssid_menu = \
        {
            'XPATH': '//*[@data-automation-tag="automation-wireless-ssids-add-btn"]',
            'wait_for': 5
        }

    select_all_other_networks = \
        {
            'XPATH': '//*[@data-automation-tag="automation-wireless-ssids-menu-all-other-networks-(standard)"]',
            'wait_for': 5
        }

    wireless_networks_ssid_textfield = \
        {
            'XPATH': '//input[@data-automation-tag="automation-ssid-details-ssid-name"]',
            'wait_for': 5
        }

    OWE_wifi2_checkbox = \
        {
            'XPATH': '//*[@data-automation-tag="automation-ssid-details-wifi2-radio"]',
            'wait_for': 5
        }

    OWE_wifi2_dialogue_box_yes = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    Enhanced_Open_Authentication = \
        {
            'XPATH': '//*[@data-automation-tag="undefined-enhanced-open-access"]',
            'wait_for': 5
        }

    OWE_Transition_mode = \
        {
            'XPATH': '//input[@data-automation-tag="ssid-details-access-security-owe-transition-mode"]',
            'wait_for': 5
        }

    enhanced_open_ssid_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enhancedOpenSsid"]',
            'wait_for': 5
        }

    save_enhanced_open_ssid = \
        {
            'XPATH': '//*[@data-automation-tag="ssid-details-save-button"]',
            'wait_for': 5
        }

    network_policy_management_options = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ManagementOptions"]',
            'wait_for': 5
        }

    enable_management_options = \
        {
            'XPATH': '//input[@data-dojo-attach-point="globalSwitcher"]',
            'wait_for': 5
        }

    management_option_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="settings"]//*[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    enable_legacy_http_redirect = \
        {
            'XPATH': '//*[@data-automation-tag="automation-http-redirect"]',
            'wait_for': 5
        }

    save_management_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buttonArea"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    mgmt_option_success = \
        {
            'XPATH': '//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 1
        }

    management_option_on_off_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="globalSwitcher"]',
            'wait_for': 5
        }

    re_use_management_options_setting_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="resuableIcon"]',
            'index': 2,
            'wait_for': 4
        }

    table_management_options_rows = \
        {
            "CSS_SELECTOR": '.dojoxGridRow',
            
        }

    table_management_options_row_checkbox = \
        {
            "CSS_SELECTOR": '.dojoxGridCell',
            'wait_for': 5
        }

    management_options_select_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-dialog-link"]',
            
        }

    device_templates_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tab-switch-settings"]',
            'wait_for': 5
        }

    nw_policy_port_types_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="100"]',
            'wait_for': 3
        }

    next_page_element_disabled = \
        {
            'CSS_SELECTOR': '.J-page-next.ui-page-item-next.ui-page-item-disable'
        }

    next_page_element = \
        {
            'XPATH': '//*[@data-dojo-attach-point="next-item1"]',
            'index': 1
        }

    switching_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tab-switch-settings"]',
            'wait_for': 3
        }

    common_settings_voss = \
        {
            'XPATH': '//*[@data-automation-tag="policy-switching-settings-voss"]',
            'wait_for': 3
        }

    voss_parameters_text = \
        {
            'XPATH': "//div[@class='common-switch-settings']",
            'wait_for': 3
        }

    port_types_section = \
        {
            'XPATH': '//li[@data-automation-tag="policy-switching-port-types"]',
            'wait_for': 3
        }

    port_types_title_page = \
        {
            'XPATH': '//div[contains(text(),"Port Types")]',
            'wait_for': 3
        }

    add_new_port_type = \
        {
            'XPATH': '//button[@data-automation="grid-add-button"]',
            'wait_for': 3
        }

    select_platform_voss = \
        {
            'XPATH': '//a[@data-automation-tag="switching-port-type-add-voss"]',
            'wait_for': 3
        }

    select_platform_exos = \
        {
            'XPATH': '//a[@data-automation-tag="switching-port-type-add-exos"]',
            'wait_for': 3
        }

    edit_port_type = \
        {
            'XPATH': '//div[@data-automation="grid-edit-button"]',
            'wait_for': 3
        }

    delete_port_type = \
        {
            'XPATH': '//div[@data-automation="grid-delete-button"]',
            'wait_for': 3
        }

    port_types_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="hcGrid"]//table[@class="dgrid-row-table"]//tr',
            'wait_for': 5
        }

    port_type_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 3
        }

    nw_policy_additional_settings_dns_server_tab = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-dnsServer"]',
            'wait_for': 5
        }

    dns_server_status = \
        {
            "XPATH": "//input[@data-automation-tag='automation-dns-server-enable']",
            'wait_for': 5
        }

    dns_server_save_button = \
        {
            "XPATH": '//button[@data-dojo-attach-point="saveButton" and text()="Save DNS Server"]',
            'wait_for': 5
        }

    common_settings_exos = \
        {
            'XPATH': '//li[@data-automation-tag="policy-switching-settings-exos"]',
            'wait_for': 3
        }

    common_settings_exos_stp_toogle = \
        {
            'CSS_SELECTOR': '.panel-container.exos-settings [data-automation-tag="automation-common-settings-stp-toggle"]',
            'wait_for': 3
        }

    common_settings_voss_stp_toogle = \
        {
            'CSS_SELECTOR': '.panel-container.voss-settings [data-automation-tag="automation-common-settings-stp-toggle"]',
            'wait_for': 3
        }

    common_settings_save_button = \
        {
            'XPATH': '//button[@data-automation-tag="common-settings-save"]',
            'wait_for': 3
        }

    all_common_settings_configs = \
        {
            'CSS_SELECTOR': '.ui-tle .title',
            'wait_for': 3
        }
