class ExtremeGuestReportsWebElementsDefs:
    extreme_guest_manage_reports_tab = \
        {
            'XPATH': '//span[text()="Manage Reports"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-add-btn"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_name_field = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-reportname-txt"]//input',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_type_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-reporttype-list"]//input',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_type_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-scope-tree"]//input',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_root_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_city_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_building_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_floor_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-4")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_root_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_city_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_scope_building_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_period_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-period-list"]//input',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_period_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_format_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-format-list"]//input',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_format_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_dashboard_name_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-dashboardname-list"]//input',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_dashboard_name_dropdown_items = \
        {
            'CSS_SELECTOR': '.x-boundlist-item',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_save_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-save-btn"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_run_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-run-btn"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_save_run_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-savenrun-btn"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_cancel_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-createreport-cancel-btn"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_add_report_ok_button = \
        {
            'XPATH': '//span[text()="OK"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-managereports-delete-btn"]',
            'wait_for': 5
        }

    extreme_guest_manage_reports_grid_rows = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]',
            
        }

    extreme_guest_manage_reports_grid_row_cells = \
        {
            'XPATH': '//span[@class="reports" or @class="x-grid-checkcolumn"]',
            'wait_for': 5
        }

    extreme_guest_generated_reports_tab = \
        {
            'XPATH': '//span[text()="Generated Reports"]',
            'wait_for': 5
        }

    extreme_guest_generated_reports_grid_rows = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]',
            
        }

    extreme_guest_generated_reports_grid_row_cells = \
        {
            'XPATH': '//*[@class="eguest-report" or @class="x-grid-checkcolumn"]',
            'wait_for': 5
        }

    extreme_guest_generated_reports_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-generatedreports-delete-btn"]',
            'wait_for': 5
        }