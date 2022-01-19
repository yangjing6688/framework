class AdditionalSettingsEebElememtsDefs:
    ntp_server_classification_rule_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ntpServer"]//div[@data-dojo-attach-point="classificationCtn"]'
                     '//div[@data-dojo-attach-point="gridContent"]//table[@class="dojoxGridRowTable"]',
            'wait_for': 5
        }

    ntp_server_classification_rule_grid_row_cells = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ntpServer"]//div[@data-dojo-attach-point="classificationCtn"]'
                     '//div[@data-dojo-attach-point="gridContent"]//table[@class="dojoxGridRowTable"]'
                     '//td[@class="dojoxGridCell"]',
            'wait_for': 5
        }

    nw_policy_additional_settings_tab = \
        {
            'XPATH': '//li[@data-automation-tag="automation-tab-additional-settings"]',
            'wait_for': 5
        }

    nw_policy_additional_settings_ntp_server_tab = \
        {
            'XPATH': '//li[@data-automation-tag="automation-sider-list-NTPServer"]',
            'wait_for': 5
        }