class CopilotDefs:

    wifi_capacity_content = \
        {
            'XPATH': '//*[@class="wifi-capacity-widget"]'
                     '//*[@class="nui-auto-copilot-wifi-capacity-summary-description"]',
            'wait_for': 10
         }

    wifi_capacity_widget = \
        {
            'XPATH':  '//*[@class="wifi-capacity-widget"]',
            'wait_for': 20
         }
    wifi_capacity_status = \
        {
            'XPATH': '//button[contains(@class,"mat-focus-indicator secondary-button-color")]',
            'index': 1,
            'wait_for': 10
        }

    wifi_capacity_widget_location_grid_rows = \
        {
            'XPATH': '//*[@class="wifi-capacity-widget"]//*[contains(@class, "list-item ng-star-inserted")]',
            'CSS_SELECTOR': '.as-list-item-clickable',
            'wait_for': 5
         }

    wifi_capacity_widget_location_grid_internal_rows = \
        {
            'CSS_SELECTOR': '.as-ah-row',
            'wait_for': 5
        }

    wifi_capacity_widget_location_grid_pin_rows = \
        {
            'XPATH': '//*[@class="wifi-capacity-widget"]//*[contains(@class, "list-item ng-star-inserted")]'
                     '//*[contains(@class, "pinned-item")]',
            'wait_for': 5
         }

    wifi_capacity_widget_location_pin_button = \
        {
            'CSS_SELECTOR':'.material-icons.nui-auto-copilot-wifi-capacity-summary-pin',
            'wait_for': 5
        }

    wifi_capacity_widget_location_already_pinned_status = \
        {
            'CSS_SELECTOR':'.pinned-item',
            'wait_for': 5
        }

    wifi_capacity_widget_location_more_options_button = \
        {
            'CSS_SELECTOR':'.nui-auto-copilot-wifi-capacity-summary-more-options',
            'wait_for': 5
        }

    wifi_capacity_widget_location_more_options_mute_button = \
        {
            'CSS_SELECTOR': '.mat-focus-indicator.mat-menu-item',
            'wait_for': 5
        }

    wifi_capacity_widget_location_grid_muted_rows = \
        {
            'XPATH': '//*[@class="wifi-capacity-widget"]//*[@class="as-list-item-wrapper as-list-muted"]',
            'wait_for': 5
         }

    wifi_capacity_anomaly_ap_issue_details = \
        {
            'CSS_SELECTOR': '.eff-aly-desc',
            'wait_for': 5
        }

    wifi_capacity_anomaly_ap_recommended_actions_details = \
        {
            'XPATH': '//div[@class="eff-rec-desc nui-auto-copilot-wifi-capacity-detail-recommend-action-desc"]',
            'wait_for': 5
        }

    total_anomalies_detected_from_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="headAnomalyRingNum"]',
            'wait_for': 10
         }

    anomalies_detected_grid_rows = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="headAnomalyRingList"]//div[@class="as-list-item"]',
            'wait_for': 5
         }

    wifi_capacity_more_options_btn = \
        {
            'CSS_SELECTOR':'.nui-auto-copilot-wifi-capacity-summary-more-options',
            'wait_for': 5
        }

    wifi_capacity_dismiss_option = \
        {
            'CSS_SELECTOR': '.mat-focus-indicator.mat-menu-item',
            'index': 1,
            'wait_for': 5
        }

    wifi_capacity_dismiss_warning = \
        {
            'CSS_SELECTOR': '.mat-dialog-content',
            'wait_for': 5
        }

    wifi_capacity_dismiss_no_option = \
        {
            'XPATH': '//*[@class="mat-dialog-actions"]'
                     '//*[@class="mat-focus-indicator secondary-button-color mat-button mat-button-base"]',
            'wait_for': 5
        }

    wifi_capacity_dismiss_yes_option = \
        {
            'XPATH': '//*[@class="mat-dialog-actions"]//*[@class="mat-focus-indicator primary-button-color '
                     'mat-raised-button mat-button-base mat-primary"]',
            'wait_for': 5
        }

    wifi_capacity_widget_location_grid_individual_ap_rows = \
        {
            'CSS_SELECTOR': '.as-ah-row',
            'wait_for': 5
         }

    wifi_capacity_widget_location_individual_ap_pin_button = \
        {
            'CSS_SELECTOR':'.material-icons',
            'wait_for': 5
        }

    wifi_capacity_widget_location_individual_ap_unpin_button = \
        {
            'CSS_SELECTOR':'.material-icons.pinned-item',
            'wait_for': 5
        }

    wifi_capacity_widget_location_detailed_view_close_button = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-capacity-detail-close-btn',
            'wait_for': 5
        }
    
    anomalies_view_all_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="activeAlarmLink"]',
            'wait_for': 5
        }

    copilot_branded_image = \
        {
            'CSS_SELECTOR': '.pilot.co-pilot-beta',
            'wait_for': 5
        }

    assurance_scan_widget = \
        {
            'XPATH': '//*[@class="assurance-scan-widget"]',
            'wait_for': 10
        }

    assurance_total_scan_count = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-assurance-scanheader-text',
            'wait_for': 10
        }

    show_or_hide_muted_button_in_wifi_capacity_widget = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-capacity-summary-toggle-muted-btn',
            'wait_for': 10
        }

    anomaly_notification_grid_rows = \
        {
            'XPATH': '//*[@data-dojo-attach-point="headAnomalyRingList"]//div[@class="as-list-item"]',
            'wait_for': 5
         }

    wifi_capacity_video_help_icon = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-efficiency-summary-help-btn',
            'wait_for': 5
         }

    wifi_capacity_additional_resources_docs_links = \
        {
            'XPATH': '//ul[@class="resource"]//a[@href]',
            'wait_for': 5
         }

    wifi_capacity_additional_resources_video_links = \
        {
            'XPATH': '//div[@class="video-container"]//iframe[@src]',
            'wait_for': 5
         }

    wifi_capacity_additional_resources_close_button = \
        {
            'CSS_SELECTOR': '.nui-auto-wifi-efficiency-help-dialog-close-btn',
            'wait_for': 5
         }

    wifi_capacity_widget_anomaly_pinned_status = \
        {
            'CSS_SELECTOR': '.pinned-item',
            'wait_for': 1
        }

    wifi_capacity_widget_sort_options = \
        {
            'XPATH': '//*[@class="copilot-card copilot-wifi-capacity-card"]'
                     '//ul[@data-automation-tag="chzn-results-ctn"]//li',
            'wait_for': 5
        }

    wifi_capacity_widget_sort = \
        {
            'XPATH': '//div[@class="copilot-card copilot-wifi-capacity-card"]'
                     '//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5
        }

    wifi_efficiency_widget = \
        {
            'XPATH': '//*[@class="wifi-efficiency-widget"]',
            'wait_for': 5
         }

    wifi_efficiency_widget_content = \
        {
            'XPATH': '//*[@class="wifi-efficiency-widget"]'
                     '//*[@class="nui-auto-copilot-wifi-efficiency-summary-description"]',
            'wait_for': 5
        }

    wifi_efficiency_widget_location_grid_rows = \
        {
            'XPATH': '//*[@class="wifi-efficiency-widget"]//*[contains(@class, "list-item ng-star-inserted")]',
            'wait_for': 5
         }

    wifi_efficiency_widget_location_already_pinned_status = \
        {
            'CSS_SELECTOR':'.pinned-item',
            'wait_for': 5
        }

    wifi_efficiency_widget_location_pin_button = \
        {
            'CSS_SELECTOR':'.material-icons.pin-anomaly-cls',
            'wait_for': 5
        }

    poe_stability_widget = \
        {
                'XPATH': '//*[@class="poe-stability-widget"]',
                'wait_for': 10
         }

    poe_stability_content = \
        {
            'XPATH': '//*[@class="poe-stability-widget"]'
                     '//*[@class="nui-auto-copilot-poe-stability-summary-description"]',
            'wait_for': 10
         }

    poe_stability_widget_location_grid_rows = \
        {
            'XPATH': '//*[@class="poe-stability-widget"]//*[contains(@class, "list-item ng-star-inserted")]',
            'CSS_SELECTOR': '.as-list-item-clickable',
            'wait_for': 10
         }

    poe_stability_widget_location_grid_pin_rows = \
        {
            'XPATH': '//*[@class="poe-stability-widget"]//*[contains(@class, "list-item ng-star-inserted")]'
                     '//*[contains(@class, "pinned-item")]',
            'wait_for': 5
         }

    poe_stability_widget_location_pin_button = \
        {
            'CSS_SELECTOR':'.material-icons.nui-auto-copilot-poe-stability-summary-pin',
            'wait_for': 5
        }

    poe_stability_widget_location_already_pinned_status = \
        {
            'CSS_SELECTOR':'.pinned-item',
            'wait_for': 5
        }

    port_efficiency_widget = \
        {
            'XPATH':  '//*[@class="uplink-efficiency-widget"]',
            'wait_for': 1
        }

    port_efficiency_widget_details = \
        {
            'XPATH': '//*[@class="uplink-efficiency-widget"]'
                     '//*[@class="nui-auto-copilot-uplink-efficiency-summary-description"]',
            'wait_for': 10
        }

    port_efficiency_widget_location_grid_rows = \
        {
            'XPATH': '//*[@class="uplink-efficiency-widget"]//*[contains(@class, "list-item ng-star-inserted")]',
            'CSS_SELECTOR': '.as-list-item-clickable',
            'wait_for': 10
         }

    port_efficiency_widget_location_grid_pin_rows = \
        {
            'XPATH': '//*[@class="uplink-efficiency-widget"]//*[contains(@class, "list-item ng-star-inserted")]'
                     '//*[contains(@class, "pinned-item")]',
            'wait_for': 10
         }

    port_efficiency_widget_location_pin_button = \
        {
            'CSS_SELECTOR':'.material-icons.nui-auto-copilot-uplink-efficiency-summary-pin',
            'wait_for': 5
        }

    port_efficiency_widget_location_already_pinned_status = \
        {
            'CSS_SELECTOR':'.pinned-item',
            'wait_for': 5
        }

    dfs_recurrence_widget = \
        {
            'CSS_SELECTOR': '.dfs-recurrence-widget',
            'wait_for': 15
         }

    dfs_recurrence_widget_content = \
        {
            'CSS_SELECTOR': '.anomaly-description',
            'wait_for': 5,
         }

    dfs_recurrence_anomaly_list  = \
        {
            'TAG_NAME': 'nui-copilot-anomaly-list-item',
            'wait_for': 5,
         }

    anomaly_location =  \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-summary-location-name',
            'wait_for': 5,
         }

    anomaly_severity = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-summary-overall-severity',
            'wait_for': 5,
        }

    anomaly_last_detected = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-summary-last-detected',
            'wait_for': 5,
        }

    anomaly_pinned = \
        {
            'CSS_SELECTOR': '.pinned-item.nui-auto-copilot-dfs-recurrence-summary-pin',
            'wait_for': 5,
        }

    anomaly_muted = \
        {
            'CSS_SELECTOR': '.impact.alm-impact-muted.nui-auto-copilot-dfs-recurrence-summary-overall-severity',
            'wait_for': 5,
        }

    anomaly_device_details = \
        {
            'CSS_SELECTOR': '.mat-content',
            'wait_for': 5,
        }

    anomaly_device_name = \
        {
            'CSS_SELECTOR': '.as-ah-site-name.nui-auto-copilot-dfs-recurrence-detail-location-name',
            'wait_for': 5,
        }

    anomaly_device_last_detected = \
        {
            'CSS_SELECTOR': '.as-ah-last-detected.nui-auto-copilot-dfs-recurrence-detail-last-detected',
            'wait_for': 5,
        }

    anomaly_device_anomaly_severity = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-detail-severity',
            'wait_for': 5,
        }

    anomaly_device_pinned_status = \
        {
            'CSS_SELECTOR': '.material-icons.nui-auto-copilot-dfs-recurrence-detail-pin.pinned-item',
            'wait_for': 5
        }

    dfs_recurrence_anomaly_muted = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-summary-toggle-muted-btn',
            'wait_for': 5
        }
    account_summary_widget = \
        {
            'CSS_SELECTOR': '.account-summary-widget',
            'wait_for': 5
        }

    account_summary_row = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-account-summary-list',
            'wait_for': 5
        }

    account_summary_row_key = \
        {
            'CSS_SELECTOR': '.account-key',
            'wait_for': 5
        }

    account_summary_row_value = \
        {
            'CSS_SELECTOR': '.value-display',
            'wait_for': 5
        }

    extremecloud_iq_applications_widget = \
        {
            'CSS_SELECTOR': '.app-subscription-widget',
            'wait_for': 5
        }

    extremecloud_iq_applications_row = \
        {
            'CSS_SELECTOR': '.appList',
            'wait_for': 5
        }

    extremecloud_iq_applications_row_key = \
        {
            'CSS_SELECTOR': '.appName',
            'wait_for': 5
        }

    extremecloud_iq_applications_row_value = \
        {
            'CSS_SELECTOR': '.ng-star-inserted',
            'wait_for': 5
        }

    devices_by_os_widget = \
        {
            'CSS_SELECTOR': '.devices-by-os-widget',
            'wait_for': 5
        }

    devices_by_os_row = \
        {
            'CSS_SELECTOR': '.ng-star-inserted',
            'wait_for': 5
        }

    devices_by_os_row_key = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5,
            'index': 0
        }

    devices_by_os_row_value = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5,
            'index': 1
        }

    devices_by_type_widget = \
        {
            'CSS_SELECTOR': '.devices-by-type-widget',
            'wait_for': 5
        }

    devices_by_type_row = \
        {
            'CSS_SELECTOR': '.ng-star-inserted',
            'wait_for': 5

        }

    devices_by_type_row_key = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5,
            'index': 0
        }

    devices_by_type_row_value = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5,
            'index': 1
        }

    devices_by_os_iqagent = \
        {
            'XPATH': '//span[text()="IQ ENGINE RELEASE NOTES "]',
            'wait_for': 5
        }

    copilot_widget = \
        {
            'CSS_SELECTOR': '.license-widget',
            'wait_for': 5
        }

    copilot_widget_row = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-liceneses-list',
            'wait_for': 5

        }

    copilot_widget_row_key = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5,
            'index': 0
        }

    copilot_widget_row_value = \
        {
            'TAG_NAME': 'span',
            'wait_for': 5,
            'index': 1
        }

    dfs_recurrence_widget_location_grid_rows = \
        {
            'XPATH': '//*[@class="dfs-recurrence-widget"]//*[contains(@class, "list-item ng-star-inserted")]',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_grid_pin_rows = \
        {
            'XPATH': '//*[@class="dfs-recurrence-widget"]//*[contains(@class, "list-item ng-star-inserted")]'
                     '//*[contains(@class, "pinned-item")]',
            'wait_for': 5
         }

    dfs_recurrence_widget_location_pin_button = \
        {
            'CSS_SELECTOR': '.material-icons.nui-auto-copilot-dfs-recurrence-summary-pin',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_already_pinned_status = \
        {
            'CSS_SELECTOR': '.pinned-item',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_more_options_button = \
        {
            'CSS_SELECTOR': '.alarm-actions.as-dropdown-src',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_more_options_mute_button = \
        {
            'CSS_SELECTOR': '.mat-focus-indicator.mat-menu-item',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_grid_muted_rows = \
        {
            'XPATH': '//*[@class="dfs-recurrence-widget"]//*[@class="as-list-item-wrapper as-list-muted"]',
            'wait_for': 5
         }

    dfs_recurrence_widget_location_grid_unmute_button = \
        {
            'CSS_SELECTOR': '.unmute-action.nui-auto-copilot-dfs-recurrence-summary-unmute-btn',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_more_options_btn = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-summary-more-options',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_dismiss_option = \
        {
            'CSS_SELECTOR': '.mat-focus-indicator.mat-menu-item',
            'index': 1,
            'wait_for': 5
        }

    dfs_recurrence_widget_location_dismiss_warning = \
        {
            'CSS_SELECTOR': '.mat-dialog-content',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_dismiss_no_option = \
        {
            'XPATH': '//*[@class="mat-dialog-actions"]'
                     '//*[@class="mat-focus-indicator secondary-button-color mat-button mat-button-base"]',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_dismiss_yes_option = \
        {
            'XPATH': '//*[@class="mat-dialog-actions"]//*[@class="mat-focus-indicator primary-button-color '
                     'mat-raised-button mat-button-base mat-primary"]',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_grid_individual_ap_rows = \
        {
            'CSS_SELECTOR': '.as-ah-row',
            'wait_for': 5
         }

    dfs_recurrence_widget_location_individual_ap_pin_button = \
        {
            'CSS_SELECTOR': '.material-icons',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_detailed_view_close_button = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-dfs-recurrence-detail-close-btn',
            'wait_for': 5
        }

    dfs_recurrence_widget_location_individual_ap_unpin_button = \
        {
            'CSS_SELECTOR': '.material-icons.pinned-item',
            'wait_for': 5
        }

    license_page_heading = \
        {
            'XPATH': '//*[@data-dojo-attach-point="licenseCtn"]',
            'wait_for': 10
        }

    copilot_license_mange_link = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-liceneses-manage-btn',
            'wait_for': 5
        }

    page_refresh_button = \
        {
            'XPATH': '//button/span/mat-icon[text()="refresh"]',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_grid_rows = \
        {
            'XPATH': '//*[@class="high-mbcast-widget"]//*[contains(@class, "list-item ng-star-inserted")]',
            'wait_for': 5
         }

    adverse_traffic_patterns_widget_location_grid_pin_rows = \
        {
            'XPATH': '//*[@class="high-mbcast-widget"]//*[contains(@class, "list-item ng-star-inserted")]'
                     '//*[contains(@class, "pinned-item")]',
            'wait_for': 5
         }

    adverse_traffic_patterns_widget_location_pin_button = \
        {
            'CSS_SELECTOR': '.material-icons.nui-auto-copilot-high-mbcast-summary-pin',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_already_pinned_status = \
        {
            'CSS_SELECTOR':'.pinned-item',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_anomaly_muted = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-toggle-muted-btn',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget = \
        {
            'CSS_SELECTOR': '.high-mbcast-widget',
            'wait_for': 15
         }

    adverse_traffic_patterns_anomaly_list  = \
        {
            'TAG_NAME': 'nui-copilot-anomaly-list-item',
            'wait_for': 5,
         }

    adverse_traffic_patterns_anomaly_location =  \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-location-name',
            'wait_for': 5,
         }

    adverse_traffic_patterns_anomaly_severity = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-overall-severity',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_last_detected = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-last-detected',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_pinned = \
        {
            'CSS_SELECTOR': '.pinned-item.nui-auto-copilot-high-mbcast-summary-pin',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_muted = \
        {
            'CSS_SELECTOR': '.impact.alm-impact-muted.nui-auto-copilot-high-mbcast-summary-overall-severity',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_device_details = \
        {
            'CSS_SELECTOR': '.mat-content',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_device_name = \
        {
            'CSS_SELECTOR': '.as-ah-site-name.nui-auto-copilot-high-mbcast-detail-location-name',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_device_last_detected = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-detail-last-detected',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_device_anomaly_severity = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-detail-severity',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_device_pinned_status = \
        {
            'CSS_SELECTOR': '.material-icons.nui-auto-copilot-high-mbcast-detail-pin.pinned-item',
            'wait_for': 5
        }

    adverse_traffic_patterns_dfs_recurrence_anomaly_muted = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-toggle-muted-btn',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_grid_individual_ap_rows = \
        {
            'CSS_SELECTOR': '.as-ah-row',
            'wait_for': 5
         }

    adverse_traffic_patterns_device_list  = \
        {
            'TAG_NAME': 'nui-copilot-device-list-item',
            'wait_for': 5,
         }

    adverse_traffic_patterns_anomaly_device_location_name =  \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-detail-location-name',
            'wait_for': 5,
         }

    adverse_traffic_patterns_anomaly_device_severity = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-detail-severity',
            'wait_for': 5,
        }

    adverse_traffic_patterns_anomaly_device_pinned = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-detail-pin.pinned-item',
            'wait_for': 5,
        }

    adverse_traffic_patterns_widget_anomaly_muted = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-toggle-muted-btn',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget = \
        {
            'CSS_SELECTOR': '.high-mbcast-widget',
            'wait_for': 15
        }

    adverse_traffic_patterns_widget_location_more_button = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-more-options',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_mute_and_dismiss_div = \
        {
            'CSS_SELECTOR': '.mat-menu-content',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_mute_button = \
        {
            'CSS_SELECTOR': '.mat-focus-indicator',
            'index': 0,
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_dismiss_button = \
        {
            'CSS_SELECTOR': '.mat-focus-indicator',
            'index': 1,
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_unmute_button = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-unmute-btn',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_dismiss_confirm_dialog = \
        {
            'CSS_SELECTOR': '.confirmation-dialog',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_cancel = \
        {
            'XPATH': '//*[@class="mat-dialog-actions"]'
                     '//*[@class="mat-focus-indicator secondary-button-color mat-button mat-button-base"]',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_okay = \
        {
            'XPATH': '//*[@class="mat-dialog-actions"]//*[@class="mat-focus-indicator primary-button-color '
                     'mat-raised-button mat-button-base mat-primary"]',
            'wait_for': 5
        }

    adverse_traffic_patterns_widget_content = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-high-mbcast-summary-description',
            'wait_for': 5,
         }

    wifi_capacity_widget_location_ap_dislike = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-capacity-detail-downvote',
            'XPATH': '//span[text()="thumb_down"]',
            'wait_for': 10
        }

    wifi_capacity_widget_location_ap_dislike_send_feedback_button = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-capacity-detail-send-feedback',
            'XPATH': '//span[text()="send"]',
            'wait_for': 10
        }

    wifi_capacity_widget_location_ap_dislike_send_feedback_textfield = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-capacity-detail-send-feedback-input',
            'wait_for': 10
        }

    wifi_capacity_widget_location_ap_like_tooltip = \
        {
            'TAG_NAME': 'simple-snack-bar',
            'wait_for': 10
        }

    wifi_capacity_widget_location_ap_dislike_button_enabled_status = \
        {
            'CSS_SELECTOR': '.nui-auto-copilot-wifi-capacity-detail-downvote.material-icons.vote-thumb-down.user-vote',
            'wait_for': 10
        }
