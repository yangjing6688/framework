

class CommonOperationsPanelWebElementsDefinitions:

    operations_button = \
        {
            'DESC': 'Operations Button',
            'XPATH': '//a[contains(@class, "operationStatusBtn")]',
            
        }

    operations_table_group_rows = \
        {
            'DESC': 'Group Table Rows in the Operations Panel',
            'XPATH': '//div[contains(@id, "operationStatusGrid")]//table//tr/td[@class="x-group-hd-container"]/..',
            
        }

    operations_table_group_data_rows = \
        {
            'DESC': 'Group Data Table Rows in the Operations Panel',
            'XPATH': '//div[contains(@id, "operationStatusGrid")]//table//tr[contains(@class, "x-grid-row")]',
            
        }

    operations_table_group_row = \
        {
            # Need to use the substring method since ends-with only works with xpath 2.0, and CSS selector doesn't
            # allow to get the parent of an element.  This xpath will get the matching group which ends with the
            # specified value.  This is to handle the case where the desired value is a substring of another value;
            # for example, "Discover Site" vs "Discover Site Actions" - in this case, two matches will be found unless
            # we perform the "ends-with".
            # Also need to use "normalize-space" since some operations (e.g., Device Added) end with an extra space.
            'DESC': 'Group table row for the specified element_id group in the Operations panel',
            'XPATH': '//div[substring(normalize-space(@data-groupname), ' +
                     'string-length(normalize-space(@data-groupname)) - string-length("${element_id}") +1) = ' +
                     '"${element_id}"]/ancestor::tr',
            
        }

    operations_table_group_data_row = \
        {
            'DESC': 'Table row for the specified element_id of the expanded group in the Operations panel',
            'XPATH': '//div[contains(@class, "x-grid-cell-inner") and text()="${element_id}"]/ancestor::tr',
            
        }

    operations_table_data_row_progress = \
        {
            'DESC': 'Progress for the Data Row in the Operations Panel',
            'CSS_SELECTOR': '.x-progress-bar .x-progress-text',
            
        }

    operations_table_data_row_cells = \
        {
            'DESC': 'Cells for the Data Row in the Operations Panel',
            'CSS_SELECTOR': '.x-grid-cell[data-qtip]',
            
        }

    clear_all_menu = \
        {
            'DESC': 'Clear All menu when right clicking a row in the Operations Panel',
            'XPATH': '//span[text()="Clear All"]/ancestor::a[@class="x-menu-item-link"]',
            'wait_for': 5
        }
