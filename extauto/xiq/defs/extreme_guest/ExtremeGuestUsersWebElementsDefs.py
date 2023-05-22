class ExtremeGuestUsersWebElementsDefs:
    extreme_guest_users_tab = \
        {
            'XPATH': '//span[text()="Users"]',
        }

    extreme_guest_users_add_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-users-add-menu")]',
        }

    extreme_guest_users_create_bulk_users_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-users-create-bulk-users-btn")]',
        }

    create_bulk_users_access_group_drop_down_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-users-bulkvoucher-usergroup-db")]//div[contains('
                     '@class, "x-form-arrow-trigger")]',
        }

    create_bulk_users_access_group_drop_down_options = \
        {
            'XPATH': '//li[@class="x-boundlist-item"]',
        }

    create_bulk_users_number_of_vouchers_textfield = \
        {
            'XPATH': '//input[contains(@name, "number")]',
        }

    create_bulk_users_location_drop_down_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-users-bulkvoucher-location-tree"]'
                     '//div[contains(@class, "x-form-arrow-trigger")]',
        }

    extreme_guest_users_locations_root_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]/ancestor::tr',
        }

    extreme_guest_users_locations_city_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]/ancestor::tr',
        }

    extreme_guest_users_locations_building_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]/ancestor::tr',
        }

    extreme_guest_users_locations_floor_name = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-4")]/ancestor::tr',
        }

    extreme_guest_users_locations_root_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-1")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
        }

    extreme_guest_users_locations_city_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-2")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
        }

    extreme_guest_users_locations_building_name_expand_button = \
        {
            'XPATH': '//*[contains(@data-automation-tag, "eguest-tree-node-3")]'
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
        }

    extreme_guest_users_create_bulk_users_close_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-popup-message"]//span[text()="Close"]',
        }

    extreme_guest_users_create_bulk_users_print_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-popup-message"]//span[text()="Print"]',
        }

    extreme_guest_users_create_bulk_users_create_button = \
        {
            'XPATH': '//span[text()="Create"]',
        }

    extreme_guest_users_create_bulk_users_clear_button = \
        {
            'XPATH': '//span[text()="Clear"]',
        }

    extreme_guest_users_grid_rows = \
        {
            'XPATH': '//div[contains(@data-automation-tag,"eguest-users-grid")]//td/..',
            
        }

    extreme_facebook_guest_users = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-key-metrics-facebook-btn")]//span[@class="eguest-metrics-text count eguest-facebook-count"]',
        }

    extreme_linkedin_guest_users = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-key-metrics-linkedin-btn")]//span[@class="eguest-metrics-text count eguest-linkedin-count"]',
        }

    extreme_guest_users_grid_row_cells = \
        {
            'XPATH': '//td[contains(@class,"x-grid-cell-gridcolumn")]',
        }

    extreme_guest_users_grid_row_cells_user_name_list = \
        {
            'XPATH': '//span[@class="eguest-user-name"]',
        }

    extreme_guest_users_select_button = \
        {
            'XPATH': '(//div[contains(@class, "x-column-header-inner x-leaf-column-header x-column-header-inner-empty")])[3]',
        }

    extreme_guest_users_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="eguest-users-delete-user-btn"]',
        }

    extreme_guest_users_delete_ok_button = \
        {
            'XPATH': '(//div[@data-automation-tag="eguest-popup-message"]//span[text()="OK"])[1]',
        }

    extreme_guest_users_delete_ok_button_duplicate = \
        {
            'XPATH': '(//div[@data-automation-tag="eguest-popup-message"]//span[text()="OK"])[2]',
        }

    extreme_guest_users_delete_status_ok_button = \
        {
            'XPATH': '//span[text()="OK"]',
        }

    extreme_guest_users_print_user_cells = \
        {
            'XPATH': '//td[1]',
        }

    extreme_guest_users_print_password_cells = \
        {
            'XPATH': '//td[2]',
        }
