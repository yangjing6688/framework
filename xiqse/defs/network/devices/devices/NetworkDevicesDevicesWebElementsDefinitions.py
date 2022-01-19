

class NetworkDevicesDevicesWebElementsDefinitions:

    devices_table = \
        {
            'DESC': 'Devices Table',
            'XPATH': '//div[contains(@id, "deviceGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            'wait_for': 10
        }

    devices_table_rows = \
        {
            'DESC': 'Devices Table Rows',
            'XPATH': '//div[contains(@id, "deviceGrid")]//table[contains(@id, "gridview")]//tr',
            'wait_for': 10
        }

    devices_table_status_column_header = \
        {
            'DESC': 'Devices Table Status Column Header',
            'XPATH': '//div[contains(@id, "deviceGrid")]//span[@class="x-column-header-text-inner" and text()="Status"]',
            'wait_for': 10
        }

    devices_table_status_cell = \
        {
            'DESC': 'Devices Table Row Status Cell',
            'CSS_SELECTOR': '[data-qtip^="Device Status"]',
            'wait_for': 10
        }

    devices_table_column_by_name = \
        {
            'DESC': 'Devices Table Column with the Specified Name',
            'XPATH': '//div[contains(@id, "deviceGrid")]//span[contains(@id, "gridcolumn") and text()="${element_name}"]',
            'wait_for': 10
        }

    devices_table_column_value = \
        {
            'DESC': 'Devices Table Column Value',
            'CSS_SELECTOR': 'td[data-columnid="${element_id}"]',
            'wait_for': 10
        }

    devices_table_row_by_index = \
        {
            'DESC': 'Devices Table Row at the Specified Index',
            'XPATH': '//div[contains(@id, "deviceGrid")]//table[@data-recordindex="${element_index}"]//tr',
            'wait_for': 10
        }

    device_menu_tb_button = \
        {
            'DESC': 'Device Menu Toolbar Button',
            'XPATH': '//div[contains(@id, "deviceGrid")]//a[contains(@class, "x-btn-default-toolbar-small")]//span[contains(@class, "fa fa-bars")]',
            'wait_for': 10
        }

    add_device_tb_button = \
        {
            'DESC': 'Add Device Toolbar Button',
            'XPATH': '//a[contains(@class, "x-btn-default-toolbar-small")]//span[text()="Add Device..."]',
            'wait_for': 10
        }

    more_actions_menu_item = \
        {
            'DESC': 'More Actions Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="More Actions"]',
            'wait_for': 10
        }

    delete_device_menu_item = \
        {
            'DESC': 'Delete Device Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Delete Device"]',
            'wait_for': 10
        }

    restart_device_menu_item = \
        {
            'DESC':  'Restart Device Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Restart Device..."]',
            'wait_for': 10
        }

    set_device_profile_menu_item = \
        {
            'DESC': 'Set Device Profile Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Set Device Profile..."]',
            'wait_for': 10
        }

    configure_menu_item = \
        {
            'DESC': 'Configure Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Configure..."]',
            'wait_for': 10
        }

    upgrade_firmware_menu_item = \
        {
            'DESC': 'Upgrade Firmware Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Upgrade Firmware..."]',
            'wait_for': 10
        }

    table_displaying_label = \
        {
            'DESC': 'Set Device Profile Dialog Cancel Button',
            'XPATH': '//div[contains(@class, "x-toolbar-text") and contains(text(), "Displaying")]',
            'wait_for': 10
        }

    archives_menu_item = \
        {
            'DESC': 'Archives Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Archives"]',
            'wait_for': 10
        }

    backup_configuration_menu_item = \
        {
            'DESC': 'Backup Configuration Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Backup Configuration"]',
            'wait_for': 10
        }

    restore_configuration_menu_item = \
        {
            'DESC': 'Restore Configuration Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Restore Configuration..."]',
            'wait_for': 10
        }

    register_trap_receiver_menu_item = \
        {
            'DESC': 'Register Trap Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Register Trap Receiver"]',
            'wait_for': 10
        }

    unregister_trap_receiver_menu_item = \
        {
            'DESC': 'Unregister Trap Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Unregister Trap Receiver"]',
            'wait_for': 10
        }

    register_syslog_receiver_menu_item = \
        {
            'DESC': 'Register Syslog Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Register SysLog Receiver"]',
            'wait_for': 10
        }

    unregister_syslog_receiver_menu_item = \
        {
            'DESC': 'Unregister Syslog Receiver Menu Item',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Unregister SysLog Receiver"]',
            'wait_for': 10
        }

    search_open_button = \
        {
            'DESC': 'Button to open the Search field for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//span[contains(@class, "x-form-search-trigger")]/ancestor::a',
            'wait_for': 10
        }

    search_text_field = \
        {
            'DESC': 'Search Text Field for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "inputWrap")]/input',
            'wait_for': 10
        }

    search_trigger_button = \
        {
            'DESC': 'Button to trigger the search for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//div[contains(@id, "trigger-search")]',
            'wait_for': 10
        }

    search_clear_button = \
        {
            'DESC': 'Button to clear the search for the Devices table',
            'XPATH': '//div[contains(@id, "deviceGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "trigger-clear")]',
            'wait_for': 10
        }
