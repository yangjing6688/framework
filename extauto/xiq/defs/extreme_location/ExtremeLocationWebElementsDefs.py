class ExtremeLocationWebElementsDefs:
    extreme_location_more_insights_tab = \
        {
            'CSS_SELECTOR': '.mat-button-wrapper',
            'index': 5,
            'wait_for': 3
        }

    extreme_location_subscribe_page = \
        {
            'CSS_SELECTOR': '.subscribe-flow',
            'wait_for': 5
        }

    extreme_location_subscribe_button = \
        {
            'CSS_SELECTOR': '.dijitReset.dijitInline.dijitButtonText',
            'wait_for': 5
        }

    extreme_location_subscribe_apply_button = \
        {
            'CSS_SELECTOR': '.btn.btn-primary',
            'wait_for': 5
        }

    bss_device_button = \
        {
            'XPATH': '(//*[text()="BSS Devices"])[1]',
            'wait_for': 5
        }
    
    devices_bss_devices_sites_dropdown_button = \
    {
        'XPATH': '//*[contains(@class, "xloc-bss-main-site-db")]'
                 '//span[@class="select2-selection__arrow"]',
            'wait_for': 5
    }
    
    extreme_location_devices_wireless_devices_sites_dropdown = \
        {
            'XPATH': '//*[contains(@class, "xloc-wireless-devices-main-site-db")]'
                     '//span[@class="select2-selection__arrow"]',
            'wait_for': 5
        }

    devices_wireless_devices_sites_dropdown_items = \
        {
            'CSS_SELECTOR': '.select2-results__option',
            'wait_for': 5
        }

    search_xloc_ap_page = \
        {
            'XPATH': '//div[contains(@class,"xloc-ap-summary-grid-search")]//div[contains(@class,"x-form-search-trigger")]',
            'wait_for': 5
        }

    host_to_xloc_ap_page = \
        {
            'XPATH': '//div[contains(@class,"xloc-ap-summary-grid-search")]//input[contains(@id,"allcolumnssearch")]',
            'wait_for': 5
        }

    device_building_from_xloc = \
        {
            'XPATH': '//div[contains(@id,"ApSummaryGrid")]//table[contains(@id,"gridview")]//td[contains(@class,"x-grid-cell")]//div[contains(@class,"x-grid-cell-inner ")]',
            'index': 4,
            'wait_for': 5
        }

    device_floor_from_xloc = \
        {
            'XPATH': '//div[contains(@id,"ApSummaryGrid")]//table[contains(@id,"gridview")]//td[contains(@class,"x-grid-cell")]//div[contains(@class,"x-grid-cell-inner ")]',
            'index': 5,
            'wait_for': 5
        }

    devices_bss_search_textfield = \
        {
            'XPATH': '//*[contains(@class, "xloc-bss-grid-search-txt")]'
                     '//*[contains(@class, "x-form-field")]',
            'wait_for': 5
        }
    
    devices_bss_devices_bss_textfield = \
        {
            'XPATH': '(//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")])[20]',
            'wait_for': 5
        }
    
    devices_bss_devices_ssid_textfield = \
        {
            'XPATH': '(//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")])[12]',
            'wait_for': 5
        }
    
    devices_bss_devices_floor_name_textfield = \
        {
            'XPATH': '(//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")])[22]',
            'wait_for': 5
        }
    
    
    devices_wireless_devices_search_textfield = \
        {
            'XPATH': '//*[contains(@class, "xloc-wireless-devices-grid-search-txt")]'
                     '//*[contains(@class, "x-form-field")]',
            'wait_for': 5
        }

    devices_wireless_devices_client_mac_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'wait_for': 5
        }

    devices_wireless_devices_host_name_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 1,
            'wait_for': 5
        }

    devices_wireless_devices_ip_address_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 2,
            'wait_for': 5
        }

    devices_wireless_devices_user_name_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 3,
            'wait_for': 5
        }

    devices_wireless_devices_device_type_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 4,
            'wait_for': 5
        }

    devices_wireless_devices_floor_name_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 5,
            'wait_for': 5
        }

    devices_wireless_devices_category_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 6,
            'wait_for': 5
        }

    devices_wireless_devices_site_enter_time_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 7,
            'wait_for': 5
        }

    devices_wireless_devices_category_enter_time_textfield = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]//td[contains(@class, "x-grid-cell")]',
            'index': 5,
            'wait_for': 5
        }

    wireless_devices_grid_row = \
        {
            'XPATH': '//*[contains(@id, "WirelessDevicesGrid") and contains'
                     '(@class, "x-grid-with-row-lines")]//tr[contains(@class, "x-grid-row")]',
            
        }

    extreme_location_sites_menu_dropdown_button = \
        {
            'XPATH': '//*[contains(@id, "combowithbutton")]//*[contains(@id, "trigger-picker") '
                     'and contains(@class, "x-form-arrow-trigger-default")]',
            'wait_for': 5
        }

    xloc_search_name_field = \
        {   'XPATH': '(//input[contains(@placeholder,"Search Name, MAC, Site, UUID")])[2]',
            'wait_for': 5
        } 

    common_object_grid_rows = \
        {
            'XPATH': "//tr[@class='  x-grid-row']//td[2]",
            'wait_for': 3
        }
    
    common_object_grid_ap_status = \
        {
            'XPATH': "//tr[@class='  x-grid-row']//td[10]",
            'wait_for': 3
        }
    
    view_ibeacon_details_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-third-party-beacon-grid-row-action-view")]',
            'wait_for': 3
        }
    
    xloc_third_party_beacon_edit_button = \
        {
            'XPATH': '//*[contains(@class, "x-btn xloc-third-party-beacon-edit")]',
            'wait_for': 3
        }
    
    xloc_third_party_beacon_settings = \
        {
            'XPATH': '//*[contains(@class, "xloc-third-party-beacon-settings-nav")]',
            'wait_for': 3 
        }
    
    xloc_third_party_beacon_uuid_text = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-uuid-text")]//*[contains(@class,"x-form-required-field")]',
            'wait_for': 3
        }

    xloc_third_party_beacon_major_minor_version = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-uuid-minor-version-txt")]//*[contains(@class,"x-form-required-field")]',
            'wait_for': 3
        }

    xloc_third_party_beacon_save_btn = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-save-btn")]',
            'wait_for': 3
        }

    xloc_third_party_major_minor_error_message = \
        {
            'XPATH': "//div[contains(., 'Invalid UUID Major and Minor Version')]",
            'wait_for': 2
        }

    xloc_third_party_success_message = \
        {
            'XPATH': "//div[contains(., 'Beacon details updated successfully')]",
            'wait_for': 2
        }
    
    xloc_third_party_beacon_delete_button = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-grid-row-action-delete")]',
            'wait_for': 2
        }
    xloc_third_party_beacon_confirm_button = \
        {
            'XPATH': '//*[text()="Yes"]',
            'wait_for': 2

        }
    xloc_third_party_beacon_download_button = \
        {
            'XPATH': '(//*[contains(@class,"xloc-third-party-beacon-grid-download-btn")])[2]',
            'wait_for': 2

        }
    xloc_third_party_beacon_refresh_button = \
        {
            'XPATH': '(//*[contains(@class,"xloc-third-party-beacon-grid-refresh-btn")])[2]',
            'wait_for': 2

        }
    
    extreme_location_sites_menu_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    extreme_location_sites_name_icon = \
        {
            'CSS_SELECTOR': '.leaflet-marker-icon.leaflet-zoom-animated',
            'wait_for': 5
        }

    extreme_location_sites_name_floor_link = \
        {
            'ID': 'floormap',
            'wait_for': 5
        }

    extreme_location_sites_client_mac_search_textfield = \
        {
            'CSS_SELECTOR': '.x-tagfield-input-field',
            'wait_for': 5
        }

    extreme_location_sites_client_mac_radio_button = \
        {
            'ID': 'radio-1160-inputEl',
            'wait_for': 5
        }

    extreme_location_sites_device_preference_apply_button = \
        {
            'XPATH': '//*[@class="x-btn-button x-btn-button-e-tbar-p-btn-flat-toolbar-small x-btn-text    x-btn-button-center "]',
            'index': 1,
            'wait_for': 5
        }

    extreme_location_sites_client_mac_search_suggestions_textfield = \
        {
            'CSS_SELECTOR': '.x-tagfield-arialist-item',
            'wait_for': 5
        }

    extreme_location_sites_client_mac_search_entered_textfield = \
        {
            'CSS_SELECTOR': '.x-tagfield-item-text',
            'wait_for': 5
        }

    extreme_location_sites_device_preference_apply_button_disabled = \
        {
            'CSS_SELECTOR': '.x-btn-e-tbar-p-btn-flat-toolbar-small.x-item-disabled.x-btn-disabled',
            'wait_for': 5
        }

    extreme_location_sites_menu_floor_name_dropdown_button = \
        {
            'ID': 'combo-1214-trigger-picker',
            'wait_for': 5
        }

    extreme_location_sites_menu_floor_name_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    async_window_presence_button = \
        {
            'XPATH': '//input[contains(@class,"presence-analytics-on")]',
            
        }

    async_window_ibeacon_button = \
        {
            'XPATH': '//input[contains(@class,"ibeacon-on")]',
            
        }

    xloc_authentication_error = \
        {
            'XPATH': '//span[contains(text(),"Authentication Failure")]',
            
        }

    refresh_eloc_sites_page = \
        {
            'XPATH': '//*[@class="fa fa-refresh"]',
            'index': 1,
            'wait_for': 5
        }

    refresh_eloc_devices_page = \
        {
            'XPATH': '//*[@class="fa fa-refresh"]',
            'index': 9,
            'wait_for': 5
        }

    extreme_location_asset_add_button = \
        {
            'XPATH': '//*[contains(@class,"xloc-asset-form-add-btn")]//*[contains(@class,"x-btn-inner x-btn-inner-e-tbar-p-btn-circular-toolbar-small")]',
            'wait_for': 3
        }

    xloc_assetname_textfield = \
        {
            'XPATH': '//input[contains(@name,"assetname")]',
            'wait_for': 3
        }

    xloc_asset_sites_click = \
        {
            'CSS_SELECTOR': '.xloc-asset-form-select-site-db',
            'wait_for': 3
        }

    xloc_asset_sites_search_field = \
        {
            'CSS_SELECTOR': '.select2-search__field',
            'wait_for': 3
        }

    xloc_asset_sites_search_click = \
        {
            'CSS_SELECTOR': '.select2-results',
            'wait_for': 3
        }

    xloc_asset_assetcategory_click = \
        {
            'XPATH': '//*[@class="x-field xloc-asset-form-select-category-db x-form-item x-form-item-default x-form-type-text x-box-item x-field-default x-vbox-form-item x-form-invalid"]//*[@class="x-form-trigger x-form-trigger-default x-form-arrow-trigger x-form-arrow-trigger-default  "]',
            'wait_for': 3
        }

    xloc_asset_assetcategory_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 3
        }

    enable_wifi_radio_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-asset-form-tracker-details-wifi-rb")]'
                     '//*[contains(@class, "x-form-radio-default")]',
            'wait_for': 3
        }

    xloc_wifi_asset_mac = \
        {
            'XPATH': '//*[@class="x-form-field x-form-empty-field x-form-empty-field-default x-form-text x-form-text-default  x-form-invalid-field x-form-invalid-field-default"]',
            'wait_for': 3
        }

    enable_ble_radio_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-asset-form-tracker-details-ble-rb")]'
                     '//*[contains(@class, "x-form-radio")]',
            'wait_for': 3
        }

    xloc_asset_ibeacon_click = \
        {
            'XPATH': '//*[contains(@class, "xloc-asset-form-beacon-id-db")]//*[contains(@class, "x-form-trigger")]',
            'wait_for': 3
        }

    xloc_asset_ibeacon_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 3
        }

    enable_none_radio_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-asset-form-tracker-details-none-rb")]'
                     '//*[contains(@class, "x-form-radio")]',
            'wait_for': 3
        }

    xloc_asset_cc_click = \
        {
            'CSS_SELECTOR': '.xloc-asset-form-confined-cat-db',
            'wait_for': 3
        }

    xloc_asset_cc_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 3
        }

    xloc_asset_pc_click = \
        {
            'CSS_SELECTOR': '.xloc-asset-form-prohibited-cat-db',
            'wait_for': 3
        }

    xloc_asset_pc_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 3
        }

    extreme_location_asset_save_button = \
        {
            'CSS_SELECTOR': '.xloc-asset-form-save-changes-btn',
            'wait_for': 3
        }

    assets_search_textfield = \
        {
            'CSS_SELECTOR': '.eloc-grid-search-cls.xloc-asset-grid-clmn-search',
            'wait_for': 3
        }

    grid_row_assets = \
        {
            'XPATH': '//div[@class="x-grid-item-container"]//tr[@class="  x-grid-row"]',
            'wait_for': 3
        }

    delete_asset = \
        {
            'CSS_SELECTOR': '.xloc-asset-gridrow-action-delete',
            'wait_for': 3
        }

    delete_asset_yes = \
        {
            'XPATH': '//*[contains(@class, "xloc-delete-asset-msg-box")]//*[contains(@class, "x-btn-button")]',
            'wait_for': 3,
            'index': 1
        }

    delete_asset_no = \
        {
            'XPATH': '//*[contains(@class, "xloc-delete-asset-msg-box")]//*[contains(@class, "x-btn-button")]',
            'wait_for': 3,
            'index': 2
        }

    actions_asset = \
        {
            'CSS_SELECTOR': '.xloc-asset-gridrow-action-view',
            'wait_for': 3
        }

    actions_edit_asset = \
        {
            'CSS_SELECTOR': '.xloc-asset-form-edit-btn',
            'wait_for': 3
        }

    click_refresh_xloc_summary = \
        {
            'XPATH': '//*[contains(text(), "refresh")]',
            'wait_for': 5
        }

    device_classification_table_rows = \
        {
            'XPATH': '//*[contains(@id, "DeviceClassificationGrid") and contains'
                     '(@class, "x-grid-with-row-lines")]//tr[contains(@class, "x-grid-row")]',
            
        }

    device_classification_edit_btn = \
        {
            'XPATH': '//div[contains(@class,"xloc-device-classification-gridrow-action-edit")]',
            'wait_for': 5
        }

    provide_ssid_checkbox = \
        {
            'XPATH': '//*[contains(@class, "xloc-configure-rule-provide-ssid-rb")]'
                     '//*[contains(@class, "x-form-radio-eloc-radio-checkbox")]',
            'wait_for': 5
        }

    visitor_duration_checkbox = \
        {
            'XPATH': '//*[contains(@class, "xloc-configure-rule-visitor-duration-rb")]'
                     '//*[contains(@class, "x-form-radio-eloc-radio-checkbox")]',
            'wait_for': 5
        }

    device_classification_ssid_text_field = \
        {
            'XPATH': '//*[contains(@class, "x-form-required-field")]//*[contains(@class, "x-tagfield-list")]',
            'wait_for': 5
        }

    device_classification_ssid_dropdown_items = \
        {
            'XPATH' : '//*[contains(@class, "x-boundlist-list-ct")]//li',
            'wait_for' : 10,
        }

    device_classification_ssid_list = \
        {
            'XPATH': '//*[contains(@class, "x-form-required-field")]//*[contains(@class, "x-tagfield-list")]//li',
            'wait_for': 5
        }

    device_classification_ssid_close_btn = \
        {
            'XPATH': '//*[contains(@class, "x-tagfield-item-close")]',
            'wait_for': 5
        }

    visitor_duration_hrs_textbox = \
        {
            'XPATH': '//*[contains(@class, "xloc-configure-rule-visitor-duration-hr-txt")]'
                     '//*[contains(@class, "x-form-text-default")]',
            'wait_for': 5
        }

    visitor_duration_min_textbox = \
        {
            'XPATH': '//*[contains(@class, "x-field xloc-configure-rule-visitor-duration-mins-txt")]'
                     '//*[contains(@class, "x-form-text-default")]',
            'wait_for': 5
        }

    device_classification_edit_disabled_btn = \
        {
            'XPATH': '//div[contains(@class,"xloc-device-classification-gridrow-action-edit") and contains(@class, "x-item-disabled")]',
            'wait_for': 5,
            'index': 0
        }

    get_datapoint1_value = \
        {
            'XPATH': '//*[contains(@class, "user-summary-wrapper")]//div[@class="user-count"]',
            'index': 0,
            'wait_for': 5
        }

    get_datapoint2_value = \
        {
            'XPATH': '//*[contains(@class, "user-summary-wrapper")]//div[@class="user-count"]',
            'index': 1,
            'wait_for': 5
        }

    xloc_ibeacon_add_button = \
        {
            'XPATH': '//*[contains(@data-qtip, "Beacons")]//*[contains(@id, "btnInnerEl") '
                     'and contains(@class, "circular-toolbar-small")]',
            'wait_for': 5
        }

    xloc_ibeacon_name = \
        {
            'XPATH': '//*[contains(@id, "ThirdPartyBeacons")]//*[contains(@id, "textfield") '
                     'and contains(@class,"x-form-required-field")]',
            'wait_for': 5
        }

    
    xloc_uuid_name = \
        {
            'XPATH': '//*[contains(@class,"x-field xloc-third-party-beacon-uuid-text")]//*[contains(@class, "x-form-field x-form-empty-field")]',
            'wait_for': 5
        }

    xloc_major_version = \
        {
            'XPATH': '(//*[contains(@class, "x-field xloc-third-party-beacon-uuid-major-version-txt")]//*[contains(@class, "x-form-field x-form-empty-field")])[1]',
            'wait_for': 5
        }

    xloc_minor_version = \
        {
            'XPATH': '(//*[contains(@class, "x-field xloc-third-party-beacon-uuid-minor-version-txt")]//*[contains(@class, "x-form-field x-form-empty-field")])[1]',
            'wait_for': 5
        }

    xloc_ibeacon_site_dropdown = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-site-db")]//*[@class="select2-selection__arrow"]',
            'wait_for': 5
        }

    xloc_ibeacon_site_name = \
        {
            'CSS_SELECTOR': '.select2-results__option',
            'wait_for': 5
        }

    xloc_ibeacon_as_category_dropdown = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-category-db")]//*[contains(@class,"x-form-arrow-trigger")]',
            'wait_for': 5
        }

    xloc_ibeacon_as_category_name = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    xloc_ibeacon_ibeacon_mac_address = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-mac-address-txt")]//*[contains(@class,"x-form-required-field")]',
            'wait_for': 3
        }

    xloc_ibeacon_rssi = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-rssi-txt")]//*[contains(@class,"x-form-required-field")]',
            'wait_for': 3
        }

    xloc_ibeacon_advertisement_interval = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-ad-interval-db")]//*[contains(@class,"x-form-required-field")]',
            'wait_for': 3
        }

    xloc_ibeacon_save = \
        {
            'XPATH': '//*[contains(@class,"xloc-third-party-beacon-form-save-btn")]',
            'wait_for': 3
        }

    xloc_device_classification_add_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-device-classification-btn")]',
            'wait_for': 5
        }

    xloc_device_classification_add_device_rule_menu_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-device-classification-create-rule-btn")]',
            'wait_for': 5
        }

    xloc_device_classification_user_type_drop_down_options = \
        {
            'XPATH': '//*[contains(@class, "x-boundlist")]//*[contains(@id, "picker-listEl")]//li',
            'wait_for': 5
        }

    xloc_device_classification_user_type_drop_down_button = \
        {
            'XPATH': '//div[contains(@class, "xloc-configure-rule-user-type-db")]'
                     '//div[contains(@class, "x-form-arrow-trigger")]',
            'wait_for': 5
        }

    xloc_device_classification_duration_hours_textfield = \
        {
            'XPATH': '//div[contains(@class, "xloc-configure-rule-visitor-duration-hr-txt")]//input',
            'wait_for': 5
        }

    xloc_device_classification_duration_minutes_textfield = \
        {
            'XPATH': '//div[contains(@class, "xloc-configure-rule-visitor-duration-mins-txt")]//input',
            'wait_for': 5
        }

    xloc_device_classification_visitor_duration_radio_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-configure-rule-visitor-duration-rb")]//input',
            'wait_for': 5
        }

    xloc_device_classification_save_button = \
        {
            'XPATH': '//*[contains(@class, "xloc-configure-rule-save-btn")]',
            'wait_for': 5
        }

    xloc_device_classification_success_message = \
        {
            'XPATH': '//*[contains(text(), "Classification Configuration saved")]',
            'wait_for': 5
        }

    xloc_device_classification_rows = \
        {
            'XPATH': '//*[contains(@class, "deviceClassificationGrid")]//*[contains(@class, "x-grid-row")]',
            'wait_for': 5
        }

    device_classification_save_btn = \
        {
            'XPATH': '//a[contains(@class,"xloc-configure-rule-save-btn")]',
            'wait_for': 5
        }

    device_classification_ssid_drop_down_list = \
        {
            'XPATH': '//div[contains(@class,"x-boundlist")]//ul[contains(@class,"x-list-plain")]//li',
            'wait_for': 5
        }

    device_classification_ssid_drop_down = \
        {
            'XPATH': '//div[contains(@class,"addDeviceRuleCls")]//div[contains(@class,"x-fit-item")]//div[contains(@class,"tagfield-min-height")]//div[contains(@class,"x-form-item-body")]//div[contains(@class,"x-form-arrow-trigger")]',
            'wait_for': 5
        }

    device_type_sites_page_drop_down_list = \
        {
            'XPATH': '//div[contains(@class,"x-boundlist")]//ul//li',
            'wait_for': 5
        }

    device_classification_grid_row = \
        {
            'XPATH': '//div[contains(@class,"deviceClassificationGrid")]//table//tr[contains(@class,"x-grid-row")]',
            
         }

    device_classification_ssid_radio_btn = \
        {
            'XPATH': '//div[contains(@class,"xloc-configure-rule-provide-ssid-rb")]',
            'wait_for': 5
        }

    enter_subscriber_url = \
        {
            'XPATH': '//input[@name="textfield-2040-inputEl"]',
            'wait_for': 5
        }

    enter_subscriber_url_username = \
        {
            'XPATH': '//input[@name="lsenseusername"]',
            'wait_for': 5
        }

    enter_subscriber_url_password = \
        {
            'XPATH': '//input[@name="pwdText"]',
            'wait_for': 5
        }

    click_presence_event = \
        {
            'XPATH': '//input[@name="presenceEnabled"]',
            'wait_for': 5
        }

    click_category_event = \
        {
            'XPATH': '//input[@name="categoryEnabled"]',
            'wait_for': 5
        }

    click_location_event = \
        {
            'XPATH': '//input[@name="locationEnabled"]',
            'wait_for': 5
        }

    click_rssi_event = \
        {
            'XPATH': '//input[@name="rssiEnabled"]',
            'wait_for': 5
        }

    click_crowding_event = \
        {
            'XPATH': '//input[@name="crowdingEnabled"]',
            'wait_for': 5
        }

    click_alarm_event = \
        {
            'XPATH': '//input[@name="alarmEnabled"]',
            'wait_for': 5
        }

    click_save_third_party_btn = \
        {
            'XPATH': '//a[@id="button-2064"]',
            'wait_for': 5
        }

    click_reset_third_party_btn = \
        {
            'XPATH': '//a[@id="button-2063"]',
            'wait_for': 5
        }

    click_test_connection_btn_third_party = \
        {
            'CSS_SELECTOR': '.xloc-test-connection-btn',
            'wait_for': 5
        }

    test_connection_xloc_status_textfield = \
        {
            'CSS_SELECTOR': '.xloc-status-text',
            'wait_for': 5
        }

    click_xloc_test_connection_close_btn = \
        {
            'CSS_SELECTOR': '.x-tool-close',
            'wait_for': 5
        }

    click_engagement_category = \
        {
            'XPATH': '//*[@class="x-grid-cell-inner x-grid-cell-inner-treecolumn"]//span[contains(text(), "Engagement Category")]',
            'wait_for': 5
        }

    click_engagement_category_add = \
        {
            'XPATH': '//span[@id="button-1361-btnEl"]',
            'wait_for': 5
        }

    click_engagement_category_name = \
        {
            'XPATH': '//input[@id="textfield-1277-inputEl"]',
            'wait_for': 5
        }

    click_engagement_category_threshold = \
        {
            'XPATH': '//input[@id="numberfield-1280-inputEl"]',
            'wait_for': 5
        }

    click_engagement_category_save = \
        {
            'XPATH': '//span[@id="button-1364-btnInnerEl"]',
            'wait_for': 5
        }

    click_engagement_category_site = \
        {
            'XPATH': '//*[@class="journeyCountDiv countDiv"]',
            'wait_for': 5
        }

    click_engagement_category_site_edit = \
        {
            'XPATH': '//span[@id="button-1362-btnEl"]',
            'wait_for': 5
        }

    click_engagement_category_site_map = \
        {
            'XPATH': '//span[@id="button-1301-btnInnerEl"]',
            'wait_for': 5
        }

    xloc_category_site_list = \
        {
            'XPATH': '//*[@class="x-panel-body x-grid-with-row-lines x-grid-body x-panel-body-default x-panel-body-default x-noborder-rbl"]//*[@class="x-grid-item-container"]//*[@class="x-grid-item"]',
            'wait_for': 5
        }

    click_category_site_select_next = \
        {
            'XPATH': '//*[@class="x-btn-inner x-btn-inner-default-small"]//*[@class="fa fa-arrow-right"]',
            'wait_for': 5
        }

    click_category_site_map_final = \
        {
            'XPATH': '//*[contains(@class,"xloc-asset-cat-select-sites-map-btn")]',
            'wait_for': 3
        }

    click_asset_category = \
        {
            'XPATH': '//*[@class="x-grid-cell-inner x-grid-cell-inner-treecolumn"]//span[contains(text(), "Asset Category")]',
            'wait_for': 5
        }

    click_asset_category_add = \
        {
            'XPATH': '(//*[contains(@class,"x-btn-inner x-btn-inner-e-tbar-p-btn-circular-toolbar-small")])[5]',
            'wait_for': 5
        }

    click_asset_category_name = \
        {
            'XPATH': '(//*[contains(@class,"x-form-field x-form-required-field x-form-text x-form-text-default  x-form-empty-field x-form-empty-field-default x-form-invalid-field x-form-invalid-field-default")])',
            'wait_for': 5
        }


    click_asset_category_save = \
        {
            'XPATH': '(//*[contains(@class,"x-btn-inner x-btn-inner-e-tbar-p-btn-flat-toolbar-small")])[3]',
            'wait_for': 5
        }

    click_asset_category_site = \
        {
            'XPATH': '//*[@class="x-grid-cell-inner x-grid-cell-inner-treecolumn"]//span[contains(text(), "Site")]',
            'wait_for': 5
        }

    click_asset_category_site_edit = \
        {
            'XPATH': '(//*[@class="x-btn-inner x-btn-inner-e-tbar-p-btn-circular-toolbar-small"])[6]',
            'wait_for': 5
        }

    click_asset_category_site_map = \
        {
            'XPATH': '(//span[contains(text(), "Map Site")])[2]',
            'wait_for': 5
        }
