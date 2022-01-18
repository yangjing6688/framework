class A3InventoryWebElementsDefs:

    a3_devices_page_grid_rows = \
        {
            'XPATH':'//*[@class="el-table__fixed-body-wrapper"]//tr[contains(@class, "el-table__row")]',
            'wait_for': 10
         }

    a3_devices_page_refresh_button = \
        {
            'CSS_SELECTOR': '.ah-icon-refresh',
            'XPATH': '//*[@class="ah-icon-refresh"]',
            'wait_for': 2
         }

    devices_a3_status_green = \
        {
            'CSS_SELECTOR': '.ah-icon-status',
            'wait_for': 1
         }

    a3_device_row_cells = \
        {
            'CSS_SELECTOR': '.cell',
            'wait_for': 15
        }

    a3_device_expanded_status = \
        {
            'XPATH': '//*[@class="el-table__row hover-row a-row-expand expanded"]'
                     '//div[@class="el-table__expand-icon el-table__expand-icon--expanded"]',
            'wait_for': 5
        }

    a3_device_expanded_button = \
        {
            'CSS_SELECTOR': '.el-icon.el-icon-arrow-right',
            'wait_for': 10
        }

    a3_device_host_name_cell = \
        {
            'CSS_SELECTOR': '.i-hostname',
            'wait_for': 10,
        }

    a3_nodes_grid_rows_div = \
        {
            'XPATH': '//div[@class="el-table__fixed-body-wrapper"]',
            'wait_for': 10
         }

    a3_nodes__grid_rows = \
        {
            'XPATH': '//*[@class="el-table__fixed-body-wrapper"]//tr[contains(@class, "a-row-unexpand")]',
            'wait_for': 10
         }

    a3_node_go_to_a3_button = \
        {
            'XPATH': '//*[@class="el-table__fixed-body-wrapper"]//tr[contains(@class, "a-row-unexpand")]'
                     '//i[@class="ah-icon-login el-tooltip"]',
            'wait_for': 10
        }

    go_to_a3_button = \
        {
            'CSS_SELECTOR': '.ah-icon-login',
            'wait_for': 10
        }

    a3_login_username_field = \
        {
            'ID': 'username',
            'wait_for': 5,
        }

    a3_login_password_field = \
        {
            'ID': 'password',
            'wait_for': 5,
        }

    a3_login_button = \
        {
            'CSS_SELECTOR': '.btn.btn-primary',
            'wait_for': 10,
        }

    a3_unlink_page_text = \
        {
            'XPATH': '//div[@class="div-container"]//h3',
            'wait_for': 10
         }
