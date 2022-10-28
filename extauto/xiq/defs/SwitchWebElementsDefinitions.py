

class SwitchWebElementsDefinitions:
    switch_exos_serial_text_area = \
        {
         'CSS_SELECTOR': '.serial-numbers.exos',
         'wait_for': 1
         }

    switch_type_select_exos_platform = \
        {
         'XPATH': '//*[@id="ah/util/form/dgrid/TaskGrid_0"]/div[1]/div[5]/div[1]/div[1]/div[2]/ul/li[3]/a',
         'wait_for': 5
         }

    switch_type_select_exos_parent = \
        {
         'CLASS_NAME': 'quick-exos-select',
         'XPATH': '//*[@id="ah/util/form/dgrid/TaskGrid_0"]/div[1]/div[5]/div[1]/div[1]/div[2]/ul/li[3]',
         'wait_for': 5
         }

    switch_type_select_child = \
        {
         'CLASS_NAME': 'unselected-navpill',
         'XPATH': '//*[@id="ah/util/form/dgrid/TaskGrid_0"]/div[1]/div[5]/div[1]/div[1]/div[2]/ul/li[3]/a',
         'wait_for': 5
         }

    switch_type_select_voss_platform = \
        {
         'CSS_SELECTOR': '.chzn-results li[data-automation-tag="chzn-option-VOSS"]',
         'wait_for': 1
        }

    switch_edit_button = \
        {
         'CSS_SELECTOR': '.table-action-icons.table-edit',
         'wait_for': 5
        }

    switch_monitor_get_ip_address = \
        {
            'CLASS_NAME': 'ip-address',
            'index': 0,
            'wait_for': 1
        }

    switch_monitor_get_mac_address = \
        {
            'CLASS_NAME': 'mac-address',
            'wait_for': 1
        }

    switch_monitor_get_software_version = \
        {
            'CLASS_NAME': 'software-version',
            'wait_for': 1
        }

    switch_monitor_get_model = \
        {
            'CLASS_NAME': 'product-type',
            'wait_for': 1
        }

    switch_monitor_get_serial_number = \
        {
            'CLASS_NAME': 'service-tag',
            'wait_for': 1
        }

    switch_monitor_get_manufacturer = \
        {
            'CLASS_NAME': 'make',
            'wait_for': 1
        }

    switch_monitor_get_iqagent_version = \
        {
            'CLASS_NAME': 'agent-version',
            'wait_for': 1
        }

    switch_select_port_button = \
        {
            'CSS_SELECTOR': '.ethernet-port',
            'wait_for': 5,
        }

    devices_switch_name_link = \
        {
            'CLASS_NAME': 'switch-entity',
            'wait_for': 1
         }

    devices_page_grid_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            
         }

    devices_switch_port_detail_rows = \
        {
            'CSS_SELECTOR': '.table-content-row',
            'wait_for': 1
        }

    devices_refresh_page = \
        {
            'CLASS_NAME': 'ui-fresh-icon',
            'wait_for': 5
         }

    devices_search_field = \
        {
            'XPATH': '//*[@id="ah/util/form/dgrid/TaskGrid_0"]/div[1]/div[5]/div[2]/div[1]/input',
            'wait_for': 5
         }

    devices_search_button = \
        {
            'CLASS_NAME': 'search-btn',
            'wait_for': 5
         }
    devices_select_checkbox_field = \
        {
            'CLASS_NAME': 'dgrid-cell',
            'wait_for': 5
         }

    get_monitor_tab_menu = \
        {
            'XPATH': '//*[@id="appHeader"]/ul/li[3]/span/a',
            'wait_for': 3
         }

    get_monitor_devices_tab_menu = \
        {
            'XPATH': '//*[@id="appHeader"]/ul/li[3]/ul/li[1]/a',
            'wait_for': 3
         }

    switch_type_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickAddCtn"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5,
            'index': 0
        }

    switch_type_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickAddCtn"]'
                     '//ul[contains(@class, "qa-chzn-results-quickdeviceselect")]//li',
            'wait_for': 5
        }

    switch_make_drop_down = \
        {
            # 'XPATH': '//div[@data-dojo-attach-point="quickMakeSelect"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-make-select"]',
            'wait_for': 10,
            # 'index': 0
        }

    switch_make_drop_down_options = \
        {
            # 'XPATH': '//div[@data-dojo-attach-point="quickMakeSelect"]'
            #          '//ul[contains(@class, "qa-chzn-results-quickaddselect")]//li',
            'XPATH': '//*[@data-automation-tag="automation-quick-add-onboard-make-select-dropdown"]'
                     '//tr[contains(@class, "dijitMenuItem")]',
            'wait_for': 5
        }

    switch_entry_type_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickEntrySelect"]//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5,
            'index': 0
        }

    switch_entry_type_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="quickEntrySelect"]'
                     '//ul[contains(@class, "qa-chzn-results-quickaddentrytype")]//li',
            'wait_for': 5
        }



    switch_voss_serial_text_area = \
        {
            'CSS_SELECTOR': '.serial-numbers.voss',
            'wait_for': 1
        }
