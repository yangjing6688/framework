class ExtremeGuestUsersWebElementsDefs:
    extreme_guest_users_tab = \
        {
            'XPATH': '//span[text()="Users"]',
            'wait_for': 5
        }

    extreme_guest_users_add_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-users-add-menu")]',
            'wait_for': 5
        }

    extreme_guest_users_create_bulk_users_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-users-create-bulk-users-btn")]',
            'wait_for': 5
        }

    create_bulk_users_access_group_drop_down_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-users-bulkvoucher-usergroup-db")]//div[contains('
                     '@class, "x-form-arrow-trigger")]',
            'wait_for': 5
        }

    create_bulk_users_access_group_drop_down_options = \
        {
            'XPATH': '//li[@class="x-boundlist-item"]',
            'wait_for': 5
        }

    create_bulk_users_number_of_vouchers_textfield = \
        {
            'XPATH': '//input[contains(@name, "number")]',
            'wait_for': 5
        }

    create_bulk_users_location_drop_down_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-users-bulkvoucher-location-tree"]'
                     '//div[contains(@class, "x-form-arrow-trigger")]',
            'wait_for': 5
        }

    extreme_guest_users_locations_root_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_users_locations_city_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_users_locations_building_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_users_locations_floor_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-4")]/ancestor::tr',
            'wait_for': 5
        }

    extreme_guest_users_locations_root_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_users_locations_city_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_users_locations_building_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            'wait_for': 5
        }

    extreme_guest_users_create_bulk_users_close_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-popup-message"]//span[text()="Close"]',
            'wait_for': 5
        }

    extreme_guest_users_create_bulk_users_print_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-popup-message"]//span[text()="Print"]',
            'wait_for': 5
        }

    extreme_guest_users_create_bulk_users_create_button = \
        {
            'XPATH': '//span[text()="Create"]',
            'wait_for': 5
        }

    extreme_guest_users_create_bulk_users_clear_button = \
        {
            'XPATH': '//span[text()="Clear"]',
            'wait_for': 5
        }

    extreme_guest_users_grid_rows = \
        {
            'XPATH': '//tr[@class="  x-grid-row"]',
            'wait_for': 10
        }

    extreme_guest_users_grid_row_cells = \
        {
            'XPATH': '//span[@class="eguest-user-name" or @class="x-grid-checkcolumn"]',
            'wait_for': 5
        }

    extreme_guest_users_grid_row_cells_user_name_list = \
        {
            'XPATH': '//span[@class="eguest-user-name"]',
            'wait_for': 5
        }

    extreme_guest_users_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-users-delete-user-btn"]',
            'wait_for': 5
        }

    extreme_guest_users_delete_ok_button = \
        {
            'XPATH': '//span[text()="OK"]',
            'wait_for': 5
        }

    extreme_guest_users_delete_status_ok_button = \
        {
            'XPATH': '//span[text()="OK"]',
            'wait_for': 5
        }

    extreme_guest_users_print_user_cells = \
        {
            'XPATH': '//td[1]',
            'wait_for': 5
        }

    extreme_guest_users_print_password_cells = \
        {
            'XPATH': '//td[2]',
            'wait_for': 5
        }
