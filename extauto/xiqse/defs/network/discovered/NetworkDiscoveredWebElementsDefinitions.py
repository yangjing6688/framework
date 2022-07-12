

class NetworkDiscoveredWebElementsDefinitions:

    discovered_table = \
        {
            'DESC': 'Discovered Table',
            'XPATH': '//div[contains(@id, "discoveredDevicesGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            
        }

    displaying_rows_label = \
        {
            'DESC': 'Displaying # Rows label for the Discovered Table',
            'XPATH': '//label[contains(text(), "Displaying") and contains(text(), "rows")]',
            
        }

    discovered_table_rows = \
        {
            'DESC': 'Discovered Table Rows',
            'XPATH': '//div[contains(@id, "discoveredDevicesGrid")]//table[contains(@id, "gridview")]//tr',
            
        }

    discovered_table_ip_column_header = \
        {
            'DESC': 'Discovered Table IP Address Column Header',
            'XPATH': '//div[contains(@id, "discoveredDevicesGrid")]//span[@class="x-column-header-text-inner" and text()="IP Address"]',
            
        }

    discovered_table_serial_number_column_header = \
        {
            'DESC': 'Discovered Table Serial Number Column Header',
            'XPATH': '//div[contains(@id, "discoveredDevicesGrid")]//span[@class="x-column-header-text-inner" and text()="Serial Number"]',
            
        }

    show_in_groups_menu = \
        {
            'DESC': 'Show in Groups column menu on the Network> Discovered Tab',
            'XPATH': '//span[text()="Show in Groups"]/ancestor::a',
            
        }

    group_by_menu = \
        {
            'DESC': 'Group by This Field column menu on the Network> Discovered Tab',
            'XPATH': '//span[text()="Group by This Field"]/ancestor::a',
            
        }

    clear_button = \
        {
            'DESC': 'Clear button on the toolbar of the Network> Discovered Tab',
            'XPATH': '//span[text()="Clear"]/ancestor::a',
            
        }

    clear_all_button = \
        {
            'DESC': 'Clear All Devices button on the toolbar of the Network> Discovered Tab',
            'XPATH': '//span[text()="Clear All Devices"]/ancestor::a',
            
        }

    pre_register_button = \
        {
            'DESC': 'Pre-Register Device button on the toolbar of the Network> Discovered Tab',
            'XPATH': '//span[text()="Pre-Register Device..."]/ancestor::a',
            
        }

    load_config_button = \
        {
            'DESC': 'Load Configuration button on the toolbar of the Network> Discovered Tab',
            'XPATH': '//span[text()="Load Configuration..."]/ancestor::a',
            
        }

    add_devices_button = \
        {
            'DESC': 'Add Devices button on the toolbar of the Network> Discovered Tab',
            'XPATH': '//span[text()="Add Devices..."]/ancestor::a',
            
        }

    configure_devices_button = \
        {
            'DESC': 'Configure Devices button on the toolbar of the Network> Discovered Tab',
            # 'XPATH': '//span[text()="Configure Devices..."]/ancestor::a',
            'XPATH': '//span[@class="x-btn-inner x-btn-inner-default-toolbar-small"][text()="Configure Devices..."]',
            
        }

    clear_menu = \
        {
            'DESC': 'Clear menu option',
            'XPATH': '//span[contains(@class, "x-menu-item-text")][text()="Clear"]',
            
        }
    load_configuration_menu = \
        {
            'DESC': 'Load Configuration... menu option',
            'XPATH': '//span[contains(@class, "x-menu-item-text")][text()="Load Configuration..."]',
            
        }
    add_devices_menu = \
        {
            'DESC': 'Add Devices... menu option',
            'XPATH': '//span[contains(@class, "x-menu-item-text")][text()="Add Devices..."]',
            
        }

    configure_devices_menu = \
        {
            'DESC': 'Configure Devices... menu option',
            'XPATH': '//span[contains(@class, "x-menu-item-text")][text()="Configure Devices..."]',
            
        }

    discovered_column_by_name = \
        {
            'DESC': 'Column in the Discovered table specified by the element_name',
            'XPATH': '//div[contains(@id, "discoveredDevicesGrid")]//span[@class="x-column-header-text-inner" and text()="${element_name}"]',
            
        }

    discovered_column_value = \
        {
            'DESC': 'Column data/value in the Discovered table specified by the element_id',
            'CSS_SELECTOR': 'td[data-columnid="${element_id}"]',
            
        }
