

class CommonTableWebElementsDefinitions:

    table_column_header_menu = \
        {
            'DESC': 'Table Header Column Menu',
            'XPATH': '//div[@class="x-column-header-trigger"]',
            
        }

    table_column_selection_menu = \
        {
            'DESC': 'Table Header Column Selection Menu',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Columns"]',
            
        }

    table_sort_ascending_menu = \
        {
            'DESC': 'Sort Ascending column selection menu',
            'XPATH': '//span[text()="Sort Ascending"]/ancestor::a',
            
        }

    table_sort_descending_menu = \
        {
            'DESC': 'Sort Descending column selection menu ',
            'XPATH': '//span[text()="Sort Descending"]/ancestor::a',
            
        }

    table_column_selection_menu_item = \
        {
            'DESC': 'Table Header Column Selection Menu Item, as specified by element_name',
            'XPATH': '//a[@role="menuitemcheckbox"]/span[text()="${element_name}"]/..',
            
        }

    table_column_filters_toolbar_button = \
        {
            'DESC': 'Toolbar button to display the Column Filters dialog',
            'XPATH': '//a[contains(@data-qtip, "Column Filters")]',
            
        }

    table_refresh_button = \
        {
            'DESC': 'Refresh Table Button',
            'XPATH': '//span[contains(@class, "x-tbar-loading")]',
            
        }

    table_reset_button = \
        {
            'DESC': 'Reset Table Button',
            'XPATH': '//span[text()="Reset"]/ancestor::a',
            
        }
