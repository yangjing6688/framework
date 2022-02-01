class NetworkManagementOptionsDefinitions:
    delete_network_management_options_entry = \
        {
            'XPATH': '//span[@class="table-action-icons table-remove"]',
            'index': 1,
            'wait_for': 5
        }

    add_network_management_options_entry = \
        {
            'XPATH': '//span[@class="table-action-icons table-add"]',
            'index': 1,
            'wait_for': 5
        }

    network_management_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]',
            'wait_for': 10
        }

    network_management_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 5
        }

    new_management_option_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    legacy_http_redirect = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableLegacyHttpRedirect"]',
            'wait_for': 5
        }

    cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    confirm_yes = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    confirm_no = \
        {
            'XPATH': '//button[@data-dojo-attach-point="noBtn"]',
            'wait_for': 5
        }
