class Device360WebElementDefs:
    system_info_button = \
        {
            'XPATH': '//*[@data-id="systeminfo"]',
            'wait_for': 5
        }

    system_info_device_host_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceHostName"]',
            'wait_for': 5
        }

    system_info_network_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkPolicyName"]',
            'wait_for': 5
        }

    system_info_device_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceModel"]',
            'wait_for': 5
        }

    system_info_device_function = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceFunction"]',
            'wait_for': 5
        }

    system_info_device_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTemplateName"]',
            'wait_for': 5
        }

    system_info_conf_type = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configurationType"]',
            'wait_for': 5
        }

    system_info_serial_num = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceserialNumber"]',
            'wait_for': 5
        }

    system_info_iq_engine = \
        {
            'XPATH': '//*[@data-dojo-attach-point="displayVer"]',
            'wait_for': 5
        }

    system_info_dev_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceAdminStatus"]',
            'wait_for': 5
        }

    system_info_mgt0_ipv4 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mgmtIpAddress"]',
            'wait_for': 5
        }

    system_info_mgt0_ipv6 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipv6Address"]',
            'wait_for': 5
        }

    system_info_ipv6_subnet = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipv6Netmask"]',
            'wait_for': 5
        }

    system_info_ipv4_subnet = \
        {
            'XPATH': '//*[@data-dojo-attach-point="subnetMask"]',
            'wait_for': 5
        }

    system_info_ipv4_default = \
        {
            'XPATH': '//*[@data-dojo-attach-point="defaultGateway"]',
            'wait_for': 5
        }

    system_info_ipv6_default = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipv6Gateway"]',
            'wait_for': 5
        }

    system_info_mgt0_mac = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mgmtMacAddress"]',
            'wait_for': 5
        }

    system_info_dns = \
        {
            'XPATH': '//*[@data-dojo-attach-point="dnsSrvAddress"]',
            'wait_for': 5
        }

    system_info_ntp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ntpSrvAddress"]',
            'wait_for': 5
        }

    close_dialog = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeDialog']",
            'wait_for': 10
        }

    actions_adv_cli_access_cmd_input = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cli"]',
            'wait_for': 5
        }

    actions_adv_cli_access_cmd_apply = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apply"]',
            'wait_for': 5
        }

    actions_adv_cli_access_cmd_output = \
        {
            'XPATH': '//*[@class="cli-command-result-pre"]',
            'wait_for': 5
        }

    device360_cells_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 5
        }

    device_active_clients_grid = \
        {
            'XPATH': '//*[@class="entity-content-ctn device-entity-connected-ctn"]//table[@class="dgrid-row-table"]',
            'index': 1,
            'wait_for': 5
        }

    device_active_clients_grid_rows = \
        {
            'XPATH': 'tr',
            'wait_for': 5
        }

    device_utilities_status = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Status")]',
            'wait_for': 5
        }

    utilities_status_interface = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Interface")]',
            'wait_for': 5
        }

    utilities_status_adv_channel_sel = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Advanced Channel Selection Protocol")]',
            'wait_for': 5
        }

    utilities_status_wifi_status_summary = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Wi-Fi Status Summary")]',
            'wait_for': 5
        }

    utilities_status_interface_name_dropdown = \
        {
            'XPATH': '//*[@class="option-list-ctn"]//span[contains(text(), "All")]',
            'wait_for': 5
        }

    utilities_status_interface_name_dropdown_opt = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-optionlist"]//li',
            'wait_for': 5
        }

    utilities_status_interface_contents = \
        {
            'XPATH': '//*[@data-dojo-attach-point="contentList"]//pre',
            'wait_for': 5
        }

    utilities_status_adv_channel_sel_contents = \
        {
            'XPATH': '//*[@data-dojo-attach-point="contentList"]',
            'wait_for': 5
        }

    utilities_status_wifi_summary_station_btn = \
        {
            'XPATH': '//*[@class="ui-tab ui-tab-updated ui-tab-inactive clearfix"]//a[contains(text(), "Station")]',
            'wait_for': 5
        }

    utilities_status_wifi_summary_station_content = \
        {
            'XPATH': '//*[@data-dojo-attach-point="statusTabs"]//div[@class="ui-tab-panel-wrap clearfix "]',
            # 'index': 22,
            'wait_for': 5
        }

    device360_configure_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureViewSelect"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_tab = \
        {
            'XPATH': '//*[@data-id="sshavailability"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_tab = \
        {
            'XPATH': '//*[@data-id="sshavailability1"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_5min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-5"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_30min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-30"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_60min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-60"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_120min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-120"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_240min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-240"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_enable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_ip = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addressInfo"]//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_port = \
        {
            'XPATH': '//*[@data-dojo-attach-point="port"]',
            'wait_for': 5
        }
    exos_switch_info_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    exos_switch_info_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    exos_switch_info_software_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    exos_switch_info_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    exos_switch_info_serial = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="serviceTag"]',
            'wait_for': 5
        }

    exos_switch_info_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    exos_switch_info_iqagent_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="hiveAgent"]',
            'wait_for': 5
        }

    exos_switch_info_device_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="devicePolicy"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_ip = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5,
            'index':1
        }

    device360_configure_ssh_web_port = \
        {
            'XPATH': '//*[@data-dojo-attach-point="port"]',
            'wait_for': 5,
            'index':1
        }

    device360_configure_ssh_web_url = \
        {
            'XPATH': '//*[@data-dojo-attach-point="exampleCommand"]',
            'wait_for': 5,
            'index': 1
        }

    device360_configure_ssh_web_enable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH"]',
            'wait_for': 5,
            'index':1
        }

    device360_configure_ssh_web_disable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH" and contains(text(), "Disable SSH Web")]',
            'wait_for': 5,
        }

    device360_configure_ssh_web_5min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-5"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_30min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-30"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_60min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-60"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_120min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-120"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_240min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-240"]',
            'wait_for': 5
        }

    device360_device_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configNav"]',
            'wait_for': 5
        }

    device360_port_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portNav"]',
            'wait_for': 5
        }

    device360_port_configuration_title = \
        {
            'CSS_SELECTOR': '.port-configuration-title',
            'wait_for': 5
        }

    device360_configure_device_host_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hostName"]',
            'wait_for': 5
        }

    device360_configure_device_snmp_location = \
        {
            'XPATH': '//*[@data-dojo-attach-point="snmpLocation"]',
            'wait_for': 5
        }

    device360_configure_device_network_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkPolicyArea"]//a[contains(@class, "chzn-single")]/span',
            'wait_for': 5
        }

    device360_configure_device_device_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTemplateArea"]//a[contains(@class, "chzn-single")]/span',
            'wait_for': 5
        }

    device360_configure_device_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceConfigNode"]//a[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    device360_configure_device_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceConfigNode"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    voss_switch_info_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    voss_switch_info_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    voss_switch_info_software_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    voss_switch_info_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    voss_switch_info_serial = \
        {
            'XPATH': '//*[@class="health-item service-tag data-item"]',
            'wait_for': 5
        }

    voss_switch_info_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    voss_switch_info_iqagent_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hiveAgent"]',
            'wait_for': 5
        }

    voss_switch_info_device_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="devicePolicy"]',
            'wait_for': 5
        }

    device360_configure_ssh_disable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH"][@value="disable"]',
            'wait_for': 5
        }

    device360_events_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="eventsNav"]',
            'wait_for': 5
        }

    device360_events_grid = \
        {
            'XPATH': '//div[@data-dojo-attach-point="eventsList"]//div[contains(@class, "dgrid-content")]',
            'wait_for': 5
        }

    device360_events_grid_rows = \
        {
            'XPATH': 'div[@role="row"]',
            'wait_for': 5
        }

    device360_events_grid_cells = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td',
            
         }

    device360_event_timestamp = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-timestamp")]',
            
         }

    device360_event_description = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-description")]',
            
         }
    device360_event_severity = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-severity")]',
            
         }
    device360_alarms_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="alarmsTab"]',
            'wait_for': 5
        }

    device360_alarms_grid = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//table[@class="dgrid-row-table" and not(contains(@id, "-header"))]',
            'wait_for': 5
        }

    device360_alarms_grid_rows = \
        {
            'XPATH': 'tr',
            'wait_for': 5
        }

    device360_alarms_grid_cells = \
        {
            'XPATH': 'td',
            
         }

    device360_alarm_timestamp = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//td[contains(@class, "field-timestamp")]',
            'index': 0,
            
         }

    device360_alarm_category = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//td[contains(@class, "field-category")]',
            'index': 0,
            
         }

    device360_configure_port_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="listArea"]',
            'wait_for': 5
        }

    device360_configure_port_rows = \
        {
            'XPATH': '//div[contains(@class, "port-details-entry")]',
            'wait_for': 5
        }

    device360_configure_port_row_cells = \
        {
            'CSS_SELECTOR': '.column',
            'wait_for': 5
        }

    device360_configure_port_row_state_toggle = \
        {
            'CSS_SELECTOR': '.port-enabled input[data-repeater-bind-to-field="enabled"]',
            'wait_for': 5
        }

    device360_configure_port_row_state_enabled = \
        {
            'CSS_SELECTOR': '.port-enabled input[checked]',
            'wait_for': 5
        }

    device360_configure_port_row_state_disabled = \
        {
            'CSS_SELECTOR': '.port-enabled input:not([checked])',
            'wait_for': 5
        }

    device360_configure_port_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device360_refresh_page_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pageRefresh"]',
            'wait_for': 5
        }

    device360_monitor_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="monitorViewSelect"]',
            'wait_for': 5
        }

    device360_monitor_overview_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="monitorOverviewTab"]',
            'wait_for': 5
        }

    device360_switch_system_info_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoNav"]',
            'wait_for': 5
        }

    device360_monitor_clients_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientNav"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="diagnosticsNav"]',
            'wait_for': 5
        }

    device360_time_range_drop_down = \
        {
            'XPATH': '//div[@class="timeline-select-ctn"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    device360_time_range_drop_down_selection = \
        {
            'XPATH': '//div[@class="timeline-select-ctn"]//div[@data-automation-tag="automation-chzn-container-ctn"]//span',
            'wait_for': 5
        }

    device360_time_range_drop_down_items = \
        {
            'XPATH': '//div[@class="timeline-select-ctn"]//div[@data-automation-tag="automation-chzn-container-ctn"]//ul/li',
            'wait_for': 5
        }

    device360_day_time_range_one_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="oneHour"]',
            'wait_for': 5
        }

    device360_day_time_range_two_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="twoHour"]',
            'wait_for': 5
        }

    device360_day_time_range_four_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="fourHour"]',
            'wait_for': 5
        }

    device360_day_time_range_eight_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="eightHour"]',
            'wait_for': 5
        }

    device360_day_time_range_twenty_four_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="twentyFourHour"]',
            'wait_for': 5
        }

    device360_week_time_range_one_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker week-range"]//li[@data-dojo-attach-point="oneDay"]',
            'wait_for': 5
        }

    device360_week_time_range_two_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker week-range"]//li[@data-dojo-attach-point="twoDay"]',
            'wait_for': 5
        }

    device360_week_time_range_seven_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker week-range"]//li[@data-dojo-attach-point="sevenDay"]',
            'wait_for': 5
        }

    device360_month_time_range_seven_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="oneWeek"]',
            'wait_for': 5
        }

    device360_month_time_range_fourteen_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="twoWeek"]',
            'wait_for': 5
        }

    device360_month_time_range_thirty_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="thirtyDay"]',
            'wait_for': 5
        }

    device360_month_time_range_ninety_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="ninetyDay"]',
            'wait_for': 5
        }

    device360_port_diagnostics_select_all_ports_button = \
        {
            'XPATH': '//div[@class="selection-buttons"]/button[@data-dojo-attach-point="selectAllButton"]',
            'wait_for': 5
        }

    device360_port_diagnostics_deselect_all_ports_button = \
        {
            'XPATH': '//div[@class="selection-buttons"]/button[@data-dojo-attach-point="deselectAllButton"]',
            'wait_for': 5
        }

    device360_port_diagnostics_selected_ports = \
        {
            'XPATH': '//div[contains(@class, "device-ports")]/ul//li/ul/li/div[(contains(@class, "active"))]',
            'wait_for': 5
        }

    device360_port_diagnostics_deselected_ports = \
        {
            'XPATH': '//div[contains(@class, "device-ports")]/ul//li/ul/li/div[not(contains(@class, "active"))]',
            'wait_for': 5
        }

    device360_monitor_overview_chart_graph = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceoverview"]//div[@data-dojo-attach-point="highChartCtn"]',
            'wait_for': 5
        }

    device360_monitor_clients_chart_graph = \
        {
            'XPATH': '//div[@data-dojo-attach-point="connectedclients"]//div[@data-dojo-attach-point="highChartCtn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_chart_graph = \
        {
            'XPATH': '//div[contains(@class, "device-diagnostics")]//div[@data-dojo-attach-point="highChartCtn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_chart_graph_port_errors = \
        {
            'XPATH': '//div[contains(@class, "device-diagnostics")]//div[@data-dojo-attach-point="portErrorsCtn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_chart_graph_port_casts = \
        {
            'XPATH': '//div[contains(@class, "device-diagnostics")]//div[@data-dojo-attach-point="portCastsCtn"]',
            'wait_for': 5
        }

    overview_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    overview_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    overview_software_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    overview_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    overview_serial = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceTag"]',
            'wait_for': 5
        }

    overview_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    device360_configure_device_function_dropdown = \
        {
            'XPATH': '//div[@class="device-config-section"]//select[@data-dojo-attach-point="deviceFunction"]/../div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 5
        }

    device360_configure_device_function_dropdown_items = \
        {
            'XPATH': '//div[@class="device-config-section"]//select[@data-dojo-attach-point="deviceFunction"]/../div[@data-automation-tag="chzn-container-ctn"]//ul/li',
            'wait_for': 5
        }

    device360_device_title = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceTitle"]',
            'wait_for': 5
        }

    device360_sidebar_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceModel"]',
            'wait_for': 5
        }

    device360_sidebar_device_image = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceImg"]/img',
            'wait_for': 5
        }

    device360_sidebar_host_name = \
        {
            'XPATH': '//strong[@data-dojo-attach-point="deviceHostName"]',
            'wait_for': 5
        }

    device360_sidebar_enabled_ports = \
        {
            'XPATH': '//strong[@data-dojo-attach-point="portEnable"]',
            'wait_for': 5
        }

    device360_sidebar_disabled_ports = \
        {
            'XPATH': '//strong[@data-dojo-attach-point="portDisable"]',
            'wait_for': 5
        }

    device360_sidebar_connected_state = \
        {
            'XPATH': '//p[@data-dojo-attach-point="deviceConnectedTest"]',
            'wait_for': 5
        }

    device360_sidebar_active_since = \
        {
            'XPATH': '//p[@data-dojo-attach-point="connectedTime"]',
            'wait_for': 5
        }

    device360_sidebar_active_alarms = \
        {
            'XPATH': '//span[@data-id="alarmDetails"]',
            'wait_for': 5
        }

    device360_sidebar_unique_clients = \
        {
            'XPATH': '//span[@data-id="connectedclients"]',
            'wait_for': 5
        }

    device360_sidebar_cpu_usage = \
        {
            'XPATH': '//div[@class="title" and text()="CPU Usage"]/../div[@data-dojo-attach-point="metricElem"]',
            'wait_for': 5
        }

    device360_sidebar_memory_usage = \
        {
            'XPATH': '//div[@class="title" and text()="Memory Usage"]/../div[@data-dojo-attach-point="metricElem"]',
            'wait_for': 5
        }

    device360_tooltip_content = \
        {
            'XPATH': '//div[@class="tooltip-content"]',
            'wait_for': 5
        }

    device360_topbar_cpu = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cpuElement"]',
            'wait_for': 5
        }

    device360_topbar_memory = \
        {
            'XPATH': '//div[@data-dojo-attach-point="memoryElement"]',
            'wait_for': 5
        }

    device360_topbar_mac_usage = \
        {
            'XPATH': '//div[@data-dojo-attach-point="macElement"]',
            'wait_for': 5
        }

    device360_topbar_uptime = \
        {
            'XPATH': '//div[@data-dojo-attach-point="uptimeElement"]',
            'wait_for': 5
        }

    device360_topbar_temperature = \
        {
            'XPATH': '//span[@class="temperature-digits"]',
            'wait_for': 5
        }

    device360_topbar_power = \
        {
            'XPATH': '//div[@data-dojo-attach-point="powerElement"]',
            'wait_for': 5
        }

    device360_topbar_fan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="fanElement"]',
            'wait_for': 5
        }

    device360_topbar_ip_address = \
        {
            'XPATH': '//span[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    device360_topbar_mac_address = \
        {
            'XPATH': '//span[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    device360_topbar_software_version = \
        {
            'XPATH': '//span[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    device360_topbar_model = \
        {
            'XPATH': '//span[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    device360_topbar_serial = \
        {
            'XPATH': '//span[@data-dojo-attach-point="serviceTag"]',
            'wait_for': 5
        }

    device360_topbar_make = \
        {
            'XPATH': '//span[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    device360_open_site_engine_link = \
        {
            'XPATH': '//a[@data-dojo-attach-point="seLink"]',
            'wait_for': 5
        }

    device360_overview_port_icons = \
        {
            'XPATH': '//div[@class="device-ports"]/ul/li/ul/li',
            'wait_for': 5
        }

    device360_overview_port_details_table = \
        {
            'XPATH': '//div[@data-dojo-attach-point="portDetailsContainer"]/ul[@class="portdetails-table"]',
            'wait_for': 5
        }

    device360_overview_total_active_alarms = \
        {
            'XPATH': '//h1[@data-dojo-attach-point="totalMetric"]',
            'wait_for': 5
        }

    system_info_device_ssids = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssids"]',
            'wait_for': 5
        }

    switch_system_info_archived = \
        {
            'XPATH': '//td[contains(@class, "field-archived")]',
            'wait_for': 5
        }

    switch_system_info_asset_tag = \
        {
            'XPATH': '//td[contains(@class, "field-assetTag")]',
            'wait_for': 5
        }

    switch_system_info_user_data_1 = \
        {
            'XPATH': '//td[contains(@class, "field-userData1")]',
            'wait_for': 5
        }

    switch_system_info_user_data_2 = \
        {
            'XPATH': '//td[contains(@class, "field-userData2")]',
            'wait_for': 5
        }

    switch_system_info_user_data_3 = \
        {
            'XPATH': '//td[contains(@class, "field-userData3")]',
            'wait_for': 5
        }

    switch_system_info_user_data_4 = \
        {
            'XPATH': '//td[contains(@class, "field-userData4")]',
            'wait_for': 5
        }

    switch_system_info_note = \
        {
            'XPATH': '//td[contains(@class, "field-note")]',
            'wait_for': 5
        }

    hyper_link_device_template = \
        {
            'CSS_SELECTOR': '.link-item',
            'wait_for': 5
        }

    device360_stack_configure_device_snmp_location = \
        {
            'XPATH': '//*[@data-dojo-attach-point="snmpLocationInput"]',
            'wait_for': 5
        }

    device360_dev_config_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device360_title_stack_info = \
        {
            'XPATH': '//*[@data-dojo-attach-point="numStackMembers"]',
            'wait_for': 5
        }

    device360_topbar_iqagent_version = \
        {
            'XPATH': '//span[@data-dojo-attach-point="hiveAgent"]',
            'wait_for': 5
        }

    device360_topbar_stack_mem_status = \
        {
            'XPATH': '//span[@data-dojo-attach-point="stackMemberStatus"]',
            'wait_for': 5
        }

    device360_switch_sidebar_active_alarms = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-active-alarms-number"]',
            'wait_for': 5
        }

    device360_switch_sidebar_unique_clients = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-unique-clients-number"]',
            'wait_for': 5
        }

    device360_stack_topbar_power = \
        {
            'XPATH': '//div[@data-dojo-attach-point="powerElement"]',
            'wait_for': 5
        }

    device360_stack_topbar_fan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="fanElement"]',
            'wait_for': 5
        }

    device360_fan_tooltip_content = \
        {
            'CSS_SELECTOR': '.ui-tipbox-ctn',
            'wait_for': 5
        }

    device360_stack_overview_port_icons = \
        {
            'XPATH': '//div[@class="device-ports"]/ul/li/ul/li//div',
            'wait_for': 5
        }

    device360_stack_overview_sl_ports_row = \
        {
            'CSS_SELECTOR': '.device-switch',
            'wait_for': 5
        }

    device360_stack_overview_slot_ports = \
        {
            'CLASS_NAME': 'AH-ports-icons',
            'wait_for': 5
        }

    device360_stack_select_port_group = \
        {
            'XPATH': '//div[@class="device-ports"]//li[contains(@class, "port-group")',
            'wait_for': 5
        }

    device360_stack_port_table_port_name = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(), "Port Name")]//following-sibling::span[contains(text(), "")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_type = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Type")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_status = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Port Status")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_mode = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Port Mode")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_vlan = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"VLAN")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_speed = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Port Speed")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_system_info_button = \
        {
            'XPATH': '//li[@data-dojo-attach-point="stackSystemInfoNav"]',
            'wait_for': 5
        }

    stack_system_info_unit_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-unitNumber")]',
            'wait_for': 5
        }

    stack_system_info_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-ipAddress")]',
            'wait_for': 5
        }

    stack_system_info_netmask = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-netMask")]',
            'wait_for': 5
        }

    stack_system_info_mac = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-macAddress")]',
            'wait_for': 5
        }

    stack_system_info_serial_num = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-serialNumber")]',
            'wait_for': 5
        }

    stack_system_info_prod_type = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-productType")]',
            'wait_for': 5
        }

    stack_system_info_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-make")]',
            'wait_for': 5
        }

    stack_system_info_admin_state = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-adminState")]',
            'wait_for': 5
        }

    stack_system_info_software_ver = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-softwareVersion")]',
            'wait_for': 5
        }

    stack_system_info_stack_mgmt_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-stackManagementStatus")]',
            'wait_for': 5
        }

    sw_template_stack_add_items = \
        {
            'XPATH': '//div[@id="switchesMenu"]//ul/li/a',

            'wait_for': 5
        }

    sw_template_stack_added_items = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="templateElements"]/li',
            'wait_for': 5
        }

    sw_template_stack_first_page = \
        {
            'CSS_SELECTOR': '.stack-template',
            'wait_for': 5
        }

    device360_device_configuration_stack_template_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackTemplateArea"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    device360_device_configuration_stack_template_items = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackTemplateArea"]//div[@class="chzn-drop"]/ul/li',
            'wait_for': 5
        }

    device360_device_configuration_save_button = \
        {
            'XPATH': '//div[@class="btn-area"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device360_device_configuration_update_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="deployNowBtn"]',
            'wait_for': 5
        }

    device360_device_configuration_exit_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    d360Event_search_textbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="eventSearchInput"]',
            'wait_for': 3
        }

    device360_configure_vlan_port_one = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portOverrideNode"]//input[@data-dojo-attach-point="accessPortVLAN"]',
            'wait_for':5
        }

    d360_configure_port_row_override_revert = \
        {
            'CSS_SELECTOR': '.override-revert',
            'wait_for': 5
        }

    d360_configure_port_row_revert_button = \
        {
            'XPATH': '//*[@class="revert-tip-button"]',
            'wait_for': 3
        }

    device360_configure_port_settings_aggregation_rows = \
        {
            'XPATH': '//div[contains(@class, "port-settings-entry")]',
            'wait_for': 5
        }

    device360_configure_stp_rows = \
        {
            'XPATH': '//div[contains(@class, "port-stp-entry")]',
            'wait_for': 5
        }

    device360_configure_storm_control_rows = \
        {
            'XPATH': '//div[contains(@class, "port-storm-control-entry")]',
            'wait_for': 5
        }

    d360_configure_port_state_override_revert = \
        {
            'XPATH': '//div[@class="port-enabled"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_port_usage_override_revert = \
        {
            'XPATH': '//div[@class="port-type-choose"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_vlan_override_revert = \
        {
            'XPATH': '//div[@class="port-vlan-type port-vlan-type-trunk"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_description_override_revert = \
        {
            'XPATH': '//div[@class="port-description"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_transmission_override_revert = \
        {
            'XPATH': '//div[@class="port-transmission-type"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_speed_override_revert = \
        {
            'XPATH': '//div[@class="port-transmission-speed"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_flow_override_revert = \
        {
            'XPATH': '//div[@class="port-flow-control "]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_transmit_override_revert = \
        {
            'XPATH': '//div[@class="port-lldp-transmit cb-field"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_receive_override_revert = \
        {
            'XPATH': '//div[@class="port-lldp-recieve cb-field"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_cdp_override_revert = \
        {
            'XPATH': '//div[@class="port-cdp-receive cb-field "]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_client_reporting_override_revert = \
        {
            'XPATH': '//div[@class="port-client-reporting cb-field"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_stp_status_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-status"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_edge_port_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-edge-port"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_bpdu_protection_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-bpdu-protection "]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_priority_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-priority"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_path_cost_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-path-cost"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_broadcast_override_revert = \
        {
            'XPATH': '//div[@class="port-broadcast-traffic"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_unknown_unicast_override_revert = \
        {
            'XPATH': '//div[@class="port-unknown-unicast"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_multicast_override_revert = \
        {
            'XPATH': '//div[@class="port-multicast"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_value_override_revert = \
        {
            'XPATH': '//div[@class="port-rate-limit-value"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_port_details_tab_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahTabContainer"]//a[contains(text(), "Port Details")]',
            'wait_for': 5
        }

    d360_configure_port_settings_aggregation_tab_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahTabContainer"]//a[contains(text(), "Port Settings & Aggregation")]',
            'wait_for': 5
        }

    d360_configure_port_stp_tab_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahTabContainer"]//a[contains(text(), "STP")]',
            'wait_for': 5
        }

    d360_configure_port_storm_control_tab_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahTabContainer"]//a[contains(text(), "Storm Control")]',
            'wait_for': 5
        }

    d360_configure_port_state_click_button = \
        {
            'CSS_SELECTOR': '.port-enabled input[data-repeater-bind-to-field="enabled"]',
            'wait_for': 5
        }

    d360_configure_transmit_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-lldp-transmit input[data-repeater-bind-to-field="enableLldpTransmit"]',
            'wait_for': 5
        }

    d360_configure_receive_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-lldp-recieve input[data-repeater-bind-to-field="enableLldpReceive"]',
            'wait_for': 5
        }

    d360_configure_cdp_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-cdp-receive input[data-repeater-bind-to-field="enableCdpReceive"]',
            'wait_for': 5
        }

    d360_configure_client_reporting_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-client-reporting input[data-repeater-bind-to-field="enableClientReporting"]',
            'wait_for': 5
        }

    d360_configure_stp_status_click_button = \
        {
            'CSS_SELECTOR': '.port-stp-status input[data-repeater-bind-to-field="enabled"]',
            'wait_for': 5
        }

    d360_configure_edge_port_click_button = \
        {
            'CSS_SELECTOR': '.port-stp-edge-port input[data-repeater-bind-to-field="enableEdgePort"]',
            'wait_for': 5
        }

    d360_configure_broadcast_click_checkbox = \
        {
            'CSS_SELECTOR': '.checkbox input[data-repeater-bind-to-field="enableBroadcastTraffic"]',
            'wait_for': 5
        }

    d360_configure_unknown_unicast_click_checkbox = \
        {
            'CSS_SELECTOR': '.checkbox input[data-repeater-bind-to-field="enableUnknownUnicastTraffic"]',
            'wait_for': 5
        }

    d360_configure_multicast_click_checkbox = \
        {
            'CSS_SELECTOR': '.checkbox input[data-repeater-bind-to-field="enableMuticastTraffic"]',
            'wait_for': 5
        }

    d360_switch_port_view_all_pages_button = \
        {
            'XPATH': '//div[@class="pagination-size-ctn"]//span[contains(text(),"100")]',
            'wait_for': 3
        }

    d360_switch_ports_table_port_name_cell = \
        {
            'CSS_SELECTOR':'.field-ifName',
            'wait_for': 3
        }

    d360_switch_ports_table_grid_rows = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portGridNode"]//*[@class="dgrid-row-table"]',
            
         }

    device360_switch_port_table_port_name = \
        {
            'CSS_SELECTOR': '.field-ifName',
            'wait_for': 5
        }

    device360_switch_port_table_port_type = \
        {
            'CSS_SELECTOR': '.field-pType',
            'wait_for': 5
        }

    device360_switch_port_table_lacp_neighbor = \
        {
            'CSS_SELECTOR': '.field-lldpSystemName',
            'wait_for': 5
        }

    device360_switch_port_table_lacp_status = \
        {
            'CSS_SELECTOR': '.field-lacpActive',
            'wait_for': 5
        }

    device360_switch_port_table_port_status = \
        {
            'CSS_SELECTOR': '.field-status',
            'wait_for': 5
        }

    device360_switch_port_table_transmission_mode = \
        {
            'CSS_SELECTOR': '.field-transmissionMode',
            'wait_for': 5
        }

    device360_switch_port_table_port_mode = \
        {
            'CSS_SELECTOR': '.field-portMode',
            'wait_for': 5
        }

    device360_switch_port_table_access_vlan = \
        {
            'CSS_SELECTOR': '.field-vlan',
            'wait_for': 5
        }

    device360_switch_port_table_tagged_vlans = \
        {
            'CSS_SELECTOR': '.field-taggedVlans',
            'wait_for': 5
        }

    device360_switch_port_table_traffic_received = \
        {
            'CSS_SELECTOR': '.field-rxByteCount',
            'wait_for': 5
        }

    device360_switch_port_table_traffic_transmitted = \
        {
            'CSS_SELECTOR': '.field-txByteCount',
            'wait_for': 5
        }

    device360_switch_port_table_power_used = \
        {
            'CSS_SELECTOR': '.field-powerUsed',
            'wait_for': 5
        }

    device360_switch_port_table_port_speed = \
        {
            'CSS_SELECTOR': '.field-portSpeed',
            'wait_for': 5
        }

    d360_monitor_items_rows = \
        {
            'XPATH': '//div[contains(@class, "dgrid-row  ui-state-default")]',
            'wait_for': 5
        }

    d360_monitor_transmission_mode = \
        {
            'CSS_SELECTOR': '.field-transmissionMode',
            'wait_for': 5
        }

    d360_monitor_port_speed = \
        {
            'CSS_SELECTOR': '.field-portSpeed',
            'wait_for': 5
        }
    device360_port_settings_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-configuration-port-settings"]',
            'wait_for': 5
        }

    icon_ports_items = \
        {
            'XPATH': '//li[contains(@class,"port-rel")]',
            'wait_for': 5
        }

    port_click = \
        {
            'CSS_SELECTOR': '.AH-ports-icons',
            'wait_for': 5
        }

    d360_interface_transmission_mode = \
        {
            'XPATH': '//*[@class="port-info port-trans-mode  "]/b',
            'wait_for': 5
        }
    d360_interface_port_speed = \
        {
            'XPATH': '//*[@class="port-info port-speed  low "]/b',
            'wait_for': 5
        }

    d360_view_100_rows_on_page = \
        {
            'XPATH': '//div[@class="pagination-size-ctn"]//span[contains(text(), "100")]',
            'wait_for': 5
        }
    d360_monitor_port_name = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-ifName")]',
            
        }

    d360_monitor_interface_name = \
        {
            'CSS_SELECTOR': '.field-ifName',
            'wait_for': 5
        }

    d360_vim_model = \
        {
            'XPATH': '//li[@class="port-group-label"]',
            'wait_for': 5
        }

    d360_vim_ports = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="utilPortWrap"]//span[contains(@class,"port-desc")]',
            'wait_for': 5
        }

    d360_wireframe_port = \
        {
            'XPATH': '//div[@class="device-ports device-ports--padding"]/ul/li/ul/li',
            'wait_for': 5
        }

    d360_port_leftclick_interface_name = \
        {
            'XPATH': '//div[@class="port-info interface-name"]',
            'wait_for': 5
        }

    d360_port_leftclick_interface_type = \
        {
            'XPATH': '//div[@class="port-info port-type "]',
            'wait_for': 5
        }

    d360_port_leftclick_port_mode = \
        {
            'XPATH': '//div[@class="port-info port-mode "]',
            'wait_for': 5
        }

    d360_port_leftclick_access_vlan = \
        {
            'XPATH': '//div[@class="port-info port-vlan  "]',
            'wait_for': 5
        }

    d360_port_leftclick_tagged_vlan = \
        {
            'XPATH': '//div[@class="port-info port-tagged-vlan   "]',
            'wait_for': 5
        }

    d360_port_leftclick_port_status = \
        {
            'XPATH': '//div[@class="port-info port-status-a "]',
            'wait_for': 5
        }

    device360_create_auto_template_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createStackTemplate"]',
            'wait_for': 5
        }
    
    d360_pagination_next_button = \
        {
            'XPATH': '//div[@class="pagination-num-ctn"]//span[@class="ui-page-item J-page-next ui-page-item-next "]',
            'wait_for': 3
        }

    d360_pagination_page_button = \
        {
            'XPATH': '//span[@class="pagination-page"]',
            'wait_for': 3
        }

    device360_port_configuration_content = \
        {
            'CSS_SELECTOR': '.port-configuration',
            'wait_for': 5
        }

    device360_configure_port_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureNav"]//li[@data-id="portconfiguration"]',
            'wait_for': 5
        }

    policy_configure_port_rows = \
        {
            'XPATH': '//tabset[@data-dojo-attach-point="configuration-ports-tabs"]//portdetails//portentry-row',
            'wait_for': 5
        }

    sw_template_stack_sw_item = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceType"]',
            'wait_for': 5
        }

    device360_configure_port_usage_drop_down_button = \
        {
            'CSS_SELECTOR': '.chzn-single',
            'wait_for': 5
        }

    device360_configure_port_usage_drop_down_options = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    device360_configure_port_access_vlan_textfield = \
        {
            'CSS_SELECTOR': '.port-type-vlan-value',
            'wait_for': 5
        }

    device360_configure_port_trunk_native_vlan_textfield = \
        {
            'CSS_SELECTOR': '.native-vlan',
            'index': 1,
            'wait_for': 5
        }

    device360_configure_port_trunk_vlan_textfield = \
        {
            'CSS_SELECTOR': '.allowed-vlan',
            'index': 1,
            'wait_for': 5
        }

    device360_port_configuration_port_settings_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-configuration-port-settings"]',
            'wait_for': 5
        }

    device360_port_settings_transmission_mode_drop_down_button = \
        {
            'CSS_SELECTOR': '.chzn-single',
            'wait_for': 5
        }

    device360_port_settings_transmission_mode_drop_down_options = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-transmissiontype li',
            'wait_for': 5
        }

    device360_port_settings_speed_drop_down_button = \
        {
            'CSS_SELECTOR': '.chzn-single',
            'index': 1,
            'wait_for': 5
        }

    device360_port_settings_speed_drop_down_options = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-speed li',
            'wait_for': 5
        }

    device360_configure_port_pse_poe_state_enabled = \
        {
            'CSS_SELECTOR': '.grid_2 column.not-master-content input[checked]',
            'wait_for': 5
        }

    device360_configure_port_pse_poe_state_disabled = \
        {
            'CSS_SELECTOR': '..grid_2 column.not-master-content input:not([checked])',
            'wait_for': 5
        }

    device360_port_configuration_pse_tab = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-config-pse"]',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_select_button = \
        {
            'CSS_SELECTOR': '.ui-ip-mark',
            'wait_for': 5
        }
    
    device360_port_configuration_pse_profile_drop_down_options = \
        {
            'CSS_SELECTOR': '.item-area li',
            'wait_for': 5
        }

    device360_wireframe_cpu_utilization_tooltip_content = \
        {
            'XPATH': '//*[contains(text(), "CPU Usage:")]',
            'wait_for': 5
        }

    device360_wireframe_cpu_utilization_piechart = \
        {
            'CSS_SELECTOR': '.highcharts-point.highcharts-color-0',
            'wait_for': 5
        }

    result_area = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cliPaneResutArea"]',
            'wait_for': 5
        }

    advanced_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-actions"]//li[@class="ui-menu-item ui-menu-item-pa"]//a',
            'wait_for': 5
        }

    actions_button = \
        {
            'XPATH': '//button[contains(text(),"Actions")]',
            'wait_for': 5
        }

    cli_command_line = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mainContent"]//input[@data-dojo-attach-point="cli"]',
            'wait_for': 5
        }

    device_rows = \
        {
            'XPATH': '//div[@class="dgrid-content ui-widget-content"]//tr',
            'wait_for': 5
        }

    row_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 5
        }

    cli_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-switch-cli-access"]',
            'wait_for': 5
        }

    cli_close_button = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialogTop"]',
            'wait_for': 5
        }

    cli_apply = \
        {
            'XPATH': '//button[@data-dojo-attach-point="apply"]',
            'wait_for': 5
        }

    device360_select_supplemental_cli = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipMark"]',
            'wait_for': 3
        }

    device360_supplemental_cli_list = \
        {
            'XPATH': '//*[@class="item-area"]//li',
            'wait_for': 3
        }

    device_360_supplemental_cli_new_profile = \
        {
            'XPATH': '//*[@data-type="supplemental-cli-profile"]',
            'wait_for': 3
        }

    device_360_supplemental_cli_profile_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 3
        }
    device_360_supplemental_cli_profile_commands = \
        {
            'XPATH': '//textarea[@data-dojo-attach-point="cli"]',
            'wait_for': 3
        }

    device360_supplemental_cli_save_profile = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buttonEl"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    device360_supplemental_cli_edit_profile = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 3
        }

    device360_thunderbold_icon = \
        {
            'XPATH': '//div[@data-dojo-attach-point="portCtn"]//div[@data-automation-tag="automation-entity-health-status-power"]',
            'wait_for': 5
        }

    device360_power_details = \
        {
            'XPATH': '//div[@data-dojo-attach-point="contentEl"]',
            'wait_for': 5
        }

    device360_pse_settings_for_device_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="showPSESettingsBtn"]',
            'wait_for': 5
        }

    device360_edit_threshold_poe = \
        {
            'XPATH': '//div[@class="field-container max-power-budget"]//input[@type="text"]',
            'wait_for': 5
        }

    device360_save_threshold_poe_value = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    device360_device_configuration_description = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    device360_device_configuration_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    device360_device_configuration_device_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceconfiguration"]//input[@data-dojo-attach-point="deviceModel"]',
            'wait_for': 5
        }

    device360_device_configuration_iq_engine = \
        {
            'XPATH': '//*[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    device360_device_configuration_override_acsp_network_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="overrideAcspLogging"]',
            'wait_for': 5
        }

    device360_device_configuration_production_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deploymentState-production"]',
            'wait_for': 5
        }

    device360_device_configuration_pre_provision_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deploymentState-preprovisioned"]',
            'wait_for': 5
        }

    device360_device_configuration_device_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTemplateStatic"]',
            'wait_for': 5
        }

    device360_configure_device_network_policy_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="networkPolicyArea"]//div/ul/li',
            'wait_for': 5
        }

    device360_configure_dhcp_ip_address_link = \
        {
            'XPATH': '//li[@data-automation-tag="automation-device-entity-ip-addressing-tab"]',
            'wait_for': 5
        }

    device360_configure_subnetworks_all_cells = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ipaddressing-area-subnet-list"]//div[@class="dgrid-content ui-widget-content"]//table/tr/td',
            'wait_for': 5
        }

    device360_configure_subnetworks_header = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ipaddressing-area-subnet-list"]//div/table/tr/th',
            'wait_for': 5
        }
    device360_click_particular_client = \
        {
            'XPATH': '//td[contains(@class,"field-clientMac")]//a[contains(@class,"open-client-entity")]',
            'wait_for': 5
        }
    close_client360_dialog = \
        {
            'XPATH': '//div[@class="entity-page-icon entity-page-close"][@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }
    device360_hyperlink_client = \
        {
            'XPATH': '//*[@class="entity-content-ctn device-entity-connected-ctn"]//table[@class="dgrid-row-table"]//*[@data-mac]',
            'wait_for': 5
        }
    device360_column_picker_scroll_bar = \
        {
            'XPATH': '//*[@class="dgrid-hider-menu"]',
            'wait_for': 5
        }

    device360_column_picker_icon = \
        {
            'XPATH': '//*[@class="ui-icon dgrid-hider-toggle"]',
            'wait_for': 5
        }

    d360_create_port_type = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'wait_for': 5
        }

    policy_edit_port_type = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-edit',
            'wait_for': 5
        }

    close_port_type_box = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-save"]',
            'wait_for': 5
        }
    #tab
    select_element_port_type_tab_usage = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-info"]',
            'wait_for': 5
        }

    select_element_port_type_tab_vlan = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-vlan"]',
            'wait_for': 5
        }

    select_element_port_type_tab_transmission = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-trans"]',
            'wait_for': 5
        }

    select_element_port_type_tab_stp = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-stp"]',
            'wait_for': 5
        }

    select_element_port_type_tab_storm_control = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-storm-control"]',
            'wait_for': 5
        }

    select_element_port_type_tab_pse_settings = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-pse"]',
            'wait_for': 5
        }

    select_element_port_type_tab_summary = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-summary"]',
            'wait_for': 5
        }

    defacutelrdp = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-name"]',
            'wait_for': 5
        }

    #page Name
    select_element_port_type_name = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-name"]',
            'wait_for': 5
        }

    select_element_port_type_description = \
        {
            'XPATH': '//textarea[@data-automation-tag="port-type-editor-description"]',
            'wait_for': 5
        }

    select_element_port_type_status = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-status"]',
            'wait_for': 5
        }

    select_element_port_type_auto_sense = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-auto-sense-status"]',
            'wait_for': 5
        }

    select_element_port_type_port_usage_access = \
        {
            'XPATH': '//input[@data-dojo-attach-point="accessType"]',
            'wait_for': 5
        }

    select_element_port_type_port_usage_trunk = \
        {
            'XPATH': '//input[@data-dojo-attach-point="trunkType"]',
            'wait_for': 5
        }

    # page Vlan
    select_element_port_type_next_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="wizardNext"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_name_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_add_vlan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanArea"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_id_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_select_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-vlan-select-btn"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_dropdown_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul/li',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_name_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_add_vlan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="nativeVlanArea"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_id_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="nativeVlanArea"]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_dropdown_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul//li',
            'wait_for': 5
        }

    select_element_port_type_save_vlan = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    select_element_port_type_allowed_vlans = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-allowed-vlans"]',
            'wait_for': 5
        }

    #Page Transmission
    select_element_port_type_transmission_type = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-duplex-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_type_dropdown_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-duplex-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_transmission_speed = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-speed-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_speed_dropdown_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-speed-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_cdp_receive = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-cdp"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_transmit = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-lldp-tx"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_receive = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-lldp-rx"]',
            'wait_for': 5
        }

    # page STP
    select_element_port_type_stp_enable= \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-stp-enable"]',
            'wait_for': 5
        }
    select_element_port_type_edge_port = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-stp-edge-port"]',
            'wait_for': 5
        }
    select_element_port_type_bpdu_protection = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-stp-bpdu-prot-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_bpdu_protection_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-stp-bpdu-prot-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_priority = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-stp-priority-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_priority_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-stp-priority-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_path_cost = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-stp-path-cost"]',
            'wait_for': 5
        }

    # page Storm
    select_element_port_type_broadcast = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-broadcast"]',
            'wait_for': 5
        }
    select_element_port_type_unknown_unicast = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-unicast"]',
            'wait_for': 5
        }
    select_element_port_type_multicast = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-multicast"]',
            'wait_for': 5
        }
    select_element_port_type_rate_limit_value = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-rate-limit-value"]',
            'wait_for': 5
        }
    #pag6 ELRP (ONLY FOR EXOS)
    select_element_port_type_elrp_status = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-elrp-enable"]',
            'wait_for': 5
        }

    # page PSE
    select_element_port_type_pse_profile = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-pse-profile"]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }
    select_element_port_type_pse_profile_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul//li',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_add = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-pse-profile"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_name = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_power_mode_items = \
        {
            'XPATH': '.J-ip-item',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_priority = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//div[contains(@class,"priority")]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_priority_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//div[contains(@class,"priority")]//ul[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_description = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//input[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    select_element_port_type_poe_status = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-pse-enable"]',
            'wait_for': 5
        }

    #Page summary
    select_element_port_type_name_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-name"]',
            'wait_for': 5
        }

    select_element_port_type_description_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-desc"]',
            'wait_for': 5
        }

    select_element_port_type_status_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-status"]',
            'wait_for': 5
        }

    select_element_port_type_port_usage_access_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-usage"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-vlan"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-native-vlan"]',
            'wait_for': 5
        }

    select_element_port_type_allowed_vlans_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-allowed-vlans"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_type_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-duplex"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_speed_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-speed"]',
            'wait_for': 5
        }

    select_element_port_type_cdp_receive_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_transmit_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-lldp-tx"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_receive_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-lldp-rx"]',
            'wait_for': 5
        }

    select_element_port_type_stp_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-status"]',
            'wait_for': 5
        }

    select_element_port_type_edge_port_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-edge-port"]',
            'wait_for': 5
        }

    select_element_port_type_bpdu_protection_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-bpdu-prot"]',
            'wait_for': 5
        }


    select_element_port_type_priority_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-priority"]',
            'wait_for': 5
        }

    select_element_port_type_path_cost_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-path-cost"]',
            'wait_for': 5
        }

    select_element_port_type_broadcast_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-broadcast"]',
            'wait_for': 5
        }

    select_element_port_type_unknown_unicast_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-unicast"]',
            'wait_for': 5
        }

    select_element_port_type_multicast_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-multicast"]',
            'wait_for': 5
        }

    select_element_port_type_rate_limit_type_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-rate-limit-type"]',
            'wait_for': 5
        }

    select_element_port_type_rate_limit_value_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-rate-limit-value"]',
            'wait_for': 5
        }


    select_element_port_type_elrp_status_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-elrp-enabled"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-pse-profile"]',
            'wait_for': 5
        }

    select_element_port_type_poe_status_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-pse-status"]',
            'wait_for': 5
        }

    device_d360_save_port_configuration = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-configuration-save-button"]',
            'wait_for': 5
        }

    device_d360_cancel_port_configuration = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }
        
    device360_configure_port_usage_drop_down_options_presence = \
        {
            'CSS_SELECTOR': '.chzn-single-with-drop',
            'wait_for': 5
        }

    device360_port_configuration_stack_units_dropdown = \
        {
            'XPATH': '//div[@class="stack-member-chooser"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    device360_port_configuration_stack_units_dropdown_parent_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="stackMemberChooserArea"]//ul[@data-automation-tag="automation-chzn-results-ctn"]',
            'index': 0,
            'wait_for': 5
        }

    device360_port_configuration_stack_units_rows = \
        {
            "CSS_SELECTOR": '.active-result',
            'wait_for': 5
        }

    policy_configure_port_rows = \
        {
            'XPATH': '//tabset[@data-dojo-attach-point="configuration-ports-tabs"]//portdetails//portentry-row',
            'wait_for': 5
        }

    device360_port_config_pse_tab_slot_stack = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-config-pse"]',
            'wait_for': 5
        }

    device360_pse_settings_for_device_button_stack = \
        {
            'XPATH': '//button[@data-dojo-attach-point="showPSESettingsBtn"]',
            'wait_for': 5
        }

    device360_edit_threshold_poe_stack = \
        {
            'XPATH': '//div[@class="field-container max-power-budget"]//input[@type="text"]',
            'wait_for': 5
        }

    device360_save_threshold_poe_value_stack = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    device360_configure_port_save_button_stack = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-config-save"]',
            'wait_for': 5
        }

    device360_stack_overview_slot_details_rows = \
        {
            'XPATH': '//*[@data-dojo-attach-point="switchStackPortsPanelContainer"]',
            'wait_for': 5
        }

    device360_thunderbold_icon_stack = \
        {
            'CSS_SELECTOR': '.power-supply',
            'wait_for': 5
        }

    select_element_port_type_macLock_status = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableMacLocking"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_max_first_arrival = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-maxfa"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_disable_port = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-shutdown"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_link_down_clear = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-clear"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_link_down_retain = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-retain"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_remove_aged_MACs = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-remove-aged"]',
            'wait_for': 5
        }

    select_mac_locking_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-enable"]'
        }

    select_mac_locking_first_arrival_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-max-fa-limit"]'
        }

    select_mac_locking_port_disable_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-disable-port"]'
        }

    select_mac_locking_link_down_action_clear_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-link-down-action"][@title="Clear"]'
        }

    select_mac_locking_link_down_action_retain_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-link-down-action"][@title="Retain"]'
        }

    select_mac_locking_remove_aged_macs_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-remove-aged-macs"]'
        }