class AdvanceOnboardingDefinitions:
    deploy_devices_to_cloud_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="cloudButton"]',
            'wait_for': 5
         }

    deploy_devices_locally_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="localButton"]',
            'wait_for': 5
         }

    deploy_devices_get_started_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-zero-day-welcome-get-started"]',
            'wait_for': 5
         }

    deploy_devices_next_location_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-zero-day-location-next-button"]',
            'wait_for': 5
         }

    deploy_location_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="locationNode"]//input[@class="location-input"]',
            'wait_for': 5
         }
    deploy_building_textfield = \
        {
            'XPATH': '//div[@class="location-building-ctn"]//input[@class="location-input"]',
            'wait_for': 5
         }

    deploy_building_address = \
        {
            'XPATH': '//div[@class="location-building-ctn"]//input[@data-automation-tag="automation-location-search"]',
            'wait_for': 5
         }

    deploy_floor_textfield = \
        {
            'XPATH': '//div[@class="floor-input"]//input[@class="location-input"]',
            'wait_for': 5
        }

    deploy_floor_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveFloor"]',
            'wait_for': 5
        }

    devices_type_real_radio_button = \
        {
            'XPATH': '//input[@data-automation-tag="automation-zero-day-onboard-real-device-radio"]',
            'wait_for': 5
         }

    devices_type_simulated_radio_button = \
        {
            'XPATH': '//input[@data-automation-tag="automation-zero-day-onboard-sim-device-radio"]',
            'wait_for': 5
         }

    entry_type_manual_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enterManuallyRadio"]',
            'wait_for': 5
         }

    entry_type_csv_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="importCsvRadio"]',
            'wait_for': 5
         }

    serial_number_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="serialNumbers"]',
            'wait_for': 5
         }

    device_make_aerohive_dropdown = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]//span[contains(text(), "Extreme - Aerohive")]',
            'wait_for': 5
        }

    device_make_select_one_dropdown = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]//span[contains(text(), "Select One")]',
            'wait_for': 5
        }

    device_make_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="chzn-drop-ctn"]'
                     '//ul[@class="chzn-results qa-chzn-results-manualdevicemake"]//li',
            'wait_for': 5
        }

    assign_location_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="locationNode"]//input[@data-dojo-attach-point="hcSelectButton"]',
            'wait_for': 5
        }

    location_select_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="btnSelect"]',
            'wait_for': 5
        }

    onboard_devices_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="btnSave"]',
            'wait_for': 5
        }

    onboard_success_status_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceMsg"]//div[@class="device-onboard-success-status"]',
            'wait_for': 5
        }

    onboard_device_finish_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-zero-day-onboard-save-button"]',
            'wait_for': 5
        }

    drawer_trigger = \
        {
         'XPATH': '//div[@data-dojo-attach-point="drawerTrigger"]',
         'wait_for': 3
         }

    drawer_content = \
        {
         'XPATH': '//div[@data-dojo-attach-point="drawerContent"]',
         'wait_for': 3
         }

    select_assign_location_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSelect"]',
            'wait_for': 5
        }

    onboard_success_message = \
        {
         'CSS_SELECTOR': '.device-onboard-success-status',
         'wait_for': 10
         }

    locations_generic = \
        {
            'XPATH': '//*[@data-folder-type="GENERIC"]',
            'wait_for': 5
        }

    locations_building = \
        {
            'XPATH': '//*[@data-folder-type="BUILDING"]',
            'wait_for': 5
        }

    locations_floors = \
        {
            'XPATH': '//*[@data-folder-type="FLOOR"]',
            'wait_for': 5
        }

    deploy_devices_next_topology_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-zero-day-onboard-save-button"]',
            'wait_for': 5
         }

    advance_onboard_device_finish_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    advance_onboard_cloudiq_engine_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cloudIqEngineRadio"]',
            'wait_for': 5
        }


