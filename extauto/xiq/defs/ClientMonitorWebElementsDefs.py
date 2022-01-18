class ClientMonitorWebElementsDefs:

    client_monitor_tab = \
        {
            'XPATH': '//div//td[@data-automation-tag="automation-tools-controller-issue-list-link"]',
            'wait_for': 5
        }

    auth_issue_counts_status_card = \
        {
            'XPATH': '//div[@data-dojo-attach-point="issueCountAuthentication"]',
            'wait_for': 5
        }

    issue_type_drop_down = \
        {
            'XPATH': '//div[@class="troubleshoot-issue-list-grid-header"]//div[contains(@class, "issue-type-menu")]',
            'wait_for': 5,
            'index': 0
        }

    issue_type_drop_down_options = \
        {
            'XPATH': '//div[@class="troubleshoot-issue-list-grid-header"]'
                     '//div[contains(@class, "issue-type-menu")]//ul//a',
            'wait_for': 5
        }

    issue_status_drop_down = \
        {
            'XPATH': '//div[@class="troubleshoot-issue-list-grid-header"]//div[contains(@class, "issue-type-menu")]',
            'wait_for': 5,
            'index': 1
        }

    issue_status_drop_down_options = \
        {
            'XPATH': '//div[@class="troubleshoot-issue-list-grid-header"]'
                     '//div[contains(@class, "issue-type-menu")]//ul//a',
            'wait_for': 5
        }

    troubleshoot_issue_aggregate_icon = \
        {
            'CSS_SELECTOR': '.troubleshoot-issue-list-icon-plus',
            'wait_for': 5
        }

    client_issue_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="treeListGrid"]//table//tr',
            'wait_for': 5
        }

    client_issue_grid_row_cell = \
        {
            'CSS_SELECTOR': '.dojoxGridCell',
            'wait_for': 5
        }
