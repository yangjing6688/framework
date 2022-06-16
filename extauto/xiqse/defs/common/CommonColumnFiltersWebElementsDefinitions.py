

class CommonColumnFiltersWebElementsDefinitions:

    column_filters_dialog = \
        {
            'DESC': 'Column Filters Dialog',
            'XPATH': '//div[contains(@id, "showFiltersWindow")]',
            
        }

    column_filters_dialog_add_filter_dropdown_trigger = \
        {
            'DESC': 'Add Filter dropdown trigger arrow in the Column Filters dialog',
            'XPATH': '//div[contains(@id, "showFiltersWindow")]//div[contains(@id, "trigger-picker")]',
            
        }

    column_filters_dialog_add_filter_dropdown = \
        {
            'DESC': 'Add Filter dropdown field in the Column Filters dialog',
            'XPATH': '//div[contains(@id, "showFiltersWindow")]//div[contains(@class, "x-toolbar-item")]//input',
            
        }

    column_filters_dialog_filter_panel = \
        {
            'DESC': 'Filter panel for the filter specified by element_name',
            'XPATH': '//div[contains(@class, "x-title")]//div[text()="${element_name}"]',
            
        }

    column_filters_dialog_filter_text_field = \
        {
            'DESC': 'Text field for the filter specified by element_name',
            'XPATH': '//input[@placeholder="Enter ${element_name}..."]',
            
        }

    column_filters_dialog_filter_radio_field = \
        {
            'DESC': 'Radio button with label element_value for the filter specified by element_name',
            'XPATH': '//div[contains(@class, "x-title")]//div[text()="${element_name}"]' +
                     '//ancestor::div[contains(@class, "x-panel-bordered-panel")]//label[text()="${element_value}"]',
            
        }

    column_filters_dialog_filter_checkbox_field = \
        {
            'DESC': 'checkbox with label element_value for the filter specified by element_name',
            'XPATH': '//div[contains(@class, "x-title")]//div[text()="${element_name}"]' +
                     '//ancestor::div[contains(@class, "x-panel-bordered-panel")]//label[text()="${element_value}"]',
            
        }

    column_filters_dialog_remove_filter_button = \
        {
            'DESC': 'Remove Filter button for the filter specified by element_name in the Column Filters dialog',
            'XPATH': '//div[text()="${element_name}"]/ancestor::div[@class="x-box-target"]/div[@data-qtip="Remove Filter"]',
            
        }

    column_filters_dialog_close_button = \
        {
            'DESC': 'Close button in the Column Filters dialog',
            'XPATH': '//div[contains(@id, "showFiltersWindow")]//span[text()="Close"]/ancestor::a',
            
        }
