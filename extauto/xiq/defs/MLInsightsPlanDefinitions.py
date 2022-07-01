class MLInsightsPlanDefinitions:

    n360_plan_create_new_map_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCreateNewMap"]',
            'CSS_SELECTOR': '.addLocationBtn',
            'wait_for': 2
        }

    n360_plan_create_new_map_window = \
        {
            'XPATH': '//*[@id="ah/util/dojocover/AHDialog_1_title"]',
            'wait_for': 2
        }

    n360_plan_create_map_organization = \
        {
            'XPATH': '//*[@data-dojo-attach-point="organization"]',
            'wait_for': 2
        }

    n360_plan_create_map_street_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="street"]',
            'wait_for': 2
        }

    n360_plan_create_map_city_state = \
        {
            'XPATH': "//*[@data-dojo-attach-point='city']",
            'wait_for': 2
        }

    n360_plan_create_map_get_started = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnSave']",
            'wait_for': 2
        }

    n360_plan_map_close_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnCancelLocation']",
            'wait_for': 2
        }

    n360_plan_import_map_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnImportMap"]',
            'wait_for': 5
        }

    n360_plan_import_map_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnImport"]',
            'wait_for': 5
        }

    n360_plan_import_map_cancel_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancel"]',
            'wait_for': 5
        }

    n360_plan_add_location_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addLocationBtn"]',
            'wait_for': 5
        }

    n360_plan_add_loc_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="locationName"]',
            'wait_for': 5
        }

    n360_plan_add_loc_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="locationAddress"]',
            'wait_for': 5
        }

    n360_plan_add_loc_city = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cityAsLoc"]',
            'wait_for': 5
        }

    n360_plan_add_loc_state_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stateAsLoc"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_loc_state_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-stateasloc"]/li',
            'wait_for': 5
        }

    n360_plan_add_loc_outdoor_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="isOutdoor"]',
            'wait_for': 5
        }

    n360_plan_add_loc_associated_loc_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="assoWithInLocation"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_loc_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveLocation"]',
            'wait_for': 5
        }

    n360_plan_add_loc_cancel = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancelLocation"]',
            'wait_for': 5
        }

    n360_plan_add_building_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingName"]',
            'wait_for': 5
        }

    n360_plan_add_building_addr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingAddress"]',
            'wait_for': 5
        }

    n360_plan_add_building_city = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingCity"]',
            'wait_for': 5
        }

    n360_plan_add_building_state_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buildingState"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_building_state_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-buildingstate"]/li'
        }

    n360_plan_add_building_associated_loc_dropdown = \
        {
            'XPATH': '//*[@class="input-field chzn-done"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_building_associated_loc_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-parentid10"]/li',
            'wait_for': 5
        }

    n360_plan_add_building_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveBuilding"]',
            'wait_for': 5
        }

    n360_plan_add_building_cancel = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCancelBuilding"]',
            'wait_for': 5
        }

    n360_plan_add_floor_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="floorName"]',
            'wait_for': 5
        }

    n360_plan_add_floor_association_dropdown = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]/a[@class="chzn-single"]/span',
            'index': 0,
            'wait_for': 5
        }

    n360_plan_add_floor_association_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-parentid2"]/li',
            'wait_for': 5
        }

    n360_plan_add_floor_environment_dropdown = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]/a[@class="chzn-single"]/span',
            'index': 1,
            'wait_for': 5
        }

    n360_plan_add_floor_environment_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-environment"]/li',
            'wait_for': 5
        }

    n360_plan_add_floor_attenuation = \
        {
            'XPATH': '//*[@data-dojo-attach-point="floorLoss"]',
            'wait_for': 5
        }

    n360_plan_add_floor_height = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceElevation"]',
            'wait_for': 5
        }

    n360_plan_add_floor_size_width = \
        {
            'XPATH': '//*[@data-dojo-attach-point="metricWidth"]',
            'wait_for': 5
        }

    n360_plan_add_floor_size_height = \
        {
            'XPATH': '//*[@data-dojo-attach-point="metricHeight"]',
            'wait_for': 5
        }

    n360_plan_add_floor_height_metric_drop_down = \
        {
            'XPATH': '//*[@class="input-col ap-install-height-col"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_floor_size_metric_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mapSizeRow"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_floor_metric_option_feet = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-option-feet"]',
            'wait_for': 5
        }

    n360_plan_add_floor_metric_option_meter = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-option-meters"]',
            'wait_for': 5
        }

    n360_plan_add_floor_bgimg_dropdown = \
        {
            'XPATH': '//*[@class="folder-row back-image-row"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_plan_add_floor_bgimg_options = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-backimagesel"]/li',
            'wait_for': 5
        }

    n360_plan_add_floor_bgimg_lib_floorpln_img = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imgListWrp"]',
            'wait_for': 5
        }

    n360_plan_add_floor_bgimg_lib_floorpln_choose = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnChoose"]',
            'wait_for': 5
        }
    n360_plan_floor_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSaveFloor"]',
            'wait_for': 5
        }

    n360_plan_network_summary = \
        {
            'XPATH': '//*[@data-dojo-attach-point="summaryName"]//h2[contains(text(), "Network Summary")]',
            'wait_for': 5
        }

    n360_plan_search_box = \
        {
            'XPATH': '//*[@data-automation-tag="automation-plan-search-field"]',
            'wait_for': 5
        }

    n360_plan_edit = \
        {
            'CSS_SELECTOR': '.plan-leftnav.edit',
            'wait_for': 5
        }

    n360_plan_add = \
        {
            'CSS_SELECTOR': '.plan-leftnav.add',
            'wait_for': 5
        }

    n360_plan_more = \
        {
            'CSS_SELECTOR': '.plan-leftnav.more',
            'wait_for': 5
        }

    n360_plan_export = \
        {
            'CSS_SELECTOR': '.plan-leftnav.export',
            'wait_for': 5
        }

    n360_plan_delete = \
        {
            'CSS_SELECTOR': '.plan-leftnav.delete',
            'wait_for': 5
        }

    n360_plan_add_map_folder = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addMapFolder"]',
            'wait_for': 5
        }

    n360_plan_ap_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apCount"]',
            'wait_for': 5
        }

    n360_plan_device_name = \
        {
            'XPATH': '//*[@class="leaf-label"]',
            'index': 1,
            'wait_for': 5
        }

    n360_plan_search_grid = \
        {
            'XPATH': '//*[@class="text"]',
            'wait_for': 5
        }

    n360_plan_router_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="routerCount"]',
            'wait_for': 5
        }

    n360_plan_switch_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="srCount"]',
            'wait_for': 5
        }

    n360_plan_vgva_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vgvaCount"]',
            'wait_for': 5
        }

    ml_insights_click = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-n360"]',
            'wait_for': 5
        }

    network_360_plan_click = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-plan"]',
            'wait_for': 5
        }

    n360_plan_add_global_view = \
        {
            'XPATH': '//div[@class="map-tree"]//dd[@data-level="0"]//span[@title="Add"]',
            'wait_for': 5
        }

    n360_select_locn = \
        {
            'XPATH': '//dd[@data-folder-type="GENERIC"]',
            'wait_for': 5
        }

    n360_add_building_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addBuildingBtn"]',
            'wait_for': 5
        }

    n360_select_building_tab = \
        {
            'XPATH': '//*[@data-folder-type="BUILDING"]//div[@class="actions"]',
            'wait_for': 5
        }

    n360_plan_select_bldg_tab = \
        {
            'XPATH': '//dl[@data-dojo-attach-point="tabs"]//dd[2]',
            'wait_for': 5
        }

    n360_add_floor_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addFloorBtn"]',
            'wait_for': 5
        }

    n360_plan_select_add_floor = \
        {
            'XPATH': '//dd[@class="level-last building level1"]//span[@title="Add"]',
            'wait_for': 5
        }

    manage_left_pane_click = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-manage"]',
            'wait_for': 5
        }

    manage_devices_click = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-nav-devices"]',
            'wait_for': 5
        }

    n360_select_floor_more = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[@data-level="3"]//span[contains(@class, "more")]',
            'wait_for': 2
        }

    n360_delete_floor = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[@data-level="3"]//span[contains(@class, "delete")]',
            'wait_for': 5
        }

    n360_select_building_more = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[@data-level="2"]//span[contains(@class, "more")]',
            'wait_for': 2
        }

    n360_delete_building = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[@data-level="2"]//span[contains(@class, "delete")]',
            'wait_for': 5
        }

    n360_select_location_more = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[@data-level="1"]//span[contains(@class, "more")]',
            'wait_for': 2
        }

    n360_delete_location = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[@data-level="1"]//span[contains(@class, "delete")]',
            'wait_for': 5
        }

    n360_delete_yes = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    n360_country_list_click = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }
    n360_country_change_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }
    n360_click_x_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createDoneTipX"]',
            'wait_for': 5
        }

    n360_extend_floor = \
        {
            'XPATH': '//*[@data-folder-type="BUILDING"]//span[@class="plan-leftnav oc-icon"]',
            'wait_for': 5
        }

    n360_click_floor = \
        {
            'XPATH': '//*[@data-folder-type="FLOOR"]',
            'wait_for': 5
        }

    n360_upload_floor_map = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnUploadFloorPlan"]',
            'wait_for': 5
        }
    n360_choose_from_library = \
        {
            'XPATH': '//*[@data-dojo-attach-point="chooseItem"]',
            'wait_for': 5
        }
    n360_choose_image = \
        {
            'XPATH': '//*[@data-dojo-attach-point="imgListWrp"]',
            'wait_for': 5
        }
    n360_save_button_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnChoose"]',
            'wait_for': 5
        }

    n360_size_floor_plan = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSizeFloorPlan"]',
            'wait_for': 5
        }
    n360_width_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="width"]',
            'wait_for': 5
        }

    n360_height_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="height"]',
            'wait_for': 5

        }
    n360_apply_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnApply"]',
            'wait_for': 5
        }
