class Network360MonitorDefinitions:
    n360_monitor_location_search_box = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tracker-search-field"]',
            'wait_for': 5
        }

    n360_monitor_floors = \
        {
            'XPATH': '//*[@data-automation-tag="automation-plan-search-field"]',
            'wait_for': 5
        }

    n360_monitor_search_matches = \
        {
            'XPATH': '//*[@style="background-color: #fc0;"]',
            'wait_for': 5
        }

    n360_monitor_aps_on_floor = \
        {
            'CSS_SELECTOR': '.device-hostname',
            'wait_for': 5
        }

    n360_monitor_ap_count_on_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apCount"]',
            'wait_for': 2
        }

    n360_monitor_connected_clients_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMenuItem"]',
            'wait_for': 5
        }

    n360_monitor_clients_on_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMenuItem"]',
            'wait_for': 5
        }

    n360_connected_client_macs = \
        {
            'CSS_SELECTOR': '.field-macAddress',
            'wait_for': 5
        }

    n360_monitor_devices_score = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceHealthScoreLabelCtn"]',
            'wait_for': 5
        }

    n360_monitor_devices_card = \
        {
            #'XPATH': '//*[@data-dojo-attach-point="deviceHealthScoreLabelCtn"]//span[@class="open-screen-icon ah-global-icon"]',
            #'XPATH': '//*[@data-dojo-attach-point="automation-tracker-n360-card-device"]',
            'CSS_SELECTOR': '.open-screen-icon.ah-global-icon',
            'index': 0,
            'wait_for': 5
        }

    n360_monitor_clients_card = \
        {
            'CSS_SELECTOR': '.open-screen-icon.ah-global-icon',
            'index': 1,
            'wait_for': 5
        }

    device_health_overal_score_availability_score = \
        {
            'XPATH': '//*[@data-dojo-attach-point="scoreAvailabilityValue"]',
            'wait_for': 5
        }

    device_health_overal_score_hw_health = \
        {
            'XPATH': '//*[@data-dojo-attach-point="scoreHardwareValue"]',
            'wait_for': 5
        }

    device_health_overal_score_fw_score = \
        {
            'XPATH': '//*[@data-dojo-attach-point="scoreConfFirmwareValue"]',
            'wait_for': 5
        }

    n360_monitor_map = \
        {
            'XPATH': '//*[@data-dojo-attach-point="physicalMap"]',
            'wait_for': 5
        }

    client_health_clients_widget_count_2G = \
        {
            'XPATH': '//span[contains(text(), "2.4 GHz")]/../b',
            'wait_for': 5
        }

    client_health_clients_widget_count_5G = \
    {
        'XPATH': '//span[contains(text(),"5 GHz")]/../b',
        'wait_for': 5
    }

    client_health_clients_widget_count_6G = \
    {
        'XPATH': '//span[contains(text(),"6 GHz")]/../b',
        'wait_for': 5
    }