class MLInsightsMonitorDefinitions:

    n360_monitor_click_create_map = \
        {
            'XPATH': '//*[@class="map-landing"]//a[contains(text, "Click here")]',
            'wait_for': 5
        }

    n360_monitor_create_new_map_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCreateNewMap"]',
            'CSS_SELECTOR': '.addLocationBtn',
            'wait_for': 2
        }

    n360_monitor_create_map_organization = \
        {
            'XPATH': '//*[@data-dojo-attach-point="organization"]',
            'wait_for': 2
        }

    n360_monitor_create_map_street_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="street"]',
            'wait_for': 2
        }

    n360_monitor_create_map_city_state = \
        {
            'XPATH': "//*[@data-dojo-attach-point='city']",
            'wait_for': 2
        }

    n360_monitor_create_map_country_code = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-container-ctn"]//a[@class="chzn-single"]',
            'index': 0,
            'wait_for': 5
        }

    n360_monitor_create_map_get_started = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnSave']",
            'wait_for': 2
        }

    n360_monitor_map_close_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnCancelLocation']",
            'wait_for': 2
        }

    n360_monitor_import_map_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnImportMap"]',
            'wait_for': 5
        }

    n360_monitor_import_map_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnImport"]',
            'wait_for': 5
        }

    n360_monitor_import_map_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancel"]',
            'wait_for': 5
        }

    n360_monitor_add_location_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addLocationBtn"]',
            'wait_for': 5
        }

    n360_monitor_add_building_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addBuildingBtn"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="locationName"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="locationAddress"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_city = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cityAsLoc"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_state_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stateAsLoc"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_state_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-stateasloc"]/li',
            'wait_for': 5
        }

    n360_monitor_add_loc_outdoor_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="isOutdoor"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_associated_loc_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="assoWithInLocation"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveLocation"]',
            'wait_for': 5
        }

    n360_monitor_add_loc_cancel = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancelLocation"]',
            'wait_for': 5
        }

    n360_monitor_add_building_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingName"]',
            'wait_for': 5
        }

    n360_monitor_add_building_addr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingAddress"]',
            'wait_for': 5
        }

    n360_monitor_add_building_city = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingCity"]',
            'wait_for': 5
        }

    n360_monitor_add_building_state_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingState"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_building_state_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-buildingstate"]/li'
        }

    n360_monitor_add_building_associated_loc_dropdown = \
        {
            'XPATH': '//*[@class="input-field chzn-done"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_building_associated_loc_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-parentid10"]/li',
            'wait_for': 5
        }

    n360_monitor_add_building_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveBuilding"]',
            'wait_for': 5
        }

    n360_monitor_add_building_cancel = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancelBuilding"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="floorName"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_association_dropdown = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]/a[@class="chzn-single"]/span',
            'index': 0,
            'wait_for': 5
        }

    n360_monitor_add_floor_association_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-parentid2"]/li',
            'wait_for': 5
        }

    n360_monitor_add_floor_environment_dropdown = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]/a[@class="chzn-single"]/span',
            'index': 1,
            'wait_for': 5
        }

    n360_monitor_add_floor_environment_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-environment"]/li',
            'wait_for': 5
        }

    n360_monitor_add_floor_attenuation = \
        {
            'XPATH': '//*[@data-dojo-attach-point="floorLoss"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_height = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceElevation"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_size_width = \
        {
            'XPATH': '//*[@data-dojo-attach-point="metricWidth"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_size_height = \
        {
            'XPATH': '//*[@data-dojo-attach-point="metricHeight"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_height_metric_drop_down = \
        {
            'XPATH': '//*[@class="input-col ap-install-height-col"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_size_metric_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mapSizeRow"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_metric_option_feet = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-option-feet"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_metric_option_meter = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-option-meters"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_bgimg_dropdown = \
        {
            'XPATH': '//*[@class="folder-row back-image-row"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_bgimg_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-backimagesel"]/li',
            'wait_for': 5
        }

    n360_monitor_add_floor_bgimg_lib_floorpln_img = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imgListWrp"]',
            'wait_for': 5
        }

    n360_monitor_add_floor_bgimg_lib_floorpln_choose = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnChoose"]',
            'wait_for': 5
        }
    n360_monitor_floor_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveFloor"]',
            'wait_for': 5
        }

    n360_monitor_net_summary = \
        {
            'XPATH': '//*[@data-dojo-attach-point="summaryName"]//h2[contains(text(), "Network Summary")]',
            'wait_for': 5
        }

    n360_monitor_net_summary_loc_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="locCount"]',
            'wait_for': 5
        }

    n360_monitor_net_summary_alarm = \
        {
            'XPATH': '//*[@data-dojo-attach-point="alarm"]',
            'wait_for': 5
        }

    n360_monitor_search_box = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tracker-search-field"]',
            'wait_for': 5
        }

    n360_monitor_device_view = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceView"]',
            'wait_for': 5
        }

    n360_monitor_zone_view = \
        {
            'XPATH': '//*[@data-dojo-attach-point="zoneView"]',
            'wait_for': 5
        }

    n360_monitor_refresh_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="refreshIcon"]',
            'wait_for': 5
        }

    n360_monitor_refresh_setting = \
        {
            'XPATH': '//*[@data-dojo-attach-point="refreshSettings"]',
            'wait_for': 5
        }

    n360_monitor_refresh_setting_options = \
        {
            'XPATH': '//*[@class="settings-content-options"]/li',
            'wait_for': 5
        }

    n360_monitor_device_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceNum"]',
            'wait_for': 5
        }

    n360_monitor_device_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceStatus"]',
            'wait_for': 5
        }

    n360_monitor_client_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientNum"]',
            'wait_for': 5
        }

    n360_monitor_client_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientStatus"]',
            'wait_for': 5
        }

    n360_monitor_wifi_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifiNum"]',
            'wait_for': 5
        }

    n360_monitor_wifi_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifiStatus"]',
            'wait_for': 5
        }

    n360_monitor_network_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkNum"]',
            'wait_for': 5
        }

    n360_monitor_network_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkStatus"]',
            'wait_for': 5
        }

    n360_monitor_service_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="servicesNum"]',
            'wait_for': 5
        }

    n360_monitor_service_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="servicesStatus"]',
            'wait_for': 5
        }

    n360_monitor_app_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="appNum"]',
            'wait_for': 5
        }

    n360_monitor_app_usage = \
        {
            'XPATH': '//*[@data-dojo-attach-point="appStatus"]',
            'wait_for': 5
        }

    n360_monitor_security_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="securityNum"]',
            'wait_for': 5
        }

    n360_monitor_security_total_rogues = \
        {
            'XPATH': '//*[@data-dojo-attach-point="securityStatus"]',
            'wait_for': 5
        }

    n360_monitor_select_bt_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="selectBtDevice"]',
            'wait_for': 5
        }

    n360_monitor_ap_name = \
        {
            'XPATH': '//*[@class="device-hostname"]',
            'wait_for': 5
        }

    n360_monitor_ap_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apCount"]',
            'wait_for': 5
        }
    n360_monitor_search_grid = \
        {
            'XPATH': '//*[@class="text"]',
            'wait_for': 5
        }

