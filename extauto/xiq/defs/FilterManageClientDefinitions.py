class FilterManageClientDefinitions:
    filter_client_device_list = \
        location_filter_link = \
        {
            'XPATH': '//div[contains(@id,"dgrid_")]/table/tr/td[19]',
            'wait_for': 5
        }

    filter_client_os_type_list = \
        {
            'XPATH': '//div[contains(@id,"dgrid_")]/table/tr/td[12]',
            'wait_for': 5
        }

    filter_client_connection_list = \
        {
            'XPATH': '//div[contains(@id,"dgrid_")]/table/tr/td[2]',
            'wait_for': 5
        }

    filter_client_ssid_list = \
        {
            'XPATH': '//div[contains(@id,"dgrid_")]/table/tr/td[14]',
            'wait_for': 5
        }

    filter_client_device_function_link = \
        {
            'XPATH': '//span[@data-dojo-attach-point="titleNode" and contains(text(),"Device Function")]',
            'wait_for': 5
        }

    filter_client_device_function_all_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_FUNCTIONS"]',
            'wait_for': 5
        }

    filter_client_device_function_ap_chkbox = \
        {
            'XPATH': '//input[@data-name="Access Point"]',
            'wait_for': 5
        }

    filter_client_device_function_sw_chkbox = \
        {
            'XPATH': '//input[@data-name="Switch"]',
            'wait_for': 5
        }

    list_page_size_100_link = \
        {
            'XPATH': '//a[contains(text(),"100")]',
            'wait_for': 3
        }

    filter_client_device_connection_link = \
        {
            'XPATH': '//span[@data-dojo-attach-point="titleNode" and contains(text(),"Client Connection Types")]',
            'wait_for': 5
        }

    filter_client_device_connection_all_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_CLIENT_CONNECTION_TYPES"]',
            'wait_for': 5
        }

    filter_client_device_wireless_connection_chkbox = \
        {
            'XPATH': '//input[@data-name="Wireless"]',
            'wait_for': 5
        }

    filter_client_device_wired_connection_chkbox = \
        {
            'XPATH': '//input[@data-name="Wired"]',
            'wait_for': 5
        }

    filter_client_os_type_link = \
        {
            'XPATH': '//span[@data-dojo-attach-point="titleNode" and contains(text(),"OS Types")]',
            'wait_for': 5
        }

    filter_client_windows_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="Windows"]',
            'wait_for': 5
        }

    filter_client_windows_phone_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="Windows Phone"]',
            'wait_for': 5
        }

    filter_client_mac_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="Mac OS"]',
            'wait_for': 5
        }

    filter_client_ipad_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="iPad"]',
            'wait_for': 5
        }

    filter_client_iphone_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="iPhone"]',
            'wait_for': 5
        }

    filter_client_android_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="Android"]',
            'wait_for': 5
        }

    filter_client_chrome_os_type_chkbox = \
        {
            'XPATH': '//input[@data-name="Chrome"]',
            'wait_for': 5
        }

    filter_client_ssid_filter_link = \
        {
            'XPATH': '//span[contains(text(),"SSIDs") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    filter_client_ssid_filter_chkbox = \
        {
            'XPATH': '//input[@data-name=',
            'wait_for': 5
        }

    filter_client_application_table_list = \
        {
            'XPATH': '//div[contains(@id,"dojox_grid__View")]//div/table/tbody/tr',
            'wait_for': 5
        }