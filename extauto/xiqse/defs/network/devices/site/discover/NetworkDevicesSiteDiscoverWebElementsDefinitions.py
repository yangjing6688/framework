

class NetworkDevicesSiteDiscoverWebElementsDefinitions:

    address_add_button = \
        {
            'DESC': 'Address Add Button',
            'XPATH': '//div[contains(@id, "deviceDiscoverPanel")]//span[contains(@class, "x-btn-inner-default-toolbar-small") and text()="Add"]/ancestor::a',
            
        }

    address_edit_button = \
        {
            'DESC': 'Address Edit Button',
            'XPATH': '//div[contains(@id, "deviceDiscoverPanel")]//span[contains(@class, "x-btn-inner-default-toolbar-small") and text()="Edit"]/ancestor::a',
            
        }

    address_delete_button = \
        {
            'DESC': 'Address Delete Button',
            'XPATH': '//div[contains(@id, "deviceDiscoverPanel")]//span[contains(@class, "x-btn-inner-default-toolbar-small") and text()="Delete"]/ancestor::a',
            
        }

    addresses_panel_table = \
        {
            'DESC': 'Table in the Addresses Panel on the Discover tab',
            'XPATH': '//div[contains(@class, "x-title-text") and text()="Addresses"]//ancestor::div[contains(@class, "x-grid")]//div[contains(@class, "x-grid-item-container")]',
            
        }

    addresses_table_rows = \
        {
            'DESC': 'Rows in the Addresses Panel table on the Discover tab',
            'XPATH': '//div[contains(@class, "x-title-text") and text()="Addresses"]//ancestor::div[contains(@class, "x-grid")]//div[contains(@class, "x-grid-item-container")]//tr',
            
        }

    profiles_panel_table = \
        {
            'DESC': 'Table in the Profiles Panel on the Discover tab',
            'XPATH': '//div[contains(@class, "x-title-text") and text()="Profiles"]//ancestor::div[contains(@class, "x-grid")]//div[contains(@class, "x-grid-item-container")]',
            
        }

    profiles_table_rows = \
        {
            'DESC': 'Rows in the Profiles Panel table on the Discover tab',
            'XPATH': '//div[contains(@class, "x-title-text") and text()="Profiles"]//ancestor::div[contains(@class, "x-grid")]//div[contains(@class, "x-grid-item-container")]//tr',
            
        }

    profiles_table_selected_accept_check_buttons = \
        {
            'DESC': 'Profiles Table Selected Accept Check Buttons',
            'CSS_SELECTOR': '.x-grid-cell-acceptColumn .x-grid-checkcolumn-checked',
            
        }

    profiles_table_selected_reject_check_buttons = \
        {
            'DESC': 'Profiles Table Selected Reject Check Buttons',
            'CSS_SELECTOR': '.x-grid-cell-rejectColumn .x-grid-checkcolumn-checked',
            
        }

    profiles_table_accept_cell = \
        {
            'DESC': 'Profiles Table Accept Cell',
            'CSS_SELECTOR': '.x-grid-cell-acceptColumn',
            
        }

    profiles_table_accept_cell_checked = \
        {
            'DESC': 'Profiles Table Accept Cell Checked',
            'CSS_SELECTOR': '.x-grid-cell-acceptColumn .x-grid-checkcolumn-checked',
            
        }

    profiles_table_reject_cell = \
        {
            'DESC': 'Profiles Table Reject Cell',
            'CSS_SELECTOR': '.x-grid-cell-rejectColumn',
            
        }

    profiles_table_reject_cell_checked = \
        {
            'DESC': 'Profiles Table Reject Cell Checked',
            'CSS_SELECTOR': '.x-grid-cell-rejectColumn .x-grid-checkcolumn-checked',
            
        }
