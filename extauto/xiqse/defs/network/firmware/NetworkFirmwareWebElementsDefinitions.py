

class NetworkFirmwareWebElementsDefinitions:

    firmware_type_node = \
        {
            'DESC': 'Firmware Type with name specified by element_name on the Firmware tab',
            'XPATH': '//div[contains(@class,"x-grid-cell-inner")]/span[contains(text(),"${element_name}")]',
            'wait_for': 10
        }

    firmware_refresh_button = \
        {
            'DESC': 'Selects the Refresh button for refreshing firmware images',
            'XPATH': '//span[contains(text(),"Refresh")]',
            'wait_for': 10
        }

    firmware_upload_button = \
        {
            'DESC': 'Selects the Upload Firmware button for uploading firmware images',
            'XPATH': '//span[contains(text(),"Upload")]',
            'wait_for': 10
        }

    firmware_refresh_load_mask = \
        {
            'DESC': 'Refreshing firmware icon',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Loading..."]',
            'wait_for': 10
        }

    search_open_button = \
        {
            'DESC': 'Button to open the Search field',
            'XPATH': '//div[contains(@id, "firmwareGrid")]//span[contains(@class, "x-form-search-trigger")]/ancestor::a',
            'wait_for': 10
        }

    search_text_field = \
        {
            'DESC': 'Search Text Field',
            'XPATH': '//div[contains(@id, "firmwareGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "inputWrap")]/input',
            'wait_for': 10
        }

    search_trigger_button = \
        {
            'DESC': 'Button to trigger the search',
            'XPATH': '//div[contains(@id, "firmwareGrid")]//div[contains(@id, "trigger-search")]',
            'wait_for': 10
        }

    search_clear_button = \
        {
            'DESC': 'Button to clear the search',
            'XPATH': '//div[contains(@id, "firmwareGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "trigger-clear")]',
            'wait_for': 10
        }

    firmware_table = \
        {
            'DESC': 'Firmware Table',
            'XPATH': '//div[contains(@id, "firmwareGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            'wait_for': 10
        }

    firmware_table_rows = \
        {
            'DESC': 'Firmware Table Rows',
            'XPATH': '//div[contains(@id, "firmwareGrid")]//table[contains(@id, "gridview")]//tr',
            'wait_for': 10
        }

    assign_firmware_menu_item = \
    {
        'DESC': 'The Assign Firmware menu item in the firmware context menu',
        'XPATH': '//span[contains(text(),"Assign Firmware")]',
        'wait_for': 10
    }

    remove_firmware_from_group_menu_item = \
        {
            'DESC': 'The Remove Firmware from Group menu item in firmware context menu',
            'XPATH': '//span[contains(text(),"Remove Firmware from Group")]',
            'wait_for': 10
        }

    set_as_reference_image_menu_item = \
        {
            'DESC': 'The Set As Reference Image menu item in firmware context menu',
            'XPATH': '//span[contains(text(),"Set as Reference Image")]',
            'wait_for': 10
        }

    unset_as_reference_image_menu_item = \
        {
            'DESC': 'The Unset as Reference Image menu item in firmware context menu',
            'XPATH': '//span[contains(text(),"Unset as Reference Image")]',
            'wait_for': 10
        }

    delete_image_menu_item = \
        {
            'DESC': 'The Delete Image menu item in firmware context menu',
            'XPATH': '//span[contains(text(),"Delete Image")]',
            'wait_for': 10
        }