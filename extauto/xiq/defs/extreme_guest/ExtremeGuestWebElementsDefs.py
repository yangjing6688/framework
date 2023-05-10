class ExtremeGuestWebElementsDefs:
    extreme_guest_subscription_page = \
        {
            'XPATH': '//div[contains(@class, "subscribe-flow")]',
        }

    extreme_guest_subscription_page_subscribe_button = \
        {
            'XPATH': '//span[text()="Enable"]',
        }

    extreme_guest_subscription_page_help_information = \
        {
            'XPATH': '//div[contains(@class, "ui-tipbox-success")]',
        }

    extreme_guest_subscription_page_open_ssid_checkbox = \
        {
            'XPATH': '//div[contains(@class, "choose-guest-policies-view")]//*[contains(@class, "dgrid-column-0")]',
        }

    extreme_guest_subscription_page_open_ssid_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            
        }

    extreme_guest_subscription_page_open_ssid_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
        }

    extreme_guest_subscription_page_apply_button = \
        {
            'XPATH': '//button[text()="Apply"]',
        }

    extreme_guest_more_insights_tab = \
        {
            'XPATH': '//button[contains(@aria-label, "More Insights")]',
        }

    extreme_guest_monitor_page = \
        {
            'XPATH': '//div[contains(@class, "x-treelist-toolstrip")]//div[contains(@class, "dashboardIconCls")]',
        }

    extreme_guest_configure_page = \
        {
            'XPATH': '//div[contains(@class, "x-treelist-toolstrip")]//div[contains(@class, "settingIconCls")]',
        }

    extreme_guest_analyze_page = \
        {
            'XPATH': '//div[contains(@class, "x-treelist-toolstrip")]//div[contains(@class, "wirelessDevicesIconCls")]',
        }

    extreme_guest_configure_splash_template_tab = \
        {
            'XPATH': '//span[text()="Splash Templates"]',
        }


    extreme_guest_configure_preview_button = \
        {
            'XPATH': '(//div[contains(@class, "eguest-preview-button")])[1]',
        }

    extreme_guest_configure_users_tab = \
        {
            'XPATH': '//span[text()="Users" and contains(@class, "x-tree-node-text ")]',
        }

    extreme_guest_monitor_dashboard_tab = \
        {
            'XPATH': '//span[text()="Dashboard"]',
        }
