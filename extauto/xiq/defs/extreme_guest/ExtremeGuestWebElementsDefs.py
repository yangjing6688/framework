class ExtremeGuestWebElementsDefs:
    extreme_guest_subscription_page = \
        {
            'XPATH': '//div[contains(@class, "subscribe-flow")]',
            'wait_for': 5
        }

    extreme_guest_subscription_page_subscribe_button = \
        {
            'XPATH': '//span[text()="Enable"]',
            'wait_for': 5
        }

    extreme_guest_subscription_page_help_information = \
        {
            'XPATH': '//div[contains(@class, "ui-tipbox-success")]',
            'wait_for': 5
        }

    extreme_guest_subscription_page_open_ssid_checkbox = \
        {
            'XPATH': '//div[contains(@class, "choose-guest-policies-view")]//*[contains(@class, "dgrid-column-0")]',
            'wait_for': 5
        }

    extreme_guest_subscription_page_open_ssid_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 10
        }

    extreme_guest_subscription_page_open_ssid_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 2
        }

    extreme_guest_subscription_page_apply_button = \
        {
            'XPATH': '//button[text()="Apply"]',
            'wait_for': 5
        }

    extreme_guest_more_insights_tab = \
        {
            'XPATH': '//button[contains(@aria-label, "More Insights")]',
            'wait_for': 5
        }

    extreme_guest_monitor_page = \
        {
            'XPATH': '//div[contains(@class, "x-treelist-toolstrip")]//div[contains(@class, "dashboardIconCls")]',
            'wait_for': 5
        }

    extreme_guest_configure_page = \
        {
            'XPATH': '//div[contains(@class, "x-treelist-toolstrip")]//div[contains(@class, "settingIconCls")]',
            'wait_for': 5
        }

    extreme_guest_analyze_page = \
        {
            'XPATH': '//div[contains(@class, "x-treelist-toolstrip")]//div[contains(@class, "wirelessDevicesIconCls")]',
            'wait_for': 5
        }

    extreme_guest_configure_splash_template_tab = \
        {
            'XPATH': '//span[text()="Splash Templates"]',
            'wait_for': 5
        }

    extreme_guest_configure_users_tab = \
        {
            'XPATH': '//span[text()="Users" and contains(@class, "x-tree-node-text ")]',
            'wait_for': 5
        }

    extreme_guest_monitor_dashboard_tab = \
        {
            'XPATH': '//span[text()="Dashboard"]',
            'wait_for': 5
        }
