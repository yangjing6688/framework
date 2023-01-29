class Network360PlanDefinitions:
    n360_plan_location_search_box = \
        {
            'XPATH': '//*[@data-automation-tag="automation-plan-search-field"]',
            'wait_for': 5
        }

    n360_plan_floors = \
        {
            'XPATH': '//*[@data-automation-tag="automation-plan-search-field"]',
            'wait_for': 5
        }

    n360_plan_search_matches = \
        {
            'XPATH': '//*[@style="background-color: #fc0;"]',
            'wait_for': 5
        }

    n360_plan_aps_on_floor = \
        {
            'CSS_SELECTOR': '.wlan-node.map-node',
            'wait_for': 5
        }

    n360_plan_ap_count_on_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apCount"]',
            'wait_for': 2
        }

    import_map_upload_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importForm"]'
                     '//div[@data-dojo-attach-point="importFileUploader"]'
                     '//input[@name="file"]',
            'wait_for': 5,
            'index': 0
        }

    import_map_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnImportMap"]',
            'wait_for': 5
        }

    import_map_successful_text = \
        {
            'XPATH': '//*[@data-dojo-attach-point="importDoneTip"]',
            'wait_for': 5
        }

    import_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnImport"]',
            'wait_for': 5
        }

    add_building_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addBuildingBtn"]',
            'wait_for': 5
        }

    tooltip_close_button = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeButtonNode"]',
            'wait_for': 5
        }

    import_map_button_from_loaded_account = \
        {
            'XPATH': '//*[@data-dojo-attach-point="importMapBtn"]',
            'wait_for': 5
        }

    import_map_already_exist_text = \
        {
            'XPATH': '//*[@class="ui-tipbox ui-tipbox-error"]//*[@class="ui-tipbox-title"]',
            'wait_for': 5
        }