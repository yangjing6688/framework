class DeviceCommonDefs:
    device_grid_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]//div[contains(@class, "dgrid-row")]',
            'wait_for': 5,
        }

    device_row_select_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'wait_for': 5
        }

    device_row_select_check_box_status = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-0 w30 dgrid-selector"]/input',
            'wait_for': 5
        }

    device_table_edit_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-device-list-bulkEdit-btn"]',
            'wait_for': 5,
        }

    device_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    device360_cells_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 15
        }

    manage_devices_select_all_devices_checkbox = \
        {
            'XPATH': '//*[@class="dgrid-resize-header-container"]//input[@type="checkbox"]',
            'index': 0,
            'wait_for': 5
        }

    devices_per_page_value = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[@data-size="${element_id}"]',
            'wait_for': 5
        }

    devices_per_page_current = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridBottomLeft"]//a[contains(@class,"ui-page-size-cur")]',
            'wait_for': 5
        }
