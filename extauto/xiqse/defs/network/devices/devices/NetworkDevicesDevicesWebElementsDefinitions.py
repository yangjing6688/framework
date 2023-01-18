

class NetworkDevicesDevicesWebElementsDefinitions:

    devices_table = \
        {
            'DESC': 'Devices Table',
            'XPATH': '//div[contains(@id, "deviceGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            
        }

    devices_table_rows = \
        {
            'DESC': 'Devices Table Rows',
            'XPATH': '//div[contains(@id, "deviceGrid")]//table[contains(@id, "gridview")]//tr',
            
        }

    devices_table_status_column_header = \
        {
            'DESC': 'Devices Table Status Column Header',
            'XPATH': '//div[contains(@id, "deviceGrid")]//span[@class="x-column-header-text-inner" and text()="Status"]',
            
        }

    devices_table_status_cell = \
        {
            'DESC': 'Devices Table Row Status Cell',
            'CSS_SELECTOR': '[data-qtip^="Device Status"]',
            
        }

    devices_table_column_by_name = \
        {
            'DESC': 'Devices Table Column with the Specified Name',
            'XPATH': '//div[contains(@id, "deviceGrid")]//span[contains(@id, "gridcolumn") and text()="${element_name}"]',
            
        }

    devices_table_column_value = \
        {
            'DESC': 'Devices Table Column Value',
            'CSS_SELECTOR': 'td[data-columnid="${element_id}"]',
            
        }

    devices_table_row_by_index = \
        {
            'DESC': 'Devices Table Row at the Specified Index',
            'XPATH': '//div[contains(@id, "deviceGrid")]//table[@data-recordindex="${element_index}"]//tr',
            
        }

    device_menu_tb_button = \
        {
            'DESC': 'Device Menu Toolbar Button',
            'XPATH': '//div[contains(@id, "deviceGrid")]//a[contains(@class, "x-btn-default-toolbar-small")]//span[contains(@class, "fa fa-bars")]',
            
        }

    add_device_tb_button = \
        {
            'DESC': 'Add Device Toolbar Button',
            'XPATH': '//a[contains(@class, "x-btn-default-toolbar-small")]//span[text()="Add Device..."]',
            
        }

    more_actions_menu_item = \
        {
            'DESC': 'More Actions Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="More Actions"]',
            
        }

    delete_device_menu_item = \
        {
            'DESC': 'Delete Device Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Delete Device"]',
            
        }

    rediscover_device_menu_item = \
        {
            'DESC': 'Restart Device Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Rediscover"]',

        }

    rediscover_device_confirmation_item = \
        {
            'DESC': 'Refresh (Rediscover)',
            'XPATH': '//a[@role="button"]//span[text()="Yes"]',
        }

    restart_device_menu_item = \
        {
            'DESC':  'Restart Device Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Restart Device..."]',
            
        }

    set_device_profile_menu_item = \
        {
            'DESC': 'Set Device Profile Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Set Device Profile..."]',
            
        }

    configure_menu_item = \
        {
            'DESC': 'Configure Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Configure..."]',
            
        }

    upgrade_firmware_menu_item = \
        {
            'DESC': 'Upgrade Firmware Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Upgrade Firmware..."]',
            
        }

    table_displaying_label = \
        {
            'DESC': 'Set Device Profile Dialog Cancel Button',
            'XPATH': '//div[contains(@class, "x-toolbar-text") and contains(text(), "Displaying")]',
            
        }

    archives_menu_item = \
        {
            'DESC': 'Archives Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Archives"]',
            
        }

    backup_configuration_menu_item = \
        {
            'DESC': 'Backup Configuration Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Backup Configuration"]',
            
        }

    restore_configuration_menu_item = \
        {
            'DESC': 'Restore Configuration Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Restore Configuration..."]',
            
        }

    register_trap_receiver_menu_item = \
        {
            'DESC': 'Register Trap Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Register Trap Receiver"]',
            
        }

    unregister_trap_receiver_menu_item = \
        {
            'DESC': 'Unregister Trap Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Unregister Trap Receiver"]',
            
        }

    register_syslog_receiver_menu_item = \
        {
            'DESC': 'Register Syslog Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Register SysLog Receiver"]',
            
        }

    unregister_syslog_receiver_menu_item = \
        {
            'DESC': 'Unregister Syslog Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Unregister SysLog Receiver"]',
            
        }

    search_open_button = \
        {
            'DESC': 'Button to open the Search field for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//span[contains(@class, "x-form-search-trigger")]/ancestor::a',
            
        }

    search_text_field = \
        {
            'DESC': 'Search Text Field for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "inputWrap")]/input',
            
        }

    search_trigger_button = \
        {
            'DESC': 'Button to trigger the search for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//div[contains(@id, "trigger-search")]',
            
        }

    search_clear_button = \
        {
            'DESC': 'Button to clear the search for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "trigger-clear")]',
            
        }
