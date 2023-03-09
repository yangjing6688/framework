class GlobalSearchWebElementsDefinitions:
    global_search_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="headerSearchIcon"]'
        }

    global_search_textbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="searchField" and @name="search"]',
            'wait_for': 20
        }

    global_search_result = \
        {
            'XPATH': '//*[@class="search-results"]//li',
            'wait_for': 20
        }

    system_info_button = \
        {
            'XPATH': "//*[@data-id='systeminfo']"
        }

    system_info_ap_name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceHostName']"
        }

    system_info_ap_serial_number =  \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceserialNumber']"
        }

    system_info_ap_mac = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mgmtMacAddress']"
        }

    close_dialog = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeDialog']"
        }
    application_name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='appName']"
        }
    application_category = \
        {
            'XPATH': "//*[@data-dojo-attach-point='appCategory']"
        }
    net_policy_sum_view = \
        {
            'XPATH': "//*[contains(@class,'ah-policy-entity hmOverride')]//*[@class='policy-entity']"
                     "//*[@data-dojo-attach-point='clientTitle']"
        }
    net_policy_ssid_title = \
        {
            'XPATH': "//*[@class='entity-type-title mb10']"
        }

    client_title = \
        {
            'XPATH': "//*[@data-dojo-attach-point='clientTitle']"
        }

    client_ip = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ip']"
        }

    client_mac = \
        {
            'XPATH': "//*[@data-dojo-attach-point='clientMac']"
        }

    system_info_ap_ip = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mgmtIpAddress']"
        }

    view_organizations_button = \
        {
            'XPATH': "//*[@class='msp-multi-org-display expanded']"
        }

    view_org_select = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mspSelectAll']"
        }

    view_org_close_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeBtn']"
        }

    tool_tip_close = \
        {
            'XPATH': '//*[@class="ui-tipbox ui-tipbox-warning"]//i[@class="ui-tipbox-close"]'
        }

    tool_tip_error_close = \
        {
            'XPATH': '//*[@class="ui-tipbox ui-tipbox-error"]//i[@class="ui-tipbox-close"]'
        }

    global_search_clear_icon = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clearSearchIcon"]',
            'index': 1
        }

    global_search_client_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameNode"]'
        }

