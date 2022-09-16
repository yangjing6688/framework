class MLInsightsClient360Definitions:

    n360_client_360_avg_rssi_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="avgRSSIStaticRef"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_client_360_avg_snr_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="avgSNRStaticRef"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_client_360_wifi_health_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifiStaticRef"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    n360_client_360_avg_rssi_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="avgRSSIStaticRef"]//ul[@class="chzn-results"]/li',
            'wait_for': 5
        }

    n360_client_360_avg_snr_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="avgSNRStaticRef"]//ul[@class="chzn-results"]/li',
            'wait_for': 5
        }

    n360_client_360_wifi_health_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifiStaticRef"]//ul[@class="chzn-results"]/li',
            'wait_for': 5
        }

    n360_client_360_supported_mode_loc = \
        {
            'XPATH': '//*[@data-dojo-attach-point="supModeStaticRef"]//div[@client-location-tip]',
            'wait_for': 5
        }

    n360_client_360_real_time_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="realTime"]',
            'wait_for': 5
        }

    n360_client_360_historical_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="historical"]',
            'wait_for': 5
        }

    n360_client_360_client_total_use = \
        {
            'XPATH': '//*[@data-dojo-attach-point="totalUsageRec"]//span',
            'wait_for': 5,
            'index': 1
        }

    n360_client_360_client_last_con = \
        {
            'XPATH': '//*[@data-dojo-attach-point="lastConnectedRec"]//span',
            'wait_for': 5,
            'index': 1
        }

    n360_client_360_con_time = \
        {
            'XPATH': '//*[@data-dojo-attach-point="totalSessionTimeRec"]',
            'wait_for': 5,
            'index': 1
        }

    n360_client_360_avg_rssi = \
        {
            'XPATH': '//*[@data-dojo-attach-point="avgRssiRec"]',
            'wait_for': 5,
            'index': 1
        }

    n360_client_360_avg_snr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="avgSnrRec"]',
            'wait_for': 5,
            'index': 1
        }

    n360_client_360_wifi_health = \
        {
            'XPATH': '//*[@data-dojo-attach-point="wifiHealthRec"]',
            'wait_for': 5,
            'index': 1
        }

    n360_client_360_client_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientBtnName"]',
            'wait_for': 5
        }

    n360_client_360_client_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            
        }

    n360_client_360_table_select_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="tableSelector"]//span[contains(text(), "IoT View")]',
            'wait_for': 5
        }

    n360_client_360_table_sel_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="tableSelector]//ul[@data-automation-tag="chzn-results-ctn"]/li',
            'wait_for': 5
        }

    n360_client_360_client_refresh = \
        {
            'XPATH': '//*[@data-dojo-attach-point="refresh"]',
            'wait_for': 5
        }

    client_360_real_time_tab = \
        {
            'XPATH': '//li[@data-dojo-attach-point="realTime"]',
            'wait_for': 5
        }

    client_360_inactive_tab = \
        {
            'XPATH': '//li[@data-dojo-attach-point="historical"]',
            'wait_for': 5
        }

    client_360_real_time_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="activeClientsBox"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    client_360_real_time_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    client360_health_status = \
        {
            'CSS_SELECTOR': '.status-ico',
            'wait_for': 5
        }

    client360_cells_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 5
        }

    client_360_status_ostype = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientOSType"]',
            'wait_for': 5
        }

    client_360_status_ipaddress = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ip"]',
            'wait_for': 5
        }

    client_360_status_macaddress = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMac"]',
            'wait_for': 5
        }

    client_360_status_user = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userName"]',
            'wait_for': 5
        }

    client_360_status_connectto = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientDeviceName"]',
            'wait_for': 5
        }

    client_360_status_connecttime = \
        {
            'XPATH': '//*[@data-dojo-attach-point="connectedTime"]',
            'wait_for': 5
        }

    client_360_status_vlan = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlan"]',
            'wait_for': 5
        }

    client_360_status_cwp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cwpUsed"]',
            'wait_for': 5
        }

    client_360_status_userprofile = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userProfile"]',
            'wait_for': 5
        }

    client_360_status_ssid = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssid"]',
            'wait_for': 5
        }

    client_360_status_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macProtocol"]',
            'wait_for': 5
        }

    client_36_status_channel = \
        {
            'XPATH': '//*[@data-dojo-attach-point="channel"]',
            'wait_for': 5
        }

    close_current_connection_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }