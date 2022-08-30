
class ClientWebElementsDefinitions:
    get_monitor_tab_menu = \
        {
            'XPATH': '/html/body/div[1]/div[1]/div/div/div/ul/li[3]/ul/li[3]/a',
            'wait_for': 3
         }

    get_monitor_clients_tab_menu = \
        {
            'XPATH': '//*[@id="appHeader"]/ul/li[3]/ul/li[3]/a',
            'wait_for': 3
         }

    client_page_grid_rows = {'CSS_SELECTOR': '.dgrid-row', }

    client_status_green = \
        {
            'CSS_SELECTOR': '.status-connected-good',
            'wait_for': 1
         }

    client_connection_status = \
        {
            'CSS_SELECTOR': '.field-connectionStatus',
            'wait_for': 5
        }

    clients_historical_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="historical"]',
            'wait_for': 5,
        }

    clients_real_time_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="realTime"]',
            'wait_for': 1,
        }

    client_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    client_gdpr_delete_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="gdprDelete"]',
            'wait_for': 1,
        }

    client_gdpr_delete_yes_confirm_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="gdprDeleteConfirmYes"]',
            'wait_for': 1,
        }

    client_mac_cell = \
        {
            'CSS_SELECTOR': '.open-client-entity',
            'wait_for': 15
        }

    client_dialog_window_close_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 1,
        }

    client_page_refresh_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="refresh"]',
            'CSS_SELECTOR': '.ui-icon.ui-fresh-icon',
            'wait_for': 5
        }

    client_health_status = \
        {
            'CSS_SELECTOR': '.status-ico',
            'wait_for': 5
        }

    client_page_size_100 = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottom"]/div/a[@data-size="100"]',
            'wait_for': 3
        }

    client360_os_type_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientOSType"]',
            'wait_for': 1,
        }

    client360_ip_address_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ip"]',
            'wait_for': 1,
        }

    client360_mac_address_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMac"]',
            'wait_for': 1,
        }

    client360_connected_ap_info_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientDeviceName"]',
            'wait_for': 1,
        }

    client360_vlan_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlan"]',
            'wait_for': 1,
        }

    client360_captive_web_portal_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cwpUsed"]',
            'wait_for': 1,
        }

    client360_user_profile_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userProfile"]',
            'wait_for': 1,
        }

    client360_user_name_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userName"]',
            'wait_for': 1,
        }

    client360_ssid_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssid"]',
            'wait_for': 1,
        }

    client360_radio_mac_protocol_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macProtocol"]',
            'wait_for': 1,
        }

    client360_radio_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="radioInfo"]',
            'wait_for': 1,
        }

    client360_channel_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="channel"]',
            'wait_for': 1,
        }
