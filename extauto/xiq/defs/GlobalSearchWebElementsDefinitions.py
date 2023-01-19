class GlobalSearchWebElementsDefinitions:
    global_search_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="headerSearchIcon"]',
            'wait_for': 3
        }

    global_search_textbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="searchField" and @name="search"]',
            'wait_for': 3
        }

    global_search_result = \
        {
            'XPATH': '//*[@class="search-results"]//li',
            'wait_for': 5
        }

    system_info_button = \
        {
            'XPATH': "//*[@data-id='systeminfo']",
            'wait_for': 5
        }

    system_info_ap_name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceHostName']",
            'wait_for': 5
        }

    system_info_ap_serial_number =  \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceserialNumber']",
            'wait_for': 5
        }

    system_info_ap_mac = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mgmtMacAddress']",
            'wait_for': 5
        }

    close_dialog = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeDialog']",
            'wait_for': 5
        }
    application_name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='appName']",
            'wait_for': 5
        }
    application_category = \
        {
            'XPATH': "//*[@data-dojo-attach-point='appCategory']",
            'wait_for': 5
        }
    net_policy_sum_view = \
        {
            'XPATH': "//*[@data-dojo-attach-point='clientTitle']",
            'wait_for': 5
        }
    net_policy_ssid_title = \
        {
            'XPATH': "//*[@class='entity-type-title mb10']",
            'wait_for': 5
        }

    client_title = \
        {
            'XPATH': "//*[@data-dojo-attach-point='clientTitle']",
            'wait_for': 5
        }

    client_ip = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ip']",
            'wait_for': 5
        }

    client_mac = \
        {
            'XPATH': "//*[@data-dojo-attach-point='clientMac']",
            'wait_for': 5
        }

    system_info_ap_ip = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mgmtIpAddress']",
            'wait_for': 5
        }

    view_organizations_button = \
        {
            'XPATH': "//*[@class='msp-multi-org-display expanded']",
            'wait_for': 5
        }

    view_org_select = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mspSelectAll']",
            'wait_for': 5
        }

    view_org_close_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeBtn']",
            'wait_for': 5
        }

    tool_tip_close = \
        {
            'XPATH': '//*[@class="ui-tipbox ui-tipbox-warning"]//i[@class="ui-tipbox-close"]',
            'wait_for': 5
        }

    tool_tip_error_close = \
        {
            'XPATH': '//*[@class="ui-tipbox ui-tipbox-error"]//i[@class="ui-tipbox-close"]',
            'wait_for': 5
        }